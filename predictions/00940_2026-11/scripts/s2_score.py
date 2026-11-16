"""依 V1.3.0 規則重建 00940 指數名單（近似版）。

python s2_score.py <cutoff> <members csv> [--q YYYY-MM-DD 最近一季季底] [--no-growth]
輸出 out/score_<cutoff>.csv、out/pred_<cutoff>.csv

資訊時點：預設「截止日往前 4 個月」以前結束的季度才算已知（4/30 → 前一年 Q4；10/30 → Q2）。
做不到的規則：區域投資集中度（無資料，略過）、自由流通係數（略過）、
長期成長率（規則沒寫定義，用近四季營收對三年前同期的成長率代理）、下行風險用未還原收盤。
"""
import sys, pathlib, datetime as dt
import numpy as np
import polars as pl
from s1_universe import build, load_price, cap_factor

HERE = pathlib.Path(__file__).resolve().parent
DATA = HERE / "data"
RAW = pathlib.Path.home() / "quant/data/raw/finmind_daily"
N, IN_RANK, OUT_RANK, MAX_SWAP = 50, 35, 65, 10


def qend_back(q: dt.date, k: int) -> dt.date:
    """q 往前 k 季的季底。"""
    m = q.year * 12 + q.month - 1 - 3 * k
    y, mo = divmod(m, 12)
    nxt = dt.date(y + (mo == 11), (mo + 1) % 12 + 1, 1)
    return nxt - dt.timedelta(days=1)


def read(ds: str, sid: str) -> "pl.DataFrame | None":
    f = DATA / ds / f"{sid}.parquet"
    if not f.exists():
        return None
    d = pl.read_parquet(f)
    return d if d.height and "date" in d.columns else None


def series(d: pl.DataFrame, types: list[str]) -> dict[str, float]:
    for t in types:
        x = d.filter(pl.col("type") == t)
        if x.height:
            return dict(zip(x["date"], x["value"]))
    return {}


def ttm(s: dict[str, float], q: dt.date, cumulative: bool = False) -> float:
    """近四季合計。cumulative=True 表示資料是年初累計（現金流量表）。"""
    try:
        if not cumulative:
            return sum(s[qend_back(q, k).isoformat()] for k in range(4))
        if q.month == 12:
            return s[q.isoformat()]
        return s[q.isoformat()] + s[dt.date(q.year - 1, 12, 31).isoformat()] - s[dt.date(q.year - 1, q.month, q.day).isoformat()]
    except KeyError:
        return float("nan")


def period_end(label: str) -> "dt.date | None":
    import re
    m = re.match(r"(\d+)年(.*)", label)
    if not m:
        return None
    y, rest = int(m.group(1)) + 1911, m.group(2)
    if rest == "" or "後半" in rest or "第4季" in rest: return dt.date(y, 12, 31)
    if "前半" in rest or "第2季" in rest: return dt.date(y, 6, 30)
    if "第1季" in rest: return dt.date(y, 3, 31)
    if "第3季" in rest: return dt.date(y, 9, 30)
    return None


def dividend_feats(sid: str, known: dt.date, cutoff: str) -> dict:
    d = read("TaiwanStockDividend", sid)
    out = dict(div12=float("nan"), sdiv12=0.0, div3y=False, surplus5y=False)
    if d is None:
        return out
    # 現金股利換算成截止日的每股基礎：除息日（含）之後若有配股／面額變更就往下調
    rows = []
    for r in d.iter_rows(named=True):
        k = cap_factor(sid, r["CashExDividendTradingDate"], cutoff, inclusive=True) if r["CashExDividendTradingDate"] else 1.0
        rows.append((period_end(r["year"]), ((r["CashEarningsDistribution"] or 0) + (r["CashStatutorySurplus"] or 0)) / k, r["CashStatutorySurplus"] or 0,
                     (r["StockEarningsDistribution"] or 0) + (r["StockStatutorySurplus"] or 0)))
    rows = [r for r in rows if r[0] is not None and r[0] <= known]
    if not rows:
        return out
    last = max(r[0] for r in rows)
    out["div12"] = sum(c for e, c, _, _ in rows if dt.date(last.year - 1, last.month, last.day) < e <= last)
    out["sdiv12"] = sum(k for e, _, _, k in rows if dt.date(last.year - 1, last.month, last.day) < e <= last)
    fy = known.year if known.month == 12 else known.year - 1  # 最近一個完整會計年度
    by = {y: sum(c for e, c, _, _ in rows if e.year == y) for y in (fy, fy - 1, fy - 2)}
    out["div3y"] = all(v > 0 for v in by.values())
    out["surplus5y"] = any(s > 0 for e, _, s, _ in rows if e.year > fy - 5)
    return out


def feats(sid: str, q: dt.date, known: dt.date, cutoff: str) -> dict:
    o = dict(stock_id=sid, has_fs=False)
    fs, bs, cf = read("TaiwanStockFinancialStatements", sid), read("TaiwanStockBalanceSheet", sid), read("TaiwanStockCashFlowsStatement", sid)
    o.update(dividend_feats(sid, known, cutoff))
    if fs is None:
        return o
    o["has_fs"] = True
    eps, ni = series(fs, ["EPS"]), series(fs, ["EquityAttributableToOwnersOfParent", "IncomeAfterTaxes"])
    rev, gp = series(fs, ["Revenue"]), series(fs, ["GrossProfit"])
    o["eps4"], o["ni4"] = ttm(eps, q), ttm(ni, q)
    o["eps2"] = sum(eps.get(qend_back(q, k).isoformat(), float("nan")) for k in range(2))
    r4, r4p, g4, g4p = ttm(rev, q), ttm(rev, qend_back(q, 4)), ttm(gp, q), ttm(gp, qend_back(q, 4))
    o["gm_growth"] = g4 / r4 - g4p / r4p if gp and r4 and r4p else float("nan")
    r4_3y = ttm(rev, qend_back(q, 12))
    o["growth3y"] = r4 / r4_3y - 1 if r4_3y and r4_3y > 0 else float("nan")
    if bs is not None:
        k = q.isoformat()
        ta, li, eq = series(bs, ["TotalAssets"]).get(k), series(bs, ["Liabilities"]).get(k), series(bs, ["EquityAttributableToOwnersOfParent", "Equity"]).get(k)
        if ta and li is not None and eq:
            o["debt"], o["roa"], o["roe"] = li / ta, o["ni4"] / ta, o["ni4"] / eq
    if cf is not None:
        ocf = ttm(series(cf, ["CashFlowsFromOperatingActivities", "NetCashInflowFromOperatingActivities"]), q, True)
        capex = ttm(series(cf, ["PropertyAndPlantAndEquipment"]), q, True)
        o["fcf"] = ocf + (0.0 if np.isnan(capex) else capex)
    return o


def top(col: str, keep: float, high: bool, by: "str | None" = None) -> pl.Expr:
    """屬前 keep 高（或低）；缺值視為通過。"""
    r = pl.col(col).rank(descending=high) / pl.col(col).count()
    r = r.over(by) if by else r
    return (r <= keep) | pl.col(col).is_null() | pl.col(col).is_nan()


def zw(col: str) -> pl.Expr:
    x = pl.col(col)
    w = x.clip(x.quantile(0.025), x.quantile(0.975))
    return (w - w.mean()) / w.std()


def run(cutoff: str, members: list[str], q: "dt.date | None" = None, growth: bool = True, verbose: bool = True) -> pl.DataFrame:
    c = dt.date.fromisoformat(cutoff)
    m = c.year * 12 + c.month - 1 - 4
    known = dt.date(m // 12, m % 12 + 1, 28)
    known = (known.replace(day=1) + dt.timedelta(days=32)).replace(day=1) - dt.timedelta(days=1)  # 該月月底
    q = q or max(d for d in [qend_back(dt.date(known.year, 12, 31), k) for k in range(8)] if d <= known)
    u = build(cutoff, members)
    info = pl.read_parquet(next((RAW / "ai_screen/TaiwanStockInfo").glob("*.parquet"))).group_by("stock_id").agg(fin=pl.col("industry_category").str.contains("金融").any())
    u = u.join(info, on="stock_id", how="left").filter(pl.col("in_range"))
    f = pl.DataFrame([feats(s, q, known, cutoff) for s in u["stock_id"]], infer_schema_length=None)
    for col in ["eps4", "ni4", "eps2", "gm_growth", "growth3y", "debt", "roa", "roe", "fcf"]:
        if col not in f.columns:
            f = f.with_columns(pl.lit(None, dtype=pl.Float64).alias(col))
    u = u.join(f, on="stock_id")
    # 下行風險（252 日）
    px = load_price().filter(pl.col("date") <= cutoff).sort("stock_id", "date")
    px = px.with_columns(r=pl.col("close").pct_change().over("stock_id")).group_by("stock_id").tail(252)
    dr = px.group_by("stock_id").agg(downside=((pl.col("r").clip(upper_bound=0) ** 2).mean()).sqrt() * np.sqrt(252))
    u = u.join(dr, on="stock_id", how="left")
    u = u.with_columns(dy=pl.col("div12") / pl.col("close"), dyt=(pl.col("div12") + pl.col("sdiv12")) / pl.col("close"), ep=pl.col("ni4") / pl.col("mv"), ep2=pl.col("eps2") / pl.col("close"),
                       fcfy=pl.when(pl.col("fin")).then(None).otherwise(pl.col("fcf") / pl.col("mv")))
    # 少數公司損益表沒有母公司淨利欄位 → 退回 EPS/股價；NaN 一律轉 null，避免污染縮尾與標準化
    u = u.with_columns(ep=pl.when(pl.col("ep").is_nan() | pl.col("ep").is_null()).then(pl.col("eps4") / pl.col("close")).otherwise(pl.col("ep")))
    u = u.with_columns(pl.col("dy", "dyt", "ep", "ep2", "fcfy").fill_nan(None))
    base = pl.col("liq_ok") & ~pl.col("ky") & pl.col("has_fs")
    u = u.with_columns(base=base,
                       s_eps=pl.col("eps4") > 0,
                       s_div=pl.col("div3y") & ~(pl.col("fin") & pl.col("surplus5y")))
    b = u.filter(pl.col("base")).with_columns(
        s_debt=top("debt", 0.9, False, "fin"), s_roa=top("roa", 0.9, True, "fin"), s_roe=top("roe", 0.9, True, "fin"),
        s_ep2=top("ep2", 0.8, True), s_ni=top("ni4", 0.9, True), s_gm=top("gm_growth", 0.9, True), s_down=top("downside", 0.9, False))
    nm = b.filter(~pl.col("member")).with_columns(s_growth=top("growth3y", 0.75, True)).select("stock_id", "s_growth")
    b = b.join(nm, on="stock_id", how="left").with_columns(pl.col("s_growth").fill_null(True) if growth else pl.lit(True).alias("s_growth"))
    screens = ["s_eps", "s_div", "s_debt", "s_roa", "s_roe", "s_ep2", "s_ni", "s_gm", "s_growth", "s_down"]
    b = b.with_columns(passed=pl.all_horizontal(screens))
    p = b.filter(pl.col("passed")).with_columns(z_dy=zw("dy"), z_ep=zw("ep"), z_fcf=zw("fcfy"))
    p = p.with_columns(score=pl.mean_horizontal("z_dy", "z_ep", "z_fcf")).sort("score", descending=True).with_columns(rank=pl.int_range(1, pl.len() + 1))
    out = u.join(b.select("stock_id", *[s for s in screens if s not in ("s_eps", "s_div")], "passed"), on="stock_id", how="left").join(
        p.select("stock_id", "z_dy", "z_ep", "z_fcf", "score", "rank"), on="stock_id", how="left").with_columns(pl.col("passed").fill_null(False))

    # 緩衝區 + 至多換 10 檔
    pm = p.filter(pl.col("member")); pn = p.filter(~pl.col("member"))
    keep = pm.filter(pl.col("rank") <= OUT_RANK)["stock_id"].to_list()
    adds = pn.filter(pl.col("rank") <= IN_RANK)["stock_id"].to_list()
    fill = pn.filter((pl.col("rank") > IN_RANK))["stock_id"].to_list()
    adds = (adds + fill)[: max(len(adds), N - len(keep))] if len(keep) + len(adds) < N else adds
    if len(keep) + len(adds) > N:  # 自動納入太多 → 從排名最後的既有成分股擠出
        keep = keep[: N - len(adds)]
    if len(adds) > MAX_SWAP:
        keep = pm["stock_id"].to_list()[: N - MAX_SWAP]
        adds = pn["stock_id"].to_list()[: N - len(keep)]
    dels = [s for s in members if s not in keep]
    out = out.with_columns(pred=pl.when(pl.col("stock_id").is_in(adds)).then(pl.lit("add")).when(pl.col("stock_id").is_in(dels)).then(pl.lit("delete"))
                           .when(pl.col("member")).then(pl.lit("stay")).otherwise(pl.lit("")))
    if verbose:
        print(f"cutoff {cutoff} 最近一季 {q} 股利已知期別至 {known}｜範圍內 {u.height}、base {b.height}、通過篩選 {p.height}（成分股 {pm.height}）")
    return out


if __name__ == "__main__":
    cutoff, mem = sys.argv[1], sys.argv[2]
    q = dt.date.fromisoformat(sys.argv[sys.argv.index("--q") + 1]) if "--q" in sys.argv else None
    members = pl.read_csv(HERE / mem, schema_overrides={"stock_id": pl.Utf8})["stock_id"].to_list()
    out = run(cutoff, members, q, "--no-growth" not in sys.argv)
    out.sort("rank", nulls_last=True).write_csv(HERE / f"out/score_{cutoff}.csv")
    pl.Config.set_tbl_rows(60); pl.Config.set_tbl_cols(20); pl.Config.set_tbl_width_chars(200)
    cols = ["stock_id", "stock_name", "mv_rank", "passed", "rank", "score", "dy", "ep", "fcfy"]
    for k in ["add", "delete"]:
        print(k.upper()); print(out.filter(pl.col("pred") == k).sort("rank", nulls_last=True).select(cols))

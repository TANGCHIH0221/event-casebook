"""採樣範圍＋流動性檢驗。python s1_universe.py <cutoff YYYY-MM-DD> <members csv>
輸出 data/universe_<cutoff>.csv：市值排名、是否成分股、流動性是否通過。
市值 = 最近一季季底股數 × 截止日收盤（近似；TIP 用發行市值）。
"""
import sys, pathlib, datetime as dt
import polars as pl

HERE = pathlib.Path(__file__).resolve().parent
RAW = pathlib.Path.home() / "quant/data/raw/finmind_daily"


def load_price() -> pl.DataFrame:
    loc = pl.read_parquet(RAW / "price/year=202[456]/data.parquet").select("date", "stock_id", "Trading_Volume", "Trading_money", "close")
    loc = loc.with_columns(pl.col("date").cast(pl.Utf8).str.slice(0, 10))
    fs = list((HERE / "data/TaiwanStockPrice").glob("*.parquet"))
    new = pl.concat([pl.read_parquet(f).select("date", "stock_id", "Trading_Volume", "Trading_money", "close") for f in fs if pl.read_parquet_schema(f).get("date")], how="vertical_relaxed")
    new = new.filter(pl.col("date") > loc["date"].max())
    return pl.concat([loc, new.cast(loc.schema)]).unique(["date", "stock_id"])


_SPLIT = None


def cap_factor(sid: str, start: str, end: str, inclusive: bool = False) -> float:
    """start 之後（inclusive=True 含當日）到 end（含）之間，股數因配股／面額變更放大的倍數。"""
    global _SPLIT
    if _SPLIT is None:
        sp = pl.read_parquet(next((RAW / "ai_screen/TaiwanStockSplitPrice").glob("*.parquet")))
        _SPLIT = {}
        for r in sp.iter_rows(named=True):
            _SPLIT.setdefault(r["stock_id"], []).append((r["date"], r["before_price"] / r["after_price"]))
    ev = list(_SPLIT.get(sid, []))
    f = HERE / "data/TaiwanStockDividend" / f"{sid}.parquet"
    if f.exists():
        d = pl.read_parquet(f)
        if "StockExDividendTradingDate" in d.columns:
            for r in d.iter_rows(named=True):
                k = (r["StockEarningsDistribution"] or 0) + (r["StockStatutorySurplus"] or 0)
                if k > 0 and r["StockExDividendTradingDate"]:
                    ev.append((r["StockExDividendTradingDate"], 1 + k / 10))
    out = 1.0
    for d_, k in ev:
        if (start <= d_ if inclusive else start < d_) and d_ <= end:
            out *= k
    return out


def build(cutoff: str, members: list[str]) -> pl.DataFrame:
    px = load_price().filter(pl.col("date") <= cutoff)
    assert px["date"].max() == cutoff, (px["date"].max(), cutoff)
    info = pl.read_parquet(RAW / "ai_screen/TaiwanStockInfo/all.parquet" if (RAW / "ai_screen/TaiwanStockInfo/all.parquet").exists() else next((RAW / "ai_screen/TaiwanStockInfo").glob("*.parquet")))
    info = info.filter(pl.col("type").is_in(["twse", "tpex"])).group_by("stock_id").agg(pl.col("stock_name").last(), pl.col("industry_category").unique().alias("inds"))
    sh = pl.read_parquet(RAW / "shares_outstanding_quarter.parquet").with_columns(pl.col("snap_date").cast(pl.Utf8).str.slice(0, 10))
    sh = sh.filter(pl.col("snap_date") <= cutoff)
    snap = sh["snap_date"].max()
    sh = sh.filter(pl.col("snap_date") == snap).select("stock_id", "shares_outstanding")
    sh = sh.with_columns(shares_outstanding=pl.col("shares_outstanding") * pl.col("stock_id").map_elements(lambda x: cap_factor(x, snap, cutoff), return_dtype=pl.Float64))
    last = px.filter(pl.col("date") == cutoff).select("stock_id", "close")
    u = sh.join(last, on="stock_id").join(info, on="stock_id").filter(pl.col("stock_id").str.contains(r"^[1-9]\d{3}$"))
    u = u.with_columns(mv=pl.col("shares_outstanding") * pl.col("close"),
                       construction=pl.col("inds").list.contains("建材營造"),
                       ky=pl.col("stock_name").str.contains("KY"),
                       member=pl.col("stock_id").is_in(members))
    u = u.filter(~pl.col("construction")).sort("mv", descending=True).with_columns(mv_rank=pl.int_range(1, pl.len() + 1))

    # 流動性：月 = 日曆月
    c = dt.date.fromisoformat(cutoff)
    ym = lambda d: d.year * 12 + d.month - 1
    px = px.with_columns(ymi=pl.col("date").str.slice(0, 4).cast(pl.Int32) * 12 + pl.col("date").str.slice(5, 2).cast(pl.Int32) - 1)
    px = px.filter(pl.col("stock_id").str.contains(r"^[1-9]\d{3}$") & (pl.col("ymi") > ym(c) - 12) & (pl.col("ymi") <= ym(c)))
    m = px.group_by("stock_id", "ymi").agg(val=pl.col("Trading_money").sum(), vol=pl.col("Trading_Volume").sum(), adv=pl.col("Trading_money").mean())
    m = m.join(sh, on="stock_id").with_columns(turn=pl.col("vol") / pl.col("shares_outstanding"))
    y = m.group_by("stock_id").agg(val12=pl.col("val").sum(), n_turn=(pl.col("turn") >= 0.03).sum(), n_adv=(pl.col("adv") >= 1e8).sum(),
                                   val1=pl.col("val").filter(pl.col("ymi") == ym(c)).sum())
    y = y.with_columns(pct1=pl.col("val1").rank(descending=True) / pl.len(), pct12=pl.col("val12").rank(descending=True) / pl.len())
    y = y.with_columns(liq=(pl.col("pct1") <= 0.70) & ((pl.col("pct12") <= 0.20) | (pl.col("n_turn") >= 8) | (pl.col("n_adv") >= 8)))
    u = u.join(y.select("stock_id", "pct1", "pct12", "n_turn", "n_adv", "liq"), on="stock_id", how="left").with_columns(pl.col("liq").fill_null(False))
    # 市值 10% 緩衝：成分股前 330、非成分股前 270
    u = u.with_columns(in_range=pl.when(pl.col("member")).then(pl.col("mv_rank") <= 330).otherwise(pl.col("mv_rank") <= 270),
                       liq_ok=pl.col("member") | pl.col("liq"))
    return u.drop("inds")


if __name__ == "__main__":
    cutoff, mem = sys.argv[1], sys.argv[2]
    members = pl.read_csv(HERE / mem, schema_overrides={"stock_id": pl.Utf8})["stock_id"].to_list()
    u = build(cutoff, members)
    u.write_csv(HERE / f"data/universe_{cutoff}.csv")
    print(u.filter(pl.col("mv_rank") <= 330).select(n=pl.len(), ky=pl.col("ky").sum(), liq=pl.col("liq").sum(), member=pl.col("member").sum()))
    print("members outside top330:", u.filter(pl.col("member") & (pl.col("mv_rank") > 330)).select("stock_id", "stock_name", "mv_rank"))
    print("members missing:", set(members) - set(u["stock_id"].to_list()))

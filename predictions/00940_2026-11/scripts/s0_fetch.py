"""抓 00940 名單重建需要的 FinMind 資料（Free：每小時 600 次，逐檔抓、快取 parquet、可續跑）。

用法：python s0_fetch.py price | fund
  price：候選股（6/30 股數 × 9/16 收盤的市值前 450 檔＋現有成分股）2026-09-17 起日 K
  fund ：data/fund_list.csv 內股票的損益表、資產負債表、現金流量表、股利
"""
import sys, time, pathlib, requests
import polars as pl

HERE = pathlib.Path(__file__).resolve().parent
DATA = HERE / "data"
RAW = pathlib.Path.home() / "quant/data/raw/finmind_daily"
TOKEN = next(l.split("=", 1)[1].strip().strip('"') for l in (pathlib.Path.home() / "quant/.env").read_text().splitlines() if l.startswith("FINMIND_TOKEN="))


def fetch(dataset: str, sid: str, start: str) -> None:
    f = DATA / dataset / f"{sid}.parquet"
    if f.exists():
        return
    f.parent.mkdir(parents=True, exist_ok=True)
    while True:
        try:
            r = requests.get("https://api.finmindtrade.com/api/v4/data", params=dict(dataset=dataset, data_id=sid, start_date=start),
                             headers={"Authorization": f"Bearer {TOKEN}"}, timeout=60)
        except requests.RequestException as e:
            print("net err", e, flush=True); time.sleep(30); continue
        if r.status_code == 402:
            print(time.strftime("%H:%M"), "quota hit, sleep 5 min", flush=True); time.sleep(300); continue
        if r.status_code != 200:
            print(dataset, sid, r.status_code, r.text[:200], flush=True); time.sleep(20); continue
        break
    rows = r.json().get("data", [])
    df = pl.DataFrame(rows, infer_schema_length=None) if rows else pl.DataFrame({"stock_id": []}, schema={"stock_id": pl.Utf8})
    df.write_parquet(f)
    time.sleep(0.3)


def candidates() -> list[str]:
    sh = pl.read_parquet(RAW / "shares_outstanding_quarter.parquet").filter(pl.col("snap_date") == pl.col("snap_date").max())
    px = pl.read_parquet(RAW / "price/year=2026/data.parquet")
    px = px.filter(pl.col("date") == px["date"].max()).select("stock_id", "close")
    mv = sh.join(px, on="stock_id").with_columns(mv=pl.col("shares_outstanding") * pl.col("close"))
    mv = mv.filter(pl.col("stock_id").str.contains(r"^[1-9]\d{3}$")).sort("mv", descending=True).head(450)
    mem = pl.read_csv(HERE / "members_20261113.csv", schema_overrides={"stock_id": pl.Utf8})["stock_id"].to_list()
    return sorted(set(mv["stock_id"].to_list()) | set(mem))


if __name__ == "__main__":
    mode = sys.argv[1]
    if mode == "price":
        ids = candidates()
        for i, s in enumerate(ids):
            fetch("TaiwanStockPrice", s, "2026-09-01")
            if i % 50 == 0: print("price", i, len(ids), flush=True)
    else:
        ids = pl.read_csv(DATA / "fund_list.csv", schema_overrides={"stock_id": pl.Utf8})["stock_id"].to_list()
        for i, s in enumerate(ids):
            fetch("TaiwanStockFinancialStatements", s, "2022-01-01")
            fetch("TaiwanStockBalanceSheet", s, "2023-01-01")
            fetch("TaiwanStockCashFlowsStatement", s, "2023-01-01")
            fetch("TaiwanStockDividend", s, "2020-01-01")
            if i % 25 == 0: print("fund", i, len(ids), flush=True)
    print("DONE", mode, flush=True)

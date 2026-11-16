"""FinMind 小工具：讀 ~/quant/.env 的 FINMIND_TOKEN，抓資料並快取到 data/。"""
import os, pathlib, requests, pandas as pd

ROOT = pathlib.Path(__file__).resolve().parents[1]
CACHE = ROOT / "data"

def _token():
    tok = os.environ.get("FINMIND_TOKEN")
    if tok:
        return tok
    env = pathlib.Path.home() / "quant/.env"
    for line in env.read_text().splitlines():
        if line.startswith("FINMIND_TOKEN="):
            return line.split("=", 1)[1].strip().strip('"')
    raise RuntimeError("FINMIND_TOKEN not found")

def get(dataset, data_id, start, end):
    f = CACHE / f"{dataset}_{data_id}_{start}_{end}.csv"
    if f.exists():
        return pd.read_csv(f, dtype={"stock_id": str})
    r = requests.get("https://api.finmindtrade.com/api/v4/data",
                     params=dict(dataset=dataset, data_id=data_id, start_date=start, end_date=end),
                     headers={"Authorization": f"Bearer {_token()}"}, timeout=60)
    r.raise_for_status()
    df = pd.DataFrame(r.json()["data"])
    CACHE.mkdir(exist_ok=True)
    df.to_csv(f, index=False)
    return df

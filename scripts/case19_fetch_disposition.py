"""抓證交所＋櫃買 2026 年處置公告，整理成 4 碼普通股的處置期間表。"""
import json, pathlib, re, time, requests, pandas as pd
ROOT = pathlib.Path(__file__).resolve().parents[1]
RAW = ROOT / "data/raw"; RAW.mkdir(parents=True, exist_ok=True)
UA = {"User-Agent": "Mozilla/5.0"}

def roc(s):  # '115/08/24' -> Timestamp
    y, m, d = s.strip().split("/"); return pd.Timestamp(int(y) + 1911, int(m), int(d))

def twse(a, b):
    f = RAW / f"twse_punish_{a}_{b}.json"
    if not f.exists():
        r = requests.get("https://www.twse.com.tw/rwd/zh/announcement/punish", params=dict(startDate=a, endDate=b, response="json"), headers=UA, timeout=60)
        f.write_text(r.text); time.sleep(3)
    d = json.loads(f.read_text())
    out = []
    for r in d.get("data", []):
        s, e = r[6].split("～")
        out.append(dict(market="TWSE", announce=roc(r[1]), stock_id=r[2].strip(), name=r[3].strip(), measure=r[7].strip(),
                        start=roc(s), end=roc(e), every2min="二分鐘" in r[8]))
    return out

def tpex(a, b):
    f = RAW / f"tpex_punish_{a.replace('/', '')}_{b.replace('/', '')}.json"
    if not f.exists():
        r = requests.get("https://www.tpex.org.tw/www/zh-tw/bulletin/disposal", params=dict(startDate=a, endDate=b, response="json"), headers=UA, timeout=60)
        f.write_text(r.text); time.sleep(3)
    d = json.loads(f.read_text())
    out = []
    for r in d["tables"][0]["data"]:
        if not r[2]: continue
        s, e = re.split("[~～]", r[5])
        out.append(dict(market="TPEx", announce=roc(r[1]), stock_id=str(r[2]).strip(), name=re.sub("<.*?>", "", r[3]).strip(),
                        measure=r[7].strip(), start=roc(s), end=roc(e), every2min="二分鐘" in r[8]))
    return out

rows = []
for a, b in [("20260101", "20260430"), ("20260501", "20260809"), ("20260810", "20261113")]:
    rows += twse(a, b)
    rows += tpex(f"{a[:4]}/{a[4:6]}/{a[6:]}", f"{b[:4]}/{b[4:6]}/{b[6:]}")
df = pd.DataFrame(rows).drop_duplicates(["stock_id", "start", "end"])
df = df[df.stock_id.str.fullmatch(r"\d{4}")]
df.to_csv(ROOT / "data/case19_disposition_2026.csv", index=False)
print(len(df), df.market.value_counts().to_dict())
print(df.groupby(df.start >= "2026-08-10").every2min.mean())
print(df.sample(5, random_state=1).to_string(index=False))

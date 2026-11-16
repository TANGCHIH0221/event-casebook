"""案例 19：2026-08-10 處置新制前後，處置股在處置期間與出關後的走勢。
舊制 = 2026 年內、處置迄日早於 2026-08-10 的處置；新制 = 起日 ≥ 2026-08-10。跨新舊制的交替案例排除。
報酬 = 個股收盤報酬 − 加權指數報酬（簡單超額），從 D1（處置第一天）收盤起算。
"""
import sys, glob, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent))
import finmind as fm, pandas as pd, numpy as np, matplotlib.pyplot as plt
from matplotlib import font_manager
font_manager.fontManager.addfont("/System/Library/Fonts/STHeiti Medium.ttc")
plt.rcParams.update({"font.family": "Heiti TC", "axes.unicode_minus": False,
                     "axes.spines.top": False, "axes.spines.right": False})
ROOT = pathlib.Path(__file__).resolve().parents[1]
INK, INK2, BLUE, ORANGE = "#0b0b0b", "#52514e", "#2a78d6", "#eb6834"
POST = 10

ev = pd.read_csv(ROOT / "data/case19_disposition_2026.csv", parse_dates=["start", "end"], dtype={"stock_id": str})
ev["regime"] = np.where(ev.start >= "2026-08-10", "new", np.where(ev.end < "2026-08-10", "old", "mixed"))
ev = ev[ev.regime != "mixed"]

loc = pd.concat(pd.read_parquet(f) for f in glob.glob(str(pathlib.Path.home() / "quant/data/raw/finmind_daily/price/year=202[56]/*.parquet")))
loc["date"] = pd.to_datetime(loc.date)
close = loc.pivot_table(index="date", columns="stock_id", values="close")
new_ids = sorted(ev[ev.regime == "new"].stock_id.unique())
extra = {}
for s in new_ids:
    d = fm.get("TaiwanStockPrice", s, "2026-07-01", "2026-11-13")
    if len(d):
        extra[s] = d.set_index(pd.to_datetime(d.date)).close
ext = pd.DataFrame(extra)
close = close.combine_first(ext) if len(ext) else close
close.update(ext)
tx = fm.get("TaiwanStockPrice", "TAIEX", "2025-01-01", "2026-11-13").set_index("date").close
tx.index = pd.to_datetime(tx.index)
close = close.reindex(tx.index).replace(0, np.nan)  # 停牌日資料有 0 價，當缺值
ret = close.pct_change(fill_method=None).sub(tx.pct_change(), axis=0).replace([np.inf, -np.inf], np.nan)

rows, paths = [], {"old": [], "new": []}
for _, r in ev.iterrows():
    if r.stock_id not in ret: continue
    idx = tx.index
    i1 = idx.searchsorted(r.start); ie = idx.searchsorted(r.end, side="right") - 1
    if i1 >= len(idx) or ie < i1 or ie + POST >= len(idx): continue
    rr = ret[r.stock_id].iloc[i1 + 1: ie + POST + 1]          # D1 收盤之後的日報酬
    if rr.isna().mean() > 0.2: continue
    rr = rr.fillna(0)
    n = ie - i1
    cum = np.concatenate([[0], np.cumsum(rr.values)]) * 1e4  # bp，日報酬加總
    rows.append(dict(regime=r.regime, stock_id=r.stock_id, measure=r.measure, start=r.start.date(), n_days=n + 1,
                     d1_de=cum[n], last2_de=cum[n] - cum[max(0, n - 2)], de_post5=cum[n + 5] - cum[n], de_post10=cum[n + POST] - cum[n]))
    paths[r.regime].append(pd.Series(cum - cum[n], index=range(-n, POST + 1)))
res = pd.DataFrame(rows)
res.to_csv(ROOT / "data/case19_results.csv", index=False)

def ci(x):
    m = x.mean(); se = x.std(ddof=1) / np.sqrt(len(x)); return f"{m:6.0f} [{m-1.96*se:5.0f},{m+1.96*se:5.0f}] 中位 {x.median():5.0f} 勝率 {(x>0).mean():.0%}"
for g, x in res.groupby("regime"):
    print(f"{g}: n={len(x)} 處置天數中位 {x.n_days.median():.0f}")
    for c in ["d1_de", "last2_de", "de_post5", "de_post10"]:
        print(f"   {c:9s} {ci(x[c])}")

fig, ax = plt.subplots(figsize=(9, 4.4))
for g, col, lab in [("old", ORANGE, "舊制（10 個營業日）"), ("new", BLUE, "新制（5 個營業日）")]:
    P = pd.concat(paths[g], axis=1)
    m = P.mean(axis=1).dropna(); cnt = P.notna().sum(axis=1); m = m[cnt >= 0.5 * P.shape[1]]
    ax.plot(m.index, m.values, color=col, lw=2, label=f"{lab}，n = {P.shape[1]}")
    ax.annotate(f"{m.iloc[-1]:+.0f}", (m.index[-1], m.iloc[-1]), xytext=(4, 0), textcoords="offset points", fontsize=9, color=INK)
ax.axvline(0, color=INK2, lw=0.8, ls="--"); ax.axhline(0, color=INK2, lw=0.8)
ax.text(0.2, ax.get_ylim()[0] * 0.95, "DE = 處置最後一天", fontsize=8, color=INK2)
ax.set_xticks(range(-9, POST + 1))
ax.set_xlabel("相對 DE 的交易日", fontsize=9, color=INK2)
ax.set_title("處置股相對加權指數的累積超額報酬（bp），以 DE 收盤 = 0", loc="left", fontsize=11, color=INK)
ax.legend(frameon=False, fontsize=9, loc="lower right")
ax.grid(axis="y", color="#e4e3df", lw=0.6); ax.tick_params(colors=INK2, labelsize=9)
fig.text(0.01, 0.01, "2026 年上市櫃 4 碼股票處置事件。資料：證交所、櫃買中心處置公告；FinMind 日 K。日報酬加總，未扣成本。", fontsize=8, color=INK2)
fig.tight_layout(rect=(0, 0.04, 1, 1))
fig.savefig(ROOT / "figures/case19_disposition_reform.png", dpi=160)

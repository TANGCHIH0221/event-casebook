"""案例 18：國安基金歷次進場後的加權指數表現。
t0 = 第一個進場日的前一個交易日收盤（≈ 委員會決議公告日；決議都在收盤後或前一晚）。
對照組：加權指數比前 60 日高點低 13% 以上的所有交易日（排除國安基金進場後 90 天內）。
"""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent))
import finmind as fm, pandas as pd, numpy as np, matplotlib.pyplot as plt
from matplotlib import font_manager
font_manager.fontManager.addfont("/System/Library/Fonts/STHeiti Medium.ttc")
plt.rcParams.update({"font.family": "Heiti TC", "axes.unicode_minus": False,
                     "axes.spines.top": False, "axes.spines.right": False})
ROOT = pathlib.Path(__file__).resolve().parents[1]
INK, INK2, BLUE = "#0b0b0b", "#52514e", "#2a78d6"

ENTRIES = {"2000-03": "2000-03-16", "2000-10": "2000-10-03", "2004-05": "2004-05-20", "2008-09": "2008-09-19",
           "2011-12": "2011-12-20", "2015-08": "2015-08-25", "2020-03": "2020-03-19", "2022-07": "2022-07-13",
           "2025-04": "2025-04-09"}
H = [5, 20, 60]
tx = fm.get("TaiwanStockPrice", "TAIEX", "2000-01-01", "2026-11-13").set_index("date").close
tx.index = pd.to_datetime(tx.index)
fwd = {k: (tx.shift(-k) / tx - 1) * 100 for k in H}
dd = (tx / tx.rolling(61, min_periods=20).max() - 1) * 100

t0 = {k: tx.index[tx.index.searchsorted(pd.Timestamp(v)) - 1] for k, v in ENTRIES.items()}
rows = [dict(episode=k, t0=t.date(), drawdown_60d=round(dd[t], 1), **{f"r{h}d": round(fwd[h][t], 1) for h in H}) for k, t in t0.items()]
ev = pd.DataFrame(rows)
mask = pd.Series(False, index=tx.index)
for t in t0.values():
    mask.loc[t:t + pd.Timedelta(days=90)] = True
ctrl = (dd <= -13) & ~mask
ctrl_mean = {h: fwd[h][ctrl].mean() for h in H}
ctrl_win = {h: (fwd[h][ctrl] > 0).mean() for h in H}
ev.to_csv(ROOT / "data/case18_events.csv", index=False)
print(ev.to_string(index=False))
for h in H:
    x = ev[f"r{h}d"]
    print(f"{h}d: 國安 mean {x.mean():.1f} median {x.median():.1f} win {(x>0).mean():.2f} t {x.mean()/(x.std(ddof=1)/np.sqrt(len(x))):.1f} | 對照 mean {ctrl_mean[h]:.1f} win {ctrl_win[h]:.2f} n {ctrl.sum()}")

fig, axes = plt.subplots(1, 3, figsize=(10, 4), sharey=True)
for ax, h in zip(axes, H):
    x = ev[f"r{h}d"].values
    ax.axhline(0, color=INK2, lw=0.8)
    ax.axhline(ctrl_mean[h], color=INK2, lw=1.2, ls="--")
    ax.scatter(range(len(x)), x, s=36, color=BLUE, zorder=3, edgecolor="white", linewidth=1)
    ax.set_xticks(range(len(x))); ax.set_xticklabels(ev.episode, rotation=60, fontsize=8, color=INK2)
    ax.set_title(f"進場後 {h} 個交易日（%）", loc="left", fontsize=10, color=INK)
    ax.text(len(x) - 0.5, ctrl_mean[h], f"對照 {ctrl_mean[h]:+.1f}", fontsize=8, color=INK2, va="bottom", ha="right")
    ax.grid(axis="y", color="#e4e3df", lw=0.6); ax.tick_params(colors=INK2, labelsize=9)
fig.suptitle("國安基金歷次進場後的加權指數報酬（藍點 = 每次進場；虛線 = 同樣深跌但沒有國安基金的日子平均）",
             x=0.01, ha="left", fontsize=10.5, color=INK)
fig.text(0.01, 0.01, "進場 = 第一個進場日前一交易日收盤買進。對照組 = 加權指數比前 60 日高點低 13% 以上的日子。資料：FinMind。", fontsize=8, color=INK2)
fig.tight_layout(rect=(0, 0.04, 1, 0.94))
fig.savefig(ROOT / "figures/case18_stabilization_fund.png", dpi=160)

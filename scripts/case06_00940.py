"""案例 6：00940 建倉。
圖 A：全市場投信每日淨買超（億元），2024-03 ~ 04。
圖 B：前十大成分股等權 vs 加權指數的累積超額報酬，以募集結束日 3/15 歸零。
表：每檔建倉期投信淨買、佔成交量比重、各區間超額報酬。
"""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent))
import finmind as fm, pandas as pd, matplotlib.pyplot as plt, matplotlib.dates as mdates

ROOT = pathlib.Path(__file__).resolve().parents[1]
from matplotlib import font_manager
font_manager.fontManager.addfont("/System/Library/Fonts/STHeiti Medium.ttc")
plt.rcParams.update({"font.family": "Heiti TC", "axes.unicode_minus": False,
                     "axes.spines.top": False, "axes.spines.right": False})
INK, INK2, BLUE, ORANGE, SHADE = "#0b0b0b", "#52514e", "#2a78d6", "#eb6834", "#f0efec"

TOP10 = {"2603": "長榮", "2303": "聯電", "5483": "中美晶", "3005": "神基", "2404": "漢唐",
         "2385": "群光", "6176": "瑞儀", "2454": "聯發科", "3293": "鈊象", "6121": "新普"}
S, E = "2024-02-15", "2024-06-28"
BUILD = ("2024-03-18", "2024-03-29")

px = {i: fm.get("TaiwanStockPrice", i, S, E).set_index("date") for i in [*TOP10, "TAIEX"]}
close = pd.DataFrame({i: d.close for i, d in px.items()})
close.index = pd.to_datetime(close.index)
ret = close.pct_change()
excess = ret[list(TOP10)].mean(axis=1) - ret["TAIEX"]
cum = (1 + excess).cumprod()
cum = (cum / cum.loc["2024-03-15"] - 1) * 100

tot = fm.get("TaiwanStockTotalInstitutionalInvestors", "", "2024-03-01", "2024-04-30")
it = tot[tot.name == "Investment_Trust"].assign(net=lambda d: (d.buy - d.sell) / 1e8)
it["date"] = pd.to_datetime(it.date)

# ---- 表 ----
def ex(i, a, b):
    c, t = close[i], close["TAIEX"]
    return ((c[b] / c[a]) - (t[b] / t[a])) * 100
rows = []
for i, name in TOP10.items():
    f = fm.get("TaiwanStockInstitutionalInvestorsBuySell", i, S, E)
    f = f[f.name == "Investment_Trust"].set_index("date").loc[BUILD[0]:BUILD[1]]
    net = (f.buy - f.sell).sum() / 1000
    vol = px[i].Trading_Volume.loc[BUILD[0]:BUILD[1]].sum() / 1000
    rows.append(dict(代號=i, 名稱=name, 投信淨買_張=round(net), 佔成交量=f"{net/vol:.0%}",
                     募集前=ex(i, "2024-02-15", "2024-03-08"), 募集期=ex(i, "2024-03-08", "2024-03-15"), 建倉期=ex(i, "2024-03-15", "2024-03-29"),
                     掛牌後1月=ex(i, "2024-03-29", "2024-04-30"), 掛牌後3月=ex(i, "2024-03-29", "2024-06-28")))
tab = pd.DataFrame(rows).round(1)
tab.to_csv(ROOT / "data/case06_table.csv", index=False)
print(tab.to_string(index=False))
print(tab[["募集前", "募集期", "建倉期", "掛牌後1月", "掛牌後3月"]].mean().round(1).to_dict())
print("build-window IT net (億):", it.set_index("date").loc[BUILD[0]:BUILD[1]].net.sum().round(0))

# ---- 圖 ----
fig, (a, b) = plt.subplots(2, 1, figsize=(9, 6.6), gridspec_kw={"height_ratios": [1, 1.2]})
for ax in (a, b):
    ax.axvspan(pd.Timestamp("2024-03-11"), pd.Timestamp("2024-03-15"), color=SHADE, zorder=0)
    ax.axvspan(pd.Timestamp(BUILD[0]), pd.Timestamp(BUILD[1]), color="#cde2fb", zorder=0)
    ax.grid(axis="y", color="#e4e3df", lw=0.6); ax.tick_params(colors=INK2, labelsize=9)
    ax.xaxis.set_major_formatter(mdates.DateFormatter("%m/%d"))

a.bar(it.date, it.net, width=0.7, color=BLUE)
a.set_title("A. 全市場投信每日淨買超（億元）", loc="left", fontsize=11, color=INK)
pk = it.loc[it.net.idxmax()]
a.annotate(f"3/29 {pk.net:.0f} 億", (pk.date, pk.net), xytext=(8, -4), textcoords="offset points", fontsize=9, color=INK)
a.text(pd.Timestamp("2024-03-13"), it.net.max() * 0.92, "募集", ha="center", fontsize=9, color=INK2)
a.text(pd.Timestamp("2024-03-23"), it.net.max() * 0.92, "建倉", ha="center", fontsize=9, color=INK2)

b.plot(cum.index, cum.values, color=ORANGE, lw=2)
b.axhline(0, color=INK2, lw=0.8)
b.axvline(pd.Timestamp("2024-04-01"), color=INK2, lw=0.8, ls="--")
b.text(pd.Timestamp("2024-04-02"), cum.max() * 0.9, "4/1 掛牌", fontsize=9, color=INK2)
b.annotate(f"{cum.iloc[-1]:.1f}%", (cum.index[-1], cum.iloc[-1]), xytext=(4, 0), textcoords="offset points", fontsize=9, color=INK)
b.set_title("B. 前十大成分股（等權）減加權指數的累積超額報酬，3/15 = 0（%）", loc="left", fontsize=11, color=INK)
fig.text(0.01, 0.005, "資料：FinMind（證交所／櫃買）。成分股為 00940 掛牌前公布的前十大持股。", fontsize=8, color=INK2)
fig.tight_layout(rect=(0, 0.02, 1, 1))
fig.savefig(ROOT / "figures/case06_00940.png", dpi=160)

"""案例 10、11：航運三雄（2021）與緯創（2023）處置期間的股價。
報酬口徑與使用者處置研究一致：D1（處置第一天）收盤 → DE（處置最後一天）收盤。
"""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent))
import finmind as fm, pandas as pd, matplotlib.pyplot as plt, matplotlib.dates as mdates
from matplotlib import font_manager
font_manager.fontManager.addfont("/System/Library/Fonts/STHeiti Medium.ttc")
plt.rcParams.update({"font.family": "Heiti TC", "axes.unicode_minus": False,
                     "axes.spines.top": False, "axes.spines.right": False})
ROOT = pathlib.Path(__file__).resolve().parents[1]
INK, INK2 = "#0b0b0b", "#52514e"
COL = {"2603": "#2a78d6", "2609": "#eb6834", "2615": "#1baf7a", "3231": "#2a78d6"}
NAME = {"2603": "長榮", "2609": "陽明", "2615": "萬海", "3231": "緯創"}
DISP = pathlib.Path.home() / "quant/data/raw/finmind_daily/disposition_securities.parquet"

d = pd.read_parquet(DISP)
d = d[d.stock_id.isin(list(NAME))]
d = d[(d.period_start.astype(str) >= "2021-01-01") & (d.period_start.astype(str) <= "2023-12-31")]
px = {"2603": ("2020-06-01", "2022-07-29"), "2609": ("2020-06-01", "2022-07-29"),
      "2615": ("2020-06-01", "2022-07-29"), "3231": ("2022-12-01", "2023-10-31")}
close = {}
for s, (a, b) in px.items():
    c = fm.get("TaiwanStockPrice", s, a, b).set_index("date").close
    c.index = pd.to_datetime(c.index)
    # 自行還原除權息：除權息日之前的價格乘上（參考價 ÷ 前一日收盤）
    ex = fm.get("TaiwanStockDividendResult", s, a, b)
    for _, e in ex.iterrows():
        c[c.index < pd.Timestamp(e.date)] *= e.after_price / e.before_price
    close[s] = c

rows = []
for _, r in d.sort_values("period_start").iterrows():
    c = close[r.stock_id]
    d1 = c.index[c.index.searchsorted(pd.Timestamp(r.period_start))]
    de = c.index[c.index.searchsorted(pd.Timestamp(r.period_end), side="right") - 1]
    i_de = c.index.get_loc(de)
    pre6 = c.index[max(c.index.get_loc(d1), i_de - 6)]
    post20 = c.index[min(i_de + 20, len(c) - 1)]
    rows.append(dict(stock=f"{r.stock_id} {NAME[r.stock_id]}", measure=r.measure, d1=d1.date(), de=de.date(),
                     d1_to_de=round((c[de] / c[d1] - 1) * 100, 1), last6_to_de=round((c[de] / c[pre6] - 1) * 100, 1),
                     de_to_20d=round((c[post20] / c[de] - 1) * 100, 1)))
tab = pd.DataFrame(rows)
tab.to_csv(ROOT / "data/case10_11_disposition.csv", index=False)
print(tab.to_string(index=False))

fig, (a, b) = plt.subplots(2, 1, figsize=(9, 7))
for s in ["2603", "2609", "2615"]:
    c = close[s]["2020-10-01":"2022-07-29"]
    a.plot(c.index, c / c.iloc[0] * 100, color=COL[s], lw=1.5, label=NAME[s])
for _, r in d[d.stock_id.isin(["2603", "2609", "2615"])].iterrows():
    a.axvspan(pd.Timestamp(r.period_start), pd.Timestamp(r.period_end), color=COL[r.stock_id], alpha=0.12, lw=0)
a.axvline(pd.Timestamp("2021-10-04"), color=INK2, lw=0.8, ls="--")
a.text(pd.Timestamp("2021-10-08"), a.get_ylim()[1] * 0.92, "10/4 三雄同步跌停", fontsize=8, color=INK2)
a.set_title("A. 航運三雄還原股價（2020-10-01 = 100），色塊 = 各自的處置期間", loc="left", fontsize=11, color=INK)
a.legend(frameon=False, fontsize=9, loc="upper left")
c = close["3231"]
b.plot(c.index, c, color=COL["3231"], lw=1.5)
for _, r in d[d.stock_id == "3231"].iterrows():
    b.axvspan(pd.Timestamp(r.period_start), pd.Timestamp(r.period_end), color=COL["3231"], alpha=0.15, lw=0)
    b.text(pd.Timestamp(r.period_start), c.max() * 1.02, "處置", fontsize=8, color=INK2)
b.set_title("B. 緯創還原收盤價（元），色塊 = 處置期間", loc="left", fontsize=11, color=INK)
for ax in (a, b):
    ax.grid(axis="y", color="#e4e3df", lw=0.6); ax.tick_params(colors=INK2, labelsize=9)
    ax.xaxis.set_major_formatter(mdates.DateFormatter("%Y-%m"))
fig.text(0.01, 0.005, "資料：FinMind 日 K，以除權息結果自行還原、證交所處置公告。", fontsize=8, color=INK2)
fig.tight_layout(rect=(0, 0.02, 1, 1))
fig.savefig(ROOT / "figures/case10_11_disposition.png", dpi=160)

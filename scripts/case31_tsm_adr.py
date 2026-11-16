"""案例 31：台積電 ADR 溢價。
溢價 = TSM 收盤（美元）÷（5 × 2330 收盤 ÷ 美元兌台幣即期中價）− 1。
同一日曆日對齊：台股 13:30 收盤早於美股收盤，兩者相差約半天，日頻比較可接受。
"""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent))
import finmind as fm, pandas as pd, matplotlib.pyplot as plt, matplotlib.dates as mdates
from matplotlib import font_manager
font_manager.fontManager.addfont("/System/Library/Fonts/STHeiti Medium.ttc")
plt.rcParams.update({"font.family": "Heiti TC", "axes.unicode_minus": False,
                     "axes.spines.top": False, "axes.spines.right": False})
ROOT = pathlib.Path(__file__).resolve().parents[1]
INK, INK2, BLUE = "#0b0b0b", "#52514e", "#2a78d6"
S, E = "2022-01-01", "2026-11-13"

tsm = fm.get("USStockPrice", "TSM", S, E).set_index("date").Close
tw = fm.get("TaiwanStockPrice", "2330", S, E).set_index("date").close
fx = fm.get("TaiwanExchangeRate", "USD", S, E).set_index("date")
fx = ((fx.spot_buy + fx.spot_sell) / 2).replace(0, float("nan"))
df = pd.concat({"tsm": tsm, "tw": tw, "fx": fx}, axis=1).dropna()
df.index = pd.to_datetime(df.index)
df["prem"] = (df.tsm / (5 * df.tw / df.fx) - 1) * 100
df.to_csv(ROOT / "data/case31_premium.csv")

m = df.prem.resample("ME").mean()
print("yearly mean:", df.prem.groupby(df.index.year).mean().round(1).to_dict())
print("max:", df.prem.idxmax().date(), round(df.prem.max(), 1), " min:", df.prem.idxmin().date(), round(df.prem.min(), 1))
print("2022Q4 mean:", round(df.prem["2022-10":"2022-12"].mean(), 1))
print("2024-01~03 max:", round(df.prem["2024-01":"2024-03"].max(), 1))
print("2025-12 mean:", round(df.prem["2025-12"].mean(), 1), " 2026-05 mean:", round(df.prem["2026-05"].mean(), 1))
print("last 6 months:", m.tail(7).round(1).to_dict())

fig, ax = plt.subplots(figsize=(9, 4.2))
ax.plot(df.index, df.prem, color=BLUE, lw=1.2)
ax.plot(m.index - pd.offsets.MonthBegin(1) + pd.Timedelta(days=14), m.values, color=INK, lw=1.6, alpha=0.6)
ax.axhline(0, color=INK2, lw=0.8)
ax.axvline(pd.Timestamp("2026-04-24"), color=INK2, lw=0.8, ls="--")
ax.text(pd.Timestamp("2026-04-28"), df.prem.max() * 0.95, "4/24 主動 ETF 單一個股\n上限 10%→25%", fontsize=8, color=INK2, va="top")
ax.annotate(f"{df.prem.iloc[-1]:.1f}%", (df.index[-1], df.prem.iloc[-1]), xytext=(4, 0), textcoords="offset points", fontsize=9, color=INK)
ax.set_title("台積電 ADR 相對台股的溢價（%）：藍 = 每日，深色 = 月平均", loc="left", fontsize=11, color=INK)
ax.grid(axis="y", color="#e4e3df", lw=0.6); ax.tick_params(colors=INK2, labelsize=9)
ax.xaxis.set_major_formatter(mdates.DateFormatter("%Y-%m"))
fig.text(0.01, 0.01, "溢價 = TSM ÷ (5 × 2330 ÷ USD/TWD) − 1。資料：FinMind（美股日 K、台股日 K、台銀即期匯率中價）。", fontsize=8, color=INK2)
fig.tight_layout(rect=(0, 0.04, 1, 1))
fig.savefig(ROOT / "figures/case31_tsm_adr.png", dpi=160)

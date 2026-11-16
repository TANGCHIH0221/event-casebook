"""三次審核：把預測放寬成候選名單時，實際納入／刪除的涵蓋率。先跑 evalspec.py 產生 out/diag_*.csv。"""
import polars as pl


def z(col: str) -> pl.Expr:
    x = pl.col(col)
    w = x.clip(x.quantile(0.025), x.quantile(0.975))
    return (w - w.mean()) / w.std()


for cutoff in ["2025-04-30", "2025-10-31", "2026-04-30"]:
    b = pl.read_csv(f"out/diag_{cutoff}.csv", schema_overrides={"stock_id": pl.Utf8}).with_columns(sc=pl.mean_horizontal(z("dy"), z("ep"), z("fcfy")))
    n = b.filter(~pl.col("member"))
    g = n.with_columns(gp=pl.col("growth3y").rank(descending=True) / pl.col("growth3y").count())
    var = {
        "none": n.sort("sc", descending=True),
        "passed": n.filter(pl.col("passed")).sort("sc", descending=True),
        "growth75": g.filter((pl.col("gp") <= 0.75) | pl.col("gp").is_null()).sort("sc", descending=True),
        "growth50": g.filter((pl.col("gp") <= 0.5) | pl.col("gp").is_null()).sort("sc", descending=True),
    }
    print(cutoff, "non-members", n.height, "adds", n["isA"].sum())
    for k, v in var.items():
        print(f"  add {k:9s} pool {v.height:3d} adds in pool {int(v['isA'].sum()):2d} | top10 {int(v.head(10)['isA'].sum())} top20 {int(v.head(20)['isA'].sum())} top30 {int(v.head(30)['isA'].sum())} top40 {int(v.head(40)['isA'].sum())}")
    m = b.filter(pl.col("member")).sort("sc")
    print(f"  del in table {int(m['isD'].sum())} | bottom5 {int(m.head(5)['isD'].sum())} bottom8 {int(m.head(8)['isD'].sum())} bottom10 {int(m.head(10)['isD'].sum())} bottom15 {int(m.head(15)['isD'].sum())}; members failing pct screens: {int((~m['passed']).sum())}, of which deleted {int(m.filter(~pl.col('passed'))['isD'].sum())}")

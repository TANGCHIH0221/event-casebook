"""三次審核比較分數定義。指標：刪除＝成分股分數墊底 k 檔命中數（k=實際在表內的刪除數）；納入＝非成分股前 10 命中數與實際納入的平均排名百分位。"""
import polars as pl, numpy as np
import s2_score as s
S = [("2025-04-30", "members_before_202505.csv", "2025-05"), ("2025-10-31", "members_before_202511.csv", "2025-11"), ("2026-04-30", "members_before_202605.csv", "2026-05")]
ch = pl.read_csv("../data/changes_00940.csv", schema_overrides={"stock_id": pl.Utf8})
tabs = {}
for cutoff, mem, rev in S:
    members = pl.read_csv(mem, schema_overrides={"stock_id": pl.Utf8})["stock_id"].to_list()
    o = s.run(cutoff, members, growth=False, verbose=False)
    c = ch.filter(pl.col("review").str.starts_with(rev))
    A = c.filter(pl.col("action") == "add")["stock_id"].to_list(); D = c.filter(pl.col("action") == "delete")["stock_id"].to_list()
    b = o.filter(pl.col("base") & pl.col("s_eps") & pl.col("s_div")).with_columns(isA=pl.col("stock_id").is_in(A), isD=pl.col("stock_id").is_in(D))
    print(rev, "adds in table", b["isA"].sum(), "/", len(A), " dels in table", b["isD"].sum(), "/", len(D), " adds lost:", [x for x in A if x not in b["stock_id"].to_list()])
    tabs[rev] = b
    b.write_csv(f"out/diag_{cutoff}.csv")

def z(col, lo=0.025, hi=0.975):
    x = pl.col(col); w = x.clip(x.quantile(lo), x.quantile(hi)); return (w - w.mean()) / w.std()

SPECS = {
    "mean(dy,ep,fcf)": pl.mean_horizontal(z("dy"), z("ep"), z("fcfy")),
    "mean(dyt,ep,fcf)": pl.mean_horizontal(z("dyt"), z("ep"), z("fcfy")),
    "sum, fin fcf=0": z("dy") + z("ep") + z("fcfy").fill_null(0),
    "sum dyt, fin fcf=0": z("dyt") + z("ep") + z("fcfy").fill_null(0),
    "dy only": z("dy"), "dyt only": z("dyt"), "ep only": z("ep"), "fcf only (fin=0)": z("fcfy").fill_null(0),
    "dy+fcf": pl.mean_horizontal(z("dy"), z("fcfy")), "dyt+fcf": pl.mean_horizontal(z("dyt"), z("fcfy")),
    "ep+fcf": pl.mean_horizontal(z("ep"), z("fcfy")),
    "mean pass-only std": None,
}
print(f"{'spec':22s}" + "".join(f"| {r} del  add10 addPct " for _, _, r in S))
for name, e in SPECS.items():
    line = f"{name:22s}"
    for _, _, rev in S:
        b = tabs[rev]
        if e is None:
            b = b.filter(pl.col("passed") | pl.col("isA") | pl.col("isD") | pl.col("member")); ee = SPECS["mean(dy,ep,fcf)"]
        else: ee = e
        b = b.with_columns(sc=ee)
        m = b.filter(pl.col("member")).sort("sc"); k = int(m["isD"].sum())
        n = b.filter(~pl.col("member")).sort("sc", descending=True).with_columns(r=pl.int_range(1, pl.len() + 1))
        pct = (n.filter(pl.col("isA"))["r"] / n.height).mean()
        line += f"|   {int(m.head(k)['isD'].sum())}/{k}      {int(n.head(10)['isA'].sum())}/{int(n['isA'].sum())}    {pct:.2f}   "
    print(line)

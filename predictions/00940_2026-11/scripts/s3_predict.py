"""定案版預測：硬性條件 + 綜合分數排序（不套百分位篩選，三次回測顯示那些篩選我重建不準）。

python s3_predict.py <cutoff> <members csv> [review prefix 用來對答案]
硬性條件：市值範圍（成分股前 330、非成分股前 270）、非建材營造、非 KY、
          近四季 EPS 合計 > 0、近三年度皆有現金股利、非成分股須過流動性檢驗。
分數：自由現金流量收益率、現金股利率、益本比各自 2.5%/97.5% 縮尾後標準化取平均（金融業不計自由現金流）。
刪除：不符硬性條件的成分股 + 分數最低者，補到 10 檔。納入：非成分股分數最高 10 檔。
輸出 out/pred_<cutoff>.csv（含全部排名，方便事後對照）。
"""
import sys
import polars as pl
import s2_score as s

MAX_SWAP = 10


def predict(cutoff: str, members: list[str]) -> pl.DataFrame:
    o = s.run(cutoff, members, growth=False, verbose=False)
    ok = pl.col("base") & pl.col("s_eps") & pl.col("s_div")
    b = o.filter(ok).with_columns(sc=pl.mean_horizontal(s.zw("dy"), s.zw("ep"), s.zw("fcfy")))
    o = o.join(b.select("stock_id", "sc"), on="stock_id", how="left")
    # 成分股：硬性不符者排最前（必刪），其餘依分數由低到高
    in_tab = set(o["stock_id"].to_list())
    gone = [m for m in members if m not in in_tab]  # 掉出市值範圍或被排除產業
    mem = o.filter(pl.col("member")).with_columns(hard_fail=pl.col("sc").is_null()).sort(["hard_fail", "sc"], descending=[True, False])
    mem = mem.with_columns(del_rank=pl.int_range(1, pl.len() + 1) + len(gone))
    non = o.filter(~pl.col("member") & pl.col("sc").is_not_null())
    if cutoff >= "2026-04-16":  # V1.3.0 起：非既有成分股長期成長率須屬前 75%（代理：近四季營收對三年前同期成長率）
        non = non.with_columns(gp=pl.col("growth3y").rank(descending=True) / pl.col("growth3y").count()).filter((pl.col("gp") <= 0.75) | pl.col("gp").is_null())
    non = non.sort("sc", descending=True).with_columns(add_rank=pl.int_range(1, pl.len() + 1))
    out = pl.concat([mem, non], how="diagonal")
    out = out.with_columns(pred=pl.when(pl.col("del_rank") <= MAX_SWAP).then(pl.lit("delete")).when(pl.col("add_rank") <= MAX_SWAP).then(pl.lit("add")).otherwise(pl.lit("")))
    if gone:
        print("成分股不在採樣範圍（必刪）:", gone)
    return out.select("stock_id", "stock_name", "member", "pred", "del_rank", "add_rank", "sc", "mv_rank", "close", "dy", "ep", "fcfy", "eps4", "div12", "growth3y", "hard_fail", "fin")


if __name__ == "__main__":
    cutoff, mem = sys.argv[1], sys.argv[2]
    members = pl.read_csv(mem, schema_overrides={"stock_id": pl.Utf8})["stock_id"].to_list()
    out = predict(cutoff, members)
    out.write_csv(f"out/pred_{cutoff}.csv")
    pl.Config.set_tbl_rows(60); pl.Config.set_tbl_cols(20); pl.Config.set_tbl_width_chars(220)
    show = ["stock_id", "stock_name", "sc", "mv_rank", "close", "dy", "ep", "fcfy", "hard_fail"]
    if len(sys.argv) > 3:
        c = pl.read_csv("../data/changes_00940.csv", schema_overrides={"stock_id": pl.Utf8}).filter(pl.col("review").str.starts_with(sys.argv[3]))
        A = c.filter(pl.col("action") == "add")["stock_id"].to_list(); D = c.filter(pl.col("action") == "delete")["stock_id"].to_list()
        out = out.with_columns(actual=pl.when(pl.col("stock_id").is_in(A)).then(pl.lit("ADD")).when(pl.col("stock_id").is_in(D)).then(pl.lit("DEL")).otherwise(pl.lit("")))
        show = ["actual"] + show
        d, a = out.filter(pl.col("del_rank").is_not_null()), out.filter(pl.col("add_rank").is_not_null())
        missing_d = [x for x in D if x not in out["stock_id"].to_list()]
        print(f"{sys.argv[3]} 刪除：前10命中 {d.filter((pl.col('del_rank') <= 10) & (pl.col('actual') == 'DEL')).height + len(missing_d)}/10（其中不在範圍 {len(missing_d)}），前15涵蓋 {d.filter((pl.col('del_rank') <= 15) & (pl.col('actual') == 'DEL')).height + len(missing_d)}")
        print(f"{sys.argv[3]} 納入：前10命中 {a.filter((pl.col('add_rank') <= 10) & (pl.col('actual') == 'ADD')).height}/10，前20 {a.filter((pl.col('add_rank') <= 20) & (pl.col('actual') == 'ADD')).height}，前30 {a.filter((pl.col('add_rank') <= 30) & (pl.col('actual') == 'ADD')).height}，前40 {a.filter((pl.col('add_rank') <= 40) & (pl.col('actual') == 'ADD')).height}")
    else:
        print("DELETE 排序前 15"); print(out.filter(pl.col("del_rank") <= 15).select("del_rank", *show).with_columns(pl.col(pl.Float64).round(3)))
        print("ADD 排序前 30"); print(out.filter(pl.col("add_rank") <= 30).select("add_rank", *show).with_columns(pl.col(pl.Float64).round(3)))

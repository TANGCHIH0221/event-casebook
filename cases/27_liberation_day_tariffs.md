# 案例 27：美國「解放日」對等關稅（2025-04）

> **一句話**：關稅公告讓美股兩天跌 10.5%，但讓川普在一週內暫停的是美債：10 年期殖利率在股市大跌時不降反升。台股因為清明連假休市兩天，把全球兩天的跌幅在 04-07 一次吸收，指數跌 9.7%、台積電開盤即鎖跌停。

| 項目 | 內容 |
|---|---|
| 接縫 | (1) 政策由行政命令一夜改變，市場只能用價格回應，而政策制定者又看價格（尤其是債市）調整政策；(2) 台股休市制度與全球交易時間不同步，連假期間的資訊在開盤第一天集中釋放，又被 10% 漲跌幅限制卡住 |
| 強制流來源 | 槓桿部位去化：美債市場的 swap spread 交易被迫平倉（見第 2 節）；台股則是融資追繳與跌停鎖死後隔日的延續賣壓 |
| 量級 | S&P 500 兩日 −10.5%；10 年期美債殖利率一週 +47 bp（收盤口徑）；台股 04-07 跌 2,065.87 點 |
| 不看價格的一方 | 被迫平倉的槓桿部位（融資戶、swap spread 交易者） |
| 天然對手方 | 有資金在政策轉向時接手的人：國安基金（2025-04-08 授權）、空手的長線資金 |
| 規則風險 | 極高：政策可以在盤中一則社群貼文就反轉（04-09） |
| 查證狀態 | ✅ 指數與殖利率對 FRED／FinMind；⚠️ 盤中殖利率高低點、「基差交易瓦解」說法未證實或與官方研究矛盾（見第 5 節） |

---

## 1. 發生了什麼

| 日期 | 事件 | 來源 |
|---|---|---|
| 2025-04-02（三） | 美股收盤後宣布對等關稅；S&P 500 當日收 5,670.97 | [FRED SP500](https://fred.stlouisfed.org/series/SP500) |
| 2025-04-03 | S&P 500 −4.84%（收 5,396.52）、Nasdaq −5.97%；台股清明連假休市 | [FRED SP500](https://fred.stlouisfed.org/series/SP500)、[FRED NASDAQCOM](https://fred.stlouisfed.org/series/NASDAQCOM) |
| 2025-04-04 | S&P 500 −5.97%（收 5,074.08）、Nasdaq −5.82%；10 年期美債殖利率收 4.01% | 同上；[FRED DGS10](https://fred.stlouisfed.org/series/DGS10) |
| 2025-04-06（日） | 金管會宣布 04-07～04-11 暫時措施：盤中借券賣出上限由 30% 降到 3%、融券保證金成數由 90% 提高到 130%、可用其他擔保品補繳 | [今周刊](https://www.businesstoday.com.tw/article/category/183008/post/202504070039/) |
| 2025-04-07（一） | 加權指數跌 2,065.87 點、−9.70%，收 19,232.35；台積電開盤即鎖跌停（848 元）、鴻海、大立光跌停；證交所公告上市跌停 936 檔 | FinMind；[證交所每日市場成交資訊](https://www.twse.com.tw/zh/trading/historical/fmtqik.html)；[今周刊](https://www.businesstoday.com.tw/article/category/183008/post/202504070039/) |
| 2025-04-08 | 加權 −4.02%；國安基金臨時會授權進場，上限 5,000 億元；美股 S&P 500 再跌 1.57%，四日累計 −12.1% | FinMind；[數位時代](https://www.bnext.com.tw/article/82861/black-monday-2025)；[FRED SP500](https://fred.stlouisfed.org/series/SP500) |
| 2025-04-09 | 美國盤中宣布 90 天暫停（中國除外，對中關稅提高到 125%）。S&P 500 +9.5%（2008-10 以來最大單日漲幅）、Nasdaq +12.2%。台股當天收盤時尚未宣布：加權 −5.79%，台積電 −3.8%，鴻海跌停 | [PBS（AP）](https://www.pbs.org/newshour/economy/u-s-stocks-shoot-to-historic-gains-after-trump-pauses-most-of-his-tariffs)；[CNN](https://edition-prod-cf.sitemirror.cnn.com/2025/04/09/business/trump-stocks-bond-market-nightcap/index.html)；FinMind |
| 2025-04-10 | 加權 +9.25%（+1,608 點），台積電漲停 | FinMind |
| 2025-04-11 | 10 年期美債殖利率收 4.48%，比 04-04 高 47 bp；30 年期 04-10 收 4.86% | [FRED DGS10](https://fred.stlouisfed.org/series/DGS10)、[FRED DGS30](https://fred.stlouisfed.org/series/DGS30) |

## 2. 機制

正常的避險模式下，股市大跌時資金會買美債，殖利率下降。04-04 確實如此（10 年期 4.01%），但 04-07 到 04-11 殖利率反而一路上升，股債同跌。紐約聯準會 SOMA 負責人 Perli 在 2025-05-09 演講中認為，swap spread 交易被迫平倉加劇了這段流動性壓力（[NY Fed](https://www.newyorkfed.org/newsevents/speeches/2025/per250509)）；達拉斯聯準會 2025-07-15 的研究則指出，期現貨基差交易（basis trade）部位在 04 月「明顯穩定」，基差幾乎沒有受影響（[Dallas Fed](https://www.dallasfed.org/research/economics/2025/0715)）。紐約聯準會後續文章也提到另一種解釋：外國投資人持有美債的意願下降（[Liberty Street Economics](https://libertystreeteconomics.newyorkfed.org/2026/04/treasury-market-liquidity-since-april-2025/)）。川普在宣布暫停時說他一直在看債市，「人們有點緊張」（[PBS（AP）](https://www.pbs.org/newshour/economy/u-s-stocks-shoot-to-historic-gains-after-trump-pauses-most-of-his-tariffs)）。台股這邊是制度層的放大：清明連假讓台股錯過 04-03、04-04 兩天，04-07 開盤要一次反映美股兩日 −10.5%，但個股漲跌幅上限 10%，大量股票開盤即鎖死、沒有成交，賣壓順延到 04-08、04-09。

## 3. 關鍵數字

| 指標 | 數值 | 來源 |
|---|---|---|
| S&P 500 兩日跌幅（04-02 → 04-04） | −10.5% | [FRED SP500](https://fred.stlouisfed.org/series/SP500) 自行計算 |
| S&P 500 四日跌幅（04-02 → 04-08） | −12.1%；Nasdaq −13.3% | [FRED](https://fred.stlouisfed.org/series/SP500) 自行計算 |
| S&P 500 暫停日漲幅（04-09） | +9.5% | [FRED SP500](https://fred.stlouisfed.org/series/SP500)；[PBS（AP）](https://www.pbs.org/newshour/economy/u-s-stocks-shoot-to-historic-gains-after-trump-pauses-most-of-his-tariffs) |
| 10 年期美債殖利率（收盤） | 04-04 4.01% → 04-11 4.48%（+47 bp） | [FRED DGS10](https://fred.stlouisfed.org/series/DGS10) |
| 30 年期美債殖利率（收盤） | 04-04 4.41% → 04-10 4.86%（+45 bp） | [FRED DGS30](https://fred.stlouisfed.org/series/DGS30) |
| 加權指數 04-07 | −2,065.87 點、−9.70%，收 19,232.35；史上最大收盤跌點 | FinMind；[Yahoo（中央社）](https://tw.stock.yahoo.com/news/%E5%8F%B0%E8%82%A1%E7%84%A1%E9%87%8F%E9%87%8D%E6%8C%AB2065%E9%BB%9E-%E6%B3%95%E4%BA%BA-%E6%AD%A2%E8%B7%8C%E5%85%88%E7%9C%8B4%E5%A4%A7%E8%A8%8A%E8%99%9F-094210289.html) |
| 加權指數三日累計（04-02 → 04-09） | 21,298.22 → 17,391.76，−18.3% | FinMind 自行計算 |
| 04-07 上市跌停檔數 | 936 檔（證交所晚間公告，隔日起禁止平盤下放空） | [今周刊](https://www.businesstoday.com.tw/article/category/183008/post/202504070039/) |
| 國安基金可動用上限 | 5,000 億元（第 9 次進場） | [數位時代](https://www.bnext.com.tw/article/82861/black-monday-2025) |

## 4. 我的解讀（草稿，待討論）

1. **政策制定者的反應函數看的是債市，不是股市。** 股市跌 12% 沒讓政策轉向，10 年期殖利率在股災中反向上升才讓政策轉向。對 prop desk 而言，「股跌債也跌」是政策可能轉向的領先訊號，比股價本身更值得盯。
2. **休市 + 漲跌幅限制 = 價格發現被切成好幾段，而且可以預測。** 04-07 台積電整天鎖在跌停、成交量極低，真正的成交與價格發現延到 04-08、04-09；而 04-09 美國宣布暫停時台股已收盤，反彈又延到 04-10 才一次反映（+9.25%）。凡是「台股休市、海外開市」的重大事件，都可以預先推算台股會在哪一天、以什麼幅度補缺口。
3. **監管反應有固定順序，可以事前排進行事曆。** 週日金管會限空 → 週一跌停家數公告、隔日禁平盤下放空 → 週二國安基金授權。這是一套已知的反應函數：第一天是制度限制賣方，第二天才是買方進場。
4. **「基差交易瓦解」是當時媒體的敘事，事後官方研究不支持。** 寫事件案例時，事發當週的解釋要等事後資料驗證；本案事後的主流解釋是 swap spread 平倉與外資減持，不是 basis trade。

## 5. 限制與未證實

- 原手冊寫「4/2（週三）盤後宣布（S&P 500 約 5,633）」：5,633.07 是 04-01 收盤；04-02 收盤是 5,670.97（FRED）。
- 原手冊寫「10 年殖利率 4/7 低點 3.87% → 4/9 盤中高點 4.47%」「4/11 破 4.5%」：這些是盤中數字，本文只用 FRED 收盤口徑（04-04 4.01% → 04-11 4.48%）。盤中高低點沒有找到一手來源，未採用。
- 原手冊寫「Fortune 指槓桿美債基差交易瓦解是逼川普暫停的關鍵」：達拉斯聯準會研究認為 basis trade 部位在 04 月穩定，紐約聯準會 Perli 指向 swap spread 交易。此說法刪除。
- 原手冊寫「川普約 13:18 發文」「中國升至 145%」：發文確切時間未找到一手來源；04-09 宣布的對中稅率是 125%（AP），145% 是之後與既有 20% 關稅合計的數字，口徑不同。
- 原手冊寫「創紀錄 945 檔跌停」：證交所公告的上市跌停是 936 檔；另有報導盤中上市櫃合計曾達 1,860 家。945 檔查無來源。
- 原手冊寫「當時史上最大單日百分比跌幅」：中央社的說法是「史上最大收盤跌點」；另有媒體寫「1990 年以來最大單日跌幅」。百分比排名本文未確認。
- 原手冊的 Dow 點數（−1,679、−2,231 點）與「市值蒸發 5.06 兆美元」本次未查證，未採用。

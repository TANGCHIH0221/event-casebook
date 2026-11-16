# 案例 01：Jane Street 印度 Bank Nifty 到期日案（2023-01 ～ 2025-05，監管程序進行中）

> **一句話**：印度指數選擇權用現貨收盤價結算，而選擇權名目是現貨的數百倍；SEBI 認定 Jane Street 用「單獨看會虧」的現貨與期貨推動到期日指數，讓大很多倍的選擇權部位獲利。這是初步認定（prima facie），上訴仍未判決。

| 項目 | 內容 |
|---|---|
| 接縫 | 選擇權以現貨收盤價結算（合理）＋ 選擇權名目遠大於現貨、Bank Nifty 只有 12 檔且高度集中（各自是市場自然長出來的）→ 推現貨便宜，選擇權賠率大 |
| 強制流來源 | 不是有人被迫交易，是**結算機制被迫**：到期日所有指數選擇權都依當日收盤結算價現金結算，不看結算價是怎麼來的 |
| 量級 | 檢查期間淨利 ₹36,502 crore；SEBI 認定 18 天不法所得 ₹4,843.57 crore（見第 3 節） |
| 不看價格的一方 | 到期日持有選擇權的人（大多是散戶），部位依結算價自動了結 |
| 天然對手方 | 印度散戶選擇權交易者：FY22–FY24 有 93% 虧錢 |
| 規則風險 | 已發生：SEBI 減少週到期、加盤中部位監控、限制指數集中度；2026-08 起收盤價改用收盤集合競價 |
| 查證狀態 | ✅ 金額與時間線已對 SEBI 命令摘要與兩個以上媒體；⚠️ 全部是 SEBI 臨時命令的初步認定，非終局判決 |

---

## 1. 發生了什麼

| 日期 | 事件 | 來源 |
|---|---|---|
| 2024-04 | Jane Street 在紐約告 Millennium 與兩名前交易員竊取交易策略；開庭時律師不慎說出策略與印度選擇權有關，法官提到 Jane Street 稱該策略前一年賺約 US$1B | [Bloomberg](https://www.bloomberg.com/news/articles/2024-04-19/jane-street-s-secret-strategy-concerns-india-hearing-reveals)；[Business Today](https://www.businesstoday.in/markets/global-markets/story/a-wall-street-giant-is-taking-rival-to-court-for-stealing-trading-secrets-involving-india-426268-2024-04-21) |
| 2024-12 | Jane Street 與 Millennium 和解，條件未公開 | [Bloomberg](https://www.bloomberg.com/news/articles/2024-12-05/jane-street-millennium-settle-india-options-trade-secrets-case) |
| 2025-02 | NSE 依 SEBI 指示發函警告 Jane Street；Jane Street 於 2025-02-06、02-21 回覆 | [Legal500（命令摘要）](https://www.legal500.com/intelligence/india/corporate-commercial-law/sebi-update-interim-order-against-jane-street-group-for-alleged-index-manipulation) |
| 2025-04-30 | NSE 自行結案 | [CA Alley](https://www.caalley.com/news-updates/indian-news/how-sebi-s-crackdown-on-jane-street-unfolded-a-15-month-trail-of-scrutiny-and-ignored-warnings) |
| 2025-05-15 | Nifty 到期日 13:00–14:00 大買成分股與期貨推高指數，SEBI 認定是警告後再犯 | [Legal500](https://www.legal500.com/intelligence/india/corporate-commercial-law/sebi-update-interim-order-against-jane-street-group-for-alleged-index-manipulation) |
| 2025-07-03 | SEBI 發布單方面臨時命令（ex-parte interim order），禁止 Jane Street 四家實體進入印度市場，扣押 ₹4,843.57 crore | [SEBI](https://www.sebi.gov.in/enforcement/orders/jul-2025/interim-order-in-the-matter-of-index-manipulation-by-jane-street-group_95040.html)；[SCC Online](https://www.scconline.com/blog/post/2025/07/09/sebi-restrains-jane-street-group-from-accessing-securities-market/) |
| 2025-07-14 | Jane Street 把 ₹4,843.57 crore 存入以 SEBI 為受益的託管帳戶（escrow） | [Outlook Business](https://www.outlookbusiness.com/corporate/sebi-lifts-trading-ban-on-jane-street-after-4843-cr-escrow-deposit) |
| 2025-07-21 | SEBI 解除交易禁令，調查繼續 | [The Week / PTI](https://www.theweek.in/wire-updates/business/2025/07/21/del102-biz-ld-jane-street-sebi.html) |
| 2025-09 | Jane Street 向證券上訴法庭（Securities Appellate Tribunal, SAT）上訴，主張 SEBI 不給完整調查資料（含 SEBI 監視部門報告與 NSE 往來文件） | [Business Standard](https://www.business-standard.com/markets/news/jane-street-files-appeal-in-sat-alleging-sebi-bias-in-probe-125090301189_1.html) |
| 2026-02-25 | SAT 延期開庭 | [Business Today](https://www.businesstoday.in/markets/story/jane-street-vs-sebi-sat-adjourns-hearing-in-market-manipulation-case-517925-2026-02-25) |
| 2026-10-21 | SAT 就「調閱 SEBI 文件」的請求保留裁定（reserved order），擇日宣判；SEBI 稱已交出超過 10GB 資料，指這是拖延戰術。截至 2026-11-16 未查到宣判 | [Business Standard](https://www.business-standard.com/markets/news/jane-street-appeal-sat-reserves-order-on-plea-for-additional-sebi-records-126102100972_1.html)；[Kalkine](https://www.kalkine.co.in/article/news/sat-reserves-order-in-jane-street-case-over-access-to-sebi-documents) |
| 2026-08-13 | 另案：JPMorgan 旗下 Copthall Mauritius 與 Mansi 券商在 BSE Sensex 週到期日的收盤集合競價大量掛單後撤單，SEBI 於 2026-08-19 發臨時命令 | [Outlook Money](https://www.outlookmoney.com/invest/sensex-closing-auction-manipulation-explained-sebi-interim-order-jpmorgan-entity-mansi-stock-broking-cas-august-13)；[Business Today](https://www.businesstoday.in/markets/story/sebi-flags-prima-facie-manipulation-in-sensex-closing-auction-session-blocks-two-entities-550200-2026-08-19) |

## 2. 機制

- **法規／稅制**：NSE 指數選擇權到期以指數收盤價現金結算，而收盤價（2026-08 以前）是成分股最後 30 分鐘的加權平均，所以只要影響最後半小時就影響結算（[NSE](https://www.nseindia.com/static/products-services/equity-derivatives-settlement-price)）。外國投資人（FPI）規定現貨必須實際交割、不能做日內現貨，Jane Street 因此用印度本地公司 JSI Investments 做日內現貨、離岸實體持選擇權；SEBI 把這個架構當成「刻意繞過規定」的證據（[SEBI 命令](https://www.sebi.gov.in/enforcement/orders/jul-2025/interim-order-in-the-matter-of-index-manipulation-by-jane-street-group_95040.html) ¶30、¶51）。
- **制度／產品設計**：交易所為搶量推出週選，2023 下半年起週一到週五每天都有某個指數到期（[Business Today](https://www.businesstoday.in/markets/stocks/story/nse-bse-fo-expiry-days-what-has-changed-for-stock-investors-history-more-480781-2025-06-18)）。Bank Nifty 只有 12 檔，前兩大權重合計超過一半（2024-10 NSE factsheet：HDFC Bank 28.71%、ICICI Bank 24.65%，[NSE](https://nsearchives.nseindia.com/content/indices/ind_nifty_bank.pdf)），推少數幾檔就能推動指數。
- **SEBI 指控的兩種手法**：(1) 盤中指數操縱：早盤（Patch I）大買成分股與期貨推高指數，同時在選擇權建立大量空方 delta；午盤（Patch II）反手賣出壓低指數。(2) 延長版收盤操縱（extended marking the close）：到期日最後約 60 分鐘大量賣出壓低結算價。
- **合法邊界**：SEBI 的判準是「這種交易單獨看沒有任何經濟理由」：現貨與期貨腿單獨看是虧的，只靠選擇權腿賺。

## 3. 關鍵數字

| 指標 | 數值 | 來源 |
|---|---|---|
| 檢查期間 | 2023-01-01 ～ 2025-05-31 | [Legal500](https://www.legal500.com/intelligence/india/corporate-commercial-law/sebi-update-interim-order-against-jane-street-group-for-alleged-index-manipulation) |
| 指數選擇權獲利 | ₹43,289 crore | 同上 |
| 虧損：股票期貨／指數期貨／現貨 | ₹7,208 / ₹191 / ₹288 crore | 同上 |
| 淨利 | ₹36,502 crore（約 US$4.3B） | 同上；[Business Today](https://www.businesstoday.in/markets/story/sebi-cracks-down-on-jane-street-in-landmark-derivatives-market-case-484348-2025-07-11) |
| 15 個 Bank Nifty 到期日的指數選擇權獲利 | ₹3,914 crore | [Legal500](https://www.legal500.com/intelligence/india/corporate-commercial-law/sebi-update-interim-order-against-jane-street-group-for-alleged-index-manipulation) |
| 不法所得（18 天：15 天 Bank Nifty + 3 天 Nifty） | ₹4,843.57 crore（約 US$566M） | 同上；[SCC Online](https://www.scconline.com/blog/post/2025/07/09/sebi-restrains-jane-street-group-from-accessing-securities-market/) |
| 2024-01-17 早盤買進成分股與期貨 | ₹4,370.03 crore；選擇權 delta 由 −₹7,311 擴大到 −₹39,426 crore；下午賣出 ₹5,372 crore；當日獲利 ₹734.93 crore | [Legal500](https://www.legal500.com/intelligence/india/corporate-commercial-law/sebi-update-interim-order-against-jane-street-group-for-alleged-index-manipulation) |
| 2024-01-17 Bank Nifty 選擇權名目 vs 成分股現貨 | 約 US$1.26T vs US$3.6B（約 350:1） | [SEBI 命令](https://www.sebi.gov.in/enforcement/orders/jul-2025/interim-order-in-the-matter-of-index-manipulation-by-jane-street-group_95040.html) |
| 散戶 F&O 虧損比例 | FY22–FY24 93%，合計逾 ₹1.8 lakh crore | [SEBI 研究](https://www.sebi.gov.in/media-and-notifications/press-releases/sep-2024/updated-sebi-study-reveals-93-of-individual-traders-incurred-losses-in-equity-fando-between-fy22-and-fy24-aggregate-losses-exceed-1-8-lakh-crores-over-three-years_86906.html) |
| Copthall 案 | Copthall 佔 Sensex 成分股收盤競價買單總值 86.6%；一筆 ₹98.11 crore 買單 7 秒內撤銷；扣押合計約 ₹3.67–3.68 crore | [Outlook Money](https://www.outlookmoney.com/invest/sensex-closing-auction-manipulation-explained-sebi-interim-order-jpmorgan-entity-mansi-stock-broking-cas-august-13) |

**監管後續**

| 日期 | 措施 | 來源 |
|---|---|---|
| 2024-11-20 起（2024-10-01 通函） | 每個交易所只留一個基準指數週到期（NSE 只留 Nifty 50，Bank Nifty 週選取消）、最低合約規模升至 ₹15 lakh、到期日賣方加收 2% 極端損失保證金；2025-02-01 起預收權利金、取消到期日跨期抵減 | [Angel One](https://www.angelone.in/news/market-updates/sebi-strengthens-index-derivative-rules)；[Outlook Money](https://www.outlookmoney.com/news/nse-discontinues-these-3-weekly-index-options-will-offer-only-nifty-50-weekly-option) |
| 2025-04 起 | 指數衍生品部位限制改為盤中監控（每日至少 4 次快照） | [SEBI](https://www.sebi.gov.in/legal/circulars/mar-2025/intraday-monitoring-of-position-limits-for-index-derivatives_93123.html) |
| 2025-09-01 | NSE 到期改週二、BSE 改週四；之後 BSE 權利金市佔升至約 28% | [ScanX](https://scanx.trade/stock-market-news/stocks/bse-gains-market-share-after-swapping-weekly-derivatives-expiry-day/18867657) |
| 2025-10-30 | 非基準指數衍生品須 ≥14 檔、單檔 ≤20%、前三大 ≤45% | [Upstox](https://upstox.com/news/market-news/financial-regulations/sebi-sets-implementation-timeline-for-derivatives-on-banknifty-bankex-finnifty/article-183871/) |
| 2026-08-03 | 收盤價改由收盤集合競價（Closing Auction Session, CAS）決定，15:20 開始、15:28–15:30 隨機結束（依 2026-01-16 通函） | [Outlook Money](https://www.outlookmoney.com/invest/sensex-closing-auction-manipulation-explained-sebi-interim-order-jpmorgan-entity-mansi-stock-broking-cas-august-13) |

## 4. 我的解讀（草稿，待討論）

1. **這個接縫的關鍵不是「推得動」，是「推的成本和收益在不同帳上」。** 現貨腿的虧損是真的、看得到的；選擇權腿的獲利來自結算價被移動，看不出來是誰付的。SEBI 的判準「單獨看沒有經濟理由」其實就是把兩條腿合起來看。對 prop desk 的含義很直接：任何策略只要有一條腿「必須靠另一條腿才賺錢，而且那條腿的獲利來自自己造成的價格」，在印度就是違法的。純粹在不同市場間收斂價差的 index arbitrage 不受影響，前提是現貨腿單獨也有正期望值。
2. **監管關的是「門」，不是接縫本身。** 減週到期、提高合約規模、盤中快照，這些都是讓同一件事變難或變貴，但「選擇權以現貨收盤結算 + 現貨薄」這個結構還在。2026-08-03 改成收盤集合競價後只過了 10 天就出現 Copthall 案：手法從「最後一小時大量成交」變成「競價時段掛大單再撤」，作用的仍然是結算價。這是「流量往同一接縫的另一個出口走」的直接例子。
3. **交易所自己是利益方。** NSE 先前自己調查後在 2025-04-30 結案，兩週後 Jane Street 再犯，最後是 SEBI 出手。當一線監管者的收入大多來自選擇權量時，期待它主動關接縫是不切實際的。台灣的對應問題是：台指選擇權的結算價機制有沒有類似「被結算的名目遠大於被推的現貨」的地方，需要另外查證，這裡不下結論。
4. **洩漏源是人才流動，不是監管偵測。** 策略曝光是因為 Jane Street 自己告前員工、律師在法庭上說溜嘴。對 prop desk 來說，一個好賺的接縫策略，最大的風險可能不是 alpha 衰退，而是自己的訴訟或離職員工讓監管知道它存在。

## 5. 限制與未證實

- **全部是初步認定**：SEBI 2025-07-03 是單方面臨時命令（prima facie），Jane Street 稱 SEBI 命令「根本錯誤」（fundamentally mistaken），主張是基本的指數套利。截至 2026-11-16，SAT 只就「調閱文件」的請求保留裁定，主要案件（是否操縱）沒有終局判決，SEBI 也還沒發確認命令（confirmatory order）。
- **淨利數字來源不一**：多數來源（含 Legal500 的命令摘要）寫 ₹36,502 crore；The Week / PTI 寫 ₹36,671 crore。本文以 SEBI 命令摘要的 ₹36,502 crore 為準。
- **2024-07-10 範例**：原手冊寫「該日積極賣出 Bank Nifty 期貨 ₹2,800 crore、建立選擇權空單 ₹44,154 crore、軟化收盤獲利 ₹225 crore」。我查到的命令摘要只說 3 個收盤操縱日（含 2024-07-10）合計約 ₹560 crore 選擇權獲利，沒有找到原手冊的三個數字，因此不採用。
- **原手冊寫「NSE 2025 年 5 月 15 日等日仍以 ₹4,911 crore 買進」**：命令摘要只說 2025-05-15 13:00–14:00 大買成分股與期貨，未查到 ₹4,911 crore，不採用。
- **原手冊寫「FIA 稱全球 84% 的股票選擇權在印度交易所買賣」**：FIA 的 84% 是 2024Q1 印度佔全球股權選擇權**成交量**（FIA 統計口徑為合約口數），印度合約名目小，以權利金計的佔比不同（[FIA](https://www.fia.org/marketvoice/articles/premium-turnover-indian-options-hits-150-billion)）。原手冊的寫法容易被讀成金額，本文未放入關鍵數字表。
- **原手冊寫「Bank Nifty 五檔權值股佔權重約 82%」**：未查證，不採用。正文改用 NSE 官方 factsheet 的前兩大權重（2024-10 合計 53.4%）。檢查期間（2023-01～2025-05）各月權重會隨價格變動，例如有報導寫 2024-02 為 25.2% 與 24.8%，本文只引用有官方文件的時點。
- Copthall 扣押金額各來源寫 ₹3.67 或 ₹3.68 crore（四捨五入差異）；Copthall 表示會向 SEBI 尋求澄清，目前未見上訴報導（[Free Press Journal](https://www.freepressjournal.in/business/jpmorgan-unit-plans-to-seek-clarification-on-sebis-market-manipulation-order)）。
- Jane Street 內部是否有合法性爭論：付費牆內，未能證實。

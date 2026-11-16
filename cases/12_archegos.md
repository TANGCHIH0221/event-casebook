# 案例 12：Archegos 爆倉（2021-03）

> **一句話**：Archegos 用總報酬互換（TRS）在多家主經紀商堆出 1,600 億美元曝險，每家銀行只看得到自己那一塊；ViacomCBS 增資觸發股價下跌、保證金追繳違約後，先賣的 Goldman、Morgan Stanley 幾乎全身而退，最後賣的 Credit Suisse 與 Nomura 虧掉 80 億美元以上。

| 項目 | 內容 |
|---|---|
| 接縫 | TRS 部位不需要像直接持股那樣申報（市場與其他銀行看不到總曝險）× 每家主經紀商各自計算保證金、只看自己的帳 |
| 強制流來源 | Archegos 未能補繳保證金而違約，各主經紀商依 TRS 合約處分自己的避險股票 |
| 量級 | SEC：2021-03 高峰時資產逾 360 億美元、曝險 1,600 億美元；2021-03-26 Goldman 單日 block 賣出 105 億美元 |
| 不看價格的一方 | 處分擔保品的主經紀商（目標是在別家之前出清） |
| 天然對手方 | 承接 block 的避險基金與長線資金（以大幅折價接手） |
| 規則風險 | 中：刑事與民事追訴已完成（Bill Hwang 判刑 18 年）；TRS 部位揭露規範的修法進度本文未查證 |
| 查證狀態 | ✅ 曝險數字對 SEC 新聞稿；銀行損失對媒體彙整與 CS 特別委員會報告；block 金額對 Bloomberg |

---

## 1. 發生了什麼

| 日期 | 事件 | 來源 |
|---|---|---|
| 2020-03 → 2021-03 | 依 SEC 起訴：Archegos 從資產約 15 億、曝險 100 億美元，膨脹到資產逾 360 億、曝險 1,600 億美元 | [SEC 新聞稿 2022-70](https://www.sec.gov/news/press-release/2022-70) |
| 2021-03-11 ～ 03-19 | Archegos 向 Credit Suisse 取回共 24 億美元的超額保證金，CS 風控全數核准 | [BNN Bloomberg（引 Paul, Weiss 報告）](https://www.bnnbloomberg.ca/credit-suisse-claws-back-pay-as-it-faults-staff-for-archegos-1.1634291)；[Investing.com/Reuters 重點整理](https://m.investing.com/news/stock-market-news/factboxkey-points-of-credit-suisse-archegos-postmortem-2572392?ampMode=1) |
| 2021-03-22 | ViacomCBS 盤後宣布約 30 億美元股票與可轉換特別股增資 | [Motley Fool](https://www.fool.com/investing/2021/03/23/viacomcbs-floating-3-billion-in-new-stock-followin)；[Bloomberg](https://www.bloomberg.com/news/articles/2021-03-22/viacomcbs-sinks-after-announcing-3-billion-share-offering) |
| 2021-03-23 | ViacomCBS 收跌 9% | [CNBC](https://www.cnbc.com/2021/03/23/viacomcbs-stock-closes-down-9percent-company-says-itll-raise-3-billion.html) |
| 2021-03-26（五） | Goldman 以 block 賣出 105 億美元：開盤前 66 億（百度、騰訊音樂、唯品會），其餘約 39 億（ViacomCBS、Discovery、Farfetch、愛奇藝、跟誰學）；ViacomCBS 與 Discovery 當日各跌逾 27% | [Bloomberg](https://www.bloomberg.com/news/articles/2021-03-27/goldman-sold-10-5-billion-of-stocks-in-block-trade-spree)；[CNBC](https://www.cnbc.com/2021/03/29/the-archegos-blowup-and-its-ripple-effect-across-markets.html) |
| 2021-03-29（一） | Nomura 揭露約 20 億美元可能損失，股價收跌約 16.3%（史上最大單日跌幅）；Credit Suisse 收跌約 14% | [Business Standard/Reuters](https://www.business-standard.com/amp/article/international/credit-suisse-nomura-tumble-as-banks-tally-exposure-to-archegos-damage-121032900348_1.html)；[Yahoo/Reuters](https://news.yahoo.com/nomura-credit-suisse-warn-losses-072836792.html) |
| 2021-04 下旬 | 各銀行公布損失：CS 約 55 億、Nomura 23 億（另預估 2021 會計年度再損約 5.7 億）、Morgan Stanley 9.11 億、UBS 7.74 億（Q2 再認 0.87 億）、三菱 UFJ 2.7 億美元；Goldman、Deutsche Bank 無重大損失 | [Fortune 2021-04-27](https://fortune.com/2021/04/27/heres-how-much-big-banks-have-lost-so-far-from-the-archegos-collapse/)；[nippon.com/Reuters](https://nippon.com/en/news/reu20210427KBN2CE0HM) |
| 2021-07-29 | Credit Suisse 公布 Paul, Weiss 獨立調查報告：損失源於風控失靈與缺乏問責 | [Paul, Weiss](https://paulweiss.com/practices/litigation/internal-investigations/news/credit-suisse-publishes-independent-review-of-archegos-losses?id=40637)；[Fortune](https://fortune.com/2021/07/29/credit-suisse-report-archegos-loss-bank-massive-culture-problem/) |
| 2022-04-27 | SEC、司法部、CFTC 起訴 Bill Hwang 等人 | [SEC 新聞稿 2022-70](https://www.sec.gov/news/press-release/2022-70) |
| 2024-11-20 | Hwang 7 月遭陪審團定罪 10 項罪名後，被判刑 18 年 | [美國司法部 SDNY](https://www.justice.gov/usao-sdny/pr/founder-and-head-archegos-capital-management-bill-hwang-sentenced-18-years-prison)；[NBC News](https://www.nbcnews.com/news/us-news/archegos-bill-hwang-sentenced-18-years-prison-massive-us-fraud-rcna181134) |

## 2. 機制

- **法規**：用 TRS 取得的經濟曝險，名義上股票掛在銀行名下，Archegos 不必像直接持股那樣申報。市場與其他銀行看不到它在同一檔股票上的總部位。SEC 起訴書指控 Archegos 還刻意對交易對手隱瞞曝險、集中度與流動性。
- **制度設計**：每家主經紀商只用自己帳上的部位算保證金。對單一銀行看起來可控的部位，加總起來可能是個股流通量的一大塊。
- **觸發**：ViacomCBS 在股價高檔增資，股價下跌觸發保證金追繳；Archegos 繳不出來，所有銀行同時面臨同一個問題：誰先賣。
- **誘因**：先賣的人用接近市價出清，後賣的人面對已經被砸過的價格。這是典型的囚徒困境，合作停損的協議在 03-26 前破局（銀行間協商細節未對一手來源，見第 5 節）。

## 3. 關鍵數字

| 指標 | 數值 | 來源 |
|---|---|---|
| 高峰資產 / 曝險 | 逾 360 億 / 1,600 億美元 | [SEC 新聞稿 2022-70](https://www.sec.gov/news/press-release/2022-70) |
| Goldman 03-26 block | 105 億美元 | [Bloomberg](https://www.bloomberg.com/news/articles/2021-03-27/goldman-sold-10-5-billion-of-stocks-in-block-trade-spree) |
| Credit Suisse 損失 | 約 55 億美元（50 億瑞郎） | [Fortune](https://fortune.com/2021/04/27/heres-how-much-big-banks-have-lost-so-far-from-the-archegos-collapse/)；[Paul, Weiss](https://paulweiss.com/practices/litigation/internal-investigations/news/credit-suisse-publishes-independent-review-of-archegos-losses?id=40637) |
| Nomura 損失 | 約 29 億美元（含後續認列） | [nippon.com/Reuters](https://nippon.com/en/news/reu20210427KBN2CE0HM) |
| Morgan Stanley 損失 | 9.11 億美元 | [Fortune](https://fortune.com/2021/04/27/heres-how-much-big-banks-have-lost-so-far-from-the-archegos-collapse/) |
| UBS 損失 | 7.74 億 + 0.87 億美元 | 同上 |
| 銀行合計 | 約 100 億美元 | 同上 |
| Hwang 刑期 | 18 年 | [美國司法部 SDNY](https://www.justice.gov/usao-sdny/pr/founder-and-head-archegos-capital-management-bill-hwang-sentenced-18-years-prison) |

## 4. 我的解讀（草稿，待討論）

1. **強制賣方之間也有排序，排序決定誰付帳。** 同一個違約、同一批股票，Goldman 與 Deutsche Bank 幾乎沒損失，CS 與 Nomura 合計虧逾 80 億美元。差別在誰先按下賣出。對 prop desk 來說，看到異常大的 block 出現在一組看似無關的股票（中概 + 美國傳媒）時，要先問「是不是同一個持有人在被清算、還有幾家銀行還沒賣」。第一批 block 通常不是最後一批。
2. **看不見的槓桿，接縫在揭露規則。** 直接持股要申報，TRS 不用；每家銀行的風控都合理，但沒有人看得到總數。這跟案例 8 的 Robinhood 很像：單一機構的規則都合理，系統層面的風險落在規則的縫隙。
3. **發行人行為可以是觸發點。** ViacomCBS 在股價高檔增資，從公司角度完全合理，卻是壓垮 Archegos 的第一根稻草。對高度集中持股（不管是可見的還是透過 swap）的個股，增資、可轉債發行這類「公司自己製造供給」的事件，應該被當成潛在的強制流觸發日。

## 5. 限制與未證實

- 原手冊寫「資產約 100 億美元但部位逾 500 億美元（約 5 倍槓桿）」：與 SEC 起訴書數字不符。SEC 是**資產逾 360 億、曝險 1,600 億美元**（約 4.4 倍）。原手冊的數字來源不明，本文刪除。
- 原手冊寫「Goldman 最早於 3/26 與 Archegos 達成協議、單日賣出 30–40 億 block」：Bloomberg 的數字是 Goldman 當天 block 共 **105 億**（開盤前 66 億）。「與 Archegos 達成協議」以及銀行間曾經協商一起慢慢出清的說法，只見於媒體轉述，未對一手來源，本文不寫成事實。
- 原手冊寫「Nomura 損失 3,070 億日圓（約 28.7 億美元）」：Nomura 2021-04-27 公布總損失約 29 億美元，其中約 23 億認列在截至 2021-03-31 的季度（[Japan Times](https://japantimes.co.jp/news/2021/04/27/business/corporate-business/nomura-losses-archegos-capital-management)）。3,070 億日圓這個數字沒有找到來源。
- 原手冊寫「UBS 首季淨利減 4.34 億美元」：Fortune 報導 UBS 首季認列 **7.74 億美元**損失、Q2 再認 0.87 億。4.34 億的來源不明，本文刪除。
- 原手冊寫「CS 損失成為其 2023 年倒閉的遠因之一」：屬於評論，本文未納入。
- ViacomCBS 增資公告是 03-22 盤後還是 03-23，各家報導不一；本文採 03-22 盤後、03-23 反映。
- TRS 部位揭露規範（例如 SEC 對大額 security-based swap 部位的申報規則）的現況未查證。

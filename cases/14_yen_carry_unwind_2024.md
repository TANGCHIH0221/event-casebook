# 案例 14：日圓套利平倉與 2024-08-05 全球急跌（2024-07 ～ 2024-08）

> **一句話**：日銀意外升息加上美國就業數據轉弱，日圓急升，借日圓買高收益資產的槓桿部位被迫平倉；日經 8/5 單日跌 12.4%、台股跌 8.35%，兩天後日銀副總裁說「市場不穩就不升息」，市場隔天就反彈。

| 項目 | 內容 |
|---|---|
| 接縫 | 日圓長期接近零利率（日銀政策）＋ 全球槓桿資金用日圓當融資貨幣、用保證金與波動率控管部位（市場慣例）→ 日圓一升，融資成本與風險管理同時逼人減倉 |
| 強制流來源 | 保證金追繳與風險限額：匯率與股價同時不利時，槓桿部位必須減倉；BIS 稱這次是「順週期去槓桿與保證金上調」放大了波動 |
| 量級 | BIS 粗估事件前日圓套利部位約 ¥40 兆（約 US$2,500 億），且可能低估；CFTC 投機者日圓淨空單約 18.4 萬口（約 17 年最大），8 月中翻成淨多 |
| 不看價格的一方 | 被追繳保證金、觸發風險限額的槓桿部位 |
| 天然對手方 | 8/6 接手的買盤（日經單日 +10.2%）；以及事後改口的日銀 |
| 規則風險 | 央行溝通本身就是規則：8/7 日銀副總裁內田表示市場不穩時不升息 |
| 查證狀態 | ✅ 價格與日期已對兩個以上來源；⚠️ 套利部位規模只有 BIS 粗估，各家口徑不同 |

---

## 1. 發生了什麼

| 日期 | 事件 | 來源 |
|---|---|---|
| 2024-07-11 | 日經 225 收盤創當時新高 42,224.02，盤中高 42,426.77 | [Business Standard](https://www.business-standard.com/markets/capital-market-news/japanese-markets-reach-record-highs-124071100753_1.html) |
| 2024-07 上旬 | CFTC 投機者日圓淨空單約 18.4 萬口，約 17 年最大 | [The Star / Reuters](https://www.thestar.com.my/business/business-news/2024/08/20/funds-go-long-yen-for-first-time-in-four-years-as-carry-trade-unwinds) |
| 2024-07-31 | 日銀以 7 比 2 決議把隔夜拆款利率目標由 0–0.1% 升到約 0.25%，並公布縮減購債計畫；市場多數未預期 | [BNN Bloomberg](https://bnnbloomberg.ca/business/international/2024/07/31/boj-hikes-interest-rate-unveils-plan-to-reduce-bond-buying)；[ING](https://think.ing.com/snaps/bank-of-japan-surprise-15bp-hike-and-gradual-tapering-of-jgb-purchases) |
| 2024-08-02 | 美國 7 月非農僅增 11.4 萬人，失業率升到 4.3%，觸發薩姆規則（Sahm rule） | [PBS](https://www.pbs.org/newshour/amp/economy/u-s-hiring-slows-with-just-114000-jobs-added-in-july-unemployment-rate-hits-4-3-percent)；[Fox Business](https://www.foxbusiness.com/economy/july-jobs-report-just-triggered-reliable-recession-indicator) |
| 2024-08-05 | 日經收 31,458.42，跌 4,451.28 點（−12.4%），點數史上最大、跌幅 1987 年黑色星期一以來最大；台股加權收 19,830.88，跌 1,807.21 點（−8.35%），點數與幅度皆創紀錄；VIX 盤前一度 65.73；S&P 500 約 −3% | [Fox Business](https://foxbusiness.com/economy/japanese-stocks-plunge-largest-rout-black-monday)；[數位時代](https://www.bnext.com.tw/article/79996/taiex-fell-by-1807-points)；[Investing.com](https://investing.com/news/economy-news/wall-street-fear-gauge-posts-record-intraday-jump-as-stocks-slide-3554919) |
| 2024-08-06 | 日經收 34,675.46，漲 3,217.04 點（+10.2%），點數史上最大漲幅 | [Business Standard](https://www.business-standard.com/amp/markets/capital-market-news/japanese-markets-recover-sharply-nikkei-rebounds-10-23-124080600913_1.html) |
| 2024-08-07 | 日銀副總裁內田真一：「金融與資本市場不穩定時，日銀不會升息」，日圓一度貶 2.5% | [Bloomberg](https://www.bloomberg.com/news/articles/2024-08-07/boj-won-t-raise-interest-rate-if-markets-unstable-uchida-says)；[Sharecast](https://sharecast.com/amp/news/international-economic/bojs-uchida-says-rates-wont-rise-when-markets-unstable--17214533.html) |
| 2024-08-13 那週 | CFTC 投機者日圓轉為淨多約 2.3 萬口，2021-03 以來首次 | [The Star / Reuters](https://www.thestar.com.my/business/business-news/2024/08/20/funds-go-long-yen-for-first-time-in-four-years-as-carry-trade-unwinds) |
| 2024-08-27 | BIS Bulletin No. 90 分析此次動盪與套利平倉 | [BIS](https://www.bis.org/publ/bisbull90.htm) |

## 2. 機制

- **法規／政策**：日本長期零利率讓日圓成為最便宜的融資貨幣。日銀 7/31 升息幅度只有 15bp，但它改變的是「這個融資來源會不會一直便宜」的預期。
- **制度／市場結構**：借日圓買美股、墨西哥披索等高收益資產的部位，同時暴露在匯率與資產價格上。美國就業數據轉弱讓美國利率預期下修，美日利差收窄、日圓走強，兩邊一起虧。保證金追繳與波動率上升觸發的減倉都是順週期的：越跌越要賣。BIS 的說法是「又一個被順週期去槓桿與保證金上調放大的波動事件」。
- **人性／誘因**：部位擁擠。CFTC 日圓淨空單在 7 月初達約 17 年高點，代表同一方向的人很多；出口很窄。

## 3. 關鍵數字

| 指標 | 數值 | 來源 |
|---|---|---|
| 日圓套利部位規模（事件前） | 粗估約 ¥40 兆（約 US$2,500 億），BIS 認為因資料缺口可能偏低 | [BIS Bulletin 90](https://www.bis.org/publ/bisbull90.htm) |
| CFTC 投機者日圓部位 | 7 月初淨空約 18.4 萬口 → 8/13 那週淨多約 2.3 萬口 | [The Star / Reuters](https://www.thestar.com.my/business/business-news/2024/08/20/funds-go-long-yen-for-first-time-in-four-years-as-carry-trade-unwinds) |
| 槓桿基金日圓淨空（另一口徑） | 6 月底約 13.8 萬口，2007 年以來最大 | [Hedgeweek 引 Bloomberg](https://www.hedgeweek.com/hedge-funds-cut-yen-shorts-following-of-us-japan-intervention/) |
| 日經 2024-08-05 | 31,458.42，−4,451.28 點，−12.4% | [Fox Business](https://foxbusiness.com/economy/japanese-stocks-plunge-largest-rout-black-monday) |
| 日經 2024-08-06 | 34,675.46，+3,217.04 點，+10.2% | [Business Standard](https://www.business-standard.com/amp/markets/capital-market-news/japanese-markets-recover-sharply-nikkei-rebounds-10-23-124080600913_1.html) |
| 台股加權 2024-08-05 | 19,830.88，−1,807.21 點，−8.35% | [數位時代](https://www.bnext.com.tw/article/79996/taiex-fell-by-1807-points) |
| VIX 2024-08-05 | 盤前高 65.73；美股正常交易時段最高約 55.68；收 38.57 | [Investing.com](https://investing.com/news/economy-news/wall-street-fear-gauge-posts-record-intraday-jump-as-stocks-slide-3554919)；[Russell Rhoads](https://russellrhoads.substack.com/p/did-vix-at-65-count-maybe-not)；[E*TRADE](https://us.etrade.com/knowledge/library/perspectives/daily-insights/aug-12-market-recap) |
| S&P 500 2024-08-05 | 約 −3.0% | [Investing.com](https://investing.com/news/economy-news/wall-street-fear-gauge-posts-record-intraday-jump-as-stocks-slide-3554919) |
| 美國 10 年期公債 2024-08-05 | 盤中低至 3.67%，2023 年中以來最低 | [Briefing.com](https://briefing.com/bond-market-update/archive/2024/8/5/opening-advance-reversed) |

## 4. 我的解讀（草稿，待討論）

1. **這個案例的「強制流」沒有規則可以事先算。** 跟槓桿 ETF 或指數調整不同，套利部位的規模、成本、停損點都不公開，BIS 只能給「粗估 ¥40 兆、可能偏低」。能事先看到的只有擁擠度（CFTC 部位在 17 年高點）。所以這類事件對 prop desk 的用法不是預測何時爆，而是在擁擠度高時降低與該部位同向的曝險、準備好在平倉日當流動性提供者。
2. **接縫是央行溝通，而監管反應快到兩天。** 7/31 升息、8/5 崩、8/7 副總裁說「市場不穩不升息」。跟印度、韓國要幾個月甚至幾年才修規相比，央行的反應是用一句話修正預期。這代表「被迫賣出」的流量很集中，但也很短：日經 8/6 就漲回 10.2%。對事件交易來說，這類宏觀去槓桿的報酬主要在「接住」而不是「放空」。
3. **台股的損失是被傳染，不是自己的接縫。** 台股 8/5 跌點與跌幅都創紀錄，但台灣不是套利資金的融資端。用證交所資料看傳導路徑（FinMind 全市場三大法人與融資餘額）：
   - **外資先賣**：8/2 賣超 944 億、8/5 賣超 688 億；從日經高點 7/11 到 8/5 累計賣超 4,703 億元。
   - **融資斷頭晚一天**：融資餘額 8/5 減少 183 億、8/6 再減 163 億，兩天共 346 億。追繳有時間差，所以本地的強制賣壓落在反彈日 8/6，正好被外資回補（+248 億）接住。
   - **投信逆勢買**：8/2 ～ 8/7 每天淨買 104 ～ 178 億。
   外資的全球減風險是第一波，本地融資斷頭是第二波，兩波隔一天。

## 5. 限制與未證實

- **原手冊寫「BIS Bulletin No. 90 明確指出日圓套利平倉為主因」**：BIS 的說法是槓桿部位（股票與外匯）平倉放大了市場對美國負面數據的反應，套利交易「受到去槓桿壓力重創」，是放大器之一，不是單一主因。
- **原手冊寫「CFTC 非商業日圓淨空單從紀錄高約 18 萬口降至約四分之一」**：實際上 8/13 那週已翻成淨多約 2.3 萬口，不是降到四分之一；且 18.4 萬口是「約 17 年最大」，不一定是歷史紀錄（[Reuters 轉載](https://www.thestar.com.my/business/business-news/2024/08/20/funds-go-long-yen-for-first-time-in-four-years-as-carry-trade-unwinds)）。不同口徑（投機者 vs 槓桿基金）的峰值也不同：18.4 萬 vs 13.8 萬。
- **原手冊寫「10 年美債殖利率 7/24–8/5 下跌 55bp（4.28%→3.73%）」**：8/5 收盤各來源寫約 3.79–3.80%，盤中低 3.67%；我沒有找到 3.73% 的收盤來源，也沒有核對 7/24 的 4.28%，不採用。
- **原手冊寫「日經自 7/11 高點蒸發 7,920 億美元市值」**：未查到來源，不採用。
- **原手冊寫「VIX 飆破 65」**：65.73 是美股開盤前（流動性低）的報價；正常交易時段最高約 55.68。引用時應註明。
- **原手冊寫日經是「1987 年黑色星期一以來最差單日」**：正確；但 1987 年跌 14.9% 仍較大，所以 12.4% 是史上第二大跌幅，點數則是史上最大。
- 日本本地 2 倍槓桿 ETF（如 NEXT FUNDS 1570）當天的再平衡量沒有公開數字，未納入。

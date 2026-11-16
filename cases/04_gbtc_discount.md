# 案例 4：GBTC 折價收斂與轉 ETF 後的強制贖回（2022-12 ～ 2024-12）

> **一句話**：GBTC 是不能贖回的封閉式信託，折價一度近 50%；法院判 SEC 敗訴、轉成 ETF 之後，贖回打開、折價消失，接著破產遺產（FTX、Genesis）與高費率逃離者一年內贖回逾 200 億美元，這次賣壓透過申贖機制直接傳到比特幣現貨。

| 項目 | 內容 |
|---|---|
| 接縫 | 封閉式信託無贖回機制（折價套不掉）× 大量受監管帳戶只能透過證券帳戶取得比特幣曝險（GBTC 是 2024 年前少數管道） |
| 強制流來源 | 轉 ETF 前：無；轉 ETF 後：破產遺產依法院程序變現（FTX、Genesis），以及 1.5% 高費率驅動的換倉 |
| 量級 | FTX 遺產約 2,200 萬股、近 10 億美元；Genesis 獲准出售 GBTC 約 13.8 億美元；2024 全年 GBTC 淨流出逾 200 億美元 |
| 不看價格的一方 | 破產遺產（目標是還債，不是擇時）；轉 ETF 前「只能買 GBTC」的受限帳戶 |
| 天然對手方 | 轉 ETF 前：買折價等轉換的套利者；轉 ETF 後：授權參與者（AP）贖回並在現貨市場賣比特幣，以及其他現貨 ETF 的買方 |
| 規則風險 | 已實現：2023-08-29 法院判決 + 2024-01-10 SEC 核准，是這個接縫的關閉時間戳 |
| 查證狀態 | ✅ 折價與流量數字已對 CoinDesk、Bloomberg、法院判決報導；FTX 出售股數兩家媒體說法不同（見第 5 節） |

---

## 1. 發生了什麼

| 日期 | 事件 | 來源 |
|---|---|---|
| 2022-12-13 | GBTC 折價首次突破 50%（SEC 重申駁回理由後），數小時內回到約 48.66% | [CoinDesk](https://www.coindesk.com/business/2022/12/13/grayscale-bitcoin-trust-discount-reaches-record-50) |
| 2022-12 下旬 | CoinDesk 事後回顧稱折價紀錄為 49% | [CoinDesk 2023-02-13](https://www.coindesk.com/markets/2023/02/13/grayscales-gbtc-discount-widens-to-near-record-high/) |
| 2023-08-29 | 華盛頓特區巡迴上訴法院判 SEC 駁回 GBTC 轉 ETF「武斷且反覆無常」（arbitrary and capricious），撤銷該駁回令；GBTC 當日漲約 17%，2021-07 以來最大單日漲幅，折價收斂到約 18% | [Decrypt](https://decrypt.co/154119/grayscale-wins-appeal-against-sec-to-convert-bitcoin-trust-to-etf)；[Bloomberg](https://www.bloomberg.com/news/articles/2023-08-30/grayscale-bitcoin-trust-gbtc-surges-most-since-2021-on-court-ruling)；[InvestmentNews](https://www.investmentnews.com/alternatives/bitcoin-fund-behemoth-surges-after-etf-court-ruling/241573) |
| 2023-11-24 | 折價收斂到 8.6%，2021-07 以來最窄 | [CoinDesk](https://www.coindesk.com/markets/2023/11/24/grayscales-gbtc-discount-to-nav-at-narrowest-since-july-2021-on-etf-optimism/) |
| 2024-01-10 | SEC 核准 11 檔比特幣現貨 ETF（含 GBTC 轉換） | [ETFdb](https://etfdb.com/crypto-content-hub/grayscale-bitcoin-trust-gbtc-becomes-spot-bitcoin-etf/) |
| 2024-01-11 | GBTC 以 ETF 身分交易，管理費維持 1.5%（部分同業低至 0.2%，到 01-17 已流出約 5.79 億美元）；開始每日淨流出 | [WealthManagement/Bloomberg](https://www.wealthmanagement.com/etfs/traders-pull-579-million-out-of-grayscale-bitcoin-etf) |
| 2024-01-17 ～ 19 | 折價縮到 0.5% 以下，之後貼近淨值 | [FXStreet](https://www.fxstreet.com/amp/cryptocurrencies/news/grayscale-outflows-reach-28-billion-even-as-gbtc-discount-contracts-to-less-than-03-202401200556) |
| 2024-01-22 | 報導 FTX 破產遺產賣出約 2,200 萬股 GBTC、價值近 10 億美元，佔轉換後頭幾天流出的一大塊 | [CoinDesk](https://www.coindesk.com/business/2024/01/22/ftx-sold-about-1b-of-grayscales-bitcoin-etf-explaining-much-of-outflow-sources) |
| 2024-02-14 | 破產法官核准 Genesis 出售 Grayscale 信託持股合計約 16 億美元（其中 GBTC 約 13.8 億） | [Decrypt](https://decrypt.co/217803/genesis-approved-sell-1-6b-grayscale-bitcoin-shares)；[Investing.com/Reuters](https://uk.investing.com/news/cryptocurrency-news/bankrupt-genesis-gets-green-light-to-liquidate-138-billion-in-grayscale-trust-shares-3339677) |
| 2024-02-26 | 轉 ETF 後頭 30 個交易日累計流出 74 億美元 | [Bloomberg](https://www.bloomberg.com/news/articles/2024-02-26/grayscale-s-gbtc-bitcoin-etf-exodus-reaches-7-4-billion-in-30-days) |
| 2024-03-04 | 連續 36 天流出，累計 92.6 億美元；持幣從約 62 萬顆降到約 42 萬顆（−33%） | [Cointelegraph](https://cointelegraph.com/news/grayscale-gbtc-bitcoin-fallen-33-percent-since-etf-conversion) |
| 2024-12-31 | 2024 全年 GBTC 淨流出逾 200 億美元 | [Cointelegraph](https://cointelegraph.com/news/blackrock-bitcoin-etf-tops-rivals-2024-net-inflows) |

## 2. 機制

- **法規**：2024 年以前 SEC 不核准比特幣現貨 ETF，受監管帳戶（退休帳戶、部分機構）想要比特幣曝險只能買 GBTC 這類證券。
- **產品設計**：GBTC 是信託，只有申購、沒有贖回。2021 年以前需求大於供給，GBTC 有溢價；需求消失後，折價沒有任何機制可以拉回，只能等轉成 ETF。
- **觸發**：法院判決（2023-08-29）把「會不會轉 ETF」從不確定變成「什麼時候」，折價當天就收斂到約 18%。
- **轉換後反轉**：ETF 有申贖，折價消失，但 1.5% 費率與破產遺產的變現需求同時湧出。AP 收到贖回單就把比特幣在現貨市場賣掉，所以這波賣壓沒有反映在 GBTC 的折價上，而是反映在比特幣本身。

## 3. 關鍵數字

| 指標 | 數值 | 來源 |
|---|---|---|
| 折價紀錄 | 盤中破 50%（2022-12-13） | [CoinDesk](https://www.coindesk.com/business/2022/12/13/grayscale-bitcoin-trust-discount-reaches-record-50) |
| 判決當日折價 | 約 18% | [InvestmentNews](https://www.investmentnews.com/alternatives/bitcoin-fund-behemoth-surges-after-etf-court-ruling/241573) |
| 轉換前最窄 | 8.6%（2023-11-24） | [CoinDesk](https://www.coindesk.com/markets/2023/11/24/grayscales-gbtc-discount-to-nav-at-narrowest-since-july-2021-on-etf-optimism/) |
| GBTC 管理費 | 1.5% | [WealthManagement/Bloomberg](https://www.wealthmanagement.com/etfs/traders-pull-579-million-out-of-grayscale-bitcoin-etf) |
| FTX 遺產賣出 | 約 2,200 萬股，近 10 億美元 | [CoinDesk](https://www.coindesk.com/business/2024/01/22/ftx-sold-about-1b-of-grayscales-bitcoin-etf-explaining-much-of-outflow-sources) |
| Genesis 獲准出售 | GBTC 約 13.8 億美元（三檔信託合計約 16 億） | [Investing.com/Reuters](https://uk.investing.com/news/cryptocurrency-news/bankrupt-genesis-gets-green-light-to-liquidate-138-billion-in-grayscale-trust-shares-3339677) |
| 2024 全年淨流出 | 逾 200 億美元 | [Cointelegraph](https://cointelegraph.com/news/blackrock-bitcoin-etf-tops-rivals-2024-net-inflows) |

## 4. 我的解讀（草稿，待討論）

1. **折價交易的報酬來自「監管時間戳」，不是來自基本面。** 折價從 50% 收斂到 0，幾乎全部發生在兩個日期附近：法院判決與 SEC 核准。這類交易的風險是資金被卡住、不知道要等多久，報酬是對「規則何時改」的判斷。這跟接縫理論說的「接縫要靠修法才會消失，修法有時間戳」完全對應。
2. **一旦有申贖，強制流就會穿透到標的。** 轉 ETF 前，持有人只能在次級市場賣 GBTC，賣壓變成折價；轉 ETF 後，同樣的賣壓透過 AP 贖回變成比特幣現貨賣單。對 prop desk 來說，看到結構改變時要跟著換交易標的：從「做 GBTC 折價」換成「做比特幣現貨的短期賣壓」。
3. **破產遺產是最好預測的不看價格賣方。** FTX、Genesis 的出售要經過法院程序，動機、持股量都在公開文件裡。Genesis 2024-02-14 獲准、FTX 在 2023-11 申報書就揭露持有 2,230 萬股。持股與獲准日期都是公開資訊，這類流量可以事前排進日曆。

## 5. 限制與未證實

- 原手冊寫「2022 年 12 月底創紀錄 49% 折價」：CoinDesk 當時的報導是 12-13 盤中首次突破 50%、數小時後回到 48.66%；「12 月底 49%」是 CoinDesk 2023-02 回顧時的說法。數字差異來自取樣時點，兩者都對，但紀錄應寫「盤中破 50%」。
- 原手冊寫「2023 年 8 月 Grayscale 對 SEC 訴訟勝訴 → 折價收斂」：正確，但勝訴不是直接核准 ETF，而是撤銷 SEC 的駁回令、發回重審。
- 原手冊寫 2023-12-20 約 7%、2024-01 上市前低至 5.6%：未找到可對的一手數據，本文刪除。
- FTX 遺產出售：CoinDesk 說全部賣光（約 2,200 萬股）；Bloomberg（經 Cointelegraph 轉述）說轉換後三天賣出「超過三分之二」。兩者不一致，本文採 CoinDesk 的總量並標註。
- 全年淨流出「逾 200 億美元」是 Farside 資料經媒體轉述，未直接下載 Farside 原始資料核對。

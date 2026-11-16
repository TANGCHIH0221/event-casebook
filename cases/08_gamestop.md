# 案例 8：GameStop（2021-01）

> **一句話**：讓 GME 漲勢停下來的不是空方，而是結算所：NSCC 在 2021-01-28 清晨要求 Robinhood 補約 30 億美元保證金，Robinhood 只能禁止買進，需求面瞬間被切斷；SEC 事後報告認為空方回補只佔買量一小部分，也沒找到 gamma squeeze 的證據。

| 項目 | 內容 |
|---|---|
| 接縫 | T+2 結算期間由券商向結算所（NSCC）繳保證金，且保證金依波動度與券商資本動態加碼 × 零手續費、靠 PFOF 營利的散戶券商，把大量同方向散戶流量集中在資本很薄的少數幾家 |
| 強制流來源 | NSCC 依其規則計算的 VaR 保證金 + 超額資本附加費（Excess Capital Premium, ECP）；券商為了繳得出來，只能限制客戶「只能賣、不能買」 |
| 量級 | Robinhood 01-28 清晨通知應繳總額約 37 億美元（已存 6.96 億，缺口約 30 億）；01-27 NSCC 對 36 家會員盤中追繳共 69 億美元 |
| 不看價格的一方 | 被限制只能賣出的 Robinhood 等券商客戶；保證金被追繳、必須回補的空方 |
| 天然對手方 | 限制買進後仍持有空單或新建空單的人；造市商（承接散戶流量） |
| 規則風險 | 已實現：SEC 2023-02 通過 T+1，2024-05-28 實施，縮短結算期間、降低保證金需求 |
| 查證狀態 | ✅ 已對 SEC 員工報告與 Robinhood 執行長國會書面證詞兩份一手文件 |

---

## 1. 發生了什麼

| 日期 | 事件 | 來源 |
|---|---|---|
| 2020-12-31 | GME 放空股數佔流通在外股數 109.26%（SEC 統計的高點）；以自由流通股計，2021-01 最高 122.97% | [SEC 員工報告 p.24–25](https://www.sec.gov/files/staff-report-equity-options-market-struction-conditions-early-2021.pdf) |
| 2021-01-11 | 宣布 Ryan Cohen 加入董事會，盤中高 20.65 美元 | [SEC 員工報告 p.18](https://www.sec.gov/files/staff-report-equity-options-market-struction-conditions-early-2021.pdf) |
| 2021-01-22 | 約三小時內從 43 漲到 72 美元（+71%）；單日成交 1.972 億股，當月最高 | [SEC 員工報告 p.18–19](https://www.sec.gov/files/staff-report-equity-options-market-struction-conditions-early-2021.pdf) |
| 2021-01-25 | Citadel 與 Point72 注資 Melvin Capital 27.5 億美元；Melvin 1 月虧損約 53% | [Fox Business](https://foxbusiness.com/markets/melvin-capital-hedge-fund-that-bet-against-gamestop-lost-53-in-january) |
| 2021-01-27 | 收盤 347.51 美元，較 01-11 收盤漲逾 1,600%；NSCC 盤中向 36 家會員追繳 69 億美元（其中 48 億為特別 ECP 附加費），全體會員保證金需求達 255 億美元 | [SEC 員工報告 p.18, 31](https://www.sec.gov/files/staff-report-equity-options-market-struction-conditions-early-2021.pdf) |
| 2021-01-28 05:11 ET | NSCC 自動通知 Robinhood：VaR 保證金近 13 億 + ECP 逾 22 億，總額約 37 億美元，扣掉已存 6.96 億，缺口約 30 億 | [Tenev 國會證詞 p.9](https://democrats-financialservices.house.gov/UploadedFiles/HHRG-117-BA00-Wstate-TenevV-20210218.pdf) |
| 2021-01-28 06:30–07:30 | Robinhood 決定限制 GME 等股票只能賣不能買 | 同上 |
| 2021-01-28 09:00 後 | NSCC 先把 ECP 減半，後當日全額豁免；淨需求降為約 14 億，Robinhood 再存入 7.37 億 | 同上 p.9–10；[SEC 員工報告 p.31](https://www.sec.gov/files/staff-report-equity-options-market-struction-conditions-early-2021.pdf) |
| 2021-01-28 | 盤中高 483.00 美元；收 193.60 美元 | [SEC 員工報告 p.18](https://www.sec.gov/files/staff-report-equity-options-market-struction-conditions-early-2021.pdf)；[FXStreet](https://www.fxstreet.com/amp/news/gamestop-gme-stock-price-and-forecast-gme-what-is-happening-now-202101291133) |
| 2021-02 初 | Robinhood 約四天內取得約 34 億美元新資金承諾 | [Tenev 國會證詞 p.10](https://democrats-financialservices.house.gov/UploadedFiles/HHRG-117-BA00-Wstate-TenevV-20210218.pdf) |
| 2021-02-04 | 收 53.50 美元 | [TDmonthly](https://www.toydirectory.com/monthly/print-article.asp?id=6032) |
| 2021-10-14 | SEC 發布《2021 年初股票與選擇權市場結構狀況》員工報告 | [SEC](https://www.sec.gov/files/staff-report-equity-options-market-struction-conditions-early-2021.pdf) |
| 2024-05-28 | 美股結算週期由 T+2 改為 T+1（SEC 2023-02-15 通過） | [Morrison Foerster](https://www.mofo.com/resources/insights/230224-new-sec-rules-and-amendments) |

## 2. 機制

- **制度設計（結算）**：T+2 期間，結算所承擔「買方付不出錢、賣方交不出股」的風險，所以向會員券商收保證金。NSCC 的 VaR 會隨個股波動放大，而且當 VaR 超過券商的超額淨資本時，再加收 ECP 附加費。Robinhood 在 01-28 正好踩到這條線（[Tenev 證詞](https://democrats-financialservices.house.gov/UploadedFiles/HHRG-117-BA00-Wstate-TenevV-20210218.pdf)）。
- **制度設計（券商模式）**：零手續費券商靠把訂單賣給造市商（PFOF）賺錢，資本相對交易量很薄。GME 選擇權的個人帳戶中，Robinhood、TD Ameritrade、E*Trade 三家就佔超過 66%（[SEC 員工報告 p.43](https://www.sec.gov/files/staff-report-equity-options-market-struction-conditions-early-2021.pdf)）。
- **人性**：社群媒體協同 + 高放空比例的軋空敘事。但 SEC 的資料顯示，真正撐住漲勢的是「正向情緒」，不是空方回補（見第 3 節）。

## 3. 關鍵數字

| 指標 | 數值 | 來源 |
|---|---|---|
| 放空 / 流通在外股數高點 | 109.26%（2020-12-31） | [SEC 員工報告 p.25](https://www.sec.gov/files/staff-report-equity-options-market-struction-conditions-early-2021.pdf) |
| 01-27 NSCC 全體追繳 | 69 億美元（36 家會員） | 同上 p.31 |
| Robinhood 01-28 應繳 / 缺口 | 約 37 億 / 約 30 億美元 | [Tenev 證詞 p.9](https://democrats-financialservices.house.gov/UploadedFiles/HHRG-117-BA00-Wstate-TenevV-20210218.pdf) |
| Robinhood 每日 VaR 需求 | 01-25 開盤 1.25 億 → 01-28 14 億美元（約 10 倍） | 同上 p.10 |
| 個人帳戶 GME 選擇權成交額 | 01-21 5,850 萬 → 01-27 24 億美元 | [SEC 員工報告 p.29](https://www.sec.gov/files/staff-report-equity-options-market-struction-conditions-early-2021.pdf) |
| 個人帳戶佔非造市商選擇權量 | 1 月中高點 91%，1 月底降到 56% | 同上 p.43 |

**SEC 報告的兩段原文（p.26、p.29）**：

- 空方回補：「such buying was a small fraction of overall buy volume … it was the positive sentiment, not the buying-to-cover, that sustained the weeks-long price appreciation」（回補買進只佔整體買量一小部分……撐住數週漲勢的是正向情緒，不是回補）。
- Gamma squeeze：「staff did not find evidence of a gamma squeeze in GME during January 2021」。理由是個人帳戶選擇權量的增加「mostly driven by an increase in the buying of put, rather than call, options」，而且「market-makers were buying, rather than writing, call options」，報告的結論是這些觀察「by themselves are not consistent with a gamma squeeze」。

## 4. 我的解讀（草稿，待討論）

1. **真正的熔斷機制在結算層，不在交易所。** 交易所沒有停止交易，是 NSCC 的保證金公式把帳單寄給資本最薄的散戶券商，券商只能把需求切掉。對 prop desk 來說，散戶擁擠交易的「頂部」不一定由價格決定，可能由「主要散戶券商的資本 / 結算保證金比」決定。值得追蹤的是：哪家券商的散戶流量集中、它的淨資本有多少。
2. **軋空敘事要先看資料再相信。** 放空比例超過 100% 是真的，但 SEC 看到回補只佔買量一小部分，也沒找到 gamma squeeze。很多「軋空」其實是需求衝擊，空方只是被拖著走。這對案例 9（白銀）是直接的對照：連放空燃料都沒有的時候，軋空敘事就只剩需求衝擊。
3. **T+1 縮小了接縫但沒有關掉。** 結算期間縮短一天，保證金需求下降，但「零手續費散戶流量集中在少數薄資本券商」這一半沒有改變。按接縫理論，只動了結算規則的一半，下一次擁擠交易的停止點仍可能出在結算保證金。

## 5. 限制與未證實

- 原手冊寫「1/28 凌晨 3:00 NSCC 提出約 30 億美元，起初 37 億，5:30 降至 7 億……9:11 降至 14 億但仍短缺 7 億」：時間與數字都不對。依 Tenev 國會書面證詞：**05:11** 通知總額約 37 億（缺口約 30 億）；NSCC 先把 ECP 減半，**09:00 後**全額豁免 ECP，淨需求約 14 億；Robinhood 已存 6.96 億、再存 7.37 億即足額。「Robinhood 僅有 7 億可用」是把「已存在 NSCC 的 6.96 億」誤讀。
- 原手冊寫「SEC 認為無證據支持 gamma squeeze」：方向正確但措辭要精確。這是 SEC **員工**報告（不代表委員會），原文是「staff did not find evidence of a gamma squeeze」，並說這些觀察「本身」與 gamma squeeze 不一致。
- 原手冊寫「三分之二經 Robinhood/ETrade/TD Ameritrade」：SEC 原文是「三家佔交易 GME 選擇權的**個人帳戶數**超過 66%」，是帳戶數，不是成交量。
- 原手冊寫「1/28 盤中高點 483.41」：SEC 報告寫 483.00 美元。原手冊寫「1/12–1/27 漲近 1,800%」：SEC 報告寫 01-27 收盤較 01-11 收盤漲逾 1,600%。
- 原手冊寫「推動 T+1 結算（2024/3/31 實施）」：實際實施日為 **2024-05-28**。
- 原手冊引「哥倫比亞大學學術委員會」對 SEC gamma 分析的批評：沒有找到這份文件，本文刪除。
- 01-28 與 02-04 收盤價來自媒體與價格表彙整，未對交易所官方收盤資料。

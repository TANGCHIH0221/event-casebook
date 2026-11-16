# 案例 15：KOSPI 2026-07 槓桿清算與 7/31 史上最大單日反彈（2026-07-27 ～ 07-31）

> **一句話**：KOSPI 有一半以上市值壓在三星與 SK 海力士兩檔，上面疊了散戶槓桿 ETF 與融資；記憶體題材一轉弱，三天連跌、史上首次連兩日熔斷，月中最深跌 34%；去槓桿一結束，7/31 單日漲 17.91%。

| 項目 | 內容 |
|---|---|
| 接縫 | 指數高度集中在兩檔記憶體股（市場自然結果）＋ 這兩檔上有每日再平衡的 2 倍槓桿 ETF 與散戶融資（案例 5 的政策產物）→ 同一個基本面消息同時打到指數、槓桿商品與保證金 |
| 強制流來源 | 槓桿 ETF 收盤再平衡（跌時賣）、融資斷頭、外資去槓桿；7/30 一檔大型 AI 對沖基金把公開股票部位整包賣給 Citadel |
| 量級 | 7/28 外資淨賣 4.98 兆韓元；7/31 外資淨買約 7.2 兆、散戶淨賣 8.25 兆；個股槓桿商品成交值 7/30 約 12.4 兆韓元 |
| 不看價格的一方 | 被追繳的融資戶、槓桿 ETF 再平衡、被券商要求降槓桿的基金 |
| 天然對手方 | 7/29 起逢低承接的外資與機構；7/30 承接 Situational Awareness 部位的 Citadel |
| 規則風險 | 已發生：7/31 個股槓桿預託金 3,000 萬韓元現金、業者把再平衡移出收盤競價（見案例 5） |
| 查證狀態 | ✅ 指數與個股數字已對兩個以上韓國媒體；⚠️ 各事件對 7/31 反彈的因果貢獻沒有可靠拆解 |

---

## 1. 發生了什麼

| 日期 | 事件 | 來源 |
|---|---|---|
| 2026-06-30 | KOSPI 收 8,476.48（7 月計算基準） | [Money Today](https://www.mt.co.kr/index.php/en/stock/2026/08/03/2026080311181646960) |
| 2026-07-27 | 中國長鑫存儲（CXMT）上海上市，募資約 US$86 億，首日漲約 466% | [TechNode](https://technode.com/2026/07/27/cxmt-becomes-chinas-most-valuable-a-share-company-after-8-6-billion-ipo/)；[BNN Bloomberg](https://www.bnnbloomberg.ca/business/technology/2026/07/27/china-memory-chipmaker-cxmts-shares-soar-in-a-blockbuster-share-listing-in-shanghai/) |
| 2026-07-28 | KOSPI 收 6,023.63（−10.84%），10:14 熔斷停止交易 20 分鐘；SK 海力士 −14.65%、三星 −13.39%；外資淨賣 4.98 兆韓元。分析師歸因於費城半導體指數下跌與 CXMT 上市引發的記憶體競爭疑慮 | [Korea Times](https://koreatimes.co.kr/economy/20260728/black-tuesday-seoul-stocks-crash-over-10-as-chip-rout-deepens)；[Edaily](https://en.edaily.co.kr/news/eda202607285659/) |
| 2026-07-29 | SK 海力士財報獲利成長但低於預期，股價盤中跌近 20%；KOSPI 12:32 再度熔斷，史上首次連兩日熔斷，收 5,663.24（−5.98%）；財政部長為引進個股槓桿 ETF 道歉 | [Korea Herald](https://www.koreaherald.com/article/10824514)；[Khaleej Times](https://www.khaleejtimes.com/business/markets/south-korea-2-trillion-stock-rout-breaks-records-as-sk-hynix-results-disappoint) |
| 2026-07-30 | KOSPI 收 5,593.56，較 6/30 跌 34.0%。Reuters 報導 AI 主題對沖基金 Situational Awareness（Leopold Aschenbrenner）把大部分公開股票部位賣給 Citadel；WSJ 引該基金致投資人信，7 月至當時約 −67% | [Money Today](https://www.mt.co.kr/index.php/en/stock/2026/08/03/2026080311181646960)；[Reuters via Yahoo](https://finance.yahoo.com/markets/stocks/articles/citadel-buys-most-situationals-stock-180422112.html) |
| 2026-07-31 | KOSPI 收 6,595.45，+1,001.89 點（+17.91%），點數與幅度皆史上最大（前紀錄 2008-10-30 +11.95%）；9:06 買方 sidecar；三星 +26.81%、SK 海力士 +29.95%（觸及 30% 漲停，史上首次）；外資淨買約 7.2 兆、散戶淨賣 8.25 兆韓元。同日個股槓桿新預託金門檻施行 | [Korea Times](https://koreatimes.co.kr/economy/20260731/kospi-rockets-18-in-record-breaking-rally)；[亞洲經濟](https://view.asiae.co.kr/en/article/2026073115513003224) |
| 2026-07-31 | 台股加權收 43,119.75，+3,186.45 點（+7.98%），單日點數史上最大；台積電漲停 | [中央社 Focus Taiwan](https://focustaiwan.tw/business/202607310012) |
| 2026-08-21 | Ken Griffin 表示 Citadel 已透過逾 40 億美元大宗交易，出清承接自 Situational Awareness 的八成以上風險 | [CNBC](https://www.cnbc.com/2026/08/21/citadel-situational-awareness-ken-griffin.html) |

## 2. 機制

- **制度／產品設計**：三星＋海力士佔 KOSPI 市值由 2025 年底 36.1% 升到 55.3%（2026-07 初報導時），成交值佔 63.5%（[nocutnews 引韓國銀行](https://nocutnews.co.kr/news/6543245)）。兩檔股票上有 2 倍個股槓桿 ETF，跌時要在收盤賣（案例 5）。指數、槓桿商品與融資部位全部綁在同一個風險因子上。
- **人性／誘因**：散戶用借來的錢加碼，券商強制平倉放大賣壓（[Khaleej Times](https://www.khaleejtimes.com/business/markets/south-korea-2-trillion-stock-rout-breaks-records-as-sk-hynix-results-disappoint)）。法國興業銀行的評論是「這顯然是一個非常擁擠的交易正在被平倉」。
- **反轉**：7/31 的報導把反彈歸因於美國半導體反彈、微軟與亞馬遜雲端業績優於預期、外資大買，以及 JPMorgan 認為槓桿 ETF 去槓桿實質上已完成（[Korea Times](https://koreatimes.co.kr/economy/20260731/kospi-rockets-18-in-record-breaking-rally)）。

## 3. 關鍵數字

| 指標 | 數值 | 來源 |
|---|---|---|
| KOSPI 7 月月跌幅 | −22.2%（8,476.48 → 6,595.45） | [Money Today](https://www.mt.co.kr/index.php/en/stock/2026/08/03/2026080311181646960) |
| KOSPI 7 月月中最深跌幅 | −34.0%（6/30 → 7/30 收盤 5,593.56） | 同上 |
| 7/28 跌幅 | −10.84%，收 6,023.63 | [Korea Times](https://koreatimes.co.kr/economy/20260728/black-tuesday-seoul-stocks-crash-over-10-as-chip-rout-deepens) |
| 7/29 跌幅 | −5.98%，收 5,663.24；盤中最深約 −12.6% | [Korea Herald](https://www.koreaherald.com/article/10824514)；[Khaleej Times](https://www.khaleejtimes.com/business/markets/south-korea-2-trillion-stock-rout-breaks-records-as-sk-hynix-results-disappoint) |
| 7/31 漲幅 | +17.91%，+1,001.89 點，收 6,595.45 | [Korea Times](https://koreatimes.co.kr/economy/20260731/kospi-rockets-18-in-record-breaking-rally) |
| 7/31 前三個交易日 | SK 海力士 −29.9%、三星 −19.34% | 同上 |
| 7/31 個股 | 三星 +26.81%（262,500 韓元）、SK 海力士 +29.95%（1,718,000 韓元） | 同上 |
| 7/31 法人 | 外資淨買約 7.18–7.24 兆、機構約 1.18 兆、散戶淨賣約 8.25 兆韓元 | 同上；[亞洲經濟](https://view.asiae.co.kr/en/article/2026073115513003224) |
| Situational Awareness | 7 月至 7/30 約 −67%（WSJ 引致投資人信）；交易後保留約 100 億美元（含 Anthropic 持股） | [Reuters via Yahoo](https://finance.yahoo.com/markets/stocks/articles/citadel-buys-most-situationals-stock-180422112.html) |
| 台股 7/31 | +7.98%，收 43,119.75 | [Focus Taiwan](https://focustaiwan.tw/business/202607310012) |

## 4. 我的解讀（草稿，待討論）

1. **接縫在「集中度」：一個因子、三種槓桿。** 兩檔股票佔指數過半市值、六成以上成交，上面同時有個股 2 倍 ETF、散戶融資、海外 AI 主題基金的槓桿多單。記憶體題材一轉弱，三種槓桿在同一天被逼平倉。這是案例 5 的延伸：政策開了個股槓桿，但真正的風險來自標的本身已經是整個指數。
2. **去槓桿型崩盤的底部，看「被迫賣的人賣完沒」，不看基本面。** 7/31 的反彈沒有新的韓國基本面消息；分析師說的是「去槓桿實質完成」、Situational Awareness 部位已由 Citadel 承接、散戶在新門檻施行當天淨賣 8.25 兆。這跟案例 14 的日經 8/6 反彈同型：被迫賣方清空後，價格回彈很快。對 prop desk 而言，可以觀測的清空訊號包括槓桿 ETF 成交值驟降、融資餘額與斷頭量、大型部位被整包移轉的報導。
3. **監管的時間戳本身就是事件。** 預託金新規在 7/31 施行，剛好也是反彈日。新規讓散戶不能再加碼個股槓桿，等於在底部關掉最後一批潛在賣方的再進場來源；但這是推論，資料上無法區分新規的效果與美股科技股反彈的效果。
4. **台股同日 +7.98% 不代表台股有同一個接縫。** 台股當天主要由台積電漲停帶動，台灣沒有個股 2 倍槓桿 ETF。比較合理的讀法是區域 AI／半導體因子的同步，而不是同一種強制流；要驗證需比較兩地融資與槓桿商品的變化。

## 5. 限制與未證實

- **原手冊寫「Leopold Aschenbrenner 的 AI 對沖基金 7 月虧 67% 並把部位賣給 Citadel」**：**查到可靠來源，予以保留但修正**。Reuters（2026-07-30）報導 Situational Awareness 把大部分公開股票部位賣給 Citadel；−67% 是 WSJ 引該基金致投資人信、「7 月至當時」的數字。另有 Calcalist 把 −67% 說成約 160 億美元公開股票組合的跌幅、Quartz／CNBC 說資產減少約 350 億美元，口徑不一，本文不採用金額。Reuters 列出的持股是 Broadcom、Intel、CoreWeave；Quartz 稱 Citadel 承接的部位包括 SK 海力士，未在 Reuters 原文看到，屬單一來源。**原手冊把它寫成 7/31 反彈的「催化劑」：沒有來源支持這個因果關係**，7/31 的韓國報導都沒提到這件事。
- **原手冊寫「台股 7/31 +7.98%」**：查證正確（[Focus Taiwan](https://focustaiwan.tw/business/202607310012)），保留。
- **原手冊寫「三星 +19.57%、SK 海力士 +24.05%（17 年來首次漲停）」**：錯誤。實際為三星 +26.81%、SK 海力士 +29.95%，且報導稱 SK 海力士漲停是「史上首次」。
- **原手冊寫「微軟財報超預期」為催化劑**：報導寫的是微軟與亞馬遜的雲端業績優於預期，緩解晶片需求疑慮；不是單獨微軟。
- **原手冊寫「7/28 史上第四大單日跌幅」**：未查到來源，刪除。
- **原手冊寫「7/28 熔斷為 2026 年第 8 次」**：Edaily 內文同時寫「今年第 8 次」與標題「今年第 3 次」，互相矛盾；Korea Times 只說當天 sidecar 是今年第 22 次。刪除。
- **原手冊寫「KOSPI 7 月為史上最差月份（跌逾 30–35%，超越 1997、2008）」**：只在月中成立（7/30 收盤較 6/30 −34.0%）。以月底收盤計 7 月為 −22.2%（[Money Today](https://www.mt.co.kr/index.php/en/stock/2026/08/03/2026080311181646960)），是否為史上最大月跌幅沒有查到官方說法；1997、2008 的月跌幅比較未查證，刪除「超越 1997、2008」。
- **原手冊寫「三日跌 17.20%」**：依 7/28 收盤與跌幅反推的 7/27 收盤，到 7/30 收盤約 −17.2%，算術上一致，但沒有直接來源，本文改用 Korea Times 的個股三日跌幅。
- **原手冊寫「DUV 微影本土化」為下跌原因**：未查到同期報導把它列為原因，刪除。
- **原手冊寫「外資淨買 7 兆韓元」**：各來源為 7.18、7.22、7.24 兆，寫成約 7.2 兆。
- 7/29 盤中最低點各來源不同（5,262.77 為單一來源），未採用。

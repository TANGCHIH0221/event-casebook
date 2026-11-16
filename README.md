# 事件交易案例集（2021–2026）：規則的接縫與強制流

> 我想做事件交易：找出**事前可以預期、而且大到會推動價格**的交易。這類交易幾乎都不是誰比較會看盤，而是**規則逼某些人在某個時間、不看價格地買賣**。
>
> 這個 repo 整理了 32 個 2021–2026 年的全球與台灣案例。每個案例都回答同一組問題：哪兩套規則疊出了不對稱、誰被迫交易、量多大、誰在對面接、規則會不會改。台灣的案例我用公開資料自己重算，國際案例逐條查證來源。原始手冊有不少錯誤，每案第 5 節都有勘誤。

**狀態**：32 案完成查證與改寫（持續更新）。台灣案例 8 個有自己的資料分析與圖。
**資料**：FinMind（證交所／櫃買日 K、三大法人、匯率、美股）、證交所與櫃買中心處置公告、各案一手來源（法院判決、監管命令、公司申報）
**工具**：Python / pandas / matplotlib

---

## 我從 32 個案例看到的五件事

| | 發現 | 代表案例 |
|---|---|---|
| 1 | **公開的強制流，價格在「公告」時就反映，不在「執行」時。** 執行那天常常是反轉點。 | 00940 建倉期投信佔成交量 15%，成分股卻跑輸大盤（[6](cases/06_00940.md)）；GBTC（[4](cases/04_gbtc_discount.md)） |
| 2 | **規則訂出「確定的日期」，市場就會搶在那天之前。** | 處置舊制出關前 2 天 +270 bp（[19](cases/19_disposition_reform_2026.md)）；環球晶的審查期限（[23](cases/23_globalwafers_siltronic.md)）；國安基金（[18](cases/18_national_stabilization_fund.md)） |
| 3 | **最後的對手方是規則制定者。** 交易所、監管、法院可以在事後改變結果。 | LME 取消交易（[16](cases/16_lme_nickel.md)）、FINMA 清零 AT1（[25](cases/25_cs_at1.md)）、NSCC 保證金停掉 GME 買盤（[8](cases/08_gamestop.md)） |
| 4 | **監管動「門檻」不會關掉接縫，只會換掉參與者；動「結構或時點」才會。** | 處置新制把出關前急拉攤平（[19](cases/19_disposition_reform_2026.md)）；韓國把再平衡移出收盤競價（[5](cases/05_korea_single_stock_leverage_etf.md)）；印度關一個交易所、流量換到另一個（[1](cases/01_jane_street_india.md)） |
| 5 | **強制去槓桿的報酬在「接住」，不在放空。** 賣壓的時點算不準，但賣壓結束後的反彈很一致。 | 國安基金進場後 5 天 9/9 正報酬（[18](cases/18_national_stabilization_fund.md)）；日圓套利平倉（[14](cases/14_yen_carry_unwind_2024.md)）；KOSPI 7/31 +17.9%（[15](cases/15_kospi_deleveraging_2026_07.md)） |

---

## 框架：接縫理論

每個案例都可以拆成同一條因果鏈：

```
制度設計 → 產生「可預測的機械性流量」或「便宜的價格槓桿點」
        → 有能力、有動機的人利用它（機構），或被它吃掉（散戶）
        → 成本由看不到帳單的人承擔
        → 監管事後反應 → 流量遷移到下一個接縫
```

**接縫**指的是兩套各自合理的規則疊在一起產生的不對稱。不是單一規則有漏洞，例如：

- **印度**：選擇權用現貨收盤價結算（合理）＋現貨市場比選擇權名目小數百倍（市場自然形成）→ 推動現貨很便宜，選擇權的賠率很大。
- **台灣**：清算按淨值計算（合理）＋次級市場按市價交易（合理）→ 溢價在清算日一定歸零（[00677U](cases/07_fubon_vix_00677u.md)）。
- **台積電 ADR**：ADR 可在美國自由交易＋台股轉 ADR 要核准 → 溢價只能往一邊偏（[31](cases/31_tsmc_adr_premium.md)）。

**對 prop desk 的意義**：找接縫比找訊號持久。接縫要修法才會消失，而修法有明確的生效日，可以直接當成 regime break 檢驗（例如[處置新制](cases/19_disposition_reform_2026.md)）。

每個案例開頭都有一張摘要表：

| 欄位 | 問的問題 |
|---|---|
| 接縫 | 哪兩套規則疊出了不對稱？ |
| 強制流來源 | 誰被迫交易？依據哪條規則或契約？ |
| 量級 | 多大？佔成交量多少？ |
| 不看價格的一方 | 誰必須成交，不管價格？ |
| 天然對手方 | 誰在對面接？ |
| 規則風險 | 監管、交易所、法院會不會改規則？ |
| 查證狀態 | 哪些數字對過一手來源，哪些沒有？ |

---

## 我自己量化過的強制流

案例集是「別人的事件」。下面三個 repo 是我挑出台灣本地的強制流，從資料開始做完整的檢驗：

| Repo | 強制流 | 結論 |
|---|---|---|
| [settlement-flow](https://github.com/TANGCHIH0221/settlement-flow) | 股票期貨結算日，到期部位被迫在現貨端平倉 | 估得出對手部位、成交量證據成立；扣成本後中小型股仍有 edge，大型股沒有 |
| [tx-etf-rebalance](https://github.com/TANGCHIH0221/tx-etf-rebalance) | 槓桿／反向 ETF 每日收盤前的台指期再平衡 | 機制成立（五項證據）；edge 隨再平衡量與波動放大，利潤集中在少數幾天 |
| [sitc-flow](https://github.com/TANGCHIH0221/sitc-flow) | 投信大買／大賣對個股的衝擊 | 投信大買日盤中超額 +90 bp、七年都成立；但能事前猜到的那部分價格上沒有肉 |

這三個研究跟本集的關係：[案例 5](cases/05_korea_single_stock_leverage_etf.md)（韓國槓桿 ETF 再平衡）是 tx-etf-rebalance 的韓國版；[案例 6](cases/06_00940.md)（00940 建倉）是 sitc-flow 的極端事件；[案例 1](cases/01_jane_street_india.md)（Jane Street 結算日）跟 settlement-flow 是同一種接縫（衍生品以現貨收盤價結算）。

---

## 案例索引

★ = 有自己的資料分析與圖（`scripts/` 可重跑）

### 一、結算與到期日
| # | 案例 | 一句話 |
|---|---|---|
| 1 | [Jane Street 印度 Bank Nifty](cases/01_jane_street_india.md) | 選擇權用現貨收盤價結算、名目是現貨數百倍；SEBI 初步認定用「單獨看會虧」的現貨推指數 |

### 二、指數與 ETF 強制流
| # | 案例 | 一句話 |
|---|---|---|
| 2 | [Super Micro 納入 S&P 500](cases/02_smci_sp500.md) | 被動資金在高點被迫買；真正落地的被動賣出是 Nasdaq-100 剔除 |
| 3 | [MicroStrategy 與 mNAV](cases/03_mstr_nasdaq100.md) | 指數只看市值；mNAV 跌破 1 時，發股買幣的飛輪變成稀釋器 |
| 4 | [GBTC 折價收斂](cases/04_gbtc_discount.md) | 封閉式信託折價近 50%，轉 ETF 後歸零；接著破產遺產贖回逾 200 億美元 |
| 5 | [韓國個股槓桿 ETF](cases/05_korea_single_stock_leverage_etf.md) | 為留住散戶而核准；收盤再平衡變成可預測流量，崩盤後被移出收盤競價 |
| 6 ★ | [00940 募集與建倉](cases/06_00940.md) | 成分股漲在募集前；建倉 10 天投信佔量 15%，成分股反而跑輸 |
| 7 ★ | [期富邦 VIX 清算](cases/07_fubon_vix_00677u.md) | 清算按淨值、交易按市價；監管說不救，兩天爆量 154 萬張 |

### 三、軋空與處置
| # | 案例 | 一句話 |
|---|---|---|
| 8 | [GameStop](cases/08_gamestop.md) | 讓漲勢停下的是結算所保證金，不是空方 |
| 9 | [白銀軋空失敗](cases/09_silver_squeeze_2021.md) | 投機部位本來淨多、SLV 可申購、CME 調保證金，兩天吐回 |
| 10 ★ | [航運三雄與處置](cases/10_shipping_2021.md) | 長榮第一次處置 10 天又漲 52%；處置的位置決定是續漲還是頂部 |
| 11 ★ | [緯創 2023](cases/11_wistron_2023.md) | 漲幅集中在出關前 6 天，出關後 20 天 −28% |

### 四、強制去槓桿與傳染
| # | 案例 | 一句話 |
|---|---|---|
| 12 | [Archegos](cases/12_archegos.md) | 強制賣方之間也有排序，先賣的全身而退 |
| 13 | [FTX 債權](cases/13_ftx_claims.md) | 債權從 3 美分漲到超過面額，賺到的是有法務能力的人 |
| 14 | [日圓套利平倉 2024-08](cases/14_yen_carry_unwind_2024.md) | 日經單日 −12.4%，日銀說不升息後隔天反彈 |
| 15 | [KOSPI 2026-07](cases/15_kospi_deleveraging_2026_07.md) | 史上首次連兩日熔斷，去槓桿結束後單日 +17.9% |

### 五、交易所與監管規則
| # | 案例 | 一句話 |
|---|---|---|
| 16 | [LME 鎳](cases/16_lme_nickel.md) | 交易所直接取消已成交的單，法院認定合法 |
| 17 | [SVB](cases/17_svb.md) | HTM 會計藏住虧損、94% 存款無保險；週末宣布全額保障 |
| 18 ★ | [國安基金](cases/18_national_stabilization_fund.md) | 9 次進場持有 5 天全賺（平均 +6.1%），對照組 −0.2%；超過 20 天沒差 |
| 19 ★ | [處置新制 2026-08](cases/19_disposition_reform_2026.md) | 出關前 2 天急拉從 +270 bp 降到 +45 bp（t = 3.7） |

### 六、併購與監管套利
| # | 案例 | 一句話 |
|---|---|---|
| 20 | [Twitter–Musk](cases/20_twitter_musk.md) | 強制履約條款 + 法院排期，讓價差在開庭前收斂 |
| 21 | [微軟–動視暴雪](cases/21_msft_activision.md) | 兩個監管機關各自的准駁日，就是價差跳動的日子 |
| 22 | [新日鐵–美國鋼鐵](cases/22_nippon_steel_us_steel.md) | 價差定價的不是反托拉斯，是誰坐在白宮 |
| 23 | [環球晶–Siltronic](cases/23_globalwafers_siltronic.md) | 監管不必說不，只要在期限前不核准 |
| 24 | [台新新光 vs 中信金](cases/24_taishin_shinkong_ctbc.md) | 競購由監管的准駁時鐘決定，不是價格 |

### 七、法律文件與資本結構
| # | 案例 | 一句話 |
|---|---|---|
| 25 | [瑞信 AT1 清零](cases/25_cs_at1.md) | 債券清零、股東拿到股票；一審判違法，仍在上訴 |
| 26 | [AMC–APE](cases/26_amc_ape.md) | 經濟上相同卻半價交易，收斂取決於法院 |

### 八、政策與地緣
| # | 案例 | 一句話 |
|---|---|---|
| 27 | [解放日關稅 2025-04](cases/27_liberation_day_tariffs.md) | 讓川普暫停的是美債；台股連假後一次吸收兩天跌幅 |
| 28 | [美伊與荷莫茲 2026](cases/28_us_iran_hormuz_2026.md) | 期貨與實貨價差拉大，關鍵在實貨 |
| 29 | [東證 PBR 改革](cases/29_tse_pbr_reform.md) | 沒有罰則的揭露要求，讓庫藏股倍增 |

### 九、資訊事件與跨市場
| # | 案例 | 一句話 |
|---|---|---|
| 30 | [Hindenburg–Adani](cases/30_hindenburg_adani.md) | 放空報告透過 MSCI 自由流通量調整，變成固定日期的被動賣壓 |
| 31 ★ | [台積電 ADR 溢價](cases/31_tsmc_adr_premium.md) | 水位由制度決定；偏離 60 日均值後一個月內回歸 |
| 32 | [Porsche IPO 與控股折價](cases/32_porsche_ipo_holdco_discount.md) | 上市 81 天快速納入 DAX、三年後被剔除，股價較 IPO 價 −45%；母公司 Porsche SE 長期折價 35–39% |

---

## 怎麼查證

- 每個數字都附來源。優先順序：監管命令、法院判決、交易所公告 > 公司申報 > 深度財經媒體 > 其他。
- 查不到就不寫，或標「未證實」。不拿常識補數字。
- 原始手冊的錯誤寫在每案第 5 節「原手冊勘誤」。最常見的錯誤類型：日期錯月或錯年（00677U 把 1 月寫成 4 月、國安基金出清年份錯一年）、把預估或試算當成實際數字（LME 保證金）、把兩方加總當成一方（LME 求償金額）、因果寫反（SVB 增資與擠兌）。
- 每案第 4 節「我的解讀」是我的觀點，標為草稿，跟事實分開。

## 重跑

```bash
# 需要 FinMind token：環境變數 FINMIND_TOKEN 或 ~/quant/.env
python3 scripts/case06_00940.py
python3 scripts/case18_stabilization_fund.py
python3 scripts/case31_tsm_adr.py
python3 scripts/case10_11_disposition.py      # 需要本機處置資料（見腳本說明）
python3 scripts/case19_fetch_disposition.py && python3 scripts/case19_disposition_reform.py
```

`scripts/finmind.py` 會把抓過的資料快取在 `data/`。

## 免責聲明

本 repo 只供研究與學習，不構成投資建議。案例 1、25 等仍在法律程序中，引用的監管認定為初步或非終局。

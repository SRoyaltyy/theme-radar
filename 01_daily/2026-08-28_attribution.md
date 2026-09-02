# Factor attribution — signal 2026-08-28 → prediction day 2026-09-02

## Trade window (read this first)

| Role | Date | Meaning |
|------|------|---------|
| **Signal as-of** | **2026-08-28** | Features/scores formed from this snapshot (and deltas vs **2026-08-26**). Only data on/before this date. |
| **Prediction day** | **2026-09-02** | The trading day the forward return is for (exit snapshot). |
| **Entry price** | Price @ 2026-08-28 | Long: buy here; short: sell here. |
| **Exit price** | Price @ 2026-09-02 | Close proxy on prediction day. |
| **Return column** | `fwd_3d` | Long: exit/entry − 1; short = opposite. |

Graded **n=11608** names with valid entry and exit prices.

Provisional until multiple signal dates agree.

_Column guide: **IC** = Spearman(feature, long forward return); **IC↑** / **IC↓** = IC among names that went up / down._

## Score calibration (long fwd)
- Spearman IC(total_score, fwd_3d) = **0.0108**

| Quintile | Mean long fwd | Hit up>1.5% | n |
|---|---|---|---|
| 1 | 14.94% | 19.1% | 2345 |
| 2 | 1.34% | 16.1% | 2408 |
| 3 | -0.17% | 7.8% | 2589 |
| 4 | -0.81% | 7.8% | 1945 |
| 5 | -1.03% | 22.0% | 2321 |

## Top |IC| features

| Feature | IC | IC↑ | IC↓ | Mean fwd when + | Mean fwd when − | n+/n− |
|---|---|---|---|---|---|---|
| Relative Strength Index (14) | +0.1320 | -0.1152 | +0.1963 | 2.97% | n/a | 11472/0 |
| d_Performance (Quarter) | +0.1320 | -0.0076 | +0.1903 | 2.60% | 3.49% | 3604/7240 |
| d_Volatility (Month) | +0.1047 | -0.0730 | +0.2486 | 15.09% | -0.11% | 2286/8292 |
| d_Forward P/E | +0.0902 | +0.0841 | +0.0317 | -0.50% | -0.93% | 1073/1872 |
| upside_pct_lvl | -0.0828 | +0.3029 | -0.3062 | 2.21% | 0.22% | 4309/334 |
| true_ret | +0.0718 | -0.0770 | +0.1811 | -0.48% | 5.05% | 4082/7075 |
| d_Price | +0.0665 | +0.0297 | +0.0858 | -0.48% | 5.05% | 4082/7075 |
| d_Performance (YTD) | +0.0641 | -0.0443 | +0.1536 | -0.39% | 5.00% | 4149/7124 |
| Short Float | -0.0600 | +0.1773 | -0.1597 | 6.00% | n/a | 5691/0 |
| d_Relative Volume | -0.0585 | -0.0128 | -0.0193 | 1.02% | 5.33% | 5872/5293 |
| d_20-Day Simple Moving Average | +0.0582 | -0.0931 | +0.1688 | -0.50% | 4.61% | 3716/7769 |
| Performance (Week) | +0.0558 | -0.1143 | +0.1865 | -0.55% | 5.64% | 4857/6517 |
| d_200-Day Simple Moving Average | +0.0427 | -0.0277 | +0.1227 | -0.49% | 4.86% | 4094/7386 |
| d_50-Day Simple Moving Average | +0.0353 | -0.0544 | +0.1286 | -0.53% | 4.93% | 4148/7335 |
| d_Beta | +0.0291 | +0.0360 | +0.0113 | 0.65% | 14.51% | 2050/2429 |
| d_Short Ratio | -0.0275 | +0.0334 | -0.0806 | -0.11% | 9.44% | 5162/2864 |
| d_Market Cap | +0.0252 | +0.0611 | -0.0422 | -0.13% | 10.32% | 2128/3617 |
| d_Sales Year Over Year TTM | +0.0241 | +0.0037 | -0.0092 | 0.11% | 2.95% | 44/34 |
| d_Institutional Ownership | -0.0233 | +0.0018 | -0.0013 | 19.84% | 3.06% | 630/624 |
| d_Analyst Recom | -0.0221 | -0.0305 | -0.0004 | -1.28% | -0.34% | 167/128 |
| Relative Volume | -0.0200 | +0.0778 | -0.0564 | 3.00% | n/a | 11312/0 |
| d_Gross Margin | -0.0183 | +0.0253 | -0.0433 | -0.92% | 4.63% | 51/29 |
| d_Performance (Month) | -0.0159 | -0.1177 | +0.0629 | -0.41% | 5.70% | 4956/6337 |
| d_Relative Strength Index (14) | +0.0153 | +0.0682 | -0.0435 | -0.45% | 4.89% | 4040/7323 |
| d_Average Volume | +0.0152 | -0.0424 | +0.0819 | 7.97% | 0.10% | 4198/7036 |

## Combinations

| Pattern | n | Mean long fwd | Hit up |
|---|---|---|---|
| true_ret>3% & DOWNTREND | 198 | 0.15% | 22.2% |
| true_ret>3% & UPTREND | 386 | -1.10% | 31.6% |
| true_ret>3% & MIXED | 186 | -1.79% | 29.6% |

## Risk dominance probes

| State | n | Mean long fwd | Mean fwd if score top quintile |
|---|---|---|---|
| EXTENDED | 271 | -1.85% | -4.25% |
| WASHED | 461 | 79.66% | -1.07% |

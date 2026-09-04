# Factor attribution — signal 2026-09-01 → prediction day 2026-09-04

## Trade window (read this first)

| Role | Date | Meaning |
|------|------|---------|
| **Signal as-of** | **2026-09-01** | Features/scores formed from this snapshot (and deltas vs **2026-08-31**). Only data on/before this date. |
| **Prediction day** | **2026-09-04** | The trading day the forward return is for (exit snapshot). |
| **Entry price** | Price @ 2026-09-01 | Long: buy here; short: sell here. |
| **Exit price** | Price @ 2026-09-04 | Close proxy on prediction day. |
| **Return column** | `fwd_3d` | Long: exit/entry − 1; short = opposite. |

Graded **n=11619** names with valid entry and exit prices.

Provisional until multiple signal dates agree.

_Column guide: **IC** = Spearman(feature, long forward return); **IC↑** / **IC↓** = IC among names that went up / down._

## Score calibration (long fwd)
- Spearman IC(total_score, fwd_3d) = **-0.2756**

| Quintile | Mean long fwd | Hit up>1.5% | n |
|---|---|---|---|
| 1 | 5.17% | 58.8% | 2559 |
| 2 | 2.70% | 54.8% | 2135 |
| 3 | 0.95% | 20.9% | 2369 |
| 4 | 0.89% | 25.6% | 2639 |
| 5 | 0.06% | 29.7% | 1917 |

## Top |IC| features

| Feature | IC | IC↑ | IC↓ | Mean fwd when + | Mean fwd when − | n+/n− |
|---|---|---|---|---|---|---|
| d_Performance (Month) | -0.3570 | -0.4871 | +0.0882 | -0.09% | 2.61% | 2182/9096 |
| d_200-Day Simple Moving Average | -0.3489 | -0.4088 | -0.0062 | 0.12% | 2.60% | 2453/9024 |
| d_Performance (YTD) | -0.3487 | -0.4057 | +0.0122 | 0.13% | 2.63% | 2369/8910 |
| d_Performance (Week) | -0.3311 | -0.4272 | +0.0226 | 0.04% | 2.62% | 2375/9053 |
| d_Price | -0.3246 | -0.2394 | -0.0593 | 0.13% | 2.65% | 2315/8849 |
| true_ret | -0.3198 | -0.4293 | +0.0592 | 0.13% | 2.65% | 2315/8849 |
| d_50-Day Simple Moving Average | -0.3012 | -0.3839 | +0.0229 | 0.32% | 2.54% | 2471/9041 |
| d_20-Day Simple Moving Average | -0.2883 | -0.3764 | +0.0375 | 0.38% | 2.55% | 2592/8908 |
| d_Performance (Quarter) | -0.2823 | -0.2765 | -0.0909 | 2.68% | 1.75% | 3097/7730 |
| Performance (Week) | -0.2518 | -0.3650 | +0.0777 | 0.82% | 2.41% | 2465/8980 |
| d_Market Cap | -0.2073 | -0.1212 | -0.0019 | 0.57% | 3.47% | 1693/4040 |
| d_Forward P/E | -0.1917 | -0.1723 | +0.0570 | 0.72% | 2.27% | 786/2165 |
| Short Float | +0.1459 | +0.2160 | -0.1638 | 2.63% | n/a | 5696/0 |
| d_Relative Strength Index (14) | -0.1275 | +0.1907 | -0.1237 | 0.12% | 2.64% | 2367/8852 |
| Relative Strength Index (14) | -0.0687 | -0.0245 | -0.0007 | 2.06% | n/a | 11501/0 |
| upside_pct_lvl | +0.0465 | +0.2450 | -0.3451 | 1.93% | 1.12% | 4353/297 |
| Performance (Month) | -0.0438 | -0.0693 | +0.0575 | 1.50% | 2.63% | 5638/5736 |
| d_Sales Year Over Year TTM | -0.0417 | -0.0247 | -0.0259 | -5.94% | 10.41% | 5/2 |
| d_Gross Margin | -0.0364 | +0.0013 | -0.0338 | -8.00% | 5.19% | 6/6 |
| d_Volatility (Month) | -0.0282 | -0.0130 | +0.0224 | 0.62% | -0.10% | 40/17 |
| d_Average Volume | -0.0267 | -0.0968 | +0.0417 | 3.04% | 1.50% | 4257/6777 |
| d_Short Float | +0.0265 | +0.0263 | +0.0021 | 2.55% | -0.30% | 27/30 |
| d_Sales Growth Quarter Over Quarter | -0.0240 | -0.0156 | -0.0013 | -4.98% | 7.49% | 4/4 |
| d_Short Ratio | +0.0225 | +0.0715 | -0.0187 | 1.66% | 1.90% | 4607/2486 |
| Institutional Transactions | +0.0212 | +0.0511 | -0.0704 | 3.93% | 1.38% | 3181/1858 |

## Combinations

| Pattern | n | Mean long fwd | Hit up |
|---|---|---|---|
| true_ret>3% & DOWNTREND | 158 | -2.68% | 29.7% |
| true_ret>3% & UPTREND | 188 | 1.23% | 36.7% |
| true_ret>3% & MIXED | 126 | -0.86% | 31.0% |

## Risk dominance probes

| State | n | Mean long fwd | Mean fwd if score top quintile |
|---|---|---|---|
| EXTENDED | 199 | 0.69% | -2.16% |
| WASHED | 851 | 1.48% | -1.79% |

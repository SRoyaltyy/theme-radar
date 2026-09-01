# Factor attribution — signal 2026-08-28 → prediction day 2026-08-31

## Trade window (read this first)

| Role | Date | Meaning |
|------|------|---------|
| **Signal as-of** | **2026-08-28** | Features/scores formed from this snapshot (and deltas vs **2026-08-26**). Only data on/before this date. |
| **Prediction day** | **2026-08-31** | The trading day the forward return is for (exit snapshot). |
| **Entry price** | Price @ 2026-08-28 | Long: buy here; short: sell here. |
| **Exit price** | Price @ 2026-08-31 | Close proxy on prediction day. |
| **Return column** | `fwd_1d` | Long: exit/entry − 1; short = opposite. |

Graded **n=11611** names with valid entry and exit prices.

Provisional until multiple signal dates agree.

_Column guide: **IC** = Spearman(feature, long forward return); **IC↑** / **IC↓** = IC among names that went up / down._

## Score calibration (long fwd)
- Spearman IC(total_score, fwd_1d) = **-0.0442**

| Quintile | Mean long fwd | Hit up>1.5% | n |
|---|---|---|---|
| 1 | 6.95% | 18.5% | 2346 |
| 2 | 1.73% | 11.3% | 2408 |
| 3 | 0.13% | 4.7% | 2590 |
| 4 | -0.27% | 4.7% | 1945 |
| 5 | -0.47% | 15.1% | 2322 |

## Top |IC| features

| Feature | IC | IC↑ | IC↓ | Mean fwd when + | Mean fwd when − | n+/n− |
|---|---|---|---|---|---|---|
| d_Beta | +0.1499 | +0.0876 | +0.1140 | 1.75% | 6.74% | 2051/2429 |
| d_Price | +0.1170 | -0.0365 | +0.1249 | 0.01% | 2.70% | 4083/7077 |
| Relative Strength Index (14) | +0.1166 | -0.1175 | +0.1940 | 1.68% | n/a | 11475/0 |
| Short Float | -0.1084 | +0.0974 | -0.1932 | 2.64% | n/a | 5693/0 |
| d_200-Day Simple Moving Average | +0.0987 | -0.0736 | +0.1677 | 0.05% | 2.58% | 4095/7388 |
| d_Performance (YTD) | +0.0956 | -0.0995 | +0.1875 | 0.03% | 2.68% | 4150/7126 |
| Performance (Month) | +0.0940 | +0.1143 | +0.0550 | 0.34% | 4.14% | 7301/4052 |
| d_Forward P/E | +0.0875 | +0.0404 | +0.0610 | -0.26% | -0.60% | 1074/1872 |
| d_50-Day Simple Moving Average | +0.0869 | -0.1034 | +0.1805 | 0.03% | 2.61% | 4149/7337 |
| d_Volatility (Month) | +0.0848 | -0.0751 | +0.2237 | 6.72% | 0.39% | 2287/8294 |
| true_ret | +0.0841 | -0.1291 | +0.2085 | 0.01% | 2.70% | 4083/7077 |
| d_Market Cap | +0.0802 | +0.0458 | -0.0151 | 0.05% | 5.06% | 2129/3618 |
| d_Performance (Month) | -0.0742 | -0.1230 | -0.0135 | 0.05% | 3.00% | 4957/6339 |
| d_EPS Surprise | -0.0417 | -0.0499 | +0.0053 | -1.10% | 0.95% | 38/32 |
| d_Relative Strength Index (14) | +0.0401 | +0.0266 | -0.0182 | -0.02% | 2.63% | 4041/7325 |
| Performance (Week) | +0.0384 | -0.1453 | +0.1808 | -0.09% | 3.02% | 4859/6518 |
| d_20-Day Simple Moving Average | +0.0378 | -0.1674 | +0.1653 | -0.09% | 2.52% | 3717/7771 |
| d_Gross Margin | -0.0363 | +0.0081 | -0.0384 | -0.72% | 1.35% | 51/29 |
| d_Performance (Quarter) | +0.0352 | -0.0393 | +0.0783 | -0.25% | 2.76% | 3605/7242 |
| d_Analyst Recom | -0.0339 | -0.0186 | -0.0280 | -0.82% | -0.30% | 167/128 |
| d_Performance (Week) | -0.0334 | -0.1831 | +0.0957 | -0.16% | 3.07% | 4899/6502 |
| d_Profit Margin | -0.0231 | -0.0324 | -0.0181 | -0.61% | 1.19% | 47/33 |
| d_Relative Volume | +0.0230 | -0.0382 | +0.0017 | 1.79% | 1.67% | 5873/5295 |
| d_Insider Transactions | +0.0206 | -0.0211 | +0.0127 | 0.78% | -0.61% | 326/299 |
| d_Institutional Ownership | -0.0192 | +0.0114 | -0.0248 | 3.92% | 4.09% | 630/624 |

## Combinations

| Pattern | n | Mean long fwd | Hit up |
|---|---|---|---|
| true_ret>3% & DOWNTREND | 198 | 2.44% | 19.7% |
| true_ret>3% & UPTREND | 387 | 0.31% | 26.4% |
| true_ret>3% & MIXED | 186 | -0.60% | 32.8% |

## Risk dominance probes

| State | n | Mean long fwd | Mean fwd if score top quintile |
|---|---|---|---|
| EXTENDED | 271 | 0.65% | 0.86% |
| WASHED | 461 | 38.17% | -1.02% |

# Factor attribution — signal 2026-09-29 → prediction day 2026-09-30

## Trade window (read this first)

| Role | Date | Meaning |
|------|------|---------|
| **Signal as-of** | **2026-09-29** | Features/scores formed from this snapshot (and deltas vs **2026-09-28**). Only data on/before this date. |
| **Prediction day** | **2026-09-30** | The trading day the forward return is for (exit snapshot). |
| **Entry price** | Price @ 2026-09-29 | Long: buy here; short: sell here. |
| **Exit price** | Price @ 2026-09-30 | Close proxy on prediction day. |
| **Return column** | `fwd_1d` | Long: exit/entry − 1; short = opposite. |

Graded **n=11673** names with valid entry and exit prices.

Provisional until multiple signal dates agree.

_Column guide: **IC** = Spearman(feature, long forward return); **IC↑** / **IC↓** = IC among names that went up / down._

## Score calibration (long fwd)
- Spearman IC(total_score, fwd_1d) = **-0.0367**

| Quintile | Mean long fwd | Hit up>1.5% | n |
|---|---|---|---|
| 1 | 0.20% | 12.0% | 2364 |
| 2 | -0.25% | 5.3% | 2529 |
| 3 | -0.41% | 5.6% | 2177 |
| 4 | -0.41% | 9.3% | 2298 |
| 5 | -0.05% | 16.4% | 2305 |

## Top |IC| features

| Feature | IC | IC↑ | IC↓ | Mean fwd when + | Mean fwd when − | n+/n− |
|---|---|---|---|---|---|---|
| d_Performance (Quarter) | -0.1076 | -0.0841 | -0.0837 | -0.27% | -0.10% | 4227/6823 |
| Performance (Month) | +0.0782 | -0.2483 | +0.2127 | -0.38% | -0.11% | 3092/8390 |
| d_Short Ratio | -0.0680 | +0.1001 | -0.1539 | -0.39% | 0.11% | 5154/2449 |
| upside_pct_lvl | +0.0557 | +0.3569 | -0.2760 | -0.42% | -0.51% | 4389/247 |
| d_Average Volume | +0.0553 | -0.1057 | +0.1599 | 0.14% | -0.38% | 4140/6938 |
| Performance (Week) | +0.0529 | -0.3109 | +0.2270 | -0.50% | -0.12% | 1894/9629 |
| d_Performance (Month) | -0.0447 | +0.0231 | -0.0840 | -0.22% | -0.32% | 6639/4752 |
| d_Volatility (Month) | -0.0446 | +0.0474 | -0.0874 | -0.09% | -0.30% | 5837/3580 |
| Relative Strength Index (14) | +0.0429 | -0.1292 | -0.0663 | -0.18% | n/a | 11568/0 |
| d_Institutional Ownership | -0.0403 | -0.0203 | -0.0079 | -3.79% | 1.45% | 5/26 |
| d_20-Day Simple Moving Average | -0.0389 | -0.0295 | -0.0322 | -0.05% | -0.29% | 5415/6112 |
| d_Performance (Week) | +0.0369 | -0.1060 | +0.1157 | -0.18% | -0.19% | 4042/7371 |
| Relative Volume | -0.0346 | +0.0634 | -0.0137 | -0.18% | n/a | 11430/0 |
| d_Sales Year Over Year TTM | -0.0306 | +0.0056 | -0.0279 | -2.27% | -0.61% | 14/9 |
| d_Beta | -0.0303 | +0.1508 | -0.0685 | 0.01% | -0.53% | 3551/1245 |
| Short Float | -0.0296 | +0.1515 | -0.0591 | -0.07% | n/a | 5694/0 |
| d_Forward P/E | -0.0238 | +0.0876 | -0.0640 | -0.57% | -0.58% | 1188/1742 |
| Institutional Transactions | +0.0228 | +0.0727 | -0.0474 | -0.47% | 0.18% | 3234/1813 |
| d_50-Day Simple Moving Average | -0.0223 | -0.0574 | -0.0059 | 0.02% | -0.31% | 4559/6979 |
| d_Gross Margin | -0.0199 | -0.0001 | -0.0247 | -1.65% | 0.17% | 14/15 |
| d_Relative Strength Index (14) | -0.0194 | -0.0319 | -0.0790 | -0.18% | -0.32% | 4307/6921 |
| d_200-Day Simple Moving Average | -0.0165 | -0.0658 | -0.0136 | -0.01% | -0.29% | 4470/7065 |
| d_Insider Transactions | +0.0126 | +0.0136 | -0.0277 | 2.54% | -0.18% | 63/111 |
| true_ret | -0.0124 | -0.1075 | +0.0267 | -0.19% | -0.30% | 4230/6815 |
| d_EPS Surprise | -0.0121 | +0.0150 | -0.0361 | -1.50% | -0.18% | 7/5 |

## Combinations

| Pattern | n | Mean long fwd | Hit up |
|---|---|---|---|
| true_ret>3% & DOWNTREND | 269 | 3.11% | 26.4% |
| true_ret>3% & UPTREND | 195 | -0.72% | 19.0% |
| true_ret>3% & MIXED | 127 | -0.81% | 28.3% |

## Risk dominance probes

| State | n | Mean long fwd | Mean fwd if score top quintile |
|---|---|---|---|
| EXTENDED | 160 | -1.12% | -1.57% |
| WASHED | 2419 | 0.34% | 1.53% |

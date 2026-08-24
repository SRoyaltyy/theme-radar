# Factor attribution — signal 2026-08-20 → prediction day 2026-08-24

## Trade window (read this first)

| Role | Date | Meaning |
|------|------|---------|
| **Signal as-of** | **2026-08-20** | Features/scores formed from this snapshot (and deltas vs **2026-08-19**). Only data on/before this date. |
| **Prediction day** | **2026-08-24** | The trading day the forward return is for (exit snapshot). |
| **Entry price** | Price @ 2026-08-20 | Long: buy here; short: sell here. |
| **Exit price** | Price @ 2026-08-24 | Close proxy on prediction day. |
| **Return column** | `fwd_2d` | Long: exit/entry − 1; short = opposite. |

Graded **n=11591** names with valid entry and exit prices.

Provisional until multiple signal dates agree.

_Column guide: **IC** = Spearman(feature, long forward return); **IC↑** / **IC↓** = IC among names that went up / down._

## Score calibration (long fwd)
- Spearman IC(total_score, fwd_2d) = **0.0530**

| Quintile | Mean long fwd | Hit up>1.5% | n |
|---|---|---|---|
| 1 | 5.25% | 27.2% | 2322 |
| 2 | 0.54% | 13.6% | 3302 |
| 3 | 3.12% | 16.0% | 1394 |
| 4 | 0.29% | 10.5% | 2339 |
| 5 | 5.99% | 36.6% | 2234 |

## Top |IC| features

| Feature | IC | IC↑ | IC↓ | Mean fwd when + | Mean fwd when − | n+/n− |
|---|---|---|---|---|---|---|
| Performance (Month) | +0.1907 | +0.1601 | +0.1431 | 1.51% | 5.10% | 7081/4269 |
| Relative Strength Index (14) | +0.1884 | -0.0004 | +0.1944 | 2.84% | n/a | 11453/0 |
| d_Beta | +0.1844 | +0.2046 | +0.0709 | 5.69% | 10.30% | 2044/1418 |
| Performance (Week) | +0.1462 | +0.0525 | +0.2045 | 2.98% | 2.79% | 3649/7747 |
| upside_pct_lvl | -0.1021 | +0.2972 | -0.3861 | 2.80% | 0.51% | 4313/334 |
| Relative Volume | +0.0766 | +0.1548 | -0.0079 | 2.86% | n/a | 11324/0 |
| Institutional Transactions | -0.0727 | -0.0189 | -0.0677 | 7.12% | 2.40% | 2690/2352 |
| d_Forward P/E | +0.0530 | -0.0270 | +0.0716 | 1.59% | 0.41% | 1041/1898 |
| d_20-Day Simple Moving Average | -0.0468 | -0.0616 | +0.0294 | 6.46% | 1.39% | 3256/8211 |
| d_Relative Strength Index (14) | -0.0429 | +0.2895 | -0.1726 | 5.02% | 1.96% | 3415/7755 |
| d_Institutional Ownership | +0.0399 | -0.0572 | +0.1168 | 0.31% | 13.11% | 711/757 |
| d_50-Day Simple Moving Average | -0.0342 | -0.0346 | +0.0257 | 5.83% | 1.56% | 3403/8066 |
| d_Performance (Week) | -0.0305 | -0.0395 | +0.0365 | 4.71% | 2.16% | 3117/8256 |
| d_Gross Margin | +0.0276 | +0.0024 | +0.0249 | 2.17% | -4.91% | 29/31 |
| d_EPS Surprise | -0.0209 | -0.0151 | -0.0035 | 0.14% | 4.74% | 21/27 |
| d_Profit Margin | +0.0199 | -0.0024 | +0.0298 | 2.42% | -4.14% | 22/34 |
| d_Relative Volume | +0.0193 | -0.0457 | +0.0590 | 3.82% | 2.23% | 4753/6395 |
| d_Short Float | +0.0182 | -0.0463 | +0.0385 | -0.29% | 37.24% | 85/155 |
| d_Analyst Recom | +0.0179 | +0.0128 | +0.0310 | 0.40% | -0.19% | 114/102 |
| d_Sales Year Over Year TTM | +0.0142 | -0.0233 | +0.0376 | -1.48% | 1.03% | 22/29 |
| d_200-Day Simple Moving Average | -0.0114 | +0.0015 | +0.0284 | 4.94% | 1.93% | 3460/7974 |
| d_Price | -0.0112 | +0.1127 | -0.0373 | 3.80% | 1.96% | 3310/7742 |
| d_Short Ratio | -0.0093 | -0.0204 | +0.0150 | 0.36% | 4.12% | 3647/3257 |
| d_Total Debt/Equity | -0.0080 | +0.0065 | -0.0330 | -3.22% | -1.82% | 27/21 |
| true_ret | +0.0062 | -0.0337 | +0.0873 | 3.80% | 1.96% | 3310/7742 |

## Combinations

| Pattern | n | Mean long fwd | Hit up |
|---|---|---|---|
| true_ret>3% & DOWNTREND | 245 | 21.15% | 26.5% |
| true_ret>3% & UPTREND | 249 | 4.74% | 42.6% |
| true_ret>3% & MIXED | 276 | 20.03% | 67.8% |

## Risk dominance probes

| State | n | Mean long fwd | Mean fwd if score top quintile |
|---|---|---|---|
| EXTENDED | 289 | 5.74% | 20.35% |
| WASHED | 575 | 30.00% | 47.70% |

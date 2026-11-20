# Factor attribution — signal 2026-11-16 → prediction day 2026-11-19

## Trade window (read this first)

| Role | Date | Meaning |
|------|------|---------|
| **Signal as-of** | **2026-11-16** | Features/scores formed from this snapshot (and deltas vs **2026-11-13**). Only data on/before this date. |
| **Prediction day** | **2026-11-19** | The trading day the forward return is for (exit snapshot). |
| **Entry price** | Price @ 2026-11-16 | Long: buy here; short: sell here. |
| **Exit price** | Price @ 2026-11-19 | Close proxy on prediction day. |
| **Return column** | `fwd_3d` | Long: exit/entry − 1; short = opposite. |

Graded **n=11722** names with valid entry and exit prices.

Provisional until multiple signal dates agree.

_Column guide: **IC** = Spearman(feature, long forward return); **IC↑** / **IC↓** = IC among names that went up / down._

## Score calibration (long fwd)
- Spearman IC(total_score, fwd_3d) = **0.1293**

| Quintile | Mean long fwd | Hit up>1.5% | n |
|---|---|---|---|
| 1 | -1.68% | 6.5% | 2543 |
| 2 | -1.48% | 5.1% | 2290 |
| 3 | -2.94% | 6.0% | 2213 |
| 4 | -1.41% | 6.8% | 2560 |
| 5 | -1.01% | 14.4% | 2116 |

## Top |IC| features

| Feature | IC | IC↑ | IC↓ | Mean fwd when + | Mean fwd when − | n+/n− |
|---|---|---|---|---|---|---|
| true_ret | +0.3318 | -0.1690 | +0.3464 | -1.08% | -2.47% | 2046/9225 |
| d_20-Day Simple Moving Average | +0.3275 | -0.1238 | +0.3214 | 0.71% | -2.25% | 2143/9483 |
| d_Performance (Week) | +0.3177 | -0.1823 | +0.3135 | 4.75% | -2.83% | 1703/9866 |
| d_50-Day Simple Moving Average | +0.3098 | -0.1070 | +0.2958 | 0.32% | -2.24% | 2390/9215 |
| d_200-Day Simple Moving Average | +0.2980 | -0.1187 | +0.2645 | -0.63% | -2.25% | 2264/9334 |
| d_Performance (YTD) | +0.2769 | -0.1326 | +0.2203 | -0.56% | -2.25% | 2110/9288 |
| Performance (Week) | +0.2559 | -0.2122 | +0.3202 | -1.95% | -1.64% | 2305/9289 |
| d_Price | +0.2479 | -0.1136 | +0.0786 | -1.08% | -2.47% | 2046/9225 |
| d_Performance (Quarter) | +0.2184 | -0.0653 | +0.2110 | -2.12% | -1.50% | 3382/7830 |
| Performance (Month) | +0.1922 | -0.2315 | +0.2803 | -2.26% | -1.39% | 4104/7470 |
| upside_pct_lvl | -0.1841 | +0.4093 | -0.4066 | -1.14% | -3.03% | 4354/272 |
| d_Performance (Month) | +0.1790 | +0.0999 | +0.1202 | -1.16% | -1.98% | 3775/7723 |
| d_Relative Strength Index (14) | +0.1662 | -0.1197 | -0.0864 | -0.61% | -1.96% | 2138/9284 |
| Relative Strength Index (14) | +0.1529 | -0.1281 | +0.1950 | -1.70% | n/a | 11672/0 |
| Short Float | -0.1428 | +0.2782 | -0.1636 | -0.88% | n/a | 5626/0 |
| Institutional Transactions | -0.0655 | +0.1159 | -0.1100 | -1.26% | 0.18% | 2991/2019 |
| d_Average Volume | +0.0591 | +0.0099 | +0.0513 | -0.19% | -3.06% | 5444/5542 |
| d_Market Cap | +0.0551 | +0.0156 | -0.0245 | -2.70% | -0.40% | 1354/4396 |
| Relative Volume | -0.0515 | +0.1628 | -0.0599 | -1.72% | n/a | 11524/0 |
| d_Target Price | +0.0496 | -0.0317 | +0.0830 | -3.58% | -4.79% | 339/398 |
| d_Beta | -0.0424 | +0.1228 | -0.1104 | 3.11% | -3.96% | 1888/1373 |
| d_Short Ratio | -0.0403 | +0.0000 | -0.0275 | -1.84% | -1.10% | 3361/3089 |
| d_Institutional Ownership | +0.0317 | -0.0714 | +0.0133 | -1.54% | 0.38% | 3294/2199 |
| d_EPS Surprise | +0.0264 | +0.0058 | +0.0287 | 3.22% | -7.98% | 55/68 |
| d_Short Float | +0.0221 | -0.0564 | +0.0518 | -2.91% | -4.20% | 33/128 |

## Combinations

| Pattern | n | Mean long fwd | Hit up |
|---|---|---|---|
| true_ret>3% & DOWNTREND | 183 | -5.79% | 26.2% |
| true_ret>3% & UPTREND | 118 | 3.47% | 42.4% |
| true_ret>3% & MIXED | 120 | 11.61% | 63.3% |

## Risk dominance probes

| State | n | Mean long fwd | Mean fwd if score top quintile |
|---|---|---|---|
| EXTENDED | 203 | 1.32% | 1.68% |
| WASHED | 1657 | 4.06% | 9.05% |

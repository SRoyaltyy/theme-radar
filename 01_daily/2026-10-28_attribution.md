# Factor attribution — signal 2026-10-28 → prediction day 2026-10-29

## Trade window (read this first)

| Role | Date | Meaning |
|------|------|---------|
| **Signal as-of** | **2026-10-28** | Features/scores formed from this snapshot (and deltas vs **2026-10-27**). Only data on/before this date. |
| **Prediction day** | **2026-10-29** | The trading day the forward return is for (exit snapshot). |
| **Entry price** | Price @ 2026-10-28 | Long: buy here; short: sell here. |
| **Exit price** | Price @ 2026-10-29 | Close proxy on prediction day. |
| **Return column** | `fwd_1d` | Long: exit/entry − 1; short = opposite. |

Graded **n=11761** names with valid entry and exit prices.

Provisional until multiple signal dates agree.

_Column guide: **IC** = Spearman(feature, long forward return); **IC↑** / **IC↓** = IC among names that went up / down._

## Score calibration (long fwd)
- Spearman IC(total_score, fwd_1d) = **0.0096**

| Quintile | Mean long fwd | Hit up>1.5% | n |
|---|---|---|---|
| 1 | 5.13% | 23.3% | 2374 |
| 2 | 0.18% | 14.6% | 2616 |
| 3 | 0.13% | 15.4% | 2978 |
| 4 | 4.50% | 25.2% | 1530 |
| 5 | 0.14% | 28.0% | 2263 |

## Top |IC| features

| Feature | IC | IC↑ | IC↓ | Mean fwd when + | Mean fwd when − | n+/n− |
|---|---|---|---|---|---|---|
| Performance (Month) | +0.2837 | -0.0289 | +0.4626 | 0.60% | 2.94% | 5862/5725 |
| d_Beta | +0.2633 | -0.0596 | +0.3721 | 0.83% | 6.39% | 1746/2707 |
| d_20-Day Simple Moving Average | -0.2497 | +0.0052 | -0.3543 | 0.76% | 3.16% | 6823/4764 |
| d_Performance (Quarter) | +0.2305 | +0.0983 | +0.1562 | 2.31% | 1.57% | 3944/7250 |
| d_Relative Strength Index (14) | -0.2159 | +0.0251 | -0.0637 | 0.85% | 0.51% | 6861/4447 |
| upside_pct_lvl | -0.2098 | +0.2343 | -0.3486 | 2.12% | 0.45% | 4303/329 |
| d_200-Day Simple Moving Average | -0.2026 | +0.0162 | -0.2681 | 0.79% | 3.25% | 7017/4517 |
| d_Performance (YTD) | -0.1987 | -0.0050 | -0.2171 | 0.84% | 0.50% | 6841/4447 |
| true_ret | -0.1965 | -0.0021 | -0.2593 | 0.51% | 3.33% | 6739/4362 |
| d_Price | -0.1861 | -0.0027 | -0.0948 | 0.51% | 3.33% | 6739/4362 |
| d_50-Day Simple Moving Average | -0.1858 | +0.0444 | -0.3027 | 0.78% | 3.45% | 7383/4182 |
| Relative Strength Index (14) | +0.1777 | -0.1864 | +0.3906 | 1.74% | n/a | 11677/0 |
| Performance (Week) | +0.1379 | +0.0653 | +0.0882 | 0.29% | 3.60% | 6406/5107 |
| Relative Volume | +0.0952 | +0.1469 | -0.0820 | 1.76% | n/a | 11451/0 |
| Short Float | +0.0809 | +0.2266 | -0.0535 | 3.80% | n/a | 5657/0 |
| d_Performance (Month) | -0.0802 | +0.0547 | -0.1629 | 0.93% | 3.45% | 7619/3841 |
| d_Forward P/E | -0.0638 | +0.0300 | -0.1045 | 0.93% | 1.02% | 1482/1453 |
| d_Market Cap | -0.0587 | +0.0166 | -0.0366 | 2.46% | 5.46% | 3205/2503 |
| Institutional Transactions | -0.0506 | -0.0027 | -0.0457 | 0.50% | 10.82% | 3237/1813 |
| d_Short Ratio | -0.0389 | -0.0750 | +0.0221 | 0.31% | 5.65% | 3251/3491 |
| d_Average Volume | +0.0362 | +0.0516 | -0.0258 | 3.39% | 0.20% | 5633/5345 |
| d_Target Price | -0.0265 | -0.0525 | +0.0588 | 0.99% | 1.28% | 231/246 |
| d_Short Float | +0.0166 | -0.0179 | +0.0241 | 0.07% | 0.37% | 30/21 |
| d_Volatility (Month) | -0.0115 | +0.0511 | -0.0485 | 4.25% | 0.29% | 4381/5069 |
| d_Institutional Ownership | +0.0104 | +0.0229 | +0.0151 | 0.73% | 0.51% | 1109/974 |

## Combinations

| Pattern | n | Mean long fwd | Hit up |
|---|---|---|---|
| true_ret>3% & DOWNTREND | 833 | 4.13% | 22.7% |
| true_ret>3% & UPTREND | 240 | 0.61% | 36.7% |
| true_ret>3% & MIXED | 218 | -1.09% | 28.4% |

## Risk dominance probes

| State | n | Mean long fwd | Mean fwd if score top quintile |
|---|---|---|---|
| EXTENDED | 179 | 0.57% | 0.94% |
| WASHED | 1165 | 12.73% | -2.81% |

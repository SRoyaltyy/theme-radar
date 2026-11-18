# Factor attribution — signal 2026-11-13 → prediction day 2026-11-17

## Trade window (read this first)

| Role | Date | Meaning |
|------|------|---------|
| **Signal as-of** | **2026-11-13** | Features/scores formed from this snapshot (and deltas vs **2026-11-12**). Only data on/before this date. |
| **Prediction day** | **2026-11-17** | The trading day the forward return is for (exit snapshot). |
| **Entry price** | Price @ 2026-11-13 | Long: buy here; short: sell here. |
| **Exit price** | Price @ 2026-11-17 | Close proxy on prediction day. |
| **Return column** | `fwd_2d` | Long: exit/entry − 1; short = opposite. |

Graded **n=11714** names with valid entry and exit prices.

Provisional until multiple signal dates agree.

_Column guide: **IC** = Spearman(feature, long forward return); **IC↑** / **IC↓** = IC among names that went up / down._

## Score calibration (long fwd)
- Spearman IC(total_score, fwd_2d) = **0.1738**

| Quintile | Mean long fwd | Hit up>1.5% | n |
|---|---|---|---|
| 1 | -3.22% | 7.6% | 2360 |
| 2 | -2.20% | 4.0% | 2338 |
| 3 | -2.24% | 3.4% | 3271 |
| 4 | -2.52% | 4.2% | 1959 |
| 5 | 2.04% | 11.6% | 1786 |

## Top |IC| features

| Feature | IC | IC↑ | IC↓ | Mean fwd when + | Mean fwd when − | n+/n− |
|---|---|---|---|---|---|---|
| upside_pct_lvl | -0.3648 | +0.5058 | -0.5431 | -1.09% | -2.20% | 4347/277 |
| Performance (Month) | +0.3599 | -0.1351 | +0.4591 | -1.69% | -1.92% | 4485/7069 |
| d_Performance (Week) | +0.2867 | -0.0469 | +0.3416 | -1.64% | -1.97% | 4367/7168 |
| Relative Strength Index (14) | +0.2718 | -0.0130 | +0.3997 | -1.82% | n/a | 11668/0 |
| true_ret | +0.2618 | +0.0034 | +0.3092 | -0.44% | -2.67% | 4232/6922 |
| d_Performance (YTD) | +0.2508 | +0.0227 | +0.2840 | -0.46% | -2.67% | 4313/6990 |
| d_200-Day Simple Moving Average | +0.2433 | +0.0377 | +0.2731 | -0.58% | -2.79% | 4475/7087 |
| d_Performance (Month) | +0.2405 | -0.0211 | +0.2433 | 0.36% | -2.48% | 2626/8869 |
| Short Float | -0.2396 | +0.2065 | -0.2377 | -0.80% | n/a | 5614/0 |
| d_Price | +0.2363 | +0.0858 | +0.2378 | -0.44% | -2.67% | 4232/6922 |
| d_20-Day Simple Moving Average | +0.2037 | +0.0363 | +0.2268 | -0.44% | -2.70% | 4441/7147 |
| d_50-Day Simple Moving Average | +0.2012 | +0.0416 | +0.2343 | -0.61% | -2.73% | 4863/6708 |
| d_Performance (Quarter) | +0.1828 | +0.0877 | +0.2131 | -0.88% | -2.86% | 5837/5355 |
| d_Beta | -0.1657 | +0.0318 | -0.2151 | 1.47% | -1.38% | 1859/886 |
| d_Market Cap | +0.1292 | -0.1293 | +0.1472 | 0.08% | -1.58% | 2556/3137 |
| Performance (Week) | -0.1177 | -0.1383 | -0.0452 | -3.31% | 0.50% | 7086/4512 |
| d_Forward P/E | +0.1147 | -0.0969 | +0.1089 | -2.93% | -3.60% | 1563/1313 |
| d_Relative Strength Index (14) | +0.1123 | +0.0822 | +0.1172 | -0.51% | -2.69% | 4342/7001 |
| Relative Volume | -0.0932 | +0.1253 | -0.0951 | -1.85% | n/a | 11465/0 |
| d_Target Price | +0.0780 | -0.0957 | +0.0812 | -3.31% | -5.08% | 279/406 |
| Institutional Transactions | -0.0734 | +0.0837 | -0.1119 | 0.60% | -2.63% | 3093/1914 |
| d_Short Float | +0.0616 | -0.0444 | +0.0822 | -3.62% | -7.35% | 50/115 |
| d_Sales Year Over Year TTM | +0.0422 | +0.0301 | +0.0476 | -4.71% | -7.06% | 109/134 |
| d_Volatility (Month) | +0.0414 | +0.0959 | +0.0216 | -2.35% | -1.53% | 4560/5811 |
| d_Institutional Ownership | +0.0396 | -0.0938 | +0.0329 | 0.49% | -2.46% | 2724/2329 |

## Combinations

| Pattern | n | Mean long fwd | Hit up |
|---|---|---|---|
| true_ret>3% & DOWNTREND | 320 | 21.39% | 14.4% |
| true_ret>3% & UPTREND | 151 | -2.83% | 21.2% |
| true_ret>3% & MIXED | 133 | 0.47% | 41.4% |

## Risk dominance probes

| State | n | Mean long fwd | Mean fwd if score top quintile |
|---|---|---|---|
| EXTENDED | 190 | -0.52% | -0.62% |
| WASHED | 1420 | 3.07% | 24.02% |

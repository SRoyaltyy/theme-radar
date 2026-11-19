# Factor attribution — signal 2026-11-13 → prediction day 2026-11-18

## Trade window (read this first)

| Role | Date | Meaning |
|------|------|---------|
| **Signal as-of** | **2026-11-13** | Features/scores formed from this snapshot (and deltas vs **2026-11-12**). Only data on/before this date. |
| **Prediction day** | **2026-11-18** | The trading day the forward return is for (exit snapshot). |
| **Entry price** | Price @ 2026-11-13 | Long: buy here; short: sell here. |
| **Exit price** | Price @ 2026-11-18 | Close proxy on prediction day. |
| **Return column** | `fwd_3d` | Long: exit/entry − 1; short = opposite. |

Graded **n=11714** names with valid entry and exit prices.

Provisional until multiple signal dates agree.

_Column guide: **IC** = Spearman(feature, long forward return); **IC↑** / **IC↓** = IC among names that went up / down._

## Score calibration (long fwd)
- Spearman IC(total_score, fwd_3d) = **0.1431**

| Quintile | Mean long fwd | Hit up>1.5% | n |
|---|---|---|---|
| 1 | -2.59% | 9.7% | 2360 |
| 2 | -2.36% | 6.4% | 2338 |
| 3 | -2.44% | 5.1% | 3271 |
| 4 | -2.80% | 5.7% | 1959 |
| 5 | 1.03% | 14.2% | 1786 |

## Top |IC| features

| Feature | IC | IC↑ | IC↓ | Mean fwd when + | Mean fwd when − | n+/n− |
|---|---|---|---|---|---|---|
| Performance (Month) | +0.3562 | -0.1327 | +0.4561 | -1.65% | -2.20% | 4485/7069 |
| upside_pct_lvl | -0.3460 | +0.3990 | -0.5297 | -1.13% | -2.14% | 4347/277 |
| Relative Strength Index (14) | +0.2745 | -0.0345 | +0.4131 | -1.98% | n/a | 11668/0 |
| d_Performance (Week) | +0.2329 | -0.0681 | +0.2781 | -2.05% | -1.98% | 4367/7168 |
| true_ret | +0.1956 | -0.0628 | +0.2376 | -1.11% | -2.50% | 4232/6922 |
| d_Performance (Quarter) | +0.1825 | +0.0903 | +0.2039 | -1.24% | -2.81% | 5837/5355 |
| d_Beta | -0.1780 | +0.0365 | -0.2324 | 1.13% | -1.44% | 1859/886 |
| d_Performance (YTD) | +0.1769 | -0.0493 | +0.2018 | -1.13% | -2.50% | 4313/6990 |
| d_Performance (Month) | +0.1703 | -0.1253 | +0.2046 | -0.61% | -2.40% | 2626/8869 |
| d_200-Day Simple Moving Average | +0.1696 | -0.0405 | +0.1901 | -1.30% | -2.52% | 4475/7087 |
| d_Price | +0.1553 | +0.0043 | +0.1490 | -1.11% | -2.50% | 4232/6922 |
| d_50-Day Simple Moving Average | +0.1253 | -0.0316 | +0.1497 | -1.44% | -2.40% | 4863/6708 |
| d_20-Day Simple Moving Average | +0.1253 | -0.0280 | +0.1395 | -1.33% | -2.40% | 4441/7147 |
| Short Float | -0.1239 | +0.1891 | -0.2038 | -0.81% | n/a | 5614/0 |
| d_Market Cap | +0.0904 | -0.1088 | +0.1067 | -0.66% | -1.01% | 2556/3137 |
| d_Target Price | +0.0835 | -0.0148 | +0.1059 | -3.06% | -5.80% | 279/406 |
| Relative Volume | -0.0703 | +0.1537 | -0.0863 | -2.01% | n/a | 11465/0 |
| Institutional Transactions | -0.0671 | +0.1059 | -0.1007 | 0.63% | -2.58% | 3093/1914 |
| Performance (Week) | -0.0633 | -0.0677 | +0.0233 | -3.47% | 0.33% | 7086/4512 |
| d_Short Float | +0.0561 | -0.0361 | +0.0587 | -3.62% | -8.21% | 50/115 |
| d_Volatility (Month) | +0.0547 | +0.0942 | +0.0355 | -1.97% | -2.11% | 4560/5811 |
| d_Sales Year Over Year TTM | +0.0533 | +0.0353 | +0.0602 | -5.29% | -8.44% | 109/134 |
| d_Forward P/E | +0.0523 | -0.0173 | +0.0521 | -3.11% | -3.59% | 1563/1313 |
| d_Relative Strength Index (14) | +0.0504 | +0.0288 | +0.0431 | -1.20% | -2.53% | 4342/7001 |
| d_Institutional Ownership | +0.0499 | -0.0275 | +0.0441 | 0.33% | -1.90% | 2724/2329 |

## Combinations

| Pattern | n | Mean long fwd | Hit up |
|---|---|---|---|
| true_ret>3% & DOWNTREND | 320 | 17.70% | 16.9% |
| true_ret>3% & UPTREND | 151 | -2.57% | 27.8% |
| true_ret>3% & MIXED | 133 | 0.92% | 40.6% |

## Risk dominance probes

| State | n | Mean long fwd | Mean fwd if score top quintile |
|---|---|---|---|
| EXTENDED | 190 | 0.11% | 2.11% |
| WASHED | 1420 | 3.20% | 19.42% |

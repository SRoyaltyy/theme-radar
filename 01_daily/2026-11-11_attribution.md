# Factor attribution — signal 2026-11-11 → prediction day 2026-11-13

## Trade window (read this first)

| Role | Date | Meaning |
|------|------|---------|
| **Signal as-of** | **2026-11-11** | Features/scores formed from this snapshot (and deltas vs **2026-11-10**). Only data on/before this date. |
| **Prediction day** | **2026-11-13** | The trading day the forward return is for (exit snapshot). |
| **Entry price** | Price @ 2026-11-11 | Long: buy here; short: sell here. |
| **Exit price** | Price @ 2026-11-13 | Close proxy on prediction day. |
| **Return column** | `fwd_2d` | Long: exit/entry − 1; short = opposite. |

Graded **n=11737** names with valid entry and exit prices.

Provisional until multiple signal dates agree.

_Column guide: **IC** = Spearman(feature, long forward return); **IC↑** / **IC↓** = IC among names that went up / down._

## Score calibration (long fwd)
- Spearman IC(total_score, fwd_2d) = **-0.2004**

| Quintile | Mean long fwd | Hit up>1.5% | n |
|---|---|---|---|
| 1 | -1.75% | 15.3% | 2356 |
| 2 | -0.91% | 4.4% | 2837 |
| 3 | -0.86% | 6.1% | 1955 |
| 4 | -1.92% | 6.4% | 2249 |
| 5 | -1.11% | 10.0% | 2340 |

## Top |IC| features

| Feature | IC | IC↑ | IC↓ | Mean fwd when + | Mean fwd when − | n+/n− |
|---|---|---|---|---|---|---|
| upside_pct_lvl | -0.3547 | +0.4870 | -0.5739 | -1.70% | -1.56% | 4326/308 |
| d_Performance (Month) | -0.2915 | +0.0770 | -0.3450 | -1.33% | -1.28% | 7544/3925 |
| Performance (Month) | +0.2351 | -0.2473 | +0.3634 | -0.92% | -1.64% | 5373/6199 |
| Short Float | -0.2181 | +0.1537 | -0.2372 | -0.91% | n/a | 5644/0 |
| d_50-Day Simple Moving Average | -0.2176 | +0.1148 | -0.2621 | -1.29% | -1.38% | 8060/3524 |
| Relative Strength Index (14) | +0.2047 | -0.3566 | +0.3658 | -1.30% | n/a | 11687/0 |
| d_20-Day Simple Moving Average | -0.1983 | +0.1240 | -0.2449 | -1.29% | -1.36% | 7387/4197 |
| true_ret | -0.1954 | +0.0653 | -0.2217 | -1.53% | -1.90% | 7705/3453 |
| d_200-Day Simple Moving Average | -0.1915 | +0.0852 | -0.2110 | -1.56% | -1.33% | 7985/3569 |
| d_Performance (Quarter) | -0.1902 | +0.0342 | -0.2141 | -1.65% | -1.27% | 6407/4811 |
| d_Volatility (Month) | -0.1585 | +0.2427 | -0.2923 | -1.32% | -1.56% | 7541/2369 |
| d_Performance (YTD) | -0.1532 | +0.0490 | -0.1494 | -1.50% | -1.45% | 7781/3522 |
| Institutional Transactions | -0.1274 | +0.0635 | -0.1586 | -2.03% | 0.73% | 3099/1915 |
| d_Price | -0.1073 | -0.0124 | -0.0359 | -1.53% | -1.90% | 7705/3453 |
| d_Beta | -0.0963 | +0.1699 | -0.1623 | 0.42% | -1.71% | 1993/1542 |
| d_Relative Strength Index (14) | -0.0888 | +0.0454 | +0.0039 | -1.26% | -1.43% | 7796/3554 |
| Relative Volume | -0.0772 | +0.0842 | -0.1327 | -1.32% | n/a | 11457/0 |
| d_Forward P/E | -0.0667 | +0.1453 | -0.1846 | -0.71% | -1.37% | 1715/1187 |
| d_Performance (Week) | -0.0654 | +0.1239 | -0.1153 | -1.08% | -1.45% | 4210/7360 |
| d_Short Float | -0.0496 | -0.0146 | -0.0711 | -1.50% | -0.48% | 2331/3123 |
| d_Institutional Ownership | +0.0492 | -0.0930 | -0.0006 | -1.40% | -2.27% | 2071/2025 |
| d_Short Ratio | -0.0486 | +0.0034 | -0.0879 | -1.64% | -1.35% | 4803/6300 |
| d_Total Debt/Equity | -0.0431 | -0.0175 | -0.0378 | -5.17% | -1.96% | 68/52 |
| d_EPS Surprise | -0.0402 | -0.0275 | -0.0379 | -5.73% | -2.74% | 77/66 |
| d_Insider Transactions | -0.0330 | +0.0314 | -0.0369 | -4.02% | -2.51% | 103/159 |

## Combinations

| Pattern | n | Mean long fwd | Hit up |
|---|---|---|---|
| true_ret>3% & DOWNTREND | 1260 | -2.06% | 11.4% |
| true_ret>3% & UPTREND | 201 | -2.72% | 18.4% |
| true_ret>3% & MIXED | 294 | -2.56% | 18.7% |

## Risk dominance probes

| State | n | Mean long fwd | Mean fwd if score top quintile |
|---|---|---|---|
| EXTENDED | 257 | -3.18% | -7.77% |
| WASHED | 1248 | 0.19% | 10.44% |

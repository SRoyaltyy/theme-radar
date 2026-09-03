# Factor attribution — signal 2026-08-31 → prediction day 2026-09-03

## Trade window (read this first)

| Role | Date | Meaning |
|------|------|---------|
| **Signal as-of** | **2026-08-31** | Features/scores formed from this snapshot (and deltas vs **2026-08-28**). Only data on/before this date. |
| **Prediction day** | **2026-09-03** | The trading day the forward return is for (exit snapshot). |
| **Entry price** | Price @ 2026-08-31 | Long: buy here; short: sell here. |
| **Exit price** | Price @ 2026-09-03 | Close proxy on prediction day. |
| **Return column** | `fwd_3d` | Long: exit/entry − 1; short = opposite. |

Graded **n=11615** names with valid entry and exit prices.

Provisional until multiple signal dates agree.

_Column guide: **IC** = Spearman(feature, long forward return); **IC↑** / **IC↓** = IC among names that went up / down._

## Score calibration (long fwd)
- Spearman IC(total_score, fwd_3d) = **0.1004**

| Quintile | Mean long fwd | Hit up>1.5% | n |
|---|---|---|---|
| 1 | -0.50% | 21.2% | 2467 |
| 2 | 8.40% | 18.5% | 2252 |
| 3 | 0.32% | 13.8% | 2286 |
| 4 | 0.39% | 17.2% | 2348 |
| 5 | 1.03% | 37.8% | 2262 |

## Top |IC| features

| Feature | IC | IC↑ | IC↓ | Mean fwd when + | Mean fwd when − | n+/n− |
|---|---|---|---|---|---|---|
| Relative Strength Index (14) | +0.1685 | -0.0594 | +0.0913 | 1.89% | n/a | 11491/0 |
| Performance (Month) | +0.1228 | +0.1183 | +0.0284 | 0.58% | 4.27% | 7256/4104 |
| upside_pct_lvl | -0.1103 | +0.2293 | -0.3291 | 0.56% | 0.42% | 4329/321 |
| d_Performance (Week) | -0.0927 | -0.0408 | -0.1365 | 1.99% | 1.85% | 5451/5899 |
| d_50-Day Simple Moving Average | -0.0709 | -0.0824 | -0.0222 | 2.43% | 1.60% | 4051/7395 |
| d_Market Cap | -0.0695 | +0.0407 | -0.0730 | 4.53% | 2.84% | 2098/3613 |
| d_20-Day Simple Moving Average | -0.0649 | -0.0993 | +0.0138 | 2.66% | 1.53% | 3664/7784 |
| d_200-Day Simple Moving Average | -0.0632 | -0.0643 | -0.0136 | 2.61% | 1.53% | 3889/7536 |
| d_Relative Strength Index (14) | -0.0623 | +0.1176 | -0.1062 | 0.49% | 2.72% | 3829/7276 |
| d_Price | -0.0607 | +0.0272 | -0.0638 | 0.36% | 0.20% | 3757/7174 |
| d_Performance (Quarter) | +0.0554 | +0.0528 | +0.0934 | 0.67% | 3.08% | 4855/5981 |
| d_Total Debt/Equity | +0.0487 | +0.0233 | +0.0449 | 2.90% | -9.26% | 15/7 |
| d_Performance (Month) | +0.0448 | +0.1035 | +0.0369 | 0.57% | 2.98% | 4901/6368 |
| d_Forward P/E | +0.0442 | +0.0298 | +0.0040 | 0.17% | 0.50% | 981/1967 |
| d_Performance (YTD) | -0.0429 | -0.0637 | +0.0144 | 0.50% | 2.70% | 3847/7295 |
| Relative Volume | +0.0361 | +0.1223 | +0.0545 | 1.89% | n/a | 11388/0 |
| d_Institutional Transactions | +0.0352 | +0.0464 | -0.0393 | 4.59% | 0.11% | 2012/2002 |
| d_Average Volume | +0.0297 | -0.0173 | +0.0548 | 4.92% | 0.09% | 4243/6746 |
| d_Short Ratio | -0.0293 | +0.0122 | -0.0558 | 0.13% | 0.37% | 4381/2500 |
| true_ret | -0.0279 | -0.0706 | +0.0342 | 0.36% | 0.20% | 3757/7174 |
| d_Profit Margin | +0.0260 | -0.0068 | +0.0483 | -1.00% | -7.62% | 9/15 |
| Performance (Week) | +0.0207 | -0.0903 | +0.1056 | 0.37% | 3.02% | 4779/6627 |
| Short Float | +0.0187 | +0.1718 | -0.1712 | 3.52% | n/a | 5701/0 |
| d_Institutional Ownership | +0.0181 | +0.0160 | -0.0097 | 69.51% | 0.10% | 124/141 |
| d_EPS Surprise | +0.0177 | +0.0145 | -0.0074 | 2.67% | 1.02% | 8/4 |

## Combinations

| Pattern | n | Mean long fwd | Hit up |
|---|---|---|---|
| true_ret>3% & DOWNTREND | 222 | -0.61% | 34.7% |
| true_ret>3% & UPTREND | 204 | 0.46% | 44.1% |
| true_ret>3% & MIXED | 182 | 0.17% | 41.8% |

## Risk dominance probes

| State | n | Mean long fwd | Mean fwd if score top quintile |
|---|---|---|---|
| EXTENDED | 292 | 0.84% | 1.35% |
| WASHED | 498 | 35.41% | -0.76% |

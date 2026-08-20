# Factor attribution — signal 2026-08-18 → prediction day 2026-08-20

## Trade window (read this first)

| Role | Date | Meaning |
|------|------|---------|
| **Signal as-of** | **2026-08-18** | Features/scores formed from this snapshot (and deltas vs **2026-08-17**). Only data on/before this date. |
| **Prediction day** | **2026-08-20** | The trading day the forward return is for (exit snapshot). |
| **Entry price** | Price @ 2026-08-18 | Long: buy here; short: sell here. |
| **Exit price** | Price @ 2026-08-20 | Close proxy on prediction day. |
| **Return column** | `fwd_2d` | Long: exit/entry − 1; short = opposite. |

Graded **n=11571** names with valid entry and exit prices.

Provisional until multiple signal dates agree.

_Column guide: **IC** = Spearman(feature, long forward return); **IC↑** / **IC↓** = IC among names that went up / down._

## Score calibration (long fwd)
- Spearman IC(total_score, fwd_2d) = **0.0270**

| Quintile | Mean long fwd | Hit up>1.5% | n |
|---|---|---|---|
| 1 | 1.08% | 29.2% | 2490 |
| 2 | 0.40% | 19.8% | 2144 |
| 3 | 1.79% | 12.1% | 2478 |
| 4 | 0.01% | 11.9% | 2242 |
| 5 | 1.55% | 32.7% | 2217 |

## Top |IC| features

| Feature | IC | IC↑ | IC↓ | Mean fwd when + | Mean fwd when − | n+/n− |
|---|---|---|---|---|---|---|
| d_Forward P/E | +0.1881 | -0.0788 | +0.2616 | 0.37% | -0.65% | 1095/1855 |
| d_Price | +0.1785 | -0.0473 | +0.1479 | 2.83% | 0.19% | 3444/7525 |
| d_200-Day Simple Moving Average | +0.1683 | -0.0904 | +0.2550 | 2.79% | 0.16% | 3654/7757 |
| d_Performance (YTD) | +0.1575 | -0.1133 | +0.2531 | 2.77% | 0.20% | 3542/7593 |
| true_ret | +0.1455 | -0.1323 | +0.2824 | 2.83% | 0.19% | 3444/7525 |
| d_50-Day Simple Moving Average | +0.1434 | -0.1334 | +0.2707 | 2.75% | 0.22% | 3504/7907 |
| d_20-Day Simple Moving Average | +0.1399 | -0.1299 | +0.2696 | 2.81% | 0.18% | 3562/7891 |
| d_Relative Strength Index (14) | +0.1388 | +0.0152 | -0.0242 | 2.74% | 0.23% | 3555/7544 |
| d_Performance (Week) | +0.1375 | -0.1106 | +0.2770 | 2.64% | 0.23% | 3709/7564 |
| d_Market Cap | +0.1062 | -0.0771 | +0.1041 | 3.51% | 0.39% | 2196/3507 |
| d_Volatility (Month) | +0.1004 | -0.1212 | +0.2194 | 3.29% | 0.14% | 3036/6596 |
| d_Performance (Quarter) | +0.0766 | -0.0244 | +0.1397 | 2.90% | 0.23% | 3530/7265 |
| Institutional Transactions | -0.0718 | +0.0109 | -0.0841 | 1.41% | 2.26% | 2690/2352 |
| d_Performance (Month) | +0.0672 | -0.1296 | +0.1407 | 1.61% | 0.55% | 4956/6308 |
| d_Average Volume | -0.0463 | -0.0731 | -0.0015 | 1.72% | 0.51% | 4642/6340 |
| d_Short Ratio | +0.0414 | +0.0793 | -0.0102 | 0.56% | 1.54% | 4088/2715 |
| d_EPS Surprise | -0.0332 | -0.0453 | -0.0310 | -1.94% | 1.53% | 25/30 |
| Performance (Month) | -0.0316 | +0.0587 | -0.0640 | 0.45% | 1.99% | 7208/4149 |
| d_Total Debt/Equity | +0.0307 | +0.0236 | +0.0280 | 6.96% | -1.03% | 13/13 |
| Relative Volume | -0.0282 | +0.0238 | -0.0688 | 1.01% | n/a | 11279/0 |
| d_Insider Transactions | +0.0229 | -0.0236 | +0.0300 | -0.35% | -1.05% | 280/372 |
| Performance (Week) | +0.0225 | -0.0794 | +0.1055 | 0.96% | 1.05% | 4902/6437 |
| Relative Strength Index (14) | +0.0176 | -0.0379 | +0.2739 | 1.01% | n/a | 11448/0 |
| d_Short Float | +0.0155 | -0.0223 | +0.0251 | -0.15% | -0.13% | 226/271 |
| d_Sales Growth Quarter Over Quarter | -0.0127 | +0.0045 | -0.0394 | -1.00% | 1.19% | 19/14 |

## Combinations

| Pattern | n | Mean long fwd | Hit up |
|---|---|---|---|
| true_ret>3% & DOWNTREND | 248 | 28.78% | 38.3% |
| true_ret>3% & UPTREND | 204 | 0.55% | 45.1% |
| true_ret>3% & MIXED | 147 | 0.37% | 45.6% |

## Risk dominance probes

| State | n | Mean long fwd | Mean fwd if score top quintile |
|---|---|---|---|
| EXTENDED | 236 | -1.54% | -3.58% |
| WASHED | 523 | 11.36% | 0.30% |

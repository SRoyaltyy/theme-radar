# Factor attribution — signal 2026-11-17 → prediction day 2026-11-20

## Trade window (read this first)

| Role | Date | Meaning |
|------|------|---------|
| **Signal as-of** | **2026-11-17** | Features/scores formed from this snapshot (and deltas vs **2026-11-16**). Only data on/before this date. |
| **Prediction day** | **2026-11-20** | The trading day the forward return is for (exit snapshot). |
| **Entry price** | Price @ 2026-11-17 | Long: buy here; short: sell here. |
| **Exit price** | Price @ 2026-11-20 | Close proxy on prediction day. |
| **Return column** | `fwd_3d` | Long: exit/entry − 1; short = opposite. |

Graded **n=11734** names with valid entry and exit prices.

Provisional until multiple signal dates agree.

_Column guide: **IC** = Spearman(feature, long forward return); **IC↑** / **IC↓** = IC among names that went up / down._

## Score calibration (long fwd)
- Spearman IC(total_score, fwd_3d) = **0.2127**

| Quintile | Mean long fwd | Hit up>1.5% | n |
|---|---|---|---|
| 1 | -4.45% | 5.4% | 2609 |
| 2 | -2.68% | 4.1% | 2160 |
| 3 | -4.66% | 3.3% | 2390 |
| 4 | -3.53% | 5.6% | 2238 |
| 5 | -3.01% | 10.9% | 2337 |

## Top |IC| features

| Feature | IC | IC↑ | IC↓ | Mean fwd when + | Mean fwd when − | n+/n− |
|---|---|---|---|---|---|---|
| Performance (Week) | +0.4775 | -0.1540 | +0.4835 | -0.52% | -4.33% | 1723/9862 |
| Performance (Month) | +0.4737 | -0.0542 | +0.5384 | -1.59% | -4.79% | 3919/7663 |
| upside_pct_lvl | -0.4042 | +0.5338 | -0.5643 | -4.68% | -3.36% | 4398/226 |
| Relative Strength Index (14) | +0.3840 | -0.1193 | +0.3658 | -3.70% | n/a | 11673/0 |
| d_Performance (Month) | +0.2733 | +0.1673 | +0.2151 | -2.61% | -4.21% | 3440/8072 |
| true_ret | +0.2582 | +0.0613 | +0.1787 | -2.89% | -4.12% | 2321/8893 |
| d_Volatility (Month) | -0.2341 | +0.3504 | -0.2839 | -3.38% | -5.48% | 7335/2693 |
| d_Beta | -0.1942 | +0.0948 | -0.2473 | -2.07% | -3.73% | 3350/3086 |
| d_Performance (YTD) | +0.1801 | +0.0837 | +0.0291 | -2.81% | -4.39% | 2380/8958 |
| d_200-Day Simple Moving Average | +0.1722 | +0.1013 | +0.0364 | -3.30% | -3.87% | 2631/8962 |
| Short Float | -0.1715 | +0.2335 | -0.1653 | -2.50% | n/a | 5612/0 |
| d_Performance (Quarter) | +0.1508 | -0.0928 | +0.0913 | -5.18% | -3.27% | 2531/8718 |
| d_Price | +0.1351 | +0.1207 | -0.0770 | -2.89% | -4.12% | 2321/8893 |
| d_50-Day Simple Moving Average | +0.1306 | +0.0862 | +0.0157 | -3.24% | -3.94% | 2964/8648 |
| d_Target Price | +0.1036 | -0.0522 | +0.1098 | -4.37% | -8.41% | 197/273 |
| d_20-Day Simple Moving Average | +0.0915 | +0.0663 | -0.0151 | -4.24% | -3.59% | 3096/8500 |
| d_Forward P/E | -0.0746 | -0.1273 | -0.0784 | -6.78% | -4.66% | 602/2313 |
| d_Market Cap | -0.0741 | +0.0932 | -0.1830 | -4.96% | -1.80% | 1404/4310 |
| Institutional Transactions | -0.0716 | +0.0690 | -0.1003 | -3.54% | -0.85% | 2991/2019 |
| d_Institutional Ownership | +0.0669 | -0.0946 | +0.0412 | -0.34% | -4.64% | 2873/2471 |
| Relative Volume | -0.0506 | +0.1431 | -0.0287 | -3.78% | n/a | 11503/0 |
| d_Relative Strength Index (14) | -0.0417 | +0.1075 | -0.2878 | -2.90% | -4.00% | 2422/8961 |
| d_Performance (Week) | +0.0389 | +0.0881 | -0.0547 | -2.47% | -4.54% | 4285/7271 |
| d_Total Debt/Equity | -0.0370 | -0.0613 | -0.0282 | 7.86% | -4.90% | 70/51 |
| d_Short Float | +0.0314 | -0.0810 | +0.0649 | -8.51% | -6.57% | 24/81 |

## Combinations

| Pattern | n | Mean long fwd | Hit up |
|---|---|---|---|
| true_ret>3% & DOWNTREND | 350 | -4.95% | 12.9% |
| true_ret>3% & UPTREND | 70 | 5.80% | 44.3% |
| true_ret>3% & MIXED | 87 | 4.54% | 41.4% |

## Risk dominance probes

| State | n | Mean long fwd | Mean fwd if score top quintile |
|---|---|---|---|
| EXTENDED | 166 | 4.74% | 11.10% |
| WASHED | 1834 | -2.00% | -7.01% |

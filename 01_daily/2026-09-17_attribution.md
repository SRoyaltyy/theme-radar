# Factor attribution — signal 2026-09-17 → prediction day 2026-09-18

## Trade window (read this first)

| Role | Date | Meaning |
|------|------|---------|
| **Signal as-of** | **2026-09-17** | Features/scores formed from this snapshot (and deltas vs **2026-09-16**). Only data on/before this date. |
| **Prediction day** | **2026-09-18** | The trading day the forward return is for (exit snapshot). |
| **Entry price** | Price @ 2026-09-17 | Long: buy here; short: sell here. |
| **Exit price** | Price @ 2026-09-18 | Close proxy on prediction day. |
| **Return column** | `fwd_1d` | Long: exit/entry − 1; short = opposite. |

Graded **n=11636** names with valid entry and exit prices.

Provisional until multiple signal dates agree.

_Column guide: **IC** = Spearman(feature, long forward return); **IC↑** / **IC↓** = IC among names that went up / down._

## Score calibration (long fwd)
- Spearman IC(total_score, fwd_1d) = **0.0987**

| Quintile | Mean long fwd | Hit up>1.5% | n |
|---|---|---|---|
| 1 | 0.43% | 11.2% | 2383 |
| 2 | -0.13% | 6.6% | 2277 |
| 3 | -0.06% | 9.6% | 2503 |
| 4 | 0.07% | 13.5% | 2478 |
| 5 | 0.86% | 27.6% | 1995 |

## Top |IC| features

| Feature | IC | IC↑ | IC↓ | Mean fwd when + | Mean fwd when − | n+/n− |
|---|---|---|---|---|---|---|
| Relative Strength Index (14) | +0.1068 | -0.1143 | -0.0821 | 0.21% | n/a | 11557/0 |
| d_Performance (Month) | +0.1064 | +0.2898 | -0.1446 | 0.15% | 0.43% | 8741/2593 |
| Short Float | -0.0972 | +0.0659 | -0.2033 | 0.15% | n/a | 5701/0 |
| d_Beta | -0.0923 | -0.0155 | -0.0653 | 0.94% | 0.49% | 2119/1461 |
| upside_pct_lvl | +0.0904 | +0.4449 | -0.2931 | -0.21% | -1.09% | 4360/285 |
| d_Performance (Week) | +0.0881 | +0.3655 | -0.1752 | 0.39% | -0.51% | 9174/2282 |
| Performance (Month) | +0.0720 | -0.0399 | +0.1328 | 0.53% | 0.06% | 3699/7742 |
| d_200-Day Simple Moving Average | +0.0634 | +0.2453 | -0.1430 | 0.14% | 0.44% | 8780/2759 |
| d_Performance (YTD) | +0.0634 | +0.1909 | -0.1084 | 0.14% | 0.50% | 8667/2649 |
| d_50-Day Simple Moving Average | +0.0561 | +0.2756 | -0.1770 | 0.13% | 0.48% | 8852/2702 |
| d_Performance (Quarter) | -0.0532 | +0.1304 | -0.1842 | -0.02% | 1.02% | 8961/2023 |
| true_ret | +0.0529 | +0.2570 | -0.1600 | 0.12% | -0.36% | 8600/2603 |
| d_Price | +0.0522 | +0.0272 | +0.0300 | 0.12% | -0.36% | 8600/2603 |
| d_Short Float | +0.0409 | +0.0091 | +0.0272 | 0.71% | 27.72% | 41/77 |
| d_Analyst Recom | -0.0408 | -0.0073 | -0.0398 | -1.38% | -0.22% | 67/69 |
| d_20-Day Simple Moving Average | +0.0394 | +0.2805 | -0.2014 | 0.35% | -0.33% | 9169/2390 |
| Institutional Transactions | +0.0374 | +0.0916 | -0.0421 | -0.17% | 0.83% | 3211/1829 |
| Relative Volume | -0.0368 | +0.0888 | -0.0403 | 0.22% | n/a | 11423/0 |
| d_Relative Strength Index (14) | +0.0359 | -0.2480 | +0.2627 | 0.13% | 0.47% | 8645/2648 |
| d_EPS Surprise | -0.0345 | -0.0363 | +0.0131 | -1.61% | 4.45% | 3/3 |
| d_Profit Margin | -0.0340 | -0.0505 | -0.0109 | -5.15% | 2.78% | 4/7 |
| Performance (Week) | -0.0334 | -0.1784 | +0.0331 | -0.15% | 0.59% | 5697/5720 |
| d_Target Price | +0.0324 | +0.0370 | +0.0257 | 0.17% | -0.80% | 108/136 |
| d_Sales Growth Quarter Over Quarter | +0.0273 | -0.0069 | +0.0272 | 6.64% | 1.53% | 4/5 |
| d_Average Volume | -0.0262 | +0.0174 | +0.0260 | 0.48% | -0.05% | 5582/5455 |

## Combinations

| Pattern | n | Mean long fwd | Hit up |
|---|---|---|---|
| true_ret>3% & DOWNTREND | 711 | 0.39% | 32.3% |
| true_ret>3% & UPTREND | 543 | 1.21% | 37.9% |
| true_ret>3% & MIXED | 381 | 3.18% | 42.8% |

## Risk dominance probes

| State | n | Mean long fwd | Mean fwd if score top quintile |
|---|---|---|---|
| EXTENDED | 162 | 1.68% | 3.81% |
| WASHED | 1115 | 1.69% | 0.05% |

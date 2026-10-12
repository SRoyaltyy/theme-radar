# Factor attribution — signal 2026-10-07 → prediction day 2026-10-12

## Trade window (read this first)

| Role | Date | Meaning |
|------|------|---------|
| **Signal as-of** | **2026-10-07** | Features/scores formed from this snapshot (and deltas vs **2026-10-06**). Only data on/before this date. |
| **Prediction day** | **2026-10-12** | The trading day the forward return is for (exit snapshot). |
| **Entry price** | Price @ 2026-10-07 | Long: buy here; short: sell here. |
| **Exit price** | Price @ 2026-10-12 | Close proxy on prediction day. |
| **Return column** | `fwd_3d` | Long: exit/entry − 1; short = opposite. |

Graded **n=11690** names with valid entry and exit prices.

Provisional until multiple signal dates agree.

_Column guide: **IC** = Spearman(feature, long forward return); **IC↑** / **IC↓** = IC among names that went up / down._

## Score calibration (long fwd)
- Spearman IC(total_score, fwd_3d) = **0.0717**

| Quintile | Mean long fwd | Hit up>1.5% | n |
|---|---|---|---|
| 1 | -0.19% | 24.4% | 2625 |
| 2 | -0.70% | 15.8% | 2326 |
| 3 | -0.25% | 17.3% | 2532 |
| 4 | -0.18% | 16.1% | 1878 |
| 5 | 1.93% | 35.6% | 2329 |

## Top |IC| features

| Feature | IC | IC↑ | IC↓ | Mean fwd when + | Mean fwd when − | n+/n− |
|---|---|---|---|---|---|---|
| upside_pct_lvl | -0.3341 | +0.1563 | -0.4234 | 0.03% | 0.28% | 4381/251 |
| d_Performance (Month) | +0.2141 | +0.0428 | +0.2552 | 1.90% | -1.28% | 5084/6317 |
| d_Forward P/E | +0.1880 | +0.1387 | +0.1667 | 1.07% | 0.13% | 785/2160 |
| d_Performance (Quarter) | +0.1699 | -0.0896 | +0.2088 | 1.87% | -0.22% | 2266/8847 |
| d_20-Day Simple Moving Average | +0.1468 | -0.0919 | +0.2050 | 1.32% | -0.34% | 3265/8334 |
| d_50-Day Simple Moving Average | +0.1462 | -0.1243 | +0.2199 | 1.51% | -0.34% | 2942/8653 |
| true_ret | +0.1437 | -0.1446 | +0.2595 | 1.05% | -0.49% | 2495/8607 |
| d_Performance (Week) | +0.1214 | -0.0602 | +0.1816 | 0.15% | 0.05% | 4018/7441 |
| d_200-Day Simple Moving Average | +0.1111 | -0.1305 | +0.1704 | 1.67% | -0.34% | 2747/8800 |
| d_Performance (YTD) | +0.1068 | -0.1274 | +0.1634 | 1.83% | -0.38% | 2582/8705 |
| Relative Strength Index (14) | -0.1003 | -0.0307 | +0.1409 | 0.13% | n/a | 11600/0 |
| d_Beta | +0.0958 | +0.0007 | +0.1366 | 1.27% | 0.37% | 984/1603 |
| Institutional Transactions | -0.0815 | +0.0165 | -0.1175 | 1.72% | -0.40% | 3242/1800 |
| Performance (Week) | +0.0760 | -0.0154 | +0.1509 | -0.13% | 0.44% | 6199/5308 |
| Relative Volume | +0.0616 | +0.0644 | -0.0182 | 0.13% | n/a | 11429/0 |
| d_Relative Strength Index (14) | +0.0472 | +0.0609 | -0.0853 | 1.74% | -0.39% | 2614/8680 |
| d_Sales Year Over Year TTM | +0.0432 | +0.0690 | +0.0117 | 5.94% | -1.70% | 5/3 |
| d_Market Cap | -0.0365 | +0.0930 | -0.0494 | 2.40% | 0.18% | 1665/4054 |
| Short Float | -0.0343 | +0.2201 | -0.1605 | 0.93% | n/a | 5681/0 |
| d_Relative Volume | +0.0338 | +0.0219 | +0.0458 | 0.73% | -0.43% | 5581/5636 |
| d_Price | +0.0328 | -0.0566 | +0.0029 | 1.05% | -0.49% | 2495/8607 |
| d_Institutional Ownership | +0.0276 | +0.0160 | -0.0163 | 0.27% | -0.17% | 517/497 |
| d_Sales Growth Quarter Over Quarter | +0.0262 | +0.0108 | +0.0115 | 4.30% | -0.04% | 6/3 |
| d_EPS Surprise | -0.0262 | -0.0542 | +0.0131 | 1.37% | 3.86% | 2/6 |
| d_Short Float | -0.0234 | -0.0230 | -0.0196 | -5.04% | -0.33% | 23/44 |

## Combinations

| Pattern | n | Mean long fwd | Hit up |
|---|---|---|---|
| true_ret>3% & DOWNTREND | 223 | 7.70% | 32.7% |
| true_ret>3% & UPTREND | 110 | -3.33% | 33.6% |
| true_ret>3% & MIXED | 88 | 7.25% | 34.1% |

## Risk dominance probes

| State | n | Mean long fwd | Mean fwd if score top quintile |
|---|---|---|---|
| EXTENDED | 182 | -4.13% | -4.57% |
| WASHED | 1833 | 1.15% | 4.01% |

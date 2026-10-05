# Factor attribution — signal 2026-09-30 → prediction day 2026-10-05

## Trade window (read this first)

| Role | Date | Meaning |
|------|------|---------|
| **Signal as-of** | **2026-09-30** | Features/scores formed from this snapshot (and deltas vs **2026-09-29**). Only data on/before this date. |
| **Prediction day** | **2026-10-05** | The trading day the forward return is for (exit snapshot). |
| **Entry price** | Price @ 2026-09-30 | Long: buy here; short: sell here. |
| **Exit price** | Price @ 2026-10-05 | Close proxy on prediction day. |
| **Return column** | `fwd_3d` | Long: exit/entry − 1; short = opposite. |

Graded **n=11668** names with valid entry and exit prices.

Provisional until multiple signal dates agree.

_Column guide: **IC** = Spearman(feature, long forward return); **IC↑** / **IC↓** = IC among names that went up / down._

## Score calibration (long fwd)
- Spearman IC(total_score, fwd_3d) = **0.0472**

| Quintile | Mean long fwd | Hit up>1.5% | n |
|---|---|---|---|
| 1 | 1.03% | 31.9% | 2445 |
| 2 | 0.97% | 27.0% | 2615 |
| 3 | 2.57% | 35.8% | 2499 |
| 4 | 2.14% | 40.3% | 1934 |
| 5 | 1.35% | 40.0% | 2175 |

## Top |IC| features

| Feature | IC | IC↑ | IC↓ | Mean fwd when + | Mean fwd when − | n+/n− |
|---|---|---|---|---|---|---|
| upside_pct_lvl | -0.2694 | +0.1832 | -0.4506 | 1.51% | 2.75% | 4399/233 |
| Performance (Month) | +0.1890 | -0.0017 | +0.2931 | 1.81% | 1.53% | 3052/8439 |
| Relative Strength Index (14) | +0.1829 | +0.1592 | -0.1738 | 1.60% | n/a | 11570/0 |
| d_Beta | -0.1046 | -0.0449 | -0.0964 | 2.88% | 2.00% | 1567/855 |
| d_Forward P/E | +0.0994 | +0.1116 | -0.0047 | 2.35% | 1.17% | 896/2050 |
| d_Average Volume | -0.0879 | -0.1319 | +0.0697 | 2.06% | 1.29% | 4795/6257 |
| d_20-Day Simple Moving Average | -0.0854 | -0.0888 | -0.0174 | 2.31% | 1.15% | 4506/7026 |
| d_Institutional Ownership | +0.0781 | -0.0229 | +0.0880 | 1.53% | 5.83% | 621/281 |
| d_Price | -0.0776 | -0.0052 | -0.0922 | 1.62% | 1.09% | 3735/7337 |
| Short Float | +0.0753 | +0.1845 | -0.2031 | 2.13% | n/a | 5683/0 |
| Institutional Transactions | -0.0735 | +0.0070 | -0.1363 | 2.17% | 2.78% | 3232/1810 |
| d_Volatility (Month) | -0.0703 | -0.0844 | -0.0441 | 1.40% | 2.09% | 5449/4738 |
| d_Market Cap | -0.0611 | +0.1351 | -0.1062 | 3.44% | 1.28% | 2145/3562 |
| d_Short Ratio | +0.0606 | +0.1045 | -0.0716 | 1.20% | 1.39% | 4346/3039 |
| d_50-Day Simple Moving Average | -0.0539 | -0.0576 | -0.0052 | 2.58% | 1.06% | 4139/7400 |
| d_200-Day Simple Moving Average | -0.0533 | -0.0541 | -0.0079 | 2.68% | 1.05% | 3967/7562 |
| d_Performance (Quarter) | +0.0531 | +0.0873 | +0.0341 | 2.05% | 1.20% | 5250/5802 |
| Performance (Week) | +0.0528 | -0.1144 | +0.1922 | 1.61% | 1.63% | 2675/8815 |
| d_Relative Strength Index (14) | -0.0457 | +0.0364 | -0.0448 | 2.52% | 1.18% | 3860/7410 |
| d_Performance (Month) | -0.0428 | -0.0554 | -0.0114 | 1.90% | 1.35% | 5593/5737 |
| d_Short Float | +0.0376 | -0.0020 | +0.0408 | 0.89% | 24.36% | 26/63 |
| d_Performance (YTD) | -0.0325 | -0.0477 | +0.0150 | 2.55% | 1.21% | 3832/7421 |
| d_Insider Transactions | -0.0297 | -0.0105 | -0.0132 | 7.91% | 0.26% | 105/167 |
| d_Sales Year Over Year TTM | +0.0196 | +0.0219 | +0.0351 | 1.20% | -2.42% | 10/11 |
| d_Analyst Recom | +0.0185 | -0.0072 | +0.0396 | 2.63% | 1.09% | 72/66 |

## Combinations

| Pattern | n | Mean long fwd | Hit up |
|---|---|---|---|
| true_ret>3% & DOWNTREND | 283 | 6.78% | 30.0% |
| true_ret>3% & UPTREND | 150 | 3.87% | 54.7% |
| true_ret>3% & MIXED | 120 | 0.09% | 39.2% |

## Risk dominance probes

| State | n | Mean long fwd | Mean fwd if score top quintile |
|---|---|---|---|
| EXTENDED | 172 | 1.47% | 4.51% |
| WASHED | 2591 | 1.69% | 3.99% |

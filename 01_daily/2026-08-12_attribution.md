# Factor attribution — signal 2026-08-12 → prediction day 2026-08-17

## Trade window (read this first)

| Role | Date | Meaning |
|------|------|---------|
| **Signal as-of** | **2026-08-12** | Features/scores formed from this snapshot (and deltas vs **2026-08-11**). Only data on/before this date. |
| **Prediction day** | **2026-08-17** | The trading day the forward return is for (exit snapshot). |
| **Entry price** | Price @ 2026-08-12 | Long: buy here; short: sell here. |
| **Exit price** | Price @ 2026-08-17 | Close proxy on prediction day. |
| **Return column** | `fwd_3d` | Long: exit/entry − 1; short = opposite. |

Graded **n=11530** names with valid entry and exit prices.

Provisional until multiple signal dates agree.

_Column guide: **IC** = Spearman(feature, long forward return); **IC↑** / **IC↓** = IC among names that went up / down._

## Score calibration (long fwd)
- Spearman IC(total_score, fwd_3d) = **0.0878**

| Quintile | Mean long fwd | Hit up>1.5% | n |
|---|---|---|---|
| 1 | 3.72% | 24.0% | 2324 |
| 2 | -0.09% | 10.6% | 3040 |
| 3 | 0.29% | 11.2% | 1645 |
| 4 | 0.51% | 15.4% | 2357 |
| 5 | 1.67% | 33.9% | 2164 |

## Top |IC| features

| Feature | IC | IC↑ | IC↓ | Mean fwd when + | Mean fwd when − | n+/n− |
|---|---|---|---|---|---|---|
| d_Price | +0.1840 | +0.0290 | +0.1446 | 0.74% | 2.06% | 7102/3867 |
| d_Performance (YTD) | +0.1667 | +0.1251 | +0.0949 | 0.72% | 2.05% | 7195/3938 |
| true_ret | +0.1605 | +0.1344 | +0.0937 | 0.74% | 2.06% | 7102/3867 |
| d_Performance (Week) | +0.1574 | +0.2113 | +0.0403 | 1.21% | 1.19% | 7134/4146 |
| d_50-Day Simple Moving Average | +0.1574 | +0.1662 | +0.0505 | 1.37% | 0.90% | 7257/4156 |
| d_200-Day Simple Moving Average | +0.1521 | +0.1484 | +0.0541 | 1.10% | 1.28% | 7327/4062 |
| d_20-Day Simple Moving Average | +0.1513 | +0.1410 | +0.0761 | 1.52% | 0.68% | 6990/4430 |
| d_Relative Strength Index (14) | +0.1426 | -0.0496 | +0.1690 | 0.71% | 2.06% | 7159/3946 |
| d_Performance (Quarter) | +0.0981 | +0.1533 | -0.0332 | 1.17% | 1.18% | 7469/3301 |
| Performance (Week) | +0.0949 | +0.1561 | -0.0303 | 0.43% | 2.54% | 7237/4090 |
| d_Forward P/E | +0.0898 | +0.0518 | +0.0500 | 0.47% | -0.14% | 1625/1342 |
| d_Market Cap | +0.0809 | -0.0093 | +0.0766 | 0.83% | 3.19% | 3029/2653 |
| d_Beta | +0.0638 | +0.0770 | +0.0242 | 0.89% | 6.21% | 1987/1247 |
| Institutional Transactions | +0.0498 | +0.0665 | -0.0375 | 1.36% | 2.88% | 2517/2514 |
| d_Target Price | +0.0422 | -0.0147 | +0.0297 | 0.75% | 0.20% | 349/203 |
| d_Institutional Ownership | +0.0388 | -0.0531 | +0.0251 | 0.14% | 1.73% | 2136/1544 |
| d_Volatility (Month) | -0.0356 | -0.1156 | +0.0612 | 2.45% | 0.84% | 3454/5822 |
| d_Gross Margin | +0.0315 | -0.0319 | +0.0071 | 0.39% | -0.17% | 126/100 |
| d_Sales Year Over Year TTM | +0.0292 | +0.0040 | +0.0018 | 0.79% | -0.19% | 109/93 |
| Performance (Month) | -0.0268 | -0.0887 | +0.0115 | 0.30% | 2.60% | 6912/4379 |
| d_Profit Margin | +0.0224 | +0.0025 | +0.0059 | 0.62% | -0.34% | 133/106 |
| Relative Strength Index (14) | +0.0222 | -0.3346 | +0.1362 | 1.18% | n/a | 11420/0 |
| d_Short Ratio | +0.0178 | +0.0181 | -0.0047 | 1.07% | 1.12% | 5137/5835 |
| d_Sales Growth Quarter Over Quarter | +0.0161 | +0.0126 | +0.0075 | 0.57% | -0.38% | 112/110 |
| Short Float | -0.0138 | +0.1895 | -0.1760 | 1.96% | n/a | 5692/0 |

## Combinations

| Pattern | n | Mean long fwd | Hit up |
|---|---|---|---|
| true_ret>3% & DOWNTREND | 382 | 6.28% | 42.4% |
| true_ret>3% & UPTREND | 377 | 1.98% | 45.9% |
| true_ret>3% & MIXED | 296 | 3.17% | 52.4% |

## Risk dominance probes

| State | n | Mean long fwd | Mean fwd if score top quintile |
|---|---|---|---|
| EXTENDED | 324 | -0.90% | -2.39% |
| WASHED | 545 | 17.83% | 4.61% |

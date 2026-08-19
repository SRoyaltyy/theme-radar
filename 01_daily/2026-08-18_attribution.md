# Factor attribution — signal 2026-08-18 → prediction day 2026-08-19

## Trade window (read this first)

| Role | Date | Meaning |
|------|------|---------|
| **Signal as-of** | **2026-08-18** | Features/scores formed from this snapshot (and deltas vs **2026-08-17**). Only data on/before this date. |
| **Prediction day** | **2026-08-19** | The trading day the forward return is for (exit snapshot). |
| **Entry price** | Price @ 2026-08-18 | Long: buy here; short: sell here. |
| **Exit price** | Price @ 2026-08-19 | Close proxy on prediction day. |
| **Return column** | `fwd_1d` | Long: exit/entry − 1; short = opposite. |

Graded **n=11572** names with valid entry and exit prices.

Provisional until multiple signal dates agree.

_Column guide: **IC** = Spearman(feature, long forward return); **IC↑** / **IC↓** = IC among names that went up / down._

## Score calibration (long fwd)
- Spearman IC(total_score, fwd_1d) = **0.0486**

| Quintile | Mean long fwd | Hit up>1.5% | n |
|---|---|---|---|
| 1 | 1.24% | 31.0% | 2490 |
| 2 | 0.80% | 23.9% | 2144 |
| 3 | 2.29% | 14.6% | 2479 |
| 4 | 0.47% | 12.7% | 2242 |
| 5 | 1.41% | 40.7% | 2217 |

## Top |IC| features

| Feature | IC | IC↑ | IC↓ | Mean fwd when + | Mean fwd when − | n+/n− |
|---|---|---|---|---|---|---|
| Short Float | +0.1639 | +0.2902 | -0.1623 | 2.00% | n/a | 5699/0 |
| d_Forward P/E | +0.1473 | -0.0918 | +0.2867 | 0.96% | 0.21% | 1095/1855 |
| d_Price | +0.1255 | +0.0251 | +0.1214 | 2.45% | 0.80% | 3444/7526 |
| upside_pct_lvl | +0.1207 | +0.2903 | -0.1823 | 1.51% | 0.95% | 4331/318 |
| d_200-Day Simple Moving Average | +0.1128 | -0.0595 | +0.2060 | 2.40% | 0.76% | 3654/7758 |
| d_Relative Strength Index (14) | +0.1115 | +0.1515 | -0.0137 | 2.37% | 0.82% | 3555/7545 |
| d_Performance (YTD) | +0.1016 | -0.0784 | +0.2044 | 2.39% | 0.79% | 3542/7594 |
| d_Performance (Week) | +0.0984 | -0.0910 | +0.2444 | 2.38% | 0.78% | 3709/7565 |
| Performance (Week) | -0.0921 | -0.1550 | +0.0267 | 0.69% | 1.75% | 4902/6438 |
| true_ret | +0.0850 | -0.1085 | +0.2340 | 2.45% | 0.80% | 3444/7526 |
| d_20-Day Simple Moving Average | +0.0830 | -0.1030 | +0.2273 | 2.41% | 0.77% | 3562/7892 |
| d_50-Day Simple Moving Average | +0.0808 | -0.1122 | +0.2166 | 2.35% | 0.81% | 3504/7908 |
| d_Performance (Month) | +0.0745 | -0.0345 | +0.1311 | 1.89% | 0.84% | 4956/6309 |
| d_Performance (Quarter) | +0.0740 | -0.0227 | +0.1171 | 2.61% | 0.80% | 3530/7266 |
| d_Average Volume | -0.0705 | -0.1039 | -0.0490 | 1.77% | 0.98% | 4642/6341 |
| d_Short Ratio | +0.0697 | +0.0959 | +0.0116 | 1.11% | 1.33% | 4089/2715 |
| d_Market Cap | +0.0673 | -0.0502 | +0.1391 | 3.19% | 1.23% | 2196/3508 |
| d_Volatility (Month) | +0.0533 | -0.1464 | +0.1746 | 3.16% | 0.63% | 3037/6596 |
| Institutional Transactions | -0.0510 | +0.0084 | -0.0775 | 2.30% | 2.06% | 2690/2353 |
| d_Beta | -0.0466 | -0.0794 | +0.0180 | 0.83% | 3.56% | 1854/1961 |
| d_EPS Surprise | -0.0243 | -0.0239 | -0.0292 | -0.34% | 1.11% | 25/30 |
| d_Relative Volume | -0.0217 | -0.0733 | +0.0193 | 0.63% | 1.92% | 5401/5721 |
| Relative Strength Index (14) | -0.0203 | -0.1435 | +0.2021 | 1.29% | n/a | 11449/0 |
| d_Insider Transactions | +0.0179 | +0.0138 | +0.0276 | 0.77% | 0.29% | 280/372 |
| d_Profit Margin | -0.0156 | -0.0138 | -0.0123 | -2.39% | -0.52% | 13/19 |

## Combinations

| Pattern | n | Mean long fwd | Hit up |
|---|---|---|---|
| true_ret>3% & DOWNTREND | 248 | 21.20% | 42.3% |
| true_ret>3% & UPTREND | 204 | 1.33% | 47.1% |
| true_ret>3% & MIXED | 147 | 0.55% | 45.6% |

## Risk dominance probes

| State | n | Mean long fwd | Mean fwd if score top quintile |
|---|---|---|---|
| EXTENDED | 236 | -0.79% | -2.00% |
| WASHED | 523 | 12.38% | 1.41% |

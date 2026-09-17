# Factor attribution — signal 2026-09-15 → prediction day 2026-09-17

## Trade window (read this first)

| Role | Date | Meaning |
|------|------|---------|
| **Signal as-of** | **2026-09-15** | Features/scores formed from this snapshot (and deltas vs **2026-09-14**). Only data on/before this date. |
| **Prediction day** | **2026-09-17** | The trading day the forward return is for (exit snapshot). |
| **Entry price** | Price @ 2026-09-15 | Long: buy here; short: sell here. |
| **Exit price** | Price @ 2026-09-17 | Close proxy on prediction day. |
| **Return column** | `fwd_2d` | Long: exit/entry − 1; short = opposite. |

Graded **n=11620** names with valid entry and exit prices.

Provisional until multiple signal dates agree.

_Column guide: **IC** = Spearman(feature, long forward return); **IC↑** / **IC↓** = IC among names that went up / down._

## Score calibration (long fwd)
- Spearman IC(total_score, fwd_2d) = **-0.1290**

| Quintile | Mean long fwd | Hit up>1.5% | n |
|---|---|---|---|
| 1 | 4.07% | 31.8% | 2931 |
| 2 | 1.08% | 23.2% | 2398 |
| 3 | 0.45% | 18.0% | 1730 |
| 4 | 0.49% | 20.3% | 2266 |
| 5 | 0.46% | 27.8% | 2295 |

## Top |IC| features

| Feature | IC | IC↑ | IC↓ | Mean fwd when + | Mean fwd when − | n+/n− |
|---|---|---|---|---|---|---|
| Performance (Week) | -0.2995 | -0.4621 | -0.0130 | 0.60% | 1.76% | 2378/9092 |
| d_Performance (Quarter) | -0.2961 | -0.3317 | -0.0670 | 0.38% | 1.84% | 3074/7882 |
| d_Performance (Week) | -0.2439 | -0.2451 | -0.0802 | 0.38% | 2.54% | 5356/6026 |
| upside_pct_lvl | +0.1473 | +0.3415 | -0.2294 | 1.20% | 0.19% | 4361/278 |
| d_Performance (YTD) | -0.1261 | -0.2126 | +0.0100 | 0.49% | 1.88% | 2747/8497 |
| true_ret | -0.1259 | -0.2517 | +0.0475 | 0.43% | 1.71% | 2693/8406 |
| d_200-Day Simple Moving Average | -0.1238 | -0.2105 | +0.0008 | 0.55% | 1.84% | 2870/8591 |
| d_Beta | +0.1236 | +0.0957 | +0.0468 | 3.68% | 1.97% | 1886/1551 |
| Performance (Month) | -0.1178 | -0.2949 | +0.0748 | 1.45% | 1.54% | 2721/8709 |
| d_50-Day Simple Moving Average | -0.1028 | -0.1909 | +0.0155 | 0.66% | 1.85% | 3155/8324 |
| d_Price | -0.0996 | -0.0732 | -0.0867 | 0.43% | 1.71% | 2693/8406 |
| Relative Strength Index (14) | -0.0942 | +0.1123 | -0.0821 | 1.51% | n/a | 11529/0 |
| d_Performance (Month) | -0.0912 | -0.2097 | +0.0275 | 0.64% | 1.93% | 3440/7855 |
| d_Relative Strength Index (14) | -0.0771 | +0.1026 | -0.0820 | 0.48% | 1.88% | 2755/8473 |
| d_20-Day Simple Moving Average | -0.0750 | -0.1501 | +0.0312 | 0.78% | 1.86% | 3636/7838 |
| Relative Volume | -0.0468 | -0.0153 | -0.0327 | 1.53% | n/a | 11385/0 |
| d_Relative Volume | -0.0400 | -0.0567 | +0.0143 | 0.79% | 2.23% | 5449/5787 |
| Institutional Transactions | +0.0348 | +0.1148 | -0.0532 | 2.60% | 1.86% | 3210/1829 |
| d_Total Debt/Equity | +0.0316 | +0.0531 | -0.0008 | 2.64% | -3.49% | 13/6 |
| d_EPS Surprise | -0.0225 | -0.0339 | n/a | 2.54% | 9.10% | 5/6 |
| d_Sales Year Over Year TTM | -0.0212 | +0.0076 | -0.0366 | -0.29% | 5.37% | 11/9 |
| d_Target Price | -0.0209 | -0.0014 | -0.0294 | -0.17% | 0.89% | 179/168 |
| d_Forward P/E | -0.0184 | +0.0000 | -0.0327 | 0.01% | 0.10% | 1008/1922 |
| d_Average Volume | -0.0181 | -0.0458 | -0.0217 | 1.91% | 1.17% | 5700/5326 |
| d_Short Ratio | +0.0178 | +0.0294 | +0.0137 | 1.21% | 1.74% | 3362/3766 |

## Combinations

| Pattern | n | Mean long fwd | Hit up |
|---|---|---|---|
| true_ret>3% & DOWNTREND | 169 | 0.53% | 36.1% |
| true_ret>3% & UPTREND | 196 | 0.85% | 37.8% |
| true_ret>3% & MIXED | 70 | -0.40% | 35.7% |

## Risk dominance probes

| State | n | Mean long fwd | Mean fwd if score top quintile |
|---|---|---|---|
| EXTENDED | 157 | 4.18% | 9.16% |
| WASHED | 1979 | 3.80% | 1.21% |

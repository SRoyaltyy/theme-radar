# Factor attribution — signal 2026-09-15 → prediction day 2026-09-18

## Trade window (read this first)

| Role | Date | Meaning |
|------|------|---------|
| **Signal as-of** | **2026-09-15** | Features/scores formed from this snapshot (and deltas vs **2026-09-14**). Only data on/before this date. |
| **Prediction day** | **2026-09-18** | The trading day the forward return is for (exit snapshot). |
| **Entry price** | Price @ 2026-09-15 | Long: buy here; short: sell here. |
| **Exit price** | Price @ 2026-09-18 | Close proxy on prediction day. |
| **Return column** | `fwd_3d` | Long: exit/entry − 1; short = opposite. |

Graded **n=11619** names with valid entry and exit prices.

Provisional until multiple signal dates agree.

_Column guide: **IC** = Spearman(feature, long forward return); **IC↑** / **IC↓** = IC among names that went up / down._

## Score calibration (long fwd)
- Spearman IC(total_score, fwd_3d) = **-0.1450**

| Quintile | Mean long fwd | Hit up>1.5% | n |
|---|---|---|---|
| 1 | 5.15% | 33.7% | 2931 |
| 2 | 1.35% | 24.8% | 2398 |
| 3 | 0.35% | 17.8% | 1730 |
| 4 | 0.32% | 20.0% | 2265 |
| 5 | -0.21% | 23.5% | 2295 |

## Top |IC| features

| Feature | IC | IC↑ | IC↓ | Mean fwd when + | Mean fwd when − | n+/n− |
|---|---|---|---|---|---|---|
| d_Performance (Quarter) | -0.3119 | -0.4066 | -0.0596 | -0.29% | 2.24% | 3074/7881 |
| Performance (Week) | -0.2725 | -0.4897 | -0.0118 | -0.04% | 2.11% | 2377/9092 |
| d_Performance (Week) | -0.2620 | -0.2985 | -0.1281 | -0.14% | 3.28% | 5356/6025 |
| upside_pct_lvl | +0.1586 | +0.3695 | -0.2324 | 0.93% | -0.63% | 4360/278 |
| d_Performance (YTD) | -0.1280 | -0.2744 | +0.0394 | 0.23% | 2.19% | 2747/8496 |
| d_200-Day Simple Moving Average | -0.1249 | -0.2747 | +0.0371 | 0.22% | 2.16% | 2870/8590 |
| true_ret | -0.1230 | -0.3098 | +0.0840 | 0.16% | 2.02% | 2693/8405 |
| d_Performance (Month) | -0.1194 | -0.3063 | +0.0396 | 0.15% | 2.35% | 3440/7854 |
| d_Beta | +0.1071 | +0.0475 | +0.0800 | 4.27% | 2.57% | 1886/1550 |
| d_Relative Strength Index (14) | -0.1052 | +0.0156 | -0.0832 | 0.22% | 2.17% | 2755/8472 |
| d_50-Day Simple Moving Average | -0.1048 | -0.2541 | +0.0521 | 0.33% | 2.18% | 3155/8323 |
| d_Price | -0.1009 | -0.1334 | -0.0561 | 0.16% | 2.02% | 2693/8405 |
| d_20-Day Simple Moving Average | -0.0763 | -0.2008 | +0.0688 | 0.57% | 2.18% | 3636/7837 |
| Relative Volume | -0.0697 | -0.0145 | -0.0307 | 1.68% | n/a | 11384/0 |
| Short Float | -0.0550 | +0.2272 | -0.2418 | 1.73% | n/a | 5698/0 |
| Performance (Month) | -0.0497 | -0.2193 | +0.0946 | 2.11% | 1.52% | 2720/8709 |
| Institutional Transactions | +0.0488 | +0.1117 | -0.0333 | 2.42% | 2.20% | 3210/1829 |
| d_Relative Volume | -0.0425 | -0.0663 | +0.0103 | 1.18% | 2.18% | 5449/5786 |
| Relative Strength Index (14) | -0.0413 | +0.1474 | -0.1661 | 1.65% | n/a | 11528/0 |
| d_Total Debt/Equity | +0.0411 | +0.0591 | +0.0037 | 5.00% | -4.26% | 13/6 |
| d_Forward P/E | -0.0338 | -0.0399 | +0.0118 | -0.52% | -0.47% | 1008/1922 |
| d_Average Volume | -0.0252 | -0.0507 | -0.0022 | 2.26% | 1.11% | 5699/5326 |
| d_Sales Year Over Year TTM | -0.0228 | +0.0002 | -0.0415 | -1.17% | 8.34% | 11/9 |
| d_EPS Surprise | -0.0223 | -0.0376 | -0.0044 | 1.59% | 12.29% | 5/6 |
| d_Short Ratio | +0.0163 | +0.0223 | -0.0066 | 0.98% | 1.65% | 3362/3766 |

## Combinations

| Pattern | n | Mean long fwd | Hit up |
|---|---|---|---|
| true_ret>3% & DOWNTREND | 169 | -0.52% | 34.9% |
| true_ret>3% & UPTREND | 196 | -0.49% | 30.1% |
| true_ret>3% & MIXED | 70 | -0.54% | 37.1% |

## Risk dominance probes

| State | n | Mean long fwd | Mean fwd if score top quintile |
|---|---|---|---|
| EXTENDED | 157 | 5.87% | 6.59% |
| WASHED | 1979 | 4.32% | 0.50% |

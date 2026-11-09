# Factor attribution — signal 2026-11-04 → prediction day 2026-11-09

## Trade window (read this first)

| Role | Date | Meaning |
|------|------|---------|
| **Signal as-of** | **2026-11-04** | Features/scores formed from this snapshot (and deltas vs **2026-11-03**). Only data on/before this date. |
| **Prediction day** | **2026-11-09** | The trading day the forward return is for (exit snapshot). |
| **Entry price** | Price @ 2026-11-04 | Long: buy here; short: sell here. |
| **Exit price** | Price @ 2026-11-09 | Close proxy on prediction day. |
| **Return column** | `fwd_3d` | Long: exit/entry − 1; short = opposite. |

Graded **n=11720** names with valid entry and exit prices.

Provisional until multiple signal dates agree.

_Column guide: **IC** = Spearman(feature, long forward return); **IC↑** / **IC↓** = IC among names that went up / down._

## Score calibration (long fwd)
- Spearman IC(total_score, fwd_3d) = **0.0039**

| Quintile | Mean long fwd | Hit up>1.5% | n |
|---|---|---|---|
| 1 | 2.93% | 22.0% | 2350 |
| 2 | 2.57% | 10.4% | 2723 |
| 3 | -0.32% | 10.5% | 2088 |
| 4 | -0.02% | 19.9% | 2614 |
| 5 | 0.54% | 24.5% | 1945 |

## Top |IC| features

| Feature | IC | IC↑ | IC↓ | Mean fwd when + | Mean fwd when − | n+/n− |
|---|---|---|---|---|---|---|
| d_Performance (Quarter) | -0.0963 | +0.0290 | -0.0441 | 0.06% | 4.80% | 8221/2977 |
| d_20-Day Simple Moving Average | -0.0791 | +0.1321 | -0.0941 | 0.95% | 2.08% | 8769/2864 |
| Relative Strength Index (14) | +0.0787 | -0.3161 | +0.2898 | 1.22% | n/a | 11648/0 |
| Performance (Week) | +0.0732 | -0.1467 | +0.2067 | 0.12% | 2.43% | 5971/5622 |
| Performance (Month) | +0.0717 | -0.2695 | +0.2748 | -0.64% | 2.91% | 5462/6090 |
| d_Performance (Month) | -0.0701 | +0.0910 | -0.0649 | 0.24% | 3.63% | 8045/3412 |
| d_200-Day Simple Moving Average | -0.0627 | +0.0648 | -0.0194 | 0.68% | 2.18% | 8554/3048 |
| d_Forward P/E | -0.0605 | -0.0187 | -0.0521 | -1.21% | -0.21% | 2159/816 |
| d_50-Day Simple Moving Average | -0.0589 | +0.1058 | -0.0484 | 0.71% | 2.78% | 8711/2917 |
| true_ret | -0.0586 | +0.0690 | -0.0360 | -0.11% | 2.67% | 8347/2968 |
| d_Price | -0.0566 | -0.0703 | +0.1455 | -0.11% | 2.67% | 8347/2968 |
| d_Performance (YTD) | -0.0497 | +0.0392 | +0.0340 | -0.13% | 2.40% | 8411/3006 |
| d_Average Volume | +0.0420 | +0.0255 | -0.0072 | 2.02% | 0.61% | 5597/5491 |
| Institutional Transactions | +0.0413 | +0.0888 | -0.0581 | 4.82% | 1.23% | 3189/1829 |
| d_Short Ratio | -0.0361 | -0.0270 | +0.0159 | 0.46% | -0.56% | 3440/3487 |
| Short Float | -0.0346 | +0.3580 | -0.1961 | 2.72% | n/a | 5630/0 |
| d_Total Debt/Equity | +0.0231 | -0.0363 | +0.0300 | -0.57% | -1.81% | 95/79 |
| d_Performance (Week) | -0.0230 | +0.0043 | +0.0216 | 0.58% | 2.60% | 7846/3715 |
| d_Volatility (Month) | -0.0212 | +0.0689 | -0.0729 | 2.43% | 0.87% | 4498/5081 |
| d_Insider Transactions | +0.0207 | +0.0351 | -0.0265 | -1.22% | -1.55% | 94/218 |
| d_Sales Growth Quarter Over Quarter | -0.0153 | +0.0164 | +0.0064 | -1.53% | -0.85% | 86/107 |
| d_Target Price | -0.0142 | -0.0282 | +0.0151 | -0.74% | -0.09% | 290/300 |
| d_Analyst Recom | -0.0124 | -0.0066 | +0.0131 | -1.23% | 0.28% | 97/76 |
| d_Beta | +0.0120 | +0.0150 | +0.0370 | 8.66% | -1.60% | 1783/1067 |
| Relative Volume | +0.0099 | +0.1743 | -0.0686 | 1.25% | n/a | 11470/0 |

## Combinations

| Pattern | n | Mean long fwd | Hit up |
|---|---|---|---|
| true_ret>3% & DOWNTREND | 1013 | 5.49% | 38.0% |
| true_ret>3% & UPTREND | 1096 | -1.39% | 19.7% |
| true_ret>3% & MIXED | 573 | -1.40% | 26.5% |

## Risk dominance probes

| State | n | Mean long fwd | Mean fwd if score top quintile |
|---|---|---|---|
| EXTENDED | 391 | -1.23% | -2.06% |
| WASHED | 1533 | 12.42% | 5.71% |

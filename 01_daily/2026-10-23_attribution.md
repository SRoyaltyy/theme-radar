# Factor attribution — signal 2026-10-23 → prediction day 2026-10-28

## Trade window (read this first)

| Role | Date | Meaning |
|------|------|---------|
| **Signal as-of** | **2026-10-23** | Features/scores formed from this snapshot (and deltas vs **2026-10-22**). Only data on/before this date. |
| **Prediction day** | **2026-10-28** | The trading day the forward return is for (exit snapshot). |
| **Entry price** | Price @ 2026-10-23 | Long: buy here; short: sell here. |
| **Exit price** | Price @ 2026-10-28 | Close proxy on prediction day. |
| **Return column** | `fwd_3d` | Long: exit/entry − 1; short = opposite. |

Graded **n=11745** names with valid entry and exit prices.

Provisional until multiple signal dates agree.

_Column guide: **IC** = Spearman(feature, long forward return); **IC↑** / **IC↓** = IC among names that went up / down._

## Score calibration (long fwd)
- Spearman IC(total_score, fwd_3d) = **-0.1140**

| Quintile | Mean long fwd | Hit up>1.5% | n |
|---|---|---|---|
| 1 | 8.26% | 48.3% | 2763 |
| 2 | 6.97% | 45.4% | 2050 |
| 3 | 2.80% | 24.7% | 2282 |
| 4 | 1.61% | 25.6% | 2306 |
| 5 | 2.08% | 39.7% | 2344 |

## Top |IC| features

| Feature | IC | IC↑ | IC↓ | Mean fwd when + | Mean fwd when − | n+/n− |
|---|---|---|---|---|---|---|
| Relative Strength Index (14) | -0.3969 | -0.4798 | +0.1925 | 4.46% | n/a | 11655/0 |
| Performance (Month) | -0.3805 | -0.5788 | +0.0885 | -0.39% | 7.64% | 4524/7025 |
| d_Beta | +0.3201 | +0.4529 | -0.1085 | 13.19% | -0.24% | 3320/2541 |
| d_Performance (Week) | +0.2637 | +0.4014 | -0.0785 | 4.19% | 5.03% | 6880/4617 |
| upside_pct_lvl | +0.2479 | +0.4248 | -0.2672 | 4.58% | -0.58% | 4289/341 |
| Performance (Week) | -0.2271 | -0.2752 | +0.0345 | 0.59% | 8.29% | 5684/5866 |
| Short Float | +0.1108 | +0.3489 | -0.0717 | 6.86% | n/a | 5652/0 |
| Institutional Transactions | +0.1029 | +0.1404 | +0.0208 | 5.92% | 12.28% | 3253/1788 |
| d_20-Day Simple Moving Average | +0.0831 | +0.1045 | +0.0320 | 3.32% | 5.28% | 4598/6973 |
| d_Relative Strength Index (14) | +0.0549 | +0.1998 | -0.0676 | 2.71% | 5.54% | 3799/7464 |
| d_Volatility (Month) | +0.0520 | +0.2351 | -0.1419 | 5.22% | 2.76% | 5806/4030 |
| d_Relative Volume | -0.0474 | -0.0748 | -0.0105 | 3.61% | 5.18% | 4136/7126 |
| d_Performance (Quarter) | +0.0416 | -0.0243 | +0.0920 | 2.96% | 5.29% | 3460/7696 |
| true_ret | -0.0405 | -0.0917 | +0.0919 | 2.31% | 5.46% | 3691/7401 |
| d_Analyst Recom | -0.0401 | -0.0258 | +0.0166 | -0.33% | 1.81% | 96/66 |
| d_Performance (YTD) | -0.0395 | -0.0574 | +0.0452 | 2.83% | 4.18% | 3781/7481 |
| d_Performance (Month) | -0.0328 | -0.0435 | +0.0322 | 4.08% | 4.95% | 5529/5898 |
| d_Target Price | -0.0298 | -0.0243 | +0.0002 | 1.09% | 2.24% | 267/248 |
| d_200-Day Simple Moving Average | -0.0279 | -0.0399 | +0.0412 | 4.94% | 4.13% | 4041/7526 |
| d_Forward P/E | +0.0199 | +0.0413 | +0.0596 | 1.06% | 0.94% | 1123/1821 |
| Relative Volume | +0.0188 | +0.0605 | -0.0015 | 4.57% | n/a | 11388/0 |
| d_50-Day Simple Moving Average | +0.0184 | +0.0105 | +0.0554 | 3.10% | 5.37% | 4448/7125 |
| d_Institutional Ownership | +0.0175 | +0.0165 | +0.0061 | 1.85% | 2.47% | 991/902 |
| d_Short Ratio | -0.0170 | -0.0729 | +0.0027 | 2.00% | 2.87% | 2542/4489 |
| d_Average Volume | +0.0168 | +0.0809 | -0.0406 | 5.90% | 2.65% | 6845/4189 |

## Combinations

| Pattern | n | Mean long fwd | Hit up |
|---|---|---|---|
| true_ret>3% & DOWNTREND | 390 | 7.50% | 57.4% |
| true_ret>3% & UPTREND | 231 | -0.46% | 38.5% |
| true_ret>3% & MIXED | 132 | 2.44% | 56.8% |

## Risk dominance probes

| State | n | Mean long fwd | Mean fwd if score top quintile |
|---|---|---|---|
| EXTENDED | 194 | -2.67% | -0.33% |
| WASHED | 1767 | 22.38% | 11.47% |

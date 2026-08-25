# Factor attribution — signal 2026-08-20 → prediction day 2026-08-25

## Trade window (read this first)

| Role | Date | Meaning |
|------|------|---------|
| **Signal as-of** | **2026-08-20** | Features/scores formed from this snapshot (and deltas vs **2026-08-19**). Only data on/before this date. |
| **Prediction day** | **2026-08-25** | The trading day the forward return is for (exit snapshot). |
| **Entry price** | Price @ 2026-08-20 | Long: buy here; short: sell here. |
| **Exit price** | Price @ 2026-08-25 | Close proxy on prediction day. |
| **Return column** | `fwd_3d` | Long: exit/entry − 1; short = opposite. |

Graded **n=11591** names with valid entry and exit prices.

Provisional until multiple signal dates agree.

_Column guide: **IC** = Spearman(feature, long forward return); **IC↑** / **IC↓** = IC among names that went up / down._

## Score calibration (long fwd)
- Spearman IC(total_score, fwd_3d) = **0.0387**

| Quintile | Mean long fwd | Hit up>1.5% | n |
|---|---|---|---|
| 1 | 6.76% | 34.2% | 2322 |
| 2 | 1.04% | 19.0% | 3302 |
| 3 | 4.34% | 22.3% | 1394 |
| 4 | 0.63% | 14.9% | 2339 |
| 5 | 6.84% | 41.8% | 2234 |

## Top |IC| features

| Feature | IC | IC↑ | IC↓ | Mean fwd when + | Mean fwd when − | n+/n− |
|---|---|---|---|---|---|---|
| d_Beta | +0.2109 | +0.2315 | +0.0643 | 7.91% | 10.68% | 2044/1418 |
| Performance (Month) | +0.1470 | +0.1622 | +0.0759 | 2.21% | 6.17% | 7081/4269 |
| Relative Strength Index (14) | +0.1183 | -0.0121 | +0.1229 | 3.67% | n/a | 11453/0 |
| Performance (Week) | +0.0970 | +0.0138 | +0.1039 | 3.78% | 3.64% | 3649/7747 |
| d_Performance (Quarter) | -0.0852 | -0.1885 | -0.0128 | 9.40% | 2.33% | 2206/8622 |
| Relative Volume | +0.0806 | +0.1389 | +0.0010 | 3.67% | n/a | 11324/0 |
| d_20-Day Simple Moving Average | -0.0730 | -0.1186 | -0.0007 | 7.07% | 2.27% | 3256/8211 |
| upside_pct_lvl | +0.0671 | +0.3461 | -0.3316 | 3.89% | 0.55% | 4313/334 |
| d_50-Day Simple Moving Average | -0.0554 | -0.0879 | -0.0085 | 6.50% | 2.42% | 3403/8066 |
| Short Float | +0.0530 | +0.2267 | -0.1247 | 5.36% | n/a | 5697/0 |
| d_Relative Strength Index (14) | -0.0413 | +0.2368 | -0.1200 | 5.69% | 2.83% | 3415/7755 |
| d_200-Day Simple Moving Average | -0.0379 | -0.0567 | -0.0162 | 5.64% | 2.78% | 3460/7974 |
| d_Performance (YTD) | -0.0356 | -0.0640 | -0.0016 | 5.74% | 2.81% | 3392/7809 |
| true_ret | -0.0355 | -0.0926 | +0.0385 | 4.30% | 2.83% | 3310/7742 |
| d_Short Ratio | -0.0320 | -0.0388 | -0.0019 | 0.89% | 5.22% | 3647/3257 |
| d_Performance (Week) | -0.0286 | -0.0546 | -0.0004 | 5.43% | 3.04% | 3117/8256 |
| d_Profit Margin | +0.0274 | -0.0116 | +0.0340 | 22.76% | -4.12% | 22/34 |
| d_Average Volume | +0.0261 | +0.0563 | -0.0696 | 6.74% | 1.08% | 5220/5733 |
| d_Market Cap | -0.0244 | +0.0118 | -0.0665 | 6.74% | 4.45% | 2082/3661 |
| d_Short Float | +0.0237 | -0.0339 | +0.0573 | 1.06% | 40.85% | 85/155 |
| d_Institutional Ownership | +0.0235 | -0.0839 | +0.1048 | 0.76% | 14.40% | 711/757 |
| d_Forward P/E | +0.0213 | -0.0355 | +0.0353 | 1.70% | 1.16% | 1041/1898 |
| Institutional Transactions | -0.0181 | +0.0446 | -0.0271 | 8.71% | 2.91% | 2690/2352 |
| d_Price | -0.0176 | +0.0602 | -0.0696 | 4.30% | 2.83% | 3310/7742 |
| d_Target Price | -0.0162 | -0.0117 | -0.0028 | 0.53% | 0.94% | 244/140 |

## Combinations

| Pattern | n | Mean long fwd | Hit up |
|---|---|---|---|
| true_ret>3% & DOWNTREND | 245 | 21.57% | 38.4% |
| true_ret>3% & UPTREND | 249 | 6.26% | 44.2% |
| true_ret>3% & MIXED | 276 | 21.74% | 70.3% |

## Risk dominance probes

| State | n | Mean long fwd | Mean fwd if score top quintile |
|---|---|---|---|
| EXTENDED | 289 | 9.87% | 21.50% |
| WASHED | 575 | 33.46% | 47.61% |

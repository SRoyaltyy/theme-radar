# Factor attribution — signal 2026-08-18 → prediction day 2026-08-21

## Trade window (read this first)

| Role | Date | Meaning |
|------|------|---------|
| **Signal as-of** | **2026-08-18** | Features/scores formed from this snapshot (and deltas vs **2026-08-17**). Only data on/before this date. |
| **Prediction day** | **2026-08-21** | The trading day the forward return is for (exit snapshot). |
| **Entry price** | Price @ 2026-08-18 | Long: buy here; short: sell here. |
| **Exit price** | Price @ 2026-08-21 | Close proxy on prediction day. |
| **Return column** | `fwd_3d` | Long: exit/entry − 1; short = opposite. |

Graded **n=11570** names with valid entry and exit prices.

Provisional until multiple signal dates agree.

_Column guide: **IC** = Spearman(feature, long forward return); **IC↑** / **IC↓** = IC among names that went up / down._

## Score calibration (long fwd)
- Spearman IC(total_score, fwd_3d) = **0.0058**

| Quintile | Mean long fwd | Hit up>1.5% | n |
|---|---|---|---|
| 1 | 3.01% | 37.2% | 2490 |
| 2 | 3.13% | 27.0% | 2143 |
| 3 | 5.04% | 18.0% | 2478 |
| 4 | 0.54% | 16.9% | 2242 |
| 5 | 2.86% | 40.2% | 2217 |

## Top |IC| features

| Feature | IC | IC↑ | IC↓ | Mean fwd when + | Mean fwd when − | n+/n− |
|---|---|---|---|---|---|---|
| d_Forward P/E | +0.1536 | -0.1139 | +0.2465 | 1.04% | 0.28% | 1095/1855 |
| d_Price | +0.0966 | -0.0579 | +0.0901 | 3.85% | 1.85% | 3444/7524 |
| d_200-Day Simple Moving Average | +0.0792 | -0.1300 | +0.1879 | 5.61% | 1.77% | 3654/7756 |
| d_Performance (Week) | +0.0760 | -0.1406 | +0.2408 | 5.55% | 1.81% | 3709/7563 |
| Institutional Transactions | -0.0706 | +0.0057 | -0.0751 | 6.63% | 3.77% | 2690/2352 |
| d_Performance (YTD) | +0.0700 | -0.1492 | +0.1858 | 5.65% | 1.84% | 3542/7592 |
| d_Market Cap | +0.0699 | -0.0898 | +0.0713 | 8.10% | 2.64% | 2196/3507 |
| d_Average Volume | -0.0689 | -0.0913 | -0.0123 | 4.59% | 1.95% | 4641/6340 |
| d_Short Ratio | +0.0601 | +0.0921 | -0.0167 | 1.68% | 2.20% | 4088/2714 |
| d_Relative Strength Index (14) | +0.0590 | +0.0436 | -0.0464 | 5.60% | 1.88% | 3555/7543 |
| true_ret | +0.0574 | -0.1772 | +0.2202 | 3.85% | 1.85% | 3444/7524 |
| Performance (Month) | +0.0547 | +0.1037 | -0.0039 | 1.84% | 5.03% | 7207/4149 |
| d_Volatility (Month) | +0.0545 | -0.1278 | +0.2086 | 7.81% | 1.42% | 3036/6595 |
| upside_pct_lvl | +0.0535 | +0.3138 | -0.2700 | 1.86% | 0.79% | 4330/318 |
| Relative Strength Index (14) | +0.0504 | -0.1200 | +0.2144 | 3.00% | n/a | 11447/0 |
| d_50-Day Simple Moving Average | +0.0494 | -0.1774 | +0.1990 | 5.57% | 1.85% | 3504/7906 |
| Relative Volume | -0.0489 | +0.0223 | -0.0843 | 3.03% | n/a | 11278/0 |
| d_20-Day Simple Moving Average | +0.0461 | -0.1758 | +0.2024 | 5.69% | 1.77% | 3562/7890 |
| d_EPS Surprise | -0.0454 | -0.0432 | -0.0107 | -0.44% | 3.77% | 25/30 |
| Short Float | +0.0434 | +0.1856 | -0.2156 | 4.74% | n/a | 5698/0 |
| Performance (Week) | -0.0425 | -0.1217 | +0.0645 | 2.38% | 3.49% | 4902/6436 |
| d_Performance (Quarter) | +0.0278 | -0.0470 | +0.1160 | 4.83% | 2.33% | 3530/7264 |
| d_Relative Volume | -0.0258 | -0.0665 | +0.0365 | 1.84% | 4.17% | 5401/5719 |
| d_Sales Year Over Year TTM | +0.0212 | +0.0093 | -0.0148 | 1.26% | 0.47% | 13/17 |
| d_Sales Growth Quarter Over Quarter | -0.0202 | -0.0109 | -0.0446 | -2.77% | 4.12% | 19/14 |

## Combinations

| Pattern | n | Mean long fwd | Hit up |
|---|---|---|---|
| true_ret>3% & DOWNTREND | 248 | 33.86% | 38.7% |
| true_ret>3% & UPTREND | 204 | 1.46% | 47.5% |
| true_ret>3% & MIXED | 147 | 0.56% | 43.5% |

## Risk dominance probes

| State | n | Mean long fwd | Mean fwd if score top quintile |
|---|---|---|---|
| EXTENDED | 236 | -0.44% | -3.32% |
| WASHED | 523 | 24.66% | -0.49% |

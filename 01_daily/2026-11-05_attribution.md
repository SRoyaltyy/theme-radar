# Factor attribution — signal 2026-11-05 → prediction day 2026-11-10

## Trade window (read this first)

| Role | Date | Meaning |
|------|------|---------|
| **Signal as-of** | **2026-11-05** | Features/scores formed from this snapshot (and deltas vs **2026-11-04**). Only data on/before this date. |
| **Prediction day** | **2026-11-10** | The trading day the forward return is for (exit snapshot). |
| **Entry price** | Price @ 2026-11-05 | Long: buy here; short: sell here. |
| **Exit price** | Price @ 2026-11-10 | Close proxy on prediction day. |
| **Return column** | `fwd_3d` | Long: exit/entry − 1; short = opposite. |

Graded **n=11721** names with valid entry and exit prices.

Provisional until multiple signal dates agree.

_Column guide: **IC** = Spearman(feature, long forward return); **IC↑** / **IC↓** = IC among names that went up / down._

## Score calibration (long fwd)
- Spearman IC(total_score, fwd_3d) = **-0.3617**

| Quintile | Mean long fwd | Hit up>1.5% | n |
|---|---|---|---|
| 1 | 6.58% | 76.8% | 2357 |
| 2 | 11.09% | 60.3% | 2338 |
| 3 | 4.99% | 49.3% | 2510 |
| 4 | 2.29% | 24.6% | 2248 |
| 5 | 0.75% | 21.8% | 2268 |

## Top |IC| features

| Feature | IC | IC↑ | IC↓ | Mean fwd when + | Mean fwd when − | n+/n− |
|---|---|---|---|---|---|---|
| d_Performance (YTD) | -0.4580 | -0.4915 | +0.2297 | 0.26% | 6.16% | 1888/9592 |
| d_200-Day Simple Moving Average | -0.4462 | -0.5311 | +0.2436 | 0.15% | 6.14% | 1977/9643 |
| true_ret | -0.4424 | -0.6249 | +0.3132 | 0.17% | 6.01% | 1870/9573 |
| d_50-Day Simple Moving Average | -0.4412 | -0.5791 | +0.2669 | 0.22% | 6.29% | 2049/9590 |
| d_20-Day Simple Moving Average | -0.4317 | -0.5850 | +0.2786 | 0.59% | 6.13% | 1901/9728 |
| d_Price | -0.4142 | -0.2525 | +0.1448 | 0.17% | 6.01% | 1870/9573 |
| d_Performance (Month) | -0.3974 | -0.5053 | +0.1921 | 1.12% | 6.59% | 2773/8710 |
| d_Performance (Week) | -0.3896 | -0.5259 | +0.2263 | 1.01% | 6.10% | 1898/9635 |
| Performance (Week) | -0.3868 | -0.5469 | +0.1842 | 0.17% | 7.55% | 3639/7958 |
| d_Performance (Quarter) | -0.3854 | -0.5205 | +0.2813 | 2.87% | 5.72% | 1610/9595 |
| Relative Strength Index (14) | -0.3596 | -0.3942 | +0.3258 | 5.20% | n/a | 11662/0 |
| Performance (Month) | -0.3142 | -0.5144 | +0.2498 | 0.57% | 8.33% | 4613/6945 |
| d_Relative Strength Index (14) | -0.2924 | +0.1203 | +0.1547 | 0.22% | 6.30% | 1898/9568 |
| d_Forward P/E | -0.2893 | -0.3821 | +0.1463 | 0.66% | 2.63% | 477/2496 |
| d_Market Cap | -0.2042 | -0.1177 | -0.0972 | 2.43% | 8.78% | 883/4921 |
| upside_pct_lvl | +0.1770 | +0.4911 | -0.3831 | 5.97% | 0.02% | 4311/317 |
| Relative Volume | +0.1628 | +0.1658 | -0.0725 | 5.25% | n/a | 11570/0 |
| Short Float | +0.1246 | +0.3463 | -0.1871 | 6.61% | n/a | 5622/0 |
| d_Beta | -0.1172 | -0.0309 | -0.1662 | 7.27% | 11.93% | 2527/1797 |
| d_Relative Volume | +0.1154 | +0.0941 | -0.0476 | 5.01% | 5.72% | 7036/4393 |
| d_Volatility (Month) | +0.1149 | +0.3372 | -0.3412 | 5.54% | 7.05% | 7756/2266 |
| Institutional Transactions | +0.0865 | +0.1357 | -0.0585 | 10.30% | 5.23% | 3187/1829 |
| d_Institutional Ownership | +0.0398 | +0.0862 | -0.0754 | 4.46% | 4.20% | 1775/1493 |
| d_Insider Transactions | +0.0385 | +0.0339 | +0.0214 | 4.59% | 1.13% | 197/203 |
| d_Analyst Recom | -0.0367 | -0.0339 | -0.0116 | 1.45% | 4.59% | 79/94 |

## Combinations

| Pattern | n | Mean long fwd | Hit up |
|---|---|---|---|
| true_ret>3% & DOWNTREND | 136 | 8.71% | 35.3% |
| true_ret>3% & UPTREND | 150 | -0.31% | 39.3% |
| true_ret>3% & MIXED | 142 | -4.62% | 31.7% |

## Risk dominance probes

| State | n | Mean long fwd | Mean fwd if score top quintile |
|---|---|---|---|
| EXTENDED | 259 | -2.57% | -6.60% |
| WASHED | 2719 | 16.71% | 12.74% |

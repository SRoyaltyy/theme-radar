# Factor attribution — signal 2026-09-03 → prediction day 2026-09-08

## Trade window (read this first)

| Role | Date | Meaning |
|------|------|---------|
| **Signal as-of** | **2026-09-03** | Features/scores formed from this snapshot (and deltas vs **2026-09-02**). Only data on/before this date. |
| **Prediction day** | **2026-09-08** | The trading day the forward return is for (exit snapshot). |
| **Entry price** | Price @ 2026-09-03 | Long: buy here; short: sell here. |
| **Exit price** | Price @ 2026-09-08 | Close proxy on prediction day. |
| **Return column** | `fwd_2d` | Long: exit/entry − 1; short = opposite. |

Graded **n=11588** names with valid entry and exit prices.

Provisional until multiple signal dates agree.

_Column guide: **IC** = Spearman(feature, long forward return); **IC↑** / **IC↓** = IC among names that went up / down._

## Score calibration (long fwd)
- Spearman IC(total_score, fwd_2d) = **-0.0607**

| Quintile | Mean long fwd | Hit up>1.5% | n |
|---|---|---|---|
| 1 | 3.74% | 20.6% | 2330 |
| 2 | -0.25% | 8.0% | 3244 |
| 3 | 0.78% | 11.8% | 2161 |
| 4 | 1.38% | 26.8% | 1557 |
| 5 | 2.20% | 23.8% | 2296 |

## Top |IC| features

| Feature | IC | IC↑ | IC↓ | Mean fwd when + | Mean fwd when − | n+/n− |
|---|---|---|---|---|---|---|
| d_Performance (Week) | -0.1915 | -0.0842 | -0.1735 | 0.82% | 2.78% | 7464/3906 |
| Relative Strength Index (14) | -0.1827 | -0.1562 | -0.1058 | 1.47% | n/a | 11489/0 |
| Performance (Week) | -0.1480 | -0.2877 | -0.0142 | 2.10% | 1.05% | 4608/6845 |
| d_200-Day Simple Moving Average | -0.1474 | +0.0516 | -0.1749 | 0.81% | 3.06% | 8121/3362 |
| Performance (Month) | -0.1399 | -0.1742 | -0.1371 | -0.33% | 3.18% | 5537/5827 |
| true_ret | -0.1368 | +0.0459 | -0.1717 | 0.54% | 3.28% | 7930/3160 |
| d_Relative Strength Index (14) | -0.1338 | -0.1044 | +0.1540 | 0.73% | 3.54% | 7972/3195 |
| d_Performance (YTD) | -0.1289 | +0.0405 | -0.1409 | 0.73% | 3.55% | 8000/3200 |
| d_Price | -0.1261 | -0.0284 | -0.0466 | 0.54% | 3.28% | 7930/3160 |
| upside_pct_lvl | +0.1200 | +0.3856 | -0.1951 | 1.39% | -1.55% | 4300/342 |
| d_20-Day Simple Moving Average | -0.1129 | +0.1013 | -0.1657 | 0.79% | 3.15% | 8226/3273 |
| d_50-Day Simple Moving Average | -0.0995 | +0.1196 | -0.1614 | 0.81% | 3.08% | 8186/3324 |
| d_Market Cap | -0.0833 | -0.0071 | -0.0340 | 1.67% | 4.09% | 3295/2376 |
| Institutional Transactions | +0.0798 | +0.1010 | +0.0416 | 4.19% | 1.09% | 3182/1856 |
| d_Forward P/E | -0.0739 | +0.0532 | -0.1227 | -0.85% | -0.33% | 1925/1016 |
| Short Float | -0.0471 | +0.2411 | -0.1846 | 2.57% | n/a | 5683/0 |
| d_Target Price | -0.0349 | -0.0078 | -0.0264 | -1.32% | 0.12% | 156/118 |
| d_Volatility (Month) | -0.0340 | -0.1855 | +0.0942 | 4.13% | 0.65% | 3129/6539 |
| Relative Volume | -0.0320 | +0.0266 | -0.0369 | 1.49% | n/a | 11304/0 |
| d_Profit Margin | +0.0267 | -0.0116 | -0.0011 | 1.78% | 1.80% | 25/11 |
| d_Total Debt/Equity | +0.0263 | -0.0406 | +0.0396 | 2.18% | 0.12% | 13/18 |
| d_Performance (Quarter) | +0.0262 | +0.0646 | +0.0021 | 1.50% | 1.36% | 5638/5174 |
| d_Short Ratio | -0.0216 | +0.1127 | -0.0995 | 0.85% | 2.60% | 4226/2809 |
| d_Analyst Recom | -0.0211 | -0.0344 | +0.0037 | -0.76% | 0.04% | 92/71 |
| d_EPS Surprise | -0.0209 | +0.0045 | -0.0090 | -1.18% | 1.20% | 24/30 |

## Combinations

| Pattern | n | Mean long fwd | Hit up |
|---|---|---|---|
| true_ret>3% & DOWNTREND | 331 | 19.23% | 48.0% |
| true_ret>3% & UPTREND | 509 | -2.26% | 17.1% |
| true_ret>3% & MIXED | 343 | 2.61% | 27.4% |

## Risk dominance probes

| State | n | Mean long fwd | Mean fwd if score top quintile |
|---|---|---|---|
| EXTENDED | 250 | -1.43% | -6.41% |
| WASHED | 733 | 4.76% | 4.46% |

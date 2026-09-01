# Factor attribution — signal 2026-08-28 → prediction day 2026-09-01

## Trade window (read this first)

| Role | Date | Meaning |
|------|------|---------|
| **Signal as-of** | **2026-08-28** | Features/scores formed from this snapshot (and deltas vs **2026-08-26**). Only data on/before this date. |
| **Prediction day** | **2026-09-01** | The trading day the forward return is for (exit snapshot). |
| **Entry price** | Price @ 2026-08-28 | Long: buy here; short: sell here. |
| **Exit price** | Price @ 2026-09-01 | Close proxy on prediction day. |
| **Return column** | `fwd_2d` | Long: exit/entry − 1; short = opposite. |

Graded **n=11610** names with valid entry and exit prices.

Provisional until multiple signal dates agree.

_Column guide: **IC** = Spearman(feature, long forward return); **IC↑** / **IC↓** = IC among names that went up / down._

## Score calibration (long fwd)
- Spearman IC(total_score, fwd_2d) = **0.0258**

| Quintile | Mean long fwd | Hit up>1.5% | n |
|---|---|---|---|
| 1 | 14.74% | 13.0% | 2346 |
| 2 | 0.71% | 11.1% | 2408 |
| 3 | -0.63% | 5.6% | 2589 |
| 4 | -1.18% | 4.5% | 1945 |
| 5 | -1.63% | 13.8% | 2322 |

## Top |IC| features

| Feature | IC | IC↑ | IC↓ | Mean fwd when + | Mean fwd when − | n+/n− |
|---|---|---|---|---|---|---|
| Short Float | -0.1963 | +0.1580 | -0.2478 | 5.49% | n/a | 5693/0 |
| d_Performance (Quarter) | +0.1794 | +0.0131 | +0.2134 | 2.21% | 3.02% | 3605/7241 |
| d_Volatility (Month) | +0.1692 | -0.0562 | +0.2649 | 14.89% | -0.68% | 2287/8293 |
| Relative Strength Index (14) | +0.1514 | -0.0924 | +0.2047 | 2.50% | n/a | 11474/0 |
| Performance (Week) | +0.1320 | -0.1135 | +0.2348 | -0.98% | 5.14% | 4858/6518 |
| true_ret | +0.1313 | -0.0299 | +0.2128 | -0.88% | 4.57% | 4083/7076 |
| d_Performance (YTD) | +0.1249 | +0.0074 | +0.1916 | -0.81% | 4.51% | 4150/7125 |
| d_20-Day Simple Moving Average | +0.1245 | -0.0267 | +0.2056 | -0.91% | 4.12% | 3717/7770 |
| d_Price | +0.1210 | +0.0821 | +0.1368 | -0.88% | 4.57% | 4083/7076 |
| d_200-Day Simple Moving Average | +0.1179 | +0.0171 | +0.1764 | -0.88% | 4.36% | 4095/7387 |
| d_50-Day Simple Moving Average | +0.1038 | +0.0002 | +0.1718 | -0.94% | 4.44% | 4149/7336 |
| d_Forward P/E | +0.0978 | +0.1001 | +0.0987 | -1.36% | -1.89% | 1074/1872 |
| upside_pct_lvl | -0.0970 | +0.2754 | -0.2826 | 1.39% | -0.83% | 4310/334 |
| d_Market Cap | +0.0667 | +0.0713 | +0.0435 | -0.86% | 9.98% | 2129/3618 |
| Relative Volume | -0.0579 | +0.0832 | -0.0621 | 2.54% | n/a | 11314/0 |
| d_Short Ratio | -0.0570 | +0.0126 | -0.0853 | -0.81% | 9.12% | 5163/2865 |
| d_Relative Volume | -0.0531 | +0.0270 | -0.0237 | 0.44% | 4.97% | 5872/5295 |
| d_Performance (Week) | +0.0504 | -0.0904 | +0.1143 | 3.46% | 1.80% | 4898/6502 |
| d_Average Volume | +0.0477 | -0.0022 | +0.0907 | 7.69% | -0.47% | 4199/7037 |
| d_Beta | +0.0447 | -0.0141 | +0.0316 | -0.11% | 14.39% | 2051/2429 |
| d_Performance (Month) | +0.0304 | -0.1268 | +0.0768 | -0.96% | 5.30% | 4957/6338 |
| d_Gross Margin | -0.0278 | -0.0180 | -0.0350 | -1.82% | 0.27% | 51/29 |
| Performance (Month) | -0.0275 | +0.0311 | -0.0597 | -0.68% | 8.35% | 7301/4051 |
| d_Analyst Recom | -0.0253 | -0.0473 | -0.0099 | -1.91% | -1.12% | 167/128 |
| d_Institutional Ownership | -0.0241 | +0.0192 | -0.0226 | 19.94% | 2.51% | 630/624 |

## Combinations

| Pattern | n | Mean long fwd | Hit up |
|---|---|---|---|
| true_ret>3% & DOWNTREND | 198 | 1.15% | 20.7% |
| true_ret>3% & UPTREND | 387 | -1.31% | 20.4% |
| true_ret>3% & MIXED | 186 | -2.18% | 28.5% |

## Risk dominance probes

| State | n | Mean long fwd | Mean fwd if score top quintile |
|---|---|---|---|
| EXTENDED | 271 | -1.24% | -2.46% |
| WASHED | 461 | 82.13% | -1.39% |

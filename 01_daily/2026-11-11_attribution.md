# Factor attribution — signal 2026-11-11 → prediction day 2026-11-16

## Trade window (read this first)

| Role | Date | Meaning |
|------|------|---------|
| **Signal as-of** | **2026-11-11** | Features/scores formed from this snapshot (and deltas vs **2026-11-10**). Only data on/before this date. |
| **Prediction day** | **2026-11-16** | The trading day the forward return is for (exit snapshot). |
| **Entry price** | Price @ 2026-11-11 | Long: buy here; short: sell here. |
| **Exit price** | Price @ 2026-11-16 | Close proxy on prediction day. |
| **Return column** | `fwd_3d` | Long: exit/entry − 1; short = opposite. |

Graded **n=11704** names with valid entry and exit prices.

Provisional until multiple signal dates agree.

_Column guide: **IC** = Spearman(feature, long forward return); **IC↑** / **IC↓** = IC among names that went up / down._

## Score calibration (long fwd)
- Spearman IC(total_score, fwd_3d) = **-0.2759**

| Quintile | Mean long fwd | Hit up>1.5% | n |
|---|---|---|---|
| 1 | -2.78% | 14.7% | 2345 |
| 2 | -1.61% | 4.5% | 2821 |
| 3 | -0.47% | 6.4% | 1954 |
| 4 | -4.38% | 5.0% | 2246 |
| 5 | -4.82% | 6.7% | 2338 |

## Top |IC| features

| Feature | IC | IC↑ | IC↓ | Mean fwd when + | Mean fwd when − | n+/n− |
|---|---|---|---|---|---|---|
| upside_pct_lvl | -0.4549 | +0.4264 | -0.6017 | -3.40% | -2.51% | 4316/306 |
| d_Performance (Month) | -0.3933 | -0.0352 | -0.4355 | -3.32% | -1.96% | 7529/3913 |
| Performance (Month) | +0.3645 | -0.1031 | +0.4537 | -1.71% | -3.80% | 5359/6181 |
| d_50-Day Simple Moving Average | -0.3411 | -0.0552 | -0.3638 | -3.14% | -2.16% | 8057/3519 |
| d_20-Day Simple Moving Average | -0.3311 | -0.0647 | -0.3585 | -3.26% | -2.12% | 7384/4192 |
| d_200-Day Simple Moving Average | -0.3117 | -0.0748 | -0.3168 | -3.39% | -2.13% | 7982/3564 |
| true_ret | -0.3088 | -0.1024 | -0.3216 | -3.88% | -2.86% | 7703/3449 |
| Relative Strength Index (14) | +0.3062 | -0.2617 | +0.4083 | -2.82% | n/a | 11655/0 |
| d_Performance (Quarter) | -0.2834 | -0.1330 | -0.2895 | -3.87% | -1.80% | 6396/4797 |
| d_Performance (YTD) | -0.2746 | -0.1113 | -0.2595 | -3.59% | -2.30% | 7779/3518 |
| Short Float | -0.2332 | +0.1855 | -0.2456 | -2.24% | n/a | 5628/0 |
| d_Price | -0.2223 | -0.1268 | -0.1661 | -3.88% | -2.86% | 7703/3449 |
| d_Volatility (Month) | -0.2197 | +0.2753 | -0.3108 | -3.14% | -2.57% | 7533/2369 |
| d_Relative Strength Index (14) | -0.2086 | -0.0843 | -0.1379 | -3.10% | -2.30% | 7794/3551 |
| d_Forward P/E | -0.1580 | -0.0276 | -0.1861 | -2.96% | -2.65% | 1714/1186 |
| d_Performance (Week) | -0.1510 | -0.0571 | -0.1800 | -3.53% | -2.45% | 4206/7354 |
| d_Beta | -0.1336 | +0.0798 | -0.1755 | -1.80% | -3.52% | 1986/1538 |
| Institutional Transactions | -0.1060 | +0.0867 | -0.1341 | -2.82% | -1.45% | 3094/1911 |
| Relative Volume | -0.1003 | +0.0921 | -0.1255 | -2.86% | n/a | 11452/0 |
| d_Target Price | +0.0783 | -0.0337 | +0.0585 | -3.37% | -6.34% | 271/368 |
| d_Short Ratio | -0.0591 | +0.0373 | -0.0917 | -3.75% | -2.55% | 4793/6285 |
| d_Short Float | -0.0577 | +0.0050 | -0.0711 | -3.56% | -1.28% | 2324/3115 |
| d_Market Cap | -0.0550 | -0.0364 | -0.0501 | -2.06% | -3.46% | 3315/2377 |
| d_Insider Transactions | -0.0495 | +0.0021 | -0.0531 | -7.89% | -3.91% | 100/159 |
| d_Institutional Ownership | +0.0478 | -0.1624 | -0.0075 | -3.67% | -4.58% | 2065/2021 |

## Combinations

| Pattern | n | Mean long fwd | Hit up |
|---|---|---|---|
| true_ret>3% & DOWNTREND | 1258 | -7.09% | 7.2% |
| true_ret>3% & UPTREND | 201 | -4.97% | 15.9% |
| true_ret>3% & MIXED | 294 | -6.84% | 9.9% |

## Risk dominance probes

| State | n | Mean long fwd | Mean fwd if score top quintile |
|---|---|---|---|
| EXTENDED | 256 | -4.53% | -13.70% |
| WASHED | 1238 | -0.40% | 6.35% |

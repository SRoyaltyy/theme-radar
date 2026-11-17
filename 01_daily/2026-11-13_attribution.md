# Factor attribution — signal 2026-11-13 → prediction day 2026-11-16

## Trade window (read this first)

| Role | Date | Meaning |
|------|------|---------|
| **Signal as-of** | **2026-11-13** | Features/scores formed from this snapshot (and deltas vs **2026-11-12**). Only data on/before this date. |
| **Prediction day** | **2026-11-16** | The trading day the forward return is for (exit snapshot). |
| **Entry price** | Price @ 2026-11-13 | Long: buy here; short: sell here. |
| **Exit price** | Price @ 2026-11-16 | Close proxy on prediction day. |
| **Return column** | `fwd_1d` | Long: exit/entry − 1; short = opposite. |

Graded **n=11715** names with valid entry and exit prices.

Provisional until multiple signal dates agree.

_Column guide: **IC** = Spearman(feature, long forward return); **IC↑** / **IC↓** = IC among names that went up / down._

## Score calibration (long fwd)
- Spearman IC(total_score, fwd_1d) = **0.2039**

| Quintile | Mean long fwd | Hit up>1.5% | n |
|---|---|---|---|
| 1 | -2.12% | 7.3% | 2360 |
| 2 | -1.80% | 3.9% | 2339 |
| 3 | -1.25% | 3.6% | 3271 |
| 4 | -1.43% | 4.7% | 1959 |
| 5 | -0.55% | 11.5% | 1786 |

## Top |IC| features

| Feature | IC | IC↑ | IC↓ | Mean fwd when + | Mean fwd when − | n+/n− |
|---|---|---|---|---|---|---|
| Performance (Month) | +0.4465 | -0.0153 | +0.5523 | -0.79% | -1.88% | 4486/7069 |
| upside_pct_lvl | -0.4272 | +0.3818 | -0.5880 | -1.53% | -0.94% | 4348/277 |
| d_Performance (Week) | +0.3863 | +0.0602 | +0.4511 | -0.37% | -2.15% | 4367/7169 |
| Relative Strength Index (14) | +0.3602 | +0.0286 | +0.4726 | -1.46% | n/a | 11669/0 |
| true_ret | +0.3407 | +0.0963 | +0.4055 | -0.71% | -1.94% | 4232/6923 |
| d_Performance (YTD) | +0.3336 | +0.1006 | +0.3797 | -0.69% | -1.96% | 4313/6991 |
| d_Price | +0.3265 | +0.1296 | +0.3331 | -0.71% | -1.94% | 4232/6923 |
| d_200-Day Simple Moving Average | +0.3227 | +0.1083 | +0.3667 | -0.77% | -2.05% | 4475/7088 |
| d_Performance (Quarter) | +0.3132 | +0.1793 | +0.3403 | -0.72% | -2.29% | 5838/5355 |
| d_50-Day Simple Moving Average | +0.2712 | +0.1048 | +0.3212 | -0.76% | -1.98% | 4863/6709 |
| d_20-Day Simple Moving Average | +0.2506 | +0.0860 | +0.2947 | -0.76% | -1.91% | 4441/7148 |
| d_Market Cap | +0.2084 | -0.0779 | +0.2197 | -0.97% | -1.07% | 2556/3138 |
| d_Forward P/E | +0.2043 | -0.0146 | +0.2116 | -1.29% | -2.42% | 1563/1314 |
| d_Performance (Month) | +0.1936 | -0.0399 | +0.2242 | -1.12% | -1.57% | 2626/8870 |
| d_Relative Strength Index (14) | +0.1930 | +0.1321 | +0.2039 | -0.73% | -1.96% | 4342/7002 |
| d_Beta | -0.1776 | +0.0324 | -0.2256 | -0.96% | -2.03% | 1859/886 |
| Short Float | -0.1746 | +0.0973 | -0.2242 | -1.01% | n/a | 5615/0 |
| Performance (Week) | -0.1135 | -0.0294 | -0.0541 | -2.17% | -0.36% | 7087/4512 |
| d_Target Price | +0.0970 | -0.0435 | +0.0944 | -1.72% | -3.55% | 280/406 |
| Relative Volume | -0.0916 | +0.0900 | -0.1189 | -1.48% | n/a | 11466/0 |
| d_Short Float | +0.0630 | -0.0293 | +0.1023 | -1.96% | -4.93% | 50/115 |
| Institutional Transactions | -0.0617 | +0.0999 | -0.0901 | -0.34% | -1.99% | 3094/1914 |
| d_Sales Year Over Year TTM | +0.0517 | +0.0385 | +0.0610 | -3.02% | -5.40% | 109/134 |
| d_Institutional Ownership | +0.0395 | -0.0409 | +0.0558 | -0.42% | -1.95% | 2724/2330 |
| d_Insider Transactions | -0.0375 | +0.0360 | -0.0303 | -2.49% | -2.15% | 256/324 |

## Combinations

| Pattern | n | Mean long fwd | Hit up |
|---|---|---|---|
| true_ret>3% & DOWNTREND | 320 | 2.62% | 17.5% |
| true_ret>3% & UPTREND | 151 | -0.54% | 27.8% |
| true_ret>3% & MIXED | 133 | 0.36% | 38.3% |

## Risk dominance probes

| State | n | Mean long fwd | Mean fwd if score top quintile |
|---|---|---|---|
| EXTENDED | 190 | -0.71% | -2.09% |
| WASHED | 1420 | -0.55% | 2.67% |

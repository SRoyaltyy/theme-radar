# Factor attribution — signal 2026-11-10 → prediction day 2026-11-11

## Trade window (read this first)

| Role | Date | Meaning |
|------|------|---------|
| **Signal as-of** | **2026-11-10** | Features/scores formed from this snapshot (and deltas vs **2026-11-09**). Only data on/before this date. |
| **Prediction day** | **2026-11-11** | The trading day the forward return is for (exit snapshot). |
| **Entry price** | Price @ 2026-11-10 | Long: buy here; short: sell here. |
| **Exit price** | Price @ 2026-11-11 | Close proxy on prediction day. |
| **Return column** | `fwd_1d` | Long: exit/entry − 1; short = opposite. |

Graded **n=11734** names with valid entry and exit prices.

Provisional until multiple signal dates agree.

_Column guide: **IC** = Spearman(feature, long forward return); **IC↑** / **IC↓** = IC among names that went up / down._

## Score calibration (long fwd)
- Spearman IC(total_score, fwd_1d) = **-0.1184**

| Quintile | Mean long fwd | Hit up>1.5% | n |
|---|---|---|---|
| 1 | 3.02% | 41.5% | 2615 |
| 2 | 1.39% | 33.1% | 2154 |
| 3 | 1.67% | 12.6% | 2393 |
| 4 | 0.67% | 14.9% | 2462 |
| 5 | 0.90% | 32.1% | 2110 |

## Top |IC| features

| Feature | IC | IC↑ | IC↓ | Mean fwd when + | Mean fwd when − | n+/n− |
|---|---|---|---|---|---|---|
| Performance (Month) | -0.3807 | -0.5662 | +0.1577 | -0.05% | 2.86% | 5070/6508 |
| Relative Strength Index (14) | -0.3531 | -0.4869 | +0.1895 | 1.57% | n/a | 11685/0 |
| Performance (Week) | -0.3356 | -0.4246 | -0.0568 | 0.16% | 2.93% | 5581/5967 |
| d_Beta | -0.2116 | -0.1650 | -0.0983 | 1.63% | 2.20% | 4134/2682 |
| d_Performance (Week) | -0.2073 | -0.3622 | +0.0932 | 0.37% | 2.25% | 4020/7534 |
| d_Volatility (Month) | +0.1734 | +0.3957 | -0.3316 | 2.02% | 0.91% | 7780/2244 |
| d_Performance (Quarter) | -0.1591 | -0.2864 | +0.0300 | 1.37% | 1.67% | 3042/8205 |
| upside_pct_lvl | +0.1474 | +0.5083 | -0.4705 | 2.39% | 0.20% | 4322/312 |
| d_Performance (Month) | +0.1108 | +0.1507 | -0.0069 | 2.49% | 1.10% | 4067/7405 |
| d_Price | -0.0976 | -0.1081 | -0.1112 | 0.61% | 1.97% | 3066/8224 |
| d_Relative Strength Index (14) | +0.0954 | +0.1390 | -0.2170 | 0.62% | 1.96% | 3139/8273 |
| true_ret | -0.0940 | -0.2596 | +0.1176 | 0.61% | 1.97% | 3066/8224 |
| d_Performance (YTD) | -0.0871 | -0.2088 | +0.0474 | 0.62% | 1.95% | 3124/8267 |
| d_20-Day Simple Moving Average | +0.0841 | -0.0029 | +0.0916 | 1.42% | 1.65% | 3409/8210 |
| d_200-Day Simple Moving Average | -0.0823 | -0.2016 | +0.0443 | 0.73% | 1.88% | 3161/8441 |
| Short Float | +0.0754 | +0.1967 | -0.0856 | 1.79% | n/a | 5626/0 |
| Institutional Transactions | +0.0478 | +0.1326 | -0.0684 | 2.65% | 0.83% | 3099/1918 |
| d_Analyst Recom | -0.0408 | -0.0189 | +0.0462 | 0.60% | 1.97% | 118/87 |
| d_50-Day Simple Moving Average | -0.0374 | -0.1602 | +0.0659 | 0.89% | 1.87% | 3424/8186 |
| d_Relative Volume | -0.0327 | -0.0532 | +0.0202 | 1.60% | 1.59% | 4498/6847 |
| Relative Volume | +0.0295 | +0.0843 | -0.0322 | 1.60% | n/a | 11495/0 |
| d_Average Volume | +0.0269 | +0.0762 | -0.0133 | 2.12% | 0.84% | 6746/4307 |
| d_Short Ratio | -0.0262 | -0.0640 | +0.0167 | 0.89% | 1.94% | 2609/4425 |
| d_Short Float | +0.0258 | +0.0096 | +0.0358 | 0.67% | -6.05% | 2/4 |
| d_Gross Margin | -0.0238 | -0.0027 | -0.0651 | 0.82% | 1.54% | 118/128 |

## Combinations

| Pattern | n | Mean long fwd | Hit up |
|---|---|---|---|
| true_ret>3% & DOWNTREND | 275 | 1.46% | 46.5% |
| true_ret>3% & UPTREND | 169 | -1.63% | 30.2% |
| true_ret>3% & MIXED | 140 | -0.86% | 36.4% |

## Risk dominance probes

| State | n | Mean long fwd | Mean fwd if score top quintile |
|---|---|---|---|
| EXTENDED | 276 | -1.39% | -2.67% |
| WASHED | 1537 | 8.33% | 4.49% |

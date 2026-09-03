# Factor attribution — signal 2026-09-01 → prediction day 2026-09-03

## Trade window (read this first)

| Role | Date | Meaning |
|------|------|---------|
| **Signal as-of** | **2026-09-01** | Features/scores formed from this snapshot (and deltas vs **2026-08-31**). Only data on/before this date. |
| **Prediction day** | **2026-09-03** | The trading day the forward return is for (exit snapshot). |
| **Entry price** | Price @ 2026-09-01 | Long: buy here; short: sell here. |
| **Exit price** | Price @ 2026-09-03 | Close proxy on prediction day. |
| **Return column** | `fwd_2d` | Long: exit/entry − 1; short = opposite. |

Graded **n=11620** names with valid entry and exit prices.

Provisional until multiple signal dates agree.

_Column guide: **IC** = Spearman(feature, long forward return); **IC↑** / **IC↓** = IC among names that went up / down._

## Score calibration (long fwd)
- Spearman IC(total_score, fwd_2d) = **-0.2394**

| Quintile | Mean long fwd | Hit up>1.5% | n |
|---|---|---|---|
| 1 | 2.18% | 52.6% | 2560 |
| 2 | 2.24% | 54.9% | 2135 |
| 3 | 0.93% | 23.6% | 2369 |
| 4 | 0.83% | 23.4% | 2639 |
| 5 | 0.16% | 29.8% | 1917 |

## Top |IC| features

| Feature | IC | IC↑ | IC↓ | Mean fwd when + | Mean fwd when − | n+/n− |
|---|---|---|---|---|---|---|
| d_Performance (Month) | -0.3350 | -0.4691 | +0.0674 | 0.02% | 1.65% | 2182/9097 |
| d_200-Day Simple Moving Average | -0.3187 | -0.3820 | -0.0229 | 0.22% | 1.61% | 2453/9025 |
| d_Performance (YTD) | -0.3111 | -0.3735 | -0.0029 | 0.26% | 1.63% | 2369/8911 |
| d_Price | -0.3076 | -0.2277 | -0.0817 | 0.24% | 1.64% | 2315/8850 |
| d_50-Day Simple Moving Average | -0.3047 | -0.3928 | +0.0023 | 0.28% | 1.59% | 2471/9042 |
| true_ret | -0.2900 | -0.4036 | +0.0491 | 0.24% | 1.64% | 2315/8850 |
| d_20-Day Simple Moving Average | -0.2843 | -0.3765 | +0.0142 | 0.37% | 1.59% | 2592/8909 |
| d_Performance (Week) | -0.2683 | -0.3640 | +0.0600 | 0.29% | 1.60% | 2375/9054 |
| Performance (Week) | -0.1938 | -0.3270 | +0.1382 | 0.65% | 1.50% | 2465/8981 |
| d_Market Cap | -0.1916 | -0.0938 | -0.0610 | 0.60% | 1.42% | 1693/4041 |
| d_Performance (Quarter) | -0.1785 | -0.1789 | -0.0799 | 1.06% | 1.37% | 3097/7731 |
| d_Relative Strength Index (14) | -0.1629 | +0.1088 | -0.1561 | 0.24% | 1.64% | 2367/8853 |
| Short Float | +0.1412 | +0.1867 | -0.1418 | 1.19% | n/a | 5697/0 |
| d_Forward P/E | -0.1073 | -0.1280 | +0.0086 | 0.91% | 1.94% | 786/2165 |
| d_Beta | -0.0619 | -0.0581 | -0.0451 | 1.02% | 2.01% | 1382/1558 |
| Performance (Month) | +0.0514 | +0.0252 | +0.1320 | 1.54% | 1.11% | 5638/5737 |
| d_Average Volume | -0.0411 | -0.0805 | -0.0150 | 1.24% | 1.35% | 4258/6777 |
| d_Sales Year Over Year TTM | -0.0405 | -0.0226 | -0.0174 | -3.67% | 10.18% | 5/2 |
| d_Gross Margin | -0.0392 | -0.0075 | -0.0337 | -2.18% | 4.38% | 6/6 |
| d_Short Ratio | +0.0384 | +0.0611 | +0.0189 | 1.51% | 1.36% | 4607/2486 |
| Relative Strength Index (14) | +0.0370 | +0.0723 | +0.0237 | 1.31% | n/a | 11502/0 |
| upside_pct_lvl | -0.0328 | +0.2189 | -0.3925 | 1.45% | 1.29% | 4353/297 |
| d_Volatility (Month) | -0.0282 | -0.0158 | +0.0206 | 0.49% | 0.35% | 40/17 |
| d_Target Price | +0.0231 | +0.0156 | -0.0157 | 1.44% | 1.02% | 175/144 |
| d_Sales Growth Quarter Over Quarter | -0.0185 | -0.0242 | +0.0074 | -2.49% | 7.94% | 4/4 |

## Combinations

| Pattern | n | Mean long fwd | Hit up |
|---|---|---|---|
| true_ret>3% & DOWNTREND | 158 | -3.03% | 27.2% |
| true_ret>3% & UPTREND | 188 | 1.16% | 37.8% |
| true_ret>3% & MIXED | 126 | -0.41% | 36.5% |

## Risk dominance probes

| State | n | Mean long fwd | Mean fwd if score top quintile |
|---|---|---|---|
| EXTENDED | 199 | 2.42% | -2.39% |
| WASHED | 852 | 0.81% | -1.29% |

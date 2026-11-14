# Factor attribution — signal 2026-11-12 → prediction day 2026-11-13

## Trade window (read this first)

| Role | Date | Meaning |
|------|------|---------|
| **Signal as-of** | **2026-11-12** | Features/scores formed from this snapshot (and deltas vs **2026-11-11**). Only data on/before this date. |
| **Prediction day** | **2026-11-13** | The trading day the forward return is for (exit snapshot). |
| **Entry price** | Price @ 2026-11-12 | Long: buy here; short: sell here. |
| **Exit price** | Price @ 2026-11-13 | Close proxy on prediction day. |
| **Return column** | `fwd_1d` | Long: exit/entry − 1; short = opposite. |

Graded **n=11740** names with valid entry and exit prices.

Provisional until multiple signal dates agree.

_Column guide: **IC** = Spearman(feature, long forward return); **IC↑** / **IC↓** = IC among names that went up / down._

## Score calibration (long fwd)
- Spearman IC(total_score, fwd_1d) = **0.0286**

| Quintile | Mean long fwd | Hit up>1.5% | n |
|---|---|---|---|
| 1 | -0.35% | 12.6% | 2538 |
| 2 | -0.57% | 12.2% | 2214 |
| 3 | 0.31% | 4.9% | 2411 |
| 4 | -0.42% | 4.5% | 2398 |
| 5 | -0.07% | 14.7% | 2179 |

## Top |IC| features

| Feature | IC | IC↑ | IC↓ | Mean fwd when + | Mean fwd when − | n+/n− |
|---|---|---|---|---|---|---|
| upside_pct_lvl | -0.2789 | +0.3967 | -0.5686 | -0.51% | -0.19% | 4367/270 |
| Performance (Month) | +0.2781 | -0.1099 | +0.4264 | 0.15% | -0.53% | 5374/6206 |
| d_Performance (Week) | -0.2485 | +0.0276 | -0.3302 | -0.59% | 0.73% | 8361/3243 |
| Relative Strength Index (14) | +0.2395 | -0.1789 | +0.3177 | -0.22% | n/a | 11689/0 |
| d_Performance (Month) | -0.2147 | -0.0835 | -0.2199 | -0.33% | -0.07% | 6383/5098 |
| Performance (Week) | -0.1963 | -0.0718 | -0.1905 | -0.60% | 0.38% | 7166/4439 |
| true_ret | +0.1803 | -0.1745 | +0.3641 | -0.32% | -0.58% | 2055/9281 |
| d_Performance (YTD) | +0.1432 | -0.0996 | +0.2540 | 0.46% | -0.58% | 2099/9323 |
| d_200-Day Simple Moving Average | +0.1377 | -0.1154 | +0.2706 | 0.37% | -0.57% | 2160/9443 |
| d_50-Day Simple Moving Average | +0.1362 | -0.1326 | +0.2820 | 1.21% | -0.58% | 2312/9306 |
| d_Volatility (Month) | -0.1303 | +0.0844 | -0.2154 | -0.16% | -0.33% | 5525/4053 |
| d_Performance (Quarter) | +0.1116 | -0.1109 | +0.2495 | 0.12% | -0.30% | 2579/8673 |
| d_20-Day Simple Moving Average | +0.0997 | -0.1316 | +0.2392 | 0.86% | -0.50% | 2411/9210 |
| Institutional Transactions | -0.0922 | +0.0216 | -0.1269 | 0.20% | 0.40% | 3099/1916 |
| d_Beta | +0.0719 | -0.0132 | +0.0900 | -0.10% | 0.36% | 3166/2208 |
| d_Price | +0.0716 | +0.0510 | +0.0203 | -0.32% | -0.58% | 2055/9281 |
| d_Sales Year Over Year TTM | +0.0491 | +0.0253 | +0.0142 | -1.27% | -3.55% | 30/28 |
| d_Market Cap | -0.0472 | +0.0872 | -0.0880 | 0.66% | 0.04% | 1453/4290 |
| d_Average Volume | -0.0460 | +0.0276 | -0.0705 | 0.02% | -0.47% | 5681/5295 |
| Short Float | -0.0453 | +0.1135 | -0.1814 | 0.21% | n/a | 5639/0 |
| d_Short Ratio | +0.0398 | -0.0387 | +0.0621 | -0.58% | -0.55% | 3141/3352 |
| d_EPS Surprise | -0.0275 | -0.0385 | +0.0116 | -1.87% | -1.36% | 75/75 |
| d_Forward P/E | +0.0244 | -0.0926 | +0.1176 | -0.01% | 0.61% | 709/2208 |
| d_Gross Margin | -0.0224 | -0.0284 | -0.0178 | -2.91% | -0.22% | 37/29 |
| Relative Volume | -0.0209 | +0.0865 | -0.1011 | -0.23% | n/a | 11465/0 |

## Combinations

| Pattern | n | Mean long fwd | Hit up |
|---|---|---|---|
| true_ret>3% & DOWNTREND | 250 | -1.07% | 30.0% |
| true_ret>3% & UPTREND | 81 | -0.91% | 33.3% |
| true_ret>3% & MIXED | 135 | 0.09% | 38.5% |

## Risk dominance probes

| State | n | Mean long fwd | Mean fwd if score top quintile |
|---|---|---|---|
| EXTENDED | 321 | -3.06% | -4.44% |
| WASHED | 1185 | 0.93% | -2.20% |

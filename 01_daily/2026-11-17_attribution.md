# Factor attribution — signal 2026-11-17 → prediction day 2026-11-19

## Trade window (read this first)

| Role | Date | Meaning |
|------|------|---------|
| **Signal as-of** | **2026-11-17** | Features/scores formed from this snapshot (and deltas vs **2026-11-16**). Only data on/before this date. |
| **Prediction day** | **2026-11-19** | The trading day the forward return is for (exit snapshot). |
| **Entry price** | Price @ 2026-11-17 | Long: buy here; short: sell here. |
| **Exit price** | Price @ 2026-11-19 | Close proxy on prediction day. |
| **Return column** | `fwd_2d` | Long: exit/entry − 1; short = opposite. |

Graded **n=11735** names with valid entry and exit prices.

Provisional until multiple signal dates agree.

_Column guide: **IC** = Spearman(feature, long forward return); **IC↑** / **IC↓** = IC among names that went up / down._

## Score calibration (long fwd)
- Spearman IC(total_score, fwd_2d) = **0.1330**

| Quintile | Mean long fwd | Hit up>1.5% | n |
|---|---|---|---|
| 1 | -0.65% | 9.5% | 2609 |
| 2 | 0.56% | 5.6% | 2160 |
| 3 | -1.90% | 4.1% | 2390 |
| 4 | -1.74% | 8.1% | 2238 |
| 5 | -1.70% | 14.5% | 2338 |

## Top |IC| features

| Feature | IC | IC↑ | IC↓ | Mean fwd when + | Mean fwd when − | n+/n− |
|---|---|---|---|---|---|---|
| Performance (Week) | +0.3267 | -0.2476 | +0.3734 | -0.58% | -1.20% | 1724/9862 |
| Performance (Month) | +0.2693 | -0.2062 | +0.3508 | -0.95% | -1.17% | 3920/7663 |
| true_ret | +0.2549 | -0.1446 | +0.2471 | -1.22% | -1.04% | 2322/8893 |
| Relative Strength Index (14) | +0.2258 | -0.1602 | +0.1912 | -1.10% | n/a | 11674/0 |
| d_Performance (YTD) | +0.2142 | -0.1131 | +0.1152 | -1.16% | -1.44% | 2381/8958 |
| d_Performance (Quarter) | +0.2136 | -0.1217 | +0.2056 | -1.63% | -0.94% | 2532/8718 |
| d_200-Day Simple Moving Average | +0.2109 | -0.1008 | +0.1367 | -1.42% | -1.00% | 2632/8962 |
| d_Price | +0.1895 | -0.0641 | -0.0328 | -1.22% | -1.04% | 2322/8893 |
| upside_pct_lvl | -0.1892 | +0.4595 | -0.4670 | -1.24% | -1.55% | 4398/226 |
| d_50-Day Simple Moving Average | +0.1797 | -0.0981 | +0.1294 | -1.23% | -1.06% | 2965/8648 |
| d_Performance (Month) | +0.1734 | -0.0783 | +0.1276 | -1.18% | -1.07% | 3441/8072 |
| d_20-Day Simple Moving Average | +0.1521 | -0.0851 | +0.1094 | -1.30% | -1.04% | 3097/8500 |
| d_Volatility (Month) | -0.1351 | +0.4025 | -0.2321 | -0.61% | -2.44% | 7335/2694 |
| d_Beta | -0.0995 | +0.1446 | -0.1600 | 0.73% | -1.97% | 3350/3087 |
| d_Performance (Week) | +0.0910 | -0.0591 | +0.0399 | -1.22% | -1.04% | 4286/7271 |
| d_Relative Strength Index (14) | +0.0875 | -0.0653 | -0.1623 | -1.23% | -1.05% | 2423/8961 |
| d_Institutional Ownership | +0.0815 | -0.0496 | +0.0675 | -0.17% | -0.76% | 2873/2472 |
| Short Float | -0.0783 | +0.1600 | -0.1419 | -0.58% | n/a | 5613/0 |
| d_Target Price | +0.0628 | -0.0219 | +0.0865 | -2.09% | -3.72% | 197/273 |
| Relative Volume | -0.0545 | +0.1243 | -0.0525 | -1.11% | n/a | 11504/0 |
| d_Total Debt/Equity | -0.0522 | -0.1013 | -0.0439 | -6.41% | 1.13% | 70/51 |
| Institutional Transactions | -0.0433 | +0.1147 | -0.0959 | 0.55% | -1.96% | 2992/2019 |
| d_Gross Margin | -0.0237 | -0.0401 | +0.0137 | -3.61% | -2.46% | 70/79 |
| d_Sales Year Over Year TTM | +0.0175 | +0.0394 | +0.0058 | -1.13% | -4.42% | 53/74 |
| d_Insider Transactions | +0.0167 | +0.0021 | -0.0073 | 24.96% | -2.75% | 137/202 |

## Combinations

| Pattern | n | Mean long fwd | Hit up |
|---|---|---|---|
| true_ret>3% & DOWNTREND | 350 | -4.87% | 22.6% |
| true_ret>3% & UPTREND | 70 | 2.35% | 44.3% |
| true_ret>3% & MIXED | 88 | 2.50% | 46.6% |

## Risk dominance probes

| State | n | Mean long fwd | Mean fwd if score top quintile |
|---|---|---|---|
| EXTENDED | 167 | 2.52% | 5.38% |
| WASHED | 1834 | 2.02% | -5.09% |

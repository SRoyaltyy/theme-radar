# Factor attribution — signal 2026-08-31 → prediction day 2026-09-01

## Trade window (read this first)

| Role | Date | Meaning |
|------|------|---------|
| **Signal as-of** | **2026-08-31** | Features/scores formed from this snapshot (and deltas vs **2026-08-28**). Only data on/before this date. |
| **Prediction day** | **2026-09-01** | The trading day the forward return is for (exit snapshot). |
| **Entry price** | Price @ 2026-08-31 | Long: buy here; short: sell here. |
| **Exit price** | Price @ 2026-09-01 | Close proxy on prediction day. |
| **Return column** | `fwd_1d` | Long: exit/entry − 1; short = opposite. |

Graded **n=11617** names with valid entry and exit prices.

Provisional until multiple signal dates agree.

_Column guide: **IC** = Spearman(feature, long forward return); **IC↑** / **IC↓** = IC among names that went up / down._

## Score calibration (long fwd)
- Spearman IC(total_score, fwd_1d) = **-0.0065**

| Quintile | Mean long fwd | Hit up>1.5% | n |
|---|---|---|---|
| 1 | -1.34% | 10.3% | 2468 |
| 2 | 9.11% | 5.0% | 2252 |
| 3 | -0.78% | 3.8% | 2286 |
| 4 | -0.88% | 4.6% | 2349 |
| 5 | -1.07% | 14.3% | 2262 |

## Top |IC| features

| Feature | IC | IC↑ | IC↓ | Mean fwd when + | Mean fwd when − | n+/n− |
|---|---|---|---|---|---|---|
| d_Beta | +0.1693 | -0.0213 | +0.2245 | 20.51% | -1.43% | 1070/2130 |
| Short Float | -0.1687 | +0.1745 | -0.2089 | 3.02% | n/a | 5703/0 |
| d_Volatility (Month) | +0.1560 | -0.0607 | +0.2289 | 3.58% | 0.44% | 2520/7142 |
| d_Performance (Week) | -0.1331 | +0.0257 | -0.1632 | 0.87% | 1.07% | 5452/5900 |
| upside_pct_lvl | -0.1314 | +0.3172 | -0.3118 | -0.84% | -0.76% | 4330/321 |
| Relative Strength Index (14) | +0.1023 | -0.0288 | +0.1177 | 0.96% | n/a | 11493/0 |
| Performance (Month) | -0.0945 | +0.0584 | -0.1237 | -0.95% | 4.40% | 7258/4104 |
| d_Performance (Quarter) | +0.0940 | -0.0048 | +0.0892 | -0.61% | 2.54% | 4855/5983 |
| d_Forward P/E | +0.0919 | +0.1428 | +0.0071 | -1.12% | -1.26% | 982/1967 |
| d_Relative Volume | +0.0873 | -0.0265 | +0.0942 | -0.82% | 3.49% | 6439/4740 |
| Performance (Week) | +0.0606 | +0.0133 | +0.1136 | -0.94% | 2.35% | 4781/6627 |
| d_Target Price | +0.0469 | +0.0581 | +0.0528 | -0.68% | -1.89% | 141/107 |
| d_20-Day Simple Moving Average | +0.0455 | -0.0139 | +0.0491 | 2.22% | 0.37% | 3665/7785 |
| d_Profit Margin | +0.0406 | +0.0216 | +0.0364 | 0.47% | -5.53% | 9/15 |
| true_ret | +0.0400 | -0.0011 | +0.0362 | -1.01% | -1.05% | 3758/7175 |
| d_Performance (YTD) | +0.0379 | +0.0203 | +0.0180 | -0.84% | 1.98% | 3848/7296 |
| d_Sales Growth Quarter Over Quarter | -0.0343 | -0.0473 | -0.0269 | -2.72% | -1.01% | 14/18 |
| d_Market Cap | +0.0287 | +0.1403 | -0.0959 | 5.14% | 1.79% | 2099/3614 |
| d_Price | +0.0265 | +0.0874 | -0.0640 | -1.01% | -1.05% | 3758/7175 |
| d_Total Debt/Equity | +0.0246 | +0.0181 | +0.0273 | -0.67% | -4.87% | 15/7 |
| d_Short Ratio | -0.0241 | -0.0254 | -0.0521 | -1.19% | -1.16% | 4382/2500 |
| d_200-Day Simple Moving Average | +0.0238 | +0.0294 | -0.0004 | 2.04% | 0.41% | 3890/7537 |
| d_Analyst Recom | -0.0213 | +0.0104 | -0.0438 | -0.77% | -0.26% | 59/57 |
| d_Relative Strength Index (14) | -0.0201 | +0.1004 | -0.1635 | -0.83% | 1.99% | 3830/7277 |
| d_Gross Margin | +0.0190 | +0.0008 | +0.0088 | -2.63% | -3.75% | 15/17 |

## Combinations

| Pattern | n | Mean long fwd | Hit up |
|---|---|---|---|
| true_ret>3% & DOWNTREND | 222 | -2.41% | 17.6% |
| true_ret>3% & UPTREND | 204 | -2.10% | 24.0% |
| true_ret>3% & MIXED | 182 | -3.31% | 14.8% |

## Risk dominance probes

| State | n | Mean long fwd | Mean fwd if score top quintile |
|---|---|---|---|
| EXTENDED | 292 | -2.16% | -2.71% |
| WASHED | 498 | 43.70% | -0.28% |

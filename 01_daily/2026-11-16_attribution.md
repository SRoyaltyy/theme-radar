# Factor attribution — signal 2026-11-16 → prediction day 2026-11-18

## Trade window (read this first)

| Role | Date | Meaning |
|------|------|---------|
| **Signal as-of** | **2026-11-16** | Features/scores formed from this snapshot (and deltas vs **2026-11-13**). Only data on/before this date. |
| **Prediction day** | **2026-11-18** | The trading day the forward return is for (exit snapshot). |
| **Entry price** | Price @ 2026-11-16 | Long: buy here; short: sell here. |
| **Exit price** | Price @ 2026-11-18 | Close proxy on prediction day. |
| **Return column** | `fwd_2d` | Long: exit/entry − 1; short = opposite. |

Graded **n=11723** names with valid entry and exit prices.

Provisional until multiple signal dates agree.

_Column guide: **IC** = Spearman(feature, long forward return); **IC↑** / **IC↓** = IC among names that went up / down._

## Score calibration (long fwd)
- Spearman IC(total_score, fwd_2d) = **0.0929**

| Quintile | Mean long fwd | Hit up>1.5% | n |
|---|---|---|---|
| 1 | 1.55% | 10.9% | 2543 |
| 2 | 0.29% | 7.9% | 2291 |
| 3 | -1.45% | 9.9% | 2213 |
| 4 | -0.82% | 10.1% | 2560 |
| 5 | -0.94% | 18.4% | 2116 |

## Top |IC| features

| Feature | IC | IC↑ | IC↓ | Mean fwd when + | Mean fwd when − | n+/n− |
|---|---|---|---|---|---|---|
| true_ret | +0.2039 | -0.2739 | +0.3038 | -0.85% | -0.17% | 2047/9225 |
| d_Performance (Quarter) | +0.2000 | -0.0910 | +0.2277 | -0.74% | 0.03% | 3383/7830 |
| d_20-Day Simple Moving Average | +0.1933 | -0.2383 | +0.2766 | -0.49% | -0.17% | 2144/9483 |
| d_50-Day Simple Moving Average | +0.1801 | -0.2222 | +0.2491 | -0.53% | -0.16% | 2391/9215 |
| d_Performance (Month) | +0.1755 | +0.0341 | +0.1646 | -1.10% | 0.20% | 3776/7723 |
| d_200-Day Simple Moving Average | +0.1741 | -0.2119 | +0.2143 | -0.42% | -0.18% | 2265/9334 |
| d_Performance (YTD) | +0.1622 | -0.2064 | +0.1706 | -0.36% | -0.17% | 2111/9288 |
| Performance (Week) | +0.1517 | -0.2665 | +0.2790 | -1.37% | 0.06% | 2306/9289 |
| d_Performance (Week) | +0.1512 | -0.2936 | +0.2349 | 3.88% | -0.94% | 1704/9866 |
| d_Price | +0.1494 | -0.1479 | +0.0014 | -0.85% | -0.17% | 2047/9225 |
| upside_pct_lvl | -0.1448 | +0.3782 | -0.4484 | 1.10% | -1.03% | 4354/272 |
| Performance (Month) | +0.1442 | -0.2183 | +0.2674 | -0.86% | 0.12% | 4105/7470 |
| d_Relative Strength Index (14) | +0.1280 | -0.1450 | -0.1639 | -0.40% | -0.18% | 2139/9284 |
| Relative Strength Index (14) | +0.1183 | -0.1107 | +0.1761 | -0.23% | n/a | 11673/0 |
| d_Forward P/E | -0.0833 | -0.1125 | +0.0839 | -1.70% | -1.55% | 731/2166 |
| Institutional Transactions | -0.0523 | +0.0935 | -0.0973 | -0.32% | 3.40% | 2991/2019 |
| d_Average Volume | +0.0469 | -0.0062 | +0.0530 | 1.31% | -1.60% | 5444/5543 |
| d_Beta | -0.0409 | +0.1080 | -0.1351 | 5.13% | -1.66% | 1888/1373 |
| Relative Volume | -0.0397 | +0.1186 | -0.0740 | -0.24% | n/a | 11525/0 |
| Short Float | -0.0384 | +0.1785 | -0.1659 | 0.91% | n/a | 5627/0 |
| d_Target Price | +0.0384 | -0.0424 | +0.0644 | -1.73% | -2.50% | 339/398 |
| d_Short Ratio | -0.0327 | -0.0009 | -0.0295 | 0.53% | 0.16% | 3361/3089 |
| d_Institutional Ownership | +0.0310 | -0.0286 | +0.0103 | 1.05% | 0.63% | 3294/2200 |
| d_Volatility (Month) | -0.0272 | +0.0471 | -0.0654 | 1.80% | -1.64% | 4340/5388 |
| d_Short Float | +0.0269 | -0.0491 | +0.0582 | -1.01% | -2.03% | 33/128 |

## Combinations

| Pattern | n | Mean long fwd | Hit up |
|---|---|---|---|
| true_ret>3% & DOWNTREND | 183 | -3.37% | 21.9% |
| true_ret>3% & UPTREND | 118 | 0.21% | 44.1% |
| true_ret>3% & MIXED | 120 | 3.08% | 59.2% |

## Risk dominance probes

| State | n | Mean long fwd | Mean fwd if score top quintile |
|---|---|---|---|
| EXTENDED | 204 | 0.08% | -1.46% |
| WASHED | 1657 | 5.38% | -1.28% |

# Factor attribution — signal 2026-11-16 → prediction day 2026-11-17

## Trade window (read this first)

| Role | Date | Meaning |
|------|------|---------|
| **Signal as-of** | **2026-11-16** | Features/scores formed from this snapshot (and deltas vs **2026-11-13**). Only data on/before this date. |
| **Prediction day** | **2026-11-17** | The trading day the forward return is for (exit snapshot). |
| **Entry price** | Price @ 2026-11-16 | Long: buy here; short: sell here. |
| **Exit price** | Price @ 2026-11-17 | Close proxy on prediction day. |
| **Return column** | `fwd_1d` | Long: exit/entry − 1; short = opposite. |

Graded **n=11723** names with valid entry and exit prices.

Provisional until multiple signal dates agree.

_Column guide: **IC** = Spearman(feature, long forward return); **IC↑** / **IC↓** = IC among names that went up / down._

## Score calibration (long fwd)
- Spearman IC(total_score, fwd_1d) = **-0.0069**

| Quintile | Mean long fwd | Hit up>1.5% | n |
|---|---|---|---|
| 1 | 2.44% | 8.7% | 2543 |
| 2 | -0.87% | 6.0% | 2291 |
| 3 | -1.14% | 5.4% | 2213 |
| 4 | -0.61% | 5.1% | 2560 |
| 5 | -0.86% | 11.6% | 2116 |

## Top |IC| features

| Feature | IC | IC↑ | IC↓ | Mean fwd when + | Mean fwd when − | n+/n− |
|---|---|---|---|---|---|---|
| d_Performance (Week) | +0.2097 | -0.2712 | +0.2704 | 5.13% | -1.06% | 1704/9866 |
| d_20-Day Simple Moving Average | +0.2019 | -0.2398 | +0.2627 | -0.39% | -0.09% | 2144/9483 |
| true_ret | +0.1818 | -0.2798 | +0.2576 | -0.84% | -0.07% | 2047/9225 |
| Short Float | -0.1764 | +0.0745 | -0.2091 | 0.72% | n/a | 5627/0 |
| d_50-Day Simple Moving Average | +0.1752 | -0.2274 | +0.2185 | -0.47% | -0.06% | 2391/9215 |
| d_200-Day Simple Moving Average | +0.1659 | -0.2198 | +0.1810 | -0.41% | -0.08% | 2265/9334 |
| d_Performance (Quarter) | +0.1570 | -0.0616 | +0.1720 | -0.62% | 0.09% | 3383/7830 |
| d_Price | +0.1518 | -0.1253 | -0.0215 | -0.84% | -0.07% | 2047/9225 |
| d_Performance (YTD) | +0.1506 | -0.1990 | +0.1287 | -0.33% | -0.08% | 2111/9288 |
| Performance (Week) | +0.1419 | -0.2595 | +0.2685 | -1.02% | 0.08% | 2306/9289 |
| d_Forward P/E | -0.1182 | -0.0600 | -0.0048 | -1.65% | -1.39% | 731/2166 |
| d_Relative Strength Index (14) | +0.1016 | -0.1402 | -0.1567 | -0.35% | -0.08% | 2139/9284 |
| upside_pct_lvl | -0.0691 | +0.4754 | -0.3979 | 1.08% | -1.23% | 4354/272 |
| d_Volatility (Month) | +0.0587 | +0.0874 | +0.0258 | 1.61% | -1.37% | 4340/5388 |
| Institutional Transactions | -0.0498 | +0.0964 | -0.0828 | -0.97% | 3.71% | 2991/2019 |
| d_Average Volume | +0.0490 | -0.0077 | +0.0612 | 0.97% | -1.14% | 5444/5543 |
| d_Performance (Month) | +0.0409 | -0.0345 | +0.0126 | -1.02% | 0.29% | 3776/7723 |
| d_Short Ratio | -0.0398 | +0.0005 | -0.0452 | 1.36% | -0.69% | 3361/3089 |
| d_Short Float | +0.0307 | -0.0202 | +0.0713 | -0.75% | -0.97% | 33/128 |
| d_Insider Transactions | +0.0280 | -0.0194 | +0.0322 | 18.25% | -2.05% | 465/291 |
| d_Institutional Transactions | +0.0277 | +0.0599 | -0.0137 | -0.68% | 2.26% | 2166/2774 |
| d_EPS Surprise | +0.0266 | +0.0296 | +0.0374 | 5.17% | -4.51% | 55/68 |
| d_Beta | +0.0246 | +0.1541 | -0.0417 | 3.99% | -1.56% | 1888/1373 |
| Relative Volume | -0.0221 | +0.1333 | -0.0430 | -0.15% | n/a | 11525/0 |
| Performance (Month) | +0.0212 | -0.3138 | +0.1351 | -0.90% | 0.27% | 4105/7470 |

## Combinations

| Pattern | n | Mean long fwd | Hit up |
|---|---|---|---|
| true_ret>3% & DOWNTREND | 183 | -1.29% | 27.9% |
| true_ret>3% & UPTREND | 118 | -1.25% | 27.1% |
| true_ret>3% & MIXED | 120 | 0.84% | 47.5% |

## Risk dominance probes

| State | n | Mean long fwd | Mean fwd if score top quintile |
|---|---|---|---|
| EXTENDED | 204 | -0.44% | -2.74% |
| WASHED | 1657 | 4.81% | 0.42% |

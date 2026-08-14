# Factor attribution — signal 2026-08-13 → prediction day 2026-08-14

## Trade window (read this first)

| Role | Date | Meaning |
|------|------|---------|
| **Signal as-of** | **2026-08-13** | Features/scores formed from this snapshot (and deltas vs **2026-08-12**). Only data on/before this date. |
| **Prediction day** | **2026-08-14** | The trading day the forward return is for (exit snapshot). |
| **Entry price** | Price @ 2026-08-13 | Long: buy here; short: sell here. |
| **Exit price** | Price @ 2026-08-14 | Close proxy on prediction day. |
| **Return column** | `fwd_1d` | Long: exit/entry − 1; short = opposite. |

Graded **n=11566** names with valid entry and exit prices.

Provisional until multiple signal dates agree.

_Column guide: **IC** = Spearman(feature, long forward return); **IC↑** / **IC↓** = IC among names that went up / down._

## Score calibration (long fwd)
- Spearman IC(total_score, fwd_1d) = **-0.0908**

| Quintile | Mean long fwd | Hit up>1.5% | n |
|---|---|---|---|
| 1 | 1.96% | 26.6% | 2376 |
| 2 | 0.01% | 6.5% | 2587 |
| 3 | 1.25% | 7.0% | 1992 |
| 4 | 0.07% | 9.8% | 2377 |
| 5 | -0.13% | 22.7% | 2234 |

## Top |IC| features

| Feature | IC | IC↑ | IC↓ | Mean fwd when + | Mean fwd when − | n+/n− |
|---|---|---|---|---|---|---|
| d_Forward P/E | -0.2660 | -0.1304 | -0.2564 | -0.16% | 0.84% | 1842/1133 |
| d_200-Day Simple Moving Average | -0.2475 | -0.1594 | -0.2087 | 0.09% | 1.69% | 7679/3755 |
| d_Relative Strength Index (14) | -0.2369 | -0.2490 | +0.1309 | 0.12% | 1.70% | 7557/3584 |
| true_ret | -0.2342 | -0.1675 | -0.2022 | -0.21% | 0.86% | 7508/3526 |
| d_50-Day Simple Moving Average | -0.2322 | -0.1173 | -0.2370 | 0.14% | 1.60% | 7699/3736 |
| d_20-Day Simple Moving Average | -0.2274 | -0.1412 | -0.2207 | 0.60% | 0.66% | 7361/4064 |
| d_Performance (YTD) | -0.2246 | -0.1777 | -0.1527 | 0.12% | 1.71% | 7596/3587 |
| d_Price | -0.2123 | -0.2297 | +0.0173 | -0.21% | 0.86% | 7508/3526 |
| d_Performance (Week) | -0.1931 | -0.1280 | -0.1915 | 0.56% | 0.73% | 7773/3565 |
| d_Market Cap | -0.1750 | -0.1383 | -0.0286 | 0.50% | 2.11% | 3304/2408 |
| d_Performance (Quarter) | -0.1634 | -0.0742 | -0.2222 | 0.74% | 0.47% | 6584/4179 |
| d_Performance (Month) | -0.1067 | -0.0502 | -0.1298 | 0.33% | 1.03% | 6424/4768 |
| upside_pct_lvl | +0.1059 | +0.4573 | -0.3239 | 1.05% | -0.60% | 4274/375 |
| Relative Strength Index (14) | -0.0733 | -0.3664 | +0.2098 | 0.61% | n/a | 11441/0 |
| Institutional Transactions | +0.0640 | +0.0988 | -0.0106 | 0.36% | 2.35% | 2520/2519 |
| d_Beta | +0.0532 | +0.0386 | +0.0365 | 0.21% | 2.13% | 1659/1551 |
| Performance (Week) | -0.0500 | +0.0843 | -0.1839 | 0.31% | 1.47% | 8441/2943 |
| Performance (Month) | -0.0409 | -0.0775 | -0.0248 | 0.04% | 1.59% | 7103/4222 |
| d_Relative Volume | -0.0394 | -0.0122 | -0.0520 | 0.01% | 1.23% | 5381/5681 |
| d_Sales Growth Quarter Over Quarter | -0.0305 | -0.0078 | -0.0302 | -0.34% | 0.30% | 64/73 |
| d_Volatility (Month) | +0.0231 | +0.0432 | -0.0067 | 1.08% | 0.54% | 3942/5159 |
| d_EPS Surprise | -0.0188 | -0.0122 | -0.0297 | -0.35% | 0.63% | 119/101 |
| d_Total Debt/Equity | -0.0180 | -0.0260 | -0.0233 | 0.27% | 0.74% | 70/88 |
| Short Float | +0.0172 | +0.1735 | -0.2014 | 1.22% | n/a | 5701/0 |
| d_Profit Margin | +0.0151 | +0.0321 | -0.0135 | -0.22% | 0.18% | 103/71 |

## Combinations

| Pattern | n | Mean long fwd | Hit up |
|---|---|---|---|
| true_ret>3% & DOWNTREND | 399 | -0.75% | 28.1% |
| true_ret>3% & UPTREND | 469 | -1.12% | 18.8% |
| true_ret>3% & MIXED | 283 | -1.41% | 22.3% |

## Risk dominance probes

| State | n | Mean long fwd | Mean fwd if score top quintile |
|---|---|---|---|
| EXTENDED | 402 | -0.59% | -2.14% |
| WASHED | 505 | 11.94% | 0.69% |

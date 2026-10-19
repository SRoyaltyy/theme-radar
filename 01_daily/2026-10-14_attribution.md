# Factor attribution — signal 2026-10-14 → prediction day 2026-10-19

## Trade window (read this first)

| Role | Date | Meaning |
|------|------|---------|
| **Signal as-of** | **2026-10-14** | Features/scores formed from this snapshot (and deltas vs **2026-10-13**). Only data on/before this date. |
| **Prediction day** | **2026-10-19** | The trading day the forward return is for (exit snapshot). |
| **Entry price** | Price @ 2026-10-14 | Long: buy here; short: sell here. |
| **Exit price** | Price @ 2026-10-19 | Close proxy on prediction day. |
| **Return column** | `fwd_3d` | Long: exit/entry − 1; short = opposite. |

Graded **n=11707** names with valid entry and exit prices.

Provisional until multiple signal dates agree.

_Column guide: **IC** = Spearman(feature, long forward return); **IC↑** / **IC↓** = IC among names that went up / down._

## Score calibration (long fwd)
- Spearman IC(total_score, fwd_3d) = **0.2597**

| Quintile | Mean long fwd | Hit up>1.5% | n |
|---|---|---|---|
| 1 | -2.11% | 15.4% | 2351 |
| 2 | 0.29% | 14.9% | 2357 |
| 3 | 0.47% | 13.7% | 2349 |
| 4 | -0.13% | 13.6% | 2419 |
| 5 | 2.41% | 32.9% | 2231 |

## Top |IC| features

| Feature | IC | IC↑ | IC↓ | Mean fwd when + | Mean fwd when − | n+/n− |
|---|---|---|---|---|---|---|
| Performance (Week) | +0.4128 | +0.0045 | +0.5190 | 0.52% | -0.04% | 4242/7284 |
| true_ret | +0.3347 | -0.1703 | +0.4886 | 2.45% | -0.78% | 2303/8950 |
| d_50-Day Simple Moving Average | +0.3323 | -0.1267 | +0.4323 | 2.51% | -0.56% | 2751/8832 |
| d_20-Day Simple Moving Average | +0.3202 | -0.1347 | +0.4163 | 2.40% | -0.54% | 2762/8825 |
| d_200-Day Simple Moving Average | +0.3135 | -0.1349 | +0.3724 | 2.76% | -0.54% | 2497/9054 |
| d_Performance (YTD) | +0.3089 | -0.1318 | +0.3424 | 3.05% | -0.55% | 2337/9013 |
| d_Performance (Week) | +0.2766 | -0.0155 | +0.3273 | 1.51% | -0.76% | 4690/6810 |
| d_Performance (Month) | +0.2646 | +0.0131 | +0.3160 | 1.53% | -0.59% | 4084/7312 |
| d_Price | +0.2306 | -0.0429 | +0.0905 | 2.45% | -0.78% | 2303/8950 |
| d_Relative Strength Index (14) | +0.2283 | +0.0855 | -0.1639 | 2.95% | -0.55% | 2355/8992 |
| d_Forward P/E | +0.2178 | -0.0484 | +0.3127 | 0.96% | -0.16% | 782/2166 |
| upside_pct_lvl | -0.2163 | +0.2829 | -0.4224 | 1.80% | -0.52% | 4376/254 |
| Relative Strength Index (14) | +0.1719 | -0.0460 | +0.3293 | 0.16% | n/a | 11635/0 |
| Institutional Transactions | -0.0823 | +0.0290 | -0.0768 | 0.56% | 2.95% | 3260/1776 |
| d_Volatility (Month) | +0.0576 | +0.0607 | -0.0007 | 1.73% | -0.98% | 4272/5409 |
| d_Beta | +0.0411 | -0.0922 | +0.0883 | -1.96% | 2.47% | 543/932 |
| d_Relative Volume | -0.0409 | +0.0168 | -0.0424 | 0.23% | 0.15% | 6842/4465 |
| d_Performance (Quarter) | -0.0350 | -0.1912 | +0.0724 | 0.40% | 0.14% | 3279/7858 |
| d_Short Float | +0.0297 | -0.0094 | +0.0235 | -1.61% | -4.93% | 7/36 |
| d_EPS Surprise | +0.0269 | +0.0155 | -0.0100 | 1.34% | -2.35% | 5/8 |
| d_Market Cap | +0.0224 | -0.0221 | +0.0255 | 4.64% | -0.01% | 1340/4397 |
| d_Average Volume | +0.0215 | -0.0183 | -0.0193 | 0.87% | -0.53% | 5628/5381 |
| d_Analyst Recom | -0.0211 | -0.0218 | -0.0226 | -0.46% | 0.73% | 46/59 |
| Relative Volume | +0.0196 | +0.0881 | -0.0872 | 0.17% | n/a | 11462/0 |
| d_Total Debt/Equity | -0.0193 | -0.0051 | -0.0041 | -9.17% | -1.14% | 7/6 |

## Combinations

| Pattern | n | Mean long fwd | Hit up |
|---|---|---|---|
| true_ret>3% & DOWNTREND | 207 | 23.34% | 47.8% |
| true_ret>3% & UPTREND | 90 | 1.09% | 43.3% |
| true_ret>3% & MIXED | 84 | 0.28% | 42.9% |

## Risk dominance probes

| State | n | Mean long fwd | Mean fwd if score top quintile |
|---|---|---|---|
| EXTENDED | 134 | -1.38% | 1.08% |
| WASHED | 1770 | 1.29% | -1.67% |

# Factor attribution — signal 2026-10-28 → prediction day 2026-10-30

## Trade window (read this first)

| Role | Date | Meaning |
|------|------|---------|
| **Signal as-of** | **2026-10-28** | Features/scores formed from this snapshot (and deltas vs **2026-10-27**). Only data on/before this date. |
| **Prediction day** | **2026-10-30** | The trading day the forward return is for (exit snapshot). |
| **Entry price** | Price @ 2026-10-28 | Long: buy here; short: sell here. |
| **Exit price** | Price @ 2026-10-30 | Close proxy on prediction day. |
| **Return column** | `fwd_2d` | Long: exit/entry − 1; short = opposite. |

Graded **n=11761** names with valid entry and exit prices.

Provisional until multiple signal dates agree.

_Column guide: **IC** = Spearman(feature, long forward return); **IC↑** / **IC↓** = IC among names that went up / down._

## Score calibration (long fwd)
- Spearman IC(total_score, fwd_2d) = **-0.0713**

| Quintile | Mean long fwd | Hit up>1.5% | n |
|---|---|---|---|
| 1 | 3.08% | 20.1% | 2374 |
| 2 | 0.50% | 13.0% | 2616 |
| 3 | -1.26% | 13.3% | 2978 |
| 4 | 2.12% | 20.0% | 1530 |
| 5 | -3.65% | 20.0% | 2263 |

## Top |IC| features

| Feature | IC | IC↑ | IC↓ | Mean fwd when + | Mean fwd when − | n+/n− |
|---|---|---|---|---|---|---|
| Performance (Month) | +0.4214 | +0.0661 | +0.4980 | -0.07% | 0.11% | 5862/5725 |
| d_Beta | +0.4054 | +0.0261 | +0.4521 | 0.67% | 3.39% | 1746/2707 |
| d_20-Day Simple Moving Average | -0.3828 | -0.0927 | -0.4089 | -2.15% | 2.19% | 6823/4764 |
| d_Performance (Quarter) | +0.3696 | +0.1748 | +0.3020 | 2.35% | -1.12% | 3944/7250 |
| upside_pct_lvl | -0.3315 | +0.2039 | -0.3641 | -0.06% | -0.98% | 4303/329 |
| d_200-Day Simple Moving Average | -0.3104 | -0.0504 | -0.3188 | -1.93% | 1.99% | 7017/4517 |
| d_50-Day Simple Moving Average | -0.3096 | -0.0368 | -0.3370 | -1.81% | 2.17% | 7383/4182 |
| d_Relative Strength Index (14) | -0.3051 | +0.0035 | -0.1432 | -1.81% | 0.53% | 6861/4447 |
| true_ret | -0.2973 | -0.0701 | -0.3021 | -2.14% | 2.08% | 6739/4362 |
| d_Performance (YTD) | -0.2971 | -0.0590 | -0.2738 | -1.83% | 0.06% | 6841/4447 |
| d_Price | -0.2905 | -0.0425 | -0.2010 | -2.14% | 2.08% | 6739/4362 |
| Relative Strength Index (14) | +0.2864 | -0.1801 | +0.3904 | 0.00% | n/a | 11677/0 |
| d_Performance (Month) | -0.1593 | +0.0097 | -0.1591 | -0.76% | 1.58% | 7619/3841 |
| d_Forward P/E | -0.1555 | +0.0207 | -0.2072 | -1.04% | 0.12% | 1482/1453 |
| d_Market Cap | -0.1405 | +0.0020 | -0.0909 | -0.20% | 3.75% | 3205/2503 |
| Performance (Week) | +0.1118 | +0.0290 | +0.0908 | -1.45% | 1.04% | 6406/5107 |
| Institutional Transactions | -0.1059 | -0.0442 | -0.0992 | -1.61% | 9.08% | 3237/1813 |
| Short Float | -0.0508 | +0.2489 | -0.1633 | 2.19% | n/a | 5657/0 |
| Relative Volume | +0.0478 | +0.1466 | -0.0839 | -0.37% | n/a | 11451/0 |
| d_Volatility (Month) | -0.0423 | +0.0429 | -0.0446 | 1.41% | -1.61% | 4381/5069 |
| d_Short Float | +0.0326 | +0.0014 | +0.0258 | -1.54% | -0.09% | 30/21 |
| d_Performance (Week) | +0.0267 | +0.0922 | -0.0027 | -0.80% | -0.01% | 5070/6401 |
| d_Short Ratio | -0.0194 | -0.0404 | +0.0232 | -1.60% | 1.53% | 3251/3491 |
| d_Average Volume | +0.0179 | +0.0255 | -0.0249 | 0.98% | -1.64% | 5633/5345 |
| d_Target Price | +0.0137 | -0.0367 | +0.0168 | -0.06% | -0.60% | 231/246 |

## Combinations

| Pattern | n | Mean long fwd | Hit up |
|---|---|---|---|
| true_ret>3% & DOWNTREND | 833 | -2.94% | 11.6% |
| true_ret>3% & UPTREND | 240 | -3.40% | 26.2% |
| true_ret>3% & MIXED | 218 | -4.69% | 18.8% |

## Risk dominance probes

| State | n | Mean long fwd | Mean fwd if score top quintile |
|---|---|---|---|
| EXTENDED | 179 | -1.26% | -3.12% |
| WASHED | 1165 | 10.19% | -10.25% |

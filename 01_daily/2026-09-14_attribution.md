# Factor attribution — signal 2026-09-14 → prediction day 2026-09-17

## Trade window (read this first)

| Role | Date | Meaning |
|------|------|---------|
| **Signal as-of** | **2026-09-14** | Features/scores formed from this snapshot (and deltas vs **2026-09-11**). Only data on/before this date. |
| **Prediction day** | **2026-09-17** | The trading day the forward return is for (exit snapshot). |
| **Entry price** | Price @ 2026-09-14 | Long: buy here; short: sell here. |
| **Exit price** | Price @ 2026-09-17 | Close proxy on prediction day. |
| **Return column** | `fwd_3d` | Long: exit/entry − 1; short = opposite. |

Graded **n=11603** names with valid entry and exit prices.

Provisional until multiple signal dates agree.

_Column guide: **IC** = Spearman(feature, long forward return); **IC↑** / **IC↓** = IC among names that went up / down._

## Score calibration (long fwd)
- Spearman IC(total_score, fwd_3d) = **-0.2010**

| Quintile | Mean long fwd | Hit up>1.5% | n |
|---|---|---|---|
| 1 | 1.05% | 31.1% | 2518 |
| 2 | 0.19% | 12.2% | 2855 |
| 3 | -0.56% | 13.8% | 1662 |
| 4 | 0.61% | 10.3% | 2302 |
| 5 | 0.75% | 22.0% | 2266 |

## Top |IC| features

| Feature | IC | IC↑ | IC↓ | Mean fwd when + | Mean fwd when − | n+/n− |
|---|---|---|---|---|---|---|
| d_Relative Strength Index (14) | -0.3086 | -0.0310 | -0.2102 | 0.09% | 0.71% | 4020/7169 |
| d_Price | -0.3003 | -0.1417 | -0.2222 | 0.04% | 0.73% | 3934/7090 |
| d_200-Day Simple Moving Average | -0.2885 | -0.2460 | -0.1896 | 0.13% | 0.67% | 4134/7342 |
| d_Performance (YTD) | -0.2863 | -0.2485 | -0.1735 | 0.09% | 0.73% | 3999/7186 |
| d_20-Day Simple Moving Average | -0.2817 | -0.2328 | -0.1897 | 0.08% | 0.76% | 4797/6660 |
| d_50-Day Simple Moving Average | -0.2812 | -0.2454 | -0.1853 | 0.11% | 0.70% | 4336/7140 |
| true_ret | -0.2781 | -0.2808 | -0.1575 | 0.04% | 0.73% | 3934/7090 |
| d_Performance (Week) | -0.2490 | -0.2858 | -0.1166 | 0.24% | 0.62% | 4356/7015 |
| d_Forward P/E | -0.2426 | -0.1459 | -0.1578 | -1.49% | 0.13% | 1451/1497 |
| d_Performance (Quarter) | -0.1717 | -0.1491 | -0.1719 | 0.94% | 0.08% | 3719/7170 |
| d_Market Cap | -0.1546 | -0.0150 | -0.0892 | 0.87% | 0.49% | 2574/3108 |
| d_Performance (Month) | -0.1528 | -0.2218 | -0.0313 | 1.06% | 0.22% | 3326/7992 |
| Short Float | -0.0935 | +0.2765 | -0.2777 | 0.68% | n/a | 5705/0 |
| d_Volatility (Month) | -0.0476 | -0.1312 | +0.0103 | 0.26% | 0.88% | 4397/4729 |
| upside_pct_lvl | -0.0461 | +0.2716 | -0.3399 | -0.15% | -0.10% | 4366/273 |
| Performance (Week) | -0.0452 | -0.3468 | +0.1343 | 1.76% | 0.16% | 2230/9235 |
| d_Relative Volume | +0.0409 | +0.0433 | +0.0177 | 0.69% | 0.19% | 6641/4550 |
| Performance (Month) | -0.0356 | -0.2885 | +0.0956 | 0.14% | 0.58% | 3032/8386 |
| Relative Strength Index (14) | -0.0338 | +0.0308 | -0.0790 | 0.46% | n/a | 11524/0 |
| d_Beta | +0.0332 | +0.0978 | -0.0605 | 0.34% | 1.52% | 1733/1692 |
| d_EPS Surprise | +0.0285 | +0.0270 | +0.0156 | -1.72% | -8.17% | 7/9 |
| d_Insider Transactions | -0.0241 | -0.0330 | +0.0056 | -1.30% | -0.59% | 472/419 |
| d_Short Float | +0.0218 | -0.0623 | +0.0580 | -1.07% | 1.05% | 103/256 |
| d_Institutional Transactions | +0.0217 | -0.0279 | +0.0312 | 0.49% | -0.50% | 2142/1491 |
| d_Analyst Recom | -0.0189 | -0.0210 | +0.0049 | -1.32% | -0.70% | 96/124 |

## Combinations

| Pattern | n | Mean long fwd | Hit up |
|---|---|---|---|
| true_ret>3% & DOWNTREND | 329 | 6.46% | 21.6% |
| true_ret>3% & UPTREND | 364 | -0.21% | 30.2% |
| true_ret>3% & MIXED | 223 | 3.70% | 18.4% |

## Risk dominance probes

| State | n | Mean long fwd | Mean fwd if score top quintile |
|---|---|---|---|
| EXTENDED | 158 | 13.63% | 1.01% |
| WASHED | 1684 | 2.03% | 3.17% |

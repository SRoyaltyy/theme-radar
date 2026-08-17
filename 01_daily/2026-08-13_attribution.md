# Factor attribution — signal 2026-08-13 → prediction day 2026-08-17

## Trade window (read this first)

| Role | Date | Meaning |
|------|------|---------|
| **Signal as-of** | **2026-08-13** | Features/scores formed from this snapshot (and deltas vs **2026-08-12**). Only data on/before this date. |
| **Prediction day** | **2026-08-17** | The trading day the forward return is for (exit snapshot). |
| **Entry price** | Price @ 2026-08-13 | Long: buy here; short: sell here. |
| **Exit price** | Price @ 2026-08-17 | Close proxy on prediction day. |
| **Return column** | `fwd_2d` | Long: exit/entry − 1; short = opposite. |

Graded **n=11544** names with valid entry and exit prices.

Provisional until multiple signal dates agree.

_Column guide: **IC** = Spearman(feature, long forward return); **IC↑** / **IC↓** = IC among names that went up / down._

## Score calibration (long fwd)
- Spearman IC(total_score, fwd_2d) = **-0.1428**

| Quintile | Mean long fwd | Hit up>1.5% | n |
|---|---|---|---|
| 1 | 2.68% | 32.2% | 2360 |
| 2 | -0.19% | 10.1% | 2585 |
| 3 | 1.16% | 8.3% | 1990 |
| 4 | -0.32% | 11.7% | 2375 |
| 5 | -0.91% | 23.1% | 2234 |

## Top |IC| features

| Feature | IC | IC↑ | IC↓ | Mean fwd when + | Mean fwd when − | n+/n− |
|---|---|---|---|---|---|---|
| d_200-Day Simple Moving Average | -0.3226 | -0.1823 | -0.2747 | -0.42% | 2.29% | 7676/3754 |
| d_20-Day Simple Moving Average | -0.3154 | -0.1824 | -0.2871 | 0.35% | 0.69% | 7358/4063 |
| true_ret | -0.3056 | -0.1903 | -0.2644 | -0.74% | 1.70% | 7506/3526 |
| d_Performance (YTD) | -0.2974 | -0.1954 | -0.2220 | -0.41% | 2.39% | 7593/3587 |
| d_50-Day Simple Moving Average | -0.2972 | -0.1404 | -0.2940 | -0.36% | 2.17% | 7696/3735 |
| d_Forward P/E | -0.2957 | -0.1234 | -0.2731 | -1.24% | 0.67% | 1842/1133 |
| d_Relative Strength Index (14) | -0.2920 | -0.2202 | +0.0623 | -0.42% | 2.38% | 7555/3584 |
| d_Price | -0.2806 | -0.2163 | -0.0632 | -0.74% | 1.70% | 7506/3526 |
| d_Performance (Quarter) | -0.2733 | -0.1176 | -0.2631 | 0.06% | 1.02% | 6575/4174 |
| d_Performance (Week) | -0.2464 | -0.1655 | -0.2399 | 0.22% | 0.98% | 7769/3564 |
| d_Market Cap | -0.2247 | -0.1047 | -0.0605 | -0.44% | 2.70% | 3298/2407 |
| d_Performance (Month) | -0.1369 | -0.0430 | -0.1470 | -0.04% | 1.15% | 6420/4757 |
| d_Beta | +0.1022 | +0.0589 | +0.0858 | -0.10% | 2.54% | 1657/1547 |
| Institutional Transactions | +0.0876 | +0.0774 | -0.0069 | 0.64% | 1.29% | 2517/2514 |
| Short Float | -0.0643 | +0.1941 | -0.2654 | 0.91% | n/a | 5691/0 |
| upside_pct_lvl | +0.0604 | +0.3665 | -0.3091 | 0.22% | -1.64% | 4270/374 |
| Relative Strength Index (14) | -0.0490 | -0.2763 | +0.2366 | 0.46% | n/a | 11422/0 |
| Performance (Month) | -0.0414 | -0.0385 | -0.0306 | -0.31% | 1.77% | 7097/4210 |
| d_Short Float | +0.0317 | +0.0035 | +0.0293 | 0.28% | -1.66% | 79/130 |
| d_Relative Volume | -0.0310 | -0.0073 | -0.0391 | 0.12% | 0.85% | 5379/5678 |
| Relative Volume | -0.0284 | +0.1524 | -0.1271 | 0.48% | n/a | 11281/0 |
| d_Sales Year Over Year TTM | +0.0241 | +0.0167 | +0.0344 | -0.16% | -1.76% | 76/83 |
| d_Target Price | +0.0204 | +0.0002 | +0.0357 | 0.00% | -0.99% | 323/207 |
| d_Volatility (Month) | -0.0195 | -0.0156 | -0.0192 | 0.92% | 0.38% | 3941/5158 |
| d_Short Ratio | -0.0181 | -0.0046 | -0.0126 | -0.30% | 0.89% | 4120/2745 |

## Combinations

| Pattern | n | Mean long fwd | Hit up |
|---|---|---|---|
| true_ret>3% & DOWNTREND | 398 | -1.70% | 22.1% |
| true_ret>3% & UPTREND | 469 | -2.13% | 23.9% |
| true_ret>3% & MIXED | 283 | -2.93% | 23.0% |

## Risk dominance probes

| State | n | Mean long fwd | Mean fwd if score top quintile |
|---|---|---|---|
| EXTENDED | 400 | -1.26% | -2.48% |
| WASHED | 505 | 15.39% | -1.84% |

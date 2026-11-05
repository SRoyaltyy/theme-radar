# Factor attribution — signal 2026-11-02 → prediction day 2026-11-05

## Trade window (read this first)

| Role | Date | Meaning |
|------|------|---------|
| **Signal as-of** | **2026-11-02** | Features/scores formed from this snapshot (and deltas vs **2026-10-30**). Only data on/before this date. |
| **Prediction day** | **2026-11-05** | The trading day the forward return is for (exit snapshot). |
| **Entry price** | Price @ 2026-11-02 | Long: buy here; short: sell here. |
| **Exit price** | Price @ 2026-11-05 | Close proxy on prediction day. |
| **Return column** | `fwd_3d` | Long: exit/entry − 1; short = opposite. |

Graded **n=11733** names with valid entry and exit prices.

Provisional until multiple signal dates agree.

_Column guide: **IC** = Spearman(feature, long forward return); **IC↑** / **IC↓** = IC among names that went up / down._

## Score calibration (long fwd)
- Spearman IC(total_score, fwd_3d) = **0.3515**

| Quintile | Mean long fwd | Hit up>1.5% | n |
|---|---|---|---|
| 1 | -7.78% | 11.7% | 2477 |
| 2 | -2.85% | 8.4% | 2625 |
| 3 | -2.02% | 11.4% | 1941 |
| 4 | 0.89% | 13.7% | 2360 |
| 5 | -0.12% | 34.6% | 2330 |

## Top |IC| features

| Feature | IC | IC↑ | IC↓ | Mean fwd when + | Mean fwd when − | n+/n− |
|---|---|---|---|---|---|---|
| d_Performance (Quarter) | +0.4083 | +0.0816 | +0.4414 | 0.83% | -3.75% | 3314/7888 |
| d_Performance (Month) | +0.3954 | +0.1957 | +0.4010 | -0.14% | -3.99% | 4540/6953 |
| Performance (Month) | +0.3694 | -0.0714 | +0.4662 | -0.39% | -4.06% | 5043/6526 |
| d_Performance (Week) | +0.3556 | +0.2445 | +0.3691 | 0.03% | -4.42% | 5027/6532 |
| true_ret | +0.3436 | +0.2053 | +0.3700 | -0.55% | -4.72% | 5177/6018 |
| d_Price | +0.3420 | +0.1923 | +0.3335 | -0.55% | -4.72% | 5177/6018 |
| d_Performance (YTD) | +0.3404 | +0.1859 | +0.3530 | -0.62% | -4.69% | 5275/6092 |
| d_200-Day Simple Moving Average | +0.3384 | +0.2106 | +0.3416 | -0.08% | -4.62% | 5481/6114 |
| d_Forward P/E | +0.3316 | +0.0306 | +0.3954 | -0.30% | -5.73% | 1886/1076 |
| Relative Strength Index (14) | +0.3302 | -0.1692 | +0.3601 | -2.46% | n/a | 11651/0 |
| d_50-Day Simple Moving Average | +0.3262 | +0.2337 | +0.3290 | -0.20% | -4.69% | 5714/5903 |
| d_Market Cap | +0.2864 | +0.0034 | +0.2839 | -0.15% | -4.76% | 3046/2678 |
| Performance (Week) | +0.2717 | +0.0319 | +0.3112 | -1.17% | -3.60% | 5349/6237 |
| d_20-Day Simple Moving Average | +0.2680 | +0.2348 | +0.2734 | -0.50% | -4.36% | 5655/5952 |
| upside_pct_lvl | -0.2503 | +0.2954 | -0.3694 | -2.17% | -0.96% | 4299/334 |
| d_Relative Strength Index (14) | +0.2464 | +0.2452 | +0.2373 | -0.14% | -4.69% | 5278/6092 |
| d_Beta | -0.2337 | +0.1474 | -0.3126 | -3.50% | -0.96% | 3609/3660 |
| d_Volatility (Month) | -0.1817 | +0.1564 | -0.2560 | -3.27% | -1.86% | 5611/4520 |
| Institutional Transactions | -0.0908 | +0.0456 | -0.0947 | -2.42% | -1.96% | 3193/1831 |
| Short Float | -0.0792 | +0.2704 | -0.2298 | -2.11% | n/a | 5639/0 |
| d_Average Volume | +0.0460 | +0.0375 | -0.0109 | -2.09% | -3.07% | 6434/4647 |
| d_Institutional Transactions | +0.0384 | -0.0293 | +0.0409 | -2.69% | -1.83% | 1995/2370 |
| d_Short Ratio | -0.0268 | -0.0600 | +0.0026 | -3.46% | -2.60% | 2939/4104 |
| d_Relative Volume | +0.0244 | -0.0449 | +0.0417 | -1.89% | -3.08% | 5639/5686 |
| d_Sales Year Over Year TTM | -0.0228 | +0.0060 | +0.0053 | -3.04% | -0.71% | 62/46 |

## Combinations

| Pattern | n | Mean long fwd | Hit up |
|---|---|---|---|
| true_ret>3% & DOWNTREND | 462 | -1.51% | 35.5% |
| true_ret>3% & UPTREND | 357 | 0.85% | 36.1% |
| true_ret>3% & MIXED | 317 | 1.53% | 45.4% |

## Risk dominance probes

| State | n | Mean long fwd | Mean fwd if score top quintile |
|---|---|---|---|
| EXTENDED | 270 | 0.01% | 5.16% |
| WASHED | 1780 | -7.04% | 4.66% |

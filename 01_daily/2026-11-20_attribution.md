# Factor attribution — signal 2026-11-20 → prediction day 2026-11-25

## Trade window (read this first)

| Role | Date | Meaning |
|------|------|---------|
| **Signal as-of** | **2026-11-20** | Features/scores formed from this snapshot (and deltas vs **2026-11-19**). Only data on/before this date. |
| **Prediction day** | **2026-11-25** | The trading day the forward return is for (exit snapshot). |
| **Entry price** | Price @ 2026-11-20 | Long: buy here; short: sell here. |
| **Exit price** | Price @ 2026-11-25 | Close proxy on prediction day. |
| **Return column** | `fwd_3d` | Long: exit/entry − 1; short = opposite. |

Graded **n=11731** names with valid entry and exit prices.

Provisional until multiple signal dates agree.

_Column guide: **IC** = Spearman(feature, long forward return); **IC↑** / **IC↓** = IC among names that went up / down._

## Score calibration (long fwd)
- Spearman IC(total_score, fwd_3d) = **-0.3294**

| Quintile | Mean long fwd | Hit up>1.5% | n |
|---|---|---|---|
| 1 | 5.59% | 92.2% | 2366 |
| 2 | 8.73% | 80.8% | 2642 |
| 3 | 8.51% | 68.4% | 2037 |
| 4 | 5.80% | 58.7% | 2426 |
| 5 | 4.04% | 28.9% | 2260 |

## Top |IC| features

| Feature | IC | IC↑ | IC↓ | Mean fwd when + | Mean fwd when − | n+/n− |
|---|---|---|---|---|---|---|
| Performance (Week) | -0.4111 | -0.5614 | +0.1858 | 0.65% | 7.08% | 1495/10122 |
| d_200-Day Simple Moving Average | -0.3995 | -0.4405 | +0.0266 | 1.44% | 7.32% | 2084/9549 |
| d_50-Day Simple Moving Average | -0.3935 | -0.4656 | +0.0576 | 1.50% | 7.16% | 2200/9449 |
| true_ret | -0.3928 | -0.5072 | +0.1326 | 1.39% | 7.04% | 1959/9439 |
| d_Performance (YTD) | -0.3907 | -0.4065 | +0.0120 | 1.42% | 7.39% | 1978/9465 |
| d_Price | -0.3877 | -0.3019 | -0.0699 | 1.39% | 7.04% | 1959/9439 |
| d_20-Day Simple Moving Average | -0.3823 | -0.4636 | +0.0655 | 2.76% | 7.11% | 2318/9341 |
| d_Performance (Week) | -0.3678 | -0.4419 | +0.0038 | 3.93% | 6.91% | 2415/9153 |
| d_Performance (Quarter) | -0.3628 | -0.3977 | +0.0237 | 4.65% | 7.28% | 2290/8996 |
| d_Performance (Month) | -0.3603 | -0.4093 | +0.0220 | 7.08% | 6.57% | 1866/9641 |
| Performance (Month) | -0.3107 | -0.4675 | +0.2224 | 1.32% | 7.81% | 2141/9441 |
| Short Float | +0.2623 | +0.3049 | -0.0937 | 10.66% | n/a | 5607/0 |
| d_Relative Strength Index (14) | -0.2535 | -0.1419 | +0.0020 | 1.38% | 7.38% | 2002/9440 |
| Relative Strength Index (14) | -0.2497 | -0.2171 | +0.1060 | 6.57% | n/a | 11664/0 |
| d_Volatility (Month) | +0.2269 | +0.3696 | -0.3824 | 7.37% | 5.12% | 7778/2674 |
| d_Market Cap | -0.2187 | -0.0888 | -0.1044 | 4.76% | 10.76% | 947/4775 |
| d_Forward P/E | -0.1731 | -0.2058 | +0.0677 | 3.65% | 4.02% | 454/2446 |
| Relative Volume | +0.1427 | +0.1081 | +0.0067 | 6.30% | n/a | 11551/0 |
| upside_pct_lvl | +0.1133 | +0.4174 | -0.4772 | 10.63% | 2.56% | 4462/165 |
| d_Relative Volume | +0.0755 | +0.0628 | +0.0274 | 7.44% | 4.34% | 7343/4041 |
| d_Beta | +0.0454 | +0.1025 | -0.1001 | 13.04% | 5.15% | 3455/3375 |
| d_Target Price | -0.0317 | -0.0416 | +0.0217 | 4.55% | 5.10% | 177/242 |
| d_Short Ratio | -0.0315 | -0.0222 | -0.0183 | 4.40% | 5.09% | 2662/4394 |
| d_Institutional Ownership | -0.0265 | -0.0565 | +0.0116 | -0.07% | 9.52% | 9/24 |
| d_Average Volume | +0.0265 | +0.0160 | -0.0037 | 7.60% | 4.48% | 6799/4331 |

## Combinations

| Pattern | n | Mean long fwd | Hit up |
|---|---|---|---|
| true_ret>3% & DOWNTREND | 156 | 12.95% | 49.4% |
| true_ret>3% & UPTREND | 136 | -8.89% | 16.2% |
| true_ret>3% & MIXED | 69 | -5.83% | 24.6% |

## Risk dominance probes

| State | n | Mean long fwd | Mean fwd if score top quintile |
|---|---|---|---|
| EXTENDED | 174 | -6.37% | -11.23% |
| WASHED | 5092 | 11.08% | 11.99% |

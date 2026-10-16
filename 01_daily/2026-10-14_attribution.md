# Factor attribution — signal 2026-10-14 → prediction day 2026-10-16

## Trade window (read this first)

| Role | Date | Meaning |
|------|------|---------|
| **Signal as-of** | **2026-10-14** | Features/scores formed from this snapshot (and deltas vs **2026-10-13**). Only data on/before this date. |
| **Prediction day** | **2026-10-16** | The trading day the forward return is for (exit snapshot). |
| **Entry price** | Price @ 2026-10-14 | Long: buy here; short: sell here. |
| **Exit price** | Price @ 2026-10-16 | Close proxy on prediction day. |
| **Return column** | `fwd_2d` | Long: exit/entry − 1; short = opposite. |

Graded **n=11725** names with valid entry and exit prices.

Provisional until multiple signal dates agree.

_Column guide: **IC** = Spearman(feature, long forward return); **IC↑** / **IC↓** = IC among names that went up / down._

## Score calibration (long fwd)
- Spearman IC(total_score, fwd_2d) = **0.2573**

| Quintile | Mean long fwd | Hit up>1.5% | n |
|---|---|---|---|
| 1 | -2.56% | 18.0% | 2353 |
| 2 | -0.98% | 18.1% | 2362 |
| 3 | 0.66% | 20.3% | 2354 |
| 4 | -0.07% | 16.6% | 2422 |
| 5 | 0.65% | 38.3% | 2234 |

## Top |IC| features

| Feature | IC | IC↑ | IC↓ | Mean fwd when + | Mean fwd when − | n+/n− |
|---|---|---|---|---|---|---|
| Performance (Week) | +0.4432 | +0.0436 | +0.5557 | 0.86% | -1.26% | 4242/7288 |
| d_50-Day Simple Moving Average | +0.3645 | -0.0794 | +0.4791 | 1.24% | -1.01% | 2752/8834 |
| d_20-Day Simple Moving Average | +0.3521 | -0.0898 | +0.4656 | 1.10% | -0.97% | 2763/8827 |
| true_ret | +0.3503 | -0.1235 | +0.5239 | 0.79% | -0.95% | 2304/8952 |
| d_200-Day Simple Moving Average | +0.3501 | -0.0872 | +0.4345 | 1.27% | -0.95% | 2498/9056 |
| d_Performance (YTD) | +0.3457 | -0.0831 | +0.4107 | 1.41% | -0.95% | 2338/9015 |
| d_Performance (Week) | +0.3381 | +0.0723 | +0.4009 | 0.83% | -1.38% | 4690/6813 |
| d_Relative Strength Index (14) | +0.3067 | +0.0789 | -0.1289 | 1.38% | -0.96% | 2356/8994 |
| d_Forward P/E | +0.3018 | +0.0342 | +0.3651 | 1.42% | 0.03% | 782/2166 |
| d_Performance (Month) | +0.2819 | +0.0291 | +0.3867 | 0.38% | -0.95% | 4091/7319 |
| d_Price | +0.2789 | -0.0205 | +0.1963 | 0.79% | -0.95% | 2304/8952 |
| upside_pct_lvl | -0.2311 | +0.2315 | -0.3395 | -0.06% | -0.48% | 4378/258 |
| Relative Strength Index (14) | +0.1135 | -0.0248 | +0.3279 | -0.47% | n/a | 11653/0 |
| Institutional Transactions | -0.0977 | -0.0097 | -0.1150 | -0.38% | 0.39% | 3265/1778 |
| d_Performance (Quarter) | -0.0897 | -0.2019 | +0.0303 | -1.11% | -0.16% | 3285/7868 |
| Performance (Month) | -0.0827 | -0.3141 | +0.1998 | -1.12% | -0.14% | 3837/7712 |
| d_Beta | +0.0671 | -0.0682 | +0.1178 | -1.38% | -0.11% | 544/932 |
| d_Volatility (Month) | +0.0620 | +0.0557 | -0.0188 | -0.22% | -0.83% | 4275/5409 |
| d_Market Cap | +0.0527 | -0.0101 | +0.0956 | 1.34% | -0.63% | 1343/4398 |
| d_Target Price | -0.0479 | +0.0059 | +0.0181 | 0.12% | 0.77% | 194/305 |
| d_Average Volume | +0.0462 | -0.0293 | -0.0349 | -0.29% | -0.69% | 5631/5382 |
| Relative Volume | +0.0444 | +0.0762 | -0.1161 | -0.48% | n/a | 11465/0 |
| d_Short Ratio | -0.0360 | +0.0208 | +0.0205 | -0.46% | -0.13% | 3415/3579 |
| d_Total Debt/Equity | -0.0322 | -0.0488 | -0.0422 | -8.53% | 1.73% | 7/6 |
| d_Short Float | +0.0283 | -0.0407 | +0.0327 | 1.25% | -3.64% | 7/36 |

## Combinations

| Pattern | n | Mean long fwd | Hit up |
|---|---|---|---|
| true_ret>3% & DOWNTREND | 207 | 1.67% | 52.7% |
| true_ret>3% & UPTREND | 90 | 2.02% | 48.9% |
| true_ret>3% & MIXED | 84 | 1.37% | 46.4% |

## Risk dominance probes

| State | n | Mean long fwd | Mean fwd if score top quintile |
|---|---|---|---|
| EXTENDED | 135 | 0.14% | 4.23% |
| WASHED | 1775 | -0.57% | -1.12% |

# Factor attribution — signal 2026-10-14 → prediction day 2026-10-15

## Trade window (read this first)

| Role | Date | Meaning |
|------|------|---------|
| **Signal as-of** | **2026-10-14** | Features/scores formed from this snapshot (and deltas vs **2026-10-13**). Only data on/before this date. |
| **Prediction day** | **2026-10-15** | The trading day the forward return is for (exit snapshot). |
| **Entry price** | Price @ 2026-10-14 | Long: buy here; short: sell here. |
| **Exit price** | Price @ 2026-10-15 | Close proxy on prediction day. |
| **Return column** | `fwd_1d` | Long: exit/entry − 1; short = opposite. |

Graded **n=11725** names with valid entry and exit prices.

Provisional until multiple signal dates agree.

_Column guide: **IC** = Spearman(feature, long forward return); **IC↑** / **IC↓** = IC among names that went up / down._

## Score calibration (long fwd)
- Spearman IC(total_score, fwd_1d) = **0.0872**

| Quintile | Mean long fwd | Hit up>1.5% | n |
|---|---|---|---|
| 1 | 0.82% | 32.8% | 2353 |
| 2 | 0.90% | 28.8% | 2362 |
| 3 | 1.57% | 23.7% | 2354 |
| 4 | 0.72% | 20.6% | 2422 |
| 5 | 1.45% | 42.4% | 2234 |

## Top |IC| features

| Feature | IC | IC↑ | IC↓ | Mean fwd when + | Mean fwd when − | n+/n− |
|---|---|---|---|---|---|---|
| Short Float | +0.2648 | +0.2980 | -0.1403 | 1.59% | n/a | 5674/0 |
| Performance (Month) | -0.2164 | -0.4072 | +0.1582 | 0.37% | 1.46% | 3837/7712 |
| d_Performance (Quarter) | -0.1668 | -0.2456 | +0.0767 | 0.79% | 1.28% | 3285/7868 |
| d_Performance (Month) | +0.1434 | -0.0342 | +0.2519 | 1.37% | 0.97% | 4091/7319 |
| Relative Strength Index (14) | -0.1394 | -0.2335 | +0.1845 | 1.09% | n/a | 11653/0 |
| d_Relative Strength Index (14) | +0.1154 | +0.1776 | -0.0688 | 1.72% | 0.96% | 2356/8994 |
| d_Forward P/E | +0.1135 | -0.0810 | +0.3117 | 1.75% | 1.37% | 782/2166 |
| Relative Volume | +0.0895 | +0.1116 | -0.0121 | 1.11% | n/a | 11465/0 |
| d_Performance (Week) | +0.0885 | -0.0654 | +0.2376 | 1.48% | 0.85% | 4690/6813 |
| Performance (Week) | +0.0556 | -0.1610 | +0.3175 | 0.98% | 1.17% | 4242/7288 |
| d_Beta | -0.0542 | -0.1265 | +0.0169 | 0.52% | 3.50% | 544/932 |
| upside_pct_lvl | +0.0524 | +0.3091 | -0.3425 | 1.99% | 0.94% | 4378/258 |
| d_Market Cap | -0.0501 | -0.0536 | +0.0787 | 2.62% | 1.26% | 1343/4398 |
| d_Volatility (Month) | +0.0463 | +0.0456 | -0.0402 | 1.50% | 0.96% | 4275/5409 |
| d_50-Day Simple Moving Average | +0.0339 | -0.2037 | +0.2899 | 1.67% | 0.92% | 2752/8834 |
| d_Total Debt/Equity | -0.0322 | -0.0014 | -0.0500 | -6.89% | 1.37% | 7/6 |
| d_Target Price | -0.0322 | +0.0043 | +0.0002 | 0.94% | 1.58% | 194/305 |
| d_Short Float | +0.0305 | +0.0041 | +0.0547 | 2.67% | -0.40% | 7/36 |
| d_20-Day Simple Moving Average | +0.0262 | -0.2068 | +0.2799 | 1.63% | 0.93% | 2763/8827 |
| d_Performance (YTD) | +0.0258 | -0.1903 | +0.2074 | 1.73% | 0.96% | 2338/9015 |
| d_Relative Volume | +0.0242 | +0.0496 | +0.0167 | 1.30% | 0.79% | 6844/4467 |
| d_Price | +0.0227 | -0.0554 | +0.0544 | 1.06% | 0.96% | 2304/8952 |
| d_EPS Surprise | +0.0205 | +0.0355 | +0.0064 | 1.46% | -0.20% | 5/8 |
| d_Institutional Ownership | +0.0202 | -0.0050 | +0.0150 | 1.74% | 1.80% | 549/336 |
| d_Average Volume | +0.0197 | -0.0081 | -0.0631 | 1.27% | 0.96% | 5631/5382 |

## Combinations

| Pattern | n | Mean long fwd | Hit up |
|---|---|---|---|
| true_ret>3% & DOWNTREND | 207 | 1.59% | 49.3% |
| true_ret>3% & UPTREND | 90 | 1.49% | 48.9% |
| true_ret>3% & MIXED | 84 | -0.84% | 34.5% |

## Risk dominance probes

| State | n | Mean long fwd | Mean fwd if score top quintile |
|---|---|---|---|
| EXTENDED | 135 | 0.08% | 1.31% |
| WASHED | 1775 | 2.90% | 2.30% |

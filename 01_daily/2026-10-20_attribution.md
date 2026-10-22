# Factor attribution — signal 2026-10-20 → prediction day 2026-10-22

## Trade window (read this first)

| Role | Date | Meaning |
|------|------|---------|
| **Signal as-of** | **2026-10-20** | Features/scores formed from this snapshot (and deltas vs **2026-10-19**). Only data on/before this date. |
| **Prediction day** | **2026-10-22** | The trading day the forward return is for (exit snapshot). |
| **Entry price** | Price @ 2026-10-20 | Long: buy here; short: sell here. |
| **Exit price** | Price @ 2026-10-22 | Close proxy on prediction day. |
| **Return column** | `fwd_2d` | Long: exit/entry − 1; short = opposite. |

Graded **n=11744** names with valid entry and exit prices.

Provisional until multiple signal dates agree.

_Column guide: **IC** = Spearman(feature, long forward return); **IC↑** / **IC↓** = IC among names that went up / down._

## Score calibration (long fwd)
- Spearman IC(total_score, fwd_2d) = **0.3252**

| Quintile | Mean long fwd | Hit up>1.5% | n |
|---|---|---|---|
| 1 | -2.40% | 11.0% | 2422 |
| 2 | 0.94% | 14.4% | 2362 |
| 3 | -0.11% | 13.2% | 2718 |
| 4 | 0.17% | 21.5% | 1919 |
| 5 | 0.62% | 44.9% | 2323 |

## Top |IC| features

| Feature | IC | IC↑ | IC↓ | Mean fwd when + | Mean fwd when − | n+/n− |
|---|---|---|---|---|---|---|
| Performance (Week) | +0.4460 | +0.1753 | +0.4921 | 0.82% | -0.90% | 4814/6713 |
| Relative Strength Index (14) | +0.3516 | +0.0222 | +0.4462 | -0.17% | n/a | 11664/0 |
| Performance (Month) | +0.3389 | -0.0278 | +0.5276 | 0.66% | -0.51% | 3363/8197 |
| d_Performance (Month) | +0.3314 | +0.2598 | +0.1773 | 0.32% | -0.62% | 5450/5962 |
| d_Price | +0.3051 | +0.2124 | +0.2548 | 0.03% | -2.14% | 7882/3144 |
| upside_pct_lvl | -0.2948 | +0.1078 | -0.3506 | -0.30% | 0.92% | 4324/311 |
| d_Forward P/E | +0.2936 | +0.1755 | +0.2439 | 1.18% | -1.88% | 2211/739 |
| d_Market Cap | +0.2847 | +0.1157 | +0.1782 | 0.45% | 0.83% | 3934/1835 |
| d_Relative Strength Index (14) | +0.2841 | +0.0950 | +0.2629 | 0.01% | -0.54% | 7974/3266 |
| d_Performance (YTD) | +0.2627 | +0.2705 | +0.1587 | 0.01% | -0.53% | 7976/3237 |
| d_Beta | +0.2550 | -0.0127 | +0.3068 | 0.75% | 0.25% | 1326/1854 |
| d_200-Day Simple Moving Average | +0.2545 | +0.3121 | +0.1099 | 0.03% | -0.66% | 8217/3329 |
| true_ret | +0.2403 | +0.3154 | +0.1245 | 0.03% | -2.14% | 7882/3144 |
| d_50-Day Simple Moving Average | +0.2267 | +0.3393 | +0.0505 | -0.07% | -0.49% | 8579/2972 |
| d_Performance (Quarter) | +0.1637 | +0.2661 | -0.0123 | -0.19% | -0.02% | 8104/3015 |
| d_20-Day Simple Moving Average | +0.1272 | +0.3267 | -0.0867 | 0.22% | -1.58% | 8987/2573 |
| Relative Volume | +0.0755 | +0.0587 | -0.0316 | -0.18% | n/a | 11411/0 |
| d_Performance (Week) | +0.0670 | +0.2601 | -0.1309 | 0.20% | -1.06% | 8068/3385 |
| Short Float | +0.0648 | +0.2421 | -0.1790 | 0.60% | n/a | 5662/0 |
| Institutional Transactions | -0.0482 | +0.0542 | -0.0750 | 1.10% | -0.16% | 3260/1788 |
| d_Relative Volume | +0.0393 | +0.0443 | +0.0101 | -0.28% | -0.03% | 5673/5610 |
| d_Target Price | -0.0307 | -0.0355 | +0.0118 | -0.60% | 0.02% | 219/309 |
| d_Short Float | +0.0307 | +0.0250 | +0.0460 | 115.79% | -3.32% | 38/54 |
| d_Institutional Ownership | +0.0278 | +0.0257 | +0.0257 | n/a | -4.66% | 0/5 |
| d_Sales Growth Quarter Over Quarter | -0.0271 | -0.0336 | -0.0258 | -0.08% | 3.57% | 16/15 |

## Combinations

| Pattern | n | Mean long fwd | Hit up |
|---|---|---|---|
| true_ret>3% & DOWNTREND | 724 | -0.41% | 33.6% |
| true_ret>3% & UPTREND | 322 | 1.10% | 50.9% |
| true_ret>3% & MIXED | 222 | -0.43% | 39.6% |

## Risk dominance probes

| State | n | Mean long fwd | Mean fwd if score top quintile |
|---|---|---|---|
| EXTENDED | 160 | -0.82% | -2.94% |
| WASHED | 1551 | -0.05% | -2.89% |

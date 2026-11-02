# Factor attribution — signal 2026-10-28 → prediction day 2026-11-02

## Trade window (read this first)

| Role | Date | Meaning |
|------|------|---------|
| **Signal as-of** | **2026-10-28** | Features/scores formed from this snapshot (and deltas vs **2026-10-27**). Only data on/before this date. |
| **Prediction day** | **2026-11-02** | The trading day the forward return is for (exit snapshot). |
| **Entry price** | Price @ 2026-10-28 | Long: buy here; short: sell here. |
| **Exit price** | Price @ 2026-11-02 | Close proxy on prediction day. |
| **Return column** | `fwd_3d` | Long: exit/entry − 1; short = opposite. |

Graded **n=11720** names with valid entry and exit prices.

Provisional until multiple signal dates agree.

_Column guide: **IC** = Spearman(feature, long forward return); **IC↑** / **IC↓** = IC among names that went up / down._

## Score calibration (long fwd)
- Spearman IC(total_score, fwd_3d) = **-0.1078**

| Quintile | Mean long fwd | Hit up>1.5% | n |
|---|---|---|---|
| 1 | 2.46% | 26.2% | 2360 |
| 2 | 1.93% | 19.8% | 2594 |
| 3 | -1.47% | 18.7% | 2978 |
| 4 | 2.62% | 29.4% | 1526 |
| 5 | -5.27% | 23.6% | 2262 |

## Top |IC| features

| Feature | IC | IC↑ | IC↓ | Mean fwd when + | Mean fwd when − | n+/n− |
|---|---|---|---|---|---|---|
| d_20-Day Simple Moving Average | -0.4013 | -0.1160 | -0.4207 | -2.48% | 2.30% | 6820/4764 |
| d_Beta | +0.3835 | +0.0112 | +0.4278 | 0.94% | 3.34% | 1744/2700 |
| Performance (Month) | +0.3739 | +0.0399 | +0.4545 | -0.01% | -0.18% | 5846/5703 |
| d_Performance (Quarter) | +0.3637 | +0.2335 | +0.2981 | 3.72% | -1.99% | 3916/7240 |
| d_200-Day Simple Moving Average | -0.3388 | -0.0833 | -0.3359 | -2.22% | 2.03% | 7015/4516 |
| d_Performance (YTD) | -0.3374 | -0.1014 | -0.2954 | -2.57% | 0.33% | 6839/4446 |
| d_50-Day Simple Moving Average | -0.3329 | -0.0640 | -0.3616 | -2.06% | 2.20% | 7381/4181 |
| true_ret | -0.3305 | -0.1097 | -0.3255 | -2.90% | 2.13% | 6737/4361 |
| upside_pct_lvl | -0.3303 | +0.2234 | -0.3132 | -0.13% | -1.61% | 4302/326 |
| d_Relative Strength Index (14) | -0.3275 | -0.0004 | -0.1471 | -2.54% | 0.69% | 6859/4446 |
| d_Price | -0.3265 | -0.0914 | -0.2187 | -2.90% | 2.13% | 6737/4361 |
| Relative Strength Index (14) | +0.2285 | -0.1757 | +0.3649 | -0.11% | n/a | 11639/0 |
| d_Forward P/E | -0.1922 | +0.0082 | -0.2116 | -1.01% | 1.23% | 1481/1453 |
| d_Market Cap | -0.1909 | -0.0317 | -0.0742 | -0.60% | 3.68% | 3202/2501 |
| d_Performance (Month) | -0.1908 | -0.0096 | -0.2085 | -0.81% | 1.35% | 7588/3835 |
| Institutional Transactions | -0.1313 | -0.0151 | -0.1104 | -1.31% | 9.51% | 3231/1813 |
| Short Float | -0.0652 | +0.3581 | -0.2544 | 2.60% | n/a | 5650/0 |
| Performance (Week) | +0.0646 | +0.0309 | +0.0295 | -1.53% | 0.82% | 6404/5105 |
| Relative Volume | +0.0585 | +0.1917 | -0.1010 | -0.51% | n/a | 11448/0 |
| d_Short Float | +0.0451 | +0.0129 | +0.0193 | 1.06% | -3.25% | 29/21 |
| d_Volatility (Month) | -0.0442 | +0.0647 | -0.0650 | 1.45% | -1.94% | 4380/5067 |
| d_Target Price | -0.0237 | -0.0638 | -0.0058 | -0.11% | 0.70% | 231/246 |
| d_Short Ratio | -0.0214 | -0.0453 | +0.0111 | -2.01% | 1.34% | 3251/3489 |
| d_Insider Transactions | -0.0213 | +0.0050 | +0.0114 | -3.36% | -1.43% | 53/67 |
| d_Average Volume | +0.0162 | +0.0154 | -0.0171 | 1.05% | -2.02% | 5630/5345 |

## Combinations

| Pattern | n | Mean long fwd | Hit up |
|---|---|---|---|
| true_ret>3% & DOWNTREND | 832 | -4.87% | 14.5% |
| true_ret>3% & UPTREND | 240 | -5.57% | 25.8% |
| true_ret>3% & MIXED | 217 | -6.60% | 20.3% |

## Risk dominance probes

| State | n | Mean long fwd | Mean fwd if score top quintile |
|---|---|---|---|
| EXTENDED | 176 | -2.62% | -7.05% |
| WASHED | 1154 | 10.81% | -14.31% |

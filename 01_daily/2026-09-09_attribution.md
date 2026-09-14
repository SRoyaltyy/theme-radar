# Factor attribution — signal 2026-09-09 → prediction day 2026-09-14

## Trade window (read this first)

| Role | Date | Meaning |
|------|------|---------|
| **Signal as-of** | **2026-09-09** | Features/scores formed from this snapshot (and deltas vs **2026-09-08**). Only data on/before this date. |
| **Prediction day** | **2026-09-14** | The trading day the forward return is for (exit snapshot). |
| **Entry price** | Price @ 2026-09-09 | Long: buy here; short: sell here. |
| **Exit price** | Price @ 2026-09-14 | Close proxy on prediction day. |
| **Return column** | `fwd_3d` | Long: exit/entry − 1; short = opposite. |

Graded **n=11576** names with valid entry and exit prices.

Provisional until multiple signal dates agree.

_Column guide: **IC** = Spearman(feature, long forward return); **IC↑** / **IC↓** = IC among names that went up / down._

## Score calibration (long fwd)
- Spearman IC(total_score, fwd_3d) = **-0.0591**

| Quintile | Mean long fwd | Hit up>1.5% | n |
|---|---|---|---|
| 1 | 0.72% | 22.1% | 2767 |
| 2 | 0.16% | 11.2% | 2118 |
| 3 | 3.34% | 11.7% | 2191 |
| 4 | -1.20% | 10.4% | 2315 |
| 5 | 3.85% | 23.2% | 2185 |

## Top |IC| features

| Feature | IC | IC↑ | IC↓ | Mean fwd when + | Mean fwd when − | n+/n− |
|---|---|---|---|---|---|---|
| Performance (Week) | -0.2108 | -0.1778 | -0.1884 | -0.98% | 3.80% | 5829/5543 |
| upside_pct_lvl | -0.2042 | +0.2032 | -0.3326 | 3.84% | -0.54% | 4366/278 |
| d_Beta | +0.1241 | +0.0366 | +0.1149 | 7.87% | -1.93% | 1280/1454 |
| d_Performance (Week) | -0.1048 | -0.0224 | -0.1139 | 1.02% | 1.80% | 6560/4835 |
| d_Performance (Quarter) | -0.0995 | -0.0843 | -0.0510 | 2.30% | 1.26% | 3409/7468 |
| d_Market Cap | -0.0724 | -0.0069 | -0.0734 | 5.29% | 2.63% | 1500/4218 |
| d_Relative Strength Index (14) | -0.0639 | +0.1270 | -0.2336 | 2.91% | 1.01% | 2299/8920 |
| Institutional Transactions | -0.0637 | +0.0288 | -0.0839 | 4.26% | 2.35% | 3198/1831 |
| d_EPS Surprise | +0.0592 | +0.0473 | +0.0467 | 1.97% | -4.88% | 27/19 |
| d_Volatility (Month) | +0.0583 | -0.0013 | +0.1163 | 3.44% | 0.46% | 4303/4862 |
| d_Performance (Month) | -0.0565 | -0.1256 | +0.0234 | 2.09% | 1.02% | 3958/7310 |
| d_Price | -0.0518 | -0.0378 | -0.0534 | 2.96% | 0.73% | 2251/8888 |
| d_50-Day Simple Moving Average | -0.0497 | -0.2228 | +0.0977 | 2.75% | 0.95% | 2483/8996 |
| d_Short Ratio | -0.0461 | -0.0006 | -0.0656 | 1.33% | 1.26% | 3813/4190 |
| d_Institutional Ownership | -0.0441 | -0.0311 | -0.0258 | -0.66% | 0.05% | 473/710 |
| d_Forward P/E | -0.0373 | -0.1301 | -0.0221 | -0.88% | 0.15% | 689/2266 |
| d_Sales Year Over Year TTM | -0.0356 | -0.0264 | -0.0434 | -1.38% | 3.90% | 17/17 |
| d_Relative Volume | +0.0307 | -0.0417 | +0.0799 | 2.81% | 0.25% | 4995/6195 |
| Relative Volume | +0.0272 | +0.1010 | -0.0259 | 1.36% | n/a | 11330/0 |
| d_Short Float | +0.0270 | +0.0109 | +0.0370 | -0.98% | -1.82% | 64/153 |
| d_Profit Margin | +0.0247 | +0.0078 | +0.0221 | 0.92% | -1.05% | 28/10 |
| d_Sales Growth Quarter Over Quarter | -0.0214 | -0.0432 | -0.0131 | 0.07% | 2.27% | 17/19 |
| d_Total Debt/Equity | -0.0208 | -0.0294 | -0.0124 | -0.63% | 2.59% | 15/16 |
| Performance (Month) | +0.0207 | -0.0996 | +0.0594 | -0.83% | 2.58% | 4006/7361 |
| d_200-Day Simple Moving Average | -0.0205 | -0.1782 | +0.1067 | 2.71% | 0.85% | 2393/9075 |

## Combinations

| Pattern | n | Mean long fwd | Hit up |
|---|---|---|---|
| true_ret>3% & DOWNTREND | 149 | 56.27% | 28.2% |
| true_ret>3% & UPTREND | 154 | -5.82% | 22.1% |
| true_ret>3% & MIXED | 83 | -1.71% | 31.3% |

## Risk dominance probes

| State | n | Mean long fwd | Mean fwd if score top quintile |
|---|---|---|---|
| EXTENDED | 220 | -3.55% | -7.68% |
| WASHED | 952 | 6.56% | 20.25% |

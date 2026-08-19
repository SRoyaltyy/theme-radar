# Factor attribution — signal 2026-08-14 → prediction day 2026-08-19

## Trade window (read this first)

| Role | Date | Meaning |
|------|------|---------|
| **Signal as-of** | **2026-08-14** | Features/scores formed from this snapshot (and deltas vs **2026-08-13**). Only data on/before this date. |
| **Prediction day** | **2026-08-19** | The trading day the forward return is for (exit snapshot). |
| **Entry price** | Price @ 2026-08-14 | Long: buy here; short: sell here. |
| **Exit price** | Price @ 2026-08-19 | Close proxy on prediction day. |
| **Return column** | `fwd_3d` | Long: exit/entry − 1; short = opposite. |

Graded **n=11549** names with valid entry and exit prices.

Provisional until multiple signal dates agree.

_Column guide: **IC** = Spearman(feature, long forward return); **IC↑** / **IC↓** = IC among names that went up / down._

## Score calibration (long fwd)
- Spearman IC(total_score, fwd_3d) = **-0.1404**

| Quintile | Mean long fwd | Hit up>1.5% | n |
|---|---|---|---|
| 1 | 4.85% | 27.8% | 2326 |
| 2 | 0.49% | 13.5% | 2553 |
| 3 | 4.48% | 8.9% | 2399 |
| 4 | -0.72% | 18.7% | 1996 |
| 5 | -1.70% | 28.9% | 2275 |

## Top |IC| features

| Feature | IC | IC↑ | IC↓ | Mean fwd when + | Mean fwd when − | n+/n− |
|---|---|---|---|---|---|---|
| d_Forward P/E | -0.1628 | -0.0121 | -0.1818 | -1.71% | -0.57% | 1582/1351 |
| d_Performance (Month) | -0.1490 | +0.1673 | -0.2811 | -0.88% | 4.82% | 6304/4932 |
| Performance (Week) | -0.1396 | -0.0256 | -0.1873 | -1.01% | 6.07% | 7149/4183 |
| d_Volatility (Month) | +0.1357 | -0.0437 | +0.1926 | 5.77% | -0.18% | 3383/6024 |
| d_Relative Strength Index (14) | -0.1097 | +0.0853 | -0.1590 | -1.22% | 4.31% | 5300/5731 |
| d_50-Day Simple Moving Average | -0.0997 | -0.0119 | -0.1508 | -1.30% | 3.34% | 5102/6272 |
| true_ret | -0.0975 | -0.0322 | -0.1215 | -1.28% | 1.24% | 5168/5660 |
| d_Price | -0.0957 | +0.0045 | -0.1226 | -1.28% | 1.24% | 5168/5660 |
| d_Performance (YTD) | -0.0935 | -0.0208 | -0.1225 | -1.26% | 3.63% | 5289/5751 |
| d_Market Cap | -0.0871 | +0.0143 | -0.1036 | -0.94% | 9.05% | 2949/2725 |
| Performance (Month) | -0.0809 | +0.0658 | -0.1340 | -0.98% | 6.17% | 7233/4097 |
| d_200-Day Simple Moving Average | -0.0723 | +0.0221 | -0.1301 | -1.13% | 3.26% | 5176/6185 |
| d_Performance (Quarter) | +0.0702 | +0.0232 | +0.0401 | 3.00% | 1.13% | 4236/6510 |
| d_20-Day Simple Moving Average | -0.0637 | -0.0543 | -0.0830 | -0.06% | 2.70% | 4641/6766 |
| d_Performance (Week) | -0.0425 | -0.1973 | +0.0477 | 3.82% | 0.70% | 3303/8002 |
| d_Profit Margin | +0.0326 | +0.0020 | +0.0125 | -0.14% | -1.21% | 126/116 |
| d_Analyst Recom | +0.0318 | -0.0256 | +0.0247 | 0.09% | -1.08% | 132/89 |
| Relative Strength Index (14) | -0.0294 | -0.0848 | +0.2875 | 1.59% | n/a | 11425/0 |
| d_Total Debt/Equity | -0.0292 | -0.0200 | -0.0366 | -0.90% | 0.34% | 119/113 |
| upside_pct_lvl | +0.0217 | +0.3567 | -0.2611 | 3.66% | -0.47% | 4275/367 |
| d_Target Price | -0.0191 | -0.0296 | +0.0255 | -0.50% | -0.10% | 292/209 |
| d_Relative Volume | -0.0175 | -0.0429 | +0.0032 | 0.34% | 2.38% | 4320/6750 |
| Relative Volume | -0.0160 | +0.0819 | -0.1083 | 1.60% | n/a | 11264/0 |
| d_Institutional Ownership | -0.0150 | +0.0294 | -0.0316 | -0.15% | 4.60% | 2863/2118 |
| d_Insider Transactions | -0.0121 | -0.0627 | -0.0009 | -0.55% | 7.21% | 248/261 |

## Combinations

| Pattern | n | Mean long fwd | Hit up |
|---|---|---|---|
| true_ret>3% & DOWNTREND | 333 | -3.44% | 23.4% |
| true_ret>3% & UPTREND | 317 | -4.35% | 27.8% |
| true_ret>3% & MIXED | 249 | -3.25% | 26.9% |

## Risk dominance probes

| State | n | Mean long fwd | Mean fwd if score top quintile |
|---|---|---|---|
| EXTENDED | 378 | -2.69% | -6.39% |
| WASHED | 447 | 45.12% | -2.91% |

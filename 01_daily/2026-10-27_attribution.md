# Factor attribution — signal 2026-10-27 → prediction day 2026-10-29

## Trade window (read this first)

| Role | Date | Meaning |
|------|------|---------|
| **Signal as-of** | **2026-10-27** | Features/scores formed from this snapshot (and deltas vs **2026-10-26**). Only data on/before this date. |
| **Prediction day** | **2026-10-29** | The trading day the forward return is for (exit snapshot). |
| **Entry price** | Price @ 2026-10-27 | Long: buy here; short: sell here. |
| **Exit price** | Price @ 2026-10-29 | Close proxy on prediction day. |
| **Return column** | `fwd_2d` | Long: exit/entry − 1; short = opposite. |

Graded **n=11760** names with valid entry and exit prices.

Provisional until multiple signal dates agree.

_Column guide: **IC** = Spearman(feature, long forward return); **IC↑** / **IC↓** = IC among names that went up / down._

## Score calibration (long fwd)
- Spearman IC(total_score, fwd_2d) = **0.0826**

| Quintile | Mean long fwd | Hit up>1.5% | n |
|---|---|---|---|
| 1 | 6.34% | 25.0% | 2353 |
| 2 | 0.35% | 14.0% | 2371 |
| 3 | 0.52% | 19.0% | 2858 |
| 4 | 0.90% | 32.3% | 2254 |
| 5 | 2.62% | 44.4% | 1924 |

## Top |IC| features

| Feature | IC | IC↑ | IC↓ | Mean fwd when + | Mean fwd when − | n+/n− |
|---|---|---|---|---|---|---|
| Short Float | +0.1273 | +0.2959 | -0.0318 | 4.08% | n/a | 5658/0 |
| d_Performance (Week) | -0.0964 | -0.0176 | -0.0973 | 1.17% | 3.06% | 5774/5709 |
| d_Market Cap | +0.0917 | +0.1452 | -0.0002 | 2.29% | 6.72% | 3601/2191 |
| Performance (Week) | +0.0891 | +0.0262 | +0.1592 | 0.82% | 3.91% | 6746/4778 |
| Relative Volume | +0.0815 | +0.1231 | -0.0739 | 2.12% | n/a | 11406/0 |
| d_Forward P/E | +0.0813 | +0.1815 | -0.0791 | 1.59% | 0.96% | 1647/1295 |
| Performance (Month) | +0.0570 | -0.1850 | +0.3237 | 0.63% | 3.45% | 5564/6008 |
| d_Beta | +0.0531 | -0.1232 | +0.1965 | 4.90% | 2.75% | 2232/2525 |
| d_Relative Volume | +0.0505 | +0.0694 | -0.0077 | 3.24% | 1.08% | 5509/5733 |
| Relative Strength Index (14) | +0.0505 | -0.2641 | +0.3439 | 2.08% | n/a | 11673/0 |
| d_Performance (Quarter) | +0.0483 | +0.2500 | -0.1122 | 1.19% | 5.20% | 8414/2724 |
| d_Target Price | -0.0436 | -0.0636 | +0.0473 | 0.38% | 1.66% | 250/199 |
| d_50-Day Simple Moving Average | +0.0372 | +0.2469 | -0.1600 | 1.04% | 4.70% | 8252/3332 |
| d_Relative Strength Index (14) | -0.0258 | +0.0314 | +0.1048 | 1.03% | 4.63% | 7853/3464 |
| d_Short Float | +0.0250 | +0.0289 | +0.0213 | 5.45% | 2.93% | 2782/2708 |
| d_Profit Margin | +0.0241 | n/a | -0.0200 | n/a | -1.91% | 0/4 |
| true_ret | +0.0237 | +0.2055 | -0.1367 | 1.04% | 4.75% | 7810/3370 |
| d_Short Ratio | +0.0235 | +0.0418 | -0.0237 | 1.22% | 3.09% | 5492/5638 |
| d_Volatility (Month) | -0.0193 | -0.0323 | -0.0133 | -0.67% | 0.93% | 34/12 |
| d_Average Volume | +0.0191 | +0.0365 | -0.0546 | 2.02% | 2.38% | 6041/4952 |
| d_Total Debt/Equity | -0.0175 | n/a | -0.0362 | -3.51% | -0.87% | 3/1 |
| d_200-Day Simple Moving Average | +0.0171 | +0.2069 | -0.1281 | 1.02% | 4.53% | 8031/3527 |
| d_EPS Surprise | -0.0155 | +0.0052 | +0.0174 | 1.63% | 2.35% | 38/48 |
| d_Gross Margin | -0.0139 | n/a | -0.0076 | -3.37% | -0.92% | 3/2 |
| d_Performance (YTD) | +0.0124 | +0.1733 | -0.0851 | 1.03% | 4.68% | 7874/3429 |

## Combinations

| Pattern | n | Mean long fwd | Hit up |
|---|---|---|---|
| true_ret>3% & DOWNTREND | 1308 | 3.17% | 43.8% |
| true_ret>3% & UPTREND | 242 | 2.26% | 54.5% |
| true_ret>3% & MIXED | 287 | 1.00% | 40.4% |

## Risk dominance probes

| State | n | Mean long fwd | Mean fwd if score top quintile |
|---|---|---|---|
| EXTENDED | 157 | 0.88% | 1.48% |
| WASHED | 1294 | 12.10% | 1.59% |

# Factor attribution — signal 2026-09-24 → prediction day 2026-09-29

## Trade window (read this first)

| Role | Date | Meaning |
|------|------|---------|
| **Signal as-of** | **2026-09-24** | Features/scores formed from this snapshot (and deltas vs **2026-09-23**). Only data on/before this date. |
| **Prediction day** | **2026-09-29** | The trading day the forward return is for (exit snapshot). |
| **Entry price** | Price @ 2026-09-24 | Long: buy here; short: sell here. |
| **Exit price** | Price @ 2026-09-29 | Close proxy on prediction day. |
| **Return column** | `fwd_3d` | Long: exit/entry − 1; short = opposite. |

Graded **n=11657** names with valid entry and exit prices.

Provisional until multiple signal dates agree.

_Column guide: **IC** = Spearman(feature, long forward return); **IC↑** / **IC↓** = IC among names that went up / down._

## Score calibration (long fwd)
- Spearman IC(total_score, fwd_3d) = **0.0182**

| Quintile | Mean long fwd | Hit up>1.5% | n |
|---|---|---|---|
| 1 | 6.46% | 12.8% | 2787 |
| 2 | -0.74% | 7.3% | 2585 |
| 3 | -0.16% | 8.5% | 2396 |
| 4 | -0.19% | 9.2% | 1874 |
| 5 | -0.81% | 18.1% | 2015 |

## Top |IC| features

| Feature | IC | IC↑ | IC↓ | Mean fwd when + | Mean fwd when − | n+/n− |
|---|---|---|---|---|---|---|
| upside_pct_lvl | -0.1931 | +0.2832 | -0.3808 | 1.73% | -0.61% | 4381/256 |
| Performance (Month) | +0.1245 | -0.1326 | +0.2236 | -0.53% | 1.95% | 3436/8024 |
| Short Float | -0.0795 | +0.2119 | -0.1558 | 3.13% | n/a | 5690/0 |
| Relative Strength Index (14) | +0.0768 | -0.0686 | -0.0267 | 1.19% | n/a | 11561/0 |
| Performance (Week) | +0.0751 | -0.0225 | +0.1092 | -0.31% | 2.16% | 4471/7018 |
| d_Performance (Quarter) | -0.0714 | +0.0182 | -0.0832 | 0.96% | 1.53% | 4108/6882 |
| d_Performance (Week) | +0.0625 | -0.1401 | +0.1450 | 0.61% | 1.38% | 2644/8842 |
| Institutional Transactions | -0.0586 | +0.0709 | -0.0883 | 5.01% | 2.17% | 3221/1809 |
| d_Market Cap | -0.0538 | +0.0526 | -0.0126 | -0.05% | 5.65% | 2283/3404 |
| d_Beta | -0.0500 | +0.0618 | -0.0624 | 5.58% | -0.78% | 3104/1228 |
| d_Forward P/E | -0.0471 | -0.0443 | +0.0428 | -1.01% | -0.88% | 1238/1690 |
| d_Institutional Ownership | -0.0358 | +0.0477 | -0.1064 | -1.36% | -0.55% | 434/1538 |
| d_Performance (Month) | +0.0341 | -0.0865 | +0.1052 | 0.04% | 1.70% | 3256/8120 |
| d_Price | -0.0318 | -0.0049 | -0.0516 | -0.46% | 2.30% | 3916/7065 |
| d_Relative Strength Index (14) | -0.0225 | +0.0265 | -0.0665 | -0.45% | 2.25% | 4046/7147 |
| d_20-Day Simple Moving Average | -0.0179 | -0.0486 | +0.0147 | -0.16% | 2.16% | 4741/6738 |
| d_Average Volume | -0.0179 | +0.0063 | -0.0116 | 3.65% | -0.90% | 5320/5762 |
| d_Sales Year Over Year TTM | -0.0174 | +0.0051 | -0.0190 | -5.34% | -0.02% | 6/3 |
| d_EPS Surprise | +0.0173 | -0.0037 | +0.0333 | 0.84% | -2.60% | 3/6 |
| d_Gross Margin | -0.0157 | +0.0238 | -0.0145 | -5.08% | -1.95% | 7/7 |
| Relative Volume | -0.0153 | +0.0728 | -0.0394 | 1.20% | n/a | 11439/0 |
| d_Short Float | -0.0146 | -0.0032 | -0.0009 | 5.84% | -0.38% | 3229/2281 |
| true_ret | +0.0142 | -0.0931 | +0.0774 | -0.46% | 2.30% | 3916/7065 |
| d_Total Debt/Equity | +0.0123 | -0.0045 | +0.0251 | -1.35% | -6.58% | 6/5 |
| d_200-Day Simple Moving Average | -0.0121 | -0.0536 | +0.0216 | -0.62% | 0.92% | 3975/7529 |

## Combinations

| Pattern | n | Mean long fwd | Hit up |
|---|---|---|---|
| true_ret>3% & DOWNTREND | 199 | 4.62% | 17.6% |
| true_ret>3% & UPTREND | 264 | -0.83% | 30.7% |
| true_ret>3% & MIXED | 145 | 2.25% | 22.8% |

## Risk dominance probes

| State | n | Mean long fwd | Mean fwd if score top quintile |
|---|---|---|---|
| EXTENDED | 203 | 1.04% | 18.84% |
| WASHED | 2262 | 7.94% | 1.45% |

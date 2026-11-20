# Factor attribution — signal 2026-11-18 → prediction day 2026-11-19

## Trade window (read this first)

| Role | Date | Meaning |
|------|------|---------|
| **Signal as-of** | **2026-11-18** | Features/scores formed from this snapshot (and deltas vs **2026-11-17**). Only data on/before this date. |
| **Prediction day** | **2026-11-19** | The trading day the forward return is for (exit snapshot). |
| **Entry price** | Price @ 2026-11-18 | Long: buy here; short: sell here. |
| **Exit price** | Price @ 2026-11-19 | Close proxy on prediction day. |
| **Return column** | `fwd_1d` | Long: exit/entry − 1; short = opposite. |

Graded **n=11740** names with valid entry and exit prices.

Provisional until multiple signal dates agree.

_Column guide: **IC** = Spearman(feature, long forward return); **IC↑** / **IC↓** = IC among names that went up / down._

## Score calibration (long fwd)
- Spearman IC(total_score, fwd_1d) = **0.0285**

| Quintile | Mean long fwd | Hit up>1.5% | n |
|---|---|---|---|
| 1 | 1.14% | 8.0% | 2487 |
| 2 | -1.43% | 3.8% | 2221 |
| 3 | -1.71% | 1.9% | 2337 |
| 4 | -1.17% | 6.4% | 2644 |
| 5 | -2.01% | 9.0% | 2051 |

## Top |IC| features

| Feature | IC | IC↑ | IC↓ | Mean fwd when + | Mean fwd when − | n+/n− |
|---|---|---|---|---|---|---|
| Performance (Week) | +0.3764 | -0.2118 | +0.4280 | -0.01% | -1.14% | 1498/10117 |
| Performance (Month) | +0.2418 | -0.2463 | +0.3211 | -0.91% | -1.02% | 3447/8136 |
| Short Float | -0.2283 | +0.2403 | -0.2198 | -0.71% | n/a | 5613/0 |
| d_Performance (Week) | +0.1872 | -0.0600 | +0.1720 | -1.15% | -0.94% | 3561/7993 |
| Relative Strength Index (14) | +0.1640 | -0.1599 | +0.1212 | -0.99% | n/a | 11680/0 |
| upside_pct_lvl | -0.1434 | +0.4787 | -0.3941 | -1.63% | -1.94% | 4388/240 |
| d_Performance (Quarter) | -0.0945 | -0.0451 | -0.0976 | -1.80% | 0.20% | 6643/4616 |
| d_20-Day Simple Moving Average | -0.0889 | -0.0306 | -0.1238 | -1.82% | -0.06% | 6171/5423 |
| Relative Volume | -0.0780 | +0.1272 | -0.0610 | -1.00% | n/a | 11496/0 |
| d_Performance (Month) | +0.0668 | -0.1093 | +0.0347 | -1.73% | -1.37% | 3698/7762 |
| d_Volatility (Month) | -0.0609 | +0.1822 | -0.1150 | -1.37% | -0.48% | 5193/4311 |
| d_50-Day Simple Moving Average | -0.0473 | -0.0475 | -0.0811 | -1.76% | -0.22% | 5800/5781 |
| d_Insider Transactions | +0.0460 | +0.0427 | +0.0126 | -1.50% | 20.27% | 152/238 |
| d_Short Float | +0.0445 | -0.0453 | +0.0813 | -2.12% | -3.37% | 17/94 |
| d_Profit Margin | +0.0367 | +0.0177 | +0.0183 | 52.33% | -4.40% | 53/49 |
| d_Total Debt/Equity | -0.0365 | -0.0998 | -0.0423 | -5.81% | -2.48% | 53/38 |
| d_Institutional Ownership | +0.0345 | -0.0855 | -0.0107 | -0.27% | -2.15% | 1484/2088 |
| d_Market Cap | -0.0314 | +0.0703 | -0.0484 | -1.16% | -0.49% | 2565/3133 |
| Institutional Transactions | -0.0247 | +0.0386 | -0.0820 | 0.48% | -2.36% | 2992/2019 |
| d_EPS Surprise | +0.0231 | +0.0376 | +0.0120 | -1.48% | -4.46% | 15/23 |
| d_Gross Margin | +0.0228 | -0.0205 | +0.0070 | 56.06% | -3.96% | 49/62 |
| d_Sales Year Over Year TTM | +0.0224 | +0.0560 | +0.0149 | -2.68% | -5.27% | 45/40 |
| d_Forward P/E | -0.0223 | +0.1513 | -0.0218 | -2.28% | -2.17% | 1390/1506 |
| d_Analyst Recom | +0.0185 | -0.0670 | +0.0138 | -2.14% | -2.39% | 167/148 |
| d_Target Price | +0.0159 | -0.0201 | +0.0386 | -1.84% | -2.19% | 160/224 |

## Combinations

| Pattern | n | Mean long fwd | Hit up |
|---|---|---|---|
| true_ret>3% & DOWNTREND | 463 | -3.76% | 14.3% |
| true_ret>3% & UPTREND | 224 | -2.06% | 19.6% |
| true_ret>3% & MIXED | 207 | -1.73% | 19.3% |

## Risk dominance probes

| State | n | Mean long fwd | Mean fwd if score top quintile |
|---|---|---|---|
| EXTENDED | 173 | 0.39% | -1.11% |
| WASHED | 2065 | 1.42% | -2.89% |

# Factor attribution — signal 2026-10-07 → prediction day 2026-10-08

## Trade window (read this first)

| Role | Date | Meaning |
|------|------|---------|
| **Signal as-of** | **2026-10-07** | Features/scores formed from this snapshot (and deltas vs **2026-10-06**). Only data on/before this date. |
| **Prediction day** | **2026-10-08** | The trading day the forward return is for (exit snapshot). |
| **Entry price** | Price @ 2026-10-07 | Long: buy here; short: sell here. |
| **Exit price** | Price @ 2026-10-08 | Close proxy on prediction day. |
| **Return column** | `fwd_1d` | Long: exit/entry − 1; short = opposite. |

Graded **n=11704** names with valid entry and exit prices.

Provisional until multiple signal dates agree.

_Column guide: **IC** = Spearman(feature, long forward return); **IC↑** / **IC↓** = IC among names that went up / down._

## Score calibration (long fwd)
- Spearman IC(total_score, fwd_1d) = **0.0543**

| Quintile | Mean long fwd | Hit up>1.5% | n |
|---|---|---|---|
| 1 | -0.79% | 14.5% | 2627 |
| 2 | -0.30% | 7.6% | 2330 |
| 3 | -0.09% | 11.0% | 2536 |
| 4 | -0.41% | 10.0% | 1880 |
| 5 | -0.10% | 26.2% | 2331 |

## Top |IC| features

| Feature | IC | IC↑ | IC↓ | Mean fwd when + | Mean fwd when − | n+/n− |
|---|---|---|---|---|---|---|
| upside_pct_lvl | -0.2689 | +0.1750 | -0.4064 | -0.32% | -0.01% | 4384/252 |
| Relative Strength Index (14) | -0.2312 | +0.1232 | +0.1003 | -0.34% | n/a | 11613/0 |
| d_Performance (Month) | +0.2294 | +0.0997 | +0.3054 | 0.30% | -0.85% | 5092/6319 |
| d_Performance (Quarter) | +0.2190 | -0.0282 | +0.3327 | -0.02% | -0.38% | 2271/8850 |
| d_Forward P/E | +0.2063 | +0.1384 | +0.1728 | 0.68% | 0.23% | 785/2160 |
| d_20-Day Simple Moving Average | +0.1972 | -0.0185 | +0.3032 | 0.05% | -0.50% | 3267/8336 |
| d_50-Day Simple Moving Average | +0.1867 | -0.0585 | +0.3160 | 0.01% | -0.46% | 2943/8656 |
| d_Performance (Week) | +0.1649 | +0.0098 | +0.2531 | -0.17% | -0.51% | 4020/7444 |
| true_ret | +0.1551 | -0.0733 | +0.3211 | -0.12% | -0.45% | 2496/8610 |
| Performance (Month) | -0.1521 | -0.2765 | +0.0853 | -1.09% | -0.01% | 3495/8025 |
| d_200-Day Simple Moving Average | +0.1491 | -0.0496 | +0.2704 | -0.01% | -0.44% | 2749/8801 |
| d_Performance (YTD) | +0.1373 | -0.0446 | +0.2617 | -0.11% | -0.46% | 2583/8707 |
| d_Relative Strength Index (14) | +0.1116 | +0.1234 | +0.0279 | -0.14% | -0.47% | 2615/8683 |
| Institutional Transactions | -0.0999 | -0.0061 | -0.1375 | -0.22% | -0.08% | 3243/1803 |
| d_Price | +0.0881 | +0.0270 | +0.1207 | -0.12% | -0.45% | 2496/8610 |
| d_Target Price | -0.0815 | +0.0194 | -0.0533 | -0.13% | 0.50% | 198/379 |
| d_Beta | +0.0676 | -0.0316 | +0.1233 | -0.51% | -0.75% | 985/1606 |
| Relative Volume | +0.0666 | -0.0188 | -0.0368 | -0.35% | n/a | 11434/0 |
| d_Relative Volume | +0.0535 | +0.0225 | +0.0416 | -0.31% | -0.37% | 5583/5639 |
| d_Institutional Ownership | +0.0400 | +0.0348 | +0.0051 | 0.38% | -0.06% | 517/499 |
| Short Float | +0.0347 | +0.1845 | -0.1774 | -0.02% | n/a | 5692/0 |
| d_Insider Transactions | -0.0270 | -0.0247 | -0.0083 | -1.05% | -0.77% | 126/166 |
| d_Analyst Recom | -0.0176 | -0.0503 | +0.0185 | -0.73% | -0.07% | 69/62 |
| d_Volatility (Month) | -0.0163 | +0.0366 | -0.0468 | -0.19% | -0.68% | 5305/3946 |
| d_Market Cap | -0.0155 | +0.0978 | -0.0454 | -0.26% | -0.01% | 1666/4058 |

## Combinations

| Pattern | n | Mean long fwd | Hit up |
|---|---|---|---|
| true_ret>3% & DOWNTREND | 223 | -0.87% | 37.2% |
| true_ret>3% & UPTREND | 110 | -2.54% | 16.4% |
| true_ret>3% & MIXED | 88 | -0.69% | 29.5% |

## Risk dominance probes

| State | n | Mean long fwd | Mean fwd if score top quintile |
|---|---|---|---|
| EXTENDED | 182 | -3.00% | -3.15% |
| WASHED | 1836 | -0.27% | -0.87% |

# Factor attribution — signal 2026-11-05 → prediction day 2026-11-09

## Trade window (read this first)

| Role | Date | Meaning |
|------|------|---------|
| **Signal as-of** | **2026-11-05** | Features/scores formed from this snapshot (and deltas vs **2026-11-04**). Only data on/before this date. |
| **Prediction day** | **2026-11-09** | The trading day the forward return is for (exit snapshot). |
| **Entry price** | Price @ 2026-11-05 | Long: buy here; short: sell here. |
| **Exit price** | Price @ 2026-11-09 | Close proxy on prediction day. |
| **Return column** | `fwd_2d` | Long: exit/entry − 1; short = opposite. |

Graded **n=11723** names with valid entry and exit prices.

Provisional until multiple signal dates agree.

_Column guide: **IC** = Spearman(feature, long forward return); **IC↑** / **IC↓** = IC among names that went up / down._

## Score calibration (long fwd)
- Spearman IC(total_score, fwd_2d) = **-0.3612**

| Quintile | Mean long fwd | Hit up>1.5% | n |
|---|---|---|---|
| 1 | 7.16% | 82.6% | 2357 |
| 2 | 13.70% | 66.3% | 2338 |
| 3 | 6.16% | 57.2% | 2512 |
| 4 | 1.67% | 31.2% | 2248 |
| 5 | 1.22% | 28.1% | 2268 |

## Top |IC| features

| Feature | IC | IC↑ | IC↓ | Mean fwd when + | Mean fwd when − | n+/n− |
|---|---|---|---|---|---|---|
| true_ret | -0.5071 | -0.6585 | +0.2307 | 0.28% | 7.33% | 1870/9575 |
| d_50-Day Simple Moving Average | -0.4859 | -0.6061 | +0.1955 | 0.49% | 7.29% | 2049/9592 |
| d_20-Day Simple Moving Average | -0.4817 | -0.6113 | +0.2027 | 0.85% | 7.12% | 1901/9730 |
| d_Performance (YTD) | -0.4811 | -0.5232 | +0.1645 | 0.36% | 7.10% | 1888/9594 |
| d_200-Day Simple Moving Average | -0.4797 | -0.5612 | +0.1758 | 0.33% | 7.07% | 1977/9645 |
| d_Performance (Quarter) | -0.4608 | -0.5859 | +0.1799 | 0.92% | 7.06% | 1610/9597 |
| Performance (Week) | -0.4305 | -0.5596 | +0.1106 | 0.88% | 8.49% | 3639/7960 |
| d_Performance (Week) | -0.4219 | -0.5379 | +0.1418 | 1.49% | 7.05% | 1898/9637 |
| d_Performance (Month) | -0.4159 | -0.5156 | +0.1484 | 1.83% | 7.51% | 2773/8712 |
| Relative Strength Index (14) | -0.4086 | -0.4636 | +0.2619 | 6.06% | n/a | 11664/0 |
| Performance (Month) | -0.3958 | -0.5580 | +0.1680 | 1.00% | 9.48% | 4613/6947 |
| d_Price | -0.3900 | -0.3054 | +0.1095 | 0.28% | 7.33% | 1870/9575 |
| d_Forward P/E | -0.3294 | -0.3761 | +0.0985 | 1.34% | 3.35% | 477/2496 |
| upside_pct_lvl | +0.3073 | +0.5184 | -0.3305 | 6.84% | 0.83% | 4313/317 |
| d_Relative Strength Index (14) | -0.2658 | +0.0054 | +0.1577 | 0.32% | 7.32% | 1898/9570 |
| d_Market Cap | -0.1901 | -0.1166 | -0.0909 | 2.30% | 9.86% | 883/4923 |
| Short Float | +0.1743 | +0.3340 | -0.1690 | 7.27% | n/a | 5624/0 |
| Relative Volume | +0.1486 | +0.1795 | -0.0706 | 6.12% | n/a | 11572/0 |
| d_Volatility (Month) | +0.1254 | +0.3185 | -0.3048 | 6.12% | 9.21% | 7756/2267 |
| Institutional Transactions | +0.1177 | +0.1495 | -0.0571 | 10.75% | 6.64% | 3189/1829 |
| d_Relative Volume | +0.1063 | +0.1021 | -0.0654 | 5.66% | 6.95% | 7038/4393 |
| d_Beta | -0.0839 | -0.0185 | -0.1267 | 8.86% | 13.44% | 2528/1797 |
| d_Target Price | -0.0531 | -0.0615 | +0.0242 | 3.26% | 5.16% | 379/322 |
| d_Institutional Ownership | +0.0529 | +0.0898 | -0.0773 | 6.32% | 5.61% | 1776/1493 |
| d_Insider Transactions | +0.0408 | +0.0117 | +0.0239 | 5.25% | 2.31% | 197/204 |

## Combinations

| Pattern | n | Mean long fwd | Hit up |
|---|---|---|---|
| true_ret>3% & DOWNTREND | 136 | 4.35% | 42.6% |
| true_ret>3% & UPTREND | 150 | -1.40% | 36.0% |
| true_ret>3% & MIXED | 142 | -4.64% | 30.3% |

## Risk dominance probes

| State | n | Mean long fwd | Mean fwd if score top quintile |
|---|---|---|---|
| EXTENDED | 259 | -2.80% | -7.04% |
| WASHED | 2719 | 18.13% | 9.55% |

# Factor attribution — signal 2026-10-19 → prediction day 2026-10-22

## Trade window (read this first)

| Role | Date | Meaning |
|------|------|---------|
| **Signal as-of** | **2026-10-19** | Features/scores formed from this snapshot (and deltas vs **2026-10-16**). Only data on/before this date. |
| **Prediction day** | **2026-10-22** | The trading day the forward return is for (exit snapshot). |
| **Entry price** | Price @ 2026-10-19 | Long: buy here; short: sell here. |
| **Exit price** | Price @ 2026-10-22 | Close proxy on prediction day. |
| **Return column** | `fwd_3d` | Long: exit/entry − 1; short = opposite. |

Graded **n=11741** names with valid entry and exit prices.

Provisional until multiple signal dates agree.

_Column guide: **IC** = Spearman(feature, long forward return); **IC↑** / **IC↓** = IC among names that went up / down._

## Score calibration (long fwd)
- Spearman IC(total_score, fwd_3d) = **0.0943**

| Quintile | Mean long fwd | Hit up>1.5% | n |
|---|---|---|---|
| 1 | 0.94% | 25.6% | 2687 |
| 2 | 1.65% | 22.1% | 2181 |
| 3 | 0.22% | 28.2% | 2309 |
| 4 | 0.52% | 30.7% | 2374 |
| 5 | 0.67% | 47.6% | 2190 |

## Top |IC| features

| Feature | IC | IC↑ | IC↓ | Mean fwd when + | Mean fwd when − | n+/n− |
|---|---|---|---|---|---|---|
| Performance (Week) | +0.3450 | -0.0134 | +0.4980 | 1.74% | 0.33% | 3875/7700 |
| d_Performance (Week) | -0.2817 | -0.0890 | -0.3079 | 0.29% | 1.39% | 5978/5535 |
| d_Relative Strength Index (14) | -0.2662 | +0.0343 | +0.1012 | -0.58% | 2.02% | 5150/6142 |
| d_Beta | -0.2638 | +0.0526 | -0.3574 | 1.54% | 1.85% | 3071/2068 |
| d_20-Day Simple Moving Average | -0.2444 | -0.0891 | -0.2107 | 0.03% | 1.65% | 6012/5590 |
| d_Price | -0.2427 | -0.0708 | -0.0138 | -0.56% | 1.32% | 5068/6062 |
| Relative Strength Index (14) | +0.2251 | -0.0356 | +0.3925 | 0.80% | n/a | 11655/0 |
| upside_pct_lvl | -0.2172 | +0.1188 | -0.3212 | 1.70% | 1.87% | 4360/270 |
| d_Performance (Quarter) | +0.2018 | -0.0136 | +0.2874 | 1.20% | 0.75% | 3181/7963 |
| d_Performance (YTD) | -0.2013 | -0.0963 | -0.0601 | -0.55% | 2.04% | 5145/6131 |
| d_50-Day Simple Moving Average | -0.2007 | -0.0790 | -0.1540 | -0.61% | 2.22% | 5759/5816 |
| d_200-Day Simple Moving Average | -0.2002 | -0.0971 | -0.0888 | -0.61% | 2.04% | 5316/6235 |
| true_ret | -0.1802 | -0.1174 | -0.0685 | -0.56% | 1.32% | 5068/6062 |
| Performance (Month) | +0.1771 | -0.1300 | +0.4713 | 1.03% | 0.71% | 3589/7963 |
| Short Float | +0.1652 | +0.3168 | -0.1851 | 2.16% | n/a | 5659/0 |
| d_Market Cap | -0.0930 | +0.0161 | -0.0309 | 0.60% | 1.94% | 2322/3438 |
| d_Forward P/E | -0.0928 | +0.0227 | -0.1548 | 0.91% | 1.96% | 1138/1795 |
| d_Volatility (Month) | -0.0860 | +0.2000 | -0.2330 | 1.06% | 0.38% | 7512/2514 |
| Relative Volume | +0.0659 | +0.0500 | -0.0643 | 0.81% | n/a | 11488/0 |
| d_Institutional Transactions | -0.0506 | -0.0236 | -0.0198 | 3.12% | 1.94% | 1907/2190 |
| d_Institutional Ownership | -0.0384 | -0.0572 | -0.0158 | 1.00% | 1.70% | 1692/1734 |
| d_Performance (Month) | +0.0299 | +0.0212 | +0.0379 | 0.27% | 1.60% | 6656/4775 |
| Institutional Transactions | -0.0293 | +0.0750 | -0.0771 | 2.96% | 1.44% | 3260/1788 |
| d_Average Volume | +0.0276 | -0.0392 | -0.0091 | 1.38% | 0.23% | 5987/5040 |
| d_Analyst Recom | +0.0256 | +0.0424 | -0.0269 | 2.12% | 0.98% | 92/81 |

## Combinations

| Pattern | n | Mean long fwd | Hit up |
|---|---|---|---|
| true_ret>3% & DOWNTREND | 493 | -3.67% | 30.0% |
| true_ret>3% & UPTREND | 162 | 0.87% | 47.5% |
| true_ret>3% & MIXED | 159 | -0.86% | 39.0% |

## Risk dominance probes

| State | n | Mean long fwd | Mean fwd if score top quintile |
|---|---|---|---|
| EXTENDED | 116 | -0.23% | -8.86% |
| WASHED | 1661 | 3.06% | -2.31% |

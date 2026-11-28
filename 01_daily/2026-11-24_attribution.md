# Factor attribution — signal 2026-11-24 → prediction day 2026-11-27

## Trade window (read this first)

| Role | Date | Meaning |
|------|------|---------|
| **Signal as-of** | **2026-11-24** | Features/scores formed from this snapshot (and deltas vs **2026-11-23**). Only data on/before this date. |
| **Prediction day** | **2026-11-27** | The trading day the forward return is for (exit snapshot). |
| **Entry price** | Price @ 2026-11-24 | Long: buy here; short: sell here. |
| **Exit price** | Price @ 2026-11-27 | Close proxy on prediction day. |
| **Return column** | `fwd_2d` | Long: exit/entry − 1; short = opposite. |

Graded **n=11768** names with valid entry and exit prices.

Provisional until multiple signal dates agree.

_Column guide: **IC** = Spearman(feature, long forward return); **IC↑** / **IC↓** = IC among names that went up / down._

## Score calibration (long fwd)
- Spearman IC(total_score, fwd_2d) = **-0.1890**

| Quintile | Mean long fwd | Hit up>1.5% | n |
|---|---|---|---|
| 1 | 6.48% | 70.7% | 2449 |
| 2 | 1.92% | 44.2% | 3292 |
| 3 | 1.95% | 37.1% | 1638 |
| 4 | 2.56% | 38.8% | 2166 |
| 5 | 2.59% | 50.7% | 2223 |

## Top |IC| features

| Feature | IC | IC↑ | IC↓ | Mean fwd when + | Mean fwd when − | n+/n− |
|---|---|---|---|---|---|---|
| Performance (Week) | -0.3573 | -0.4729 | +0.1532 | 1.16% | 3.97% | 3390/8208 |
| Performance (Month) | -0.3199 | -0.4660 | +0.1956 | 1.72% | 3.63% | 2948/8640 |
| Relative Strength Index (14) | -0.3052 | -0.3776 | +0.2269 | 3.13% | n/a | 11676/0 |
| d_Forward P/E | -0.2344 | -0.2685 | +0.1761 | 2.08% | 3.88% | 1704/1168 |
| true_ret | -0.2104 | -0.2301 | -0.0093 | 2.16% | 4.07% | 5136/6061 |
| d_Performance (YTD) | -0.1993 | -0.2060 | +0.0297 | 2.25% | 3.61% | 5201/6116 |
| d_Performance (Month) | -0.1976 | -0.1791 | -0.0904 | 2.74% | 3.47% | 4723/6763 |
| d_200-Day Simple Moving Average | -0.1951 | -0.2002 | -0.0070 | 2.20% | 4.02% | 5456/6140 |
| d_Price | -0.1902 | -0.1798 | +0.0334 | 2.16% | 4.07% | 5136/6061 |
| Short Float | +0.1852 | +0.2170 | -0.0264 | 4.48% | n/a | 5597/0 |
| d_50-Day Simple Moving Average | -0.1749 | -0.1757 | -0.0301 | 2.33% | 3.94% | 5662/5952 |
| upside_pct_lvl | +0.1720 | +0.4945 | -0.5380 | 4.14% | 1.23% | 4412/215 |
| d_Performance (Quarter) | -0.1696 | -0.1697 | +0.0141 | 2.58% | 3.83% | 5499/5739 |
| d_Market Cap | -0.1647 | -0.2450 | +0.2526 | 3.03% | 6.16% | 3141/2558 |
| d_20-Day Simple Moving Average | -0.1483 | -0.1407 | -0.0509 | 2.42% | 3.94% | 6009/5599 |
| d_Relative Strength Index (14) | -0.1454 | -0.1256 | +0.0589 | 2.24% | 4.02% | 5224/6121 |
| d_Volatility (Month) | +0.1440 | +0.2724 | -0.2401 | 3.77% | 2.72% | 7326/2680 |
| Relative Volume | +0.1042 | +0.0870 | -0.0347 | 3.16% | n/a | 11542/0 |
| d_Beta | -0.0710 | -0.0907 | +0.0732 | 3.09% | 3.86% | 5248/3515 |
| d_Target Price | -0.0665 | -0.0817 | +0.0020 | 2.89% | 4.47% | 159/302 |
| d_Average Volume | +0.0595 | +0.0498 | -0.0757 | 3.39% | 2.86% | 7214/3903 |
| d_Performance (Week) | -0.0479 | -0.0493 | -0.0287 | 2.48% | 4.38% | 7358/4184 |
| d_Relative Volume | -0.0238 | -0.0174 | +0.0615 | 2.96% | 3.30% | 4487/6943 |
| d_Insider Transactions | +0.0195 | +0.0397 | -0.0594 | 5.22% | 3.42% | 91/105 |
| Institutional Transactions | -0.0181 | +0.0043 | -0.0393 | 5.62% | 3.49% | 2579/2421 |

## Combinations

| Pattern | n | Mean long fwd | Hit up |
|---|---|---|---|
| true_ret>3% & DOWNTREND | 592 | 5.68% | 52.0% |
| true_ret>3% & UPTREND | 312 | 0.05% | 38.1% |
| true_ret>3% & MIXED | 231 | 0.39% | 43.3% |

## Risk dominance probes

| State | n | Mean long fwd | Mean fwd if score top quintile |
|---|---|---|---|
| EXTENDED | 154 | -0.51% | -1.28% |
| WASHED | 2072 | 7.88% | 8.41% |

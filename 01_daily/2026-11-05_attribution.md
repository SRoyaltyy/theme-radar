# Factor attribution — signal 2026-11-05 → prediction day 2026-11-06

## Trade window (read this first)

| Role | Date | Meaning |
|------|------|---------|
| **Signal as-of** | **2026-11-05** | Features/scores formed from this snapshot (and deltas vs **2026-11-04**). Only data on/before this date. |
| **Prediction day** | **2026-11-06** | The trading day the forward return is for (exit snapshot). |
| **Entry price** | Price @ 2026-11-05 | Long: buy here; short: sell here. |
| **Exit price** | Price @ 2026-11-06 | Close proxy on prediction day. |
| **Return column** | `fwd_1d` | Long: exit/entry − 1; short = opposite. |

Graded **n=11744** names with valid entry and exit prices.

Provisional until multiple signal dates agree.

_Column guide: **IC** = Spearman(feature, long forward return); **IC↑** / **IC↓** = IC among names that went up / down._

## Score calibration (long fwd)
- Spearman IC(total_score, fwd_1d) = **-0.2242**

| Quintile | Mean long fwd | Hit up>1.5% | n |
|---|---|---|---|
| 1 | 2.10% | 30.8% | 2357 |
| 2 | 7.75% | 33.5% | 2357 |
| 3 | 3.29% | 30.6% | 2500 |
| 4 | 0.12% | 14.2% | 2261 |
| 5 | 0.09% | 17.9% | 2269 |

## Top |IC| features

| Feature | IC | IC↑ | IC↓ | Mean fwd when + | Mean fwd when − | n+/n− |
|---|---|---|---|---|---|---|
| Performance (Month) | -0.4118 | -0.5165 | -0.0210 | -0.36% | 4.81% | 4622/6959 |
| Performance (Week) | -0.3831 | -0.4850 | -0.0044 | -0.34% | 4.16% | 3639/7962 |
| Relative Strength Index (14) | -0.3759 | -0.2889 | +0.0597 | 2.73% | n/a | 11685/0 |
| upside_pct_lvl | +0.3376 | +0.4937 | -0.2543 | 2.42% | -0.76% | 4317/317 |
| true_ret | -0.3267 | -0.5430 | +0.2109 | -0.20% | 3.36% | 1871/9575 |
| d_50-Day Simple Moving Average | -0.2941 | -0.4745 | +0.1757 | -0.13% | 3.36% | 2049/9593 |
| d_200-Day Simple Moving Average | -0.2824 | -0.4106 | +0.1273 | -0.17% | 3.02% | 1977/9646 |
| d_20-Day Simple Moving Average | -0.2822 | -0.4995 | +0.2005 | 0.28% | 3.22% | 1901/9731 |
| d_Performance (YTD) | -0.2771 | -0.3668 | +0.0952 | -0.17% | 3.03% | 1888/9595 |
| d_Performance (Quarter) | -0.2755 | -0.4536 | +0.1673 | -0.15% | 3.30% | 1625/9603 |
| d_Performance (Month) | -0.2576 | -0.3912 | +0.1419 | 0.33% | 3.54% | 2778/8726 |
| d_Performance (Week) | -0.2110 | -0.4587 | +0.2013 | 0.46% | 3.22% | 1899/9638 |
| d_Forward P/E | -0.2064 | -0.3095 | +0.0267 | -0.19% | 0.48% | 477/2496 |
| Institutional Transactions | +0.1342 | +0.1454 | +0.0166 | 6.70% | 0.69% | 3193/1832 |
| d_Price | -0.1335 | -0.1424 | +0.0016 | -0.20% | 3.36% | 1871/9575 |
| d_Relative Volume | +0.1140 | +0.0540 | +0.0382 | 2.22% | 3.69% | 7039/4393 |
| d_Beta | -0.1059 | -0.0193 | -0.1145 | 3.14% | 9.89% | 2537/1799 |
| Relative Volume | +0.1028 | +0.1598 | -0.0606 | 2.76% | n/a | 11573/0 |
| Short Float | +0.0654 | +0.3530 | -0.1845 | 3.22% | n/a | 5632/0 |
| d_Volatility (Month) | +0.0643 | +0.3642 | -0.3194 | 3.08% | 3.38% | 7757/2267 |
| d_Institutional Ownership | +0.0576 | +0.1107 | -0.0457 | 4.35% | 0.85% | 1777/1497 |
| d_EPS Surprise | +0.0542 | +0.0609 | +0.0322 | 2.12% | 0.46% | 263/286 |
| d_Market Cap | -0.0434 | -0.0769 | -0.1215 | 0.24% | 5.21% | 885/4924 |
| d_Target Price | -0.0421 | -0.0324 | +0.0553 | 0.69% | 1.43% | 380/322 |
| d_Relative Strength Index (14) | -0.0377 | +0.1963 | -0.0908 | -0.19% | 3.37% | 1898/9571 |

## Combinations

| Pattern | n | Mean long fwd | Hit up |
|---|---|---|---|
| true_ret>3% & DOWNTREND | 136 | -0.39% | 38.2% |
| true_ret>3% & UPTREND | 150 | -0.71% | 25.3% |
| true_ret>3% & MIXED | 143 | -2.13% | 25.2% |

## Risk dominance probes

| State | n | Mean long fwd | Mean fwd if score top quintile |
|---|---|---|---|
| EXTENDED | 260 | -1.95% | -3.19% |
| WASHED | 2722 | 9.41% | 3.88% |

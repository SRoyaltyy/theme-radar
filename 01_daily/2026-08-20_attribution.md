# Factor attribution — signal 2026-08-20 → prediction day 2026-08-21

## Trade window (read this first)

| Role | Date | Meaning |
|------|------|---------|
| **Signal as-of** | **2026-08-20** | Features/scores formed from this snapshot (and deltas vs **2026-08-19**). Only data on/before this date. |
| **Prediction day** | **2026-08-21** | The trading day the forward return is for (exit snapshot). |
| **Entry price** | Price @ 2026-08-20 | Long: buy here; short: sell here. |
| **Exit price** | Price @ 2026-08-21 | Close proxy on prediction day. |
| **Return column** | `fwd_1d` | Long: exit/entry − 1; short = opposite. |

Graded **n=11599** names with valid entry and exit prices.

Provisional until multiple signal dates agree.

_Column guide: **IC** = Spearman(feature, long forward return); **IC↑** / **IC↓** = IC among names that went up / down._

## Score calibration (long fwd)
- Spearman IC(total_score, fwd_1d) = **-0.0007**

| Quintile | Mean long fwd | Hit up>1.5% | n |
|---|---|---|---|
| 1 | 2.08% | 32.2% | 2323 |
| 2 | 0.58% | 14.9% | 3302 |
| 3 | 3.96% | 16.4% | 1398 |
| 4 | 0.49% | 10.6% | 2341 |
| 5 | 4.30% | 34.9% | 2235 |

## Top |IC| features

| Feature | IC | IC↑ | IC↓ | Mean fwd when + | Mean fwd when − | n+/n− |
|---|---|---|---|---|---|---|
| Performance (Month) | +0.1966 | +0.1457 | +0.1160 | 1.16% | 3.43% | 7086/4272 |
| d_Performance (Quarter) | -0.1741 | -0.1868 | +0.0206 | 6.78% | 0.85% | 2211/8622 |
| d_20-Day Simple Moving Average | -0.1607 | -0.1465 | -0.0359 | 4.84% | 0.88% | 3258/8212 |
| d_50-Day Simple Moving Average | -0.1388 | -0.1201 | -0.0377 | 4.13% | 1.11% | 3405/8067 |
| d_Beta | +0.1341 | +0.1984 | +0.0519 | 2.58% | 8.71% | 2044/1418 |
| d_200-Day Simple Moving Average | -0.1307 | -0.0933 | -0.0524 | 4.12% | 1.10% | 3462/7975 |
| d_Performance (YTD) | -0.1240 | -0.1022 | -0.0234 | 4.16% | 1.11% | 3394/7810 |
| true_ret | -0.1176 | -0.1301 | +0.0001 | 2.84% | 1.12% | 3312/7743 |
| Relative Strength Index (14) | +0.1085 | -0.0569 | +0.0796 | 2.00% | n/a | 11461/0 |
| d_Price | -0.1027 | +0.0249 | -0.0878 | 2.84% | 1.12% | 3312/7743 |
| Short Float | +0.0976 | +0.1812 | -0.1228 | 3.27% | n/a | 5701/0 |
| d_Performance (Week) | -0.0974 | -0.0822 | -0.0011 | 3.16% | 1.59% | 3119/8257 |
| d_Market Cap | -0.0815 | +0.0221 | -0.1045 | 6.02% | 1.60% | 2085/3662 |
| d_Forward P/E | -0.0766 | -0.0663 | +0.0136 | 0.68% | 0.90% | 1041/1898 |
| d_Performance (Month) | -0.0549 | -0.0175 | -0.0395 | 2.76% | 1.54% | 4571/6660 |
| upside_pct_lvl | +0.0529 | +0.3364 | -0.3857 | 1.27% | 0.57% | 4317/334 |
| Relative Volume | +0.0520 | +0.1385 | -0.0059 | 2.03% | n/a | 11325/0 |
| d_Relative Strength Index (14) | -0.0464 | +0.1947 | -0.2295 | 4.12% | 1.12% | 3417/7757 |
| Performance (Week) | -0.0372 | -0.0275 | +0.0499 | 1.44% | 2.29% | 3651/7748 |
| d_Volatility (Month) | +0.0370 | +0.1270 | -0.1212 | 2.59% | 2.03% | 5474/3871 |
| d_Profit Margin | +0.0334 | +0.0005 | +0.0509 | 1.31% | -1.59% | 22/34 |
| d_EPS Surprise | -0.0332 | -0.0209 | -0.0396 | 0.11% | 3.11% | 21/27 |
| d_Gross Margin | +0.0330 | +0.0212 | +0.0788 | 1.23% | -2.02% | 29/31 |
| Institutional Transactions | -0.0233 | +0.0261 | -0.0372 | 5.50% | 1.49% | 2690/2353 |
| d_Sales Year Over Year TTM | +0.0216 | -0.0037 | +0.0202 | -0.39% | -0.83% | 22/29 |

## Combinations

| Pattern | n | Mean long fwd | Hit up |
|---|---|---|---|
| true_ret>3% & DOWNTREND | 246 | 20.99% | 33.3% |
| true_ret>3% & UPTREND | 249 | 2.89% | 48.6% |
| true_ret>3% & MIXED | 276 | 8.01% | 66.7% |

## Risk dominance probes

| State | n | Mean long fwd | Mean fwd if score top quintile |
|---|---|---|---|
| EXTENDED | 289 | 2.31% | 5.73% |
| WASHED | 575 | 12.69% | 45.59% |

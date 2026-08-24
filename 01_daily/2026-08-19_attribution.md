# Factor attribution — signal 2026-08-19 → prediction day 2026-08-24

## Trade window (read this first)

| Role | Date | Meaning |
|------|------|---------|
| **Signal as-of** | **2026-08-19** | Features/scores formed from this snapshot (and deltas vs **2026-08-18**). Only data on/before this date. |
| **Prediction day** | **2026-08-24** | The trading day the forward return is for (exit snapshot). |
| **Entry price** | Price @ 2026-08-19 | Long: buy here; short: sell here. |
| **Exit price** | Price @ 2026-08-24 | Close proxy on prediction day. |
| **Return column** | `fwd_3d` | Long: exit/entry − 1; short = opposite. |

Graded **n=11578** names with valid entry and exit prices.

Provisional until multiple signal dates agree.

_Column guide: **IC** = Spearman(feature, long forward return); **IC↑** / **IC↓** = IC among names that went up / down._

## Score calibration (long fwd)
- Spearman IC(total_score, fwd_3d) = **0.1772**

| Quintile | Mean long fwd | Hit up>1.5% | n |
|---|---|---|---|
| 1 | 5.28% | 15.4% | 2332 |
| 2 | -0.06% | 10.7% | 2838 |
| 3 | 0.38% | 10.8% | 2291 |
| 4 | 0.68% | 18.3% | 1801 |
| 5 | 6.27% | 36.3% | 2316 |

## Top |IC| features

| Feature | IC | IC↑ | IC↓ | Mean fwd when + | Mean fwd when − | n+/n− |
|---|---|---|---|---|---|---|
| Performance (Week) | +0.2214 | +0.1745 | +0.2263 | 3.67% | 1.53% | 5369/5989 |
| d_Performance (Month) | +0.2140 | +0.1887 | +0.1988 | 2.27% | 2.81% | 5235/6030 |
| d_Price | +0.2107 | +0.1677 | +0.1933 | 2.13% | 2.15% | 7193/3829 |
| d_200-Day Simple Moving Average | +0.1978 | +0.3073 | +0.0921 | 2.28% | 2.97% | 7292/4127 |
| d_Performance (YTD) | +0.1975 | +0.2734 | +0.1107 | 2.11% | 3.16% | 7282/3894 |
| true_ret | +0.1948 | +0.3068 | +0.0990 | 2.13% | 2.15% | 7193/3829 |
| d_Performance (Week) | +0.1939 | +0.3084 | +0.0935 | 3.80% | 1.06% | 6112/5184 |
| d_Relative Strength Index (14) | +0.1915 | +0.1663 | +0.2633 | 2.27% | 3.20% | 7269/3866 |
| Relative Strength Index (14) | +0.1836 | -0.1103 | +0.3101 | 2.53% | n/a | 11448/0 |
| d_20-Day Simple Moving Average | +0.1834 | +0.3159 | +0.0756 | 2.79% | 2.09% | 7126/4300 |
| d_Forward P/E | +0.1826 | +0.1937 | +0.1148 | 0.33% | -0.21% | 1657/1316 |
| d_50-Day Simple Moving Average | +0.1812 | +0.3187 | +0.0671 | 2.80% | 2.05% | 7255/4170 |
| upside_pct_lvl | -0.1478 | +0.3264 | -0.4003 | 1.66% | 0.10% | 4291/354 |
| Short Float | -0.1257 | +0.1378 | -0.2685 | 3.89% | n/a | 5665/0 |
| d_Performance (Quarter) | +0.1072 | +0.3066 | -0.0449 | 2.34% | 3.52% | 7933/2886 |
| d_Market Cap | +0.1011 | +0.1146 | +0.0524 | 2.13% | 5.66% | 3318/2394 |
| Performance (Month) | +0.0931 | +0.0552 | +0.0644 | 1.05% | 5.15% | 7195/4147 |
| Institutional Transactions | -0.0810 | -0.0178 | -0.1031 | 6.04% | 2.42% | 2690/2351 |
| d_Beta | +0.0771 | -0.0398 | +0.1433 | 6.75% | 4.00% | 1827/2382 |
| d_Relative Volume | +0.0743 | +0.1656 | -0.0201 | 4.57% | 0.24% | 6003/5125 |
| d_Analyst Recom | +0.0341 | -0.0138 | +0.0211 | 0.11% | -1.33% | 103/105 |
| d_Volatility (Month) | -0.0331 | -0.0582 | -0.0098 | 1.10% | 3.69% | 3847/5542 |
| d_Short Float | +0.0277 | -0.0774 | +0.0954 | -0.68% | 12.36% | 213/345 |
| d_Sales Growth Quarter Over Quarter | +0.0269 | +0.0202 | +0.0322 | 1.37% | -1.38% | 17/25 |
| d_Target Price | +0.0232 | -0.0377 | +0.0358 | -0.24% | -0.47% | 236/159 |

## Combinations

| Pattern | n | Mean long fwd | Hit up |
|---|---|---|---|
| true_ret>3% & DOWNTREND | 523 | 13.15% | 40.5% |
| true_ret>3% & UPTREND | 682 | 1.41% | 39.6% |
| true_ret>3% & MIXED | 514 | 13.83% | 53.1% |

## Risk dominance probes

| State | n | Mean long fwd | Mean fwd if score top quintile |
|---|---|---|---|
| EXTENDED | 293 | 5.41% | 25.74% |
| WASHED | 544 | 22.53% | 6.69% |

# Factor attribution — signal 2026-10-02 → prediction day 2026-10-07

## Trade window (read this first)

| Role | Date | Meaning |
|------|------|---------|
| **Signal as-of** | **2026-10-02** | Features/scores formed from this snapshot (and deltas vs **2026-10-01**). Only data on/before this date. |
| **Prediction day** | **2026-10-07** | The trading day the forward return is for (exit snapshot). |
| **Entry price** | Price @ 2026-10-02 | Long: buy here; short: sell here. |
| **Exit price** | Price @ 2026-10-07 | Close proxy on prediction day. |
| **Return column** | `fwd_3d` | Long: exit/entry − 1; short = opposite. |

Graded **n=11684** names with valid entry and exit prices.

Provisional until multiple signal dates agree.

_Column guide: **IC** = Spearman(feature, long forward return); **IC↑** / **IC↓** = IC among names that went up / down._

## Score calibration (long fwd)
- Spearman IC(total_score, fwd_3d) = **-0.0028**

| Quintile | Mean long fwd | Hit up>1.5% | n |
|---|---|---|---|
| 1 | 2.06% | 17.2% | 2538 |
| 2 | 0.05% | 9.5% | 2472 |
| 3 | -0.38% | 12.1% | 2086 |
| 4 | -0.15% | 16.1% | 2284 |
| 5 | -1.10% | 22.8% | 2304 |

## Top |IC| features

| Feature | IC | IC↑ | IC↓ | Mean fwd when + | Mean fwd when − | n+/n− |
|---|---|---|---|---|---|---|
| d_Forward P/E | -0.1765 | -0.1059 | -0.1256 | -0.68% | 0.28% | 1895/1056 |
| upside_pct_lvl | -0.1186 | +0.2863 | -0.3629 | 0.18% | -1.30% | 4368/264 |
| Institutional Transactions | -0.1029 | +0.0109 | -0.1270 | 1.01% | -0.26% | 3231/1811 |
| Performance (Week) | +0.0898 | -0.0707 | +0.1615 | -0.53% | 0.47% | 3926/7592 |
| d_Beta | -0.0766 | +0.0433 | -0.1052 | 0.41% | 0.50% | 4377/2560 |
| Short Float | -0.0557 | +0.1587 | -0.1836 | 0.41% | n/a | 5689/0 |
| d_20-Day Simple Moving Average | -0.0543 | +0.1671 | -0.0631 | -0.24% | 1.09% | 8302/3294 |
| d_Market Cap | -0.0535 | -0.0989 | +0.0480 | -0.74% | 1.60% | 3313/2388 |
| d_Relative Volume | -0.0477 | +0.0925 | -0.1050 | 0.39% | -0.07% | 4702/6664 |
| Relative Strength Index (14) | +0.0474 | +0.0759 | -0.0836 | 0.13% | n/a | 11575/0 |
| d_50-Day Simple Moving Average | -0.0458 | +0.1101 | -0.0368 | -0.28% | 0.96% | 7718/3899 |
| d_Volatility (Month) | -0.0372 | +0.0723 | -0.1009 | 0.30% | -0.09% | 6289/3607 |
| Performance (Month) | +0.0363 | -0.1745 | +0.0956 | -0.68% | 0.52% | 3752/7741 |
| true_ret | -0.0342 | +0.0900 | -0.0164 | -0.34% | 1.17% | 7328/3868 |
| Relative Volume | -0.0324 | +0.0450 | -0.0095 | 0.14% | n/a | 11480/0 |
| d_200-Day Simple Moving Average | -0.0320 | +0.0977 | -0.0129 | -0.25% | 0.89% | 7599/3978 |
| d_Sales Growth Quarter Over Quarter | -0.0296 | +0.0121 | -0.0394 | -11.62% | -0.99% | 4/3 |
| d_Institutional Ownership | +0.0295 | +0.0529 | -0.0678 | -0.52% | -0.96% | 331/514 |
| d_Performance (YTD) | -0.0269 | +0.0730 | +0.0121 | -0.36% | 0.86% | 7384/3935 |
| d_Performance (Week) | -0.0251 | +0.1064 | -0.0582 | -0.29% | 0.75% | 6830/4626 |
| d_EPS Surprise | -0.0240 | +0.0049 | -0.0259 | -2.91% | 3.13% | 2/3 |
| d_Performance (Quarter) | -0.0197 | -0.0180 | +0.0149 | -0.24% | 0.53% | 5107/5944 |
| d_Profit Margin | +0.0184 | -0.0259 | +0.0174 | -4.12% | -6.47% | 2/6 |
| d_Analyst Recom | -0.0183 | -0.0424 | -0.0146 | -0.93% | -0.20% | 63/65 |
| d_Relative Strength Index (14) | +0.0175 | -0.0739 | +0.1508 | -0.35% | 1.09% | 7356/3935 |

## Combinations

| Pattern | n | Mean long fwd | Hit up |
|---|---|---|---|
| true_ret>3% & DOWNTREND | 381 | 1.03% | 27.6% |
| true_ret>3% & UPTREND | 378 | -1.86% | 24.6% |
| true_ret>3% & MIXED | 220 | -1.21% | 26.8% |

## Risk dominance probes

| State | n | Mean long fwd | Mean fwd if score top quintile |
|---|---|---|---|
| EXTENDED | 215 | -1.50% | -2.62% |
| WASHED | 2057 | 2.50% | -1.75% |

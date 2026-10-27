# Factor attribution — signal 2026-10-21 → prediction day 2026-10-26

## Trade window (read this first)

| Role | Date | Meaning |
|------|------|---------|
| **Signal as-of** | **2026-10-21** | Features/scores formed from this snapshot (and deltas vs **2026-10-20**). Only data on/before this date. |
| **Prediction day** | **2026-10-26** | The trading day the forward return is for (exit snapshot). |
| **Entry price** | Price @ 2026-10-21 | Long: buy here; short: sell here. |
| **Exit price** | Price @ 2026-10-26 | Close proxy on prediction day. |
| **Return column** | `fwd_3d` | Long: exit/entry − 1; short = opposite. |

Graded **n=11733** names with valid entry and exit prices.

Provisional until multiple signal dates agree.

_Column guide: **IC** = Spearman(feature, long forward return); **IC↑** / **IC↓** = IC among names that went up / down._

## Score calibration (long fwd)
- Spearman IC(total_score, fwd_3d) = **0.0185**

| Quintile | Mean long fwd | Hit up>1.5% | n |
|---|---|---|---|
| 1 | 6.98% | 23.0% | 2349 |
| 2 | 1.83% | 16.4% | 3007 |
| 3 | -1.30% | 12.6% | 1711 |
| 4 | -0.23% | 16.3% | 2443 |
| 5 | -1.66% | 26.2% | 2223 |

## Top |IC| features

| Feature | IC | IC↑ | IC↓ | Mean fwd when + | Mean fwd when − | n+/n− |
|---|---|---|---|---|---|---|
| d_Performance (Week) | -0.3873 | +0.0510 | -0.4312 | -0.03% | 5.45% | 8588/2898 |
| Performance (Month) | +0.3748 | -0.0754 | +0.5399 | 0.22% | 1.86% | 3617/7920 |
| upside_pct_lvl | -0.3440 | +0.1412 | -0.4036 | 0.32% | 0.00% | 4320/310 |
| d_20-Day Simple Moving Average | -0.3279 | -0.0996 | -0.3135 | 0.25% | 3.36% | 7515/4016 |
| Relative Strength Index (14) | +0.2942 | -0.0780 | +0.4300 | 1.32% | n/a | 11653/0 |
| d_Performance (Quarter) | -0.2781 | -0.0167 | -0.2098 | -0.38% | 6.53% | 8294/2862 |
| d_50-Day Simple Moving Average | -0.2715 | -0.0675 | -0.2404 | 0.40% | 3.26% | 7786/3762 |
| d_200-Day Simple Moving Average | -0.2541 | -0.0953 | -0.1836 | 0.20% | 3.17% | 7318/4175 |
| true_ret | -0.2453 | -0.1072 | -0.1836 | -1.34% | 3.03% | 7014/3996 |
| d_Performance (YTD) | -0.2370 | -0.1028 | -0.1322 | -0.55% | 3.32% | 7101/4097 |
| d_Beta | +0.2369 | -0.0630 | +0.3132 | 10.36% | 8.84% | 678/1704 |
| d_Relative Strength Index (14) | -0.2352 | -0.1291 | +0.0686 | 0.12% | 3.51% | 7110/4116 |
| d_Price | -0.2259 | -0.1132 | -0.0258 | -1.34% | 3.03% | 7014/3996 |
| Performance (Week) | +0.1896 | +0.1324 | +0.1734 | 0.35% | 3.14% | 7425/4113 |
| d_Forward P/E | -0.1629 | -0.0530 | -0.1474 | -0.68% | 1.04% | 1508/1420 |
| d_Market Cap | -0.1085 | -0.0228 | -0.0126 | 3.10% | 4.53% | 2903/2772 |
| Relative Volume | +0.0767 | +0.1015 | -0.0380 | 1.37% | n/a | 11386/0 |
| d_Volatility (Month) | -0.0568 | +0.1296 | -0.1924 | 1.97% | 1.23% | 5869/3828 |
| d_Performance (Month) | -0.0437 | -0.0125 | -0.0006 | -0.25% | 3.43% | 6382/4985 |
| Institutional Transactions | -0.0408 | +0.0805 | -0.1006 | 3.81% | 6.47% | 3255/1788 |
| d_Analyst Recom | +0.0385 | -0.0039 | +0.0030 | 0.21% | -1.79% | 83/54 |
| d_Average Volume | +0.0329 | +0.0074 | -0.0461 | 3.23% | -0.59% | 5946/5047 |
| d_Total Debt/Equity | -0.0243 | -0.0282 | -0.0373 | -0.88% | 2.42% | 20/27 |
| d_Gross Margin | -0.0243 | -0.0253 | +0.0076 | -1.43% | 2.94% | 24/16 |
| d_Short Ratio | -0.0188 | -0.0051 | +0.0248 | -0.89% | -1.18% | 3159/3690 |

## Combinations

| Pattern | n | Mean long fwd | Hit up |
|---|---|---|---|
| true_ret>3% & DOWNTREND | 651 | -1.93% | 13.4% |
| true_ret>3% & UPTREND | 254 | -2.52% | 34.3% |
| true_ret>3% & MIXED | 185 | -4.81% | 17.3% |

## Risk dominance probes

| State | n | Mean long fwd | Mean fwd if score top quintile |
|---|---|---|---|
| EXTENDED | 156 | -0.82% | -2.29% |
| WASHED | 1473 | 14.16% | -4.50% |

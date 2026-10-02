# Factor attribution — signal 2026-09-29 → prediction day 2026-10-02

## Trade window (read this first)

| Role | Date | Meaning |
|------|------|---------|
| **Signal as-of** | **2026-09-29** | Features/scores formed from this snapshot (and deltas vs **2026-09-28**). Only data on/before this date. |
| **Prediction day** | **2026-10-02** | The trading day the forward return is for (exit snapshot). |
| **Entry price** | Price @ 2026-09-29 | Long: buy here; short: sell here. |
| **Exit price** | Price @ 2026-10-02 | Close proxy on prediction day. |
| **Return column** | `fwd_3d` | Long: exit/entry − 1; short = opposite. |

Graded **n=11671** names with valid entry and exit prices.

Provisional until multiple signal dates agree.

_Column guide: **IC** = Spearman(feature, long forward return); **IC↑** / **IC↓** = IC among names that went up / down._

## Score calibration (long fwd)
- Spearman IC(total_score, fwd_3d) = **0.0858**

| Quintile | Mean long fwd | Hit up>1.5% | n |
|---|---|---|---|
| 1 | 2.44% | 20.9% | 2364 |
| 2 | -0.15% | 12.3% | 2529 |
| 3 | 0.32% | 18.0% | 2177 |
| 4 | 0.07% | 20.3% | 2296 |
| 5 | 1.23% | 41.1% | 2305 |

## Top |IC| features

| Feature | IC | IC↑ | IC↓ | Mean fwd when + | Mean fwd when − | n+/n− |
|---|---|---|---|---|---|---|
| upside_pct_lvl | -0.1824 | +0.1969 | -0.3654 | 0.20% | 0.02% | 4388/247 |
| Performance (Month) | +0.1813 | -0.0377 | +0.2419 | 0.88% | 0.75% | 3091/8389 |
| d_Performance (Quarter) | -0.1811 | -0.1794 | -0.0033 | 0.91% | 0.68% | 4226/6822 |
| Relative Strength Index (14) | +0.1315 | +0.0412 | -0.1660 | 0.78% | n/a | 11566/0 |
| d_Beta | -0.0955 | +0.0275 | -0.0848 | 0.42% | -0.04% | 3551/1244 |
| Performance (Week) | +0.0736 | -0.2194 | +0.2291 | 0.10% | 0.92% | 1894/9627 |
| d_Performance (Week) | +0.0726 | -0.0664 | +0.1624 | 1.46% | 0.42% | 4040/7371 |
| true_ret | +0.0650 | +0.0185 | +0.0972 | 1.61% | 0.10% | 4228/6815 |
| d_Average Volume | -0.0629 | -0.2294 | +0.1344 | 1.46% | 0.40% | 4140/6936 |
| d_Short Ratio | +0.0618 | +0.2004 | -0.1438 | 0.39% | 0.16% | 5154/2449 |
| d_Volatility (Month) | -0.0576 | +0.0359 | -0.1093 | 1.23% | 0.44% | 5835/3580 |
| d_Performance (Month) | +0.0534 | +0.1888 | -0.0832 | 0.60% | 0.86% | 6638/4751 |
| d_Performance (YTD) | +0.0531 | +0.0305 | +0.0615 | 1.58% | 0.23% | 4315/6938 |
| d_Price | +0.0473 | +0.0766 | -0.0239 | 1.61% | 0.10% | 4228/6815 |
| d_Forward P/E | +0.0435 | +0.1254 | +0.0055 | 0.65% | 0.29% | 1188/1742 |
| d_50-Day Simple Moving Average | +0.0396 | +0.0308 | +0.0570 | 1.78% | 0.15% | 4558/6978 |
| d_EPS Surprise | -0.0351 | -0.0135 | -0.0050 | -5.15% | 0.68% | 7/5 |
| d_Relative Strength Index (14) | +0.0329 | +0.1013 | -0.0045 | 1.57% | 0.21% | 4306/6920 |
| d_200-Day Simple Moving Average | +0.0289 | +0.0304 | +0.0412 | 1.58% | 0.29% | 4469/7064 |
| Institutional Transactions | -0.0199 | +0.0252 | -0.1084 | 0.50% | 2.42% | 3234/1812 |
| d_Sales Year Over Year TTM | +0.0173 | +0.0330 | +0.0024 | -1.00% | -4.48% | 14/9 |
| d_Total Debt/Equity | -0.0169 | +0.0007 | -0.0017 | -4.79% | -1.59% | 10/11 |
| d_20-Day Simple Moving Average | +0.0144 | +0.0413 | +0.0281 | 1.44% | 0.22% | 5414/6111 |
| Short Float | +0.0133 | +0.2382 | -0.1406 | 1.28% | n/a | 5692/0 |
| d_Market Cap | +0.0109 | +0.0752 | -0.0289 | 1.88% | 0.49% | 2437/3260 |

## Combinations

| Pattern | n | Mean long fwd | Hit up |
|---|---|---|---|
| true_ret>3% & DOWNTREND | 268 | 17.35% | 39.2% |
| true_ret>3% & UPTREND | 194 | 4.10% | 54.6% |
| true_ret>3% & MIXED | 127 | 1.88% | 38.6% |

## Risk dominance probes

| State | n | Mean long fwd | Mean fwd if score top quintile |
|---|---|---|---|
| EXTENDED | 160 | -1.17% | -2.57% |
| WASHED | 2418 | 0.83% | 0.75% |

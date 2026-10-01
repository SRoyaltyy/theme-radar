# Factor attribution — signal 2026-09-28 → prediction day 2026-10-01

## Trade window (read this first)

| Role | Date | Meaning |
|------|------|---------|
| **Signal as-of** | **2026-09-28** | Features/scores formed from this snapshot (and deltas vs **2026-09-25**). Only data on/before this date. |
| **Prediction day** | **2026-10-01** | The trading day the forward return is for (exit snapshot). |
| **Entry price** | Price @ 2026-09-28 | Long: buy here; short: sell here. |
| **Exit price** | Price @ 2026-10-01 | Close proxy on prediction day. |
| **Return column** | `fwd_3d` | Long: exit/entry − 1; short = opposite. |

Graded **n=11666** names with valid entry and exit prices.

Provisional until multiple signal dates agree.

_Column guide: **IC** = Spearman(feature, long forward return); **IC↑** / **IC↓** = IC among names that went up / down._

## Score calibration (long fwd)
- Spearman IC(total_score, fwd_3d) = **-0.0752**

| Quintile | Mean long fwd | Hit up>1.5% | n |
|---|---|---|---|
| 1 | 3.33% | 26.8% | 2340 |
| 2 | -0.28% | 11.7% | 3371 |
| 3 | 1.23% | 11.5% | 1306 |
| 4 | -0.61% | 12.5% | 2704 |
| 5 | -1.40% | 20.1% | 1945 |

## Top |IC| features

| Feature | IC | IC↑ | IC↓ | Mean fwd when + | Mean fwd when − | n+/n− |
|---|---|---|---|---|---|---|
| d_Performance (Month) | -0.1812 | -0.2788 | -0.0467 | -1.64% | 1.09% | 3062/8322 |
| Performance (Month) | +0.1634 | -0.1209 | +0.2970 | 0.22% | 0.39% | 2791/8712 |
| upside_pct_lvl | -0.1250 | +0.2215 | -0.3559 | -0.40% | -0.74% | 4384/248 |
| d_Relative Strength Index (14) | -0.1190 | +0.1259 | -0.3313 | 0.13% | 0.43% | 2313/8986 |
| d_Forward P/E | -0.1138 | -0.1303 | -0.0394 | -0.79% | -0.24% | 843/2087 |
| d_Price | -0.1041 | -0.0590 | -0.1787 | -1.25% | 0.04% | 2256/8967 |
| d_Performance (Quarter) | -0.1013 | -0.2375 | +0.0326 | -0.04% | 0.46% | 2565/8478 |
| Relative Strength Index (14) | +0.1007 | +0.0202 | -0.0280 | 0.35% | n/a | 11563/0 |
| d_20-Day Simple Moving Average | -0.0903 | -0.2187 | +0.0137 | 1.22% | 0.06% | 2869/8718 |
| d_200-Day Simple Moving Average | -0.0843 | -0.2112 | +0.0054 | 0.94% | 0.04% | 2366/9197 |
| d_Performance (YTD) | -0.0817 | -0.2021 | +0.0040 | 0.14% | 0.29% | 2298/9038 |
| d_50-Day Simple Moving Average | -0.0787 | -0.2330 | +0.0363 | 0.88% | 0.21% | 2499/9095 |
| d_Market Cap | -0.0780 | -0.0356 | -0.1218 | -0.87% | 1.77% | 1744/3974 |
| d_Beta | +0.0739 | -0.0006 | +0.0557 | 0.55% | -0.67% | 1133/2391 |
| d_Performance (Week) | -0.0701 | -0.2295 | +0.0530 | 0.33% | 0.36% | 2551/8936 |
| Institutional Transactions | -0.0668 | -0.0074 | -0.1355 | 0.55% | 1.77% | 3234/1812 |
| true_ret | -0.0506 | -0.2496 | +0.0799 | -1.25% | 0.04% | 2256/8967 |
| Short Float | -0.0424 | +0.2523 | -0.1148 | 0.99% | n/a | 5690/0 |
| d_Volatility (Month) | -0.0348 | -0.0145 | -0.0183 | 0.50% | 0.27% | 5593/3892 |
| Performance (Week) | +0.0281 | -0.2323 | +0.1780 | -0.36% | 0.54% | 2398/9100 |
| d_Insider Transactions | +0.0273 | +0.0054 | +0.0334 | -1.07% | -2.28% | 261/151 |
| d_Institutional Ownership | +0.0253 | +0.0170 | -0.0056 | 0.74% | -1.00% | 210/397 |
| d_Relative Volume | +0.0244 | +0.0301 | +0.0001 | -0.11% | 0.87% | 6159/5076 |
| d_Sales Year Over Year TTM | +0.0189 | +0.0238 | -0.0079 | 0.56% | -2.99% | 7/2 |
| d_Gross Margin | -0.0138 | +0.0027 | +0.0014 | -3.44% | 0.19% | 5/12 |

## Combinations

| Pattern | n | Mean long fwd | Hit up |
|---|---|---|---|
| true_ret>3% & DOWNTREND | 192 | -3.14% | 30.7% |
| true_ret>3% & UPTREND | 133 | -1.43% | 34.6% |
| true_ret>3% & MIXED | 108 | -2.11% | 28.7% |

## Risk dominance probes

| State | n | Mean long fwd | Mean fwd if score top quintile |
|---|---|---|---|
| EXTENDED | 169 | -0.79% | 3.37% |
| WASHED | 2432 | 0.71% | -2.15% |

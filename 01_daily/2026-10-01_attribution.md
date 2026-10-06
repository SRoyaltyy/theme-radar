# Factor attribution — signal 2026-10-01 → prediction day 2026-10-06

## Trade window (read this first)

| Role | Date | Meaning |
|------|------|---------|
| **Signal as-of** | **2026-10-01** | Features/scores formed from this snapshot (and deltas vs **2026-09-30**). Only data on/before this date. |
| **Prediction day** | **2026-10-06** | The trading day the forward return is for (exit snapshot). |
| **Entry price** | Price @ 2026-10-01 | Long: buy here; short: sell here. |
| **Exit price** | Price @ 2026-10-06 | Close proxy on prediction day. |
| **Return column** | `fwd_3d` | Long: exit/entry − 1; short = opposite. |

Graded **n=11679** names with valid entry and exit prices.

Provisional until multiple signal dates agree.

_Column guide: **IC** = Spearman(feature, long forward return); **IC↑** / **IC↓** = IC among names that went up / down._

## Score calibration (long fwd)
- Spearman IC(total_score, fwd_3d) = **0.1116**

| Quintile | Mean long fwd | Hit up>1.5% | n |
|---|---|---|---|
| 1 | 3.50% | 31.9% | 2366 |
| 2 | 0.73% | 23.2% | 2372 |
| 3 | 0.87% | 36.3% | 2380 |
| 4 | 0.94% | 41.1% | 2321 |
| 5 | 1.83% | 47.9% | 2240 |

## Top |IC| features

| Feature | IC | IC↑ | IC↓ | Mean fwd when + | Mean fwd when − | n+/n− |
|---|---|---|---|---|---|---|
| upside_pct_lvl | -0.1528 | +0.2759 | -0.4400 | 1.67% | 0.59% | 4385/247 |
| Performance (Month) | +0.1128 | -0.0141 | +0.2082 | 1.43% | 1.65% | 3717/7769 |
| d_Performance (Month) | +0.1109 | +0.1892 | +0.0059 | 1.11% | 2.81% | 8153/3238 |
| Relative Strength Index (14) | +0.1022 | +0.1796 | -0.1328 | 1.58% | n/a | 11573/0 |
| d_Performance (Quarter) | +0.0816 | +0.1315 | -0.0090 | 1.22% | 1.97% | 5525/5542 |
| d_Price | +0.0764 | +0.0569 | +0.1467 | 1.27% | 2.10% | 6031/5090 |
| d_Performance (YTD) | +0.0711 | +0.0484 | +0.1294 | 1.23% | 2.11% | 6113/5170 |
| d_Market Cap | +0.0692 | -0.0348 | +0.1305 | 1.08% | 2.61% | 2860/2830 |
| true_ret | +0.0651 | +0.0408 | +0.1346 | 1.27% | 2.10% | 6031/5090 |
| Institutional Transactions | -0.0477 | +0.0499 | -0.0990 | 2.09% | 1.95% | 3231/1811 |
| d_Performance (Week) | +0.0456 | +0.0883 | +0.0304 | 1.11% | 2.33% | 7029/4447 |
| d_50-Day Simple Moving Average | +0.0436 | +0.0417 | +0.0935 | 1.12% | 2.13% | 6347/5201 |
| d_200-Day Simple Moving Average | +0.0432 | +0.0429 | +0.0993 | 1.13% | 2.12% | 6187/5353 |
| d_Average Volume | -0.0382 | -0.0536 | +0.0435 | 2.16% | 1.05% | 5265/5820 |
| d_Relative Strength Index (14) | +0.0372 | +0.0084 | +0.2074 | 1.24% | 2.05% | 6119/5185 |
| d_Sales Growth Quarter Over Quarter | -0.0307 | -0.0090 | -0.0456 | -2.09% | 265.39% | 10/5 |
| d_Beta | -0.0307 | -0.0099 | -0.0636 | 1.31% | 2.35% | 2075/1021 |
| d_20-Day Simple Moving Average | +0.0292 | +0.0369 | +0.0742 | 1.06% | 2.30% | 6801/4766 |
| d_Sales Year Over Year TTM | -0.0270 | -0.0050 | -0.0270 | 144.58% | 5.14% | 9/10 |
| d_Short Ratio | +0.0265 | +0.0454 | -0.0578 | 1.06% | 1.06% | 3895/3492 |
| d_Gross Margin | -0.0256 | -0.0416 | +0.0088 | -2.39% | 123.46% | 10/11 |
| d_Short Float | +0.0169 | -0.0028 | +0.0372 | n/a | -5.22% | 0/3 |
| d_Institutional Ownership | +0.0167 | -0.0470 | +0.0708 | 0.20% | -3.37% | 15/33 |
| d_Relative Volume | +0.0163 | -0.0444 | +0.0427 | 2.12% | 1.00% | 5882/5467 |
| d_Volatility (Month) | -0.0153 | +0.0002 | +0.0320 | -0.02% | -0.99% | 34/4 |

## Combinations

| Pattern | n | Mean long fwd | Hit up |
|---|---|---|---|
| true_ret>3% & DOWNTREND | 306 | 4.24% | 36.6% |
| true_ret>3% & UPTREND | 318 | 0.30% | 44.0% |
| true_ret>3% & MIXED | 190 | 0.08% | 39.5% |

## Risk dominance probes

| State | n | Mean long fwd | Mean fwd if score top quintile |
|---|---|---|---|
| EXTENDED | 186 | -0.20% | -0.42% |
| WASHED | 2312 | 3.00% | -0.56% |

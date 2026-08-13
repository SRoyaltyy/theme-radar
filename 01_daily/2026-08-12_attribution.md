# Factor attribution — signal 2026-08-12 → prediction day 2026-08-13

## Trade window (read this first)

| Role | Date | Meaning |
|------|------|---------|
| **Signal as-of** | **2026-08-12** | Features/scores formed from this snapshot (and deltas vs **2026-08-11**). Only data on/before this date. |
| **Prediction day** | **2026-08-13** | The trading day the forward return is for (exit snapshot). |
| **Entry price** | Price @ 2026-08-12 | Long: buy here; short: sell here. |
| **Exit price** | Price @ 2026-08-13 | Close proxy on prediction day. |
| **Return column** | `fwd_1d` | Long: exit/entry − 1; short = opposite. |

Graded **n=11553** names with valid entry and exit prices.

Provisional until multiple signal dates agree.

_Column guide: **IC** = Spearman(feature, long forward return); **IC↑** / **IC↓** = IC among names that went up / down._

## Score calibration (long fwd)
- Spearman IC(total_score, fwd_1d) = **-0.0472**

| Quintile | Mean long fwd | Hit up>1.5% | n |
|---|---|---|---|
| 1 | 1.41% | 30.1% | 2331 |
| 2 | 0.59% | 11.7% | 3052 |
| 3 | 0.49% | 9.9% | 1646 |
| 4 | 0.53% | 12.0% | 2357 |
| 5 | 1.29% | 27.5% | 2167 |

## Top |IC| features

| Feature | IC | IC↑ | IC↓ | Mean fwd when + | Mean fwd when − | n+/n− |
|---|---|---|---|---|---|---|
| d_Forward P/E | -0.0866 | -0.1060 | -0.0786 | 0.58% | 1.01% | 1625/1342 |
| Performance (Week) | -0.0778 | +0.0426 | -0.1228 | 0.55% | 1.42% | 7242/4092 |
| d_Performance (Week) | +0.0733 | +0.1220 | +0.0045 | 0.72% | 1.15% | 7139/4148 |
| d_Performance (Quarter) | +0.0690 | +0.1243 | -0.0421 | 0.79% | 1.12% | 7476/3310 |
| d_Market Cap | -0.0679 | -0.0998 | -0.0225 | 1.30% | 1.41% | 3033/2655 |
| upside_pct_lvl | -0.0548 | +0.3371 | -0.3655 | 0.99% | 0.70% | 4291/354 |
| d_Short Float | -0.0503 | -0.0476 | -0.0087 | 1.98% | 0.94% | 2401/3102 |
| Performance (Month) | -0.0494 | -0.0185 | -0.0307 | 0.57% | 1.34% | 6922/4388 |
| Institutional Transactions | -0.0474 | -0.0143 | -0.0733 | 1.17% | 1.70% | 2521/2519 |
| Short Float | +0.0429 | +0.2496 | -0.1606 | 1.30% | n/a | 5703/0 |
| Relative Strength Index (14) | -0.0412 | -0.1890 | +0.1299 | 0.86% | n/a | 11440/0 |
| d_50-Day Simple Moving Average | -0.0398 | +0.0055 | -0.1061 | 0.92% | 0.78% | 7261/4158 |
| d_Relative Strength Index (14) | -0.0396 | -0.1863 | +0.0226 | 0.71% | 1.19% | 7161/3947 |
| d_Beta | +0.0376 | +0.0116 | +0.0560 | 1.07% | 3.33% | 1993/1249 |
| true_ret | -0.0371 | -0.0164 | -0.0752 | 0.71% | 1.10% | 7106/3868 |
| d_Performance (YTD) | -0.0360 | -0.0257 | -0.0657 | 0.71% | 1.18% | 7199/3939 |
| d_200-Day Simple Moving Average | -0.0303 | +0.0055 | -0.0868 | 0.72% | 1.14% | 7331/4064 |
| d_Profit Margin | +0.0238 | -0.0060 | +0.0087 | 0.72% | -0.11% | 133/106 |
| Relative Volume | +0.0229 | +0.1238 | -0.1281 | 0.88% | n/a | 11262/0 |
| d_Institutional Ownership | +0.0205 | -0.0451 | +0.0325 | 0.61% | 0.53% | 2139/1545 |
| d_Sales Year Over Year TTM | +0.0177 | -0.0037 | -0.0023 | 0.81% | 0.10% | 109/93 |
| d_Short Ratio | -0.0175 | -0.0102 | -0.0246 | 1.15% | 0.63% | 5143/5844 |
| d_20-Day Simple Moving Average | -0.0164 | -0.0053 | -0.0477 | 0.77% | 1.03% | 6995/4431 |
| d_Price | -0.0149 | -0.0757 | -0.0072 | 0.71% | 1.10% | 7106/3868 |
| d_Volatility (Month) | +0.0141 | -0.0571 | +0.0284 | 1.90% | 0.44% | 3456/5824 |

## Combinations

| Pattern | n | Mean long fwd | Hit up |
|---|---|---|---|
| true_ret>3% & DOWNTREND | 383 | 6.60% | 37.3% |
| true_ret>3% & UPTREND | 377 | -0.36% | 32.4% |
| true_ret>3% & MIXED | 296 | 3.10% | 37.5% |

## Risk dominance probes

| State | n | Mean long fwd | Mean fwd if score top quintile |
|---|---|---|---|
| EXTENDED | 326 | -0.05% | -1.28% |
| WASHED | 546 | 5.17% | 0.14% |

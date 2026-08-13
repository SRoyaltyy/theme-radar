# Factor attribution — signal 2026-08-11 → prediction day 2026-08-13

## Trade window (read this first)

| Role | Date | Meaning |
|------|------|---------|
| **Signal as-of** | **2026-08-11** | Features/scores formed from this snapshot (and deltas vs **2026-08-10**). Only data on/before this date. |
| **Prediction day** | **2026-08-13** | The trading day the forward return is for (exit snapshot). |
| **Entry price** | Price @ 2026-08-11 | Long: buy here; short: sell here. |
| **Exit price** | Price @ 2026-08-13 | Close proxy on prediction day. |
| **Return column** | `fwd_2d` | Long: exit/entry − 1; short = opposite. |

Graded **n=11543** names with valid entry and exit prices.

Provisional until multiple signal dates agree.

_Column guide: **IC** = Spearman(feature, long forward return); **IC↑** / **IC↓** = IC among names that went up / down._

## Score calibration (long fwd)
- Spearman IC(total_score, fwd_2d) = **0.0174**

| Quintile | Mean long fwd | Hit up>1.5% | n |
|---|---|---|---|
| 1 | 2.16% | 34.8% | 2347 |
| 2 | 0.61% | 13.6% | 3055 |
| 3 | 0.60% | 12.9% | 1944 |
| 4 | 1.64% | 34.9% | 2049 |
| 5 | 1.35% | 36.5% | 2148 |

## Top |IC| features

| Feature | IC | IC↑ | IC↓ | Mean fwd when + | Mean fwd when − | n+/n− |
|---|---|---|---|---|---|---|
| Performance (Week) | -0.1570 | -0.1363 | -0.0553 | 0.63% | 1.95% | 6032/5301 |
| d_Performance (Week) | -0.1569 | -0.3244 | +0.0544 | 0.72% | 1.43% | 2858/8494 |
| d_Beta | -0.0960 | -0.0939 | -0.0447 | 0.84% | 1.97% | 1463/1965 |
| d_Forward P/E | -0.0803 | -0.0856 | +0.0073 | 0.70% | 1.49% | 1665/1316 |
| upside_pct_lvl | -0.0707 | +0.3028 | -0.3460 | 1.24% | 0.65% | 4278/370 |
| Performance (Month) | -0.0675 | -0.0442 | +0.0278 | 0.66% | 2.14% | 6985/4304 |
| Relative Strength Index (14) | -0.0603 | -0.1800 | +0.1757 | 1.24% | n/a | 11436/0 |
| Short Float | +0.0551 | +0.2644 | -0.1641 | 1.54% | n/a | 5696/0 |
| d_Performance (Month) | +0.0452 | +0.2054 | -0.1317 | 1.19% | 1.33% | 7758/3463 |
| d_Volatility (Month) | -0.0413 | +0.0166 | -0.0539 | 1.19% | 1.53% | 4698/4534 |
| d_Average Volume | -0.0411 | -0.0586 | -0.0222 | 1.49% | 1.01% | 5279/5704 |
| d_Market Cap | -0.0368 | -0.0568 | +0.0450 | 0.84% | 2.43% | 3183/2513 |
| d_Sales Growth Quarter Over Quarter | -0.0362 | -0.0179 | -0.0405 | -0.18% | 1.69% | 89/103 |
| d_Institutional Ownership | +0.0333 | +0.0003 | +0.0277 | 1.24% | 0.27% | 182/349 |
| d_Sales Year Over Year TTM | -0.0211 | -0.0249 | +0.0199 | 0.19% | 0.95% | 92/95 |
| d_Relative Strength Index (14) | -0.0184 | -0.0138 | -0.0274 | 0.95% | 1.66% | 5980/5049 |
| d_200-Day Simple Moving Average | -0.0168 | +0.0356 | -0.0613 | 1.03% | 1.51% | 5980/5374 |
| Relative Volume | +0.0147 | +0.0698 | -0.0372 | 1.26% | n/a | 11273/0 |
| d_Gross Margin | -0.0125 | +0.0157 | -0.0135 | 0.85% | 0.57% | 90/103 |
| d_50-Day Simple Moving Average | -0.0122 | +0.0545 | -0.0840 | 1.11% | 1.42% | 6070/5310 |
| d_20-Day Simple Moving Average | +0.0114 | +0.0445 | -0.0618 | 1.19% | 1.32% | 5731/5661 |
| d_Price | +0.0112 | +0.0211 | -0.0099 | 0.98% | 1.51% | 5857/4933 |
| d_Short Ratio | +0.0110 | +0.0479 | -0.0088 | 0.93% | 1.02% | 3581/3162 |
| true_ret | -0.0075 | +0.0289 | -0.0473 | 0.98% | 1.51% | 5857/4933 |
| d_Analyst Recom | +0.0073 | -0.0008 | -0.0159 | 1.44% | 1.68% | 68/75 |

## Combinations

| Pattern | n | Mean long fwd | Hit up |
|---|---|---|---|
| true_ret>3% & DOWNTREND | 409 | 5.46% | 44.7% |
| true_ret>3% & UPTREND | 300 | -0.44% | 37.0% |
| true_ret>3% & MIXED | 257 | 0.06% | 37.7% |

## Risk dominance probes

| State | n | Mean long fwd | Mean fwd if score top quintile |
|---|---|---|---|
| EXTENDED | 313 | -0.28% | -1.49% |
| WASHED | 558 | 5.84% | 10.69% |

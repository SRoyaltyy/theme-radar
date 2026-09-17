# Factor attribution — signal 2026-09-16 → prediction day 2026-09-17

## Trade window (read this first)

| Role | Date | Meaning |
|------|------|---------|
| **Signal as-of** | **2026-09-16** | Features/scores formed from this snapshot (and deltas vs **2026-09-15**). Only data on/before this date. |
| **Prediction day** | **2026-09-17** | The trading day the forward return is for (exit snapshot). |
| **Entry price** | Price @ 2026-09-16 | Long: buy here; short: sell here. |
| **Exit price** | Price @ 2026-09-17 | Close proxy on prediction day. |
| **Return column** | `fwd_1d` | Long: exit/entry − 1; short = opposite. |

Graded **n=11627** names with valid entry and exit prices.

Provisional until multiple signal dates agree.

_Column guide: **IC** = Spearman(feature, long forward return); **IC↑** / **IC↓** = IC among names that went up / down._

## Score calibration (long fwd)
- Spearman IC(total_score, fwd_1d) = **-0.0722**

| Quintile | Mean long fwd | Hit up>1.5% | n |
|---|---|---|---|
| 1 | 1.63% | 30.5% | 2932 |
| 2 | 0.94% | 17.7% | 2856 |
| 3 | 0.94% | 25.0% | 1218 |
| 4 | 0.96% | 26.5% | 2401 |
| 5 | 4.14% | 38.5% | 2220 |

## Top |IC| features

| Feature | IC | IC↑ | IC↓ | Mean fwd when + | Mean fwd when − | n+/n− |
|---|---|---|---|---|---|---|
| Performance (Week) | -0.3108 | -0.4039 | -0.0155 | 1.28% | 1.87% | 2444/9005 |
| upside_pct_lvl | +0.1608 | +0.3987 | -0.3562 | 1.49% | 1.21% | 4379/262 |
| d_Performance (Quarter) | +0.1527 | +0.1869 | -0.0279 | 2.80% | 0.83% | 4853/6043 |
| Performance (Month) | -0.1370 | -0.2448 | +0.0857 | 2.01% | 1.66% | 2683/8751 |
| d_Performance (Month) | -0.1026 | -0.0518 | -0.1459 | 2.14% | 1.40% | 5494/5792 |
| d_Average Volume | -0.0744 | -0.1348 | +0.0090 | 2.31% | 1.33% | 4953/6088 |
| d_Performance (Week) | +0.0687 | +0.1376 | -0.1024 | 1.68% | 1.88% | 7117/4251 |
| d_Short Ratio | +0.0661 | +0.1052 | -0.0144 | 1.30% | 1.22% | 4080/3272 |
| d_Relative Strength Index (14) | +0.0582 | +0.1623 | -0.1202 | 2.99% | 1.17% | 3701/7451 |
| d_Forward P/E | +0.0532 | +0.0977 | -0.0389 | 0.76% | 0.60% | 1047/1883 |
| d_Market Cap | +0.0525 | +0.1173 | -0.1091 | 4.03% | 1.28% | 2115/3546 |
| Institutional Transactions | +0.0499 | +0.0912 | -0.0723 | 2.62% | 2.35% | 3210/1829 |
| Relative Volume | -0.0441 | -0.0045 | -0.0505 | 1.76% | n/a | 11384/0 |
| d_Price | +0.0422 | +0.0998 | -0.1130 | 2.28% | 1.17% | 3606/7357 |
| d_Profit Margin | +0.0421 | +0.0334 | -0.0238 | 5.12% | -0.89% | 6/4 |
| d_Beta | +0.0405 | +0.0939 | -0.0835 | 4.42% | 1.24% | 2346/1208 |
| Short Float | +0.0364 | +0.2199 | -0.1179 | 1.82% | n/a | 5705/0 |
| d_Volatility (Month) | -0.0363 | -0.0417 | +0.0081 | 2.36% | 1.57% | 5064/4079 |
| d_Insider Transactions | +0.0325 | +0.0472 | -0.0246 | 2.35% | 0.90% | 145/322 |
| d_Target Price | +0.0311 | +0.0173 | +0.0240 | 1.32% | 0.67% | 142/150 |
| d_Sales Growth Quarter Over Quarter | +0.0305 | +0.0271 | +0.0066 | 5.21% | 1.33% | 5/5 |
| d_Relative Volume | +0.0269 | +0.0542 | -0.0872 | 2.31% | 1.08% | 5869/5340 |
| d_20-Day Simple Moving Average | +0.0254 | +0.0185 | -0.0346 | 2.68% | 1.11% | 4628/6873 |
| d_Performance (YTD) | +0.0192 | +0.0172 | -0.0606 | 3.01% | 1.17% | 3682/7452 |
| d_Institutional Ownership | -0.0187 | -0.0252 | +0.0077 | 254.40% | 78.94% | 11/31 |

## Combinations

| Pattern | n | Mean long fwd | Hit up |
|---|---|---|---|
| true_ret>3% & DOWNTREND | 299 | 13.77% | 52.2% |
| true_ret>3% & UPTREND | 161 | 3.86% | 57.1% |
| true_ret>3% & MIXED | 126 | 1.01% | 45.2% |

## Risk dominance probes

| State | n | Mean long fwd | Mean fwd if score top quintile |
|---|---|---|---|
| EXTENDED | 122 | 4.83% | 6.60% |
| WASHED | 2001 | 3.60% | 10.71% |

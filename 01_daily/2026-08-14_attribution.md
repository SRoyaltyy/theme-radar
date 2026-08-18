# Factor attribution — signal 2026-08-14 → prediction day 2026-08-18

## Trade window (read this first)

| Role | Date | Meaning |
|------|------|---------|
| **Signal as-of** | **2026-08-14** | Features/scores formed from this snapshot (and deltas vs **2026-08-13**). Only data on/before this date. |
| **Prediction day** | **2026-08-18** | The trading day the forward return is for (exit snapshot). |
| **Entry price** | Price @ 2026-08-14 | Long: buy here; short: sell here. |
| **Exit price** | Price @ 2026-08-18 | Close proxy on prediction day. |
| **Return column** | `fwd_2d` | Long: exit/entry − 1; short = opposite. |

Graded **n=11549** names with valid entry and exit prices.

Provisional until multiple signal dates agree.

_Column guide: **IC** = Spearman(feature, long forward return); **IC↑** / **IC↓** = IC among names that went up / down._

## Score calibration (long fwd)
- Spearman IC(total_score, fwd_2d) = **-0.1560**

| Quintile | Mean long fwd | Hit up>1.5% | n |
|---|---|---|---|
| 1 | 1.82% | 16.0% | 2326 |
| 2 | 0.11% | 6.1% | 2553 |
| 3 | 3.62% | 5.2% | 2399 |
| 4 | -1.36% | 11.1% | 1996 |
| 5 | -2.44% | 16.1% | 2275 |

## Top |IC| features

| Feature | IC | IC↑ | IC↓ | Mean fwd when + | Mean fwd when − | n+/n− |
|---|---|---|---|---|---|---|
| d_Performance (Month) | -0.1822 | +0.1234 | -0.2749 | -1.60% | 3.10% | 6304/4932 |
| Short Float | -0.1624 | +0.1848 | -0.2489 | 2.17% | n/a | 5688/0 |
| d_Performance (Week) | +0.1390 | -0.0224 | +0.1621 | 2.07% | -0.22% | 3303/8002 |
| Performance (Month) | -0.1359 | -0.0245 | -0.1458 | -1.55% | 4.00% | 7233/4097 |
| d_Volatility (Month) | +0.1224 | -0.0154 | +0.1652 | 4.64% | -1.56% | 3383/6024 |
| Performance (Week) | -0.0985 | +0.0076 | -0.1332 | -1.40% | 3.62% | 7149/4183 |
| upside_pct_lvl | -0.0859 | +0.3957 | -0.3580 | 1.94% | -1.43% | 4275/367 |
| d_Forward P/E | -0.0807 | +0.0393 | -0.1189 | -1.83% | -1.48% | 1582/1351 |
| d_Performance (Quarter) | +0.0702 | +0.0280 | +0.0523 | 1.92% | -0.20% | 4236/6510 |
| d_50-Day Simple Moving Average | -0.0601 | +0.0283 | -0.1163 | -1.61% | 2.11% | 5102/6272 |
| d_Relative Strength Index (14) | -0.0576 | +0.0120 | -0.1696 | -1.44% | 2.27% | 5300/5731 |
| d_Beta | -0.0570 | -0.0524 | -0.0238 | 1.38% | 4.90% | 1960/2166 |
| Relative Volume | -0.0424 | +0.0769 | -0.0702 | 0.44% | n/a | 11264/0 |
| true_ret | -0.0394 | +0.0053 | -0.0753 | -1.49% | -0.06% | 5168/5660 |
| d_Sales Year Over Year TTM | +0.0381 | +0.0468 | +0.0282 | -1.61% | -2.22% | 106/106 |
| d_Average Volume | +0.0378 | +0.0362 | +0.0702 | 2.93% | -1.31% | 4662/6316 |
| d_Short Ratio | -0.0356 | -0.0189 | -0.0552 | -1.30% | 3.65% | 4025/2720 |
| d_Performance (YTD) | -0.0350 | +0.0049 | -0.0752 | -1.48% | 2.25% | 5289/5751 |
| d_Price | -0.0350 | +0.0024 | -0.0867 | -1.49% | -0.06% | 5168/5660 |
| d_200-Day Simple Moving Average | -0.0312 | +0.0416 | -0.0902 | -1.48% | 2.06% | 5176/6185 |
| d_Market Cap | -0.0230 | +0.0186 | -0.0418 | -1.33% | 5.98% | 2949/2725 |
| d_Short Float | +0.0222 | -0.0449 | +0.0540 | -0.95% | -1.66% | 82/270 |
| d_Analyst Recom | +0.0164 | -0.0244 | +0.0284 | -1.43% | -2.11% | 132/89 |
| d_Sales Growth Quarter Over Quarter | +0.0156 | -0.0299 | +0.0190 | -2.94% | -1.85% | 107/120 |
| d_Total Debt/Equity | -0.0150 | -0.0032 | -0.0198 | -2.27% | -0.50% | 119/113 |

## Combinations

| Pattern | n | Mean long fwd | Hit up |
|---|---|---|---|
| true_ret>3% & DOWNTREND | 333 | -1.58% | 21.3% |
| true_ret>3% & UPTREND | 317 | -3.63% | 21.5% |
| true_ret>3% & MIXED | 249 | -3.88% | 14.1% |

## Risk dominance probes

| State | n | Mean long fwd | Mean fwd if score top quintile |
|---|---|---|---|
| EXTENDED | 378 | -2.26% | -1.73% |
| WASHED | 447 | 34.70% | -3.61% |

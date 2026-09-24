# Factor attribution — signal 2026-09-21 → prediction day 2026-09-24

## Trade window (read this first)

| Role | Date | Meaning |
|------|------|---------|
| **Signal as-of** | **2026-09-21** | Features/scores formed from this snapshot (and deltas vs **2026-09-18**). Only data on/before this date. |
| **Prediction day** | **2026-09-24** | The trading day the forward return is for (exit snapshot). |
| **Entry price** | Price @ 2026-09-21 | Long: buy here; short: sell here. |
| **Exit price** | Price @ 2026-09-24 | Close proxy on prediction day. |
| **Return column** | `fwd_3d` | Long: exit/entry − 1; short = opposite. |

Graded **n=11627** names with valid entry and exit prices.

Provisional until multiple signal dates agree.

_Column guide: **IC** = Spearman(feature, long forward return); **IC↑** / **IC↓** = IC among names that went up / down._

## Score calibration (long fwd)
- Spearman IC(total_score, fwd_3d) = **-0.0110**

| Quintile | Mean long fwd | Hit up>1.5% | n |
|---|---|---|---|
| 1 | 0.34% | 16.6% | 2369 |
| 2 | -1.19% | 7.0% | 2285 |
| 3 | -1.08% | 7.5% | 2520 |
| 4 | -1.32% | 10.3% | 2234 |
| 5 | -0.05% | 18.3% | 2219 |

## Top |IC| features

| Feature | IC | IC↑ | IC↓ | Mean fwd when + | Mean fwd when − | n+/n− |
|---|---|---|---|---|---|---|
| Relative Strength Index (14) | +0.1839 | -0.1505 | +0.1734 | -0.66% | n/a | 11544/0 |
| upside_pct_lvl | -0.1500 | +0.2425 | -0.3435 | -1.42% | -0.30% | 4352/282 |
| Performance (Month) | +0.1333 | -0.0967 | +0.2365 | -0.45% | -0.79% | 4295/7150 |
| Performance (Week) | +0.1058 | +0.0498 | +0.1410 | -0.48% | -0.86% | 6054/5376 |
| d_Forward P/E | +0.0901 | +0.1510 | -0.0408 | -1.08% | -1.55% | 1652/1284 |
| Short Float | -0.0785 | +0.1690 | -0.1642 | -0.68% | n/a | 5700/0 |
| Relative Volume | -0.0710 | +0.0481 | -0.0941 | -0.67% | n/a | 11433/0 |
| d_Performance (Week) | -0.0576 | +0.0284 | -0.0468 | -0.84% | -0.30% | 7866/3574 |
| d_20-Day Simple Moving Average | -0.0468 | +0.0891 | -0.0571 | -0.82% | -0.25% | 8362/3185 |
| d_Relative Volume | +0.0462 | -0.0484 | +0.1537 | -0.42% | -0.81% | 4478/6842 |
| d_Market Cap | +0.0440 | +0.0297 | -0.0003 | -0.74% | -0.55% | 3169/2552 |
| Institutional Transactions | -0.0376 | +0.1012 | -0.0609 | -0.62% | -1.60% | 3221/1808 |
| d_Average Volume | -0.0365 | +0.0596 | -0.0559 | -0.36% | -0.91% | 5454/5633 |
| d_50-Day Simple Moving Average | -0.0363 | +0.0767 | -0.0318 | -0.81% | -0.33% | 8011/3527 |
| d_Sales Growth Quarter Over Quarter | +0.0322 | +0.0637 | +0.0244 | 5.67% | -1.79% | 6/3 |
| d_Sales Year Over Year TTM | +0.0318 | +0.0123 | +0.0349 | 5.09% | -1.33% | 5/2 |
| d_Performance (Month) | -0.0307 | +0.0847 | -0.0523 | -0.81% | -0.30% | 8183/3184 |
| d_Target Price | +0.0261 | +0.0738 | -0.0161 | -1.38% | -2.09% | 162/223 |
| d_Performance (Quarter) | -0.0238 | +0.0897 | -0.0259 | -0.67% | -0.60% | 7364/3587 |
| d_Profit Margin | -0.0235 | -0.0075 | -0.0061 | 3.65% | 4.70% | 4/7 |
| true_ret | -0.0222 | +0.0486 | +0.0003 | -0.82% | -0.36% | 7647/3531 |
| d_Short Ratio | +0.0219 | -0.0126 | +0.0363 | -0.94% | -0.34% | 3673/3767 |
| d_Price | +0.0182 | -0.0010 | +0.1160 | -0.82% | -0.36% | 7647/3531 |
| d_Institutional Ownership | +0.0181 | -0.0176 | +0.0170 | -1.83% | -1.81% | 163/177 |
| d_Relative Strength Index (14) | +0.0180 | -0.0432 | +0.2506 | -0.80% | -0.36% | 7700/3579 |

## Combinations

| Pattern | n | Mean long fwd | Hit up |
|---|---|---|---|
| true_ret>3% & DOWNTREND | 538 | 1.97% | 23.4% |
| true_ret>3% & UPTREND | 724 | -0.30% | 23.6% |
| true_ret>3% & MIXED | 296 | 1.12% | 23.6% |

## Risk dominance probes

| State | n | Mean long fwd | Mean fwd if score top quintile |
|---|---|---|---|
| EXTENDED | 236 | 1.09% | 5.18% |
| WASHED | 1114 | 1.96% | 6.50% |

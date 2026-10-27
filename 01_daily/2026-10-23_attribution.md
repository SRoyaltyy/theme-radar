# Factor attribution — signal 2026-10-23 → prediction day 2026-10-26

## Trade window (read this first)

| Role | Date | Meaning |
|------|------|---------|
| **Signal as-of** | **2026-10-23** | Features/scores formed from this snapshot (and deltas vs **2026-10-22**). Only data on/before this date. |
| **Prediction day** | **2026-10-26** | The trading day the forward return is for (exit snapshot). |
| **Entry price** | Price @ 2026-10-23 | Long: buy here; short: sell here. |
| **Exit price** | Price @ 2026-10-26 | Close proxy on prediction day. |
| **Return column** | `fwd_1d` | Long: exit/entry − 1; short = opposite. |

Graded **n=11747** names with valid entry and exit prices.

Provisional until multiple signal dates agree.

_Column guide: **IC** = Spearman(feature, long forward return); **IC↑** / **IC↓** = IC among names that went up / down._

## Score calibration (long fwd)
- Spearman IC(total_score, fwd_1d) = **0.0067**

| Quintile | Mean long fwd | Hit up>1.5% | n |
|---|---|---|---|
| 1 | 4.06% | 16.0% | 2764 |
| 2 | 5.64% | 10.9% | 2050 |
| 3 | 1.69% | 10.6% | 2282 |
| 4 | 0.44% | 12.3% | 2306 |
| 5 | 0.46% | 23.4% | 2345 |

## Top |IC| features

| Feature | IC | IC↑ | IC↓ | Mean fwd when + | Mean fwd when − | n+/n− |
|---|---|---|---|---|---|---|
| upside_pct_lvl | -0.1221 | +0.3673 | -0.4466 | 1.34% | -0.32% | 4290/341 |
| d_Performance (Quarter) | +0.1203 | +0.0390 | +0.0998 | 0.55% | 3.48% | 3461/7697 |
| d_Volatility (Month) | +0.1026 | +0.2568 | -0.0080 | 3.08% | 0.45% | 5808/4030 |
| d_Forward P/E | +0.0889 | +0.0426 | -0.0127 | -0.08% | 0.03% | 1123/1821 |
| Relative Strength Index (14) | -0.0783 | -0.3404 | +0.2783 | 2.47% | n/a | 11657/0 |
| Relative Volume | +0.0670 | +0.0803 | +0.0775 | 2.52% | n/a | 11390/0 |
| Performance (Week) | -0.0588 | -0.2174 | +0.1510 | -0.20% | 5.10% | 5685/5867 |
| d_Performance (Week) | +0.0566 | +0.3074 | -0.2349 | 1.88% | 3.43% | 6882/4617 |
| d_50-Day Simple Moving Average | +0.0543 | +0.0511 | +0.0380 | 1.01% | 3.40% | 4449/7126 |
| Short Float | -0.0493 | +0.1250 | -0.0803 | 4.34% | n/a | 5654/0 |
| d_Average Volume | +0.0440 | +0.0814 | +0.0077 | 3.88% | 0.50% | 6847/4189 |
| d_20-Day Simple Moving Average | +0.0410 | +0.1088 | -0.0494 | 0.89% | 3.54% | 4599/6974 |
| d_Short Ratio | -0.0374 | -0.0731 | -0.0310 | -0.17% | 0.83% | 2542/4490 |
| true_ret | +0.0360 | -0.0225 | +0.0851 | 0.36% | 3.33% | 3692/7402 |
| d_Institutional Ownership | +0.0351 | +0.0009 | +0.0317 | 0.36% | 1.28% | 991/902 |
| d_Relative Volume | -0.0323 | -0.0507 | -0.0456 | 0.96% | 3.51% | 4138/7126 |
| Performance (Month) | -0.0320 | -0.3867 | +0.3319 | -0.18% | 4.22% | 4525/7026 |
| d_Profit Margin | +0.0240 | +0.0219 | -0.0205 | 0.67% | 0.84% | 78/49 |
| d_Price | -0.0235 | +0.0790 | -0.0325 | 0.36% | 3.33% | 3692/7402 |
| d_Beta | +0.0231 | +0.2986 | -0.2514 | 8.55% | -0.18% | 3321/2541 |
| d_Performance (Month) | +0.0204 | -0.0100 | +0.0498 | 2.85% | 2.21% | 5530/5899 |
| d_Analyst Recom | -0.0174 | -0.0373 | +0.0320 | -0.38% | 0.50% | 96/66 |
| d_Performance (YTD) | +0.0159 | +0.0055 | +0.0267 | 0.91% | 2.08% | 3782/7482 |
| d_Market Cap | +0.0157 | +0.0841 | -0.1204 | 0.36% | 6.98% | 2181/3524 |
| d_200-Day Simple Moving Average | +0.0143 | +0.0162 | +0.0100 | 2.94% | 2.12% | 4042/7527 |

## Combinations

| Pattern | n | Mean long fwd | Hit up |
|---|---|---|---|
| true_ret>3% & DOWNTREND | 390 | 1.91% | 36.7% |
| true_ret>3% & UPTREND | 231 | -1.34% | 38.1% |
| true_ret>3% & MIXED | 132 | 0.17% | 41.7% |

## Risk dominance probes

| State | n | Mean long fwd | Mean fwd if score top quintile |
|---|---|---|---|
| EXTENDED | 194 | -0.43% | 0.14% |
| WASHED | 1767 | 14.37% | 4.35% |

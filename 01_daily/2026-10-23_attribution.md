# Factor attribution — signal 2026-10-23 → prediction day 2026-10-27

## Trade window (read this first)

| Role | Date | Meaning |
|------|------|---------|
| **Signal as-of** | **2026-10-23** | Features/scores formed from this snapshot (and deltas vs **2026-10-22**). Only data on/before this date. |
| **Prediction day** | **2026-10-27** | The trading day the forward return is for (exit snapshot). |
| **Entry price** | Price @ 2026-10-23 | Long: buy here; short: sell here. |
| **Exit price** | Price @ 2026-10-27 | Close proxy on prediction day. |
| **Return column** | `fwd_2d` | Long: exit/entry − 1; short = opposite. |

Graded **n=11746** names with valid entry and exit prices.

Provisional until multiple signal dates agree.

_Column guide: **IC** = Spearman(feature, long forward return); **IC↑** / **IC↓** = IC among names that went up / down._

## Score calibration (long fwd)
- Spearman IC(total_score, fwd_2d) = **-0.0839**

| Quintile | Mean long fwd | Hit up>1.5% | n |
|---|---|---|---|
| 1 | 7.25% | 38.3% | 2763 |
| 2 | 6.59% | 35.1% | 2050 |
| 3 | 2.36% | 20.3% | 2282 |
| 4 | 1.18% | 22.4% | 2306 |
| 5 | 1.51% | 36.3% | 2345 |

## Top |IC| features

| Feature | IC | IC↑ | IC↓ | Mean fwd when + | Mean fwd when − | n+/n− |
|---|---|---|---|---|---|---|
| Relative Strength Index (14) | -0.3549 | -0.4873 | +0.2076 | 3.88% | n/a | 11656/0 |
| Performance (Month) | -0.3282 | -0.5695 | +0.1334 | -0.32% | 6.64% | 4525/7025 |
| d_Beta | +0.2726 | +0.4519 | -0.1125 | 12.01% | -0.30% | 3321/2541 |
| d_Performance (Week) | +0.2300 | +0.3985 | -0.1149 | 3.29% | 4.90% | 6881/4617 |
| Performance (Week) | -0.1983 | -0.2885 | +0.0661 | 0.29% | 7.42% | 5685/5866 |
| upside_pct_lvl | +0.1734 | +0.4437 | -0.2788 | 3.75% | -0.74% | 4289/341 |
| Short Float | +0.1055 | +0.2951 | -0.0195 | 6.18% | n/a | 5653/0 |
| Institutional Transactions | +0.0993 | +0.1267 | -0.0040 | 5.12% | 11.68% | 3254/1788 |
| d_Volatility (Month) | +0.0784 | +0.2450 | -0.0685 | 4.57% | 2.17% | 5807/4030 |
| d_20-Day Simple Moving Average | +0.0760 | +0.1135 | -0.0217 | 2.34% | 4.93% | 4599/6973 |
| d_Relative Volume | -0.0625 | -0.0731 | -0.0198 | 3.14% | 4.52% | 4137/7126 |
| d_Performance (Quarter) | +0.0609 | -0.0210 | +0.0712 | 2.23% | 4.78% | 3461/7696 |
| Relative Volume | +0.0464 | +0.0574 | +0.0263 | 3.96% | n/a | 11389/0 |
| d_Analyst Recom | -0.0417 | -0.0381 | +0.0281 | -0.55% | 1.36% | 96/66 |
| d_Short Ratio | -0.0380 | -0.0636 | -0.0148 | 1.38% | 2.16% | 2542/4489 |
| d_Average Volume | +0.0375 | +0.0700 | -0.0179 | 5.32% | 1.99% | 6846/4189 |
| d_Performance (YTD) | -0.0370 | -0.0530 | +0.0014 | 2.08% | 3.67% | 3782/7481 |
| d_Forward P/E | +0.0367 | +0.0495 | -0.0246 | 0.62% | 0.64% | 1123/1821 |
| d_Relative Strength Index (14) | +0.0339 | +0.2183 | -0.0832 | 2.01% | 5.02% | 3800/7464 |
| d_Price | -0.0303 | +0.0310 | -0.0545 | 1.57% | 4.94% | 3692/7401 |
| d_50-Day Simple Moving Average | +0.0291 | +0.0140 | +0.0211 | 2.27% | 4.92% | 4449/7125 |
| true_ret | -0.0285 | -0.0842 | +0.0536 | 1.57% | 4.94% | 3692/7401 |
| d_200-Day Simple Moving Average | -0.0266 | -0.0333 | -0.0096 | 4.10% | 3.68% | 4042/7526 |
| d_Target Price | -0.0257 | -0.0082 | -0.0024 | 0.57% | 1.26% | 267/248 |
| d_Institutional Ownership | +0.0223 | +0.0122 | +0.0181 | 1.35% | 2.33% | 991/902 |

## Combinations

| Pattern | n | Mean long fwd | Hit up |
|---|---|---|---|
| true_ret>3% & DOWNTREND | 390 | 5.57% | 55.9% |
| true_ret>3% & UPTREND | 231 | -1.10% | 36.8% |
| true_ret>3% & MIXED | 132 | 1.68% | 51.5% |

## Risk dominance probes

| State | n | Mean long fwd | Mean fwd if score top quintile |
|---|---|---|---|
| EXTENDED | 194 | -1.47% | 1.65% |
| WASHED | 1767 | 20.44% | 8.41% |

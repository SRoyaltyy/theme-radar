# Factor attribution — signal 2026-08-19 → prediction day 2026-08-20

## Trade window (read this first)

| Role | Date | Meaning |
|------|------|---------|
| **Signal as-of** | **2026-08-19** | Features/scores formed from this snapshot (and deltas vs **2026-08-18**). Only data on/before this date. |
| **Prediction day** | **2026-08-20** | The trading day the forward return is for (exit snapshot). |
| **Entry price** | Price @ 2026-08-19 | Long: buy here; short: sell here. |
| **Exit price** | Price @ 2026-08-20 | Close proxy on prediction day. |
| **Return column** | `fwd_1d` | Long: exit/entry − 1; short = opposite. |

Graded **n=11587** names with valid entry and exit prices.

Provisional until multiple signal dates agree.

_Column guide: **IC** = Spearman(feature, long forward return); **IC↑** / **IC↓** = IC among names that went up / down._

## Score calibration (long fwd)
- Spearman IC(total_score, fwd_1d) = **0.0108**

| Quintile | Mean long fwd | Hit up>1.5% | n |
|---|---|---|---|
| 1 | -0.78% | 13.3% | 2332 |
| 2 | -0.43% | 6.7% | 2841 |
| 3 | -0.48% | 4.8% | 2294 |
| 4 | -0.33% | 9.7% | 1803 |
| 5 | 0.57% | 21.8% | 2317 |

## Top |IC| features

| Feature | IC | IC↑ | IC↓ | Mean fwd when + | Mean fwd when − | n+/n− |
|---|---|---|---|---|---|---|
| Short Float | -0.1983 | +0.1163 | -0.2775 | -0.43% | n/a | 5669/0 |
| Performance (Week) | +0.1653 | +0.1850 | +0.1317 | 0.25% | -0.78% | 5371/5991 |
| upside_pct_lvl | -0.1348 | +0.3855 | -0.3619 | -0.94% | -0.53% | 4295/354 |
| Relative Strength Index (14) | +0.0855 | -0.0659 | +0.1959 | -0.29% | n/a | 11457/0 |
| d_Performance (Quarter) | -0.0802 | +0.1986 | -0.1961 | -0.22% | -0.53% | 7934/2891 |
| d_Relative Strength Index (14) | +0.0687 | +0.1470 | +0.1511 | -0.06% | -0.75% | 7272/3868 |
| d_Performance (Month) | +0.0608 | +0.1084 | +0.0565 | 0.06% | -0.61% | 5241/6033 |
| Institutional Transactions | -0.0500 | +0.0285 | -0.1071 | -0.84% | 0.08% | 2690/2352 |
| Performance (Month) | -0.0460 | -0.0084 | -0.0628 | -0.24% | -0.39% | 7201/4150 |
| d_Short Float | +0.0441 | -0.0732 | +0.0835 | -1.11% | -1.53% | 213/345 |
| d_Forward P/E | +0.0433 | +0.1523 | -0.0360 | -0.68% | -0.86% | 1657/1316 |
| d_Price | +0.0423 | +0.1328 | +0.0337 | -0.07% | -0.75% | 7196/3831 |
| d_Average Volume | +0.0408 | -0.0138 | +0.0926 | -0.07% | -0.47% | 4491/6523 |
| d_20-Day Simple Moving Average | +0.0385 | +0.2428 | -0.0601 | -0.04% | -0.72% | 7129/4302 |
| d_Relative Volume | +0.0379 | +0.1484 | -0.0414 | -0.03% | -0.60% | 6006/5126 |
| d_Institutional Ownership | -0.0378 | -0.1412 | +0.0267 | -1.02% | -0.93% | 2402/935 |
| d_Short Ratio | -0.0362 | +0.0276 | -0.0892 | -0.58% | -0.60% | 4178/2660 |
| d_200-Day Simple Moving Average | +0.0292 | +0.2238 | -0.0613 | -0.05% | -0.73% | 7295/4129 |
| d_Performance (YTD) | +0.0291 | +0.2011 | -0.0491 | -0.06% | -0.75% | 7285/3896 |
| d_50-Day Simple Moving Average | +0.0274 | +0.2394 | -0.0735 | -0.05% | -0.72% | 7258/4172 |
| d_Volatility (Month) | +0.0268 | -0.0641 | +0.0746 | -0.52% | -0.14% | 3848/5545 |
| true_ret | +0.0258 | +0.2186 | -0.0609 | -0.07% | -0.75% | 7196/3831 |
| d_Beta | +0.0219 | -0.0242 | +0.0699 | -0.35% | 0.15% | 1829/2382 |
| d_Total Debt/Equity | -0.0210 | -0.0093 | -0.0200 | -1.84% | -0.09% | 20/15 |
| d_Target Price | +0.0197 | -0.0203 | -0.0160 | -0.78% | -0.84% | 236/159 |

## Combinations

| Pattern | n | Mean long fwd | Hit up |
|---|---|---|---|
| true_ret>3% & DOWNTREND | 523 | 0.35% | 32.5% |
| true_ret>3% & UPTREND | 682 | -0.68% | 24.9% |
| true_ret>3% & MIXED | 514 | 4.47% | 36.0% |

## Risk dominance probes

| State | n | Mean long fwd | Mean fwd if score top quintile |
|---|---|---|---|
| EXTENDED | 293 | 0.06% | 1.26% |
| WASHED | 544 | -0.44% | -1.53% |

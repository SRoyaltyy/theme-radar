# Factor attribution — signal 2026-09-04 → prediction day 2026-09-09

## Trade window (read this first)

| Role | Date | Meaning |
|------|------|---------|
| **Signal as-of** | **2026-09-04** | Features/scores formed from this snapshot (and deltas vs **2026-09-03**). Only data on/before this date. |
| **Prediction day** | **2026-09-09** | The trading day the forward return is for (exit snapshot). |
| **Entry price** | Price @ 2026-09-04 | Long: buy here; short: sell here. |
| **Exit price** | Price @ 2026-09-09 | Close proxy on prediction day. |
| **Return column** | `fwd_2d` | Long: exit/entry − 1; short = opposite. |

Graded **n=11591** names with valid entry and exit prices.

Provisional until multiple signal dates agree.

_Column guide: **IC** = Spearman(feature, long forward return); **IC↑** / **IC↓** = IC among names that went up / down._

## Score calibration (long fwd)
- Spearman IC(total_score, fwd_2d) = **-0.0659**

| Quintile | Mean long fwd | Hit up>1.5% | n |
|---|---|---|---|
| 1 | 3.29% | 15.2% | 2338 |
| 2 | -0.10% | 7.8% | 2860 |
| 3 | 0.01% | 6.7% | 1766 |
| 4 | -1.27% | 8.0% | 2311 |
| 5 | 0.36% | 19.2% | 2316 |

## Top |IC| features

| Feature | IC | IC↑ | IC↓ | Mean fwd when + | Mean fwd when − | n+/n− |
|---|---|---|---|---|---|---|
| Short Float | -0.2168 | +0.2084 | -0.2656 | 0.99% | n/a | 5675/0 |
| Performance (Week) | +0.0976 | +0.0896 | +0.0602 | -0.23% | 1.22% | 5732/5641 |
| d_Price | +0.0634 | +0.0825 | +0.0088 | -0.28% | 1.03% | 5235/5645 |
| upside_pct_lvl | -0.0569 | +0.3400 | -0.2720 | 1.35% | -2.13% | 4308/335 |
| d_Performance (Week) | +0.0553 | +0.2013 | -0.0746 | 0.10% | 1.20% | 7414/3988 |
| Performance (Month) | +0.0524 | -0.0477 | +0.0401 | -0.81% | 1.84% | 5823/5541 |
| d_Beta | -0.0508 | +0.0638 | -0.0995 | 7.60% | 0.23% | 1559/1207 |
| d_50-Day Simple Moving Average | +0.0476 | +0.1105 | +0.0109 | 0.07% | 0.86% | 5552/5898 |
| d_Short Ratio | -0.0467 | +0.0173 | -0.0717 | -0.89% | 2.48% | 4291/2675 |
| d_Performance (YTD) | +0.0453 | +0.0855 | +0.0127 | 0.03% | 1.00% | 5341/5756 |
| d_200-Day Simple Moving Average | +0.0440 | +0.1071 | +0.0056 | 0.00% | 0.91% | 5416/6022 |
| Relative Volume | -0.0433 | +0.1023 | -0.0582 | 0.47% | n/a | 11309/0 |
| true_ret | +0.0432 | +0.0943 | +0.0164 | -0.28% | 1.03% | 5235/5645 |
| d_Performance (Month) | -0.0395 | +0.0598 | -0.0533 | 0.16% | 0.91% | 6379/4873 |
| d_Average Volume | +0.0387 | -0.0252 | +0.0865 | 2.29% | -0.69% | 4506/6535 |
| d_Relative Strength Index (14) | +0.0354 | +0.0825 | -0.0243 | 0.02% | 1.01% | 5347/5762 |
| d_EPS Surprise | +0.0314 | +0.0141 | -0.0040 | 0.26% | -2.70% | 19/16 |
| Institutional Transactions | +0.0270 | +0.0762 | -0.0362 | -0.06% | 3.71% | 3181/1856 |
| Relative Strength Index (14) | +0.0266 | -0.1513 | +0.0368 | 0.48% | n/a | 11492/0 |
| d_Analyst Recom | +0.0240 | +0.0228 | +0.0218 | -1.00% | -1.96% | 68/50 |
| d_Short Float | -0.0229 | -0.0184 | -0.0115 | -4.33% | -3.05% | 19/28 |
| d_Institutional Ownership | +0.0203 | -0.0469 | -0.0100 | -1.72% | -2.04% | 353/293 |
| d_Forward P/E | +0.0181 | +0.1078 | -0.0190 | -1.85% | -2.08% | 1533/1400 |
| d_Market Cap | -0.0177 | +0.0253 | -0.0427 | -0.45% | 2.19% | 2961/2708 |
| d_20-Day Simple Moving Average | +0.0164 | +0.1088 | -0.0228 | 0.25% | 0.70% | 5851/5593 |

## Combinations

| Pattern | n | Mean long fwd | Hit up |
|---|---|---|---|
| true_ret>3% & DOWNTREND | 366 | 8.03% | 35.0% |
| true_ret>3% & UPTREND | 279 | 2.91% | 30.1% |
| true_ret>3% & MIXED | 235 | 1.17% | 41.7% |

## Risk dominance probes

| State | n | Mean long fwd | Mean fwd if score top quintile |
|---|---|---|---|
| EXTENDED | 242 | -2.18% | -2.65% |
| WASHED | 679 | 13.08% | 13.85% |

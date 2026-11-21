# Factor attribution — signal 2026-11-18 → prediction day 2026-11-20

## Trade window (read this first)

| Role | Date | Meaning |
|------|------|---------|
| **Signal as-of** | **2026-11-18** | Features/scores formed from this snapshot (and deltas vs **2026-11-17**). Only data on/before this date. |
| **Prediction day** | **2026-11-20** | The trading day the forward return is for (exit snapshot). |
| **Entry price** | Price @ 2026-11-18 | Long: buy here; short: sell here. |
| **Exit price** | Price @ 2026-11-20 | Close proxy on prediction day. |
| **Return column** | `fwd_2d` | Long: exit/entry − 1; short = opposite. |

Graded **n=11739** names with valid entry and exit prices.

Provisional until multiple signal dates agree.

_Column guide: **IC** = Spearman(feature, long forward return); **IC↑** / **IC↓** = IC among names that went up / down._

## Score calibration (long fwd)
- Spearman IC(total_score, fwd_2d) = **0.0749**

| Quintile | Mean long fwd | Hit up>1.5% | n |
|---|---|---|---|
| 1 | -3.25% | 4.6% | 2487 |
| 2 | -4.23% | 3.8% | 2220 |
| 3 | -0.95% | 1.6% | 2337 |
| 4 | -3.56% | 5.8% | 2644 |
| 5 | -5.91% | 6.7% | 2051 |

## Top |IC| features

| Feature | IC | IC↑ | IC↓ | Mean fwd when + | Mean fwd when − | n+/n− |
|---|---|---|---|---|---|---|
| Performance (Week) | +0.5567 | -0.0604 | +0.5516 | 0.50% | -4.17% | 1497/10117 |
| Performance (Month) | +0.4573 | -0.0461 | +0.4870 | -1.44% | -4.40% | 3446/8136 |
| upside_pct_lvl | -0.3965 | +0.5654 | -0.5217 | -4.80% | -3.66% | 4388/240 |
| Relative Strength Index (14) | +0.3478 | -0.0609 | +0.2834 | -3.52% | n/a | 11679/0 |
| d_Performance (Week) | +0.3397 | +0.2035 | +0.3071 | -2.76% | -3.96% | 3560/7993 |
| Short Float | -0.2573 | +0.2855 | -0.2347 | -2.43% | n/a | 5612/0 |
| d_20-Day Simple Moving Average | -0.1411 | +0.0734 | -0.1850 | -5.29% | -1.62% | 6171/5423 |
| d_Beta | -0.0786 | +0.0378 | -0.0647 | -1.08% | -4.41% | 3247/2072 |
| Institutional Transactions | -0.0757 | +0.0672 | -0.0967 | -3.21% | -1.27% | 2991/2019 |
| d_Performance (Quarter) | -0.0715 | +0.0655 | -0.0752 | -4.91% | -1.48% | 6643/4615 |
| d_50-Day Simple Moving Average | -0.0637 | +0.0768 | -0.1108 | -4.93% | -2.21% | 5800/5781 |
| d_Forward P/E | -0.0636 | +0.1024 | -0.0649 | -5.29% | -4.80% | 1390/1506 |
| d_Short Float | +0.0619 | -0.0909 | +0.0800 | -6.62% | 6.58% | 17/94 |
| Relative Volume | -0.0526 | +0.1269 | -0.0092 | -3.59% | n/a | 11496/0 |
| d_Analyst Recom | +0.0456 | -0.0556 | +0.0392 | -4.63% | -5.91% | 167/148 |
| d_Institutional Ownership | +0.0437 | -0.1286 | +0.0084 | -3.26% | -2.56% | 1484/2088 |
| d_Target Price | +0.0394 | -0.0007 | +0.0562 | -4.74% | -6.17% | 160/224 |
| d_Volatility (Month) | -0.0389 | +0.1135 | -0.0390 | -3.45% | -3.99% | 5193/4311 |
| d_Market Cap | -0.0377 | +0.0506 | -0.0476 | -4.08% | -1.40% | 2565/3133 |
| true_ret | +0.0328 | +0.0467 | -0.0055 | -5.02% | -3.82% | 4957/6117 |
| d_EPS Surprise | +0.0307 | +0.0159 | +0.0124 | -4.95% | -9.82% | 15/23 |
| d_Profit Margin | +0.0302 | +0.0811 | +0.0132 | 26.36% | -10.97% | 53/49 |
| d_Performance (Month) | +0.0271 | -0.0304 | -0.0667 | -5.52% | -3.34% | 3698/7761 |
| d_Average Volume | +0.0234 | +0.0220 | +0.0006 | -2.47% | -5.06% | 6636/4424 |
| d_Relative Volume | +0.0215 | -0.0153 | +0.0295 | -4.19% | -3.02% | 5255/6070 |

## Combinations

| Pattern | n | Mean long fwd | Hit up |
|---|---|---|---|
| true_ret>3% & DOWNTREND | 463 | -9.35% | 7.8% |
| true_ret>3% & UPTREND | 224 | -3.47% | 15.6% |
| true_ret>3% & MIXED | 207 | -5.13% | 13.0% |

## Risk dominance probes

| State | n | Mean long fwd | Mean fwd if score top quintile |
|---|---|---|---|
| EXTENDED | 172 | 2.74% | 1.15% |
| WASHED | 2065 | -2.06% | -10.71% |

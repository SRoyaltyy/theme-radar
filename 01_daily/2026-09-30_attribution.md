# Factor attribution — signal 2026-09-30 → prediction day 2026-10-02

## Trade window (read this first)

| Role | Date | Meaning |
|------|------|---------|
| **Signal as-of** | **2026-09-30** | Features/scores formed from this snapshot (and deltas vs **2026-09-29**). Only data on/before this date. |
| **Prediction day** | **2026-10-02** | The trading day the forward return is for (exit snapshot). |
| **Entry price** | Price @ 2026-09-30 | Long: buy here; short: sell here. |
| **Exit price** | Price @ 2026-10-02 | Close proxy on prediction day. |
| **Return column** | `fwd_2d` | Long: exit/entry − 1; short = opposite. |

Graded **n=11681** names with valid entry and exit prices.

Provisional until multiple signal dates agree.

_Column guide: **IC** = Spearman(feature, long forward return); **IC↑** / **IC↓** = IC among names that went up / down._

## Score calibration (long fwd)
- Spearman IC(total_score, fwd_2d) = **0.0403**

| Quintile | Mean long fwd | Hit up>1.5% | n |
|---|---|---|---|
| 1 | 0.60% | 24.5% | 2449 |
| 2 | 0.33% | 17.7% | 2616 |
| 3 | 2.20% | 26.1% | 2501 |
| 4 | 0.89% | 24.2% | 1936 |
| 5 | 0.80% | 33.8% | 2179 |

## Top |IC| features

| Feature | IC | IC↑ | IC↓ | Mean fwd when + | Mean fwd when − | n+/n− |
|---|---|---|---|---|---|---|
| upside_pct_lvl | -0.2538 | +0.1611 | -0.4296 | 0.68% | 0.61% | 4405/233 |
| Performance (Month) | +0.1681 | -0.0365 | +0.2627 | 1.25% | 0.87% | 3052/8452 |
| Relative Strength Index (14) | +0.1244 | +0.1027 | -0.1674 | 0.97% | n/a | 11583/0 |
| d_Performance (Quarter) | +0.1065 | +0.0996 | +0.0685 | 1.55% | 0.42% | 5256/5808 |
| d_Beta | -0.0974 | -0.0316 | -0.1005 | 0.74% | 0.97% | 1571/855 |
| d_20-Day Simple Moving Average | -0.0918 | -0.1278 | -0.0110 | 1.35% | 0.74% | 4507/7029 |
| d_Average Volume | -0.0873 | -0.1646 | +0.0561 | 1.17% | 0.87% | 4797/6260 |
| d_Institutional Ownership | +0.0823 | +0.0192 | +0.0792 | 1.11% | 3.97% | 621/281 |
| d_Price | -0.0783 | -0.0421 | -0.0798 | 0.85% | 0.61% | 3736/7340 |
| d_Market Cap | -0.0732 | +0.0591 | -0.1180 | 2.64% | 0.55% | 2146/3563 |
| d_200-Day Simple Moving Average | -0.0718 | -0.1016 | -0.0077 | 1.57% | 0.69% | 3968/7565 |
| d_Short Ratio | +0.0708 | +0.1403 | -0.0574 | 0.87% | 0.65% | 4348/3040 |
| d_Relative Strength Index (14) | -0.0575 | +0.0046 | -0.0364 | 1.76% | 0.61% | 3861/7413 |
| d_Performance (YTD) | -0.0543 | -0.0990 | +0.0117 | 1.78% | 0.63% | 3833/7424 |
| d_50-Day Simple Moving Average | -0.0498 | -0.0821 | +0.0027 | 1.59% | 0.63% | 4140/7403 |
| d_Forward P/E | +0.0493 | +0.0325 | +0.0204 | 1.23% | 0.91% | 896/2050 |
| d_Performance (Week) | -0.0418 | +0.1025 | -0.1094 | 1.15% | 0.47% | 8424/3079 |
| d_Volatility (Month) | -0.0410 | -0.0692 | -0.0351 | 0.85% | 1.29% | 5453/4739 |
| Performance (Week) | +0.0392 | -0.1322 | +0.1588 | 0.97% | 1.00% | 2675/8821 |
| Institutional Transactions | -0.0344 | +0.0624 | -0.1120 | 0.99% | 2.31% | 3235/1812 |
| Short Float | +0.0336 | +0.1874 | -0.1674 | 1.34% | n/a | 5689/0 |
| true_ret | -0.0261 | -0.1027 | +0.0575 | 0.85% | 0.61% | 3736/7340 |
| d_Short Float | +0.0211 | -0.0105 | +0.0344 | 0.13% | 21.88% | 27/63 |
| d_Sales Growth Quarter Over Quarter | +0.0208 | +0.0291 | -0.0169 | -0.96% | -3.42% | 7/11 |
| d_Analyst Recom | +0.0199 | -0.0334 | +0.0039 | 1.35% | 0.16% | 72/66 |

## Combinations

| Pattern | n | Mean long fwd | Hit up |
|---|---|---|---|
| true_ret>3% & DOWNTREND | 284 | 2.81% | 26.4% |
| true_ret>3% & UPTREND | 150 | 1.71% | 42.0% |
| true_ret>3% & MIXED | 120 | 0.35% | 35.0% |

## Risk dominance probes

| State | n | Mean long fwd | Mean fwd if score top quintile |
|---|---|---|---|
| EXTENDED | 172 | 0.10% | 4.05% |
| WASHED | 2595 | 0.61% | 1.83% |

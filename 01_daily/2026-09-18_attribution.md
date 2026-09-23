# Factor attribution — signal 2026-09-18 → prediction day 2026-09-23

## Trade window (read this first)

| Role | Date | Meaning |
|------|------|---------|
| **Signal as-of** | **2026-09-18** | Features/scores formed from this snapshot (and deltas vs **2026-09-17**). Only data on/before this date. |
| **Prediction day** | **2026-09-23** | The trading day the forward return is for (exit snapshot). |
| **Entry price** | Price @ 2026-09-18 | Long: buy here; short: sell here. |
| **Exit price** | Price @ 2026-09-23 | Close proxy on prediction day. |
| **Return column** | `fwd_3d` | Long: exit/entry − 1; short = opposite. |

Graded **n=11626** names with valid entry and exit prices.

Provisional until multiple signal dates agree.

_Column guide: **IC** = Spearman(feature, long forward return); **IC↑** / **IC↓** = IC among names that went up / down._

## Score calibration (long fwd)
- Spearman IC(total_score, fwd_3d) = **0.1188**

| Quintile | Mean long fwd | Hit up>1.5% | n |
|---|---|---|---|
| 1 | 1.64% | 19.0% | 2788 |
| 2 | 0.04% | 14.5% | 2022 |
| 3 | 0.53% | 13.4% | 2520 |
| 4 | 0.07% | 20.3% | 2072 |
| 5 | 1.58% | 38.1% | 2224 |

## Top |IC| features

| Feature | IC | IC↑ | IC↓ | Mean fwd when + | Mean fwd when − | n+/n− |
|---|---|---|---|---|---|---|
| Relative Strength Index (14) | +0.1936 | -0.0759 | -0.1622 | 0.84% | n/a | 11543/0 |
| d_Price | +0.1481 | +0.0982 | -0.1303 | 0.89% | 0.61% | 4258/6857 |
| Performance (Week) | +0.1441 | +0.0359 | +0.1330 | 1.31% | 0.62% | 3793/7602 |
| d_Relative Strength Index (14) | +0.1354 | +0.0817 | -0.2426 | 1.32% | 0.60% | 4348/6918 |
| d_Performance (YTD) | +0.1253 | +0.0769 | -0.0335 | 1.31% | 0.60% | 4345/6927 |
| d_200-Day Simple Moving Average | +0.1200 | +0.0847 | -0.0279 | 1.28% | 0.56% | 4293/7182 |
| true_ret | +0.1138 | +0.0576 | -0.0006 | 0.89% | 0.61% | 4258/6857 |
| d_50-Day Simple Moving Average | +0.1108 | +0.0885 | -0.0233 | 1.31% | 0.54% | 4548/6957 |
| Performance (Month) | +0.1100 | -0.0915 | +0.1640 | 0.99% | 0.79% | 3347/8086 |
| d_Performance (Month) | +0.1069 | +0.0622 | +0.0358 | 1.57% | 0.47% | 3887/7472 |
| d_Performance (Quarter) | -0.1053 | -0.1561 | -0.0352 | 0.09% | 1.08% | 2994/7988 |
| Relative Volume | -0.1039 | +0.1760 | -0.1996 | 0.85% | n/a | 11414/0 |
| d_20-Day Simple Moving Average | +0.0983 | +0.0987 | -0.0393 | 1.20% | 0.58% | 4921/6588 |
| d_Volatility (Month) | -0.0730 | -0.0772 | -0.0306 | 0.80% | 1.26% | 4214/5065 |
| d_Relative Volume | -0.0544 | +0.1384 | -0.1745 | 0.73% | 1.07% | 7191/4111 |
| Institutional Transactions | -0.0339 | +0.0748 | -0.0818 | 1.23% | -0.52% | 3209/1825 |
| d_Sales Year Over Year TTM | -0.0328 | +0.0189 | -0.0394 | -8.79% | 1.17% | 2/1 |
| d_Beta | +0.0289 | -0.0295 | +0.0141 | 0.17% | 2.90% | 1719/2584 |
| d_Average Volume | -0.0255 | -0.0331 | +0.0056 | 1.84% | 0.18% | 4562/6489 |
| d_Gross Margin | -0.0229 | +0.0201 | -0.0218 | -4.63% | 0.50% | 3/2 |
| d_Sales Growth Quarter Over Quarter | -0.0217 | n/a | -0.0348 | -6.65% | -1.68% | 2/1 |
| d_Institutional Ownership | -0.0205 | +0.0098 | +0.0360 | -1.11% | -0.31% | 90/78 |
| d_Short Ratio | +0.0140 | +0.0158 | -0.0210 | -0.12% | 1.73% | 4391/2883 |
| d_Performance (Week) | -0.0101 | -0.0189 | -0.0336 | 0.76% | 0.88% | 3325/8096 |
| d_Short Float | +0.0099 | +0.0066 | +0.0080 | 2.31% | 1.27% | 25/39 |

## Combinations

| Pattern | n | Mean long fwd | Hit up |
|---|---|---|---|
| true_ret>3% & DOWNTREND | 328 | 1.80% | 43.0% |
| true_ret>3% & UPTREND | 362 | 4.45% | 46.4% |
| true_ret>3% & MIXED | 253 | 3.67% | 50.6% |

## Risk dominance probes

| State | n | Mean long fwd | Mean fwd if score top quintile |
|---|---|---|---|
| EXTENDED | 165 | 0.50% | 7.69% |
| WASHED | 1370 | 5.50% | 7.59% |

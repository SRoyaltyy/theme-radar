# Factor attribution — signal 2026-09-18 → prediction day 2026-09-22

## Trade window (read this first)

| Role | Date | Meaning |
|------|------|---------|
| **Signal as-of** | **2026-09-18** | Features/scores formed from this snapshot (and deltas vs **2026-09-17**). Only data on/before this date. |
| **Prediction day** | **2026-09-22** | The trading day the forward return is for (exit snapshot). |
| **Entry price** | Price @ 2026-09-18 | Long: buy here; short: sell here. |
| **Exit price** | Price @ 2026-09-22 | Close proxy on prediction day. |
| **Return column** | `fwd_2d` | Long: exit/entry − 1; short = opposite. |

Graded **n=11626** names with valid entry and exit prices.

Provisional until multiple signal dates agree.

_Column guide: **IC** = Spearman(feature, long forward return); **IC↑** / **IC↓** = IC among names that went up / down._

## Score calibration (long fwd)
- Spearman IC(total_score, fwd_2d) = **0.0651**

| Quintile | Mean long fwd | Hit up>1.5% | n |
|---|---|---|---|
| 1 | 2.69% | 32.0% | 2788 |
| 2 | 1.35% | 27.1% | 2022 |
| 3 | 1.63% | 29.4% | 2520 |
| 4 | 1.68% | 38.9% | 2072 |
| 5 | 3.01% | 50.9% | 2224 |

## Top |IC| features

| Feature | IC | IC↑ | IC↓ | Mean fwd when + | Mean fwd when − | n+/n− |
|---|---|---|---|---|---|---|
| d_Performance (Quarter) | -0.1935 | -0.1830 | -0.1165 | 1.57% | 2.26% | 2994/7988 |
| Short Float | +0.1799 | +0.3046 | -0.1003 | 2.18% | n/a | 5686/0 |
| upside_pct_lvl | +0.1493 | +0.3142 | -0.2033 | 1.67% | 0.21% | 4367/271 |
| Relative Strength Index (14) | +0.1119 | +0.1841 | -0.1960 | 2.12% | n/a | 11543/0 |
| d_Volatility (Month) | -0.1116 | -0.1121 | -0.0582 | 2.20% | 2.67% | 4214/5065 |
| d_Relative Strength Index (14) | +0.1087 | +0.2700 | -0.1675 | 2.65% | 1.85% | 4348/6918 |
| d_Price | +0.1001 | +0.1821 | -0.0900 | 2.22% | 1.86% | 4258/6857 |
| d_Performance (YTD) | +0.0733 | +0.1240 | -0.0518 | 2.67% | 1.85% | 4345/6927 |
| d_50-Day Simple Moving Average | +0.0732 | +0.1278 | -0.0360 | 2.88% | 1.63% | 4548/6957 |
| Performance (Week) | +0.0699 | +0.0111 | +0.0744 | 2.54% | 1.93% | 3793/7602 |
| d_20-Day Simple Moving Average | +0.0698 | +0.1338 | -0.0462 | 2.78% | 1.64% | 4921/6588 |
| d_200-Day Simple Moving Average | +0.0694 | +0.1224 | -0.0513 | 2.67% | 1.65% | 4293/7182 |
| d_Performance (Week) | -0.0627 | -0.0220 | -0.0564 | 2.81% | 1.86% | 3325/8096 |
| true_ret | +0.0605 | +0.0964 | -0.0273 | 2.22% | 1.86% | 4258/6857 |
| d_Average Volume | -0.0507 | -0.0677 | -0.0048 | 2.95% | 1.59% | 4562/6489 |
| d_Beta | -0.0473 | -0.0413 | -0.0129 | 1.50% | 4.21% | 1719/2584 |
| d_Sales Growth Quarter Over Quarter | -0.0365 | -0.0178 | -0.0378 | -5.11% | 5.04% | 2/1 |
| d_Performance (Month) | -0.0344 | +0.0086 | -0.0358 | 2.87% | 1.76% | 3887/7472 |
| d_Short Ratio | +0.0335 | +0.0502 | -0.0119 | 1.43% | 2.97% | 4391/2883 |
| Relative Volume | -0.0325 | +0.1555 | -0.0608 | 2.14% | n/a | 11414/0 |
| d_Sales Year Over Year TTM | -0.0291 | +0.0176 | -0.0424 | -6.20% | 1.24% | 2/1 |
| d_Institutional Ownership | -0.0201 | -0.0261 | +0.0438 | 0.53% | 1.07% | 90/78 |
| d_Forward P/E | -0.0200 | +0.0630 | -0.0604 | 1.11% | 0.70% | 987/1951 |
| d_Short Float | +0.0143 | -0.0002 | +0.0335 | 4.80% | 1.87% | 25/39 |
| Institutional Transactions | +0.0108 | +0.1020 | -0.0408 | 2.88% | 1.08% | 3209/1825 |

## Combinations

| Pattern | n | Mean long fwd | Hit up |
|---|---|---|---|
| true_ret>3% & DOWNTREND | 328 | 4.28% | 55.2% |
| true_ret>3% & UPTREND | 362 | 4.55% | 70.7% |
| true_ret>3% & MIXED | 253 | 7.29% | 64.4% |

## Risk dominance probes

| State | n | Mean long fwd | Mean fwd if score top quintile |
|---|---|---|---|
| EXTENDED | 165 | 2.50% | 11.18% |
| WASHED | 1370 | 6.92% | 13.11% |

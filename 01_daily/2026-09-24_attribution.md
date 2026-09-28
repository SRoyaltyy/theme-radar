# Factor attribution — signal 2026-09-24 → prediction day 2026-09-28

## Trade window (read this first)

| Role | Date | Meaning |
|------|------|---------|
| **Signal as-of** | **2026-09-24** | Features/scores formed from this snapshot (and deltas vs **2026-09-23**). Only data on/before this date. |
| **Prediction day** | **2026-09-28** | The trading day the forward return is for (exit snapshot). |
| **Entry price** | Price @ 2026-09-24 | Long: buy here; short: sell here. |
| **Exit price** | Price @ 2026-09-28 | Close proxy on prediction day. |
| **Return column** | `fwd_2d` | Long: exit/entry − 1; short = opposite. |

Graded **n=11657** names with valid entry and exit prices.

Provisional until multiple signal dates agree.

_Column guide: **IC** = Spearman(feature, long forward return); **IC↑** / **IC↓** = IC among names that went up / down._

## Score calibration (long fwd)
- Spearman IC(total_score, fwd_2d) = **0.0435**

| Quintile | Mean long fwd | Hit up>1.5% | n |
|---|---|---|---|
| 1 | 8.31% | 11.1% | 2787 |
| 2 | -0.83% | 6.0% | 2585 |
| 3 | -0.00% | 7.5% | 2396 |
| 4 | -0.17% | 8.3% | 1874 |
| 5 | -1.08% | 18.1% | 2015 |

## Top |IC| features

| Feature | IC | IC↑ | IC↓ | Mean fwd when + | Mean fwd when − | n+/n− |
|---|---|---|---|---|---|---|
| upside_pct_lvl | -0.2150 | +0.3214 | -0.4006 | 2.32% | -0.52% | 4381/256 |
| d_Performance (Week) | +0.1416 | -0.0939 | +0.2109 | 0.48% | 1.96% | 2644/8842 |
| d_Performance (Month) | +0.1022 | -0.0629 | +0.1643 | -0.44% | 2.48% | 3256/8120 |
| Performance (Month) | +0.0806 | -0.1603 | +0.1951 | -0.88% | 2.70% | 3436/8024 |
| Short Float | -0.0689 | +0.1552 | -0.1486 | 3.83% | n/a | 5690/0 |
| true_ret | +0.0567 | -0.0739 | +0.0910 | -0.60% | 3.04% | 3916/7065 |
| d_50-Day Simple Moving Average | +0.0544 | -0.0239 | +0.0644 | -0.66% | 2.89% | 4136/7377 |
| Institutional Transactions | -0.0491 | +0.0709 | -0.0768 | 6.84% | 1.18% | 3221/1809 |
| d_Performance (Quarter) | -0.0473 | +0.0258 | -0.0815 | 1.71% | 1.80% | 4108/6882 |
| d_Performance (YTD) | +0.0466 | -0.0489 | +0.0593 | -0.62% | 3.00% | 4013/7163 |
| d_20-Day Simple Moving Average | +0.0441 | -0.0161 | +0.0444 | -0.29% | 2.96% | 4741/6738 |
| d_Institutional Ownership | -0.0437 | +0.0809 | -0.1172 | -0.93% | -0.70% | 434/1538 |
| Relative Strength Index (14) | +0.0381 | -0.0519 | -0.0772 | 1.61% | n/a | 11561/0 |
| Performance (Week) | +0.0378 | -0.0228 | +0.0791 | -0.69% | 3.09% | 4471/7018 |
| d_200-Day Simple Moving Average | +0.0364 | -0.0332 | +0.0387 | -0.70% | 1.27% | 3975/7529 |
| d_Beta | -0.0362 | +0.0502 | -0.0615 | 7.80% | -1.56% | 3104/1228 |
| d_EPS Surprise | +0.0281 | -0.0150 | +0.0272 | 0.90% | -3.31% | 3/6 |
| d_Target Price | -0.0169 | +0.0287 | -0.0554 | -0.93% | 0.37% | 101/193 |
| d_Relative Strength Index (14) | +0.0158 | +0.0319 | -0.0639 | -0.58% | 2.99% | 4046/7147 |
| d_Volatility (Month) | +0.0139 | +0.0300 | +0.0199 | 3.59% | -0.54% | 5990/3892 |
| d_Profit Margin | +0.0136 | +0.0284 | +0.0070 | -2.28% | -4.43% | 6/6 |
| d_Insider Transactions | +0.0132 | +0.0574 | +0.0023 | -1.33% | 68.77% | 148/168 |
| d_Average Volume | -0.0125 | +0.0080 | +0.0049 | 4.50% | -0.88% | 5320/5762 |
| d_Price | +0.0124 | +0.0026 | -0.0461 | -0.60% | 3.04% | 3916/7065 |
| d_Sales Growth Quarter Over Quarter | +0.0117 | -0.0363 | +0.0056 | -5.63% | -2.21% | 3/7 |

## Combinations

| Pattern | n | Mean long fwd | Hit up |
|---|---|---|---|
| true_ret>3% & DOWNTREND | 199 | 4.94% | 23.6% |
| true_ret>3% & UPTREND | 264 | -1.42% | 23.9% |
| true_ret>3% & MIXED | 145 | -2.72% | 22.8% |

## Risk dominance probes

| State | n | Mean long fwd | Mean fwd if score top quintile |
|---|---|---|---|
| EXTENDED | 203 | -2.67% | -0.42% |
| WASHED | 2262 | 10.73% | 2.22% |

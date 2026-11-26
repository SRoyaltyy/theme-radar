# Factor attribution — signal 2026-11-24 → prediction day 2026-11-25

## Trade window (read this first)

| Role | Date | Meaning |
|------|------|---------|
| **Signal as-of** | **2026-11-24** | Features/scores formed from this snapshot (and deltas vs **2026-11-23**). Only data on/before this date. |
| **Prediction day** | **2026-11-25** | The trading day the forward return is for (exit snapshot). |
| **Entry price** | Price @ 2026-11-24 | Long: buy here; short: sell here. |
| **Exit price** | Price @ 2026-11-25 | Close proxy on prediction day. |
| **Return column** | `fwd_1d` | Long: exit/entry − 1; short = opposite. |

Graded **n=11768** names with valid entry and exit prices.

Provisional until multiple signal dates agree.

_Column guide: **IC** = Spearman(feature, long forward return); **IC↑** / **IC↓** = IC among names that went up / down._

## Score calibration (long fwd)
- Spearman IC(total_score, fwd_1d) = **0.1239**

| Quintile | Mean long fwd | Hit up>1.5% | n |
|---|---|---|---|
| 1 | 0.42% | 27.1% | 2449 |
| 2 | 0.40% | 12.5% | 3292 |
| 3 | 0.45% | 16.6% | 1638 |
| 4 | 0.80% | 19.8% | 2166 |
| 5 | 1.63% | 35.0% | 2223 |

## Top |IC| features

| Feature | IC | IC↑ | IC↓ | Mean fwd when + | Mean fwd when − | n+/n− |
|---|---|---|---|---|---|---|
| d_Price | +0.1336 | +0.0111 | -0.0322 | 1.03% | 0.49% | 5136/6061 |
| d_Performance (Week) | +0.1224 | +0.1193 | +0.0620 | 0.90% | 0.42% | 7358/4184 |
| d_Relative Strength Index (14) | +0.1197 | +0.0391 | -0.0039 | 1.02% | 0.48% | 5224/6121 |
| d_Performance (Month) | +0.1103 | +0.0440 | +0.0520 | 1.17% | 0.42% | 4723/6763 |
| d_Performance (YTD) | +0.1072 | +0.0053 | +0.0591 | 1.03% | 0.49% | 5201/6116 |
| d_200-Day Simple Moving Average | +0.1070 | +0.0180 | +0.0692 | 1.00% | 0.47% | 5456/6140 |
| Short Float | +0.1057 | +0.2149 | -0.0269 | 1.19% | n/a | 5597/0 |
| d_50-Day Simple Moving Average | +0.1031 | +0.0376 | +0.0734 | 1.01% | 0.45% | 5662/5952 |
| d_20-Day Simple Moving Average | +0.1018 | +0.0600 | +0.0614 | 0.98% | 0.45% | 6009/5599 |
| d_Performance (Quarter) | +0.0964 | +0.0196 | +0.0561 | 1.02% | 0.49% | 5499/5739 |
| true_ret | +0.0881 | -0.0056 | +0.1094 | 1.03% | 0.49% | 5136/6061 |
| Institutional Transactions | -0.0666 | +0.0158 | -0.0498 | 0.78% | 1.10% | 2579/2421 |
| d_Beta | +0.0534 | -0.0235 | +0.0176 | 0.69% | 1.05% | 5248/3515 |
| d_Insider Transactions | +0.0457 | +0.0724 | +0.0020 | 2.62% | 0.67% | 91/105 |
| Relative Volume | +0.0408 | +0.0556 | -0.0259 | 0.73% | n/a | 11542/0 |
| Performance (Week) | -0.0390 | -0.2683 | +0.2428 | 0.58% | 0.78% | 3390/8208 |
| d_Volatility (Month) | +0.0277 | +0.2554 | -0.2694 | 0.85% | 0.61% | 7326/2680 |
| upside_pct_lvl | +0.0266 | +0.4273 | -0.4924 | 1.34% | 0.49% | 4412/215 |
| d_Sales Year Over Year TTM | -0.0242 | +0.0085 | -0.0429 | -0.10% | 1.72% | 34/21 |
| Relative Strength Index (14) | -0.0228 | -0.2216 | +0.1713 | 0.72% | n/a | 11676/0 |
| d_Total Debt/Equity | -0.0209 | -0.0077 | +0.0160 | 1.76% | 2.49% | 19/33 |
| d_Short Ratio | -0.0202 | -0.0338 | -0.0025 | 0.59% | 0.89% | 5530/5579 |
| d_Average Volume | +0.0176 | +0.0136 | -0.0526 | 0.81% | 0.59% | 7214/3903 |
| d_EPS Surprise | +0.0169 | +0.0223 | +0.0089 | -0.05% | -1.32% | 20/18 |
| d_Sales Growth Quarter Over Quarter | -0.0158 | +0.0037 | -0.0239 | 0.98% | 1.43% | 29/27 |

## Combinations

| Pattern | n | Mean long fwd | Hit up |
|---|---|---|---|
| true_ret>3% & DOWNTREND | 592 | 3.91% | 40.9% |
| true_ret>3% & UPTREND | 312 | 0.43% | 28.8% |
| true_ret>3% & MIXED | 231 | 0.25% | 37.7% |

## Risk dominance probes

| State | n | Mean long fwd | Mean fwd if score top quintile |
|---|---|---|---|
| EXTENDED | 154 | 0.42% | 1.54% |
| WASHED | 2072 | 1.86% | 5.87% |

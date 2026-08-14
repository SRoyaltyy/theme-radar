# Factor attribution — signal 2026-08-11 → prediction day 2026-08-14

## Trade window (read this first)

| Role | Date | Meaning |
|------|------|---------|
| **Signal as-of** | **2026-08-11** | Features/scores formed from this snapshot (and deltas vs **2026-08-10**). Only data on/before this date. |
| **Prediction day** | **2026-08-14** | The trading day the forward return is for (exit snapshot). |
| **Entry price** | Price @ 2026-08-11 | Long: buy here; short: sell here. |
| **Exit price** | Price @ 2026-08-14 | Close proxy on prediction day. |
| **Return column** | `fwd_3d` | Long: exit/entry − 1; short = opposite. |

Graded **n=11542** names with valid entry and exit prices.

Provisional until multiple signal dates agree.

_Column guide: **IC** = Spearman(feature, long forward return); **IC↑** / **IC↓** = IC among names that went up / down._

## Score calibration (long fwd)
- Spearman IC(total_score, fwd_3d) = **0.0639**

| Quintile | Mean long fwd | Hit up>1.5% | n |
|---|---|---|---|
| 1 | 3.27% | 34.6% | 2347 |
| 2 | 0.64% | 13.8% | 3055 |
| 3 | 0.63% | 15.1% | 1944 |
| 4 | 1.70% | 37.7% | 2049 |
| 5 | 2.71% | 41.6% | 2147 |

## Top |IC| features

| Feature | IC | IC↑ | IC↓ | Mean fwd when + | Mean fwd when − | n+/n− |
|---|---|---|---|---|---|---|
| Performance (Week) | -0.1431 | -0.1410 | -0.0493 | 0.92% | 2.70% | 6031/5301 |
| d_Performance (Week) | -0.1243 | -0.2633 | +0.0688 | 1.53% | 1.83% | 2857/8494 |
| Performance (Month) | -0.0722 | -0.0868 | +0.0334 | 0.73% | 3.36% | 6985/4303 |
| Relative Strength Index (14) | -0.0643 | -0.2323 | +0.1363 | 1.74% | n/a | 11435/0 |
| Short Float | +0.0581 | +0.2259 | -0.1591 | 2.54% | n/a | 5695/0 |
| d_Performance (Quarter) | -0.0562 | -0.0165 | -0.0914 | 1.32% | 2.12% | 5735/5009 |
| d_Price | +0.0548 | +0.0778 | -0.0065 | 1.54% | 2.04% | 5856/4933 |
| d_20-Day Simple Moving Average | +0.0545 | +0.1112 | -0.0583 | 1.75% | 1.76% | 5730/5661 |
| d_Beta | -0.0515 | -0.0984 | -0.0181 | 2.10% | 3.69% | 1462/1965 |
| d_Performance (Month) | +0.0493 | +0.2102 | -0.1535 | 1.53% | 2.22% | 7757/3463 |
| d_Forward P/E | -0.0486 | -0.0521 | -0.0154 | 1.00% | 1.60% | 1665/1316 |
| Institutional Transactions | +0.0433 | +0.0582 | -0.0622 | 1.53% | 3.94% | 2520/2519 |
| d_Performance (YTD) | +0.0402 | +0.0863 | -0.0298 | 1.14% | 2.13% | 5977/5046 |
| Relative Volume | +0.0351 | +0.0935 | -0.0272 | 1.77% | n/a | 11272/0 |
| true_ret | +0.0350 | +0.0872 | -0.0364 | 1.54% | 2.04% | 5856/4933 |
| d_50-Day Simple Moving Average | +0.0334 | +0.1136 | -0.0803 | 1.61% | 1.93% | 6069/5310 |
| d_Average Volume | -0.0234 | -0.0457 | -0.0377 | 1.95% | 1.61% | 5278/5704 |
| d_Market Cap | -0.0166 | -0.0457 | +0.0203 | 1.63% | 3.60% | 3182/2513 |
| d_200-Day Simple Moving Average | +0.0155 | +0.0867 | -0.0654 | 1.53% | 2.01% | 5979/5374 |
| d_Sales Growth Quarter Over Quarter | -0.0132 | +0.0077 | +0.0135 | 0.49% | 1.61% | 89/103 |
| d_Relative Strength Index (14) | +0.0128 | +0.0370 | -0.0236 | 1.50% | 2.14% | 5979/5049 |
| d_Relative Volume | -0.0117 | -0.0366 | -0.0534 | 3.00% | 0.95% | 4529/6599 |
| d_Insider Transactions | +0.0095 | +0.0099 | +0.0230 | 1.44% | 0.76% | 164/220 |
| d_Total Debt/Equity | +0.0075 | +0.0033 | -0.0002 | 0.89% | 1.50% | 93/74 |
| d_EPS Surprise | -0.0064 | +0.0058 | +0.0141 | 0.13% | 0.29% | 99/119 |

## Combinations

| Pattern | n | Mean long fwd | Hit up |
|---|---|---|---|
| true_ret>3% & DOWNTREND | 408 | 10.22% | 47.1% |
| true_ret>3% & UPTREND | 300 | -0.13% | 37.0% |
| true_ret>3% & MIXED | 257 | 0.08% | 43.6% |

## Risk dominance probes

| State | n | Mean long fwd | Mean fwd if score top quintile |
|---|---|---|---|
| EXTENDED | 313 | -0.47% | -0.41% |
| WASHED | 557 | 15.37% | 29.75% |

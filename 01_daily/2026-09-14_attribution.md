# Factor attribution — signal 2026-09-14 → prediction day 2026-09-16

## Trade window (read this first)

| Role | Date | Meaning |
|------|------|---------|
| **Signal as-of** | **2026-09-14** | Features/scores formed from this snapshot (and deltas vs **2026-09-11**). Only data on/before this date. |
| **Prediction day** | **2026-09-16** | The trading day the forward return is for (exit snapshot). |
| **Entry price** | Price @ 2026-09-14 | Long: buy here; short: sell here. |
| **Exit price** | Price @ 2026-09-16 | Close proxy on prediction day. |
| **Return column** | `fwd_2d` | Long: exit/entry − 1; short = opposite. |

Graded **n=11604** names with valid entry and exit prices.

Provisional until multiple signal dates agree.

_Column guide: **IC** = Spearman(feature, long forward return); **IC↑** / **IC↓** = IC among names that went up / down._

## Score calibration (long fwd)
- Spearman IC(total_score, fwd_2d) = **-0.1114**

| Quintile | Mean long fwd | Hit up>1.5% | n |
|---|---|---|---|
| 1 | -0.56% | 14.5% | 2518 |
| 2 | -0.79% | 5.0% | 2855 |
| 3 | -1.37% | 6.1% | 1662 |
| 4 | -0.97% | 5.8% | 2302 |
| 5 | -1.43% | 13.6% | 2267 |

## Top |IC| features

| Feature | IC | IC↑ | IC↓ | Mean fwd when + | Mean fwd when − | n+/n− |
|---|---|---|---|---|---|---|
| upside_pct_lvl | -0.2036 | +0.2706 | -0.3792 | -1.48% | -1.17% | 4367/273 |
| d_Relative Strength Index (14) | -0.1554 | -0.0426 | -0.2488 | -1.72% | -0.58% | 4021/7169 |
| d_Forward P/E | -0.1516 | -0.0600 | -0.1064 | -1.64% | -0.90% | 1451/1497 |
| Performance (Week) | +0.1445 | -0.1544 | +0.2391 | -0.47% | -1.11% | 2231/9235 |
| Short Float | -0.1411 | +0.1392 | -0.2367 | -1.08% | n/a | 5706/0 |
| d_Price | -0.1317 | -0.0778 | -0.1911 | -1.88% | -0.55% | 3935/7090 |
| d_20-Day Simple Moving Average | -0.1226 | -0.1316 | -0.1239 | -1.62% | -0.53% | 4798/6660 |
| d_Performance (Week) | -0.1196 | -0.1592 | -0.0835 | -1.57% | -0.64% | 4357/7015 |
| d_200-Day Simple Moving Average | -0.1170 | -0.1308 | -0.1200 | -1.74% | -0.57% | 4135/7342 |
| d_50-Day Simple Moving Average | -0.1122 | -0.1348 | -0.1090 | -1.70% | -0.56% | 4337/7140 |
| d_Performance (YTD) | -0.1108 | -0.1289 | -0.1125 | -1.72% | -0.57% | 4000/7186 |
| true_ret | -0.1028 | -0.1672 | -0.0853 | -1.88% | -0.55% | 3935/7090 |
| d_Market Cap | -0.0763 | -0.0069 | -0.0637 | -1.53% | -0.73% | 2575/3108 |
| Performance (Month) | +0.0555 | -0.1889 | +0.1584 | -1.53% | -0.80% | 3033/8386 |
| d_Short Float | +0.0502 | -0.0283 | +0.0798 | -2.25% | 0.25% | 104/256 |
| d_Relative Volume | +0.0448 | +0.0144 | +0.0232 | -0.86% | -1.16% | 6641/4551 |
| d_Institutional Transactions | +0.0351 | -0.0004 | +0.0450 | -1.37% | -1.85% | 2142/1491 |
| d_Volatility (Month) | -0.0344 | -0.0817 | +0.0092 | -1.31% | -0.83% | 4398/4729 |
| d_Short Ratio | -0.0337 | +0.0263 | -0.0524 | -0.89% | -1.50% | 4521/2743 |
| d_Average Volume | +0.0296 | -0.0440 | +0.0713 | -1.16% | -0.87% | 4306/6740 |
| d_Performance (Quarter) | -0.0247 | -0.0200 | -0.0573 | -1.01% | -1.04% | 3720/7170 |
| Relative Strength Index (14) | -0.0177 | -0.0166 | -0.1011 | -0.99% | n/a | 11525/0 |
| d_Total Debt/Equity | +0.0156 | -0.0227 | +0.0281 | -2.71% | -8.18% | 7/4 |
| d_Profit Margin | +0.0117 | n/a | +0.0154 | -4.08% | -5.23% | 4/5 |
| Relative Volume | +0.0112 | +0.0456 | -0.0248 | -0.99% | n/a | 11409/0 |

## Combinations

| Pattern | n | Mean long fwd | Hit up |
|---|---|---|---|
| true_ret>3% & DOWNTREND | 329 | -1.14% | 16.7% |
| true_ret>3% & UPTREND | 365 | -2.15% | 17.3% |
| true_ret>3% & MIXED | 223 | -6.09% | 13.5% |

## Risk dominance probes

| State | n | Mean long fwd | Mean fwd if score top quintile |
|---|---|---|---|
| EXTENDED | 158 | -3.15% | -2.30% |
| WASHED | 1684 | -0.73% | -1.54% |

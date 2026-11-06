# Factor attribution — signal 2026-11-04 → prediction day 2026-11-06

## Trade window (read this first)

| Role | Date | Meaning |
|------|------|---------|
| **Signal as-of** | **2026-11-04** | Features/scores formed from this snapshot (and deltas vs **2026-11-03**). Only data on/before this date. |
| **Prediction day** | **2026-11-06** | The trading day the forward return is for (exit snapshot). |
| **Entry price** | Price @ 2026-11-04 | Long: buy here; short: sell here. |
| **Exit price** | Price @ 2026-11-06 | Close proxy on prediction day. |
| **Return column** | `fwd_2d` | Long: exit/entry − 1; short = opposite. |

Graded **n=11741** names with valid entry and exit prices.

Provisional until multiple signal dates agree.

_Column guide: **IC** = Spearman(feature, long forward return); **IC↑** / **IC↓** = IC among names that went up / down._

## Score calibration (long fwd)
- Spearman IC(total_score, fwd_2d) = **0.0430**

| Quintile | Mean long fwd | Hit up>1.5% | n |
|---|---|---|---|
| 1 | -1.08% | 11.5% | 2358 |
| 2 | -0.83% | 4.9% | 2734 |
| 3 | -2.14% | 5.5% | 2089 |
| 4 | -2.41% | 10.1% | 2615 |
| 5 | -1.69% | 15.1% | 1945 |

## Top |IC| features

| Feature | IC | IC↑ | IC↓ | Mean fwd when + | Mean fwd when − | n+/n− |
|---|---|---|---|---|---|---|
| Performance (Month) | +0.2231 | -0.1485 | +0.3249 | -1.97% | -1.28% | 5472/6101 |
| Relative Strength Index (14) | +0.2020 | -0.2444 | +0.3033 | -1.61% | n/a | 11669/0 |
| Performance (Week) | +0.1792 | -0.0009 | +0.2614 | -1.85% | -1.34% | 5972/5623 |
| Short Float | -0.1756 | +0.3224 | -0.2246 | -0.76% | n/a | 5638/0 |
| upside_pct_lvl | -0.0984 | +0.2919 | -0.3143 | -1.61% | -3.19% | 4226/412 |
| d_Performance (Quarter) | -0.0789 | +0.0457 | -0.0153 | -2.25% | 0.40% | 8236/2983 |
| d_20-Day Simple Moving Average | -0.0696 | +0.1751 | -0.0353 | -1.73% | -1.27% | 8770/2864 |
| d_Relative Strength Index (14) | +0.0684 | -0.1139 | +0.2678 | -1.79% | -2.50% | 8388/3021 |
| d_Volatility (Month) | -0.0541 | +0.0803 | -0.0849 | 0.03% | -2.92% | 4499/5081 |
| d_Market Cap | +0.0539 | -0.0042 | +0.1542 | -1.48% | 2.88% | 3846/1892 |
| d_Performance (Week) | +0.0475 | +0.1015 | +0.0979 | -1.52% | -1.86% | 7848/3715 |
| Relative Volume | -0.0466 | +0.2225 | -0.0537 | -1.62% | n/a | 11471/0 |
| d_Average Volume | +0.0443 | +0.0136 | +0.0064 | -0.91% | -2.23% | 5598/5491 |
| d_Beta | +0.0414 | +0.0506 | +0.0537 | 5.36% | -5.01% | 1792/1067 |
| d_Relative Volume | -0.0367 | +0.1654 | -0.0659 | -0.92% | -2.71% | 7157/4192 |
| d_Short Ratio | -0.0335 | +0.0056 | -0.0118 | -2.05% | -3.00% | 3440/3488 |
| d_Performance (Month) | -0.0329 | +0.1456 | -0.0005 | -2.28% | -0.04% | 8051/3426 |
| d_50-Day Simple Moving Average | -0.0319 | +0.1665 | +0.0165 | -1.66% | -1.49% | 8712/2917 |
| d_Insider Transactions | +0.0280 | -0.0138 | -0.0015 | 4.34% | -3.82% | 95/218 |
| d_200-Day Simple Moving Average | -0.0265 | +0.1302 | +0.0424 | -1.63% | -2.39% | 8555/3048 |
| d_Forward P/E | +0.0265 | +0.0555 | +0.0212 | -3.23% | -3.93% | 2159/816 |
| d_Sales Growth Quarter Over Quarter | -0.0230 | +0.0389 | -0.0202 | -4.05% | -3.08% | 86/107 |
| true_ret | -0.0228 | +0.1315 | +0.0285 | -2.07% | -1.65% | 8348/2968 |
| d_Short Float | +0.0195 | -0.0838 | +0.0433 | -2.72% | -3.38% | 91/53 |
| d_Performance (YTD) | -0.0179 | +0.0950 | +0.0733 | -2.08% | -2.38% | 8412/3006 |

## Combinations

| Pattern | n | Mean long fwd | Hit up |
|---|---|---|---|
| true_ret>3% & DOWNTREND | 1013 | 0.66% | 21.9% |
| true_ret>3% & UPTREND | 1097 | -2.62% | 10.8% |
| true_ret>3% & MIXED | 573 | -2.29% | 16.9% |

## Risk dominance probes

| State | n | Mean long fwd | Mean fwd if score top quintile |
|---|---|---|---|
| EXTENDED | 393 | -0.13% | 8.20% |
| WASHED | 1536 | 2.29% | -5.18% |

# Factor attribution — signal 2026-09-23 → prediction day 2026-09-28

## Trade window (read this first)

| Role | Date | Meaning |
|------|------|---------|
| **Signal as-of** | **2026-09-23** | Features/scores formed from this snapshot (and deltas vs **2026-09-22**). Only data on/before this date. |
| **Prediction day** | **2026-09-28** | The trading day the forward return is for (exit snapshot). |
| **Entry price** | Price @ 2026-09-23 | Long: buy here; short: sell here. |
| **Exit price** | Price @ 2026-09-28 | Close proxy on prediction day. |
| **Return column** | `fwd_3d` | Long: exit/entry − 1; short = opposite. |

Graded **n=11650** names with valid entry and exit prices.

Provisional until multiple signal dates agree.

_Column guide: **IC** = Spearman(feature, long forward return); **IC↑** / **IC↓** = IC among names that went up / down._

## Score calibration (long fwd)
- Spearman IC(total_score, fwd_3d) = **0.0444**

| Quintile | Mean long fwd | Hit up>1.5% | n |
|---|---|---|---|
| 1 | 3.46% | 15.1% | 2493 |
| 2 | -0.45% | 6.7% | 3301 |
| 3 | -1.21% | 12.3% | 1199 |
| 4 | 2.96% | 6.5% | 2542 |
| 5 | -1.41% | 18.4% | 2115 |

## Top |IC| features

| Feature | IC | IC↑ | IC↓ | Mean fwd when + | Mean fwd when − | n+/n− |
|---|---|---|---|---|---|---|
| upside_pct_lvl | -0.2653 | +0.2332 | -0.3920 | 1.05% | -0.41% | 4370/267 |
| Performance (Month) | +0.1341 | -0.1201 | +0.2422 | -0.85% | 1.74% | 3691/7777 |
| true_ret | +0.1240 | -0.2056 | +0.2555 | -0.94% | 0.30% | 1878/9370 |
| Relative Strength Index (14) | +0.1219 | -0.0778 | +0.0325 | 0.90% | n/a | 11556/0 |
| d_50-Day Simple Moving Average | +0.0987 | -0.1856 | +0.2128 | -0.05% | 1.09% | 2075/9488 |
| d_20-Day Simple Moving Average | +0.0983 | -0.1743 | +0.2041 | -0.71% | 1.26% | 2216/9349 |
| d_Performance (YTD) | +0.0773 | -0.1514 | +0.1644 | -0.92% | 0.29% | 1923/9420 |
| d_200-Day Simple Moving Average | +0.0739 | -0.1646 | +0.1700 | -0.68% | 1.23% | 2023/9533 |
| d_Performance (Quarter) | -0.0708 | -0.1260 | -0.0305 | -1.49% | 2.01% | 3097/7902 |
| d_Performance (Week) | +0.0618 | -0.1474 | +0.1521 | 1.74% | 0.55% | 3375/8089 |
| Short Float | -0.0559 | +0.1459 | -0.1531 | 2.56% | n/a | 5700/0 |
| d_Market Cap | -0.0471 | +0.0822 | -0.0659 | -1.40% | 3.88% | 1406/4333 |
| d_Relative Strength Index (14) | -0.0416 | +0.1433 | -0.2553 | -0.95% | 1.31% | 1930/9385 |
| Relative Volume | -0.0392 | +0.0693 | -0.0455 | 0.89% | n/a | 11417/0 |
| Institutional Transactions | -0.0355 | +0.0949 | -0.0995 | 4.97% | 0.53% | 3221/1808 |
| d_Short Ratio | -0.0321 | +0.0004 | -0.0415 | -0.68% | -0.93% | 3913/3307 |
| d_Performance (Month) | +0.0298 | -0.0547 | +0.0702 | -0.62% | 1.57% | 3406/7988 |
| d_Beta | +0.0260 | -0.0391 | +0.0457 | -1.03% | 0.34% | 215/327 |
| d_Short Float | +0.0218 | n/a | +0.0267 | n/a | -15.95% | 0/1 |
| d_Average Volume | +0.0204 | +0.0082 | +0.0338 | 2.83% | -0.63% | 5089/5975 |
| d_Target Price | +0.0162 | +0.0456 | +0.0058 | -1.44% | -2.04% | 104/138 |
| d_Institutional Ownership | +0.0145 | +0.0084 | +0.0192 | 1.68% | -1.09% | 12/40 |
| d_Insider Transactions | -0.0131 | -0.0302 | -0.0128 | -4.45% | -1.17% | 92/177 |
| d_Volatility (Month) | +0.0123 | +0.0250 | +0.0042 | 1.12% | 1.47% | 5313/3987 |
| Performance (Week) | +0.0122 | +0.0556 | +0.0337 | -0.64% | 2.46% | 5741/5716 |

## Combinations

| Pattern | n | Mean long fwd | Hit up |
|---|---|---|---|
| true_ret>3% & DOWNTREND | 205 | 4.25% | 36.1% |
| true_ret>3% & UPTREND | 115 | -1.89% | 27.0% |
| true_ret>3% & MIXED | 91 | -2.69% | 26.4% |

## Risk dominance probes

| State | n | Mean long fwd | Mean fwd if score top quintile |
|---|---|---|---|
| EXTENDED | 204 | -2.63% | -7.73% |
| WASHED | 1805 | 10.46% | 10.60% |

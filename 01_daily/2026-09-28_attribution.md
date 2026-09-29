# Factor attribution — signal 2026-09-28 → prediction day 2026-09-29

## Trade window (read this first)

| Role | Date | Meaning |
|------|------|---------|
| **Signal as-of** | **2026-09-28** | Features/scores formed from this snapshot (and deltas vs **2026-09-25**). Only data on/before this date. |
| **Prediction day** | **2026-09-29** | The trading day the forward return is for (exit snapshot). |
| **Entry price** | Price @ 2026-09-28 | Long: buy here; short: sell here. |
| **Exit price** | Price @ 2026-09-29 | Close proxy on prediction day. |
| **Return column** | `fwd_1d` | Long: exit/entry − 1; short = opposite. |

Graded **n=11668** names with valid entry and exit prices.

Provisional until multiple signal dates agree.

_Column guide: **IC** = Spearman(feature, long forward return); **IC↑** / **IC↓** = IC among names that went up / down._

## Score calibration (long fwd)
- Spearman IC(total_score, fwd_1d) = **-0.0477**

| Quintile | Mean long fwd | Hit up>1.5% | n |
|---|---|---|---|
| 1 | 1.31% | 19.4% | 2340 |
| 2 | -0.16% | 6.1% | 3371 |
| 3 | 1.06% | 5.6% | 1306 |
| 4 | -0.31% | 6.4% | 2705 |
| 5 | 0.01% | 14.7% | 1946 |

## Top |IC| features

| Feature | IC | IC↑ | IC↓ | Mean fwd when + | Mean fwd when − | n+/n− |
|---|---|---|---|---|---|---|
| d_Performance (Quarter) | -0.1392 | -0.2056 | -0.0084 | 1.03% | 0.03% | 2566/8479 |
| d_Performance (Week) | -0.1231 | -0.1864 | +0.0003 | 1.13% | 0.02% | 2551/8938 |
| d_Relative Strength Index (14) | -0.1150 | +0.1153 | -0.3123 | -0.10% | 0.38% | 2314/8987 |
| d_20-Day Simple Moving Average | -0.0925 | -0.2138 | +0.0517 | 0.94% | 0.05% | 2870/8719 |
| d_Performance (Month) | -0.0896 | -0.1868 | +0.0460 | -0.22% | 0.45% | 3064/8322 |
| d_200-Day Simple Moving Average | -0.0846 | -0.2027 | +0.0469 | 0.55% | 0.01% | 2367/9198 |
| Relative Strength Index (14) | +0.0845 | -0.0582 | -0.0361 | 0.26% | n/a | 11565/0 |
| Performance (Month) | +0.0844 | -0.1957 | +0.2672 | 0.53% | 0.18% | 2793/8712 |
| d_Performance (YTD) | -0.0841 | -0.1973 | +0.0461 | -0.10% | 0.20% | 2299/9039 |
| d_50-Day Simple Moving Average | -0.0831 | -0.2190 | +0.0716 | 0.50% | 0.20% | 2500/9096 |
| true_ret | -0.0694 | -0.2595 | +0.1116 | -0.10% | 0.03% | 2257/8968 |
| d_Price | -0.0586 | -0.0112 | -0.1442 | -0.10% | 0.03% | 2257/8968 |
| d_Forward P/E | -0.0572 | -0.1181 | +0.0594 | -0.20% | -0.22% | 843/2087 |
| Short Float | -0.0442 | +0.1459 | -0.0880 | 0.63% | n/a | 5692/0 |
| Institutional Transactions | -0.0399 | +0.0734 | -0.0875 | 0.56% | 1.07% | 3235/1813 |
| upside_pct_lvl | -0.0286 | +0.3391 | -0.3604 | 0.04% | -0.19% | 4386/248 |
| d_Market Cap | -0.0284 | +0.0550 | -0.0850 | 0.61% | 0.66% | 1745/3975 |
| d_Gross Margin | -0.0284 | -0.0283 | -0.0117 | -4.45% | 1.10% | 5/12 |
| d_Relative Volume | +0.0271 | +0.0323 | +0.0017 | 0.08% | 0.55% | 6159/5078 |
| d_Average Volume | -0.0262 | -0.0309 | +0.0418 | 0.69% | -0.02% | 4759/6342 |
| d_Beta | +0.0249 | -0.0560 | +0.0145 | 1.81% | 0.20% | 1135/2391 |
| d_Sales Growth Quarter Over Quarter | +0.0243 | +0.0111 | +0.0262 | 0.69% | -2.62% | 7/4 |
| d_Profit Margin | +0.0230 | -0.0200 | +0.0311 | -2.80% | 0.77% | 5/7 |
| d_EPS Surprise | -0.0182 | n/a | -0.0158 | -3.07% | -1.26% | 3/1 |
| d_Institutional Transactions | +0.0133 | +0.0230 | -0.0127 | 0.05% | 0.56% | 1831/1724 |

## Combinations

| Pattern | n | Mean long fwd | Hit up |
|---|---|---|---|
| true_ret>3% & DOWNTREND | 192 | -1.02% | 26.0% |
| true_ret>3% & UPTREND | 134 | 4.59% | 28.4% |
| true_ret>3% & MIXED | 108 | 0.43% | 29.6% |

## Risk dominance probes

| State | n | Mean long fwd | Mean fwd if score top quintile |
|---|---|---|---|
| EXTENDED | 170 | 0.74% | 3.17% |
| WASHED | 2432 | 0.68% | -0.73% |

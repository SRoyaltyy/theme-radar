# Factor attribution — signal 2026-08-14 → prediction day 2026-08-17

## Trade window (read this first)

| Role | Date | Meaning |
|------|------|---------|
| **Signal as-of** | **2026-08-14** | Features/scores formed from this snapshot (and deltas vs **2026-08-13**). Only data on/before this date. |
| **Prediction day** | **2026-08-17** | The trading day the forward return is for (exit snapshot). |
| **Entry price** | Price @ 2026-08-14 | Long: buy here; short: sell here. |
| **Exit price** | Price @ 2026-08-17 | Close proxy on prediction day. |
| **Return column** | `fwd_1d` | Long: exit/entry − 1; short = opposite. |

Graded **n=11551** names with valid entry and exit prices.

Provisional until multiple signal dates agree.

_Column guide: **IC** = Spearman(feature, long forward return); **IC↑** / **IC↓** = IC among names that went up / down._

## Score calibration (long fwd)
- Spearman IC(total_score, fwd_1d) = **0.1577**

| Quintile | Mean long fwd | Hit up>1.5% | n |
|---|---|---|---|
| 1 | -0.76% | 11.7% | 2327 |
| 2 | 0.36% | 5.2% | 2553 |
| 3 | -0.30% | 5.9% | 2399 |
| 4 | 0.08% | 15.2% | 1996 |
| 5 | -0.07% | 27.0% | 2276 |

## Top |IC| features

| Feature | IC | IC↑ | IC↓ | Mean fwd when + | Mean fwd when − | n+/n− |
|---|---|---|---|---|---|---|
| d_Performance (Month) | +0.2294 | +0.3058 | +0.0606 | -0.02% | -0.31% | 6305/4933 |
| Short Float | -0.1213 | +0.2061 | -0.2336 | -0.28% | n/a | 5690/0 |
| d_Forward P/E | +0.1202 | +0.0940 | +0.0870 | -0.58% | -0.94% | 1582/1352 |
| d_Beta | -0.1158 | -0.0611 | -0.0903 | -0.87% | 0.68% | 1961/2166 |
| d_Performance (Quarter) | +0.0938 | +0.0578 | +0.0659 | 0.17% | -0.43% | 4238/6510 |
| d_50-Day Simple Moving Average | +0.0702 | +0.0970 | +0.0077 | -0.24% | -0.04% | 5103/6272 |
| d_Market Cap | +0.0685 | +0.0203 | +0.0483 | -0.56% | 0.00% | 2950/2726 |
| Performance (Month) | +0.0656 | +0.0979 | +0.0006 | -0.25% | 0.05% | 7234/4098 |
| d_Price | +0.0621 | +0.0588 | -0.0080 | -0.24% | -0.35% | 5169/5660 |
| d_Institutional Ownership | +0.0530 | +0.0201 | +0.0504 | -0.59% | 0.12% | 2864/2119 |
| d_Performance (YTD) | +0.0527 | +0.0607 | +0.0139 | -0.23% | -0.03% | 5290/5751 |
| true_ret | +0.0466 | +0.0590 | +0.0158 | -0.24% | -0.35% | 5169/5660 |
| d_Sales Year Over Year TTM | +0.0462 | +0.0042 | +0.0285 | -0.75% | -2.29% | 106/107 |
| Relative Volume | -0.0453 | +0.1265 | -0.1094 | -0.14% | n/a | 11266/0 |
| Institutional Transactions | +0.0437 | +0.0769 | -0.0029 | 0.27% | -0.91% | 2518/2514 |
| d_Relative Strength Index (14) | +0.0431 | +0.0715 | -0.0851 | -0.25% | -0.03% | 5301/5731 |
| Performance (Week) | +0.0430 | +0.0993 | -0.0124 | -0.25% | 0.04% | 7150/4184 |
| d_200-Day Simple Moving Average | +0.0408 | +0.0834 | -0.0221 | -0.29% | -0.01% | 5177/6186 |
| d_Volatility (Month) | -0.0360 | -0.0435 | +0.0341 | 0.15% | -0.30% | 3385/6024 |
| d_Target Price | +0.0333 | +0.0101 | +0.0657 | -0.25% | -1.17% | 293/209 |
| d_Sales Growth Quarter Over Quarter | +0.0319 | +0.0113 | +0.0187 | -1.34% | -1.87% | 108/120 |
| d_20-Day Simple Moving Average | +0.0295 | +0.0346 | +0.0140 | 0.11% | -0.30% | 4642/6767 |
| d_Analyst Recom | -0.0270 | -0.0308 | -0.0167 | -1.03% | -0.08% | 132/89 |
| d_Performance (Week) | +0.0261 | -0.0759 | +0.1099 | -0.39% | -0.04% | 3304/8003 |
| d_Short Ratio | -0.0207 | -0.0274 | -0.0277 | -0.40% | -0.33% | 4025/2721 |

## Combinations

| Pattern | n | Mean long fwd | Hit up |
|---|---|---|---|
| true_ret>3% & DOWNTREND | 333 | 0.39% | 29.1% |
| true_ret>3% & UPTREND | 317 | -0.42% | 30.3% |
| true_ret>3% & MIXED | 249 | -1.28% | 28.5% |

## Risk dominance probes

| State | n | Mean long fwd | Mean fwd if score top quintile |
|---|---|---|---|
| EXTENDED | 378 | 0.23% | 4.56% |
| WASHED | 447 | 3.60% | -2.52% |

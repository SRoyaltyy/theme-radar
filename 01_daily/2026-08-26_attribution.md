# Factor attribution — signal 2026-08-26 → prediction day 2026-08-28

## Trade window (read this first)

| Role | Date | Meaning |
|------|------|---------|
| **Signal as-of** | **2026-08-26** | Features/scores formed from this snapshot (and deltas vs **2026-08-25**). Only data on/before this date. |
| **Prediction day** | **2026-08-28** | The trading day the forward return is for (exit snapshot). |
| **Entry price** | Price @ 2026-08-26 | Long: buy here; short: sell here. |
| **Exit price** | Price @ 2026-08-28 | Close proxy on prediction day. |
| **Return column** | `fwd_1d` | Long: exit/entry − 1; short = opposite. |

Graded **n=11621** names with valid entry and exit prices.

Provisional until multiple signal dates agree.

_Column guide: **IC** = Spearman(feature, long forward return); **IC↑** / **IC↓** = IC among names that went up / down._

## Score calibration (long fwd)
- Spearman IC(total_score, fwd_1d) = **0.0468**

| Quintile | Mean long fwd | Hit up>1.5% | n |
|---|---|---|---|
| 1 | 0.35% | 24.0% | 2448 |
| 2 | 1.97% | 15.5% | 2612 |
| 3 | 0.25% | 9.7% | 1961 |
| 4 | 0.36% | 12.2% | 2280 |
| 5 | 1.48% | 28.1% | 2320 |

## Top |IC| features

| Feature | IC | IC↑ | IC↓ | Mean fwd when + | Mean fwd when − | n+/n− |
|---|---|---|---|---|---|---|
| Performance (Month) | +0.2470 | +0.2825 | +0.0371 | 1.29% | 0.21% | 7586/3766 |
| d_20-Day Simple Moving Average | -0.1765 | -0.2711 | +0.0140 | 1.45% | 0.68% | 3850/7593 |
| d_Performance (Month) | +0.1514 | +0.1012 | +0.0772 | 1.96% | 0.24% | 4549/6744 |
| true_ret | -0.0984 | -0.1839 | +0.0169 | 0.64% | 0.68% | 4644/6216 |
| d_200-Day Simple Moving Average | -0.0979 | -0.1529 | -0.0087 | 1.41% | 0.63% | 4515/6858 |
| d_Volatility (Month) | -0.0968 | -0.2033 | +0.0961 | 1.01% | 1.00% | 3070/6477 |
| d_Performance (YTD) | -0.0903 | -0.1674 | +0.0133 | 1.37% | 0.65% | 4778/6323 |
| Institutional Transactions | +0.0853 | +0.0972 | -0.0036 | 2.07% | 0.39% | 3177/1880 |
| d_50-Day Simple Moving Average | -0.0842 | -0.1421 | +0.0047 | 1.42% | 0.60% | 4715/6676 |
| d_Beta | +0.0834 | +0.1208 | -0.0402 | 1.11% | 2.09% | 1792/1137 |
| d_Market Cap | -0.0749 | -0.0643 | +0.0671 | 2.21% | 0.55% | 2504/3189 |
| d_Price | -0.0677 | -0.1401 | -0.0226 | 0.64% | 0.68% | 4644/6216 |
| d_Relative Strength Index (14) | -0.0606 | -0.1080 | -0.0971 | 1.36% | 0.64% | 4773/6318 |
| Relative Volume | -0.0452 | +0.0635 | -0.0435 | 0.94% | n/a | 11334/0 |
| d_Institutional Ownership | +0.0398 | -0.0013 | +0.0360 | 0.21% | -0.05% | 1243/915 |
| Performance (Week) | -0.0389 | -0.0924 | +0.0268 | 1.05% | 0.84% | 5476/5884 |
| d_Target Price | +0.0375 | +0.0598 | +0.0139 | 0.70% | -0.76% | 155/70 |
| d_Short Float | -0.0343 | -0.0239 | +0.0087 | 0.42% | 2.14% | 2558/2935 |
| d_Forward P/E | -0.0318 | -0.0534 | +0.0747 | 0.10% | 0.21% | 1390/1552 |
| d_Performance (Week) | -0.0287 | -0.1294 | +0.0963 | 1.55% | 0.60% | 4079/7285 |
| Relative Strength Index (14) | +0.0280 | -0.2138 | +0.1278 | 0.93% | n/a | 11497/0 |
| d_Average Volume | +0.0270 | -0.1663 | +0.1737 | 1.60% | 0.76% | 2540/8707 |
| d_Performance (Quarter) | +0.0262 | -0.0191 | +0.0536 | 1.50% | 0.39% | 5140/5663 |
| d_Gross Margin | +0.0256 | -0.0223 | +0.0291 | 0.33% | -1.37% | 20/15 |
| Short Float | +0.0230 | +0.2340 | -0.1459 | 1.29% | n/a | 5702/0 |

## Combinations

| Pattern | n | Mean long fwd | Hit up |
|---|---|---|---|
| true_ret>3% & DOWNTREND | 231 | 5.60% | 24.7% |
| true_ret>3% & UPTREND | 164 | -0.39% | 29.3% |
| true_ret>3% & MIXED | 136 | 1.14% | 31.6% |

## Risk dominance probes

| State | n | Mean long fwd | Mean fwd if score top quintile |
|---|---|---|---|
| EXTENDED | 400 | 1.15% | -2.41% |
| WASHED | 427 | 2.85% | 15.35% |

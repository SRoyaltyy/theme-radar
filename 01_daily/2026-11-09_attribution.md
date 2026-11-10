# Factor attribution — signal 2026-11-09 → prediction day 2026-11-10

## Trade window (read this first)

| Role | Date | Meaning |
|------|------|---------|
| **Signal as-of** | **2026-11-09** | Features/scores formed from this snapshot (and deltas vs **2026-11-06**). Only data on/before this date. |
| **Prediction day** | **2026-11-10** | The trading day the forward return is for (exit snapshot). |
| **Entry price** | Price @ 2026-11-09 | Long: buy here; short: sell here. |
| **Exit price** | Price @ 2026-11-10 | Close proxy on prediction day. |
| **Return column** | `fwd_1d` | Long: exit/entry − 1; short = opposite. |

Graded **n=11727** names with valid entry and exit prices.

Provisional until multiple signal dates agree.

_Column guide: **IC** = Spearman(feature, long forward return); **IC↑** / **IC↓** = IC among names that went up / down._

## Score calibration (long fwd)
- Spearman IC(total_score, fwd_1d) = **-0.0405**

| Quintile | Mean long fwd | Hit up>1.5% | n |
|---|---|---|---|
| 1 | -0.42% | 13.2% | 2396 |
| 2 | -0.77% | 7.1% | 2311 |
| 3 | 0.32% | 6.8% | 2546 |
| 4 | -0.93% | 7.4% | 2561 |
| 5 | -1.21% | 12.7% | 1913 |

## Top |IC| features

| Feature | IC | IC↑ | IC↓ | Mean fwd when + | Mean fwd when − | n+/n− |
|---|---|---|---|---|---|---|
| Performance (Month) | +0.2369 | -0.1512 | +0.3248 | -0.46% | -0.66% | 5293/6276 |
| upside_pct_lvl | -0.2350 | +0.4258 | -0.4807 | -0.56% | -0.76% | 4301/326 |
| Relative Strength Index (14) | +0.1697 | -0.2157 | +0.2821 | -0.57% | n/a | 11674/0 |
| d_20-Day Simple Moving Average | -0.1659 | +0.1085 | -0.2357 | -0.45% | -1.03% | 9258/2369 |
| d_50-Day Simple Moving Average | -0.1387 | +0.0934 | -0.2006 | -0.45% | -1.17% | 9631/1989 |
| true_ret | -0.1370 | +0.0850 | -0.1942 | -0.69% | -1.30% | 9323/1975 |
| d_Performance (Week) | -0.1244 | +0.1367 | -0.1773 | -0.39% | -1.13% | 8726/2866 |
| d_Forward P/E | -0.1123 | +0.0133 | -0.1085 | -0.65% | -0.70% | 2414/532 |
| d_200-Day Simple Moving Average | -0.1035 | +0.0384 | -0.1231 | -0.42% | -1.19% | 9536/2066 |
| Short Float | -0.0994 | +0.0842 | -0.1973 | -0.35% | n/a | 5597/0 |
| d_Target Price | +0.0937 | -0.0144 | +0.0735 | -0.44% | -1.61% | 393/469 |
| d_Performance (Quarter) | -0.0634 | +0.0522 | -0.0788 | -0.48% | -0.87% | 8588/2607 |
| d_Performance (YTD) | -0.0619 | -0.0049 | -0.0436 | -0.38% | -1.33% | 9381/2025 |
| d_Beta | +0.0594 | -0.1206 | +0.1126 | -0.72% | -1.12% | 2571/2742 |
| d_Performance (Month) | -0.0560 | +0.0857 | -0.1192 | -0.46% | -0.89% | 8642/2839 |
| d_Short Float | +0.0533 | -0.0741 | +0.0721 | -0.39% | -0.94% | 308/372 |
| d_Volatility (Month) | -0.0467 | +0.2198 | -0.1912 | -0.40% | -0.93% | 6062/3779 |
| Institutional Transactions | -0.0411 | +0.1001 | -0.0966 | 0.14% | -1.01% | 3097/1918 |
| d_Average Volume | -0.0397 | +0.0182 | -0.0406 | -0.52% | -0.63% | 6536/4539 |
| Relative Volume | -0.0303 | +0.0589 | -0.1054 | -0.58% | n/a | 11481/0 |
| d_Sales Year Over Year TTM | +0.0276 | -0.0192 | +0.0142 | -0.85% | -1.19% | 222/205 |
| d_Short Ratio | +0.0274 | -0.0171 | +0.0369 | -0.88% | -0.39% | 2836/4221 |
| d_Profit Margin | +0.0249 | +0.0296 | -0.0006 | -0.69% | -1.38% | 219/234 |
| Performance (Week) | -0.0243 | -0.0542 | +0.0066 | -0.69% | -0.39% | 6802/4771 |
| d_Market Cap | +0.0237 | -0.1569 | +0.1938 | -0.09% | -1.49% | 4486/1280 |

## Combinations

| Pattern | n | Mean long fwd | Hit up |
|---|---|---|---|
| true_ret>3% & DOWNTREND | 2139 | -1.70% | 10.6% |
| true_ret>3% & UPTREND | 837 | -0.82% | 15.2% |
| true_ret>3% & MIXED | 642 | -0.67% | 16.5% |

## Risk dominance probes

| State | n | Mean long fwd | Mean fwd if score top quintile |
|---|---|---|---|
| EXTENDED | 343 | 0.36% | 1.75% |
| WASHED | 1502 | -1.81% | -2.74% |

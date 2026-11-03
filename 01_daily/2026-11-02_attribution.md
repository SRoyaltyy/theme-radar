# Factor attribution — signal 2026-11-02 → prediction day 2026-11-03

## Trade window (read this first)

| Role | Date | Meaning |
|------|------|---------|
| **Signal as-of** | **2026-11-02** | Features/scores formed from this snapshot (and deltas vs **2026-10-30**). Only data on/before this date. |
| **Prediction day** | **2026-11-03** | The trading day the forward return is for (exit snapshot). |
| **Entry price** | Price @ 2026-11-02 | Long: buy here; short: sell here. |
| **Exit price** | Price @ 2026-11-03 | Close proxy on prediction day. |
| **Return column** | `fwd_1d` | Long: exit/entry − 1; short = opposite. |

Graded **n=11735** names with valid entry and exit prices.

Provisional until multiple signal dates agree.

_Column guide: **IC** = Spearman(feature, long forward return); **IC↑** / **IC↓** = IC among names that went up / down._

## Score calibration (long fwd)
- Spearman IC(total_score, fwd_1d) = **-0.3312**

| Quintile | Mean long fwd | Hit up>1.5% | n |
|---|---|---|---|
| 1 | 2.05% | 41.1% | 2477 |
| 2 | 0.41% | 14.6% | 2625 |
| 3 | -0.01% | 12.0% | 1941 |
| 4 | 0.24% | 9.2% | 2360 |
| 5 | -0.56% | 16.6% | 2332 |

## Top |IC| features

| Feature | IC | IC↑ | IC↓ | Mean fwd when + | Mean fwd when − | n+/n− |
|---|---|---|---|---|---|---|
| Performance (Month) | -0.3753 | -0.5496 | +0.0100 | -0.52% | 1.23% | 5044/6527 |
| d_Price | -0.3659 | -0.1885 | -0.1425 | -0.39% | 1.06% | 5179/6018 |
| d_Performance (YTD) | -0.3576 | -0.2754 | -0.1808 | -0.37% | 1.04% | 5277/6092 |
| true_ret | -0.3512 | -0.3253 | -0.1986 | -0.39% | 1.06% | 5179/6018 |
| d_200-Day Simple Moving Average | -0.3499 | -0.2675 | -0.2065 | -0.16% | 1.02% | 5483/6114 |
| d_50-Day Simple Moving Average | -0.3420 | -0.2722 | -0.2271 | -0.14% | 1.05% | 5716/5903 |
| Relative Strength Index (14) | -0.3375 | -0.2954 | +0.0797 | 0.46% | n/a | 11653/0 |
| d_Performance (Quarter) | -0.3222 | -0.3547 | -0.0829 | -0.17% | 0.75% | 3316/7888 |
| d_Performance (Week) | -0.3141 | -0.2309 | -0.2397 | -0.07% | 0.88% | 5029/6532 |
| d_Performance (Month) | -0.3016 | -0.2785 | -0.1635 | -0.09% | 0.85% | 4542/6953 |
| d_Relative Strength Index (14) | -0.2908 | +0.0042 | -0.1572 | -0.38% | 1.05% | 5280/6092 |
| d_20-Day Simple Moving Average | -0.2855 | -0.2084 | -0.2284 | -0.05% | 0.97% | 5657/5952 |
| d_Beta | +0.2819 | +0.4302 | -0.0603 | 1.38% | -0.51% | 3610/3660 |
| Performance (Week) | -0.2724 | -0.2837 | -0.0863 | -0.21% | 1.05% | 5350/6238 |
| d_Market Cap | -0.2412 | -0.1496 | +0.0589 | -0.40% | 1.01% | 3048/2678 |
| upside_pct_lvl | +0.2298 | +0.4281 | -0.2503 | 0.57% | -0.65% | 4300/334 |
| d_Forward P/E | -0.2297 | -0.2210 | -0.0518 | -0.68% | 0.54% | 1886/1076 |
| d_Volatility (Month) | +0.1880 | +0.3160 | -0.0687 | 1.05% | -0.10% | 5612/4521 |
| Institutional Transactions | +0.0664 | +0.1130 | -0.0249 | 0.35% | 0.61% | 3193/1832 |
| d_Relative Volume | -0.0536 | -0.0686 | +0.0068 | 0.32% | 0.62% | 5640/5687 |
| Relative Volume | -0.0357 | +0.0350 | -0.0671 | 0.47% | n/a | 11496/0 |
| Short Float | +0.0337 | +0.2705 | -0.1844 | 0.45% | n/a | 5640/0 |
| d_Target Price | -0.0282 | -0.0762 | +0.0368 | -0.21% | 0.49% | 361/329 |
| d_Short Float | -0.0261 | -0.0422 | +0.0441 | -0.17% | -0.32% | 169/137 |
| d_Analyst Recom | -0.0186 | -0.0148 | -0.0310 | -0.38% | -0.06% | 112/146 |

## Combinations

| Pattern | n | Mean long fwd | Hit up |
|---|---|---|---|
| true_ret>3% & DOWNTREND | 463 | -0.04% | 32.6% |
| true_ret>3% & UPTREND | 357 | -1.34% | 8.1% |
| true_ret>3% & MIXED | 318 | -1.37% | 15.7% |

## Risk dominance probes

| State | n | Mean long fwd | Mean fwd if score top quintile |
|---|---|---|---|
| EXTENDED | 270 | -1.57% | -4.28% |
| WASHED | 1780 | 3.27% | 3.56% |

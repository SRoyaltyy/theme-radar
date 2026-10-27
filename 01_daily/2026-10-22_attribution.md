# Factor attribution — signal 2026-10-22 → prediction day 2026-10-27

## Trade window (read this first)

| Role | Date | Meaning |
|------|------|---------|
| **Signal as-of** | **2026-10-22** | Features/scores formed from this snapshot (and deltas vs **2026-10-21**). Only data on/before this date. |
| **Prediction day** | **2026-10-27** | The trading day the forward return is for (exit snapshot). |
| **Entry price** | Price @ 2026-10-22 | Long: buy here; short: sell here. |
| **Exit price** | Price @ 2026-10-27 | Close proxy on prediction day. |
| **Return column** | `fwd_3d` | Long: exit/entry − 1; short = opposite. |

Graded **n=11736** names with valid entry and exit prices.

Provisional until multiple signal dates agree.

_Column guide: **IC** = Spearman(feature, long forward return); **IC↑** / **IC↓** = IC among names that went up / down._

## Score calibration (long fwd)
- Spearman IC(total_score, fwd_3d) = **-0.3132**

| Quintile | Mean long fwd | Hit up>1.5% | n |
|---|---|---|---|
| 1 | 14.11% | 56.9% | 2494 |
| 2 | 2.08% | 25.5% | 2326 |
| 3 | 0.60% | 15.8% | 2513 |
| 4 | -0.13% | 19.7% | 2079 |
| 5 | 0.60% | 17.2% | 2324 |

## Top |IC| features

| Feature | IC | IC↑ | IC↓ | Mean fwd when + | Mean fwd when − | n+/n− |
|---|---|---|---|---|---|---|
| d_Price | -0.4118 | -0.3395 | +0.0577 | 0.22% | 5.81% | 4818/6443 |
| d_Performance (YTD) | -0.4041 | -0.4304 | +0.0095 | 0.22% | 5.39% | 4867/6504 |
| d_200-Day Simple Moving Average | -0.4033 | -0.4354 | -0.0219 | 0.30% | 6.29% | 5001/6580 |
| d_50-Day Simple Moving Average | -0.3890 | -0.4382 | -0.0438 | 0.55% | 6.20% | 5160/6441 |
| d_20-Day Simple Moving Average | -0.3831 | -0.4210 | -0.0671 | 0.62% | 6.15% | 5177/6426 |
| true_ret | -0.3830 | -0.4707 | -0.0130 | 0.22% | 5.81% | 4818/6443 |
| d_Forward P/E | -0.3827 | -0.4005 | -0.0060 | -0.38% | 1.98% | 1793/1174 |
| d_Relative Strength Index (14) | -0.3597 | -0.1500 | +0.1537 | 0.20% | 6.42% | 4869/6490 |
| d_Performance (Month) | -0.3482 | -0.3482 | -0.0953 | 0.21% | 8.38% | 6561/4907 |
| Relative Strength Index (14) | -0.3132 | -0.4421 | +0.2094 | 3.65% | n/a | 11654/0 |
| d_Market Cap | -0.2933 | -0.2845 | +0.0998 | 1.04% | 10.61% | 2831/2890 |
| d_Performance (Week) | -0.2871 | -0.4481 | +0.0740 | 0.53% | 5.14% | 3568/7950 |
| Performance (Month) | -0.2775 | -0.5160 | +0.1089 | 0.15% | 6.01% | 4573/6967 |
| Performance (Week) | -0.2648 | -0.4262 | +0.0969 | 0.40% | 6.17% | 4965/6582 |
| d_Performance (Quarter) | -0.2244 | -0.1741 | -0.0605 | 3.25% | 4.14% | 4902/6274 |
| d_Beta | -0.1792 | -0.3507 | +0.1307 | 3.21% | 12.43% | 1412/2487 |
| upside_pct_lvl | +0.1004 | +0.3784 | -0.2539 | 3.20% | -0.76% | 4292/340 |
| Institutional Transactions | +0.0949 | +0.1434 | -0.0244 | 5.82% | 9.45% | 3254/1788 |
| Relative Volume | +0.0776 | +0.1174 | +0.0306 | 3.74% | n/a | 11444/0 |
| d_Relative Volume | +0.0541 | +0.0625 | +0.0035 | 4.29% | 2.83% | 6650/4669 |
| Short Float | +0.0481 | +0.3163 | -0.1275 | 5.97% | n/a | 5645/0 |
| d_Total Debt/Equity | -0.0444 | +0.0308 | +0.0046 | -0.23% | 1.48% | 36/60 |
| d_Institutional Ownership | +0.0387 | +0.0142 | +0.0288 | 0.83% | 3.92% | 1077/1056 |
| d_Gross Margin | +0.0253 | +0.0250 | -0.0053 | 2.02% | 0.22% | 42/37 |
| d_Analyst Recom | -0.0250 | -0.0327 | +0.0026 | -1.06% | 1.33% | 70/84 |

## Combinations

| Pattern | n | Mean long fwd | Hit up |
|---|---|---|---|
| true_ret>3% & DOWNTREND | 472 | -1.29% | 26.5% |
| true_ret>3% & UPTREND | 448 | -2.51% | 13.8% |
| true_ret>3% & MIXED | 286 | 9.89% | 15.4% |

## Risk dominance probes

| State | n | Mean long fwd | Mean fwd if score top quintile |
|---|---|---|---|
| EXTENDED | 237 | -0.74% | -3.21% |
| WASHED | 1744 | 20.25% | -0.14% |

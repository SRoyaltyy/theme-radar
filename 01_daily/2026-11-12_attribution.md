# Factor attribution — signal 2026-11-12 → prediction day 2026-11-17

## Trade window (read this first)

| Role | Date | Meaning |
|------|------|---------|
| **Signal as-of** | **2026-11-12** | Features/scores formed from this snapshot (and deltas vs **2026-11-11**). Only data on/before this date. |
| **Prediction day** | **2026-11-17** | The trading day the forward return is for (exit snapshot). |
| **Entry price** | Price @ 2026-11-12 | Long: buy here; short: sell here. |
| **Exit price** | Price @ 2026-11-17 | Close proxy on prediction day. |
| **Return column** | `fwd_3d` | Long: exit/entry − 1; short = opposite. |

Graded **n=11706** names with valid entry and exit prices.

Provisional until multiple signal dates agree.

_Column guide: **IC** = Spearman(feature, long forward return); **IC↑** / **IC↓** = IC among names that went up / down._

## Score calibration (long fwd)
- Spearman IC(total_score, fwd_3d) = **-0.0056**

| Quintile | Mean long fwd | Hit up>1.5% | n |
|---|---|---|---|
| 1 | -2.50% | 8.9% | 2529 |
| 2 | 0.66% | 8.4% | 2208 |
| 3 | -1.80% | 3.8% | 2397 |
| 4 | -3.08% | 4.0% | 2396 |
| 5 | -2.74% | 9.9% | 2176 |

## Top |IC| features

| Feature | IC | IC↑ | IC↓ | Mean fwd when + | Mean fwd when − | n+/n− |
|---|---|---|---|---|---|---|
| d_Performance (Week) | -0.4096 | +0.0397 | -0.4144 | -2.76% | 0.16% | 8353/3241 |
| upside_pct_lvl | -0.3969 | +0.4503 | -0.5742 | -1.15% | -2.32% | 4357/267 |
| Performance (Month) | +0.3339 | -0.1241 | +0.4362 | -1.67% | -2.13% | 5358/6189 |
| true_ret | +0.3249 | -0.0749 | +0.3755 | -1.60% | -3.28% | 2051/9280 |
| d_200-Day Simple Moving Average | +0.2778 | -0.0143 | +0.2955 | 3.23% | -3.27% | 2156/9440 |
| d_Performance (YTD) | +0.2747 | -0.0135 | +0.2843 | 3.46% | -3.30% | 2095/9322 |
| Relative Strength Index (14) | +0.2739 | -0.0577 | +0.3815 | -1.92% | n/a | 11656/0 |
| d_50-Day Simple Moving Average | +0.2650 | -0.0344 | +0.2945 | 3.15% | -3.20% | 2308/9303 |
| d_Performance (Month) | -0.2586 | -0.0705 | -0.2552 | -3.49% | 0.00% | 6363/5089 |
| Performance (Week) | -0.2579 | -0.0679 | -0.2456 | -2.48% | -1.03% | 7157/4433 |
| d_20-Day Simple Moving Average | +0.2242 | -0.0426 | +0.2470 | 2.29% | -3.04% | 2407/9206 |
| d_Performance (Quarter) | +0.2237 | -0.0636 | +0.2564 | 1.42% | -2.87% | 2571/8655 |
| Short Float | -0.2159 | +0.1966 | -0.2385 | -0.45% | n/a | 5622/0 |
| d_Price | +0.1852 | +0.1208 | +0.1067 | -1.60% | -3.28% | 2051/9280 |
| d_Volatility (Month) | -0.1498 | +0.1012 | -0.2052 | -3.38% | -0.08% | 5522/4048 |
| Institutional Transactions | -0.0959 | +0.1005 | -0.1282 | 1.16% | -2.38% | 3093/1912 |
| d_Beta | +0.0879 | +0.0119 | +0.1139 | -2.74% | 0.36% | 3156/2201 |
| d_Forward P/E | +0.0706 | -0.0056 | +0.1246 | -2.99% | -2.77% | 707/2208 |
| Relative Volume | -0.0624 | +0.0992 | -0.0728 | -1.96% | n/a | 11461/0 |
| d_Target Price | +0.0542 | -0.0563 | +0.0668 | -3.28% | -4.76% | 277/277 |
| d_Average Volume | -0.0515 | +0.0233 | -0.0582 | -0.67% | -3.16% | 5676/5291 |
| d_Relative Volume | +0.0510 | -0.0189 | +0.0487 | -2.57% | -1.23% | 5857/5393 |
| d_Short Float | +0.0497 | +0.0206 | +0.0737 | -2.35% | -6.96% | 58/130 |
| d_Short Ratio | +0.0435 | -0.0057 | +0.0554 | -3.88% | -1.23% | 3141/3348 |
| d_Relative Strength Index (14) | -0.0419 | +0.2457 | -0.1330 | 3.42% | -3.15% | 2111/9320 |

## Combinations

| Pattern | n | Mean long fwd | Hit up |
|---|---|---|---|
| true_ret>3% & DOWNTREND | 249 | 1.02% | 21.7% |
| true_ret>3% & UPTREND | 81 | -0.89% | 38.3% |
| true_ret>3% & MIXED | 135 | 0.76% | 36.3% |

## Risk dominance probes

| State | n | Mean long fwd | Mean fwd if score top quintile |
|---|---|---|---|
| EXTENDED | 320 | -8.19% | -9.20% |
| WASHED | 1175 | 7.82% | -3.53% |

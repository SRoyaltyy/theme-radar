# Factor attribution — signal 2026-11-10 → prediction day 2026-11-13

## Trade window (read this first)

| Role | Date | Meaning |
|------|------|---------|
| **Signal as-of** | **2026-11-10** | Features/scores formed from this snapshot (and deltas vs **2026-11-09**). Only data on/before this date. |
| **Prediction day** | **2026-11-13** | The trading day the forward return is for (exit snapshot). |
| **Entry price** | Price @ 2026-11-10 | Long: buy here; short: sell here. |
| **Exit price** | Price @ 2026-11-13 | Close proxy on prediction day. |
| **Return column** | `fwd_3d` | Long: exit/entry − 1; short = opposite. |

Graded **n=11731** names with valid entry and exit prices.

Provisional until multiple signal dates agree.

_Column guide: **IC** = Spearman(feature, long forward return); **IC↑** / **IC↓** = IC among names that went up / down._

## Score calibration (long fwd)
- Spearman IC(total_score, fwd_3d) = **-0.0060**

| Quintile | Mean long fwd | Hit up>1.5% | n |
|---|---|---|---|
| 1 | 2.75% | 21.3% | 2613 |
| 2 | -0.53% | 15.1% | 2153 |
| 3 | -0.28% | 8.7% | 2393 |
| 4 | 0.05% | 8.7% | 2462 |
| 5 | -1.74% | 22.1% | 2110 |

## Top |IC| features

| Feature | IC | IC↑ | IC↓ | Mean fwd when + | Mean fwd when − | n+/n− |
|---|---|---|---|---|---|---|
| d_Beta | -0.2742 | -0.1576 | -0.1551 | 0.40% | 1.19% | 4133/2681 |
| d_20-Day Simple Moving Average | +0.2564 | +0.0188 | +0.2673 | -0.38% | 0.38% | 3409/8207 |
| upside_pct_lvl | -0.2008 | +0.4739 | -0.5173 | 0.51% | -1.22% | 4321/312 |
| d_Relative Strength Index (14) | +0.1942 | +0.0968 | -0.0875 | -0.64% | 0.48% | 3139/8270 |
| d_50-Day Simple Moving Average | +0.1833 | -0.0651 | +0.2521 | -0.65% | 0.50% | 3424/8183 |
| true_ret | +0.1793 | -0.1360 | +0.3095 | -0.58% | 0.48% | 3066/8221 |
| Performance (Week) | -0.1719 | -0.3294 | +0.0461 | -1.35% | 1.57% | 5580/5965 |
| d_200-Day Simple Moving Average | +0.1661 | -0.0831 | +0.2384 | -0.73% | 0.24% | 3161/8438 |
| d_Performance (YTD) | +0.1623 | -0.0854 | +0.2265 | -0.59% | 0.24% | 3124/8264 |
| Short Float | -0.1345 | +0.2349 | -0.1807 | 0.78% | n/a | 5623/0 |
| d_Performance (Week) | +0.1269 | -0.1154 | +0.2957 | -0.54% | 0.53% | 4019/7532 |
| d_Forward P/E | +0.1075 | -0.1222 | +0.2046 | -0.33% | 0.13% | 1192/1725 |
| d_Price | +0.1064 | +0.0230 | +0.0303 | -0.58% | 0.48% | 3066/8221 |
| d_Performance (Quarter) | +0.0993 | -0.0928 | +0.1944 | -0.39% | 0.38% | 3042/8202 |
| Relative Strength Index (14) | -0.0851 | -0.3258 | +0.2672 | 0.16% | n/a | 11682/0 |
| Institutional Transactions | -0.0845 | +0.0933 | -0.1193 | 0.17% | 1.96% | 3099/1915 |
| d_Performance (Month) | +0.0788 | -0.0046 | +0.0492 | -0.45% | 0.50% | 4067/7402 |
| d_Market Cap | +0.0780 | -0.0748 | +0.0273 | -1.23% | 2.00% | 2049/3695 |
| d_Institutional Ownership | +0.0712 | -0.0230 | +0.0934 | -0.32% | -2.73% | 383/561 |
| Performance (Month) | -0.0697 | -0.3392 | +0.2653 | -0.88% | 0.97% | 5069/6506 |
| d_EPS Surprise | -0.0412 | -0.0190 | -0.0431 | -2.93% | -1.16% | 107/112 |
| d_Short Float | +0.0375 | +0.0058 | +0.0465 | 0.83% | -17.19% | 2/4 |
| d_Sales Growth Quarter Over Quarter | +0.0367 | +0.0807 | +0.0030 | 0.64% | -3.09% | 110/131 |
| d_Volatility (Month) | -0.0307 | +0.2976 | -0.2895 | -0.29% | 2.09% | 7779/2242 |
| d_Average Volume | +0.0287 | +0.1289 | -0.0305 | 0.17% | 0.23% | 6744/4306 |

## Combinations

| Pattern | n | Mean long fwd | Hit up |
|---|---|---|---|
| true_ret>3% & DOWNTREND | 275 | -2.85% | 30.2% |
| true_ret>3% & UPTREND | 169 | -3.83% | 24.3% |
| true_ret>3% & MIXED | 140 | -1.75% | 31.4% |

## Risk dominance probes

| State | n | Mean long fwd | Mean fwd if score top quintile |
|---|---|---|---|
| EXTENDED | 276 | -3.02% | -4.94% |
| WASHED | 1536 | 6.92% | -0.59% |

# Factor attribution — signal 2026-11-12 → prediction day 2026-11-16

## Trade window (read this first)

| Role | Date | Meaning |
|------|------|---------|
| **Signal as-of** | **2026-11-12** | Features/scores formed from this snapshot (and deltas vs **2026-11-11**). Only data on/before this date. |
| **Prediction day** | **2026-11-16** | The trading day the forward return is for (exit snapshot). |
| **Entry price** | Price @ 2026-11-12 | Long: buy here; short: sell here. |
| **Exit price** | Price @ 2026-11-16 | Close proxy on prediction day. |
| **Return column** | `fwd_2d` | Long: exit/entry − 1; short = opposite. |

Graded **n=11707** names with valid entry and exit prices.

Provisional until multiple signal dates agree.

_Column guide: **IC** = Spearman(feature, long forward return); **IC↑** / **IC↓** = IC among names that went up / down._

## Score calibration (long fwd)
- Spearman IC(total_score, fwd_2d) = **0.0135**

| Quintile | Mean long fwd | Hit up>1.5% | n |
|---|---|---|---|
| 1 | -1.60% | 10.6% | 2529 |
| 2 | -2.25% | 11.3% | 2208 |
| 3 | -0.65% | 4.4% | 2397 |
| 4 | -2.15% | 4.9% | 2397 |
| 5 | -2.10% | 12.4% | 2176 |

## Top |IC| features

| Feature | IC | IC↑ | IC↓ | Mean fwd when + | Mean fwd when − | n+/n− |
|---|---|---|---|---|---|---|
| upside_pct_lvl | -0.4394 | +0.3890 | -0.5955 | -2.09% | -1.04% | 4357/268 |
| d_Performance (Week) | -0.4121 | -0.0000 | -0.4295 | -2.79% | 0.97% | 8354/3241 |
| Performance (Month) | +0.4032 | -0.0387 | +0.4992 | -0.76% | -2.56% | 5359/6189 |
| Relative Strength Index (14) | +0.3362 | -0.0929 | +0.4025 | -1.73% | n/a | 11657/0 |
| true_ret | +0.2984 | -0.1251 | +0.3746 | -1.09% | -2.19% | 2052/9280 |
| Performance (Week) | -0.2829 | -0.1063 | -0.2714 | -2.81% | -0.02% | 7158/4433 |
| d_Performance (Month) | -0.2775 | -0.1442 | -0.2740 | -2.48% | -0.83% | 6364/5089 |
| d_Performance (YTD) | +0.2502 | -0.0625 | +0.2803 | -0.51% | -2.21% | 2096/9322 |
| d_200-Day Simple Moving Average | +0.2457 | -0.0702 | +0.2895 | -0.72% | -2.16% | 2157/9440 |
| d_50-Day Simple Moving Average | +0.2291 | -0.0911 | +0.2882 | -0.22% | -2.12% | 2309/9303 |
| d_Performance (Quarter) | +0.2269 | -0.0789 | +0.2726 | -1.31% | -1.83% | 2571/8656 |
| d_20-Day Simple Moving Average | +0.1804 | -0.1060 | +0.2325 | -0.92% | -1.95% | 2408/9206 |
| d_Volatility (Month) | -0.1713 | +0.1051 | -0.2347 | -2.46% | -1.10% | 5522/4049 |
| Short Float | -0.1507 | +0.1417 | -0.2277 | -1.00% | n/a | 5623/0 |
| d_Price | +0.1506 | +0.0412 | +0.0879 | -1.09% | -2.19% | 2052/9280 |
| d_Beta | +0.1255 | +0.0433 | +0.1340 | -1.67% | -2.69% | 3157/2201 |
| Institutional Transactions | -0.0923 | +0.1148 | -0.1022 | -0.47% | -1.63% | 3094/1912 |
| d_Target Price | +0.0557 | -0.0564 | +0.0644 | -2.12% | -3.41% | 277/277 |
| d_Forward P/E | +0.0547 | -0.1067 | +0.1432 | -1.72% | -1.35% | 708/2208 |
| Relative Volume | -0.0537 | +0.0827 | -0.0843 | -1.76% | n/a | 11462/0 |
| d_Average Volume | -0.0518 | +0.0322 | -0.0710 | -1.36% | -2.11% | 5677/5291 |
| d_Short Float | +0.0474 | -0.0487 | +0.0518 | -1.77% | -4.73% | 58/130 |
| d_Short Ratio | +0.0471 | -0.0061 | +0.0718 | -2.63% | -3.05% | 3141/3349 |
| d_Relative Strength Index (14) | -0.0413 | +0.1475 | -0.1858 | -0.53% | -2.02% | 2112/9320 |
| d_Relative Volume | +0.0386 | -0.0109 | +0.0627 | -1.45% | -2.06% | 5858/5393 |

## Combinations

| Pattern | n | Mean long fwd | Hit up |
|---|---|---|---|
| true_ret>3% & DOWNTREND | 249 | 0.23% | 24.1% |
| true_ret>3% & UPTREND | 81 | -0.25% | 39.5% |
| true_ret>3% & MIXED | 135 | 0.14% | 36.3% |

## Risk dominance probes

| State | n | Mean long fwd | Mean fwd if score top quintile |
|---|---|---|---|
| EXTENDED | 320 | -7.70% | -9.10% |
| WASHED | 1175 | 1.57% | -2.23% |

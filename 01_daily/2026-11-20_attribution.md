# Factor attribution — signal 2026-11-20 → prediction day 2026-11-24

## Trade window (read this first)

| Role | Date | Meaning |
|------|------|---------|
| **Signal as-of** | **2026-11-20** | Features/scores formed from this snapshot (and deltas vs **2026-11-19**). Only data on/before this date. |
| **Prediction day** | **2026-11-24** | The trading day the forward return is for (exit snapshot). |
| **Entry price** | Price @ 2026-11-20 | Long: buy here; short: sell here. |
| **Exit price** | Price @ 2026-11-24 | Close proxy on prediction day. |
| **Return column** | `fwd_2d` | Long: exit/entry − 1; short = opposite. |

Graded **n=11733** names with valid entry and exit prices.

Provisional until multiple signal dates agree.

_Column guide: **IC** = Spearman(feature, long forward return); **IC↑** / **IC↓** = IC among names that went up / down._

## Score calibration (long fwd)
- Spearman IC(total_score, fwd_2d) = **-0.3709**

| Quintile | Mean long fwd | Hit up>1.5% | n |
|---|---|---|---|
| 1 | 5.31% | 90.9% | 2366 |
| 2 | 8.54% | 76.8% | 2643 |
| 3 | 8.09% | 64.7% | 2037 |
| 4 | 5.26% | 51.8% | 2426 |
| 5 | 2.88% | 26.8% | 2261 |

## Top |IC| features

| Feature | IC | IC↑ | IC↓ | Mean fwd when + | Mean fwd when − | n+/n− |
|---|---|---|---|---|---|---|
| d_200-Day Simple Moving Average | -0.4357 | -0.4817 | +0.1143 | 1.08% | 6.78% | 2085/9550 |
| d_Performance (YTD) | -0.4348 | -0.4507 | +0.1005 | 1.08% | 6.86% | 1979/9466 |
| d_Price | -0.4313 | -0.3258 | +0.0378 | 1.05% | 6.56% | 1960/9440 |
| d_50-Day Simple Moving Average | -0.4201 | -0.4998 | +0.1245 | 1.11% | 6.56% | 2201/9450 |
| d_20-Day Simple Moving Average | -0.4081 | -0.4976 | +0.1182 | 2.13% | 6.64% | 2319/9342 |
| true_ret | -0.4064 | -0.5327 | +0.1938 | 1.05% | 6.56% | 1960/9440 |
| d_Performance (Quarter) | -0.3908 | -0.4208 | +0.0839 | 4.60% | 6.62% | 2291/8997 |
| Performance (Week) | -0.3894 | -0.5649 | +0.2534 | 0.52% | 6.53% | 1495/10124 |
| d_Performance (Week) | -0.3786 | -0.4576 | +0.0585 | 3.29% | 6.45% | 2417/9153 |
| d_Performance (Month) | -0.3382 | -0.3638 | +0.0371 | 6.08% | 6.16% | 1867/9642 |
| d_Relative Strength Index (14) | -0.3249 | -0.1775 | +0.1453 | 1.05% | 6.85% | 2003/9441 |
| Performance (Month) | -0.2978 | -0.4844 | +0.2749 | 0.94% | 7.27% | 2142/9442 |
| Relative Strength Index (14) | -0.2739 | -0.2374 | +0.2052 | 6.06% | n/a | 11666/0 |
| d_Volatility (Month) | +0.2484 | +0.4087 | -0.4174 | 6.72% | 5.00% | 7779/2675 |
| Short Float | +0.2389 | +0.2836 | -0.0994 | 9.90% | n/a | 5609/0 |
| d_Market Cap | -0.2090 | -0.0677 | -0.0985 | 4.24% | 10.03% | 948/4776 |
| d_Forward P/E | -0.1939 | -0.2250 | +0.0771 | 2.60% | 3.11% | 454/2446 |
| Relative Volume | +0.1509 | +0.1137 | -0.0331 | 5.79% | n/a | 11553/0 |
| d_Relative Volume | +0.0882 | +0.0774 | -0.0142 | 7.19% | 3.35% | 7344/4042 |
| upside_pct_lvl | +0.0824 | +0.4333 | -0.4788 | 9.66% | 2.03% | 4463/165 |
| d_Short Ratio | -0.0301 | -0.0131 | -0.0038 | 3.61% | 4.15% | 2663/4395 |
| d_Gross Margin | +0.0261 | -0.0032 | +0.0224 | 4.68% | 151.56% | 26/26 |
| d_Average Volume | +0.0230 | +0.0128 | +0.0003 | 7.01% | 4.12% | 6800/4332 |
| d_Institutional Ownership | -0.0192 | -0.0522 | -0.0361 | -2.58% | 6.37% | 9/24 |
| d_EPS Surprise | +0.0179 | +0.0256 | -0.0002 | 4.94% | 2.92% | 14/6 |

## Combinations

| Pattern | n | Mean long fwd | Hit up |
|---|---|---|---|
| true_ret>3% & DOWNTREND | 157 | 12.97% | 45.2% |
| true_ret>3% & UPTREND | 136 | -8.94% | 14.7% |
| true_ret>3% & MIXED | 69 | -5.39% | 30.4% |

## Risk dominance probes

| State | n | Mean long fwd | Mean fwd if score top quintile |
|---|---|---|---|
| EXTENDED | 174 | -6.98% | -14.75% |
| WASHED | 5093 | 10.66% | 9.93% |

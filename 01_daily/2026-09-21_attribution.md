# Factor attribution — signal 2026-09-21 → prediction day 2026-09-23

## Trade window (read this first)

| Role | Date | Meaning |
|------|------|---------|
| **Signal as-of** | **2026-09-21** | Features/scores formed from this snapshot (and deltas vs **2026-09-18**). Only data on/before this date. |
| **Prediction day** | **2026-09-23** | The trading day the forward return is for (exit snapshot). |
| **Entry price** | Price @ 2026-09-21 | Long: buy here; short: sell here. |
| **Exit price** | Price @ 2026-09-23 | Close proxy on prediction day. |
| **Return column** | `fwd_2d` | Long: exit/entry − 1; short = opposite. |

Graded **n=11629** names with valid entry and exit prices.

Provisional until multiple signal dates agree.

_Column guide: **IC** = Spearman(feature, long forward return); **IC↑** / **IC↓** = IC among names that went up / down._

## Score calibration (long fwd)
- Spearman IC(total_score, fwd_2d) = **-0.0452**

| Quintile | Mean long fwd | Hit up>1.5% | n |
|---|---|---|---|
| 1 | 1.03% | 15.3% | 2369 |
| 2 | -0.94% | 6.3% | 2286 |
| 3 | -0.61% | 7.2% | 2520 |
| 4 | -1.01% | 10.2% | 2234 |
| 5 | 0.20% | 17.1% | 2220 |

## Top |IC| features

| Feature | IC | IC↑ | IC↓ | Mean fwd when + | Mean fwd when − | n+/n− |
|---|---|---|---|---|---|---|
| d_Forward P/E | +0.0990 | +0.1797 | +0.0019 | -0.67% | -1.24% | 1652/1285 |
| Relative Strength Index (14) | +0.0964 | -0.1882 | +0.0992 | -0.26% | n/a | 11546/0 |
| Short Float | -0.0958 | +0.1487 | -0.2049 | -0.03% | n/a | 5702/0 |
| upside_pct_lvl | -0.0817 | +0.2500 | -0.2916 | -0.57% | -0.68% | 4354/282 |
| d_20-Day Simple Moving Average | -0.0813 | +0.0665 | -0.1040 | -0.52% | 0.43% | 8363/3186 |
| Relative Volume | -0.0762 | +0.0193 | -0.1130 | -0.26% | n/a | 11435/0 |
| d_50-Day Simple Moving Average | -0.0723 | +0.0528 | -0.0793 | -0.52% | 0.33% | 8012/3528 |
| Performance (Month) | +0.0659 | -0.1596 | +0.1725 | -0.46% | -0.14% | 4296/7151 |
| true_ret | -0.0637 | +0.0180 | -0.0518 | -0.59% | 0.34% | 7648/3532 |
| d_Performance (Week) | -0.0597 | +0.0327 | -0.0668 | -0.52% | 0.29% | 7867/3575 |
| Performance (Week) | +0.0569 | -0.0090 | +0.1019 | -0.36% | -0.13% | 6055/5377 |
| d_200-Day Simple Moving Average | -0.0552 | +0.0362 | -0.0410 | -0.57% | 0.33% | 7854/3677 |
| Institutional Transactions | -0.0547 | +0.0609 | -0.0783 | -0.07% | -0.98% | 3221/1809 |
| d_Relative Volume | +0.0494 | -0.0656 | +0.1792 | -0.19% | -0.29% | 4479/6843 |
| d_Performance (Month) | -0.0489 | +0.0657 | -0.0841 | -0.51% | 0.39% | 8184/3185 |
| d_Performance (YTD) | -0.0462 | +0.0119 | -0.0154 | -0.57% | -0.28% | 7721/3573 |
| d_Average Volume | -0.0444 | +0.0520 | -0.0697 | 0.07% | -0.52% | 5454/5635 |
| d_Performance (Quarter) | -0.0392 | +0.0691 | -0.0429 | -0.42% | 0.15% | 7366/3587 |
| d_Short Ratio | +0.0384 | +0.0075 | +0.0567 | -0.43% | 0.11% | 3674/3767 |
| d_Market Cap | +0.0380 | +0.0387 | +0.0118 | -0.37% | 0.40% | 3170/2553 |
| d_Institutional Ownership | +0.0329 | +0.0071 | +0.0195 | -0.68% | -1.50% | 163/177 |
| d_Price | -0.0255 | -0.0158 | +0.0668 | -0.59% | 0.34% | 7648/3532 |
| d_Sales Year Over Year TTM | +0.0243 | +0.0494 | -0.0034 | 3.68% | -6.05% | 5/2 |
| d_EPS Surprise | -0.0226 | -0.0074 | -0.0150 | 0.56% | 1.81% | 4/4 |
| d_Relative Strength Index (14) | -0.0224 | -0.0514 | +0.2156 | -0.57% | 0.43% | 7701/3580 |

## Combinations

| Pattern | n | Mean long fwd | Hit up |
|---|---|---|---|
| true_ret>3% & DOWNTREND | 538 | 2.67% | 22.7% |
| true_ret>3% & UPTREND | 725 | -1.14% | 18.1% |
| true_ret>3% & MIXED | 296 | 0.39% | 25.3% |

## Risk dominance probes

| State | n | Mean long fwd | Mean fwd if score top quintile |
|---|---|---|---|
| EXTENDED | 236 | -0.79% | 2.35% |
| WASHED | 1114 | 3.55% | 7.15% |

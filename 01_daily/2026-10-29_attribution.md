# Factor attribution — signal 2026-10-29 → prediction day 2026-11-03

## Trade window (read this first)

| Role | Date | Meaning |
|------|------|---------|
| **Signal as-of** | **2026-10-29** | Features/scores formed from this snapshot (and deltas vs **2026-10-28**). Only data on/before this date. |
| **Prediction day** | **2026-11-03** | The trading day the forward return is for (exit snapshot). |
| **Entry price** | Price @ 2026-10-29 | Long: buy here; short: sell here. |
| **Exit price** | Price @ 2026-11-03 | Close proxy on prediction day. |
| **Return column** | `fwd_3d` | Long: exit/entry − 1; short = opposite. |

Graded **n=11727** names with valid entry and exit prices.

Provisional until multiple signal dates agree.

_Column guide: **IC** = Spearman(feature, long forward return); **IC↑** / **IC↓** = IC among names that went up / down._

## Score calibration (long fwd)
- Spearman IC(total_score, fwd_3d) = **0.2750**

| Quintile | Mean long fwd | Hit up>1.5% | n |
|---|---|---|---|
| 1 | -0.65% | 12.0% | 2360 |
| 2 | -1.27% | 8.6% | 2755 |
| 3 | -1.82% | 7.3% | 2228 |
| 4 | -0.14% | 14.3% | 2041 |
| 5 | -0.83% | 28.2% | 2343 |

## Top |IC| features

| Feature | IC | IC↑ | IC↓ | Mean fwd when + | Mean fwd when − | n+/n− |
|---|---|---|---|---|---|---|
| d_Price | +0.3537 | +0.0521 | +0.3312 | -0.70% | -2.78% | 6325/4871 |
| d_Relative Strength Index (14) | +0.3325 | -0.0472 | +0.3332 | -0.70% | -2.72% | 6391/4950 |
| d_Performance (YTD) | +0.3266 | +0.0885 | +0.3165 | -0.70% | -2.76% | 6401/4953 |
| d_200-Day Simple Moving Average | +0.3254 | +0.1393 | +0.2982 | -0.71% | -2.75% | 6550/5028 |
| Performance (Month) | +0.3198 | -0.0618 | +0.4241 | -0.76% | -1.16% | 6282/5269 |
| true_ret | +0.3117 | +0.1430 | +0.3049 | -0.70% | -2.78% | 6325/4871 |
| d_Performance (Week) | -0.3067 | -0.0063 | -0.3358 | -2.36% | 0.21% | 7361/4194 |
| d_50-Day Simple Moving Average | +0.3053 | +0.1762 | +0.2678 | -0.56% | -2.67% | 6793/4805 |
| d_Performance (Month) | +0.2787 | +0.1474 | +0.2651 | -0.42% | -1.70% | 6714/4733 |
| Relative Strength Index (14) | +0.2740 | -0.2587 | +0.4339 | -0.96% | n/a | 11648/0 |
| d_Forward P/E | +0.2648 | +0.0624 | +0.2366 | -0.31% | -3.32% | 2040/919 |
| d_20-Day Simple Moving Average | +0.2612 | +0.1815 | +0.2201 | -0.63% | -2.49% | 6532/5046 |
| d_Market Cap | +0.2597 | -0.0118 | +0.2731 | -0.62% | -0.54% | 3418/2291 |
| d_Performance (Quarter) | +0.2253 | +0.1250 | +0.1704 | -1.04% | -0.66% | 6492/4686 |
| upside_pct_lvl | -0.2226 | +0.3085 | -0.3796 | -1.86% | -1.80% | 4283/349 |
| Performance (Week) | -0.2111 | -0.0739 | -0.2212 | -2.54% | 0.90% | 7853/3718 |
| d_Beta | +0.2108 | -0.1100 | +0.2861 | -1.48% | 3.63% | 982/1701 |
| Short Float | -0.1107 | +0.2711 | -0.2612 | 0.09% | n/a | 5636/0 |
| Institutional Transactions | -0.0956 | -0.0156 | -0.1189 | -1.48% | 2.87% | 3231/1814 |
| d_Volatility (Month) | -0.0410 | +0.1368 | -0.1248 | -1.02% | -1.99% | 4788/4464 |
| Relative Volume | +0.0337 | +0.1407 | -0.0423 | -1.47% | n/a | 11408/0 |
| d_Average Volume | +0.0287 | +0.0064 | +0.0522 | -0.53% | -2.25% | 5377/5622 |
| d_Relative Volume | +0.0269 | +0.0179 | +0.0362 | -1.02% | -1.77% | 5427/5842 |
| d_Sales Growth Quarter Over Quarter | +0.0225 | +0.0437 | +0.0073 | -0.03% | -1.03% | 127/104 |
| d_Short Float | +0.0188 | -0.0233 | +0.0559 | -0.29% | -3.77% | 33/25 |

## Combinations

| Pattern | n | Mean long fwd | Hit up |
|---|---|---|---|
| true_ret>3% & DOWNTREND | 463 | 1.16% | 32.6% |
| true_ret>3% & UPTREND | 323 | -0.86% | 33.1% |
| true_ret>3% & MIXED | 283 | -0.20% | 40.6% |

## Risk dominance probes

| State | n | Mean long fwd | Mean fwd if score top quintile |
|---|---|---|---|
| EXTENDED | 225 | -3.98% | -9.92% |
| WASHED | 1212 | 5.46% | 1.77% |

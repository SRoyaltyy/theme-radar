# Factor attribution — signal 2026-10-29 → prediction day 2026-11-02

## Trade window (read this first)

| Role | Date | Meaning |
|------|------|---------|
| **Signal as-of** | **2026-10-29** | Features/scores formed from this snapshot (and deltas vs **2026-10-28**). Only data on/before this date. |
| **Prediction day** | **2026-11-02** | The trading day the forward return is for (exit snapshot). |
| **Entry price** | Price @ 2026-10-29 | Long: buy here; short: sell here. |
| **Exit price** | Price @ 2026-11-02 | Close proxy on prediction day. |
| **Return column** | `fwd_2d` | Long: exit/entry − 1; short = opposite. |

Graded **n=11727** names with valid entry and exit prices.

Provisional until multiple signal dates agree.

_Column guide: **IC** = Spearman(feature, long forward return); **IC↑** / **IC↓** = IC among names that went up / down._

## Score calibration (long fwd)
- Spearman IC(total_score, fwd_2d) = **0.3184**

| Quintile | Mean long fwd | Hit up>1.5% | n |
|---|---|---|---|
| 1 | -2.66% | 9.5% | 2360 |
| 2 | -1.20% | 8.6% | 2755 |
| 3 | -1.82% | 7.1% | 2228 |
| 4 | -0.33% | 16.4% | 2041 |
| 5 | -0.54% | 34.0% | 2343 |

## Top |IC| features

| Feature | IC | IC↑ | IC↓ | Mean fwd when + | Mean fwd when − | n+/n− |
|---|---|---|---|---|---|---|
| Performance (Month) | +0.4129 | +0.0820 | +0.4597 | -0.46% | -2.33% | 6282/5269 |
| d_Price | +0.4120 | +0.1511 | +0.3371 | -0.56% | -3.55% | 6325/4871 |
| d_Relative Strength Index (14) | +0.3865 | +0.0013 | +0.3196 | -0.57% | -3.49% | 6391/4950 |
| d_Performance (Week) | -0.3814 | -0.1338 | -0.3590 | -3.05% | 0.63% | 7361/4194 |
| d_Performance (YTD) | +0.3811 | +0.1832 | +0.3297 | -0.57% | -3.54% | 6401/4953 |
| d_200-Day Simple Moving Average | +0.3786 | +0.2318 | +0.3119 | -0.63% | -3.48% | 6550/5028 |
| true_ret | +0.3660 | +0.2408 | +0.3231 | -0.56% | -3.55% | 6325/4871 |
| d_50-Day Simple Moving Average | +0.3541 | +0.2672 | +0.2824 | -0.53% | -3.42% | 6793/4805 |
| Relative Strength Index (14) | +0.3365 | -0.1872 | +0.4134 | -1.32% | n/a | 11648/0 |
| upside_pct_lvl | -0.3334 | +0.2411 | -0.3654 | -2.33% | -1.59% | 4283/349 |
| d_Performance (Month) | +0.3306 | +0.2474 | +0.2741 | -0.60% | -2.35% | 6714/4733 |
| d_Market Cap | +0.3137 | +0.0626 | +0.2703 | -0.58% | -1.15% | 3418/2291 |
| d_20-Day Simple Moving Average | +0.2957 | +0.2496 | +0.2242 | -0.65% | -3.12% | 6532/5046 |
| d_Forward P/E | +0.2844 | +0.1118 | +0.2867 | 0.22% | -3.40% | 2040/919 |
| d_Beta | +0.2728 | -0.0599 | +0.3116 | -0.82% | 1.79% | 982/1701 |
| d_Performance (Quarter) | +0.2651 | +0.1919 | +0.1767 | -1.11% | -1.46% | 6492/4686 |
| Performance (Week) | -0.2413 | -0.1056 | -0.2454 | -2.95% | 0.88% | 7853/3718 |
| Institutional Transactions | -0.1347 | -0.0201 | -0.1217 | -1.41% | 1.61% | 3231/1814 |
| Short Float | -0.1251 | +0.2779 | -0.3051 | -0.28% | n/a | 5636/0 |
| d_Volatility (Month) | -0.0616 | +0.1047 | -0.1389 | -1.45% | -2.29% | 4788/4464 |
| Relative Volume | +0.0545 | +0.1691 | -0.0299 | -1.74% | n/a | 11408/0 |
| d_Relative Volume | +0.0345 | +0.0396 | +0.0601 | -0.95% | -2.36% | 5427/5842 |
| d_Short Float | +0.0314 | -0.0339 | +0.0425 | 0.42% | -5.35% | 33/25 |
| d_Target Price | +0.0237 | -0.0100 | +0.0245 | -0.64% | -1.56% | 253/246 |
| d_Average Volume | +0.0234 | -0.0496 | +0.0584 | -0.87% | -2.50% | 5377/5622 |

## Combinations

| Pattern | n | Mean long fwd | Hit up |
|---|---|---|---|
| true_ret>3% & DOWNTREND | 463 | 0.39% | 30.7% |
| true_ret>3% & UPTREND | 323 | -0.36% | 41.5% |
| true_ret>3% & MIXED | 283 | 1.13% | 44.9% |

## Risk dominance probes

| State | n | Mean long fwd | Mean fwd if score top quintile |
|---|---|---|---|
| EXTENDED | 225 | -3.92% | -10.65% |
| WASHED | 1212 | 2.55% | -1.34% |

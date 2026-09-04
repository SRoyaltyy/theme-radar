# Factor attribution — signal 2026-09-02 → prediction day 2026-09-04

## Trade window (read this first)

| Role | Date | Meaning |
|------|------|---------|
| **Signal as-of** | **2026-09-02** | Features/scores formed from this snapshot (and deltas vs **2026-09-01**). Only data on/before this date. |
| **Prediction day** | **2026-09-04** | The trading day the forward return is for (exit snapshot). |
| **Entry price** | Price @ 2026-09-02 | Long: buy here; short: sell here. |
| **Exit price** | Price @ 2026-09-04 | Close proxy on prediction day. |
| **Return column** | `fwd_2d` | Long: exit/entry − 1; short = opposite. |

Graded **n=11628** names with valid entry and exit prices.

Provisional until multiple signal dates agree.

_Column guide: **IC** = Spearman(feature, long forward return); **IC↑** / **IC↓** = IC among names that went up / down._

## Score calibration (long fwd)
- Spearman IC(total_score, fwd_2d) = **-0.1304**

| Quintile | Mean long fwd | Hit up>1.5% | n |
|---|---|---|---|
| 1 | 5.55% | 48.0% | 2348 |
| 2 | 0.66% | 18.7% | 2314 |
| 3 | 0.62% | 15.1% | 2576 |
| 4 | 0.53% | 18.5% | 2064 |
| 5 | 1.08% | 33.0% | 2326 |

## Top |IC| features

| Feature | IC | IC↑ | IC↓ | Mean fwd when + | Mean fwd when − | n+/n− |
|---|---|---|---|---|---|---|
| d_Performance (Month) | -0.2319 | -0.2733 | -0.0327 | 0.64% | 2.26% | 3643/7665 |
| Performance (Week) | -0.1744 | -0.2591 | +0.0099 | 0.53% | 2.25% | 3443/7962 |
| d_Performance (Quarter) | +0.1618 | +0.3291 | -0.0855 | 0.90% | 4.78% | 8641/2217 |
| Performance (Month) | -0.1458 | -0.1598 | -0.0112 | 0.82% | 2.37% | 4719/6681 |
| d_Institutional Ownership | +0.0956 | +0.0372 | +0.0326 | 0.96% | 0.36% | 1874/537 |
| d_Volatility (Month) | -0.0903 | -0.2599 | +0.1292 | 3.30% | 1.10% | 3776/5897 |
| d_20-Day Simple Moving Average | +0.0885 | +0.1879 | -0.0509 | 0.89% | 3.79% | 8203/3288 |
| d_Price | +0.0834 | +0.0569 | +0.0389 | 0.86% | 3.99% | 7768/3236 |
| Relative Strength Index (14) | -0.0803 | -0.0171 | -0.0161 | 1.72% | n/a | 11518/0 |
| d_50-Day Simple Moving Average | +0.0705 | +0.1835 | -0.0713 | 0.86% | 3.76% | 8088/3404 |
| d_Performance (YTD) | +0.0552 | +0.1221 | -0.0311 | 0.86% | 3.93% | 7876/3311 |
| d_Beta | +0.0482 | +0.0478 | +0.0453 | 1.12% | 3.70% | 3803/2926 |
| d_200-Day Simple Moving Average | +0.0476 | +0.1398 | -0.0620 | 0.84% | 3.82% | 8040/3413 |
| true_ret | +0.0475 | +0.1320 | -0.0486 | 0.86% | 3.99% | 7768/3236 |
| d_Forward P/E | -0.0474 | -0.0032 | -0.0634 | 0.84% | 1.03% | 2008/943 |
| Short Float | +0.0432 | +0.1722 | -0.1481 | 2.38% | n/a | 5702/0 |
| d_Performance (Week) | +0.0383 | +0.1622 | -0.0864 | 0.87% | 3.82% | 8019/3366 |
| upside_pct_lvl | +0.0360 | +0.3358 | -0.2807 | 0.99% | -0.01% | 4324/328 |
| d_Average Volume | -0.0354 | -0.1329 | +0.0387 | 3.02% | 0.94% | 4367/6697 |
| d_Short Ratio | +0.0275 | +0.0817 | -0.0260 | 0.99% | 4.25% | 4436/2664 |
| Relative Volume | -0.0275 | -0.0032 | +0.0292 | 1.74% | n/a | 11355/0 |
| d_Analyst Recom | -0.0228 | +0.0037 | +0.0096 | 0.84% | 1.07% | 75/105 |
| d_Relative Strength Index (14) | +0.0214 | -0.1233 | +0.0763 | 0.85% | 3.94% | 7843/3303 |
| d_Gross Margin | +0.0198 | +0.0139 | +0.0246 | 0.67% | -2.44% | 12/10 |
| d_Market Cap | +0.0195 | -0.0065 | +0.0305 | 0.60% | 5.36% | 3609/2100 |

## Combinations

| Pattern | n | Mean long fwd | Hit up |
|---|---|---|---|
| true_ret>3% & DOWNTREND | 442 | 2.75% | 45.5% |
| true_ret>3% & UPTREND | 432 | 0.38% | 35.9% |
| true_ret>3% & MIXED | 304 | 1.56% | 39.8% |

## Risk dominance probes

| State | n | Mean long fwd | Mean fwd if score top quintile |
|---|---|---|---|
| EXTENDED | 200 | 1.44% | 0.90% |
| WASHED | 840 | 12.33% | 1.19% |

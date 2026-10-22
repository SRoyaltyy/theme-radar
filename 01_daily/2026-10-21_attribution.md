# Factor attribution — signal 2026-10-21 → prediction day 2026-10-22

## Trade window (read this first)

| Role | Date | Meaning |
|------|------|---------|
| **Signal as-of** | **2026-10-21** | Features/scores formed from this snapshot (and deltas vs **2026-10-20**). Only data on/before this date. |
| **Prediction day** | **2026-10-22** | The trading day the forward return is for (exit snapshot). |
| **Entry price** | Price @ 2026-10-21 | Long: buy here; short: sell here. |
| **Exit price** | Price @ 2026-10-22 | Close proxy on prediction day. |
| **Return column** | `fwd_1d` | Long: exit/entry − 1; short = opposite. |

Graded **n=11755** names with valid entry and exit prices.

Provisional until multiple signal dates agree.

_Column guide: **IC** = Spearman(feature, long forward return); **IC↑** / **IC↓** = IC among names that went up / down._

## Score calibration (long fwd)
- Spearman IC(total_score, fwd_1d) = **-0.0789**

| Quintile | Mean long fwd | Hit up>1.5% | n |
|---|---|---|---|
| 1 | 1.71% | 27.0% | 2363 |
| 2 | -0.48% | 18.2% | 3013 |
| 3 | -0.98% | 15.3% | 1711 |
| 4 | -0.47% | 16.8% | 2444 |
| 5 | -2.35% | 21.4% | 2224 |

## Top |IC| features

| Feature | IC | IC↑ | IC↓ | Mean fwd when + | Mean fwd when − | n+/n− |
|---|---|---|---|---|---|---|
| d_Performance (Week) | -0.5197 | -0.1104 | -0.5744 | -1.02% | 1.16% | 8593/2898 |
| d_20-Day Simple Moving Average | -0.4610 | -0.2416 | -0.4610 | -1.91% | 2.23% | 7518/4016 |
| d_50-Day Simple Moving Average | -0.4006 | -0.1875 | -0.3904 | -1.70% | 2.07% | 7789/3762 |
| d_200-Day Simple Moving Average | -0.3955 | -0.2067 | -0.3441 | -1.78% | 1.84% | 7321/4175 |
| d_Performance (YTD) | -0.3934 | -0.2211 | -0.3092 | -1.80% | 1.83% | 7104/4097 |
| d_Relative Strength Index (14) | -0.3924 | -0.2361 | -0.0854 | -1.80% | 1.83% | 7113/4116 |
| true_ret | -0.3872 | -0.2230 | -0.3461 | -1.81% | 1.94% | 7017/3996 |
| d_Price | -0.3836 | -0.2337 | -0.2282 | -1.81% | 1.94% | 7017/3996 |
| Performance (Month) | +0.3549 | -0.0056 | +0.5300 | 0.52% | -0.90% | 3624/7935 |
| d_Forward P/E | -0.3394 | -0.1304 | -0.2753 | -0.93% | 1.51% | 1508/1420 |
| d_Performance (Quarter) | -0.3249 | -0.0456 | -0.3127 | -1.26% | 2.04% | 8310/2868 |
| upside_pct_lvl | -0.3051 | +0.0528 | -0.2649 | -0.44% | 0.42% | 4324/310 |
| Relative Strength Index (14) | +0.2780 | -0.0213 | +0.4232 | -0.46% | n/a | 11675/0 |
| d_Market Cap | -0.2545 | -0.1330 | -0.1298 | -1.20% | 2.38% | 2906/2772 |
| d_Beta | +0.2417 | -0.0356 | +0.3235 | 0.70% | 0.50% | 679/1708 |
| Performance (Week) | +0.2347 | +0.1668 | +0.2250 | -0.22% | -0.90% | 7427/4117 |
| d_Performance (Month) | -0.1765 | -0.1369 | -0.0912 | -1.32% | 0.64% | 6386/5002 |
| Short Float | +0.0891 | +0.2741 | -0.2182 | 0.59% | n/a | 5638/0 |
| Relative Volume | +0.0865 | +0.0765 | -0.0631 | -0.46% | n/a | 11389/0 |
| Institutional Transactions | -0.0814 | +0.0127 | -0.0750 | 1.17% | -0.29% | 3260/1788 |
| d_Average Volume | +0.0550 | +0.0002 | +0.0004 | 0.07% | -1.00% | 5947/5049 |
| d_Analyst Recom | +0.0491 | +0.0083 | +0.0162 | 0.98% | -0.93% | 83/54 |
| d_Short Ratio | -0.0453 | +0.0074 | -0.0062 | -0.85% | -0.63% | 3161/3690 |
| d_Sales Year Over Year TTM | -0.0267 | -0.0224 | -0.0055 | 0.56% | 2.64% | 30/31 |
| d_Gross Margin | -0.0238 | -0.0582 | -0.0200 | -0.55% | 3.75% | 24/16 |

## Combinations

| Pattern | n | Mean long fwd | Hit up |
|---|---|---|---|
| true_ret>3% & DOWNTREND | 652 | -6.47% | 12.0% |
| true_ret>3% & UPTREND | 255 | -3.35% | 17.6% |
| true_ret>3% & MIXED | 185 | -5.86% | 11.4% |

## Risk dominance probes

| State | n | Mean long fwd | Mean fwd if score top quintile |
|---|---|---|---|
| EXTENDED | 157 | 0.83% | 0.44% |
| WASHED | 1475 | -0.01% | -5.70% |

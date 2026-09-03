# Factor attribution — signal 2026-09-02 → prediction day 2026-09-03

## Trade window (read this first)

| Role | Date | Meaning |
|------|------|---------|
| **Signal as-of** | **2026-09-02** | Features/scores formed from this snapshot (and deltas vs **2026-09-01**). Only data on/before this date. |
| **Prediction day** | **2026-09-03** | The trading day the forward return is for (exit snapshot). |
| **Entry price** | Price @ 2026-09-02 | Long: buy here; short: sell here. |
| **Exit price** | Price @ 2026-09-03 | Close proxy on prediction day. |
| **Return column** | `fwd_1d` | Long: exit/entry − 1; short = opposite. |

Graded **n=11629** names with valid entry and exit prices.

Provisional until multiple signal dates agree.

_Column guide: **IC** = Spearman(feature, long forward return); **IC↑** / **IC↓** = IC among names that went up / down._

## Score calibration (long fwd)
- Spearman IC(total_score, fwd_1d) = **-0.0842**

| Quintile | Mean long fwd | Hit up>1.5% | n |
|---|---|---|---|
| 1 | 1.24% | 33.5% | 2349 |
| 2 | 0.53% | 15.1% | 2314 |
| 3 | 0.68% | 12.4% | 2576 |
| 4 | 0.65% | 16.0% | 2064 |
| 5 | 0.44% | 26.8% | 2326 |

## Top |IC| features

| Feature | IC | IC↑ | IC↓ | Mean fwd when + | Mean fwd when − | n+/n− |
|---|---|---|---|---|---|---|
| d_Performance (Month) | -0.1822 | -0.2384 | -0.0102 | 0.35% | 0.91% | 3643/7666 |
| d_Performance (Quarter) | +0.1731 | +0.3433 | -0.1113 | 0.88% | -0.04% | 8641/2218 |
| Performance (Week) | -0.1235 | -0.2307 | +0.0590 | 0.26% | 0.91% | 3443/7963 |
| d_Forward P/E | -0.1176 | -0.1105 | -0.1131 | 0.53% | 1.06% | 2008/943 |
| d_Price | +0.0728 | -0.0014 | -0.0034 | 0.63% | 0.98% | 7768/3237 |
| upside_pct_lvl | -0.0587 | +0.2968 | -0.3363 | 0.51% | 0.07% | 4324/328 |
| d_Average Volume | -0.0488 | -0.1386 | +0.0388 | 0.59% | 0.79% | 4368/6697 |
| d_Short Ratio | +0.0462 | +0.1020 | -0.0335 | 0.83% | 0.58% | 4436/2664 |
| d_Institutional Ownership | +0.0373 | +0.0048 | +0.0304 | 0.58% | 0.48% | 1874/537 |
| d_Sales Growth Quarter Over Quarter | +0.0334 | -0.0002 | +0.0275 | 0.74% | -1.75% | 8/11 |
| d_Sales Year Over Year TTM | +0.0334 | +0.0308 | +0.0198 | 0.93% | -2.40% | 9/9 |
| d_Performance (Week) | +0.0321 | +0.1338 | -0.1062 | 0.78% | 0.60% | 8019/3367 |
| Relative Volume | -0.0320 | -0.0234 | +0.0284 | 0.72% | n/a | 11356/0 |
| d_EPS Surprise | +0.0313 | +0.0143 | +0.0645 | 2.29% | -1.27% | 23/17 |
| d_Target Price | +0.0308 | +0.0200 | +0.0160 | 0.99% | 0.52% | 135/128 |
| d_Relative Volume | -0.0274 | +0.0096 | -0.0335 | 0.60% | 0.82% | 4973/6187 |
| d_Short Float | -0.0268 | -0.0240 | +0.0042 | -1.19% | 0.65% | 43/82 |
| Relative Strength Index (14) | +0.0263 | +0.0673 | +0.0136 | 0.72% | n/a | 11519/0 |
| Institutional Transactions | -0.0252 | +0.0183 | -0.0881 | 0.49% | 0.47% | 3183/1858 |
| Performance (Month) | -0.0234 | -0.0471 | +0.0513 | 0.92% | 0.58% | 4719/6682 |
| Short Float | +0.0219 | +0.1366 | -0.1603 | 0.41% | n/a | 5703/0 |
| d_Profit Margin | +0.0210 | +0.0252 | -0.0055 | 0.12% | -2.24% | 11/9 |
| d_Analyst Recom | -0.0174 | +0.0028 | -0.0351 | 0.88% | 1.11% | 75/105 |
| d_20-Day Simple Moving Average | +0.0169 | +0.0881 | -0.1139 | 0.59% | 1.03% | 8203/3289 |
| d_Gross Margin | +0.0157 | +0.0144 | +0.0041 | 0.01% | -1.27% | 12/10 |

## Combinations

| Pattern | n | Mean long fwd | Hit up |
|---|---|---|---|
| true_ret>3% & DOWNTREND | 442 | 1.15% | 33.7% |
| true_ret>3% & UPTREND | 432 | -0.16% | 31.2% |
| true_ret>3% & MIXED | 304 | 1.52% | 35.2% |

## Risk dominance probes

| State | n | Mean long fwd | Mean fwd if score top quintile |
|---|---|---|---|
| EXTENDED | 200 | 2.38% | 0.58% |
| WASHED | 841 | 0.27% | 0.09% |

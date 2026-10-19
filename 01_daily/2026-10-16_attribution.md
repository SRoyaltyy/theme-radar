# Factor attribution — signal 2026-10-16 → prediction day 2026-10-19

## Trade window (read this first)

| Role | Date | Meaning |
|------|------|---------|
| **Signal as-of** | **2026-10-16** | Features/scores formed from this snapshot (and deltas vs **2026-10-15**). Only data on/before this date. |
| **Prediction day** | **2026-10-19** | The trading day the forward return is for (exit snapshot). |
| **Entry price** | Price @ 2026-10-16 | Long: buy here; short: sell here. |
| **Exit price** | Price @ 2026-10-19 | Close proxy on prediction day. |
| **Return column** | `fwd_1d` | Long: exit/entry − 1; short = opposite. |

Graded **n=11733** names with valid entry and exit prices.

Provisional until multiple signal dates agree.

_Column guide: **IC** = Spearman(feature, long forward return); **IC↑** / **IC↓** = IC among names that went up / down._

## Score calibration (long fwd)
- Spearman IC(total_score, fwd_1d) = **-0.2579**

| Quintile | Mean long fwd | Hit up>1.5% | n |
|---|---|---|---|
| 1 | 2.64% | 24.1% | 2495 |
| 2 | 2.67% | 18.3% | 2247 |
| 3 | -0.28% | 10.8% | 2347 |
| 4 | -0.29% | 4.2% | 2655 |
| 5 | -0.70% | 8.6% | 1989 |

## Top |IC| features

| Feature | IC | IC↑ | IC↓ | Mean fwd when + | Mean fwd when − | n+/n− |
|---|---|---|---|---|---|---|
| d_Relative Strength Index (14) | -0.3582 | +0.0597 | +0.0346 | -0.65% | 1.51% | 3370/8002 |
| d_Price | -0.3485 | -0.2542 | +0.0313 | -0.66% | 1.30% | 3295/7950 |
| d_Performance (YTD) | -0.3263 | -0.4575 | +0.1141 | -0.63% | 1.51% | 3351/8024 |
| d_200-Day Simple Moving Average | -0.3174 | -0.4682 | +0.1083 | -0.66% | 1.49% | 3508/8088 |
| d_20-Day Simple Moving Average | -0.3136 | -0.4845 | +0.0667 | -0.22% | 1.38% | 3859/7728 |
| d_50-Day Simple Moving Average | -0.3074 | -0.4883 | +0.0977 | -0.69% | 1.60% | 3819/7796 |
| d_Performance (Week) | -0.2980 | -0.4613 | +0.0579 | 0.93% | 0.82% | 3154/8385 |
| d_Performance (Quarter) | -0.2818 | -0.3404 | +0.0268 | 0.55% | 1.10% | 4824/6369 |
| true_ret | -0.2754 | -0.5268 | +0.1538 | -0.66% | 1.30% | 3295/7950 |
| d_Performance (Month) | -0.2420 | -0.4631 | +0.1668 | -0.70% | 1.30% | 2601/8873 |
| Performance (Week) | -0.2387 | -0.4971 | +0.2080 | -0.49% | 1.66% | 4370/7205 |
| d_Forward P/E | -0.2201 | -0.3131 | +0.0711 | -0.52% | -0.05% | 1160/1787 |
| d_Market Cap | -0.1751 | -0.1499 | +0.0566 | -0.65% | 2.72% | 1871/3871 |
| Relative Strength Index (14) | -0.1097 | -0.3350 | +0.2690 | 0.84% | n/a | 11647/0 |
| d_Volatility (Month) | +0.0988 | +0.2894 | -0.1296 | 1.75% | 0.17% | 5077/5012 |
| d_Target Price | +0.0774 | +0.0365 | +0.0053 | 0.37% | -0.84% | 187/316 |
| Short Float | +0.0611 | +0.2491 | -0.0885 | 1.64% | n/a | 5660/0 |
| Performance (Month) | +0.0480 | -0.3717 | +0.3492 | -0.11% | 1.24% | 3396/8143 |
| d_Average Volume | -0.0392 | +0.0931 | -0.0575 | 1.53% | -0.11% | 6739/4317 |
| d_Profit Margin | +0.0352 | -0.0102 | +0.0373 | -0.54% | -2.69% | 14/16 |
| d_Analyst Recom | -0.0233 | -0.0401 | +0.0058 | -0.47% | 0.44% | 71/78 |
| d_Gross Margin | +0.0230 | +0.0019 | +0.0033 | -1.39% | -2.67% | 7/11 |
| d_Relative Volume | +0.0205 | -0.0404 | +0.0001 | 0.48% | 1.16% | 4811/6515 |
| Institutional Transactions | +0.0201 | +0.1171 | -0.0852 | 1.22% | 3.22% | 3260/1776 |
| d_Short Ratio | +0.0186 | -0.0709 | +0.0499 | -0.09% | -0.06% | 2672/4516 |

## Combinations

| Pattern | n | Mean long fwd | Hit up |
|---|---|---|---|
| true_ret>3% & DOWNTREND | 166 | -2.92% | 18.1% |
| true_ret>3% & UPTREND | 111 | -0.91% | 17.1% |
| true_ret>3% & MIXED | 84 | -1.61% | 15.5% |

## Risk dominance probes

| State | n | Mean long fwd | Mean fwd if score top quintile |
|---|---|---|---|
| EXTENDED | 140 | -1.52% | -0.96% |
| WASHED | 1710 | 6.49% | -1.20% |

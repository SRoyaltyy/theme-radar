# Factor attribution — signal 2026-09-10 → prediction day 2026-09-14

## Trade window (read this first)

| Role | Date | Meaning |
|------|------|---------|
| **Signal as-of** | **2026-09-10** | Features/scores formed from this snapshot (and deltas vs **2026-09-09**). Only data on/before this date. |
| **Prediction day** | **2026-09-14** | The trading day the forward return is for (exit snapshot). |
| **Entry price** | Price @ 2026-09-10 | Long: buy here; short: sell here. |
| **Exit price** | Price @ 2026-09-14 | Close proxy on prediction day. |
| **Return column** | `fwd_2d` | Long: exit/entry − 1; short = opposite. |

Graded **n=11594** names with valid entry and exit prices.

Provisional until multiple signal dates agree.

_Column guide: **IC** = Spearman(feature, long forward return); **IC↑** / **IC↓** = IC among names that went up / down._

## Score calibration (long fwd)
- Spearman IC(total_score, fwd_2d) = **0.1308**

| Quintile | Mean long fwd | Hit up>1.5% | n |
|---|---|---|---|
| 1 | 5.77% | 21.9% | 2353 |
| 2 | 0.37% | 9.5% | 3820 |
| 3 | -0.06% | 25.7% | 934 |
| 4 | 0.20% | 17.1% | 2425 |
| 5 | 3.59% | 31.6% | 2062 |

## Top |IC| features

| Feature | IC | IC↑ | IC↓ | Mean fwd when + | Mean fwd when − | n+/n− |
|---|---|---|---|---|---|---|
| d_Performance (Month) | +0.1882 | -0.0349 | +0.3072 | 2.91% | 1.75% | 2755/8557 |
| d_Forward P/E | +0.1615 | -0.0403 | +0.2925 | 0.96% | 0.13% | 990/1941 |
| Performance (Week) | -0.1585 | -0.2639 | +0.0143 | 1.38% | 2.23% | 3053/8367 |
| d_Performance (YTD) | +0.1580 | -0.0426 | +0.2622 | 3.87% | 1.33% | 2353/8923 |
| true_ret | +0.1555 | -0.0897 | +0.3160 | 3.29% | 1.56% | 2285/8855 |
| d_Relative Strength Index (14) | +0.1471 | +0.3628 | -0.1923 | 3.84% | 1.54% | 2365/8888 |
| d_200-Day Simple Moving Average | +0.1434 | -0.0522 | +0.2611 | 3.72% | 1.52% | 2436/9062 |
| upside_pct_lvl | -0.1384 | +0.2561 | -0.4022 | 4.82% | 0.14% | 4387/258 |
| d_20-Day Simple Moving Average | +0.1343 | -0.0746 | +0.2622 | 3.31% | 1.57% | 2745/8776 |
| d_Performance (Week) | +0.1150 | -0.0914 | +0.3000 | 4.31% | 1.46% | 2143/9291 |
| d_50-Day Simple Moving Average | +0.1140 | -0.1067 | +0.2652 | 3.56% | 1.54% | 2504/9004 |
| d_Beta | +0.1040 | +0.0888 | +0.0239 | 8.52% | 5.05% | 1747/1161 |
| Short Float | +0.0987 | +0.2308 | -0.1830 | 4.12% | n/a | 5701/0 |
| d_Price | +0.0983 | +0.0892 | +0.0636 | 3.29% | 1.56% | 2285/8855 |
| d_Performance (Quarter) | +0.0695 | +0.0040 | +0.0491 | 1.67% | 2.66% | 5353/5557 |
| d_Market Cap | +0.0611 | -0.0076 | +0.0566 | 4.60% | 3.82% | 1848/3863 |
| Institutional Transactions | -0.0538 | +0.0205 | -0.0590 | 5.35% | 2.40% | 3199/1831 |
| d_Institutional Ownership | -0.0532 | +0.0032 | -0.0142 | -0.09% | 0.63% | 242/876 |
| d_Volatility (Month) | +0.0493 | -0.0836 | +0.1271 | 4.12% | 0.96% | 4415/4874 |
| d_Average Volume | +0.0434 | -0.0402 | +0.1169 | 4.52% | 0.54% | 4225/6783 |
| d_EPS Surprise | -0.0431 | -0.0520 | +0.0028 | 7.77% | 5.66% | 6/13 |
| Relative Volume | +0.0398 | +0.0573 | +0.0708 | 2.01% | n/a | 11362/0 |
| d_Gross Margin | +0.0319 | +0.0613 | -0.0288 | 6.17% | 1.83% | 21/11 |
| d_Total Debt/Equity | -0.0292 | -0.0699 | +0.0107 | 1.46% | 7.91% | 10/17 |
| Performance (Month) | +0.0222 | -0.1121 | +0.1571 | 1.24% | 2.34% | 3356/8042 |

## Combinations

| Pattern | n | Mean long fwd | Hit up |
|---|---|---|---|
| true_ret>3% & DOWNTREND | 217 | 12.20% | 45.6% |
| true_ret>3% & UPTREND | 141 | -0.50% | 34.8% |
| true_ret>3% & MIXED | 73 | 56.67% | 42.5% |

## Risk dominance probes

| State | n | Mean long fwd | Mean fwd if score top quintile |
|---|---|---|---|
| EXTENDED | 202 | -0.31% | -0.71% |
| WASHED | 1563 | 4.85% | 7.20% |

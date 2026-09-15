# Factor attribution — signal 2026-09-10 → prediction day 2026-09-15

## Trade window (read this first)

| Role | Date | Meaning |
|------|------|---------|
| **Signal as-of** | **2026-09-10** | Features/scores formed from this snapshot (and deltas vs **2026-09-09**). Only data on/before this date. |
| **Prediction day** | **2026-09-15** | The trading day the forward return is for (exit snapshot). |
| **Entry price** | Price @ 2026-09-10 | Long: buy here; short: sell here. |
| **Exit price** | Price @ 2026-09-15 | Close proxy on prediction day. |
| **Return column** | `fwd_3d` | Long: exit/entry − 1; short = opposite. |

Graded **n=11594** names with valid entry and exit prices.

Provisional until multiple signal dates agree.

_Column guide: **IC** = Spearman(feature, long forward return); **IC↑** / **IC↓** = IC among names that went up / down._

## Score calibration (long fwd)
- Spearman IC(total_score, fwd_3d) = **0.1827**

| Quintile | Mean long fwd | Hit up>1.5% | n |
|---|---|---|---|
| 1 | 4.10% | 16.7% | 2353 |
| 2 | -0.43% | 5.9% | 3820 |
| 3 | -0.79% | 18.7% | 934 |
| 4 | -0.18% | 12.6% | 2425 |
| 5 | 2.53% | 27.4% | 2062 |

## Top |IC| features

| Feature | IC | IC↑ | IC↓ | Mean fwd when + | Mean fwd when − | n+/n− |
|---|---|---|---|---|---|---|
| true_ret | +0.2938 | -0.0330 | +0.3555 | 2.61% | 0.56% | 2285/8855 |
| upside_pct_lvl | -0.2885 | +0.1996 | -0.4243 | 3.32% | 0.04% | 4387/258 |
| d_Performance (YTD) | +0.2780 | -0.0034 | +0.2853 | 3.20% | 0.35% | 2353/8923 |
| d_20-Day Simple Moving Average | +0.2639 | -0.0172 | +0.2971 | 2.68% | 0.54% | 2745/8776 |
| d_200-Day Simple Moving Average | +0.2634 | -0.0102 | +0.2843 | 2.96% | 0.54% | 2436/9062 |
| d_Performance (Month) | +0.2550 | -0.0279 | +0.3238 | 2.14% | 0.75% | 2755/8557 |
| d_50-Day Simple Moving Average | +0.2484 | -0.0431 | +0.2986 | 2.69% | 0.59% | 2504/9004 |
| d_Performance (Week) | +0.2320 | -0.0433 | +0.3094 | 3.04% | 0.60% | 2143/9291 |
| d_Forward P/E | +0.2111 | -0.0160 | +0.2472 | 0.50% | -0.75% | 990/1941 |
| d_Price | +0.1913 | +0.0995 | +0.0330 | 2.61% | 0.56% | 2285/8855 |
| d_Relative Strength Index (14) | +0.1515 | +0.2890 | -0.2178 | 3.17% | 0.52% | 2365/8888 |
| d_Market Cap | +0.1078 | -0.0074 | +0.0368 | 3.44% | 2.51% | 1848/3863 |
| Performance (Month) | +0.0838 | -0.1311 | +0.1729 | 0.18% | 1.44% | 3356/8042 |
| Relative Strength Index (14) | +0.0559 | -0.0063 | -0.1559 | 1.06% | n/a | 11513/0 |
| Institutional Transactions | -0.0470 | +0.0372 | -0.0833 | 3.94% | 1.37% | 3199/1831 |
| Performance (Week) | -0.0458 | -0.2245 | +0.0603 | 0.34% | 1.33% | 3053/8367 |
| d_Beta | +0.0417 | +0.0610 | -0.0021 | 7.11% | 3.66% | 1747/1161 |
| d_Average Volume | +0.0401 | -0.0316 | +0.0907 | 3.48% | -0.34% | 4225/6783 |
| d_Performance (Quarter) | +0.0374 | -0.0440 | +0.0771 | 0.63% | 1.80% | 5353/5557 |
| d_Institutional Ownership | -0.0350 | +0.0058 | -0.0148 | -0.40% | -0.31% | 242/876 |
| d_EPS Surprise | -0.0336 | -0.0336 | -0.0030 | 11.09% | 3.92% | 6/13 |
| d_Gross Margin | +0.0323 | +0.0851 | -0.0122 | 7.23% | -0.19% | 21/11 |
| d_Total Debt/Equity | -0.0302 | -0.0548 | +0.0183 | -0.77% | 8.06% | 10/17 |
| Relative Volume | +0.0277 | +0.1051 | +0.0221 | 1.07% | n/a | 11362/0 |
| d_Target Price | +0.0253 | +0.0233 | +0.0283 | -0.06% | -0.93% | 199/134 |

## Combinations

| Pattern | n | Mean long fwd | Hit up |
|---|---|---|---|
| true_ret>3% & DOWNTREND | 217 | 11.13% | 41.9% |
| true_ret>3% & UPTREND | 141 | -0.18% | 34.0% |
| true_ret>3% & MIXED | 73 | 50.99% | 37.0% |

## Risk dominance probes

| State | n | Mean long fwd | Mean fwd if score top quintile |
|---|---|---|---|
| EXTENDED | 202 | -2.05% | 1.08% |
| WASHED | 1563 | 3.59% | 7.20% |

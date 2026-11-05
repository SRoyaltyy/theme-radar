# Factor attribution — signal 2026-11-04 → prediction day 2026-11-05

## Trade window (read this first)

| Role | Date | Meaning |
|------|------|---------|
| **Signal as-of** | **2026-11-04** | Features/scores formed from this snapshot (and deltas vs **2026-11-03**). Only data on/before this date. |
| **Prediction day** | **2026-11-05** | The trading day the forward return is for (exit snapshot). |
| **Entry price** | Price @ 2026-11-04 | Long: buy here; short: sell here. |
| **Exit price** | Price @ 2026-11-05 | Close proxy on prediction day. |
| **Return column** | `fwd_1d` | Long: exit/entry − 1; short = opposite. |

Graded **n=11741** names with valid entry and exit prices.

Provisional until multiple signal dates agree.

_Column guide: **IC** = Spearman(feature, long forward return); **IC↑** / **IC↓** = IC among names that went up / down._

## Score calibration (long fwd)
- Spearman IC(total_score, fwd_1d) = **0.1371**

| Quintile | Mean long fwd | Hit up>1.5% | n |
|---|---|---|---|
| 1 | -5.37% | 6.8% | 2358 |
| 2 | -3.27% | 2.6% | 2734 |
| 3 | -2.53% | 2.9% | 2089 |
| 4 | -3.18% | 6.1% | 2615 |
| 5 | -3.47% | 8.5% | 1945 |

## Top |IC| features

| Feature | IC | IC↑ | IC↓ | Mean fwd when + | Mean fwd when − | n+/n− |
|---|---|---|---|---|---|---|
| Performance (Month) | +0.4331 | +0.0478 | +0.5010 | -1.72% | -5.26% | 5472/6101 |
| Relative Strength Index (14) | +0.3968 | -0.1738 | +0.4655 | -3.58% | n/a | 11669/0 |
| upside_pct_lvl | -0.3955 | +0.3298 | -0.5022 | -3.65% | -2.43% | 4226/412 |
| Performance (Week) | +0.3632 | +0.1547 | +0.4335 | -2.05% | -5.25% | 5972/5623 |
| Short Float | -0.2880 | +0.2470 | -0.3049 | -3.39% | n/a | 5638/0 |
| d_Market Cap | +0.2447 | -0.0968 | +0.2973 | -3.30% | -3.45% | 3846/1892 |
| d_Forward P/E | +0.2376 | +0.1082 | +0.2392 | -2.82% | -6.12% | 2159/816 |
| d_Relative Strength Index (14) | +0.2196 | -0.0716 | +0.3859 | -2.93% | -5.48% | 8388/3021 |
| d_Performance (Week) | +0.1937 | +0.1772 | +0.2738 | -2.71% | -5.52% | 7848/3715 |
| d_Price | +0.1643 | +0.0820 | +0.2948 | -2.92% | -5.56% | 8348/2968 |
| d_Beta | +0.1286 | +0.1401 | +0.1384 | -0.73% | -7.91% | 1792/1067 |
| d_Performance (YTD) | +0.1194 | +0.1571 | +0.2316 | -2.93% | -7.12% | 8412/3006 |
| Institutional Transactions | -0.1131 | +0.0822 | -0.1283 | -3.20% | -4.21% | 3193/1832 |
| d_200-Day Simple Moving Average | +0.1072 | +0.1867 | +0.2045 | -2.97% | -5.34% | 8555/3048 |
| true_ret | +0.1006 | +0.1881 | +0.1856 | -2.92% | -5.56% | 8348/2968 |
| d_50-Day Simple Moving Average | +0.0842 | +0.2131 | +0.1695 | -3.01% | -5.33% | 8712/2917 |
| d_Performance (Month) | +0.0731 | +0.2313 | +0.1304 | -3.06% | -4.91% | 8051/3426 |
| d_Volatility (Month) | -0.0713 | +0.0575 | -0.0961 | -3.95% | -3.82% | 4499/5081 |
| Relative Volume | -0.0538 | +0.2146 | -0.0363 | -3.63% | n/a | 11471/0 |
| d_Performance (Quarter) | +0.0537 | +0.1301 | +0.1393 | -3.10% | -4.85% | 8236/2983 |
| d_Relative Volume | -0.0518 | +0.1825 | -0.0653 | -3.72% | -3.42% | 7157/4192 |
| d_Short Float | +0.0474 | -0.0332 | +0.0586 | -2.54% | -4.39% | 91/53 |
| d_Average Volume | +0.0396 | +0.0147 | +0.0143 | -3.00% | -4.22% | 5598/5491 |
| d_Target Price | +0.0395 | -0.0849 | +0.0548 | -3.13% | -4.24% | 290/300 |
| d_Analyst Recom | +0.0360 | +0.0175 | +0.0500 | -3.47% | -4.84% | 97/76 |

## Combinations

| Pattern | n | Mean long fwd | Hit up |
|---|---|---|---|
| true_ret>3% & DOWNTREND | 1013 | -4.81% | 10.6% |
| true_ret>3% & UPTREND | 1097 | -1.84% | 9.0% |
| true_ret>3% & MIXED | 573 | -3.24% | 12.7% |

## Risk dominance probes

| State | n | Mean long fwd | Mean fwd if score top quintile |
|---|---|---|---|
| EXTENDED | 393 | 0.96% | 8.77% |
| WASHED | 1536 | -7.69% | -7.87% |

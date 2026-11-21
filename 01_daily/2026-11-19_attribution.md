# Factor attribution — signal 2026-11-19 → prediction day 2026-11-20

## Trade window (read this first)

| Role | Date | Meaning |
|------|------|---------|
| **Signal as-of** | **2026-11-19** | Features/scores formed from this snapshot (and deltas vs **2026-11-18**). Only data on/before this date. |
| **Prediction day** | **2026-11-20** | The trading day the forward return is for (exit snapshot). |
| **Entry price** | Price @ 2026-11-19 | Long: buy here; short: sell here. |
| **Exit price** | Price @ 2026-11-20 | Close proxy on prediction day. |
| **Return column** | `fwd_1d` | Long: exit/entry − 1; short = opposite. |

Graded **n=11744** names with valid entry and exit prices.

Provisional until multiple signal dates agree.

_Column guide: **IC** = Spearman(feature, long forward return); **IC↑** / **IC↓** = IC among names that went up / down._

## Score calibration (long fwd)
- Spearman IC(total_score, fwd_1d) = **0.3689**

| Quintile | Mean long fwd | Hit up>1.5% | n |
|---|---|---|---|
| 1 | -1.09% | 2.0% | 3060 |
| 2 | -3.35% | 4.4% | 1667 |
| 3 | -2.69% | 4.2% | 2354 |
| 4 | -1.86% | 2.1% | 2373 |
| 5 | -1.68% | 11.9% | 2290 |

## Top |IC| features

| Feature | IC | IC↑ | IC↓ | Mean fwd when + | Mean fwd when − | n+/n− |
|---|---|---|---|---|---|---|
| Performance (Week) | +0.5695 | +0.0166 | +0.5800 | -0.24% | -2.37% | 1740/9859 |
| Performance (Month) | +0.5471 | -0.0006 | +0.5850 | -0.70% | -2.44% | 2907/8693 |
| d_Performance (Month) | +0.4454 | +0.0752 | +0.4045 | -1.54% | -2.14% | 2242/9252 |
| upside_pct_lvl | -0.4361 | +0.4885 | -0.5740 | -2.98% | -1.78% | 4443/190 |
| true_ret | +0.4086 | -0.0008 | +0.3680 | -1.56% | -2.15% | 1829/9414 |
| d_Volatility (Month) | -0.4029 | +0.3956 | -0.4602 | -2.25% | -1.82% | 8397/1945 |
| Relative Strength Index (14) | +0.3985 | -0.0514 | +0.2619 | -2.00% | n/a | 11685/0 |
| d_Performance (Quarter) | +0.3499 | +0.0635 | +0.2537 | -1.01% | -2.21% | 2133/9148 |
| d_Performance (YTD) | +0.2991 | +0.0301 | +0.1559 | -1.58% | -2.15% | 1893/9458 |
| d_200-Day Simple Moving Average | +0.2980 | +0.0496 | +0.1748 | -1.74% | -2.12% | 2129/9466 |
| d_20-Day Simple Moving Average | +0.2824 | +0.0330 | +0.2032 | 3.42% | -3.54% | 2482/9142 |
| d_50-Day Simple Moving Average | +0.2816 | +0.0382 | +0.1858 | -1.42% | -2.21% | 2305/9307 |
| d_Price | +0.2392 | +0.0746 | +0.0064 | -1.56% | -2.15% | 1829/9414 |
| Short Float | -0.1978 | +0.1227 | -0.1818 | -0.43% | n/a | 5611/0 |
| d_Forward P/E | +0.1120 | -0.0756 | +0.1287 | -3.29% | -2.85% | 316/2600 |
| d_Target Price | +0.0839 | -0.0494 | +0.0717 | -2.47% | -4.20% | 175/222 |
| Institutional Transactions | -0.0770 | +0.1430 | -0.0988 | -3.42% | 4.28% | 2991/2019 |
| d_Performance (Week) | +0.0705 | +0.1006 | -0.0237 | -0.27% | -3.14% | 4387/7195 |
| d_Short Float | +0.0655 | -0.0297 | +0.0965 | -2.40% | 3.71% | 26/88 |
| Relative Volume | -0.0615 | +0.1101 | -0.0107 | -2.06% | n/a | 11518/0 |
| d_Analyst Recom | +0.0586 | -0.0978 | +0.0433 | -2.42% | -2.93% | 402/188 |
| d_Relative Strength Index (14) | +0.0487 | +0.0370 | -0.2538 | -1.62% | -2.16% | 1914/9452 |
| d_Relative Volume | -0.0414 | +0.0467 | -0.0282 | -3.77% | 0.33% | 6583/4779 |
| d_Institutional Ownership | +0.0348 | -0.0545 | +0.0697 | -3.41% | 0.66% | 1015/501 |
| d_Market Cap | -0.0324 | +0.1780 | -0.1345 | -3.90% | 0.18% | 1051/4682 |

## Combinations

| Pattern | n | Mean long fwd | Hit up |
|---|---|---|---|
| true_ret>3% & DOWNTREND | 267 | -5.95% | 17.2% |
| true_ret>3% & UPTREND | 103 | 6.22% | 64.1% |
| true_ret>3% & MIXED | 86 | 4.67% | 52.3% |

## Risk dominance probes

| State | n | Mean long fwd | Mean fwd if score top quintile |
|---|---|---|---|
| EXTENDED | 155 | 2.96% | 5.10% |
| WASHED | 2713 | -1.24% | -5.34% |

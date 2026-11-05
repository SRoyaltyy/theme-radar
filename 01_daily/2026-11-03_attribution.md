# Factor attribution — signal 2026-11-03 → prediction day 2026-11-05

## Trade window (read this first)

| Role | Date | Meaning |
|------|------|---------|
| **Signal as-of** | **2026-11-03** | Features/scores formed from this snapshot (and deltas vs **2026-11-02**). Only data on/before this date. |
| **Prediction day** | **2026-11-05** | The trading day the forward return is for (exit snapshot). |
| **Entry price** | Price @ 2026-11-03 | Long: buy here; short: sell here. |
| **Exit price** | Price @ 2026-11-05 | Close proxy on prediction day. |
| **Return column** | `fwd_2d` | Long: exit/entry − 1; short = opposite. |

Graded **n=11736** names with valid entry and exit prices.

Provisional until multiple signal dates agree.

_Column guide: **IC** = Spearman(feature, long forward return); **IC↑** / **IC↓** = IC among names that went up / down._

## Score calibration (long fwd)
- Spearman IC(total_score, fwd_2d) = **-0.1219**

| Quintile | Mean long fwd | Hit up>1.5% | n |
|---|---|---|---|
| 1 | -0.45% | 21.7% | 2608 |
| 2 | -2.49% | 16.6% | 2316 |
| 3 | -1.32% | 15.9% | 2129 |
| 4 | -2.30% | 13.9% | 2396 |
| 5 | -7.07% | 17.7% | 2287 |

## Top |IC| features

| Feature | IC | IC↑ | IC↓ | Mean fwd when + | Mean fwd when − | n+/n− |
|---|---|---|---|---|---|---|
| d_20-Day Simple Moving Average | -0.4490 | -0.1972 | -0.4518 | -5.64% | 0.50% | 6049/5547 |
| Performance (Month) | +0.4480 | +0.0103 | +0.5274 | 0.15% | -4.76% | 4873/6695 |
| d_Price | -0.3943 | -0.1489 | -0.3447 | -5.44% | -0.04% | 5604/5512 |
| d_50-Day Simple Moving Average | -0.3918 | -0.1722 | -0.3955 | -5.11% | 0.11% | 6264/5332 |
| d_Relative Strength Index (14) | -0.3884 | -0.0235 | -0.2798 | -5.34% | -0.05% | 5715/5595 |
| d_Performance (Quarter) | -0.3843 | -0.1784 | -0.3903 | -5.19% | 0.31% | 5993/5189 |
| d_200-Day Simple Moving Average | -0.3770 | -0.1809 | -0.3626 | -5.16% | -0.12% | 5919/5646 |
| d_Performance (YTD) | -0.3766 | -0.1913 | -0.3454 | -5.35% | -0.10% | 5701/5587 |
| true_ret | -0.3718 | -0.2227 | -0.3493 | -5.44% | -0.04% | 5604/5512 |
| Performance (Week) | +0.3452 | +0.0653 | +0.3888 | -0.71% | -3.96% | 4478/7097 |
| Relative Strength Index (14) | +0.3396 | -0.0998 | +0.3371 | -2.68% | n/a | 11660/0 |
| upside_pct_lvl | -0.3278 | +0.2255 | -0.3667 | -2.36% | -0.46% | 4331/303 |
| d_Forward P/E | -0.2959 | -0.0285 | -0.2982 | -4.83% | -0.11% | 1138/1799 |
| d_Market Cap | -0.2941 | -0.0348 | -0.2265 | -4.84% | -0.17% | 2646/3041 |
| d_Volatility (Month) | -0.2599 | +0.2569 | -0.3752 | -3.46% | -1.74% | 7234/3017 |
| d_Performance (Month) | -0.2337 | -0.2098 | -0.2352 | -5.59% | -0.84% | 4505/6959 |
| Institutional Transactions | -0.1195 | +0.0383 | -0.1252 | -2.29% | -2.50% | 3193/1831 |
| Short Float | -0.0761 | +0.2423 | -0.2828 | -2.27% | n/a | 5651/0 |
| Relative Volume | +0.0567 | +0.1363 | -0.0351 | -2.72% | n/a | 11467/0 |
| d_Average Volume | +0.0462 | +0.0627 | -0.0334 | -2.37% | -3.22% | 6612/4473 |
| d_Short Ratio | -0.0400 | -0.0800 | +0.0004 | -3.41% | -2.81% | 2755/4390 |
| d_Target Price | +0.0399 | -0.0116 | +0.0572 | -1.08% | -3.57% | 283/233 |
| d_Beta | -0.0381 | -0.1943 | +0.0153 | -4.98% | -1.47% | 1694/4369 |
| d_Total Debt/Equity | +0.0328 | -0.0178 | +0.0293 | -1.21% | -4.05% | 84/97 |
| d_Short Float | +0.0246 | -0.0120 | +0.0202 | 3.72% | -5.33% | 2/5 |

## Combinations

| Pattern | n | Mean long fwd | Hit up |
|---|---|---|---|
| true_ret>3% & DOWNTREND | 934 | -14.88% | 9.2% |
| true_ret>3% & UPTREND | 155 | 0.04% | 25.2% |
| true_ret>3% & MIXED | 201 | -7.18% | 17.4% |

## Risk dominance probes

| State | n | Mean long fwd | Mean fwd if score top quintile |
|---|---|---|---|
| EXTENDED | 200 | 4.97% | 15.24% |
| WASHED | 1678 | -8.32% | -17.56% |

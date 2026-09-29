# Factor attribution — signal 2026-09-25 → prediction day 2026-09-29

## Trade window (read this first)

| Role | Date | Meaning |
|------|------|---------|
| **Signal as-of** | **2026-09-25** | Features/scores formed from this snapshot (and deltas vs **2026-09-24**). Only data on/before this date. |
| **Prediction day** | **2026-09-29** | The trading day the forward return is for (exit snapshot). |
| **Entry price** | Price @ 2026-09-25 | Long: buy here; short: sell here. |
| **Exit price** | Price @ 2026-09-29 | Close proxy on prediction day. |
| **Return column** | `fwd_2d` | Long: exit/entry − 1; short = opposite. |

Graded **n=11665** names with valid entry and exit prices.

Provisional until multiple signal dates agree.

_Column guide: **IC** = Spearman(feature, long forward return); **IC↑** / **IC↓** = IC among names that went up / down._

## Score calibration (long fwd)
- Spearman IC(total_score, fwd_2d) = **-0.0598**

| Quintile | Mean long fwd | Hit up>1.5% | n |
|---|---|---|---|
| 1 | 4.45% | 12.4% | 2372 |
| 2 | -0.11% | 5.8% | 2562 |
| 3 | -0.94% | 5.3% | 2131 |
| 4 | 3.63% | 7.3% | 2330 |
| 5 | -1.35% | 13.2% | 2270 |

## Top |IC| features

| Feature | IC | IC↑ | IC↓ | Mean fwd when + | Mean fwd when − | n+/n− |
|---|---|---|---|---|---|---|
| upside_pct_lvl | -0.1635 | +0.3184 | -0.3671 | 1.96% | -0.64% | 4375/260 |
| d_Performance (Month) | -0.1133 | -0.0477 | -0.1023 | 0.60% | 2.33% | 7275/4079 |
| Performance (Month) | +0.1094 | -0.1401 | +0.2167 | -0.65% | 2.05% | 3598/7880 |
| d_20-Day Simple Moving Average | -0.0938 | -0.0606 | -0.0672 | 0.54% | 2.54% | 7865/3714 |
| d_Performance (Week) | -0.0727 | -0.1308 | -0.0407 | 0.07% | 3.31% | 7465/3996 |
| Relative Strength Index (14) | +0.0716 | -0.1060 | +0.0345 | 1.19% | n/a | 11563/0 |
| Short Float | -0.0696 | +0.2285 | -0.1531 | 3.36% | n/a | 5698/0 |
| d_50-Day Simple Moving Average | -0.0622 | -0.0833 | -0.0100 | 0.49% | 2.40% | 7352/4210 |
| d_200-Day Simple Moving Average | -0.0573 | -0.0812 | +0.0083 | -0.81% | 2.33% | 7196/4339 |
| Performance (Week) | +0.0560 | -0.0934 | +0.1358 | -1.02% | 2.96% | 5081/6397 |
| true_ret | -0.0429 | -0.1057 | +0.0271 | -0.97% | 2.36% | 6906/4151 |
| d_Short Ratio | -0.0400 | -0.0593 | -0.0607 | -0.88% | 2.04% | 4239/3175 |
| d_Performance (YTD) | -0.0384 | -0.0930 | +0.0444 | -0.73% | 2.34% | 7002/4224 |
| d_Average Volume | +0.0316 | +0.0728 | +0.0637 | 3.84% | -0.84% | 5027/6098 |
| Institutional Transactions | -0.0283 | +0.0913 | -0.0947 | 5.29% | 2.35% | 3221/1809 |
| d_Beta | -0.0265 | +0.0157 | -0.0334 | 0.78% | 2.03% | 1025/598 |
| Relative Volume | -0.0226 | +0.0708 | -0.0243 | 1.20% | n/a | 11411/0 |
| d_Market Cap | -0.0223 | -0.0921 | +0.0884 | 3.03% | 4.24% | 2962/2698 |
| d_Performance (Quarter) | +0.0207 | -0.0956 | +0.1490 | -0.39% | 2.87% | 5237/5769 |
| d_Price | -0.0198 | -0.1047 | +0.1050 | -0.97% | 2.36% | 6906/4151 |
| d_Forward P/E | -0.0181 | -0.0373 | +0.0261 | -1.17% | -1.12% | 1734/1192 |
| d_EPS Surprise | -0.0179 | +0.0109 | -0.0189 | -1.28% | -1.10% | 10/5 |
| d_Total Debt/Equity | -0.0159 | -0.0181 | +0.0032 | -8.54% | -0.01% | 3/9 |
| d_Gross Margin | +0.0140 | -0.0055 | -0.0022 | 0.36% | -3.72% | 6/10 |
| d_Profit Margin | +0.0134 | -0.0040 | -0.0026 | -0.06% | -4.53% | 8/5 |

## Combinations

| Pattern | n | Mean long fwd | Hit up |
|---|---|---|---|
| true_ret>3% & DOWNTREND | 277 | -2.51% | 23.5% |
| true_ret>3% & UPTREND | 219 | -2.29% | 19.2% |
| true_ret>3% & MIXED | 139 | 1.22% | 23.0% |

## Risk dominance probes

| State | n | Mean long fwd | Mean fwd if score top quintile |
|---|---|---|---|
| EXTENDED | 216 | -1.60% | 0.01% |
| WASHED | 1885 | 10.35% | 26.58% |

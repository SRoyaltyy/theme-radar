# Factor attribution — signal 2026-10-16 → prediction day 2026-10-21

## Trade window (read this first)

| Role | Date | Meaning |
|------|------|---------|
| **Signal as-of** | **2026-10-16** | Features/scores formed from this snapshot (and deltas vs **2026-10-15**). Only data on/before this date. |
| **Prediction day** | **2026-10-21** | The trading day the forward return is for (exit snapshot). |
| **Entry price** | Price @ 2026-10-16 | Long: buy here; short: sell here. |
| **Exit price** | Price @ 2026-10-21 | Close proxy on prediction day. |
| **Return column** | `fwd_3d` | Long: exit/entry − 1; short = opposite. |

Graded **n=11733** names with valid entry and exit prices.

Provisional until multiple signal dates agree.

_Column guide: **IC** = Spearman(feature, long forward return); **IC↑** / **IC↓** = IC among names that went up / down._

## Score calibration (long fwd)
- Spearman IC(total_score, fwd_3d) = **-0.2950**

| Quintile | Mean long fwd | Hit up>1.5% | n |
|---|---|---|---|
| 1 | 5.15% | 58.1% | 2495 |
| 2 | 4.94% | 36.5% | 2247 |
| 3 | 1.06% | 29.4% | 2347 |
| 4 | 0.20% | 11.8% | 2655 |
| 5 | -0.33% | 21.7% | 1989 |

## Top |IC| features

| Feature | IC | IC↑ | IC↓ | Mean fwd when + | Mean fwd when − | n+/n− |
|---|---|---|---|---|---|---|
| d_Price | -0.4115 | -0.4181 | +0.1764 | -0.24% | 3.23% | 3295/7950 |
| d_Performance (YTD) | -0.4011 | -0.5394 | +0.2103 | -0.22% | 3.40% | 3351/8024 |
| d_200-Day Simple Moving Average | -0.3987 | -0.5466 | +0.1978 | -0.25% | 3.36% | 3508/8088 |
| d_50-Day Simple Moving Average | -0.3770 | -0.5486 | +0.1844 | -0.24% | 3.49% | 3819/7796 |
| d_20-Day Simple Moving Average | -0.3751 | -0.5383 | +0.1556 | 0.15% | 3.33% | 3859/7728 |
| d_Performance (Week) | -0.3551 | -0.5177 | +0.1432 | 1.56% | 2.55% | 3154/8385 |
| true_ret | -0.3525 | -0.5712 | +0.2392 | -0.24% | 3.23% | 3295/7950 |
| d_Relative Strength Index (14) | -0.3502 | -0.1982 | +0.1876 | -0.25% | 3.39% | 3370/8002 |
| d_Performance (Month) | -0.3369 | -0.5157 | +0.2023 | -0.41% | 3.06% | 2601/8873 |
| d_Performance (Quarter) | -0.2841 | -0.3876 | +0.1163 | 1.49% | 2.91% | 4824/6369 |
| Performance (Week) | -0.2588 | -0.4886 | +0.2870 | 0.15% | 3.57% | 4370/7205 |
| d_Forward P/E | -0.2393 | -0.3894 | +0.1693 | 0.32% | 1.59% | 1160/1787 |
| d_Market Cap | -0.2390 | -0.2932 | +0.1307 | -0.04% | 5.12% | 1871/3871 |
| Short Float | +0.1605 | +0.3251 | -0.1620 | 3.44% | n/a | 5660/0 |
| Relative Strength Index (14) | -0.1489 | -0.3485 | +0.3219 | 2.25% | n/a | 11647/0 |
| d_Volatility (Month) | +0.1329 | +0.3115 | -0.1470 | 3.99% | 1.02% | 5077/5012 |
| d_Target Price | +0.0701 | +0.0577 | +0.0146 | 2.28% | 0.02% | 187/316 |
| d_Beta | -0.0660 | -0.2201 | +0.1962 | 0.35% | 6.17% | 708/1652 |
| Relative Volume | +0.0472 | +0.0855 | +0.0340 | 2.28% | n/a | 11510/0 |
| Institutional Transactions | +0.0457 | +0.1269 | -0.1005 | 3.36% | 5.14% | 3260/1776 |
| Performance (Month) | -0.0391 | -0.3115 | +0.3484 | 0.78% | 2.88% | 3396/8143 |
| d_Average Volume | -0.0230 | +0.0675 | -0.0376 | 2.96% | 1.35% | 6739/4317 |
| d_Profit Margin | +0.0207 | +0.0147 | +0.0053 | 1.22% | -1.05% | 14/16 |
| d_EPS Surprise | -0.0202 | -0.0102 | -0.0147 | 0.03% | 1.90% | 13/15 |
| d_Relative Volume | -0.0167 | -0.0306 | +0.0099 | 2.15% | 2.43% | 4811/6515 |

## Combinations

| Pattern | n | Mean long fwd | Hit up |
|---|---|---|---|
| true_ret>3% & DOWNTREND | 166 | -4.81% | 22.3% |
| true_ret>3% & UPTREND | 111 | -1.37% | 16.2% |
| true_ret>3% & MIXED | 84 | -3.95% | 14.3% |

## Risk dominance probes

| State | n | Mean long fwd | Mean fwd if score top quintile |
|---|---|---|---|
| EXTENDED | 140 | -1.97% | -3.66% |
| WASHED | 1710 | 9.97% | 0.46% |

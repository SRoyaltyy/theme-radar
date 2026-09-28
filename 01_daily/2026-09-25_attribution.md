# Factor attribution — signal 2026-09-25 → prediction day 2026-09-28

## Trade window (read this first)

| Role | Date | Meaning |
|------|------|---------|
| **Signal as-of** | **2026-09-25** | Features/scores formed from this snapshot (and deltas vs **2026-09-24**). Only data on/before this date. |
| **Prediction day** | **2026-09-28** | The trading day the forward return is for (exit snapshot). |
| **Entry price** | Price @ 2026-09-25 | Long: buy here; short: sell here. |
| **Exit price** | Price @ 2026-09-28 | Close proxy on prediction day. |
| **Return column** | `fwd_1d` | Long: exit/entry − 1; short = opposite. |

Graded **n=11665** names with valid entry and exit prices.

Provisional until multiple signal dates agree.

_Column guide: **IC** = Spearman(feature, long forward return); **IC↑** / **IC↓** = IC among names that went up / down._

## Score calibration (long fwd)
- Spearman IC(total_score, fwd_1d) = **-0.1114**

| Quintile | Mean long fwd | Hit up>1.5% | n |
|---|---|---|---|
| 1 | 5.66% | 11.6% | 2372 |
| 2 | -0.85% | 4.4% | 2562 |
| 3 | -0.77% | 4.3% | 2131 |
| 4 | 4.87% | 5.7% | 2330 |
| 5 | -1.18% | 10.6% | 2270 |

## Top |IC| features

| Feature | IC | IC↑ | IC↓ | Mean fwd when + | Mean fwd when − | n+/n− |
|---|---|---|---|---|---|---|
| upside_pct_lvl | -0.1946 | +0.3155 | -0.4324 | 2.44% | -0.43% | 4375/260 |
| d_20-Day Simple Moving Average | -0.1320 | -0.0902 | -0.0976 | 1.05% | 2.70% | 7865/3714 |
| d_Performance (Month) | -0.1269 | -0.0615 | -0.1143 | 0.94% | 2.86% | 7275/4079 |
| d_200-Day Simple Moving Average | -0.1112 | -0.1051 | -0.0389 | -0.64% | 2.56% | 7196/4339 |
| d_50-Day Simple Moving Average | -0.1048 | -0.1050 | -0.0448 | 1.00% | 2.60% | 7352/4210 |
| true_ret | -0.0986 | -0.1442 | -0.0229 | -0.87% | 2.66% | 6906/4151 |
| d_Performance (YTD) | -0.0960 | -0.1268 | -0.0047 | -0.62% | 2.63% | 7002/4224 |
| d_Price | -0.0761 | -0.1272 | +0.0621 | -0.87% | 2.66% | 6906/4151 |
| Performance (Month) | +0.0645 | -0.1325 | +0.1572 | -1.04% | 2.81% | 3598/7880 |
| Short Float | -0.0613 | +0.1354 | -0.1314 | 4.02% | n/a | 5698/0 |
| d_Forward P/E | -0.0517 | -0.1186 | +0.0131 | -1.00% | -0.87% | 1734/1192 |
| d_Performance (Week) | -0.0482 | -0.1047 | +0.0066 | 1.06% | 2.62% | 7465/3996 |
| d_Market Cap | -0.0364 | -0.1086 | +0.0940 | 4.17% | 4.36% | 2962/2698 |
| d_Average Volume | +0.0331 | +0.0857 | +0.0580 | 4.57% | -0.70% | 5027/6098 |
| d_Beta | -0.0328 | +0.0547 | -0.0422 | 0.72% | 0.63% | 1025/598 |
| d_Performance (Quarter) | -0.0324 | -0.0804 | +0.0952 | -0.22% | 3.54% | 5237/5769 |
| d_Short Ratio | -0.0313 | -0.0682 | -0.0397 | -0.68% | 3.13% | 4239/3175 |
| d_Total Debt/Equity | -0.0303 | -0.0344 | -0.0115 | -3.69% | 0.58% | 3/9 |
| d_Gross Margin | +0.0247 | -0.0015 | +0.0045 | 0.76% | -2.21% | 6/10 |
| Relative Volume | -0.0243 | +0.0628 | -0.0055 | 1.60% | n/a | 11411/0 |
| Relative Strength Index (14) | +0.0228 | -0.0806 | -0.0524 | 1.59% | n/a | 11563/0 |
| d_Analyst Recom | +0.0227 | +0.0529 | +0.0131 | -0.18% | -1.22% | 39/67 |
| d_Relative Strength Index (14) | -0.0226 | -0.1197 | +0.2040 | 1.09% | 2.63% | 6984/4221 |
| d_EPS Surprise | -0.0206 | +0.0031 | -0.0226 | -1.38% | 0.01% | 10/5 |
| d_Institutional Ownership | +0.0165 | -0.0426 | +0.0289 | -1.14% | -1.60% | 13/23 |

## Combinations

| Pattern | n | Mean long fwd | Hit up |
|---|---|---|---|
| true_ret>3% & DOWNTREND | 277 | -2.09% | 18.4% |
| true_ret>3% & UPTREND | 219 | -2.90% | 12.3% |
| true_ret>3% & MIXED | 139 | 0.66% | 20.9% |

## Risk dominance probes

| State | n | Mean long fwd | Mean fwd if score top quintile |
|---|---|---|---|
| EXTENDED | 216 | -2.36% | -2.56% |
| WASHED | 1885 | 13.57% | 34.11% |

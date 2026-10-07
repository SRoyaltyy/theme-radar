# Factor attribution — signal 2026-10-05 → prediction day 2026-10-07

## Trade window (read this first)

| Role | Date | Meaning |
|------|------|---------|
| **Signal as-of** | **2026-10-05** | Features/scores formed from this snapshot (and deltas vs **2026-10-02**). Only data on/before this date. |
| **Prediction day** | **2026-10-07** | The trading day the forward return is for (exit snapshot). |
| **Entry price** | Price @ 2026-10-05 | Long: buy here; short: sell here. |
| **Exit price** | Price @ 2026-10-07 | Close proxy on prediction day. |
| **Return column** | `fwd_2d` | Long: exit/entry − 1; short = opposite. |

Graded **n=11690** names with valid entry and exit prices.

Provisional until multiple signal dates agree.

_Column guide: **IC** = Spearman(feature, long forward return); **IC↑** / **IC↓** = IC among names that went up / down._

## Score calibration (long fwd)
- Spearman IC(total_score, fwd_2d) = **-0.0538**

| Quintile | Mean long fwd | Hit up>1.5% | n |
|---|---|---|---|
| 1 | -0.36% | 13.4% | 2464 |
| 2 | -0.44% | 7.5% | 2318 |
| 3 | 0.10% | 8.9% | 2366 |
| 4 | -0.91% | 8.1% | 2211 |
| 5 | -1.55% | 15.7% | 2331 |

## Top |IC| features

| Feature | IC | IC↑ | IC↓ | Mean fwd when + | Mean fwd when − | n+/n− |
|---|---|---|---|---|---|---|
| d_Performance (Quarter) | -0.2090 | +0.0345 | -0.2434 | -0.76% | -0.19% | 7852/3246 |
| Short Float | -0.1269 | +0.1847 | -0.1830 | -0.64% | n/a | 5687/0 |
| d_Performance (Week) | -0.1180 | +0.1221 | -0.1557 | -0.64% | -0.57% | 8846/2661 |
| Institutional Transactions | -0.0802 | +0.0452 | -0.1057 | -0.76% | -0.51% | 3242/1803 |
| upside_pct_lvl | -0.0788 | +0.3335 | -0.3154 | -1.10% | -2.31% | 4351/282 |
| d_20-Day Simple Moving Average | -0.0753 | +0.0363 | -0.0535 | -0.63% | -0.61% | 8012/3576 |
| true_ret | -0.0598 | -0.0422 | -0.0279 | -0.91% | -0.54% | 6922/4222 |
| d_50-Day Simple Moving Average | -0.0558 | -0.0066 | -0.0301 | -0.65% | -0.58% | 7355/4237 |
| d_Performance (YTD) | -0.0519 | -0.0618 | -0.0027 | -0.68% | -0.52% | 7002/4295 |
| Relative Volume | -0.0477 | +0.0303 | -0.0363 | -0.64% | n/a | 11463/0 |
| d_200-Day Simple Moving Average | -0.0469 | -0.0217 | -0.0200 | -0.65% | -0.57% | 7142/4407 |
| d_Total Debt/Equity | +0.0389 | -0.0015 | +0.0389 | 1.58% | -11.53% | 2/2 |
| Performance (Month) | +0.0322 | -0.2567 | +0.0743 | -1.16% | -0.38% | 3557/7937 |
| Relative Strength Index (14) | -0.0313 | -0.0437 | -0.0773 | -0.62% | n/a | 11597/0 |
| d_Institutional Transactions | -0.0303 | -0.0474 | -0.0148 | -1.44% | 0.49% | 2258/1886 |
| d_Target Price | -0.0294 | +0.0626 | -0.0693 | -1.50% | -0.94% | 248/468 |
| d_Performance (Month) | +0.0289 | -0.1068 | +0.0590 | -0.75% | -0.54% | 4135/7250 |
| d_Average Volume | +0.0289 | -0.0645 | +0.0405 | -0.61% | -0.64% | 5381/5686 |
| d_Short Ratio | -0.0270 | +0.0349 | -0.0296 | -1.05% | -0.75% | 3831/3432 |
| d_Sales Year Over Year TTM | +0.0226 | +0.0087 | +0.0313 | 1.72% | -6.85% | 2/2 |
| d_Institutional Ownership | -0.0201 | +0.0398 | -0.0454 | -1.39% | -1.19% | 1171/1735 |
| d_Sales Growth Quarter Over Quarter | +0.0199 | -0.0057 | +0.0039 | -4.08% | -12.61% | 5/2 |
| d_Forward P/E | +0.0193 | -0.0148 | -0.0336 | -0.84% | -0.86% | 1599/1332 |
| d_Gross Margin | -0.0179 | +0.0097 | -0.0114 | -14.98% | -3.23% | 2/6 |
| d_Price | -0.0177 | -0.1002 | +0.0554 | -0.91% | -0.54% | 6922/4222 |

## Combinations

| Pattern | n | Mean long fwd | Hit up |
|---|---|---|---|
| true_ret>3% & DOWNTREND | 381 | -1.55% | 19.7% |
| true_ret>3% & UPTREND | 356 | -3.71% | 12.1% |
| true_ret>3% & MIXED | 218 | -3.01% | 19.7% |

## Risk dominance probes

| State | n | Mean long fwd | Mean fwd if score top quintile |
|---|---|---|---|
| EXTENDED | 251 | -3.06% | -4.92% |
| WASHED | 1953 | 0.11% | -1.93% |

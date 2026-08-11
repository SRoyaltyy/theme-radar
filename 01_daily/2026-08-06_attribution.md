# Factor attribution — 2026-08-06

**What this report measures, exactly:** features computed from the **2026-08-06** Finviz snapshot (deltas vs the **?** snapshot), graded against `fwd_2d` = the return from **2026-08-06** to **2026-08-10** (n=11518 stocks with valid labels).
Provisional until multiple scan dates agree.

_Column guide: **IC** = Spearman rank correlation between the feature and the forward return (whole universe); **IC↑** = IC computed only among stocks that went UP; **IC↓** = IC only among stocks that went DOWN. A high IC↑ means the feature ranks winners among winners._

## Score calibration
- Spearman IC(total_score, fwd_2d) = **0.0636**

| Quintile | Mean fwd | Hit up>1.5% | n |
|---|---|---|---|
| 1 | 7.41% | 22.7% | 2552 |
| 2 | 3.19% | 21.3% | 2828 |
| 3 | 4.09% | 22.7% | 2747 |
| 4 | 1.41% | 34.0% | 1551 |
| 5 | 3.37% | 35.9% | 1840 |

## Top |IC| features (full universe)

| Feature | IC | IC↑ | IC↓ | Mean fwd when + | Mean fwd when − | n+/n− |
|---|---|---|---|---|---|---|
| Performance (Week) | +0.1820 | +0.2194 | -0.0317 | 1.28% | 10.63% | 7796/3528 |
| upside_pct_lvl | +0.1357 | +0.2750 | -0.2780 | 4.46% | 0.62% | 4270/374 |
| Relative Strength Index (14) | +0.1102 | -0.1791 | +0.0528 | 4.16% | n/a | 11422/0 |
| Performance (Month) | +0.0570 | -0.0069 | +0.0939 | 0.85% | 8.75% | 6468/4787 |
| Short Float | +0.0551 | +0.2985 | -0.1586 | 7.57% | n/a | 5674/0 |
| Institutional Transactions | +0.0251 | +0.0794 | -0.0067 | 13.90% | 3.03% | 2535/2487 |
| Relative Volume | -0.0105 | +0.0924 | -0.1040 | 4.24% | n/a | 11231/0 |

## Risk dominance probes

| State | n | Mean fwd | Mean fwd if score top quintile |
|---|---|---|---|
| Week>40% | 90 | -0.81% | -1.86% |
| Week>25% | 273 | 1.89% | 1.36% |
| Week>100% | 16 | -14.32% | -12.29% |
| RSI>75 | 145 | 0.12% | n/a |

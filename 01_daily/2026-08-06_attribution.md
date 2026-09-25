# Factor attribution — 2026-08-06

**What this report measures, exactly:** features computed from the **2026-08-06** Finviz snapshot (deltas vs the **?** snapshot), graded against `fwd_3d` = the return from **2026-08-06** to **2026-08-11** (n=11518 stocks with valid labels).
Provisional until multiple scan dates agree.

_Column guide: **IC** = Spearman rank correlation between the feature and the forward return (whole universe); **IC↑** = IC computed only among stocks that went UP; **IC↓** = IC only among stocks that went DOWN. A high IC↑ means the feature ranks winners among winners._

## Score calibration
- Spearman IC(total_score, fwd_3d) = **0.0815**

| Quintile | Mean fwd | Hit up>1.5% | n |
|---|---|---|---|
| 1 | 8.20% | 24.3% | 2552 |
| 2 | 3.11% | 22.2% | 2828 |
| 3 | 4.16% | 25.3% | 2747 |
| 4 | 1.84% | 40.5% | 1551 |
| 5 | 3.79% | 39.1% | 1840 |

## Top |IC| features (full universe)

| Feature | IC | IC↑ | IC↓ | Mean fwd when + | Mean fwd when − | n+/n− |
|---|---|---|---|---|---|---|
| Performance (Week) | +0.2028 | +0.2195 | +0.0137 | 1.53% | 11.07% | 7796/3528 |
| upside_pct_lvl | +0.1337 | +0.3693 | -0.2696 | 4.66% | 0.50% | 4270/374 |
| Short Float | +0.0737 | +0.3127 | -0.1807 | 8.10% | n/a | 5674/0 |
| Relative Strength Index (14) | +0.0623 | -0.2001 | +0.0829 | 4.47% | n/a | 11422/0 |
| Institutional Transactions | +0.0453 | +0.0611 | -0.0324 | 14.44% | 3.67% | 2535/2487 |
| Performance (Month) | +0.0221 | -0.0422 | +0.0895 | 0.96% | 9.30% | 6468/4787 |
| Relative Volume | +0.0088 | +0.0988 | -0.0889 | 4.55% | n/a | 11231/0 |

## Risk dominance probes

| State | n | Mean fwd | Mean fwd if score top quintile |
|---|---|---|---|
| Week>40% | 90 | -0.77% | -1.53% |
| Week>25% | 273 | 2.77% | 1.77% |
| Week>100% | 16 | -16.86% | -11.58% |
| RSI>75 | 145 | 0.28% | n/a |

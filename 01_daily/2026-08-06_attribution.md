# Factor attribution — signal 2026-08-06 → prediction day 2026-08-11

## Trade window (read this first)

| Role | Date | Meaning |
|------|------|---------|
| **Signal as-of** | **2026-08-06** | Features/scores formed from this snapshot (and deltas vs **?**). Only data on/before this date. |
| **Prediction day** | **2026-08-11** | The trading day the forward return is for (exit snapshot). |
| **Entry price** | Price @ 2026-08-06 | Long: buy here; short: sell here. |
| **Exit price** | Price @ 2026-08-11 | Close proxy on prediction day. |
| **Return column** | `fwd_3d` | Long: exit/entry − 1; short = opposite. |

Graded **n=11518** names with valid entry and exit prices.

Provisional until multiple signal dates agree.

_Column guide: **IC** = Spearman(feature, long forward return); **IC↑** / **IC↓** = IC among names that went up / down._

## Score calibration (long fwd)
- Spearman IC(total_score, fwd_3d) = **0.0815**

| Quintile | Mean long fwd | Hit up>1.5% | n |
|---|---|---|---|
| 1 | 8.20% | 24.3% | 2552 |
| 2 | 3.11% | 22.2% | 2828 |
| 3 | 4.16% | 25.3% | 2747 |
| 4 | 1.84% | 40.5% | 1551 |
| 5 | 3.79% | 39.1% | 1840 |

## Top |IC| features

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

| State | n | Mean long fwd | Mean fwd if score top quintile |
|---|---|---|---|
| EXTENDED | 239 | 1.37% | 0.14% |
| WASHED | 607 | 64.91% | 95.37% |

# Factor attribution — signal 2026-09-08 → prediction day 2026-09-10

## Trade window (read this first)

| Role | Date | Meaning |
|------|------|---------|
| **Signal as-of** | **2026-09-08** | Features/scores formed from this snapshot (and deltas vs **?**). Only data on/before this date. |
| **Prediction day** | **2026-09-10** | The trading day the forward return is for (exit snapshot). |
| **Entry price** | Price @ 2026-09-08 | Long: buy here; short: sell here. |
| **Exit price** | Price @ 2026-09-10 | Close proxy on prediction day. |
| **Return column** | `fwd_2d` | Long: exit/entry − 1; short = opposite. |

Graded **n=11593** names with valid entry and exit prices.

Provisional until multiple signal dates agree.

_Column guide: **IC** = Spearman(feature, long forward return); **IC↑** / **IC↓** = IC among names that went up / down._

## Score calibration (long fwd)
- Spearman IC(total_score, fwd_2d) = **-0.1276**

| Quintile | Mean long fwd | Hit up>1.5% | n |
|---|---|---|---|
| 1 | 2.19% | 7.7% | 2802 |
| 2 | -1.31% | 5.2% | 2828 |
| 3 | -1.53% | 6.3% | 2645 |
| 4 | -2.23% | 9.4% | 1283 |
| 5 | -2.32% | 9.0% | 2035 |

## Top |IC| features

| Feature | IC | IC↑ | IC↓ | Mean fwd when + | Mean fwd when − | n+/n− |
|---|---|---|---|---|---|---|
| Short Float | -0.2767 | +0.1079 | -0.2839 | -0.72% | n/a | 5685/0 |
| upside_pct_lvl | -0.2629 | +0.3527 | -0.4100 | -0.93% | -1.52% | 4348/297 |
| Performance (Month) | +0.1134 | -0.0297 | +0.1424 | -1.64% | -0.25% | 4384/7000 |
| Relative Volume | -0.0813 | +0.0667 | -0.1070 | -0.80% | n/a | 11350/0 |
| Institutional Transactions | -0.0754 | +0.0586 | -0.1166 | -1.60% | 0.95% | 3198/1830 |
| Relative Strength Index (14) | +0.0697 | -0.1034 | +0.0392 | -0.79% | n/a | 11504/0 |
| Performance (Week) | +0.0032 | -0.0041 | -0.0130 | -1.73% | -0.02% | 5077/6295 |

## Risk dominance probes

| State | n | Mean long fwd | Mean fwd if score top quintile |
|---|---|---|---|
| EXTENDED | 232 | -4.21% | -6.91% |
| WASHED | 775 | 6.71% | -0.94% |

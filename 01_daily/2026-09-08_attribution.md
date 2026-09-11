# Factor attribution — signal 2026-09-08 → prediction day 2026-09-11

## Trade window (read this first)

| Role | Date | Meaning |
|------|------|---------|
| **Signal as-of** | **2026-09-08** | Features/scores formed from this snapshot (and deltas vs **?**). Only data on/before this date. |
| **Prediction day** | **2026-09-11** | The trading day the forward return is for (exit snapshot). |
| **Entry price** | Price @ 2026-09-08 | Long: buy here; short: sell here. |
| **Exit price** | Price @ 2026-09-11 | Close proxy on prediction day. |
| **Return column** | `fwd_3d` | Long: exit/entry − 1; short = opposite. |

Graded **n=11592** names with valid entry and exit prices.

Provisional until multiple signal dates agree.

_Column guide: **IC** = Spearman(feature, long forward return); **IC↑** / **IC↓** = IC among names that went up / down._

## Score calibration (long fwd)
- Spearman IC(total_score, fwd_3d) = **-0.0619**

| Quintile | Mean long fwd | Hit up>1.5% | n |
|---|---|---|---|
| 1 | 2.29% | 9.6% | 2802 |
| 2 | -0.78% | 6.9% | 2828 |
| 3 | -0.96% | 9.9% | 2645 |
| 4 | 4.28% | 14.7% | 1283 |
| 5 | -2.48% | 13.1% | 2034 |

## Top |IC| features

| Feature | IC | IC↑ | IC↓ | Mean fwd when + | Mean fwd when − | n+/n− |
|---|---|---|---|---|---|---|
| upside_pct_lvl | -0.2473 | +0.2970 | -0.4061 | 0.95% | -0.96% | 4347/297 |
| Short Float | -0.1996 | +0.1702 | -0.2649 | 0.72% | n/a | 5684/0 |
| Relative Strength Index (14) | +0.1245 | -0.1586 | +0.0782 | 0.19% | n/a | 11503/0 |
| Performance (Month) | +0.0860 | -0.0549 | +0.1202 | 0.05% | 0.29% | 4384/6999 |
| Institutional Transactions | -0.0727 | +0.0610 | -0.1101 | 0.20% | 1.16% | 3197/1830 |
| Relative Volume | -0.0716 | +0.1287 | -0.1098 | 0.20% | n/a | 11349/0 |
| Performance (Week) | +0.0434 | +0.0068 | +0.0294 | -0.27% | 0.60% | 5076/6295 |

## Risk dominance probes

| State | n | Mean long fwd | Mean fwd if score top quintile |
|---|---|---|---|
| EXTENDED | 232 | -3.59% | -7.33% |
| WASHED | 775 | 6.56% | -0.62% |

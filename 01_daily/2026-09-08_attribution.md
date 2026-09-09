# Factor attribution — signal 2026-09-08 → prediction day 2026-09-09

## Trade window (read this first)

| Role | Date | Meaning |
|------|------|---------|
| **Signal as-of** | **2026-09-08** | Features/scores formed from this snapshot (and deltas vs **?**). Only data on/before this date. |
| **Prediction day** | **2026-09-09** | The trading day the forward return is for (exit snapshot). |
| **Entry price** | Price @ 2026-09-08 | Long: buy here; short: sell here. |
| **Exit price** | Price @ 2026-09-09 | Close proxy on prediction day. |
| **Return column** | `fwd_1d` | Long: exit/entry − 1; short = opposite. |

Graded **n=11595** names with valid entry and exit prices.

Provisional until multiple signal dates agree.

_Column guide: **IC** = Spearman(feature, long forward return); **IC↑** / **IC↓** = IC among names that went up / down._

## Score calibration (long fwd)
- Spearman IC(total_score, fwd_1d) = **-0.0849**

| Quintile | Mean long fwd | Hit up>1.5% | n |
|---|---|---|---|
| 1 | 1.99% | 6.0% | 2804 |
| 2 | -0.50% | 4.8% | 2828 |
| 3 | -0.77% | 6.7% | 2645 |
| 4 | -1.34% | 8.8% | 1283 |
| 5 | -0.87% | 10.1% | 2035 |

## Top |IC| features

| Feature | IC | IC↑ | IC↓ | Mean fwd when + | Mean fwd when − | n+/n− |
|---|---|---|---|---|---|---|
| Short Float | -0.2673 | +0.1150 | -0.2784 | 0.08% | n/a | 5687/0 |
| upside_pct_lvl | -0.2122 | +0.3262 | -0.4056 | 0.32% | -0.79% | 4349/297 |
| Performance (Month) | +0.1885 | -0.0088 | +0.2159 | -0.70% | 0.25% | 4384/7002 |
| Relative Strength Index (14) | +0.1435 | -0.1000 | +0.1013 | -0.12% | n/a | 11506/0 |
| Relative Volume | -0.0789 | +0.0619 | -0.1207 | -0.11% | n/a | 11352/0 |
| Performance (Week) | +0.0723 | +0.0283 | +0.0588 | -0.62% | 0.30% | 5077/6297 |
| Institutional Transactions | -0.0709 | +0.0676 | -0.0913 | -1.16% | 2.40% | 3199/1830 |

## Risk dominance probes

| State | n | Mean long fwd | Mean fwd if score top quintile |
|---|---|---|---|
| EXTENDED | 232 | -2.03% | -2.58% |
| WASHED | 775 | 7.38% | -0.42% |

# Weight learning — decision log

_Generated 2026-08-13 17:36 EDT_

- label dates per horizon: 1d: 5, 2d: 4, 3d: 3
- primary horizon for promotion test: **1d** (5 dates)
- existing overrides: {'Price|ret': 0.3248288034498433, 'Performance (Month)|delta': 1.0103895505289044, 'Average Volume|delta': 0.8235276528272834, 'Relative Strength Index (14)|delta': 0.5150254789401248, 'Short Float|delta': 1.305315557100349, 'Institutional Transactions|level': 1.2725452838291316, 'Institutional Ownership|delta': 1.4413457739206899, 'Insider Transactions|level': 0.9528252174933872, 'Target Price|delta': 0.9924352340489596, 'Analyst Recom|delta': 1.2007084256548959, 'Sales Growth Quarter Over Quarter|level': 1.665043855385312, 'Sales Year Over Year TTM|level': 1.6363786585013698, 'Profit Margin|delta': 0.8836091924780013, 'EPS Surprise|level': 0.9063591426451629, 'n_catalysts|level': 1.5595336313235404}

## Per-rule aligned IC (direction corrected for polarity)

| Rule | Horizon | Mean aligned IC | Dates | Proposed × | Testable |
|---|---|---|---|---|---|
| Price|ret | 1d | -0.0494 | 4 | 0.293 | yes |
| Price|ret | 2d | -0.0776 | 3 | 0.274 | yes |
| Price|ret | 3d | -0.0966 | 2 | 0.262 | yes |
| Performance (Month)|delta | 1d | +0.0295 | 4 | 1.070 | yes |
| Performance (Month)|delta | 2d | -0.0076 | 3 | 0.995 | yes |
| Performance (Month)|delta | 3d | -0.0873 | 2 | 0.834 | yes |
| Average Volume|delta | 1d | -0.0099 | 4 | 0.807 | NO — logs only |
| Average Volume|delta | 2d | -0.0205 | 3 | 0.790 | NO — logs only |
| Average Volume|delta | 3d | -0.0187 | 2 | 0.793 | NO — logs only |
| Relative Strength Index (14)|delta | 1d | -0.0377 | 4 | 0.476 | yes |
| Relative Strength Index (14)|delta | 2d | -0.0592 | 3 | 0.454 | yes |
| Relative Strength Index (14)|delta | 3d | -0.0914 | 2 | 0.421 | yes |
| Short Float|delta | 1d | +0.0293 | 3 | 1.382 | NO — logs only |
| Short Float|delta | 2d | +0.0044 | 2 | 1.317 | NO — logs only |
| Short Float|delta | 3d | -0.0277 | 1 | 1.233 | NO — logs only |
| Institutional Transactions|level | 1d | +0.0122 | 5 | 1.304 | NO — logs only |
| Institutional Transactions|level | 2d | +0.0284 | 4 | 1.345 | NO — logs only |
| Institutional Transactions|level | 3d | +0.0385 | 3 | 1.371 | NO — logs only |
| Institutional Ownership|delta | 1d | +0.0194 | 4 | 1.497 | NO — logs only |
| Institutional Ownership|delta | 2d | +0.0301 | 3 | 1.528 | NO — logs only |
| Institutional Ownership|delta | 3d | +0.0277 | 2 | 1.521 | NO — logs only |
| Insider Transactions|level | 1d | -0.0100 | 5 | 0.934 | NO — logs only |
| Insider Transactions|level | 2d | -0.0138 | 4 | 0.927 | NO — logs only |
| Insider Transactions|level | 3d | -0.0177 | 3 | 0.919 | NO — logs only |
| Target Price|delta | 1d | +0.0028 | 4 | 0.998 | NO — logs only |
| Target Price|delta | 2d | +0.0016 | 3 | 0.996 | NO — logs only |
| Target Price|delta | 3d | -0.0014 | 2 | 0.990 | NO — logs only |
| Analyst Recom|delta | 1d | +0.0146 | 4 | 1.236 | NO — logs only |
| Analyst Recom|delta | 2d | +0.0051 | 3 | 1.213 | NO — logs only |
| Analyst Recom|delta | 3d | +0.0145 | 2 | 1.236 | NO — logs only |
| Sales Growth Quarter Over Quarter|level | 1d | +0.0348 | 5 | 1.781 | NO — logs only |
| Sales Growth Quarter Over Quarter|level | 2d | +0.0505 | 4 | 1.833 | NO — logs only |
| Sales Growth Quarter Over Quarter|level | 3d | +0.0689 | 3 | 1.895 | NO — logs only |
| Sales Year Over Year TTM|level | 1d | +0.0369 | 5 | 1.757 | NO — logs only |
| Sales Year Over Year TTM|level | 2d | +0.0559 | 4 | 1.819 | NO — logs only |
| Sales Year Over Year TTM|level | 3d | +0.0675 | 3 | 1.857 | NO — logs only |
| Profit Margin|delta | 1d | -0.0012 | 4 | 0.881 | NO — logs only |
| Profit Margin|delta | 2d | -0.0082 | 3 | 0.869 | NO — logs only |
| Profit Margin|delta | 3d | -0.0012 | 2 | 0.881 | NO — logs only |
| EPS Surprise|level | 1d | +0.0096 | 5 | 0.924 | NO — logs only |
| EPS Surprise|level | 2d | +0.0086 | 4 | 0.922 | NO — logs only |
| EPS Surprise|level | 3d | +0.0117 | 3 | 0.928 | NO — logs only |
| n_catalysts|level | 1d | +0.0211 | 5 | 1.625 | yes |
| n_catalysts|level | 2d | +0.0266 | 4 | 1.643 | yes |
| n_catalysts|level | 3d | +0.0441 | 3 | 1.697 | yes |
| Relative Volume|level | — | n/a (curved polarity) | — | 1.000 | not adjustable |
| Relative Strength Index (14)|level | — | n/a (curved polarity) | — | 1.000 | not adjustable |
| 50-Day Simple Moving Average|level | — | n/a (curved polarity) | — | 1.000 | not adjustable |
| 200-Day Simple Moving Average|level | — | n/a (curved polarity) | — | 1.000 | not adjustable |
| Volatility (Month)|level | — | n/a (curved polarity) | — | 1.000 | not adjustable |
| Short Float|level | — | n/a (curved polarity) | — | 1.000 | not adjustable |
| upside_pct|level | — | n/a (curved polarity) | — | 1.000 | not adjustable |
| Total Debt/Equity|level | — | n/a (curved polarity) | — | 1.000 | not adjustable |

## Champion vs challenger (1d score)

| Scan date | Horizon | Champion IC | Challenger IC | Δ |
|---|---|---|---|---|
| 2026-08-06 | 1d | +0.0958 | +0.0963 | +0.0005 |
| 2026-08-06 | 2d | +0.0636 | +0.0636 | +0.0000 |
| 2026-08-06 | 3d | +0.0815 | +0.0818 | +0.0003 |
| 2026-08-07 | 1d | -0.0339 | -0.0208 | +0.0132 |
| 2026-08-07 | 2d | -0.0242 | -0.0155 | +0.0087 |
| 2026-08-07 | 3d | -0.0009 | +0.0017 | +0.0026 |
| 2026-08-10 | 1d | -0.0491 | -0.0298 | +0.0192 |
| 2026-08-10 | 2d | -0.0596 | -0.0377 | +0.0220 |
| 2026-08-10 | 3d | -0.1054 | -0.0921 | +0.0133 |
| 2026-08-11 | 1d | +0.1007 | +0.1091 | +0.0084 |
| 2026-08-11 | 2d | +0.0174 | +0.0150 | -0.0024 |
| 2026-08-12 | 1d | -0.0472 | -0.0442 | +0.0030 |

_Champion reconstruction check: mean |rebuilt price category − stored price_score| = 0.3933 (should be ~0; large values mean the learner's model of the engine has drifted from score_engine — distrust this run)._

## Decision

PROMOTED — challenger mean IC gain +0.0089 on 1d, improved on 100% of 5 dates. New multipliers: Price|ret ×0.293, Performance (Month)|delta ×1.070, Average Volume|delta ×0.807, Relative Strength Index (14)|delta ×0.476, Short Float|delta ×1.382, Institutional Transactions|level ×1.304, Institutional Ownership|delta ×1.497, Insider Transactions|level ×0.934, Target Price|delta ×0.998, Analyst Recom|delta ×1.236, Sales Growth Quarter Over Quarter|level ×1.781, Sales Year Over Year TTM|level ×1.757, Profit Margin|delta ×0.881, EPS Surprise|level ×0.924, n_catalysts|level ×1.625

_Note: curved-polarity rules (rvol/rsi/sma/short/upside/debt curves) are never auto-adjusted; change those in score_rubric.py by hand with git history as the audit trail._

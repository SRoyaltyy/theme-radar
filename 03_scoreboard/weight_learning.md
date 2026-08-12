# Weight learning — decision log

_Generated 2026-08-12 04:22 EDT_

- label dates per horizon: 1d: 3, 2d: 2, 3d: 1
- primary horizon for promotion test: **1d** (3 dates)
- existing overrides: {'Price|ret': 0.6673068043289552, 'Performance (Month)|delta': 0.9711617174689832, 'Average Volume|delta': 0.9367094709700153, 'Relative Strength Index (14)|delta': 0.7908881727561615, 'Short Float|delta': 1.0961105433812623, 'Institutional Transactions|level': 1.0781819759102833, 'Institutional Ownership|delta': 1.1402542190370604, 'Insider Transactions|level': 0.9941540219682281, 'Target Price|delta': 0.995326882495001, 'Analyst Recom|delta': 1.0608330576452683, 'Sales Growth Quarter Over Quarter|level': 1.1829273347030094, 'Sales Year Over Year TTM|level': 1.1754233964762253, 'Profit Margin|delta': 0.9590876697623671, 'EPS Surprise|level': 0.964835204498689, 'n_catalysts|level': 1.1601223547032775}

## Per-rule aligned IC (direction corrected for polarity)

| Rule | Horizon | Mean aligned IC | Dates | Proposed × | Testable |
|---|---|---|---|---|---|
| Price|ret | 1d | -0.0916 | 2 | 0.545 | yes |
| Price|ret | 2d | -0.0711 | 1 | 0.572 | yes |
| Performance (Month)|delta | 1d | -0.0073 | 2 | 0.957 | yes |
| Performance (Month)|delta | 2d | +0.0107 | 1 | 0.992 | yes |
| Average Volume|delta | 1d | -0.0161 | 2 | 0.907 | NO — logs only |
| Average Volume|delta | 2d | -0.0146 | 1 | 0.909 | NO — logs only |
| Relative Strength Index (14)|delta | 1d | -0.0553 | 2 | 0.703 | yes |
| Relative Strength Index (14)|delta | 2d | -0.0437 | 1 | 0.722 | yes |
| Short Float|delta | 1d | +0.0235 | 1 | 1.148 | NO — logs only |
| Institutional Transactions|level | 1d | +0.0192 | 3 | 1.120 | NO — logs only |
| Institutional Transactions|level | 2d | +0.0268 | 2 | 1.136 | NO — logs only |
| Institutional Transactions|level | 3d | +0.0453 | 1 | 1.176 | NO — logs only |
| Institutional Ownership|delta | 1d | +0.0339 | 2 | 1.218 | NO — logs only |
| Institutional Ownership|delta | 2d | -0.0107 | 1 | 1.116 | NO — logs only |
| Insider Transactions|level | 1d | -0.0015 | 3 | 0.991 | NO — logs only |
| Insider Transactions|level | 2d | +0.0173 | 2 | 1.029 | NO — logs only |
| Insider Transactions|level | 3d | -0.0005 | 1 | 0.993 | NO — logs only |
| Target Price|delta | 1d | -0.0012 | 2 | 0.993 | NO — logs only |
| Target Price|delta | 2d | +0.0047 | 1 | 1.005 | NO — logs only |
| Analyst Recom|delta | 1d | +0.0150 | 2 | 1.093 | NO — logs only |
| Analyst Recom|delta | 2d | +0.0096 | 1 | 1.081 | NO — logs only |
| Sales Growth Quarter Over Quarter|level | 1d | +0.0438 | 3 | 1.287 | NO — logs only |
| Sales Growth Quarter Over Quarter|level | 2d | +0.0571 | 2 | 1.318 | NO — logs only |
| Sales Growth Quarter Over Quarter|level | 3d | +0.0643 | 1 | 1.335 | NO — logs only |
| Sales Year Over Year TTM|level | 1d | +0.0421 | 3 | 1.274 | NO — logs only |
| Sales Year Over Year TTM|level | 2d | +0.0529 | 2 | 1.300 | NO — logs only |
| Sales Year Over Year TTM|level | 3d | +0.0607 | 1 | 1.318 | NO — logs only |
| Profit Margin|delta | 1d | -0.0103 | 2 | 0.939 | NO — logs only |
| Profit Margin|delta | 2d | -0.0046 | 1 | 0.950 | NO — logs only |
| EPS Surprise|level | 1d | -0.0089 | 3 | 0.948 | NO — logs only |
| EPS Surprise|level | 2d | -0.0123 | 2 | 0.941 | NO — logs only |
| EPS Surprise|level | 3d | -0.0133 | 1 | 0.939 | NO — logs only |
| n_catalysts|level | 1d | +0.0385 | 3 | 1.250 | yes |
| n_catalysts|level | 2d | +0.0253 | 2 | 1.219 | yes |
| n_catalysts|level | 3d | +0.0530 | 1 | 1.283 | yes |
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
| 2026-08-07 | 1d | -0.0339 | -0.0283 | +0.0056 |
| 2026-08-07 | 2d | -0.0242 | -0.0199 | +0.0043 |
| 2026-08-10 | 1d | -0.0491 | -0.0385 | +0.0106 |

_Champion reconstruction check: mean |rebuilt price category − stored price_score| = 0.2366 (should be ~0; large values mean the learner's model of the engine has drifted from score_engine — distrust this run)._

## Decision

PROMOTED — challenger mean IC gain +0.0056 on 1d, improved on 100% of 3 dates. New multipliers: Price|ret ×0.545, Performance (Month)|delta ×0.957, Average Volume|delta ×0.907, Relative Strength Index (14)|delta ×0.703, Short Float|delta ×1.148, Institutional Transactions|level ×1.120, Institutional Ownership|delta ×1.218, Insider Transactions|level ×0.991, Target Price|delta ×0.993, Analyst Recom|delta ×1.093, Sales Growth Quarter Over Quarter|level ×1.287, Sales Year Over Year TTM|level ×1.274, Profit Margin|delta ×0.939, EPS Surprise|level ×0.948, n_catalysts|level ×1.250

_Note: curved-polarity rules (rvol/rsi/sma/short/upside/debt curves) are never auto-adjusted; change those in score_rubric.py by hand with git history as the audit trail._

# Weight learning — decision log

_Generated 2026-08-12 05:19 EDT_

- label dates per horizon: 1d: 3, 2d: 2, 3d: 1
- primary horizon for promotion test: **1d** (3 dates)
- existing overrides: {'Price|ret': 0.4452983711037225, 'Performance (Month)|delta': 0.9431550814773051, 'Average Volume|delta': 0.877424633004926, 'Relative Strength Index (14)|delta': 0.62550410180558, 'Short Float|delta': 1.201458323311566, 'Institutional Transactions|level': 1.1624763731778025, 'Institutional Ownership|delta': 1.3001796840318163, 'Insider Transactions|level': 0.9883422193956042, 'Target Price|delta': 0.9906756030172175, 'Analyst Recom|delta': 1.125366776193009, 'Sales Growth Quarter Over Quarter|level': 1.3993170791875655, 'Sales Year Over Year TTM|level': 1.3816201609837053, 'Profit Margin|delta': 0.9198491582902074, 'EPS Surprise|level': 0.9309069718400269, 'n_catalysts|level': 1.3458838778822773}

## Per-rule aligned IC (direction corrected for polarity)

| Rule | Horizon | Mean aligned IC | Dates | Proposed × | Testable |
|---|---|---|---|---|---|
| Price|ret | 1d | -0.0916 | 2 | 0.364 | yes |
| Price|ret | 2d | -0.0711 | 1 | 0.382 | yes |
| Performance (Month)|delta | 1d | -0.0073 | 2 | 0.929 | yes |
| Performance (Month)|delta | 2d | +0.0107 | 1 | 0.963 | yes |
| Average Volume|delta | 1d | -0.0161 | 2 | 0.849 | NO — logs only |
| Average Volume|delta | 2d | -0.0146 | 1 | 0.852 | NO — logs only |
| Relative Strength Index (14)|delta | 1d | -0.0553 | 2 | 0.556 | yes |
| Relative Strength Index (14)|delta | 2d | -0.0437 | 1 | 0.571 | yes |
| Short Float|delta | 1d | +0.0235 | 1 | 1.258 | NO — logs only |
| Institutional Transactions|level | 1d | +0.0192 | 3 | 1.207 | NO — logs only |
| Institutional Transactions|level | 2d | +0.0268 | 2 | 1.225 | NO — logs only |
| Institutional Transactions|level | 3d | +0.0453 | 1 | 1.268 | NO — logs only |
| Institutional Ownership|delta | 1d | +0.0339 | 2 | 1.388 | NO — logs only |
| Institutional Ownership|delta | 2d | -0.0107 | 1 | 1.272 | NO — logs only |
| Insider Transactions|level | 1d | -0.0015 | 3 | 0.985 | NO — logs only |
| Insider Transactions|level | 2d | +0.0173 | 2 | 1.023 | NO — logs only |
| Insider Transactions|level | 3d | -0.0005 | 1 | 0.987 | NO — logs only |
| Target Price|delta | 1d | -0.0012 | 2 | 0.988 | NO — logs only |
| Target Price|delta | 2d | +0.0047 | 1 | 1.000 | NO — logs only |
| Analyst Recom|delta | 1d | +0.0150 | 2 | 1.159 | NO — logs only |
| Analyst Recom|delta | 2d | +0.0096 | 1 | 1.147 | NO — logs only |
| Sales Growth Quarter Over Quarter|level | 1d | +0.0438 | 3 | 1.522 | NO — logs only |
| Sales Growth Quarter Over Quarter|level | 2d | +0.0571 | 2 | 1.559 | NO — logs only |
| Sales Growth Quarter Over Quarter|level | 3d | +0.0643 | 1 | 1.579 | NO — logs only |
| Sales Year Over Year TTM|level | 1d | +0.0421 | 3 | 1.498 | NO — logs only |
| Sales Year Over Year TTM|level | 2d | +0.0529 | 2 | 1.528 | NO — logs only |
| Sales Year Over Year TTM|level | 3d | +0.0607 | 1 | 1.549 | NO — logs only |
| Profit Margin|delta | 1d | -0.0103 | 2 | 0.901 | NO — logs only |
| Profit Margin|delta | 2d | -0.0046 | 1 | 0.911 | NO — logs only |
| EPS Surprise|level | 1d | -0.0089 | 3 | 0.914 | NO — logs only |
| EPS Surprise|level | 2d | -0.0123 | 2 | 0.908 | NO — logs only |
| EPS Surprise|level | 3d | -0.0133 | 1 | 0.906 | NO — logs only |
| n_catalysts|level | 1d | +0.0385 | 3 | 1.450 | yes |
| n_catalysts|level | 2d | +0.0253 | 2 | 1.414 | yes |
| n_catalysts|level | 3d | +0.0530 | 1 | 1.489 | yes |
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
| 2026-08-06 | 1d | +0.0958 | +0.0969 | +0.0012 |
| 2026-08-06 | 2d | +0.0636 | +0.0642 | +0.0006 |
| 2026-08-06 | 3d | +0.0815 | +0.0825 | +0.0010 |
| 2026-08-07 | 1d | -0.0339 | -0.0257 | +0.0082 |
| 2026-08-07 | 2d | -0.0242 | -0.0181 | +0.0061 |
| 2026-08-10 | 1d | -0.0491 | -0.0327 | +0.0164 |

_Champion reconstruction check: mean |rebuilt price category − stored price_score| = 0.3961 (should be ~0; large values mean the learner's model of the engine has drifted from score_engine — distrust this run)._

## Decision

PROMOTED — challenger mean IC gain +0.0086 on 1d, improved on 100% of 3 dates. New multipliers: Price|ret ×0.364, Performance (Month)|delta ×0.929, Average Volume|delta ×0.849, Relative Strength Index (14)|delta ×0.556, Short Float|delta ×1.258, Institutional Transactions|level ×1.207, Institutional Ownership|delta ×1.388, Insider Transactions|level ×0.985, Target Price|delta ×0.988, Analyst Recom|delta ×1.159, Sales Growth Quarter Over Quarter|level ×1.522, Sales Year Over Year TTM|level ×1.498, Profit Margin|delta ×0.901, EPS Surprise|level ×0.914, n_catalysts|level ×1.450

_Note: curved-polarity rules (rvol/rsi/sma/short/upside/debt curves) are never auto-adjusted; change those in score_rubric.py by hand with git history as the audit trail._

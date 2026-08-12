# Weight learning — decision log

_Generated 2026-08-12 17:36 EDT_

- label dates per horizon: 1d: 4, 2d: 3, 3d: 2
- primary horizon for promotion test: **1d** (4 dates)
- existing overrides: {'Price|ret': 0.36375911376172987, 'Performance (Month)|delta': 0.9294561089120174, 'Average Volume|delta': 0.8492044834462719, 'Relative Strength Index (14)|delta': 0.5562726432759099, 'Short Float|delta': 1.2578703725395441, 'Institutional Transactions|level': 1.2070636414051228, 'Institutional Ownership|delta': 1.3883667992368758, 'Insider Transactions|level': 0.9854490714267117, 'Target Price|delta': 0.9883581206287305, 'Analyst Recom|delta': 1.1590912086582315, 'Sales Growth Quarter Over Quarter|level': 1.5219317198095426, 'Sales Year Over Year TTM|level': 1.4979103701464263, 'Profit Margin|delta': 0.9008360738387076, 'EPS Surprise|level': 0.914392917619847, 'n_catalysts|level': 1.449637745269303}

## Per-rule aligned IC (direction corrected for polarity)

| Rule | Horizon | Mean aligned IC | Dates | Proposed × | Testable |
|---|---|---|---|---|---|
| Price|ret | 1d | -0.0535 | 3 | 0.325 | yes |
| Price|ret | 2d | -0.1126 | 2 | 0.282 | yes |
| Price|ret | 3d | -0.0154 | 1 | 0.353 | yes |
| Performance (Month)|delta | 1d | +0.0435 | 3 | 1.010 | yes |
| Performance (Month)|delta | 2d | -0.0340 | 2 | 0.866 | yes |
| Performance (Month)|delta | 3d | -0.0417 | 1 | 0.852 | yes |
| Average Volume|delta | 1d | -0.0151 | 3 | 0.824 | NO — logs only |
| Average Volume|delta | 2d | -0.0172 | 2 | 0.820 | NO — logs only |
| Average Volume|delta | 3d | -0.0242 | 1 | 0.808 | NO — logs only |
| Relative Strength Index (14)|delta | 1d | -0.0371 | 3 | 0.515 | yes |
| Relative Strength Index (14)|delta | 2d | -0.0795 | 2 | 0.468 | yes |
| Relative Strength Index (14)|delta | 3d | -0.0389 | 1 | 0.513 | yes |
| Short Float|delta | 1d | +0.0189 | 2 | 1.305 | NO — logs only |
| Short Float|delta | 2d | +0.0131 | 1 | 1.291 | NO — logs only |
| Institutional Transactions|level | 1d | +0.0271 | 4 | 1.273 | NO — logs only |
| Institutional Transactions|level | 2d | +0.0388 | 3 | 1.301 | NO — logs only |
| Institutional Transactions|level | 3d | +0.0453 | 2 | 1.316 | NO — logs only |
| Institutional Ownership|delta | 1d | +0.0191 | 3 | 1.441 | NO — logs only |
| Institutional Ownership|delta | 2d | +0.0285 | 2 | 1.468 | NO — logs only |
| Institutional Ownership|delta | 3d | -0.0199 | 1 | 1.333 | NO — logs only |
| Insider Transactions|level | 1d | -0.0166 | 4 | 0.953 | NO — logs only |
| Insider Transactions|level | 2d | -0.0046 | 3 | 0.976 | NO — logs only |
| Insider Transactions|level | 3d | -0.0113 | 2 | 0.963 | NO — logs only |
| Target Price|delta | 1d | +0.0021 | 3 | 0.992 | NO — logs only |
| Target Price|delta | 2d | +0.0008 | 2 | 0.990 | NO — logs only |
| Target Price|delta | 3d | +0.0139 | 1 | 1.016 | NO — logs only |
| Analyst Recom|delta | 1d | +0.0180 | 3 | 1.201 | NO — logs only |
| Analyst Recom|delta | 2d | +0.0113 | 2 | 1.185 | NO — logs only |
| Analyst Recom|delta | 3d | +0.0129 | 1 | 1.189 | NO — logs only |
| Sales Growth Quarter Over Quarter|level | 1d | +0.0470 | 4 | 1.665 | NO — logs only |
| Sales Growth Quarter Over Quarter|level | 2d | +0.0578 | 3 | 1.698 | NO — logs only |
| Sales Growth Quarter Over Quarter|level | 3d | +0.0838 | 2 | 1.777 | NO — logs only |
| Sales Year Over Year TTM|level | 1d | +0.0462 | 4 | 1.636 | NO — logs only |
| Sales Year Over Year TTM|level | 2d | +0.0586 | 3 | 1.673 | NO — logs only |
| Sales Year Over Year TTM|level | 3d | +0.0728 | 2 | 1.716 | NO — logs only |
| Profit Margin|delta | 1d | -0.0096 | 3 | 0.884 | NO — logs only |
| Profit Margin|delta | 2d | -0.0089 | 2 | 0.885 | NO — logs only |
| Profit Margin|delta | 3d | +0.0060 | 1 | 0.912 | NO — logs only |
| EPS Surprise|level | 1d | -0.0044 | 4 | 0.906 | NO — logs only |
| EPS Surprise|level | 2d | -0.0097 | 3 | 0.897 | NO — logs only |
| EPS Surprise|level | 3d | -0.0017 | 2 | 0.911 | NO — logs only |
| n_catalysts|level | 1d | +0.0379 | 4 | 1.560 | yes |
| n_catalysts|level | 2d | +0.0392 | 3 | 1.563 | yes |
| n_catalysts|level | 3d | +0.0536 | 2 | 1.605 | yes |
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
| 2026-08-07 | 1d | -0.0339 | -0.0225 | +0.0114 |
| 2026-08-07 | 2d | -0.0242 | -0.0161 | +0.0080 |
| 2026-08-07 | 3d | -0.0009 | +0.0027 | +0.0037 |
| 2026-08-10 | 1d | -0.0491 | -0.0296 | +0.0195 |
| 2026-08-10 | 2d | -0.0596 | -0.0375 | +0.0222 |
| 2026-08-11 | 1d | +0.1007 | +0.1082 | +0.0074 |

_Champion reconstruction check: mean |rebuilt price category − stored price_score| = 0.4833 (should be ~0; large values mean the learner's model of the engine has drifted from score_engine — distrust this run)._

## Decision

PROMOTED — challenger mean IC gain +0.0099 on 1d, improved on 100% of 4 dates. New multipliers: Price|ret ×0.325, Performance (Month)|delta ×1.010, Average Volume|delta ×0.824, Relative Strength Index (14)|delta ×0.515, Short Float|delta ×1.305, Institutional Transactions|level ×1.273, Institutional Ownership|delta ×1.441, Insider Transactions|level ×0.953, Target Price|delta ×0.992, Analyst Recom|delta ×1.201, Sales Growth Quarter Over Quarter|level ×1.665, Sales Year Over Year TTM|level ×1.636, Profit Margin|delta ×0.884, EPS Surprise|level ×0.906, n_catalysts|level ×1.560

_Note: curved-polarity rules (rvol/rsi/sma/short/upside/debt curves) are never auto-adjusted; change those in score_rubric.py by hand with git history as the audit trail._

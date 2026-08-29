# Weight learning — decision log

_Generated 2026-08-28 22:58 EDT_

- label dates per horizon: 1d: 15, 2d: 14, 3d: 13
- primary horizon for promotion test: **1d** (15 dates)
- existing overrides: {'Price|ret': 0.25, 'Performance (Month)|delta': 1.293429190134703, 'Average Volume|delta': 0.7077000596510837, 'Relative Strength Index (14)|delta': 0.25, 'Short Float|delta': 1.659372381033694, 'Institutional Transactions|level': 1.5429669062577924, 'Institutional Ownership|delta': 1.8362775062901133, 'Insider Transactions|level': 0.8518978371749509, 'Target Price|delta': 1.1309402598648262, 'Analyst Recom|delta': 1.4931862945971204, 'Sales Growth Quarter Over Quarter|level': 2.0, 'Sales Year Over Year TTM|level': 2.0, 'Profit Margin|delta': 0.9696808921410759, 'EPS Surprise|level': 0.9330019373294487, 'n_catalysts|level': 1.8991908036184673}

## Per-rule aligned IC (direction corrected for polarity)

| Rule | Horizon | Mean aligned IC | Dates | Proposed × | Testable |
|---|---|---|---|---|---|
| Price|ret | 1d | -0.0745 | 14 | 0.250 | yes |
| Price|ret | 2d | -0.0641 | 13 | 0.250 | yes |
| Price|ret | 3d | -0.0281 | 12 | 0.250 | yes |
| Performance (Month)|delta | 1d | -0.0006 | 14 | 1.292 | yes |
| Performance (Month)|delta | 2d | -0.0269 | 13 | 1.224 | yes |
| Performance (Month)|delta | 3d | -0.0422 | 12 | 1.184 | yes |
| Average Volume|delta | 1d | -0.0093 | 14 | 0.695 | NO — logs only |
| Average Volume|delta | 2d | -0.0122 | 13 | 0.690 | NO — logs only |
| Average Volume|delta | 3d | -0.0115 | 12 | 0.691 | NO — logs only |
| Relative Strength Index (14)|delta | 1d | -0.0587 | 14 | 0.250 | yes |
| Relative Strength Index (14)|delta | 2d | -0.0621 | 13 | 0.250 | yes |
| Relative Strength Index (14)|delta | 3d | -0.0267 | 12 | 0.250 | yes |
| Short Float|delta | 1d | +0.0034 | 13 | 1.671 | NO — logs only |
| Short Float|delta | 2d | -0.0067 | 12 | 1.637 | NO — logs only |
| Short Float|delta | 3d | -0.0122 | 11 | 1.619 | NO — logs only |
| Institutional Transactions|level | 1d | -0.0080 | 15 | 1.518 | NO — logs only |
| Institutional Transactions|level | 2d | -0.0055 | 14 | 1.526 | NO — logs only |
| Institutional Transactions|level | 3d | -0.0052 | 13 | 1.527 | NO — logs only |
| Institutional Ownership|delta | 1d | +0.0004 | 14 | 1.838 | NO — logs only |
| Institutional Ownership|delta | 2d | +0.0084 | 13 | 1.867 | NO — logs only |
| Institutional Ownership|delta | 3d | +0.0046 | 12 | 1.853 | NO — logs only |
| Insider Transactions|level | 1d | +0.0048 | 15 | 0.860 | NO — logs only |
| Insider Transactions|level | 2d | +0.0100 | 14 | 0.869 | NO — logs only |
| Insider Transactions|level | 3d | +0.0180 | 13 | 0.883 | NO — logs only |
| Target Price|delta | 1d | +0.0030 | 14 | 1.138 | NO — logs only |
| Target Price|delta | 2d | +0.0027 | 13 | 1.137 | NO — logs only |
| Target Price|delta | 3d | +0.0007 | 12 | 1.133 | NO — logs only |
| Analyst Recom|delta | 1d | +0.0065 | 14 | 1.513 | NO — logs only |
| Analyst Recom|delta | 2d | -0.0027 | 13 | 1.485 | NO — logs only |
| Analyst Recom|delta | 3d | -0.0064 | 12 | 1.474 | NO — logs only |
| Sales Growth Quarter Over Quarter|level | 1d | +0.0132 | 15 | 2.000 | NO — logs only |
| Sales Growth Quarter Over Quarter|level | 2d | +0.0151 | 14 | 2.000 | NO — logs only |
| Sales Growth Quarter Over Quarter|level | 3d | +0.0170 | 13 | 2.000 | NO — logs only |
| Sales Year Over Year TTM|level | 1d | +0.0136 | 15 | 2.000 | NO — logs only |
| Sales Year Over Year TTM|level | 2d | +0.0174 | 14 | 2.000 | NO — logs only |
| Sales Year Over Year TTM|level | 3d | +0.0201 | 13 | 2.000 | NO — logs only |
| Profit Margin|delta | 1d | +0.0037 | 14 | 0.977 | NO — logs only |
| Profit Margin|delta | 2d | -0.0005 | 13 | 0.969 | NO — logs only |
| Profit Margin|delta | 3d | +0.0069 | 12 | 0.983 | NO — logs only |
| EPS Surprise|level | 1d | +0.0032 | 15 | 0.939 | NO — logs only |
| EPS Surprise|level | 2d | +0.0007 | 14 | 0.934 | NO — logs only |
| EPS Surprise|level | 3d | -0.0026 | 13 | 0.928 | NO — logs only |
| n_catalysts|level | 1d | -0.0063 | 15 | 1.875 | yes |
| n_catalysts|level | 2d | -0.0100 | 14 | 1.861 | yes |
| n_catalysts|level | 3d | -0.0135 | 13 | 1.848 | yes |
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
| 2026-08-06 | 1d | +0.0958 | +0.0952 | -0.0005 |
| 2026-08-06 | 2d | +0.0636 | +0.0636 | -0.0000 |
| 2026-08-06 | 3d | +0.0815 | +0.0812 | -0.0003 |
| 2026-08-07 | 1d | -0.0339 | -0.0166 | +0.0173 |
| 2026-08-07 | 2d | -0.0242 | -0.0145 | +0.0097 |
| 2026-08-07 | 3d | -0.0009 | -0.0020 | -0.0011 |
| 2026-08-10 | 1d | -0.0491 | -0.0318 | +0.0173 |
| 2026-08-10 | 2d | -0.0596 | -0.0405 | +0.0191 |
| 2026-08-10 | 3d | -0.1054 | -0.0938 | +0.0116 |
| 2026-08-11 | 1d | +0.1007 | +0.1122 | +0.0115 |
| 2026-08-11 | 2d | +0.0174 | +0.0172 | -0.0002 |
| 2026-08-11 | 3d | +0.0639 | +0.0584 | -0.0055 |
| 2026-08-12 | 1d | -0.0472 | -0.0414 | +0.0058 |
| 2026-08-12 | 2d | +0.0520 | +0.0494 | -0.0026 |
| 2026-08-12 | 3d | +0.0878 | +0.0704 | -0.0174 |
| 2026-08-13 | 1d | -0.0908 | -0.0858 | +0.0050 |
| 2026-08-13 | 2d | -0.1428 | -0.1337 | +0.0091 |
| 2026-08-13 | 3d | -0.1672 | -0.1636 | +0.0035 |
| 2026-08-14 | 1d | +0.1577 | +0.1666 | +0.0089 |
| 2026-08-14 | 2d | -0.1560 | -0.1596 | -0.0037 |
| 2026-08-14 | 3d | -0.1404 | -0.1397 | +0.0007 |
| 2026-08-17 | 1d | -0.2097 | -0.2089 | +0.0009 |
| 2026-08-17 | 2d | -0.1365 | -0.1363 | +0.0002 |
| 2026-08-17 | 3d | -0.1034 | -0.1007 | +0.0027 |
| 2026-08-18 | 1d | +0.0486 | +0.0485 | -0.0001 |
| 2026-08-18 | 2d | +0.0270 | +0.0278 | +0.0008 |
| 2026-08-18 | 3d | +0.0058 | +0.0051 | -0.0007 |
| 2026-08-19 | 1d | +0.0108 | +0.0127 | +0.0020 |
| 2026-08-19 | 2d | +0.0519 | +0.0501 | -0.0018 |
| 2026-08-19 | 3d | +0.1772 | +0.1793 | +0.0021 |
| 2026-08-20 | 1d | -0.0007 | -0.0022 | -0.0015 |
| 2026-08-20 | 2d | +0.0530 | +0.0516 | -0.0014 |
| 2026-08-20 | 3d | +0.0387 | +0.0373 | -0.0014 |
| 2026-08-21 | 1d | -0.0802 | -0.0792 | +0.0010 |
| 2026-08-21 | 2d | +0.0158 | +0.0168 | +0.0009 |
| 2026-08-21 | 3d | -0.0723 | -0.0717 | +0.0006 |
| 2026-08-24 | 1d | +0.0056 | +0.0093 | +0.0037 |
| 2026-08-24 | 2d | -0.0285 | -0.0248 | +0.0037 |
| 2026-08-24 | 3d | -0.0880 | -0.0870 | +0.0011 |
| 2026-08-25 | 1d | -0.0503 | -0.0482 | +0.0022 |
| 2026-08-25 | 2d | -0.1093 | -0.1081 | +0.0012 |
| 2026-08-26 | 1d | -0.0710 | -0.0712 | -0.0002 |

_Champion reconstruction check: mean |rebuilt price category − stored price_score| = 0.2095 (should be ~0; large values mean the learner's model of the engine has drifted from score_engine — distrust this run)._

## Decision

PROMOTED — challenger mean IC gain +0.0049 on 1d, improved on 73% of 15 dates. New multipliers: Performance (Month)|delta ×1.292, Average Volume|delta ×0.695, Short Float|delta ×1.671, Institutional Transactions|level ×1.518, Institutional Ownership|delta ×1.838, Insider Transactions|level ×0.860, Target Price|delta ×1.138, Analyst Recom|delta ×1.513, Profit Margin|delta ×0.977, EPS Surprise|level ×0.939, n_catalysts|level ×1.875

_Note: curved-polarity rules (rvol/rsi/sma/short/upside/debt curves) are never auto-adjusted; change those in score_rubric.py by hand with git history as the audit trail._

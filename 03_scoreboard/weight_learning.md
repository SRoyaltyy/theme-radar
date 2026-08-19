# Weight learning — decision log

_Generated 2026-08-19 17:18 EDT_

- label dates per horizon: 1d: 9, 2d: 8, 3d: 7
- primary horizon for promotion test: **1d** (9 dates)
- existing overrides: {'Price|ret': 0.25, 'Performance (Month)|delta': 1.158420684404411, 'Average Volume|delta': 0.7709289002322821, 'Relative Strength Index (14)|delta': 0.25345708100946657, 'Short Float|delta': 1.5953112327041707, 'Institutional Transactions|level': 1.5326010169324307, 'Institutional Ownership|delta': 1.687516490038983, 'Insider Transactions|level': 0.8093269183763848, 'Target Price|delta': 1.046605620394193, 'Analyst Recom|delta': 1.368486445713597, 'Sales Growth Quarter Over Quarter|level': 2.0, 'Sales Year Over Year TTM|level': 2.0, 'Profit Margin|delta': 0.9088277562401182, 'EPS Surprise|level': 0.9602741533954501, 'n_catalysts|level': 1.9168457054655073}

## Per-rule aligned IC (direction corrected for polarity)

| Rule | Horizon | Mean aligned IC | Dates | Proposed × | Testable |
|---|---|---|---|---|---|
| Price|ret | 1d | -0.0573 | 8 | 0.250 | yes |
| Price|ret | 2d | -0.0920 | 7 | 0.250 | yes |
| Price|ret | 3d | -0.0566 | 6 | 0.250 | yes |
| Performance (Month)|delta | 1d | +0.0063 | 8 | 1.173 | yes |
| Performance (Month)|delta | 2d | -0.0706 | 7 | 0.995 | yes |
| Performance (Month)|delta | 3d | -0.0779 | 6 | 0.978 | yes |
| Average Volume|delta | 1d | -0.0099 | 8 | 0.756 | NO — logs only |
| Average Volume|delta | 2d | -0.0064 | 7 | 0.761 | NO — logs only |
| Average Volume|delta | 3d | -0.0056 | 6 | 0.762 | NO — logs only |
| Relative Strength Index (14)|delta | 1d | -0.0550 | 8 | 0.250 | yes |
| Relative Strength Index (14)|delta | 2d | -0.0905 | 7 | 0.250 | yes |
| Relative Strength Index (14)|delta | 3d | -0.0445 | 6 | 0.250 | yes |
| Short Float|delta | 1d | +0.0081 | 7 | 1.621 | NO — logs only |
| Short Float|delta | 2d | -0.0041 | 6 | 1.582 | NO — logs only |
| Short Float|delta | 3d | -0.0116 | 5 | 1.558 | NO — logs only |
| Institutional Transactions|level | 1d | +0.0092 | 9 | 1.561 | NO — logs only |
| Institutional Transactions|level | 2d | +0.0232 | 8 | 1.604 | NO — logs only |
| Institutional Transactions|level | 3d | +0.0346 | 7 | 1.639 | NO — logs only |
| Institutional Ownership|delta | 1d | +0.0140 | 8 | 1.735 | NO — logs only |
| Institutional Ownership|delta | 2d | +0.0130 | 7 | 1.731 | NO — logs only |
| Institutional Ownership|delta | 3d | +0.0149 | 6 | 1.738 | NO — logs only |
| Insider Transactions|level | 1d | -0.0029 | 9 | 0.805 | NO — logs only |
| Insider Transactions|level | 2d | -0.0071 | 8 | 0.798 | NO — logs only |
| Insider Transactions|level | 3d | -0.0167 | 7 | 0.782 | NO — logs only |
| Target Price|delta | 1d | +0.0057 | 8 | 1.059 | NO — logs only |
| Target Price|delta | 2d | +0.0036 | 7 | 1.054 | NO — logs only |
| Target Price|delta | 3d | +0.0103 | 6 | 1.068 | NO — logs only |
| Analyst Recom|delta | 1d | +0.0084 | 8 | 1.392 | NO — logs only |
| Analyst Recom|delta | 2d | -0.0023 | 7 | 1.362 | NO — logs only |
| Analyst Recom|delta | 3d | +0.0003 | 6 | 1.369 | NO — logs only |
| Sales Growth Quarter Over Quarter|level | 1d | +0.0256 | 9 | 2.000 | NO — logs only |
| Sales Growth Quarter Over Quarter|level | 2d | +0.0387 | 8 | 2.000 | NO — logs only |
| Sales Growth Quarter Over Quarter|level | 3d | +0.0566 | 7 | 2.000 | NO — logs only |
| Sales Year Over Year TTM|level | 1d | +0.0249 | 9 | 2.000 | NO — logs only |
| Sales Year Over Year TTM|level | 2d | +0.0391 | 8 | 2.000 | NO — logs only |
| Sales Year Over Year TTM|level | 3d | +0.0535 | 7 | 2.000 | NO — logs only |
| Profit Margin|delta | 1d | +0.0045 | 8 | 0.917 | NO — logs only |
| Profit Margin|delta | 2d | +0.0005 | 7 | 0.910 | NO — logs only |
| Profit Margin|delta | 3d | +0.0088 | 6 | 0.925 | NO — logs only |
| EPS Surprise|level | 1d | -0.0011 | 9 | 0.958 | NO — logs only |
| EPS Surprise|level | 2d | +0.0061 | 8 | 0.972 | NO — logs only |
| EPS Surprise|level | 3d | +0.0113 | 7 | 0.982 | NO — logs only |
| n_catalysts|level | 1d | +0.0033 | 9 | 1.929 | yes |
| n_catalysts|level | 2d | -0.0036 | 8 | 1.903 | yes |
| n_catalysts|level | 3d | +0.0042 | 7 | 1.933 | yes |
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
| 2026-08-07 | 1d | -0.0339 | -0.0168 | +0.0171 |
| 2026-08-07 | 2d | -0.0242 | -0.0131 | +0.0111 |
| 2026-08-07 | 3d | -0.0009 | +0.0004 | +0.0013 |
| 2026-08-10 | 1d | -0.0491 | -0.0281 | +0.0210 |
| 2026-08-10 | 2d | -0.0596 | -0.0363 | +0.0233 |
| 2026-08-10 | 3d | -0.1054 | -0.0903 | +0.0151 |
| 2026-08-11 | 1d | +0.1007 | +0.1129 | +0.0122 |
| 2026-08-11 | 2d | +0.0174 | +0.0179 | +0.0005 |
| 2026-08-11 | 3d | +0.0639 | +0.0596 | -0.0043 |
| 2026-08-12 | 1d | -0.0472 | -0.0426 | +0.0047 |
| 2026-08-12 | 2d | +0.0520 | +0.0500 | -0.0020 |
| 2026-08-12 | 3d | +0.0878 | +0.0730 | -0.0147 |
| 2026-08-13 | 1d | -0.0908 | -0.0854 | +0.0054 |
| 2026-08-13 | 2d | -0.1428 | -0.1343 | +0.0085 |
| 2026-08-13 | 3d | -0.1672 | -0.1643 | +0.0029 |
| 2026-08-14 | 1d | +0.1577 | +0.1625 | +0.0048 |
| 2026-08-14 | 2d | -0.1560 | -0.1598 | -0.0039 |
| 2026-08-14 | 3d | -0.1404 | -0.1403 | +0.0001 |
| 2026-08-17 | 1d | -0.2097 | -0.2097 | +0.0001 |
| 2026-08-17 | 2d | -0.1365 | -0.1369 | -0.0004 |
| 2026-08-18 | 1d | +0.0486 | +0.0479 | -0.0007 |

_Champion reconstruction check: mean |rebuilt price category − stored price_score| = 0.2652 (should be ~0; large values mean the learner's model of the engine has drifted from score_engine — distrust this run)._

## Decision

PROMOTED — challenger mean IC gain +0.0072 on 1d, improved on 89% of 9 dates. New multipliers: Performance (Month)|delta ×1.173, Average Volume|delta ×0.756, Relative Strength Index (14)|delta ×0.250, Short Float|delta ×1.621, Institutional Transactions|level ×1.561, Institutional Ownership|delta ×1.735, Insider Transactions|level ×0.805, Target Price|delta ×1.059, Analyst Recom|delta ×1.392, Profit Margin|delta ×0.917, EPS Surprise|level ×0.958, n_catalysts|level ×1.929

_Note: curved-polarity rules (rvol/rsi/sma/short/upside/debt curves) are never auto-adjusted; change those in score_rubric.py by hand with git history as the audit trail._

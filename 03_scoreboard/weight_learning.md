# Weight learning — decision log

_Generated 2026-08-15 04:32 EDT_

- label dates per horizon: 1d: 6, 2d: 5, 3d: 4
- primary horizon for promotion test: **1d** (6 dates)
- existing overrides: {'Price|ret': 0.25, 'Performance (Month)|delta': 1.0748789800042493, 'Average Volume|delta': 0.7967841472039041, 'Relative Strength Index (14)|delta': 0.4023466195563533, 'Short Float|delta': 1.4420713076809448, 'Institutional Transactions|level': 1.3580369170607804, 'Institutional Ownership|delta': 1.5366532686602226, 'Insider Transactions|level': 0.901665435801283, 'Target Price|delta': 1.0052547357131567, 'Analyst Recom|delta': 1.267918419663856, 'Sales Growth Quarter Over Quarter|level': 1.933485284920823, 'Sales Year Over Year TTM|level': 1.909636517311839, 'Profit Margin|delta': 0.8850404263671232, 'EPS Surprise|level': 0.92963264405898, 'n_catalysts|level': 1.7118884261449432}

## Per-rule aligned IC (direction corrected for polarity)

| Rule | Horizon | Mean aligned IC | Dates | Proposed × | Testable |
|---|---|---|---|---|---|
| Price|ret | 1d | -0.0864 | 5 | 0.250 | yes |
| Price|ret | 2d | -0.0465 | 4 | 0.250 | yes |
| Price|ret | 3d | -0.0528 | 3 | 0.250 | yes |
| Performance (Month)|delta | 1d | +0.0023 | 5 | 1.080 | yes |
| Performance (Month)|delta | 2d | +0.0014 | 4 | 1.078 | yes |
| Performance (Month)|delta | 3d | -0.0418 | 3 | 0.985 | yes |
| Average Volume|delta | 1d | -0.0065 | 5 | 0.786 | NO — logs only |
| Average Volume|delta | 2d | -0.0131 | 4 | 0.776 | NO — logs only |
| Average Volume|delta | 3d | -0.0170 | 3 | 0.770 | NO — logs only |
| Relative Strength Index (14)|delta | 1d | -0.0775 | 5 | 0.340 | yes |
| Relative Strength Index (14)|delta | 2d | -0.0402 | 4 | 0.370 | yes |
| Relative Strength Index (14)|delta | 3d | -0.0567 | 3 | 0.357 | yes |
| Short Float|delta | 1d | +0.0218 | 4 | 1.505 | NO — logs only |
| Short Float|delta | 2d | +0.0107 | 3 | 1.473 | NO — logs only |
| Short Float|delta | 3d | -0.0139 | 2 | 1.402 | NO — logs only |
| Institutional Transactions|level | 1d | +0.0209 | 6 | 1.415 | NO — logs only |
| Institutional Transactions|level | 2d | +0.0259 | 5 | 1.429 | NO — logs only |
| Institutional Transactions|level | 3d | +0.0397 | 4 | 1.466 | NO — logs only |
| Institutional Ownership|delta | 1d | +0.0131 | 5 | 1.577 | NO — logs only |
| Institutional Ownership|delta | 2d | +0.0263 | 4 | 1.618 | NO — logs only |
| Institutional Ownership|delta | 3d | +0.0187 | 3 | 1.594 | NO — logs only |
| Insider Transactions|level | 1d | -0.0172 | 6 | 0.871 | NO — logs only |
| Insider Transactions|level | 2d | -0.0176 | 5 | 0.870 | NO — logs only |
| Insider Transactions|level | 3d | -0.0285 | 4 | 0.850 | NO — logs only |
| Target Price|delta | 1d | +0.0036 | 5 | 1.012 | NO — logs only |
| Target Price|delta | 2d | +0.0028 | 4 | 1.011 | NO — logs only |
| Target Price|delta | 3d | +0.0009 | 3 | 1.007 | NO — logs only |
| Analyst Recom|delta | 1d | +0.0130 | 5 | 1.301 | NO — logs only |
| Analyst Recom|delta | 2d | +0.0032 | 4 | 1.276 | NO — logs only |
| Analyst Recom|delta | 3d | +0.0099 | 3 | 1.293 | NO — logs only |
| Sales Growth Quarter Over Quarter|level | 1d | +0.0428 | 6 | 2.000 | NO — logs only |
| Sales Growth Quarter Over Quarter|level | 2d | +0.0507 | 5 | 2.000 | NO — logs only |
| Sales Growth Quarter Over Quarter|level | 3d | +0.0677 | 4 | 2.000 | NO — logs only |
| Sales Year Over Year TTM|level | 1d | +0.0434 | 6 | 2.000 | NO — logs only |
| Sales Year Over Year TTM|level | 2d | +0.0559 | 5 | 2.000 | NO — logs only |
| Sales Year Over Year TTM|level | 3d | +0.0713 | 4 | 2.000 | NO — logs only |
| Profit Margin|delta | 1d | +0.0020 | 5 | 0.889 | NO — logs only |
| Profit Margin|delta | 2d | -0.0012 | 4 | 0.883 | NO — logs only |
| Profit Margin|delta | 3d | -0.0016 | 3 | 0.882 | NO — logs only |
| EPS Surprise|level | 1d | +0.0031 | 6 | 0.935 | NO — logs only |
| EPS Surprise|level | 2d | +0.0155 | 5 | 0.959 | NO — logs only |
| EPS Surprise|level | 3d | +0.0186 | 4 | 0.964 | NO — logs only |
| n_catalysts|level | 1d | +0.0267 | 6 | 1.803 | yes |
| n_catalysts|level | 2d | +0.0247 | 5 | 1.796 | yes |
| n_catalysts|level | 3d | +0.0408 | 4 | 1.852 | yes |
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
| 2026-08-07 | 1d | -0.0339 | -0.0188 | +0.0151 |
| 2026-08-07 | 2d | -0.0242 | -0.0141 | +0.0100 |
| 2026-08-07 | 3d | -0.0009 | +0.0014 | +0.0024 |
| 2026-08-10 | 1d | -0.0491 | -0.0279 | +0.0212 |
| 2026-08-10 | 2d | -0.0596 | -0.0353 | +0.0244 |
| 2026-08-10 | 3d | -0.1054 | -0.0901 | +0.0153 |
| 2026-08-11 | 1d | +0.1007 | +0.1105 | +0.0098 |
| 2026-08-11 | 2d | +0.0174 | +0.0156 | -0.0018 |
| 2026-08-11 | 3d | +0.0639 | +0.0589 | -0.0049 |
| 2026-08-12 | 1d | -0.0472 | -0.0445 | +0.0027 |
| 2026-08-12 | 2d | +0.0520 | +0.0515 | -0.0005 |
| 2026-08-13 | 1d | -0.0908 | -0.0784 | +0.0124 |

_Champion reconstruction check: mean |rebuilt price category − stored price_score| = 0.3832 (should be ~0; large values mean the learner's model of the engine has drifted from score_engine — distrust this run)._

## Decision

PROMOTED — challenger mean IC gain +0.0103 on 1d, improved on 100% of 6 dates. New multipliers: Performance (Month)|delta ×1.080, Average Volume|delta ×0.786, Relative Strength Index (14)|delta ×0.340, Short Float|delta ×1.505, Institutional Transactions|level ×1.415, Institutional Ownership|delta ×1.577, Insider Transactions|level ×0.871, Target Price|delta ×1.012, Analyst Recom|delta ×1.301, Sales Growth Quarter Over Quarter|level ×2.000, Sales Year Over Year TTM|level ×2.000, Profit Margin|delta ×0.889, EPS Surprise|level ×0.935, n_catalysts|level ×1.803

_Note: curved-polarity rules (rvol/rsi/sma/short/upside/debt curves) are never auto-adjusted; change those in score_rubric.py by hand with git history as the audit trail._

# Weight learning — decision log

_Generated 2026-08-26 20:22 EDT_

- label dates per horizon: 1d: 14, 2d: 13, 3d: 12
- primary horizon for promotion test: **1d** (14 dates)
- existing overrides: {'Price|ret': 0.25, 'Performance (Month)|delta': 1.2335723163535777, 'Average Volume|delta': 0.7259803850966688, 'Relative Strength Index (14)|delta': 0.25, 'Short Float|delta': 1.6352015623291074, 'Institutional Transactions|level': 1.5507473060753008, 'Institutional Ownership|delta': 1.8093409726571392, 'Insider Transactions|level': 0.8473715121655647, 'Target Price|delta': 1.1135220199708062, 'Analyst Recom|delta': 1.4480049634356833, 'Sales Growth Quarter Over Quarter|level': 2.0, 'Sales Year Over Year TTM|level': 2.0, 'Profit Margin|delta': 0.9592710894879852, 'EPS Surprise|level': 0.9381364817811603, 'n_catalysts|level': 1.900195319058596}

## Per-rule aligned IC (direction corrected for polarity)

| Rule | Horizon | Mean aligned IC | Dates | Proposed × | Testable |
|---|---|---|---|---|---|
| Price|ret | 1d | -0.0808 | 13 | 0.250 | yes |
| Price|ret | 2d | -0.0515 | 12 | 0.250 | yes |
| Price|ret | 3d | -0.0199 | 11 | 0.250 | yes |
| Performance (Month)|delta | 1d | +0.0069 | 13 | 1.250 | yes |
| Performance (Month)|delta | 2d | -0.0241 | 12 | 1.174 | yes |
| Performance (Month)|delta | 3d | -0.0413 | 11 | 1.132 | yes |
| Average Volume|delta | 1d | -0.0049 | 13 | 0.719 | NO — logs only |
| Average Volume|delta | 2d | -0.0078 | 12 | 0.715 | NO — logs only |
| Average Volume|delta | 3d | -0.0063 | 11 | 0.717 | NO — logs only |
| Relative Strength Index (14)|delta | 1d | -0.0631 | 13 | 0.250 | yes |
| Relative Strength Index (14)|delta | 2d | -0.0562 | 12 | 0.250 | yes |
| Relative Strength Index (14)|delta | 3d | -0.0147 | 11 | 0.250 | yes |
| Short Float|delta | 1d | +0.0025 | 12 | 1.643 | NO — logs only |
| Short Float|delta | 2d | -0.0077 | 11 | 1.610 | NO — logs only |
| Short Float|delta | 3d | -0.0142 | 10 | 1.589 | NO — logs only |
| Institutional Transactions|level | 1d | -0.0042 | 14 | 1.538 | NO — logs only |
| Institutional Transactions|level | 2d | +0.0002 | 13 | 1.551 | NO — logs only |
| Institutional Transactions|level | 3d | -0.0026 | 12 | 1.543 | NO — logs only |
| Institutional Ownership|delta | 1d | +0.0024 | 13 | 1.818 | NO — logs only |
| Institutional Ownership|delta | 2d | +0.0058 | 12 | 1.830 | NO — logs only |
| Institutional Ownership|delta | 3d | +0.0069 | 11 | 1.834 | NO — logs only |
| Insider Transactions|level | 1d | +0.0028 | 14 | 0.852 | NO — logs only |
| Insider Transactions|level | 2d | +0.0128 | 13 | 0.869 | NO — logs only |
| Insider Transactions|level | 3d | +0.0201 | 12 | 0.881 | NO — logs only |
| Target Price|delta | 1d | +0.0026 | 13 | 1.119 | NO — logs only |
| Target Price|delta | 2d | +0.0036 | 12 | 1.122 | NO — logs only |
| Target Price|delta | 3d | +0.0010 | 11 | 1.116 | NO — logs only |
| Analyst Recom|delta | 1d | +0.0080 | 13 | 1.471 | NO — logs only |
| Analyst Recom|delta | 2d | -0.0017 | 12 | 1.443 | NO — logs only |
| Analyst Recom|delta | 3d | -0.0067 | 11 | 1.428 | NO — logs only |
| Sales Growth Quarter Over Quarter|level | 1d | +0.0160 | 14 | 2.000 | NO — logs only |
| Sales Growth Quarter Over Quarter|level | 2d | +0.0173 | 13 | 2.000 | NO — logs only |
| Sales Growth Quarter Over Quarter|level | 3d | +0.0197 | 12 | 2.000 | NO — logs only |
| Sales Year Over Year TTM|level | 1d | +0.0151 | 14 | 2.000 | NO — logs only |
| Sales Year Over Year TTM|level | 2d | +0.0196 | 13 | 2.000 | NO — logs only |
| Sales Year Over Year TTM|level | 3d | +0.0201 | 12 | 2.000 | NO — logs only |
| Profit Margin|delta | 1d | +0.0029 | 13 | 0.965 | NO — logs only |
| Profit Margin|delta | 2d | +0.0006 | 12 | 0.960 | NO — logs only |
| Profit Margin|delta | 3d | +0.0086 | 11 | 0.976 | NO — logs only |
| EPS Surprise|level | 1d | -0.0013 | 14 | 0.936 | NO — logs only |
| EPS Surprise|level | 2d | -0.0056 | 13 | 0.928 | NO — logs only |
| EPS Surprise|level | 3d | -0.0037 | 12 | 0.931 | NO — logs only |
| n_catalysts|level | 1d | -0.0012 | 14 | 1.896 | yes |
| n_catalysts|level | 2d | -0.0056 | 13 | 1.879 | yes |
| n_catalysts|level | 3d | -0.0124 | 12 | 1.853 | yes |
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
| 2026-08-07 | 1d | -0.0339 | -0.0167 | +0.0172 |
| 2026-08-07 | 2d | -0.0242 | -0.0145 | +0.0097 |
| 2026-08-07 | 3d | -0.0009 | -0.0019 | -0.0010 |
| 2026-08-10 | 1d | -0.0491 | -0.0317 | +0.0174 |
| 2026-08-10 | 2d | -0.0596 | -0.0405 | +0.0191 |
| 2026-08-10 | 3d | -0.1054 | -0.0938 | +0.0116 |
| 2026-08-11 | 1d | +0.1007 | +0.1119 | +0.0112 |
| 2026-08-11 | 2d | +0.0174 | +0.0169 | -0.0005 |
| 2026-08-11 | 3d | +0.0639 | +0.0582 | -0.0057 |
| 2026-08-12 | 1d | -0.0472 | -0.0421 | +0.0051 |
| 2026-08-12 | 2d | +0.0520 | +0.0490 | -0.0030 |
| 2026-08-12 | 3d | +0.0878 | +0.0704 | -0.0174 |
| 2026-08-13 | 1d | -0.0908 | -0.0858 | +0.0050 |
| 2026-08-13 | 2d | -0.1428 | -0.1337 | +0.0091 |
| 2026-08-13 | 3d | -0.1672 | -0.1636 | +0.0035 |
| 2026-08-14 | 1d | +0.1577 | +0.1659 | +0.0083 |
| 2026-08-14 | 2d | -0.1560 | -0.1597 | -0.0038 |
| 2026-08-14 | 3d | -0.1404 | -0.1397 | +0.0006 |
| 2026-08-17 | 1d | -0.2097 | -0.2094 | +0.0004 |
| 2026-08-17 | 2d | -0.1365 | -0.1363 | +0.0002 |
| 2026-08-17 | 3d | -0.1034 | -0.1017 | +0.0017 |
| 2026-08-18 | 1d | +0.0486 | +0.0487 | +0.0001 |
| 2026-08-18 | 2d | +0.0270 | +0.0277 | +0.0007 |
| 2026-08-18 | 3d | +0.0058 | +0.0056 | -0.0002 |
| 2026-08-19 | 1d | +0.0108 | +0.0115 | +0.0007 |
| 2026-08-19 | 2d | +0.0519 | +0.0511 | -0.0008 |
| 2026-08-19 | 3d | +0.1772 | +0.1786 | +0.0014 |
| 2026-08-20 | 1d | -0.0007 | -0.0011 | -0.0004 |
| 2026-08-20 | 2d | +0.0530 | +0.0522 | -0.0007 |
| 2026-08-20 | 3d | +0.0387 | +0.0382 | -0.0006 |
| 2026-08-21 | 1d | -0.0802 | -0.0798 | +0.0004 |
| 2026-08-21 | 2d | +0.0158 | +0.0160 | +0.0001 |
| 2026-08-21 | 3d | -0.0723 | -0.0722 | +0.0001 |
| 2026-08-24 | 1d | +0.0056 | +0.0068 | +0.0012 |
| 2026-08-24 | 2d | -0.0285 | -0.0271 | +0.0014 |
| 2026-08-25 | 1d | -0.0503 | -0.0494 | +0.0009 |

_Champion reconstruction check: mean |rebuilt price category − stored price_score| = 0.1957 (should be ~0; large values mean the learner's model of the engine has drifted from score_engine — distrust this run)._

## Decision

PROMOTED — challenger mean IC gain +0.0048 on 1d, improved on 86% of 14 dates. New multipliers: Performance (Month)|delta ×1.250, Average Volume|delta ×0.719, Short Float|delta ×1.643, Institutional Transactions|level ×1.538, Institutional Ownership|delta ×1.818, Insider Transactions|level ×0.852, Target Price|delta ×1.119, Analyst Recom|delta ×1.471, Profit Margin|delta ×0.965, EPS Surprise|level ×0.936, n_catalysts|level ×1.896

_Note: curved-polarity rules (rvol/rsi/sma/short/upside/debt curves) are never auto-adjusted; change those in score_rubric.py by hand with git history as the audit trail._

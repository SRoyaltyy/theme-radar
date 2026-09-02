# Weight learning — decision log

_Generated 2026-09-02 18:56 EDT_

- label dates per horizon: 1d: 18, 2d: 17, 3d: 16
- primary horizon for promotion test: **1d** (18 dates)
- existing overrides: {'Price|ret': 0.25, 'Performance (Month)|delta': 1.2671041247197685, 'Average Volume|delta': 0.6685517273545409, 'Relative Strength Index (14)|delta': 0.25, 'Short Float|delta': 1.6870275254821043, 'Institutional Transactions|level': 1.4691366378713675, 'Institutional Ownership|delta': 1.8312003809075459, 'Insider Transactions|level': 0.8814156415844945, 'Target Price|delta': 1.1540399417176792, 'Analyst Recom|delta': 1.5658718293230052, 'Sales Growth Quarter Over Quarter|level': 2.0, 'Sales Year Over Year TTM|level': 2.0, 'Profit Margin|delta': 0.9893413583719363, 'EPS Surprise|level': 0.9527011918609353, 'n_catalysts|level': 1.8125146186745298}

## Per-rule aligned IC (direction corrected for polarity)

| Rule | Horizon | Mean aligned IC | Dates | Proposed × | Testable |
|---|---|---|---|---|---|
| Price|ret | 1d | -0.0608 | 17 | 0.250 | yes |
| Price|ret | 2d | -0.0453 | 16 | 0.250 | yes |
| Price|ret | 3d | -0.0241 | 15 | 0.250 | yes |
| Performance (Month)|delta | 1d | -0.0129 | 17 | 1.234 | yes |
| Performance (Month)|delta | 2d | -0.0181 | 16 | 1.221 | yes |
| Performance (Month)|delta | 3d | -0.0355 | 15 | 1.177 | yes |
| Average Volume|delta | 1d | -0.0083 | 17 | 0.657 | NO — logs only |
| Average Volume|delta | 2d | -0.0104 | 16 | 0.655 | NO — logs only |
| Average Volume|delta | 3d | -0.0138 | 15 | 0.650 | NO — logs only |
| Relative Strength Index (14)|delta | 1d | -0.0482 | 17 | 0.250 | yes |
| Relative Strength Index (14)|delta | 2d | -0.0536 | 16 | 0.250 | yes |
| Relative Strength Index (14)|delta | 3d | -0.0241 | 15 | 0.250 | yes |
| Short Float|delta | 1d | +0.0013 | 16 | 1.692 | NO — logs only |
| Short Float|delta | 2d | -0.0047 | 15 | 1.671 | NO — logs only |
| Short Float|delta | 3d | -0.0092 | 14 | 1.656 | NO — logs only |
| Institutional Transactions|level | 1d | -0.0060 | 18 | 1.452 | NO — logs only |
| Institutional Transactions|level | 2d | -0.0077 | 17 | 1.447 | NO — logs only |
| Institutional Transactions|level | 3d | -0.0110 | 16 | 1.437 | NO — logs only |
| Institutional Ownership|delta | 1d | +0.0014 | 17 | 1.836 | NO — logs only |
| Institutional Ownership|delta | 2d | +0.0041 | 16 | 1.846 | NO — logs only |
| Institutional Ownership|delta | 3d | +0.0007 | 15 | 1.834 | NO — logs only |
| Insider Transactions|level | 1d | +0.0057 | 18 | 0.891 | NO — logs only |
| Insider Transactions|level | 2d | +0.0130 | 17 | 0.904 | NO — logs only |
| Insider Transactions|level | 3d | +0.0180 | 16 | 0.913 | NO — logs only |
| Target Price|delta | 1d | +0.0053 | 17 | 1.166 | NO — logs only |
| Target Price|delta | 2d | +0.0037 | 16 | 1.163 | NO — logs only |
| Target Price|delta | 3d | +0.0022 | 15 | 1.159 | NO — logs only |
| Analyst Recom|delta | 1d | +0.0104 | 17 | 1.599 | NO — logs only |
| Analyst Recom|delta | 2d | -0.0026 | 16 | 1.558 | NO — logs only |
| Analyst Recom|delta | 3d | -0.0060 | 15 | 1.547 | NO — logs only |
| Sales Growth Quarter Over Quarter|level | 1d | +0.0125 | 18 | 2.000 | NO — logs only |
| Sales Growth Quarter Over Quarter|level | 2d | +0.0115 | 17 | 2.000 | NO — logs only |
| Sales Growth Quarter Over Quarter|level | 3d | +0.0134 | 16 | 2.000 | NO — logs only |
| Sales Year Over Year TTM|level | 1d | +0.0106 | 18 | 2.000 | NO — logs only |
| Sales Year Over Year TTM|level | 2d | +0.0118 | 17 | 2.000 | NO — logs only |
| Sales Year Over Year TTM|level | 3d | +0.0144 | 16 | 2.000 | NO — logs only |
| Profit Margin|delta | 1d | +0.0041 | 17 | 0.997 | NO — logs only |
| Profit Margin|delta | 2d | +0.0016 | 16 | 0.993 | NO — logs only |
| Profit Margin|delta | 3d | +0.0057 | 15 | 1.001 | NO — logs only |
| EPS Surprise|level | 1d | +0.0023 | 18 | 0.957 | NO — logs only |
| EPS Surprise|level | 2d | +0.0047 | 17 | 0.962 | NO — logs only |
| EPS Surprise|level | 3d | +0.0049 | 16 | 0.962 | NO — logs only |
| n_catalysts|level | 1d | -0.0103 | 18 | 1.775 | yes |
| n_catalysts|level | 2d | -0.0206 | 17 | 1.738 | yes |
| n_catalysts|level | 3d | -0.0238 | 16 | 1.726 | yes |
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
| 2026-08-07 | 1d | -0.0339 | -0.0168 | +0.0172 |
| 2026-08-07 | 2d | -0.0242 | -0.0145 | +0.0096 |
| 2026-08-07 | 3d | -0.0009 | -0.0019 | -0.0010 |
| 2026-08-10 | 1d | -0.0491 | -0.0317 | +0.0174 |
| 2026-08-10 | 2d | -0.0596 | -0.0405 | +0.0191 |
| 2026-08-10 | 3d | -0.1054 | -0.0938 | +0.0116 |
| 2026-08-11 | 1d | +0.1007 | +0.1119 | +0.0111 |
| 2026-08-11 | 2d | +0.0174 | +0.0169 | -0.0005 |
| 2026-08-11 | 3d | +0.0639 | +0.0582 | -0.0057 |
| 2026-08-12 | 1d | -0.0472 | -0.0422 | +0.0051 |
| 2026-08-12 | 2d | +0.0520 | +0.0490 | -0.0030 |
| 2026-08-12 | 3d | +0.0878 | +0.0705 | -0.0173 |
| 2026-08-13 | 1d | -0.0908 | -0.0857 | +0.0051 |
| 2026-08-13 | 2d | -0.1428 | -0.1337 | +0.0091 |
| 2026-08-13 | 3d | -0.1672 | -0.1635 | +0.0036 |
| 2026-08-14 | 1d | +0.1577 | +0.1659 | +0.0082 |
| 2026-08-14 | 2d | -0.1560 | -0.1598 | -0.0038 |
| 2026-08-14 | 3d | -0.1404 | -0.1398 | +0.0006 |
| 2026-08-17 | 1d | -0.2097 | -0.2094 | +0.0003 |
| 2026-08-17 | 2d | -0.1365 | -0.1363 | +0.0002 |
| 2026-08-17 | 3d | -0.1034 | -0.1017 | +0.0017 |
| 2026-08-18 | 1d | +0.0486 | +0.0487 | +0.0001 |
| 2026-08-18 | 2d | +0.0270 | +0.0277 | +0.0007 |
| 2026-08-18 | 3d | +0.0058 | +0.0056 | -0.0002 |
| 2026-08-19 | 1d | +0.0108 | +0.0115 | +0.0008 |
| 2026-08-19 | 2d | +0.0519 | +0.0511 | -0.0008 |
| 2026-08-19 | 3d | +0.1772 | +0.1785 | +0.0013 |
| 2026-08-20 | 1d | -0.0007 | -0.0006 | +0.0001 |
| 2026-08-20 | 2d | +0.0530 | +0.0526 | -0.0003 |
| 2026-08-20 | 3d | +0.0387 | +0.0386 | -0.0001 |
| 2026-08-21 | 1d | -0.0802 | -0.0796 | +0.0006 |
| 2026-08-21 | 2d | +0.0158 | +0.0163 | +0.0004 |
| 2026-08-21 | 3d | -0.0723 | -0.0720 | +0.0003 |
| 2026-08-24 | 1d | +0.0056 | +0.0054 | -0.0002 |
| 2026-08-24 | 2d | -0.0285 | -0.0287 | -0.0002 |
| 2026-08-24 | 3d | -0.0880 | -0.0886 | -0.0006 |
| 2026-08-25 | 1d | -0.0503 | -0.0508 | -0.0005 |
| 2026-08-25 | 2d | -0.1093 | -0.1104 | -0.0011 |
| 2026-08-25 | 3d | -0.0661 | -0.0676 | -0.0015 |
| 2026-08-26 | 1d | -0.0710 | -0.0714 | -0.0004 |
| 2026-08-26 | 2d | -0.0146 | -0.0151 | -0.0005 |
| 2026-08-26 | 3d | -0.0019 | -0.0024 | -0.0005 |
| 2026-08-28 | 1d | -0.0442 | -0.0438 | +0.0005 |
| 2026-08-28 | 2d | +0.0258 | +0.0246 | -0.0012 |
| 2026-08-28 | 3d | +0.0108 | +0.0110 | +0.0002 |
| 2026-08-31 | 1d | -0.0065 | -0.0071 | -0.0006 |
| 2026-08-31 | 2d | +0.0398 | +0.0403 | +0.0006 |
| 2026-09-01 | 1d | -0.0847 | -0.0811 | +0.0036 |

_Champion reconstruction check: mean |rebuilt price category − stored price_score| = 0.1678 (should be ~0; large values mean the learner's model of the engine has drifted from score_engine — distrust this run)._

## Decision

PROMOTED — challenger mean IC gain +0.0038 on 1d, improved on 72% of 18 dates. New multipliers: Performance (Month)|delta ×1.234, Average Volume|delta ×0.657, Short Float|delta ×1.692, Institutional Transactions|level ×1.452, Institutional Ownership|delta ×1.836, Insider Transactions|level ×0.891, Target Price|delta ×1.166, Analyst Recom|delta ×1.599, Profit Margin|delta ×0.997, EPS Surprise|level ×0.957, n_catalysts|level ×1.775

_Note: curved-polarity rules (rvol/rsi/sma/short/upside/debt curves) are never auto-adjusted; change those in score_rubric.py by hand with git history as the audit trail._

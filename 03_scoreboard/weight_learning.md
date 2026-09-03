# Weight learning — decision log

_Generated 2026-09-03 18:56 EDT_

- label dates per horizon: 1d: 19, 2d: 18, 3d: 17
- primary horizon for promotion test: **1d** (19 dates)
- existing overrides: {'Price|ret': 0.25, 'Performance (Month)|delta': 1.2344032145949224, 'Average Volume|delta': 0.6574405081346789, 'Relative Strength Index (14)|delta': 0.25, 'Short Float|delta': 1.6915720994197565, 'Institutional Transactions|level': 1.4515698188806738, 'Institutional Ownership|delta': 1.8364191820557776, 'Insider Transactions|level': 0.8914160645008861, 'Target Price|delta': 1.166164076887458, 'Analyst Recom|delta': 1.5985489320892463, 'Sales Growth Quarter Over Quarter|level': 2.0, 'Sales Year Over Year TTM|level': 2.0, 'Profit Margin|delta': 0.997481836573653, 'EPS Surprise|level': 0.9571606649511294, 'n_catalysts|level': 1.7752711849143379}

## Per-rule aligned IC (direction corrected for polarity)

| Rule | Horizon | Mean aligned IC | Dates | Proposed × | Testable |
|---|---|---|---|---|---|
| Price|ret | 1d | -0.0569 | 18 | 0.250 | yes |
| Price|ret | 2d | -0.0597 | 17 | 0.250 | yes |
| Price|ret | 3d | -0.0244 | 16 | 0.250 | yes |
| Performance (Month)|delta | 1d | -0.0223 | 18 | 1.179 | yes |
| Performance (Month)|delta | 2d | -0.0367 | 17 | 1.144 | yes |
| Performance (Month)|delta | 3d | -0.0304 | 16 | 1.159 | yes |
| Average Volume|delta | 1d | -0.0112 | 18 | 0.643 | NO — logs only |
| Average Volume|delta | 2d | -0.0112 | 17 | 0.643 | NO — logs only |
| Average Volume|delta | 3d | -0.0105 | 16 | 0.644 | NO — logs only |
| Relative Strength Index (14)|delta | 1d | -0.0448 | 18 | 0.250 | yes |
| Relative Strength Index (14)|delta | 2d | -0.0601 | 17 | 0.250 | yes |
| Relative Strength Index (14)|delta | 3d | -0.0265 | 16 | 0.250 | yes |
| Short Float|delta | 1d | +0.0028 | 17 | 1.701 | NO — logs only |
| Short Float|delta | 2d | -0.0050 | 16 | 1.675 | NO — logs only |
| Short Float|delta | 3d | -0.0089 | 15 | 1.661 | NO — logs only |
| Institutional Transactions|level | 1d | -0.0070 | 19 | 1.431 | NO — logs only |
| Institutional Transactions|level | 2d | -0.0066 | 18 | 1.432 | NO — logs only |
| Institutional Transactions|level | 3d | -0.0100 | 17 | 1.423 | NO — logs only |
| Institutional Ownership|delta | 1d | +0.0034 | 18 | 1.849 | NO — logs only |
| Institutional Ownership|delta | 2d | +0.0046 | 17 | 1.853 | NO — logs only |
| Institutional Ownership|delta | 3d | +0.0018 | 16 | 1.843 | NO — logs only |
| Insider Transactions|level | 1d | +0.0029 | 19 | 0.897 | NO — logs only |
| Insider Transactions|level | 2d | +0.0103 | 18 | 0.910 | NO — logs only |
| Insider Transactions|level | 3d | +0.0157 | 17 | 0.919 | NO — logs only |
| Target Price|delta | 1d | +0.0067 | 18 | 1.182 | NO — logs only |
| Target Price|delta | 2d | +0.0049 | 17 | 1.178 | NO — logs only |
| Target Price|delta | 3d | +0.0026 | 16 | 1.172 | NO — logs only |
| Analyst Recom|delta | 1d | +0.0108 | 18 | 1.633 | NO — logs only |
| Analyst Recom|delta | 2d | -0.0015 | 17 | 1.594 | NO — logs only |
| Analyst Recom|delta | 3d | -0.0060 | 16 | 1.579 | NO — logs only |
| Sales Growth Quarter Over Quarter|level | 1d | +0.0159 | 19 | 2.000 | NO — logs only |
| Sales Growth Quarter Over Quarter|level | 2d | +0.0150 | 18 | 2.000 | NO — logs only |
| Sales Growth Quarter Over Quarter|level | 3d | +0.0159 | 17 | 2.000 | NO — logs only |
| Sales Year Over Year TTM|level | 1d | +0.0163 | 19 | 2.000 | NO — logs only |
| Sales Year Over Year TTM|level | 2d | +0.0169 | 18 | 2.000 | NO — logs only |
| Sales Year Over Year TTM|level | 3d | +0.0178 | 17 | 2.000 | NO — logs only |
| Profit Margin|delta | 1d | +0.0051 | 18 | 1.008 | NO — logs only |
| Profit Margin|delta | 2d | +0.0011 | 17 | 1.000 | NO — logs only |
| Profit Margin|delta | 3d | +0.0070 | 16 | 1.011 | NO — logs only |
| EPS Surprise|level | 1d | +0.0024 | 19 | 0.962 | NO — logs only |
| EPS Surprise|level | 2d | +0.0027 | 18 | 0.962 | NO — logs only |
| EPS Surprise|level | 3d | +0.0041 | 17 | 0.965 | NO — logs only |
| n_catalysts|level | 1d | -0.0086 | 19 | 1.745 | yes |
| n_catalysts|level | 2d | -0.0185 | 18 | 1.710 | yes |
| n_catalysts|level | 3d | -0.0257 | 17 | 1.684 | yes |
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
| 2026-08-07 | 1d | -0.0339 | -0.0175 | +0.0164 |
| 2026-08-07 | 2d | -0.0242 | -0.0147 | +0.0094 |
| 2026-08-07 | 3d | -0.0009 | -0.0015 | -0.0005 |
| 2026-08-10 | 1d | -0.0491 | -0.0313 | +0.0178 |
| 2026-08-10 | 2d | -0.0596 | -0.0403 | +0.0194 |
| 2026-08-10 | 3d | -0.1054 | -0.0933 | +0.0121 |
| 2026-08-11 | 1d | +0.1007 | +0.1115 | +0.0108 |
| 2026-08-11 | 2d | +0.0174 | +0.0168 | -0.0005 |
| 2026-08-11 | 3d | +0.0639 | +0.0589 | -0.0050 |
| 2026-08-12 | 1d | -0.0472 | -0.0426 | +0.0047 |
| 2026-08-12 | 2d | +0.0520 | +0.0499 | -0.0021 |
| 2026-08-12 | 3d | +0.0878 | +0.0730 | -0.0148 |
| 2026-08-13 | 1d | -0.0908 | -0.0854 | +0.0054 |
| 2026-08-13 | 2d | -0.1428 | -0.1343 | +0.0085 |
| 2026-08-13 | 3d | -0.1672 | -0.1642 | +0.0030 |
| 2026-08-14 | 1d | +0.1577 | +0.1633 | +0.0056 |
| 2026-08-14 | 2d | -0.1560 | -0.1608 | -0.0049 |
| 2026-08-14 | 3d | -0.1404 | -0.1409 | -0.0005 |
| 2026-08-17 | 1d | -0.2097 | -0.2097 | +0.0000 |
| 2026-08-17 | 2d | -0.1365 | -0.1369 | -0.0003 |
| 2026-08-17 | 3d | -0.1034 | -0.1024 | +0.0010 |
| 2026-08-18 | 1d | +0.0486 | +0.0484 | -0.0002 |
| 2026-08-18 | 2d | +0.0270 | +0.0273 | +0.0003 |
| 2026-08-18 | 3d | +0.0058 | +0.0056 | -0.0002 |
| 2026-08-19 | 1d | +0.0108 | +0.0116 | +0.0008 |
| 2026-08-19 | 2d | +0.0519 | +0.0516 | -0.0003 |
| 2026-08-19 | 3d | +0.1772 | +0.1780 | +0.0008 |
| 2026-08-20 | 1d | -0.0007 | -0.0003 | +0.0004 |
| 2026-08-20 | 2d | +0.0530 | +0.0530 | +0.0000 |
| 2026-08-20 | 3d | +0.0387 | +0.0389 | +0.0002 |
| 2026-08-21 | 1d | -0.0802 | -0.0799 | +0.0003 |
| 2026-08-21 | 2d | +0.0158 | +0.0156 | -0.0003 |
| 2026-08-21 | 3d | -0.0723 | -0.0724 | -0.0001 |
| 2026-08-24 | 1d | +0.0056 | +0.0033 | -0.0024 |
| 2026-08-24 | 2d | -0.0285 | -0.0307 | -0.0022 |
| 2026-08-24 | 3d | -0.0880 | -0.0891 | -0.0011 |
| 2026-08-25 | 1d | -0.0503 | -0.0516 | -0.0013 |
| 2026-08-25 | 2d | -0.1093 | -0.1103 | -0.0010 |
| 2026-08-25 | 3d | -0.0661 | -0.0678 | -0.0018 |
| 2026-08-26 | 1d | -0.0710 | -0.0705 | +0.0006 |
| 2026-08-26 | 2d | -0.0146 | -0.0152 | -0.0007 |
| 2026-08-26 | 3d | -0.0019 | -0.0022 | -0.0003 |
| 2026-08-28 | 1d | -0.0442 | -0.0430 | +0.0012 |
| 2026-08-28 | 2d | +0.0258 | +0.0253 | -0.0005 |
| 2026-08-28 | 3d | +0.0108 | +0.0122 | +0.0014 |
| 2026-08-31 | 1d | -0.0065 | -0.0075 | -0.0010 |
| 2026-08-31 | 2d | +0.0398 | +0.0406 | +0.0008 |
| 2026-08-31 | 3d | +0.1004 | +0.1013 | +0.0010 |
| 2026-09-01 | 1d | -0.0847 | -0.0772 | +0.0075 |
| 2026-09-01 | 2d | -0.2394 | -0.2323 | +0.0071 |
| 2026-09-02 | 1d | -0.0842 | -0.0810 | +0.0032 |

_Champion reconstruction check: mean |rebuilt price category − stored price_score| = 0.1526 (should be ~0; large values mean the learner's model of the engine has drifted from score_engine — distrust this run)._

## Decision

PROMOTED — challenger mean IC gain +0.0036 on 1d, improved on 74% of 19 dates. New multipliers: Performance (Month)|delta ×1.179, Average Volume|delta ×0.643, Short Float|delta ×1.701, Institutional Transactions|level ×1.431, Institutional Ownership|delta ×1.849, Insider Transactions|level ×0.897, Target Price|delta ×1.182, Analyst Recom|delta ×1.633, Profit Margin|delta ×1.008, EPS Surprise|level ×0.962, n_catalysts|level ×1.745

_Note: curved-polarity rules (rvol/rsi/sma/short/upside/debt curves) are never auto-adjusted; change those in score_rubric.py by hand with git history as the audit trail._

# Weight learning — decision log

_Generated 2026-08-31 20:14 EDT_

- label dates per horizon: 1d: 16, 2d: 15, 3d: 14
- primary horizon for promotion test: **1d** (16 dates)
- existing overrides: {'Price|ret': 0.25, 'Performance (Month)|delta': 1.2918496363925176, 'Average Volume|delta': 0.6945355202645986, 'Relative Strength Index (14)|delta': 0.25, 'Short Float|delta': 1.6705856788346778, 'Institutional Transactions|level': 1.5182198525012738, 'Institutional Ownership|delta': 1.8376405526627302, 'Insider Transactions|level': 0.8600437489399057, 'Target Price|delta': 1.1376930862941643, 'Analyst Recom|delta': 1.5125919144568065, 'Sales Growth Quarter Over Quarter|level': 2.0, 'Sales Year Over Year TTM|level': 2.0, 'Profit Margin|delta': 0.9769486406237569, 'EPS Surprise|level': 0.9389154237934246, 'n_catalysts|level': 1.8751040522201676}

## Per-rule aligned IC (direction corrected for polarity)

| Rule | Horizon | Mean aligned IC | Dates | Proposed × | Testable |
|---|---|---|---|---|---|
| Price|ret | 1d | -0.0639 | 15 | 0.250 | yes |
| Price|ret | 2d | -0.0578 | 14 | 0.250 | yes |
| Price|ret | 3d | -0.0388 | 13 | 0.250 | yes |
| Performance (Month)|delta | 1d | -0.0055 | 15 | 1.278 | yes |
| Performance (Month)|delta | 2d | -0.0240 | 14 | 1.230 | yes |
| Performance (Month)|delta | 3d | -0.0394 | 13 | 1.190 | yes |
| Average Volume|delta | 1d | -0.0100 | 15 | 0.681 | NO — logs only |
| Average Volume|delta | 2d | -0.0147 | 14 | 0.674 | NO — logs only |
| Average Volume|delta | 3d | -0.0144 | 13 | 0.674 | NO — logs only |
| Relative Strength Index (14)|delta | 1d | -0.0521 | 15 | 0.250 | yes |
| Relative Strength Index (14)|delta | 2d | -0.0578 | 14 | 0.250 | yes |
| Relative Strength Index (14)|delta | 3d | -0.0312 | 13 | 0.250 | yes |
| Short Float|delta | 1d | +0.0028 | 14 | 1.680 | NO — logs only |
| Short Float|delta | 2d | -0.0055 | 13 | 1.652 | NO — logs only |
| Short Float|delta | 3d | -0.0113 | 12 | 1.633 | NO — logs only |
| Institutional Transactions|level | 1d | -0.0080 | 16 | 1.494 | NO — logs only |
| Institutional Transactions|level | 2d | -0.0087 | 15 | 1.492 | NO — logs only |
| Institutional Transactions|level | 3d | -0.0097 | 14 | 1.489 | NO — logs only |
| Institutional Ownership|delta | 1d | -0.0009 | 15 | 1.834 | NO — logs only |
| Institutional Ownership|delta | 2d | +0.0059 | 14 | 1.859 | NO — logs only |
| Institutional Ownership|delta | 3d | +0.0064 | 13 | 1.861 | NO — logs only |
| Insider Transactions|level | 1d | +0.0057 | 16 | 0.870 | NO — logs only |
| Insider Transactions|level | 2d | +0.0121 | 15 | 0.881 | NO — logs only |
| Insider Transactions|level | 3d | +0.0160 | 14 | 0.888 | NO — logs only |
| Target Price|delta | 1d | +0.0022 | 15 | 1.143 | NO — logs only |
| Target Price|delta | 2d | +0.0027 | 14 | 1.144 | NO — logs only |
| Target Price|delta | 3d | +0.0011 | 13 | 1.140 | NO — logs only |
| Analyst Recom|delta | 1d | +0.0083 | 15 | 1.538 | NO — logs only |
| Analyst Recom|delta | 2d | -0.0044 | 14 | 1.499 | NO — logs only |
| Analyst Recom|delta | 3d | -0.0062 | 13 | 1.494 | NO — logs only |
| Sales Growth Quarter Over Quarter|level | 1d | +0.0139 | 16 | 2.000 | NO — logs only |
| Sales Growth Quarter Over Quarter|level | 2d | +0.0135 | 15 | 2.000 | NO — logs only |
| Sales Growth Quarter Over Quarter|level | 3d | +0.0160 | 14 | 2.000 | NO — logs only |
| Sales Year Over Year TTM|level | 1d | +0.0134 | 16 | 2.000 | NO — logs only |
| Sales Year Over Year TTM|level | 2d | +0.0166 | 15 | 2.000 | NO — logs only |
| Sales Year Over Year TTM|level | 3d | +0.0187 | 14 | 2.000 | NO — logs only |
| Profit Margin|delta | 1d | +0.0020 | 15 | 0.981 | NO — logs only |
| Profit Margin|delta | 2d | -0.0010 | 14 | 0.975 | NO — logs only |
| Profit Margin|delta | 3d | +0.0067 | 13 | 0.990 | NO — logs only |
| EPS Surprise|level | 1d | +0.0025 | 16 | 0.944 | NO — logs only |
| EPS Surprise|level | 2d | +0.0038 | 15 | 0.946 | NO — logs only |
| EPS Surprise|level | 3d | +0.0016 | 14 | 0.942 | NO — logs only |
| n_catalysts|level | 1d | -0.0059 | 16 | 1.853 | yes |
| n_catalysts|level | 2d | -0.0139 | 15 | 1.823 | yes |
| n_catalysts|level | 3d | -0.0168 | 14 | 1.812 | yes |
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
| 2026-08-07 | 3d | -0.0009 | -0.0020 | -0.0010 |
| 2026-08-10 | 1d | -0.0491 | -0.0317 | +0.0174 |
| 2026-08-10 | 2d | -0.0596 | -0.0405 | +0.0191 |
| 2026-08-10 | 3d | -0.1054 | -0.0938 | +0.0116 |
| 2026-08-11 | 1d | +0.1007 | +0.1119 | +0.0112 |
| 2026-08-11 | 2d | +0.0174 | +0.0169 | -0.0004 |
| 2026-08-11 | 3d | +0.0639 | +0.0582 | -0.0057 |
| 2026-08-12 | 1d | -0.0472 | -0.0417 | +0.0055 |
| 2026-08-12 | 2d | +0.0520 | +0.0492 | -0.0028 |
| 2026-08-12 | 3d | +0.0878 | +0.0704 | -0.0174 |
| 2026-08-13 | 1d | -0.0908 | -0.0858 | +0.0050 |
| 2026-08-13 | 2d | -0.1428 | -0.1338 | +0.0090 |
| 2026-08-13 | 3d | -0.1672 | -0.1636 | +0.0035 |
| 2026-08-14 | 1d | +0.1577 | +0.1662 | +0.0085 |
| 2026-08-14 | 2d | -0.1560 | -0.1598 | -0.0038 |
| 2026-08-14 | 3d | -0.1404 | -0.1398 | +0.0006 |
| 2026-08-17 | 1d | -0.2097 | -0.2091 | +0.0006 |
| 2026-08-17 | 2d | -0.1365 | -0.1360 | +0.0005 |
| 2026-08-17 | 3d | -0.1034 | -0.1012 | +0.0022 |
| 2026-08-18 | 1d | +0.0486 | +0.0485 | -0.0001 |
| 2026-08-18 | 2d | +0.0270 | +0.0278 | +0.0008 |
| 2026-08-18 | 3d | +0.0058 | +0.0050 | -0.0008 |
| 2026-08-19 | 1d | +0.0108 | +0.0128 | +0.0020 |
| 2026-08-19 | 2d | +0.0519 | +0.0505 | -0.0014 |
| 2026-08-19 | 3d | +0.1772 | +0.1795 | +0.0023 |
| 2026-08-20 | 1d | -0.0007 | -0.0015 | -0.0008 |
| 2026-08-20 | 2d | +0.0530 | +0.0519 | -0.0010 |
| 2026-08-20 | 3d | +0.0387 | +0.0375 | -0.0012 |
| 2026-08-21 | 1d | -0.0802 | -0.0790 | +0.0012 |
| 2026-08-21 | 2d | +0.0158 | +0.0165 | +0.0007 |
| 2026-08-21 | 3d | -0.0723 | -0.0718 | +0.0005 |
| 2026-08-24 | 1d | +0.0056 | +0.0068 | +0.0012 |
| 2026-08-24 | 2d | -0.0285 | -0.0272 | +0.0013 |
| 2026-08-24 | 3d | -0.0880 | -0.0880 | +0.0000 |
| 2026-08-25 | 1d | -0.0503 | -0.0487 | +0.0016 |
| 2026-08-25 | 2d | -0.1093 | -0.1084 | +0.0010 |
| 2026-08-25 | 3d | -0.0661 | -0.0655 | +0.0005 |
| 2026-08-26 | 1d | -0.0710 | -0.0710 | +0.0000 |
| 2026-08-26 | 2d | -0.0146 | -0.0141 | +0.0005 |
| 2026-08-28 | 1d | -0.0442 | -0.0435 | +0.0008 |

_Champion reconstruction check: mean |rebuilt price category − stored price_score| = 0.1959 (should be ~0; large values mean the learner's model of the engine has drifted from score_engine — distrust this run)._

## Decision

PROMOTED — challenger mean IC gain +0.0044 on 1d, improved on 81% of 16 dates. New multipliers: Performance (Month)|delta ×1.278, Average Volume|delta ×0.681, Short Float|delta ×1.680, Institutional Transactions|level ×1.494, Institutional Ownership|delta ×1.834, Insider Transactions|level ×0.870, Target Price|delta ×1.143, Analyst Recom|delta ×1.538, Profit Margin|delta ×0.981, EPS Surprise|level ×0.944, n_catalysts|level ×1.853

_Note: curved-polarity rules (rvol/rsi/sma/short/upside/debt curves) are never auto-adjusted; change those in score_rubric.py by hand with git history as the audit trail._

# Weight learning — decision log

_Generated 2026-09-15 19:21 EDT_

- label dates per horizon: 1d: 26, 2d: 25, 3d: 24
- primary horizon for promotion test: **1d** (26 dates)
- existing overrides: {'Price|ret': 0.25, 'Performance (Month)|delta': 0.8844930530640328, 'Average Volume|delta': 0.5680936547136068, 'Relative Strength Index (14)|delta': 0.25, 'Short Float|delta': 1.7424530151692303, 'Institutional Transactions|level': 1.3206061848168316, 'Institutional Ownership|delta': 1.9240323675479842, 'Insider Transactions|level': 0.891284922916825, 'Target Price|delta': 1.2275582428252452, 'Analyst Recom|delta': 1.8924630220904755, 'Sales Growth Quarter Over Quarter|level': 2.0, 'Sales Year Over Year TTM|level': 2.0, 'Profit Margin|delta': 1.0921451756973148, 'EPS Surprise|level': 1.0447074061583053, 'n_catalysts|level': 1.5802352941336726}

## Per-rule aligned IC (direction corrected for polarity)

| Rule | Horizon | Mean aligned IC | Dates | Proposed × | Testable |
|---|---|---|---|---|---|
| Price|ret | 1d | -0.0546 | 24 | 0.250 | yes |
| Price|ret | 2d | -0.0477 | 23 | 0.250 | yes |
| Price|ret | 3d | -0.0292 | 22 | 0.250 | yes |
| Performance (Month)|delta | 1d | -0.0170 | 24 | 0.854 | yes |
| Performance (Month)|delta | 2d | -0.0303 | 23 | 0.831 | yes |
| Performance (Month)|delta | 3d | -0.0464 | 22 | 0.802 | yes |
| Average Volume|delta | 1d | -0.0062 | 24 | 0.561 | NO — logs only |
| Average Volume|delta | 2d | -0.0057 | 23 | 0.562 | NO — logs only |
| Average Volume|delta | 3d | -0.0076 | 22 | 0.559 | NO — logs only |
| Relative Strength Index (14)|delta | 1d | -0.0498 | 24 | 0.250 | yes |
| Relative Strength Index (14)|delta | 2d | -0.0499 | 23 | 0.250 | yes |
| Relative Strength Index (14)|delta | 3d | -0.0314 | 22 | 0.250 | yes |
| Short Float|delta | 1d | -0.0018 | 23 | 1.736 | NO — logs only |
| Short Float|delta | 2d | -0.0047 | 22 | 1.726 | NO — logs only |
| Short Float|delta | 3d | -0.0077 | 21 | 1.716 | NO — logs only |
| Institutional Transactions|level | 1d | -0.0083 | 26 | 1.299 | NO — logs only |
| Institutional Transactions|level | 2d | -0.0090 | 25 | 1.297 | NO — logs only |
| Institutional Transactions|level | 3d | -0.0101 | 24 | 1.294 | NO — logs only |
| Institutional Ownership|delta | 1d | +0.0030 | 24 | 1.936 | NO — logs only |
| Institutional Ownership|delta | 2d | +0.0060 | 23 | 1.947 | NO — logs only |
| Institutional Ownership|delta | 3d | +0.0014 | 22 | 1.929 | NO — logs only |
| Insider Transactions|level | 1d | -0.0045 | 26 | 0.883 | NO — logs only |
| Insider Transactions|level | 2d | -0.0002 | 25 | 0.891 | NO — logs only |
| Insider Transactions|level | 3d | +0.0016 | 24 | 0.894 | NO — logs only |
| Target Price|delta | 1d | +0.0049 | 24 | 1.240 | NO — logs only |
| Target Price|delta | 2d | +0.0047 | 23 | 1.239 | NO — logs only |
| Target Price|delta | 3d | +0.0041 | 22 | 1.238 | NO — logs only |
| Analyst Recom|delta | 1d | +0.0084 | 24 | 1.924 | NO — logs only |
| Analyst Recom|delta | 2d | -0.0017 | 23 | 1.886 | NO — logs only |
| Analyst Recom|delta | 3d | -0.0037 | 22 | 1.879 | NO — logs only |
| Sales Growth Quarter Over Quarter|level | 1d | +0.0155 | 26 | 2.000 | NO — logs only |
| Sales Growth Quarter Over Quarter|level | 2d | +0.0169 | 25 | 2.000 | NO — logs only |
| Sales Growth Quarter Over Quarter|level | 3d | +0.0228 | 24 | 2.000 | NO — logs only |
| Sales Year Over Year TTM|level | 1d | +0.0113 | 26 | 2.000 | NO — logs only |
| Sales Year Over Year TTM|level | 2d | +0.0145 | 25 | 2.000 | NO — logs only |
| Sales Year Over Year TTM|level | 3d | +0.0186 | 24 | 2.000 | NO — logs only |
| Profit Margin|delta | 1d | +0.0065 | 24 | 1.106 | NO — logs only |
| Profit Margin|delta | 2d | +0.0035 | 23 | 1.100 | NO — logs only |
| Profit Margin|delta | 3d | +0.0078 | 22 | 1.109 | NO — logs only |
| EPS Surprise|level | 1d | +0.0107 | 26 | 1.067 | NO — logs only |
| EPS Surprise|level | 2d | +0.0126 | 25 | 1.071 | NO — logs only |
| EPS Surprise|level | 3d | +0.0129 | 24 | 1.072 | NO — logs only |
| n_catalysts|level | 1d | -0.0116 | 26 | 1.543 | yes |
| n_catalysts|level | 2d | -0.0210 | 25 | 1.514 | yes |
| n_catalysts|level | 3d | -0.0235 | 24 | 1.506 | yes |
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
| 2026-08-07 | 1d | -0.0339 | -0.0240 | +0.0100 |
| 2026-08-07 | 2d | -0.0242 | -0.0176 | +0.0066 |
| 2026-08-07 | 3d | -0.0009 | +0.0019 | +0.0029 |
| 2026-08-10 | 1d | -0.0491 | -0.0303 | +0.0188 |
| 2026-08-10 | 2d | -0.0596 | -0.0370 | +0.0227 |
| 2026-08-10 | 3d | -0.1054 | -0.0912 | +0.0141 |
| 2026-08-11 | 1d | +0.1007 | +0.1051 | +0.0043 |
| 2026-08-11 | 2d | +0.0174 | +0.0120 | -0.0054 |
| 2026-08-11 | 3d | +0.0639 | +0.0590 | -0.0049 |
| 2026-08-12 | 1d | -0.0472 | -0.0467 | +0.0005 |
| 2026-08-12 | 2d | +0.0520 | +0.0521 | +0.0001 |
| 2026-08-12 | 3d | +0.0878 | +0.0805 | -0.0073 |
| 2026-08-13 | 1d | -0.0908 | -0.0862 | +0.0046 |
| 2026-08-13 | 2d | -0.1428 | -0.1378 | +0.0050 |
| 2026-08-13 | 3d | -0.1672 | -0.1646 | +0.0026 |
| 2026-08-14 | 1d | +0.1577 | +0.1453 | -0.0123 |
| 2026-08-14 | 2d | -0.1560 | -0.1593 | -0.0033 |
| 2026-08-14 | 3d | -0.1404 | -0.1426 | -0.0022 |
| 2026-08-17 | 1d | -0.2097 | -0.2062 | +0.0035 |
| 2026-08-17 | 2d | -0.1365 | -0.1354 | +0.0012 |
| 2026-08-17 | 3d | -0.1034 | -0.1042 | -0.0008 |
| 2026-08-18 | 1d | +0.0486 | +0.0461 | -0.0025 |
| 2026-08-18 | 2d | +0.0270 | +0.0231 | -0.0040 |
| 2026-08-18 | 3d | +0.0058 | +0.0075 | +0.0017 |
| 2026-08-19 | 1d | +0.0108 | +0.0033 | -0.0075 |
| 2026-08-19 | 2d | +0.0519 | +0.0545 | +0.0026 |
| 2026-08-19 | 3d | +0.1772 | +0.1687 | -0.0085 |
| 2026-08-20 | 1d | -0.0007 | +0.0058 | +0.0065 |
| 2026-08-20 | 2d | +0.0530 | +0.0566 | +0.0037 |
| 2026-08-20 | 3d | +0.0387 | +0.0460 | +0.0072 |
| 2026-08-21 | 1d | -0.0802 | -0.0804 | -0.0001 |
| 2026-08-21 | 2d | +0.0158 | +0.0141 | -0.0017 |
| 2026-08-21 | 3d | -0.0723 | -0.0726 | -0.0003 |
| 2026-08-24 | 1d | +0.0056 | -0.0141 | -0.0197 |
| 2026-08-24 | 2d | -0.0285 | -0.0501 | -0.0217 |
| 2026-08-24 | 3d | -0.0880 | -0.0876 | +0.0005 |
| 2026-08-25 | 1d | -0.0503 | -0.0696 | -0.0193 |
| 2026-08-25 | 2d | -0.1093 | -0.1164 | -0.0071 |
| 2026-08-25 | 3d | -0.0661 | -0.0775 | -0.0114 |
| 2026-08-26 | 1d | -0.0710 | -0.0577 | +0.0133 |
| 2026-08-26 | 2d | -0.0146 | -0.0124 | +0.0021 |
| 2026-08-26 | 3d | -0.0019 | +0.0061 | +0.0080 |
| 2026-08-28 | 1d | -0.0442 | -0.0339 | +0.0104 |
| 2026-08-28 | 2d | +0.0258 | +0.0239 | -0.0019 |
| 2026-08-28 | 3d | +0.0108 | +0.0213 | +0.0105 |
| 2026-08-31 | 1d | -0.0065 | -0.0075 | -0.0010 |
| 2026-08-31 | 2d | +0.0398 | +0.0423 | +0.0025 |
| 2026-08-31 | 3d | +0.1004 | +0.1054 | +0.0050 |
| 2026-09-01 | 1d | -0.0847 | -0.0518 | +0.0329 |
| 2026-09-01 | 2d | -0.2394 | -0.1941 | +0.0453 |
| 2026-09-01 | 3d | -0.2756 | -0.2358 | +0.0398 |
| 2026-09-02 | 1d | -0.0842 | -0.0564 | +0.0278 |
| 2026-09-02 | 2d | -0.1304 | -0.0975 | +0.0329 |
| 2026-09-02 | 3d | -0.1700 | -0.1492 | +0.0208 |
| 2026-09-03 | 1d | -0.0656 | -0.0861 | -0.0204 |
| 2026-09-03 | 2d | -0.0607 | -0.0887 | -0.0279 |
| 2026-09-03 | 3d | -0.1049 | -0.1256 | -0.0207 |
| 2026-09-04 | 1d | -0.0292 | -0.0350 | -0.0058 |
| 2026-09-04 | 2d | -0.0659 | -0.0715 | -0.0056 |
| 2026-09-04 | 3d | -0.1272 | -0.1314 | -0.0041 |
| 2026-09-08 | 1d | -0.0849 | -0.0849 | +0.0000 |
| 2026-09-08 | 2d | -0.1276 | -0.1276 | +0.0000 |
| 2026-09-08 | 3d | -0.0619 | -0.0619 | +0.0000 |
| 2026-09-09 | 1d | -0.0163 | -0.0218 | -0.0055 |
| 2026-09-09 | 2d | +0.0188 | +0.0139 | -0.0049 |
| 2026-09-09 | 3d | -0.0591 | -0.0601 | -0.0009 |
| 2026-09-10 | 1d | -0.0932 | -0.0889 | +0.0043 |
| 2026-09-10 | 2d | +0.1308 | +0.1193 | -0.0115 |
| 2026-09-10 | 3d | +0.1827 | +0.1704 | -0.0123 |
| 2026-09-11 | 1d | -0.0419 | -0.0495 | -0.0076 |
| 2026-09-11 | 2d | -0.0676 | -0.0749 | -0.0073 |
| 2026-09-14 | 1d | -0.0250 | -0.0258 | -0.0009 |

_Champion reconstruction check: mean |rebuilt price category − stored price_score| = 0.2351 (should be ~0; large values mean the learner's model of the engine has drifted from score_engine — distrust this run)._

## Decision

PROMOTED — challenger mean IC gain +0.0013 on 1d, improved on 50% of 26 dates. New multipliers: Performance (Month)|delta ×0.854, Average Volume|delta ×0.561, Short Float|delta ×1.736, Institutional Transactions|level ×1.299, Institutional Ownership|delta ×1.936, Insider Transactions|level ×0.883, Target Price|delta ×1.240, Analyst Recom|delta ×1.924, Profit Margin|delta ×1.106, EPS Surprise|level ×1.067, n_catalysts|level ×1.543

_Note: curved-polarity rules (rvol/rsi/sma/short/upside/debt curves) are never auto-adjusted; change those in score_rubric.py by hand with git history as the audit trail._

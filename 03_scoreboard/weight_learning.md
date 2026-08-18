# Weight learning — decision log

_Generated 2026-08-18 17:16 EDT_

- label dates per horizon: 1d: 8, 2d: 7, 3d: 6
- primary horizon for promotion test: **1d** (8 dates)
- existing overrides: {'Price|ret': 0.25, 'Performance (Month)|delta': 1.1664057667578247, 'Average Volume|delta': 0.7756955604235289, 'Relative Strength Index (14)|delta': 0.3009009425394926, 'Short Float|delta': 1.5582750368454732, 'Institutional Transactions|level': 1.4829172329230038, 'Institutional Ownership|delta': 1.6392451740553646, 'Insider Transactions|level': 0.8302811912203507, 'Target Price|delta': 1.0296903720657669, 'Analyst Recom|delta': 1.340836253597462, 'Sales Growth Quarter Over Quarter|level': 2.0, 'Sales Year Over Year TTM|level': 2.0, 'Profit Margin|delta': 0.8956825817303707, 'EPS Surprise|level': 0.944919457654456, 'n_catalysts|level': 1.8910561887342285}

## Per-rule aligned IC (direction corrected for polarity)

| Rule | Horizon | Mean aligned IC | Dates | Proposed × | Testable |
|---|---|---|---|---|---|
| Price|ret | 1d | -0.0776 | 7 | 0.250 | yes |
| Price|ret | 2d | -0.0885 | 6 | 0.250 | yes |
| Price|ret | 3d | -0.0484 | 5 | 0.250 | yes |
| Performance (Month)|delta | 1d | -0.0034 | 7 | 1.158 | yes |
| Performance (Month)|delta | 2d | -0.0522 | 6 | 1.045 | yes |
| Performance (Month)|delta | 3d | -0.0636 | 5 | 1.018 | yes |
| Average Volume|delta | 1d | -0.0031 | 7 | 0.771 | NO — logs only |
| Average Volume|delta | 2d | -0.0056 | 6 | 0.767 | NO — logs only |
| Average Volume|delta | 3d | -0.0079 | 5 | 0.763 | NO — logs only |
| Relative Strength Index (14)|delta | 1d | -0.0788 | 7 | 0.253 | yes |
| Relative Strength Index (14)|delta | 2d | -0.0851 | 6 | 0.250 | yes |
| Relative Strength Index (14)|delta | 3d | -0.0315 | 5 | 0.282 | yes |
| Short Float|delta | 1d | +0.0119 | 6 | 1.595 | NO — logs only |
| Short Float|delta | 2d | -0.0043 | 5 | 1.545 | NO — logs only |
| Short Float|delta | 3d | -0.0170 | 4 | 1.505 | NO — logs only |
| Institutional Transactions|level | 1d | +0.0168 | 8 | 1.533 | NO — logs only |
| Institutional Transactions|level | 2d | +0.0325 | 7 | 1.579 | NO — logs only |
| Institutional Transactions|level | 3d | +0.0415 | 6 | 1.606 | NO — logs only |
| Institutional Ownership|delta | 1d | +0.0147 | 7 | 1.688 | NO — logs only |
| Institutional Ownership|delta | 2d | +0.0173 | 6 | 1.696 | NO — logs only |
| Institutional Ownership|delta | 3d | +0.0209 | 5 | 1.708 | NO — logs only |
| Insider Transactions|level | 1d | -0.0126 | 8 | 0.809 | NO — logs only |
| Insider Transactions|level | 2d | -0.0197 | 7 | 0.798 | NO — logs only |
| Insider Transactions|level | 3d | -0.0298 | 6 | 0.781 | NO — logs only |
| Target Price|delta | 1d | +0.0082 | 7 | 1.047 | NO — logs only |
| Target Price|delta | 2d | +0.0068 | 6 | 1.044 | NO — logs only |
| Target Price|delta | 3d | +0.0160 | 5 | 1.063 | NO — logs only |
| Analyst Recom|delta | 1d | +0.0103 | 7 | 1.368 | NO — logs only |
| Analyst Recom|delta | 2d | +0.0015 | 6 | 1.345 | NO — logs only |
| Analyst Recom|delta | 3d | +0.0067 | 5 | 1.359 | NO — logs only |
| Sales Growth Quarter Over Quarter|level | 1d | +0.0366 | 8 | 2.000 | NO — logs only |
| Sales Growth Quarter Over Quarter|level | 2d | +0.0537 | 7 | 2.000 | NO — logs only |
| Sales Growth Quarter Over Quarter|level | 3d | +0.0713 | 6 | 2.000 | NO — logs only |
| Sales Year Over Year TTM|level | 1d | +0.0315 | 8 | 2.000 | NO — logs only |
| Sales Year Over Year TTM|level | 2d | +0.0507 | 7 | 2.000 | NO — logs only |
| Sales Year Over Year TTM|level | 3d | +0.0681 | 6 | 2.000 | NO — logs only |
| Profit Margin|delta | 1d | +0.0073 | 7 | 0.909 | NO — logs only |
| Profit Margin|delta | 2d | +0.0014 | 6 | 0.898 | NO — logs only |
| Profit Margin|delta | 3d | +0.0041 | 5 | 0.903 | NO — logs only |
| EPS Surprise|level | 1d | +0.0081 | 8 | 0.960 | NO — logs only |
| EPS Surprise|level | 2d | +0.0115 | 7 | 0.967 | NO — logs only |
| EPS Surprise|level | 3d | +0.0172 | 6 | 0.977 | NO — logs only |
| n_catalysts|level | 1d | +0.0068 | 8 | 1.917 | yes |
| n_catalysts|level | 2d | +0.0090 | 7 | 1.925 | yes |
| n_catalysts|level | 3d | +0.0202 | 6 | 1.968 | yes |
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
| 2026-08-07 | 1d | -0.0339 | -0.0176 | +0.0164 |
| 2026-08-07 | 2d | -0.0242 | -0.0131 | +0.0111 |
| 2026-08-07 | 3d | -0.0009 | +0.0010 | +0.0019 |
| 2026-08-10 | 1d | -0.0491 | -0.0280 | +0.0211 |
| 2026-08-10 | 2d | -0.0596 | -0.0356 | +0.0240 |
| 2026-08-10 | 3d | -0.1054 | -0.0901 | +0.0153 |
| 2026-08-11 | 1d | +0.1007 | +0.1113 | +0.0106 |
| 2026-08-11 | 2d | +0.0174 | +0.0158 | -0.0015 |
| 2026-08-11 | 3d | +0.0639 | +0.0588 | -0.0051 |
| 2026-08-12 | 1d | -0.0472 | -0.0438 | +0.0034 |
| 2026-08-12 | 2d | +0.0520 | +0.0514 | -0.0006 |
| 2026-08-12 | 3d | +0.0878 | +0.0705 | -0.0172 |
| 2026-08-13 | 1d | -0.0908 | -0.0774 | +0.0134 |
| 2026-08-13 | 2d | -0.1428 | -0.1280 | +0.0148 |
| 2026-08-13 | 3d | -0.1672 | -0.1621 | +0.0051 |
| 2026-08-14 | 1d | +0.1577 | +0.1614 | +0.0037 |
| 2026-08-14 | 2d | -0.1560 | -0.1600 | -0.0041 |
| 2026-08-17 | 1d | -0.2097 | -0.2096 | +0.0001 |

_Champion reconstruction check: mean |rebuilt price category − stored price_score| = 0.2993 (should be ~0; large values mean the learner's model of the engine has drifted from score_engine — distrust this run)._

## Decision

PROMOTED — challenger mean IC gain +0.0086 on 1d, improved on 100% of 8 dates. New multipliers: Performance (Month)|delta ×1.158, Average Volume|delta ×0.771, Relative Strength Index (14)|delta ×0.253, Short Float|delta ×1.595, Institutional Transactions|level ×1.533, Institutional Ownership|delta ×1.688, Insider Transactions|level ×0.809, Target Price|delta ×1.047, Analyst Recom|delta ×1.368, Profit Margin|delta ×0.909, EPS Surprise|level ×0.960, n_catalysts|level ×1.917

_Note: curved-polarity rules (rvol/rsi/sma/short/upside/debt curves) are never auto-adjusted; change those in score_rubric.py by hand with git history as the audit trail._

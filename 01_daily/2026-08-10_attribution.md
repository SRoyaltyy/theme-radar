# Factor attribution — 2026-08-10

**What this report measures, exactly:** features computed from the **2026-08-10** Finviz snapshot (deltas vs the **2026-08-07** snapshot), graded against `fwd_1d` = the return from **2026-08-10** to **2026-08-11** (n=11533 stocks with valid labels).
Provisional until multiple scan dates agree.

_Column guide: **IC** = Spearman rank correlation between the feature and the forward return (whole universe); **IC↑** = IC computed only among stocks that went UP; **IC↓** = IC only among stocks that went DOWN. A high IC↑ means the feature ranks winners among winners._

## Score calibration
- Spearman IC(total_score, fwd_1d) = **-0.0491**

| Quintile | Mean fwd | Hit up>1.5% | n |
|---|---|---|---|
| 1 | 0.50% | 31.1% | 2360 |
| 2 | 0.11% | 8.3% | 2843 |
| 3 | 0.03% | 6.1% | 2310 |
| 4 | 0.18% | 9.0% | 1801 |
| 5 | 1.01% | 25.3% | 2219 |

## Top |IC| features (full universe)

| Feature | IC | IC↑ | IC↓ | Mean fwd when + | Mean fwd when − | n+/n− |
|---|---|---|---|---|---|---|
| d_Performance (YTD) | -0.1047 | -0.1336 | +0.0208 | 0.48% | 0.28% | 4316/6793 |
| d_Price | -0.1018 | -0.0265 | -0.0243 | 0.51% | 0.27% | 4198/6681 |
| true_ret | -0.1000 | -0.1427 | +0.0286 | 0.51% | 0.27% | 4198/6681 |
| d_200-Day Simple Moving Average | -0.0964 | -0.1113 | -0.0012 | 0.51% | 0.27% | 4289/7067 |
| Relative Strength Index (14) | -0.0938 | -0.1405 | +0.3270 | 0.37% | n/a | 11434/0 |
| d_50-Day Simple Moving Average | -0.0883 | -0.1070 | -0.0032 | 0.52% | 0.27% | 4315/7071 |
| d_20-Day Simple Moving Average | -0.0882 | -0.1309 | +0.0101 | 0.54% | 0.27% | 3983/7418 |
| d_Performance (Week) | -0.0813 | -0.2858 | +0.1541 | 0.75% | 0.23% | 2936/8417 |
| d_Relative Strength Index (14) | -0.0719 | +0.1187 | -0.0278 | 0.48% | 0.28% | 4316/6779 |
| Performance (Month) | -0.0702 | -0.1210 | +0.0875 | 0.10% | 0.69% | 6338/4971 |
| upside_pct_lvl | +0.0593 | +0.3580 | -0.2748 | 0.39% | -0.30% | 4274/369 |
| Short Float | +0.0568 | +0.2039 | -0.1247 | 0.63% | n/a | 5686/0 |
| d_Institutional Ownership | +0.0562 | -0.0363 | +0.0578 | 0.65% | 0.19% | 3404/1512 |
| d_Volatility (Month) | +0.0440 | +0.1245 | -0.0614 | 0.54% | 0.34% | 4595/4618 |
| Institutional Transactions | +0.0414 | +0.0946 | -0.0510 | 0.74% | 0.69% | 2521/2519 |
| d_Forward P/E | -0.0368 | -0.0359 | -0.0280 | -0.01% | 0.16% | 1097/1885 |
| d_Performance (Month) | -0.0361 | -0.0498 | -0.0074 | 0.36% | 0.37% | 4089/7117 |
| d_Market Cap | -0.0340 | +0.0334 | -0.0554 | 1.04% | 0.31% | 2379/3333 |
| d_Profit Margin | -0.0302 | +0.0090 | -0.0461 | -0.07% | 0.54% | 196/203 |
| d_Target Price | -0.0274 | -0.0518 | +0.0702 | 0.06% | 0.28% | 544/279 |
| d_Performance (Quarter) | -0.0243 | -0.0284 | -0.0104 | 0.68% | 0.17% | 3689/7111 |
| d_Short Float | -0.0235 | -0.0694 | +0.0525 | 0.41% | 0.53% | 406/610 |
| d_Beta | +0.0234 | +0.0866 | +0.0076 | 0.42% | 1.16% | 2276/1692 |
| d_Insider Transactions | +0.0200 | +0.0285 | -0.0418 | 0.56% | 0.59% | 393/386 |
| d_Average Volume | -0.0199 | -0.0409 | +0.0191 | 0.64% | 0.20% | 4318/6677 |

## Combinations

| Pattern | n | Mean fwd | Hit up |
|---|---|---|---|
| true_ret>3% & DOWNTREND | 304 | 4.35% | 38.2% |
| true_ret>3% & UPTREND | 446 | 0.19% | 29.6% |
| true_ret>3% & MIXED | 216 | -0.45% | 27.8% |
| MonthΔ+ & Month<0 | 778 | 0.32% | 32.4% |
| MonthΔ+ & Month>0 | 1387 | 0.14% | 22.9% |

## Risk dominance probes

| State | n | Mean fwd | Mean fwd if score top quintile |
|---|---|---|---|
| Week>40% | 106 | -0.53% | 0.70% |
| Week>25% | 276 | 0.09% | 0.28% |
| RSI>75 | 251 | -0.10% | n/a |

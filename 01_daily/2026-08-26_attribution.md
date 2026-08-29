# Factor attribution — signal 2026-08-26 → prediction day 2026-08-28

## Trade window (read this first)

| Role | Date | Meaning |
|------|------|---------|
| **Signal as-of** | **2026-08-26** | Features/scores formed from this snapshot (and deltas vs **2026-08-25**). Only data on/before this date. |
| **Prediction day** | **2026-08-28** | The trading day the forward return is for (exit snapshot). |
| **Entry price** | Price @ 2026-08-26 | Long: buy here; short: sell here. |
| **Exit price** | Price @ 2026-08-28 | Close proxy on prediction day. |
| **Return column** | `fwd_1d` | Long: exit/entry − 1; short = opposite. |

Graded **n=11620** names with valid entry and exit prices.

Provisional until multiple signal dates agree.

_Column guide: **IC** = Spearman(feature, long forward return); **IC↑** / **IC↓** = IC among names that went up / down._

## Score calibration (long fwd)
- Spearman IC(total_score, fwd_1d) = **-0.0710**

| Quintile | Mean long fwd | Hit up>1.5% | n |
|---|---|---|---|
| 1 | -0.37% | 18.5% | 2448 |
| 2 | 0.87% | 10.7% | 2612 |
| 3 | -0.27% | 5.8% | 1960 |
| 4 | -0.59% | 6.8% | 2280 |
| 5 | -0.52% | 15.0% | 2320 |

## Top |IC| features

| Feature | IC | IC↑ | IC↓ | Mean fwd when + | Mean fwd when − | n+/n− |
|---|---|---|---|---|---|---|
| upside_pct_lvl | -0.1923 | +0.2424 | -0.4265 | 0.25% | -0.22% | 4310/338 |
| Short Float | -0.1643 | +0.2462 | -0.2063 | 0.24% | n/a | 5702/0 |
| d_Performance (Month) | -0.0976 | -0.0675 | -0.1376 | -0.04% | -0.21% | 4548/6744 |
| d_Forward P/E | -0.0914 | -0.0718 | -0.0240 | -0.73% | -0.27% | 1390/1552 |
| d_Beta | -0.0723 | +0.0313 | -0.1086 | -1.04% | 1.46% | 1792/1137 |
| Relative Strength Index (14) | +0.0708 | -0.2602 | +0.1604 | -0.14% | n/a | 11496/0 |
| Institutional Transactions | -0.0611 | +0.0637 | -0.1101 | 0.74% | -0.41% | 3177/1880 |
| Relative Volume | -0.0568 | +0.0909 | -0.0467 | -0.15% | n/a | 11333/0 |
| Performance (Week) | -0.0414 | -0.1629 | +0.0538 | -0.10% | -0.18% | 5475/5884 |
| d_Average Volume | +0.0409 | -0.2075 | +0.1552 | 0.13% | -0.22% | 2540/8707 |
| d_Market Cap | -0.0392 | -0.0583 | +0.0319 | 0.97% | -0.41% | 2504/3189 |
| d_Relative Volume | +0.0299 | +0.0146 | +0.0092 | 0.04% | -0.29% | 5015/6087 |
| d_Sales Year Over Year TTM | -0.0290 | -0.0096 | -0.0004 | -2.23% | -1.13% | 23/16 |
| d_Institutional Ownership | -0.0257 | -0.0394 | -0.0324 | -1.09% | -0.78% | 1243/915 |
| d_Performance (Week) | +0.0252 | -0.1394 | +0.0647 | 0.09% | -0.28% | 4078/7285 |
| d_EPS Surprise | +0.0231 | +0.0190 | +0.0045 | 1.05% | -0.69% | 38/27 |
| d_Short Ratio | -0.0207 | +0.0086 | -0.0088 | -0.65% | 0.42% | 5433/5574 |
| Performance (Month) | +0.0194 | +0.1694 | -0.1026 | 0.09% | -0.61% | 7586/3765 |
| d_Profit Margin | +0.0153 | -0.0062 | +0.0021 | -1.04% | -2.40% | 20/19 |
| d_50-Day Simple Moving Average | -0.0153 | -0.1181 | +0.0340 | 0.25% | -0.43% | 4714/6676 |
| d_Short Float | -0.0144 | -0.0300 | -0.0214 | -0.76% | 1.16% | 2558/2935 |
| d_Sales Growth Quarter Over Quarter | +0.0131 | -0.0184 | +0.0160 | -0.83% | -1.31% | 16/19 |
| d_Performance (Quarter) | +0.0126 | -0.0177 | +0.0286 | 0.39% | -0.49% | 5139/5663 |
| d_Analyst Recom | +0.0125 | +0.0236 | +0.0226 | -0.24% | -0.67% | 74/72 |
| d_Price | +0.0116 | -0.1024 | +0.0156 | -0.27% | -0.51% | 4643/6216 |

## Combinations

| Pattern | n | Mean long fwd | Hit up |
|---|---|---|---|
| true_ret>3% & DOWNTREND | 231 | 3.73% | 24.7% |
| true_ret>3% & UPTREND | 164 | -2.50% | 23.2% |
| true_ret>3% & MIXED | 136 | -1.57% | 21.3% |

## Risk dominance probes

| State | n | Mean long fwd | Mean fwd if score top quintile |
|---|---|---|---|
| EXTENDED | 400 | -2.29% | -7.16% |
| WASHED | 427 | 1.49% | 13.45% |

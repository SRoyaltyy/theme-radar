# Factor attribution — signal 2026-10-30 → prediction day 2026-11-02

## Trade window (read this first)

| Role | Date | Meaning |
|------|------|---------|
| **Signal as-of** | **2026-10-30** | Features/scores formed from this snapshot (and deltas vs **2026-10-29**). Only data on/before this date. |
| **Prediction day** | **2026-11-02** | The trading day the forward return is for (exit snapshot). |
| **Entry price** | Price @ 2026-10-30 | Long: buy here; short: sell here. |
| **Exit price** | Price @ 2026-11-02 | Close proxy on prediction day. |
| **Return column** | `fwd_1d` | Long: exit/entry − 1; short = opposite. |

Graded **n=11731** names with valid entry and exit prices.

Provisional until multiple signal dates agree.

_Column guide: **IC** = Spearman(feature, long forward return); **IC↑** / **IC↓** = IC among names that went up / down._

## Score calibration (long fwd)
- Spearman IC(total_score, fwd_1d) = **0.2337**

| Quintile | Mean long fwd | Hit up>1.5% | n |
|---|---|---|---|
| 1 | -1.83% | 12.9% | 2635 |
| 2 | 1.35% | 18.4% | 2146 |
| 3 | 0.07% | 23.3% | 2264 |
| 4 | 0.05% | 15.3% | 2403 |
| 5 | 0.39% | 32.3% | 2283 |

## Top |IC| features

| Feature | IC | IC↑ | IC↓ | Mean fwd when + | Mean fwd when − | n+/n− |
|---|---|---|---|---|---|---|
| d_Performance (Week) | +0.3511 | +0.0930 | +0.4590 | 0.71% | -0.47% | 3976/7564 |
| Performance (Month) | +0.2787 | -0.0015 | +0.3965 | 0.28% | -0.35% | 5345/6213 |
| d_50-Day Simple Moving Average | +0.2733 | -0.0034 | +0.3885 | 0.42% | -0.25% | 3255/8380 |
| true_ret | +0.2706 | -0.0421 | +0.4338 | 0.41% | -0.23% | 2928/8403 |
| d_200-Day Simple Moving Average | +0.2660 | +0.0082 | +0.3552 | 0.48% | -0.25% | 3088/8533 |
| d_Performance (YTD) | +0.2555 | +0.0133 | +0.3316 | 0.45% | -0.79% | 2966/8453 |
| d_Forward P/E | +0.2527 | +0.1520 | +0.1890 | 1.27% | 0.14% | 932/2029 |
| d_20-Day Simple Moving Average | +0.2406 | -0.0457 | +0.3918 | 0.30% | -0.18% | 2824/8800 |
| upside_pct_lvl | -0.2346 | +0.1820 | -0.3282 | -0.31% | -0.30% | 4324/307 |
| d_Performance (Month) | +0.2076 | -0.0428 | +0.3250 | 0.38% | -0.24% | 3441/8036 |
| Relative Strength Index (14) | +0.2003 | -0.0592 | +0.2608 | -0.06% | n/a | 11650/0 |
| d_Price | +0.1899 | +0.0841 | +0.1654 | 0.41% | -0.23% | 2928/8403 |
| d_Performance (Quarter) | +0.1759 | -0.1544 | +0.3538 | -0.00% | -0.03% | 2602/8581 |
| d_Relative Strength Index (14) | +0.1629 | +0.1623 | -0.1015 | 0.43% | -0.24% | 2969/8447 |
| d_Beta | -0.1583 | +0.0428 | -0.2431 | 1.06% | -0.02% | 1820/1191 |
| d_Market Cap | +0.1134 | +0.0722 | +0.0936 | 0.60% | 0.57% | 1617/4119 |
| Institutional Transactions | -0.1113 | -0.0139 | -0.1268 | 0.87% | 0.07% | 3231/1814 |
| Performance (Week) | +0.0887 | +0.0091 | +0.0902 | -0.32% | 0.21% | 5950/5620 |
| Short Float | -0.0560 | +0.2408 | -0.2821 | 0.62% | n/a | 5648/0 |
| d_Relative Volume | -0.0493 | -0.0348 | -0.0171 | 0.10% | -0.28% | 6741/4576 |
| d_Short Float | +0.0451 | +0.0046 | +0.0510 | 1.92% | -1.38% | 39/38 |
| d_Target Price | -0.0262 | -0.0487 | +0.0445 | 0.26% | 1.20% | 336/295 |
| d_Analyst Recom | -0.0216 | +0.0116 | +0.0295 | 0.46% | 1.14% | 63/58 |
| d_Profit Margin | -0.0155 | -0.0055 | +0.0049 | 0.70% | 1.09% | 167/125 |
| Relative Volume | +0.0137 | +0.1022 | -0.0801 | -0.06% | n/a | 11471/0 |

## Combinations

| Pattern | n | Mean long fwd | Hit up |
|---|---|---|---|
| true_ret>3% & DOWNTREND | 166 | 1.12% | 44.6% |
| true_ret>3% & UPTREND | 147 | -0.03% | 40.1% |
| true_ret>3% & MIXED | 146 | 2.77% | 51.4% |

## Risk dominance probes

| State | n | Mean long fwd | Mean fwd if score top quintile |
|---|---|---|---|
| EXTENDED | 219 | 0.75% | 4.09% |
| WASHED | 1669 | 0.34% | -1.04% |

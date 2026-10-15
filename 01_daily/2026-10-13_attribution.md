# Factor attribution — signal 2026-10-13 → prediction day 2026-10-15

## Trade window (read this first)

| Role | Date | Meaning |
|------|------|---------|
| **Signal as-of** | **2026-10-13** | Features/scores formed from this snapshot (and deltas vs **2026-10-12**). Only data on/before this date. |
| **Prediction day** | **2026-10-15** | The trading day the forward return is for (exit snapshot). |
| **Entry price** | Price @ 2026-10-13 | Long: buy here; short: sell here. |
| **Exit price** | Price @ 2026-10-15 | Close proxy on prediction day. |
| **Return column** | `fwd_2d` | Long: exit/entry − 1; short = opposite. |

Graded **n=11714** names with valid entry and exit prices.

Provisional until multiple signal dates agree.

_Column guide: **IC** = Spearman(feature, long forward return); **IC↑** / **IC↓** = IC among names that went up / down._

## Score calibration (long fwd)
- Spearman IC(total_score, fwd_2d) = **-0.0959**

| Quintile | Mean long fwd | Hit up>1.5% | n |
|---|---|---|---|
| 1 | -0.52% | 24.8% | 2347 |
| 2 | -0.33% | 16.4% | 2593 |
| 3 | -0.63% | 14.6% | 2255 |
| 4 | -0.72% | 15.6% | 2222 |
| 5 | -1.22% | 19.9% | 2297 |

## Top |IC| features

| Feature | IC | IC↑ | IC↓ | Mean fwd when + | Mean fwd when − | n+/n− |
|---|---|---|---|---|---|---|
| Performance (Week) | +0.3634 | +0.0423 | +0.4703 | 0.29% | -1.37% | 4766/6752 |
| d_Performance (Month) | -0.2569 | -0.2939 | -0.1656 | -1.23% | 0.14% | 6781/4631 |
| upside_pct_lvl | -0.1923 | +0.2276 | -0.3274 | 0.20% | -0.53% | 4355/280 |
| d_20-Day Simple Moving Average | +0.1739 | -0.0356 | +0.2424 | 0.01% | -1.29% | 5416/6156 |
| d_50-Day Simple Moving Average | +0.1593 | -0.0473 | +0.2342 | -0.04% | -1.25% | 5438/6098 |
| d_200-Day Simple Moving Average | +0.1426 | -0.0592 | +0.2218 | -0.06% | -1.18% | 5203/6309 |
| d_Price | +0.1376 | -0.0781 | +0.2044 | -0.05% | -1.22% | 5046/5892 |
| true_ret | +0.1362 | -0.0866 | +0.2504 | -0.05% | -1.22% | 5046/5892 |
| d_Performance (YTD) | +0.1347 | -0.0852 | +0.2343 | -0.06% | -1.20% | 5190/6004 |
| d_Performance (Week) | +0.1344 | -0.0139 | +0.1595 | -0.19% | -0.97% | 4269/7230 |
| d_Relative Strength Index (14) | +0.1245 | -0.1343 | +0.1560 | -0.06% | -1.22% | 5201/6013 |
| d_Beta | +0.1185 | -0.0858 | +0.1834 | -1.30% | -1.13% | 578/990 |
| Performance (Month) | -0.1176 | -0.2645 | +0.0949 | -1.66% | -0.11% | 4139/7389 |
| Institutional Transactions | -0.1069 | -0.0022 | -0.1047 | -0.75% | 0.95% | 3265/1778 |
| d_Performance (Quarter) | -0.0890 | -0.1533 | -0.0466 | -1.60% | 0.00% | 4442/6711 |
| d_Target Price | -0.0847 | -0.0295 | -0.0706 | -0.52% | 0.94% | 191/376 |
| Short Float | +0.0601 | +0.2403 | -0.2370 | -0.27% | n/a | 5673/0 |
| d_Forward P/E | +0.0569 | +0.0541 | +0.1093 | 0.04% | -0.35% | 1463/1473 |
| Relative Volume | +0.0548 | +0.0454 | -0.1048 | -0.69% | n/a | 11426/0 |
| d_Volatility (Month) | -0.0548 | -0.0074 | -0.0771 | -0.65% | -0.84% | 4056/5089 |
| d_Relative Volume | +0.0376 | -0.0217 | -0.0074 | -0.63% | -0.75% | 6637/4625 |
| d_Total Debt/Equity | -0.0291 | +0.0045 | -0.0392 | -14.30% | 6.99% | 4/2 |
| d_Analyst Recom | +0.0267 | +0.0305 | -0.0151 | 0.39% | -0.78% | 67/68 |
| d_Gross Margin | -0.0237 | -0.0326 | -0.0373 | -23.68% | 12.74% | 2/1 |
| d_Short Float | -0.0225 | -0.0203 | -0.0325 | -4.97% | -1.72% | 37/25 |

## Combinations

| Pattern | n | Mean long fwd | Hit up |
|---|---|---|---|
| true_ret>3% & DOWNTREND | 233 | 6.85% | 29.6% |
| true_ret>3% & UPTREND | 162 | -2.43% | 30.9% |
| true_ret>3% & MIXED | 96 | -2.43% | 33.3% |

## Risk dominance probes

| State | n | Mean long fwd | Mean fwd if score top quintile |
|---|---|---|---|
| EXTENDED | 157 | -1.47% | -4.08% |
| WASHED | 1275 | 1.07% | 5.54% |

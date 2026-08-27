# Factor attribution — signal 2026-08-24 → prediction day 2026-08-26

## Trade window (read this first)

| Role | Date | Meaning |
|------|------|---------|
| **Signal as-of** | **2026-08-24** | Features/scores formed from this snapshot (and deltas vs **2026-08-21**). Only data on/before this date. |
| **Prediction day** | **2026-08-26** | The trading day the forward return is for (exit snapshot). |
| **Entry price** | Price @ 2026-08-24 | Long: buy here; short: sell here. |
| **Exit price** | Price @ 2026-08-26 | Close proxy on prediction day. |
| **Return column** | `fwd_2d` | Long: exit/entry − 1; short = opposite. |

Graded **n=11605** names with valid entry and exit prices.

Provisional until multiple signal dates agree.

_Column guide: **IC** = Spearman(feature, long forward return); **IC↑** / **IC↓** = IC among names that went up / down._

## Score calibration (long fwd)
- Spearman IC(total_score, fwd_2d) = **-0.0285**

| Quintile | Mean long fwd | Hit up>1.5% | n |
|---|---|---|---|
| 1 | 0.90% | 27.1% | 2376 |
| 2 | 0.35% | 15.2% | 2960 |
| 3 | 0.19% | 8.3% | 1781 |
| 4 | 0.26% | 8.5% | 2187 |
| 5 | 1.21% | 31.2% | 2301 |

## Top |IC| features

| Feature | IC | IC↑ | IC↓ | Mean fwd when + | Mean fwd when − | n+/n− |
|---|---|---|---|---|---|---|
| Performance (Week) | -0.2602 | -0.2546 | -0.1008 | -0.11% | 1.13% | 5048/6337 |
| d_Price | -0.2455 | -0.2471 | +0.0363 | 0.22% | 0.80% | 4452/6543 |
| d_Performance (YTD) | -0.2400 | -0.3226 | +0.0195 | 0.24% | 0.81% | 4523/6632 |
| d_200-Day Simple Moving Average | -0.2377 | -0.3121 | -0.0042 | 0.30% | 0.76% | 4561/6899 |
| true_ret | -0.2318 | -0.3384 | +0.0214 | 0.22% | 0.80% | 4452/6543 |
| d_50-Day Simple Moving Average | -0.2184 | -0.3219 | +0.0086 | 0.29% | 0.75% | 4443/7007 |
| Relative Strength Index (14) | -0.2083 | -0.2954 | +0.0862 | 0.59% | n/a | 11481/0 |
| d_20-Day Simple Moving Average | -0.2035 | -0.3357 | +0.0514 | 0.32% | 0.72% | 4156/7305 |
| d_Forward P/E | -0.2005 | -0.2086 | -0.0521 | -0.30% | 1.10% | 1398/1537 |
| d_Relative Strength Index (14) | -0.2002 | -0.1656 | +0.0672 | 0.25% | 0.80% | 4532/6578 |
| d_Performance (Week) | -0.1912 | -0.2136 | -0.0369 | 0.08% | 1.19% | 6179/5151 |
| d_Performance (Quarter) | -0.1858 | -0.2446 | -0.0122 | 0.32% | 0.72% | 4059/6757 |
| upside_pct_lvl | +0.1476 | +0.4172 | -0.2708 | 0.90% | -0.46% | 4297/346 |
| d_Market Cap | -0.1401 | -0.1344 | +0.0133 | 0.67% | 0.80% | 2451/3252 |
| Performance (Month) | -0.1057 | -0.0085 | -0.1279 | 0.36% | 1.11% | 7796/3550 |
| d_Performance (Month) | +0.0716 | +0.1303 | -0.0588 | 1.04% | 0.29% | 4677/6591 |
| d_Beta | -0.0582 | +0.0519 | -0.0886 | 1.45% | 0.79% | 2014/1223 |
| d_Analyst Recom | -0.0452 | -0.0277 | -0.0250 | -0.59% | 0.80% | 109/111 |
| Short Float | +0.0425 | +0.2607 | -0.0485 | 0.75% | n/a | 5681/0 |
| Institutional Transactions | +0.0274 | +0.0974 | -0.0443 | 1.01% | 0.82% | 3177/1880 |
| d_Volatility (Month) | +0.0236 | -0.0426 | +0.0342 | 0.60% | 0.70% | 3466/5985 |
| d_Institutional Ownership | -0.0229 | -0.0936 | +0.0838 | 0.07% | 0.56% | 881/409 |
| d_Short Float | +0.0196 | -0.0242 | +0.0379 | 6.31% | 0.13% | 173/219 |
| d_Profit Margin | -0.0189 | -0.0137 | -0.0158 | -1.29% | 0.58% | 9/10 |
| d_Gross Margin | +0.0179 | +0.0227 | +0.0176 | 1.71% | -0.27% | 16/6 |

## Combinations

| Pattern | n | Mean long fwd | Hit up |
|---|---|---|---|
| true_ret>3% & DOWNTREND | 206 | 6.45% | 35.0% |
| true_ret>3% & UPTREND | 226 | -1.03% | 22.1% |
| true_ret>3% & MIXED | 171 | 0.50% | 26.3% |

## Risk dominance probes

| State | n | Mean long fwd | Mean fwd if score top quintile |
|---|---|---|---|
| EXTENDED | 458 | -0.36% | -0.49% |
| WASHED | 491 | 1.44% | 1.24% |

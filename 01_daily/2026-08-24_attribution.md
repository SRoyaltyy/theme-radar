# Factor attribution — signal 2026-08-24 → prediction day 2026-08-28

## Trade window (read this first)

| Role | Date | Meaning |
|------|------|---------|
| **Signal as-of** | **2026-08-24** | Features/scores formed from this snapshot (and deltas vs **2026-08-21**). Only data on/before this date. |
| **Prediction day** | **2026-08-28** | The trading day the forward return is for (exit snapshot). |
| **Entry price** | Price @ 2026-08-24 | Long: buy here; short: sell here. |
| **Exit price** | Price @ 2026-08-28 | Close proxy on prediction day. |
| **Return column** | `fwd_3d` | Long: exit/entry − 1; short = opposite. |

Graded **n=11604** names with valid entry and exit prices.

Provisional until multiple signal dates agree.

_Column guide: **IC** = Spearman(feature, long forward return); **IC↑** / **IC↓** = IC among names that went up / down._

## Score calibration (long fwd)
- Spearman IC(total_score, fwd_3d) = **-0.0880**

| Quintile | Mean long fwd | Hit up>1.5% | n |
|---|---|---|---|
| 1 | 0.16% | 27.8% | 2376 |
| 2 | 0.16% | 16.0% | 2960 |
| 3 | -0.26% | 7.4% | 1781 |
| 4 | -0.24% | 9.2% | 2186 |
| 5 | 1.78% | 23.9% | 2301 |

## Top |IC| features

| Feature | IC | IC↑ | IC↓ | Mean fwd when + | Mean fwd when − | n+/n− |
|---|---|---|---|---|---|---|
| d_Relative Strength Index (14) | -0.1582 | -0.1029 | +0.0433 | -0.22% | 0.72% | 4531/6578 |
| d_Price | -0.1451 | -0.1766 | +0.0176 | -0.26% | 0.18% | 4451/6543 |
| Performance (Week) | -0.1389 | -0.1781 | -0.0532 | -0.03% | 0.63% | 5047/6337 |
| d_Performance (Quarter) | -0.1364 | -0.2227 | -0.0134 | -0.46% | 0.91% | 4058/6757 |
| d_Performance (YTD) | -0.1298 | -0.2415 | +0.0361 | -0.27% | 0.72% | 4522/6632 |
| d_200-Day Simple Moving Average | -0.1270 | -0.2296 | +0.0225 | -0.19% | 0.68% | 4560/6899 |
| d_50-Day Simple Moving Average | -0.1220 | -0.2590 | +0.0377 | -0.24% | 0.69% | 4442/7007 |
| true_ret | -0.1183 | -0.2572 | +0.0491 | -0.26% | 0.18% | 4451/6543 |
| d_Forward P/E | -0.1082 | -0.1059 | +0.0163 | -0.64% | 0.33% | 1398/1537 |
| d_20-Day Simple Moving Average | -0.1082 | -0.2868 | +0.0852 | -0.17% | 0.61% | 4155/7305 |
| Relative Volume | -0.0818 | +0.0786 | -0.0431 | 0.33% | n/a | 11328/0 |
| Short Float | -0.0723 | +0.2531 | -0.1026 | 0.83% | n/a | 5681/0 |
| d_Market Cap | -0.0631 | -0.0597 | +0.0339 | 0.13% | 1.28% | 2451/3252 |
| Relative Strength Index (14) | -0.0573 | -0.2062 | +0.0447 | 0.35% | n/a | 11480/0 |
| d_Performance (Month) | -0.0516 | -0.0129 | -0.1137 | 0.97% | -0.08% | 4677/6590 |
| d_Performance (Week) | -0.0490 | -0.0725 | +0.0164 | 0.28% | 0.40% | 6178/5151 |
| d_Average Volume | -0.0482 | -0.0347 | -0.0473 | 0.61% | 0.15% | 4920/6082 |
| upside_pct_lvl | -0.0458 | +0.3357 | -0.3488 | 0.93% | -0.49% | 4297/346 |
| d_Beta | -0.0414 | +0.0915 | -0.1072 | 0.42% | 1.11% | 2014/1223 |
| d_Volatility (Month) | -0.0382 | -0.1022 | +0.0116 | 0.31% | 0.51% | 3466/5984 |
| Institutional Transactions | -0.0361 | +0.1054 | -0.0759 | 1.49% | 0.26% | 3177/1880 |
| d_Short Ratio | +0.0278 | +0.0092 | +0.0134 | 0.25% | -0.46% | 3704/3061 |
| d_Institutional Ownership | -0.0216 | -0.0339 | +0.0745 | -0.48% | -0.16% | 881/409 |
| d_Sales Year Over Year TTM | -0.0185 | -0.0022 | -0.0087 | -2.40% | -1.56% | 9/8 |
| Performance (Month) | -0.0184 | +0.1288 | -0.1095 | 0.04% | 1.03% | 7796/3549 |

## Combinations

| Pattern | n | Mean long fwd | Hit up |
|---|---|---|---|
| true_ret>3% & DOWNTREND | 206 | 3.14% | 30.6% |
| true_ret>3% & UPTREND | 226 | -1.59% | 22.6% |
| true_ret>3% & MIXED | 171 | -0.49% | 30.4% |

## Risk dominance probes

| State | n | Mean long fwd | Mean fwd if score top quintile |
|---|---|---|---|
| EXTENDED | 458 | -0.25% | 3.28% |
| WASHED | 491 | 1.82% | 1.10% |

# Factor attribution — signal 2026-10-09 → prediction day 2026-10-12

## Trade window (read this first)

| Role | Date | Meaning |
|------|------|---------|
| **Signal as-of** | **2026-10-09** | Features/scores formed from this snapshot (and deltas vs **2026-10-08**). Only data on/before this date. |
| **Prediction day** | **2026-10-12** | The trading day the forward return is for (exit snapshot). |
| **Entry price** | Price @ 2026-10-09 | Long: buy here; short: sell here. |
| **Exit price** | Price @ 2026-10-12 | Close proxy on prediction day. |
| **Return column** | `fwd_1d` | Long: exit/entry − 1; short = opposite. |

Graded **n=11699** names with valid entry and exit prices.

Provisional until multiple signal dates agree.

_Column guide: **IC** = Spearman(feature, long forward return); **IC↑** / **IC↓** = IC among names that went up / down._

## Score calibration (long fwd)
- Spearman IC(total_score, fwd_1d) = **-0.1863**

| Quintile | Mean long fwd | Hit up>1.5% | n |
|---|---|---|---|
| 1 | 1.33% | 13.3% | 2346 |
| 2 | 1.77% | 6.3% | 2389 |
| 3 | -0.46% | 5.8% | 2342 |
| 4 | -0.79% | 7.7% | 2287 |
| 5 | -0.58% | 8.3% | 2335 |

## Top |IC| features

| Feature | IC | IC↑ | IC↓ | Mean fwd when + | Mean fwd when − | n+/n− |
|---|---|---|---|---|---|---|
| d_Performance (Quarter) | -0.3882 | -0.1529 | -0.3092 | -0.10% | 1.42% | 8054/3103 |
| upside_pct_lvl | -0.3659 | +0.1739 | -0.4613 | 0.57% | -0.51% | 4353/278 |
| d_Performance (Month) | -0.2826 | -0.0645 | -0.2395 | -0.16% | 1.70% | 8719/2718 |
| Performance (Week) | +0.2511 | +0.0121 | +0.3610 | 0.09% | 0.49% | 6246/5268 |
| d_20-Day Simple Moving Average | -0.1679 | -0.0511 | -0.0833 | 0.01% | 0.91% | 8199/3392 |
| d_50-Day Simple Moving Average | -0.1520 | -0.0686 | -0.0451 | -0.46% | 1.88% | 7974/3617 |
| d_200-Day Simple Moving Average | -0.1514 | -0.0842 | -0.0105 | -0.45% | 1.73% | 7706/3860 |
| d_Performance (YTD) | -0.1421 | -0.0901 | +0.0293 | -0.41% | 1.71% | 7516/3804 |
| true_ret | -0.1362 | -0.0776 | -0.0116 | -0.41% | 0.38% | 7434/3713 |
| d_Forward P/E | -0.1243 | -0.0227 | -0.0856 | -0.40% | -0.00% | 1556/1401 |
| Short Float | -0.1060 | +0.1222 | -0.2062 | 1.17% | n/a | 5683/0 |
| d_Price | -0.1050 | -0.1191 | +0.1731 | -0.41% | 0.38% | 7434/3713 |
| d_Relative Strength Index (14) | -0.0981 | -0.2039 | +0.2758 | -0.43% | 1.69% | 7494/3812 |
| Institutional Transactions | -0.0949 | +0.0649 | -0.1296 | 2.59% | -0.85% | 3242/1801 |
| Relative Strength Index (14) | +0.0840 | +0.0384 | +0.2318 | 0.27% | n/a | 11612/0 |
| d_Beta | -0.0623 | +0.0523 | -0.1059 | 1.18% | 7.20% | 1553/735 |
| Performance (Month) | +0.0616 | -0.1232 | +0.2223 | -0.68% | 0.86% | 4342/7158 |
| Relative Volume | +0.0483 | +0.0283 | +0.0082 | 0.28% | n/a | 11404/0 |
| d_Market Cap | -0.0475 | -0.0038 | +0.0959 | -0.33% | 2.78% | 3039/2669 |
| d_Volatility (Month) | -0.0437 | +0.0904 | -0.1225 | 1.11% | -0.88% | 6021/3626 |
| d_Gross Margin | +0.0298 | +0.0178 | +0.0252 | 1.95% | 32.47% | 6/4 |
| d_Short Float | +0.0286 | -0.0257 | +0.0394 | -2.19% | 1.12% | 28/57 |
| d_Performance (Week) | -0.0281 | -0.0868 | +0.0293 | 0.53% | 0.05% | 5524/5954 |
| d_Relative Volume | +0.0215 | -0.0473 | +0.0565 | 2.05% | -0.50% | 3570/7764 |
| d_Short Ratio | -0.0197 | +0.0107 | -0.0028 | -0.70% | 0.86% | 3263/3920 |

## Combinations

| Pattern | n | Mean long fwd | Hit up |
|---|---|---|---|
| true_ret>3% & DOWNTREND | 428 | 2.13% | 11.2% |
| true_ret>3% & UPTREND | 361 | -2.05% | 15.2% |
| true_ret>3% & MIXED | 187 | -1.15% | 20.9% |

## Risk dominance probes

| State | n | Mean long fwd | Mean fwd if score top quintile |
|---|---|---|---|
| EXTENDED | 172 | -1.73% | -7.45% |
| WASHED | 1068 | 7.68% | 4.67% |

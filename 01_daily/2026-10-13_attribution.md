# Factor attribution — signal 2026-10-13 → prediction day 2026-10-14

## Trade window (read this first)

| Role | Date | Meaning |
|------|------|---------|
| **Signal as-of** | **2026-10-13** | Features/scores formed from this snapshot (and deltas vs **2026-10-12**). Only data on/before this date. |
| **Prediction day** | **2026-10-14** | The trading day the forward return is for (exit snapshot). |
| **Entry price** | Price @ 2026-10-13 | Long: buy here; short: sell here. |
| **Exit price** | Price @ 2026-10-14 | Close proxy on prediction day. |
| **Return column** | `fwd_1d` | Long: exit/entry − 1; short = opposite. |

Graded **n=11714** names with valid entry and exit prices.

Provisional until multiple signal dates agree.

_Column guide: **IC** = Spearman(feature, long forward return); **IC↑** / **IC↓** = IC among names that went up / down._

## Score calibration (long fwd)
- Spearman IC(total_score, fwd_1d) = **-0.0400**

| Quintile | Mean long fwd | Hit up>1.5% | n |
|---|---|---|---|
| 1 | -2.68% | 10.3% | 2347 |
| 2 | -1.43% | 5.7% | 2593 |
| 3 | -1.33% | 4.1% | 2255 |
| 4 | -1.47% | 4.5% | 2222 |
| 5 | -1.84% | 6.4% | 2297 |

## Top |IC| features

| Feature | IC | IC↑ | IC↓ | Mean fwd when + | Mean fwd when − | n+/n− |
|---|---|---|---|---|---|---|
| Performance (Week) | +0.4450 | +0.0265 | +0.5118 | -0.62% | -2.58% | 4766/6752 |
| upside_pct_lvl | -0.3368 | +0.2881 | -0.4518 | -1.80% | -1.40% | 4355/280 |
| d_20-Day Simple Moving Average | +0.2058 | -0.0724 | +0.2736 | -0.99% | -2.45% | 5416/6156 |
| true_ret | +0.1998 | -0.1271 | +0.2865 | -0.93% | -2.54% | 5046/5892 |
| d_50-Day Simple Moving Average | +0.1988 | -0.0892 | +0.2731 | -0.97% | -2.49% | 5438/6098 |
| d_Performance (YTD) | +0.1966 | -0.1319 | +0.2764 | -0.94% | -2.52% | 5190/6004 |
| d_200-Day Simple Moving Average | +0.1925 | -0.1101 | +0.2604 | -0.98% | -2.41% | 5203/6309 |
| d_Price | +0.1924 | -0.1367 | +0.2549 | -0.93% | -2.54% | 5046/5892 |
| Short Float | -0.1895 | +0.0057 | -0.2079 | -1.86% | n/a | 5673/0 |
| d_Performance (Week) | +0.1882 | -0.0199 | +0.2105 | -1.17% | -2.13% | 4269/7230 |
| d_Relative Strength Index (14) | +0.1739 | -0.1948 | +0.2307 | -0.93% | -2.53% | 5201/6013 |
| d_Beta | +0.1697 | -0.0033 | +0.2143 | -1.87% | -4.18% | 578/990 |
| d_Performance (Month) | -0.1581 | -0.2431 | -0.0788 | -1.75% | -1.80% | 6781/4631 |
| Relative Strength Index (14) | +0.1538 | +0.0090 | +0.2555 | -1.75% | n/a | 11649/0 |
| Institutional Transactions | -0.1206 | +0.0259 | -0.1254 | -2.54% | -0.70% | 3265/1778 |
| d_Market Cap | +0.0901 | -0.1358 | +0.1172 | -0.95% | -2.49% | 2390/3314 |
| d_Forward P/E | +0.0800 | -0.1059 | +0.1168 | -1.41% | -1.81% | 1463/1473 |
| Performance (Month) | +0.0715 | -0.2007 | +0.1516 | -1.91% | -1.67% | 4139/7389 |
| d_Target Price | -0.0508 | +0.0341 | -0.0445 | -1.60% | -1.29% | 191/376 |
| d_Volatility (Month) | -0.0388 | +0.0318 | -0.0471 | -2.08% | -1.91% | 4056/5089 |
| d_Performance (Quarter) | +0.0374 | -0.1100 | +0.0588 | -2.22% | -1.45% | 4442/6711 |
| d_Institutional Ownership | +0.0309 | -0.0143 | +0.0429 | 4.33% | -2.69% | 11/20 |
| d_Total Debt/Equity | -0.0293 | -0.0037 | -0.0301 | -6.25% | 4.06% | 4/2 |
| d_Relative Volume | +0.0288 | -0.0554 | +0.0207 | -1.62% | -1.99% | 6637/4625 |
| d_Analyst Recom | +0.0259 | +0.0383 | +0.0106 | -1.16% | -1.88% | 67/68 |

## Combinations

| Pattern | n | Mean long fwd | Hit up |
|---|---|---|---|
| true_ret>3% & DOWNTREND | 233 | 4.75% | 15.5% |
| true_ret>3% & UPTREND | 162 | -2.27% | 15.4% |
| true_ret>3% & MIXED | 96 | -1.30% | 30.2% |

## Risk dominance probes

| State | n | Mean long fwd | Mean fwd if score top quintile |
|---|---|---|---|
| EXTENDED | 157 | -1.19% | -3.28% |
| WASHED | 1275 | -2.40% | 3.19% |

# Factor attribution — signal 2026-09-04 → prediction day 2026-09-08

## Trade window (read this first)

| Role | Date | Meaning |
|------|------|---------|
| **Signal as-of** | **2026-09-04** | Features/scores formed from this snapshot (and deltas vs **2026-09-03**). Only data on/before this date. |
| **Prediction day** | **2026-09-08** | The trading day the forward return is for (exit snapshot). |
| **Entry price** | Price @ 2026-09-04 | Long: buy here; short: sell here. |
| **Exit price** | Price @ 2026-09-08 | Close proxy on prediction day. |
| **Return column** | `fwd_1d` | Long: exit/entry − 1; short = opposite. |

Graded **n=11593** names with valid entry and exit prices.

Provisional until multiple signal dates agree.

_Column guide: **IC** = Spearman(feature, long forward return); **IC↑** / **IC↓** = IC among names that went up / down._

## Score calibration (long fwd)
- Spearman IC(total_score, fwd_1d) = **-0.0292**

| Quintile | Mean long fwd | Hit up>1.5% | n |
|---|---|---|---|
| 1 | 1.24% | 18.2% | 2339 |
| 2 | 1.17% | 8.0% | 2861 |
| 3 | 0.83% | 7.1% | 1766 |
| 4 | -0.46% | 9.6% | 2311 |
| 5 | 1.50% | 25.3% | 2316 |

## Top |IC| features

| Feature | IC | IC↑ | IC↓ | Mean fwd when + | Mean fwd when − | n+/n− |
|---|---|---|---|---|---|---|
| d_Performance (Week) | +0.1355 | +0.3185 | -0.0533 | 0.83% | 1.02% | 7415/3989 |
| d_Price | +0.1101 | +0.1020 | +0.0355 | 0.62% | 0.94% | 5236/5646 |
| d_50-Day Simple Moving Average | +0.1044 | +0.1426 | +0.0448 | 1.03% | 0.76% | 5553/5899 |
| d_Performance (Quarter) | +0.0917 | +0.3248 | -0.1174 | 0.74% | 1.32% | 8558/2363 |
| d_200-Day Simple Moving Average | +0.0888 | +0.1232 | +0.0316 | 0.93% | 0.85% | 5417/6023 |
| Short Float | -0.0862 | +0.2097 | -0.2039 | 1.46% | n/a | 5677/0 |
| Institutional Transactions | +0.0859 | +0.1359 | +0.0063 | 2.27% | 1.03% | 3182/1856 |
| true_ret | +0.0855 | +0.1108 | +0.0455 | 0.62% | 0.94% | 5236/5646 |
| d_Performance (YTD) | +0.0851 | +0.1054 | +0.0391 | 0.95% | 0.92% | 5342/5757 |
| d_Relative Strength Index (14) | +0.0825 | +0.0890 | +0.0066 | 0.94% | 0.93% | 5348/5763 |
| d_20-Day Simple Moving Average | +0.0786 | +0.1383 | +0.0221 | 0.92% | 0.85% | 5852/5594 |
| upside_pct_lvl | +0.0785 | +0.3682 | -0.2034 | 0.89% | -1.40% | 4309/335 |
| Performance (Week) | +0.0738 | +0.0949 | +0.0158 | 0.50% | 1.30% | 5734/5641 |
| d_Forward P/E | +0.0731 | +0.1677 | +0.0011 | -0.72% | -1.07% | 1533/1400 |
| Relative Strength Index (14) | -0.0685 | -0.0986 | -0.0048 | 0.89% | n/a | 11494/0 |
| d_Beta | -0.0341 | +0.0484 | -0.0977 | 6.18% | 0.61% | 1560/1207 |
| d_Short Float | -0.0340 | +0.0066 | -0.0231 | -2.32% | 0.34% | 19/28 |
| Performance (Month) | -0.0303 | -0.0709 | -0.0345 | -0.05% | 1.88% | 5824/5542 |
| d_Short Ratio | -0.0297 | +0.0372 | -0.0769 | 0.15% | 1.39% | 4291/2676 |
| Relative Volume | -0.0250 | +0.0618 | -0.0565 | 0.89% | n/a | 11311/0 |
| d_Insider Transactions | +0.0225 | -0.0166 | +0.0285 | -0.36% | 1.36% | 246/237 |
| d_Institutional Ownership | +0.0216 | +0.0322 | -0.0018 | -0.57% | -0.95% | 353/293 |
| d_EPS Surprise | +0.0210 | +0.0417 | +0.0133 | 0.97% | -1.23% | 19/16 |
| d_Market Cap | +0.0148 | +0.1273 | -0.0119 | 0.61% | 2.00% | 2962/2709 |
| d_Average Volume | +0.0146 | -0.0479 | +0.0841 | 2.20% | 0.05% | 4508/6535 |

## Combinations

| Pattern | n | Mean long fwd | Hit up |
|---|---|---|---|
| true_ret>3% & DOWNTREND | 367 | 8.24% | 48.0% |
| true_ret>3% & UPTREND | 279 | 4.11% | 34.4% |
| true_ret>3% & MIXED | 235 | 2.30% | 46.8% |

## Risk dominance probes

| State | n | Mean long fwd | Mean fwd if score top quintile |
|---|---|---|---|
| EXTENDED | 242 | 0.10% | 0.80% |
| WASHED | 680 | 4.34% | 17.72% |

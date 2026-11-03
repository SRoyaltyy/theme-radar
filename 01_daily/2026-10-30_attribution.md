# Factor attribution — signal 2026-10-30 → prediction day 2026-11-03

## Trade window (read this first)

| Role | Date | Meaning |
|------|------|---------|
| **Signal as-of** | **2026-10-30** | Features/scores formed from this snapshot (and deltas vs **2026-10-29**). Only data on/before this date. |
| **Prediction day** | **2026-11-03** | The trading day the forward return is for (exit snapshot). |
| **Entry price** | Price @ 2026-10-30 | Long: buy here; short: sell here. |
| **Exit price** | Price @ 2026-11-03 | Close proxy on prediction day. |
| **Return column** | `fwd_2d` | Long: exit/entry − 1; short = opposite. |

Graded **n=11731** names with valid entry and exit prices.

Provisional until multiple signal dates agree.

_Column guide: **IC** = Spearman(feature, long forward return); **IC↑** / **IC↓** = IC among names that went up / down._

## Score calibration (long fwd)
- Spearman IC(total_score, fwd_2d) = **0.0353**

| Quintile | Mean long fwd | Hit up>1.5% | n |
|---|---|---|---|
| 1 | 0.08% | 19.2% | 2635 |
| 2 | 1.21% | 20.8% | 2146 |
| 3 | 0.09% | 20.8% | 2264 |
| 4 | -0.26% | 11.4% | 2403 |
| 5 | 0.04% | 24.4% | 2283 |

## Top |IC| features

| Feature | IC | IC↑ | IC↓ | Mean fwd when + | Mean fwd when − | n+/n− |
|---|---|---|---|---|---|---|
| d_Performance (Week) | +0.1409 | -0.0604 | +0.2833 | 0.43% | 0.11% | 3976/7564 |
| upside_pct_lvl | -0.0567 | +0.3783 | -0.2893 | 0.21% | -0.78% | 4324/307 |
| Institutional Transactions | -0.0438 | +0.0507 | -0.0904 | 0.73% | 0.72% | 3231/1814 |
| d_50-Day Simple Moving Average | +0.0407 | -0.1587 | +0.1980 | 0.02% | 0.30% | 3255/8380 |
| Performance (Month) | +0.0401 | -0.2025 | +0.2195 | -0.12% | 0.52% | 5345/6213 |
| d_Short Float | +0.0369 | -0.0073 | +0.0572 | 1.51% | -0.43% | 39/38 |
| true_ret | +0.0364 | -0.2112 | +0.2421 | -0.05% | 0.30% | 2928/8403 |
| d_200-Day Simple Moving Average | +0.0337 | -0.1355 | +0.1712 | 0.04% | 0.30% | 3088/8533 |
| d_20-Day Simple Moving Average | +0.0300 | -0.1812 | +0.2085 | -0.01% | 0.29% | 2824/8800 |
| d_Target Price | -0.0281 | -0.0525 | +0.0257 | 0.28% | 1.40% | 336/295 |
| d_Performance (YTD) | +0.0277 | -0.1224 | +0.1512 | 0.01% | -0.08% | 2966/8453 |
| Performance (Week) | +0.0239 | -0.0321 | +0.0464 | -0.16% | 0.63% | 5950/5620 |
| d_Performance (Month) | +0.0239 | -0.1277 | +0.1728 | 0.13% | 0.28% | 3441/8036 |
| d_EPS Surprise | -0.0201 | -0.0270 | -0.0270 | -0.11% | 1.37% | 97/108 |
| d_Volatility (Month) | +0.0200 | +0.1916 | -0.1778 | 0.74% | -0.11% | 4617/5051 |
| d_Performance (Quarter) | -0.0183 | -0.2232 | +0.1923 | -0.33% | 0.44% | 2602/8581 |
| Relative Volume | +0.0154 | +0.0857 | -0.0603 | 0.22% | n/a | 11471/0 |
| d_Price | -0.0151 | -0.0035 | -0.0103 | -0.05% | 0.30% | 2928/8403 |
| d_Forward P/E | +0.0151 | -0.1033 | +0.0371 | 0.15% | 0.22% | 932/2029 |
| d_Institutional Ownership | +0.0145 | -0.0219 | +0.0235 | 0.04% | -0.05% | 1382/1271 |
| d_Gross Margin | +0.0143 | +0.0325 | -0.0122 | 0.62% | 0.26% | 173/96 |
| Short Float | -0.0141 | +0.2498 | -0.2071 | 0.76% | n/a | 5648/0 |
| d_Beta | -0.0131 | +0.1473 | -0.1555 | 2.16% | -0.68% | 1820/1191 |
| d_Relative Strength Index (14) | -0.0129 | +0.1385 | -0.1778 | 0.00% | 0.30% | 2969/8447 |
| d_Relative Volume | -0.0122 | -0.0232 | +0.0270 | 0.49% | -0.13% | 6741/4576 |

## Combinations

| Pattern | n | Mean long fwd | Hit up |
|---|---|---|---|
| true_ret>3% & DOWNTREND | 166 | 1.68% | 36.7% |
| true_ret>3% & UPTREND | 147 | -0.80% | 34.7% |
| true_ret>3% & MIXED | 146 | 0.52% | 32.2% |

## Risk dominance probes

| State | n | Mean long fwd | Mean fwd if score top quintile |
|---|---|---|---|
| EXTENDED | 219 | 0.00% | 1.29% |
| WASHED | 1669 | 2.21% | -0.08% |

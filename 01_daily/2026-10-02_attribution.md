# Factor attribution — signal 2026-10-02 → prediction day 2026-10-06

## Trade window (read this first)

| Role | Date | Meaning |
|------|------|---------|
| **Signal as-of** | **2026-10-02** | Features/scores formed from this snapshot (and deltas vs **2026-10-01**). Only data on/before this date. |
| **Prediction day** | **2026-10-06** | The trading day the forward return is for (exit snapshot). |
| **Entry price** | Price @ 2026-10-02 | Long: buy here; short: sell here. |
| **Exit price** | Price @ 2026-10-06 | Close proxy on prediction day. |
| **Return column** | `fwd_2d` | Long: exit/entry − 1; short = opposite. |

Graded **n=11684** names with valid entry and exit prices.

Provisional until multiple signal dates agree.

_Column guide: **IC** = Spearman(feature, long forward return); **IC↑** / **IC↓** = IC among names that went up / down._

## Score calibration (long fwd)
- Spearman IC(total_score, fwd_2d) = **0.0757**

| Quintile | Mean long fwd | Hit up>1.5% | n |
|---|---|---|---|
| 1 | 2.54% | 23.0% | 2538 |
| 2 | 0.82% | 13.3% | 2472 |
| 3 | 0.47% | 19.7% | 2086 |
| 4 | 0.77% | 24.5% | 2284 |
| 5 | 0.48% | 34.2% | 2304 |

## Top |IC| features

| Feature | IC | IC↑ | IC↓ | Mean fwd when + | Mean fwd when − | n+/n− |
|---|---|---|---|---|---|---|
| d_Price | +0.1307 | +0.0638 | +0.1215 | 0.75% | 1.79% | 7328/3868 |
| upside_pct_lvl | -0.1042 | +0.3011 | -0.4183 | 1.32% | -0.27% | 4368/264 |
| d_Relative Strength Index (14) | +0.1009 | -0.0382 | +0.1613 | 0.74% | 1.70% | 7356/3935 |
| d_Beta | -0.0903 | +0.0049 | -0.0912 | 1.33% | 1.33% | 4377/2560 |
| d_Performance (YTD) | +0.0892 | +0.1044 | +0.0733 | 0.74% | 1.51% | 7384/3935 |
| Relative Strength Index (14) | +0.0856 | +0.1372 | -0.0483 | 1.03% | n/a | 11575/0 |
| d_200-Day Simple Moving Average | +0.0854 | +0.1247 | +0.0490 | 0.82% | 1.50% | 7599/3978 |
| Institutional Transactions | -0.0833 | +0.0708 | -0.0995 | 1.91% | 0.60% | 3231/1811 |
| d_Forward P/E | -0.0830 | -0.0255 | -0.0256 | 0.63% | 1.00% | 1895/1056 |
| true_ret | +0.0807 | +0.1205 | +0.0436 | 0.75% | 1.79% | 7328/3868 |
| d_20-Day Simple Moving Average | +0.0797 | +0.1745 | +0.0044 | 0.79% | 1.69% | 8302/3294 |
| d_50-Day Simple Moving Average | +0.0693 | +0.1319 | +0.0221 | 0.79% | 1.56% | 7718/3899 |
| d_Performance (Month) | +0.0646 | +0.0262 | +0.0582 | 0.48% | 1.61% | 5640/5711 |
| d_Volatility (Month) | -0.0588 | +0.0308 | -0.1186 | 1.22% | 0.91% | 6289/3607 |
| d_Performance (Quarter) | -0.0554 | -0.0385 | +0.0531 | 0.72% | 1.38% | 5107/5944 |
| d_Performance (Week) | +0.0472 | +0.1512 | -0.0407 | 0.79% | 1.43% | 6830/4626 |
| Performance (Month) | +0.0435 | -0.1042 | +0.1198 | 0.50% | 1.30% | 3752/7741 |
| d_Average Volume | -0.0374 | -0.1066 | +0.0362 | 1.70% | 0.35% | 5721/5380 |
| Performance (Week) | +0.0298 | -0.0576 | +0.1316 | 0.45% | 1.35% | 3926/7592 |
| d_Market Cap | +0.0286 | -0.0327 | +0.1491 | 0.46% | 2.12% | 3313/2388 |
| d_EPS Surprise | -0.0242 | -0.0104 | -0.0190 | -0.58% | 4.44% | 2/3 |
| d_Target Price | -0.0222 | +0.0174 | -0.0710 | 1.00% | 1.04% | 125/284 |
| d_Short Ratio | +0.0202 | +0.0722 | -0.0373 | 0.45% | 0.87% | 3659/3816 |
| Short Float | -0.0196 | +0.1596 | -0.1373 | 1.29% | n/a | 5689/0 |
| d_Institutional Ownership | +0.0177 | +0.0572 | -0.1014 | 0.17% | 0.10% | 331/514 |

## Combinations

| Pattern | n | Mean long fwd | Hit up |
|---|---|---|---|
| true_ret>3% & DOWNTREND | 381 | 3.34% | 36.2% |
| true_ret>3% & UPTREND | 378 | 0.67% | 39.9% |
| true_ret>3% & MIXED | 220 | 0.52% | 40.0% |

## Risk dominance probes

| State | n | Mean long fwd | Mean fwd if score top quintile |
|---|---|---|---|
| EXTENDED | 215 | 0.56% | 1.04% |
| WASHED | 2057 | 2.89% | -0.18% |

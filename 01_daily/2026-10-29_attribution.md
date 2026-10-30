# Factor attribution — signal 2026-10-29 → prediction day 2026-10-30

## Trade window (read this first)

| Role | Date | Meaning |
|------|------|---------|
| **Signal as-of** | **2026-10-29** | Features/scores formed from this snapshot (and deltas vs **2026-10-28**). Only data on/before this date. |
| **Prediction day** | **2026-10-30** | The trading day the forward return is for (exit snapshot). |
| **Entry price** | Price @ 2026-10-29 | Long: buy here; short: sell here. |
| **Exit price** | Price @ 2026-10-30 | Close proxy on prediction day. |
| **Return column** | `fwd_1d` | Long: exit/entry − 1; short = opposite. |

Graded **n=11768** names with valid entry and exit prices.

Provisional until multiple signal dates agree.

_Column guide: **IC** = Spearman(feature, long forward return); **IC↑** / **IC↓** = IC among names that went up / down._

## Score calibration (long fwd)
- Spearman IC(total_score, fwd_1d) = **0.2413**

| Quintile | Mean long fwd | Hit up>1.5% | n |
|---|---|---|---|
| 1 | -1.19% | 7.3% | 2375 |
| 2 | -1.93% | 5.8% | 2780 |
| 3 | -1.29% | 5.0% | 2228 |
| 4 | -0.11% | 7.4% | 2041 |
| 5 | -1.30% | 11.7% | 2344 |

## Top |IC| features

| Feature | IC | IC↑ | IC↓ | Mean fwd when + | Mean fwd when − | n+/n− |
|---|---|---|---|---|---|---|
| Performance (Month) | +0.4367 | +0.0899 | +0.5091 | -0.64% | -1.90% | 6298/5291 |
| d_Performance (Week) | -0.3972 | -0.1239 | -0.3783 | -2.14% | -0.60% | 7362/4197 |
| Relative Strength Index (14) | +0.3818 | -0.2415 | +0.4435 | -1.21% | n/a | 11686/0 |
| d_Price | +0.3365 | +0.0306 | +0.3612 | -0.70% | -3.11% | 6326/4873 |
| upside_pct_lvl | -0.3354 | +0.2498 | -0.4325 | -1.98% | -1.18% | 4285/352 |
| d_Relative Strength Index (14) | +0.3139 | -0.1126 | +0.3377 | -0.70% | -3.08% | 6392/4952 |
| d_Performance (YTD) | +0.3065 | +0.0755 | +0.3504 | -0.70% | -3.20% | 6402/4955 |
| d_Beta | +0.2969 | -0.0431 | +0.3349 | -0.74% | 1.19% | 983/1708 |
| d_200-Day Simple Moving Average | +0.2930 | +0.1043 | +0.3274 | -0.75% | -3.12% | 6551/5030 |
| true_ret | +0.2916 | +0.1151 | +0.3342 | -0.70% | -3.11% | 6326/4873 |
| d_50-Day Simple Moving Average | +0.2658 | +0.1299 | +0.2983 | -0.59% | -2.99% | 6794/4807 |
| d_Market Cap | +0.2333 | -0.1228 | +0.3332 | -0.69% | -1.83% | 3420/2295 |
| Performance (Week) | -0.2260 | -0.0940 | -0.1943 | -2.18% | -0.30% | 7855/3722 |
| d_Performance (Month) | +0.2173 | +0.0943 | +0.2693 | -0.70% | -1.96% | 6733/4750 |
| d_20-Day Simple Moving Average | +0.2026 | +0.1003 | +0.2315 | -0.63% | -2.82% | 6533/5048 |
| d_Forward P/E | +0.1997 | -0.1056 | +0.2624 | -0.91% | -2.67% | 2041/919 |
| d_Performance (Quarter) | +0.1738 | +0.0744 | +0.1737 | -1.17% | -1.21% | 6499/4717 |
| Short Float | -0.1678 | +0.1630 | -0.1880 | -0.79% | n/a | 5643/0 |
| Institutional Transactions | -0.1039 | +0.0244 | -0.0945 | -1.99% | 1.58% | 3237/1814 |
| d_Volatility (Month) | -0.0818 | +0.0838 | -0.1312 | -1.53% | -1.92% | 4791/4464 |
| d_Target Price | +0.0459 | +0.0069 | +0.0236 | -1.06% | -2.01% | 254/246 |
| d_Relative Volume | +0.0444 | +0.0212 | +0.0405 | -1.51% | -1.61% | 5429/5843 |
| d_Average Volume | +0.0315 | -0.0465 | +0.0353 | -1.02% | -2.10% | 5380/5622 |
| Relative Volume | +0.0210 | +0.1271 | -0.0071 | -1.61% | n/a | 11411/0 |
| d_EPS Surprise | -0.0206 | -0.0127 | -0.0082 | -1.29% | -1.24% | 134/186 |

## Combinations

| Pattern | n | Mean long fwd | Hit up |
|---|---|---|---|
| true_ret>3% & DOWNTREND | 463 | 1.50% | 14.7% |
| true_ret>3% & UPTREND | 323 | -0.88% | 19.5% |
| true_ret>3% & MIXED | 283 | -0.49% | 22.6% |

## Risk dominance probes

| State | n | Mean long fwd | Mean fwd if score top quintile |
|---|---|---|---|
| EXTENDED | 227 | -2.60% | -6.43% |
| WASHED | 1223 | 1.84% | 3.05% |

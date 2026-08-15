# Predictive audit — horizon **1d**

Generated: 2026-08-15T04:32:51.037342-04:00
Signal dates pooled: **6** (`2026-08-06, 2026-08-07, 2026-08-10, 2026-08-11, 2026-08-12, 2026-08-13`)

## 1. Prediction accuracy (composite `total_score`, full universe)

Rule: score > +2 → expect UP; score < −2 → expect DOWN; else neutral.

| Metric | Value |
|--------|-------|
| Names graded | 69263 |
| Actionable (|score|>2) | 18613 |
| **Accuracy (actionable)** | **45.1%** |
| Long accuracy | 47.1% |
| Short accuracy | 43.1% |
| Spearman IC(score, fwd) | -0.0059 |

### Per signal date

| Signal | n | Actionable | Accuracy | Long | Short | IC |
|--------|---|------------|----------|------|-------|----|
| 2026-08-06 | 11543 | 314 | 58.0% | 63.3% | 30.0% | +0.0958 |
| 2026-08-07 | 11525 | 4349 | 45.4% | 41.9% | 52.3% | -0.0339 |
| 2026-08-10 | 11533 | 4490 | 43.2% | 49.8% | 39.2% | -0.0491 |
| 2026-08-11 | 11543 | 3818 | 51.0% | 51.5% | 50.4% | +0.1007 |
| 2026-08-12 | 11553 | 2681 | 42.3% | 48.4% | 37.6% | -0.0472 |
| 2026-08-13 | 11566 | 2961 | 41.3% | 43.6% | 39.3% | -0.0908 |

## 2. Top correlating factors (pooled across dates)

IC = Spearman(factor, forward return). Ranked by |IC|. Spread = mean fwd when factor>0 minus mean fwd when factor<0.

| Rank | Factor | IC | n | Mean fwd if ↑ | Mean fwd if ↓ | Spread |
|------|--------|----|---|---------------|---------------|--------|
| 1 | d_Relative Strength Index (14) | -0.1060 | 57159 | +0.22% | +2.29% | -2.07% |
| 2 | d_200-Day Simple Moving Average | -0.1049 | 57671 | +0.28% | +2.12% | -1.84% |
| 3 | true_ret | -0.1009 | 57671 | +0.15% | +1.76% | -1.61% |
| 4 | d_Forward P/E | -0.0997 | 15251 | -0.02% | +0.39% | -0.41% |
| 5 | d_50-Day Simple Moving Average | -0.0988 | 57671 | +0.34% | +2.02% | -1.67% |
| 6 | d_Performance (Week) | -0.0981 | 57405 | +0.50% | +1.55% | -1.05% |
| 7 | d_Performance (YTD) | -0.0969 | 57630 | +0.22% | +1.79% | -1.57% |
| 8 | d_20-Day Simple Moving Average | -0.0951 | 57671 | +0.42% | +1.83% | -1.42% |
| 9 | d_Price | -0.0886 | 57671 | +0.15% | +1.76% | -1.61% |
| 10 | d_Market Cap | -0.0791 | 29488 | +0.65% | +3.30% | -2.65% |
| 11 | d_Performance (Quarter) | -0.0730 | 54515 | +0.35% | +2.07% | -1.73% |
| 12 | n_pos | -0.0540 | 69263 | n/a | n/a | n/a |
| 13 | upside_pct_lvl | +0.0425 | 27900 | +1.31% | -0.01% | +1.32% |
| 14 | upside_pct | +0.0425 | 27900 | +1.31% | -0.01% | +1.32% |
| 15 | Sales Year Over Year TTM | +0.0414 | 27278 | +1.77% | +2.06% | -0.29% |
| 16 | Sales Growth Quarter Over Quarter | +0.0411 | 28524 | +0.86% | +1.72% | -0.86% |
| 17 | Performance (YTD) | +0.0402 | 69208 | +0.29% | +2.38% | -2.08% |
| 18 | technical_score | -0.0378 | 69263 | +0.35% | +3.99% | -3.64% |
| 19 | 50-Day Simple Moving Average | -0.0377 | 69263 | +0.21% | +2.49% | -2.29% |
| 20 | Relative Strength Index (14) | -0.0347 | 68627 | n/a | n/a | n/a |
| 21 | Analyst Recom | -0.0321 | 27548 | n/a | n/a | n/a |
| 22 | Short Float | +0.0305 | 34604 | n/a | n/a | n/a |
| 23 | d_Institutional Ownership | +0.0297 | 29232 | +0.49% | +0.91% | -0.42% |
| 24 | Market Cap | +0.0293 | 35404 | n/a | n/a | n/a |
| 25 | Price | +0.0283 | 69263 | n/a | n/a | n/a |

## 3. Factor combinations (sign quadrants)

Among stronger single factors: A↑B↑ / A↑B↓ / A↓B↑ / A↓B↓. **Score** = |mean_fwd| × √n (ranking aid only).

| Rank | Combination | n | Mean fwd | % up | % down | Score |
|------|-------------|---|----------|------|--------|-------|
| 1 | d_Relative Strength Index (14)↓ & d_200-Day Simple Moving Average↓ | 21205 | +2.29% | 57.7% | 37.7% | 3.332 |
| 2 | d_Relative Strength Index (14)↓ & d_50-Day Simple Moving Average↓ | 20731 | +2.24% | 57.5% | 37.9% | 3.222 |
| 3 | d_200-Day Simple Moving Average↓ & d_50-Day Simple Moving Average↓ | 21929 | +2.12% | 57.3% | 37.4% | 3.141 |
| 4 | d_Relative Strength Index (14)↓ & d_20-Day Simple Moving Average↓ | 20612 | +2.15% | 57.6% | 37.7% | 3.087 |
| 5 | d_200-Day Simple Moving Average↓ & d_20-Day Simple Moving Average↓ | 21754 | +2.05% | 57.5% | 37.3% | 3.020 |
| 6 | d_Relative Strength Index (14)↓ & d_Performance (Week)↓ | 17902 | +2.24% | 58.1% | 37.3% | 2.998 |
| 7 | d_200-Day Simple Moving Average↓ & d_Performance (Week)↓ | 18458 | +2.17% | 58.2% | 37.1% | 2.943 |
| 8 | d_50-Day Simple Moving Average↓ & d_20-Day Simple Moving Average↓ | 21925 | +1.96% | 57.1% | 37.6% | 2.896 |
| 9 | d_Performance (Week)↓ & d_20-Day Simple Moving Average↓ | 19304 | +2.04% | 57.1% | 38.2% | 2.828 |
| 10 | d_50-Day Simple Moving Average↓ & d_Performance (Week)↓ | 18411 | +2.08% | 57.7% | 37.4% | 2.819 |
| 11 | d_Relative Strength Index (14)↓ & d_Performance (YTD)↓ | 21932 | +1.80% | 57.3% | 38.0% | 2.671 |
| 12 | d_Relative Strength Index (14)↓ & true_ret↓ | 21507 | +1.78% | 57.5% | 38.1% | 2.604 |
| 13 | d_200-Day Simple Moving Average↓ & d_Performance (YTD)↓ | 21299 | +1.76% | 57.7% | 37.7% | 2.574 |
| 14 | d_200-Day Simple Moving Average↓ & true_ret↓ | 21010 | +1.72% | 57.8% | 37.8% | 2.498 |
| 15 | true_ret↓ & d_20-Day Simple Moving Average↓ | 20404 | +1.74% | 57.7% | 37.8% | 2.490 |
| 16 | d_Performance (Week)↓ & d_Performance (YTD)↓ | 17888 | +1.84% | 58.1% | 37.3% | 2.465 |
| 17 | d_50-Day Simple Moving Average↓ & d_Performance (YTD)↓ | 20804 | +1.70% | 57.5% | 37.8% | 2.457 |
| 18 | true_ret↓ & d_50-Day Simple Moving Average↓ | 20551 | +1.68% | 57.7% | 37.9% | 2.407 |
| 19 | true_ret↓ & d_Performance (Week)↓ | 17586 | +1.78% | 58.3% | 37.4% | 2.367 |
| 20 | true_ret↓ & d_Performance (YTD)↓ | 21635 | +1.59% | 57.5% | 38.1% | 2.332 |

## Notes

- With few signal dates, treat rankings as **exploratory**.
- `d_*` = day-over-day delta on the signal pair; bare names = levels.
- JSON: `03_scoreboard/predictive_audit_1d.json`

# Predictive audit — horizon **2d**

Generated: 2026-08-15T04:32:53.640129-04:00
Signal dates pooled: **5** (`2026-08-06, 2026-08-07, 2026-08-10, 2026-08-11, 2026-08-12`)

## 1. Prediction accuracy (composite `total_score`, full universe)

Rule: score > +2 → expect UP; score < −2 → expect DOWN; else neutral.

| Metric | Value |
|--------|-------|
| Names graded | 57671 |
| Actionable (|score|>2) | 15652 |
| **Accuracy (actionable)** | **45.8%** |
| Long accuracy | 50.3% |
| Short accuracy | 40.9% |
| Spearman IC(score, fwd) | -0.0063 |

### Per signal date

| Signal | n | Actionable | Accuracy | Long | Short | IC |
|--------|---|------------|----------|------|-------|----|
| 2026-08-06 | 11518 | 314 | 54.8% | 60.2% | 26.0% | +0.0636 |
| 2026-08-07 | 11525 | 4349 | 47.2% | 46.0% | 49.7% | -0.0242 |
| 2026-08-10 | 11533 | 4490 | 41.6% | 51.4% | 35.7% | -0.0596 |
| 2026-08-11 | 11543 | 3818 | 46.9% | 51.8% | 40.7% | +0.0174 |
| 2026-08-12 | 11552 | 2681 | 48.0% | 54.8% | 42.8% | +0.0520 |

## 2. Top correlating factors (pooled across dates)

IC = Spearman(factor, forward return). Ranked by |IC|. Spread = mean fwd when factor>0 minus mean fwd when factor<0.

| Rank | Factor | IC | n | Mean fwd if ↑ | Mean fwd if ↓ | Spread |
|------|--------|----|---|---------------|---------------|--------|
| 1 | d_Performance (Week) | -0.0948 | 45909 | +0.90% | +2.27% | -1.37% |
| 2 | d_Relative Strength Index (14) | -0.0867 | 45720 | +0.41% | +3.44% | -3.03% |
| 3 | d_200-Day Simple Moving Average | -0.0835 | 46118 | +0.61% | +3.05% | -2.43% |
| 4 | d_50-Day Simple Moving Average | -0.0782 | 46118 | +0.69% | +2.93% | -2.24% |
| 5 | true_ret | -0.0741 | 46118 | +0.42% | +3.00% | -2.58% |
| 6 | d_Performance (YTD) | -0.0736 | 46087 | +0.42% | +2.81% | -2.39% |
| 7 | d_Price | -0.0723 | 46118 | +0.42% | +3.00% | -2.58% |
| 8 | d_20-Day Simple Moving Average | -0.0704 | 46118 | +0.71% | +2.79% | -2.08% |
| 9 | Performance (YTD) | +0.0670 | 57630 | +0.52% | +4.51% | -3.99% |
| 10 | d_Forward P/E | -0.0662 | 12203 | +0.29% | +0.72% | -0.43% |
| 11 | d_Performance (Quarter) | -0.0606 | 43594 | +0.74% | +2.95% | -2.20% |
| 12 | Sales Year Over Year TTM | +0.0555 | 22720 | +3.60% | +3.61% | -0.01% |
| 13 | 200-Day Simple Moving Average | +0.0555 | 57671 | +0.46% | +4.46% | -4.00% |
| 14 | Beta | +0.0549 | 39022 | +1.65% | +3.62% | -1.97% |
| 15 | Sales Growth Quarter Over Quarter | +0.0506 | 23752 | +1.53% | +2.89% | -1.35% |
| 16 | d_Market Cap | -0.0453 | 23585 | +0.97% | +4.87% | -3.90% |
| 17 | Price | +0.0448 | 57671 | n/a | n/a | n/a |
| 18 | Short Float | +0.0377 | 28807 | n/a | n/a | n/a |
| 19 | Volatility (Month) | +0.0373 | 45412 | n/a | n/a | n/a |
| 20 | Market Cap | +0.0362 | 29488 | n/a | n/a | n/a |
| 21 | d_Institutional Ownership | +0.0347 | 23384 | +0.89% | +1.41% | -0.52% |
| 22 | upside_pct_lvl | +0.0321 | 23246 | +2.16% | +0.02% | +2.14% |
| 23 | upside_pct | +0.0321 | 23246 | +2.16% | +0.01% | +2.14% |
| 24 | Analyst Recom | -0.0318 | 22952 | n/a | n/a | n/a |
| 25 | Institutional Transactions | +0.0257 | 25340 | +5.90% | +2.46% | +3.44% |

## 3. Factor combinations (sign quadrants)

Among stronger single factors: A↑B↑ / A↑B↓ / A↓B↑ / A↓B↓. **Score** = |mean_fwd| × √n (ranking aid only).

| Rank | Combination | n | Mean fwd | % up | % down | Score |
|------|-------------|---|----------|------|--------|-------|
| 1 | d_Relative Strength Index (14)↓ & d_200-Day Simple Moving Average↓ | 17784 | +3.28% | 63.5% | 33.6% | 4.380 |
| 2 | d_Relative Strength Index (14)↓ & d_50-Day Simple Moving Average↓ | 17418 | +3.23% | 63.5% | 33.6% | 4.260 |
| 3 | d_Relative Strength Index (14)↓ & d_20-Day Simple Moving Average↓ | 17311 | +3.24% | 63.4% | 33.6% | 4.257 |
| 4 | d_200-Day Simple Moving Average↓ & d_20-Day Simple Moving Average↓ | 18255 | +3.08% | 64.0% | 32.7% | 4.167 |
| 5 | d_200-Day Simple Moving Average↓ & d_50-Day Simple Moving Average↓ | 18423 | +3.06% | 63.9% | 32.8% | 4.154 |
| 6 | d_50-Day Simple Moving Average↓ & d_20-Day Simple Moving Average↓ | 18437 | +2.99% | 63.9% | 32.9% | 4.066 |
| 7 | d_Relative Strength Index (14)↓ & true_ret↓ | 18013 | +3.02% | 63.0% | 34.2% | 4.056 |
| 8 | d_Relative Strength Index (14)↓ & d_Price↓ | 18013 | +3.02% | 63.0% | 34.2% | 4.056 |
| 9 | true_ret↓ & d_Price↓ | 18159 | +3.00% | 63.0% | 34.2% | 4.041 |
| 10 | d_Performance (Week)↓ & d_Relative Strength Index (14)↓ | 15330 | +3.26% | 64.0% | 33.1% | 4.032 |
| 11 | d_Performance (Week)↓ & d_200-Day Simple Moving Average↓ | 15842 | +3.15% | 64.9% | 32.1% | 3.971 |
| 12 | d_Performance (Week)↓ & d_50-Day Simple Moving Average↓ | 15817 | +3.08% | 64.7% | 32.3% | 3.870 |
| 13 | d_Performance (Week)↓ & d_20-Day Simple Moving Average↓ | 16589 | +3.00% | 64.1% | 33.0% | 3.862 |
| 14 | d_Relative Strength Index (14)↓ & d_Performance (YTD)↓ | 18372 | +2.83% | 62.9% | 34.1% | 3.837 |
| 15 | d_200-Day Simple Moving Average↓ & true_ret↓ | 17609 | +2.80% | 63.6% | 33.7% | 3.714 |
| 16 | d_200-Day Simple Moving Average↓ & d_Price↓ | 17609 | +2.80% | 63.6% | 33.7% | 3.714 |
| 17 | true_ret↓ & d_Performance (YTD)↓ | 18117 | +2.74% | 63.1% | 34.2% | 3.695 |
| 18 | d_Performance (YTD)↓ & d_Price↓ | 18117 | +2.74% | 63.1% | 34.2% | 3.695 |
| 19 | true_ret↓ & d_20-Day Simple Moving Average↓ | 17128 | +2.79% | 63.6% | 33.7% | 3.658 |
| 20 | d_Price↓ & d_20-Day Simple Moving Average↓ | 17128 | +2.79% | 63.6% | 33.7% | 3.658 |

## Notes

- With few signal dates, treat rankings as **exploratory**.
- `d_*` = day-over-day delta on the signal pair; bare names = levels.
- JSON: `03_scoreboard/predictive_audit_2d.json`

# Suggestion check — signal **2026-08-06**

## What this is (not the scan.md Ret% table)

- **Signal as-of:** **2026-08-06** — scores ranked using only data through this day.
- **TOP_LONG:** highest `total_score` → we *expected* price **up** after the signal.
- **BOTTOM_SHORT:** lowest `total_score` → we *expected* price **down** after the signal.
- **Hit:** long and forward return > 0, or short and forward return < 0.
- **fwd** uses **entry = Price @ signal**, **exit = Price @ prediction day** (later snapshot). This is *after* the signal — not the same-day Ret% on the scan.

## Summary by horizon

| Horizon | Prediction day | Top hit rate | Top mean fwd | Bottom hit rate | Bottom mean fwd |
|---------|----------------|--------------|--------------|-----------------|-----------------|
| 1d | 2026-08-07 | 80.0% (n=15) | +4.06% | 20.0% (n=10) | +1.09% |
| 2d | 2026-08-10 | 53.3% (n=15) | +2.90% | 20.0% (n=10) | +2.94% |
| 3d | 2026-08-11 | 66.7% (n=15) | +4.74% | 40.0% (n=10) | -0.34% |

## Detail — horizon 1d (prediction day **2026-08-07**)

### Top scores (expected UP)

| Ticker | Score | Entry @ signal | Exit @ pred day | fwd | Expected | Hit? |
|---|---|---|---|---|---|---|
| FIP | +4.0 | 4.05 | 4.27 | +5.43% | UP | **YES** |
| CBAT | +4.0 | 0.6 | 0.65 | +8.33% | UP | **YES** |
| LIDR | +4.0 | 1.22 | 1.32 | +8.20% | UP | **YES** |
| USGO | +4.0 | 8.47 | 8.64 | +2.01% | UP | **YES** |
| AEVA | +3.3 | 25.26 | 26.62 | +5.38% | UP | **YES** |
| MDU | +3.3 | 20.76 | 20.55 | -1.01% | UP | **NO** |
| AMRC | +3.2 | 25.55 | 25.65 | +0.39% | UP | **YES** |
| ALB | +3.2 | 125.42 | 131.11 | +4.54% | UP | **YES** |
| XE | +3.2 | 20.82 | 22.65 | +8.79% | UP | **YES** |
| AIRJ | +3.2 | 5.59 | 5.92 | +5.90% | UP | **YES** |
| NBIS | +3.2 | 189.88 | 187.97 | -1.01% | UP | **NO** |
| MTSI | +3.2 | 301.64 | 310.82 | +3.04% | UP | **YES** |
| CCLD | +3.0 | 2.32 | 2.63 | +13.36% | UP | **YES** |
| GTIM | +3.0 | 1.42 | 1.47 | +3.52% | UP | **YES** |
| ZTS | +3.0 | 77.27 | 72.66 | -5.97% | UP | **NO** |

### Bottom scores (expected DOWN)

| Ticker | Score | Entry @ signal | Exit @ pred day | fwd | Expected | Hit? |
|---|---|---|---|---|---|---|
| CAR | -2.8 | 138.35 | 142.18 | +2.77% | DOWN | **NO** |
| BZFD | -2.8 | 1.13 | 1.16 | +2.65% | DOWN | **NO** |
| HTT | -2.8 | 2.48 | 2.52 | +1.61% | DOWN | **NO** |
| HIW | -2.8 | 31.48 | 31.45 | -0.10% | DOWN | **YES** |
| KG | -2.8 | 8.91 | 8.82 | -1.01% | DOWN | **YES** |
| HERZ | -2.8 | 15.77 | 15.78 | +0.06% | DOWN | **NO** |
| TIL | -2.8 | 7.28 | 7.41 | +1.79% | DOWN | **NO** |
| SGLY | -3.2 | 6.68 | 6.87 | +2.84% | DOWN | **NO** |
| APGE | -3.2 | 134.49 | 134.84 | +0.26% | DOWN | **NO** |
| EA | -3.2 | 209.7 | 209.7 | +0.00% | DOWN | **NO** |

CSV: `data/attribution/2026-08-06_suggestion_check.csv`

# Suggestion check — signal **2026-08-07**

## What this is (not the scan.md Ret% table)

- **Signal as-of:** **2026-08-07** — scores ranked using only data through this day.
- **TOP_LONG:** highest `total_score` → we *expected* price **up** after the signal.
- **BOTTOM_SHORT:** lowest `total_score` → we *expected* price **down** after the signal.
- **Hit:** long and forward return > 0, or short and forward return < 0.
- **fwd** uses **entry = Price @ signal**, **exit = Price @ prediction day** (later snapshot). This is *after* the signal — not the same-day Ret% on the scan.

## Summary by horizon

| Horizon | Prediction day | Top hit rate | Top mean fwd | Bottom hit rate | Bottom mean fwd |
|---------|----------------|--------------|--------------|-----------------|-----------------|
| 1d | 2026-08-10 | 53.3% (n=15) | -0.26% | 50.0% (n=10) | +0.61% |
| 2d | 2026-08-11 | 66.7% (n=15) | +2.05% | 40.0% (n=10) | +2.35% |

## Detail — horizon 1d (prediction day **2026-08-10**)

### Top scores (expected UP)

| Ticker | Score | Entry @ signal | Exit @ pred day | fwd | Expected | Hit? |
|---|---|---|---|---|---|---|
| MP | +9.0 | 51.11 | 54.66 | +6.95% | UP | **YES** |
| NRGV | +9.0 | 3.49 | 3.34 | -4.30% | UP | **NO** |
| TMC | +9.0 | 4.57 | 4.43 | -3.06% | UP | **NO** |
| OKLO | +8.2 | 48.42 | 44.49 | -8.12% | UP | **NO** |
| LIDR | +8.2 | 1.32 | 1.3 | -1.52% | UP | **NO** |
| ALOY | +8.2 | 12.27 | 12.98 | +5.79% | UP | **YES** |
| FIP | +8.2 | 4.27 | 4.3 | +0.70% | UP | **YES** |
| ALM | +8.2 | 14.18 | 13.7 | -3.39% | UP | **NO** |
| UUUU | +8.2 | 14.14 | 14.29 | +1.06% | UP | **YES** |
| USAR | +8.2 | 19.33 | 19.04 | -1.50% | UP | **NO** |
| BVC | +8.0 | 12.55 | 12.83 | +2.23% | UP | **YES** |
| CELH | +8.0 | 27.77 | 27.21 | -2.02% | UP | **NO** |
| DKNG | +8.0 | 24.03 | 24.27 | +1.00% | UP | **YES** |
| AAUC | +8.0 | 21.78 | 22.22 | +2.02% | UP | **YES** |
| SSP | +8.0 | 3.32 | 3.33 | +0.30% | UP | **YES** |

### Bottom scores (expected DOWN)

| Ticker | Score | Entry @ signal | Exit @ pred day | fwd | Expected | Hit? |
|---|---|---|---|---|---|---|
| CRCT | -7.5 | 5.84 | 5.9 | +1.03% | DOWN | **NO** |
| PLTZ | -7.5 | 10.25 | 9.85 | -3.90% | DOWN | **YES** |
| CABR | -7.5 | 1.34 | 1.44 | +7.46% | DOWN | **NO** |
| ODC | -7.5 | 92.79 | 88.02 | -5.14% | DOWN | **YES** |
| DUST | -7.5 | 41.75 | 41.13 | -1.49% | DOWN | **YES** |
| FG | -7.8 | 27.67 | 27.08 | -2.13% | DOWN | **YES** |
| MI | -7.8 | 7.41 | 7.7 | +3.91% | DOWN | **NO** |
| DWSN | -7.8 | 4.35 | 4.23 | -2.76% | DOWN | **YES** |
| SAIH | -8.0 | 20.82 | 22.5 | +8.07% | DOWN | **NO** |
| ZTG | -8.0 | 9.2 | 9.3 | +1.09% | DOWN | **NO** |

CSV: `data/attribution/2026-08-07_suggestion_check.csv`

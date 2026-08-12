# Suggestion check — signal **2026-08-10**

## What this is (not the scan.md Ret% table)

- **Signal as-of:** **2026-08-10** — scores ranked using only data through this day.
- **TOP_LONG:** highest `total_score` → we *expected* price **up** after the signal.
- **BOTTOM_SHORT:** lowest `total_score` → we *expected* price **down** after the signal.
- **Hit:** long and forward return > 0, or short and forward return < 0.
- **fwd** uses **entry = Price @ signal**, **exit = Price @ prediction day** (later snapshot). This is *after* the signal — not the same-day Ret% on the scan.

## Summary by horizon

| Horizon | Prediction day | Top hit rate | Top mean fwd | Bottom hit rate | Bottom mean fwd |
|---------|----------------|--------------|--------------|-----------------|-----------------|
| 1d | 2026-08-11 | 53.3% (n=15) | +0.26% | 40.0% (n=10) | +3.51% |

## Detail — horizon 1d (prediction day **2026-08-11**)

### Top scores (expected UP)

| Ticker | Score | Entry @ signal | Exit @ pred day | fwd | Expected | Hit? |
|---|---|---|---|---|---|---|
| ACHR | +8.5 | 6.26 | 6.79 | +8.47% | UP | **YES** |
| ATCX | +8.2 | 3.14 | 3.2 | +1.91% | UP | **YES** |
| MP | +8.2 | 54.66 | 55.24 | +1.06% | UP | **YES** |
| LAR | +8.2 | 7.1 | 6.65 | -6.34% | UP | **NO** |
| ALOY | +8.2 | 12.98 | 12.75 | -1.77% | UP | **NO** |
| SLI | +8.2 | 2.53 | 2.45 | -3.16% | UP | **NO** |
| SLSR | +8.2 | 8.25 | 8.13 | -1.45% | UP | **NO** |
| PDS | +8.0 | 81.39 | 83.02 | +2.00% | UP | **YES** |
| GLBS | +8.0 | 3.39 | 3.68 | +8.55% | UP | **YES** |
| DDC | +8.0 | 0.55 | 0.49 | -10.91% | UP | **NO** |
| PPBT | +8.0 | 1.5 | 1.55 | +3.33% | UP | **YES** |
| SAFX | +8.0 | 0.45 | 0.45 | +0.00% | UP | **NO** |
| CRC | +8.0 | 53.75 | 54.13 | +0.71% | UP | **YES** |
| NSLR | +8.0 | 10.33 | 10.64 | +3.00% | UP | **YES** |
| HNRG | +8.0 | 15.88 | 15.64 | -1.51% | UP | **NO** |

### Bottom scores (expected DOWN)

| Ticker | Score | Entry @ signal | Exit @ pred day | fwd | Expected | Hit? |
|---|---|---|---|---|---|---|
| FEDU | -7.8 | 7.5 | 6.91 | -7.87% | DOWN | **YES** |
| UAN | -7.8 | 117.01 | 120.17 | +2.70% | DOWN | **NO** |
| AFL | -7.8 | 121.94 | 121.07 | -0.71% | DOWN | **YES** |
| PSMT | -7.8 | 168.81 | 172.86 | +2.40% | DOWN | **NO** |
| WPP | -8.2 | 26.69 | 27.04 | +1.31% | DOWN | **NO** |
| NYC | -8.5 | 8.23 | 8.0 | -2.79% | DOWN | **YES** |
| TISI | -8.5 | 16.55 | 22.71 | +37.22% | DOWN | **NO** |
| VSTS | -8.5 | 13.87 | 13.88 | +0.07% | DOWN | **NO** |
| OPHC | -9.0 | 8.92 | 9.2 | +3.14% | DOWN | **NO** |
| HNST | -9.0 | 5.23 | 5.21 | -0.38% | DOWN | **YES** |

CSV: `data/attribution/2026-08-10_suggestion_check.csv`

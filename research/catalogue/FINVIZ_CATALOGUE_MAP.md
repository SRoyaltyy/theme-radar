# Finviz / Elite → Stock Direction Tell Catalogue map
**Owner:** Theme Radar · **Clock:** B only (09:30-knowable = prior session after-close / stamped pre-open) · **Status:** candidate predictors, not KEEP edges · Research-only

Sources: `SRoyaltyy/theme-radar` daily `data/snapshots/{date}.raw.csv` (~150 cols). Elite extended-hours fields exist on snapshot (`After-Hours*`) but are **session-T after-close outcomes** unless separately stamped pre-09:30 — treat AH as Clock A / after-T unless a pre-open Elite pull is archived.

## Legend
- **HAVE:** field present on timestamped daily snapshot (Clock B via T−1)
- **CALC:** can derive from successive snapshots (still Clock B if only past closes)
- **NEED:** requires another source or pre-09:30 Elite archive we do not yet keep
- **VOL/CROWD:** useful for risk/veto, not direction KEEP alone

---

## Priority for panel-feed / catalogue tests (Theme Radar lane)

### Family 5 — Volume & participation
| Tell | Finviz fields | Status | Clock B note |
|------|---------------|--------|--------------|
| RelVol spike | `Relative Volume`, `Average Volume`, `Volume` | HAVE | T−1 RelVol knowable at open T |
| Quiet vs loud day | `Relative Volume`, `Volatility (Week/Month)` | HAVE | |
| Float turnover | `Volume`, `Shares Float`, `Float %` | CALC | Vol/Float |
| High activity little progress | `Relative Volume` + `Change`/`ATR` | CALC | often VOL/CROWD |

### Family 7 — Premarket & overnight (gap)
| Tell | Finviz fields | Status | Clock B note |
|------|---------------|--------|--------------|
| Overnight gap | `Gap`, `Open`, `Prev Close` | HAVE on T snapshot | **Gap on T is after open of T** — for open-T entry use T−1 close only; for *next* open after T close, Gap_T is Clock A. Pre-09:30 Elite gap = NEED archive |
| AH move | `After-Hours Close/Change/Volume` | HAVE on T | after-T unless pre-open scrape |
| Sustained vs fade | Gap vs `Change from Open` | HAVE | after-T diagnostic |

### Family 1–2 — Trend / momentum (price history)
| Tell | Finviz fields | Status |
|------|---------------|--------|
| vs SMA | `20/50/200-Day Simple Moving Average`, `Price` | HAVE |
| HH/HL proxies | `50-Day High/Low`, `52-Week High/Low`, Performance* | HAVE/CALC |
| RSI / extension | `Relative Strength Index (14)`, Performance (Week/Month) | HAVE |
| ATR compression | `Average True Range`, `Volatility (Week/Month)` | HAVE |

### Family 6 — Relative strength & breadth
| Tell | Finviz fields | Status |
|------|---------------|--------|
| Sector/Industry tag | `Sector`, `Industry`, `Sector/Theme` | HAVE |
| Peer RS | Performance* cross-section within Sector | CALC on full snapshot |
| Index membership | `Index` | HAVE |

### Family 10–12 — Earnings / guidance / valuation-quality
| Tell | Finviz fields | Status |
|------|---------------|--------|
| Surprises | `EPS Surprise`, `Revenue Surprise` | HAVE | as-of stamp = snapshot day; earnings timing via `Earnings Date` |
| Growth | EPS/Sales growth YoY QoQ fields | HAVE |
| Valuation | `P/E`,`Forward P/E`,`P/S`,`P/B`,`P/FCF`,`EV/*` | HAVE |
| Quality | `ROA`,`ROE`,`ROIC`, margins, `Current/Quick Ratio` | HAVE |

### Family 13–14 — Solvency / capital structure
| Tell | Finviz fields | Status |
|------|---------------|--------|
| Leverage | `Total Debt/Equity`, `LT Debt/Equity` | HAVE |
| Cash | `Cash/sh`, `P/Cash` | HAVE |
| Dividend/payout | Dividend* fields | HAVE |
| Issuance / converts / lockups | — | NEED (news/filings) |

### Family 16–17 — Insider / institutional / short
| Tell | Finviz fields | Status |
|------|---------------|--------|
| Insider txn / own | `Insider Transactions`, `Insider Ownership` | HAVE | lag in Finviz refresh — treat as soft Clock B |
| Inst own / txn | `Institutional Ownership`, `Institutional Transactions` | HAVE |
| Short float / ratio / interest | `Short Float`, `Short Ratio`, `Short Interest` | HAVE | VOL/CROWD + borrow feasibility NEED |
| Shortable flag | `Shortable` | HAVE | feasibility flag |

### Family 15 / 22 — Catalysts / attention
| Tell | Finviz fields | Status |
|------|---------------|--------|
| Headline | `News Title`, `News Time`, `News URL`, `Daily Digest` | HAVE | **digest timing** may be stale; prefer fullscan news clocks |
| Earnings calendar | `Earnings Date` | HAVE |

### Family 8–9 — Intraday / auction
| Tell | Finviz fields | Status |
|------|---------------|--------|
| Minute/hour Performance*, Trades | many `Performance (N Minute/Hour)`, `Trades` | HAVE on dump | **NOT Clock B for 09:30 fill** — veto from open-entry tests |

### Family 18 — Options
| Tell | Finviz | Status |
|------|--------|--------|
| Optionable flag | `Optionable` | HAVE | skew/dealer NEED |

### Family 21 — Flows (ETF rows)
| Tell | Finviz ETF cols | Status |
|------|-----------------|--------|
| Net flows | `Net Flows (*)` | HAVE on ETF Type rows | mostly ETF universe; equity panel usually drops ETF Type |

---

## What Theme Radar will emit next (no ask)
1. **Clock-B gap+RelVol opportunity-set CSV** per morning T: from snapshot **T−1** — liquid midcap filter, flags `rvol_ge_X`, `|gap|_ge_Y` using **prior** fields only (for open T).  
2. Optional ownership/short/fund overlays from same T−1 row.  
3. Explicit exclusion of minute/hour Performance* and same-day Gap from open-T features.

Wire into fullscan aux panel = Taskforce after #277 remine proves multi-src. Theme Radar does not edit fullscan.

## Gaps / need-source (for Taskforce map)
- Timestamped **pre-09:30 Elite** gap/AH archive (homepage digest close/pre already separate in fullscan)
- Borrow fee / locate inventory (Family 17 feasibility)
- Options skew / IV term (Family 18)
- True peer basket RS beyond Sector tag (can CALC crude; NEED better peer map)
- Filing-grade issuance/convert/lockup events (Family 14)


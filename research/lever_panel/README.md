# Finviz lever panel, knowable by 09:30 ET (research only)

This is a frozen table for the fullscan lever search (Trading Bot Taskforce). Each row is one stock on one trading morning. It holds only what was already known and saved in this repo before that morning's 09:30 ET open.

## The clock rule

- `trade_date` is the morning the row can be used. `snapshot_date` is the **previous trading day**. Every value comes from the Finviz snapshot taken **after that day's 16:00 ET close** and **before 09:30 ET on `trade_date`**.
- **Values from the close of `trade_date` itself are never used.**
- `scrape_ts_utc` is the export time, in UTC. It comes from the first available source in this list:
  1. the snapshot's own `scrape_ts` column (only on 2026-09-24 and 2026-09-25);
  2. otherwise, the fetch time recorded in `data/snapshots/manifest.json` (`runs[].stamp`, in ET). This is used only when that run's archive copy has exactly the same sha256 as the dated file on disk;
  3. otherwise, the git commit time of the dated file. This is how `src/history_guard.close_is_in` handles old files. It was needed only for snapshot 2026-08-06, which feeds trade_date 2026-08-07, before the search window. A commit time is an upper bound on the scrape time: it proves "before 09:30" but only suggests "after 16:00" (the commit was at 20:57 ET).
  `scrape_ts_source` records which source each row used.
- `snapshot_commit_ts_utc` is when that snapshot version was committed. It is always before 09:30 ET on `trade_date`.
- Theme Radar's own outputs for `snapshot_date` are taken from the newest git version committed **before 09:30 ET on `trade_date`**. `tr_*_commit_ts_utc` records that time. If no version existed by then, the columns are left empty (not filled). Every version used is identical to today's HEAD.
- **Excluded:** anything that depends on later prices. That means `data/labels/*` (fwd returns), `data/attribution/*` (ICs graded against forward labels), suggestion checks, and outcome grades. Free-text news fields (`News Title`, `Daily Digest`, `News URL`) are also left out. `News Time` is kept.

## Files

The panel compressed to 127.3 MB, which is over the 90 MB limit, so it is **split by trade_date month**. Both parts have the same columns; stack them to get the full panel. The gzip is deterministic (mtime=0), so a rebuild from the same HEAD gives the same sha256.

| file | trade dates | rows | bytes | sha256 |
|---|---|---|---|---|
| `finviz_panel_asof0930_2026-08.csv.gz` | 2026-08-07 … 2026-08-31 | 185,474 | 55,836,833 | `c8977b8eea8e74115899e9d4cc04d5b4ea67490376d972905781eb8e1aeb6459` |
| `finviz_panel_asof0930_2026-09.csv.gz` | 2026-09-01 … 2026-09-28 | 221,175 | 71,452,629 | `cbf35da9e1587703059abd9ff77525a1047c67a91edc3276ca93db4cd8669c16` |

Also included: `panel_meta.json` (per-date provenance: commits, scrape sources, per-family status), `build_lever_panel.py` (builder), `check_lever_panel.py` (clock check).

```
python -m research.lever_panel.build_lever_panel   # rebuild (reads git history)
python -m research.lever_panel.check_lever_panel   # clock check, exit 0 = pass
```

## Date range and counts

- Trade dates run from **2026-08-07 to 2026-09-28**: 35 dates with data and 406,649 rows. There is one row per (Ticker, trade_date), so rows equal tickers on every date.
- Tickers per date: median **11,629**, min 11,543, max 11,679.
- Lever-search windows: search 08-13 … 09-04, check 09-05 … 09-11 (trade dates 09-08 … 09-11), one look 09-14 … 09-25. All of these trade dates are present. Note that 08-28 is inside the search window and is skipped.

### Skipped dates (no prior-close snapshot; NOT filled)

| trade_date | missing snapshot | note |
|---|---|---|
| 2026-08-06 | 2026-08-05 | The earliest snapshot is 2026-08-06, so no prior close exists. |
| 2026-08-28 | 2026-08-27 | No `2026-08-27.csv` exists. An archived run from 2026-08-28 00:26 ET, holding 08-27 data (`archive/2026-08-28_20260828_002624.csv`), was later replaced. That run is not a dated snapshot, so it is not used. |

Theme Radar output coverage (empty columns, not filled): trade_date 2026-08-07 has no `tr1d_/tr1w_/tr1m_/trf_/seg_` values, because the 08-06 scores were committed after 09:30 ET on 08-07. `seg_` is also empty on 08-10 and 08-11. `trc_` (composite) starts on trade_date 2026-08-13, because composite began with snapshot 08-12.

| trade_date | snapshot_date | rows | tickers |
|---|---|---|---|
| 2026-08-07 | 2026-08-06 | 11,555 | 11,555 |
| 2026-08-10 | 2026-08-07 | 11,560 | 11,560 |
| 2026-08-11 | 2026-08-10 | 11,543 | 11,543 |
| 2026-08-12 | 2026-08-11 | 11,554 | 11,554 |
| 2026-08-13 | 2026-08-12 | 11,568 | 11,568 |
| 2026-08-14 | 2026-08-13 | 11,579 | 11,579 |
| 2026-08-17 | 2026-08-14 | 11,586 | 11,586 |
| 2026-08-18 | 2026-08-17 | 11,573 | 11,573 |
| 2026-08-19 | 2026-08-18 | 11,584 | 11,584 |
| 2026-08-20 | 2026-08-19 | 11,600 | 11,600 |
| 2026-08-21 | 2026-08-20 | 11,612 | 11,612 |
| 2026-08-24 | 2026-08-21 | 11,623 | 11,623 |
| 2026-08-25 | 2026-08-24 | 11,617 | 11,617 |
| 2026-08-26 | 2026-08-25 | 11,624 | 11,624 |
| 2026-08-27 | 2026-08-26 | 11,637 | 11,637 |
| 2026-08-31 | 2026-08-28 | 11,659 | 11,659 |
| 2026-09-01 | 2026-08-31 | 11,631 | 11,631 |
| 2026-09-02 | 2026-09-01 | 11,635 | 11,635 |
| 2026-09-03 | 2026-09-02 | 11,640 | 11,640 |
| 2026-09-04 | 2026-09-03 | 11,643 | 11,643 |
| 2026-09-08 | 2026-09-04 | 11,646 | 11,646 |
| 2026-09-09 | 2026-09-08 | 11,608 | 11,608 |
| 2026-09-10 | 2026-09-09 | 11,613 | 11,613 |
| 2026-09-11 | 2026-09-10 | 11,629 | 11,629 |
| 2026-09-14 | 2026-09-11 | 11,632 | 11,632 |
| 2026-09-15 | 2026-09-14 | 11,616 | 11,616 |
| 2026-09-16 | 2026-09-15 | 11,633 | 11,633 |
| 2026-09-17 | 2026-09-16 | 11,640 | 11,640 |
| 2026-09-18 | 2026-09-17 | 11,650 | 11,650 |
| 2026-09-21 | 2026-09-18 | 11,654 | 11,654 |
| 2026-09-22 | 2026-09-21 | 11,642 | 11,642 |
| 2026-09-23 | 2026-09-22 | 11,647 | 11,647 |
| 2026-09-24 | 2026-09-23 | 11,665 | 11,665 |
| 2026-09-25 | 2026-09-24 | 11,672 | 11,672 |
| 2026-09-28 | 2026-09-25 | 11,679 | 11,679 |

## Fields (237 columns)

**Keys / clock (9):** `trade_date`, `snapshot_date`, `scrape_ts_utc`, `scrape_ts_source`, `snapshot_commit_ts_utc`, `tr_scores_commit_ts_utc`, `tr_features_commit_ts_utc`, `tr_composite_commit_ts_utc`, `tr_segments_commit_ts_utc`

**Finviz snapshot fields (50, original names):** `Ticker`, `Company`, `Industry`, `Sector`, `Country`, `Exchange`, `Index`, `News Time`, `Market Cap`, `Price`, `Average Volume`, `Short Float`, `Short Ratio`, `Institutional Transactions`, `Institutional Ownership`, `Insider Transactions`, `Insider Ownership`, `Analyst Recom`, `Target Price`, `Forward P/E`, `EV/Sales`, `PEG`, `Performance (Week)`, `Performance (Month)`, `Performance (Quarter)`, `Performance (Half Year)`, `Performance (YTD)`, `Performance (Year)`, `Relative Volume`, `Relative Strength Index (14)`, `Sales Year Over Year TTM`, `Sales Growth Quarter Over Quarter`, `EPS Surprise`, `Revenue Surprise`, `Gross Margin`, `Operating Margin`, `Profit Margin`, `20-Day Simple Moving Average`, `50-Day Simple Moving Average`, `200-Day Simple Moving Average`, `EPS Growth This Year`, `EPS Growth Next Year`, `Beta`, `Volume`, `Average True Range`, `Volatility (Week)`, `Volatility (Month)`, `Total Debt/Equity`, `Current Ratio`, `Open`. Some columns were added over time, so older dates are empty for them: `Beta`, `Volume`, `Average True Range`, `Volatility (Week)`, `Volatility (Month)`, `Total Debt/Equity` and `Current Ratio` start with snapshot 2026-08-07 (empty on trade_date 2026-08-07), and `Open` (that snapshot day's open) starts with snapshot 2026-09-25. Units are as exported by Finviz: percentages as numbers, Market Cap in $M.

**`tr1d_*` — Theme Radar rubric score, 1d horizon (`data/scores/D_1d.csv`, score_delta workflow) (26):** `tr1d_mcap_bucket`, `tr1d_beta_bucket`, `tr1d_ret_H`, `tr1d_upside_pct`, `tr1d_status_extension`, `tr1d_status_trend`, `tr1d_status_short`, `tr1d_status_street`, `tr1d_price_score`, `tr1d_flow_score`, `tr1d_technical_score`, `tr1d_positioning_score`, `tr1d_valuation_score`, `tr1d_fundamental_score`, `tr1d_catalyst_score`, `tr1d_n_pos`, `tr1d_n_neg`, `tr1d_w_pos`, `tr1d_w_neg`, `tr1d_total_score`, `tr1d_score_100`, `tr1d_confidence`, `tr1d_kill_flags`, `tr1d_top_pos`, `tr1d_top_neg`, `tr1d_n_catalysts`

**`tr1w_*` — rubric score, 1w horizon (26):** `tr1w_mcap_bucket`, `tr1w_beta_bucket`, `tr1w_ret_H`, `tr1w_upside_pct`, `tr1w_status_extension`, `tr1w_status_trend`, `tr1w_status_short`, `tr1w_status_street`, `tr1w_price_score`, `tr1w_flow_score`, `tr1w_technical_score`, `tr1w_positioning_score`, `tr1w_valuation_score`, `tr1w_fundamental_score`, `tr1w_catalyst_score`, `tr1w_n_pos`, `tr1w_n_neg`, `tr1w_w_pos`, `tr1w_w_neg`, `tr1w_total_score`, `tr1w_score_100`, `tr1w_confidence`, `tr1w_kill_flags`, `tr1w_top_pos`, `tr1w_top_neg`, `tr1w_n_catalysts`

**`tr1m_*` — rubric score, 1m horizon (26):** `tr1m_mcap_bucket`, `tr1m_beta_bucket`, `tr1m_ret_H`, `tr1m_upside_pct`, `tr1m_status_extension`, `tr1m_status_trend`, `tr1m_status_short`, `tr1m_status_street`, `tr1m_price_score`, `tr1m_flow_score`, `tr1m_technical_score`, `tr1m_positioning_score`, `tr1m_valuation_score`, `tr1m_fundamental_score`, `tr1m_catalyst_score`, `tr1m_n_pos`, `tr1m_n_neg`, `tr1m_w_pos`, `tr1m_w_neg`, `tr1m_total_score`, `tr1m_score_100`, `tr1m_confidence`, `tr1m_kill_flags`, `tr1m_top_pos`, `tr1m_top_neg`, `tr1m_n_catalysts`

**`trf_*` — Theme Radar feature log (`data/features/D_1d.csv`): backward deltas `d_*`/`dir_*` vs the prior snapshot, `true_ret` (D vs pair_date), catalyst flags `cat_*`, `pair_date` (69):** `trf_price_then`, `trf_true_ret`, `trf_true_ret_dir`, `trf_d_Price`, `trf_dir_Price`, `trf_d_Market Cap`, `trf_dir_Market Cap`, `trf_d_Average Volume`, `trf_dir_Average Volume`, `trf_d_Relative Volume`, `trf_dir_Relative Volume`, `trf_d_Performance (Week)`, `trf_dir_Performance (Week)`, `trf_d_Performance (Month)`, `trf_dir_Performance (Month)`, `trf_d_Performance (Quarter)`, `trf_dir_Performance (Quarter)`, `trf_d_Performance (YTD)`, `trf_dir_Performance (YTD)`, `trf_d_Relative Strength Index (14)`, `trf_dir_Relative Strength Index (14)`, `trf_d_Short Float`, `trf_dir_Short Float`, `trf_d_Short Ratio`, `trf_dir_Short Ratio`, `trf_d_Institutional Transactions`, `trf_dir_Institutional Transactions`, `trf_d_Institutional Ownership`, `trf_dir_Institutional Ownership`, `trf_d_Insider Transactions`, `trf_dir_Insider Transactions`, `trf_d_Analyst Recom`, `trf_dir_Analyst Recom`, `trf_d_Target Price`, `trf_dir_Target Price`, `trf_d_Forward P/E`, `trf_dir_Forward P/E`, `trf_d_Sales Year Over Year TTM`, `trf_dir_Sales Year Over Year TTM`, `trf_d_Sales Growth Quarter Over Quarter`, `trf_dir_Sales Growth Quarter Over Quarter`, `trf_d_EPS Surprise`, `trf_dir_EPS Surprise`, `trf_d_Profit Margin`, `trf_dir_Profit Margin`, `trf_d_Gross Margin`, `trf_dir_Gross Margin`, `trf_d_20-Day Simple Moving Average`, `trf_dir_20-Day Simple Moving Average`, `trf_d_50-Day Simple Moving Average`, `trf_dir_50-Day Simple Moving Average`, `trf_d_200-Day Simple Moving Average`, `trf_dir_200-Day Simple Moving Average`, `trf_cat_nuclear_smr`, `trf_cat_optics_transceiver`, `trf_cat_data_center_power`, `trf_cat_hbm_memory`, `trf_cat_copper_metals`, `trf_cat_ai_capex`, `trf_cat_defense`, `trf_cat_semiconductor_equip`, `trf_upside_pct_lvl`, `trf_pair_date`, `trf_d_Beta`, `trf_dir_Beta`, `trf_d_Volatility (Month)`, `trf_dir_Volatility (Month)`, `trf_d_Total Debt/Equity`, `trf_dir_Total Debt/Equity`

**`seg_*` — Segment membership labels (`data/universe/D_membership.csv`) (17):** `seg_size`, `seg_index`, `seg_geo`, `seg_beta`, `seg_short`, `seg_liq`, `seg_rvol`, `seg_vol`, `seg_profit`, `seg_lev`, `seg_style`, `seg_mom`, `seg_ext`, `seg_range`, `seg_earn`, `seg_themes`, `seg_n_themes`

**`trc_*` — Composite residual rank (`data/composite/D_composite_rank.csv`): factor exposures, backward `ret`/`resid`, `pressure` (14):** `trc_size`, `trc_index`, `trc_beta`, `trc_short`, `trc_mom`, `trc_profitable`, `trc_leverage`, `trc_SPEC_DURATION`, `trc_QUALITY_DEFENSIVE`, `trc_CROWDING`, `trc_SIZE_TILT`, `trc_ret`, `trc_resid`, `trc_pressure`

Every Theme Radar return in this table looks **backward**: snapshot_date against an earlier snapshot. The flags are `*_kill_flags`, the `*_status_*` buckets, `*_top_pos`/`*_top_neg` (which rules drove the score), and `trf_cat_*`. These score attributions are made at scoring time; they are not the IC attribution graded against later returns.

## Multiple-testing tally

**Theme Radar already tried 8,264 combinations on these same days.** Add them to the lever search's multiple-testing tally, along with whatever the search itself tries, before judging significance.

## Check result

`python -m research.lever_panel.check_lever_panel` → **PASS** (406,649 rows, 35 trade dates; every `scrape_ts_utc` is after 16:00 ET of the prior trading day and before 09:30 ET of `trade_date`; all source commits are before 09:30 ET). Existing guards at build time: `scripts/check_history_hashes.py verify` OK (711 files + 111 row tables); pytest 37 passed.

## Prior tries: daily return series (for the overlap-aware luck test)

These files cover the earlier searches (`/workspace/finviz-lever-grid`, `finviz-fullscan-gates2` and `finviz-excel-clear-join`). The searches had saved only pooled numbers per combination (n, hit rate, mean after fees), not daily series. The series here were **regenerated** by re-running each search's own saved script on its saved inputs, in a scratch copy (`/workspace/prior_tries_regen/`; original folders untouched). The only change was a hook that records each combination's per-date result. Every regenerated combination reproduces the saved `n` and `after_fee_mean` exactly: 9,132 of 9,132 match, with a maximum absolute difference of 7e-11.

- `prior_tries_daily_returns.csv.gz`: `combo_id, date, ret_after_fee, n_names`. `ret_after_fee` is the equal-weight mean, across the names the combination fired on that date, of the signed forward return minus a 10 bp round-trip fee. Weighting by `n_names` gives back the saved pooled mean.
- `prior_tries_combos.csv.gz`: one row per combination. Columns: `source, section, pass, side, horizon, board, n, after_fee_mean_saved, n_dates_with_fires, regen_matches_saved, date_kind, in_8264_pass1_tally`.
- **The 8,264 = Pass-1 cells**: 4,832 lever-grid + 2,808 gates2 + 624 Excel-join (`in_8264_pass1_tally`). Another 868 Pass-2 / Excel-alone tries are also listed and should count toward the tally too. 7,928 of the 8,264 have a series. The other 336 never fired (n=0), so they have no rows. Over all 9,132 tries, 656 never fired.
- **Date meaning differs by source** (`date_kind`). For lever-grid (`LG|…`), `date` is the Finviz signal date T (2026-08-07 … 09-10, 22 dates). For gates2 (`G2|…`) and Excel-join (`XJ|…`), `date` is the t1 morning after T (2026-08-13 … 09-10, 13 dates). Horizons 2d/3d/1w are forward windows that overlap across consecutive dates, so their daily values are not independent.

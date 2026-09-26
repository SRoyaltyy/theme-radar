#!/usr/bin/env python3
"""Frozen 09:30-ET-knowable Finviz lever panel (research only, add-only).

One row per (ticker, trade_date). trade_date = the US trading morning on which
the row may be used. Source = the Finviz snapshot of the PREVIOUS trading day
(taken after its 16:00 ET close) plus Theme Radar's own per-ticker outputs for
that snapshot, each taken at the git version that was committed before
09:30 ET of trade_date. Same-day (trade_date) values are never used.

Rebuild: python -m research.lever_panel.build_lever_panel
Check:   python -m research.lever_panel.check_lever_panel
"""
from __future__ import annotations

import gzip
import hashlib
import io
import json
import re
import subprocess
import sys
from datetime import date, datetime, time, timezone
from pathlib import Path
from zoneinfo import ZoneInfo

import pandas as pd

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))
from src.trading_calendar import (is_trading_day, next_trading_day,  # noqa: E402
                                  previous_trading_day, trading_days_between)

ET = ZoneInfo("America/New_York")
UTC = timezone.utc
SNAP = ROOT / "data" / "snapshots"
OUT_DIR = ROOT / "research" / "lever_panel"
OUT = OUT_DIR / "finviz_panel_asof0930.csv.gz"
META = OUT_DIR / "panel_meta.json"
END_TRADE_DATE = date(2026, 9, 28)
MAX_BYTES = 90 * 1000 * 1000  # split by month above this

# Free text, not numeric/categorical levers (News Time is kept).
DROP_SNAPSHOT_COLS = {"News Title", "Daily Digest", "News URL", "scrape_ts"}
# Any derived column whose name smells of an outcome / forward return is dropped.
OUTCOME_RX = re.compile(r"(^|_)(fwd|forward_ret|label|outcome|exit|entry|next|future|hit|y_)",
                        re.I)
DATE_FILE_RX = re.compile(r"^(\d{4}-\d{2}-\d{2})\.csv$")


def git(*args: str, binary: bool = False):
    r = subprocess.run(["git", *args], cwd=ROOT, capture_output=True, check=True)
    return r.stdout if binary else r.stdout.decode().strip()


def sha256_bytes(b: bytes) -> str:
    return hashlib.sha256(b).hexdigest()


def open_et(d: date) -> datetime:
    return datetime.combine(d, time(9, 30), ET)


def close_et(d: date) -> datetime:
    return datetime.combine(d, time(16, 0), ET)


def iso(t: datetime) -> str:
    return t.astimezone(UTC).strftime("%Y-%m-%dT%H:%M:%SZ")


def commits_of(rel: str) -> list[tuple[str, datetime]]:
    out = git("log", "--format=%H %cI", "--", rel)
    res = []
    for line in out.splitlines():
        h, ts = line.split(" ", 1)
        res.append((h, datetime.fromisoformat(ts)))
    return res  # newest first


def version_at(rel: str, cutoff: datetime):
    """(bytes, commit, commit_ts, equals_head) of the newest committed version of
    rel strictly before cutoff, or None."""
    for h, ts in commits_of(rel):
        if ts < cutoff:
            try:
                blob = git("rev-parse", f"{h}:{rel}")
            except subprocess.CalledProcessError:
                return None  # deleted at that commit
            head_blob = git("rev-parse", f"HEAD:{rel}")
            data = git("cat-file", "blob", blob, binary=True)
            return data, h, ts, blob == head_blob
    return None


def snapshot_scrape_time(d: str, manifest: dict) -> tuple[datetime, str]:
    p = SNAP / f"{d}.csv"
    df = pd.read_csv(p, usecols=lambda c: c == "scrape_ts", dtype=str)
    if "scrape_ts" in df.columns and df["scrape_ts"].notna().any():
        ts = pd.to_datetime(df["scrape_ts"].dropna(), utc=True)
        return ts.max().to_pydatetime(), "scrape_ts column"
    runs = [r for r in manifest.get("runs", []) if r.get("date") == d]
    if runs:
        r = runs[-1]
        arc = SNAP / "archive" / r["archive"]
        if arc.exists() and sha256_bytes(arc.read_bytes()) == sha256_bytes(p.read_bytes()):
            t = datetime.strptime(r["stamp"], "%Y%m%d_%H%M%S").replace(tzinfo=ET)
            return t.astimezone(UTC), "manifest run stamp (archive copy sha256-identical)"
    h, ts = commits_of(f"data/snapshots/{d}.csv")[0]
    return ts.astimezone(UTC), "git commit time of snapshot (upper bound; no scrape_ts/run stamp)"


def derived_sources(d: str) -> dict[str, str]:
    return {
        "tr1d": f"data/scores/{d}_1d.csv",
        "tr1w": f"data/scores/{d}_1w.csv",
        "tr1m": f"data/scores/{d}_1m.csv",
        "trf": f"data/features/{d}_1d.csv",
        "trc": f"data/composite/{d}_composite_rank.csv",
        "seg": f"data/universe/{d}_membership.csv",
    }


FAMILY_COMMIT_COL = {"tr1d": "tr_scores_commit_ts_utc", "tr1w": "tr_scores_commit_ts_utc",
                     "tr1m": "tr_scores_commit_ts_utc", "trf": "tr_features_commit_ts_utc",
                     "trc": "tr_composite_commit_ts_utc", "seg": "tr_segments_commit_ts_utc"}


def gz_bytes(df: pd.DataFrame) -> bytes:
    """Deterministic gzip (mtime=0, no filename) so the sha256 is reproducible."""
    buf = io.BytesIO()
    with gzip.GzipFile(filename="", mode="wb", fileobj=buf, mtime=0, compresslevel=9) as gz:
        gz.write(df.to_csv(index=False).encode())
    return buf.getvalue()


def main() -> int:
    manifest = json.loads((SNAP / "manifest.json").read_text())
    snap_dates = sorted(m.group(1) for p in SNAP.iterdir() if (m := DATE_FILE_RX.match(p.name)))
    first = date.fromisoformat(snap_dates[0])
    trade_days = trading_days_between(first, END_TRADE_DATE)

    frames, per_date, skipped, provenance = [], [], [], []
    snap_cols_seen: list[str] = []
    dropped_outcome: set[str] = set()
    for T in trade_days:
        D = previous_trading_day(T)
        Ds = D.isoformat()
        cutoff = open_et(T)
        if Ds not in snap_dates:
            skipped.append({"trade_date": T.isoformat(), "missing_snapshot_date": Ds,
                            "reason": f"no data/snapshots/{Ds}.csv (prior-close snapshot absent)"})
            continue
        rel = f"data/snapshots/{Ds}.csv"
        v = version_at(rel, cutoff)
        if v is None or not v[3]:
            skipped.append({"trade_date": T.isoformat(), "missing_snapshot_date": Ds,
                            "reason": "snapshot on disk was not committed before 09:30 ET"})
            continue
        if git("diff", "--quiet", "HEAD", "--", rel) != "":
            raise SystemExit(f"{rel} differs from HEAD")
        scrape, src = snapshot_scrape_time(Ds, manifest)
        if not (close_et(D) < scrape < cutoff):
            skipped.append({"trade_date": T.isoformat(), "missing_snapshot_date": Ds,
                            "reason": f"scrape {iso(scrape)} outside ({iso(close_et(D))}, {iso(cutoff)})"})
            continue
        snap = pd.read_csv(io.BytesIO(v[0]), dtype=str, keep_default_na=False, na_values=[""])
        snap = snap.drop(columns=[c for c in snap.columns if c in DROP_SNAPSHOT_COLS])
        snap = snap.drop_duplicates("Ticker", keep="last")
        for c in snap.columns:
            if c not in snap_cols_seen:
                snap_cols_seen.append(c)
        base = pd.DataFrame({
            "trade_date": T.isoformat(),
            "snapshot_date": Ds,
            "scrape_ts_utc": iso(scrape),
            "scrape_ts_source": src,
            "snapshot_commit_ts_utc": iso(v[2]),
        }, index=snap.index)
        df = pd.concat([base, snap], axis=1)
        prov = {"trade_date": T.isoformat(), "snapshot_date": Ds, "scrape_ts_utc": iso(scrape),
                "scrape_ts_source": src, "snapshot_commit": v[1][:10],
                "snapshot_commit_ts_utc": iso(v[2]), "derived": {}}
        fam_ts: dict[str, datetime] = {}
        for fam, drel in derived_sources(Ds).items():
            if not (ROOT / drel).exists() and not commits_of(drel):
                prov["derived"][fam] = "absent"
                continue
            dv = version_at(drel, cutoff)
            if dv is None:
                prov["derived"][fam] = "not committed before 09:30 ET -> omitted"
                continue
            prov["derived"][fam] = (f"{dv[1][:10]} {iso(dv[2])}"
                                    + ("" if dv[3] else " (pre-cutoff version, differs from HEAD)"))
            dd = pd.read_csv(io.BytesIO(dv[0]), dtype=str, keep_default_na=False, na_values=[""])
            dd = dd.drop_duplicates("Ticker", keep="last").set_index("Ticker")
            drop = {"Company", "Sector", "Industry", "Price", "sector", "industry"}
            if fam == "trf":
                drop |= set(snap.columns) | {"scan_date", "n_universe"}
                # score columns duplicated from the 1d score file
                s1 = derived_sources(Ds)["tr1d"]
                if (ROOT / s1).exists():
                    drop |= set(pd.read_csv(ROOT / s1, nrows=0).columns)
            keep = [c for c in dd.columns if c not in drop and not OUTCOME_RX.search(c)]
            dropped_outcome.update(c for c in dd.columns if c not in drop and OUTCOME_RX.search(c))
            dd = dd[keep].add_prefix(f"{fam}_")
            df = df.join(dd, on="Ticker")
            col = FAMILY_COMMIT_COL[fam]
            fam_ts[col] = max(fam_ts.get(col, dv[2]), dv[2])
        for col in dict.fromkeys(FAMILY_COMMIT_COL.values()):
            df[col] = iso(fam_ts[col]) if col in fam_ts else pd.NA
        frames.append(df)
        provenance.append(prov)
        per_date.append({"trade_date": T.isoformat(), "snapshot_date": Ds,
                         "rows": len(df), "tickers": int(df["Ticker"].nunique())})
        print(f"[panel] {T} <- {Ds} rows={len(df)} scrape={iso(scrape)} ({src})", flush=True)

    panel = pd.concat(frames, ignore_index=True, sort=False)
    lead = ["trade_date", "snapshot_date", "scrape_ts_utc", "scrape_ts_source",
            "snapshot_commit_ts_utc"] + list(dict.fromkeys(FAMILY_COMMIT_COL.values()))
    fv = [c for c in snap_cols_seen if c in panel.columns]
    rest = [c for c in panel.columns if c not in lead and c not in fv]
    panel = panel[lead + fv + rest].sort_values(["trade_date", "Ticker"], kind="stable")
    assert not panel.duplicated(["Ticker", "trade_date"]).any()

    full = gz_bytes(panel)
    OUT.unlink(missing_ok=True)
    for old in OUT_DIR.glob("finviz_panel_asof0930_*.csv.gz"):
        old.unlink()
    files = []
    if len(full) <= MAX_BYTES:
        OUT.write_bytes(full)
        files.append({"file": OUT.relative_to(ROOT).as_posix(), "sha256": sha256_bytes(full),
                      "bytes": len(full), "rows": int(len(panel)),
                      "first_trade_date": per_date[0]["trade_date"],
                      "last_trade_date": per_date[-1]["trade_date"]})
    else:  # split by trade_date month (GitHub file-size limit)
        for month, part in panel.groupby(panel["trade_date"].str[:7], sort=True):
            b = gz_bytes(part)
            assert len(b) <= MAX_BYTES, (month, len(b))
            f = OUT_DIR / f"finviz_panel_asof0930_{month}.csv.gz"
            f.write_bytes(b)
            files.append({"file": f.relative_to(ROOT).as_posix(), "sha256": sha256_bytes(b),
                          "bytes": len(b), "rows": int(len(part)),
                          "first_trade_date": part["trade_date"].min(),
                          "last_trade_date": part["trade_date"].max()})
    meta = {
        "files": files,
        "unsplit_bytes": len(full),
        "rows": int(len(panel)),
        "n_columns": int(panel.shape[1]),
        "first_trade_date": per_date[0]["trade_date"],
        "last_trade_date": per_date[-1]["trade_date"],
        "built_from_head": git("rev-parse", "HEAD"),
        "built_at_utc": iso(datetime.now(UTC)),
        "per_date": per_date,
        "skipped": skipped,
        "provenance": provenance,
        "dropped_outcome_like_columns": sorted(dropped_outcome),
        "columns": list(panel.columns),
        "finviz_columns": fv,
    }
    META.write_text(json.dumps(meta, indent=1) + "\n")
    print(json.dumps({k: meta[k] for k in ("files", "unsplit_bytes", "rows", "n_columns",
                                           "first_trade_date", "last_trade_date", "skipped")},
                     indent=1))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

"""CLI: install a new Finviz export as current snapshot.

Usage:
  python -m src.promote_snapshot /path/to/finviz_export.csv --as-of 2026-08-06
"""
from __future__ import annotations

import argparse
from pathlib import Path

from .finviz_delta import promote_snapshot


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("csv_path", type=Path)
    ap.add_argument("--as-of", default=None, help="YYYY-MM-DD archive label")
    args = ap.parse_args()
    if not args.csv_path.exists():
        raise SystemExit(f"File not found: {args.csv_path}")
    promote_snapshot(args.csv_path, as_of=args.as_of)
    print(f"Promoted {args.csv_path} → data/snapshots/current.csv")
    if args.as_of:
        print(f"Archived as data/snapshots/archive/finviz_{args.as_of}.csv")


if __name__ == "__main__":
    main()

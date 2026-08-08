"""Promote repeated attribution/score lessons to active rules.

Clusters candidate lessons by trigger_pattern token Jaccard >= 0.5;
promotes clusters with >= 2 occurrences (no LLM required).

CLI: python -m src.promote_lessons
"""
from __future__ import annotations

import glob
import os
import re
from datetime import datetime
from zoneinfo import ZoneInfo

from . import config

JACCARD = 0.5
MIN_OCC = 2
CAND = config.ROOT / "02_lessons" / "candidate"
ACTIVE = config.ROOT / "02_lessons" / "active"


def _parse(path: str) -> dict:
    with open(path, encoding="utf-8") as fh:
        text = fh.read()
    m = re.match(r"---\n(.*?)\n---", text, re.S)
    out = {"path": path, "body": text}
    if m:
        for line in m.group(1).splitlines():
            if ":" in line:
                k, v = line.split(":", 1)
                out[k.strip()] = v.strip().strip('"')
    return out


def _tokens(s: str) -> set:
    return set(re.findall(r"[a-z0-9]+", (s or "").lower()))


def _jaccard(a: set, b: set) -> float:
    return len(a & b) / len(a | b) if a and b else 0.0


def main() -> None:
    paths = sorted(glob.glob(str(CAND / "*_lesson.md")))
    cands = [_parse(p) for p in paths]
    cands = [c for c in cands if c.get("status", "candidate") == "candidate"]
    print(f"[promote] {len(cands)} open candidates")

    clusters: list[list[dict]] = []
    for c in cands:
        ct = _tokens(c.get("trigger_pattern", ""))
        placed = False
        for cl in clusters:
            if _jaccard(ct, _tokens(cl[0].get("trigger_pattern", ""))) >= JACCARD:
                cl.append(c)
                placed = True
                break
        if not placed:
            clusters.append([c])

    ACTIVE.mkdir(parents=True, exist_ok=True)
    promoted = 0
    today = datetime.now(ZoneInfo(config.TZ)).date().isoformat()
    for cl in clusters:
        if len(cl) < MIN_OCC:
            continue
        slug = re.sub(r"[^a-z0-9]+", "-", cl[0].get("trigger_pattern", "rule").lower())[:50].strip("-")
        apath = ACTIVE / f"{slug}.md"
        evidence = "\n".join(
            f"- {c.get('date')}: {c.get('evidence_cited', '')[:200]}" for c in cl
        )
        text = (
            f"---\ntrigger_pattern: \"{cl[0].get('trigger_pattern', '')}\"\n"
            f"occurrences: {len(cl)}\npromoted_on: \"{today}\"\nstatus: \"active\"\n---\n\n"
            f"# Active rule\n\n"
            f"**Corrected behavior:** {cl[0].get('corrected_behavior', '')}\n\n"
            f"## Evidence\n{evidence}\n"
        )
        apath.write_text(text, encoding="utf-8")
        for c in cl:
            body = c["body"].replace('status: "candidate"', 'status: "promoted"', 1)
            with open(c["path"], "w", encoding="utf-8") as fh:
                fh.write(body)
        promoted += 1
        print(f"[promote] cluster of {len(cl)} -> {apath.name}")
    print(f"[promote] done: {promoted} rules")


if __name__ == "__main__":
    main()

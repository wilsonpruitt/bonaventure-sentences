#!/usr/bin/env python3.11
"""Vol V census — derive corpus-wide counts instead of hand-carrying them.

WHY THIS EXISTS (2026-07-28). The Vol V runover tally forked: the resume note
said "eleven runovers in twenty chunks" while bon-brev-p2-c7's Notes said
"fourteenth runover in twenty-three chunks." Neither was right. The counts were
exact through p1-c8, then went -1 on BOTH counters at prol-s2 and stayed there,
because whoever resumed the tally after the Pars I block omitted
`bon-brev-prol` — the only vol5 chunk whose slug has no numeric suffix, so an
eye (or a glob) running down the directory listing slides straight past it. A
later session repaired the chunk count but not the runover count, so the two
numbers ended up wrong in different directions and looked like independent
drift rather than one dropped chunk.

The lesson generalizes past runovers: ANY number describing the whole corpus —
chunk counts, runover tallies, apparatus totals, [?] flag counts — must be
DERIVED at the moment it is cited, never carried forward by hand from the last
session. A hand-carried counter has no way to notice that it skipped something.

So the ledger records EVENTS, one line per chunk including the negatives, and
this script derives the totals. The load-bearing check is the roster diff:
every chunk in vol5/ must appear in the ledger and vice versa. That is exactly
the check that would have caught the original omission on the day it happened.

Usage:  python3.11 tools/check-vol5-census.py
Exit 0 = rosters agree. Exit 1 = a chunk is missing from one side.

Extending to Vols VI–X: add (chunk dir, ledger path) to VOLUMES. Each work's
prologue/opener is the likely blind spot — it is the one with no numeric suffix.
"""

import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

VOLUMES = [
    ("vol5", "manual-review/vol5-runover-ledger.tsv", "bon-brev-"),
]


def read_ledger(path):
    """-> list of (slug, [(event, kind), ...]) in file order."""
    rows = []
    with open(os.path.join(ROOT, path), encoding="utf-8") as fh:
        for lineno, line in enumerate(fh, 1):
            line = line.rstrip("\n")
            if not line.strip() or line.lstrip().startswith("#"):
                continue
            parts = line.split("\t")
            if len(parts) != 2:
                sys.exit(f"{path}:{lineno}: expected exactly 2 tab-separated fields")
            slug, raw = parts[0].strip(), parts[1].strip()
            events = []
            if raw != "-":
                for item in raw.split(","):
                    m = re.match(r"^(.*):(gutter|page)$", item.strip())
                    if not m:
                        sys.exit(f"{path}:{lineno}: bad event {item.strip()!r} "
                                 f"(want '<page> <note>:gutter' or ':page')")
                    events.append((m.group(1), m.group(2)))
            rows.append((slug, events))
    return rows


def main():
    failed = False
    for chunk_dir, ledger_path, prefix in VOLUMES:
        rows = read_ledger(ledger_path)

        on_disk = {
            f[len(prefix):-3]
            for f in os.listdir(os.path.join(ROOT, chunk_dir))
            if f.startswith(prefix) and f.endswith(".md")
        }
        in_ledger = [slug for slug, _ in rows]

        dupes = {s for s in in_ledger if in_ledger.count(s) > 1}
        missing = on_disk - set(in_ledger)   # chunk exists, never tested
        stale = set(in_ledger) - on_disk     # ledger names a chunk that is gone

        print(f"{chunk_dir}: {len(on_disk)} chunks on disk, "
              f"{len(in_ledger)} in ledger")

        for slug in sorted(missing):
            print(f"  ✗ MISSING from ledger: {prefix}{slug} — runover test not "
                  f"on record. This is the bug the ledger exists to catch.")
            failed = True
        for slug in sorted(stale):
            print(f"  ✗ STALE ledger row: {prefix}{slug} has no file")
            failed = True
        for slug in sorted(dupes):
            print(f"  ✗ DUPLICATE ledger row: {prefix}{slug}")
            failed = True

        events = [e for _, evs in rows for e in evs]
        gutter = sum(1 for _, kind in events if kind == "gutter")
        page = sum(1 for _, kind in events if kind == "page")
        tested = sum(1 for _, evs in rows if evs)

        print(f"  runovers: {len(events)} across {len(in_ledger)} chunks "
              f"({gutter} gutter-crossing, {page} page-crossing; "
              f"{tested} chunks positive, {len(in_ledger) - tested} negative)")
        if page:
            print("  page-crossing: " +
                  " · ".join(e for e, k in events if k == "page"))

    if failed:
        print("\nFAILED — cite no count until the rosters agree.")
        return 1
    print("\nRosters agree. These are the numbers to cite.")
    return 0


if __name__ == "__main__":
    sys.exit(main())

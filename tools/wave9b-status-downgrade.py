#!/usr/bin/env python3.11
"""Wave 9b status-string downgrade — for chunks flagged by hardened
audit-apparatus-count with diff >= +20, replace the
`Phase C Tier 2 complete —` prefix with `Phase C Tier 2 apparatus-incomplete —`
and append an audit-flag tail. Idempotent.

The 23 chunks below are the union of:
  - Tier A: diff >= +30 (9 chunks; rebuild this session)
  - Tier B: diff +20 to +29 (14 chunks; rebuild later session)

Run: python3.11 tools/wave9b-status-downgrade.py
"""
from __future__ import annotations
import re
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
VOL1 = REPO / "vol1"

# Format: chunk_basename → (raw_count, chunk_count, tier)
TARGETS: dict[str, tuple[int, int, str]] = {
    # Tier A — diff >= +30
    "bon-sent-I-d36-divisio":      (52, 4,  "A"),
    "bon-sent-I-d8-p1-a2-q2":      (53, 12, "A"),
    "bon-sent-I-d7-a1-q1":         (43, 5,  "A"),
    "bon-sent-I-d35-a1-q1":        (49, 12, "A"),
    "bon-sent-I-d27-p1-a1-q2":     (57, 25, "A"),
    "bon-sent-I-d5-a1-q1":         (36, 5,  "A"),
    "bon-sent-I-d8-p2-a1-q3":      (38, 7,  "A"),
    "bon-sent-I-d31-p2-dubia":     (38, 8,  "A"),
    "bon-sent-I-d37-littera":      (62, 32, "A"),
    # Tier B — diff +20 to +29
    "bon-sent-I-d39-a1-q1":        (40, 13, "B"),
    "bon-sent-I-d37-p2-a1-q1":     (38, 13, "B"),
    "bon-sent-I-d7-a1-q2":         (31, 7,  "B"),
    "bon-sent-I-d27-littera":      (40, 17, "B"),
    "bon-sent-I-d8-p1-a1-q2":      (34, 11, "B"),
    "bon-sent-I-d8-p2-a1-q2":      (31, 8,  "B"),
    "bon-sent-I-d31-littera":      (43, 21, "B"),
    "bon-sent-I-d33-littera":      (41, 19, "B"),
    "bon-sent-I-d28-littera":      (36, 15, "B"),
    "bon-sent-I-d32-littera":      (36, 15, "B"),
    "bon-sent-I-d8-p1-a1-q1":      (31, 10, "B"),
    "bon-sent-I-d38-a1-q1":        (31, 11, "B"),
    "bon-sent-I-d38-a2-q1":        (30, 10, "B"),
    "bon-sent-I-d8-littera":       (42, 14, "B"),
}

PREFIX_OLD = "Phase C Tier 2 complete —"
PREFIX_NEW = "Phase C Tier 2 apparatus-incomplete —"
TAIL_TEMPLATE = (
    " [Apparatus undercoverage flagged 2026-05-09 (Wave 9b, Tier {tier}): "
    "chunk has {chunk} apparatus defs vs hardened-heuristic raw count {raw} "
    "(diff +{diff}). Body and translation are sound; only the apparatus "
    "block is incomplete. Full apparatus rebuild from raw OCR queued — see "
    "manual-review/d1-d4-tier2-promotion-log.md Lesson 9.]"
)
TAIL_MARKER = "Wave 9b, Tier "  # idempotency check


def main() -> int:
    n_changed = 0
    n_skipped = 0
    n_missing = 0
    for stem, (raw, chunk, tier) in TARGETS.items():
        path = VOL1 / f"{stem}.md"
        if not path.exists():
            print(f"  MISSING: {path}", file=sys.stderr)
            n_missing += 1
            continue
        text = path.read_text(encoding="utf-8")
        if TAIL_MARKER in text:
            n_skipped += 1
            continue
        if PREFIX_OLD not in text:
            print(f"  NO-PREFIX-MATCH: {stem} (status string doesn't start with '{PREFIX_OLD}')", file=sys.stderr)
            continue
        diff = raw - chunk
        tail = TAIL_TEMPLATE.format(tier=tier, chunk=chunk, raw=raw, diff=diff)
        # Replace prefix once (the first occurrence is in the frontmatter)
        new_text = text.replace(PREFIX_OLD, PREFIX_NEW, 1)
        # Append tail to the closing quote of the transcription_status frontmatter line
        # The frontmatter line is `transcription_status: "..."` — find the closing `"` after `apparatus-incomplete —` and insert before it.
        m = re.search(
            r'^(transcription_status:\s*")(.*?)("\s*)$',
            new_text,
            flags=re.MULTILINE | re.DOTALL,
        )
        if not m:
            print(f"  NO-FRONTMATTER-MATCH: {stem}", file=sys.stderr)
            continue
        # Rewrite the line with the tail appended inside the quotes
        body = m.group(2) + tail
        new_text = new_text[: m.start(2)] + body + new_text[m.end(2):]
        path.write_text(new_text, encoding="utf-8")
        n_changed += 1
        print(f"  patched: {stem} (Tier {tier}, +{diff})")
    print(f"\n{n_changed} chunks patched, {n_skipped} already-patched, {n_missing} missing")
    return 0


if __name__ == "__main__":
    sys.exit(main())

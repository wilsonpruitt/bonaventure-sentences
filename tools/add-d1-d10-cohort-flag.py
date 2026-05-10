#!/usr/bin/env python3.11
"""One-shot tool (2026-05-10): append a Wave 9b residual re-verification
flag to the transcription_status of every "Phase C Tier 2 complete" chunk
in d.1-d.10. Reversible: the appended marker is a fixed substring; running
this twice is a no-op; the inverse op is `--undo`.

Why: the d.6-a1-q2 spot-check rebuild (Wave 9b residual, 2026-05-10) found
the chunk had only 7 of 21 ground-truth apparatus entries — all 14
textual-variant notes were dropped during initial Tier-2 promotion. This
exposed a systematic pattern in the d.1-d.10 cohort: chunks promoted
before the locked-in apparatus standard (audit-apparatus-count.py +
audit-paraphrase.py + audit-headers.py guard rails) may quietly miss
textual-variant entries that the audits no longer flag because banded
under-counts variant openers. Site keeps showing the chunks; this flag is
the in-chunk signal that "complete" is conditional on the campaign close.
"""
from __future__ import annotations
import argparse
import re
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
VOL1 = REPO / "vol1"

FLAG = " [d.1-d.10 Wave 9b residual re-verification campaign 2026-05-10 — apparatus completeness pending]"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--undo", action="store_true",
                    help="Strip the cohort flag (reversibility check)")
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    touched, skipped, missing_status = [], [], []
    for p in sorted(VOL1.glob("bon-sent-I-d*.md")):
        m = re.match(r"bon-sent-I-d(\d+)-", p.name)
        if not m:
            continue
        d = int(m.group(1))
        if d > 10:
            continue
        text = p.read_text(encoding="utf-8")
        # Match transcription_status ending — quoted string in frontmatter,
        # closing quote at end of line. The status spans multiple lines if
        # quoted with """, but in this corpus all are single-line "...".
        status_re = re.compile(r'^(transcription_status:\s*)"([^"]*)"', re.MULTILINE)
        sm = status_re.search(text)
        if not sm:
            missing_status.append(p.name)
            continue
        prefix, body = sm.group(1), sm.group(2)
        is_tier2 = body.lower().startswith("phase c tier 2 complete")
        if not is_tier2:
            skipped.append((p.name, "not-tier2-complete"))
            continue

        if args.undo:
            if FLAG not in body:
                skipped.append((p.name, "flag-already-absent"))
                continue
            new_body = body.replace(FLAG, "")
        else:
            if FLAG in body:
                skipped.append((p.name, "flag-already-present"))
                continue
            new_body = body + FLAG

        new_status = f'{prefix}"{new_body}"'
        new_text = text[:sm.start()] + new_status + text[sm.end():]
        if not args.dry_run:
            p.write_text(new_text, encoding="utf-8")
        touched.append(p.name)

    action = "would touch" if args.dry_run else ("stripped" if args.undo else "flagged")
    print(f"{action}: {len(touched)} chunks")
    print(f"skipped: {len(skipped)}")
    for name, reason in skipped:
        print(f"  {name} ({reason})")
    if missing_status:
        print(f"missing transcription_status: {len(missing_status)}")
        for name in missing_status:
            print(f"  {name}")


if __name__ == "__main__":
    main()

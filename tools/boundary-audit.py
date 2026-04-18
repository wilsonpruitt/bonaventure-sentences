#!/usr/bin/env python3.11
"""Audit chunk boundaries against raw text semantic markers.

For each chunk in vol1/, checks whether the start/end lines align with
actual QUAESTIO/ARTICULUS/DUBIA/DISTINCTIO markers in the raw text.
Flags chunks that:
  - Start mid-content (no marker within 5 lines of start)
  - End mid-content (next chunk's marker is inside this chunk's range)
  - Are missing (gap in distinction coverage)
  - Have running-head false starts

Also detects all semantic markers in the raw text and compares against
existing chunks to find missing ones.

Usage:
    python3.11 tools/boundary-audit.py              # audit all vol1
    python3.11 tools/boundary-audit.py --dist 10    # audit d.10 only
    python3.11 tools/boundary-audit.py --fix        # write corrected boundaries
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import dataclass, field
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
RAW_BY_PART = {
    None: REPO / "raw" / "bonaventure_vol1_raw.txt",
    1: REPO / "raw" / "bonaventure_vol1_raw.txt",
    2: REPO / "raw" / "bonaventure_vol1_pt2_raw.txt",
}
VOL1 = REPO / "vol1"

# Broad OCR-tolerant patterns
MARKER_PATTERNS = [
    ("DISTINCTIO", re.compile(r"^\s*DISTINCTIO\s+([IVXLCivxlc]+)", re.MULTILINE)),
    ("COMMENTARIUS", re.compile(r"^\s*COMMENTARIUS\s+IN", re.MULTILINE)),
    ("DIVISIO", re.compile(r"DIVISIO\s+TEXTUS", re.MULTILINE)),
    ("TRACTATIO", re.compile(r"TRACTATIO\s+QU", re.MULTILINE)),
    ("ARTICULUS", re.compile(r"^\s*ARTI[CG]ULUS\s+([IVXLC]+|UNICUS)", re.MULTILINE)),
    ("QUAESTIO", re.compile(r"^\s*Q[UIJij1][A^.flEIJij]{0,6}STIO\s+([IVXLCivxlcm]+)", re.MULTILINE)),
    ("DUBIA", re.compile(r"^\s*DUB(?:IA)?\s+CIRCA|^\s*DIST\..*DUBIA", re.MULTILINE)),
    ("SCHOLION", re.compile(r"^\s*[CS][CHI]OLIO[NK]", re.MULTILINE)),
    ("CONCLUSIO", re.compile(r"^\s*CONCLUSIO", re.MULTILINE)),
    ("RUNNING_HEAD", re.compile(
        r"^\s*DIST\.\s+[IVXLC]+\.\s+(?:ART|P)\.\s+[IVXLC]+", re.MULTILINE
    )),
]

ROMAN = {
    "I": 1, "II": 2, "III": 3, "IV": 4, "V": 5, "VI": 6, "VII": 7,
    "VIII": 8, "IX": 9, "X": 10, "XI": 11, "XII": 12, "XIII": 13,
    "XIV": 14, "XV": 15, "XVI": 16, "XVII": 17, "XVIII": 18, "XIX": 19,
    "XX": 20, "XXI": 21, "XXII": 22, "XXIII": 23, "XXIV": 24, "XXV": 25,
    "XXVI": 26, "XXVII": 27, "XXVIII": 28, "XXIX": 29, "XXX": 30,
    "XXXI": 31, "XXXII": 32, "XXXIII": 33, "XXXIV": 34, "XXXV": 35,
    "XXXVI": 36, "XXXVII": 37, "XXXVIII": 38, "XXXIX": 39, "XL": 40,
    "XLI": 41, "XLII": 42, "XLIII": 43, "XLIV": 44, "XLV": 45,
    "XLVI": 46, "XLVII": 47, "XLVIII": 48,
    "UNICUS": 1, "m": 3,
}


@dataclass
class Marker:
    line: int
    kind: str
    num: int | None = None
    raw: str = ""
    is_running_head: bool = False


@dataclass
class ChunkInfo:
    path: Path
    chunk_id: str
    dist: int | None = None
    art: int | None = None
    q: int | None = None
    kind: str = ""  # littera, divisio, quaestio, dubia
    line_start: int = 0
    line_end: int = 0
    tier2: bool = False

    @property
    def label(self):
        return self.path.stem


def parse_roman(s: str) -> int | None:
    s = s.strip().upper()
    if s in ROMAN:
        return ROMAN[s]
    trailing = len(s) - len(s.rstrip("L"))
    for n in range(1, trailing + 1):
        variant = s[:-n] + "I" * n
        if variant in ROMAN:
            return ROMAN[variant]
    return None


def find_markers(text: str) -> list[Marker]:
    markers = []
    for kind, pattern in MARKER_PATTERNS:
        for m in pattern.finditer(text):
            line = text[:m.start()].count("\n") + 1
            num = None
            if m.lastindex and m.lastindex >= 1:
                num = parse_roman(m.group(1))
            raw = m.group(0).strip()[:80]
            is_rh = kind == "RUNNING_HEAD"
            markers.append(Marker(line, kind, num, raw, is_rh))
    markers.sort(key=lambda m: m.line)
    return markers


def load_chunks(dist_filter: int | None = None, dist_range: tuple[int, int] | None = None) -> list[ChunkInfo]:
    chunks = []
    for f in sorted(VOL1.glob("bon-sent-I-d*-*.md")):
        text = f.read_text()

        # Parse frontmatter
        fm = {}
        fm_match = re.match(r"---\n(.*?)\n---", text, re.DOTALL)
        if fm_match:
            for line in fm_match.group(1).splitlines():
                if ":" in line:
                    k, v = line.split(":", 1)
                    fm[k.strip()] = v.strip().strip('"')

        dist = int(fm.get("distinctio", 0)) or None
        if dist_filter and dist != dist_filter:
            continue
        if dist_range and (dist is None or not (dist_range[0] <= dist <= dist_range[1])):
            continue

        art = int(fm["articulus"]) if "articulus" in fm else None
        q = int(fm["quaestio"]) if "quaestio" in fm else None
        kind = fm.get("type", "")
        line_start = int(fm.get("line_start", 0))
        line_end = int(fm.get("line_end", 0))

        tier2 = "Tier 2" in fm.get("transcription_status", "")

        chunks.append(ChunkInfo(
            path=f, chunk_id=f.stem, dist=dist, art=art, q=q,
            kind=kind, line_start=line_start, line_end=line_end,
            tier2=tier2,
        ))
    return chunks


def find_dist_markers(markers: list[Marker]) -> dict[int, tuple[int, int]]:
    """Map distinctio number -> (start_line, end_line)."""
    dist_markers = []
    seen = set()
    for m in markers:
        if m.kind == "DISTINCTIO" and m.num and m.num not in seen:
            dist_markers.append(m)
            seen.add(m.num)

    ranges = {}
    for i, m in enumerate(dist_markers):
        start = m.line
        end = dist_markers[i + 1].line - 1 if i + 1 < len(dist_markers) else 999999
        ranges[m.num] = (start, end)
    return ranges


def audit_distinction(
    dist_num: int,
    chunks: list[ChunkInfo],
    markers: list[Marker],
    lines: list[str],
    dist_range: tuple[int, int],
) -> list[str]:
    issues = []
    d_start, d_end = dist_range

    # Get markers within this distinction
    dist_markers = [m for m in markers if d_start <= m.line <= d_end]

    # Expected chunks: littera, divisio, then quaestiones, then dubia
    has_littera = any(c.kind in ("littera", "littera-magistri") for c in chunks)
    has_divisio = any(c.kind == "divisio" for c in chunks)
    has_dubia = any(c.kind == "dubia" for c in chunks)

    if not has_littera:
        issues.append(f"  MISSING littera chunk")
    if not has_divisio:
        issues.append(f"  MISSING divisio chunk")
    if not has_dubia:
        # Check if there are DUBIA markers
        dubia_markers = [m for m in dist_markers if m.kind == "DUBIA"]
        if dubia_markers:
            issues.append(f"  MISSING dubia chunk (markers found at lines {[m.line for m in dubia_markers]})")

    # Check quaestio markers vs chunks
    q_markers = [m for m in dist_markers if m.kind == "QUAESTIO"]
    art_markers = [m for m in dist_markers if m.kind == "ARTICULUS"]
    q_chunks = [c for c in chunks if c.kind == "quaestio"]

    # Check for running-head false starts
    rh_markers = [m for m in dist_markers if m.kind == "RUNNING_HEAD"]

    # Check each chunk's boundaries
    for c in chunks:
        if c.line_start == 0:
            continue  # No raw line info

        # Check if chunk starts at a running head instead of a real marker
        start_context = lines[max(0, c.line_start - 2):c.line_start + 3]
        start_text = "\n".join(start_context)

        has_marker_at_start = False
        for m in dist_markers:
            if abs(m.line - c.line_start) <= 5 and not m.is_running_head:
                if m.kind in ("QUAESTIO", "ARTICULUS", "DUBIA", "COMMENTARIUS",
                              "DIVISIO", "DISTINCTIO", "SCHOLION", "CONCLUSIO"):
                    has_marker_at_start = True
                    break

        rh_at_start = any(
            abs(m.line - c.line_start) <= 3
            for m in rh_markers
        )

        if rh_at_start and not has_marker_at_start:
            issues.append(f"  {c.label}: starts at RUNNING HEAD (line {c.line_start})")

        if not has_marker_at_start and c.kind == "quaestio":
            issues.append(f"  {c.label}: no semantic marker within 5 lines of start ({c.line_start})")

        # Check if content from next chunk bleeds into this one
        next_markers = [m for m in dist_markers
                        if m.line > c.line_start and m.line <= c.line_end
                        and m.kind in ("QUAESTIO", "ARTICULUS", "DUBIA")
                        and not m.is_running_head]
        if len(next_markers) > 1:
            extra = next_markers[1:]  # First one is expected (this chunk's marker)
            for em in extra:
                issues.append(
                    f"  {c.label}: contains {em.kind} {em.num or ''} marker at line {em.line} "
                    f"(should be a separate chunk?)"
                )

    # Check for quaestio markers not covered by any chunk.
    # Skip this check for distinctions whose quaestio chunks lack line_start
    # (hand-written Tier-2 chunks in d.1-d.8): we have no reliable mapping,
    # so UNCOVERED would be all noise.
    any_without_range = any(c.line_start == 0 for c in q_chunks)
    if not any_without_range:
        for qm in q_markers:
            covered = any(
                c.line_start <= qm.line <= c.line_end
                for c in q_chunks
            )
            if not covered:
                issues.append(f"  UNCOVERED QUAESTIO marker at line {qm.line}: {qm.raw}")

    # Check for gaps between consecutive quaestio chunks
    sorted_qc = sorted(q_chunks, key=lambda c: c.line_start)
    for i in range(len(sorted_qc) - 1):
        gap = sorted_qc[i + 1].line_start - sorted_qc[i].line_end
        if gap > 50:
            issues.append(
                f"  GAP: {gap} lines between {sorted_qc[i].label} (end {sorted_qc[i].line_end}) "
                f"and {sorted_qc[i+1].label} (start {sorted_qc[i+1].line_start})"
            )
        elif gap < -5:
            issues.append(
                f"  OVERLAP: {abs(gap)} lines between {sorted_qc[i].label} and {sorted_qc[i+1].label}"
            )

    return issues


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--dist", type=int, help="Audit only this distinction")
    ap.add_argument("--part", type=int, choices=[1, 2], help="Volume part (1=d.1-23, 2=d.24-48). Default: pt1.")
    ap.add_argument("--fix", action="store_true", help="Write corrected boundary metadata (not yet implemented)")
    ap.add_argument("--json", action="store_true", help="Output as JSON")
    args = ap.parse_args()

    raw_path = RAW_BY_PART[args.part]
    dist_range_filter = (24, 48) if args.part == 2 else (1, 23) if args.part == 1 else None

    if not raw_path.exists():
        print(f"ERROR: {raw_path} not found", file=sys.stderr)
        sys.exit(1)

    print(f"Raw source: {raw_path.name}")
    text = raw_path.read_text(errors="replace")
    raw_lines = text.split("\n")  # must match marker line counting (\n-based) — splitlines() also splits on form-feed and drifts
    total_lines = len(raw_lines)

    print(f"Raw text: {total_lines} lines")

    markers = find_markers(text)
    print(f"Markers found: {len(markers)}")

    dist_ranges = find_dist_markers(markers)
    print(f"Distinctions found: {len(dist_ranges)} (d.{min(dist_ranges)}–d.{max(dist_ranges)})")

    chunks = load_chunks(args.dist, dist_range_filter)
    print(f"Chunks loaded: {len(chunks)}")

    # Group chunks by distinction
    by_dist: dict[int, list[ChunkInfo]] = {}
    for c in chunks:
        if c.dist:
            by_dist.setdefault(c.dist, []).append(c)

    all_issues = {}
    if args.dist:
        dists_to_check = [args.dist]
    else:
        dists_to_check = sorted(dist_ranges.keys())
        if dist_range_filter:
            dists_to_check = [d for d in dists_to_check if dist_range_filter[0] <= d <= dist_range_filter[1]]

    for d in dists_to_check:
        if d not in dist_ranges:
            continue
        d_chunks = by_dist.get(d, [])
        tier2_count = sum(1 for c in d_chunks if c.tier2)
        total_count = len(d_chunks)

        issues = audit_distinction(d, d_chunks, markers, raw_lines, dist_ranges[d])

        if issues or not d_chunks:
            all_issues[d] = issues
            status = f"({tier2_count}/{total_count} Tier 2)" if d_chunks else "(no chunks)"
            print(f"\nd. {d} {status}:")
            if not issues:
                print("  No boundary issues detected")
            for issue in issues:
                print(issue)
        elif not args.dist:
            # Only show clean dists if auditing a specific one
            pass

    # Summary
    print(f"\n--- Summary ---")
    clean = len(dists_to_check) - len(all_issues)
    print(f"Distinctions audited: {len(dists_to_check)}")
    print(f"Clean: {clean}")
    print(f"With issues: {len(all_issues)}")
    total_issues = sum(len(v) for v in all_issues.values())
    print(f"Total issues: {total_issues}")

    if args.json:
        result = {
            str(d): issues for d, issues in all_issues.items()
        }
        (REPO / "vol1" / "boundary-audit.json").write_text(json.dumps(result, indent=2))
        print(f"\nWrote vol1/boundary-audit.json")


if __name__ == "__main__":
    main()

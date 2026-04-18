#!/usr/bin/env python3.11
"""Fill in missing littera / divisio / dubia chunks from raw text markers.

Scans each distinction's raw-text markers and compares against existing
chunks in vol1/. For any missing littera/divisio/dubia chunk, writes a
skeleton from the inferred line range.

Line-range rules:
  - littera:  from distinction start to first COMMENTARIUS (if found)
  - divisio:  from COMMENTARIUS (or DIVISIO TEXTUS) to first ARTICULUS/QUAESTIO
  - dubia:    from first in-range DUBIA marker to end of distinction

Skips a distinction if its markers are too ambiguous (no COMMENTARIUS
for littera/divisio inference, no DUBIA marker for dubia inference).

Usage:
    python3.11 tools/chunk-fill.py --part 2 --dry-run
    python3.11 tools/chunk-fill.py --part 2
"""
from __future__ import annotations

import argparse
import datetime
import re
import sys
from dataclasses import dataclass
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
VOL1 = REPO / "vol1"
RAW_BY_PART = {
    1: REPO / "raw" / "bonaventure_vol1_raw.txt",
    2: REPO / "raw" / "bonaventure_vol1_pt2_raw.txt",
}

RE_DISTINCTIO = re.compile(r"^[ \t]*DISTINCTIO\S*\s+([IVXLCivxlc]+(?:\s*[IVXLCivxlc])*)\b", re.MULTILINE)
# OCR-tolerant: covers COMMENTARIUS, C0MMENTARIU8, C0MMENTAEIU8, COMMENTAEIUS, C0MMENTARIII8.
RE_COMMENTARIUS = re.compile(r"^[ \t]*C[O0]MMENT[AE][REI]{1,3}[US8]{1,2}\s+IN\s+D", re.MULTILINE)
# OCR-tolerant: DIVISIO / DIVTSIO; TEXTUS / TE.XTUS.
RE_DIVISIO_TEXTUS = re.compile(r"^(?P<line>.*\bDIV[IT]SIO\s+TE\.?XTUS.*)$", re.MULTILINE)
# OCR-tolerant: ARTICULUS/ARTIGULUS + roman (incl. digit-OCR 1/11/111) or UNICUS / UiNICUS / UNIGUS.
RE_ARTICULUS = re.compile(r"^[ \t]*ARTI[CGI]U[L1I]U[S8]\s+([IVXLC1ivxlc]+|U[Ii]?N[IL]?[CG]U[S8])\b", re.MULTILINE)
RE_QUAESTIO = re.compile(r"^[ \t]*Q[UIJij1][A^.flEIJij]{0,6}STIO\s+([IVXLC1ivxlcm]+)\b", re.MULTILINE)
RE_DUBIA = re.compile(r"^[ \t]*(?:.*\bDUBIA\b|DUB[.\s]+[I1]\b[^IVX])", re.MULTILINE)
RE_RUNNING_HEAD = re.compile(r"\bDIST\.\s*[IVXLCivxlc]+", re.IGNORECASE)

ROMAN = {
    "I": 1, "II": 2, "III": 3, "IV": 4, "V": 5, "VI": 6, "VII": 7,
    "VIII": 8, "IX": 9, "X": 10, "XI": 11, "XII": 12, "XIII": 13,
    "XIV": 14, "XV": 15, "XVI": 16, "XVII": 17, "XVIII": 18, "XIX": 19,
    "XX": 20, "XXI": 21, "XXII": 22, "XXIII": 23, "XXIV": 24, "XXV": 25,
    "XXVI": 26, "XXVII": 27, "XXVIII": 28, "XXIX": 29, "XXX": 30,
    "XXXI": 31, "XXXII": 32, "XXXIII": 33, "XXXIV": 34, "XXXV": 35,
    "XXXVI": 36, "XXXVII": 37, "XXXVIII": 38, "XXXIX": 39, "XL": 40,
    "XLI": 41, "XLII": 42, "XLIII": 43, "XLIV": 44, "XLV": 45,
    "XLVI": 46, "XLVII": 47, "XLVIII": 48, "UNICUS": 1,
}


def parse_roman(s: str) -> int | None:
    s = s.strip().replace(" ", "").upper()
    if s in ("1", "11", "111"):
        return len(s)
    if re.fullmatch(r"U[I]?N[IL]?[CG]U[S8]", s):
        return 1
    if s in ROMAN:
        if s == "L":
            return 1
        return ROMAN[s]
    trailing = len(s) - len(s.rstrip("L"))
    for n in range(1, trailing + 1):
        variant = s[:-n] + "I" * n
        if variant in ROMAN:
            return ROMAN[variant]
    return None


def line_num(text: str, pos: int) -> int:
    return text[:pos].count("\n") + 1


def not_running_head(text: str, line: int) -> bool:
    lines = text.split("\n")  # must match line-num counting (\n-based)
    content = lines[line - 1] if 0 < line <= len(lines) else ""
    return not RE_RUNNING_HEAD.search(content)


@dataclass
class DistScan:
    num: int
    start: int
    end: int
    commentarius: list[int]
    divisio_textus: list[int]
    first_articulus: int | None
    first_quaestio: int | None
    dubia: list[int]


def scan_distinctions(text: str) -> dict[int, DistScan]:
    # Build distinctio ranges
    dist_markers = []
    for m in RE_DISTINCTIO.finditer(text):
        num = parse_roman(m.group(1))
        if num:
            dist_markers.append((num, line_num(text, m.start())))
    seen = set()
    unique = []
    for num, line in dist_markers:
        if num not in seen:
            unique.append((num, line))
            seen.add(num)

    ranges = {}
    for i, (num, start) in enumerate(unique):
        end = unique[i + 1][1] - 1 if i + 1 < len(unique) else text.count("\n") + 1
        ranges[num] = (start, end)

    scans = {}
    for num, (s, e) in ranges.items():
        comm = [line_num(text, m.start()) for m in RE_COMMENTARIUS.finditer(text)
                if s <= line_num(text, m.start()) <= e]
        div = [line_num(text, m.start()) for m in RE_DIVISIO_TEXTUS.finditer(text)
               if s <= line_num(text, m.start()) <= e and not_running_head(text, line_num(text, m.start()))]
        arts = [line_num(text, m.start()) for m in RE_ARTICULUS.finditer(text)
                if s <= line_num(text, m.start()) <= e and not_running_head(text, line_num(text, m.start()))]
        qs = [line_num(text, m.start()) for m in RE_QUAESTIO.finditer(text)
              if s <= line_num(text, m.start()) <= e and not_running_head(text, line_num(text, m.start()))]
        dubs = [line_num(text, m.start()) for m in RE_DUBIA.finditer(text)
                if s <= line_num(text, m.start()) <= e]
        scans[num] = DistScan(
            num=num, start=s, end=e,
            commentarius=sorted(comm),
            divisio_textus=sorted(div),
            first_articulus=min(arts) if arts else None,
            first_quaestio=min(qs) if qs else None,
            dubia=sorted(dubs),
        )
    return scans


@dataclass
class ExistingChunk:
    chunk_id: str
    kind: str
    line_start: int
    line_end: int


def load_existing(dist_range: tuple[int, int]) -> dict[int, list[ExistingChunk]]:
    by_dist: dict[int, list[ExistingChunk]] = {}
    for f in sorted(VOL1.glob("bon-sent-I-d*-*.md")):
        text = f.read_text()
        m = re.match(r"---\n(.*?)\n---", text, re.DOTALL)
        if not m:
            continue
        fm = {}
        for line in m.group(1).splitlines():
            if ":" in line:
                k, v = line.split(":", 1)
                fm[k.strip()] = v.strip().strip('"')
        try:
            dist = int(fm.get("distinctio", 0))
        except ValueError:
            continue
        if not (dist_range[0] <= dist <= dist_range[1]):
            continue
        try:
            ls = int(fm.get("line_start", 0))
            le = int(fm.get("line_end", 0))
        except ValueError:
            ls = le = 0
        kind = fm.get("type", "")
        # normalize littera-magistri → littera for presence-checks
        norm = "littera" if kind in ("littera", "littera-magistri") else kind
        by_dist.setdefault(dist, []).append(ExistingChunk(
            chunk_id=f.stem, kind=norm, line_start=ls, line_end=le,
        ))
    return by_dist


def build_skeleton(chunk_id: str, dist: int, kind: str, line_start: int, line_end: int,
                   raw_lines: list[str]) -> str:
    body = "\n".join(raw_lines[line_start - 1:line_end]).strip()
    word_count = len(body.split())
    fm = [
        f'id: "{chunk_id}"',
        "volume: 1",
        "book: 1",
        f"distinctio: {dist}",
        f"type: {kind}",
        f"line_start: {line_start}",
        f"line_end: {line_end}",
        f"word_count_latin: {word_count}",
        f'transcription_status: "auto-chunked {datetime.date.today()} (chunk-fill)"',
        "format_version: 1",
    ]
    return f"""---
{chr(10).join(fm)}
---

# {chunk_id}

## Latin

{body}

## English

[Translation pending]

## Apparatus

[Apparatus pending]

## Notes

[Notes pending]
"""


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--part", type=int, choices=[1, 2], required=True)
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    raw_path = RAW_BY_PART[args.part]
    text = raw_path.read_text(errors="replace")
    raw_lines = text.split("\n")  # must match line-num counting (\n-based) — splitlines() also splits on form-feed and drifts
    scans = scan_distinctions(text)

    dist_range = (24, 48) if args.part == 2 else (1, 23)
    existing = load_existing(dist_range)

    new_chunks: list[tuple[Path, str, str]] = []
    for dist in range(dist_range[0], dist_range[1] + 1):
        scan = scans.get(dist)
        if not scan:
            continue
        chunks = existing.get(dist, [])
        kinds = {c.kind for c in chunks}

        # littera — anchor at first of COMMENTARIUS, DIVISIO TEXTUS, ARTICULUS, QUAESTIO
        if "littera" not in kinds:
            anchor_candidates = []
            if scan.commentarius:
                anchor_candidates.append(scan.commentarius[0])
            if scan.divisio_textus:
                anchor_candidates.append(scan.divisio_textus[0])
            if scan.first_articulus:
                anchor_candidates.append(scan.first_articulus)
            if scan.first_quaestio:
                anchor_candidates.append(scan.first_quaestio)
            if anchor_candidates:
                ls = scan.start
                le = min(anchor_candidates) - 1
                if le - ls >= 20:
                    cid = f"bon-sent-I-d{dist}-littera"
                    path = VOL1 / f"{cid}.md"
                    if not path.exists():
                        new_chunks.append((path, "littera", f"{dist}: lines {ls}–{le} ({le-ls+1} lines)"))
                        if not args.dry_run:
                            path.write_text(build_skeleton(cid, dist, "littera", ls, le, raw_lines))
                else:
                    print(f"  d.{dist} littera: range too short ({le-ls+1} lines) — SKIP")
            else:
                print(f"  d.{dist} littera: no anchor (COMM/DIVISIO/ART/QUAEST) — SKIP")

        # divisio — start at COMMENTARIUS or DIVISIO TEXTUS, end before first ARTICULUS/QUAESTIO
        if "divisio" not in kinds:
            start_candidates = []
            if scan.commentarius:
                start_candidates.append(scan.commentarius[0])
            if scan.divisio_textus:
                start_candidates.append(scan.divisio_textus[0])
            divisio_start = min(start_candidates) if start_candidates else None
            end_candidates = [x for x in (scan.first_articulus, scan.first_quaestio) if x and (not divisio_start or x > divisio_start)]
            if divisio_start and end_candidates:
                le = min(end_candidates) - 1
                ls = divisio_start
                if le - ls >= 10:
                    cid = f"bon-sent-I-d{dist}-divisio"
                    path = VOL1 / f"{cid}.md"
                    if not path.exists():
                        new_chunks.append((path, "divisio", f"{dist}: lines {ls}–{le} ({le-ls+1} lines)"))
                        if not args.dry_run:
                            path.write_text(build_skeleton(cid, dist, "divisio", ls, le, raw_lines))
                else:
                    print(f"  d.{dist} divisio: range too short ({le-ls+1} lines) — SKIP")
            else:
                print(f"  d.{dist} divisio: cannot anchor — SKIP")

        # dubia
        if "dubia" not in kinds and scan.dubia:
            ls = scan.dubia[0]
            le = scan.end
            if le - ls >= 20:
                cid = f"bon-sent-I-d{dist}-dubia"
                path = VOL1 / f"{cid}.md"
                if not path.exists():
                    new_chunks.append((path, "dubia", f"{dist}: lines {ls}–{le} ({le-ls+1} lines)"))
                    if not args.dry_run:
                        path.write_text(build_skeleton(cid, dist, "dubia", ls, le, raw_lines))

    if not new_chunks:
        print("Nothing to fill.")
        return

    print(f"\n{len(new_chunks)} chunks {'would be created' if args.dry_run else 'created'}:")
    for p, k, desc in new_chunks:
        print(f"  {p.name}  ({k})  [{desc}]")


if __name__ == "__main__":
    main()

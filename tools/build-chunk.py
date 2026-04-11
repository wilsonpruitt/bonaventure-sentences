#!/usr/bin/env python3.11
"""
build-chunk.py — scaffold a unified-format chunk file from a legacy chunk
plus page images.

Given a legacy chunk id (or a path to a legacy chunk file), this script:

1. Parses the legacy frontmatter to extract id, book/dist/art/quaestio,
   type, and any existing title.
2. Reads the legacy Latin body and includes it as a starting point for
   the Latin section (marked clearly as pending vision-OCR cleanup).
3. Verifies that the page images for the chunk exist in raw/vision/<vol>/;
   if not, prints the exact extract-pages.py command to produce them.
4. Writes a new unified-format skeleton to vol<N>/<chunk-id>.md (or a
   user-supplied --output path). The skeleton contains:
     - Complete frontmatter with title_la / title_en placeholders,
       printed_pages and pdf_pages arrays, source, has_scholion/apparatus
       booleans, transcription_status, format_version.
     - ## Latin section with page-break HTML comments at each printed-page
       boundary and the legacy Latin body embedded as a starting point.
     - ## English section with "[Translation pending]" placeholder.
     - ## Apparatus section empty (pre-populated from tools/apparatus-
       translate.py when apparatus text is available).
     - ## Notes section with boilerplate fields.
5. Prints a human-readable next-steps summary: which pages to OCR, what
   to translate, etc.

This script is deliberately NON-destructive: it refuses to overwrite an
existing file unless --force is passed, and it only writes to the output
path, never modifies the legacy chunk.

Usage:
    # Scaffold a rebuild of dist. 2, art. 1, q. 1 covering pp. 48-51:
    python3.11 tools/build-chunk.py \\
        --legacy vol1/legacy/bon-sent-I-d2-a1-q1.md \\
        --pages 48-51 \\
        --title-la "Utrum in divinis sit personarum pluralitas" \\
        --output vol1/bon-sent-I-d2-a1-q1.md

    # Scaffold a new chunk from scratch (no legacy file):
    python3.11 tools/build-chunk.py \\
        --new bon-sent-I-d5-a2-q3 \\
        --book 1 --dist 5 --art 2 --quaestio 3 \\
        --pages 112-115 \\
        --title-la "Utrum generatio..." \\
        --output vol1/bon-sent-I-d5-a2-q3.md
"""

from __future__ import annotations

import argparse
import re
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent

# Vol I offset (matches extract-pages.py).
VOLUME_OFFSETS = {"vol1": 102}


# ----------------------------------------------------------------------------
# Legacy frontmatter parsing
# ----------------------------------------------------------------------------

FRONTMATTER_RE = re.compile(r"^---\n(.*?)\n---\n", re.DOTALL)


@dataclass
class LegacyChunk:
    id: str
    volume: int
    book: int
    distinctio: int
    articulus: int | None = None
    pars: int | None = None
    quaestio: int | None = None
    type: str = "quaestio"
    title: str = ""
    latin_body: str = ""
    raw_file: Path | None = None


def parse_yaml_simple(text: str) -> dict[str, str]:
    """
    Micro YAML parser for the flat key: value frontmatter the legacy
    chunks use. Doesn't handle nested objects or block scalars — we don't
    need them here.
    """
    out: dict[str, str] = {}
    for line in text.splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        key = key.strip()
        value = value.strip().strip('"').strip("'")
        out[key] = value
    return out


def read_legacy_chunk(path: Path) -> LegacyChunk:
    text = path.read_text(encoding="utf-8")
    fm_match = FRONTMATTER_RE.match(text)
    if not fm_match:
        raise ValueError(f"{path}: no YAML frontmatter found")
    fm = parse_yaml_simple(fm_match.group(1))

    # Extract the Latin body: everything between "### Latin" or "## Latin"
    # and the next H2/H3 (or end of file).
    body = text[fm_match.end():]
    latin_match = re.search(
        r"###?\s*Latin\s*\n(.*?)(?=\n###?\s*(?:English|Notes|Apparatus|Scholion)|\Z)",
        body, re.DOTALL,
    )
    latin_body = latin_match.group(1).strip() if latin_match else ""

    def _int_or_none(key: str) -> int | None:
        v = fm.get(key)
        if v is None or v == "":
            return None
        try:
            return int(v)
        except ValueError:
            return None

    return LegacyChunk(
        id=fm.get("id", path.stem),
        volume=int(fm.get("volume", "1")),
        book=int(fm.get("book", "1")),
        distinctio=int(fm.get("distinctio", "0")),
        articulus=_int_or_none("articulus"),
        pars=_int_or_none("pars"),
        quaestio=_int_or_none("quaestio"),
        type=fm.get("type", "quaestio"),
        title=fm.get("title", ""),
        latin_body=latin_body,
        raw_file=path,
    )


# ----------------------------------------------------------------------------
# Page image verification
# ----------------------------------------------------------------------------

def verify_page_images(volume: str, pages: list[int]) -> list[int]:
    """Return the subset of `pages` that do NOT have an extracted image."""
    missing = []
    for p in pages:
        img = REPO_ROOT / "raw" / "vision" / volume / f"p-{p:03d}.png"
        if not img.exists():
            missing.append(p)
    return missing


def parse_pages(spec: str) -> list[int]:
    """Parse '32-34' or '32,35-37' into a sorted list of ints."""
    pages: list[int] = []
    for seg in spec.split(","):
        seg = seg.strip()
        if "-" in seg:
            lo, hi = seg.split("-", 1)
            pages.extend(range(int(lo), int(hi) + 1))
        else:
            pages.append(int(seg))
    return sorted(set(pages))


# ----------------------------------------------------------------------------
# Skeleton rendering
# ----------------------------------------------------------------------------

def roman(book: int) -> str:
    return {1: "I", 2: "II", 3: "III", 4: "IV"}.get(book, str(book))


def format_title_header(chunk: LegacyChunk) -> str:
    """
    Generate the '# I Sent., d. N, a. M, q. K' header line from structured
    frontmatter, matching the convention used in the rebuilt chunks.
    """
    parts = [f"{roman(chunk.book)} Sent., d. {chunk.distinctio}"]
    if chunk.pars is not None:
        parts.append(f"p. {chunk.pars}")
    if chunk.articulus is not None:
        parts.append(f"a. {chunk.articulus}")
    if chunk.quaestio is not None:
        if chunk.type == "quaestio":
            parts.append(f"q. {chunk.quaestio}")
    if chunk.type == "dubia":
        parts.append("Dubia")
    return ", ".join(parts)


def render_skeleton(
    chunk: LegacyChunk,
    pages: list[int],
    title_la: str,
    title_en: str = "",
    volume_key: str = "vol1",
) -> str:
    """Render the full unified-format markdown skeleton as a string."""
    offset = VOLUME_OFFSETS[volume_key]
    pdf_pages = [p + offset for p in pages]
    pages_str = ", ".join(str(p) for p in pages)
    pdf_pages_str = ", ".join(str(p) for p in pdf_pages)
    header = format_title_header(chunk)

    # Frontmatter
    lines = [
        "---",
        f'id: "{chunk.id}"',
        f"volume: {chunk.volume}",
        f"book: {chunk.book}",
        f"distinctio: {chunk.distinctio}",
    ]
    if chunk.pars is not None:
        lines.append(f"pars: {chunk.pars}")
    if chunk.articulus is not None:
        lines.append(f"articulus: {chunk.articulus}")
    if chunk.quaestio is not None:
        lines.append(f"quaestio: {chunk.quaestio}")
    lines += [
        f"type: {chunk.type}",
        f'title_la: "{title_la}"',
        f'title_en: "{title_en or "[pending]"}"',
        f"printed_pages: [{pages_str}]",
        f"pdf_pages: [{pdf_pages_str}]",
        f'source: "S. Bonaventurae, Opera Omnia, Tomus {roman(chunk.volume)} '
        f'(Quaracchi, 1882), pp. {pages[0]}\u2013{pages[-1]}"',
        "has_scholion: true",
        "has_apparatus: true",
        'transcription_status: "scaffolded, Latin body from legacy raw OCR, English pending"',
        "format_version: 1",
        "---",
        "",
        f"# {header}",
        f"## *{title_la}*",
        "",
        "---",
        "",
        "## Latin",
        "",
    ]

    # Legacy Latin body, with page-break comments dropped at the start.
    # The translator will clean up OCR artifacts and insert additional
    # page-break comments inside the body during the rebuild pass.
    lines.append(f"<!-- page {pages[0]} -->")
    lines.append("")
    if chunk.latin_body:
        lines.append(
            "<!-- BEGIN legacy raw OCR — clean against the extracted page "
            "images and insert <!-- page N --> comments at each printed-page "
            "boundary. Remove this begin/end marker once the body is clean. -->"
        )
        lines.append("")
        lines.append(chunk.latin_body)
        lines.append("")
        lines.append("<!-- END legacy raw OCR -->")
    else:
        lines.append("*[Latin body pending vision OCR of pp. "
                     f"{pages[0]}\u2013{pages[-1]}]*")
    lines.append("")

    lines += [
        "### Scholion",
        "",
        "*[Scholion text pending, typically at the end of the question on "
        f"printed p. {pages[-1]}]*",
        "",
        "---",
        "",
        "## English",
        "",
        "*[Translation pending.]*",
        "",
        "---",
        "",
        "## Apparatus",
        "",
        "> The numbered footnotes below correspond to markers in both the "
        "Latin body above and the English translation. Each entry gives the "
        "Quaracchi critical apparatus in Latin, followed by an English "
        "rendering produced by `tools/apparatus-translate.py` (with manual "
        "polish where the script's draft was awkward).",
        "",
        "*[Apparatus entries pending. Extract from the bottom of each printed "
        "page and run `python3.11 tools/apparatus-translate.py` on the block "
        "to get draft English.]*",
        "",
        "---",
        "",
        "## Notes",
        "",
        f"- **Chunk scope.** This chunk covers {header} on printed pp. "
        f"{pages[0]}\u2013{pages[-1]} (PDF pp. {pdf_pages[0]}\u2013{pdf_pages[-1]}).",
        "",
        "- **Key terms** (per project glossary): *[list project-glossary "
        "terms that appear in this chunk — see `translation-prompt.md`]*.",
        "",
        "- **Vision transcription status.** Scaffolded from legacy raw OCR "
        f"(`{chunk.raw_file.name if chunk.raw_file else 'n/a'}`). The Latin body "
        "in this file should be cleaned against the extracted page images "
        f"in `raw/vision/{volume_key}/p-NNN.png` for pp. "
        f"{pages[0]}\u2013{pages[-1]} before the translation pass, and the "
        "transcription_status field in the frontmatter should be updated to "
        "`\"first-pass vision, pending final verification\"` once that cleanup is done.",
        "",
    ]

    return "\n".join(lines)


# ----------------------------------------------------------------------------
# CLI
# ----------------------------------------------------------------------------

def main() -> int:
    parser = argparse.ArgumentParser(
        description=(
            "Scaffold a unified-format chunk file from a legacy chunk plus "
            "page images. Non-destructive: never overwrites an existing "
            "output file unless --force is passed."
        )
    )
    parser.add_argument(
        "--legacy", type=Path,
        help="Path to a legacy chunk file to rebuild (e.g. vol1/legacy/bon-sent-I-d2-a1-q1.md)",
    )
    parser.add_argument(
        "--new", type=str,
        help="Create a new chunk from scratch with this id (mutually exclusive with --legacy)",
    )
    parser.add_argument(
        "--book", type=int, default=1,
        help="Book number (used only with --new)",
    )
    parser.add_argument(
        "--dist", type=int,
        help="Distinction number (required with --new)",
    )
    parser.add_argument(
        "--pars", type=int,
        help="Pars number (optional, used for II Sent. and III Sent.)",
    )
    parser.add_argument(
        "--art", type=int,
        help="Article number (optional)",
    )
    parser.add_argument(
        "--quaestio", type=int,
        help="Question number (optional)",
    )
    parser.add_argument(
        "--type", type=str, default="quaestio", choices=["quaestio", "dubia", "littera-magistri"],
        help="Chunk type",
    )
    parser.add_argument(
        "--pages", required=True,
        help="Printed page range the chunk covers (e.g. 48-51 or 48,52-54)",
    )
    parser.add_argument(
        "--title-la", required=True,
        help="Latin title of the chunk (the question's *Utrum...*)",
    )
    parser.add_argument(
        "--title-en", default="",
        help="English title (optional — leave blank to mark as [pending])",
    )
    parser.add_argument(
        "--output", "-o", type=Path, required=True,
        help="Output path for the generated skeleton",
    )
    parser.add_argument(
        "--volume", default="vol1", choices=sorted(VOLUME_OFFSETS.keys()),
        help="Volume key for page-offset calculation and image lookup",
    )
    parser.add_argument(
        "--force", action="store_true",
        help="Overwrite output file if it already exists",
    )
    args = parser.parse_args()

    if bool(args.legacy) == bool(args.new):
        print("error: pass exactly one of --legacy or --new", file=sys.stderr)
        return 1

    try:
        pages = parse_pages(args.pages)
    except ValueError as e:
        print(f"error: invalid --pages: {e}", file=sys.stderr)
        return 1

    # Build a LegacyChunk either from a file or from --new args.
    if args.legacy:
        if not args.legacy.exists():
            print(f"error: legacy file not found: {args.legacy}", file=sys.stderr)
            return 1
        chunk = read_legacy_chunk(args.legacy)
    else:
        if args.dist is None:
            print("error: --dist is required with --new", file=sys.stderr)
            return 1
        chunk = LegacyChunk(
            id=args.new,
            volume=args.book,  # Vol = book in this project
            book=args.book,
            distinctio=args.dist,
            pars=args.pars,
            articulus=args.art,
            quaestio=args.quaestio,
            type=args.type,
        )

    # Sanity check output path.
    if args.output.exists() and not args.force:
        print(
            f"error: output file exists: {args.output}\n"
            f"       pass --force to overwrite",
            file=sys.stderr,
        )
        return 1

    # Verify page images exist and warn (not error) if any are missing.
    missing = verify_page_images(args.volume, pages)
    if missing:
        missing_spec = ",".join(str(m) for m in missing)
        print(
            f"warning: {len(missing)} page image(s) missing from "
            f"raw/vision/{args.volume}/: {missing_spec}",
            file=sys.stderr,
        )
        print(
            f"  run: python3.11 tools/extract-pages.py --volume {args.volume} "
            f"--pages {missing_spec}",
            file=sys.stderr,
        )

    # Render and write the skeleton.
    skeleton = render_skeleton(
        chunk, pages,
        title_la=args.title_la,
        title_en=args.title_en,
        volume_key=args.volume,
    )
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(skeleton, encoding="utf-8")

    # Next-steps summary.
    print(f"Scaffolded: {args.output}")
    print(f"  chunk id:     {chunk.id}")
    print(f"  type:         {chunk.type}")
    print(f"  pages:        {pages[0]}\u2013{pages[-1]} (PDF "
          f"{pages[0] + VOLUME_OFFSETS[args.volume]}\u2013"
          f"{pages[-1] + VOLUME_OFFSETS[args.volume]})")
    print(f"  legacy Latin: "
          f"{'embedded' if chunk.latin_body else 'none (new chunk)'}")
    print()
    print("Next steps:")
    if missing:
        print(f"  1. Extract missing page images (see warning above)")
    print(f"  {'2' if missing else '1'}. Clean the Latin body against "
          f"raw/vision/{args.volume}/p-NNN.png for pp. {pages[0]}\u2013{pages[-1]}")
    print(f"  {'3' if missing else '2'}. Translate the body: "
          f"Latin → English")
    print(f"  {'4' if missing else '3'}. Extract apparatus entries and run "
          "tools/apparatus-translate.py on them")
    print(f"  {'5' if missing else '4'}. Update transcription_status in "
          "frontmatter once the body is clean")
    return 0


if __name__ == "__main__":
    sys.exit(main())

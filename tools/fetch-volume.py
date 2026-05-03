#!/usr/bin/env python3.11
"""Fetch a Bonaventure Opera Omnia volume from the Internet Archive
and produce raw text via pdftotext.

No external Python deps — uses curl + pdftotext (both available on the system).

Usage:
  # Fetch a volume using the default identifier guess
  python3.11 tools/fetch-volume.py 1 2          # Vol 1 part 2 → doctorisseraphic12bona
  python3.11 tools/fetch-volume.py 2            # Vol 2 (no part) → doctorisseraphic2bona

  # Override the identifier (use this after IA spot-check if naming differs)
  python3.11 tools/fetch-volume.py 5 --id bonaventureopera05bona

  # Dry-run: show what URL would be fetched, don't download
  python3.11 tools/fetch-volume.py 3 --dry-run

Output:
  raw/<identifier>.pdf
  raw/bonaventure_vol<N>[_pt<P>]_raw.txt
"""
import argparse
import shutil
import subprocess
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
RAW = REPO / "raw"
RAW.mkdir(exist_ok=True)


def default_identifier(vol: int, part: int | None) -> str:
    if part:
        return f"doctorisseraphic{vol}{part}bona"
    return f"doctorisseraphic{vol}bona"


def ia_pdf_url(identifier: str) -> str:
    return f"https://archive.org/download/{identifier}/{identifier}.pdf"


def fetch_pdf(url: str, dest: Path) -> None:
    if dest.exists() and dest.stat().st_size > 1_000_000:
        print(f"  PDF already present: {dest.name} ({dest.stat().st_size // 1024 // 1024} MB)")
        return
    print(f"  Downloading {url} → {dest.name}")
    result = subprocess.run(
        ["curl", "-L", "--fail", "--progress-bar", "-o", str(dest), url],
        check=False,
    )
    if result.returncode != 0:
        if dest.exists():
            dest.unlink()
        print(
            f"\n  ERROR: curl exit {result.returncode}. "
            f"Identifier may be wrong — verify at https://archive.org/details/{Path(url).stem}",
            file=sys.stderr,
        )
        sys.exit(1)
    size_mb = dest.stat().st_size // 1024 // 1024
    if size_mb < 5:
        print(f"  WARNING: downloaded file is only {size_mb} MB; likely an HTML error page.")
        sys.exit(1)
    print(f"  Got {size_mb} MB")


def extract_text(pdf: Path, txt: Path) -> None:
    if txt.exists() and txt.stat().st_size > 1000:
        print(f"  Raw text already present: {txt.name} ({txt.stat().st_size // 1024} KB)")
        return
    print(f"  pdftotext -layout {pdf.name} → {txt.name}")
    subprocess.run(
        ["pdftotext", "-layout", str(pdf), str(txt)],
        check=True,
    )
    word_count = len(txt.read_text(errors="replace").split())
    print(f"  Extracted {word_count:,} words")


def report(txt: Path) -> None:
    text = txt.read_text(errors="replace")
    import re

    distinctios = len(re.findall(r"^DISTINCTIO\s+[IVXLC]+\.?\s*$", text, re.MULTILINE))
    quaestios = len(re.findall(r"QU[A^.flE]{1,4}STIO|QIIAESTIO", text))
    articulus = len(re.findall(r"ARTI[CG]ULUS", text))
    dubia = len(re.findall(r"^DUB\.|^DuB\.", text, re.MULTILINE))
    print("\n  Markers detected (sanity check):")
    print(f"    DISTINCTIO: {distinctios}")
    print(f"    QUAESTIO:   {quaestios}")
    print(f"    ARTICULUS:  {articulus}")
    print(f"    DUB.:       {dubia}")


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("volume", type=int, help="Volume number (1–10)")
    ap.add_argument("part", type=int, nargs="?", default=None, help="Part number (e.g. 2 for Vol I pt 2)")
    ap.add_argument("--id", dest="identifier", help="Override IA identifier")
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    identifier = args.identifier or default_identifier(args.volume, args.part)
    url = ia_pdf_url(identifier)

    suffix = f"_pt{args.part}" if args.part else ""
    pdf = RAW / f"{identifier}.pdf"
    txt = RAW / f"bonaventure_vol{args.volume}{suffix}_raw.txt"

    print(f"Volume {args.volume}{f' part {args.part}' if args.part else ''}")
    print(f"  IA identifier: {identifier}")
    print(f"  URL:           {url}")
    print(f"  PDF target:    {pdf.relative_to(REPO)}")
    print(f"  Raw target:    {txt.relative_to(REPO)}")

    if args.dry_run:
        print("\n(dry-run; no download)")
        return

    if not shutil.which("pdftotext"):
        print("ERROR: pdftotext not on PATH. Install poppler: brew install poppler", file=sys.stderr)
        sys.exit(1)

    fetch_pdf(url, pdf)
    extract_text(pdf, txt)
    report(txt)
    print(f"\nDone. Next: chunk this volume (template: tools/rechunk_d9.py).")


if __name__ == "__main__":
    main()

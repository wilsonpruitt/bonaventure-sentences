#!/usr/bin/env python3.11
"""Triage Quaracchi internal cross-references (`supra/infra pag. N, nota M`).

WHY THIS EXISTS (2026-08-24).  Cross-refs are short digit strings with no
semantic redundancy, so a single OCR slip yields a reference that is still
well-formed and still resolves -- silently, to the wrong note.  Twelve such
errors were found and fixed by hand against plates; see AUDIT-QUEUE.md.

WHAT THIS CAN AND CANNOT DO -- read before trusting the output.

  CAN:  report references whose target PAGE is not covered by the volume's
        chunks.  A ref into a page inside the transcribed range that no chunk
        carries is worth a look (bad digit, or a real transcription gap).

  CANNOT: verify the `nota M` half.  An obvious-looking check -- "does page N
        carry at least M notes?" -- was written, and it is UNSOUND for Vol I.
        Quaracchi's footer band on page N is not the set of notes anchored in
        page N's body: when a band overflows it runs over, so page N's printed
        notes 1..k routinely belong to markers on page N-1 and are stored in
        the PREVIOUS chunk under its own sequential labels.  Measured case:
        p. 546 prints 8 notes; our chunks anchor exactly 1 marker on it (which
        is the printed note 8), the other 7 being p. 545's runover.  A
        note-count check therefore flags correct references as impossible --
        `546, nota 2` is right, and was confirmed on the plate.

  The root cause is structural: Vol I's apparatus labels are sequential within
  a chunk (`[^7]`), so nothing records which printed page an entry belongs to.
  Vol V solved this with page-qualified labels (`[^p447-3]`), which is what
  lets `check-vol5-apparatus.py` do real per-page verification.  Until Vol I is
  page-qualified, the `nota` half of every cross-reference can only be settled
  against the plate.

  Plate, no PDF needed (Vol I pt 2, leaf = printed - 411):
    https://archive.org/download/doctorisseraphic12bona/page/n<leaf>.jpg

Usage:  python3.11 tools/check-xref-pages.py [vol1 ...]
Exit 1 if anything is reported.
"""
import re, sys, glob

REF  = re.compile(r'\b(?:supra|infra)\s+pag\.\s*(\d{1,3})\s*,\s*nota\s+(\d{1,2})\b')
PAGE = re.compile(r'<!--\s*page\s+(\d+)\s*-->')

def scan(vol):
    pages, refs = set(), []
    for f in sorted(glob.glob(f'{vol}/*.md')):
        for i, l in enumerate(open(f, encoding='utf-8').read().split('\n'), 1):
            m = PAGE.search(l)
            if m:
                pages.add(int(m.group(1)))
            for r in REF.finditer(l):
                refs.append((f, i, int(r.group(1)), int(r.group(2)), l.strip()[:88]))
    return pages, refs

def main(vols):
    rc = 0
    for vol in vols:
        pages, refs = scan(vol)
        if not pages:
            print(f'{vol}: no page markers found'); continue
        lo, hi = min(pages), max(pages)
        gaps = [r for r in refs if r[2] not in pages and lo <= r[2] <= hi]
        out  = [r for r in refs if not (lo <= r[2] <= hi)]
        print(f'\n=== {vol}: {len(refs)} cross-refs; pages {lo}-{hi}, '
              f'{len(pages)} transcribed ===')
        for f, ln, pg, nota, ctx in gaps:
            rc = 1
            print(f'  [NOPAGE] {f.split("/")[-1]}:{ln} -> p. {pg} is in range '
                  f'but no chunk carries it (ref wants nota {nota})\n      {ctx}')
        if out:
            print(f'  [OUTSIDE] {len(out)} ref(s) point outside {lo}-{hi} '
                  f'(not yet transcribed): '
                  + ', '.join(sorted({str(r[2]) for r in out})))
        if not gaps:
            print('  no references into missing in-range pages.')
        print('  NOTE: the `nota M` half is NOT checked here and cannot be -- '
              'see this file\'s docstring. Plates remain the only authority.')
    return rc

if __name__ == '__main__':
    sys.exit(main(sys.argv[1:] or ['vol1']))

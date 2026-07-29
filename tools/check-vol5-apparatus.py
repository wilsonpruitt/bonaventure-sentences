#!/usr/bin/env python3.11
"""Vol V apparatus integrity check.

`audit-apparatus-count.py` is BLIND to Vol V: that script counts footer-note
openers in the raw OCR, and Vol V's OCR renders every superscript numeral as a
punctuation glyph (^ ' ") — so there is nothing for it to match. This script
replaces it with checks that do not depend on the raw at all.

It verifies three things across `vol5/*.md`:

  1. LABEL PAIRING — every `[^id]:` definition in ## Apparatus has exactly one
     matching anchor in the ## Latin body and one in the ## English body.
     (A mismatch means an entry will render detached or silently vanish.)

  2. DUPLICATE DEFS — no `[^id]:` is defined twice in one file. Quaracchi
     restarts footnote numbering on every printed page, so bare numbers would
     collide; labels are page-qualified (`[^p214-5]`) to prevent exactly this.
     A duplicate silently drops an entry at render time.

  3. FOOTER OWNERSHIP — across all chunks, each printed page's notes must run
     1..N with no gaps and no page claimed twice for the same number. A GAP
     means a note is owned by nobody (the failure mode that cost Vol IV three
     whole registers); a DOUBLE means two chunks claim the same note.

Gaps at the TOP of a page's range are expected while work is in progress — the
last note(s) of a page are often forwarded to the next, not-yet-written chunk.
Those show as a trailing shortfall, not an interior gap, and are reported
separately as PENDING rather than as an error.

Usage:  python3.11 tools/check-vol5-apparatus.py [--expect-max PAGE=N ...]
Exit code is 1 if any interior gap, duplicate, double-claim, or pairing
mismatch is found; 0 otherwise.
"""
import glob
import os
import re
import sys
from collections import defaultdict

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
VOL5 = os.path.join(REPO_ROOT, "vol5")

# Printed-page → true total number of footer notes, where known from an
# eyes-on band read. Lets the script distinguish "still pending" from "lost".
KNOWN_TOTALS = {
    205: 8,
    206: 11,
    207: 8,
    208: 7,   # prologue ends here; nothing forwarded
    201: 5,
    202: 10,
    203: 8,
    204: 9,   # nn.8-9 are § 3's — pending until prol-s3 lands
    210: 8,
    211: 7,
    212: 7,
    213: 7,
    214: 9,
    215: 6,
    216: 6,
    217: 7,
    218: 7,   # Pars I ends here; nothing forwarded
    219: 5,   # Pars II opens; nn.1-3 Cap. I, nn.4-5 Cap. II
    220: 6,   # nn.1-5 Cap. II, n.6 Cap. III
    221: 7,   # nn.1-3 Cap. III, nn.4-7 Cap. IV; page fully consumed
    222: 5,   # nn.1-2 Cap. IV (tail), nn.3-5 Cap. V
    223: 9,   # all nine Cap. V
    224: 8,   # nn.1-7 Cap. VI, n.8 Cap. VII
    225: 7,   # nn.1-4 Cap. VII, nn.5-7 Cap. VIII; page fully consumed
    226: 9,   # nn.1-5 Cap. VIII, nn.6-9 Cap. IX; page fully consumed
    227: 9,   # all nine Cap. IX; Cap. X opens on this page but claims no note
    228: 9,   # all nine Cap. X; page fully consumed
    229: 8,   # all eight Cap. XI; page fully consumed
    230: 7,   # n.1 Cap. XI, nn.2-7 Cap. XII; PARS II ends here, nothing forwarded
    231: 7,   # PARS III opens: nn.1-6 Cap. I, n.7 Cap. II (forwarded to p3-c2)
    232: 9,   # nn.1-7 Cap. II, nn.8-9 Cap. III (forwarded to p3-c3)
    233: 5,   # nn.1-3 Cap. III, nn.4-5 Cap. IV (forwarded to p3-c4)
    234: 9,   # nn.1-2 Cap. IV, nn.3-9 Cap. V; page fully consumed
    235: 7,   # n.1 Cap. V, nn.2-7 Cap. VI; page fully consumed
    236: 7,   # nn.1-6 Cap. VII, n.7 Cap. VIII (forwarded to p3-c8)
    237: 9,   # band-read while closing the p.236->p.237 runover test, then
              # re-read in full by p3-c8: nn.1-3 left block, nn.4-9 right,
              # but SIX of the nine (nn.1-6) anchor in the LEFT column -- a
              # three-note UNDERRUN of the column division. Capp. VIII AND IX
              # both sit on this page, yet ALL NINE notes are Cap. VIII's;
              # Cap. IX claims none. Page fully consumed by p3-c8.
    238: 8,   # band-read in full by p3-c9: nn.1-4 left block (n.4 broken
              # MID-WORD at "Amor ergo... fu-"), right block opens with n.4's
              # unnumbered continuation then nn.5-8. Anchors track the blocks
              # exactly here (nn.1-4 left, nn.5-8 right) -- a COINCIDENCE page
              # whose split falls INSIDE a note, the p.236 shape repeated.
              # nn.1-7 Cap. IX, n.8 Cap. X (forwarded to p3-c10).
    239: 9,   # band-read in full by p3-c10: nn.1-4 left block (n.4 broken at a
              # WORD boundary at "...II. Sent. d. 35. per totam, ubi etiam"),
              # right block opens with n.4's unnumbered continuation then
              # nn.5-9. But nn.1-6 ALL anchor in the LEFT column, so nn.5-6
              # anchor left and print right -- a one-note OVERRUN on top of a
              # split falling INSIDE a note. All nine are Cap. X's; the page is
              # fully consumed by p3-c10 and nothing is forwarded.
    240: 9,   # band-read in full by p3-c11: nn.1-4 left block (n.4 broken at a
              # PUNCTUATION boundary, after the colon of "Ibid. III. c. 3. n. 7:"),
              # right block opens with n.4's unnumbered continuation then nn.5-9.
              # Anchors and blocks COINCIDE exactly here (nn.1-4 left, nn.5-9
              # right) -- the p.238 shape, not p.239's overrun. All nine are
              # Cap. XI's; page fully consumed by p3-c11.
    241: 10,  # band-read in full by p3-c11, but split by PARS, not by block:
              # left block nn.1-5 (+ the printer's signature), right block
              # nn.6-10, both closing complete. nn.1-2 anchor in Pars III
              # Cap. XI's closing paragraph (owned by p3-c11); nn.3-10 anchor
              # in PARS QUARTA Cap. I and are a legitimate forwarded PENDING
              # until bon-brev-p4-c1 lands.
}


def section(text, name):
    """Return the body of a `## name` section, up to the next `## ` heading."""
    m = re.search(r"^## %s\s*$" % re.escape(name), text, re.M)
    if not m:
        return ""
    rest = text[m.end():]
    nxt = re.search(r"^## ", rest, re.M)
    return rest[: nxt.start()] if nxt else rest


def main():
    expect = dict(KNOWN_TOTALS)
    for arg in sys.argv[1:]:
        if arg.startswith("--expect-max"):
            _, _, spec = arg.partition("=")
            pg, _, n = spec.partition(":")
            if pg and n:
                expect[int(pg)] = int(n)

    files = sorted(glob.glob(os.path.join(VOL5, "*.md")))
    if not files:
        print("no chunks in vol5/ — nothing to check")
        return 0

    owners = defaultdict(dict)   # page -> {note_number: [chunk, ...]}
    problems = []
    unregistered = []
    total_entries = 0

    print("Per-chunk label pairing")
    print("-" * 62)
    for path in files:
        name = os.path.basename(path)
        text = open(path, encoding="utf-8").read()
        la = section(text, "Latin")
        en = section(text, "English")
        app = section(text, "Apparatus")

        defs = re.findall(r"^\[\^([^\]]+)\]:", app, re.M)
        la_anchors = re.findall(r"\[\^([^\]]+)\]", la)
        en_anchors = re.findall(r"\[\^([^\]]+)\]", en)
        total_entries += len(defs)

        dupes = sorted({d for d in defs if defs.count(d) > 1})
        if dupes:
            problems.append("%s: DUPLICATE defs %s" % (name, dupes))

        paired = sorted(defs) == sorted(la_anchors) == sorted(en_anchors)
        if not paired:
            missing_la = sorted(set(defs) - set(la_anchors))
            missing_en = sorted(set(defs) - set(en_anchors))
            orphan = sorted((set(la_anchors) | set(en_anchors)) - set(defs))
            detail = []
            if missing_la:
                detail.append("no Latin anchor: %s" % missing_la)
            if missing_en:
                detail.append("no English anchor: %s" % missing_en)
            if orphan:
                detail.append("anchored but undefined: %s" % orphan)
            problems.append("%s: PAIRING — %s" % (name, "; ".join(detail)))

        print("  %-24s %2d entries  La %2d  En %2d  %s"
              % (name, len(defs), len(la_anchors), len(en_anchors),
                 "ok" if paired and not dupes else "** FAIL **"))

        for pg, num in re.findall(r"^\[\^p(\d+)-(\d+)\]:", app, re.M):
            owners[int(pg)].setdefault(int(num), []).append(name)

    print()
    print("Footer ownership by printed page")
    print("-" * 62)
    for pg in sorted(owners):
        nums = owners[pg]
        top = max(nums)
        gaps = [i for i in range(1, top + 1) if i not in nums]
        doubles = sorted(n for n, who in nums.items() if len(who) > 1)
        known = expect.get(pg)
        pending = []
        if known is not None and known > top:
            pending = list(range(top + 1, known + 1))

        status = "ok"
        if gaps:
            problems.append("p.%d: INTERIOR GAP — notes %s owned by no chunk" % (pg, gaps))
            status = "** GAP %s **" % gaps
        if doubles:
            for n in doubles:
                problems.append("p.%d n.%d: DOUBLE-CLAIMED by %s" % (pg, n, nums[n]))
            status = "** DOUBLE %s **" % doubles

        line = "  p.%d: 1-%-2d (%d notes)  %s" % (pg, top, len(nums), status)
        if pending:
            line += "   PENDING n.%s -> not yet written" % (
                ",".join(str(p) for p in pending))
        elif known is None:
            # An unregistered page cannot be checked for a trailing shortfall:
            # with no recorded total, a page whose last notes are still
            # unwritten is indistinguishable from a page that is complete, and
            # it prints "ok". That is the failure mode this whole script exists
            # to prevent, so say so loudly rather than let it read as clean.
            line += "   ?? NOT IN KNOWN_TOTALS -- trailing notes unverifiable"
        print(line)

        if known is not None and top > known:
            problems.append(
                "p.%d: claims n.%d but the page is recorded as holding only %d"
                % (pg, top, known))
        if known is None:
            unregistered.append(pg)

    if unregistered:
        print()
        print("?? %d page(s) not in KNOWN_TOTALS: %s" % (
            len(unregistered), ", ".join("p.%d" % p for p in unregistered)))
        print("   Their trailing notes cannot be checked. Read the page's full")
        print("   footer register off the bands and add the total to KNOWN_TOTALS.")

    print()
    print("%d chunks, %d apparatus entries" % (len(files), total_entries))
    if problems:
        print()
        print("PROBLEMS (%d)" % len(problems))
        for p in problems:
            print("  - %s" % p)
        return 1
    print("All checks passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())

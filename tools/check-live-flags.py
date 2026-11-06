#!/usr/bin/env python3.11
"""Find LIVE `[?]` flags — the ones that actually stand in the text.

    python3.11 tools/check-live-flags.py [vol5 ...]

WHY THIS EXISTS (earned at the Hexaemeron mid-work gate, 2026-08-15).
A gate's pass 1 is the `[?]` resolution pass, and the obvious instrument —
`grep -n "\\[?\\]" vol*/…` — is USELESS in this corpus. Nearly every chunk's
`## Notes` discusses flags in prose ("No `[?]` flags.", "TWO `[?]` FLAGS TRAVEL
FORWARD…"), and the frontmatter `transcription_status` says "zero [?] flags" in
every Tier-2 chunk. A bare grep over vol5 returns 100+ hits, of which — at the
time this was written — exactly ONE was a real flag.

A flag is LIVE only if it stands in rendered text: the `## Latin`, `## English`
or `## Apparatus` sections. `## Notes` is never rendered (no component reads it)
and frontmatter is metadata, so a `[?]` in either is commentary, not a flag.

Exit code is 0 whether or not flags are found — an open flag is a legitimate
state, not an error. The point is to make the count DERIVED rather than
hand-carried, per the standing rule against hand-carried corpus-wide counts.
"""
import glob
import os
import re
import sys

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ALL_VOLUMES = ["vol1", "vol2", "vol3", "vol4", "vol5", "vol6"]

# ⛔⛔ THIS SCRIPT TAKES BARE POSITIONAL VOLUME NAMES, AND IT USED TO ACCEPT
# ANYTHING. `--volume 5` — the form every other tool in this repo takes — was
# read as two "volume names", matched nothing, and the script then printed
# "LIVE [?] FLAGS: none — checked, not assumed." A CLEAN VERDICT ON ZERO
# CHUNKS. It was recorded as a live trap TWICE (Vol V Sermones notes, then the
# Vol V close) and fixed neither time; the fix is eleven lines and is below.
# Every argument is now validated against ALL_VOLUMES and the run dies on
# anything else, so the failure can no longer be silent.
_args = sys.argv[1:]
for _a in _args:
    if _a.startswith("-"):
        sys.exit("this script takes BARE volume names, not flags: "
                 "%r\n  use:  check-live-flags.py vol6   (or no argument for "
                 "the whole corpus)" % _a)
    if _a not in ALL_VOLUMES:
        sys.exit("unknown volume %r (have %s)" % (_a, ", ".join(ALL_VOLUMES)))
VOLUMES = _args or ALL_VOLUMES


# ⭐ PRINTED_QUERIES (ruling 131, p. 559 shakedown gate, 2026-11-06): a `[?]`
# that QUARACCHI'S EDITORS printed, transcribed as printed (ruling 9), is not
# our flag. Skip one only when (a) the line belongs to the named apparatus
# entry (the last `[^label]:` def above it) of the named chunk AND (b) the
# context string stands on that line — so a NEW printed query can never be
# absorbed silently: it must be added here, keyed and quoted. Exempt hits are
# reported on their own line, never dropped from the output.
PRINTED_QUERIES = [
    # (chunk path, apparatus label, context on the line)
    ("vol6/bon-cioan-c2.md", "p545-6", "in caelo [?]"),       # La. — Bede, p. 545 n. 6
    ("vol6/bon-cioan-c2.md", "p545-6", "in the heaven [?]"),  # En. mirror
]


def live_region(text):
    """Everything a reader can see: frontmatter and ## Notes removed."""
    if text.startswith("---"):
        parts = text.split("---", 2)
        text = parts[2] if len(parts) > 2 else text
    return re.split(r"\n## Notes\b", text, maxsplit=1)[0]


total_files = 0
hits = []
exempt = []
for vol in VOLUMES:
    for path in sorted(glob.glob(os.path.join(REPO, vol, "*.md"))):
        total_files += 1
        with open(path, encoding="utf-8") as fh:
            region = live_region(fh.read())
        rel = os.path.relpath(path, REPO)
        label = None
        for lineno, line in enumerate(region.split("\n"), 1):
            m = re.match(r"\[\^([^\]]+)\]:", line)
            if m:
                label = m.group(1)
            elif line.startswith("## "):
                label = None
            if "[?]" in line:
                if any(rel == q[0] and label == q[1] and q[2] in line
                       for q in PRINTED_QUERIES):
                    exempt.append((rel, lineno, label))
                else:
                    hits.append((rel, lineno, line.strip()))

print(f"scanned {total_files} chunks in {', '.join(VOLUMES)}")
if exempt:
    print(f"printed by the editors, not ours (PRINTED_QUERIES, ruling 131): "
          f"{len(exempt)} — " + ", ".join(f"{p}:{n} [^{l}]" for p, n, l in exempt))
if not hits:
    print("LIVE [?] FLAGS: none — checked, not assumed.")
else:
    print(f"LIVE [?] FLAGS: {len(hits)} occurrence(s)")
    print("  (a flag mirrored in Latin and English counts twice — that is correct practice)")
    for path, lineno, line in hits:
        snippet = line if len(line) <= 150 else line[:147] + "..."
        print(f"  {path}:{lineno}  {snippet}")

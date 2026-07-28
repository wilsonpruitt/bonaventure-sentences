#!/usr/bin/env python3.11
"""Polish-blocker Pass 2: full-corpus style/formatting scan.

Scans every Tier-2 chunk (vol1/ .. vol5/) for the mechanical invariants the
polish-blocker requires. Triage signal — reports, does not fix.

"Full corpus every time" per CLAUDE.md's polish-blocker cadence — vol3/vol4 were
added 2026-07-13 at the Vol IV d.31–d.40 gate (the script had silently been
scanning only vol1+vol2 since Vol III opened). **vol5 added 2026-07-28.**

⚠ This script is NO LONGER GATE-ONLY. Per CLAUDE.md § "Polish-gate cadence for
Vols V–X" it is decoupled from the gates and runs every commit alongside
`build-content.mjs`. Gating it is exactly what hid the vol3/vol4 blindness for
four volumes.

Vol V (work chunks, `bon-brev-*` etc.) has its own invariants, checked only for
that volume:
  * page-qualified apparatus labels (`[^p214-9]`) — bare `[^9]` would collide
    across pages, because Quaracchi restarts footnote numbering every printed
    page, and the duplicate def silently drops an entry at render;
  * every label's page must appear in the chunk's `printed_pages`;
  * `work:` present and `book:` absent (the WORKS registry maps slug -> book id);
  * `division:` present (the distinctio-equivalent grouping key);
  * no `[^...]` token anywhere in `## Notes` — harmless to readers, but it
    breaks label pairing and the §6 classifier.

Usage:
    python3.11 tools/polish-style-scan.py                # full corpus
    python3.11 tools/polish-style-scan.py --volume 5     # one volume
    python3.11 tools/polish-style-scan.py --volume 5 --only APP,PAIR
"""
import re, sys, glob, os

DIRS = ["vol1", "vol2", "vol3", "vol4", "vol5"]
REQUIRED_FM = ["title_la", "title_en", "printed_pages", "pdf_pages",
               "source", "has_apparatus", "transcription_status"]
# Vol V work chunks declare `work:` instead of `book:`; `division:` replaces
# `distinctio:` as the grouping key.
REQUIRED_FM_VOL5 = ["work", "division"]

def parse_frontmatter(text):
    m = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    if not m:
        return None, text[len(m.group(0)):] if m else text
    fm = {}
    for line in m.group(1).splitlines():
        mm = re.match(r"^(\w+):\s*(.*)$", line)
        if mm:
            fm[mm.group(1)] = mm.group(2).strip()
    return fm, text[m.end():]

def is_tier2(fm):
    ts = fm.get("transcription_status", "") if fm else ""
    return "Tier 2 complete" in ts or "Tier 2 apparatus-incomplete" in ts

def body_markers(body):
    # exclude apparatus definition lines (start of line [^N]:)
    out = []
    for line in body.splitlines():
        if re.match(r"^\s*\[\^[^\]]+\]:", line):
            continue
        out.extend(re.findall(r"\[\^([^\]]+)\]", line))
    return out

def section(body, name):
    """Body of a `## name` section, up to the next `## ` heading."""
    m = re.search(r"^## %s\s*$" % re.escape(name), body, re.M)
    if not m:
        return ""
    rest = body[m.end():]
    nxt = re.search(r"^## ", rest, re.M)
    return rest[: nxt.start()] if nxt else rest


def main():
    argv = sys.argv[1:]
    want_vols, only_sev = None, None
    for i, a in enumerate(argv):
        if a == "--volume" and i + 1 < len(argv):
            want_vols = {"vol" + argv[i + 1]}
        elif a.startswith("--volume="):
            want_vols = {"vol" + a.split("=", 1)[1]}
        elif a == "--only" and i + 1 < len(argv):
            only_sev = {s.strip().upper() for s in argv[i + 1].split(",")}
        elif a.startswith("--only="):
            only_sev = {s.strip().upper() for s in a.split("=", 1)[1].split(",")}

    issues = []  # (chunk, severity, msg)
    files = []
    dirs = [d for d in DIRS if not want_vols or d in want_vols]
    for d in dirs:
        # `bon-sent-*` = Sentences chunks; `bon-brev-*` etc. = Vol V work chunks.
        files.extend(sorted(glob.glob(f"{d}/bon-*.md")))

    seen_ids = {}
    divisio_pars = {}  # distinction-key -> set of pars seen, to detect superseded plain divisio

    for f in files:
        with open(f, encoding="utf-8") as fh:
            text = fh.read()
        fm, body = parse_frontmatter(text)
        name = os.path.basename(f)
        is_vol5 = os.path.dirname(f) == "vol5"
        if fm is None:
            issues.append((name, "ERR", "no frontmatter block"))
            continue
        if not is_tier2(fm):
            continue  # skeleton — skip style checks

        # 1. required frontmatter
        for k in REQUIRED_FM:
            if k not in fm or fm[k] == "" or fm[k] == '""':
                issues.append((name, "FM", f"missing/empty frontmatter: {k}"))
        if is_vol5:
            for k in REQUIRED_FM_VOL5:
                if k not in fm or fm[k] == "" or fm[k] == '""':
                    issues.append((name, "FM", f"missing/empty frontmatter: {k}"))
            if "book" in fm:
                issues.append((name, "FM",
                               "work chunk declares book: — the WORKS registry "
                               "maps work slug -> book id; remove it"))

        # 5. transcription_status prefix
        ts = fm.get("transcription_status", "").strip().strip('"')
        if not ts.startswith("Phase C Tier 2 complete —"):
            if "apparatus-incomplete" in ts:
                issues.append((name, "STATUS", "status = apparatus-incomplete (pending rebuild)"))
            else:
                issues.append((name, "STATUS", f"status prefix: {ts[:48]!r}"))

        # 2. structure headers
        has_app = fm.get("has_apparatus", "").lower() == "true"
        if "## Latin" not in body:
            issues.append((name, "STRUCT", "missing ## Latin"))
        if "## English" not in body:
            issues.append((name, "STRUCT", "missing ## English"))
        if has_app and "## Apparatus" not in body:
            issues.append((name, "STRUCT", "has_apparatus:true but no ## Apparatus"))

        # 4. page breaks
        if "<!-- page" not in body:
            issues.append((name, "PAGE", "no <!-- page N --> markers"))

        # 3. apparatus marker pairing
        # split body into Latin / English / Apparatus regions
        defs = re.findall(r"^\s*\[\^([^\]]+)\]:", body, re.M)
        def_set = set(defs)
        # duplicate defs
        dup = set(x for x in defs if defs.count(x) > 1)
        if dup:
            issues.append((name, "APP", f"duplicate apparatus defs: {sorted(dup)}"))

        # regions
        lat = re.search(r"## Latin(.*?)(?:## English|\Z)", body, re.S)
        eng = re.search(r"## English(.*?)(?:## Apparatus|## Notes|\Z)", body, re.S)
        lat_markers = set(body_markers(lat.group(1))) if lat else set()
        eng_markers = set(body_markers(eng.group(1))) if eng else set()

        if has_app:
            # every def should be anchored in both bodies
            missing_lat = def_set - lat_markers
            missing_eng = def_set - eng_markers
            if missing_lat:
                issues.append((name, "PAIR", f"defs not anchored in Latin: {sorted(missing_lat, key=lambda s:(len(s),s))}"))
            if missing_eng:
                issues.append((name, "PAIR", f"defs not anchored in English: {sorted(missing_eng, key=lambda s:(len(s),s))}"))
            # body markers with no def
            orphan_lat = lat_markers - def_set
            orphan_eng = eng_markers - def_set
            orphans = orphan_lat | orphan_eng
            if orphans:
                issues.append((name, "PAIR", f"body markers with no apparatus def: {sorted(orphans, key=lambda s:(len(s),s))}"))

        # 7. Vol V invariants (work chunks only)
        if is_vol5:
            # 7a. page-qualified labels. A bare [^9] collides with the next
            # page's n.9 -> duplicate def -> an entry vanishes at render.
            bare = sorted({d for d in def_set
                           if not re.fullmatch(r"p\d+-\d+", d)})
            if bare:
                issues.append((name, "V5LABEL",
                               f"apparatus labels not page-qualified: {bare} "
                               "(expected [^p<page>-<n>])"))
            # 7b. every label's page must be one the chunk claims.
            pages = set(re.findall(r"\d+", fm.get("printed_pages", "")))
            for d in sorted(def_set):
                mm = re.fullmatch(r"p(\d+)-\d+", d)
                if mm and pages and mm.group(1) not in pages:
                    issues.append((name, "V5PAGE",
                                   f"label [^{d}] cites p.{mm.group(1)}, not in "
                                   f"printed_pages {sorted(pages)}"))
            # 7c. no footnote token in Notes prose — breaks pairing + §6 classifier.
            notes = section(body, "Notes")
            if notes and re.search(r"\[\^", notes):
                issues.append((name, "V5NOTES",
                               "literal [^ token in ## Notes prose — quote the "
                               "label without the bracket-caret"))

        # 6. legacy duplicate tracking: plain divisio vs pars-split
        m = re.match(r"bon-sent-(I{1,2})-d(\d+)-(p(\d)-)?divisio\.md", name)
        if m:
            key = (m.group(1), m.group(2))
            divisio_pars.setdefault(key, set()).add(m.group(4))  # None for plain

    # report superseded plain divisio
    for key, parsset in divisio_pars.items():
        if None in parsset and any(p for p in parsset if p):
            vol, dn = key
            issues.append((f"bon-sent-{vol}-d{dn}-divisio.md", "DUP",
                           "plain divisio coexists with pars-split divisio (legacy duplicate?)"))

    # output
    scope = ", ".join(dirs)
    if only_sev:
        issues = [i for i in issues if i[1] in only_sev]
    if not issues:
        print(f"CLEAN — no style/formatting issues across Tier-2 corpus ({scope}, "
              f"{len(files)} files).")
        return 0
    by_chunk = {}
    by_sev = {}
    for c, sev, msg in issues:
        by_chunk.setdefault(c, []).append((sev, msg))
        by_sev[sev] = by_sev.get(sev, 0) + 1
    print(f"# Pass-2 style scan — {len(issues)} issue(s) across {len(by_chunk)} "
          f"chunk(s)   [scope: {scope}]\n")
    for c in sorted(by_chunk):
        print(f"## {c}")
        for sev, msg in by_chunk[c]:
            print(f"  [{sev}] {msg}")
    # Severity roll-up: this is the parcelling key — one severity class is one
    # agent run, since the fix recipe is uniform within a class.
    print("\n## By severity (parcel one class per agent run)")
    for sev in sorted(by_sev, key=lambda s: -by_sev[s]):
        chunks = sorted({c for c, s, _ in issues if s == sev})
        print(f"  {sev:<9} {by_sev[sev]:>4} issue(s) / {len(chunks):>3} chunk(s)")
    print(f"\nTotal: {len(issues)} issues / {len(by_chunk)} chunks / {len(files)} scanned")
    return 1

if __name__ == "__main__":
    sys.exit(main())

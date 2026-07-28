#!/usr/bin/env python3.11
"""Pass-3 seam-continuity screen.

For each adjacent chunk pair in canonical order, determine whether they share a
printed page (mid-page boundary). For mid-page boundaries, surface the prior
chunk's Latin-body tail and the next chunk's Latin-body head so a human (or a
targeted PDF re-read) can confirm grammatical continuity — the cascade-merge
signature is a grammatically broken splice in the prior chunk's tail.

Vols I-IV take a distinction range:   seam-screen.py --volume 4 41 50
Vol V takes no range (work chunks have no distinctions), optionally filtered to
one work by its slug:                 seam-screen.py --volume 5 [--work breviloquium]

⚠ Vol IV was missing from the VOL map entirely until 2026-07-28 — this screen
had never been runnable on it. Vol V added at the same time; there the screen
matters MORE than in the Sentences, because Breviloquium capitula are sub-page
units, so nearly every chunk boundary is a mid-page boundary, and ten of the
first sixteen chunks carry a footnote runover across the seam.
"""
import re, sys, glob, os, ast

def fm_field(text, key):
    m = re.search(rf"^{key}:\s*(.*)$", text, re.M)
    return m.group(1).strip() if m else None

def printed_pages(text):
    raw = fm_field(text, "printed_pages")
    if not raw:
        return []
    try:
        return ast.literal_eval(raw)
    except Exception:
        return [int(x) for x in re.findall(r"\d+", raw)]

def latin_body(text):
    m = re.search(r"## Latin(.*?)(?:## English)", text, re.S)
    if not m:
        return ""
    body = m.group(1)
    # strip page comments, headings, blockquote markers for tail/head sampling
    lines = [l.rstrip() for l in body.splitlines()
             if l.strip() and not l.strip().startswith("<!--")
             and not l.strip().startswith("#") and not l.strip().startswith("---")]
    return lines

# canonical sort key for chunk filenames
def sortkey(name):
    # -s(\d) = editorial "sectio" level; Vol IV d.49 P.II only (see CLAUDE.md §5a)
    m = re.search(r"d(\d+)(?:-p(\d))?(?:-s(\d))?(?:-a(\d))?(?:-q(\d))?", name)
    d = int(m.group(1))
    pars = int(m.group(2)) if m.group(2) else 0
    sect = int(m.group(3)) if m.group(3) else 0
    art = int(m.group(4)) if m.group(4) else 0
    q = int(m.group(5)) if m.group(5) else 0
    # type ordering within a distinction/pars: littera, divisio, articles, dubia
    if "littera" in name: typ = 0
    elif "divisio" in name: typ = 1
    elif "dubia" in name: typ = 9
    else: typ = 2
    return (d, pars, typ, sect, art, q)

TERMINAL = ('.', '»', ':', '?', '!', '"')

def ends_terminal(tail):
    """True if the tail ends on sentence-final punctuation.

    Markdown emphasis markers and closing brackets are stripped first: Vol V
    italicises far more heavily than the Sentences do, so a legitimate close
    like `...vocabitur in regno caelorum.*` (a scripture quotation ending the
    chunk) would otherwise be flagged as a broken splice on every run.
    """
    t = tail.rstrip()
    while t and t[-1] in "*_`)]":
        t = t[:-1].rstrip()
    return t.endswith(TERMINAL)

VOL = {1: ("vol1", "I"), 2: ("vol2", "II"), 3: ("vol3", "III"),
       4: ("vol4", "IV"), 5: ("vol5", None)}

def vol5_sortkey(text, name):
    """Reading order for work chunks: no distinctions, so key off the data model
    (division/capitulum/section) with the first printed page as the outer key."""
    pp = printed_pages(text)
    first = pp[0] if pp else 0
    def num(k):
        v = fm_field(text, k)
        try:
            return int(v)
        except (TypeError, ValueError):
            return 0
    return (first, num("division"), num("capitulum"), num("section"), name)

def main():
    # ⚠ Parse flags and their values TOGETHER, consuming the value so it cannot
    # leak into the positional args. The old form filtered on `startswith("--")`
    # only, so `--volume 4 41 50` left "4" as args[0] and silently scanned
    # d4-d41 instead of d41-d50 — a mis-scoped gate that reports a plausible
    # number and looks fine. The `--volume=4` form happened to work, which is
    # why it went unnoticed.
    argv = sys.argv[1:]
    vol, work, args = 2, None, []
    i = 0
    while i < len(argv):
        a = argv[i]
        if a.startswith("--volume"):
            if "=" in a:
                vol = int(a.split("=", 1)[1])
            else:
                vol = int(argv[i + 1]); i += 1
        elif a.startswith("--work"):
            if "=" in a:
                work = a.split("=", 1)[1]
            else:
                work = argv[i + 1]; i += 1
        elif not a.startswith("--"):
            args.append(a)
        i += 1
    if vol not in VOL:
        sys.exit(f"unknown volume {vol}; known: {sorted(VOL)}")
    if vol != 5 and len(args) < 2:
        sys.exit("Vols I-IV need a distinction range: seam-screen.py --volume 4 41 50")
    vdir, vrom = VOL[vol]

    chunks = []
    if vol == 5:
        min_d = max_d = None
        rows = []
        for f in sorted(glob.glob(f"{vdir}/bon-*.md")):
            with open(f, encoding="utf-8") as fh:
                t = fh.read()
            if "Tier 2 complete" not in (fm_field(t, "transcription_status") or ""):
                continue
            if work and (fm_field(t, "work") or "").strip().strip('"') != work:
                continue
            rows.append((vol5_sortkey(t, os.path.basename(f)), f, t))
        rows.sort(key=lambda r: r[0])
        for _, f, t in rows:
            chunks.append((os.path.basename(f), printed_pages(t), latin_body(t)))
        label = f"Vol V{' / ' + work if work else ''}"
    else:
        min_d, max_d = int(args[0]), int(args[1])
        files = []
        for f in glob.glob(f"{vdir}/bon-sent-{vrom}-d*.md"):
            m = re.search(r"-d(\d+)", f)
            if m and min_d <= int(m.group(1)) <= max_d:
                files.append(f)
        files.sort(key=lambda f: sortkey(os.path.basename(f)))
        for f in files:
            with open(f, encoding="utf-8") as fh:
                t = fh.read()
            if "Tier 2 complete" not in (fm_field(t, "transcription_status") or ""):
                continue
            chunks.append((os.path.basename(f), printed_pages(t), latin_body(t)))
        label = f"d{min_d}-d{max_d}"

    print(f"# Pass-3 seam screen {label} — {len(chunks)} Tier-2 chunks\n")
    midpage = 0
    suspects = []
    for i in range(len(chunks) - 1):
        name, pp, body = chunks[i]
        nname, npp, nbody = chunks[i+1]
        if not pp or not npp or not body or not nbody:
            continue
        shares = pp[-1] == npp[0]
        if not shares:
            continue
        midpage += 1
        tail = body[-1]
        head = nbody[0]
        broken = not ends_terminal(tail)
        flag = "  <-- TAIL NOT TERMINAL" if broken else ""
        if broken:
            suspects.append((name, nname, pp[-1]))
        print(f"[p.{pp[-1]}] {name} -> {nname}{flag}")
        print(f"    tail: ...{tail[-120:]}")
        print(f"    head: {head[:100]}...")
        print()
    print(f"\n{midpage} mid-page boundaries; {len(suspects)} tail-not-terminal suspect(s).")
    for s in suspects:
        print(f"  SUSPECT p.{s[2]}: {s[0]} -> {s[1]}")

if __name__ == "__main__":
    main()

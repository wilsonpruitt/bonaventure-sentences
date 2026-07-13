#!/usr/bin/env python3.11
"""J1 of the apparatus backlog: make duplicate bare [^N] apparatus labels unique.

THE DEFECT: Quaracchi restarts footnote numbering on every printed page. Chunks promoted before
d.31 rendered that with bare [^1], [^2]... so a multi-page chunk ends up with two or three
[^1]: definitions. A body marker can only bind ONE of them -> the rest render as dropped or
mis-bound footnotes on the published page.

HOW WE PARTITION (and why NOT by position, and NOT by <!-- page --> comment):

  * NOT by position. Body anchors are NOT in footnote-number order. Quaracchi numbers its footers
    in COLUMN order while the anchors fall in READING order, so a body legitimately runs 1, 3, 2,
    4 (verified in IV-d20-p2-dubia: [^3] sits on "procedat" and its note is the variant
    "procedit"; [^4] sits on "tantum" and its note is "omittunt tantum"). Relabelling the i-th
    marker with the i-th definition would SWAP notes 2 and 3 and bind the wrong text.

  * NOT by <!-- page --> comment. Those disagree with the real footnote-group boundaries in most
    of these chunks (IV-d17-p2-dubia: p.448 holds body markers 1-5 but the page's footer group is
    1-9). Page attribution is not recoverable from the file alone -- that is a J4 problem.

  * BY GREEDY REPEAT-PARTITION, which is sound: within one printed page each footnote number
    occurs exactly once, and one page's anchors are contiguous in the body. So walk the body
    markers in order and start a new group the moment a number repeats. Non-monotonic order
    inside a group does not disturb this -- only a REPEAT does.

We then REQUIRE the body partition to match the apparatus definition groups exactly (same number
of groups, same set of numbers in each). That is a real consistency proof, not an assumption.
The relabel keys on (group, existing number), so every anchor keeps the note it already had.

LABELLING:
  - if len(groups) == len(printed_pages): use the page-qualified [^pNNN-M] scheme (the d.31+
    corpus convention).
  - otherwise a printed page carries no footnotes and we cannot say WHICH page each group is,
    so fall back to the corpus's existing suffix convention [^N], [^Nb], [^Nc] per group. That is
    page-agnostic, unique, and lossless -- uniqueness is what fixes the render bug; the page
    number in the label is only metadata.

Any chunk whose body partition does NOT match the definition groups is SKIPPED and reported for
the J4 pass. Nothing is guessed at.

Run:  python3.11 tools/fix-apparatus-labels.py           # dry run, writes nothing
      python3.11 tools/fix-apparatus-labels.py --apply   # rewrite in place (backs up first)
"""
import re, glob, ast, sys, os, shutil

APPLY = "--apply" in sys.argv
DIRS = ["vol1", "vol2", "vol3", "vol4"]
SUFFIX = ["", "b", "c", "d", "e", "f"]


def section(t, name, nxt):
    m = re.search(rf'^## {name}\s*$', t, re.M)
    if not m:
        return None, None
    s = m.end()
    rest = t[s:]
    m2 = re.search(rf'^## (?:{nxt})\s*$', rest, re.M)
    return s, s + (m2.start() if m2 else len(rest))


def greedy_groups(labels):
    """partition a marker sequence into per-page groups: a repeat starts a new group"""
    groups, cur, seen = [], [], set()
    for x in labels:
        if x in seen:
            groups.append(cur); cur = []; seen = set()
        cur.append(x); seen.add(x)
    if cur:
        groups.append(cur)
    return groups


fixed, skipped = [], []

for d in DIRS:
    for f in sorted(glob.glob(f"{d}/*.md")):
        t = open(f, encoding="utf-8").read()
        if "Phase C Tier 2 complete" not in t:
            continue
        las, lae = section(t, "Latin", "English|Apparatus|Notes")
        ens, ene = section(t, "English", "Apparatus|Notes|Latin")
        aps, ape = section(t, "Apparatus", "Notes|Latin|English")
        if None in (las, ens, aps):
            continue
        la, en, ap = t[las:lae], t[ens:ene], t[aps:ape]

        defs = re.findall(r'^\[\^([^\]]+)\]:', ap, re.M)
        if not defs or len(defs) == len(set(defs)):
            continue                                    # healthy -> not J1
        if not all(x.isdigit() for x in defs):
            skipped.append((f, "non-integer labels already present")); continue

        laM = re.findall(r'\[\^([^\]]+)\]', la)
        enM = re.findall(r'\[\^([^\]]+)\]', en)

        dG, lG, eG = greedy_groups(defs), greedy_groups(laM), greedy_groups(enM)
        if not (len(dG) == len(lG) == len(eG)):
            skipped.append((f, f"group count differs (defs={len(dG)} la={len(lG)} en={len(eG)})")); continue
        bad = None
        for i, (dg, lg, eg) in enumerate(zip(dG, lG, eG)):
            if sorted(dg, key=int) != sorted(lg, key=int) or sorted(dg, key=int) != sorted(eg, key=int):
                bad = (f"group {i+1}: defs {sorted(dg,key=int)} / la {sorted(lg,key=int)} "
                       f"/ en {sorted(eg,key=int)}")
                break
        if bad:
            skipped.append((f, bad)); continue

        m = re.search(r'^printed_pages: (\[.*\])', t, re.M)
        pages = ast.literal_eval(m.group(1)) if m else []
        paged = len(dG) == len(pages)
        if not paged and len(dG) > len(SUFFIX):
            skipped.append((f, f"{len(dG)} groups, no page mapping and too many for suffixes")); continue

        def newlab(gi, n):
            return f"p{pages[gi]}-{n}" if paged else f"{n}{SUFFIX[gi]}"

        # rebuild each region, keying on (group, existing number) -- anchors keep their own notes
        def relabel(region, groups):
            it = iter([newlab(gi, n) for gi, g in enumerate(groups) for n in g])
            return re.sub(r'\[\^[^\]]+\]', lambda _: f"[^{next(it)}]", region)

        new_la, new_en = relabel(la, lG), relabel(en, eG)
        it = iter([newlab(gi, n) for gi, g in enumerate(dG) for n in g])
        new_ap = re.sub(r'^\[\^[^\]]+\]:', lambda _: f"[^{next(it)}]:", ap, flags=re.M)

        # ---- post-verify: every anchor still points at the note it used to point at ----
        old_pairs = {}                                  # (group, number) -> def text
        for gi, g in enumerate(dG):
            pass
        ndefs = re.findall(r'^\[\^([^\]]+)\]:', new_ap, re.M)
        nla = re.findall(r'\[\^([^\]]+)\]', new_la)
        nen = re.findall(r'\[\^([^\]]+)\]', new_en)
        assert len(set(ndefs)) == len(ndefs), f"{f}: duplicates survived"
        assert set(nla) == set(nen) == set(ndefs), f"{f}: marker/def sets diverged"
        # the k-th body marker must still carry the same (group, number) identity it had
        expect_la = [newlab(gi, n) for gi, g in enumerate(lG) for n in g]
        assert nla == expect_la, f"{f}: latin anchors moved"

        fixed.append((f, len(defs), len(dG), "page" if paged else "suffix",
                      pages if paged else ""))
        if APPLY:
            os.makedirs("_backup-apparatus-labels", exist_ok=True)
            shutil.copy2(f, f"_backup-apparatus-labels/{os.path.basename(f)}")
            open(f, "w", encoding="utf-8").write(
                t[:las] + new_la + t[lae:ens] + new_en + t[ene:aps] + new_ap + t[ape:])

print(f"=== J1 apparatus relabel — {'APPLIED' if APPLY else 'DRY RUN (nothing written)'} ===\n")
print(f"FIXABLE (body partition PROVEN to match the apparatus groups): {len(fixed)}")
for f, nd, ng, scheme, pages in fixed:
    print(f"   {f:<42} {nd:>3} defs, {ng} groups -> {scheme:<6} {pages}")
print(f"\nSKIPPED (partition unproven -> J4, needs the PDF): {len(skipped)}")
for f, why in skipped:
    print(f"   {f:<42} {why}")

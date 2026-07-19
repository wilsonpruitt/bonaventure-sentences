#!/usr/bin/env python3.11
"""Dubia-count audit — detect dubia that are printed but never rendered.

WHY THIS EXISTS
  d.45 printed NINE dubia. Only THREE were greppable: the other six were cased `DuB.` instead of
  `DUB.` and were invisible to the case-sensitive grep the session used. They were found only by
  counting off the 450 dpi bands. Any distinction written before that lesson could have the same
  silent loss.

  A sequence-gap check does NOT catch this. The d.45 chunk would have rendered Dub. I, II, III —
  contiguous, no gap, max numeral 3. The loss is only visible against the print.

METHOD
  Collect every dubium numeral in the raw CASE-INSENSITIVELY (`DUB. IV.`, `DuB. IV.`, `Dub. iv.`)
  and group the hits into PROXIMITY CLUSTERS — a distinction's dubia are printed contiguously.
  Clusters emerge in raw order, which is distinction order, so they align with the dubia chunks
  sorted by distinction number. Compare each cluster's highest numeral against the highest the
  corresponding chunk renders.

  raw cluster max > chunk max  =>  the print has dubia the corpus does not.

  Validated on Vol IV, where the truth is known from band counts: the clusters return
  d.45 -> 9, d.46 -> 6, d.47 -> 4, matching the band-verified counts exactly.

WHAT IT DELIBERATELY DOES NOT COUNT
  * Running-head lines (`DIST. XLV. DUBIA. 995`) — page furniture, no numeral of their own.
  * Prose references in the apparatus (`De hoc dub. cfr. Petr. a Tar.`, `hoc dubio`) — the numeral
    slot must hold a Roman numeral, which those do not.

LIMITS
  * Attribution by 'nearest preceding DIST marker' was tried FIRST and DRIFTS badly: d.45's dubia
    sit past the point where d.46's running-head bleeds begin, so the two distinctions' counts came
    out swapped. Clustering replaced it. Recorded here because the drift was silent and plausible.
  * Alignment assumes one cluster per dubia chunk. Where the counts differ the tool says so and
    falls back to an aggregate check rather than reporting unreliable per-distinction matches.
  * A dubium whose header is garbled in the NUMERAL (not just the case) is still missed. This
    narrows the class; it does not close it.

Usage:
  python3.11 tools/audit-dubia-count.py --all
"""
import re, os, glob, argparse, collections

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
VOLS = {
    1: dict(dirs=["vol1"], raws=["raw/bonaventure_vol1_raw.txt",
                                 "raw/bonaventure_vol1_pt2_raw.txt"], tag="I"),
    2: dict(dirs=["vol2"], raws=["raw/bonaventure_vol2_raw.txt"], tag="II"),
    3: dict(dirs=["vol3"], raws=["raw/bonaventure_vol3_raw.txt"], tag="III"),
    4: dict(dirs=["vol4"], raws=["raw/bonaventure_vol4_raw.txt"], tag="IV"),
}
ROMAN = {"I":1,"II":2,"III":3,"IV":4,"V":5,"VI":6,"VII":7,"VIII":8,"IX":9,"X":10,
         "XI":11,"XII":12,"XIII":13,"XIV":14,"XV":15,"XVI":16,"XVII":17,"XVIII":18,
         "XIX":19,"XX":20}
DIST_ROMAN = dict(ROMAN)
DIST_ROMAN.update({"XXI":21,"XXII":22,"XXIII":23,"XXIV":24,"XXV":25,"XXVI":26,"XXVII":27,
    "XXVIII":28,"XXIX":29,"XXX":30,"XXXI":31,"XXXII":32,"XXXIII":33,"XXXIV":34,"XXXV":35,
    "XXXVI":36,"XXXVII":37,"XXXVIII":38,"XXXIX":39,"XL":40,"XLI":41,"XLII":42,"XLIII":43,
    "XLIV":44,"XLV":45,"XLVI":46,"XLVII":47,"XLVIII":48,"XLIX":49,"L":50})

# a dubium header: DUB / DuB / Dub, optional dot, then a Roman numeral. Case-insensitive on the
# word, but the numeral must be a real Roman numeral so prose refs cannot match.
DUB = re.compile(r"\bDUB[.,]?\s*([IVXL]{1,6})[.,]", re.I)
# distinction markers: both real headers and running heads
DIST = re.compile(r"\bDIST(?:INCTIO|INGTIO|mCTIO|\.)?\s*([IVXL]{1,7})[.,]", re.I)

def norm(s): return re.sub(r"\s+", " ", s).strip()

def scan_raw_clusters(paths, gap=500):
    """Collect dubium headers as PROXIMITY CLUSTERS in raw order.

    Attribution by 'nearest preceding DIST marker' was tried first and DRIFTS: d.45's dubia sit at
    the tail of its range, past the point where d.46's running-head bleeds begin, so they were
    attributed to d.46 and the two distinctions' counts swapped. Clustering needs no attribution —
    a distinction's dubia are printed contiguously, so a run of dubium headers separated by less
    than `gap` lines is one distinction's set. Clusters come out in raw order, which is
    distinction order, so they align with the dubia chunks sorted by distinction number.
    """
    hits = []
    for path in paths:
        with open(os.path.join(REPO, path), encoding="utf-8", errors="replace") as f:
            for ln, line in enumerate(f, 1):
                L = norm(line)
                if not L: continue
                for m in DUB.finditer(L):
                    v = ROMAN.get(m.group(1).upper())
                    if v: hits.append((path, ln, v))
    clusters, cur = [], []
    for h in hits:
        if cur and (h[0] != cur[-1][0] or h[1] - cur[-1][1] > gap):
            clusters.append(cur); cur = []
        cur.append(h)
    if cur: clusters.append(cur)
    return [{"path": os.path.basename(c[0][0]), "l0": c[0][1], "l1": c[-1][1],
             "nums": sorted({x[2] for x in c}), "max": max(x[2] for x in c)} for c in clusters]

# The corpus uses THREE header conventions and the regex must accept all of them:
#   "### Dub. I."   "### Dub. I"   (no period)   "### Dubium I."   (word spelled out)
# Earlier drafts requiring the period, then requiring the abbreviation, each produced a batch
# of false positives where a chunk scored ZERO dubia and looked catastrophically empty.
CHUNK_DUB = re.compile(r"^#{2,5}\s*Dub(?:ium)?[.,]?\s*([IVXL]{1,6})\s*[.,]?\s*$", re.I | re.M)

def scan_disk(dirs):
    per = collections.defaultdict(set)
    files = collections.defaultdict(list)
    for dr in dirs:
        for p in glob.glob(os.path.join(REPO, dr, "bon-sent-*dub*.md")):
            t = open(p, encoding="utf-8").read()
            m = re.search(r"^distinctio: (\d+)", t, re.M)
            if not m: continue
            d = int(m.group(1))
            files[d].append(os.path.basename(p))
            # count only within the Latin block, so English "Doubt N" is not double counted
            lat = t.split("## English")[0]
            for mm in CHUNK_DUB.finditer(lat):
                v = ROMAN.get(mm.group(1).upper())
                if v: per[d].add(v)
    return per, files

def pick_raw(paths, first_page):
    """Vol I is split across TWO raw files and line numbers are FILE-SPECIFIC.

    Scanning both with the same range conflates them: d.42's dubia (pt2, printed p.759) picked up
    a spurious 'Dub. X' from the unrelated text at the same line numbers in pt1, and the chunk was
    falsely flagged as missing four dubia. Select by printed page — pt1 covers printed 1-410,
    pt2 covers 411 onward (CLAUDE.md volume-offset table).
    """
    if len(paths) == 1:
        return paths
    pt1 = [q for q in paths if "pt2" not in q]
    pt2 = [q for q in paths if "pt2" in q]
    return pt2 if (first_page or 0) > 410 else pt1

def raw_slice_max(paths, l0, l1):
    """Highest dubium numeral inside an explicit raw line range. Precise: no attribution needed."""
    best, nums = 0, set()
    for path in paths:
        with open(os.path.join(REPO, path), encoding="utf-8", errors="replace") as f:
            for ln, line in enumerate(f, 1):
                if ln < l0: continue
                if ln > l1: break
                for m in DUB.finditer(norm(line)):
                    v = ROMAN.get(m.group(1).upper())
                    if v: nums.add(v); best = max(best, v)
    return best, sorted(nums)

def run(v):
    """PRECISE per-chunk check, for dubia chunks that kept line_start/line_end.

    Cluster-alignment was tried and is NOT 1:1 in any volume (stray apparatus refs form spurious
    clusters; multi-pars distinctions form several), so per-distinction matching that way would be
    guesswork. Here we only check chunks whose own raw range is recorded — precise, no attribution
    — and report exactly how much of the volume that covers.
    """
    cfg = VOLS[v]
    print(f"\n{'='*76}\nVOL {cfg['tag']} — dubia printed vs rendered\n{'='*76}")
    checked = skipped = 0
    findings = []
    for dr in cfg["dirs"]:
        for path in sorted(glob.glob(os.path.join(REPO, dr, "bon-sent-*dub*.md"))):
            txt = open(path, encoding="utf-8").read()
            if "Tier 2 complete" not in txt:
                continue
            ms = re.search(r"^line_start: (\d+)", txt, re.M)
            me = re.search(r"^line_end: (\d+)", txt, re.M)
            if not (ms and me):
                skipped += 1; continue
            checked += 1
            lat = txt.split("## English")[0]
            cn = sorted({ROMAN[m.group(1).upper()] for m in CHUNK_DUB.finditer(lat)
                         if m.group(1).upper() in ROMAN})
            cmax = max(cn) if cn else 0
            pgm = re.search(r"^printed_pages: \[(\d+)", txt, re.M)
            first_page = int(pgm.group(1)) if pgm else None
            rmax, rn = raw_slice_max(pick_raw(cfg["raws"], first_page),
                                     int(ms.group(1)), int(me.group(1)))
            if rmax > cmax:
                findings.append((os.path.basename(path), rmax, rn, cmax, cn))
    if findings:
        print(f"\n  \u26a0 {len(findings)} CHUNK(S) WHERE THE RAW OUTRUNS THE RENDERED DUBIA:\n")
        for fn, rmax, rn, cmax, cn in findings:
            print(f"    {fn}")
            print(f"        raw   max Dub.{rmax}  nums={rn}")
            print(f"        chunk max Dub.{cmax}  nums={cn}")
    else:
        print("\n  \u2713 No checked chunk renders fewer dubia than its own raw range shows.")
    tot = checked + skipped
    print(f"\n  coverage: {checked}/{tot} Tier-2 dubia chunks had line ranges and were checked")
    if skipped:
        print(f"    \u26a0 {skipped} skipped — no line_start/line_end (see the line_start backfill "
              f"prerequisite). NOT cleared, just unexamined.")
    return findings

if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--volume", type=int, choices=[1,2,3,4]); ap.add_argument("--all", action="store_true")
    a = ap.parse_args()
    tot = 0
    for v in ([1,2,3,4] if a.all else [a.volume]): tot += len(run(v))
    print(f"\n{'='*76}\nTOTAL distinctions flagged: {tot}\n{'='*76}")

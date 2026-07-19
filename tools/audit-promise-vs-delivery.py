#!/usr/bin/env python3.11
"""Promise-vs-delivery audit — detect questions/articles that exist in the PRINT but have no chunk.

WHY THIS EXISTS
  Vol IV lost five whole questions to OCR-garbled `QUAESTIO` headers (d.42 a3-q3, d.46 a2-q4,
  d.47 a2-q3, d.48 a2-q3, d.49 s2-a4-q2). In each case the auto-chunker never saw the header, the
  sibling chunk silently swallowed the range, and ALL THREE guard-rail audits reported clean —
  because they count headers in the raw with the same regex family that missed the header, so raw
  and chunk are wrong in the same direction.

  This audit breaks that symmetry by using an INDEPENDENT witness.

THE WITNESS: RUNNING HEADS
  Quaracchi prints a running head on (almost) every page naming the structural position:
      DIST. XLVII. P. II. SECT. I. ART. III. QUAEST. I.
  A question that spans ANY page top therefore leaves a trace even when its own header is garbled
  beyond grepping. So: for each (distinctio, pars, articulus), the highest QUAEST numeral appearing
  in a running head is a LOWER BOUND on how many questions the print contains. Compare that against
  the chunk files actually on disk. Running-head numeral > delivered chunks  =>  missing question.

  This needs only the raw text and the chunk filenames — no line ranges (which are missing from
  most Tier-2 chunks) and no page images. That is what makes it cheap enough to run corpus-wide.

SECOND WITNESS: THE PROMISE
  Article openers state their own question count ("Et circa hoc quaeruntur quatuor"). Reported
  separately as a per-distinction tally, since without line ranges an opener cannot be attributed
  to a specific article with confidence. Treat as a soft signal.

LIMITS — READ BEFORE ACTING ON OUTPUT
  * Vol I pt1 (`bonaventure_vol1_raw.txt`, d.1–d.25) has NO running heads in the OCR at all.
    The primary witness is unavailable there; only the soft signal applies. Reported as such.
  * A question that never spans a page top leaves no running head, so this audit UNDERCOUNTS.
    Silence is not proof of completeness — it is a screen, not a certificate.
  * Running-head numerals are themselves OCR-garbled (`ART. U.` = ART. II, `QUAEST. lU.` = III).
    Known garbles are normalised; anything unparseable is REPORTED, never guessed.

Usage:
  python3.11 tools/audit-promise-vs-delivery.py --volume 3
  python3.11 tools/audit-promise-vs-delivery.py --all
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

# --- roman numeral parsing, tolerant of the OCR's habitual substitutions -------------
GARBLE = {
    "U": "II", "N": "II", "11": "II", "H": "II", "TI": "II",
    "HI": "III", "NI": "III", "LU": "III", "LLL": "III", "IH": "III", "III": "III",
    "1H": "III", "IU": "III", "M": "III",
    "I\\": "IV", "L\\": "IV", "IY": "IV", "TV": "IV", "1V": "IV",
    "V1": "VI", "VL": "VI", "VN": "VII",
}
ROMAN = {"I":1,"II":2,"III":3,"IV":4,"V":5,"VI":6,"VII":7,"VIII":8,"IX":9,"X":10,
         "XI":11,"XII":12,"XIII":13,"XIV":14,"XV":15,"XVI":16,"XVII":17,"XVIII":18,
         "XIX":19,"XX":20,"XXI":21,"XXII":22,"XXIII":23,"XXIV":24,"XXV":25,"XXVI":26,
         "XXVII":27,"XXVIII":28,"XXIX":29,"XXX":30,"XXXI":31,"XXXII":32,"XXXIII":33,
         "XXXIV":34,"XXXV":35,"XXXVI":36,"XXXVII":37,"XXXVIII":38,"XXXIX":39,"XL":40,
         "XLI":41,"XLII":42,"XLIII":43,"XLIV":44,"XLV":45,"XLVI":46,"XLVII":47,
         "XLVIII":48,"XLIX":49,"L":50}

UNICUS = re.compile(r"^UN[I|!\[]?[CG]", re.I)   # UNICUS / UNIGUS / UN[CUS / UNICLIS

def roman(s, slot="dist"):
    """Return int, or None if unparseable. Never guesses.

    `slot` matters. Articles and questions in this corpus never exceed ~12, while
    distinctions run to 50. Without that context 'ART. l.' (lowercase L standing for I)
    parses as Roman 50, and a bare page number in a numeral-less running head
    ('DIST. VI. ART. I. QUAEST. 131') parses as the question number. Both produced
    false positives on the first run.
    """
    if not s: return None
    t = s.upper().strip(" .,;:")
    if slot in ("art", "quaest") and UNICUS.match(t):
        return 1                                  # Articulus Unicus == article 1
    t = t.replace("|", "I").replace("!", "I").replace("[", "I")
    if slot in ("art", "quaest"):
        # a 2+ digit arabic run here is a page number, not a numeral
        if re.fullmatch(r"\d{2,}", t): return None
        if t == "L": t = "I"                      # lowercase l misread as L
    val = None
    if t in ROMAN: val = ROMAN[t]
    elif t in GARBLE and GARBLE[t] in ROMAN: val = ROMAN[GARBLE[t]]
    else:
        t2 = t.replace("1", "I")
        if t2 in ROMAN: val = ROMAN[t2]
    if val is None: return None
    if slot in ("art", "quaest") and val > 12: return None   # implausible; report, don't guess
    return val

# --- running-head parsing -------------------------------------------------------------
# e.g. "DIST. XLIX. P. II. SECT. I. ART. III. QUAEST. I. 1019"
HEAD = re.compile(
    r"DIST[.,]?\s*([IVXL0-9|!\\]+)[.,]?"
    r"(?:\s*P[.,]?\s*([IVX0-9|!\\]+)[.,]?)?"
    r"(?:\s*SECT[.,]?\s*([IVX0-9|!\\]+)[.,]?)?"
    r"(?:\s*ART[.,]?\s*([IVXUNHLM0-9|!\\]+)[.,]?)?"
    r"(?:\s*QUAEST[.,]?\s*([IVXUNHLM0-9|!\\]+)[.,]?)?",
    re.I)

NUMWORD = {"unum":1,"unus":1,"una":1,"duo":2,"duae":2,"duas":2,"tria":3,"tres":3,
           "quatuor":4,"quattuor":4,"quinque":5,"sex":6,"septem":7,"octo":8,
           "novem":9,"decem":10,"undecim":11,"duodecim":12}
PROMISE = re.compile(
    r"(?:quaerunt[uv]r|quaerit[uv]r)\s+(?:principaliter\s+)?(" + "|".join(NUMWORD) + r")\b"
    r"|(" + "|".join(NUMWORD) + r")\s+(?:principaliter\s+)?quaerunt[uv]r", re.I)

def norm(line):
    return re.sub(r"\s+", " ", line).strip()

def scan_raw(paths):
    """-> heads[(d,pars,art)] = max quaest seen ; unparsed list ; promises Counter[d]"""
    heads = collections.defaultdict(int)
    seen_art = collections.defaultdict(int)   # (d,pars) -> max art
    unparsed, promises = [], collections.Counter()
    cur_d = None
    for path in paths:
        with open(os.path.join(REPO, path), encoding="utf-8", errors="replace") as f:
            for ln, raw_line in enumerate(f, 1):
                line = norm(raw_line)
                if not line: continue
                m = HEAD.search(line)
                if m and re.match(r"^\s*DIST", line, re.I):
                    d = roman(m.group(1), "dist")
                    if d is None:
                        unparsed.append((path, ln, line[:70])); continue
                    cur_d = d
                    pars = roman(m.group(2), "pars") if m.group(2) else None
                    art  = roman(m.group(4), "art") if m.group(4) else None
                    q    = roman(m.group(5), "quaest") if m.group(5) else None
                    if m.group(4) and art is None: unparsed.append((path, ln, line[:70]))
                    if m.group(5) and q is None:   unparsed.append((path, ln, line[:70]))
                    if art is not None:
                        seen_art[(d, pars)] = max(seen_art[(d, pars)], art)
                        if q is not None:
                            k = (d, pars, art)
                            heads[k] = max(heads[k], q)
                if cur_d and PROMISE.search(line):
                    promises[cur_d] += 1
    return heads, seen_art, unparsed, promises

# --- what is actually on disk ----------------------------------------------------------
CHUNK = re.compile(r"bon-sent-[IVX]+-d(\d+)(?:-p(\d+))?(?:-s(\d+))?-a(\d+)-q(\d+)\.md$")

def scan_disk(dirs):
    """-> delivered[(d,pars,art)] = set of q ; note: sectio collapses into art for comparison,
       since running heads name ART within SECT and we compare per (d,pars,art)."""
    delivered = collections.defaultdict(set)
    sectio_keys = set()
    for dr in dirs:
        for p in glob.glob(os.path.join(REPO, dr, "bon-sent-*.md")):
            m = CHUNK.search(os.path.basename(p))
            if not m: continue
            d = int(m.group(1))
            pars = int(m.group(2)) if m.group(2) else None
            sect = int(m.group(3)) if m.group(3) else None
            art, q = int(m.group(4)), int(m.group(5))
            if sect is not None: sectio_keys.add((d, pars, sect, art))
            delivered[(d, pars, art)].add(q)
    return delivered, sectio_keys

def run(volnum, verbose=False):
    cfg = VOLS[volnum]
    heads, seen_art, unparsed, promises = scan_raw(cfg["raws"])
    delivered, sectio_keys = scan_disk(cfg["dirs"])

    print(f"\n{'='*78}\nVOL {cfg['tag']}  —  promise-vs-delivery")
    print(f"{'='*78}")
    if not heads:
        print("  ⚠ NO running heads parsed from this volume's raw — the primary witness is")
        print("    unavailable here. Only the soft promise signal applies. NOT a clean result.")
    else:
        print(f"  running-head witnesses: {len(heads)} (d,pars,art) positions")

    findings = []

    # --- CHECK A: GAP in the delivered question sequence -----------------------------
    # Needs ONLY filenames. This is the signature of the Vol IV losses where the missing
    # question sits BETWEEN surviving siblings (d.47 a2-q3: disk had q1,q2,q4). Works on
    # every volume including Vol I pt1, which has no running heads.
    for key in sorted(delivered):
        d, pars, art = key
        got = delivered[key]
        gaps = [q for q in range(1, max(got)) if q not in got]
        if gaps:
            findings.append((d, pars, art, None, sorted(got),
                             f"GAP — q{gaps} missing between delivered siblings"))

    # --- CHECK B: running head outruns the delivered maximum -------------------------
    # Catches the losses at the TAIL of an article (d.46 a2-q4, d.42 a3-q3, d.49 s2-a4-q2),
    # which leave no gap. Needs the running-head witness.
    for key in sorted(heads):
        d, pars, art = key
        rh = heads[key]
        got = delivered.get(key)
        if got is None:
            alt = {k: v for k, v in delivered.items() if k[0] == d and k[2] == art}
            if alt:
                got = set().union(*alt.values())
            else:
                findings.append((d, pars, art, rh, None, "NO CHUNKS for this article"))
                continue
        if rh > max(got):
            findings.append((d, pars, art, rh, sorted(got),
                             f"TAIL — print shows QUAEST.{rh}, disk stops at q{max(got)}"))

    if findings:
        print(f"\n  ⚠ {len(findings)} POSITION(S) WHERE THE PRINT OUTRUNS THE CORPUS:\n")
        for d, pars, art, rh, got, why in sorted(findings):
            loc = f"d.{d}" + (f" p.{pars}" if pars else "") + f" a.{art}"
            rhs = f"QUAEST.{rh}" if rh else "—"
            print(f"    {loc:<16} runhead={rhs:<10} disk={got}  — {why}")
    else:
        print("\n  ✓ No gaps in delivered question sequences, and no running head outruns them.")
        print("    (Screen only: a question that never spans a page top leaves no running head.)")

    if unparsed:
        print(f"\n  {len(unparsed)} running head(s) with UNPARSEABLE numerals — not guessed, listed:")
        for path, ln, txt in unparsed[:12]:
            print(f"    {os.path.basename(path)}:{ln}  {txt}")
        if len(unparsed) > 12: print(f"    … and {len(unparsed)-12} more")

    # --- coverage: how much of the corpus did each check actually see? ---------------
    disk_keys = set(delivered)
    witnessed = {k for k in disk_keys if k in heads}
    # also count keys matched loosely (sectio volumes, where the head names ART inside SECT)
    loose = {k for k in disk_keys if k not in heads
             and any(h[0] == k[0] and h[2] == k[2] for h in heads)}
    cov = 100.0 * (len(witnessed) + len(loose)) / len(disk_keys) if disk_keys else 0.0
    print(f"\n  COVERAGE")
    print(f"    GAP check   : {len(disk_keys)}/{len(disk_keys)} articles (100%) — filenames only, "
          f"no witness needed")
    print(f"    TAIL check  : {len(witnessed)+len(loose)}/{len(disk_keys)} articles "
          f"({cov:.0f}%) had a running-head witness")
    if cov < 99:
        print(f"    ⚠ {len(disk_keys)-len(witnessed)-len(loose)} article(s) have NO running-head "
              f"witness — the TAIL check could not see them.")

    tot_promise = sum(promises.values())
    print(f"\n  soft signal: {tot_promise} 'quaeruntur N' openers found across "
          f"{len(promises)} distinction(s) (not attributed to articles — no line ranges)")
    return findings

if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--volume", type=int, choices=[1,2,3,4])
    ap.add_argument("--all", action="store_true")
    a = ap.parse_args()
    vols = [1,2,3,4] if a.all else [a.volume]
    total = 0
    for v in vols:
        total += len(run(v))
    print(f"\n{'='*78}\nTOTAL positions flagged: {total}\n{'='*78}")

# J4 Class D/E — apparatus backlog, continuation. SESSION HANDOFF (written 2026-07-17)

**Read this whole file before touching anything.** It is written for a **Sonnet** session — this
is mechanical, page-verified repair work, not a judgment-density task. Everything you need is
here; you should not need to re-derive the diagnosis. `manual-review/J4-HANDOFF.md` (the prior
J4 session's brief) is still useful background but is **not required reading** — this file is
self-contained and supersedes it for Class D/E purposes. If you want the fuller trap writeups,
read J4-HANDOFF.md §2 (the three traps) — they still apply here verbatim.

---

## 0. State of the world (verified 2026-07-17)

- Repo clean, `master` is **14 commits ahead of `origin/master`**, NOT pushed (protected — push
  needs Wilson's explicit per-action OK; do not push).
- Build: **1815 translated / 1925 questions / 4 books**. **This number must not change** —
  Class D/E work only touches `[^N]` apparatus markers/defs, never translated-status or wording.
  If a build after your edits reports a different translated count, you broke a chunk — stop and
  fix before continuing.
- **J4 Classes A, B, and C are ALL DONE** (commits `f6163b1`..`ad0a9a2`, 2026-07-17 session):
  22/22 Class-B orphaned-apparatus chunks, 10/10 Class-A duplicate-def chunks
  (`tools/fix-apparatus-labels.py` now reports 0 FIXABLE/0 SKIPPED corpus-wide), 3/3 Class-C
  anchor-with-no-def chunks. Do not re-touch any of those unless this file specifically flags a
  residual issue in one of them (a few do have deliberate, documented refusals — see §5).
- **This file is about Class D/E: repeated anchors in a body** (same `[^N]` appears 2+ times in
  one language). At handoff time this is **~43 chunks** flagged unhealthy by the §6 classifier,
  after netting out documented Class B/C refusals (see §5) — **39 of those are genuinely
  untouched** (§4 table). Active translation front is d.43+ — DO NOT touch it, this is repair
  work only.

## 1. What Class D/E actually is (revised understanding — READ THIS FIRST)

The original J4-HANDOFF.md described Class D/E optimistically: *"No text is lost — the note
still binds; there is just an extra superscript on the page... these may be legitimate."* It
recommended sampling 3-4 chunks before any bulk work, expecting most to be the benign case
(Quaracchi genuinely citing one footnote from two lemmas).

**A 2026-07-17 sample of 4 chunks falsified that expectation. Zero of the 4 were the benign
case.** Every one needed real, page-verified repair:

1. **`I-d37-littera`** — the "duplicate" `[^20]` is a symptom of a small **cascading mislabel
   cluster** (~5 adjacent markers, roughly `[^18]`–`[^22]`, on printed p.634): content-matching
   showed the def bound to `[^20]`'s first body occurrence actually belongs to a DIFFERENT
   marker (`[^18]`), and the second `[^20]` occurrence is a pure phantom with no printed
   counterpart at all. Needs Class-A-style reconciliation of the whole local cluster, not a
   1-line delete.
2. **`IV-d21-p1-littera`** — **not a real defect.** It's a **false positive** from a different,
   more important bug — see §2 below. Do not "fix" this chunk's apparatus; there is nothing
   wrong with its 14 real anchors.
3. **`II-d23-a2-q2`** — genuine **Class-B-style content loss**: ~17 real footnotes across printed
   pp.540–541 were never transcribed. The chunk's own `## Notes` self-confesses mapping the
   p.540/p.541 anchors "by position" onto the p.539 `[^1]`–`[^9]` scheme — this is exactly
   TRAP 1 (Quaracchi restarts numbering per page; a body anchor's true note must be found by
   CONTENT, never by position). 4 spot-checked anchors were all bound to the wrong def's content.
4. **`IV-d4-p1-a2-q1`** — worse: real **content loss**, not just mislabeling. ~8 of 19 real
   p.100–101 footnotes were never transcribed at all, including a citation of **Constantine's
   edict** (via Eusebius) that is completely absent from the file. Several anchors are bound to
   the wrong page's def content across the p.100/p.101 restart boundary.

**Working assumption for this pass: treat every Class D/E chunk as a suspected mislabel/missing-
content case (Class A/B-style), not a stray-marker judgment call, until you've actually read the
printed page and found otherwise.** If a chunk genuinely turns out to be the benign
"one note, two lemmas" case, great — that's a fast chunk, just document the print evidence and
move on. But don't assume it going in.

## 2. ⚠ SEPARATE BUG FOUND — NOT Class D/E, needs its own decision from Wilson

`IV-d21-p1-littera` and `III-d33-dubia` both use a corpus convention where a chunk's `## Latin`
(or `## Apparatus`) intro note **explains** the per-page footnote-numbering scheme using
backtick-quoted example ranges, e.g.:

> the markers are numbered continuously `` `[^1]–[^14]` `` across the whole Master's text...
> Page-block split: `` `[^1]–[^3]` `` = p.543...

**Both the §6/polish-style-scan classifier regex AND the live site's renderer
(`site/src/app/browse/[bookId]/d/[distId]/q/[qId]/text-reader.tsx:282`) are regex-based and do
NOT respect backtick code-spans.** So:
- The classifier miscounts these backtick-quoted example numbers as real body anchors, producing
  false-positive "duplicate/extra anchor" flags (this is what happened to both chunks above).
- **Worse: the live renderer actually turns each example number into a clickable, spurious
  footnote superscript inside what's supposed to be plain explanatory prose**, on the real
  deployed site. This is the same failure class as the already-known "literal `[^N]` in prose
  steals the binding" bug (documented in repo `CLAUDE.md` and hit twice in J2), except here it's
  inside `## Latin`/`## Apparatus` intro notes rather than `## Notes`/Scholion blocks.

A corpus-wide grep hits **300+ files** using this convention:
```
grep -rl '^> .*\[\^[0-9]' vol1 vol2 vol3 vol4 | wc -l
```
Most won't trip the count-mismatch classifier (their example numbers happen to overlap harmlessly
with real anchors), but the **live-render bug likely affects most of them to some degree**.

**Do NOT attempt to fix this corpus-wide as part of a Class D/E chunk-by-chunk pass** — it's a
different kind of fix (either de-fence the notation everywhere, e.g. write "notes 1–14" instead
of `` `[^1]–[^14]` ``, or teach the classifier + renderer regex to skip backtick code-spans; the
second is more robust but requires a code change and a scan for other affected pages). **This
needs Wilson's decision before anyone touches it.** If you encounter a Class D/E chunk in §4 that
turns out to ALSO be this same false-positive (an explanatory blockquote with backtick-quoted
`[^N]` ranges accounting for its whole "duplicate" count), do the same diagnosis as
`IV-d21-p1-littera`/`III-d33-dubia`: **confirm it, change nothing, document it in the chunk's
`## Notes`, and add it to a running list to report back** — do not fix the underlying notation
yourself without asking.

## 3. Method (unchanged from J4-HANDOFF.md — the proven recipe)

**Vol II OVERRIDE applies** to Vols II/III/IV (two-column, cascade-shattered OCR): **the PDF is
authoritative**; the IA djvu OCR is only a hint. Vol I is single-column, offset differs — check
`tools/extract-pages.py`'s vol1 config or the chunk's own `## Notes`/frontmatter for the pdf page
actually used before extracting.

```bash
# page images (offset: vol1 pt1 = printed+102 · vol1 pt2 = printed+? (check tool/file) ·
# vol2/vol3 = printed+22 · vol4 = printed+20)
python3.11 tools/extract-pages.py --volume vol3 --pages 692-694 --dpi 450 --force
python3.11 tools/colcrop.py vol3 693 1660       # vol2/vol3 split ~1660; VOL4 split = 1880
# -> reads to /tmp/colcrop/vol3-p693-{L,R}-{0,1,2}.png
```
⚠ **Never `Read` a full-page image at 450dpi for a two-column volume** — it exceeds the API's
5 MB image limit. Always read the `colcrop` bands. Vol I (single-column) may be small enough to
read directly — check file size first; crop if near/over 5MB.

**Finding the printed page range:** grep the chunk file for `pp.` or `p.` in its header/Notes, or
check `printed_pages:` in frontmatter if present.

**To diagnose a "duplicate anchor":**
1. Identify exactly which label(s) repeat, and in which language(s) — a small Python snippet
   (see §7) will tell you the labels and counts.
2. Read the printed page for EVERY occurrence of that label in the body — is there really a
   printed superscript at each spot, or is one/more a phantom?
3. Read each candidate def's content — which lemma does it actually describe? Match by content,
   never by position (TRAP 1). A "duplicate" is very often actually two DIFFERENT footnotes that
   got the same label by a numbering/counting error upstream — meaning the fix is usually a
   RELABEL of a small local cluster (see the `I-d37-littera` sample), not a simple deletion.
4. Check whether the def count vs. anchor count gap could indicate GENUINELY MISSING content
   (Class B in disguise, per `II-d23-a2-q2`/`IV-d4-p1-a2-q1`) — if the page shows footnotes with
   NO transcribed def at all, that's the real bug, and you'll need to transcribe them (mirroring
   the `**La.** ... **En.** ...` format already used elsewhere in the same file).
5. Check for the backtick-blockquote false-positive (§2) before doing any of the above — it's a
   two-minute check (grep the file for `` `[^ `` inside a `>` blockquote) that can save you from
   investigating a phantom problem.

## 4. THE WORK — 39 untouched chunks (regenerate with §7 anytime)

No priority ordering is implied by this list — pick chunks in any order, but do them ONE AT A
TIME per subagent, PDF-verified. Given the sample findings, budget real time per chunk (comparable
to a Class A/B chunk from the prior session), not a quick skim.

| chunk | defs | la | en |
|---|---|---|---|
| `vol1/bon-sent-I-d28-a1-q2.md` | 9 | 10 | 10 |
| `vol1/bon-sent-I-d3-p2-a2-q2.md` | 13 | 15 | 15 |
| `vol1/bon-sent-I-d32-a2-q2.md` | 10 | 11 | 11 |
| `vol1/bon-sent-I-d32-littera.md` | 15 | 22 | 15 |
| `vol1/bon-sent-I-d33-a1-q3.md` | 12 | 13 | 13 |
| `vol1/bon-sent-I-d35-littera.md` | 15 | 16 | 16 |
| `vol1/bon-sent-I-d36-a2-q2.md` | 8 | 9 | 9 |
| `vol1/bon-sent-I-d4-a1-q2.md` | 14 | 16 | 16 |
| `vol1/bon-sent-I-d41-a2-q1.md` | 12 | 14 | 12 |
| `vol1/bon-sent-I-d41-a2-q2.md` | 28 | 30 | 28 |
| `vol1/bon-sent-I-d42-dubia.md` | 17 | 19 | 17 |
| `vol1/bon-sent-I-d43-a1-q2.md` | 22 | 23 | 22 |
| `vol1/bon-sent-I-d43-a1-q4.md` | 13 | 15 | 13 |
| `vol1/bon-sent-I-d43-dubia.md` | 21 | 23 | 21 |
| `vol1/bon-sent-I-d44-dubia.md` | 17 | 19 | 17 |
| `vol1/bon-sent-I-d46-dubia.md` | 24 | 26 | 24 |
| `vol1/bon-sent-I-d47-a1-q1.md` | 16 | 17 | 17 |
| `vol1/bon-sent-I-d47-dubia.md` | 12 | 14 | 12 |
| `vol1/bon-sent-I-d9-dubia.md` | 65 | 66 | 66 |
| `vol2/bon-sent-II-d1-p1-divisio.md` | 5 | 6 | 6 |
| `vol2/bon-sent-II-d17-a2-q2.md` | 19 | 20 | 20 |
| `vol2/bon-sent-II-d25-p1-a1-q3.md` | 26 | 27 | 27 |
| `vol2/bon-sent-II-d34-littera.md` | 7 | 8 | 8 |
| `vol3/bon-sent-III-d32-littera.md` | 9 | 10 | 9 |
| `vol4/bon-sent-IV-d10-p2-a1-q3.md` | 10 | 14 | 14 |
| `vol4/bon-sent-IV-d11-p1-a1-q6.md` | 15 | 16 | 16 |
| `vol4/bon-sent-IV-d13-dubia.md` | 20 | 21 | 21 |
| `vol4/bon-sent-IV-d15-p1-a1-q6.md` | 12 | 13 | 13 |
| `vol4/bon-sent-IV-d17-p2-a1-q1.md` | 14 | 15 | 14 |
| `vol4/bon-sent-IV-d20-p1-a1-q5.md` | 15 | 16 | 16 |
| `vol4/bon-sent-IV-d22-dubia.md` | 8 | 10 | 8 |
| `vol4/bon-sent-IV-d23-littera.md` | 7 | 9 | 7 |
| `vol4/bon-sent-IV-d24-p1-a2-q4.md` | 12 | 16 | 12 |
| `vol4/bon-sent-IV-d26-littera.md` | 8 | 10 | 8 |
| `vol4/bon-sent-IV-d3-p1-littera.md` | 10 | 14 | 14 |
| `vol4/bon-sent-IV-d3-p2-a2-q2.md` | 10 | 11 | 11 |
| `vol4/bon-sent-IV-d3-p2-a3-q1.md` | 29 | 31 | 29 |
| `vol4/bon-sent-IV-d42-a1-q3.md` | 13 | 15 | 13 |
| `vol4/bon-sent-IV-d42-a3-q1.md` | 11 | 13 | 11 |

**Also flagged, needs its OWN investigation (mixed case, not pure D/E):**
`vol1/bon-sent-I-d42-a1-q4.md` (defs=27, la=30, en=30). This chunk has THREE separate issues
tangled together: (a) a genuine Class-D/E-style set of extra anchors (`la` has extras at labels
`1`, `28`, `26`; `en` has extras at `24`, `26`), (b) the pre-existing `[^?]` stray in the English
body (see J4-HANDOFF.md-era chunk `I-d1-a1-q3` for the same pattern — likely another phantom, but
verify against print, don't assume), sitting inside (c) an already-documented HEAVILY GARBLED
p.758 scholion passage (multiple bracketed `[?]` uncertainty flags already logged in
`manual-review/d41-d50-polish-resolution-log.md`, 2026-05-12) — meaning normal page-image
verification may be harder here than elsewhere. Take extra care; if the garble makes content-
matching genuinely impossible, refuse and document rather than guess.

## 5. Chunks with DELIBERATE, DOCUMENTED residual "unhealthy" status — DO NOT touch

These already went through Class B/C repair this session and have specific, evidence-backed
refusals recorded in their own `## Notes`. The §6 classifier still flags them (expected) — do not
re-open unless you find NEW evidence the prior refusal was wrong:

- `vol3/bon-sent-III-d15-divisio.md` — `notae-2` orphaned, refused (no printed counterpart found)
- `vol3/bon-sent-III-d31-a3-q3.md` — notes 1/2/3 orphaned, refused (no printed superscript on
  p.692 for any of them — likely a genuine 1887 Quaracchi erratum)
- `vol3/bon-sent-III-d32-a1-q2.md` — notes 13/14 orphaned, refused (verbatim duplicates of 8/9,
  no second printed location)
- `vol3/bon-sent-III-d33-dubia.md` — **this is the §2 backtick-blockquote false positive**, not a
  real defect. Confirmed 2026-07-17.
- `vol3/bon-sent-III-d5-a2-q4.md` — note 11 orphaned, refused (marginal source-sigil, not a
  footnote, per print)
- `vol4/bon-sent-IV-d1-p2-a2-q2.md` — `[^2b]` in Latin but missing from English (a genuine,
  documented gap — not yet fixed, fair game if you want to pick it up, but it's Class-B-shaped,
  not D/E; treat it like the other "extra anchor in one language only" cases below if you do)
- `vol4/bon-sent-IV-d14-p2-a2-q1.md` — notes 15/17 orphaned, refused (verbatim duplicates)
- `vol4/bon-sent-IV-d16-p2-a2-q2.md` — note 6 orphaned, refused (TRAP 3c — belongs to sibling
  `IV-d16-p2-a2-q1.md`, already correctly anchored there)

## 6. Rules of engagement

- **One chunk per subagent.** Give each the chunk, its page range, and a pointer to this file
  (§1–§3) plus J4-HANDOFF.md §2 (the traps) if you want the fuller writeup.
- **Never relabel or delete by position.** Always confirm by content against the printed page.
- **Refuse rather than guess.** A chunk left with a documented, evidence-backed refusal is a good
  outcome — do not force a resolution you're not confident in.
- **If you find genuinely missing apparatus content** (Class B in disguise): transcribe it
  verbatim from the page image, matching the `**La.** ... **En.** ...` format already used
  elsewhere in the same file.
- **If you find the §2 backtick-blockquote false positive:** change nothing in that chunk: just
  confirm, document in `## Notes`, and add it to a list to report back (do not fix the underlying
  convention).
- Never change Latin text, English wording, or existing correct apparatus prose — only add/fix/
  remove `[^N]` marker tokens and, where genuinely missing, add new apparatus `**La.**/**En.**`
  def entries transcribed from the page.
- Record every disposition in the chunk's `## Notes`.
- Commit per batch of ~4 chunks (matches the cadence that worked well in the prior J4 session),
  not all at once.
- **Vol I / Vol II / Vol III are PUBLISHED.** Be conservative; when in doubt, report.
- **Do NOT `git push`, do NOT deploy.** Both need Wilson's explicit per-action OK. Commit locally,
  report, and ask.

## 7. Verify — run after EVERY batch

Corpus-wide health check (same as J4-HANDOFF.md §6):
```bash
cd ~/bonaventure-sentences && python3.11 - <<'EOF'
import re, glob
def sec(t,n,x):
    m=re.search(rf'^## {n}\s*$',t,re.M)
    if not m: return ""
    r=t[m.end():]; m2=re.search(rf'^## (?:{x})\s*$',r,re.M)
    return r[:m2.start()] if m2 else r
bad=0; n=0
for d in ["vol1","vol2","vol3","vol4"]:
    for f in sorted(glob.glob(f"{d}/*.md")):
        t=open(f,encoding="utf-8").read()
        if "Phase C Tier 2 complete" not in t: continue
        defs=re.findall(r'^\[\^([^\]]+)\]:',sec(t,"Apparatus","Notes|Latin|English"),re.M)
        la=re.findall(r'\[\^([^\]]+)\]',sec(t,"Latin","English|Apparatus|Notes"))
        en=re.findall(r'\[\^([^\]]+)\]',sec(t,"English","Apparatus|Notes|Latin"))
        if not defs and not la: continue
        n+=1
        D=set(defs)
        healthy = (D==set(la)==set(en) and len(defs)==len(D)
                   and len(la)==len(set(la)) and len(en)==len(set(en)))
        if not healthy:
            bad+=1
            print(f"  {f:<44} defs={len(defs)} la={len(la)} en={len(en)}")
print(f"\n{n} chunks with apparatus; {bad} unhealthy")
EOF
```

Per-chunk duplicate-label finder (use while diagnosing one file):
```bash
cd ~/bonaventure-sentences && python3.11 - <<'EOF'
import re
from collections import Counter
def sec(t,n,x):
    m=re.search(rf'^## {n}\s*$',t,re.M)
    if not m: return ""
    r=t[m.end():]; m2=re.search(rf'^## (?:{x})\s*$',r,re.M)
    return r[:m2.start()] if m2 else r
t=open("PATH/TO/CHUNK.md",encoding="utf-8").read()
defs=re.findall(r'^\[\^([^\]]+)\]:',sec(t,"Apparatus","Notes|Latin|English"),re.M)
la=re.findall(r'\[\^([^\]]+)\]',sec(t,"Latin","English|Apparatus|Notes"))
en=re.findall(r'\[\^([^\]]+)\]',sec(t,"English","Apparatus|Notes|Latin"))
D=set(defs)
print("la dupes/extras:", [k for k,v in Counter(la).items() if v>1 or k not in D])
print("en dupes/extras:", [k for k,v in Counter(en).items() if v>1 or k not in D])
EOF
```

Then always:
```bash
cd site && node scripts/build-content.mjs     # MUST still say 1815 translated / 1925 questions
```

Baseline at this handoff: **~43 unhealthy** (39 untouched + the flagged `I-d42-a1-q4` mixed case
+ 2 already-sampled-but-unfixed content-loss chunks `II-d23-a2-q2`/`IV-d4-p1-a2-q1`, minus the
already-fixed `I-d37-littera`... — just regenerate with the script above at session start, don't
trust this number as-is since it will have drifted).

## 8. Suggested plan

1. Re-run §7's corpus scan to confirm the current list is accurate.
2. Start with the two already-diagnosed content-loss chunks if you want a fast, confident win:
   `II-d23-a2-q2` and `IV-d4-p1-a2-q1` already have the full diagnosis written up in §1 items 3–4
   — you mostly just need to transcribe the missing footer text from the (already-crop-verified)
   page images and relabel.
3. Work through §4's table in batches of ~4, one subagent per chunk, PDF-verified.
4. Handle `I-d42-a1-q4` carefully given its garbled-passage complication (§4 footnote).
5. Keep a running list of any NEW backtick-blockquote false positives you find (§2) — do not fix
   them, just report.
6. Commit per batch. Verify build + corpus scan after each.
7. At the end: report to Wilson with (a) final unhealthy count, (b) the backtick-blockquote
   false-positive list for his decision, (c) ask about push + deploy.

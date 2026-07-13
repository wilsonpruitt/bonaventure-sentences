# J4 — apparatus backlog, final job. SESSION HANDOFF (written 2026-07-13)

**Read this whole file before touching anything.** It is written for a **Sonnet** session.
Everything you need is here; you should not need to re-derive the diagnosis.

---

## 0. State of the world (verified 2026-07-13)

- Repo clean, `master` == `origin/master` @ `0241d34`, production deployed, site 200.
- Build: **1798 translated / 1924 questions / 4 books**. **This number must not change.**
  If a build after your edits reports anything other than 1798, you broke a chunk — stop and fix.
- J1 (`2e362ed`), J2 (`7ccf7d8`), J3 (`0241d34`) are DONE, pushed, and live.
  Corpus scan went 94 issues/64 chunks → 60/36.
- Active translation front is **d.41** — DO NOT touch it. J4 is repair work only.

## 1. What J4 is

Apparatus (footnote) defects across the corpus, all **pre-existing**, none in Vol IV d.31–d.40.
The site renders footnotes by matching `[^N]` markers in the bodies to `[^N]:` definitions in
`## Apparatus`. When those don't line up, footnotes are dropped, mis-bound, or dangle.

**A Tier-2 chunk is healthy iff:**
```
set(apparatus defs) == set(Latin anchors) == set(English anchors)
and no def is defined twice, and no anchor appears twice in a body.
```

## 2. ⚠ THE THREE TRAPS — J1/J2/J3 each nearly corrupted the text. Do not repeat these.

**TRAP 1 — Never relabel or re-anchor BY POSITION.**
Quaracchi numbers its footers in **COLUMN order** while anchors fall in **READING order**, so a
body legitimately runs `1, 3, 2, 4`. In `IV-d20-p2-dubia`, `[^3]` sits on *procedat* (its note is
the variant *procedit*) and `[^4]` on *tantum* (note: *omittunt tantum*). Assigning the i-th
marker to the i-th definition would have swapped notes 2 and 3 — a silent, plausible corruption.
**Always key on CONTENT: read the apparatus entry, it names the lemma it annotates.**

**TRAP 2 — `<!-- page N -->` comments are NOT reliable for footnote attribution.**
They disagree with the true footnote-group boundaries in many chunks (`IV-d17-p2-dubia`: p.448
holds body markers 1–5 but that page's footer group is 1–9). Use them as a hint, never as proof.

**TRAP 3 — "unanchored apparatus" is THREE different bugs. Diagnose before fixing.**
J3 hit all three in one batch of 7 chunks:
  a. markers genuinely missing from a body → mirror them from the other body (no PDF needed);
  b. anchors present but transcribed as **literal unicode superscripts (¹²³)** instead of `[^N]`
     → the build never links them; convert in place (no PDF needed beyond a confirm);
  c. **apparatus filed under the WRONG CHUNK** → a *divisio*'s notes actually answer to
     superscripts printed in Lombard's **littera**, above the `COMMENTARIUS` heading on the same
     page, and already exist correctly anchored in the sibling littera chunk. The fix is to
     **DELETE the duplicates**, not to invent anchors. (Hit `d12`/`d14`/`d15-p1-divisio`.)

**THE RULE THAT SAVED US: if you cannot place an anchor with evidence, REFUSE. Report it. Do not
guess.** Three subagents refusing is exactly what exposed trap 3c.

## 3. Method (the proven recipe)

**Vol II OVERRIDE applies** to Vols II/III/IV (two-column, cascade-shattered OCR): **the PDF is
authoritative**; the IA djvu OCR is only a hint. See repo `CLAUDE.md`.

```bash
# page images (offset: vol1 pt1 = printed+102 · vol2/vol3 = printed+22 · vol4 = printed+20)
python3.11 tools/extract-pages.py --volume vol3 --pages 692-694 --dpi 450 --force
python3.11 tools/colcrop.py vol3 693 1660       # vol2/vol3 split ~1660; VOL4 split = 1880
# -> reads to /tmp/colcrop/vol3-p693-{L,R}-{0,1,2}.png
```
⚠ **Never `Read` a full-page image** — at 450 dpi it exceeds the API's 5 MB image limit and the
call fails. Always read the `colcrop` bands. If a column is clipped, re-crop with a different
split (`2120` wider-L, `1780`/`1620` narrower-L).

**To place an orphaned note:** find the small raised superscript numeral in the printed body text
on the band. It sits on a specific word. That word is the anchor. Confirm with the apparatus
entry's own content (a codex variant names its lemma; a citation names its source).

## 4. THE WORK — 4 classes, in priority order

Regenerate the current list any time with the classifier in §6.

### Class B — ORPHANED DEFINITIONS (22 chunks). **DO THIS FIRST — highest harm.**
A definition exists but **nothing anchors it in either body**, so it renders as a dangling
footnote. Needs the PDF: find the printed superscript, place `[^N]` in the Latin at that lemma
and mirror it in the English.

⚠ **Check trap 3c FIRST on every `*-divisio` chunk in this list.** Before hunting an anchor, diff
the chunk's apparatus against its sibling **littera** chunk. If the notes duplicate the littera's
(and the littera is complete and fully anchored), the fix is to DELETE them and set
`has_apparatus: false`, exactly as J3 did for d12/d14/d15. Suspects: `IV-d1-p1-divisio`,
`IV-d13-divisio`, `IV-d16-p1-divisio`, `IV-d17-p1-divisio`, `III-d15-divisio`.

| chunk | defs | orphaned | pages |
|---|---|---|---|
| `III-d33-dubia` | 33 | 16 | 728–731 |
| `III-d33-a1-q3` | 33 | 10 | 715–719 |
| `III-d31-a3-q3` | 25 | 10 | 692–694 |
| `III-d32-a1-q2` | 21 | 9 | 699–701 |
| `IV-d13-divisio` | 6 | 5 | 301–302 |
| `IV-d18-p1-a3-q1` | 14 | 5 | 478–480 |
| `III-d19-dubia` | 20 | 4 | 412–414 |
| `IV-d14-p2-a2-q1` | 17 | 4 | 335–337 |
| `IV-d16-p1-divisio` | 6 | 4 | 382–383 |
| `III-d32-a1-q1` | 13 | 3 | 697–699 |
| `III-d34-p2-a1-q1` | 11 | 3 | 753–756 |
| `IV-d1-p1-divisio` | 6 | 3 | 10–11 |
| `IV-d10-p2-a2-q2` | 15 | 3 | 236–237 |
| `III-d15-divisio` | 5 | 2 | 329 |
| `III-d31-a2-q3` | 19 | 2 | 685–687 |
| `IV-d12-p1-a3-q2` | 11 | 2 | 284–285 |
| `IV-d16-p2-a2-q2` | 12 | 2 | 407–408 |
| `IV-d17-p1-divisio` | 4 | 2 | 418 |
| `III-d22-a1-q1` | 30 | 1 | 450–453 |
| `III-d5-a2-q4` | 22 | 1 | 138–140 |
| `IV-d1-p2-a2-q2` | 25 | 1 | 39–41 |
| `IV-d8-p2-a2-q1` | 8 | 1 | 195–196 |

### Class A — DUPLICATE DEFINITIONS (10 chunks). Second priority — footnotes are being DROPPED.
Two or three `[^1]:` definitions in one chunk (Quaracchi restarts numbering on every printed
page). A body marker binds only one, so the rest are lost at render.

**J1's script already fixed the 15 that could be PROVEN safe** — these 10 are the residue it
**refused** because their body partition does not match the definition groups (i.e. they ALSO have
missing or duplicated anchors). So they need the PDF: reconcile anchors against the printed page
first, THEN relabel.

Once a chunk's anchors are correct, you can re-run the J1 tool to do the relabel mechanically:
```bash
python3.11 tools/fix-apparatus-labels.py            # dry run — shows FIXABLE vs SKIPPED
python3.11 tools/fix-apparatus-labels.py --apply    # writes; backs up to _backup-apparatus-labels/
```
It is safe: it keys on (footnote-group, existing number) via a greedy repeat-partition and
**requires** the body partition to match the apparatus groups before writing.

`III-d26-a1-q3` (12 dup) · `III-d27-a1-q4` (16) · `III-d29-a1-q1` (16) · `III-d27-a2-q1` (14) ·
`III-d26-a2-q5` (13) · `III-d29-a1-q2` (13) · `IV-d6-p1-littera` (15) · `IV-d18-p2-a1-q3` (9) ·
`III-d30-a1-q4` (6) · `III-d11-a1-q1` (3)

### Class C — ANCHOR WITH NO DEFINITION (2 chunks). Small.
A `[^N]` in the body with no `[^N]:` entry — the footnote link goes nowhere.
- `IV-d15-p1-a1-q4` — `[^6b]` is anchored in BOTH bodies but has no definition; it appears to
  shelter under the `[^6]` entry. Needs the printed page to say whether it is a real separate
  note (→ transcribe it) or a stray marker (→ delete it).
- `I-d1-a1-q3` — 1 extra Latin/English anchor beyond the 16 defs.

Also here: **`IV-d7-divisio`** — has literal unicode superscripts in its body and **ZERO
apparatus definitions**. Its footnotes were never transcribed at all. Read the printed page and
transcribe them (`**La.** … **En.** …`), or confirm they belong to a neighbouring chunk (trap 3c).

### Class D/E — REPEATED ANCHORS IN A BODY (42 chunks). **LOWEST priority. Decide before doing.**
The same `[^N]` appears twice or more in a body (e.g. `I-d32-littera`: 15 defs, 22 Latin anchors).
**No text is lost** — the note still binds; there is just an extra superscript on the page.

**These may be legitimate.** Quaracchi does sometimes reference one note from two lemmas. But in
`IV-d9-a1-q1` (J3) the duplicates turned out to be **spurious strays**. So: **sample 3–4 of these
against the printed page first and report what you find** before doing any bulk work. If the print
shows one superscript, the extra anchor is a stray → delete it. If the print shows two, it is
faithful → leave it and record that the corpus convention allows it.
Do NOT bulk-delete on the assumption they're strays.

## 5. Rules of engagement

- **One chunk per subagent.** Give each the chunk, its page range, its band paths, and traps 1–3.
- **Never change Latin text, English wording, or apparatus prose.** J4 edits only `[^N]` markers,
  and (class C / d7-divisio) transcribes genuinely missing apparatus entries.
- **Refuse rather than guess.** A chunk left broken with a clear report is a good outcome.
- Keep `[^…]` tokens OUT of prose in `## Notes` / scholion-redirect blocks — a literal `[^20]` in
  prose renders as a LIVE footnote link and steals the binding (this bit `III-d34-p2-a2-q2` and
  `III-d36-a1-q6` in J2).
- Record every disposition in the chunk's `## Notes`.
- Commit per class (or per small batch), not all at once.
- **Vol I / Vol II / Vol III are PUBLISHED.** Be conservative; when in doubt, report.

## 6. Verify — run after EVERY batch

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
            print(f"  {f:<44} defs={len(defs)} la={len(la)} en={len(en)} "
                  f"dupDefs={len(defs)-len(D)} orphanDefs={sorted(D-set(la),key=str)} "
                  f"extraLa={sorted(set(la)-D,key=str)}")
print(f"\n{n} chunks with apparatus; {bad} unhealthy")
EOF
```
Baseline at handoff: **76 unhealthy**. Every batch should drive that down and never up.

Then always:
```bash
cd site && node scripts/build-content.mjs     # MUST still say 1798 translated
cd .. && python3.11 tools/polish-style-scan.py | tail -1    # baseline: 60 issues / 36 chunks
```

## 7. Protected actions — STOP and ask Wilson

**Do NOT** `git push`, and **do NOT** deploy. Both need his explicit per-action OK.
Commit locally, report, and ask. (Deploy recipe, for when he says yes:
`cd site && node scripts/build-content.mjs && npx vercel build --prod && npx vercel deploy --prod --prebuilt --archive=tgz`)

## 8. Suggested plan

1. Re-run the §6 classifier to confirm the lists are current.
2. **Class B, divisio chunks first** — check trap 3c; several are probably delete-not-anchor and
   will fall fast. Commit.
3. **Class B, the rest** — one subagent per chunk with band reads. Commit in batches.
4. **Class A** — reconcile anchors on the page, then re-run `tools/fix-apparatus-labels.py`. Commit.
5. **Class C** + `IV-d7-divisio`. Commit.
6. **Class D/E** — sample 3–4, report to Wilson, do NOT bulk-edit without his call.
7. Report; ask about push + deploy.

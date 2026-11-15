# Vol VII *Lucam* p. 88 GATE (ruling 14: Pars I closes; Cap. I–III complete): EVIDENCE SHEET

Compiled 2026-11-14 by a read-only agent. **Nothing here is settled. Wilson rules off this sheet.** No file under `vol7/`,
`tools/`, `site/`, `index/` or the resume note was edited. Nothing was committed, pushed or stashed. Two other agents ran at
the same time and their work is not repeated here: the mechanical passes (live flags, style scan, boundary sweep; draft at
`manual-review/vol7-lucam-p88-gate-passes-draft.md`) and manifest stage 2 (Cap. IV on).

**Scope: all 22 chunks in `vol7/`, pp. 3–88** (2 front matter + `c1` ×8, `c2` ×7, `c3` ×5). The p. 27 gate (rulings 17–26)
already ruled on the first six. **The new ground is the 16 chunks from `bon-luc-c1-v39-45` on**, plus anything that recurs
across the whole set. Docket source: the consolidated G1–G50 / T1–T13 block at the top of `next-session-resume.md` and each
chunk's `## Notes`.

⛔ **Every census is taken over the RENDERED region only:** the `## Latin` body, the `## English` body, and the `**La.**` /
`**En.**` halves of `## Apparatus`. Frontmatter and `## Notes` are excluded, and so are `tr-` definitions (they are ours and
quote the Latin they discuss). Cells read **body+apparatus**. Scripts: scratchpad `g88/regions.py`, `g88/census.py`
(all 22 chunks), `g88/drc.py`. Douay checked against `~/douay-glossa/raw/DRC.json` (Challoner), Vulgate against
`raw/VulgClementine.json` in the same repo.

**Lines** in the cost columns are lines of the chunk file. Every body paragraph and every apparatus half is one line, so
"1 line" can carry several sites. A correction that touches only `## Notes` or the manifest is counted as "doc".

---

## ▶ DOCKET SUMMARY (one word each: "Approve" takes the ⭐ recommendation)

Ordered so the items that change visible text or set a lasting convention come first.

| # | item | ⭐ recommendation (mine) | lines it changes | kind |
|---|---|---|---|---|
| 1 | The conspicuous ruling-20 Douay departures (Luke 2:32 "A lumen", v. 25 "God-fearing", Isa. 52:7 "him that announceth", the *complacere* triad, Prov. 31:28) | **Ratify all five as built.** Each passes ruling 20's test on the page, and each Douay alternative would erase or collide with something the exposition does | **0** | ratify |
| 2 | Consistency pairs: one verse or proposition, two renderings (2:19 "pondering" / 2:51 "Conferring"; v. 54 *puerum* "child" / v. 69 *pueri* "servant"; Col. 1:13 "dilection" / "love") | **Keep all three splits.** Ruling 20 is producing them as written: the exposition leans at one site and not at the other. **One fix of my own:** `c3-v23-38` ¶ 63 drops the Douay's "his", because Quaracchi prints *filii dilectionis* with no *suae* | **1** | per-site |
| 3 | Ruling-18 scope: *evangelizare* in the OT, Bede's echo, and *annuntiare* verses | **Amend ruling 18's clause** to "the Douay's 'good tidings' stands wherever the Douay itself has it, OT included". All three OT *evangelizare* verses in the Vulgate (Ps. 67:12, Isa. 40:9, Nah. 1:15) read "good tidings" in the Douay. Isa. 40:9 as built; Isa. 52:7 / 61:1 *annuntiare* → "announce" ratified | **0** + ruling sentence | ruling |
| 4 | *praeconium* → "proclamation", beside ruling 12's ban on "proclaim" | **Ratify, and write it into ruling 12:** "proclaim / proclamation" belongs to *praeconium* alone; *praeco* is "herald"; *praedicare* is never "proclaim". 15 sites, all "proclamation"; zero "proclaim" anywhere in English | **0** + ruling sentence | ruling |
| 5 | `tr-pietas` outside cc. 15–16 (`c1-v46-56` ¶ 93, `c2-v25-35` ¶ 69) | **Ratify the extension.** `tr-pietas` goes at the first site of ANY chunk where the *pietas* is God's; cc. 15–16 is where the review is held, not the only place the note can go | **0** + ruling sentence | ruling |
| 6 | New house renderings, batch RATIFY (*poenitentia*, *vacare* + `tr-vacare`, *quies* / *requies*, the angelic *lumen*, *claritas*, *clarificatio*, *timoratus*, *corripere* / *arguere*, *erudire* / *eruditor*, *largitas*, the word-pairs G24–G32, *vir occasionatus* …) | **Ratify the batch.** **One fix:** `c1-v18-25` ¶ 38 *erudimur* "we are taught" → "we are schooled", to match the three later *erudi-* body sites (and *docere* "teach") | **1** | batch |
| 7 | `title_la`: the sentence-title precedent (G3) and the other ruling-22 applications (G1, G2, G4) | **Ratify all as built.** Correct the manifest's stale cell for `c2-v21-24`, which names the t3 where the builder rightly took the lower t4 | **0** + 1 manifest line | doc |
| 8 | Manifest-cell edits (G50): two builders changed only the `confidence` cell of their own row, `low` → `high` | **Ratify.** Ruling 26 ordered exactly this edit; the diffs touch that cell and nothing else | **0** | ratify |
| 9 | Genealogy names policy (G40) | **Ratify as the work's names policy:** English in the Douay's spellings; Latin as printed; a name *mentioned* as a word (Jerome's etymologies, variants) stays Latin and italic | **0** | convention |
| 10 | Records, misprints and banked evidence (G38–G39, G41–G49) | **Ratify as recorded.** No text edit; the collection-change bank (G45–G46) asks no ruling | **0** | record |
| 11 | **Tool fix job** (T1–T13 + the inbound-form question) | **ONE bounded Sonnet job after the gate,** scope in § 11. T5 stays deferred (ruling 24 / *Ioannem* 82(a)); T2 closes (never recurred). The two own-commentary *Exposit.* inbounds go in through a site table, not by widening the regex | **0** text; 1 tool job | tool |
| 12 | **The p. 88 deploy: what must be true first** (no recommendation for or against) | Preconditions only, in § 12. Two are **not yet met**: the authorities ledger holds **zero** vol7 records (last built 2026-11-07), and **vol7 has never been through a site build** (`site/out` is dated 2026-11-07; there is no `out/lucam`, no `out/tome/7`) | — | info |

**If every ⭐ is taken: 2 English lines (`c3-v23-38` ¶ 63, `c1-v18-25` ¶ 38) + 1 manifest cell + three ruling sentences (18, 12, the
`tr-pietas` scope) + one tool job. No line in any `## Latin` or Latin apparatus half changes.**

---

## 1. THE CONSPICUOUS RULING-20 DOUAY DEPARTURES

Ruling 20 (carrying Vol VI ruling 93): *where the exposition leans on Bonaventure's word, the Douay is adjusted to it,
silently in the English and disclosed in `## Notes`; where nothing leans, the Douay stands.* Every chunk in the interval
discloses its adjustments (G33 lemma verses, G34 adduced verses). The five below are the ones a reader will notice, because
the verse is famous or liturgical.

| # | site | Vulgate / Quaracchi | Douay (Challoner) | built | what leans | Douay alternative costs |
|---|---|---|---|---|---|---|
| 1a | `c2-v25-35` ¶ 71, Luke 2:32 (*Nunc dimittis*) | *Lumen ad revelationem gentium* | "A **light** to the revelation of the Gentiles" | "A **lumen**[^tr-lumen] to the revelation of the Gentiles" | ¶ 71's own prose at once: *Et hoc lumen gentibus revelabit gloriam Dei* "And this lumen will reveal…" | **2 lines** (¶ 71 EN, which carries both sites; the `tr-lumen` def). It also breaks the ruled *lumen* exemption test (below) |
| 1b | `c2-v25-35`, Luke 2:25 lemma | *iustus et timoratus* | "just and **devout**" | "just and **God-fearing**" | ¶ 60 expounds it from *timor* (*Timor enim expellit peccatum*; Prov. 15:27 *In timore Domini*; Job 1:1 *timens Deum*) | **1–2 lines**; "devout" also stands on *devotus* / *devote* elsewhere (`c2-v36-39` ¶ 86 *devote* "devoutly") |
| 1c | `c3-v15-20` ¶ 44, Isa. 52:7 | *pedes annuntiantis et praedicantis pacem, annuntiantis bona* (Quaracchi's plural; Vulgate *bonum*) | "him that **bringeth good tidings**, and that preacheth peace: of him that **sheweth forth good**" | "him that **announceth** and preacheth peace, that **announceth good things**" | ¶ 44 glosses *Evangelizabat, id est, bona annuntiabat* "he announced good things" and adduces the verse for that gloss | **1 line**, and it would put the Douay's "good tidings" on *annuntiare*, the exact collision with ruling 18's *evangelizare* "good tidings" that the house *annuntiare* "announce" exists to prevent |
| 1d | `c3-v21-22` ¶¶ 55–56 + p. 84 nn. 8, 11, 14 | Matt. 3:17 *in quo mihi complacui*; Mark 1:11 *in te complacui*; Luke 3:22 *in te complacuit mihi*; Col. 1:19 *In ipso complacuit* | all three Gospels "**I am well pleased**"; Col. 1:19 "it hath well pleased the Father" | "in whom I am well pleased **to myself**" / "in thee I am well pleased" / "in thee **it hath well pleased me**"; Col. 1:19 "In him it hath well pleased" ("the Father" not supplied; Quaracchi prints none) | ¶ 56 IS the difference: *Matthaeus insinuat complacentiam Patris … se in se … Marcus … complacet aliis … Lucas … omnia*; Augustine (p. 84 nn. 11, 14) argues the same | **~4 lines**, and the paragraph would then explain a difference the English does not show |
| 1e | `c1-v46-56` ¶ 91, Prov. 31:28 | *Surrexerunt filii eius et beatissimam praedicaverunt* | "rose up, and **called her blessed**" | "rose up, and **preached her most blessed**" | ¶ 91 is built on the gradient *beata … beatior … beatissima* and closes with *beatissimam eam praedicant* + Cant. 6:8 *beatissimam praedicaverunt*, which ruling 21 already set as "preached her most blessed" | **1 line**; it loses the superlative the gradient needs, and the body's *praedicant* then answers a verse that no longer says it |

**The decisive sentences.**
- 1a, ¶ 71: *propter quod addit: Lumen ad revelationem gentium; … Et hoc lumen gentibus revelabit gloriam Dei* / "on account of
  which he adds: *A lumen to the revelation of the Gentiles;* … And this lumen will reveal to the Gentiles the glory of God."
- The *lumen* exemption test (Vol V *mysterio Trinitatis* shakedown gate, Wilson 2026-09-06, carried by ruling 11): *a received
  scriptural wording is exempt only where the verse is quoted AS A VERSE and no surrounding body prose leans on the term.* Its
  precedent is Ps. 4:7, which **kept "lumen" although its Douay wording is as recognisable as Ps. 35:10's**, because the body leaned.
  Luke 2:32 is that case again. The Vol V ruling also records the cost as accepted: "a transliteration, and at this frequency
  conspicuous".
- 1d, ¶ 56: *ita quod Matthaeus insinuat complacentiam Patris respectu Verbi, in quantum dicit se in se; et ideo dicit: « In quo
  mihi complacui »* / "so that Matthew intimates the complacency of the Father with respect to the Word, inasmuch as he speaks
  *himself in himself;* and therefore he says: « In whom I am well pleased *to myself* »."

**The *lumen* census over all 22 chunks (for 1a).** *lumen* in Bonaventure's prose → "lumen" + `tr-lumen`: `c2-v8-14` ¶¶ 17, 20, 21
(×3, with Acts 12:7 inside the lean; the work's first), `c2-v21-24` ¶ 55, `c2-v25-35` ¶ 71 (×2 with the verse). *lumen* inside a
quotation where nothing leans → the Douay's "light": `c2-v1-7` ¶ 11 and p. 46 n. 9 (Ps. 103:2 inside Bernard, *amictus lumine*),
`c2-v40-52` ¶ 105 (Tob. 10:4 *lumen oculorum*, G12). *luminare / luminaria / Pater luminum* are other words ("lights"). No
departure from the rule.

**Douay alternatives, if Wilson wants the famous verse kept.** Take 1a alone: Luke 2:32 "A light", ¶ 71 "this light", delete the
`tr-lumen` def = **2 lines**, plus a written exception to the test ("canticle verses keep the Douay even where the prose leans").
That exception has no stopping point in Luke: the *Magnificat*, *Benedictus* and *Nunc dimittis* are expounded verse by verse.

**⭐ Recommendation: RATIFY 1a–1e as built. 0 lines.**

---

## 2. CONSISTENCY PAIRS: ONE VERSE OR PROPOSITION, TWO RENDERINGS

| pair | site A (as built) | site B (as built) | Douay | what leans at each | costs to unify |
|---|---|---|---|---|---|
| **2a. Mary keeps the words** | `c2-v15-20` ¶ 40, Luke 2:19 *conferens in corde suo* → "**pondering** them in her heart" (×2) | `c2-v40-52` ¶ 109, Luke 2:51 *Conferens in corde suo* → "**Conferring** in her heart" (+ p. 69 n. 1 En) | 2:19 "pondering"; **2:51 has no word**: the Vulgate omits *Conferens* (p. 69 n. 1: *quod tamen exhibet Beda*) | ¶ 40: nothing leans on *conferre*. ¶ 109 runs a *conferre* chain: *Nondum enim venerant Apostoli … qui etiam invicem conferrent, secundum illud ad Galatas secundo: « Contuli cum illis Evangelium »* → "who would also **confer** with one another … « I **conferred** with them the gospel »" | 2:51 → "pondering": **2 lines** (¶ 109 EN, p. 69 n. 1 En), and the Gal. 2:2 chain loses its hook. 2:19 → "conferring": **1 line**, but it adjusts the Douay where nothing leans (against ruling 20) |
| **2b. *puer*** | `c1-v46-56` ¶ 99, v. 54 *Suscepit Israel puerum suum* → "his **child**" | `c1-v67-80` ¶ 124, v. 69 *in domo David, pueri sui* → "his **servant**" (×2) | both "his servant" | ¶ 99 adduces Osee 11:1 *Puer Israel* "Israel was a **child**" for v. 54, AND Isa. 42:1 *Ecce, servus meus* "my **servant**" in the same chain. "Child" keeps *puer* off *servus* inside ¶ 99. At ¶ 124 nothing leans; ¶ 136's *Et tu, puer* (John) is the Douay's own "child" | v. 54 → "servant": **1 line**, and ¶ 99 then reads "servant" for both *puer* and *servus*. v. 69 → "child": **2 lines** (builder's count), against ruling 20 |
| **2c. Col. 1:13** | `c3-v21-22` ¶ 55, *Transtulit in regnum Filii dilectionis suae* → "the Son of his **dilection**" | `c3-v23-38` ¶ 63, *transtulit nos in regnum filii dilectionis* → "the Son of **his love**" | "the Son of his love" | ¶ 55's chain runs on *diligere* (*Hic est Filius meus dilectus … dilecto Filio suo … Filii dilectionis suae*); the carried *dilectio* → "dilection". At ¶ 63 nothing leans | ¶ 63 → "dilection": **1 line**, against ruling 20 |

**Decisive sentence (2a).** p. 69 n. 1 tells the reader the two sites are one proposition: *cfr. supra v. 19, ubi eadem
recurrit propositio* / "cf. above, v. 19, where the same proposition recurs". And ¶ 109's *Et quia haec intelligebat, ideo
dicitur: Conferens* repeats ¶ 40's *Et quia non solum conservabat, sed etiam intelligebat; ideo additur: Conferens* almost word
for word. A reader who follows the note finds "pondering" there. That is the cost of keeping the split. It is a real cost, but
ruling 20 accepts it by design: one Latin word, rendered by what leans at each site.

**⚠ A fidelity point at 2c that is not a ruling-20 question (my finding).** Quaracchi prints ¶ 63's verse **without *suae***
(*in regnum filii dilectionis*), but the English carries the Douay's "**his** love". Elsewhere in this same chunk the Douay base is
adjusted to Quaracchi's actual wording where it differs (Gen. 5:24 "appeared not", "Quaracchi's wording"; Eph. 4:15 "let us grow
up", "Quaracchi's subjunctive"). For consistency inside the chunk: "into the kingdom of the Son of love". **1 line.**

**⭐ Recommendation: KEEP all three splits (ruling 20 working as written); APPLY the ¶ 63 "his" fix. 1 line.**

---

## 3. RULING-18 SCOPE: *evangelizare* IN THE OLD TESTAMENT, AND THE *annuntiare* VERSES

**Census: 14 Latin sites across all 22 chunks; 8 of them are new ground.**

| rendering | sites |
|---|---|
| "preach the gospel" (6) | `prooem` ¶ 19 (Luke 4:43); `prol` p. 10 n. 2 (Sedulius); `c3-v15-20` ¶ 44 ×3 (Luke 3:18 lemma and its resumption; the gloss) and p. 79 n. 4 (Bede *officium evangelizandi*) |
| "bring good tidings" (8) | `c1-v18-25` ¶ 31 ×3 + p. 18 n. 4 (Luke 1:19 and its exposition; Bede); **`c1-v39-45` ¶ 77 ×2 (Isa. 40:9, `tr-evangelizare`)**; `c2-v8-14` ¶ 23 (Luke 2:10, `tr-evangelizare`) and **p. 50 n. 12 (Bede's *evangelizante*, echoing 2:10)** |

`tr-evangelizare` stands in three chunks (`c1-v18-25`, `c1-v39-45`, `c2-v8-14`), at each one's first site. Bare "preach" for
*evangelizare*: **zero**.

**The question.** Ruling 18's clause reads: *where the Douay itself says "bring good tidings" (1:19, 2:10: an angel bringing a
message, with an object), the Douay stands.* The parenthesis names two Luke verses and an angel. Isa. 40:9 is a prophet's verse
addressed to Sion, and the Douay says "thou that bringest good tidings".

**What the Douay does across the whole Vulgate** (all 43 *evangeliz-* verses, Clementine against Challoner): "gospel" 23 ·
**bare "preach" 12** · **"good / glad tidings" 6** · "evangelizing" 1 · other 1 (Apoc. 10:7). **The Old Testament has exactly three
*evangeliz-* verses, and the Douay renders all three "good tidings":** Ps. 67:12 *evangelizantibus* "to them that preach good
tidings"; Isa. 40:9 *qui evangelizas Sion* "thou that bringest good tidings to Sion"; Nah. 1:15 *pedes evangelizantis* "the feet of
him that bringeth good tidings". So the parenthesis is a description, not the test. Read as "where the Douay itself says 'good
tidings'", the clause already covers every OT site, and nowhere does it let bare "preach" back in.

**The *annuntiare* side (G7–G8), all consistent with ruling 12's *annuntiare* "announce" (`tr-annuntiare`):**
- Isa. 52:7 *annuntiantis* → "him that announceth" (item 1c): the Douay's "good tidings" adjusted away, because the Latin is not
  *evangelizare*.
- Isa. 61:1 *ad annuntiandum mansuetis* (`c3-v1-9` ¶ 7) → "he hath sent me **to announce** to the meek" (Douay "to preach"): this
  keeps "preach" on *praedicare* alone. ⚠ **Forward:** Luke 4:18 quotes the same verse as *evangelizare pauperibus* (Douay "to
  preach the gospel to the poor"), so Cap. IV will show the two Latin words side by side. As ruled, they come out "announce" and
  "preach the gospel", which is correct.
- `c2-v8-14` house *denuntiare* "declare" / *annuntiare* "announce" [35]: the p. 27 ratification, unchanged.

**Alternatives.** (a) Ratify Isa. 40:9 as built and amend the clause to the test (0 lines). (b) Read the clause narrowly (angels
only): Isa. 40:9 → "thou that preachest the gospel to Sion", ×2, plus rewrite that chunk's `tr-evangelizare` (**2 lines**). The
Douay never says that at this verse, and it reads as an anachronism in Isaias.

**⭐ Recommendation: (a). Ruling 18's clause becomes: "where the Douay itself says 'bring / preach good tidings' (Luke 1:19,
2:10; Ps. 67:12, Isa. 40:9, Nah. 1:15), the Douay stands, with `tr-evangelizare` at each chunk's first site; an echo of such a
verse (Bede p. 50 n. 12) follows it." 0 lines + the ruling sentence.**

---

## 4. *praeconium* → "proclamation", BESIDE RULING 12'S BAN ON "proclaim"

**Census, all 22 chunks: *praeconium* 15 Latin sites (body 15 + app 0) → "proclamation" 15/15.** `c1-v39-45` ¶¶ 80, 81
(*praeconium admirativum* "the admiring proclamation"); `c1-v57-66` ¶ 117 (*magnificentia praeconii*); `c1-v67-80` ¶¶ 120, 136
×2, 138 (*prophetali praeconio*, *Ioannis praeconium*); `c2-v21-24` ¶ 47 (*praeconium angelicum*); `c2-v25-35` ¶¶ 58 ×2, 66 ×3,
75 ×2 (*testificationis praeconium*, *veritatis praeconium*, *praeconii temperamentum*). The English verb **"proclaim" occurs
zero times** in the 22 chunks. *praeco* (3 sites: `c1-v5-17` ¶ 8 + p. 13 n. 10, `prol` p. 9 n. 4, `c3-v1-9` p. 72 n. 6) →
**"herald"** every time.

**Decisive sentences.** Ruling 12: *praedicare* preach / *praedicatio* preaching / *praedicator* preacher, **never "proclaim"**.
`c2-v25-35` ¶ 66: *subditur hic veritatis praeconium elevans ad admirandum … prae magnitudine praeconii. Huius autem praeconii
excellentia* / "is subjoined here the *proclamation of truth,* raising up to wondering … for the greatness of the proclamation.
Now the excellence of this proclamation…".

**Analysis.** The ban protects *praedicare*. It does not reserve the English word. With the *praedicare* family (103 Latin sites in the 22 chunks; 108 English "preach-" hits, the surplus being
Douay quotations and the *evangelizare* "preach the gospel" sites) held to "preach", "proclamation" is free, and it is the ordinary English for a *praeconium* (the *Exsultet* is the *praeconium
paschale*, the "Easter Proclamation"). Where the noun means *praise* (*magnificentia praeconii*, ¶ 117), "proclamation" still
reads correctly.

| alternative | cost |
|---|---|
| **(a) Ratify "proclamation"; state the reservation in ruling 12** | **0 lines** |
| (b) "heralding", to match *praeco* "herald" | **10 lines** (`c1-v39-45` 2, `c1-v57-66` 1, `c1-v67-80` 3, `c2-v21-24` 1, `c2-v25-35` 3); clumsy at *praeconii temperamentum* "the tempering of the heralding" |
| (c) "praise" | 10 lines; wrong at *testificationis praeconium*, which is testimony, not praise |

**⭐ Recommendation: (a). Ruling 12 gains: "*praeconium* → 'proclamation' (the only home of 'proclaim / proclamation' in
this translation); *praeco* → 'herald'." 0 lines.**

---

## 5. `tr-pietas` OUTSIDE cc. 15–16

**Census, all 22 chunks: *pietas* / *pius* 21 Latin sites (body 18 + app 3) → "piety" / "pious" at every one.** The family
never goes to "godliness" or "compassion" (*compassio* is the only source of "compassion": `c2-v25-35` ¶¶ 75, 78 and p. 61 n. 9).

| site | whose *pietas* | `tr-pietas`? |
|---|---|---|
| `c1-v46-56` ¶¶ 92–93 *magnum et pium … magnitudine et pietate*; I Tim. 3:16 *pietatis sacramentum* "the sacrament of piety" (Douay "mystery of godliness", adjusted under the *septem donis* ruling, carried) | **God's** (the incarnation as *opus pium*) | **yes, ¶ 93** |
| `c2-v25-35` ¶ 69 *excellentiam pietatis … Ex pietate et clementia venit salus* | **God's / Christ's** | **yes, ¶ 69** |
| `prooem` ¶ 6; `c2-v21-24` ¶¶ 49, 54; `c2-v40-52` ¶¶ 91 ×2, 99, 105, 107 ×2, 111 ×2 and p. 66 nn. 10, 11; `c3-v1-9` ¶ 14; `c3-v15-20` p. 80 n. 7 (variant) | human | no (correct) |

**Decisive sentence.** Ruling 12: *⭐ pietas divina in cc. 15–16: the "piety" rule HOLDS, with `tr-pietas` at the first site of
each chunk where the pietas is God's; reviewed with sites in view at the p. 381 gate.* The rule is written about cc. 15–16 because
that is where the scouting expected God's *pietas*. It turned up 13 chapters early. `c1-v46-56` applied the note there, and
`c2-v25-35` followed it. Both definitions say the same thing: the Latin covers "the tenderness of a father toward his own as well
as the devotion of a creature toward God; Bonaventure is using the first sense."

⭐ **A reason to keep it, in the same span:** `c2-v40-52` ¶ 107 sets *pietas ad Deum* (a human's piety toward God) against *pietati
respectu parentum*, and ¶ 99 carries Jerome's *Summum enim pietatis genus est, in his crudelem esse* (the *decem praeceptis* c5 pun,
which the one-root rule exists to keep). With "piety" fixed on every site, the note is the only thing that tells the reader
which sense God's *pietas* takes.

| alternative | cost |
|---|---|
| **(a) Ratify: `tr-pietas` at the first God's-*pietas* site of ANY chunk, work-wide** | **0 lines** |
| (b) Hold the note to cc. 15–16; strip the two early ones | **4 lines** (2 EN body marker lines, 2 defs) |

**⭐ Recommendation: (a). Ruling 12's sentence is read work-wide; the p. 381 gate still reviews the rule itself. 0 lines.**

---

## 6. NEW HOUSE RENDERINGS: RATIFY AS A BATCH

Each row: Latin sites (body+app, all 22 chunks) → the English as built. Where the rendering is already a carried ruling, the
row says so. Where it is new, the reason given is the builder's, checked against the text.

| term | La sites | built | status / reason | verdict |
|---|---|---|---|---|
| *poenitentia*, *poenitere* | 23 (`c3-v1-9` 12+2) | "penance" 23/23, "do penance" | the Douay's own word at Luke 3:3, 3:8 ("baptism of penance", "fruits worthy of penance") | ratify |
| *vacare* (dative) + `tr-vacare` | 10 (`c1-v67-80` ¶ 144; `c2-v36-39` ¶ 86 ×3 + p. 63 nn. 5–7; `c2-v40-52` ¶ 94 ×3) | "free for" ×10; `tr-vacare` in 3 chunks | **already ruled** (Wilson 2026-09-15, the *dikaisune* rule: context-chosen English, footnoted, "no `vaca-` word is ever rendered 'rest'"). I Cor. 7:5 *ut vacetis orationi* (`c1-v18-25` ¶ 36, inside a quotation) keeps the Douay's "give yourselves to prayer"; `c1-v26-38` ¶ 41 *vacat a mysterio* is the other sense ("free from") | ratify |
| *quies* (noun), *requies* | *quies* body 5 (`c2-v21-24` ¶ 48; `c2-v40-52` ¶ 101; `c3-v23-38` ¶ 63 ×3) + variant `c2-v1-7` p. 45 n. 2; *requies* 3 (Heb. 4:11 ×2, Ps. 131:14) | "rest" at every site | **already ruled** on the *quies* side (*mysterio Trinitatis* q5-a2). Verbs: *requiescere* "rest", *conquiescam* "repose myself" (Wis. 8:16), Isa. 1:16 *Quiescite* "Cease" (Douay; G17); adjective *quietus* "quiet" | ratify |
| *lumen* (the angelic *lumen*) | see § 1 | "lumen" + `tr-lumen` in 3 chunks | the carried Vol V *lux* / *lumen* rule | ratify |
| *claritas* | 7 | Luke 2:9 *claritas Dei* + ¶ 21's gloss → the Douay's "**brightness**"; inside quotations the Douay's "glory" (Wis. 4:1, 8:10, II Cor. 3:18 *a claritate in claritatem*) | Douay at every site | ratify |
| *clarificatio* | 11 (`c2-v21-24` 2, `c2-v25-35` 1, `c2-v36-39` 1, `c2-v40-52` 4, `c3-v21-22` 2+1) | "glorification" 11/11 | the paired *humiliatio / clarificatio* structure of cc. 2–3. ⚠ **Shares its root with *glorificare* "glorify"** (9 Latin sites); no sentence in the 22 chunks sets the two together | ratify, record the shared root |
| *timoratus* | 1 (Luke 2:25) | "God-fearing" | § 1b | ratify |
| *corripere* / *correptio* · *arguere* | 11 · 6 | "correct" / "correction" · "reprove" | new pair, `c3-v15-20` ¶ 45 sets *corripiens principem praevaricantem* against *publice arguebat*; Luke 3:19 *cum corriperetur* "when he was corrected" (Douay "reproved") and Amos 5:10, I Tim. 5:20, Tit. 2:15 adjusted to match (G27). II Tim. 3:16 (`c1-v1-4` ¶ 5) *ad arguendum, ad corripiendum* is the Douay's "to reprove, to correct", the same split | ratify |
| *erudire* (verb), *eruditor* | verb 6 in body; *eruditor* 1 | "are schooled" (`c1-v67-80` ¶ 144, `c2-v15-20` ¶ 41, `c3-v10-14` ¶ 29), "schoolmaster" (`c2-v8-14` ¶ 20); inside quotations the Douay ("instructed" Jer. 13:21, II Tim. 3:16; Lam. 1:13 "chastised", G21) | keeps *erudire* off *instruere* "instruct" (*instruimur* "we are instructed", ×4) and off *docere* "teach". *eruditio* → "erudition" (ruling 17) | ratify, **with 1 fix:** `c1-v18-25` ¶ 38 *Sed spiritualiter erudimur* is "we are **taught**", the one body-prose *erudire* outside the family (from the p. 27 interval; ruling 17 did not reach the verb). → "we are **schooled**". **1 line** |
| *largitas* / *liberalitas* | 6 (`c1-v46-56` 4+2) | "largess" / "liberality" | two words, two English roots (ruling 12 fixed *liberalitas*) | ratify |
| *documentum* · *instructio* | sg. 6 + pl. 3 · *instructiones* 1 | sg. "instruction" · pl. "lessons" (ruling 17) · "instructions" (`c3-v10-14` ¶ 22) | G22: ¶ 22 announces *diversas instructiones* and ¶¶ 23, 28, 31 deliver each as a *documentum*. One English root for two Latin words used as near-synonyms inside one division. Unifying both as "lesson(s)" would reverse ruling 17's by-number ratification (6 lines) | ratify |
| *benedictus* / *beatus* | ~58 / ~66 | "blessed" / "blessed" | G23. **Not one sentence in the 22 chunks sets the two families together** (the only line holding both is `c2-v40-52`'s *de beato Benedicto*, a saint's name). *beatitudo* "beatitude" | ratify |
| *admirabilis* / *mirabilis* | 62 Latin sites | "wonderful" / "marvellous" / "wonder" | G24, carried into quotations (`c2-v15-20` ¶ 39 the name *Admirabilis*, Isa. 9:6) | ratify |
| *cohortatio* / *exhortatio*; *comminatio* / *increpatio* / *admonitio* | 16 (*cohort-* / *exhort-*) | "exhortation" pair split by prefix (`c2-v15-20`); "threatening / rebuke / admonition / exhortation" (`c3-v1-9`) | G25 | ratify |
| *praeceptum* / *consilium* / *mandatum* | — | "precept" / "counsel" / "commandment" | G26: the *decem praeceptis* ruling, carried; Eccle. 8:5 keeps the Douay | ratify |
| *purgatio* / *purificatio* | 18 | "purgation" / "purification" | G28 | ratify |
| *ortus* / *partus* / *nativitas* | — | "birth" / "bringing forth" (and "offspring" at `c2-v21-24` ¶ 52) / "nativity" | G29 | ratify |
| *cultus* | 15 | "worship" | G31 | ratify |
| singles (G32) | — | *exsultare* "exult" (38 La sites, incl. six Douay quotations in ¶ 88 adjusted from "rejoice"); Eccli. 18:12 *miseratio* Douay "compassion" (ruling 12's quotation clause); *divulgare* "spread abroad"; *profiteri* "profess"; *egenus* "needy"; *dominatrix* "mistress"; *comprehendere* "lay hold of"; *eventus* "proceeds"; *baptismus fluminis, flaminis, sanguinis* (Vol IV house); *virtus Spiritus septiformis* | as recorded in each chunk's Notes | ratify |
| *femina est vir occasionatus* (`c3-v23-38` ¶ 58) | 1 | "woman is a **misbegotten** man" | ⚠ the one rendering here a modern reader will stop at. It is the standard English for the Aristotelian formula (*De gen. anim.* II 3, via Thomas, *mas occasionatus*). The literal "an occasioned man" says nothing in English. Record that Bonaventure reports the formula; the translation does not soften it | ratify |
| *status* / *situs* (¶ 61, the seven differences) | 2 | "stopping-place" / "position" | *status* follows the *scientia Christi* register (*sed contra* 5) | ratify |
| *intellectus* / *intelligentia* (G18–G20) | — | "understanding" / "intelligence"; `c2-v40-52` ¶ 110 *in intellectu … in affectu* "in the intellect … in the affection" | ruling 17; ¶ 110 is Vol VI ruling 101's faculty clause | ratify |

**⭐ Recommendation: RATIFY the batch; APPLY the one `c1-v18-25` ¶ 38 fix ("we are schooled"). 1 line.**

---

## 7. `title_la`: THE SENTENCE-TITLE PRECEDENT AND THE OTHER RULING-22 APPLICATIONS

Ruling 22: *`title_la` = the LOWEST heading of the opening stack, whole … a sentence title (lemma + dividing words) only where no
heading stands.* All 22 chunks were compared with the manifest's `title_la` cell:

| class | chunks | built | manifest cell |
|---|---|---|---|
| **G3 sentence titles** (no heading anywhere in the span; the editors set the member's title in the MARGIN) | `c2-v25-35` | *Et ecce, homo erat in Ierusalem etc. Postquam descripta est Christi humiliatio secundum Legis praeceptum, hic secundo describitur eius clarificatio per veritatis testimonium* / "And behold there was a man in Jerusalem etc. After the humiliation of Christ according to the precept of the Law has been described, here secondly is described his glorification by the testimony of truth" | agrees (`divisio ¶58`) |
| | `c2-v36-39` | *Et erat Anna prophetissa etc. Post testimonium sexus virilis sequitur hic testimonium sexus muliebris* | agrees (`divisio ¶81`) |
| **G1 stacks read as ONE, lowest heading taken** | `c2-v1-7` (t4), `c3-v1-9` (69R t3 under `CAPITULUM III.` + t2 + ¶ 1), `c3-v10-14` (75L t4), `c3-v21-22` (81R t4) | as described | agree |
| **G2 departs from the manifest** | `c2-v21-24` | *Qualiter factus sit sub lege sacramentali* (the 54R **t4**) | **⚠ names the 54L t3** *Secundo, de Christi nascentis humilitate, quatenus factus est sub triplici lege.* (its `headings` cell lists `t3@54L;t4@54R;t4@56L`) |
| **G4 single-heading openings** | `c2-v40-52` 65L t4, `c3-v15-20` 78L t4, `c3-v23-38` 85L t4 (and every other capitulum chunk) | the heading | agree |

**Analysis.** The sentence titles are long, but that is the ruling's own shape ("lemma + dividing words"). They are also the
only text on those spans that names the member: the marginale is trimmed to the Notes. The site's chunk title is the
breadcrumb `Cap. 2, Vers. 25-35`, so the long `title_la` appears only as the subtitle. For G2, ruling 22 settles it: the t3 and
the t4 are one opening stack, and the t4 is the lower. The builder took the right one and left the manifest alone, as the loop
requires.

**⭐ Recommendation: RATIFY every `title_la` as built (the sentence-title shape stands as the precedent for every later
heading-less span); at the gate close, CORRECT the `c2-v21-24` manifest `title_la` / `title_la_source` cells to the 54R t4.
0 chunk lines + 1 manifest line (doc).**

---

## 8. THE MANIFEST-CELL EDITS (G50)

`git show` on the two build commits, restricted to `manual-review/lucam-chunk-manifest.tsv`:

| commit | row | cells changed |
|---|---|---|
| `e0b7c3e` (`bon-luc-c2-v25-35` built) | `bon-luc-c2-v25-35` | **`confidence` only: `low` → `high`.** Every other cell, the long `note` included, is byte-identical |
| `baa568d` (`bon-luc-c2-v36-39` built) | `bon-luc-c2-v36-39` | **`confidence` only: `low` → `high`** |

No other commit in the interval touches the manifest. **Decisive sentence (ruling 26):** *The rows stay `low` until their builder
reads pp. 58–65, then are promoted to `high`.* Both builders read pp. 58–65, and both chunks' Notes record the ¶ 81 cut confirmed on
the plate.

**⭐ Recommendation: RATIFY both edits as ruling 26 carried out. 0 lines.** (The resume's "Wilson may still overrule" stands
answered by this item.) One standing rule worth stating, because stage 2 is being drawn now: **a builder may change only its own
row's `confidence` cell, and only when a ruling names that edit; every other manifest change goes through a gate** (item 7's
`c2-v21-24` cell is the example).

---

## 9. THE GENEALOGY NAMES POLICY (G40)

**As built (`c3-v23-38` Notes):** the **English takes the Douay's spellings** for Luke 3:23–38 and for the Matthaean names ¶¶ 59–61
bring in (*Heli*, *Mathat*, *Janne*, *Amos*, *Henoch*, *Nathan*, *Mathan*, *Jacob*, *Solomon*, *Jechonias*; *Gerson* from Num. 4:22;
in the apparatus *Thamar*, *Rahab*, *Jahel*, *Abigail*). **The Latin keeps every form as printed** (*Iesus*, *Ioseph*, *Ianne*,
*Henoch*, *Iechonias*, *Salomon*). **Names *mentioned* as words stay Latin and italic in the English:** Jerome's etymological forms
*Iamna*, *Iamin*, *Iannai*, *Enoch*, the Hugo/Albert variant *Iamne*, *Ioakim* / *Ioachin* (p. 86 n. 9; p. 88 nn. 1–6), because those
notes are about the spelling.

**Check (mine).** I compared every capitalised word of the English body with the name lists of the Douay and the Clementine at
Luke 3:23–38. **No Vulgate-only form appears in the English** (no *Iamne*, *Mathusala*, *Ioanna* type intrusions outside the
italic mentioned-word sites). Many genealogy names are absent because Bonaventure expounds only seven degrees (¶ 63's *Iesus,
Ianne, Amos, Ioseph, Henoch, Adam, Deus*), not the list.

**Why this is a work-level convention, not a chunk choice.** The same three-way rule already governs the work: Luke takes the
*Ioannem*'s spellings (ruling 11, Vol VI ruling 155), i.e. *Zachary*, *Elizabeth*, *Elias*, *Solomon* (40 sites in vol7). Cap. IV
(the temptation) and Cap. VI (the Twelve) will bring the next name lists.

**⭐ Recommendation: RATIFY as the work's names policy: biblical proper names in the English take the Douay's spelling at the verse;
the Latin keeps Quaracchi's form; a name cited as a word (etymology, variant, *nomen*) stays Latin italic in both. 0 lines.**

---

## 10. RECORDS, MISPRINTS AND BANKED EVIDENCE (G38–G39, G41–G49)

No text edit is asked for in any of these. Listed so one word can close them.

- **G38 canticles as names** (*Magnificat*, *Benedictus*, *Nunc dimittis* at `c2-v25-35` ¶¶ 66, 68): ruling 12, applied.
- **G39 Trinitarian register:** "Holy Spirit" everywhere, I John 5:7 and every Douay quotation included (ruling 17); *nexus amoris*
  "the bond of love"; *discretive* "discretively". Applied.
- **G41 Quaracchi slips transcribed as printed** (p. 29 n. 7 *nota 10*; p. 38 n. 7 *pag. 1*; p. 44 n. 7 *tom. VI. pag. 91, nota 3*;
  p. 56 n. 2 *Vers. 35*; p. 54 n. 10 *d. 8. p. II. dub. 2.*; p. 65 n. 12 *Ver. 14.*; p. 66 n. 10; ¶ 98 *eum*; p. 71 n. 3 Book II for I;
  p. 83 n. 2 *Psalm. 15, 10.*; p. 85 n. 4 *Sap. 4, 8.*; Lev. 12:8 *pro eo*). **G42 bracketed misprints** (*Memomoriam*, *Christi*;
  `[so printed]` p. 63 n. 8 Greek, p. 79 n. 5 *voluisset*). **G43 type faults recorded, not bracketed.** **G44 Quaracchi's lemma
  readings translated as printed** (*Venit*, *purgabit*, *Descendit*, *Vox*, *complacuit*). All follow rulings 8 / 9 / 89 as carried.
- **G45–G46 collection change:** three *expositio* italic exceptions in the interval, all inside Bernard (`c2-v1-7` ¶ 11, `c2-v8-14`
  ¶ 26, `c2-v40-52` ¶ 108), every other chunk a positive zero; three sub-sites. **Banked; no discriminator is proposed and none is
  asked for.**
- **G47** correction of record (`CAPITULUM III.` at ~0.47 of p. 69). **G48** p. 85 holds only p. 84 n. 14's runover from `c3-v21-22`.
  **G49** the first resolved inbound (`bon-ioan-c1-v24-28` p. 258 n. 10 → `c3-v15-20`, verified in `index/citations.tsv`: `crossref /
  lucam / chunk`); the lost inbound is item 11.

**⭐ Recommendation: RATIFY as recorded. 0 lines.**

---

## 11. TOOL FIX JOB (T1–T13 + the inbound-form question)

**One docket item, one job.** None of these changes a word of text; all of them change what the index and the site's "cited
by" panels show. QA stands at **213** (`citation-qa-report.md`: 2,340 chunks, 37,675 records); two of the 213 are this
interval's (T1, T8).

**⭐ Recommendation: ONE bounded Sonnet job after the gate,** on the report → fix → report loop (measure, fix, re-measure; a
before/after table per site), touching `tools/build-citations.py` only (plus a site table if used), then
`build-citations.py` → `build-index-json.py`. No chunk file, no `tools/authorities.json`. Scope:

| # | site(s) | fix | expected effect |
|---|---|---|---|
| T1 | `c1-v46-56` ¶ 97/98 "Esth. 98" | extend the ~L362 guard past the point-verse case | QA −1 |
| T3, T8 | p. 38 n. 7 *supra pag. 1, nota 5* (`forward` forever); p. 54 n. 10 *d. 8. p. II. dub. 2.* (`dangling`) | file as Quaracchi printed slips under the r.57 "printed slips" class (records kept, flagged, not retargeted) | QA −1; one permanent `forward` closed |
| T4 | p. 44 n. 7 *tom. VI. pag. 91, nota 3* → `bon-eccl-c11-v1-10`, which does not match (same note: an unresolved *ibid. v. 45*) | mark unresolvable-with-reason rather than a wrong `chunk` | 1 wrong edge removed |
| T6 | 11 page+note self-citations on a SHARED page filed `page-multi` (p. 50 nn. 2, 3; p. 52 n. 10; p. 58 n. 1; p. 64 n. 5; p. 69 n. 4; p. 71 n. 6; p. 79 n. 3; p. 82 n. 12; p. 83 n. 3; p. 84 n. 6) | apply ruling 24's "break a shared page by its note" fix to every `pag. N, nota M` (it was written for the lucam inbound branch only) | ~11 `page-multi` → `chunk`; includes Vol III and Vol VI targets |
| T7 | Bonaventure's own *Comment. in Eccle./Ioan.* inbound to Vol VI with no record (p. 50 n. 2; p. 64 n. 10; p. 68 n. 6; p. 72 n. 4; p. 82 n. 5); *S. Bonav., IV. Sent. …* dropped under the author guard (p. 82 n. 5, p. 83 n. 9) | let `S. Bonav.` through the guard for the work's own author, as the lucam branch already does | +5–7 records |
| T9 | p. 55 n. 8 *Breviloq. … (pag. 203, in nota 8.)* filed `tom7:p203` `forward` | a parenthetical page after a named Vol V work resolves in Vol V | → `bon-brev-prol-s2` |
| T10 | cross-note *ibid.* / *loc. cit.* bound ACROSS notes (p. 64 n. 6; p. 69 nn. 4, 9; p. 73 n. 9; p. 74 n. 1; p. 77 n. 10; p. 79 n. 3) | stop the anaphor pass at a note boundary | 7 false resolutions → unresolvable |
| T11 | *Ecclesiastae N* body ordinals (`c2-v40-52` ¶¶ 107, 109; `c3-v1-9` ¶ 11; `c3-v10-14` ¶ 29); ¶ 93 *Deuteronomii, duodecimo*; p. 65 n. 12 *Ver. 14.* | add the book and the comma form to the body-ordinal scanner | +5–6 records (corpus-wide, not only vol7) |
| T13 | ROMAN-numeral distinctio (p. 69 n. 4 *III. Sent. d. XIII*; p. 85 n. 9 *II. Sent. lit. Magistri, d. XXIV. c. 7. seqq.*) | accept roman `d.` | +2 records |
| T12 + IV-d21 | the two OWN-commentary *Exposit.* inbounds (below) | an explicit two-row site table, not a wider `LUC_RE` | +2 records (1 `chunk`, 1 `forward`) |

**Not in the job:** **T5** (in-work *c. N. n. M* / *supra n. N* / *infra* + ordinal; ~25 sites in this interval) waits with the
*Ioannem*'s identical class, ruling 24 / ruling 82(a); the job should only **count** it. **T2** (Bede's "Comment. in Luc." false
positive, p. 36 n. 6) **never recurred** across 15 chunks rich in other authors' "in Luc."; **close it**.

### The inbound-form question: should the lucam class also catch *Exposit. in Luc.* / *Exposit. in cap. N, v. S. Lucae*?

**Census (mine), every apparatus `**La.**` half of Vols I–VI, `Expos(it). in … Luc…`: 17 hits.**
- **15 belong to other authors:** Ambrose's *Expositio Evangelii secundum Lucam* ×14 (e.g. `bon-sent-IV-d30-a1-q2` *Ambros., II.
  Exposit. in Luc. n. 1*; `bon-sent-IV-d18-p1-littera` *Exposit. in Evang. Lucae libr. VI. n. 109*; `bon-qpe-q2-a2` ×2), Bede ×1
  (`bon-sent-II-d27-a2-q3` *Beda, V. Expos. in Luc. 17, 10*). Widening the lead of `LUC_RE` to `Expos(it).` puts all 15 at the
  mercy of the `governed_by_author` guard. Several of them name the book first (*Exposit. in Evang. Lucae libr. VI.*) or stand in a
  bracket after another author's quotation. ⚠ **`bon-sent-IV-d18-p1-littera` n. 7 opens `**La.** Exposit. in Evang. Lucae libr.
  VI. n. 109` with no author siglum in the note at all** (Ambrose is named only in n. 8). A widened pattern would file it as
  Bonaventure's own commentary.
- **2 are Bonaventure's own Luke commentary, and today both produce NO lucam record:**
  1. **`bon-sent-IV-d21-p1-a1-q2` n. 8:** *Cfr. C. Aquam sale (20.), de Consecrat. d. 3, et **S. Bonav. Exposit. in Luc. 18, 13.*** →
     would be `lucam:18:13`, `forward`. The ledger has no record for n. 8 at all.
  2. **`bon-ioan-c3-v13-16` p. 283 n. 2 (T12):** ***Bonelli notat:** Nisi videlicet eo sensu, quo inquit **interpres noster Exposit. in
     cap. 3, 21. S. Lucae**: « Nemo ascendit in caelum, nisi qui descendit de caelo, id est, nisi sit membrum Christi … »* → would be
     `bon-luc-c3-v21-22`, `chunk`. The ledger holds only the note's Eph. 2:6.

**Is the second one really Bonaventure's, and does Quaracchi treat it so? Yes.** Quaracchi answers it from this side.
`bon-luc-c3-v21-22` **p. 83 n. 3**: *Sequitur Ioan. 3, 13, post quem **Vat.** prosequitur: id est, nisi sit membrum Christi, qui
descendit de caelo; nec hoc fieri potest … **Haec verba iuxta Bonelli allegavimus tom. VI. pag. 283, nota 2.*** So the words
Bonelli quotes from "our interpreter" are this commentary's text at Luke 3:21–22 **in the Vatican edition's form**. Quaracchi
moved that sentence out of its text into the apparatus as a Vat. addition, and it cross-refers to the Bonelli note itself. That
reverse link is in the ledger today as `crossref / page / tom. VI. pag. 283, nota 2 → page-multi`, a T6 site. **The pair should
resolve both ways.** The inbound therefore lands on an apparatus variant, not on the printed body sentence. The job's table should
say so in the row.

**⚠ On "Bonelli's Supplementum commentary is pseudonymous": the repo does not support that as stated, and points the other
way.**
- Quaracchi itself (Vol I, the d. 14 dubia apparatus, recorded in `manual-review/d14-scaffolds-sweep-audit-log.md`) cites
  ***S. Doctor** in Comment. in Ioan. c. 8, 39 (**Supplem. Bonelli, tom. I. col. 735.**)*. That treats the John commentary printed in
  Bonelli's *Supplementum* as the Seraphic Doctor's.
- The pseudo-Bonaventure text the repo does record is **the Vatican edition's Commentary on John** (`bon-ioan-c20-v1-9` Notes: "the
  Vatican edition's pseudo-Bonaventure Commentary on John"), not Bonelli's.
- Bonelli's "interpres noster" at p. 283 n. 2 is an **annotator citing Bonaventure's Luke commentary**. It is not a claim that
  Bonelli wrote it, and nothing printed in vols 6–7 calls either the Luke commentary or Bonelli's notes pseudonymous.
- **I found no Quaracchi statement on Bonelli's authorship or pseudonymity anywhere in vols 1–7 as transcribed.** If the premise
  comes from outside the repo (the Quaracchi Prolegomena to Vol VI/VII, not transcribed), it needs a plate read before it goes into
  any ruling or note. Either way **it does not change the routing:** the target text is this commentary, which Quaracchi prints
  as Bonaventure's.

**⭐ Recommendation (inbound forms): catch both, but by a two-row explicit site table in the tool job (the D1_SITES pattern),
not by widening `LUC_RE`.** Two sites against fifteen Ambrose/Bede sites that a wider pattern would have to keep excluding is the
wrong trade. Resolve the reciprocal p. 83 n. 3 → p. 283 n. 2 under T6. Revisit a pattern only if a third own-commentary *Exposit.*
form turns up.

---

## 12. THE p. 88 DEPLOY: WHAT MUST BE TRUE FIRST

Ruling 14: *The recommendation to call p. 88 (Luke 1–3 live for Advent) stands on the record; the deploy itself is still asked for,
on its own, when the p. 88 gate closes.* **This sheet makes no recommendation for or against the deploy.** The coordinator asks
Wilson separately. Below is only what must be true for it to be safe, checked against the code and the generated data on
2026-11-14.

| # | precondition | state now | evidence |
|---|---|---|---|
| D1 | **Index tools run in order before any site build:** `build-citations.py` → **`build-authorities.py`** → **`build-index-json.py`**, then `build-content.mjs` (and `build-index-json.py` + `build-content.mjs` once more before the vercel build, the c9 two-pass rule) | ⛔ **NOT MET for authorities.** `index/authorities.tsv` holds **zero** `bon-luc-*` records; its last commit is `20077ec` (2026-11-07, before vol7 existed), and `site/src/data/authorities-by-chunk.json` has 0 vol7 keys. The per-chunk loop ran `build-citations` → `build-content` → `build-index-json` → `build-content` and never `build-authorities`. `build-authorities.py` does scan vol7 (it iterates `VOLUME_COMPLETE`'s keys, and 7 is a key) | `git log -1 -- index/authorities.tsv`; resume "Build and deploy" recipe |
| D2 | the citation → site path is current | **met at HEAD.** `index-crossref.json` was committed with the ledger in `507e0b7`. ⚠ `index/citations.tsv` has a newer mtime (21:05) than the site JSON (21:01) but `git status` shows it unchanged, so a concurrent agent regenerated it byte-identical. **Re-run `build-index-json.py` after the tool job (item 11) if that job lands first** | `git status`; file mtimes |
| D3 | **`TOMES[7]` and the work registry** | **met in code.** `TOMES[7] = { title: "Book VII: Commentarius in Evangelium S. Lucae", initial: "7" }` (ruling 25); `WORKS.lucam` = book 19, tome 7, initial "L", `divisionLabel: "Capitula"`, divisions `0: Prooemium`, `1–3: Capitulum I–III`; `WORK_FACTS.lucam` = "Commentary on the Gospel of Luke", unit "pericope(s)"; `VOL_DIRS` includes `vol7` | `site/scripts/build-content.mjs` L229–236, 259, 1081–1124 |
| D4 | **breadcrumb `Cap. N, Vers. a-b`** | **met in data.** `buildWorkChunkTitle` routes `lucam` through the commentary branch; `content.json` book 19 has 4 divisions / **22 chunks, all `hasTranslation: true`**, titles `Cap. 1, Vers. 1-4` … `Cap. 3, Vers. 23-38`; division 0 reads `Prooemium` and `Expositio prologi` (type-named, no "Cap. 0") | `site/src/data/content.json` |
| D5 | **the reader renders vol7: work landing `/lucam`, tome page `/tome/7`, unit pages `/lucam/c1-v1-4` …** | ⛔ **NOT YET SEEN.** The routes are data-driven (`[work]`, `[work]/[unit]` and `tome/[n]` all `generateStaticParams` from `content.json`), so they should appear. But **no site build has run since vol7 began:** `site/out/` and `.vercel/output/` are dated 2026-11-07 13:40, and there is **no `out/lucam`, no `out/tome/7`**. Nothing for Luke has ever been rendered by Next | `ls site/out`, `site/src/app/*` |
| D6 | **"Cite this" / tome label** | met in data: `progress.json` carries `n: 7, tome: VII, year: 1895`, which `chunk-view.tsx` reads. Its Luke counts are stale (`done: 5`), but `npm run build` reruns `build-progress.mjs` | `site/src/data/progress.json`; `site/package.json` scripts |
| D7 | **the p. 16 corrigenda-inside-note, unseen in a browser** (ruling 23's owed look: `bon-luc-c1-v5-17`, p. 16 n. 8, click "tr.") | **owed.** `content.json` carries `p16-8` with `[^tr-corrigenda]` inside its `en` and a separate `tr-corrigenda` entry; `text-reader.tsx` passes apparatus `en` through `renderInline` and treats `tr-` ids as translator's notes. The code path was read end to end at p. 27. **It has still never been displayed** (D5) | `content.json`; `site/src/components/text-reader.tsx` L278–322 |
| D8 | p. 88's split register | not a defect: `KNOWN_TOTALS_VOL7[88] = 12`, nn. 1–9 `c3-v23-38`'s, **nn. 10–12 Cap. IV's and PENDING** (the apparatus check passes with them pending). A Luke 1–3 deploy shows nine notes on p. 88 by design | resume, verification line |
| D9 | what else the deploy carries | `git log origin/master..HEAD` = **53 commits unpushed**, which include **`b804dec` (the six Vol VI corrigenda, rulings 8–9: live Vol VI text changes)** and the lucam citation class `faa3d93` / `32eae12` (new backlinks into Vols I–VI). Push and deploy are each Wilson's per-action OK; a "Luke deploy" is not Luke-only | `git log` |

**The short list, if Wilson says go:** (1) run `build-authorities.py` then `build-index-json.py` (D1); (2) a local `npm run build` and
preview, opening `/tome/7`, `/lucam`, one pericope page and `/lucam/c1-v5-17`'s p. 16 n. 8 "tr." (D5, D7); (3) the push and the
deploy, each with its own OK, knowing they carry D9; (4) **one deploy per OK**, checked with `npx vercel ls` / `inspect`, never
re-run. The p. 88 gate's own edits (items 2, 6, 7) and the tool job (item 11) should land **before** step 1 if they are to be
live.

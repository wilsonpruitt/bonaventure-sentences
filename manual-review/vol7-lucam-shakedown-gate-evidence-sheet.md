# Vol VII *Lucam* SHAKEDOWN GATE (p. 27, ruling 14): EVIDENCE SHEET

Compiled 2026-11-14 by a read-only agent. **Nothing here is settled. Wilson rules off this sheet.** No file under `vol7/`,
`tools/`, `site/` or the resume note was edited. Nothing was committed, pushed or stashed. The mechanical passes (live
flags, style scan, boundary sweep) are another agent's, run at the same time, and are not repeated here.

**Scope: 6 chunks, pp. 3–27.** prooem 35 · prol 34 · c1-v1-4 11 · c1-v5-17 50 · c1-v18-25 21 · c1-v26-38 69 = **220 numbered
entries + 6 `tr-` notes** (`tr-annuntiare` ×2, `tr-corrigenda` ×3, `tr-corrigenda-2`, `tr-evangelizare`; counted as labels).

⛔ **Every census below is taken over the RENDERED region only:** the `## Latin` body, the `## English` body, and the
`**La.**` / `**En.**` halves of `## Apparatus`. Frontmatter and `## Notes` are excluded. Cells read **body+apparatus**; `·` = 0.
`tr-` definitions are excluded from the counts (they are ours, and they quote the Latin they discuss). Scripts: scratchpad
`gate/regions.py`, `gate/counts.py`, `gate/census.py`. Douay checked against `~/douay-glossa/raw/DRC.json` (Challoner),
Vulgate against `raw/VulgClementine.json` in the same repo.

**Lines** in the cost columns = lines of the chunk file. Every body paragraph and every apparatus half is one line, so
"1 line" can carry several sites. Notes-only corrections are counted separately as "doc".

---

## ▶ DOCKET SUMMARY (one word each: "Approve" takes the ⭐ recommendation)

| # | item | ⭐ recommendation (mine) | lines it changes | kind |
|---|---|---|---|---|
| 1 | ruling 12 register, sites in view | **Ratify ruling 12 at every site.** Fix three carried-rule departures: *eruditio* → "erudition" (`prooem` ¶ 17, `c1-v5-17` ¶ 7; ruling 11/VI-93), "Holy Ghost" → "Holy Spirit" (`prooem` ¶ 18; VI-80b), *intelligentia* → "intelligence" (`prooem` ¶ 24). *documentum* "lessons"/"instruction" ratified by number | **4** + 3 doc | per-site |
| 2 | *evangelizare* | **Ratify `c1-v18-25` as built and amend ruling 12 to its reason:** "preach the gospel", never bare "preach"; the Douay's "bring good tidings" stands where the Douay has it (1:19, 2:10) with `tr-evangelizare`. The Douay renders Luke's 10 sites five ways, three of them as bare "preach" | **0** + 1 doc + ruling sentence | ruling |
| 3 | *verecundia* | **"shamefastness" / "shamefast" for the work** (the Hexaemeron's *modestia, verecundia* precedent; `c1-v26-38` as built); *pudicitia* → "purity" | **3** (`c1-v18-25`) + 1 doc | per-site |
| 4 | Ps. 118:173 "Let thy hand be done" | **Ratify** (VI-93: the exposition leans on *Fiat*; silent adjustment + Notes is the corpus practice) | **0** | — |
| 5 | *praedicabilis*, Cant. 6:8; other banked items | **Keep "worthy to be preached"; adjust Cant. 6:8 → "preached her most blessed"** (¶ 49 proves ¶ 46's *praedicabilis* from it). The ten other banked items need no text edit | **1** + 1 doc | per-site |
| 6 | `title_la` scope | **Opening rubric, whole, as built** (*Ioannem* ruling 79(b)); restate the manifest gloss. Only `c1-v18-25` is affected now; `c1-v46-56` next | **0** + 1 doc | ruling |
| 7 | corrigenda addendum inside a note | **It renders** (parser keeps the marker, `content.json` has it, `renderInline` links it). **Keep the shape**; one browser look at the next preview. ~5 more uses coming | **0** | — |
| 8 | ruling 13 citation class | **Write the INBOUND class now, keyed chapter + verse** (~22 sites in Vols I–VI, today filed as Gospel verses at confidence A). **No in-work `supra n.` class yet** (the *Ioannem* has 639 unindexed). Tool job after the gate | **0** text; 1 tool job | tool |
| 9 | `TOMES[7]` | **`7: { title: "Book VII: Commentarius in Evangelium S. Lucae", initial: "7" }`** (title-page wording) | **1** code | mechanical |
| 10 | `low` rows at ¶ 81 | **Keep the ¶ 81 cut** (read on p. 62: ¶ 81 opens at the head of 62R, ¶ 80 closes at 62L's foot, marginale *De testimonio Annae*) | **0** | — |

**If all are taken: 8 English lines (prooem 3 · c1-v5-17 1 · c1-v18-25 3 · c1-v26-38 1) + 1 code line + ~7 doc lines + one sentence in ruling 12 + one
tool job. No line in any `## Latin` or Latin apparatus half changes.**

---

## 1. RULING 12 REGISTER, WITH SITES IN VIEW (plus the ruling-11 carries it touches)

**Census (Latin sites → English rendering, body+apparatus).**

| term (ruling 12 rendering) | La sites prooem / prol / v1-4 / v5-17 / v18-25 / v26-38 = total | English as built | verdict |
|---|---|---|---|
| *misericordia* (mercy) | · / · / · / 0+1 / · / 3+1 = **5** | "mercy" 5/5 | holds |
| *pietas* (piety) | 1+0 / · / · / · / · / · = **1** (Augustine, ¶ 6) | "piety" 1/1 | holds; *pietas divina* not yet met |
| *benignitas* (kindness) | · / · / · / 0+1 / · / · = **1** (+ adverb *benigne* in the Prologus, p. 7 n. 9) | "kindness" 1/1 | holds |
| *clementia* · *compassio* · *miseratio* | **0 · 0 · 0** | — | positive zeros (also *misereri* 0, *impietas* 0) |
| *praedicare* / *-atio* / *-ator* (preach…) | 17+0 / 3+6 / · / 7+1 / · / 5+0 = **39** | "preach-" 38; **"proclaim" 0**; "predicate" 0 | holds; the one non-"preach" is Cant. 6:8 (item 5) |
| *annuntiare* family (announce, `tr-annuntiare`) | 11+1 / · / · / 2+0 / 2+0 / 3+1 = **20** | "announce(ment)" throughout; *nuntius* "messenger" | holds; ⚠ *bona nuntiatio* split, see item 2 |
| *denuntiatio* (declaration) / *praenuntiare* (announce beforehand) | 18 / 7 | "declaration" / "announce beforehand" | holds (house choices in `tr-annuntiare`) |
| *evangelizare* (preach the gospel) | 1+0 / 0+1 / · / · / 3+1 / · = **6** | 2 "preach the gospel", 4 "bring good tidings" | **item 2** |
| *magisterium* (teaching office) | 3+0 / · / · / 1+0 / · / · = **4** | "teaching office" 4/4 | holds |
| *paupertas · mendicus · eleemosyna · avaritia · liberalitas* | only *avaritia* ×1 (Bernard, ¶ 45) | "avarice" | holds; family not yet met |
| *remedium* (remedy) / *medicamentum* (medicine) | 5 / 3 | "remedy" 5/5 / "medicine" 3/3 | holds (record: Jerome's *medicinam*, ¶ 15, is also "medicine") |
| *mysterium* / *sacramentum* | 20 / 2 | "mystery" 20/20 / "sacrament" 1 + Tob. 12:7 *Sacramentum regis* = Douay "the secret of a king" (quotation) | holds |
| *informatio* / *informare* | **0** | — | positive zero |
| sense labels | *spiritualiter* ×1 (v18-25 ¶ 38) | "spiritually" | holds; others 0 |
| *publicanus* · *legisperitus* · *sacerdos* | 2 · 0 · 37 | "publican" 2/2 · — · "priest" 37/37 | holds |
| *Praeceptor* (Master + `tr-praeceptor` at 5:5) | 0 | — | not yet met |
| Marian register (v26-38): *Ave, gratia plena* · *ancilla* · *obumbrabit* · *Spiritus sanctus* | — | "Hail, full of grace" · "handmaid" · "overshadow" · "Holy Spirit" | holds (*famula* I Kings 25:41 "servant") |

**Departures found (all from the carried rulings, not from ruling 12 itself).**

| # | site | Latin | built | rule it departs from | fix | lines |
|---|---|---|---|---|---|---|
| 1a | `prooem` ¶ 17; `c1-v5-17` ¶ 7 | *eruditionis magisterium / magisterio* (the Tabula's Pars II) | "the teaching office of **instruction**" | ruling 11 carries Vol VI ruling 93: ***eruditio* → "erudition" everywhere** (it collides with *instructio* → "instruction") | "the teaching office of erudition" | **2** + 2 doc (both Notes quote it) |
| 1b | `prooem` ¶ 18 (Acts 10:38) | *unxit eum Deus Spiritu sancto* | "anointed him with the **Holy Ghost**" | Vol VI ruling 80(b): **"Holy Spirit" everywhere, Douay quotations included**. The other 24 sites in scope say "Holy Spirit" | "Holy Spirit" | **1** |
| 1c | `prooem` ¶ 24 | *generalis intelligentia* | "understanding" | ruling 11 (Vol V *septem donis*): ***intelligentia* → "intelligence" in body prose**. The Notes justify it as "no *intellectus* near", but ¶¶ 2–17 run on *generalis intellectus*, so the contrast is in the chunk. `c1-v5-17` ¶ 28 and `c1-v26-38` ¶ 52 say "intelligence" | "a certain general intelligence of the whole Book" (now "…general understanding…") | **1** + 1 doc |

**Undecided term with two renderings (no rule to depart from).** *documentum*: "lessons" (`prooem` ¶¶ 8, 12, plural
*documenta*) and "instruction" (`c1-v1-4` ¶¶ 3, 6, singular *Apostolorum documentum*). Today "instruction" also carries
*eruditio* at 1a. Once 1a is fixed, "instruction" carries only *documentum* (and *instructus* "instructed"). **Ratify both by
number** (plural "lessons", singular "instruction"). 0 lines.

**Record only:** v18-25 ¶ 31 renders III Kings 1:42 *bona annuntians* as "bringest good tidings" and calls it the Douay's.
The Douay (Challoner) prints "bringest good **news**". The adjustment is licensed because ¶ 31 leans on *bona nuntiatio*
(Vol VI ruling 93), but the Notes sentence is wrong (1 doc line).

**⭐ Recommendation (mine): RATIFY ruling 12 as the Luke register at every site; apply 1a, 1b and 1c. "Approve" = 4 lines + 3
doc lines.**

---

## 2. *evangelizare*

**Census: 6 Latin sites in scope (none in `c1-v1-4`, `c1-v5-17`, `c1-v26-38`).**

| chunk | site | Latin | English as built | Douay at that verse |
|---|---|---|---|---|
| prooem | ¶ 19, Luke 4:43 | *Aliis civitatibus oportet me **evangelizare** regnum Dei* | "I must **preach the gospel** of the kingdom of God" | "I must **preach** the kingdom of God" |
| prol | p. 10 n. 2 (Sedulius, not scripture) | *per ora doctorum **evangelizat*** | "he **preaches the gospel** … through the whole world" | — |
| c1-v18-25 | ¶ 31, lemma Luke 1:19 | *haec tibi **evangelizare*** | "to **bring thee these good tidings**" + `[^tr-evangelizare]` | "to **bring thee these good tidings**" |
| c1-v18-25 | ¶ 31, exposition | *missus … et loqui et **evangelizare*** | "to **bring good tidings**" | — |
| c1-v18-25 | ¶ 31, exposition | *In **evangelizatione** vero … Evangelium enim est bona nuntiatio* | "in *the bringing of good tidings* … For the *Gospel* is good tidings" | — |
| c1-v18-25 | p. 18 n. 4 (Bede) | *ad **evangelizandum** Zachariae missum* | "sent to **bring good tidings** to Zachary" | — |

So: **2 "preach the gospel", 4 "bring good tidings"** (one line in ¶ 31 carries three of the four).

**The decisive sentences.**
- Ruling 12 (`vol7-pilot-setup.md`): *"*evangelizare* → the Douay's 'preach the gospel'."* Its proposal text (`lucam-pilot-scouting.md`
  12) gives the reason: *"the Douay's 'to preach the gospel', **which keeps it apart from *praedicare* by the word 'gospel'**."*
- ¶ 31: *In evangelizatione vero intelligenda est denuntiatio bonitatis. Evangelium enim est bona nuntiatio* / "But in *the bringing of good
  tidings* is to be understood the declaration of goodness. For the *Gospel* is good tidings."
- Vol VI ruling 93 (carried): *"the Douay is adjusted to Bonaventure's word where the exposition … leans on that word; where nothing leans,
  the Douay stands."*

**⭐ What the Douay actually does. The ruling assumes one Douay rendering, and there are five.** All ten *evangeliz-* verses in Luke (Clementine
Vulgate checked against Challoner):

| verse | Vulgate | Douay | collides with *praedicare* → "preach"? |
|---|---|---|---|
| 1:19 | *evangelizare* | **bring** thee these **good tidings** | no |
| 2:10 | *evangelizo* | I **bring** you **good tidings** | no |
| 3:18 | *evangelizabat* | did he **preach** | **yes** |
| 4:18 | *evangelizare* | to **preach the gospel** to the poor | no |
| 4:43 | *evangelizare* | I must **preach** the kingdom of God | **yes** |
| 7:22 | *evangelizantur* | **the gospel is preached** | no |
| 8:1 | ***praedicans et evangelizans*** | **preaching and evangelizing** | no; but "preach the gospel" here gives "preaching and preaching the gospel" |
| 9:6 | *evangelizantes* | **preaching the gospel** | no |
| 16:16 | *evangelizatur* | the kingdom of God **is preached** | **yes** |
| 20:1 | *evangelizante* | **preaching the gospel** | no |

The ruling's wording ties the rendering to the Douay, and its stated reason is to keep it off *praedicare*. Those two come apart at three verses
(3:18, 4:43, 16:16), where the Douay itself says bare "preach". The prooem builder already resolved one of them in favour of the reason: 4:43 is
"preach the gospel of the kingdom", *not* the Douay (⚠ its Notes call this "the Douay's wording", which is wrong; 1 doc line). The `c1-v18-25`
builder resolved 1:19 in favour of the Douay's wording. **Neither departed from the ruling's purpose. They read its two halves differently.**

**A knock-on, same Latin rendered two ways.** *Evangelium … bona nuntiatio*: prooem ¶ 14 (and Bonaventure's source in p. 5 n. 4, *bona annuntiatio*)
renders "good **announcement**", because ¶ 14 hangs *Evangelium* on *Ad annuntiandum* and `tr-annuntiare` says so. `c1-v18-25` ¶ 31 renders "good
**tidings**", because ¶ 31 hangs it on *evangelizare*. Each gloss leans on a different word, so each is the ruling-93 outcome. Conforming either would
break its own paragraph.

| option | cost (lines changed) |
|---|---|
| **(a) Amend ruling 12 to its reason: *evangelizare* → "preach the gospel" by default, never bare "preach" (Douay "preach" at 3:18, 4:43, 16:16 adjusted). Where the Douay itself says "bring good tidings" (1:19, 2:10: an angel bringing a message, with an object), the Douay stands, with `tr-evangelizare` at each chunk's first site. 8:1 *evangelizans* keeps the Douay's "evangelizing" beside "preaching"** | **0 text lines** (all 6 sites already conform). 1 doc line (prooem Notes 4:43 claim). The ruling text gains one sentence |
| (b) The ruling's letter: "preach the gospel" at every site | `c1-v18-25`: ¶ 31 En (3 sites in one line) + p. 18 n. 4 En + delete `tr-evangelizare` def + `transcription_status` = **4 lines** + Notes. Luke 1:19 becomes "to preach the gospel of these things to thee", and ¶ 31's *bona nuntiatio* gloss no longer meets its word. 2:10 will hit the same wall |
| (c) Per-verse Douay everywhere | 1 line now (prooem ¶ 19 → "preach the kingdom of God"). **Three Luke verses then render *evangelizare* and *praedicare* the same**, which is exactly what the ruling was written to prevent |
| (d) Conform *bona nuntiatio* to one English | 1 line (¶ 31 → "announcement") or 2 lines (prooem ¶ 14 + p. 5 n. 4 → "tidings", and `tr-annuntiare` reworded). Either breaks the gloss in its own paragraph. **Not recommended** |

**⭐ Recommendation (mine): (a). Ratify `c1-v18-25` as built; amend ruling 12's wording to its reason; keep both *bona nuntiatio* renderings.
"Approve" = 0 text lines + 1 doc line + the ruling sentence.**

---

## 3. *verecundia*

**Census: 5 Latin *verecund-* sites, all in the last two chunks, plus the neighbouring words they must stay apart from.**

| chunk | site | Latin | English as built |
|---|---|---|---|
| c1-v18-25 | ¶ 35 (divisio) | *verecunda occultatio* | "the **modest** concealment" |
| c1-v18-25 | ¶ 38 | *Tertio describitur **verecunda** occultatio* … *signum humilitatis et **pudicitiae*** | "the **modest** concealment" … "a sign of humility and of **modesty**" |
| c1-v18-25 | p. 20 n. 3 (Ambrose via the Gloss) | ***verecundia** seu **pudor*** | "**modesty** or **shame**" |
| c1-v26-38 | ¶ 50 | *In auditu commendatur **modestia*** | "her **modesty**" |
| c1-v26-38 | ¶ 51 (×2) + marginale *In affectu verecunda* | *In affectu commendatur **verecundia** … scilicet ex **verecundia*** | "her **shamefastness** … out of **shamefastness**" |
| c1-v26-38 | ¶ 52 | *propter **pudorem** innocentiae* | "the **shame** of innocence" |
| c1-v26-38 | ¶ 44 | *congruentia ostenditur **pudica*** | "**chaste**" |

So in `c1-v18-25` the one English word "modest(y)" carries **three** Latin words (*verecundus*, *verecundia*, *pudicitia*). In `c1-v26-38`, ¶¶ 50–52
set *modestia*, *verecundia* and *pudor* as the Virgin's three commendations side by side.

**The decisive sentence.** ¶¶ 50–51: *In auditu commendatur modestia … In affectu commendatur verecundia* / "In *hearing* her *modesty* is commended
… In *affection* her *shamefastness* is commended." **Two of the three members. One English word for both erases the division.**

**How Vols V–VI render it (grep over the rendered regions of `vol5/`, `vol6/`; 15 chunks with *verecund-*):**
- **Where *modestia* stands beside it, *verecundia* → "shamefastness".** `bon-hex-c6`: *Temperantiam sequuntur modestia, verecundia, abstinentia,
  castitas* → "modesty, shamefastness, abstinence, chastity". `bon-hex-c5`: the Aristotelian mean *verecundia* / *nemesis* → "shamefastness"
  (and *modestiae* → "modesties" in the same collatio). **This is the exact Luke ¶¶ 50–51 situation, already settled this way in Vol V.**
- **Elsewhere the noun is "shame"**: `bon-ioan-c3-v1-2` (*verecundia quaedam* → "a certain shame", ×2), `bon-ioan-c8-v1-11`, `bon-serm-s2`,
  `bon-praec-c6`; `bon-brev-p6-c8` "bashfulness".
- **The adjective in the *Ioannem* is "modest"**: `bon-ioan-prol` *virgini verecundae* → "a modest virgin"; `bon-ioan-prooem` *ut verecundus* →
  "out of modesty".
- *pudicitia*: QPE ruled *pudicitia* → **"purity"** (the purity triple, `CLAUDE.md`); Vol VI ruling 81(d) released the triple for the *Ioannem*
  because *pudicitia* had zero sites. Luke has no ruling, and its first site (¶ 38) is "modesty".

The *Ioannem* pattern (noun "shame", adjective "modest") does not port: "shame" is taken by *pudor* at ¶ 52, and "modest" by *modestia* at ¶ 50.

| option | cost (lines changed) |
|---|---|
| **(a) *verecundia* → "shamefastness", *verecundus* → "shamefast" for the whole work (the Hexaemeron precedent, and `c1-v26-38` as built); *pudicitia* → "purity" (the QPE rendering), so "modesty" is left to *modestia* alone** | `c1-v18-25` ¶ 35 En ("the shamefast concealment"), ¶ 38 En ("the shamefast concealment"; "of humility and of purity"), p. 20 n. 3 En ("shamefastness or shame") = **3 lines** + 1 doc (Notes register line) |
| (b) "modesty / modest" for *verecund-* throughout | Impossible at ¶¶ 50–51 without moving *modestia* off "modesty". If *modestia* → "moderation" instead: `c1-v26-38` ¶ 50 + ¶ 51 ×2 = **2 lines**, and *moderatio* (unmeasured in Luke) loses its word |
| (c) The *Ioannem* split (noun "shame", adjective "modest") | Collides with *pudor* → "shame" at ¶ 52 and with *modestia* at ¶ 50. Not workable |
| (d) Leave the two chunks as they are | 0 lines; the work carries two English words for *verecund-* and three Latin words under "modest" in one chunk |

**⭐ Recommendation (mine): (a). "Approve" = 3 lines in `c1-v18-25` + 1 doc line. `c1-v26-38` unchanged.**

---

## 4. Ps. 118:173 in `c1-v26-38` ("Let thy hand be done")

**Sites (2):** ¶ 69 body, and Augustine in p. 26 n. 7. ¶ 69 also quotes Ps. 105:48 *Fiat, fiat*, kept as the Douay's "So be it, so be it".

**The decisive sentence (¶ 69).** *…nec volo, ut fiat mihi … — **Fiat** enim triplicem sensum habet: desiderii … assertionis, sicut in Psalmo: « Dicet omnis
populus: Fiat, fiat »; et iterum **affectionis**, ut in Psalmo: « **Fiat manus tua**, ut salvet me »* / "…of *affection,* as in the Psalm: « **Let thy hand be
done**, to save me »." The paragraph expounds the word *Fiat* in three senses; Ps. 118:173 is the proof text for the third.

**Douay:** "Let thy hand be **with me** to save me". The word the sentence is about disappears.

**The corpus rule and its precedents.**
- `CLAUDE.md`, every pilot: *"Scripture on the Douay-Rheims base adjusted to Quaracchi's actual Latin."* Vol VI ruling 93 states the test: *"the Douay is
  adjusted to Bonaventure's word where the exposition … leans on that word; where nothing leans, the Douay stands."* The *septem donis* gate (*pietas*:
  "godliness" adjusted at Isa. 11:2 and I Tim. 4:8) and the *Ioannem* gate (ruling 82(c): thirteen Douay adjustments ratified as a block, e.g. 1:14
  "dwelt in us") are the precedents.
- **How a departure is marked: SILENTLY in the English, disclosed in the chunk's `## Notes`.** No `tr-` note in Vols V–VII exists for a Douay
  adjustment (the `tr-` labels in use are *doctrina*, *lumen*, *vacare*, *corrigenda*, *studium*, *annuntiare*, *evangelizare*, *dilectio*). The Luke
  shakedown chunks already adjust silently at 1:1 "in us", 1:2 "themselves saw", 1:4 "truth", 1:17 "prudence", John 5:35 "lamp", 1:20 "silent", Esther
  15:16 "wonderful", each with a Notes line. The `[so printed]` bracket is for Quaracchi's misprints, not for Douay wording.
- Ps. 105:48 "So be it" is the right call under the same test: it is the *assertionis* sense, and "So be it" *is* that sense in English.

| option | cost (lines changed) |
|---|---|
| **(a) Ratify as built (adjusted, disclosed in Notes)** | **0** |
| (b) Douay wording + a `tr-` note on *Fiat* | ¶ 69 En + p. 26 n. 7 En + new def = 3 lines, and a `tr-` class the corpus has never used for this |
| (c) Douay wording + inline bracket ("be with me [*Fiat*]") | 2 lines; a bracket class reserved for misprints |

**⭐ Recommendation (mine): (a). "Approve" = 0 lines.**

---

## 5. Other register drift the builders flagged, and every item banked "for the gate"

**5a. ¶ 46 *praedicabilis* → "worthy to be preached" (×2, divisio inside ¶ 46), and ¶ 49 Cant. 6:8 *praedicaverunt* → Douay "declared".**
¶ 46 divides the Virgin's excellence three ways: *amabilis* (from fullness of goodness), *venerabilis* (from height of dignity), ***praedicabilis***
(*a laudis amplitudine*). ¶ 49 carries out the third member; its marginale reads *Praedicabilis a laudis amplitudine*, and it closes on Cant. 6:8
*Viderunt eam filiae Sion et beatissimam **praedicaverunt*** / "…saw her and **declared** her most blessed". So the proof text exists to show
the word. Under Vol VI ruling 93 the exposition leans on it.
- "Praiseworthy" is taken: ¶ 49 opens *ut … ostendat ipsam **laudabilem*** → "praiseworthy".
- "Declare" is taken: *denuntiatio* → "declaration" stands in ¶ 46 itself ("the declaration of the conception to come").
- "Proclaim" is refused by ruling 12.

| option | cost |
|---|---|
| (a) Ratify both as built | 0. The ¶ 46 → ¶ 49 hinge is invisible in English |
| **(b) Keep "worthy to be preached"; adjust Cant. 6:8 to "**preached** her most blessed" (ruling 93: the exposition leans on the word)** | **1 line** (¶ 49 En) + 1 doc. The English is unidiomatic, which is the price ruling 93 has paid before (*pietas*) |
| (c) *praedicabilis* → "worthy to be declared" so it meets the Douay | 1 line (¶ 46); collides with *denuntiatio* "declaration" in the same paragraph, and breaks ruling 12 |

**⭐ Recommendation (mine): (b).** The other *praedicare* sites in the chunk need nothing: ¶ 67 Rom. 10:8 "which we preach" (Douay = rule) and ¶ 69
Bernard *declamatorie praedicatum* "preached in declamation".

**5b. Everything else banked in the six chunks' Notes, collected. None needs a text edit. The ✔ items are for the record.**

| chunk | item | disposition |
|---|---|---|
| prooem | `tr-annuntiare` is the one new house decision | ✔ ratified under item 1 |
| prooem | display heading `### Prooemium commentarii in Lucam` has no period, because none is printed (`bon-ioan-prooem` has one, but its heading is anchored and pointed) | ✔ as printed, ruling 4 |
| prooem | Notes say Luke 4:43 "preach the gospel" is "the Douay's wording"; it is not | 1 doc line (item 2) |
| prol | five roman, unguillemeted scriptural allusions in Jerome's *Prologus* (Tit. 1:14, John 17:12, Acts 1:24–26, Acts 9:5, II Tim. 2:6), banked under the COLLECTION CHANGE; and the first *expositio* whose lemma is a non-scriptural text | ✔ collection data, no ruling asked |
| prol | p. 7 n. 3 *corsummationem* bracketed `[so printed]` (not in the Corrigenda) | ✔ standing convention |
| c1-v1-4 | `section: 1` supplied though the manifest column is blank (ordering only); the same holds for v5-17 = 2, v18-25 = 3, v26-38 = 4 | ✔ the *Ioannem* practice |
| c1-v5-17 | the Corrigenda addendum leaves open whether *vel* is roman and whether the words go before or after the period | ✔ set roman, before the period; see item 7 |
| c1-v18-25 | Notes call III Kings 1:42 "bringest good tidings" the Douay's (Douay: "good news") | 1 doc line (item 1) |
| c1-v26-38 | p. 22 Corrigenda entry is loose against the plate (lemma *a Virgine et domo* / plate *de virgine et domo*; l. 14 / l. 15), applied at the page's only *et domo* | ✔ unambiguous site |
| c1-v26-38 | Quaracchi *exluditur* (¶ 44) bracketed `[so printed]` | ✔ standing convention |

---

## 6. `title_la` scope for multi-rubric chunks

**The rubrics each chunk contains, and its title as built** (all in place in both languages as `####`, per ruling 4):

| chunk | `title_la` / `title_en` (built) | rubrics in the chunk (tier @ page, ¶ governed) | does the title's rubric govern the whole chunk? |
|---|---|---|---|
| c1-v5-17 (¶¶ 7–28) | *Tria dicuntur de conceptu praecursoris* / "Three things are said of the conception of the precursor" | t0 *Divisio generalis*⁸ @12R · t1 *Pars. I. De incarnationis mysterio agitur tripliciter.* · t2 *Primo, de nativitate in utero dupliciter.* · t3 *Primo, de duplici fecundatione.* · **t4 *Tria dicuntur de conceptu praecursoris.*** (all @13L, a stack) · t4 *Primo describitur parentum conditio quadrupliciter.* @13R (¶¶ 8–11) · t4 *Secundo describitur angelica annuntiatio.* @14R (¶¶ 12–28) | **yes, and more**: it governs ¶¶ 7–39 (the precursor's conception, through `c1-v18-25`) |
| c1-v18-25 (¶¶ 29–39) | *Tertio describitur promissionis confirmatio quadrupliciter* / "Thirdly the confirmation of the promise is described in four ways" | **t4 *Tertio describitur promissionis confirmatio quadrupliciter.*** @17R (¶¶ 29–34) · t4 *Quarto describitur promissionis impletio quadrupliciter.* @19R (¶¶ 35–39) | **no**: ¶¶ 29–34 only; ¶¶ 35–39 stand under a sibling |
| c1-v26-38 (¶¶ 40–70) | *Tria dicuntur etiam de conceptu Salvatoris* / "Three things are also said of the conception of the Saviour" | **t4 *Tria dicuntur etiam de conceptu Salvatoris.*** @20R · its three children: t4 *Primo describitur destinatio nuntii quoad quatuor.* @20R · t4 *Secundo describitur executio ministerii quoad tria.* @22L · t4 *Tertio describitur assecutio propositi quoad tria.* @26L | **yes, exactly** (¶ 40 divides the matter into the three children). The question does not arise |

**So the issue is ONE chunk now (`c1-v18-25`), and it recurs.** Manifest stage 1 has at least one more two-sibling row: `c1-v46-56` (t4 @30R
*Secundo subditur canticum laetitiae* and t4 @34L *Tertio subditur obsequium benevolentiae*; the manifest note calls them "two t4 siblings"). Three more
rows carry two t4s whose relation is unmeasured: `c1-v57-66`, `c1-v67-80`, `c3-v15-20`.

**The decisive texts.**
- Ruling 4: *"`title_la` = the governing rubric as amended by the Corrigenda, else the lemma + Bonaventure's dividing words."*
- The stage-1 coordinator's gloss (`vol7-pilot-setup.md`, "two readings fixed … no new ruling"): *"the most specific heading in the opening cascade **whose
  scope covers the WHOLE chunk**"*. **That gloss is where the doubt comes from. Ruling 4 itself does not say "whole".**
- *Ioannem* gate ruling 79(b): *"**A stacked heading takes its LOWEST heading, whole** (Sap ruling 47): `c1-v43-51` is kept as built (*Prima manifestatio,
  quae est facta discipulis*), **though that heading also names 2:1–11. A sentence title is used only where no heading stands.**"* That is, the opening
  heading titles the chunk even when its scope does not match the chunk's. There it overran; here it under-covers.
- ⚠ **The lemma + dividing-words form does not cover ¶¶ 35–39 either.** ¶ 29's dividing words are *hic describit quantum ad promissionis confirmationem*,
  the same scope as the rubric. Only a composite covers both members.

| option | cost (lines) |
|---|---|
| **(a) First (opening) rubric, whole, as built: ruling 79(b) applied to Luke. Replace the coordinator's "covers the WHOLE chunk" with 79(b)'s "the lowest heading of the opening stack", so the same rule governs `c1-v46-56` and later** | **0 lines**; 1 doc line in `vol7-pilot-setup.md` |
| (b) Composite of the sibling rubrics (*Tertio describitur promissionis confirmatio…; Quarto describitur promissionis impletio…*) | 3 lines (`title_la`, `title_en`, `## *…*` subtitle); titles run to two clauses; a new title shape the *Ioannem* gate did not use |
| (c) Lemma + dividing words (*Et dixit Zacharias … promissionis confirmationem*) | 3 lines; **still covers ¶¶ 29–34 only**; and it departs from ruling 79(b)'s "a sentence title only where no heading stands" |

**⭐ Recommendation (mine): (a). "Approve" = 0 lines + 1 doc line.**

---

## 7. The Corrigenda ADDENDUM inside an apparatus note (`c1-v5-17`, p. 16 n. 8)

**The site as built** (`vol7/bon-luc-c1-v5-17.md`):
- La (l. 367): *…alii codd. et edd. existentiam veritatis vel exigentiam veritatis.* (no anchor in the Latin)
- En (l. 369): *…the other codices and the editions have* existentiam veritatis *or* exigentiam veritatis`[^tr-corrigenda]`.
- Def (l. 409): `[^tr-corrigenda]: **En.** Translator's note: Printed: … existentiam veritatis. (the note ends there); the editors add *vel exigentiam
  veritatis* after *veritatis*, Corrigenda, t. VII p. 858 ("p. 16, col. 2, notes l. 2"). …`
- The marker occurs **only** inside p16-8's En. No body line references `tr-corrigenda`.

**Code path, read end to end. It RENDERS.**
1. `site/scripts/build-content.mjs` `parseApparatus()`: entries are split on `\n[^id]:` (a definition *at the start of a line followed by a colon*). An
   inline `[^tr-corrigenda]` has no colon and is not at a line start, so it stays inside p16-8's text. `**La.**` / `**En.**` halves are taken by regex, and
   `cleanApparatusEntry()` only collapses whitespace. The marker is **preserved verbatim**.
2. `site/src/data/content.json` (generated 2026-11-14 15:57), entry `bon-luc-c1-v5-17`: `apparatus[p16-8].en` contains `…*exigentiam
   veritatis*[^tr-corrigenda]. Blessed Albert…`, and `apparatus[tr-corrigenda]` exists as its own entry with the note text. **Verified by reading the JSON.**
3. `site/src/components/text-reader.tsx` `ApparatusBlock`: Quaracchi's entries render `<div className="apparatus-en">{renderInline(e.en)}</div>`. The `tr-`
   entries render in a separate "translator's notes" list after them, each `<li id="fn-tr-corrigenda">`.
4. `renderInline()` tokenises `\[\^([^\]]+)\]` **anywhere** in the string it is given and emits `<sup class="fn-ref fn-ref-tr"><a href="#fn-tr-corrigenda">tr.</a></sup>`.
   The italic token `*exigentiam veritatis*` is matched first and closes before the marker, so the two do not interfere.
5. So the reader sees a superscript "tr." at the end of the italic words inside apparatus entry 8, linking to the translator's-note block on the same page.
   **The text-export path (`build-export.mjs`) passes apparatus text through unchanged**, as for every body marker.

**Not checked:** a browser. The code path has no branch that could treat this marker differently from a body marker, but it has never been *seen*. Cheap
check at the next local `pnpm build` or preview: open `bon-luc-c1-v5-17`, apparatus p. 16 n. 8, click "tr.". **Cosmetic, recorded:** every `tr-` note
displays as "tr." (`displayLabel`), so `c1-v26-38`'s `tr-corrigenda` and `tr-corrigenda-2` both read "tr.". Their links are distinct. This is the existing
convention, not new here.

| option | cost |
|---|---|
| **(a) Keep the shape as the convention for apparatus addenda: corrected Latin in the note, `tr-corrigenda[-N]` anchored at the word inside the note's En** | 0 lines. One browser look at the next preview |
| (b) No note-in-a-note: drop the anchor and write "(added by the editors' Corrigenda, t. VII p. 858)" into the En of the note | 2 lines here (En + delete def) and a second convention beside ruling 8's "one numbered translator's note … marked the same way" |

**How many will take this shape (from the Corrigenda table in `vol7-pilot-setup.md`):** of the 12 Luke entries still to come (four of the 16 are applied: pp. 9, 16, 22, 23), **four fall inside an
apparatus note**: p. 114 notes l. 2 *sesvet* → *servet*, p. 294 n. 13 delete *cum Vulgata*, p. 300 notes l. 5 *suam* → *suum*, p. 361 n. 13 *nota 3* →
*nota 13*. These are corrections, not additions, but the `tr-` anchor will sit inside a note's En in exactly this way. One more pure addendum falls
in the Threni (p. 624 n. 9). The other eight are body corrections (p. 252 is a rubric), anchored in the body as at pp. 22–23. **So the shape will be used about five more times.**

**⭐ Recommendation (mine): (a). It is ruling 8's own wording, it renders, and it keeps one note class. "Approve" = 0 lines.**

---

## 8. Ruling 13's citation class

**Two different things share the name, and the evidence for them is in different places.**

**(i) Self-citations INSIDE the Luke commentary (the six chunks).** Two by paragraph, three by page and note:

| chunk | note | printed | ledger today (`index/citations.tsv`) |
|---|---|---|---|
| c1-v5-17 | p. 12 n. 9 | *Prooemium n. 23.* | **no record** |
| c1-v26-38 | p. 25 n. 4 | *Cfr. supra n. 45.* | **no record** |
| prol | p. 8 n. 8 | *cfr. supra pag. 7, nota 5* / *nota 2* | `page-multi` → `bon-luc-prol+bon-luc-prooem`, no anchor |
| c1-v1-4 | p. 11 n. 4, p. 12 n. 1 | *Supra pag. 7.* | `page-multi`, same pair |
| c1-v26-38 | p. 20 n. 9, p. 22 n. 3 | *Cfr. supra pag. 19, nota 6* / *pag. 21, nota 10* | `chunk` + anchor `fn-p19-6` / `fn-p21-10` ✔ |

The scouting sheet measured **≈ 301 `supra / infra n.` sites** in the work's text layer, so the bare paragraph form is the work's main
self-reference. It names no capitulum: *supra n. 45* means ¶ 45 *of the citing chunk's own capitulum*, and *Prooemium n. 23* names the part.
⚠ Small resolver gap: *pag. 7, nota 5* lands `page-multi` although p7-5 exists in exactly one chunk (`bon-luc-prol`); *pag. 19, nota 6* resolves to the
note. The page+note branch does not use the note to break a shared page. One tool line, not a text edit.

**(ii) INBOUND citations of Bonaventure's Luke commentary from Vols I–VI. This is what ruling 13's "Comment. in Lucam c. N. v. M" names, and the
evidence is already on disk.** About 22 distinct sites in 19 built chunks (grep of the rendered text; three more hits are inside `## Notes` only):

| printed shape | sites (examples) |
|---|---|
| chapter, verse | *Comment. in Luc. 3, 16.* (`bon-ioan-c1-v24-28`) · *13, 21* (`bon-serm-s2`) · *24, 35* (`bon-ioan-c21-v9-14`) · 9, 50 · 11, 1 · 17, 1 · 17, 19 · 22, 23 · 22, 60 · 23, 33 · 24, 13 · *Lucam, 17, 4* |
| `c. N, M` / `c. N. v. M` / `c. N. ad v. M` | *Comment. in Lucam c. 9. v. 34.* (`bon-sent-I-d16-a1-q3`, `-dubia`) · *c. 22, 19* · *c. 23, 43* · *c. 9. ad v. 28* (`bon-serm-s3`) |
| roman chapter | *Comment. in Luc. IX, 28.* (`bon-sent-I-d2-dubia`) |
| `ad N, M` | *Comment. in Lucam, ad 18, 25* (`bon-serm-s2`) |
| **chapter + paragraph** | *Comment. in Lucam (c. 6. n. 20.)* (`bon-sent-III-d36-a1-q1`): one site |

⚠ **What `tools/build-citations.py` does with them today:** there is no Luke class (`IOAN_PARA_RE` matches only *Comment. in Ioan. c. N. n. M*). The
chapter-and-verse ones fall through to the SCRIPTURE scanner and are filed as the Gospel verse at confidence A. Verified: `bon-serm-s2`
`apparatus:p550-8` *Bonav. in Comment. in Luc. 13, 21* → `scripture / apparatus-explicit / Luc 13:21 / A`. The locus is right, but the class is wrong:
the reader's link goes to the Gospel, not to Bonaventure's exposition of it. This is the *Ioannem* gate's "silent wrong target" family at its mild end.

**Why not copy `IOAN_PARA_RE`.** The *Ioannem* class is keyed **capitulum + paragraph** because John is cited inbound by *c. N. n. M*. Luke is cited
inbound by **chapter + verse** at all but two sites (one paragraph form, one *ad locum cit.*), which is exactly what each Luke chunk's `division` + `verses:` fields hold. The *Ioannem* precedent
for the bare in-work *supra n. N* is also clear: the *Ioannem* has **639** such sites and none is indexed (ruling 82(a) put "the work's own `n. N` form"
on the tool docket, unbuilt).

| option | cost |
|---|---|
| **(a) Write the INBOUND class now, keyed capitulum + verse (`Comment.? in Luc(am)?` + `c.`/roman/bare chapter + verse, `ad` allowed), resolving to the chunk whose `verses:` holds M and reading `forward` until it is built; the one `c. 6. n. 20` site resolves by `paragraphs:`. Exclude other authors' "in Luc." (Ambrose, Bede, Albert …) with the existing `governed_by_author` guard. Do NOT write a bare `supra n. N` class: wait, with the *Ioannem*'s identical docket item** | 0 text lines. One tool job: ~22 records re-classed from scripture to crossref; ledger/QA re-run |
| (b) Also write the in-work `supra n. N` class now (key = citing chunk's capitulum + n; *Prooemium n.* = division 0) | the same job + a new resolver shape. 2 examples in scope against ≈ 301 in the work; the *Ioannem*'s 639 would want the same tool |
| (c) Wait for a self-citation in the "c. N" form | 0 now. **It may never come:** the work cites itself by *n.*, and the inbound evidence does not depend on Luke's own text at all |

**⭐ Recommendation (mine): (a), as a tool job after the gate, separate from the text, like *Ioannem* ruling 82(a). Fix the page-multi-with-note gap
in the same job. "Approve" = 0 text lines, 1 tool job.**

---

## 9. `TOMES[7]` (the browse-UI tome container)

**Now** (`site/scripts/build-content.mjs`, `const TOMES`):
```
5: { title: "Book V: Opuscula Theologica", initial: "5" },
6: { title: "Book VI: Commentarii in Sacram Scripturam I", initial: "6" },
```
No entry for 7. The comment above it says a container exists *"so the Opera Omnia's volume sequence still reads 1-2-3-4-5 instead of degenerating into
one top-level row per work. Tomes I-IV are a single work each and need no entry."* `content.ts` `browseEntries()` groups by `tomeTitle` and makes a
top-level row of any book without one. **So today Luke browses as a stand-alone row, initial "L", outside the numbered 1–6 sequence.** Tome VII will hold
three works once the Appendix is built (ruling 7: *Expositio Threnorum*, *Expositio Orationis Dominicae*).

**The Tome VII title page** (`site/scripts/build-progress.mjs`, `MEASURED_EXTENTS[7].identity`): *title page "COMMENTARIUS IN EVANGELIUM S. LUCAE —
TOMUS VII"; prolegomena head "PROLEGOMENA IN SEPTIMUM TOMUM"*. The landing page's `VOLUMES` list already gives Vol VII as *Commentarius in Evangelium
S. Lucae*, and Vol VI as *Commentarii in Sacram Scripturam* (the "I" in `TOMES[6]` is ours, not Quaracchi's).

| option | cost |
|---|---|
| **(a) `7: { title: "Book VII: Commentarius in Evangelium S. Lucae", initial: "7" },`** (the title-page wording, matching `VOLUMES`) | **1 code line**; the numbered sequence reads 1–7. Until the Appendix is built, the container holds one work with the same title |
| (b) `"Book VII: Commentarii in Sacram Scripturam II"` (series form, pairing `TOMES[6]`'s "I") | 1 line; **not on the title page**. Vol VII's title page does not say *Commentarii in Sacram Scripturam* |
| (c) No entry until the Appendix (after p. 604) | 0 lines; Luke browses as an "L" row out of sequence for the whole build |

**⭐ Recommendation (mine): (a). It goes live only with whatever deploy Wilson calls. "Approve" = 1 code line.**

---

## 10. The two `low`-confidence manifest rows (`bon-luc-c2-v25-35`, `bon-luc-c2-v36-39`)

**The rows** (`lucam-chunk-manifest.tsv`):

| id | ¶¶ | pp. | opens on | `title_la` (divisio form) | confidence |
|---|---|---|---|---|---|
| `bon-luc-c2-v25-35` | 58–80 | 58–62 | divisio ¶ 58, 58L upper | *Et ecce, homo erat in Ierusalem etc. Postquam descripta est Christi humiliatio secundum Legis praeceptum, hic secundo describitur eius clarificatio per veritatis testimonium.* | low |
| `bon-luc-c2-v36-39` | 81–90 | 62–65 | divisio ¶ 81, 62R top | *Et erat Anna prophetissa etc. Post testimonium sexus virilis sequitur hic testimonium sexus muliebris.* | low |

**Why they were flagged** (`lucam-chunk-manifest-notes.md` § `low` rows): no in-column heading stands between 56L (*sub lege caeremoniali*) and 65L (*sub
lege morali*), 9 pp, so ruling 1b licenses divisio cuts. The editors put the divisions in the MARGIN instead (*Secundo, de Christi clarificatione per
duplex testimonium* · *De testimonio Simeonis dicuntur tria* · *Tertio, de praeconii temperamento tria* · *De testimonio Annae*). The cut at ¶ 58 is firm
(¶ 50's own division names it). The cut at ¶ 81 is a judgement: it is the higher-order joint (the man's testimony, then the woman's), giving **4.4 + 2.7
pp**. Alternatives: (a) no cut, ¶¶ 58–90 as one ~7.1 pp chunk; (b) cut at ¶ 75 (61L, *Et benedixit illis Simeon*), 3.0 + 4.1 pp, a lower-order joint.
The setup sheet (stage-1 coordinator) already kept ¶ 81, said the rows stay `low` until their builder reads pp. 58–65, and said **Wilson may overrule at the
p. 88 gate**.

**Read on the plate here** (`raw/vision/vol7/p-062.png`, 300 dpi, already on disk; cropped, nothing written to the repo):
- **62R opens at the head of the column with *81. Et erat Anna prophetissa etc. Post testimonium sexus virilis sequitur hic testimonium sexus muliebris.***
  Nothing stands above it but the running head. The marginale beside it reads ***De testimonio Annae.***, then *Septiforme de Christo testimonium.*
- **62L's foot closes ¶ 80** (*…secundus vero vitam spiritualem.*) on the last body line of the column, above the footer rule. No heading, no partial
  paragraph carried over the column break.
- So the cut falls **at the start of a numbered paragraph** (ruling 1d), at a **column head**, and at the very joint the marginale names. The sentence that
  would become `title_la` is ¶ 81's first, as the row says.
- ⚠ p. 62 is a shared leaf: its register will split by anchor (62L carries at least nn. 1–6, the anchor of n. 6 at ¶ 80's *Lucae vigesimo secundo*⁶;
  62R's notes are ¶ 81's). The builders split it as usual. Not read further here.

| option | cost |
|---|---|
| **(a) Keep the ¶ 81 cut; leave the rows `low` until their builder confirms pp. 58–65, then promote to `high`** | 0 lines |
| (b) Recut at ¶ 75 (3.0 + 4.1 pp) | 2 manifest rows rewritten (ids → `c2-v25-32` / `c2-v33-39` or as the verses fall), in its own commit (ruling 2); a lower-order joint |
| (c) Merge ¶¶ 58–90 into one ~7.1 pp chunk | 2 rows → 1; under the cap of 8, but loses the man/woman joint the passage itself divides on |

**⭐ Recommendation (mine): (a). The plate confirms the joint is as clean as a headless joint can be. "Approve" = 0 lines.**

---

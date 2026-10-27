/**
 * Pre-build script: reads Latin chunks and translations from the repo,
 * outputs a single content.json that the Next.js app imports at build time.
 *
 * This avoids filesystem reads from parent directories at build time,
 * which fails on Vercel where the deploy root is site/.
 */

import fs from "fs";
import path from "path";
import { fileURLToPath } from "url";

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const SITE_DIR = path.resolve(__dirname, "..");
const REPO_ROOT = path.resolve(SITE_DIR, "..");

// Scan all volume dirs; each dir's files declare their own `book:` in frontmatter.
const VOL_DIRS = ["vol1", "vol2", "vol3", "vol4", "vol5", "vol6"]
  .map((v) => path.join(REPO_ROOT, v))
  .filter((p) => fs.existsSync(p));
const TRANS_DIR = path.join(REPO_ROOT, "translations", "vol1");
const OUT_FILE = path.join(SITE_DIR, "src", "data", "content.json");

function parseFrontmatter(content) {
  const match = content.match(/^---\n([\s\S]*?)\n---\n([\s\S]*)$/);
  if (!match) return { meta: {}, body: content };
  const meta = {};
  for (const line of match[1].split("\n")) {
    const m = line.match(/^(\w+):\s*"?([^"]*)"?\s*$/);
    if (m) meta[m[1]] = m[2];
  }
  return { meta, body: match[2] };
}

// Match a section header at either h2 (##) or h3 (###). Legacy format uses
// ### Latin / ### English / ### Notes in separate files; new unified format
// uses ## Latin / ## English / ## Apparatus / ## Notes in a single file.
function extractSection(body, header) {
  const h3 = body.match(new RegExp(`### ${header}\\n([\\s\\S]*?)(?=\\n### |\\n## |$)`));
  if (h3) return cleanSection(h3[1]);
  const h2 = body.match(new RegExp(`## ${header}\\n([\\s\\S]*?)(?=\\n## |$)`));
  if (h2) return cleanSection(h2[1]);
  return "";
}

// Extract a language block and split off a trailing ### Scholion subsection if
// present. Returns { body, scholion } as normalized strings. Page-break
// comments and [^N] footnote markers are PRESERVED — the client reader now
// handles them.
function extractLanguageBlock(body, header) {
  // Only terminate on known sibling-section headings, not arbitrary `## ` subheadings
  // (e.g. `## Commentarius in Distinctionem V` inside a Latin block).
  const sentinel = `\\n## (?:Latin|English|Apparatus|Notes|Scholion|---)`;
  let raw = "";
  const h2 = body.match(
    new RegExp(`## ${header}\\n([\\s\\S]*?)(?=${sentinel}|$)`)
  );
  if (h2) {
    raw = h2[1];
  } else {
    const h3 = body.match(
      new RegExp(`### ${header}\\n([\\s\\S]*?)(?=\\n### |${sentinel}|$)`)
    );
    if (h3) raw = h3[1];
  }
  if (!raw) return { body: "", scholion: "" };
  const scholionMatch = raw.match(/\n### Scholion\n([\s\S]*)$/);
  const bodyText = scholionMatch ? raw.slice(0, scholionMatch.index) : raw;
  const scholion = scholionMatch ? scholionMatch[1] : "";
  return { body: cleanSection(bodyText), scholion: cleanSection(scholion) };
}

// Parse the ## Apparatus section into structured entries. Each entry is a
// markdown footnote definition of the form:
//   [^1]: **La** — <latin apparatus text><br>
//         **En** — <english translation>
function parseApparatus(body) {
  const app = body.match(/## Apparatus\n([\s\S]*?)(?=\n## |$)/);
  if (!app) return [];
  // Append a sentinel entry so the lookahead reliably terminates the last
  // real entry without needing to match end-of-string.
  // A `---` rule between the last entry and `## Notes` is not part of that entry
  // (ruling (c), Vol VI Ecclesiastes work-close gate, 2026-10-11).
  const text = app[1].replace(/\n\s*-{3,}\s*$/, "") + "\n[^__SENTINEL__]:";
  const entries = [];
  const re = /\[\^([^\]]+)\]:\s*([\s\S]*?)(?=\n\[\^[^\]]+\]:)/g;
  let m;
  while ((m = re.exec(text)) !== null) {
    if (m[1] === "__SENTINEL__") break;
    const id = m[1];
    const content = m[2];
    const laMatch = content.match(/\*\*La\.?\*\*\s*(?:[—–-]\s*)?([\s\S]*?)(?=\*\*En\.?\*\*|$)/);
    const enMatch = content.match(/\*\*En\.?\*\*\s*(?:[—–-]\s*)?([\s\S]*)$/);
    entries.push({
      id,
      la: laMatch ? cleanApparatusEntry(laMatch[1]) : "",
      en: enMatch ? cleanApparatusEntry(enMatch[1]) : "",
    });
  }
  return entries;
}

function cleanApparatusEntry(text) {
  return text
    .replace(/<br>\s*/g, " ")
    .replace(/\s+/g, " ")
    .trim();
}

// Preserves page-break comments and [^N] markers; only normalizes whitespace.
function cleanSection(text) {
  return text.replace(/\n{3,}/g, "\n\n").trim();
}

function parseTranslationFile(content) {
  // Legacy translations/vol1/*.md files use ### English / ### Notes headers.
  const englishMatch = content.match(/### English\n([\s\S]*?)(?=\n### Notes|$)/);
  const notesMatch = content.match(/### Notes\n([\s\S]*)$/);
  return {
    english: englishMatch ? cleanSection(englishMatch[1]) : "",
    notes: notesMatch ? notesMatch[1].trim() : "",
  };
}

// Front-matter chunk types for the Sentences books (vol1–4). These sit BEFORE
// Distinction I and so carry `distinctio: 0`, which the prolegomena skip below
// would otherwise drop — the mechanism that kept all four books' Proemia out of
// the corpus until 2026-08-19. Keep this set tight: the skip is what stops
// vol1/bon-sent-I-proleg.md (a bare 77k-word OCR dump with no `type:`) from
// publishing itself, so only named, deliberately-built types are exempted.
// `praelocutio` is BOOK II ONLY and is deliberately a type of its own, not a
// second `proemium`: Vol II prints TWO display-headed units before the Master's
// text — the PRAELOCUTIO (pp.1–3, which Quaracchi's own p.1 n.1 says remained
// unpublished until their edition) and then the PROOEMIUM (pp.3–6). Folding the
// first into the second would bury the *pauper et tenuis compilator* passage
// inside a chunk titled "Proemium" and would print two "Proemium" entries in one
// division. Do NOT generalize it — like `-sN-` sectio in Vol IV d.49, it exists
// in exactly one place. (2026-08-20)
//
// ★★ `quaestio` IS IN THIS SET AND THAT IS ONLY SAFE BECAUSE OF `declaredType`
// (2026-08-20, at bon-sent-I-proem-q1). BOOK I — alone among the four — prints
// numbered questions in its front matter: QUAESTIONES PROOEMII I–IV, pp. 6–15,
// which Quaracchi themselves cite as `I. Sent. q. 4. Prooemii`. They are real
// quaestio chunks at distinctio 0 and have to publish.
//
// ⛔ THE TRAP, WHICH IS WORTH READING BEFORE TOUCHING THIS SET. The skip below
// kept vol1/bon-sent-I-proleg.md (a bare 77k-word OCR dump) out of the corpus —
// but NOT because the dump failed a type test on its merits. It declares no
// `type:` at all, and `chunkMeta.type` defaults to `"quaestio"`; the dump was
// excluded only because `"quaestio"` happened to be absent from this set.
// Adding `quaestio` to the set while testing the DEFAULTED type would therefore
// have published the dump silently, on the very commit that admitted Book I's
// questions. `declaredType` is the raw frontmatter value and is `undefined`
// when the file declares none, so the guard now tests what it actually means:
// a deliberately-typed chunk. Do not collapse the two back together.
//
// ⚠ `divisio` and `dubia` are deliberately NOT here yet. Book I's front also
// holds a COMMENTARIUS IN PROLOGUM MAGISTRI (pp. 22–25, divisio textus + dubia
// in three parts), but that unit has not been read at the plate and its chunk
// shape is not fixed. Add them when it is built, with titles that say
// "Prologus", not "Proemium" — it comments the Master's prologue, not the
// proemium. Same discipline as `-sN-` sectio: no convention before its case.
const SENTENCES_FRONT_TYPES = new Set([
  "praelocutio",
  "proemium",
  "capitula",
  "littera",
  "quaestio",
  // Book I only: COMMENTARIUS IN PROLOGUM MAGISTRI (pp. 22-25) — Bonaventure's
  // commentary on Lombard's prologue, which stands before d.1 and so carries
  // `distinctio: 0`. Books II-IV have no counterpart (Lombard prefixes a
  // prologue only to Book I).
  "commentary",
]);
const isSentencesFront = (meta) =>
  meta.distinctio === 0 &&
  meta.declaredType !== undefined &&
  SENTENCES_FRONT_TYPES.has(meta.declaredType);

function buildQuestionTitle(meta) {
  // Front matter names itself — there is no "Dist. 0" to breadcrumb against.
  if (isSentencesFront(meta)) {
    if (meta.declaredType === "praelocutio") return "Praelocutio";
    if (meta.declaredType === "proemium") return "Proemium";
    if (meta.declaredType === "capitula") return "Capitula";
    if (meta.declaredType === "littera") return "Textus Magistri";
    if (meta.declaredType === "commentary") return "Prologus, Commentarius";
    // Book I's prooemial questions. Quaracchi's own address for them is
    // `q. N. Prooemii`, so the number is the whole point of the label; a bare
    // "Proemium" would print five identical entries in one division.
    if (meta.declaredType === "quaestio" && meta.quaestio) {
      return `Proemium, Q. ${meta.quaestio}`;
    }
    return "Proemium";
  }
  const parts = [`Dist. ${meta.distinctio}`];
  if (meta.pars !== undefined) parts.push(`Part ${meta.pars}`);
  if (meta.articulus) parts.push(`Art. ${meta.articulus}`);
  if (meta.type === "quaestio" && meta.quaestio) {
    parts.push(`Q. ${meta.quaestio}`);
  } else if (meta.type === "dubia") {
    parts.push("Dubia");
  } else if (meta.type === "divisio") {
    parts.push("Divisio Textus");
  }
  return parts.join(", ");
}

const BOOK_TITLES = {
  1: "Book I: On the Mystery of the Trinity",
  2: "Book II: On the Creation of Things",
  3: "Book III: On the Incarnation of the Word",
  4: "Book IV: On the Sacraments",
};

// ---------------------------------------------------------------------------
// Vol V+ works registry. From Tome V onward each Quaracchi volume holds
// multiple independent works; a chunk declares `work: <slug>` in frontmatter
// and this registry supplies its book id, display metadata, and division
// titles. Book ids continue the integer sequence after the four Sentences
// books. A chunk's `division:` int is the distinctio-equivalent grouping key
// (0 is allowed for a prologue — the vol1–4 "skip distinctio 0" rule does
// not apply to work chunks).
// A tome that holds several independent works gets its own container entry in
// the browse UI, so the Opera Omnia's volume sequence still reads 1-2-3-4-5
// instead of degenerating into one top-level row per work. Tomes I-IV are a
// single work each and need no entry — their Book IS the tome.
const TOMES = {
  5: { title: "Book V: Opuscula Theologica", initial: "5" },
  6: { title: "Book VI: Commentarii in Sacram Scripturam I", initial: "6" },
};

const WORKS = {
  breviloquium: {
    book: 5,
    tome: 5,
    title: "Breviloquium",
    initial: "B",
    divisionLabel: "Parts",
    divisions: {
      0: "Prologus",
      1: "Pars I: De Trinitate Dei",
      2: "Pars II: De creatura mundi",
      3: "Pars III: De corruptela peccati",
      4: "Pars IV: De incarnatione Verbi",
      5: "Pars V: De gratia Spiritus sancti",
      6: "Pars VI: De medicina sacramentali",
      7: "Pars VII: De statu finalis iudicii",
    },
  },
  itinerarium: {
    book: 6,
    tome: 5,
    title: "Itinerarium mentis in Deum",
    initial: "I",
    divisionLabel: "Chapters",
    divisions: {
      0: "Prologus",
      1: "Cap. I: De gradibus ascensionis in Deum et de speculatione ipsius per vestigia eius in universo",
      2: "Cap. II: De speculatione Dei in vestigiis suis in hoc sensibili mundo",
      3: "Cap. III: De speculatione Dei per suam imaginem naturalibus potentiis insignitam",
      4: "Cap. IV: De speculatione Dei in sua imagine donis gratuitis reformata",
      5: "Cap. V: De speculatione divinae unitatis per eius nomen primarium, quod est esse",
      6: "Cap. VI: De speculatione beatissimae Trinitatis in eius nomine, quod est bonum",
      // Settled at bon-itin-c7 (2026-08-14) against the IN-PLACE heading on
      // p. 312 — the only witness that is the text. This is the VOLUME INDEX's
      // form; the capitula table transposes `totaliter` (…per excessum
      // totaliter transeunte) and that reading is recorded at bon-itin-capitula
      // as transmitted text. Do not restore the table's form here.
      7: "Cap. VII: De excessu mentali et mystico, in quo requies datur intellectui, affectu totaliter in Deum per excessum transeunte",
      8: "Scholion",
    },
  },
  // A work that the edition itself does not divide. Quaracchi print it as 26
  // numbered paragraphs of continuous prose with no capitula and no headings,
  // and the volume's own index gives it ONE line with no sub-entries (where the
  // Itinerarium above it is indexed capitulum by capitulum and the Hexaemeron
  // below it collatio by collatio). The `Pars I.`/`Pars 2.` that appear beside
  // the text are MARGINAL glosses — the editors' running outline — and are
  // trimmed to the chunk's Marginalia list like every other gloss. So the work
  // is one chunk, and division 1 is the whole of it. See
  // manual-review/de-reductione-plate-scouting.md for the full argument.
  "de-reductione": {
    book: 7,
    tome: 5,
    title: "De reductione artium ad theologiam",
    initial: "R",
    divisionLabel: "Opusculum",
    divisions: {
      1: "De reductione artium ad theologiam",
    },
  },
  // The largest work in Vol V: 23 collationes + a work-level Scholion, a
  // reportatio. The collatio is the division the edition annotates (COLLATIO I
  // carries apparatus anchor 1) and Quaracchi's own citation unit
  // ("Hexaem. coll. N. n. M"), so it is the chunk unit. NOT the *visiones*:
  // the index describes the collationes as tractationes of four visions, but a
  // grep of the whole work returns ZERO `VISIO` headings in the body — they
  // are a description of the matter, not a printed division (the same class as
  // de-reductione's marginal `Pars`). Division titles are added ONE AT A TIME
  // as each chunk is built, each verified against the IN-PLACE printed subtitle
  // rather than copied out of the volume index — the Itinerarium's Cap. VII
  // title question is why. See manual-review/hexaemeron-pilot-scouting.md.
  hexaemeron: {
    book: 11,
    tome: 5,
    title: "Collationes in Hexaëmeron",
    initial: "H",
    divisionLabel: "Collationes",
    divisions: {
      1: "Collatio I: De qualitatibus in auditoribus divini verbi requisitis et de Christo omnium scientiarum medio",
      2: "Collatio II: De plenitudine sapientiae, in qua sermo terminandus est, scilicet de sapientiae porta et forma",
      3: "Collatio III: De plenitudine intellectus, quatenus est clavis contemplationis per intellectum Verbi increati, incarnati et inspirati",
      4: "Collatio IV: De visione prima, quae est intelligentiae per naturam inditae, tractatio prima",
      5: "Collatio V: De prima visione tractatio secunda, quae est de tertio radio sive de veritate morum, et de sapientia contemplationis",
      6: "Collatio VI: De prima visione tractatio tertia, quae est de prima virtutum causa exemplari, de virtutibus exemplaribus et de cardinalibus inde fluentibus",
      7: "Collatio VII: De prima visione tractatio quarta, quae est de triplici defectu virtutum in philosophis, secundo, de fide sanante, rectificante, ordinante",
      8: "Collatio VIII: De secunda visione, scilicet intelligentiae per fidem sublevatae, tractatio prima, quae agit de altitudine fidei",
      9: "Collatio IX: De secunda visione tractatio secunda, quae est de triplici firmitate fidei",
      10: "Collatio X: De secunda visione tractatio tertia, quae incipit agere de fidei speciositate",
      11: "Collatio XI: De secunda visione tractatio quarta, quae est secunda de speciositate fidei et agit de speculatione Dei trini",
      12: "Collatio XII: De visione secunda tractatio quinta, quae est tertia de speciositate fidei et agit de Deo, ut est exemplar omnium rerum",
      13: "Collatio XIII: De tertia visione, quae est intelligentiae per Scripturam eruditae, tractatio prima, in qua agitur de Scripturae intelligentiis spiritualibus",
      14: "Collatio XIV: De tertia visione tractatio secunda, quae incipit agere de Scripturae figuris sacramentalibus, primo in genere, et deinde de duodecim mysteriis principalibus Christum significantibus",
      15: "Collatio XV: De tertia visione tractatio tertia, quae, continuans praecedentem, primo manifestat, quomodo in duodecim mysteriis principalibus ostendatur etiam antichristus; deinde incipit agere de infinitis caelestibus theoriis germinantibus ex seminibus et fructibus Scripturae",
      16: "Collatio XVI: De tertia visione tractatio quarta, quae prosequitur agere de theoriis ex Scriptura germinantibus, et quidem ratione fructuum in coaptatione temporum, quatenus haec sibi mutuo correspondent; et in specie explicatur comparatio septenarii secundum correspondentiam trium temporum",
      17: "Collatio XVII: De tertia visione tractatio quinta, quae agit de theoriis Scripturae significatis per fructus, scilicet de considerationibus reficientibus intellectum et affectum, et primo quidem de reficientibus intellectum",
      18: "Collatio XVIII: De tertia visione tractatio sexta, quae agit de theoriis Scripturae significatis per fructus, et quidem quatenus reficiunt affectum",
      19: "Collatio XIX: De tertia visione tractatio septima et ultima, quae agit de recta via et ratione, qua fructus Scripturae percipiantur, sive qua per scientiam et sanctitatem ad sapientiam perveniatur",
      20: "Collatio XX: De quarta visione, scilicet intelligentiae per contemplationem suspensae, tractatio prima, quae agit in genere de triplici obiecto huius contemplationis sive de contemplatione caelestis hierarchiae, militantis Ecclesiae et mentis humanae hierarchizatae",
      21: "Collatio XXI: De quarta visione tractatio secunda, quae specialiter agit de primo obiecto intelligentiae per contemplationem suspensae, nempe de consideratione hierarchiae caelestis",
      22: "Collatio XXII: De quarta visione tractatio tertia, quae specialiter agit tum de secundo obiecto huius visionis, nempe de consideratione militantis Ecclesiae, tum de tertio, quod est ipsa anima hierarchizata",
      24: "Scholion",
    },
  },
  // The second reportatio: nine collationes, pp. 457-503, and NO work-level
  // Scholion (the index lists none - a real difference from both the
  // Itinerarium and the Hexaemeron). The collatio is the chunk unit here as
  // there, but it is settled by the volume index and by Quaracchi's citation
  // practice, NOT by an anchor: `COLLATIO I.` on p. 457 carries NO apparatus
  // anchor, read at 10x against p. 329's, which does. Division titles added
  // one at a time, each verified against the in-place printed subtitle.
  // See manual-review/septem-donis-pilot-scouting.md.
  "septem-donis": {
    book: 12,
    tome: 5,
    title: "Collationes de septem donis Spiritus Sancti",
    initial: "D",
    divisionLabel: "Collationes",
    divisions: {
      1: "Collatio I: Praemittitur tractatio de gratia secundum eius ortum, usum et fructum",
      2: "Collatio II: De dono timoris Domini",
      3: "Collatio III: De dono pietatis",
      4: "Collatio IV: De dono scientiae",
      5: "Collatio V: De dono fortitudinis collatio prima",
      6: "Collatio VI: De dono fortitudinis collatio secunda",
      7: "Collatio VII: De dono consilii",
      8: "Collatio VIII: De dono intellectus",
      9: "Collatio IX: De dono sapientiae",
    },
  },
  // The third reportatio: seven collationes, pp. 507-532, and NO work-level
  // Scholion (the index lists none, and the plate confirms it - the same
  // answer as the septem donis). The collatio is the chunk unit, settled by
  // the volume index and by Quaracchi's citation practice, NOT by an anchor:
  // `COLLATIO I.` on p. 507 carries NO apparatus anchor, read at 4x. Two
  // works running now answer this way, so the Hexaemeron's anchored heading
  // is the exception in Vol V, not the rule. Division titles added one at a
  // time, each verified against the in-place printed subtitle.
  // See manual-review/decem-praeceptis-pilot-scouting.md.
  "decem-praeceptis": {
    book: 13,
    tome: 5,
    title: "Collationes de decem praeceptis",
    initial: "P",
    divisionLabel: "Collationes",
    divisions: {
      1: "Collatio I: De quatuor motivis ad observantiam divinorum praeceptorum inducentibus et de decalogo in genere",
      2: "Collatio II: De primo praecepto decalogi in specie",
      3: "Collatio III: De secundo praecepto decalogi",
      4: "Collatio IV: De tertio praecepto decalogi",
      5: "Collatio V: De quarto praecepto",
      6: "Collatio VI: De quinto, sexto et septimo praecepto",
      7: "Collatio VII: De octavo, nono et decimo praecepto",
    },
  },
  // See manual-review/scientia-christi-pilot-scouting.md.
  "scientia-christi": {
    book: 8,
    tome: 5,
    title: "Quaestiones disputatae de scientia Christi",
    initial: "Q",
    divisionLabel: "Quaestiones",
    divisions: {
      1: "Quaestio I: Utrum scientia Christi, secundum quod est Verbum, actu se extendat ad infinita",
      2: "Quaestio II: Utrum Deus res cognoscat per similitudines rerum, an per earum essentiam",
      3: "Quaestio III: Utrum Deus res cognoscat per similitudines realiter differentes",
      4: "Quaestio IV: Utrum quidquid a nobis certitudinaliter cognoscitur cognoscatur in ipsis rationibus aeternis",
      5: "Quaestio V: Utrum anima Christi fuerit sapiens tantum sapientia increata, an etiam sapientia creata cum increata",
      6: "Quaestio VI: Utrum anima Christi comprehendat ipsam sapientiam increatam",
      7: "Quaestio VII: Utrum anima Christi comprehendat omnia, quae comprehendit sapientia increata",
    },
  },
  // See manual-review/mysterio-trinitatis-pilot-scouting.md.
  // ⚠ The chunk here is finer than the division: divisions are the eight
  // quaestiones, and fourteen of the fifteen chunks are articuli within them.
  "mysterio-trinitatis": {
    book: 9,
    tome: 5,
    title: "Quaestiones disputatae de mysterio Trinitatis",
    initial: "Q",
    divisionLabel: "Quaestiones",
    divisions: {
      1: "Quaestio I: De certitudine, qua existentia Dei cognoscitur, et de fide, qua eiusdem Trinitas creditur",
      2: "Quaestio II: Utrum possit simul stare trinitas personarum cum naturae unitate",
      3: "Quaestio III: Utrum simul stent trinitas et summa simplicitas",
      4: "Quaestio IV: Utrum trinitas stet cum summa infinitate",
      5: "Quaestio V: Utrum personarum trinitas simul stet cum summa aeternitate",
      6: "Quaestio VI: Utrum trinitas possit stare cum summa immutabilitate",
      7: "Quaestio VII: Utrum possit stare trinitas cum summa necessitate",
      8: "Quaestio VIII: Utrum possit simul stare trinitas cum summa primitate",
    },
  },
  // See manual-review/perfectione-evangelica-pilot-scouting.md.
  // Mixed division shape: Quaestio I is undivided (one chunk, no `articulus`);
  // Quaestiones II-IV divide into three articuli each.
  "perfectione-evangelica": {
    book: 10,
    tome: 5,
    title: "Quaestiones disputatae de perfectione evangelica",
    initial: "Q",
    divisionLabel: "Quaestiones",
    divisions: {
      1: "Quaestio I: De humilitate quoad actum ipsius, utrum scilicet christianae perfectionis sit se ipsum vilificare pro Christo",
      2: "Quaestio II: De paupertate",
      3: "Quaestio III: De continentia",
      4: "Quaestio IV: De obedientia",
    },
  },
  // See manual-review/sermones-selecti-pilot-scouting.md.
  // The LAST work in Tome V. English title: "Selected Sermons on Theological
  // Matters." FOUR sermons plus one annexed Tractatus de plantatione Paradisi
  // = FIVE divisions, not "dozens of short pieces" (the work map was wrong;
  // corrected at the mini-pilot, 2026-09-18). Division 5 is the Tractatus and
  // carries `type: tractatus`, which buildWorkChunkTitle handles type-first;
  // divisions 1-4 carry `type: sermo`. Divisions are added one at a time, each
  // subtitle verified in place on the plate.
  "sermones-selecti": {
    book: 14,
    tome: 5,
    title: "Sermones selecti de rebus theologicis",
    initial: "S",
    divisionLabel: "Sermones",
    divisions: {
      1: "Sermo I: De triplici testimonio sanctissimae Trinitatis",
      2: "Sermo II: De regno Dei descripto in parabolis evangelicis",
      3: "Sermo III: De sanctissimo corpore Christi",
      4: "Sermo IV: Christus unus omnium magister",
      5: "Tractatus de plantatione Paradisi",
    },
  },
  // ---- Tome VI ----------------------------------------------------------
  // The first Scripture commentary. Its chunk is FINER than its division:
  // division is the capitulum, the chunk is the verse-pericope the volume
  // index itself lists (`Vers. 2-7`), which is also Quaracchi's citation unit
  // (`Comment. in Eccle. 1, 1`). Pericopes carry `verses:` in frontmatter and
  // buildWorkChunkTitle renders "Cap. N, Vers. a-b". Divisions go in one at a
  // time; a capitulum heading is a bare `CAPITULUM N.` with no subtitle, so
  // there is no in-place subtitle to verify against the index.
  ecclesiasten: {
    book: 15,
    tome: 6,
    title: "Commentarius in Ecclesiasten",
    initial: "E",
    divisionLabel: "Capitula",
    divisions: {
      0: "Prooemium",
      1: "Capitulum I",
      // ⚠ 2 was never added when Capitulum II landed, so its four chunks have
      // been rendering the arabic FALLBACK (`Capitulum 2`) beside division 1's
      // roman. Both are supplied here; each display heading was read in place
      // on the plate (`CAPITULUM II.` at bon-eccl-c2-v1-3 p. 20, `CAPITULUM
      // III.` at bon-eccl-c3-v1 p. 28) and neither carries a subtitle.
      2: "Capitulum II",
      3: "Capitulum III",
      // `CAPITULUM IV.` read in place on the plate at bon-eccl-c3-v16-22's last
      // leaf (p. 37, full measure, ~39 % down the leaf, no subtitle — the next
      // line is the divisio heading `Secundo, de vanitate malitiae in subditis…`).
      4: "Capitulum IV",
      // `CAPITULUM V.` read in place on the plate at bon-eccl-c5-v1-8 (p. 42,
      // full measure, ~73 % down the leaf, no subtitle). ⚠ The raw OCR DROPS
      // the heading entirely. Per ruling 15 that chunk opens on Eccle. 4:17.
      5: "Capitulum V",
      // `CAPITULUM VI.` read in place on the plate at bon-eccl-c6-v1-7 (p. 50,
      // full measure, centred at the HEAD of the leaf under the running head,
      // no subtitle and no anchor — the next line is the class-3 heading
      // `Tertio detestatur avaritiam…`). ⚠ The raw OCR DROPS the heading, as
      // it dropped CAPITULUM V.
      6: "Capitulum VI",
      // `CAPITULUM VII.` read in place on the plate at bon-eccl-c7-v1 (p. 53,
      // full measure, centred, ~44 % down the leaf below c6-v8-11's close, no
      // subtitle and no anchor — read at 2.5x; the next line is `(Vers. 1.)`).
      // The raw keeps it this time, garbled `Capitulum  VH.` (L11446).
      7: "Capitulum VII",
      // `CAPITULUM VIII.` read in place on the plate at bon-eccl-c8-v1-8 (p. 64,
      // full measure, centred, ~47 % down the leaf below c7-v24-30's close, no
      // subtitle and no anchor — read at 2.5x; the next line is the class-3
      // heading `Secundo, contra inventam concupiscentiam datur remedium
      // sapientiae…`). The raw keeps it (`Capitulum  VIII.`, L13113). Per
      // ruling 16 the chunk's first exposition is Eccle. 7:30b.
      8: "Capitulum VIII",
      // `CAPITULUM IX.` read in place on the plate at bon-eccl-c9-v1-3 (p. 71,
      // full measure, centred, ~35 % down the leaf below c8-v16-17's close, no
      // subtitle and no anchor). The raw OMITS it (L14157-14158 blank). The
      // chunk's first exposition is the second member of c8-v16-17's p. 71
      // subdivisio (ruling-16 shape).
      9: "Capitulum IX",
      // `CAPITULUM X.` read in place on the plate at bon-eccl-c10-v1-3 (p. 79,
      // full measure, centred, ~51 % down the leaf below c9-v13-18's close, no
      // subtitle and no anchor). The raw OMITS it (L15344-15345 blank). The
      // chunk's first expositions complete c9-v13-18's second part (ruling-16
      // shape).
      10: "Capitulum X",
      // `CAPITULUM XI.` read in place on the plate at bon-eccl-c11-v1-10 (p. 87,
      // full measure, centred, ~0.61 of the leaf below c10-v12-20's close, no
      // subtitle and no anchor; the raw KEEPS it, L16562). Below it the
      // small-bold `Secundo datur remedium contra vanitatem securitatis ortam
      // ex defectu retributionis iustitiae.` (the chunk's title_la).
      11: "Capitulum XI",
      // `CAPITULUM XII.` read in place on the plate at bon-eccl-c12-v1-14 (p. 92,
      // full measure, centred, ~0.11 of the leaf below two lines of Cap. XI,
      // no subtitle and no anchor; the raw keeps it, L17198). Below it the
      // italic in-column `Partis tertiae membrum II.` and `Art. 1. Poena, quae
      // est pura afflictio, describitur generaliter.` (the chunk's title_la).
      12: "Capitulum XII",
      // The work-level `SCHOLION.` read in place on the plate at bon-eccl-scholion
      // (p. 99, full measure, letter-spaced, ~0.41 of the leaf below the
      // `EXPLICIT ECCLESIASTES` colophon; no anchor). The next division after the
      // last capitulum, on the bon-itin-scholion (8) / bon-hex-scholion (24)
      // precedent; the chunk title is caught type-first ("Scholion").
      13: "Scholion",
      // The four `SCHEMA I.`–`IV.` read in place on the plates at
      // bon-eccl-schemata (pp. 100–103; Schema I upright, II–IV each under a
      // part-title set rotated up the left margin). Ruling 19: ONE chunk, the
      // next division after the Scholion; caught type-first ("Schemata").
      14: "Schemata",
    },
  },
  // The second Scripture commentary (Sapientiae mini-pilot, rulings 27–35,
  // manual-review/vol6-pilot-setup.md; evidence sapientiae-pilot-scouting.md).
  // English title "Commentary on the Book of Wisdom" (ruling 32). Unlike
  // Ecclesiastes, the volume index gives each capitulum ONE line (`Vers. 1-N`)
  // and lists no Quaestiones, so the chunk IS the capitulum (ruling 27):
  // `bon-sap-c{1..19}`, `verses: "1-N"`, rendered "Cap. N, Vers. 1-N" by the
  // ecclesiasten branch of buildWorkChunkTitle. Division 0 holds two chunks
  // (ruling 28): `bon-sap-prooem` (section 1, type prooemium) and
  // `bon-sap-prol` (section 2, type expositio). The printed `PARS I.` (p. 110)
  // and `PARS II.` (p. 144) are headings inside c1 and c6, with NO `pars:`
  // field (ruling 29). Planned: 20 Scholion, 21 Schemata (ruling 30). Each
  // capitulum adds its own line after its heading is read in place.
  sapientiam: {
    book: 16,
    tome: 6,
    title: "Commentarius in librum Sapientiae",
    initial: "S",
    divisionLabel: "Capitula",
    divisions: {
      // `PROOEMIUM / COMMENTARII IN SAPIENTIAM` read in place on p. 107 (full
      // measure, unanchored) at bon-sap-prooem.
      0: "Prooemium",
      // `CAPITULUM I.` read in place on the plate at bon-sap-c1 (p. 110, full
      // measure, centred, ~0.61 of the leaf, no subtitle and no anchor; the
      // raw keeps it, L19411). Above it on the same leaf stand the
      // COMMENTARIUS stack, DIVISIO GENERALIS and `PARS I. EXHORTATIO AD
      // IUSTITIAM.` with its subdivisiones — headings inside c1, no `pars:`
      // field (ruling 29). The chunk runs to Vers. 16, before `CAPITULUM II.`
      // on p. 118, though its `verses` keeps the index label "1-15".
      1: "Capitulum I",
      // `CAPITULUM II.` read in place at bon-sap-c2 (p. 118, full measure,
      // centred small capitals, ~0.28 of the leaf, no subtitle and no anchor;
      // the raw DROPS it). The chunk runs to Vers. 25, above `CAPITULUM III.`
      // on p. 125.
      2: "Capitulum II",
      // `CAPITULUM III.` read in place at bon-sap-c3 (p. 125, full measure,
      // centred small capitals, ~0.23 of the leaf, no subtitle and no anchor;
      // the raw DROPS it). The chunk runs to Vers. 19, above `CAPITULUM IV.`
      // on p. 131.
      3: "Capitulum III",
      // `CAPITULUM IV.` read in place at bon-sap-c4 (p. 131, full measure,
      // centred small capitals, ~0.39 of the leaf, no subtitle and no anchor;
      // the raw DROPS it). The chunk runs to Vers. 20, above `CAPITULUM V.`
      // on p. 137.
      4: "Capitulum IV",
      // `CAPITULUM V.` read in place at bon-sap-c5 (p. 137, full measure,
      // centred small capitals, ~0.10 of the leaf, no subtitle and no anchor;
      // the raw keeps it here). The chunk runs to Vers. 24, above
      // `CAPITULUM VI.` on p. 144.
      5: "Capitulum V",
      // `CAPITULUM VI.` read in place at bon-sap-c6 (p. 144, full measure,
      // centred small capitals, ~0.37 of the leaf, no subtitle and no anchor;
      // the raw DROPS it). Below it stand Sap. 6:1 (Melior est sapientia) and
      // then the `PARS II. EXHORTATIO AD SAPIENTIAM.` heading: Part II opens
      // INSIDE this chapter, transcribed as a heading, no `pars:` field
      // (ruling 29). The chunk runs to Vers. 27, above `CAPITULUM VII.` on
      // p. 151.
      6: "Capitulum VI",
      // Capitulum VII — read in place on p. 151 (full measure, centred small
      // capitals, ~0.17 of the leaf, no subtitle, no anchor). Below it the
      // roman `Secundo sumit rationem exhortandi ad sapientiam a suo exemplo.`
      // (Part II's second ratio, governing cc. VII-IX) and the italic
      // `Primo ostendit, qualiter sapientiam acceperit.` (this chapter, the
      // title_la, ruling 36). The chunk runs to Vers. 30, above `CAPITULUM
      // VIII.` on p. 159.
      7: "Capitulum VII",
      // `CAPITULUM VIII.` read in place on the plate at bon-sap-c8 (p. 159,
      // full measure, centred small capitals, ~0.65 of the leaf below Cap.
      // VII's close, no subtitle, no anchor). Below it the centred italic
      // `Secundo ostendit tripliciter, quantum amaverit sapientiam` (no final
      // point, read at 3x) — the second member of c7's ratio, governing exactly
      // this chapter (the title_la, ruling 36). The chunk runs to Vers. 21,
      // above `CAPITULUM IX.` on p. 166 (~0.48 of the leaf).
      8: "Capitulum VIII",
      // `CAPITULUM IX.` read in place on the plate at bon-sap-c9 (p. 166, full
      // measure, centred small capitals, ~0.43 of the leaf below Cap. VIII's
      // close, no subtitle, no anchor; the raw DROPS it). Below it the centred
      // italic `Tertio ostendit, quam devote sapientiam a Deo petierit.` — the
      // third member of c7's ratio, governing exactly this chapter (title_la,
      // ruling 36). The chunk runs to Vers. 19, above `CAPITULUM X.` on p. 171
      // (~0.25 of the leaf). The index's "174" for Cap. X is a pilot misreading
      // of a printed 171 (the 1/4 class); see the chunk's Notes.
      9: "Capitulum IX",
      // `CAPITULUM X.` read in place on the plate at bon-sap-c10 (p. 171, full
      // measure, centred small capitals, ~0.25 of the leaf below Cap. IX's
      // close, no subtitle, no anchor). Below it the divisio *Haec illam etc.*
      // and then the centred italic `Tertio hortatur ad sapientiam acquirendam
      // per rationes sumtas ab eius effectibus, et primo a beneficiis
      // pertinentibus ad amicorum Dei promotionem.` — the third ratio of Part II
      // (cc. X–XIX) fused in ONE heading with its first member, which governs
      // exactly this chapter; no lower heading does (title_la, ruling 36, taken
      // whole — see the chunk's Notes). The chunk runs to Vers. 21, above
      // `CAPITULUM XI.` on p. 177 (~0.40 of the leaf); the index's 177 for
      // Cap. XI re-read on the plate and right.
      10: "Capitulum X",
      // `CAPITULUM XI.` read in place on the plate at bon-sap-c11 (p. 177, full
      // measure, centred small capitals, ~0.40 of the leaf below Cap. X's
      // close, no subtitle, no anchor). Below it three headings descend: the
      // roman `De beneficiis pertinentibus principaliter ad adversariorum
      // punitionem.` (cc. XI–XIX), the italic `Primo, de punitione per poenas
      // leviores agitur dupliciter.` (cc. XI–XII), and the small bold `Primo, de
      // punitione Aegyptiorum propter duplex peccatum, primo propter
      // depressionem iniustam.` — whose first clause covers exactly this chapter
      // (its sibling `Secundo, de punitione Chananaeorum…` heads Cap. XII) and
      // whose second names Vers. 1-15 (sibling `Secundo, … propter
      // idololatriam.` on p. 180): the title_la, ruling 36, taken whole. The
      // chunk runs to Vers. 27 (index label 1-26), above `CAPITULUM XII.` on
      // p. 184 (~0.36 of the leaf); the index's 184 read on the plate and right.
      11: "Capitulum XI",
      // `CAPITULUM XII.` read in place on the plate at bon-sap-c12 (p. 184, full
      // measure, centred small capitals, ~0.36 of the leaf below Cap. XI's
      // close, no subtitle, no anchor). Below it the small bold `Secundo, de
      // punitione Chananaeorum et Amorrhaeorum.` — the second member of c11's
      // italic `Primo, de punitione per poenas leviores agitur dupliciter.` (cc.
      // XI–XII), covering exactly this chapter: the title_la, ruling 36, no
      // descent, not fused. The chunk runs to Vers. 26 (index label 1-26, last
      // address on the plate `(Vers. 26.)`), above `CAPITULUM XIII.` on p. 191
      // (~0.58 of the leaf) — the index prints 192 for Cap. XIII, the page on
      // which its `(Vers. 1.)` first stands; the heading is on 191.
      12: "Capitulum XII",
      // `CAPITULUM XIII.` read in place on the plate at bon-sap-c13 (p. 191, full
      // measure, centred small capitals, ~0.58 of the leaf below Cap. XII's
      // close, no subtitle, no anchor). Below it, descended twice under ruling
      // 36: the italic `Secundo, de punitione per poenas graviores…` (cc.
      // XIII–XIX) and the small bold `Primo determinatur de demerito culpae
      // tripliciter.` (cc. XIII–XV) both govern runs; the small bold `Primo
      // agitur de errore idololatrantium.` covers exactly this chapter (sibling
      // `Secundo agitur de detestatione idolorum quadrupliciter.` heads Cap. XIV),
      // plain, not fused: the title_la. The chunk runs to Vers. 19 (= index
      // label), above `CAPITULUM XIV.` on p. 196 (~0.21) — the index's 196 is
      // the page of XIV's heading AND its `(Vers. 1.)` (ruling 55 confirmed).
      13: "Capitulum XIII",
      // bon-sap-c14 (2026-10-16): CAPITULUM XIV. read in place on p. 196
      // (~0.21, full measure, no subtitle, no anchor); title_la = the small
      // bold `Secundo agitur de detestatione idolorum quadrupliciter.` directly
      // below it (covers exactly Cap. XIV; plain, no descent). Runs to Vers. 31
      // (= index label) on p. 203; CAPITULUM XV. heads p. 204.
      14: "Capitulum XIV",
      // bon-sap-c15 (2026-10-16): CAPITULUM XV. read in place at the head of
      // p. 204 (full measure, no subtitle, no anchor); title_la = the small
      // bold `Tertio agitur de commendatione veri Dei.` directly below it
      // (covers exactly Cap. XV; plain, no descent). Runs to Vers. 19 (= index
      // label) at the head of p. 209's right column; CAPITULUM XVI. stands
      // mid-leaf on p. 209 (the index's 209: heading and Vers. 1 both there).
      15: "Capitulum XV",
      // Capitulum XVI (bon-sap-c16): heading read in place mid-leaf on p. 209
      // (~0.37, full measure, no subtitle, no anchor). title_la descends TWICE
      // (ruling 36): past the italic run `Secundo determinatur de supplicio
      // poenae culpabilium.` (XVI-XIX) and the bold `Primo agitur de duabus
      // poenis antecedentibus mortem.` (XVI-XVII) to `De poena sensus duplici.`
      // (exactly XVI; plain). Runs to Vers. 29 (= index label) at the head of
      // p. 217; CAPITULUM XVII. stands mid-leaf on p. 217 (the index's 217:
      // heading and Vers. 1 both there).
      16: "Capitulum XVI",
      // bon-sap-c17: CAPITULUM XVII. read in place mid-leaf on p. 217 (full measure,
      // no subtitle); the chapter runs to p. 221, where CAPITULUM XVIII. stands
      // mid-leaf with its Vers. 1 on p. 222 (ruling 55: the index's 222).
      17: "Capitulum XVII",
      // bon-sap-c18: CAPITULUM XVIII. read in place mid-leaf on p. 221 (full measure,
      // no subtitle); its Vers. 1 is on p. 222 (ruling 55: the index's 222). The
      // chapter runs to p. 228, where CAPITULUM XIX. stands mid-leaf with its
      // Vers. 1 on the same leaf (the index's 228).
      18: "Capitulum XVIII",
      // bon-sap-c19: CAPITULUM XIX. read in place mid-leaf on p. 228 (full measure,
      // no subtitle, no anchor), its Vers. 1 on the same leaf. The work's last
      // chapter runs to p. 233, closing on the unanchored EXPLICIT POSTILLA IN
      // LIBRUM SAPIENTIAE., above the Scholion (division 20).
      19: "Capitulum XIX",
      // bon-sap-scholion (ruling 30): the full-measure display heading SCHOLION.
      // read in place on p. 233 (~0.46 of the leaf), below the Explicit; six
      // lines in two columns, unanchored. Its own chunk; the chunk title is
      // caught type-first ("Scholion"). Schema I. opens p. 234 (division 21).
      20: "Scholion",
      // bon-sap-schemata (ruling 30): Schema I. read in place at the head of
      // p. 234 and Schema II. at the head of p. 235 — two upright bracket-trees
      // under part-titles rotated up the left margin. ONE chunk, two sections;
      // the chunk title is caught type-first ("Schemata"). The work ends here:
      // p. 236 blank, p. 237 the Commentarius in Evangelium S. Ioannis half-title.
      21: "Schemata",
    },
  },
  // The third Scripture commentary (Ioannem mini-pilot, rulings 69–77,
  // manual-review/vol6-pilot-setup.md; evidence ioannem-pilot-scouting.md).
  // English title "Commentary on the Gospel of John" (ruling 74); the registry
  // title is the half-title form (index: in Evangelium Ioannis; running head:
  // in Ioannem). The index shape is Ecclesiastes' (verse-pericopes, each with
  // its Quaestiones), so the chunk is the pericope (ruling 69):
  // `bon-ioan-c{N}-v{a}-{b}`, `verses: "a-b"`, `type: pericope`, rendered
  // "Cap. N, Vers. a-b" by the ecclesiasten branch of buildWorkChunkTitle.
  // Each chunk also records `paragraphs: "a-b"` (ruling 73) — Quaracchi cites
  // this work by per-chapter paragraph number. Division 0 holds two chunks
  // (ruling 70): `bon-ioan-prooem` (section 1, type prooemium, pp. 239–244)
  // and `bon-ioan-prol` (section 2, type expositio, pp. 244–246). The printed
  // `PARS I.` (p. 246) and `PARS II.` (p. 250) are headings inside c1-v1-2 and
  // c1-v6-8, NO `pars:` field (ruling 71). Planned: 1–21 Capitula, 22 Scholion,
  // 23 Schemata (ruling 72). Each capitulum adds its own line after its
  // heading is read in place.
  ioannem: {
    book: 17,
    tome: 6,
    title: "Commentarius in Evangelium S. Ioannis",
    initial: "I",
    divisionLabel: "Capitula",
    divisions: {
      // `PROOEMIUM / COMMENTARII IN IOANNEM¹` read in place on p. 239 (full
      // measure, ornament below) at bon-ioan-prooem — ANCHORED: n. 1 carries
      // the whole reportatio Sermo ... quando incepit Ioannem (ruling 70).
      0: "Prooemium",
      // `CAPITULUM I.` read in place on p. 246 at bon-ioan-c1-v1-2: full-measure
      // centred small capitals under the COMMENTARIUS / IN EVANGELIUM IOANNIS.
      // stack, above ¶ 1 (the raw drops the heading). `PARS. I.` (printed with a
      // point after PARS) stands inside that chunk (ruling 71).
      1: "Capitulum I",
      // `CAPITULUM II.` read in place on p. 269 at bon-ioan-c2-v1-11: centred
      // small capitals at ~0.12 of the leaf, below Cap. I's last four lines,
      // with NO heading beneath it (ruling 79: the chunk is titled from the
      // divisio's first sentence). Unanchored.
      2: "Capitulum II",
      // `CAPITULUM III.` read in place on p. 278 at bon-ioan-c3-v1-2: centred
      // small capitals at the head of the leaf, under the running head, with
      // NO heading beneath it (ruling 79(a)). The raw has NO line for it --
      // only the running head `COMMENT. IN lOANNEM C. III.`. Unanchored.
      3: "Capitulum III",
      // `CAPITULUM IV.` read in place on p. 289 at bon-ioan-c4-v1-6: full-measure
      // centred small capitals MID-LEAF at ~0.38, below Cap. III's last Quaestio,
      // with the small bold heading `Tertia manifestatio, quae facta est
      // Samaritanis.` set in the LEFT column beneath it (ruling 79(b): the chunk
      // is titled from that heading). Both unanchored.
      4: "Capitulum IV",
      // `CAPITULUM V.` read in place on p. 303 at bon-ioan-c5-v1-9: full-measure
      // centred small capitals MID-LEAF at ~0.34, below Cap. IV's last Quaestio,
      // with TWO stacked small bold headings in the LEFT column: `Secundo, de
      // manifestatione Verbi quoad conditiones a parte ipsius Verbi manifestati.`
      // over ¶ 1 and `Primo, Filius Dei se manifestat curatorem.` over ¶ 2
      // (ruling 79(b): the chunk is titled from the lowest). All unanchored.
      5: "Capitulum V",
      // `CAPITULUM VI.` read in place on p. 318 at bon-ioan-c6-v1-9: full-measure
      // centred small capitals MID-LEAF at ~0.36, below Cap. V's last Quaestio,
      // with TWO stacked small bold headings in the LEFT column: `Secundo, Filius
      // Dei se manifestat conservatorem.` over ¶ 1 and `Primo se manifestat
      // conservatorem corporum.` inside ¶ 1, after its first paragraph (ruling
      // 79(b): the chunk is titled from the lowest). All unanchored.
      6: "Capitulum VI",
      // `CAPITULUM VII.` read in place on p. 338 at bon-ioan-c7-v1-13: full-measure
      // centred small capitals MID-LEAF at ~0.53, below Cap. VI's last Quaestio
      // (the index's `Capitulum VII … 339` is the page of `(Vers. 1.)`, one leaf
      // late, ruling 82(d)), with THREE stacked small bold headings in the LEFT
      // column: `Tertio, Filius Dei se manifestat directorem et illustratorem
      // tripliciter.` over ¶ 1 (p. 338), and inside ¶ 1 on p. 339 `Primo se
      // ostendit lucem et directorem verbo doctrinae.` and `Pars prima de
      // Doctoris propalatione agit dupliciter.` (ruling 79(b): the chunk is
      // titled from the lowest). All unanchored.
      7: "Capitulum VII",
      // `CAPITULUM VIII.` read in place on p. 353 at bon-ioan-c8-v1-11: full-measure
      // centred small capitals MID-LEAF at ~0.32, below Cap. VII's Quaest. IV
      // (…ideo erraverunt.), with NO heading beneath it (ruling 79(a): the chunk
      // is titled from ¶ 1's first sentence after the lemma). Unanchored. The
      // index (*Capitulum VIII … Vers. 1-11 … 353*) agrees.
      8: "Capitulum VIII",
      // `CAPITULUM IX.` read in place on p. 372 at bon-ioan-c9-v1-11: full-measure
      // centred small capitals MID-LEAF at ~0.22, below Cap. VIII's Quaest. IV
      // (LEFT) and Quaest. V (RIGHT, …de secundo habetur hic.), with TWO stacked
      // small bold headings in the LEFT column: `Secundo, Filius Dei se ostendit
      // lucem et directorem miraculo potentiae.` over ¶ 1, and inside ¶ 1 `In
      // parte prima insinuatur mirabilis caeci illuminatio.` (ruling 79(b): the
      // chunk is titled from the lowest). All unanchored. The raw drops the
      // capitulum heading. The index (*Capitulum IX … Vers. 1-11 … 372*) agrees.
      9: "Capitulum IX",
    },
  },
};

function buildWorkChunkTitle(meta) {
  // Type-first: standalone transmitted capitula tables and work-level scholia
  // (Itinerarium shape) name themselves regardless of division.
  if (meta.type === "capitula") return "Capitula";
  if (meta.type === "scholion") return "Scholion";
  // The Ecclesiastes Schemata (Vol VI ruling 19: one chunk, four sections).
  if (meta.type === "schemata") return "Schemata";
  // An undivided work is one chunk and names itself (De reductione).
  if (meta.type === "opusculum") return "Opusculum";
  // The Sermones selecti's fifth division is an annexed tractatulus, not a
  // sermon; it names itself by type, like the capitula/scholion/opusculum
  // cases above, so the Sermo branch below never has to special-case it.
  if (meta.type === "tractatus") return "Tractatus";
  // The Ecclesiastes Prooemium is a division-0 chunk that is NOT a prologue:
  // the `division === 0` branch below would name it "Prologus", so it names
  // itself by type first, like the cases above. (Jerome's Prologus + its
  // Expositio, the work's other division-0 chunk, is a separate decision.)
  if (meta.type === "prooemium") return "Prooemium";
  // Jerome's Prologus + Bonaventure's Expositio of it, the work's other
  // division-0 chunk. It cannot take `type: prologus`: eight Vol V chunks
  // already carry that value and six of them (bon-brev-prol-s1..s6) depend on
  // the `division === 0` branch below rendering "Prologus, §N", which a
  // type-first prologus branch would flatten. The type names Bonaventure's own
  // unit, an expositio, as the other type values name his (capitulum, collatio,
  // quaestio, sermo, tractatus, prooemium); Jerome's prologue is the
  // transmitted text expounded, carried with it.
  if (meta.type === "expositio") return "Expositio prologi";
  if (meta.division === 0) {
    return meta.section ? `Prologus, §${meta.section}` : "Prologus";
  }
  // Flat works (no partes): division IS the capitulum (Itinerarium).
  if (meta.workSlug === "itinerarium") return `Cap. ${meta.division}`;
  // Flat works whose division is the collatio (Hexaemeron, and the two
  // Collationes sets when they land).
  if (
    meta.workSlug === "hexaemeron" ||
    meta.workSlug === "septem-donis" ||
    meta.workSlug === "decem-praeceptis"
  )
    return `Coll. ${meta.division}`;
  // Flat works whose division is the quaestio (the three quaestiones disputatae).
  if (meta.workSlug === "scientia-christi") return `Quaest. ${meta.division}`;
  // Flat work whose division is the sermon (Sermones selecti). Division 5, the
  // annexed Tractatus, is caught type-first above and never reaches here.
  if (meta.workSlug === "sermones-selecti") return `Sermo ${meta.division}`;
  // The de mysterio Trinitatis divides its quaestiones into articuli, so its
  // chunk is finer than its division: "Quaest. 1, Art. 1". Quaestio VIII is
  // undivided and carries no `articulus`, so it names itself "Quaest. 8".
  // De perfectione evangelica has the same shape (its undivided Quaestio I
  // is "Quaest. 1").
  if (
    meta.workSlug === "mysterio-trinitatis" ||
    meta.workSlug === "perfectione-evangelica"
  )
    return meta.articulus
      ? `Quaest. ${meta.division}, Art. ${meta.articulus}`
      : `Quaest. ${meta.division}`;
  // The Scripture commentaries: division is the capitulum and the chunk is the
  // verse-pericope inside it, so the chunk title needs both. `verses` is the
  // index's own form ("1", "2-7"); a pericope always has one, so its absence
  // means a non-pericope chunk (Scholion, Schemata) caught type-first above.
  // The Commentarius in librum Sapientiae has the same shape (ruling 33), its
  // pericope being the whole chapter ("Cap. 3, Vers. 1-19").
  if (
    meta.workSlug === "ecclesiasten" ||
    meta.workSlug === "sapientiam" ||
    meta.workSlug === "ioannem"
  ) {
    return meta.verses
      ? `Cap. ${meta.division}, Vers. ${meta.verses}`
      : `Cap. ${meta.division}`;
  }
  // Breviloquium-style: "Pars 3, Cap. 4".
  const parts = [`Pars ${meta.division}`];
  if (meta.capitulum) parts.push(`Cap. ${meta.capitulum}`);
  return parts.join(", ");
}

// Main
const latinFiles = VOL_DIRS.flatMap((dir) =>
  fs
    .readdirSync(dir)
    .filter((f) => f.endsWith(".md"))
    .map((f) => ({ file: f, dir }))
);
const chunks = [];

for (const { file, dir } of latinFiles) {
  const content = fs.readFileSync(path.join(dir, file), "utf-8");
  const { meta, body } = parseFrontmatter(content);
  if (!meta.id) continue;

  const latinBlock = extractLanguageBlock(body, "Latin");
  const latin = latinBlock.body;
  const latinScholion = latinBlock.scholion;

  // English lookup:
  // 1. New unified format — Latin and English live in the same file at h2.
  //    Extract the English section directly; accept only if it's meaningful
  //    content (> 100 chars), not the "[Translation pending]" placeholder.
  // 2. Legacy split format — English lives in a parallel file under
  //    translations/vol1/ with ### English / ### Notes headers.
  let english = "";
  let englishScholion = "";
  let notes = "";
  const englishBlock = extractLanguageBlock(body, "English");
  if (
    englishBlock.body.length > 100 &&
    !/^\[translation pending/i.test(englishBlock.body)
  ) {
    english = englishBlock.body;
    englishScholion = englishBlock.scholion;
    notes = extractSection(body, "Notes");
  } else {
    const transFile = path.join(TRANS_DIR, file);
    if (fs.existsSync(transFile)) {
      const parsed = parseTranslationFile(fs.readFileSync(transFile, "utf-8"));
      if (parsed.english.length > 100) {
        english = parsed.english;
        notes = parsed.notes;
      }
    }
  }

  const apparatus = parseApparatus(body);

  const work = meta.work ? WORKS[meta.work] : undefined;
  if (meta.work && !work) {
    console.warn(`SKIP ${meta.id}: unknown work slug "${meta.work}" (not in WORKS registry)`);
    continue;
  }

  const chunkMeta = {
    id: meta.id,
    volume: parseInt(meta.volume) || 1,
    // Work chunks derive their book id from the registry — the frontmatter
    // carries `work:`, not `book:`, so there is a single source of truth.
    book: work ? work.book : parseInt(meta.book) || 1,
    workSlug: meta.work,
    // For work chunks the grouping key is `division:`; for the Sentences it
    // stays `distinctio:`.
    distinctio: work
      ? parseInt(meta.division) || 0
      : parseInt(meta.distinctio) || 0,
    pars: meta.pars ? parseInt(meta.pars) : undefined,
    articulus: meta.articulus ? parseInt(meta.articulus) : undefined,
    quaestio: meta.quaestio ? parseInt(meta.quaestio) : undefined,
    capitulum: meta.capitulum ? parseInt(meta.capitulum) : undefined,
    section: meta.section ? parseInt(meta.section) : undefined,
    // Scripture-commentary pericopes: the verse range as the volume index
    // prints it ("1", "2-7"). DISPLAY ONLY — the ordering key inside a
    // capitulum is `section:`, the pericope's ordinal, so a chunk is never
    // sorted by parsing this string.
    verses: meta.verses || undefined,
    division: work ? parseInt(meta.division) || 0 : undefined,
    // The RAW frontmatter type, `undefined` when the file declares none. The
    // front-matter guard tests this and never `type` below, which defaults —
    // see the trap documented at SENTENCES_FRONT_TYPES.
    declaredType: meta.type,
    type: meta.type || "quaestio",
    // First printed page, used to order a book's front matter (a linear run of
    // leaves) by what the plate says rather than by a hand-kept type rank.
    firstPage: meta.printed_pages
      ? parseInt(String(meta.printed_pages).match(/\d+/)?.[0]) || undefined
      : undefined,
    title: meta.title || "",
    titleLa: meta.title_la || "",
    titleEn: meta.title_en || "",
    wordCount: parseInt(meta.word_count_latin) || 0,
  };

  // Skip prolegomena (distinctio 0) — Sentences volumes only; work chunks
  // legitimately use division 0 for a prologue, and so do the Sentences books'
  // own front-matter chunks (Proemium / Textus Magistri / Capitula), which are
  // exempted by type. Anything else at distinctio 0 is editors' front matter.
  if (!work && chunkMeta.distinctio === 0 && !isSentencesFront(chunkMeta)) continue;

  chunks.push({
    id: chunkMeta.id,
    title: work ? buildWorkChunkTitle(chunkMeta) : buildQuestionTitle(chunkMeta),
    titleLa: chunkMeta.titleLa,
    titleEn: chunkMeta.titleEn,
    type: chunkMeta.type,
    latin,
    english,
    latinScholion,
    englishScholion,
    apparatus,
    notes,
    hasTranslation: english.length > 0,
    book: chunkMeta.book,
    workSlug: chunkMeta.workSlug,
    distinctio: chunkMeta.distinctio,
    pars: chunkMeta.pars,
    articulus: chunkMeta.articulus,
    quaestio: chunkMeta.quaestio,
    capitulum: chunkMeta.capitulum,
    section: chunkMeta.section,
    // Sort-only, stripped before output.
    isFront: isSentencesFront(chunkMeta),
    firstPage: chunkMeta.firstPage,
  });
}

// Group into books -> distinctions
const bookMap = new Map();
for (const chunk of chunks) {
  if (!bookMap.has(chunk.book)) bookMap.set(chunk.book, new Map());
  const distMap = bookMap.get(chunk.book);
  if (!distMap.has(chunk.distinctio)) distMap.set(chunk.distinctio, []);
  distMap.get(chunk.distinctio).push(chunk);
}

const books = [];
for (const [bookId, distMap] of [...bookMap.entries()].sort((a, b) => a[0] - b[0])) {
  const distinctions = [];
  for (const [distId, questions] of [...distMap.entries()].sort((a, b) => a[0] - b[0])) {
    // Type-based primary ordering: littera (Lombard's text) first, then
    // divisio textus, then quaestiones, then dubia last. Within a given type,
    // sort by pars → articulus → quaestio. This keeps dubia (which have no
    // articulus) from colliding with articulus=0 placeholders.
    const typeOrder = (q) => {
      // Front matter prints in this order: Bonaventure's Proemium, then the
      // Master's own opening, then his Capitula. Only the proemium needs a rank
      // of its own — littera and capitula already fall in printed order below.
      if (q.type === "praelocutio") return -2; // Book II only; prints before its Proemium
      if (q.type === "proemium") return -1;
      if (q.type === "littera-magistri" || q.type === "littera") return 0;
      if (q.type === "divisio") return 1;
      if (q.type === "dubia") return 3;
      return 2; // quaestio, prologus, capitulum, and anything else
    };
    questions.sort((a, b) => {
      // ★★ FRONT MATTER SORTS ON THE PLATE, NOT ON A TYPE RANK (2026-08-20).
      // A book's front matter is a strictly linear run of printed leaves, and
      // every front chunk's `printed_pages` is fixed against the plate before
      // it is written — so page order IS printed order, derived rather than
      // hand-kept. The type rank below cannot express Book I: its Master's
      // littera stands at pp. 16–17, i.e. AFTER the four prooemial questions
      // (pp. 6–15), where in Books II–IV the littera immediately follows the
      // proemium. Ranking littera ahead of quaestio is right there and wrong
      // here; the leaf number is right in all four. Ties (two units opening on
      // one leaf — Book IV's littera and capitula both open on p. 4) fall
      // through to the rank, which orders them correctly.
      if (a.isFront && b.isFront && a.firstPage && b.firstPage &&
          a.firstPage !== b.firstPage) {
        return a.firstPage - b.firstPage;
      }
      const ta = typeOrder(a), tb = typeOrder(b);
      if (ta !== tb) return ta - tb;
      const pa = a.pars ?? 0, pb = b.pars ?? 0;
      if (pa !== pb) return pa - pb;
      const aa = a.articulus ?? 0, ab = b.articulus ?? 0;
      if (aa !== ab) return aa - ab;
      const qa = a.quaestio ?? 0, qb = b.quaestio ?? 0;
      if (qa !== qb) return qa - qb;
      // Vol V+ ordering keys: prologue sections, then capitula.
      const sa = a.section ?? 0, sb = b.section ?? 0;
      if (sa !== sb) return sa - sb;
      const ca = a.capitulum ?? 0, cb = b.capitulum ?? 0;
      return ca - cb;
    });

    // A division's work registry entry (all chunks in a division share one work)
    const work = questions[0]?.workSlug ? WORKS[questions[0].workSlug] : undefined;
    // Division 0 of a Sentences book is its front matter. Quaracchi's own
    // citation idiom for it is "Prooemii" (the vol I prolegomena cite the
    // prooemial questions as `I. Sent. q. 4. Prooemii`), so the group takes the
    // edition's name rather than a "Distinction 0" that appears nowhere in
    // print. The chunk titles inside it disambiguate Proemium vs Textus
    // Magistri vs Capitula.
    const divTitle = work
      ? (work.divisions[distId] ?? `${work.divisionLabel.replace(/s$/, "")} ${distId}`)
      : distId === 0
        ? "Proemium"
        : `Distinction ${distId}`;

    // Strip grouping fields from output
    const cleaned = questions.map(
      ({ book, distinctio, workSlug, isFront, firstPage, ...rest }) => rest
    );
    distinctions.push({ id: distId, title: divTitle, questions: cleaned });
  }
  const bookWork = Object.values(WORKS).find((w) => w.book === bookId);
  books.push({
    id: bookId,
    title: bookWork ? bookWork.title : BOOK_TITLES[bookId] || `Book ${bookId}`,
    ...(bookWork
      ? {
          tome: bookWork.tome,
          initial: bookWork.initial,
          divisionLabel: bookWork.divisionLabel,
          ...(TOMES[bookWork.tome]
            ? {
                tomeTitle: TOMES[bookWork.tome].title,
                tomeInitial: TOMES[bookWork.tome].initial,
              }
            : {}),
        }
      : {}),
    distinctions,
  });
}

// Write output
fs.mkdirSync(path.dirname(OUT_FILE), { recursive: true });
fs.writeFileSync(OUT_FILE, JSON.stringify(books, null, 0));

const totalQ = books.reduce((s, b) => s + b.distinctions.reduce((s2, d) => s2 + d.questions.length, 0), 0);
const translated = books.reduce(
  (s, b) => s + b.distinctions.reduce((s2, d) => s2 + d.questions.filter((q) => q.hasTranslation).length, 0),
  0
);
console.log(`Built content.json: ${books.length} book(s), ${totalQ} questions, ${translated} translated`);

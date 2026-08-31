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
const VOL_DIRS = ["vol1", "vol2", "vol3", "vol4", "vol5"]
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
  const text = app[1] + "\n[^__SENTINEL__]:";
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
  // Future Vol V works claim book ids here as their mini-pilots run:
  // scientia-christi: 8, mysterio-trinitatis: 9,
  // perfectione-evangelica: 10, sermones-selecti: 14.
};

function buildWorkChunkTitle(meta) {
  // Type-first: standalone transmitted capitula tables and work-level scholia
  // (Itinerarium shape) name themselves regardless of division.
  if (meta.type === "capitula") return "Capitula";
  if (meta.type === "scholion") return "Scholion";
  // An undivided work is one chunk and names itself (De reductione).
  if (meta.type === "opusculum") return "Opusculum";
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

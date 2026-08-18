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

function buildQuestionTitle(meta) {
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
      24: "Scholion",
    },
  },
  // Future Vol V works claim book ids here as their mini-pilots run:
  // scientia-christi: 8, mysterio-trinitatis: 9,
  // perfectione-evangelica: 10, hexaemeron: 11, septem-donis: 12,
  // decem-praeceptis: 13, sermones-selecti: 14.
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
  if (meta.workSlug === "hexaemeron") return `Coll. ${meta.division}`;
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
    type: meta.type || "quaestio",
    title: meta.title || "",
    titleLa: meta.title_la || "",
    titleEn: meta.title_en || "",
    wordCount: parseInt(meta.word_count_latin) || 0,
  };

  // Skip prolegomena (distinctio 0) — Sentences volumes only; work chunks
  // legitimately use division 0 for a prologue.
  if (!work && chunkMeta.distinctio === 0) continue;

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
      if (q.type === "littera-magistri" || q.type === "littera") return 0;
      if (q.type === "divisio") return 1;
      if (q.type === "dubia") return 3;
      return 2; // quaestio, prologus, capitulum, and anything else
    };
    questions.sort((a, b) => {
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
    const divTitle = work
      ? (work.divisions[distId] ?? `${work.divisionLabel.replace(/s$/, "")} ${distId}`)
      : `Distinction ${distId}`;

    // Strip grouping fields from output
    const cleaned = questions.map(({ book, distinctio, workSlug, ...rest }) => rest);
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

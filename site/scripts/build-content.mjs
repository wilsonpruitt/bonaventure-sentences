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

const LATIN_DIR = path.join(REPO_ROOT, "vol1");
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

// Main
const latinFiles = fs.readdirSync(LATIN_DIR).filter((f) => f.endsWith(".md"));
const chunks = [];

for (const file of latinFiles) {
  const content = fs.readFileSync(path.join(LATIN_DIR, file), "utf-8");
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

  const chunkMeta = {
    id: meta.id,
    volume: parseInt(meta.volume) || 1,
    book: parseInt(meta.book) || 1,
    distinctio: parseInt(meta.distinctio) || 0,
    pars: meta.pars ? parseInt(meta.pars) : undefined,
    articulus: meta.articulus ? parseInt(meta.articulus) : undefined,
    quaestio: meta.quaestio ? parseInt(meta.quaestio) : undefined,
    type: meta.type || "quaestio",
    title: meta.title || "",
    titleLa: meta.title_la || "",
    titleEn: meta.title_en || "",
    wordCount: parseInt(meta.word_count_latin) || 0,
  };

  // Skip prolegomena (distinctio 0)
  if (chunkMeta.distinctio === 0) continue;

  chunks.push({
    id: chunkMeta.id,
    title: buildQuestionTitle(chunkMeta),
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
    distinctio: chunkMeta.distinctio,
    pars: chunkMeta.pars,
    articulus: chunkMeta.articulus,
    quaestio: chunkMeta.quaestio,
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
      return 2; // quaestio and anything else
    };
    questions.sort((a, b) => {
      const ta = typeOrder(a), tb = typeOrder(b);
      if (ta !== tb) return ta - tb;
      const pa = a.pars ?? 0, pb = b.pars ?? 0;
      if (pa !== pb) return pa - pb;
      const aa = a.articulus ?? 0, ab = b.articulus ?? 0;
      if (aa !== ab) return aa - ab;
      const qa = a.quaestio ?? 0, qb = b.quaestio ?? 0;
      return qa - qb;
    });

    // Strip grouping fields from output
    const cleaned = questions.map(({ book, distinctio, ...rest }) => rest);
    distinctions.push({ id: distId, title: `Distinction ${distId}`, questions: cleaned });
  }
  books.push({ id: bookId, title: BOOK_TITLES[bookId] || `Book ${bookId}`, distinctions });
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

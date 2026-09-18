/**
 * Pre-build script: measures how much of the Quaracchi Opera Omnia is
 * translated, IN PRINTED PAGES, and emits src/data/progress.json for the
 * /progress route to render.
 *
 * ⛔ THE NUMERATOR IS NEVER TYPED BY HAND. It is derived from the corpus:
 * every chunk file in vol1/…vol5/ declares `printed_pages:` in its
 * frontmatter, and this script unions those page numbers per volume. The
 * union matters — adjacent chunks share boundary leaves, so naive summing
 * double-counts every shared page. Distinct pages is the only honest count.
 *
 * The DENOMINATOR is the hard half, and it is not uniformly knowable:
 *
 *   Vols I–IV  MEASURED from the corpus itself. The Sentences commentary is
 *              complete in all four books, so each volume's body runs from
 *              the lowest printed page any of its chunks claims (the Proemium
 *              / Praelocutio, p. 1 in every volume) to the highest (the last
 *              dubium). Back matter — Quaracchi's own indices — is not body
 *              text and is not counted on either side of the ratio.
 *   Vol V      MEASURED from the volume's own index, via the work map frozen
 *              in the repo CLAUDE.md § VOL V: the ten works run from p. 3
 *              (QD de scientia Christi) to the end of the Sermones selecti.
 *              The last leaf — formerly the one soft edge, carried as ~579 —
 *              was SETTLED on 2026-09-17 against the digitized volume; see
 *              VOL5_BODY_LAST below.
 *   Vols VI–X  MEASURED on 2026-09-17 from the digitized Quaracchi volumes on
 *              the Internet Archive, leaf by leaf, replacing the round-hundred
 *              scoping estimates that stood here before. See MEASURED_EXTENTS
 *              below, which records for each volume its archive.org identifier,
 *              how its identity was confirmed, and how its last body page was
 *              established. Vol X is measured but NOT COUNTED — see below.
 *
 * The estimate machinery is deliberately left standing: any volume whose extent
 * could not be settled would fall back to UNSOURCED_VOLUMES and render hatched
 * and labelled. As of 2026-09-17 that set is empty.
 *
 * Anything that cannot be derived is either labelled an estimate or left out.
 */

import fs from "fs";
import path from "path";
import { fileURLToPath } from "url";

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const SITE_DIR = path.resolve(__dirname, "..");
const REPO_ROOT = path.resolve(SITE_DIR, "..");
const OUT_FILE = path.join(SITE_DIR, "src", "data", "progress.json");

const VOL_DIRS = ["vol1", "vol2", "vol3", "vol4", "vol5"];

// ---------------------------------------------------------------------------
// Vol V work map. Page ranges are Quaracchi's own, read off the volume index
// and frozen in CLAUDE.md § VOL V (work map). `pages` is the work's whole
// extent INCLUDING its half-title and the blank verso that faces it, which is
// why e.g. the Hexaemeron reads 327–454 while its translated body opens on
// p. 329. Those two leaves are part of the volume and are counted in the
// denominator; they carry no text, so they never appear in the numerator.
// ---------------------------------------------------------------------------
// `done` is always counted, never declared. `done` is a fact about the files;
// `complete` is a fact about the work-close gate, which no page count can see —
// it is taken from the same CLAUDE.md work map and CROSS-CHECKED below, so a
// work declared complete while leaves of it are missing fails the build loudly.
const VOL5_WORKS = [
  { slug: "scientia-christi", title: "Quaestiones disputatae de scientia Christi", first: 3, last: 43, complete: true },
  { slug: "mysterio-trinitatis", title: "Quaestiones disputatae de mysterio Trinitatis", first: 45, last: 115, complete: true },
  { slug: "perfectione-evangelica", title: "Quaestiones disputatae de perfectione evangelica", first: 117, last: 198, complete: true },
  { slug: "breviloquium", title: "Breviloquium", first: 199, last: 291, complete: true },
  { slug: "itinerarium", title: "Itinerarium mentis in Deum", first: 293, last: 316, complete: true },
  { slug: "de-reductione", title: "De reductione artium ad theologiam", first: 319, last: 325, complete: true },
  { slug: "hexaemeron", title: "Collationes in Hexaemeron", first: 327, last: 454, complete: true },
  { slug: "septem-donis", title: "Collationes de septem donis Spiritus Sancti", first: 455, last: 503, complete: true },
  { slug: "decem-praeceptis", title: "Collationes de decem praeceptis", first: 505, last: 532, complete: true },
  {
    slug: "sermones-selecti",
    title: "Sermones selecti de rebus theologicis",
    first: 533,
    // 579 was carried as approximate until 2026-09-17, when it was read off the
    // running head of the volume's last body leaf: archive.org
    // doctorisseraphic05bona, leaf 0657, head "TRACTATUS DE PLANTATIONE
    // PARADISI. 579" — the close of the fourth sermon. Leaf 0658 is blank and
    // leaf 0659 opens "INDEX OPUSCULORUM THEOLOGICORUM ... IN QUINTO TOMO" at
    // p. 581. Corroborated by the item's own _page_numbers.json (leaf 657 =
    // "579"). The tilde is gone.
    last: 579,
    complete: false,
  },
];

// How many leaves of a completed work may legitimately stand untranslated:
// its half-title, the blank verso facing it, and — in the Breviloquium alone —
// the editorial capitula table at pp. 209–210, which is apparatus and is not
// chunked. Above this, a "complete" claim is not credible and the build says so.
const NON_TEXT_LEAF_ALLOWANCE = 4;

// The volume's body extent. Start is fixed (p. 3, the first work's opening
// leaf); the end is the Sermones' approximate close.
const VOL5_BODY_FIRST = VOL5_WORKS[0].first;
const VOL5_BODY_LAST = VOL5_WORKS[VOL5_WORKS.length - 1].last;
const VOL5_LAST_IS_APPROX = false; // settled 2026-09-17, see the Sermones entry

// ---------------------------------------------------------------------------
// Vols VI–X: MEASURED, 2026-09-17, from the digitized Quaracchi volumes on the
// Internet Archive. These replace the round-hundred scoping estimates that
// OPERA-OMNIA-TRACKER.md carried ("~700/~700/~900/~800/~350"), which had no
// stated provenance.
//
// ⛔ THE DIGITS IN AN ARCHIVE.ORG IDENTIFIER ARE THE ITEM NUMBER, NOT THE
// VOLUME NUMBER. In this very family, `doctorisseraphic11bona` and
// `doctorisseraphic12bona` are the two halves of Tome I, not Tomes 11 and 12.
// So every identifier below was confirmed against the volume's own printed
// witness — its title page and its prolegomena heading — and never from the id.
//
// Method, identical for each volume:
//   1. Identity: read the title page and the "PROLEGOMENA IN <N>UM TOMUM"
//      heading out of the item's own OCR (`_djvu.xml`, which carries every
//      word on the leaf including the running heads — unlike `_djvu.txt` and
//      `_hocr_searchtext.txt`, neither of which is page-delimited here, and
//      whose hOCR page index drifts against the leaf numbering).
//   2. Body start: the volume's "OPERA HUIUS TOMI" contents leaf, which gives
//      the first work's opening page.
//   3. Body end: the last leaf before the volume's own index section, read by
//      its running head; the index heading on the following leaf is quoted.
//   4. Corroboration: the item's `_page_numbers.json`, which is an independent
//      OCR of the printed folio numbers, agreed at every boundary leaf.
// Leaf counts are NOT used as page counts: they differ by front matter, plates
// and the index, by 30–130 leaves in these volumes.
// ---------------------------------------------------------------------------
const MEASURED_EXTENTS = {
  6: {
    first: 1,
    last: 634,
    archiveId: "doctorisseraphic06bona",
    identity:
      'title page "COMMENTARII IN SACRAM SCRIPTURAM — TOMUS VI"; prolegomena head "PROLEGOMENA IN SEXTUM TOMUM"',
    bodyStart: 'contents leaf "OPERA HUIUS TOMI": Commentarius in librum Ecclesiastae, pag. 1',
    bodyEnd:
      'leaf 0678, running head "634 APPENDIX COLL. II"; leaf 0679 opens "INDEX EORUM QUAE IN HOC SEXTO TOMO CONTINENTUR"',
    confidence: "high",
  },
  7: {
    first: 1,
    last: 655,
    archiveId: "doctorisseraphic07bona",
    identity:
      'title page "COMMENTARIUS IN EVANGELIUM S. LUCAE — TOMUS VII"; prolegomena head "PROLEGOMENA IN SEPTIMUM TOMUM"; sheet signature "S. Bonav. — Tom. VII."',
    bodyStart: 'contents leaf "OPERA HUIUS TOMI": Commentarius in Evangelium S. Lucae, pag. 1',
    bodyEnd:
      'leaf 0681, running head "655 EXPOSITIO ORATIONIS DOMINICAE" (the appendix closes the volume); leaf 0682 blank, leaf 0683 opens "INDEX EORUM QUAE IN SEPTIMO TOMO CONTINENTUR"',
    confidence: "high",
  },
  8: {
    first: 3,
    last: 678,
    archiveId: "doctorisseraphic08bona",
    identity:
      'title page "OPUSCULA VARIA AD THEOLOGIAM MYSTICAM ET RES ORDINIS"; prolegomena head "PROLEGOMENA IN OCTAVUM TOMUM"',
    bodyStart: 'contents leaf "OPUSCULA HUIUS TOMI": Opusc. I, De Triplici Via, pag. 3',
    bodyEnd:
      'leaf 0810, running head "678 OPUSCULUM VII. RHYTHMICA"; leaf 0811 opens "INDEX ALPHABETICUS PRAECIPUARUM RERUM ET SENTENTIARUM QUAE IN HOC VOLUMINE CONTINENTUR"',
    confidence: "high",
  },
  9: {
    first: 3,
    last: 731,
    archiveId: "doctorisseraphic09bona",
    identity:
      'title page "SERMONES DE TEMPORE, DE SANCTIS, DE B. VIRGINE MARIA"; prolegomena head "PROLEGOMENA IN NONUM TOMUM"',
    bodyStart:
      'contents leaf "OPERA HUIUS TOMI": Introductio cum Opusculo de arte praedicandi, pag. 3',
    bodyEnd:
      'leaf 0761, the close of Sermones de diversis at p. 731 (leaf 0760 reads "730 SERMONES DE DIVERSIS"); leaf 0762 blank, leaf 0763 opens "INDEX SERMONUM ET SCHEMATUM HUIUS TOMI"',
    confidence: "high",
  },
  // Vol X is measured but NOT COUNTED. Wilson's scope call, 2026-09-17: the
  // volume is Quaracchi's own prolegomena, general indices and apparatus, and
  // this project generates its indexes from the text itself (INDEX-PLAN.md,
  // approved 2026-07-31). It is not text to translate, so it sits outside the
  // denominator — stated on the page, never dropped silently.
  10: {
    first: 1,
    last: 277,
    counted: false,
    archiveId: "doctorisseraphic10bona",
    identity:
      'item metadata volume "t.10"; contents leaf "TABULA OPERUM OMNIUM HUIUS EDITIONIS IN TOM. I.–IV."; the running indices reference tomes I–IX throughout',
    bodyStart: "the volume is index and apparatus throughout; the first numbered leaf is p. 5",
    bodyEnd:
      'leaf 0291, running head "277 INDEX LOCORUM SS. PATRUM" (Plotinus–Xenocrates); leaf 0293 is the Tabula operum, leaf 0294 the Corrigenda and Imprimatur of 16 August 1902',
    confidence: "high",
  },
};

// Volumes whose extent could NOT be settled fall back to a round estimate and
// are rendered hatched and named as estimates. Emptied 2026-09-17, when Vols
// VI–X were measured. Leave the machinery in place: it is what keeps a future
// unmeasured volume from being quietly added to a measured total.
const UNSOURCED_VOLUMES = {};

// Volume identity — titles and years as the landing page already gives them.
const VOLUMES = [
  { n: 1, tome: "I", year: 1882, title: "Commentarius in I librum Sententiarum", gloss: "Commentary on Book I of the Sentences — the Trinity" },
  { n: 2, tome: "II", year: 1885, title: "Commentarius in II librum Sententiarum", gloss: "Commentary on Book II — creation, the angels, and sin" },
  { n: 3, tome: "III", year: 1887, title: "Commentarius in III librum Sententiarum", gloss: "Commentary on Book III — the Incarnation and the virtues" },
  { n: 4, tome: "IV", year: 1889, title: "Commentarius in IV librum Sententiarum", gloss: "Commentary on Book IV — the sacraments and the last things" },
  { n: 5, tome: "V", year: 1891, title: "Opuscula varia theologica", gloss: "The Breviloquium, Itinerarium, Hexaemeron, and the disputed questions" },
  { n: 6, tome: "VI", year: 1893, title: "Commentarii in Sacram Scripturam", gloss: "Commentaries on Ecclesiastes, Wisdom, and John" },
  { n: 7, tome: "VII", year: 1895, title: "Commentarius in Evangelium S. Lucae", gloss: "The full commentary on the Gospel of Luke" },
  { n: 8, tome: "VIII", year: 1898, title: "Opuscula ad theologiam mysticam et res Ordinis", gloss: "Mystical and ascetic opuscula; Franciscan-order writings" },
  { n: 9, tome: "IX", year: 1901, title: "Sermones", gloss: "Sermons — de tempore, de sanctis, Marian, and diverse" },
  { n: 10, tome: "X", year: 1902, title: "Operum omnium complementum", gloss: "Supplements, general indices, and editorial apparatus" },
];

// ---------------------------------------------------------------------------
// Scan the corpus.
// ---------------------------------------------------------------------------

/** Pull one scalar field out of a chunk's YAML-ish frontmatter block. */
function field(front, name) {
  const m = front.match(new RegExp(`^${name}:\\s*(.+)$`, "m"));
  return m ? m[1].trim().replace(/^["']|["']$/g, "") : undefined;
}

const volumePages = new Map(); // volume number -> Set of printed pages
const workPages = new Map(); // Vol V work slug -> Set of printed pages
let chunksScanned = 0;
let chunksWithPages = 0;
const unknownWorkSlugs = new Set();

for (const dir of VOL_DIRS) {
  const abs = path.join(REPO_ROOT, dir);
  if (!fs.existsSync(abs)) continue;
  for (const file of fs.readdirSync(abs).sort()) {
    if (!file.endsWith(".md")) continue;
    const text = fs.readFileSync(path.join(abs, file), "utf8");
    const fm = text.match(/^---\n([\s\S]*?)\n---\n/);
    if (!fm) continue; // not a chunk (punch lists, notes)
    const front = fm[1];
    if (!field(front, "id")) continue;
    chunksScanned += 1;

    const raw = field(front, "printed_pages");
    if (!raw) continue; // a chunk with no page claim contributes nothing
    const pages = (raw.match(/\d+/g) || []).map(Number).filter((n) => n > 0);
    if (!pages.length) continue;
    chunksWithPages += 1;

    const vol = parseInt(field(front, "volume") || dir.replace("vol", ""), 10);
    if (!volumePages.has(vol)) volumePages.set(vol, new Set());
    for (const p of pages) volumePages.get(vol).add(p);

    const work = field(front, "work");
    if (work) {
      if (!VOL5_WORKS.some((w) => w.slug === work)) unknownWorkSlugs.add(work);
      if (!workPages.has(work)) workPages.set(work, new Set());
      for (const p of pages) workPages.get(work).add(p);
    }
  }
}

if (unknownWorkSlugs.size) {
  // Loud, because a work outside the map is a page the denominator has not
  // accounted for — the one way this page could overstate itself.
  console.warn(
    `build-progress: WORK SLUG NOT IN THE VOL V MAP: ${[...unknownWorkSlugs].join(", ")} — ` +
      `its pages are in the numerator but its extent is not in the denominator.`
  );
}

// ---------------------------------------------------------------------------
// Assemble.
// ---------------------------------------------------------------------------

function count(set) {
  return set ? set.size : 0;
}

const volumes = VOLUMES.map((v) => {
  const done = count(volumePages.get(v.n));
  const sorted = [...(volumePages.get(v.n) || [])].sort((a, b) => a - b);

  if (v.n <= 4) {
    // Measured from the corpus: the commentary is complete, so its first and
    // last translated leaves ARE the volume's first and last body leaves.
    const first = sorted[0];
    const last = sorted[sorted.length - 1];
    const total = first && last ? last - first + 1 : 0;
    return {
      ...v,
      done,
      total,
      basis: "measured",
      extent: first && last ? `pp. ${first}–${last}` : "",
      state: "complete",
      shortfall: total - done,
    };
  }

  if (v.n === 5) {
    const total = VOL5_BODY_LAST - VOL5_BODY_FIRST + 1;
    const works = VOL5_WORKS.map((w) => {
      const wDone = count(workPages.get(w.slug));
      const wTotal = w.last - w.first + 1;
      return {
        slug: w.slug,
        title: w.title,
        extent: `pp. ${w.first}–${w.lastIsApprox ? "~" : ""}${w.last}`,
        done: wDone,
        total: wTotal,
        complete: Boolean(w.complete),
        approxEnd: Boolean(w.lastIsApprox),
      };
    });
    for (const w of works) {
      if (w.complete && w.total - w.done > NON_TEXT_LEAF_ALLOWANCE) {
        throw new Error(
          `build-progress: ${w.slug} is declared complete but ${w.total - w.done} of its ` +
            `${w.total} leaves carry no translated page. Either the work map's extent is ` +
            `wrong or the work is not in fact closed — do not publish either number.`
        );
      }
      if (!w.complete && w.done > 0 && w.total - w.done <= NON_TEXT_LEAF_ALLOWANCE) {
        console.warn(
          `build-progress: ${w.slug} is not declared complete but every leaf is translated — ` +
            `update the work map if its gate has closed.`
        );
      }
    }
    // Split the volume's shortfall so the page can say what it consists of:
    // pages of works still to be done, versus leaves that carry no text at all
    // (half-titles, blank versos, the editorial capitula tables, and the blank
    // leaves standing between one work and the next).
    const pendingPages = works
      .filter((w) => !w.complete)
      .reduce((s, w) => s + (w.total - w.done), 0);
    return {
      ...v,
      done,
      total,
      basis: "measured",
      extent: `pp. ${VOL5_BODY_FIRST}–${VOL5_LAST_IS_APPROX ? "~" : ""}${VOL5_BODY_LAST}`,
      approxEnd: VOL5_LAST_IS_APPROX,
      state: "in-progress",
      shortfall: total - done,
      pendingPages,
      nonTextLeaves: total - done - pendingPages,
      works,
    };
  }

  const m = MEASURED_EXTENTS[v.n];
  if (m) {
    const total = m.last - m.first + 1;
    return {
      ...v,
      done,
      total,
      basis: "measured",
      counted: m.counted !== false,
      extent: `pp. ${m.first}\u2013${m.last}`,
      state: "planned",
      shortfall: total - done,
      source: {
        archiveId: m.archiveId,
        identity: m.identity,
        bodyStart: m.bodyStart,
        bodyEnd: m.bodyEnd,
        confidence: m.confidence,
      },
    };
  }

  if (UNSOURCED_VOLUMES[v.n] === undefined) {
    throw new Error(
      `build-progress: Vol ${v.tome} has neither a measured extent nor an estimate. ` +
        `A volume with no extent at all cannot be rendered — add it to MEASURED_EXTENTS ` +
        `or to UNSOURCED_VOLUMES; do not let it fall through as zero.`
    );
  }

  return {
    ...v,
    done,
    total: UNSOURCED_VOLUMES[v.n],
    basis: "estimated",
    counted: true,
    extent: "",
    state: "planned",
    shortfall: UNSOURCED_VOLUMES[v.n] - done,
  };
});

// `counted` is the scope gate, and it is separate from `basis`. A volume can be
// measured and still sit outside the denominator (Vol X), and nothing outside
// the denominator may contribute to the numerator either — if it ever did, the
// ratio would be a lie in the project's own favour, so the build refuses.
const counted = volumes.filter((v) => v.counted !== false);
const uncounted = volumes.filter((v) => v.counted === false);
for (const v of uncounted) {
  if (v.done > 0) {
    throw new Error(
      `build-progress: Vol ${v.tome} is excluded from the denominator but ${v.done} of its ` +
        `pages are translated. Either count the volume or stop counting its pages — ` +
        `do not publish a percentage that has it both ways.`
    );
  }
}

const measured = counted.filter((v) => v.basis === "measured");
const estimated = counted.filter((v) => v.basis === "estimated");

const pagesTranslated = counted.reduce((s, v) => s + v.done, 0);
const measuredTotal = measured.reduce((s, v) => s + v.total, 0);
const estimatedTotal = estimated.reduce((s, v) => s + v.total, 0);

const progress = {
  // Not "today" — the mtime of the newest chunk, so the stamp tracks the
  // corpus rather than the build machine's clock.
  asOf: newestChunkDate(),
  pagesTranslated,
  measuredTotal,
  measuredRemaining: measuredTotal - pagesTranslated,
  estimatedTotal,
  editionTotal: measuredTotal + estimatedTotal,
  pctOfMeasured: round1((pagesTranslated / measuredTotal) * 100),
  pctOfEdition: round1((pagesTranslated / (measuredTotal + estimatedTotal)) * 100),
  anyEstimated: estimated.length > 0,
  estimatedTomes: estimated.map((v) => v.tome),
  uncountedTomes: uncounted.map((v) => ({ tome: v.tome, total: v.total })),
  volumes,
  audit: { chunksScanned, chunksWithPages },
};

function round1(n) {
  return Math.round(n * 10) / 10;
}

function newestChunkDate() {
  let newest = 0;
  for (const dir of VOL_DIRS) {
    const abs = path.join(REPO_ROOT, dir);
    if (!fs.existsSync(abs)) continue;
    for (const file of fs.readdirSync(abs)) {
      if (!file.endsWith(".md")) continue;
      const t = fs.statSync(path.join(abs, file)).mtimeMs;
      if (t > newest) newest = t;
    }
  }
  return new Date(newest || Date.now()).toISOString().slice(0, 10);
}

fs.mkdirSync(path.dirname(OUT_FILE), { recursive: true });
fs.writeFileSync(OUT_FILE, JSON.stringify(progress, null, 2) + "\n");

console.log(
  `build-progress: ${chunksWithPages}/${chunksScanned} chunks carry printed_pages · ` +
    `${pagesTranslated} distinct printed pages translated · ` +
    `${progress.pctOfMeasured}% of the ${measuredTotal} measured pp. · ` +
    (estimated.length
      ? `${progress.pctOfEdition}% of the ~${progress.editionTotal} pp. counted edition ` +
        `(Tome${estimated.length > 1 ? "s" : ""} ${progress.estimatedTomes.join(", ")} estimated)`
      : `every counted volume measured; no estimate in the denominator`) +
    (uncounted.length
      ? ` · outside the count: Tome${uncounted.length > 1 ? "s" : ""} ` +
        progress.uncountedTomes.map((u) => `${u.tome} (${u.total} pp.)`).join(", ")
      : "")
);
for (const v of volumes) {
  console.log(
    `  Tome ${v.tome.padEnd(4)} ${String(v.done).padStart(5)} / ${String(v.total).padStart(5)} pp.  ` +
      `(${v.basis}${v.counted === false ? ", NOT COUNTED" : ""})` +
      (v.source ? `  [${v.source.archiveId}]` : "")
  );
}

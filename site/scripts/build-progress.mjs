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
 *              ⚠ The last leaf is the one soft edge — the index gives the
 *              Sermones as 533–~579 and that end has not been plate-verified.
 *   Vols VI–X  ESTIMATED. No source text for these volumes is on disk: no
 *              PDF, no OCR, no index. The only figures that exist are the
 *              scoping estimates in the repo's OPERA-OMNIA-TRACKER.md, which
 *              are round numbers to the nearest hundred. They are carried
 *              here AS ESTIMATES and are labelled as such on the page. They
 *              are never added silently into a measured total.
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
    last: 579,
    lastIsApprox: true,
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
const VOL5_LAST_IS_APPROX = true;

// ---------------------------------------------------------------------------
// Vols VI–X: ESTIMATES ONLY. Source: OPERA-OMNIA-TRACKER.md, "Scope table —
// all 10 volumes", the "Printed pp." column, every entry of which is written
// there with a tilde. Nothing on disk can improve on these until the volumes
// are fetched from the Internet Archive.
// ---------------------------------------------------------------------------
const UNSOURCED_VOLUMES = {
  6: 700,
  7: 700,
  8: 900,
  9: 800,
  10: 350,
};

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

  return {
    ...v,
    done,
    total: UNSOURCED_VOLUMES[v.n],
    basis: "estimated",
    extent: "",
    state: "planned",
    shortfall: UNSOURCED_VOLUMES[v.n] - done,
  };
});

const measured = volumes.filter((v) => v.basis === "measured");
const estimated = volumes.filter((v) => v.basis === "estimated");

const pagesTranslated = volumes.reduce((s, v) => s + v.done, 0);
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
    `${progress.pctOfMeasured}% of the ${measuredTotal} measured pp. (Vols I–V) · ` +
    `${progress.pctOfEdition}% of the ~${progress.editionTotal} pp. edition (Vols VI–X estimated)`
);
for (const v of volumes) {
  console.log(
    `  Tome ${v.tome.padEnd(4)} ${String(v.done).padStart(5)} / ${String(v.total).padStart(5)} pp.  (${v.basis})`
  );
}

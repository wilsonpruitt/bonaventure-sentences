/**
 * Shared helpers for the open-corpus reading layer (siblings + export).
 * See ~/open-corpus/PLAN.md §3/§4/Appendix E for the contract this implements.
 *
 * Sibling URL scheme deviates from the other sites' plain `.txt`/`.json`
 * convention: Next's static export already writes a `<slug>.txt` RSC
 * prefetch payload next to every `<slug>.html` page, so our plain-text
 * sibling lives at `<slug>.plain.txt` instead. `.json` was free and is
 * unchanged.
 */

const SITE_URL = "https://bonaventure.wrootpress.com";
const AUTHOR = "St. Bonaventure";
const LICENSE_SOURCE = "Public Domain Mark 1.0";
const LICENSE_TRANSLATION = "CC BY-NC 4.0";
const LICENSE_APPARATUS = "CC BY-NC 4.0";
const SOURCE_EDITION_TITLE = "Opera Omnia (Quaracchi critical edition)";
const SOURCE_EDITION_PUBLISHER = "Collegii S. Bonaventurae";
const SOURCE_EDITION_YEARS = "1882-1902";

// Strip footnote markers ([^id]) and page-break comments (<!-- page N -->)
// for the plain-text sibling; keep them in the JSON's `latin`/`english`
// fields since they carry real information (apparatus anchors).
export function toPlainText(md) {
  if (!md) return "";
  return md
    .replace(/<!--\s*page\s+\d+\s*-->/gi, "")
    .replace(/\[\^[^\]]+\]/g, "")
    .replace(/\n{3,}/g, "\n\n")
    .trim();
}

export function firstPage(md) {
  if (!md) return null;
  const m = md.match(/<!--\s*page\s+(\d+)\s*-->/i);
  return m ? parseInt(m[1], 10) : null;
}

export function lastPage(md) {
  if (!md) return null;
  const all = [...md.matchAll(/<!--\s*page\s+(\d+)\s*-->/gi)];
  if (!all.length) return null;
  return parseInt(all[all.length - 1][1], 10);
}

export function chunkUrl(bookId, distId, qId) {
  return `${SITE_URL}/browse/${bookId}/d/${distId}/q/${encodeURIComponent(qId)}`;
}

// One record per chunk, shared by the .json sibling and the bulk export.
export function buildRecord({ book, dist, q }) {
  const p1 = firstPage(q.latin) ?? firstPage(q.english);
  const p2 = lastPage(q.latin) ?? lastPage(q.english);
  const pagination = p1 && p2 ? (p1 === p2 ? `p. ${p1}` : `pp. ${p1}-${p2}`) : null;

  return {
    id: q.id,
    url: chunkUrl(book.id, dist.id, q.id),
    site: "bonaventure",
    collection: book.title,
    title: q.title,
    title_alt: [q.titleLa, q.titleEn].filter(Boolean),
    author: AUTHOR,
    languages: ["en", "la"],
    source_edition: {
      title: SOURCE_EDITION_TITLE,
      publisher: SOURCE_EDITION_PUBLISHER,
      years: SOURCE_EDITION_YEARS,
      volume: book.tome ?? book.id,
      pagination,
    },
    source_text: q.latin || null,
    english: q.english || null,
    apparatus: {
      notes: (q.apparatus || []).map((a) => ({ id: a.id, la: a.la, en: a.en })),
      latin_scholion: q.latinScholion || null,
      english_scholion: q.englishScholion || null,
      translators_notes: q.notes || null,
    },
    provenance: {
      method:
        "LLM-assisted translation from the Quaracchi Latin, verified chunk-by-chunk against the printed plates (apparatus roster, cross-references, page/gutter boundaries).",
      corrected_against_scan: true,
    },
    license_source: LICENSE_SOURCE,
    license_translation: LICENSE_TRANSLATION,
    license_apparatus: LICENSE_APPARATUS,
    generated: new Date().toISOString().slice(0, 10),
  };
}

export function plainTextSibling(record) {
  const lines = [
    record.title,
    `by ${record.author}`,
    `Source text: ${record.license_source}. English translation/apparatus/encoding: ${record.license_translation}, Wroot Press.`,
    record.url,
    "-".repeat(40),
    "",
    toPlainText(record.english || ""),
  ];
  return lines.join("\n");
}

export { SITE_URL, AUTHOR, LICENSE_SOURCE, LICENSE_TRANSLATION, LICENSE_APPARATUS };

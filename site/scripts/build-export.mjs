/**
 * Bulk export: aggregates every chunk into one JSONL file, both languages
 * inline, plus a manifest and README. Builds locally into export/ at the
 * repo root (not the site/ deploy root) — hosting is the shared Cloudflare
 * R2 bucket `wroot-corpus-export`, prefix `bonaventure/`, per
 * ~/open-corpus/PLAN.md item 8. Not wired to R2 yet — see status log.
 *
 * Run: node scripts/build-export.mjs
 */

import fs from "fs";
import path from "path";
import zlib from "zlib";
import { fileURLToPath } from "url";
import { buildRecord, toPlainText } from "./lib/reading-layer.mjs";

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const SITE_DIR = path.resolve(__dirname, "..");
const REPO_ROOT = path.resolve(SITE_DIR, "..");
const CONTENT_FILE = path.join(SITE_DIR, "src", "data", "content.json");
const EXPORT_DIR = path.join(REPO_ROOT, "export");

const books = JSON.parse(fs.readFileSync(CONTENT_FILE, "utf-8"));
const today = new Date().toISOString().slice(0, 10);

const records = [];
for (const book of books) {
  for (const dist of book.distinctions) {
    for (const q of dist.questions) {
      records.push(buildRecord({ book, dist, q }));
    }
  }
}

fs.mkdirSync(EXPORT_DIR, { recursive: true });

// jsonl.gz — one JSON object per chunk, full text inline.
const jsonlName = `bonaventure-${today}.jsonl.gz`;
const jsonlLines = records.map((r) => JSON.stringify(r)).join("\n") + "\n";
const jsonlGz = zlib.gzipSync(Buffer.from(jsonlLines, "utf-8"));
fs.writeFileSync(path.join(EXPORT_DIR, jsonlName), jsonlGz);

// txt.tar.gz would need a tar dependency; ship a flat plain-text mirror
// directory instead, gzipped per-file is unnecessary at this corpus size —
// tar the directory with the system tar binary for parity with the other
// sites' single archive.
const txtDir = path.join(EXPORT_DIR, "_txt-staging");
fs.rmSync(txtDir, { recursive: true, force: true });
fs.mkdirSync(txtDir, { recursive: true });
for (const r of records) {
  const header = [
    r.title,
    `by ${r.author}`,
    `Source text: ${r.license_source}. English translation/apparatus/encoding: ${r.license_translation}, Wroot Press.`,
    r.url,
    "-".repeat(40),
    "",
  ].join("\n");
  fs.writeFileSync(path.join(txtDir, `${r.id}.txt`), header + toPlainText(r.english || ""));
}

const { execFileSync } = await import("child_process");
const txtTarName = `bonaventure-txt-${today}.tar.gz`;
execFileSync("tar", ["-czf", path.join(EXPORT_DIR, txtTarName), "-C", txtDir, "."]);
fs.rmSync(txtDir, { recursive: true, force: true });

// README.md
const totalWords = records.reduce(
  (s, r) => s + (r.english || "").split(/\s+/).filter(Boolean).length,
  0
);
const readme = `# Bonaventure — bulk export

Generated ${today}. ${records.length} chunks (Opera Omnia, Books I-IV of the
Commentary on the Sentences plus Volume V), ~${totalWords.toLocaleString()} words of English.

## Files

- \`${jsonlName}\` — one JSON object per chunk, full English text inline in
  the \`english\` field, the Latin source text in \`source_text\`,
  apparatus notes, source-edition citation, license fields.
- \`${txtTarName}\` — plain-text mirror of each chunk as \`<id>.txt\`
  (English only, headered), one file per chunk inside the archive.

## License

**The source text.** The Quaracchi Latin (Collegii S. Bonaventurae,
1882-1902) is public domain.

**The English translation, apparatus, and encoding** are
[CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/),
attribution "bonaventure.wrootpress.com (Wilson Pruitt, Wroot Press)". Full
terms: https://bonaventure.wrootpress.com/rights — including the explicit
machine-learning-use permission (§3a of LICENSE), which covers commercial
model training.

## Hosting

Served from the shared Cloudflare R2 bucket \`wroot-corpus-export\`
(prefix \`bonaventure/\`), not baked into any deploy — see
\`~/open-corpus/PLAN.md\` item 8.
`;
fs.writeFileSync(path.join(EXPORT_DIR, "README.md"), readme);

// manifest.json
const manifest = {
  generated: today,
  chunks: records.length,
  words: totalWords,
  files: [
    {
      name: jsonlName,
      description: "One JSON object per chunk, full text inline.",
      size_bytes: fs.statSync(path.join(EXPORT_DIR, jsonlName)).size,
    },
    {
      name: txtTarName,
      description: "Plain-text mirror of each chunk, one file per chunk inside the archive.",
      size_bytes: fs.statSync(path.join(EXPORT_DIR, txtTarName)).size,
    },
    {
      name: "README.md",
      description: "Schema, license, and changelog.",
      size_bytes: fs.statSync(path.join(EXPORT_DIR, "README.md")).size,
    },
  ],
};
fs.writeFileSync(path.join(EXPORT_DIR, "manifest.json"), JSON.stringify(manifest, null, 2));

// Also copy into site/src/data so the /export page can import it at Next
// build time without reading outside the site/ deploy root (Vercel's deploy
// root here is site/, same reason content.json is pre-built — see
// build-content.mjs's header comment).
fs.writeFileSync(
  path.join(SITE_DIR, "src", "data", "export-manifest.json"),
  JSON.stringify(manifest, null, 2)
);

console.log(
  `Built export: ${records.length} chunks, ~${totalWords.toLocaleString()} words -> ${EXPORT_DIR}`
);

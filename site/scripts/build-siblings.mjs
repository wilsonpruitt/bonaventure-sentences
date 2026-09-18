/**
 * Postbuild step: writes a .json and .plain.txt sibling for every chunk page
 * into out/, straight from content.json (not from the rendered HTML/RSC
 * payload). Run after `next build` (output: "export"), before deploy.
 *
 * Open-corpus reading-layer contract: ~/open-corpus/PLAN.md §3 item 7.
 */

import fs from "fs";
import path from "path";
import { fileURLToPath } from "url";
import { buildRecord, plainTextSibling } from "./lib/reading-layer.mjs";

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const SITE_DIR = path.resolve(__dirname, "..");
const CONTENT_FILE = path.join(SITE_DIR, "src", "data", "content.json");
const OUT_DIR = path.join(SITE_DIR, "out");

const books = JSON.parse(fs.readFileSync(CONTENT_FILE, "utf-8"));

if (!fs.existsSync(OUT_DIR)) {
  console.error(`out/ not found at ${OUT_DIR} — run \`next build\` first.`);
  process.exit(1);
}

let written = 0;
for (const book of books) {
  for (const dist of book.distinctions) {
    for (const q of dist.questions) {
      const record = buildRecord({ book, dist, q });
      const dir = path.join(OUT_DIR, "browse", String(book.id), "d", String(dist.id), "q");
      fs.mkdirSync(dir, { recursive: true });
      const base = path.join(dir, encodeURIComponent(q.id));
      fs.writeFileSync(`${base}.json`, JSON.stringify(record, null, 2));
      fs.writeFileSync(`${base}.plain.txt`, plainTextSibling(record));
      written++;
    }
  }
}

console.log(`Wrote ${written} .json + .plain.txt sibling pairs into out/.`);

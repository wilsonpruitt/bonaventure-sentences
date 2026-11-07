/**
 * Writes site/vercel.json: permanent redirects from every pre-Phase-2 address
 * (/browse/{bookId}/d/{distId}/q/{chunkId}, its .json/.plain.txt siblings, the
 * book, division and tome pages) to the readable addresses of
 * scripts/lib/addresses.mjs. PATTERN rules, a few per book, not one per chunk;
 * the unit is captured from the old chunk id, which is what the new address is
 * derived from, so a chunk added later is covered by its book's rule.
 *
 * Run by `pnpm build` before `next build`. The output is committed so that a
 * reviewer can read the rules; never hand-edit it.
 */

import fs from "fs";
import path from "path";
import { fileURLToPath } from "url";
import { ROMAN, idPrefix } from "./lib/addresses.mjs";

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const SITE_DIR = path.resolve(__dirname, "..");
const books = JSON.parse(fs.readFileSync(path.join(SITE_DIR, "src/data/content.json"), "utf-8"));

const redirects = [];
const r = (source, destination) => redirects.push({ source, destination, permanent: true });

for (const b of books) {
  if (b.slug === "sentences") {
    const R = ROMAN[b.id - 1];
    r(`/browse/${b.id}/d/0/q/bon-sent-${R}-:unit`, `${b.path}/:unit`);
    r(`/browse/${b.id}/d/:d/q/bon-sent-${R}-d:n(\\d+)-:unit`, `${b.path}/d:d/:unit`);
    r(`/browse/${b.id}/d/0`, `${b.path}#d-0`);
    r(`/browse/${b.id}/d/:d`, `${b.path}/d:d`);
  } else {
    const prefix = idPrefix(b);
    if (prefix.endsWith("-")) {
      r(`/browse/${b.id}/d/:d/q/${prefix}:unit`, `${b.path}/:unit`);
    } else {
      // A one-chunk work with a bare id (bon-red → /de-reductione/text).
      for (const ext of ["", ".json", ".plain.txt"])
        r(`/browse/${b.id}/d/:d/q/${prefix}${ext}`, `${b.path}/text${ext}`);
    }
    r(`/browse/${b.id}/d/:d`, `${b.path}#d-:d`);
  }
  r(`/browse/${b.id}`, b.path);
  // Tomes I–IV are one work each: /tome/N is that book.
  if (b.slug === "sentences") r(`/tome/${b.id}`, b.path);
}
r("/browse/tome/:n", "/tome/:n");

const out = path.join(SITE_DIR, "vercel.json");
fs.writeFileSync(out, JSON.stringify({ redirects }, null, 2) + "\n");
console.log(`Wrote ${redirects.length} redirect rules to vercel.json.`);

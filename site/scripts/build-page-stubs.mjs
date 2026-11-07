/**
 * Postbuild: /tome/{n}/page/{m} for every printed page the translation holds
 * (SITE-PLAN Phase 3). Each is a tiny static page that forwards to the chunk
 * owning that page, or lists the chunks when two share it. Data: public/goto.json
 * `pages`, built by tools/build-index-json.py from the ledger's own by_page index.
 * Not indexed by search engines (the chunk page is the canonical address).
 */
import fs from "fs";
import path from "path";
import { fileURLToPath } from "url";

const SITE = path.resolve(path.dirname(fileURLToPath(import.meta.url)), "..");
const OUT = path.join(SITE, "out");
const BASE = "https://bonaventure.wrootpress.com";
const GOTO = path.join(SITE, "public", "goto.json");
if (!fs.existsSync(GOTO)) {
  console.error("build-page-stubs: public/goto.json is missing. Run `python3.11 tools/build-index-json.py` first.");
  process.exit(1);
}
const goto = JSON.parse(fs.readFileSync(GOTO, "utf8"));
const ROMAN = ["I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX", "X"];
const esc = (s) => s.replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/"/g, "&quot;");
const titleOf = new Map(goto.chunks.map((c) => [c.path, c.id]));

const page = (title, head, body) => `<!DOCTYPE html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<meta name="robots" content="noindex"><title>${esc(title)}</title>${head}
<style>body{font-family:Georgia,serif;background:#F5EFE0;color:#3D1308;max-width:40rem;margin:4rem auto;padding:0 1rem;line-height:1.6}a{color:#3D1308}</style>
</head><body>${body}</body></html>
`;

let n = 0;
for (const [key, paths] of Object.entries(goto.pages)) {
  const [tome, pg] = key.split(":");
  const label = `Quaracchi tom. ${ROMAN[tome - 1]}, p. ${pg}`;
  const file = path.join(OUT, "tome", tome, "page", `${pg}.html`);
  fs.mkdirSync(path.dirname(file), { recursive: true });
  const html =
    paths.length === 1
      ? page(
          label,
          `<meta http-equiv="refresh" content="0; url=${esc(paths[0])}"><link rel="canonical" href="${BASE}${esc(paths[0])}">`,
          `<p>${esc(label)} is in <a href="${esc(paths[0])}">${esc(paths[0])}</a>.</p>`
        )
      : page(
          label,
          "",
          `<p>${esc(label)} is shared by ${paths.length} passages:</p><ul>${paths
            .map((p) => `<li><a href="${esc(p)}">${esc(titleOf.get(p) ?? p)}</a></li>`)
            .join("")}</ul>`
        );
  fs.writeFileSync(file, html);
  n++;
}
console.log(`Wrote ${n} printed-page stubs under out/tome/*/page/.`);

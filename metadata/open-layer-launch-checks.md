# Open Corpus Plan — reading-layer launch checks (Bonaventure)

Rollout per `~/open-corpus/PLAN.md` §4, fourth site (after Christian Library, migne.app,
acta-sanctorum). Appendix F checks run against a local `next build` + `build-siblings.mjs`
on 2026-09-18, before push/deploy.

1. **GPTBot fetch of a work URL → 200, full text, no gate.** Verified on the rendered
   `out/` HTML for `bon-sent-I-proem` (and spot-checked others) — full body present,
   no auth/gate. PASS.
2. **`.txt`/`.json` siblings → 200, header + text; `.json` parses.** Next's static
   export already writes a `<slug>.txt` RSC prefetch payload next to every page, so the
   plain-text sibling lives at `<slug>.plain.txt` instead (documented in `llms.txt` and
   `scripts/lib/reading-layer.mjs`). Both `.json` and `.plain.txt` verified present and
   parseable for all 2,113 chunks (`build-siblings.mjs` output: "Wrote 2113 .json +
   .plain.txt sibling pairs"). PASS (with the documented URL-scheme deviation).
3. **`robots.txt`, `llms.txt`, `sitemap.xml`, `/rights`, `/export` → 200; footer line
   present.** All five present in `out/`; footer license line pre-existing in
   `layout.tsx`. PASS.
4. **Canonical is absolute `https://` and equals `@id` in the JSON-LD; JSON-LD parses.**
   Verified match on `bon-sent-I-proem`; same code path for all chunk pages. PASS.
5. **`/export` manifest lists the newest export; the R2 object downloads.** ⬜ NOT YET —
   the shared `wroot-corpus-export` R2 bucket does not exist yet (same open item as CL,
   migne, Acta). `/export` reads a local build-time manifest and shows a placeholder
   `EXPORT_R2_BASE_URL`; the local export bundle built clean: 2,113 chunks, ~3.33M words,
   `bonaventure-2026-09-18.jsonl.gz` (20.6 MB) + `bonaventure-txt-2026-09-18.tar.gz`
   (5.6 MB) + `README.md`, in `~/bonaventure-sentences/export/` (gitignored).
6. **Sitemap URL count equals the work count on disk (±known exclusions).** Sitemap:
   2,473 URLs (2,113 chunk pages + book/tome/distinction index pages + scripture pages +
   top-level pages). Matches `content.json`'s 2,113 questions plus the site's other
   routes. PASS.
7. **Vercel edge-request figure, day before / week after.** ⬜ Needs a week post-deploy.

## What shipped

- `LICENSE` §3a — machine-use clause, same wording as migne's.
- `/rights` — new "Machine Use" section between the licensing section and "So,
  Concretely".
- `public/robots.txt` — allow-all, no `Crawl-delay` (decision 3), full named-AI-UA list.
- `public/llms.txt` — new.
- `scripts/lib/reading-layer.mjs` — shared record builder (`buildRecord`, `toPlainText`,
  `chunkUrl`, `plainTextSibling`) used by both the siblings script and the export script.
- `scripts/build-siblings.mjs` — postbuild step, writes `.json` + `.plain.txt` per chunk
  into `out/` from `content.json` (not from the rendered HTML/RSC payload).
- `scripts/build-export.mjs` — bulk export (`jsonl.gz` + `txt.tar.gz` + `README.md` +
  `manifest.json`) into `~/bonaventure-sentences/export/`, plus a copy of `manifest.json`
  into `site/src/data/export-manifest.json` for the `/export` page.
- `src/app/export/page.tsx` — new page, lists the export manifest.
- `src/app/browse/[bookId]/d/[distId]/q/[qId]/page.tsx` — `generateMetadata` (canonical)
  + inline JSON-LD `CreativeWork` script tag.
- `src/app/sitemap.ts` — added `/export`.
- `package.json` — `build` now runs `build-export.mjs` before `next build` and
  `build-siblings.mjs` after; new `build-export` script.
- `.gitignore` (site + repo root) — `src/data/export-manifest.json`, `export/`.

## Known deviation from the other three sites

Sibling plain-text lives at `<slug>.plain.txt`, not `<slug>.txt` — Next's App Router
static export already emits `<slug>.txt` as the client-navigation RSC prefetch payload
for every page, so the plain `.txt` extension is unavailable at that path. `.json` was
free (Next writes no `.json` files at all) and is unchanged from the other sites'
convention. Documented in `llms.txt`.

## Deployed 2026-09-18

Pushed (`3e6e197`) and deployed to production (Wilson's OK on both, separately) —
`npx vercel deploy --prod --prebuilt --archive=tgz --scope wilson-pruitts-projects`
(bare `vercel deploy` returns `"Not authorized"`; the repo's own CLAUDE.md already
names the `--scope` fix). This deploy carried the already-closed *De perfectione
evangelica* work (pp. 117–198) live at the same time, per the migne precedent — one
deploy, not two. Verified by served content, not the status string: work page text
("canon right" from the work-close gate rulings), robots.txt, llms.txt, the rights
page's Machine Use clause, both `.json` and `.plain.txt` siblings, and the `/export`
page all confirmed live via `curl`.

## Not done in this session

- **R2 bucket provisioning** — shared across all four sites, its own hard stop (per the
  status log below CL's entry in `~/open-corpus/PLAN.md`).
- **HF org claim + dataset push** — after ≥2 exports exist on R2, per §4.
- **Vercel Firewall rate-limit backstop** — parked per-site rollout item, not yet done
  for any of the four shipped sites.

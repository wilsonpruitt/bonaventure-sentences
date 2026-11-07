"use client";

import { useEffect, useRef, useState } from "react";
import Link from "next/link";
import { GotoBox } from "@/components/goto-box";

// Pagefind's runtime is generated into out/pagefind/ by the post-build step
// (`pagefind --site out`). It does not exist under `next dev`; the page says so
// rather than failing silently.
interface PagefindResultData {
  url: string;
  excerpt: string; // HTML: Pagefind wraps matches in <mark>
  meta: { title?: string; context?: string };
}
interface PagefindResult {
  id: string;
  data: () => Promise<PagefindResultData>;
}
interface Pagefind {
  init: () => Promise<void>;
  search: (
    q: string,
    opts?: { filters?: Record<string, string> }
  ) => Promise<{ results: PagefindResult[] }>;
  filters: () => Promise<Record<string, Record<string, number>>>;
}

const PAGE_SIZE = 20;
const TOME_ORDER = ["I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX", "X"];

// Pagefind records exported pages as `…/chunk-id.html`; the site serves clean URLs.
const cleanUrl = (u: string) => u.replace(/\.html$/, "").replace(/\/index$/, "/");

async function loadPagefind(): Promise<Pagefind> {
  const path = "/pagefind/pagefind.js";
  const pf = (await import(/* webpackIgnore: true */ /* turbopackIgnore: true */ path)) as Pagefind;
  await pf.init();
  return pf;
}

export function SearchClient() {
  const pf = useRef<Pagefind | null>(null);
  const [status, setStatus] = useState<"loading" | "ready" | "unavailable">("loading");
  const [tomes, setTomes] = useState<string[]>([]);
  const [tome, setTome] = useState("");
  const [query, setQuery] = useState("");
  const [all, setAll] = useState<PagefindResult[]>([]);
  const [shown, setShown] = useState<PagefindResultData[]>([]);
  const [searched, setSearched] = useState(false);
  const [busy, setBusy] = useState(false);

  useEffect(() => {
    loadPagefind()
      .then(async (p) => {
        pf.current = p;
        const f = await p.filters();
        setTomes(
          Object.keys(f.tome ?? {}).sort(
            (a, b) =>
              TOME_ORDER.indexOf(a.replace("Tome ", "")) - TOME_ORDER.indexOf(b.replace("Tome ", ""))
          )
        );
        setStatus("ready");
      })
      .catch(() => setStatus("unavailable"));
  }, []);

  const doSearch = async () => {
    const q = query.trim();
    if (!pf.current || !q) {
      setAll([]);
      setShown([]);
      setSearched(false);
      return;
    }
    setBusy(true);
    const res = await pf.current.search(q, tome ? { filters: { tome } } : undefined);
    setAll(res.results);
    setShown(await Promise.all(res.results.slice(0, PAGE_SIZE).map((r) => r.data())));
    setSearched(true);
    setBusy(false);
  };

  const more = async () => {
    setBusy(true);
    const next = all.slice(shown.length, shown.length + PAGE_SIZE);
    const data = await Promise.all(next.map((r) => r.data()));
    setShown((s) => [...s, ...data]);
    setBusy(false);
  };

  return (
    <div>
      <GotoBox />
      <div className="section-title">Search the Corpus</div>
      <p className="card-meta" style={{ marginBottom: "1rem" }}>
        Searches the full Latin and English text of every chunk, with the editors&rsquo; notes. Put
        a phrase in quotation marks to match it exactly.
      </p>

      {status === "unavailable" && (
        <p className="body-text" style={{ color: "#6B4A3A" }}>
          The search index is not available. It is built with the site (<code>pnpm build</code>);
          it does not exist under the development server.
        </p>
      )}

      <div style={{ display: "flex", gap: "0.5rem", marginBottom: "0.75rem", flexWrap: "wrap" }}>
        <input
          type="text"
          value={query}
          onChange={(e) => setQuery(e.target.value)}
          onKeyDown={(e) => e.key === "Enter" && doSearch()}
          placeholder="Search Latin or English (e.g. veritas, “lumen gloriae”)…"
          className="search-input"
          style={{ flex: "1 1 260px" }}
          disabled={status !== "ready"}
          aria-label="Search terms"
        />
        <select
          value={tome}
          onChange={(e) => setTome(e.target.value)}
          className="search-input"
          style={{ flex: "0 0 auto" }}
          disabled={status !== "ready"}
          aria-label="Limit to a tome"
        >
          <option value="">All tomes</option>
          {tomes.map((t) => (
            <option key={t} value={t}>
              {t}
            </option>
          ))}
        </select>
        <button onClick={doSearch} className="search-btn" disabled={status !== "ready" || busy}>
          Search
        </button>
      </div>

      {shown.length > 0 && (
        <div>
          <p className="card-meta" style={{ margin: "1rem 0" }}>
            {all.length} result{all.length !== 1 ? "s" : ""}
          </p>
          {shown.map((r) => (
            <Link key={r.url} href={cleanUrl(r.url)} className="card-link">
              <div className="card">
                {r.meta.context && (
                  <p
                    style={{
                      fontSize: "12px",
                      color: "#8B6914",
                      fontFamily: "var(--font-cinzel), serif",
                      letterSpacing: "0.08em",
                      marginBottom: "0.25rem",
                    }}
                  >
                    {r.meta.context}
                  </p>
                )}
                <h3
                  style={{
                    fontFamily: "var(--font-cinzel), serif",
                    fontSize: "15px",
                    fontWeight: 500,
                    color: "#3D1308",
                    marginBottom: "0.5rem",
                  }}
                >
                  {r.meta.title ?? r.url}
                </h3>
                <p
                  className="search-excerpt"
                  style={{ fontSize: "13px", color: "#4A3A2A" }}
                  // Excerpt HTML comes from the site's own index (only <mark> tags).
                  dangerouslySetInnerHTML={{ __html: r.excerpt }}
                />
              </div>
            </Link>
          ))}
          {shown.length < all.length && (
            <div style={{ textAlign: "center", margin: "1.5rem 0" }}>
              <button onClick={more} className="search-btn" disabled={busy}>
                Show more
              </button>
            </div>
          )}
        </div>
      )}

      {searched && all.length === 0 && (
        <p className="body-text" style={{ color: "#6B4A3A", textAlign: "center", margin: "3rem 0" }}>
          No results for &ldquo;{query}&rdquo;.
        </p>
      )}
    </div>
  );
}

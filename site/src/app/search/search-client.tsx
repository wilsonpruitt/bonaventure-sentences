"use client";

import { useState } from "react";
import Link from "next/link";

interface SearchEntry {
  id: string;
  title: string;
  bookId: number;
  bookTitle: string;
  distId: number;
  distTitle: string;
  hasTranslation: boolean;
  latinPreview: string;
  englishPreview: string;
}

type SearchMode = "both" | "latin" | "english";

// Fold diacritics, ligatures, and the u/v distinction so queries like
// "veritas" match "ueritas", "æternus", "aeternus", and forms with macrons.
// Lowercase is applied at the call site.
function fold(s: string): string {
  return s
    .normalize("NFKD")
    .replace(/[\u0300-\u036f]/g, "")
    .replace(/æ/g, "ae")
    .replace(/œ/g, "oe")
    .replace(/v/g, "u")
    .replace(/j/g, "i");
}

export function SearchClient({ searchIndex }: { searchIndex: SearchEntry[] }) {
  const [query, setQuery] = useState("");
  const [mode, setMode] = useState<SearchMode>("both");
  const [results, setResults] = useState<SearchEntry[]>([]);
  const [searched, setSearched] = useState(false);

  const doSearch = () => {
    const q = query.trim();
    if (!q) {
      setResults([]);
      setSearched(false);
      return;
    }
    const needle = fold(q.toLowerCase());
    setResults(
      searchIndex.filter((entry) => {
        const title = fold(entry.title.toLowerCase());
        const lat = fold(entry.latinPreview.toLowerCase());
        const eng = fold(entry.englishPreview.toLowerCase());
        if (title.includes(needle)) return true;
        if (mode === "latin") return lat.includes(needle);
        if (mode === "english") return eng.includes(needle);
        return lat.includes(needle) || eng.includes(needle);
      })
    );
    setSearched(true);
  };

  // Build a short snippet showing the match in context. Falls back to the
  // first 150 chars if no match is found in the chosen preview field.
  const snippet = (text: string, needleFolded: string): string => {
    if (!text) return "";
    const folded = fold(text.toLowerCase());
    const idx = folded.indexOf(needleFolded);
    if (idx < 0) return text.substring(0, 150) + "…";
    const start = Math.max(0, idx - 60);
    const end = Math.min(text.length, idx + needleFolded.length + 90);
    const prefix = start > 0 ? "…" : "";
    const suffix = end < text.length ? "…" : "";
    return prefix + text.substring(start, end) + suffix;
  };

  const needle = fold(query.trim().toLowerCase());

  return (
    <div>
      <div className="section-title">Search the Corpus</div>
      <div
        style={{
          display: "flex",
          gap: "0.5rem",
          marginBottom: "0.75rem",
          flexWrap: "wrap",
        }}
      >
        <input
          type="text"
          value={query}
          onChange={(e) => setQuery(e.target.value)}
          onKeyDown={(e) => e.key === "Enter" && doSearch()}
          placeholder={
            mode === "latin"
              ? "Search Latin text (e.g. veritas, simplicitas)…"
              : mode === "english"
                ? "Search English translations…"
                : "Search Latin or English…"
          }
          className="search-input"
          style={{ flex: "1 1 260px" }}
        />
        <button onClick={doSearch} className="search-btn">
          Search
        </button>
      </div>

      <div
        style={{
          display: "flex",
          gap: "0.5rem",
          marginBottom: "1.5rem",
          fontFamily: "var(--font-cinzel), serif",
          fontSize: "11px",
          letterSpacing: "0.1em",
        }}
      >
        {(["both", "latin", "english"] as const).map((m) => (
          <button
            key={m}
            onClick={() => setMode(m)}
            className={mode === m ? "mode-toggle active" : "mode-toggle"}
            aria-pressed={mode === m}
          >
            {m === "both" ? "LATIN + ENGLISH" : m === "latin" ? "LATIN" : "ENGLISH"}
          </button>
        ))}
      </div>

      {results.length > 0 && (
        <div>
          <p className="card-meta" style={{ marginBottom: "1rem" }}>
            {results.length} result{results.length !== 1 ? "s" : ""} found
          </p>
          {results.map((r) => {
            const latSnip = snippet(r.latinPreview, needle);
            const engSnip = snippet(r.englishPreview, needle);
            const showLat =
              mode !== "english" && r.latinPreview && (mode === "latin" || fold(r.latinPreview.toLowerCase()).includes(needle));
            const showEng =
              mode !== "latin" && r.englishPreview && (mode === "english" || fold(r.englishPreview.toLowerCase()).includes(needle));
            return (
              <Link
                key={r.id}
                href={`/browse/${r.bookId}/d/${r.distId}/q/${encodeURIComponent(r.id)}`}
                className="card-link"
              >
                <div className="card">
                  <p
                    style={{
                      fontSize: "12px",
                      color: "#8B6914",
                      fontFamily: "var(--font-cinzel), serif",
                      letterSpacing: "0.08em",
                      marginBottom: "0.25rem",
                    }}
                  >
                    {r.bookTitle} &middot; {r.distTitle}
                    {!r.hasTranslation && (
                      <span style={{ marginLeft: "0.5rem", color: "#B8862A" }}>
                        · Latin only
                      </span>
                    )}
                  </p>
                  <h3
                    style={{
                      fontFamily: "var(--font-cinzel), serif",
                      fontSize: "15px",
                      fontWeight: 500,
                      color: "#3D1308",
                      marginBottom: "0.5rem",
                    }}
                  >
                    {r.title}
                  </h3>
                  {showLat && (
                    <p
                      style={{
                        fontSize: "13px",
                        color: "#4A3A2A",
                        fontStyle: "italic",
                        marginBottom: showEng ? "0.35rem" : 0,
                      }}
                    >
                      {latSnip}
                    </p>
                  )}
                  {showEng && (
                    <p style={{ fontSize: "13px", color: "#6B4A3A" }}>
                      {engSnip}
                    </p>
                  )}
                </div>
              </Link>
            );
          })}
        </div>
      )}

      {searched && results.length === 0 && (
        <p
          className="body-text"
          style={{ color: "#6B4A3A", textAlign: "center", margin: "3rem 0" }}
        >
          No results found for &ldquo;{query}&rdquo;. Try different terms or switch
          search mode.
        </p>
      )}
    </div>
  );
}

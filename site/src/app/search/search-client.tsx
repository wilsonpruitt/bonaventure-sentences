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
  englishPreview: string;
}

export function SearchClient({ searchIndex }: { searchIndex: SearchEntry[] }) {
  const [query, setQuery] = useState("");
  const [results, setResults] = useState<SearchEntry[]>([]);
  const [searched, setSearched] = useState(false);

  const doSearch = () => {
    if (!query.trim()) {
      setResults([]);
      setSearched(false);
      return;
    }
    const lower = query.toLowerCase();
    setResults(
      searchIndex.filter(
        (entry) =>
          entry.title.toLowerCase().includes(lower) ||
          entry.englishPreview.toLowerCase().includes(lower)
      )
    );
    setSearched(true);
  };

  return (
    <div>
      <div className="section-title">Search Translations</div>
      <div style={{ display: "flex", gap: "0.5rem", marginBottom: "1.5rem" }}>
        <input
          type="text"
          value={query}
          onChange={(e) => setQuery(e.target.value)}
          onKeyDown={(e) => e.key === "Enter" && doSearch()}
          placeholder="Search English translations..."
          className="search-input"
        />
        <button onClick={doSearch} className="search-btn">
          Search
        </button>
      </div>

      {results.length > 0 && (
        <div>
          <p className="card-meta" style={{ marginBottom: "1rem" }}>
            {results.length} result{results.length !== 1 ? "s" : ""} found
          </p>
          {results.map((r) => (
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
                <p style={{ fontSize: "13px", color: "#6B4A3A" }}>
                  {r.englishPreview.substring(0, 150)}...
                </p>
              </div>
            </Link>
          ))}
        </div>
      )}

      {searched && results.length === 0 && (
        <p className="body-text" style={{ color: "#6B4A3A", textAlign: "center", margin: "3rem 0" }}>
          No results found for &ldquo;{query}&rdquo;. Try different terms.
        </p>
      )}
    </div>
  );
}

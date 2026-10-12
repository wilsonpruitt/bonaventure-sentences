"use client";

import { useEffect, useState } from "react";
import type { ApparatusEntry } from "@/lib/content";

type PageMode = "off" | "margin" | "inline";

const PAGE_MODE_KEY = "bonaventure.pageMode";
const PAGE_MODE_ORDER: PageMode[] = ["off", "margin", "inline"];
const PAGE_MODE_LABEL: Record<PageMode, string> = {
  off: "Page markers: off",
  margin: "Page markers: margin",
  inline: "Page markers: inline",
};

export function TextReader({
  latin,
  english,
  latinScholion,
  englishScholion,
  apparatus,
  hasTranslation,
}: {
  latin: string;
  english: string;
  latinScholion: string;
  englishScholion: string;
  apparatus: ApparatusEntry[];
  hasTranslation: boolean;
}) {
  const [viewMode, setViewMode] = useState(hasTranslation ? "parallel" : "latin");
  const [pageMode, setPageMode] = useState<PageMode>("margin");

  useEffect(() => {
    try {
      const saved = localStorage.getItem(PAGE_MODE_KEY) as PageMode | null;
      if (saved && PAGE_MODE_ORDER.includes(saved)) setPageMode(saved);
    } catch {}
  }, []);

  useEffect(() => {
    try {
      localStorage.setItem(PAGE_MODE_KEY, pageMode);
    } catch {}
  }, [pageMode]);

  const cyclePageMode = () => {
    const idx = PAGE_MODE_ORDER.indexOf(pageMode);
    setPageMode(PAGE_MODE_ORDER[(idx + 1) % PAGE_MODE_ORDER.length]);
  };

  const modes = hasTranslation
    ? [
        { key: "parallel", label: "Parallel" },
        { key: "latin", label: "Latin Only" },
        { key: "english", label: "English Only" },
      ]
    : [
        { key: "latin", label: "Latin Only" },
        { key: "english", label: "English (Pending)" },
      ];

  const hasApparatus = apparatus.length > 0;

  return (
    <>
      <div className="view-toggle">
        {modes.map((m) => (
          <button
            key={m.key}
            onClick={() => setViewMode(m.key)}
            className={`view-btn ${viewMode === m.key ? "active" : ""}`}
          >
            {m.label}
          </button>
        ))}
        <button
          onClick={cyclePageMode}
          className="view-btn"
          style={{ marginLeft: "auto" }}
          title="Toggle page-break marker display"
        >
          {PAGE_MODE_LABEL[pageMode]}
        </button>
      </div>

      {viewMode === "parallel" ? (
        <div className="parallel-grid">
          <TextColumn
            label="Textus Latinus"
            body={latin}
            scholion={latinScholion}
            pageMode={pageMode}
            className="latin-text"
          />
          <TextColumn
            label="English Translation"
            body={english}
            scholion={englishScholion}
            pageMode={pageMode}
            className="english-text"
            pendingFallback={!hasTranslation}
          />
        </div>
      ) : viewMode === "latin" ? (
        <div style={{ maxWidth: "700px" }}>
          <TextColumn
            label="Textus Latinus"
            body={latin}
            scholion={latinScholion}
            pageMode={pageMode}
            className="latin-text"
          />
        </div>
      ) : (
        <div style={{ maxWidth: "700px" }}>
          <TextColumn
            label="English Translation"
            body={english}
            scholion={englishScholion}
            pageMode={pageMode}
            className="english-text"
            pendingFallback={!hasTranslation}
          />
        </div>
      )}

      {hasApparatus && <ApparatusBlock apparatus={apparatus} />}
    </>
  );
}

function TextColumn({
  label,
  body,
  scholion,
  pageMode,
  className,
  pendingFallback,
}: {
  label: string;
  body: string;
  scholion: string;
  pageMode: PageMode;
  className: string;
  pendingFallback?: boolean;
}) {
  return (
    <div>
      <div className="section-title" style={{ fontSize: "12px" }}>
        {label}
      </div>
      <div className="text-column">
        {pendingFallback ? (
          <p className={className} style={{ color: "#8B6914", fontStyle: "italic" }}>
            Translation not yet available for this section.
          </p>
        ) : (
          renderBody(body, className, pageMode)
        )}
      </div>
      {scholion && !pendingFallback && (
        <Scholion text={scholion} className={className} pageMode={pageMode} />
      )}
    </div>
  );
}

function Scholion({
  text,
  className,
  pageMode,
}: {
  text: string;
  className: string;
  pageMode: PageMode;
}) {
  return (
    <div className="scholion-block">
      <div className="scholion-label">Scholion</div>
      <div className="text-column">{renderBody(text, className, pageMode)}</div>
    </div>
  );
}

function ApparatusBlock({ apparatus }: { apparatus: ApparatusEntry[] }) {
  // Translator's notes (`tr-` labels) are ours, not Quaracchi's: they render in
  // their own block, after the edition's apparatus, and are never mixed into it.
  const editorial = apparatus.filter((e) => !isTranslatorNote(e.id));
  const translator = apparatus.filter((e) => isTranslatorNote(e.id));
  return (
    <div className="apparatus-block">
      {editorial.length > 0 && (
        <>
          <div className="section-title" style={{ fontSize: "12px" }}>
            Apparatus Criticus
          </div>
          <ol className="apparatus-list">
            {editorial.map((e) => (
              <li key={e.id} id={`fn-${e.id}`} className="apparatus-entry">
                <span className="apparatus-num">{displayLabel(e.id)}</span>
                <div className="apparatus-la">{renderInline(e.la)}</div>
                {e.en && <div className="apparatus-en">{renderInline(e.en)}</div>}
              </li>
            ))}
          </ol>
        </>
      )}
      {translator.length > 0 && (
        <div className="translator-notes">
          <div className="section-title" style={{ fontSize: "12px" }}>
            Translator&rsquo;s Notes
          </div>
          <ol className="apparatus-list">
            {translator.map((e) => (
              <li key={e.id} id={`fn-${e.id}`} className="apparatus-entry apparatus-entry-tr">
                <span className="apparatus-num">{displayLabel(e.id)}</span>
                <div className="apparatus-en">{renderInline(e.en)}</div>
              </li>
            ))}
          </ol>
        </div>
      )}
    </div>
  );
}

// Translator's notes (the dikaisune rule, 2026-09-15): an English-only note in
// our own voice, labelled `tr-<word>` in the chunk and shown as "tr.".
function isTranslatorNote(id: string): boolean {
  return id.startsWith("tr-");
}

// --- Rendering helpers ------------------------------------------------------

// Apparatus labels are page-qualified internally (`p909-1`, `p983c-2`, `p904-n1`)
// so that Quaracchi's per-printed-page footnote restarts can't collide into
// duplicate definitions — a duplicate silently drops entries at render time.
// The reader should still see the number the page actually prints, so strip the
// `p<page>` namespace and show the rest. Bare labels (`12`, `2b`) pass through.
function displayLabel(id: string): string {
  if (isTranslatorNote(id)) return "tr.";
  const m = id.match(/^p\d+[a-z]*-(.+)$/);
  return m ? m[1] : id;
}

function renderBody(body: string, className: string, pageMode: PageMode) {
  if (!body) return null;
  const paragraphs = body.split(/\n{2,}/);
  const nodes: React.ReactNode[] = [];
  paragraphs.forEach((para, i) => {
    const trimmed = para.trim();
    if (!trimmed) return;

    const pageOnly = trimmed.match(/^<!--\s*page\s+(\d+)\s*-->$/);
    if (pageOnly) {
      if (pageMode !== "off") {
        nodes.push(
          <PageMarker key={`p-${i}`} page={pageOnly[1]} mode={pageMode} standalone />
        );
      }
      return;
    }

    const headingRe = /^(####|###)\s+([^\n]+)(?:\n([\s\S]*))?$/;
    if (headingRe.test(trimmed)) {
      let remainder: string = trimmed;
      let headingIdx = 0;
      while (remainder.length > 0) {
        const m: RegExpMatchArray | null = remainder.match(headingRe);
        if (!m) break;
        const [, hashes, headingText, rest] = m;
        const Tag = hashes === "####" ? "h4" : "h3";
        const cls = hashes === "####" ? "reader-h4" : "reader-h3";
        nodes.push(
          <Tag key={`h-${i}-${headingIdx}`} className={cls}>
            {renderInline(headingText, pageMode)}
          </Tag>
        );
        headingIdx += 1;
        remainder = rest?.trim() ?? "";
      }
      if (remainder.length > 0) {
        nodes.push(
          <p key={`h-${i}-rest`} className={className} style={{ marginBottom: "1rem" }}>
            {renderInline(remainder, pageMode)}
          </p>
        );
      }
      return;
    }

    if (trimmed.startsWith("> ")) {
      const quoted = trimmed.replace(/^>\s?/gm, "");
      nodes.push(
        <blockquote key={i} className={`reader-blockquote ${className}`}>
          {renderInline(quoted, pageMode)}
        </blockquote>
      );
      return;
    }

    // A paragraph whose every line is a `- ` item (two spaces of indent per
    // level) is a NESTED INDENTED OUTLINE — the printed bracket-tree schemata
    // (Vol VI ruling 18: Commentarius in Ecclesiasten, Schemata I–IV). No other
    // body paragraph in the corpus has this shape, so nothing else changes.
    const outlineLines = para.split("\n").filter((l) => l.trim().length > 0);
    if (outlineLines.length > 0 && outlineLines.every((l) => /^( *)- \S/.test(l))) {
      nodes.push(
        <div key={i} className={className} style={{ marginBottom: "1rem" }}>
          {renderOutline(outlineLines, pageMode)}
        </div>
      );
      return;
    }

    if (/^(CONCLUSION\.|DOUBT\s+[IVXLCDM]+\.?)$/i.test(trimmed)) {
      nodes.push(
        <p key={i} className="conclusion-header">
          {trimmed}
        </p>
      );
      return;
    }

    nodes.push(
      <p key={i} className={className} style={{ marginBottom: "1rem" }}>
        {renderInline(trimmed, pageMode)}
      </p>
    );
  });
  return nodes;
}

type OutlineNode = { text: string; children: OutlineNode[] };

// Parse `- ` lines (depth = leading spaces / 2) into a tree and render it as
// nested lists. Each level below the root is indented and carries a faint
// left rule standing for the printed brace, so the depth reads at phone width.
function renderOutline(lines: string[], pageMode: PageMode): React.ReactNode {
  const root: OutlineNode = { text: "", children: [] };
  const stack: { depth: number; node: OutlineNode }[] = [{ depth: -1, node: root }];
  for (const line of lines) {
    const m = line.match(/^( *)- (.*)$/);
    if (!m) continue;
    const depth = Math.floor(m[1].length / 2);
    const node: OutlineNode = { text: m[2], children: [] };
    while (stack.length > 1 && stack[stack.length - 1].depth >= depth) stack.pop();
    stack[stack.length - 1].node.children.push(node);
    stack.push({ depth, node });
  }
  const renderLevel = (nodes: OutlineNode[], depth: number, keyPrefix: string): React.ReactNode => (
    <ul
      style={{
        listStyle: "none",
        margin: depth === 0 ? 0 : "0.15rem 0 0.15rem 0.3rem",
        padding: depth === 0 ? 0 : "0 0 0 0.7rem",
        borderLeft: depth === 0 ? "none" : "1px solid rgba(128, 128, 128, 0.45)",
      }}
    >
      {nodes.map((n, idx) => (
        <li key={`${keyPrefix}-${idx}`} style={{ margin: "0.1rem 0" }}>
          {renderInline(n.text, pageMode)}
          {n.children.length > 0 && renderLevel(n.children, depth + 1, `${keyPrefix}-${idx}`)}
        </li>
      ))}
    </ul>
  );
  return renderLevel(root.children, 0, "o");
}

function renderInline(text: string, pageMode: PageMode = "off"): React.ReactNode[] {
  const tokens: React.ReactNode[] = [];
  const regex = /<!--\s*page\s+(\d+)\s*-->|\[\^([^\]]+)\]|\*\*([^*]+)\*\*|\*([^*]+)\*/g;
  let lastIndex = 0;
  let m: RegExpExecArray | null;
  let key = 0;
  while ((m = regex.exec(text)) !== null) {
    if (m.index > lastIndex) {
      tokens.push(text.slice(lastIndex, m.index));
    }
    if (m[1] !== undefined) {
      if (pageMode !== "off") {
        tokens.push(<PageMarker key={`pm-${key++}`} page={m[1]} mode={pageMode} />);
      }
    } else if (m[2] !== undefined) {
      const id = m[2];
      tokens.push(
        <sup key={`fn-${key++}`} className={isTranslatorNote(id) ? "fn-ref fn-ref-tr" : "fn-ref"}>
          <a href={`#fn-${id}`}>{displayLabel(id)}</a>
        </sup>
      );
    } else if (m[3] !== undefined) {
      tokens.push(<strong key={`b-${key++}`}>{m[3]}</strong>);
    } else if (m[4] !== undefined) {
      tokens.push(<em key={`i-${key++}`}>{m[4]}</em>);
    }
    lastIndex = regex.lastIndex;
  }
  if (lastIndex < text.length) tokens.push(text.slice(lastIndex));
  return tokens;
}

function PageMarker({
  page,
  mode,
  standalone,
}: {
  page: string;
  mode: PageMode;
  standalone?: boolean;
}) {
  const label = `p. ${page}`;
  if (standalone) {
    return (
      <div className={`page-marker page-marker-${mode} page-marker-standalone`}>
        {label}
      </div>
    );
  }
  return <span className={`page-marker page-marker-${mode}`}>{label}</span>;
}

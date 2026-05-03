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
  return (
    <div className="apparatus-block">
      <div className="section-title" style={{ fontSize: "12px" }}>
        Apparatus Criticus
      </div>
      <ol className="apparatus-list">
        {apparatus.map((e) => (
          <li key={e.id} id={`fn-${e.id}`} className="apparatus-entry">
            <div className="apparatus-la">{renderInline(e.la)}</div>
            {e.en && <div className="apparatus-en">{renderInline(e.en)}</div>}
          </li>
        ))}
      </ol>
    </div>
  );
}

// --- Rendering helpers ------------------------------------------------------

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

    const headingLead = trimmed.match(/^(####|###)\s+([^\n]+)(?:\n([\s\S]*))?$/);
    if (headingLead) {
      const [, hashes, headingText, rest] = headingLead;
      const Tag = hashes === "####" ? "h4" : "h3";
      const cls = hashes === "####" ? "reader-h4" : "reader-h3";
      nodes.push(
        <Tag key={`h-${i}`} className={cls}>
          {renderInline(headingText, pageMode)}
        </Tag>
      );
      if (rest && rest.trim()) {
        nodes.push(
          <p key={`h-${i}-rest`} className={className} style={{ marginBottom: "1rem" }}>
            {renderInline(rest.trim(), pageMode)}
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
        <sup key={`fn-${key++}`} className="fn-ref">
          <a href={`#fn-${id}`}>{id}</a>
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

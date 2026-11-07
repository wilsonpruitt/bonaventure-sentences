import { joinPageTurns } from "./paragraphs";

// Section headings of a chunk body, in render order, with stable anchor ids.
// The walk mirrors renderParas in text-reader.tsx exactly: a paragraph that
// OPENS with ###/#### is a heading paragraph, and further headings follow only
// while each remainder still opens with one. Ids come from the LATIN headings,
// so they do not change when the English is revised.

export const HEADING_RE = /^(####|###)\s+([^\n]+)(?:\n([\s\S]*))?$/;

export function collectHeadings(body: string): string[] {
  const out: string[] = [];
  for (const para of joinPageTurns(body)) {
    let rest = para.trim();
    let m = rest.match(HEADING_RE);
    while (m) {
      out.push(m[2]);
      rest = m[3]?.trim() ?? "";
      m = rest.match(HEADING_RE);
    }
  }
  return out;
}

/** Heading text for display: footnote refs, page markers and emphasis removed. */
export function plainHeading(h: string): string {
  return h
    .replace(/\[\^[^\]]+\]/g, "")
    .replace(/<!--[\s\S]*?-->/g, "")
    .replace(/[*_]/g, "")
    .replace(/\s+/g, " ")
    .trim();
}

const ROMAN: Record<string, number> = { I: 1, V: 5, X: 10, L: 50, C: 100, D: 500, M: 1000 };
function numeral(s: string): number | null {
  if (/^\d+$/.test(s)) return Number(s);
  const u = s.toUpperCase();
  if (!/^[IVXLCDM]+$/.test(u)) return null;
  let n = 0;
  for (let i = 0; i < u.length; i++) {
    const v = ROMAN[u[i]], w = ROMAN[u[i + 1]] ?? 0;
    n += v < w ? -v : v;
  }
  return n;
}

// Named units get readable ids (#coll-18, #annot-22, #dub-3, #q-2…), which is
// what Phase 3's anchor-level cross-references will point at; anything else
// is #sec-N by position.
const NAMED: [RegExp, string][] = [
  [/^collatio\s+([ivxlcdm]+|\d+)\b/i, "coll"],
  [/^annotatio\s+(\d+|[ivxlcdm]+)\b/i, "annot"],
  [/^dub(?:ium|\.)?\s+([ivxlcdm]+|\d+)\b/i, "dub"],
  [/^quaestio\s+([ivxlcdm]+|\d+)\b/i, "q"],
  [/^articulus\s+([ivxlcdm]+|\d+)\b/i, "a"],
  [/^capitulum\s+([ivxlcdm]+|\d+)\b/i, "c"],
  [/^pars\s+([ivxlcdm]+|\d+)\b/i, "p"],
  [/^sermo\s+([ivxlcdm]+|\d+)\b/i, "sermo"],
];
const FIXED: [RegExp, string][] = [
  [/^conclusio\b/i, "conclusio"],
  [/^summarium\b/i, "summarium"],
  [/^scholion\b/i, "scholion"],
  [/^prolog(?:us|i)\b/i, "prologus"],
];

export function headingIds(latinHeadings: string[]): string[] {
  const used = new Set<string>();
  return latinHeadings.map((h, i) => {
    const t = plainHeading(h);
    let id = `sec-${i + 1}`;
    for (const [re, pre] of NAMED) {
      const m = t.match(re);
      const n = m && numeral(m[1]);
      if (n) { id = `${pre}-${n}`; break; }
    }
    if (id.startsWith("sec-")) for (const [re, name] of FIXED) if (re.test(t)) { id = name; break; }
    let unique = id;
    for (let k = 2; used.has(unique); k++) unique = `${id}-${k}`;
    used.add(unique);
    return unique;
  });
}

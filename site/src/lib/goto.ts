// The go-to box (SITE-PLAN Phase 3): a Quaracchi citation, typed as a reader
// would type it, to the passage. Self-contained (no imports) so the test harness
// can run it under plain node.
//
// The data (public/goto.json, from tools/build-index-json.py) lists every chunk
// with its coordinates. Resolution is the citation ledger's own rule
// (tools/build-citations.py resolve_locus): every coordinate the citation does
// not state is a wildcard, and only a UNIQUE surviving chunk resolves. A
// citation naming a distinction but no article or question lands on the
// distinction; one naming a work but no unit lands on the work.

export interface GotoChunk {
  id: string;
  path: string;
  w: string; // work slug, "sentences" for Tomes I–IV
  t?: Record<string, number>; // coordinates: b d p s a q (Sentences) · p c q a s (works)
  type?: string; // dubia, littera, divisio, prol, scholion…
  v?: [number, number]; // verse range (Scripture commentaries)
  n?: [number, number]; // Quaracchi paragraph range (John commentary)
  u?: Record<string, number[]>; // Collationes in Ioannem units
}
export interface GotoData {
  works: Record<string, string[]>;
  chunks: GotoChunk[];
  pages: Record<string, string[]>; // "tome:page" -> chunk paths
}
/** Where the citation is written, for forms that lean on it (`supra d. 17…`). */
export interface GotoContext {
  book?: number; // Sentences book of the citing text
  tome?: number; // Quaracchi tome of the citing text
  work?: string; // work slug of the citing text
}
export type GotoResult =
  | { kind: "chunk"; path: string; id: string; anchor?: string }
  | { kind: "level"; path: string; label: string } // a distinction or a whole work
  | { kind: "many"; label: string; options: { path: string; id: string }[] }
  | { kind: "none"; label: string };

const ROMAN: Record<string, number> = { I: 1, V: 5, X: 10, L: 50, C: 100 };
function num(s: string): number | null {
  if (/^\d+$/.test(s)) return Number(s);
  const u = s.toUpperCase();
  if (!/^[IVXLC]+$/.test(u)) return null;
  let n = 0;
  for (let i = 0; i < u.length; i++) {
    const v = ROMAN[u[i]], w = ROMAN[u[i + 1]] ?? 0;
    n += v < w ? -v : v;
  }
  return n;
}

// One coordinate token: label + number. Labels the corpus prints.
const TOKEN_RE =
  /\b(pars|p|sectio|sect|articulus|art|a|quaestio|quaest|q|dubium|dub|capitulum|cap|c|collatio|collat|coll|sermo|serm|annotatio|annotat|annot|n|versus|vers|v|d)\b\.?\s*([IVXLC]+|\d+)\b/gi;

type Token = { label: string; n: number };
function tokens(s: string): Token[] {
  const out: Token[] = [];
  for (const m of s.matchAll(TOKEN_RE)) {
    const n = num(m[2]);
    if (n !== null) out.push({ label: m[1].toLowerCase(), n });
  }
  return out;
}

// What a typed label means in each work. Hexaemeron, septem donis and decem
// praeceptis are cut one chunk per collatio (`coll. N` = chunk cN); Quaracchi
// also cites the Hexaemeron's collations as `serm. N`. In the Collationes in
// Ioannem a collatio is a UNIT inside a capitulum chunk.
function workKey(work: string, label: string): string | null {
  const l = label;
  if (["pars", "p"].includes(l)) return "p";
  if (["sectio", "sect"].includes(l)) return "s";
  if (["articulus", "art", "a"].includes(l)) return "a";
  if (["quaestio", "quaest", "q"].includes(l)) return "q";
  if (["capitulum", "cap", "c"].includes(l)) return "c";
  if (["versus", "vers", "v"].includes(l)) return "verse";
  if (l === "n") return "para";
  if (["annotatio", "annotat", "annot"].includes(l)) return "annot";
  if (["collatio", "collat", "coll"].includes(l))
    return work === "collationes-ioannem" ? "coll" : "c";
  if (["sermo", "serm"].includes(l)) return work === "sermones-selecti" ? "s" : "c";
  return null;
}

function pick(cands: GotoChunk[], label: string, anchor?: string): GotoResult {
  if (cands.length === 1) return { kind: "chunk", path: cands[0].path, id: cands[0].id, anchor };
  if (cands.length > 1)
    return { kind: "many", label, options: cands.slice(0, 40).map((c) => ({ path: c.path, id: c.id })) };
  return { kind: "none", label: `${label}: no such passage in the translation yet` };
}

function resolveSentences(data: GotoData, book: number, rest: string): GotoResult {
  const prooem = /\bpro(?:o|œ)?em/i.test(rest);
  const toks = tokens(rest);
  const dTok = toks.find((t) => t.label === "d");
  const dist = prooem ? 0 : dTok?.n;
  const label = `${["I", "II", "III", "IV"][book - 1]} Sent.`;
  if (dist === undefined) return { kind: "level", path: `/sentences/${book}`, label };
  const want: Record<string, number> = {};
  let dub: number | undefined;
  for (const t of toks) {
    if (t.label === "d") continue;
    if (t.label === "dub" || t.label === "dubium") dub = t.n;
    else {
      const k = workKey("sentences", t.label);
      if (k && ["p", "s", "a", "q"].includes(k)) want[k] = t.n;
    }
  }
  const sib = data.chunks.filter((c) => c.w === "sentences" && c.t?.b === book && c.t?.d === dist);
  if (!sib.length) return { kind: "none", label: `${label} d. ${dist}: not found` };
  if (dub === undefined && want.q === undefined && want.a === undefined) {
    return dist === 0
      ? { kind: "many", label: `${label} prooemium`, options: sib.map((c) => ({ path: c.path, id: c.id })) }
      : { kind: "level", path: `/sentences/${book}/d${dist}`, label: `${label} d. ${dist}` };
  }
  // `dub. N` names a unit INSIDE the distinction's (or pars's) dubia chunk.
  const hits = sib.filter(
    (c) =>
      (["p", "s", "a", "q"] as const).every((k) => want[k] === undefined || c.t?.[k] === want[k]) &&
      (dub === undefined || (c.type ?? "").startsWith("dub"))
  );
  return pick(hits, `${label} d. ${dist}`, dub !== undefined ? `dub-${dub}` : undefined);
}

function resolveWork(data: GotoData, work: string, rest: string): GotoResult {
  const cands0 = data.chunks.filter((c) => c.w === work);
  const toks = tokens(rest);
  if (!toks.length) return { kind: "level", path: `/${work}`, label: work };
  let cands = cands0;
  let anchor: string | undefined;
  for (const t of toks) {
    const k = workKey(work, t.label);
    if (!k) continue;
    if (k === "verse") cands = cands.filter((c) => c.v && c.v[0] <= t.n && t.n <= c.v[1]);
    else if (k === "para") {
      // In the John commentary `n.` is the Quaracchi paragraph (ruling 73);
      // elsewhere a paragraph inside the chunk, which does not move the target.
      if (cands.some((c) => c.n)) {
        cands = cands.filter((c) => c.n && c.n[0] <= t.n && t.n <= c.n[1]);
        anchor = `n-${t.n}`;
      }
    } else if (k === "coll" || k === "annot") {
      const kind = k === "coll" ? "collationes" : "annotationes";
      cands = cands.filter((c) => c.u?.[kind]?.includes(t.n));
      anchor = `${k}-${t.n}`;
    } else cands = cands.filter((c) => c.t?.[k] === t.n);
  }
  return pick(cands, work, anchor);
}

// An abbreviation matches with its points optional and spacing free:
// "Collat. in Ioan." matches "collat in ioan", "Collat.in Ioan." and so on.
const abbrevRe = (ab: string) =>
  new RegExp(
    "^" +
      ab
        .split(/[.\s]+/)
        .filter(Boolean)
        .map((w) => w.replace(/[.*+?^${}()|[\]\\]/g, "\\$&"))
        .join("\\.?\\s*") +
      "\\.?(?=\\s|$|,)",
    "i"
  );

function matchWork(data: GotoData, s: string): { work: string; rest: string } | null {
  let best: { work: string; end: number } | null = null;
  for (const [work, abbrevs] of Object.entries(data.works))
    for (const ab of abbrevs) {
      const m = s.match(abbrevRe(ab));
      if (m && (!best || m[0].length > best.end)) best = { work, end: m[0].length };
    }
  return best ? { work: best.work, rest: s.slice(best.end) } : null;
}

export function goTo(input: string, data: GotoData, ctx: GotoContext = {}): GotoResult {
  const s = input.replace(/\*/g, "").replace(/\s+/g, " ").replace(/^(?:cfr|vide|cf)\.?\s+/i, "").trim();
  if (!s) return { kind: "none", label: "Type a citation" };

  // Printed page: `tom. VI. pag. 567`, `tom. 6, 567`, `supra pag. 72` (tome from context).
  const pg =
    s.match(/\btom\.?\s*([IVX]+|\d+)\b\.?,?\s*(?:pag\.?|p\.)?\s*(\d{1,4})\b/i) ??
    s.match(/^(?:(?:supra|infra|ibid)\.?\s*)?()pag\.\s*(\d{1,4})\b/i);
  if (pg) {
    const tome = pg[1] ? num(pg[1]) : (ctx.tome ?? null);
    if (!tome) return { kind: "none", label: "Give the tome too, e.g. tom. VI pag. 567" };
    const paths = data.pages[`${tome}:${pg[2]}`] ?? [];
    const label = `tom. ${tome}, p. ${pg[2]}`;
    if (paths.length === 1) return { kind: "chunk", path: paths[0], id: "" };
    if (paths.length > 1) return { kind: "many", label, options: paths.map((p) => ({ path: p, id: "" })) };
    return { kind: "none", label: `${label}: not in the translation yet` };
  }

  // Sentences: `I. Sent. d. 3. p. 1. a. 1. q. 2`, `IV Sent. d. 15 p. I q. 1`.
  const sent = s.match(/^(?:([IV]+|[1-4])\.?\s*)?Sent(?:ent(?:iarum|ias)?)?\.?\s*(.*)$/i);
  if (sent) {
    const book = sent[1] ? num(sent[1]) : (ctx.book ?? null);
    if (!book || book > 4) return { kind: "none", label: "Which book of the Sentences? e.g. I Sent. d. 3" };
    return resolveSentences(data, book, sent[2]);
  }
  // Same-book forms, which need the citing book: `supra d. 17. p. 1. q. 2`, `d. 29. a. 1`.
  const rel = s.match(/^(?:(?:supra|infra|ibid)\.?\s*)?(d\.\s*\d+.*)$/i);
  if (rel) {
    if (ctx.book) return resolveSentences(data, ctx.book, rel[1]);
    if (!matchWork(data, s)) return { kind: "none", label: "Which book of the Sentences? e.g. I Sent. d. 3" };
  }

  const w = matchWork(data, s);
  if (w) return resolveWork(data, w.work, w.rest);
  // A unit with no work named (`Collat. XVIII.`) means the work it is written in.
  if (ctx.work && tokens(s).length) return resolveWork(data, ctx.work, s);

  return { kind: "none", label: "Not a citation form this box knows yet" };
}

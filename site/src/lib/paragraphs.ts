// Paragraph handling shared by the reader (client) and the server-rendered
// contents box, so both see exactly the same paragraphs and headings.
// Moved verbatim from text-reader.tsx (SITE-PLAN Phase 1).

export const PAGE_ONLY_RE = /^<!--\s*page\s+(\d+)\s*-->$/;
export const HEADING_START_RE = /^#{3,4}\s/;
export const CONCLUSION_RE = /^(CONCLUSION\.|DOUBT\s+[IVXLCDM]+\.?)$/i;

export function isOutline(para: string): boolean {
  const lines = para.split("\n").filter((l) => l.trim().length > 0);
  return lines.length > 0 && lines.every((l) => /^( *)- \S/.test(l));
}

// Running prose — the only kind of paragraph a page marker may be folded into.
function isProse(para: string): boolean {
  return (
    !HEADING_START_RE.test(para) &&
    !para.startsWith(">") &&
    !para.startsWith("<!--") &&
    !para.startsWith("---") &&
    !CONCLUSION_RE.test(para) &&
    !isOutline(para)
  );
}

// Does `next` carry on the sentence that `prev` broke off at a page turn?
// A lowercase start always does (incl. the 345 words hyphenated across the
// turn); otherwise only when `prev` stops without closing punctuation and
// `next` does not open a numbered argument or a bold rubric.
function continuesAcross(prev: string, next: string): boolean {
  if (/^\d+\.\s/.test(next) || next.startsWith("**")) return false;
  if (/^\p{Ll}/u.test(next)) return true;
  const last = prev.split("\n").pop()!.trimEnd();
  return !/[.!?»)\]*"”]$/.test(last);
}

// The chunks store every page turn as its own paragraph (`<!-- page N -->`
// between blank lines), even mid-sentence, which split the sentence in two
// around a block marker. Fold each marker into the text instead: a turn inside
// a sentence rejoins the halves (no space after a hyphen, so `quae-` + `stio`
// reads as printed); a turn at a real paragraph break goes onto the start of
// the next paragraph. Either way the marker renders inline (margin or boxed)
// and adds no vertical space. Markers next to headings stay standalone.
export function joinPageTurns(body: string): string[] {
  if (!body) return [];
  const paras = body.split(/\n{2,}/).map((p) => p.trim()).filter(Boolean);
  const out: string[] = [];
  for (let i = 0; i < paras.length; i++) {
    const para = paras[i];
    const next = paras[i + 1];
    if (!PAGE_ONLY_RE.test(para) || next === undefined || !isProse(next)) {
      out.push(para);
      continue;
    }
    const prev = out[out.length - 1];
    if (prev !== undefined && isProse(prev) && continuesAcross(prev, next)) {
      out[out.length - 1] = prev.endsWith("-") ? prev + para + next : `${prev} ${para}${next}`;
    } else {
      out.push(para + next);
    }
    i += 1;
  }
  return out;
}


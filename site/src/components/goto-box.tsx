"use client";

import { useRef, useState } from "react";
import { useRouter } from "next/navigation";
import Link from "next/link";
import { goTo, type GotoData, type GotoResult } from "@/lib/goto";

// "Go to a citation": type a Quaracchi reference, land on the passage.
// goto.json (~0.5 MB) is fetched on first use only.
let cache: Promise<GotoData> | null = null;
const load = () => (cache ??= fetch("/goto.json").then((r) => r.json()));

const EXAMPLES = ["I Sent. d. 3 p. 1 a. 1 q. 2", "Brevil. p. V c. 6", "Collat. in Ioan. coll. 18", "tom. VI pag. 567"];

export function GotoBox() {
  const router = useRouter();
  const [q, setQ] = useState("");
  const [res, setRes] = useState<GotoResult | null>(null);
  const [busy, setBusy] = useState(false);
  const input = useRef<HTMLInputElement>(null);

  const go = async (text = q) => {
    if (!text.trim()) return;
    setBusy(true);
    const r = goTo(text, await load());
    setBusy(false);
    if (r.kind === "chunk") router.push(r.path + (r.anchor ? `#${r.anchor}` : ""));
    else if (r.kind === "level") router.push(r.path);
    else setRes(r);
  };

  return (
    <div className="goto-box">
      <label htmlFor="goto-input" className="goto-label">
        Go to a citation
      </label>
      <div style={{ display: "flex", gap: "0.5rem", flexWrap: "wrap" }}>
        <input
          id="goto-input"
          ref={input}
          className="search-input"
          style={{ flex: "1 1 260px" }}
          value={q}
          onChange={(e) => {
            setQ(e.target.value);
            setRes(null);
          }}
          onKeyDown={(e) => e.key === "Enter" && go()}
          placeholder="e.g. II Sent. d. 38 a. 1 q. 2 · Itiner. c. 4 · tom. V pag. 300"
          autoComplete="off"
          spellCheck={false}
        />
        <button className="search-btn" onClick={() => go()} disabled={busy}>
          Go
        </button>
      </div>
      <p className="goto-examples">
        Quaracchi forms:{" "}
        {EXAMPLES.map((ex, i) => (
          <span key={ex}>
            {i > 0 ? " · " : ""}
            <button
              type="button"
              className="goto-example"
              onClick={() => {
                setQ(ex);
                go(ex);
              }}
            >
              {ex}
            </button>
          </span>
        ))}
      </p>
      {res?.kind === "none" && <p className="goto-msg">{res.label}.</p>}
      {res?.kind === "many" && (
        <div className="goto-msg">
          <p>{res.label} names more than one passage:</p>
          <ul>
            {res.options.map((o) => (
              <li key={o.path}>
                <Link href={o.path}>{o.path}</Link>
              </li>
            ))}
          </ul>
        </div>
      )}
    </div>
  );
}

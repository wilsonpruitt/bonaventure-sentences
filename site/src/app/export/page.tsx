import fs from "fs";
import path from "path";
import { Illumination, CrossDivider } from "@/components/decorations";

export const metadata = {
  title: "Bulk Export",
  description:
    "Every chunk of the Bonaventure corpus, Latin and English aligned, as a single downloadable JSONL file — no crawling required.",
};

// wroot-corpus-export R2 bucket, provisioned 2026-09-18 (~/open-corpus/PLAN.md item 8).
const EXPORT_R2_BASE_URL = "https://pub-f3e5babb712240c981d8afc263f23ecf.r2.dev/bonaventure";

type Manifest = {
  generated: string;
  chunks: number;
  words: number;
  files: { name: string; description: string; size_bytes: number }[];
};

function loadManifest(): Manifest | null {
  try {
    const p = path.join(process.cwd(), "src", "data", "export-manifest.json");
    return JSON.parse(fs.readFileSync(p, "utf-8"));
  } catch {
    return null;
  }
}

function formatBytes(n: number) {
  if (n > 1024 * 1024) return `${(n / (1024 * 1024)).toFixed(1)} MB`;
  if (n > 1024) return `${(n / 1024).toFixed(0)} KB`;
  return `${n} B`;
}

export default function ExportPage() {
  const manifest = loadManifest();

  return (
    <div style={{ maxWidth: "750px", margin: "0 auto" }}>
      <div style={{ textAlign: "center", marginBottom: "2rem" }}>
        <Illumination size={70} letter="E" color="#3D1308" />
        <h2 className="h2" style={{ fontSize: "24px", marginTop: "1rem" }}>
          Exportatio
        </h2>
        <p
          style={{
            fontFamily: "var(--font-cinzel), serif",
            fontSize: "13px",
            letterSpacing: "0.12em",
            color: "#8B6914",
            textTransform: "uppercase",
          }}
        >
          Bulk Export
        </p>
      </div>

      <CrossDivider />

      <div className="body-text">
        <p style={{ marginBottom: "1.25rem" }}>
          Every chunk of this corpus, one JSON object each, the Quaracchi Latin and the
          English translation aligned, source-edition citation and licence fields
          included. This is a mirror of the same content served on every page, packaged
          so a crawl of the whole site is not necessary.
        </p>

        {manifest ? (
          <>
            <p style={{ marginBottom: "1.25rem" }}>
              Generated {manifest.generated}. {manifest.chunks.toLocaleString()} chunks,
              ~{manifest.words.toLocaleString()} words of English.
            </p>
            <ul style={{ marginBottom: "1.25rem", paddingLeft: "1.5rem" }}>
              {manifest.files.map((f) => (
                <li key={f.name} style={{ marginBottom: "0.5rem" }}>
                  <a href={`${EXPORT_R2_BASE_URL}/${f.name}`}>{f.name}</a> (
                  {formatBytes(f.size_bytes)}) — {f.description}
                </li>
              ))}
            </ul>
          </>
        ) : (
          <p style={{ marginBottom: "1.25rem", fontStyle: "italic" }}>
            The export bundle has not been published yet. Check back shortly, or write
            to <a href="mailto:wilson@wrootlabs.com">wilson@wrootlabs.com</a>.
          </p>
        )}

        <p style={{ marginBottom: "1.25rem" }}>
          Licensed the same as the rest of the site: the Quaracchi Latin is public
          domain, the English translation and apparatus are CC BY-NC 4.0 with an
          explicit machine-learning-use permission — see{" "}
          <a href="/rights">Rights and Reuse</a>.
        </p>
      </div>
    </div>
  );
}

import type { Metadata } from "next";
import Link from "next/link";
import {
  EB_Garamond,
  Cormorant_Garamond,
  Cinzel,
  Cinzel_Decorative,
} from "next/font/google";
import { Illumination } from "@/components/decorations";
import "./globals.css";

// next/font self-hosts these at build time — zero CLS, no external request.
const ebGaramond = EB_Garamond({
  subsets: ["latin"],
  weight: ["400", "500", "600"],
  style: ["normal", "italic"],
  variable: "--font-eb-garamond",
  display: "swap",
});

const cormorantGaramond = Cormorant_Garamond({
  subsets: ["latin"],
  weight: ["400", "500", "600", "700"],
  style: ["normal", "italic"],
  variable: "--font-cormorant-garamond",
  display: "swap",
});

const cinzel = Cinzel({
  subsets: ["latin"],
  weight: ["400", "500", "600", "700"],
  variable: "--font-cinzel",
  display: "swap",
});

const cinzelDecorative = Cinzel_Decorative({
  subsets: ["latin"],
  weight: ["400", "700"],
  variable: "--font-cinzel-decorative",
  display: "swap",
});

export const metadata: Metadata = {
  title: "Bonaventure — Opera Omnia",
  description:
    "An English translation of the Opera Omnia of St. Bonaventure from the Quaracchi critical edition. Currently presenting Volume I: Commentary on Book I of the Sentences of Peter Lombard.",
};

export default function RootLayout({ children }: { children: React.ReactNode }) {
  const fontVars = `${ebGaramond.variable} ${cormorantGaramond.variable} ${cinzel.variable} ${cinzelDecorative.variable}`;
  return (
    <html lang="en" className={fontVars}>
      <body>
        <header className="site-header">
          <div className="header-inner">
            <Link href="/" style={{ display: "flex", alignItems: "center", gap: "1rem" }}>
              <Illumination size={54} />
              <div>
                <h1 className="header-title">Bonaventure</h1>
                <p className="header-subtitle">Opera Omnia</p>
              </div>
            </Link>
          </div>
          <nav className="site-nav">
            <Link href="/">Home</Link>
            <Link href="/browse">Browse</Link>
            <Link href="/search">Search</Link>
            <Link href="/about">About</Link>
          </nav>
        </header>

        <main className="main-content">{children}</main>

        <section className="site-support">
          <h2>Support the Translation</h2>
          <p>
            Bonaventure&apos;s commentary on the Sentences has never been fully translated into
            English. Books I&ndash;III are complete and free to read here; Book IV &mdash; the
            sacraments &mdash; is underway, distinction by distinction. The pipeline is proven;
            the pace is a compute bill.
          </p>
          <div className="support-tiers">
            <a href="https://buy.stripe.com/9B614m7iJfls3463z54gg08" target="_blank" rel="noopener">
              $10 &mdash; a distinction
            </a>
            <a href="https://buy.stripe.com/3cI6oG32tfls7kmc5B4gg09" target="_blank" rel="noopener">
              $100 &mdash; a decade
            </a>
            <a href="https://buy.stripe.com/cNi5kC8mN2yG5ce6Lh4gg0b" target="_blank" rel="noopener">
              $10/mo &mdash; patron
            </a>
          </div>
          <p className="support-fine">
            Everything stays free regardless. Wroot Press is a small independent press &mdash; an
            imprint of Wroot Labs LLC, not a charity. Contributions aren&apos;t tax-deductible;
            they buy compute.
          </p>
        </section>

        <footer className="site-footer">
          <p style={{ marginBottom: "0.25rem" }}>The Bonaventure Opera Omnia Translation Project</p>
          <p style={{ fontSize: "11px", opacity: 0.7 }}>
            Quaracchi Edition (1882) &middot; Working Draft &middot; MMXXVI
          </p>
        </footer>
        <script defer src="/_vercel/insights/script.js"></script>
      </body>
    </html>
  );
}

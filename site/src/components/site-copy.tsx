// ⚠ PLACEHOLDER COPY: SITE-PLAN Q2. The home introduction and the footer
// appeal are to be written by a commissioned Bonaventure scholar. What stands
// here is neutral, fact-only filler so the redesign can proceed. Replace the
// bodies of HomeIntro and SupportAppeal (and META_DESCRIPTION) with the
// scholar's text when it arrives; nothing else needs to change.
//
// Rules for whatever goes here (from the commissioning brief):
// - no progress figures or "now complete" statements: the scope table and the
//   /progress page carry status, derived from the data;
// - no unverified "first English translation" claims;
// - the not-a-charity / contributions-buy-compute facts stay accurate.
//
// SUPPORT_TIERS: the labels are wording only. The hrefs are LIVE Stripe Payment
// Links. Never change an href here; a label change needs Wilson's OK.

export const META_DESCRIPTION =
  "St. Bonaventure's Opera Omnia in English and Latin side by side, translated from the Quaracchi critical edition, with its notes and page references.";

export function HomeIntro() {
  return (
    <p className="body-text" style={{ maxWidth: "700px", margin: "0 auto", textAlign: "center" }}>
      The works of St. Bonaventure of Bagnoregio (1221&ndash;1274), the Seraphic Doctor, in English
      and Latin side by side, translated from the Quaracchi critical edition of his{" "}
      <em>Opera Omnia</em>&thinsp; (1882&ndash;1902). The editors&rsquo; notes are translated in
      full and the Quaracchi page breaks are marked, so every passage can be read and cited by the
      edition.
    </p>
  );
}

export function SupportAppeal() {
  return (
    <p>
      Bonaventure&apos;s <em>Opera Omnia</em>&thinsp; is being translated here, Latin and English
      side by side, and every page is free to read. Contributions pay for the computing time the
      translation uses.
    </p>
  );
}

export const SUPPORT_TIERS: { href: string; label: string }[] = [
  { href: "https://buy.stripe.com/9B614m7iJfls3463z54gg08", label: "$10 — a distinction" },
  { href: "https://buy.stripe.com/3cI6oG32tfls7kmc5B4gg09", label: "$100 — a decade" },
  { href: "https://buy.stripe.com/cNi5kC8mN2yG5ce6Lh4gg0b", label: "$10/mo — patron" },
];

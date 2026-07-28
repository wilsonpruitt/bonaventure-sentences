import { Illumination, CrossDivider, FleuronDivider } from "@/components/decorations";

export default function AboutPage() {
  return (
    <div style={{ maxWidth: "750px", margin: "0 auto" }}>
      <div style={{ textAlign: "center", marginBottom: "2rem" }}>
        <Illumination size={70} letter="D" color="#3D1308" />
        <h2 className="h2" style={{ fontSize: "24px", marginTop: "1rem" }}>
          De Hoc Opere
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
          About this Project
        </p>
      </div>

      <CrossDivider />

      <div className="body-text">
        <p style={{ marginBottom: "1.25rem" }}>
          This project presents an English translation of the <em>Opera Omnia</em> of St. Bonaventure
          of Bagnoregio (1221&ndash;1274), the Seraphic Doctor — drawn from the Quaracchi critical
          edition (Vols. I&ndash;X, 1882&ndash;1902) prepared by the Fathers of the Collegium
          S. Bonaventurae.
        </p>
        <p style={{ marginBottom: "1.25rem" }}>
          All four books of the <em>Commentary on the Sentences of Peter Lombard</em> — Volumes I
          through IV — are complete and published here. Work is now under way on Volume V, the
          opuscula, beginning with the <em>Breviloquium</em>; the intention is to finish all ten
          volumes, through the <em>Itinerarium mentis in Deum</em>, the{" "}
          <em>Collationes in Hexaemeron</em>, the disputed questions, and the sermons. No complete
          English edition of the Opera Omnia has ever been published.
        </p>

        <FleuronDivider />

        <div className="section-title">How This Translation Is Made</div>
        <p style={{ marginBottom: "1.25rem" }}>
          Every unit of text on this site is drafted with the help of a large language model working
          from the Quaracchi Latin, and is then checked against the printed page by a procedure that
          has been written down, tested, and revised across some five hundred units of text. The
          first half of that sentence is what people ask about. The second half is what decides
          whether the translation is any good, so it is set out here in full.
        </p>

        <div className="section-title">Setting the Latin</div>
        <p style={{ marginBottom: "1.25rem" }}>
          The Latin is not read off the page image. It is set from the Internet Archive&rsquo;s OCR
          of the Quaracchi scan, which is markedly more accurate than reading small nineteenth-century
          type at any practical resolution &mdash; a direct read of the print produces errors the OCR
          gets right (<em>bonus</em> taken for <em>utens</em>, <em>homo</em> for <em>bonum</em>, a{" "}
          <em>proceditur</em> reversed into <em>procedam</em>). Where the OCR is sound it governs,
          and the printed page is consulted to settle what it garbles.
        </p>
        <p style={{ marginBottom: "1.25rem" }}>
          From Volume II onward the edition is set in two columns, and there the OCR fails in a
          particular way: it shatters diagonally across the gutter, a token to a line, through
          exactly the passages that matter most &mdash; the <em>Respondeo</em>, the{" "}
          <em>Solutio</em>, the scholia, and every page footer. In those regions the priority
          inverts. The page is extracted at 450 dpi, cropped into column bands, and read band by
          band, top to bottom, left column and then right. The gutter is measured on each page,
          because it wanders and alternates with the page&rsquo;s parity; a band cropped at the wrong
          split truncates a column without any sign that it has. At least one word in the published
          corpus &mdash; <em>transumtum</em>, where the page reads <em>transumtivum</em> &mdash; was
          wrong for precisely that reason until a later pass caught it.
        </p>

        <div className="section-title">The English</div>
        <p style={{ marginBottom: "1.25rem" }}>
          The English is literal and it is parallel: paragraph for paragraph, and footnote marker for
          footnote marker, each marker standing where it stands in the Latin rather than at the end
          of the clause. Standard scholastic formulae are rendered the same way every time &mdash;{" "}
          <em>Videtur quod</em> as &ldquo;It seems that,&rdquo; <em>Sed contra</em> as &ldquo;On the
          contrary,&rdquo; <em>Respondeo. Dicendum quod</em> as &ldquo;I respond: It must be said
          that&rdquo; &mdash; and a table of key terms is fixed for the project and applied across
          all ten volumes.
        </p>
        <p style={{ marginBottom: "1.25rem" }}>
          The <em>scholia</em> and the critical apparatus are translated in full, to the same
          standard as the body. That is unusual, and it is deliberate. Those notes carry much of the
          scholarly value of the Quaracchi edition, they have never been put into English, and they
          are the first thing an abridgment drops.
        </p>

        <div className="section-title">The Apparatus</div>
        <p style={{ marginBottom: "1.25rem" }}>
          Quaracchi&rsquo;s footnotes are the hardest part of the edition to reproduce, and the part
          a paraphrase would quietly lose. Three properties of the printed page make them dangerous.
        </p>
        <ul style={{ marginBottom: "1.25rem", paddingLeft: "1.5rem" }}>
          <li style={{ marginBottom: "0.75rem" }}>
            <strong>The numbering restarts on every printed page.</strong> A passage spanning four
            pages carries four independent sequences of 1, 2, 3. Footnote labels are therefore
            qualified by page internally, so that two notes numbered 4 cannot collide and silently
            overwrite one another; the reader sees the printed number.
          </li>
          <li style={{ marginBottom: "0.75rem" }}>
            <strong>Notes run over.</strong> A note reaching the foot of a column continues at the
            head of the next column&rsquo;s footer &mdash; sometimes on the following page, sometimes
            in the middle of a word &mdash; and the continuation carries no number. The fragment left
            behind at the column foot usually reads as a complete entry, so the loss is invisible.
            Every footer&rsquo;s last entry is treated as incomplete until its continuation is either
            found or positively excluded from both sides. Of the sixteen units in the{" "}
            <em>Breviloquium</em> prologue and first part, ten carried a runover.
          </li>
          <li style={{ marginBottom: "0.75rem" }}>
            <strong>The OCR loses footers wholesale.</strong> In the last distinction of Book IV it
            dropped three entire footer registers &mdash; twenty-six notes across three pages &mdash;
            with nothing to indicate that anything was missing. They were recovered because the
            apparatus is read off the page bands as a matter of course, not only when something looks
            wrong. In Volume V the OCR does not render footnote numerals at all; every superscript
            arrives as a stray punctuation glyph, and the band image is the only source there is.
          </li>
        </ul>

        <div className="section-title">What Is Checked, and When</div>
        <p style={{ marginBottom: "1.25rem" }}>
          Before any unit is committed it passes a set of scripted audits: a paraphrase audit, which
          scores word overlap against the raw Latin and separates literal transcription from summary;
          a header audit, which counts the semantic divisions in the source against those in the
          file and catches a whole question gone missing; an apparatus count; and a formatting scan
          confirming that every footnote definition has a matching marker in both languages. A seam
          screen examines every boundary that falls inside a printed page, which is where text goes
          missing, and the site is rebuilt to confirm the file parses and the two languages carry the
          same anchors.
        </p>
        <p style={{ marginBottom: "1.25rem" }}>
          On a fixed cadence &mdash; roughly every hundred printed pages, and unconditionally at the
          end of each work &mdash; three further passes run. Every ambiguity flag is resolved against
          a 600 dpi read of the page or else formally accepted as illegible, with the reason
          recorded. The whole corpus is scanned for formatting drift, not merely the new part. And
          every boundary in the finished section is swept to confirm that no text and no footnote was
          lost where two units meet. In the closing gate on Book IV, a hundred and eleven mid-page
          seams were checked and three dropped notes recovered.
        </p>
        <p style={{ marginBottom: "1.25rem" }}>
          Several of these checks exist because an earlier one failed. The formatting scan spent
          months hardcoded to two volumes, so four volumes&rsquo; worth of clean results were false;
          when that was found the tool was repaired and sixty-one genuine defects surfaced behind it.
          A register of known open defects is kept with the project, along with the resolution log
          for every gate, and both are consulted before new work rather than after.
        </p>

        <div className="section-title">What We Do Not Correct</div>
        <p style={{ marginBottom: "1.25rem" }}>
          Plain scanning artifacts are repaired silently &mdash; a word broken across a line rejoined,
          an <em>ahquid</em> restored to <em>aliquid</em>. Anything genuinely uncertain is flagged
          rather than guessed, and the flag stays in the file until someone resolves it against the
          page.
        </p>
        <p style={{ marginBottom: "1.25rem" }}>
          Quaracchi&rsquo;s own errors stay. Where the editors number a footnote eleven on a page
          carrying ten, the page is reproduced as printed and the discrepancy noted; no eleventh note
          is invented to make the sequence come out. Where a scriptural citation in the apparatus is
          wrong &mdash; <em>Matth.</em> 12:14 for what is plainly 12:40 &mdash; the printed reading
          stands. An earlier pass had silently corrected that one, and the correction was reverted.
          This is an edition of Quaracchi, not an improvement on it.
        </p>

        <FleuronDivider />

        <div className="section-title">Why Translate This Way</div>
        <p style={{ marginBottom: "1.25rem" }}>
          Beneath the question of human against machine lies a prior question that settles it: nobody
          was doing this. There is no complete English Bonaventure. There is no English{" "}
          <em>Acta Sanctorum</em>. There is nothing approaching an English Migne. These are not gaps
          waiting on a translator who is nearly finished. They are gaps that stood no closer to being
          filled this year than they would a thousand years from now, because the cost is measured in
          human lifetimes and that cost has not moved since the nineteenth century. A corpus of this
          size is not translated slowly. It is not translated at all.
        </p>
        <p style={{ marginBottom: "1.25rem" }}>
          The other two are now being attempted the same way, by the same hand and under the same
          procedure: the Bollandists&rsquo; <em>Acta Sanctorum</em> at{" "}
          <a href="https://actasanctorum.org" target="_blank" rel="noopener noreferrer">
            actasanctorum.org
          </a>
          , and Migne&rsquo;s <em>Patrologia</em> at{" "}
          <a href="https://migne.app" target="_blank" rel="noopener noreferrer">
            migne.app
          </a>
          . Neither had been attempted whole before.
        </p>
        <p style={{ marginBottom: "1.25rem" }}>
          So the aim is not a perfect translation. The aim is to unlock the language gate to the
          tradition. Someone with no Latin can now reach the passage, follow what Bonaventure is
          arguing, and see exactly where to check him. That is worth more than a flawless rendering
          of a single question arriving in fifty years.
        </p>
        <p style={{ marginBottom: "1.25rem" }}>
          There will be errors in this, including serious ones. There are serious ones in Migne, and
          in Quaracchi, and in every edition of this kind ever assembled. What is striking is the
          shape they take. The model will carry a fault forward &mdash; a line, a spacing, an
          artifact of the transcription &mdash; much as a clerk copying his exemplar carried forward
          the mistake set in front of him. Working this way has made me feel nearer to the medieval
          copyists than to a modern translator.
        </p>

        <div className="section-title">Key Terms</div>
        <p style={{ marginBottom: "1.25rem" }}>
          The following scholastic terms are rendered consistently: <em>uti</em> &rarr; to use;{" "}
          <em>frui</em> &rarr; to enjoy; <em>ratio</em> &rarr; account/ground;{" "}
          <em>processio</em> &rarr; procession; <em>suppositum</em> &rarr; supposit;{" "}
          <em>potentia</em> &rarr; potency/power; <em>actus</em> &rarr; act/actuality;{" "}
          <em>caritas</em> &rarr; charity; <em>exemplar</em> &rarr; exemplar;{" "}
          <em>vestigium</em> &rarr; vestige; <em>similitudo</em> &rarr; likeness;{" "}
          <em>honestum</em> &rarr; the honorable; <em>complacentia</em> &rarr; complacency;{" "}
          <em>actus quietativus</em> &rarr; quietative act.
        </p>

        <div className="section-title">A Working Draft</div>
        <p style={{ marginBottom: "1.25rem" }}>
          Everything here is a draft and should be cited as one; passages still under review are
          marked as such in the text. Corrections are wanted, not merely welcomed. If you read Latin
          and find something wrong &mdash; a mistranslation, a dropped note, a misread page &mdash;
          write to <a href="mailto:wilson@wrootlabs.com">wilson@wrootlabs.com</a>. It will be fixed,
          and the correction recorded. Inquiries from scholars who would like to review or contribute
          to the work are welcome on the same address.
        </p>

        <FleuronDivider />

        <div
          className="card"
          style={{ cursor: "default", background: "rgba(61,19,8,0.04)", textAlign: "center" }}
        >
          <p style={{ fontFamily: "var(--font-cinzel), serif", fontSize: "14px", color: "#3D1308", marginBottom: "0.25rem" }}>
            Ad Maiorem Dei Gloriam
          </p>
          <p style={{ fontSize: "13px", color: "#8B6914", fontStyle: "italic" }}>
            &ldquo;For the perfection of the Christian, I propose a work that pertains to the
            beginning of learning.&rdquo;
          </p>
          <p style={{ fontSize: "12px", color: "#6B4A3A", marginTop: "0.5rem" }}>
            &mdash; Bonaventure, <em>Breviloquium</em>, Prol.
          </p>
        </div>
      </div>
    </div>
  );
}

# PROMPT — Rebuild the Lecture 01 study guide (v2)

Rebuild my study guide for **Overview of Metabolic Pathways** (Medical Biochemistry & Genetics I, Fall 2026). A v1 exists and is 22 pages; it is too long and written in the wrong voice. This is a **rewrite from the sources**, not an edit of v1.

Output a **PDF** (primary) plus a markdown version.

---

## 1. THE CORE CHANGE — read this before anything else

The v1 guide reads like a *report about a lecture*. The v2 must read like a **self-contained textbook chapter** — the only thing I need to open in order to know this material completely.

### Rule 1 — No meta-references. None.

**Never** write phrases like: "she said," "Dr. Bagh emphasized," "the slide shows," "the deck states," "the lecture covered," "he repeated this five times," "slide 23," "the speaker notes say," "verbatim from," "in her words," "the professor's example was."

Write the biochemistry directly, as fact. Not *"She stressed that oxidation in the body is loss of hydrogen"* but **"Biological oxidation is dehydrogenation: substrates are oxidized by losing hydrogen, not by gaining oxygen."**

The only permitted non-content text is a minimal course header (course, exam date) and a two-line legend for the emphasis system.

### Rule 2 — Synthesize, don't transcribe.

Absorb everything in the sources, then **reorganize it into the clearest possible structure**, which will often differ from the order it was presented in. Merge material that belongs together even if it was scattered across the deck. Split anything that was crammed together confusingly. Your organization should be *better* than the source's.

### Rule 3 — Reconcile errors silently.

The source material contains genuine errors, imprecise wording, and outdated framing. **Fix them using the textbook and your own knowledge, and say nothing about it in the document.** No "corrections" table, no "what was said vs. what is true," no footnotes about discrepancies. Just write the correct version.

*Exception:* where the course's preferred answer differs from the strictly-correct one in a way that could cost exam points, give the course's answer as the headline fact and the precision as a brief parenthetical — still with no reference to where either came from. Example: *"Glucokinase is inactive during fasting (its high Kₘ keeps it far below Vmax at low glucose)."*

**Report every correction you made to me in chat, not in the document.**

### Rule 4 — Emphasize by design, never by repetition.

v1 stated the same fact up to four times in different sections. Forbidden. **Each fact appears exactly once**, in the single best place for it. To make something stand out, use the visual system in §4 — do not restate it.

### Rule 5 — Write concisely. This is a real source of the savings.

Length comes down through **four** levers, and I want all four used:

1. Cutting meta-commentary (Rule 1)
2. Cutting repetition (Rule 4)
3. Cutting the corrections/sources sections (Rule 3, §5)
4. **Writing the surviving prose more tightly** ← this one is new and matters

Lever 4 does **not** mean writing less *content* or explaining less *thoroughly*. It means saying the same thing in fewer words. Concretely:

- Aim for **2–4 sentences** where v1 used 5–8, carrying identical information.
- One sentence per idea. Split long sentences rather than chaining clauses with "which is why… and this means… so that…".
- Cut hedges and intensifiers: *very, really, actually, quite, essentially, basically, simply, in fact, of course, it is worth noting, importantly.*
- Cut throat-clearing openers: *"It is important to understand that…", "As we will see…", "Before moving on…", "Note that…"*.
- Never restate an idea a second way. Delete every *"in other words," "put differently," "that is to say."*
- Where two examples make the same point, keep the better one.
- Prefer verbs to nominalizations: "phosphorylates" not "carries out the phosphorylation of."
- Prefer active voice unless the passive is genuinely clearer.
- Don't restate a heading in the first line under it.

**Calibration example.** This is real v1 prose (90 words):

> NADH and NADPH differ by exactly one phosphate group (on the 2′-OH of the adenosine ribose). Chemically they do the same thing — carry two electrons. That phosphate is a molecular tag letting the cell run two separate pools with two separate jobs, and letting enzymes recognize which one they are meant to use. NAD⁺/NADH is kept mostly oxidized, ready to accept electrons from catabolism and pass them to the electron transport chain — catabolic currency. NADP⁺/NADPH is kept mostly reduced, ready to donate electrons into biosynthesis — anabolic currency.

Target style (57 words, same facts, nothing lost):

> NADH and NADPH differ by one phosphate on the adenosine ribose. Both carry two electrons; the phosphate is a tag that lets enzymes tell them apart, so the cell can run two pools with opposite jobs. NAD⁺ is kept oxidized to accept electrons from catabolism and feed the ETC. NADP⁺ is kept reduced to donate electrons into biosynthesis.

That is roughly a **35% reduction with zero information loss**. Apply that standard throughout.

**Where not to compress.** Do not go telegraphic. Explanations must still explain — a mechanism the reader has never seen needs a real sentence, not a fragment. Never sacrifice a causal "because" to save three words. If a passage genuinely needs five sentences to be understood, give it five.

### Rule 6 — Nothing may be lost.

Every fact, number, example, definition, list, exception and clinical link in the slide deck (including speaker notes) and the transcript must survive somewhere in the document. Concision is about wording, never about coverage. When in doubt between cutting a fact and cutting six words of prose around it, cut the words.

---

## 2. Source files

Working directory: `/Users/yoelplutchok/Desktop/Biochem_Fall`
The repo is organised one folder per lecture.

| What | Path |
|---|---|
| **Slide deck** (41 slides) | `01 - Overview of Metabolic Pathways/Lecture 01 _Bagh_Overview of Metabolic Pathway (1).pptx` |
| **Lecture transcript** | `01 - Overview of Metabolic Pathways/Lecture 1 transcript Biochem.txt` |
| **Interactive-session deck** | `_Interactive Sessions/Pre discussion Week 1 Overview and enzyme PE IS F26 (1).pptx` — **use slides 2–12 only** (13+ belong to another lecture) |
| **v1 guide — mine the last two sections, see §6** | `01 - Overview of Metabolic Pathways/Lecture 01 - STUDY GUIDE (html source).html` |
| **CSS — reuse and extend** | `01 - Overview of Metabolic Pathways/Lecture 01 - STUDY GUIDE (html source).css` |
| **Required textbook** | `/Users/yoelplutchok/Desktop/Fall Courses/Medical Biochemistry and Genetics I/sga/general/textbooks/Lippincott Biochemistry - 6th Edition .pdf` — **Ch. 8, Introduction to Metabolism** |
| **Backup textbook** | `.../sga/general/textbooks/BRS Biochemistry, Molecular Biology, and Genetics 6E (2013).pdf` |
| **Figures already extracted** | `01 - Overview of Metabolic Pathways/Lecture_01_figures/` (7 images) |

Already looked up — don't re-derive: this is **Week 1, Session 1, Tue 8/4**; required reading **Lippincott Ch. 8**; assessed on **Foundation Exam #1, Mon 8/17, 11 AM–1 PM**.

**The interactive-session deck matters.** Slides 2–12 contain two exam-style questions explicitly tagged to numbered learning objectives — the closest available proxy for real exam items. v1 missed them. Use them to calibrate what to mark as high-yield, and fold them into the self-test (§6).

---

## 3. Length target

| Part | Target |
|---|---|
| Main body (everything before the self-test) | **8–10 pages** |
| Self-test | ~2–3 pages |
| Rapid-review sheet | 2 pages |
| **Total** | **13–15 pages, hard ceiling 17** |

v1's main body was ~17 pages. Roughly a third of that was meta-commentary and repetition; tightening the surviving prose per Rule 5 supplies most of the rest.

---

## 4. The emphasis system — build this into the CSS

Replace "say it again" with visual hierarchy. Define exactly three tiers and apply them consistently:

**Tier 1 — `.must` (highest yield).** A red-tinted band with a ★ marker and the label **MUST KNOW**. **Cap at 12–14 in the entire document.** Scarcity is what makes it work. Keep each one to a single line. Reserve for the facts most likely to be directly tested. Confirmed Tier-1 candidates for this lecture (verify against the sources, then mark):

- Biological oxidation = loss of hydrogen, not gain of oxygen
- NADPH is never a source of ATP; NADH and FADH₂ are (indirectly)
- The HMP shunt yields NADPH + pentoses and **no** ATP
- Anabolism requires a **high** energy charge — never a low one
- Anabolism's four requirements: ATP, acetyl-CoA, NADPH, insulin
- Insulin drives every "-genesis" **except** gluconeogenesis and ketogenesis
- Insulin always dephosphorylates; glucagon and epinephrine always phosphorylate
- Rate-limiting ⟹ regulated, but regulated ⇏ rate-limiting
- Cyclic pathways have no committed step (they do have a rate-limiting step)
- Long-term regulation changes enzyme **quantity**; short-term changes **activity**
- Glucokinase ← substrate concentration; hexokinase ← product (G6P) inhibition
- Zymogen activation is **not** reversible
- ATP has two high-energy bonds, ADP has one; ΔG°′ = −7.3 kcal/mol
- TCA is the common oxidative pathway for carbohydrate, lipid **and** protein

**Tier 2 — inline bold.** Every term, number or name that could be a fill-in-the-blank answer. Generous but not blanket — if everything is bold, nothing is.

**Tier 3 — `.vs` (confusable pairs).** A distinctly coloured box, ideally two-column, for things students actually mix up. Use <u>underline</u> or coloured text on the single discriminating word. For this lecture at minimum: product vs. feedback inhibition; committed vs. rate-limiting step; NADH vs. NADPH; hexokinase vs. glucokinase; induction vs. repression; exergonic vs. endergonic; convergent vs. divergent.

Also keep from the existing CSS: `.clin` (green) for clinical correlations, and tables.

**Reduce box count.** v1 used ~40 coloured boxes; each costs ~4 mm of padding and margin, which is several pages in aggregate. Target **~15 boxes total**. The default presentation should be: a tight prose paragraph carrying the *concept*, immediately followed by a table or compact list carrying the *specifics*. Boxes are for emphasis only, not for routine structure.

**Keep the concept/specifics distinction** — I process material that way — but make it lightweight: 2–4 sentences of "why," then the facts. The prose must never restate the list that follows it.

---

## 5. Structure of the main body

Organize by the four learning objectives, which are the natural spine and match how the material is tested:

1. Catabolism vs. anabolism
2. Key components of metabolism and the activated carriers
3. Common themes in pathways; committed vs. rate-limiting steps
4. Mechanisms of regulation

Open with a **one-page orientation**: a compact diagram or ASCII map of the whole system — diet → catabolism (oxidation = loss of H) → reduced carriers + acetyl-CoA + ATP → anabolism — plus one tight paragraph tying it together. This is the scaffold everything else hangs on. Reuse the `.map` styling from the v1 CSS.

**Structural condensation, on top of the prose-level work in Rule 5:**
- Convert any comparative prose into a table. Tables are denser than sentences and easier to revise from.
- One-line definitions, not paragraphs, for defined terms.
- Fold examples into the fact they illustrate rather than giving them their own block.
- Merge overlapping material scattered across the source into single treatments.
- Prefer a labelled list over a paragraph whenever the content is genuinely enumerable.

**Figures: keep 5–7 maximum.** The seven already extracted in `Lecture_01_figures/` are a good starting set — reassess each and drop any that prose or a table covers. **Rewrite every caption**: captions must explain the biology only, in one or two sentences, with no reference to slide numbers or sources. Never include both a figure of a table and a typeset version of that table.

**Do not include** a corrections/reconciliation section, a "sources" section, or any "how this document was made" framing.

---

## 6. The last two sections — keep, and extend

I like these and want them preserved in style.

**Self-test.** Currently 20 questions in `ol.qlist`, each one line with a one-line answer inline in green. **Keep this format exactly.** Expand to **28–34 questions so that every part of the material is covered** — audit your finished main body section by section and add questions wherever something testable isn't yet probed. Also fold in the two objective-tagged questions from the interactive-session deck and the two in-deck questions, converted to the same recall format; where a question's distractors teach a real discrimination, put that discrimination in the answer line. No meta-framing.

**Rapid-review sheet.** Two-column `.two-col` keyword sheet. Keep its structure and density. **One fix:** its current intro sentence refers to the professor and her phrasing — rewrite it to something like *"Bold = highest-yield. If you review one page, review this one."*

---

## 7. Tooling — commands verified on this machine

`python3` is at `/opt/miniconda3/bin/python3`. `pandoc` and `soffice` are installed. **There is no `pdflatex` or `wkhtmltopdf`** — do not build the PDF via LaTeX.

```bash
python3 -m pip install python-pptx pymupdf weasyprint beautifulsoup4 lxml
```

**Extract slide text + speaker notes.** Speaker notes carry content that is not on the slides and not spoken aloud — never skip them. Recurse into groups (`shape_type == 6`) and handle `sh.has_table`.

```python
from pptx import Presentation
prs = Presentation("01 - Overview of Metabolic Pathways/Lecture 01 _Bagh_Overview of Metabolic Pathway (1).pptx")
for i, slide in enumerate(prs.slides, 1):
    # print shape text; recurse groups; read tables
    if slide.has_notes_slide:
        print(slide.notes_slide.notes_text_frame.text)
```

**Render slides to PNG and actually look at them** — about half the teaching content is in figures.
```bash
soffice --headless --convert-to pdf --outdir . "01 - Overview of Metabolic Pathways/Lecture 01 _Bagh_Overview of Metabolic Pathway (1).pptx"
```
```python
import fitz
d = fitz.open("Lecture 01 _Bagh_Overview of Metabolic Pathway (1).pdf")
for i, p in enumerate(d, 1): p.get_pixmap(dpi=110).save(f"pages/s{i:02d}.png")
```
`MuPDF error: format error: No common ancestor in structure tree` is harmless; the render succeeds.

**Extract additional figures** (if you need any beyond the seven already saved): some images sit in *placeholders*, not `Picture` shapes, so a `shape_type == 13` filter misses them. Wrap `sh.image` in try/except across **all** shapes.

**Build the PDF** with WeasyPrint: `HTML(filename="guide.html").write_pdf("out.pdf")`. Keep the HTML, CSS and figures folder in the same directory so relative paths resolve.

**Markdown version.** Pandoc's raw HTML→GFM produces div soup. Pre-process with BeautifulSoup first: unwrap layout divs and all `<span>`s; convert each callout div to a `<blockquote>` led by `<strong>LABEL</strong>`; convert `<figure>` to image + italic caption; swap the `.map` block for a placeholder token and substitute a hand-written fenced code block afterward (`get_text()` mangles `<br>` layouts); inside tables replace `<br>` with ` · `, expand `colspan` into repeated cells, and strip all `class`/`style`/`colgroup` so pandoc emits pipe tables. Then `pandoc -f html -t gfm --wrap=none`.

**Verify your own output.** Render the finished PDF back to PNGs and build a PIL contact sheet to catch layout blowouts, orphaned headings and dead whitespace. Report the final page count.

**Self-edit pass before you build the PDF.** Reread your draft once with Rule 5 in hand and cut wordiness you missed on the first pass. Expect to remove 10–15% on this pass alone. Removing *words*, never facts.

---

## 8. Reading the sources

- The transcript is a rough auto-transcription with heavy phonetic garbling. Normalize silently: `kynise`→kinase, `coalent`→covalent, `alosic`/`alostric`→allosteric, `estile`/`aile COA`→acetyl-CoA, `zyosin`→zymogen, `tripsogen`→trypsinogen, `exagonic`→exergonic, `nascin`→niacin, `ura`→urea, `gluconneioenesis`→gluconeogenesis, `HMPP`→HMP, `Sam`→SAM.
- **Repetition count in the transcript is the emphasis signal** — use it to assign Tier 1, then discard the observation. It never appears in the output.
- Phrases that flag high-yield material: "please know that," "kindly remember," "don't mess up there," "very very important," "always and always," "please don't pick."
- The deck has stale artifacts: leftover title text boxes that contradict their slide, and at least one embedded image cropped mid-content. Work out the intended content and present it whole.
- Use Lippincott Ch. 8 to fill genuine gaps and supply mechanism — for instance the three-stage framing of catabolism, and the GPCR→adenylyl cyclase→cAMP→PKA basis for why glucagon phosphorylates while insulin dephosphorylates. Do not expand scope beyond what the lecture covers.

---

## 9. Deliverables

Write into `/Users/yoelplutchok/Desktop/Biochem_Fall/01 - Overview of Metabolic Pathways/`:

1. `Lecture 01 - Overview of Metabolic Pathways - STUDY GUIDE v2.pdf` ← **primary**
2. `Lecture 01 - Overview of Metabolic Pathways - STUDY GUIDE v2.md`
3. `Lecture 01 - STUDY GUIDE v2 (html source).html` and `.css`
4. Reuse `Lecture_01_figures/` for images; add to it only if needed

**Do not overwrite or delete the v1 files** — I want to compare before retiring them.

At the end, report to me in chat (not in the document):
- Final page count
- Every error you silently corrected, and what you corrected it to
- Anything in the sources you judged ambiguous and how you resolved it
- Confirmation that nothing from the deck, speaker notes, or transcript was dropped

If anything about the brief is genuinely ambiguous, ask before building rather than guessing.

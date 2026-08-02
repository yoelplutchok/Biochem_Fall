# PROMPT — Lecture 03 Study Guide

Build a complete, compressed study guide for **Lecture 3: Electron Transport Chain; Uncouplers, Inhibitors and ROS** (Dr. Shilpika Bagh) in my Medical Biochemistry & Genetics I course. Output a **PDF** (primary deliverable) plus a markdown version.

This job has already been done twice, for Lectures 1 and 2. The pipeline, the design system, and the pitfalls are documented below — follow them and you should be efficient. **Target 20–24 pages** (hard ceiling 26). Lecture 1 landed at 22 pages from a 41-slide deck using these rules, so the target is realistic.

---

## 1. Which file is "Lecture 3" — already resolved, don't re-derive

The deck filenames in this repo do **not** match the course's lecture numbering. The file called `Lecture 06 ...` **is** Lecture 3. This is confirmed by the course's own interactive-session deck, whose title slide reads *"Lecture 03: Electron Transport Chain; Uncouplers, Inhibitors and ROS."*

Working directory: `/Users/yoelplutchok/Desktop/Biochem_Fall`

> **NOTE ON REPO LAYOUT (updated):** the repo is now organised into one folder per lecture, each holding the deck and its transcript together. Root contains: `01 - Overview of Metabolic Pathways`, `02 - Enzymes and Enzyme Kinetics`, `03 - Electron Transport Chain`, `04 - Signal Transduction`, `05 - Carbohydrate Digestion`, `Primer 1 - Thermodynamics`, `Primer 2 - Carbohydrate Structure`, `_Interactive Sessions`, `_Course Documents`, `_Prompts`. All paths below reflect this. Write your deliverables **into the lecture's own folder**, keeping the HTML, CSS and figures folder together so relative paths resolve.


| What | Path | Notes |
|---|---|---|
| **Slide deck** | `03 - Electron Transport Chain/Lecture 06 Bagh_Electron Transport Chain.pptx` | **49 slides.** Genuine `.pptx` — opens directly in python-pptx, no conversion needed |
| **Lecture transcript** | `03 - Electron Transport Chain/ETC Lecture Biochem.md` | Verified: opens "Today we are going to talk about electron transport chain" |
| **Interactive-session deck** | `_Interactive Sessions/Pre discussion Week 1 ETC Signal Tr Carb Dig F26 (1).pptx` | **MANDATORY SOURCE — see §2.** Use **slides 2–16 only** |
| **Syllabus** | `_Course Documents/DO Med Biochem genetics I syllabus Fall 2026 7_22 share.docx` | |
| **Required textbook** | `/Users/yoelplutchok/Desktop/Fall Courses/Medical Biochemistry and Genetics I/sga/general/textbooks/Lippincott Biochemistry - 6th Edition .pdf` | ETC is **Ch. 6, Bioenergetics and Oxidative Phosphorylation** |
| **Backup textbook** | `.../sga/general/textbooks/BRS Biochemistry, Molecular Biology, and Genetics 6E (2013).pdf` | |
| **Style reference (read this)** | `01 - Overview of Metabolic Pathways/Lecture 01 - Overview of Metabolic Pathways - STUDY GUIDE.pdf` | The compressed 22-page version — match this density |
| **CSS — copy as-is** | `01 - Overview of Metabolic Pathways/Lecture 01 - STUDY GUIDE (html source).css` | Already tuned for the compressed format. **Do not modify it**; just copy to a new filename |
| **HTML structure example** | `01 - Overview of Metabolic Pathways/Lecture 01 - STUDY GUIDE (html source).html` | |

**Syllabus context, already looked up:**
- Delivered Week 1, **Thursday 8/6, 8:30–10:00 AM**, instructor **Bagh**, in a session shared with the Thermodynamics primer, Signal Transduction, Carbohydrate digestion, and Carbohydrate structures.
- Required reading: **Lippincott Ch. 6**; also **Panini, *Medical Biochemistry: An Essential Textbook*, 2nd ed., Ch. 11**.
- Assessed on **Foundation Exam #1, 8/17, 11 AM–1 PM**.
- Clinical vignette attached to this session: **CV: Toxic Exposure**.

---

## 2. NEW AND IMPORTANT — use the interactive-session deck

**This was missed on Lectures 1 and 2 and must not be missed here.** `_Interactive Sessions/Pre discussion Week 1 ETC Signal Tr Carb Dig F26 (1).pptx` is the in-class interactive session deck, and it contains **exam-style practice questions explicitly tagged to numbered learning objectives** — e.g. a slide labeled *"Lecture 3. 5. Compare and contrast the action of uncouplers…"* sitting directly above its question. These are the closest available proxy for the actual exam items.

Use **slides 2–16 only**:
- **Slides 2–3** — Primer 1 (Thermodynamics & coupled reactions) objectives and the three key equations: `ΔG = ΔH − TΔS`, `ΔG°′ = −RT log Keq`, `ΔG°′ = −nFΔE°′`, plus `ATP + H₂O → ADP + Pi, ΔG°′ = −7.3 kcal/mol`. Include only what ETC actually needs (see §5).
- **Slides 4–16** — the ETC material: objectives, catabolism recap, the chain itself, oxidative phosphorylation, the inhibitor/uncoupler taxonomy, CoQ, CO poisoning with a full clinical vignette ("Richard's story"), and **four worked questions** (propane-tent death, cyanide poisoning, oligomycin/oxygen-consumption, inhibitors-vs-uncouplers comparison).
- **Slides 17 onward are Signal Transduction and Carbohydrate Digestion — those are Lectures 4 and 5. Do not include them.**

Fold the practice questions into the guide as a distinct section near the end, each with the objective it tests, the answer, and **why each distractor is wrong**. Do not just list them.

---

## 3. Tooling recipe — exact commands that work on this machine

`python3` is at `/opt/miniconda3/bin/python3`. `pandoc` and `soffice` are installed. **There is no `pdflatex` or `wkhtmltopdf`** — do not build the PDF through LaTeX.

```bash
python3 -m pip install python-pptx pymupdf weasyprint beautifulsoup4 lxml
```

**Step A — extract all slide text + speaker notes.** Speaker notes carry content Dr. Bagh does not say out loud; never skip them. Recurse into groups (`shape_type == 6`) and handle `sh.has_table`.

```python
from pptx import Presentation
prs = Presentation("03 - Electron Transport Chain/Lecture 06 Bagh_Electron Transport Chain.pptx")
for i, slide in enumerate(prs.slides, 1):
    # walk shapes recursively; print sh.text_frame.text and table cells
    if slide.has_notes_slide:
        print(slide.notes_slide.notes_text_frame.text)
```

**Step B — render every slide to PNG and actually look at them.** ETC is the most diagram-dependent lecture in this block; slide text alone will mislead you badly. This step is not optional.

```bash
soffice --headless --convert-to pdf --outdir . "03 - Electron Transport Chain/Lecture 06 Bagh_Electron Transport Chain.pptx"
```
```python
import fitz
d = fitz.open("Lecture 06 Bagh_Electron Transport Chain.pdf")
for i, p in enumerate(d, 1):
    p.get_pixmap(dpi=110).save(f"pages/s{i:02d}.png")
```
`MuPDF error: format error: No common ancestor in structure tree` is harmless noise; the render succeeds. Then **read the rendered PNGs with your image tool** — every slide, given how visual this topic is.

**Step C — extract embedded figures at native resolution** for the ones you keep. Some pictures sit inside *placeholders*, not `Picture` shapes, so a `shape_type == 13` filter silently misses them. Wrap `sh.image` in try/except over **all** shapes:

```python
for j, sh in enumerate(slide.shapes):
    try: img = sh.image
    except Exception: continue
    open(f"figs/slide{i:02d}_{j}.{img.ext}", "wb").write(img.blob)
```
Save the ones you use to `Lecture_03_figures/`; delete the rest before you finish.

**Step D — build the PDF with WeasyPrint.**
```python
from weasyprint import HTML
HTML(filename="guide.html").write_pdf("out.pdf")
```
Write the HTML and CSS into the repo folder so relative image paths resolve.

**Step E — markdown version.** Pandoc's raw HTML→GFM conversion produces unusable div soup. Pre-process with BeautifulSoup first:
- unwrap layout divs (`.hdr`, `.two-col`, `.cheat`) and all `<span>`s
- convert each colored callout div into a `<blockquote>` whose first line is `<strong>LABEL — subtitle</strong>`
- convert `<figure>` → `<p><img></p>` + `<p><em>caption</em></p>`
- replace the `.map` ASCII block with a placeholder token, then substitute a hand-written fenced code block afterward (`get_text()` mangles `<br>`-based layouts)
- inside tables: replace `<br>` with ` · `, expand `colspan` into repeated cells, strip all `class`/`style`/`colgroup` — otherwise pandoc emits raw HTML tables instead of pipe tables
- then `pandoc -f html -t gfm --wrap=none`, and regex out doubled labels like `**MEMORIZE — Memorize — …**`

**Verify your own output.** Render the finished PDF back to PNGs and build a PIL contact sheet to catch layout blowouts, orphaned headings and dead whitespace. Report the final page count.

---

## 4. What I've learned about this professor

- **Repetition = exam priority.** In Lecture 1 she said "NADPH is never a source of ATP" and "insulin always dephosphorylates" five-plus times each. Count repetitions in the transcript and let that drive emphasis — but state each fact **once** in the guide, in its best home.
- **She flags high-yield verbally**: *"please know that," "kindly remember," "don't mess up there," "very very important," "always and always," "please don't pick…"*. Those sentences are the exam.
- **She integrates across lectures deliberately.** The ETC transcript opens: *"I like to bring concepts from previous lecture because… we cannot learn biochemistry piecemeal."* She spends the opening minutes re-deriving catabolism → loss of hydrogen → NADH/FADH₂ from Lecture 1. Handle that with a short bridge section and cross-references, not a re-teach.
- **She insists on clinical application**: *"we are not learning pure biochemistry, we are learning biochemistry applicable to clinical medicine."* Every mechanism gets a clinical hook. ETC is the richest lecture in the block for this — surface all of them.
- **The transcript is a rough auto-transcription with heavy phonetic garbling.** Normalize silently. Prior examples: `kynise`→kinase, `coalent`→covalent, `alosic`→allosteric, `estile COA`→acetyl-CoA, `exagonic`→exergonic, `ura`→urea. Expect ETC equivalents: `ubiquinone/ubiquinol`, `cytochrome`, `chemiosmotic`, `oligomycin`, `rotenone`, `antimycin`, `dinitrophenol/DNP`, `thermogenin`, `uncoupler`, `azide`, `oxidative phosphorylation`, `proton motive force`, `superoxide`, `catalase`, `glutathione peroxidase`.
- **Slides contain real errors and loose wording.** Preserve the version the exam is written from **and** give the correct version beside it in a grey `.note` block. See §5 for the specific ETC landmines.
- **Deck quirks**: leftover text boxes whose titles contradict the slide; embedded images cropped or truncated in the source file; in-class multiple-choice questions where **every distractor describes the opposite concept**, with the answer boxed in red. Capture those questions and explain the discriminations.
- Figure credits you'll see: **Murray, Harper's Illustrated Biochemistry 25th ed.** (heavily used in this deck), Lippincott Williams & Wilkins, Berg/Tymoczko/Stryer.

---

## 5. ETC-specific content warnings — check these explicitly

**a) The P:O ratio discrepancy — the biggest one.** The interactive-session deck states **NADH = 3:1 and FADH₂ = 2:1** (Harper's 25th ed.). Modern measurements, including **Lippincott 6th ed., give ~2.5 and ~1.5**. The course will test the deck's numbers. Give both, state plainly which one to bubble in, and explain that the newer values reflect non-integer proton stoichiometry. This is exactly the kind of thing to put in a grey `.note` block.

**b) Inhibitors vs uncouplers — the whole point of the lecture.** Build one clean discrimination table covering, for each agent: what it binds, which complex, effect on **electron flow**, on **oxygen consumption**, on **ATP synthesis**, and on the **proton gradient**. Cover at minimum rotenone, antimycin A, cyanide, carbon monoxide, azide, H₂S, oligomycin, 2,4-dinitrophenol, and thermogenin/UCP1. The counterintuitive one the deck tests directly: **uncouplers *increase* oxygen consumption while *decreasing* ATP synthesis**, whereas inhibitors decrease both. Make sure that logic is explained, not just tabulated.

**c) E°′ and ΔG.** The objectives require defining **reducing equivalent, E°′, ΔE°′**, and the relationship of ΔE°′ to ΔG. Include `ΔG°′ = −nFΔE°′` and explain the sign logic: electrons flow spontaneously from **low** E°′ to **high** E°′, a positive ΔE°′ gives a negative ΔG. Pull just enough from the Thermodynamics primer to make this land — do not fold in the whole primer, which is its own item.

**d) Watch for these common slide-level imprecisions:** complexes numbered vs named inconsistently; whether Complex II pumps protons (**it does not**); whether cytochrome c and CoQ are "complexes" (**they are mobile carriers, not complexes**); "ATP synthase = Complex V" usage; conflating the chemiosmotic *gradient* with the *proton-motive force* (which has both a chemical ΔpH and an electrical Δψ component); and loose statements about where ROS are generated.

**e) Clinical hooks to capture**: CO poisoning (including the "Richard's story" vignette — history, exam findings, diagnosis), cyanide poisoning and its treatment, the propane-in-a-closed-tent case, oligomycin's effect on oxygen consumption, brown adipose tissue / non-shivering thermogenesis via thermogenin, and ROS-related pathology.

---

## 6. Document structure and how to explain

Organize by the lecture's own **learning objectives**, in her order — she says *"pay close attention to your learning objectives because they are tied to your questions."* The interactive-session deck confirms this by numbering its questions against those objectives.

For every topic, separate two layers:
1. **The concept** — the why, the intuition, written as prose that genuinely explains.
2. **The specifics** — the facts, numbers, names and equations to memorize mechanically.

They sit next to each other, visually distinguished, but **never labeled "conceptual" and "specific" in the document text**. Use the callout system, which is already in the CSS:

| Class | Colour | Meaning |
|---|---|---|
| `.concept` | blue | The idea / the why |
| `.detail` | gold | Memorize this |
| `.trap` | red | Traps, "always/never," discrimination points |
| `.clin` | green | Clinical correlation |
| `.note` | grey | Correction where the lecture or slide was loose |
| `.rule-strip` | solid bar | One-line rules that deserve to shout |

Also already styled: `<table>` (navy header, zebra rows, `td.hi` highlight), `<figure>`/`<figcaption>`, `ol.qlist` (numbered circles), `.two-col`, `.map` (ASCII diagram box), `.hdr` + `.metagrid` (compact header), `.pagebreak`.

**Sections to produce:**
1. Compact header block — session, instructor, readings, exam — plus a 3–4 sentence orientation. **Not a full cover page.**
2. A short bridge section connecting back to Lectures 1–2 (catabolism → loss of hydrogen → NADH/FADH₂ → *this lecture is where those carriers get cashed in*), since she opens that way.
3. One section per learning objective, in her sequence.
4. **The interactive-session practice questions**, each with its tagged objective, answer, and distractor analysis.
5. A short "where the lecture was imprecise — reconciled" table (what was said → what's precisely true → does it matter for the exam).
6. A two-column rapid-review sheet that **doubles as** the always/never list — bold every always/never rule inline. Cap at 2 pages.
7. Self-test, 12–15 questions, one line each with a one-line answer inline.

**Explanation quality bar:** causal explanations, not restated definitions. Build memory hooks where they genuinely help. When a fact is arbitrary, say so and mark it for brute-force memorization. ETC rewards this heavily — the inhibitor/uncoupler table is nearly impossible to memorize cold but becomes obvious once someone explains what happens to the proton gradient in each case.

---

## 7. Compression rules

**a) Figures: 7–10 maximum.** Lecture 1 used 7 for 41 slides. ETC is genuinely more spatial, so it earns a couple more — likely the chain with its four complexes and two mobile carriers, the chemiosmotic/ATP-synthase mechanism, the inhibitor binding sites mapped onto the chain, and possibly the CO/haem figure. Only include an image when **the image itself is the information**. **Cut**: decorative photos, generic textbook tables you are already typesetting, low-information cartoons, and any figure needing a caption longer than the figure is useful. **Never include both a screenshot of a table and a typeset version of the same table** — typeset it and drop the image.

**b) Figure captions: 1–2 sentences.** Teaching goes in the body; the caption only orients.

**c) One review artifact, not two.** Do not write a separate "always/never list" *and* a cheat sheet — on Lecture 1 they duplicated each other for ~3 pages. Merge into a single two-column rapid-review sheet with the rules bolded.

**d) Eliminate cross-block repetition.** Each fact once, in its best home. The blue block explains *why*, the gold block lists *what*, and they must not restate each other. The cheat sheet is keyword recall, not sentences.

**e) Page breaks:** use `.pagebreak` only before the rapid-review sheet, so it stays printable standalone. Forced breaks elsewhere cost 3–4 pages of dead whitespace.

**f) Tight prose.** Cut throat-clearing ("It is worth noting that…", "As we will see…"). Same explanatory depth, fewer words.

**Do not compress by** dropping facts, dropping speaker-note content, dropping clinical correlations, dropping the corrections table, or replacing explanations with bullet fragments. Full information and full explanation, in less space.

---

## 8. Deliverables

Write into `/Users/yoelplutchok/Desktop/Biochem_Fall/03 - Electron Transport Chain/`:

1. `Lecture 03 - Electron Transport Chain - STUDY GUIDE.pdf` ← **primary deliverable**
2. `Lecture 03 - Electron Transport Chain - STUDY GUIDE.md`
3. `Lecture_03_figures/` — only the figures actually used
4. `Lecture 03 - STUDY GUIDE (html source).html` and `.css`

Confirm the final page count, and say so if it exceeded 26 pages and why.

---

## 9. Working notes

- Use a scratchpad directory for intermediates (renders, contact sheets); keep the repo folder to the four deliverables above.
- Read the **full** transcript, **all 49 slides**, and **slides 2–16 of the interactive deck** before writing a word of the guide. Don't stream-write while still extracting.
- Reconcile sources actively: the transcript shows what she emphasized and added verbally; the slides give canonical wording and figures; the interactive deck gives the question style. Where the slides and the transcript disagree, the slides are usually the exam's source of truth and the transcript is usually the more correct biochemistry — say so when it matters.
- **Don't fabricate.** If a slide is illegible or a transcript passage unrecoverable, say so in the guide rather than inventing content.
- Report at the end: what you included, what judgment calls you made, and anything unresolved.

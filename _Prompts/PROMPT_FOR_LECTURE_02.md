# PROMPT — Lecture 02 Study Guide

Build a complete, compressed study guide for **Lecture 2: Enzymes and Enzyme Kinetics** (Dr. Shilpika Bagh) in my Medical Biochemistry & Genetics I course. Output a **PDF** (primary deliverable) plus a markdown version.

This exact job was already done for Lecture 1. The pipeline, the design system, and the pitfalls are all documented below — follow them and you should be efficient. **The one thing to change from Lecture 1: the output was 36 pages, which is too long. Target 20–24 pages for Lecture 2 without losing information.** Specific compression rules are in section 6.

---

## 1. Source files (all paths absolute)

Working directory: `/Users/yoelplutchok/Desktop/Biochem_Fall`

> **NOTE ON REPO LAYOUT (updated):** the repo is now organised into one folder per lecture, each holding the deck and its transcript together. Root contains: `01 - Overview of Metabolic Pathways`, `02 - Enzymes and Enzyme Kinetics`, `03 - Electron Transport Chain`, `04 - Signal Transduction`, `05 - Carbohydrate Digestion`, `Primer 1 - Thermodynamics`, `Primer 2 - Carbohydrate Structure`, `_Interactive Sessions`, `_Course Documents`, `_Prompts`. All paths below reflect this. Write your deliverables **into the lecture's own folder**, keeping the HTML, CSS and figures folder together so relative paths resolve.


| What | Path |
|---|---|
| **Slide deck** | `/Users/yoelplutchok/Desktop/Biochem_Fall/02 - Enzymes and Enzyme Kinetics/Lecture 02_Bagh_Enzyme and enzyme kinetics.ppt` |
| **Lecture transcript** | `/Users/yoelplutchok/Desktop/Biochem_Fall/02 - Enzymes and Enzyme Kinetics/Lecture 2 biochem.md` |
| **Syllabus** | `/Users/yoelplutchok/Desktop/Biochem_Fall/_Course Documents/DO Med Biochem genetics I syllabus Fall 2026 7_22 share.docx` |
| **Required textbook** | `/Users/yoelplutchok/Desktop/Fall Courses/Medical Biochemistry and Genetics I/sga/general/textbooks/Lippincott Biochemistry - 6th Edition .pdf` |
| **Backup textbook** | `.../sga/general/textbooks/BRS Biochemistry, Molecular Biology, and Genetics 6E (2013).pdf` |
| **Lecture 1 guide (style reference)** | `/Users/yoelplutchok/Desktop/Biochem_Fall/01 - Overview of Metabolic Pathways/Lecture 01 - Overview of Metabolic Pathways - STUDY GUIDE.pdf` |
| **Reusable CSS** | `/Users/yoelplutchok/Desktop/Biochem_Fall/01 - Overview of Metabolic Pathways/Lecture 01 - STUDY GUIDE (html source).css` |
| **HTML source example** | `/Users/yoelplutchok/Desktop/Biochem_Fall/01 - Overview of Metabolic Pathways/Lecture 01 - STUDY GUIDE (html source).html` |

**Syllabus context, already looked up — don't re-derive it:**
- Lecture 2 is Week 1, Session 1, **Tue 8/4, 1–2 PM**, instructor **Bagh**, delivered in the same session as Lecture 1.
- Required reading: **Lippincott Illustrated Reviews: Biochemistry Ch. 5**. Also **Panini, *Medical Biochemistry: An Essential Textbook*, 2nd ed., Ch. 5**. Suggested: **Marks' Basic Medical Biochemistry 5th ed., Ch. 8**.
- Assessed on **Foundation Exam #1, 8/17, 11 AM–1 PM**, which also covers: Overview of metabolic pathways, ETC/uncouplers/inhibitors/ROS, Thermodynamics primer, Signal transduction, Carbohydrate digestion, Carbohydrate structures.
- In the syllabus table, "L Ch N" = Lippincott chapter N.

---

## 2. CRITICAL GOTCHA — read before you touch the deck

**The Lecture 2 deck is a legacy binary `.ppt`, not `.pptx`. `python-pptx` cannot open it and will throw `PackageNotFoundError`.** Convert it first with LibreOffice:

```bash
cd /private/tmp/<your-scratchpad>
soffice --headless --convert-to pptx --outdir . "/Users/yoelplutchok/Desktop/Biochem_Fall/02 - Enzymes and Enzyme Kinetics/Lecture 02_Bagh_Enzyme and enzyme kinetics.ppt"
```

I verified this works. **The converted deck has 55 slides** (Lecture 1 had 41 — Lecture 2 is meaningfully bigger, which makes the compression rules in §6 more important, not less).

Do **all** downstream work (text extraction, image extraction) on the converted `.pptx`.

---

## 3. Tooling recipe — exact commands that work on this machine

`python3` is at `/opt/miniconda3/bin/python3`. `pandoc` and `soffice` are installed. **There is no `pdflatex` or `wkhtmltopdf`** — do not try to build the PDF through LaTeX.

Install these (all confirmed to install cleanly):
```bash
python3 -m pip install python-pptx pymupdf weasyprint beautifulsoup4 lxml
```

**Step A — extract all slide text + speaker notes.** Speaker notes carry real content Dr. Bagh doesn't say out loud; never skip them. Walk groups recursively and pull tables:

```python
from pptx import Presentation
prs = Presentation("converted.pptx")
for i, slide in enumerate(prs.slides, 1):
    # print shape text; recurse into shape_type == 6 (groups); handle sh.has_table
    if slide.has_notes_slide:
        print(slide.notes_slide.notes_text_frame.text)
```

**Step B — render every slide to PNG so you can SEE the figures.** Slide text alone is useless for diagram-heavy slides — roughly half the teaching content lives in images. You must actually look at them.

```bash
soffice --headless --convert-to pdf --outdir . converted.pptx
```
```python
import fitz
d = fitz.open("converted.pdf")
for i, p in enumerate(d, 1):
    p.get_pixmap(dpi=110).save(f"pages/s{i:02d}.png")
```
`MuPDF error: format error: No common ancestor in structure tree` is harmless noise — the render succeeds. Then **read the rendered PNGs with your image-reading tool**, at minimum every slide whose extracted text was thin or that contained a `<PICTURE>` / picture-placeholder shape.

**Step C — extract embedded figures at native resolution** (for the ones you decide to keep). Note that some pictures sit inside *placeholders*, not `Picture` shapes, so a `shape_type == 13` filter will miss them — wrap `sh.image` in try/except over **all** shapes instead:

```python
for j, sh in enumerate(slide.shapes):
    try: img = sh.image
    except Exception: continue
    open(f"figs/slide{i:02d}_{j}.{img.ext}", "wb").write(img.blob)
```
Save them to `/Users/yoelplutchok/Desktop/Biochem_Fall/Lecture_02_figures/`.

**Step D — build the PDF with WeasyPrint from HTML + CSS.**
```python
from weasyprint import HTML
HTML(filename="guide.html").write_pdf("out.pdf")
```
Write the HTML and CSS into the repo folder so relative image paths resolve. Reuse the Lecture 1 CSS file (path in §1) — it is already built and tested — with the modifications in §6.

**Step E — markdown version.** Pandoc's raw HTML→GFM conversion produces unusable div soup. Pre-process the HTML with BeautifulSoup first:
- unwrap layout divs (`.cover`, `.two-col`) and all `<span>`s
- convert each colored callout div into a `<blockquote>` whose first line is `<strong>LABEL — subtitle</strong>`
- convert `<figure>` → `<p><img></p>` + `<p><em>caption</em></p>`
- inside tables: replace `<br>` with ` · `, expand `colspan` into repeated cells, strip all `class`/`style`/`colgroup` — otherwise pandoc bails to raw HTML tables instead of pipe tables
- then `pandoc -f html -t gfm --wrap=none`
- finally regex out any doubled labels like `**MEMORIZE — Memorize — ...**`

**Verify your own output.** Render the finished PDF back to PNGs and build a contact sheet (PIL grid) to catch layout blowouts, orphaned headings, and dead whitespace. Don't ship unverified.

---

## 4. What I learned about this professor and this material

- **She teaches by relentless repetition.** In Lecture 1 she stated "NADPH is never a source of ATP" and "insulin always dephosphorylates" five-plus times each. **Repetition count in the transcript = her exam priority signal.** Track it and let it drive emphasis. But the *guide* should state each fact once, in its best home — don't mirror her repetition.
- **She flags high-yield verbally.** Watch for: *"please know that," "kindly remember," "don't mess up there," "very very important," "always and always," "please don't pick..."*. Those sentences are the exam.
- **She explicitly defers content**: *"you will learn this later," "which will be taught with enzymes."* Note the deferral, don't chase it.
- **She insists on clinical application**: *"we are not learning pure biochemistry, we are learning biochemistry applicable to clinical medicine."* Every mechanism gets a clinical hook. Find them and surface them.
- **The transcript is a rough auto-transcription with heavy phonetic garbling.** Silently normalize. Lecture 1 examples: `kynise`→kinase, `coalent`→covalent, `alosic/alostric`→allosteric, `estile/aile COA`→acetyl-CoA, `zyosin`→zymogen, `tripsogen`→trypsinogen, `exagonic`→exergonic, `nascin`→niacin, `ura`→urea, `gluconneioenesis`→gluconeogenesis. Expect enzyme-kinetics equivalents: likely `michalis/mikelis`→Michaelis, `linewaver/line weaver`→Lineweaver, `vmax/v max`, `km`, `alostric`→allosteric, `zymogen`, `isoenzyme/isozyme`, `competitive/noncompetitive/uncompetitive`, `troponin`, `creatine kynise`→creatine kinase.
- **The slides contain real errors and loose wording.** Your job is to preserve the version the exam is written from *and* give the correct version beside it. Lecture 1 examples: SAM called "acetyl-S-methionine" (it's S-adenosylmethionine, donates methyl); slide labeling insulin a "counter-regulatory hormone" (it isn't — the others are counter-regulatory *to* it); ΔG conflated with activation energy. **Enzyme kinetics is a high-risk area for this** — watch especially for: Km described as "affinity" without the inverse relationship stated; "Vmax is reached" vs asymptotically approached; noncompetitive vs uncompetitive inhibition mixups; the claim that enzymes "lower activation energy" being confused with changing ΔG or shifting equilibrium (enzymes do **not** change ΔG or Keq — they change the rate at which equilibrium is reached, equally in both directions); catalytic efficiency (kcat/Km) vs turnover number (kcat); "zero-order" vs "first-order" region of the Michaelis-Menten curve.
- **Deck quirks to expect**: leftover/orphan text boxes whose content contradicts the slide (Lecture 1 slide 19 was titled "Lipoic Acid" but was actually the full activated-carriers table — ignore the stale title); embedded images that are cropped or truncated in the source file (Lecture 1 slide 4's handwritten summary was cut off mid-line — I typeset the missing lines from the transcript); in-class multiple-choice questions where **all distractors describe the opposite concept**, with the answer boxed in red on the slide. Capture those questions *and* explain why each distractor is wrong — it teaches the discrimination.
- Figure credits you'll likely see again: Lippincott Williams & Wilkins; Berg/Tymoczko/Stryer *Biochemistry* 5th ed.; Lieberman *Marks' Basic Medical Biochemistry*.
- Use the Lippincott chapter to fill genuine gaps and give mechanism, not to expand scope. Lecture 2's chapter is **Ch. 5 (Enzymes)** — locate it by scanning page text for the chapter title.

---

## 5. Document structure and how to explain things

Organize by the lecture's own **learning objectives** — Dr. Bagh states them up front and says *"pay close attention to your learning objectives because they are tied to your questions."* Use her objectives as the top-level sections, in her order.

For every topic, separate two layers — this is the explicit request from the reader:
1. **The concept** — the "why," the intuition, the thing that makes the rest inevitable. Written as prose that actually explains, not as a definition restated.
2. **The specifics** — the raw facts, numbers, names, lists, and equations that must be mechanically memorized.

They live next to each other, visually distinguished, but **never labeled "conceptual" and "specific" in the document text**. Use the color/callout system instead.

Callout types (already in the CSS, with these exact class names):
| Class | Border | Meaning |
|---|---|---|
| `.concept` | blue | The idea / the why |
| `.detail` | gold | Memorize this |
| `.trap` | red | Traps, "always/never," discrimination points |
| `.clin` | green | Clinical correlation |
| `.note` | grey | Correction or precision note where the lecture was loose |
| `.rule-strip` | solid bar | One-line rules that deserve to shout |

Also available and already styled: `<table>` (dark navy header, zebra rows, `td.hi` for highlighted cells), `<figure>`/`<figcaption>`, `ol.qlist` (numbered circles), `.two-col` (column layout for the cheat sheet), `.pagebreak`.

**Sections to produce:**
1. Compact header block — course/session/instructor/readings/exam, and a 3–4 sentence "what this lecture actually is" orientation. **Not a full cover page.**
2. One section per learning objective, following her sequence.
3. A short "where the lecture was imprecise — reconciled" table (what was said → what's precisely true → does it matter for the exam).
4. A combined rapid-review sheet in `.two-col` that **doubles as** the always/never list — see §6.
5. A self-test of 12–15 recall questions with answers inline.

**Explanation quality bar:** the reader wants to be able to process, remember, and repeat this. So: give causal explanations, not restatements. Build memory hooks where they genuinely help. When a fact seems arbitrary, either supply the underlying reason or say plainly that it's arbitrary and must be brute-forced. Enzyme kinetics rewards this heavily — Km, Vmax, and the inhibition types are much easier to hold once someone explains *why* the curves move the way they do rather than making you memorize four rows of a table.

---

## 6. COMPRESSION — the main change from Lecture 1

Lecture 1's guide came out at **36 pages**. That's too long. **Target 20–24 pages for Lecture 2** (which has more slides), with no loss of information. Here is exactly where the bloat came from and how to avoid it:

**a) Figures: 17 → keep 6–9 maximum.** This was the single biggest cost. Only include an image when **the image itself is the information** and prose cannot carry it. For enzyme kinetics that probably means: the Michaelis-Menten curve, the Lineweaver-Burk plot, the inhibition-type plot comparison, the energy-of-activation diagram, an allosteric/sigmoidal curve, and maybe one clinical figure. **Cut**: decorative photos, generic textbook tables you are already reproducing as an HTML table, low-information cartoons, and any figure whose caption ends up longer than the figure is useful. **Never include both a screenshot of a table and a typeset version of the same table — typeset it and drop the image.**

**b) Cut figure captions to 1–2 sentences.** Lecture 1's captions ran 4–6 sentences each. Put the teaching in the body text; the caption only orients the reader to what they're looking at.

**c) Merge the "always/never list" into the cheat sheet.** Lecture 1 had both, and they duplicated each other for ~3 pages. Produce **one** artifact: a two-column rapid-review sheet where the high-yield always/never rules are bolded inline. Cap it at 2 pages.

**d) Eliminate cross-block repetition.** In Lecture 1 the same fact often appeared four times: in the concept block, in the memorize block, in the always/never list, and in the cheat sheet. **State each fact once in its best home.** The concept block explains *why*; the memorize block lists *what*; they must not restate each other. The cheat sheet is pure keyword recall, not sentences.

**e) Trim the self-test to 12–15 questions**, each a single line with a single-line answer.

**f) Tighten the CSS.** Start from the Lecture 1 CSS and apply these deltas:
- `@page` margin: `16mm 15mm 18mm` → **`13mm 13mm 15mm`**
- `body` font-size: `10.1pt` → **`9.7pt`**; line-height `1.46` → **`1.38`**
- callout padding: `3mm 4mm 2.4mm` → **`2.4mm 3.2mm 2mm`**; margins `3mm 0 4mm` → **`2.2mm 0 3mm`**
- `h2` margin-top `9mm` → **`6mm`**; `h3` margin-top `6.5mm` → **`4.5mm`**
- `figure` max-height `108mm` → **`78mm`**; padding `3mm` → **`2mm`**
- table font-size `8.9pt` → **`8.5pt`**; cell padding `1.8mm 2.4mm` → **`1.4mm 2mm`**
- Keep `break-inside: avoid` on figures and callouts, but **do not** put `.pagebreak` on every objective — only where a section genuinely starts a new major topic. Forced breaks cost 3–4 pages of dead whitespace in Lecture 1.

**g) Write tighter prose.** Lecture 1's explanations were good but verbose. Same explanatory depth, fewer words. Cut throat-clearing sentences ("It is worth noting that...", "As we will see..."). Do not cut the actual explanation.

**Do not compress by**: dropping facts, dropping speaker-note content, dropping clinical correlations, dropping the corrections table, or replacing explanations with bullet fragments. The reader explicitly wants full information and full explanation in less space.

---

## 7. Deliverables

Write into `/Users/yoelplutchok/Desktop/Biochem_Fall/02 - Enzymes and Enzyme Kinetics/`:

1. `Lecture 02 - Enzymes and Enzyme Kinetics - STUDY GUIDE.pdf` ← **primary deliverable**
2. `Lecture 02 - Enzymes and Enzyme Kinetics - STUDY GUIDE.md`
3. `Lecture_02_figures/` — only the figures you actually used
4. `Lecture 02 - STUDY GUIDE (html source).html` and `.css` — so it can be regenerated or edited later

Confirm the final page count and tell me if it exceeded 24 pages and why.

---

## 8. Working notes

- Use a scratchpad directory for intermediate files (renders, contact sheets, converted decks) — keep the repo folder clean, only the four deliverables above.
- Read the **full** transcript and **all** slides before writing a single word of the guide. Don't stream-write while still extracting.
- Reconcile the two sources actively: the transcript tells you what she emphasized and what she added verbally; the slides tell you the canonical wording and the figures. Where they disagree, the slides are usually the exam's source of truth and the transcript is usually the more correct biochemistry — call that out when it matters.
- **Don't fabricate.** If a slide is illegible or a transcript passage is unrecoverable, say so in the guide rather than inventing content.
- Report honestly at the end: what you included, what judgment calls you made, and anything you couldn't resolve.

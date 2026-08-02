# PROMPT — Build the Lecture 03 study guide as a web page

Build my study guide for **Electron Transport Chain, Uncouplers, Inhibitors and ROS** (Medical Biochemistry & Genetics I, Fall 2026).

**The deliverable is one HTML page that I will serve from GitHub Pages.** No PDF. No markdown. No print pipeline. A v1 guide exists and is in the wrong voice; this is a **rewrite from the sources**, not an edit of v1.

---

## 1. THE STANDARD — read this before anything else

The house style is set by **Lecture 02 v2**. Read both of these before you start:

- `02 - Enzymes and Enzyme Kinetics/Lecture 02 - STUDY GUIDE v2 (html source).html`
- `02 - Enzymes and Enzyme Kinetics/Lecture 02 - STUDY GUIDE v2 (html source).css`

Those are print files, so ignore their `@page` rules and millimetre units — you are rebuilding for screen (§7). What you are taking from them is the **voice**, the **structure**, and the **emphasis system**. Everything below states the standard explicitly so you don't have to reverse-engineer it, but read them anyway.

### Rule 1 — No meta-references. None.

**Never** write: "she said," "Dr. Bagh emphasized," "the slide shows," "the deck states," "the lecture covered," "slide 23," "the speaker notes say," "in her words," "the professor's example."

Write the biochemistry directly, as fact. Not *"She stressed that cyanide blocks complex IV"* but **"Cyanide binds the ferric heme of cytochrome c oxidase, blocking electron transfer to oxygen at Complex IV."**

The only permitted non-content text is a minimal course header (course, session, reading, exam date) and a two-line legend for the emphasis system.

### Rule 2 — Synthesize, don't transcribe.

Absorb everything, then **reorganize into the clearest possible structure**, which will often differ from the order presented. Merge material scattered across the deck; split anything crammed together. Your organization should be *better* than the source's.

This matters here because the deck introduces the chain, then inhibitors, then comes back to the chain, then to ATP synthesis. Consolidate each into one authoritative treatment.

### Rule 3 — Reconcile errors silently.

Sources contain genuine errors and imprecise wording. **Fix them using Lippincott and your own knowledge, and say nothing about it in the document.** No corrections table, no "what was said vs. what is true," no footnotes.

*Exception:* where the course's preferred answer differs from the strictly-correct one in a way that could cost exam points, give the course's answer as the headline fact and the precision as a brief parenthetical — with no reference to where either came from.

**Report every correction you made to me in chat, not in the document.**

### Rule 4 — Each fact appears exactly ONCE. This is the strictest rule in the brief.

Not "once per section." Not "once in prose and once in a table." **Once in the entire main body.**

For every fact, pick its single best home *first*, then write only there:

| If the fact is… | Its home is… |
|---|---|
| one item in a set that varies along shared dimensions | **a table row** — and nowhere else |
| a contrast between two confusable things | **a `.vs` box** — and nowhere else |
| a mechanism or a causal chain | **prose** — and nowhere else |
| a value, threshold or constant | wherever its subject already lives; never on its own |
| genuinely enumerable | **a labelled list** — and nowhere else |

Having chosen, the other formats must not mention it. Prose that introduces a table should read as a *reason to look at the table*, never as a summary of it.

**Traps to check for:**
- A prose sentence and a table cell carrying the same fact
- A `.must` band restating a fact from the table or list next to it
- A figure caption restating the surrounding prose
- Two objectives each giving a concept a full treatment — pick one home, cross-reference in half a sentence
- The orientation map naming a fact the body then states again

**Exemption, and only this one.** The **self-test** and the **rapid-review sheet** are retrieval instruments. Re-encountering material there is their entire purpose. Everything before them says each thing once.

### Rule 5 — Write concisely.

Aim for **2–4 sentences** where a first draft used 5–8, carrying identical information.

- One sentence per idea. Split long sentences rather than chaining "which is why… and this means… so that…".
- Cut hedges: *very, really, actually, quite, essentially, basically, simply, in fact, of course, it is worth noting, importantly.*
- Cut throat-clearing: *"It is important to understand that…", "As we will see…", "Note that…"*.
- Never restate an idea a second way. Delete every *"in other words," "put differently."*
- Prefer verbs to nominalizations: "phosphorylates" not "carries out the phosphorylation of."
- Don't restate a heading in the first line under it.

**Calibration.** Wordy (88 words):

> A competitive inhibitor is a molecule that closely resembles the substrate in its structure, and because of this resemblance it is able to bind to the active site of the enzyme, which is the same site the substrate would otherwise occupy. Because the two are competing for the same site, the effect of the inhibitor can be overcome by simply raising the substrate concentration high enough, and this is why the Vmax of the reaction remains unchanged while the apparent Km is increased.

Target (52 words, same facts):

> A competitive inhibitor resembles the substrate closely enough to bind the active site, so substrate and inhibitor compete for it. Raising [S] outcompetes the inhibitor, so **Vmax is unchanged**; more substrate is needed to reach half-maximal velocity, so **apparent Km rises**.

**Where not to compress.** Explanations must still explain. Never sacrifice a causal "because" to save three words. **The energetics in particular must stay legible**: if I can't follow why ΔG°′ = −nFΔE°′ makes a positive ΔE°′ favourable, you cut too far.

### Rule 6 — Nothing may be lost.

Every fact, number, example, definition, list, exception and clinical link in the deck (including speaker notes), the transcript, and the interactive session must survive somewhere. Concision is about wording, never coverage.

---

## 2. Source files

Working directory: `/Users/yoelplutchok/Desktop/Biochem_Fall`

| What | Path |
|---|---|
| **Slide deck** (49 slides, 14 with speaker notes) | `03 - Electron Transport Chain/Lecture 06 Bagh_Electron Transport Chain.pptx` |
| **Lecture transcript** (~7,300 words, heavily garbled — see §9) | `03 - Electron Transport Chain/ETC Lecture Biochem.md` |
| **Interactive-session deck** | `_Interactive Sessions/Pre discussion Week 1 ETC Signal Tr Carb Dig F26 (1).pptx` — **use slides 2–16 only** (17+ belong to Lectures 04–05) |
| **Thermodynamics primer** — same session, prerequisite for Objective 1 | `Primer 1 - Thermodynamics/Primer 04_Kamath_Thermodynamics.pptx` and `Primer 1 - Thermodynamics/Primer Thermodynamics.md` |
| **v1 guide — mine the last two sections** | `03 - Electron Transport Chain/Lecture 03 - STUDY GUIDE (html source).html` |
| **Reference implementation of the target style** | `02 - Enzymes and Enzyme Kinetics/Lecture 02 - STUDY GUIDE v2 (html source).html` and `.css` |
| **Required textbook** | `/Users/yoelplutchok/Desktop/Fall Courses/Medical Biochemistry and Genetics I/sga/general/textbooks/Lippincott Biochemistry - 6th Edition .pdf` — **Ch. 6, Bioenergetics and Oxidative Phosphorylation**, PDF pages **134–160** (sections I–VII) |
| **Figures** | **None extracted yet** — you are creating `03 - Electron Transport Chain/figures/` from scratch |

**Note the filename.** The deck is called `Lecture 06` because that is its number in the original course files; in delivery order it is **Lecture 03**. Use 03 everywhere in the output.

Already looked up — don't re-derive: this is **Week 1, Session 2, Thu 8/6, 8:30–10 AM**, delivered in the same session as the Thermodynamics primer and Lectures 04–05; required reading **Lippincott Ch. 6**; assessed on **Foundation Exam #1, Mon 8/17, 11 AM–1 PM**.

### The five learning objectives (verbatim from the deck)

1. Define the terms: reducing equivalent, redox potential (E₀′), ΔE₀′, and describe the relationship of ΔE₀′ to ΔG₀′
2. Describe the carriers of reducing equivalents and calculate the energy yield from reduced NAD⁺
3. Describe the sequence of electron transport chain (ETC) components in mitochondria and **reactive oxygen species (ROS) production in ETC**
4. Describe the synthesis of ATP and calculate the energy yield of ETC
5. Compare and contrast the action of uncouplers and inhibitors

**The interactive deck's copy of these objectives drops the ROS clause from #3.** The lecture deck's version is authoritative — ROS is examinable. Do not let the interactive deck's shorter wording narrow your scope.

### What is on interactive-session slides 2–16 — I have already inventoried this

| Slide | Content | Note |
|---|---|---|
| 3 | Thermodynamics: ΔG = ΔH − TΔS · ΔG°′ = −RT log Keq · **ΔG°′ = −nFΔE°′** · ATP hydrolysis ΔG°′ = −7.3 kcal/mol | The bridge into Objective 1. Speaker note expands the mass-action expression |
| 5–6 | Catabolism → biological oxidation → reducing equivalents; NAD⁺/FAD and their vitamins (B3 niacin, B2 riboflavin) | Overlaps Lecture 01 — cross-reference, don't re-teach |
| 7 | ETC diagram with complexes I–IV and **P:O — NADH 3:1, FADH₂ 2:1** | |
| 8 | Oxidative phosphorylation: matrix vs intermembrane space | |
| 9 | Inhibitors, split A/B/C: inhibitors of ETC complexes vs inhibitors of oxidative phosphorylation | |
| 10 | ETC with **CN⁻, azide, H₂S** and **CO** marked at their targets; CoQ = UQ = ubiquinone | |
| 11 | **CO vs cyanide poisoning side by side** — sources, mechanism, treatment (CO: 100% O₂, hyperbaric; CN⁻: amyl nitrite, sodium thiosulfate) | High-yield clinical |
| 12 | **Clinical vignette — "Richard's story":** forklift operator, grand mal seizure, pulse oximetry 99% despite hypoxia, → CO poisoning → lactic acidosis | Use this as a `.clin` box |
| **13** | **Question 1** — death in a closed tent with a propane lantern → **carbon monoxide** | Tagged Obj 5 |
| **14** | **Question 2** — cyanide poisoning treated with amyl nitrite; which species sequesters cyanide → **methemoglobin** | Tagged Obj 5 |
| **15** | **Question 3** — why oligomycin inhibits O₂ consumption in tightly coupled mitochondria → **prevents proton influx through Complex V** | Tagged Obj 5 |
| 16 | **Blank comparison table** — ETC function / oxygen consumption / ATP synthesis × {ETC inhibitors (rotenone, antimycin, CO, CN), ATP synthase inhibitors (oligomycin), uncouplers (2,4-DNP)}, presented as a fill-in exercise. Speaker notes add **dimercaprol/BAL** and **atractyloside** | **This is the single highest-yield object in the lecture** |

All three interactive questions are tagged to **Objective 5**, which tells you where the exam pressure is. Fold all three into the self-test.

---

## 3. Length target — word budgets, not page counts

There are no pages in a web document, so length has to be measured some other way or it stops being falsifiable. Use word counts. For calibration, here is what Lecture 02 v2 actually came to:

| Section | Lecture 02 actual | Lecture 03 target |
|---|---|---|
| Orientation | 81 | **80–120** |
| Objective 1 | 1,185 | **550–750** |
| Objective 2 | 584 | **550–750** |
| Objective 3 | 760 | **750–950** (carries the chain sequence *and* ROS) |
| Objective 4 | 546 | **550–750** |
| Objective 5 | 854 | **800–1,000** (three exam questions land here) |
| **Main body total** | **4,010** | **3,400–4,300** |
| Self-test (32–38 questions) | 2,860 | **2,400–3,000** |
| Rapid-review sheet | 1,010 | **900–1,200** |
| **TOTAL** | **7,880** | **6,700–8,500** |

Count words the same way I did — the text of every `p`, `td`, `li` and `figcaption` between one `h2` and the next. Report your actuals per section when you're done. If a section is over, cut words (Rule 5), never facts (Rule 6).

---

## 4. The emphasis system — reuse it exactly

Three tiers, ported from the Lecture 02 CSS.

**Tier 1 — MUST KNOW.** A **marker applied to a fact where it already lives**, not a band that repeats it:

| The fact lives in… | Mark it by… |
|---|---|
| a table row | `<tr class="must">` — red-tinted row, with a literal `★` in the first cell |
| a `.vs` box | `★` in the `.vshead` bar, and `class="vs must"` to tint the box red |
| a figure | `★` at the start of the `<figcaption>` |
| prose, and the sentence *is* the fact's only statement | the standalone `.must` band |

The standalone band survives **only when it is the fact's single appearance anywhere in the main body** — never as a restatement of a neighbouring table or list.

**Cap at 14–16 marks for the whole document.** Scarcity is what makes it work. Expect roughly four or five standalone bands; the rest are marks on rows, boxes and captions. Tier-1 candidates — **verify each against the sources before marking it**, and add any I've missed:

- ΔG°′ = **−nF ΔE₀′** — a **positive ΔE₀′ means a negative ΔG°′**, i.e. spontaneous
- Electrons flow **from the most negative E₀′ to the most positive**; oxygen is the terminal acceptor at **+0.82 V**
- **P:O ratio — NADH 3:1, FADH₂ 2:1**, because FADH₂ enters at Complex II and bypasses Complex I
- The four complexes in order, and **which three pump protons (I, III, IV) — Complex II does not**
- **Complex V (ATP synthase) is not a proton pump** — it runs the gradient the other way, downhill, to make ATP
- **Coenzyme Q and cytochrome c are the two mobile carriers**; CoQ is lipid-soluble and mobile within the membrane, cytochrome c is water-soluble in the intermembrane space
- **Oxidation and phosphorylation are tightly coupled** — inhibit either and both stop
- **Uncouplers let ETC run faster while ATP synthesis stops**; the energy leaves as heat
- **Inhibitors of ETC stop oxygen consumption; uncouplers increase it** — this is the discriminator the exam uses
- **Cyanide, azide and H₂S block Complex IV; CO blocks Complex IV; rotenone blocks Complex I; antimycin A blocks Complex III; oligomycin blocks Complex V**
- **2,4-dinitrophenol, thermogenin (UCP1) and high-dose aspirin are uncouplers**
- **Thermogenin/UCP1 is in brown adipose tissue and produces nonshivering thermogenesis**
- Cyanide poisoning is treated with **amyl nitrite** (which makes **methemoglobin** to sequester CN⁻) and **sodium thiosulfate**; CO poisoning with **100% or hyperbaric oxygen**
- **Pulse oximetry reads falsely normal in CO poisoning** — it cannot distinguish carboxyhaemoglobin from oxyhaemoglobin
- The two shuttles: **malate–aspartate → NADH in the matrix (3 ATP)**; **glycerol phosphate → FADH₂ (2 ATP)**

Those are written as sentences so you can check them, **not as a specification of how to present them.** Most belong in tables and there they stay.

**Tier 2 — inline bold.** Every term, number or name that could be a fill-in-the-blank answer. Generous but not blanket.

**Tier 3 — `.vs` boxes (confusable pairs).** Two-column box with `<u>` on the single discriminating word. For this lecture at minimum:

- Inhibitor vs uncoupler
- Oxidation vs phosphorylation (and what "tightly coupled" means)
- Complex I vs Complex II entry
- Coenzyme Q vs cytochrome c
- E₀′ vs ΔE₀′
- Malate–aspartate vs glycerol phosphate shuttle
- CO vs cyanide poisoning
- Superoxide dismutase vs catalase vs glutathione peroxidase (three-way — use a table instead if it reads better)

Where two pairs are short, put both in one box.

Also available: `.clin` (green) for clinical correlations, `.map` for the orientation diagram, `.legend`, `figure.side`.

**Keep box count low — target ~15 boxes total** (`.must` + `.vs` + `.clin` combined). The default presentation is a tight prose paragraph carrying the *concept*, immediately followed by a table carrying the *specifics*. Boxes are for emphasis, not routine structure.

---

## 5. Structure of the main body

Organize by the five objectives — they are the natural spine and match how the material is tested.

Open with a **one-page orientation**: a compact `.map` diagram of the mitochondrion — matrix, inner membrane, intermembrane space — showing NADH and FADH₂ entering, the four complexes, the two mobile carriers, protons going out, and Complex V letting them back in to make ATP. Then one tight paragraph tying it together.

**The map is an index, not a summary.** It *names* the pieces and shows how they connect; it does not state the facts about them. "Complexes I, III, IV pump protons" belongs on the map. The P:O ratios do not — those are the ATP-yield table's, and only that table's. Write the map first, then treat every term on it as already-introduced.

**Structural requirements specific to this lecture:**

- **The inhibitor/uncoupler comparison must be a table**, with the three agent classes as rows and *ETC function · oxygen consumption · ATP synthesis · proton gradient · examples* as columns. This is the interactive deck's blank exercise, filled in. Mark the rows Tier 1.
- **The ETC sequence must be a table too**: complex, name, what it accepts, what it passes to, whether it pumps protons, and its inhibitors. One row per complex, plus rows for the mobile carriers.
- **The ATP arithmetic needs to be worked, not asserted.** Show how 3:1 and 2:1 fall out of which complexes are traversed, and carry it through to the per-glucose totals so the shuttle difference is visible.
- Convert any comparative prose into a table. One-line definitions, not paragraphs. Fold examples into the fact they illustrate.
- **ROS gets its own subsection under Objective 3** — superoxide, hydrogen peroxide, hydroxyl radical, and the three defence enzymes. The deck treats it briefly; the objective names it explicitly, so it must be there.

**Figures: 6–8 maximum.** None exist yet, so you are extracting them (§7). Prioritise: the annotated ETC/oxidative-phosphorylation diagram, the inhibitor targets on the chain, the ATP synthase mechanism, the CO/cyanide comparison, and the shuttles. **Rewrite every caption**: captions explain the biology only, in one or two sentences, with no reference to slide numbers. A caption must teach something the reader cannot get from the surrounding prose — how to *read* the diagram, which feature to look at. A caption that summarizes the paragraph above it is a Rule 4 violation.

**Do not include** a corrections section, a sources section, or any "how this document was made" framing.

---

## 6. The last two sections

**Self-test.** `ol.qlist`, each question one line with a one-line answer. Target **32–38 questions covering every part of the material** — audit your finished main body section by section and add questions wherever something testable isn't probed. Fold in **all three interactive-session questions** and every in-deck question, converted to recall format; where a question's distractors teach a real discrimination, put that discrimination in the answer line.

This lecture rewards **numerical drill**. Include questions that make me compute: ΔG°′ from ΔE₀′, ATP yield from a given number of NADH and FADH₂, what happens to the P:O ratio when a specific complex is blocked.

**Rapid-review sheet.** Two-column keyword sheet. Intro line: *"Bold = highest-yield. If you review one page, review this one."* — no reference to the instructor. It must include the **inhibitor/uncoupler grid** and the **complex-by-complex table with inhibitors**; those two are the highest-yield objects in the lecture.

---

## 7. The web build — this is where this brief differs from the earlier ones

### 7.1 What you are producing

```
03 - Electron Transport Chain/
  index.html          ← the whole guide: one self-contained document
  figures/            ← real image files, referenced with relative paths
    01-etc-overview.webp
    02-...
```

**Figures are real files, not base64 data URIs.** Inlining images bloats git history, defeats deduplication, and makes every diff useless. Relative paths from `index.html` to `figures/` work identically on GitHub Pages and on your local disk.

`index.html` is a **complete HTML document** — it starts with `<!doctype html>` and has a real `<head>`. Put the CSS in a `<style>` block and the JS in a `<script>` block at the end of the body; a single file is easier to move around than four, and this page has no dependencies.

### 7.2 Required in `<head>`

```html
<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Lecture 03 — Electron Transport Chain</title>
```

The charset declaration is not optional: this document is full of ΔG°′, E₀′, ½O₂, ⇌ and ★, and without it they render as mojibake.

### 7.3 Design system

Match the Lecture 02 palette so the guides read as one set. Define everything as custom properties on `:root`, style components through the tokens, then redefine the tokens for dark.

```
--navy    #1f3a5f   section bars, headings
--crimson #9b2c2c   masthead rule
--must    #b3282d   MUST KNOW marks
--clin    #2f7d4f   clinical boxes
```

Neutrals biased cool toward the navy rather than pure grey: ground `#f6f7f9`, surface `#ffffff`, ink `#171a1f`. Dark: ground `#0e1319`, surface `#151b23`, ink `#e2e7ee`, and lift the accents so they still read on a dark ground (`--must` becomes `#ff8f8b`, `--clin` `#63c78d`, navy text `#8fb3dd`).

**Design both themes.** `@media (prefers-color-scheme: dark)` carries the OS preference; also handle `:root[data-theme="dark"]` and `:root[data-theme="light"]` so an explicit toggle wins in both directions.

**Type.** Serif for reading, sans for chrome and tables, matching the print guides:

```css
--serif: Charter, "Bitstream Charter", "Sitka Text", Cambria, Georgia, serif;
--sans:  -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
```

Do not link a webfont from a CDN and do not embed Charter or Helvetica — they are licensed system faces. The stack above resolves to the same face as the PDFs on my Mac and to a real text serif everywhere else. Body around `1.0625rem` at `1.62` line-height; keep the reading column near **73ch**.

### 7.4 Required behaviours

- **Sticky contents rail** on the left listing the orientation, five objectives, self-test and rapid review, with a **scroll-spy** marking the current section and the **MUST KNOW count per objective** shown as ★ glyphs. Collapses above the layout to a single column below ~60rem.
- **Self-test answers hidden by default**, with a *Show answer* button per question (`aria-expanded` / `aria-controls`) and a global *Reveal all / Hide all* in the rail. This is the main thing the web version does that paper can't — the printed guide could only ask me to cover the answers.
- **Wide content scrolls in its own container.** Every table goes inside a `<div>` with `overflow-x: auto`; same for the `.map`. The page body must never scroll sideways.
- **A print stylesheet** so the page still prints sanely: hide the rail and the reveal buttons, force all answers visible, and set `break-inside: avoid` on figures, boxes, tables and self-test items.
- Visible `:focus-visible` state on every interactive element; honour `prefers-reduced-motion`.

### 7.5 Five traps I have already hit — do not repeat them

1. **Anchor jumps must be instant.** `scroll-behavior: smooth` on `html` makes load-time hash jumps land in the wrong place on a document this long, and a smooth scroll across ~20,000px is slow and loses your place anyway. Handle rail clicks in JS with `scrollIntoView({behavior:'auto'})`.
2. **Every `<img>` needs `width` and `height` attributes.** Without reserved layout space the page reflows as images arrive and anchor jumps land short. `loading="lazy"` is correct here (unlike an inlined page, these are real network fetches) **but only with the dimensions set**.
3. **Do not convert a multi-column flow into a bare CSS grid.** The rapid-review sheet is a sequence of `h3` + content pairs. A grid puts every sibling in its own cell, which splits each heading from its content into different columns. Wrap each heading with its block in a `<section>` first.
4. **Test with the real doctype.** A file served without `<!doctype html>` renders in quirks mode, where `document.scrollingElement` is `body` and scroll measurements are meaningless. Since `index.html` carries its own doctype this should not bite, but if you preview a fragment, wrap it first.
5. **Check the CSS actually parses.** A single malformed declaration (`--crimson:#d munk`) is silently dropped and the theme falls back without any error. After building, assert in the browser that every media query you wrote is present in `document.styleSheets`.

### 7.6 Tooling — verified on this machine

`python3` is at `/opt/miniconda3/bin/python3`. `soffice` is installed. **There is no `pdflatex` or `wkhtmltopdf`, and you do not need them** — nothing here builds a PDF.

```bash
/opt/miniconda3/bin/python3 -m pip install python-pptx pymupdf pillow beautifulsoup4 lxml
```

**Extract slide text and speaker notes.** Notes carry content that is neither on the slide nor spoken — 14 of the 49 slides have them. Recurse into groups (`shape_type == 6`) and handle `sh.has_table`.

```python
from pptx import Presentation
prs = Presentation("03 - Electron Transport Chain/Lecture 06 Bagh_Electron Transport Chain.pptx")
for i, slide in enumerate(prs.slides, 1):
    # print shape text; recurse groups; read tables
    if slide.has_notes_slide:
        print(slide.notes_slide.notes_text_frame.text)
```

**Render the slides and actually look at them.** Most of the teaching content in this lecture is diagrams with no extractable text.

```bash
soffice --headless --convert-to pdf --outdir . "03 - Electron Transport Chain/Lecture 06 Bagh_Electron Transport Chain.pptx"
```

```python
import fitz
d = fitz.open("Lecture 06 Bagh_Electron Transport Chain.pdf")
for i, p in enumerate(d, 1): p.get_pixmap(dpi=110).save(f"pages/s{i:02d}.png")
```

`MuPDF error: format error: No common ancestor in structure tree` is harmless; the render succeeds.

**Extract or crop figures.** Some images sit in *placeholders*, not `Picture` shapes, so a `shape_type == 13` filter misses them — wrap `sh.image` in try/except across **all** shapes. For anything low-resolution or surrounded by dead space, crop it out of the rendered slide PDF instead, which also captures overlaid text boxes the embedded image lacks:

```python
p = d[9]; r = p.rect   # slide 10, 0-indexed
p.get_pixmap(dpi=300, clip=fitz.Rect(r.width*0.05, r.height*0.15,
                                     r.width*0.95, r.height*0.80)).save("fig.png")
```

**Convert figures to WebP for the web.** Resize to ~1200px on the long edge and save at quality 90. On the Lecture 02 figures this took 2.9 MB of print-resolution PNG down to 792 KB with the axis labels still crisp. **Look at the result before committing to it** — these diagrams carry small labels, and if they blur the figure is worthless.

```python
from PIL import Image
im = Image.open(src).convert("RGB")
if im.width > 1200: im = im.resize((1200, int(im.height*1200/im.width)), Image.LANCZOS)
im.save(dst, "WEBP", quality=90, method=6)
```

### 7.7 Verify your own output

Serve the folder and open it — do not just read your own HTML:

```bash
cd "03 - Electron Transport Chain" && /opt/miniconda3/bin/python3 -m http.server 8811
```

Then check, in the browser:

- Every rail link lands with its `h2` at the top of the viewport
- *Show answer* works on individual questions, and *Reveal all* flips all of them and relabels itself
- Both themes render — toggle `document.documentElement.dataset.theme`
- `document.documentElement.scrollWidth === innerWidth` (no sideways scroll) at desktop width, and every table wider than the column sits inside a scroll container
- Every media query you wrote appears in `document.styleSheets`
- The console is clean

**Duplicate-fact audit — do this before you call it done.** It is the check that is always skipped and it is why guides repeat themselves. Read the main body once with no other goal: for every MUST mark, every table row, and every figure caption, ask *"is this fact stated anywhere else in the main body?"* — checking prose above and below, the orientation map, and any other table. Delete the weaker instance. Then extract the facts and check mechanically:

```python
import re, itertools
from bs4 import BeautifulSoup
soup = BeautifulSoup(open("index.html").read(), "lxml")
units = [n.get_text(" ", strip=True) for n in soup.select("td, li, .must, figcaption, p")]
STOP = set("the a an of to in is are and or for by with that this it as be on at from".split())
key = lambda s: {w for w in re.findall(r"[a-z]+", s.lower()) if w not in STOP}
for a, b in itertools.combinations([u for u in units if len(u) > 25], 2):
    ka, kb = key(a), key(b)
    if ka and kb and len(ka & kb) / min(len(ka), len(kb)) > 0.6:
        print("POSSIBLE DUPLICATE\n  ", a[:110], "\n  ", b[:110], "\n")
```

Filter out pairs where one node contains the other, expect false positives from `.vs` boxes (whose two halves are *supposed* to be parallel), and judge each one. **Report how many duplicates you removed.**

**Then grep for Rule 1 and Rule 5 violations:**

```bash
grep -o -i -E "she (said|stressed|emphasi[sz]ed)|dr\.? bagh|the slide|the deck|slide [0-9]+|speaker note|note that|in other words|essentially|basically|it is worth noting" index.html | sort | uniq -c
```

---

## 8. Publishing it on GitHub

This folder is not a git repository yet. Set it up so the guides are served as a small site:

```bash
cd "/Users/yoelplutchok/Desktop/Biochem_Fall"
git init -b main
```

Add a `.gitignore` for `.DS_Store` and the source decks if I don't want ~40 MB of PowerPoint in the repo — **ask me before excluding the decks**, since keeping them makes the repo self-contained.

Commit, create the repo with `gh repo create`, push, then enable **Settings → Pages → Deploy from a branch → main → / (root)**. The guide will be at:

```
https://<username>.github.io/<repo>/03%20-%20Electron%20Transport%20Chain/
```

The spaces in the folder name become `%20`, which works but is ugly. **Recommend to me whether to rename the lecture folders to slugs** (`03-electron-transport-chain`) for cleaner URLs — don't rename anything without asking, since it breaks the paths in the existing guides.

Add a root `index.html` linking to each lecture guide, so the site has a front door.

---

## 9. Reading the sources

- **The transcript is a rough auto-transcription and is worse than Lecture 02's.** Several key terms never appear in recognizable form. Normalize silently. Confirmed substitutions:

| In the transcript | Means |
|---|---|
| `oligomy`, `oligoscin` | oligomycin |
| `attract`, `attractile` | atractyloside |
| `ATP synthes comp complex` | ATP synthase (Complex V) |
| `oxidative phosphorilation` | oxidative phosphorylation |
| `redux potential` | redox potential |
| `reactive oxone species` | reactive oxygen species |
| `hexosmon phosphate shunt` | hexose monophosphate (HMP) shunt |
| `24 ditrophenol`, `24 diitol`, `24 ditro` | 2,4-dinitrophenol |
| `thermogenine` | thermogenin (UCP1) |
| `brown adipos tissue` | brown adipose tissue |
| `P is to O ratio` | P:O ratio |

  Work out any others from context. **Rotenone, antimycin A, ubiquinone and superoxide do not appear in recognizable form at all** — take them from the deck and Lippincott.

- **The transcript contradicts itself on thermogenin**, calling it a "natural uncoupler" once and an "unnatural uncoupler" a minute later. It is natural — UCP1 in brown adipose tissue. Fix silently.
- **Repetition count in the transcript is the emphasis signal** — use it to assign Tier 1, then discard the observation. It never appears in the output.
- Phrases that flag high-yield material: "please know that," "kindly remember," "don't mess up there," "very very important," "always and always."
- **The P:O ratios are NOT an error — do not "correct" them.** The deck says NADH 3:1 and FADH₂ 2:1, and **Lippincott 6th ed. says exactly the same** ("sometimes expressed as a P:O ratio of 3:1… the P:O for FADH₂ is 2:1 because Complex I is bypassed"). Some modern texts give 2.5 and 1.5; that is a different convention, not a correction. Use **3:1 and 2:1** as the headline, and if you mention the modern values at all, do it once, in a parenthetical.
- **Verify every numeric claim** — E₀′ values, ΔG°′, ATP yields, P:O ratios — against Lippincott Ch. 6 before you state it. Transcribed numbers are the least reliable part of these sources.
- Use Lippincott Ch. 6 to fill genuine gaps and supply mechanism: the chemiosmotic hypothesis, the structure of ATP synthase (F₀ and F₁), the two shuttles, the membrane transport systems, and the ROS defence enzymes. **Do not expand scope beyond what the lecture covers** — glycolysis and the TCA cycle belong to later lectures; cross-reference rather than teach them.
- **Lecture 01 already covered** biological oxidation as loss of hydrogen, the NAD⁺/FAD/NADP⁺ carriers and their vitamins, and the anabolism/catabolism split. Interactive slides 5–6 repeat that material. **Cross-reference Lecture 01 in half a sentence; do not re-teach it.**

---

## 10. Report to me in chat when you're done

- **Word count per section**, against the §3 budgets
- **How many duplicate statements the Rule 4 audit caught, and which instance you kept in each case**
- **Every error you silently corrected**, and what you corrected it to
- Anything ambiguous in the sources and how you resolved it
- Confirmation that nothing from the deck, speaker notes, transcript or interactive session was dropped — **say how you checked**, and prefer a scripted checklist over an assurance
- The list of figures you extracted, and any you dropped and why
- Confirmation that the browser checks in §7.7 all pass
- The GitHub Pages URL, once it's live

If anything about the brief is genuinely ambiguous, ask before building rather than guessing.

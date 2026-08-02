# PROMPT — Rebuild the Lecture 02 study guide (v2)

Rebuild my study guide for **Enzymes and Enzyme Kinetics** (Medical Biochemistry & Genetics I, Fall 2026). A v1 exists and is 24 pages; it is too long and written in the wrong voice. This is a **rewrite from the sources**, not an edit of v1.

Output a **PDF** (primary) plus a markdown version.

**A v2 already exists for Lecture 01 and it is exactly what I want.** Read `01 - Overview of Metabolic Pathways/Lecture 01 - STUDY GUIDE v2 (html source).html` and its `.css` before you start — that is the target voice, structure and design system, and its CSS is the one you extend. Everything below describes that standard explicitly, so you don't have to reverse-engineer it, but do look at it.

---

## 1. THE CORE CHANGE — read this before anything else

The v1 guide reads like a *report about a lecture*. The v2 must read like a **self-contained textbook chapter** — the only thing I need to open in order to know this material completely.

### Rule 1 — No meta-references. None.

**Never** write phrases like: "she said," "Dr. Bagh emphasized," "the slide shows," "the deck states," "the lecture covered," "she repeated this five times," "slide 23," "the speaker notes say," "verbatim from," "in her words," "the professor's example was."

Write the biochemistry directly, as fact. Not *"She stressed that enzymes don't change ΔG"* but **"Enzymes lower the activation energy of a reaction. They do not change ΔG, ΔG°′, the equilibrium constant, or the position of equilibrium — only how fast equilibrium is reached."**

The only permitted non-content text is a minimal course header (course, exam date) and a two-line legend for the emphasis system.

### Rule 2 — Synthesize, don't transcribe.

Absorb everything in the sources, then **reorganize it into the clearest possible structure**, which will often differ from the order it was presented in. Merge material that belongs together even if it was scattered across the deck. Split anything that was crammed together confusingly. Your organization should be *better* than the source's.

This matters more for Lecture 02 than it did for Lecture 01: the deck is 55 slides and returns to Km, Vmax and the inhibition graphs repeatedly. Consolidate each into one authoritative treatment.

### Rule 3 — Reconcile errors silently.

The source material contains genuine errors, imprecise wording, and outdated framing. **Fix them using the textbook and your own knowledge, and say nothing about it in the document.** No "corrections" table, no "what was said vs. what is true," no footnotes about discrepancies. Just write the correct version.

*Exception:* where the course's preferred answer differs from the strictly-correct one in a way that could cost exam points, give the course's answer as the headline fact and the precision as a brief parenthetical — still with no reference to where either came from. Example: *"Allosteric enzymes do not have a Km (the half-saturation point is reported as K₀.₅ or S₀.₅, since the sigmoidal curve does not obey Michaelis-Menten)."*

**Report every correction you made to me in chat, not in the document.**

### Rule 4 — Each fact appears exactly ONCE. This is the strictest rule in the brief.

Not "once per section." Not "once in prose and once in a table." **Once in the entire main body.**

This is where the Lecture 01 v2 build still fell short, so be concrete about it. It contained a table row reading *"HMP shunt · NADPH + pentoses — no ATP"* and then, four lines below, a red MUST KNOW band reading *"The HMP shunt yields NADPH and pentoses, never ATP."* That is one fact stated twice. Changing the format does not make it a new statement. The same thing happened with the TCA cycle's role and with the long-term/short-term regulation split.

**The decision procedure.** For every fact, pick its single best home *first*, then write only there:

| If the fact is… | Its home is… |
|---|---|
| one item in a set that varies along shared dimensions | **a table row** — and nowhere else |
| a contrast between two confusable things | **a `.vs` box** — and nowhere else |
| a mechanism or a causal chain | **prose** — and nowhere else |
| a value, threshold or constant | wherever its subject already lives; never on its own |
| genuinely enumerable | **a labelled list** — and nowhere else |

Having chosen, the other formats must not mention it. If a table carries the three inhibition types, the prose above that table does **not** re-list them — it explains what the reader is about to see and why the dimensions were chosen, then stops. Prose that introduces a table should be readable as a *reason to look at the table*, never as a summary of it.

**The specific traps to check for:**
- A prose sentence and a table cell carrying the same fact
- A `.must` band restating a fact from the table, list or sentence next to it — see §4, this is now structurally prevented
- A figure caption restating what the surrounding prose said
- Two objectives that both touch a concept, each giving it a full treatment — pick one home and cross-reference in half a sentence
- The orientation map naming a fact that the body then states again

**Exemption, and only this one.** The **self-test** and the **rapid-review sheet** are retrieval instruments, not exposition. Re-encountering material there is their entire purpose, and they are exempt. Everything before them says each thing once.

### Rule 5 — Write concisely. This is a real source of the savings.

Length comes down through **four** levers, and I want all four used:

1. Cutting meta-commentary (Rule 1)
2. Cutting repetition (Rule 4)
3. Cutting the corrections/sources sections (Rule 3, §5)
4. **Writing the surviving prose more tightly** ← this one matters most

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

**Calibration example.** Real v1-era prose (88 words):

> A competitive inhibitor is a molecule that closely resembles the substrate in its structure, and because of this resemblance it is able to bind to the active site of the enzyme, which is the same site the substrate would otherwise occupy. Because the two are competing for the same site, the effect of the inhibitor can be overcome by simply raising the substrate concentration high enough, and this is why the Vmax of the reaction remains unchanged while the apparent Km is increased.

Target style (52 words, same facts, nothing lost):

> A competitive inhibitor resembles the substrate closely enough to bind the active site, so substrate and inhibitor compete for it. Raising [S] outcompetes the inhibitor, so **Vmax is unchanged**; more substrate is needed to reach half-maximal velocity, so **apparent Km rises**.

That is roughly a **40% reduction with zero information loss**. Apply that standard throughout.

**Where not to compress.** Do not go telegraphic. Explanations must still explain — a mechanism the reader has never seen needs a real sentence, not a fragment. Never sacrifice a causal "because" to save three words. If a passage genuinely needs five sentences to be understood, give it five. **Kinetics derivations in particular must stay legible**: if the reader can't follow why the Lineweaver-Burk intercepts are what they are, you cut too far.

### Rule 6 — Nothing may be lost.

Every fact, number, example, definition, list, exception and clinical link in the slide deck (including speaker notes) and the transcript must survive somewhere in the document. Concision is about wording, never about coverage. When in doubt between cutting a fact and cutting six words of prose around it, cut the words.

---

## 2. Source files

Working directory: `/Users/yoelplutchok/Desktop/Biochem_Fall`
The repo is organised one folder per lecture.

| What | Path |
|---|---|
| **Slide deck** (55 slides) | `02 - Enzymes and Enzyme Kinetics/Lecture 02_Bagh_Enzyme and enzyme kinetics.pptx` |
| **Lecture transcript** | `02 - Enzymes and Enzyme Kinetics/Lecture 2 biochem.md` |
| **Interactive-session deck** | `_Interactive Sessions/Pre discussion Week 1 Overview and enzyme PE IS F26 (1).pptx` — **use slides 13–23 only** (2–12 belong to Lecture 01) |
| **v1 guide — mine the last two sections, see §6** | `02 - Enzymes and Enzyme Kinetics/Lecture 02 - STUDY GUIDE (html source).html` |
| **CSS — start from the Lecture 01 v2 sheet, not the v1 sheet** | `01 - Overview of Metabolic Pathways/Lecture 01 - STUDY GUIDE v2 (html source).css` |
| **Reference implementation of the target style** | `01 - Overview of Metabolic Pathways/Lecture 01 - STUDY GUIDE v2 (html source).html` |
| **Required textbook** | `/Users/yoelplutchok/Desktop/Fall Courses/Medical Biochemistry and Genetics I/sga/general/textbooks/Lippincott Biochemistry - 6th Edition .pdf` — **Ch. 5, Enzymes** |
| **Backup textbook** | `.../sga/general/textbooks/BRS Biochemistry, Molecular Biology, and Genetics 6E (2013).pdf` |
| **Figures already extracted** | `02 - Enzymes and Enzyme Kinetics/Lecture_02_figures/` (8 images, descriptively named) |

**Note the deck extension.** A legacy binary `.ppt` sits alongside; ignore it. The `.pptx` is a LibreOffice conversion and opens fine with `python-pptx`. If anything looks garbled, cross-check against the rendered slide images.

Already looked up — don't re-derive: this is **Week 1, Session 1, Tue 8/4, 1–2 PM**, delivered in the same session as Lecture 01; required reading **Lippincott Ch. 5** (also **Panini 2nd ed. Ch. 5**; suggested Marks' 5th ed. Ch. 8); assessed on **Foundation Exam #1, Mon 8/17, 11 AM–1 PM**.

**The interactive-session deck matters — it is richer here than it was for Lecture 01.** Slides 13–23 contain **three exam-style questions explicitly tagged to numbered learning objectives** — the closest available proxy for real exam items:

| Slide | Question | Tagged objective | Note |
|---|---|---|---|
| 15 | Reaction-coordinate diagram: which arrow is ΔG for the catalyzed S→P? | Obj 1 | Answer is in the speaker notes |
| 20 | Methotrexate competitively inhibiting dihydrofolate reductase — which plot? | Obj 4 | Lineweaver-Burk pattern recognition |
| 22 | Effect of CTP on aspartate transcarbamoylase | Obj 5 | Negative allosteric effector |

Slides 16–19 and 21 are **content**, not questions, and carry material worth harvesting: the Lineweaver-Burk transformation and why it's used, the hexokinase/glucokinase comparison (**the speaker notes on slide 17 contain the Km values, 0.05 mM vs 10 mM, and the glucose-sensor role — do not skip them**), the three-way inhibition comparison, and the K-type/V-type modulator distinction. v1 missed all of this. Use it to calibrate what to mark as high-yield, and fold the three questions into the self-test (§6).

---

## 3. Length target

| Part | Target |
|---|---|
| Main body (everything before the self-test) | **10–13 pages** |
| Self-test | ~3 pages |
| Rapid-review sheet | 2 pages |
| **Total** | **15–18 pages, hard ceiling 20** |

Larger than Lecture 01's 15 because the deck is 55 slides against 41, there are five objectives against four, and enzyme kinetics genuinely needs its graphs. It is still a **~25–35% cut** from v1's 24.

---

## 4. The emphasis system — already built, reuse it

The Lecture 01 v2 CSS defines the whole system. Copy that file, rename it for Lecture 02, and extend only if you need something new.

**Tier 1 — MUST KNOW. Read this carefully, because it changes from the Lecture 01 build.**

MUST KNOW is a **marker applied to a fact where it already lives** — not a band that repeats it. In Lecture 01 v2 it was a standalone red band, and that band kept duplicating the table row above it. Per Rule 4, that is now forbidden. The mark goes on the fact's one home:

| The fact lives in… | Mark it by… |
|---|---|
| a table row | `<tr class="must">` — red-tinted row with a ★ in the first cell |
| a `.vs` box | `★` prefix in the `.vshead` bar, and the box tinted red instead of blue |
| a figure | `★` prefix on the `<figcaption>` lead-in |
| prose, and the sentence *is* the fact's only statement | the standalone `.must` band, exactly as in Lecture 01 v2 |

So the standalone band survives, but **only when that band is the fact's single appearance anywhere in the main body** — never as a restatement of something a neighbouring table or list already says. Extend the CSS with `tr.must`, `.vs.must`, and `figcaption .must-star`; keep `.must` itself unchanged for the prose case.

The result must still let me see importance instantly on a page scan — that requirement doesn't relax, it just gets satisfied by tinting the fact rather than echoing it.

**Cap at 14–16 marks for the whole document** (slightly more than Lecture 01's 14, because there is more hard-testable numeric content). Scarcity is what makes it work. Tier-1 candidates — **verify each against the sources before marking it**, and add any I've missed:

- Enzymes lower **activation energy** only; they do not change ΔG, ΔG°′, Keq, the equilibrium position, or the transition state
- Km = the substrate concentration at **½Vmax**
- Km is **inversely** related to affinity: low Km = high affinity
- Km is **independent** of enzyme concentration; Vmax is **directly proportional** to it
- Michaelis-Menten: v = Vmax[S] / (Km + [S]); **first-order** in [S] at low [S], **zero-order** at high [S]
- Lineweaver-Burk: y-intercept = **1/Vmax**, x-intercept = **−1/Km**, slope = **Km/Vmax**
- **Competitive** inhibition: Km ↑, Vmax **unchanged** — overcome by raising [S]
- **Noncompetitive** inhibition: Km **unchanged**, Vmax ↓ — cannot be overcome by raising [S]
- **Irreversible / suicide** inhibition: Km unchanged, Vmax ↓
- Hexokinase **low Km (≈0.05 mM), low Vmax**; glucokinase **high Km (≈10 mM), high Vmax**
- Glucokinase is the **glucose sensor** of pancreatic islet cells, setting the threshold for insulin secretion
- **Allosteric enzymes give sigmoidal curves and have no true Km**
- **K-type** modulators change substrate affinity; **V-type** modulators change catalytic activity
- Blood-glucose ≈5 mM sits **below** glucokinase's Km, which is what lets the liver release glucose rather than trap it

I've written those as sentences so you can check them, **not as a specification of how to present them.** Most belong in tables, and there they stay: the three inhibition types are three marked rows of the inhibition comparison table, not three red bands beneath it. Hexokinase vs. glucokinase is one marked `.vs` box, not two bands. The Lineweaver-Burk intercepts are one marked row or one marked figure caption. Expect roughly **four or five** of the sixteen to end up as standalone `.must` bands; the rest are marks on rows, boxes and captions.

**Tier 2 — inline bold.** Every term, number or name that could be a fill-in-the-blank answer. Generous but not blanket — if everything is bold, nothing is.

**Tier 3 — `.vs` (confusable pairs).** Two-column box, with `<u>` on the single discriminating word. For this lecture at minimum: competitive vs. noncompetitive inhibition; noncompetitive vs. irreversible/suicide; Km vs. Vmax; hexokinase vs. glucokinase; K-type vs. V-type modulator; apoenzyme vs. holoenzyme; cofactor vs. coenzyme; zero-order vs. first-order kinetics; allosteric vs. Michaelis-Menten kinetics. Where two pairs are short, put both in one box as I did for exergonic/endergonic + convergent/divergent.

Also available in the CSS: `.clin` (green) for clinical correlations, `.map` for ASCII/diagram blocks, `.legend`, `figure.side` (tall image beside its caption), `figure.tall`, `table.long` (lets a long table break across pages).

**Keep box count low.** Lecture 01 v2 used 11 boxes total across 15 pages. Target **~15 for this lecture**. The default presentation is: a tight prose paragraph carrying the *concept*, immediately followed by a table or compact list carrying the *specifics*. Boxes are for emphasis only, not for routine structure.

**Keep the concept/specifics distinction** — I process material that way — but make it lightweight: 2–4 sentences of "why," then the facts. The prose must never restate the list that follows it.

---

## 5. Structure of the main body

Organize by the five learning objectives, which are the natural spine and match how the material is tested:

1. Definitions, terms and classes of enzymes; clinical uses of enzymes
2. Michaelis-Menten kinetics; Km and Vmax
3. Factors affecting enzyme activity
4. Competitive, noncompetitive and suicide inhibition
5. Allosteric modulation of enzyme activity

Open with a **one-page orientation**: a compact `.map` diagram of the reaction-coordinate / energy landscape and how every later concept hangs off it — substrate binds → transition state → activation energy is what the enzyme lowers → rate → the things that perturb rate (substrate, temperature, pH, inhibitors, allosteric modulators) — plus one tight paragraph tying it together. This is the scaffold everything else hangs on.

**The map is an index, not a summary.** It *names* the pieces and shows how they connect; it does not state the facts about them. "Inhibitors → competitive · noncompetitive · suicide" belongs on the map. What each does to Km and Vmax does not — that is the inhibition table's, and only the inhibition table's. Write the map first, then treat every term on it as already-introduced: the body develops what the map named, and never re-announces it. The single paragraph under the map is the one place a bird's-eye restatement is allowed, and it gets one paragraph.

**Structural condensation, on top of the prose-level work in Rule 5:**
- Convert any comparative prose into a table. Tables are denser than sentences and easier to revise from. The competitive/noncompetitive/suicide comparison **must** be a table.
- One-line definitions, not paragraphs, for defined terms.
- Fold examples into the fact they illustrate rather than giving them their own block.
- Merge overlapping material scattered across the source into single treatments.
- Prefer a labelled list over a paragraph whenever the content is genuinely enumerable.

**Figures: keep 6–8 maximum** (one more than Lecture 01 — the kinetics plots earn their space; a described graph is not a graph). The eight already in `Lecture_02_figures/` are a strong starting set, but **reassess each**: drop any that a table covers, and check resolution. Several Lecture 01 figures turned out to be low-resolution or padded with whitespace, and re-cropping them from the rendered deck at 300 dpi was a clear win — do the same here where needed. **Rewrite every caption**: captions explain the biology only, in one or two sentences, with no reference to slide numbers or sources. A caption must teach something the reader cannot get from the surrounding prose — how to *read* the graph, which feature to look at, what the crossing point means. A caption that summarizes the paragraph above it is a Rule 4 violation; delete it and let the figure stand on its axis labels. Never include both a figure of a table and a typeset version of that table.

**Do not include** a corrections/reconciliation section, a "sources" section, or any "how this document was made" framing.

---

## 6. The last two sections — keep, and extend

**Self-test.** `ol.qlist`, each question one line with a one-line answer inline in green. **Keep this format exactly.** Target **32–38 questions so that every part of the material is covered** — audit your finished main body section by section and add questions wherever something testable isn't yet probed. Fold in the **three objective-tagged questions from the interactive-session deck** and every in-deck question, converted to the same recall format; where a question's distractors teach a real discrimination, put that discrimination in the answer line. Include the interactive deck's plot-reading questions **with their figures** — pattern recognition on a Lineweaver-Burk plot is a skill, not a fact, and it needs the image. No meta-framing.

Lecture 02 rewards numerical drill more than Lecture 01 did. Include questions that make me *compute or read off* a value: Km from an x-intercept, Vmax from a y-intercept, which curve shifted and in which direction.

**Rapid-review sheet.** Two-column `.two-col` keyword sheet. Keep its structure and density. Intro line: *"Bold = highest-yield. If you review one page, review this one."* — no reference to the instructor. It must include a compact **inhibition summary grid** (Km / Vmax / overcome by ↑[S] / Lineweaver-Burk signature, for each of the three inhibition types); that grid is the single highest-yield object in the lecture.

---

## 7. Tooling — commands verified on this machine

`python3` is at `/opt/miniconda3/bin/python3`. `pandoc` and `soffice` are installed. **There is no `pdflatex` or `wkhtmltopdf`** — do not build the PDF via LaTeX.

```bash
python3 -m pip install python-pptx pymupdf weasyprint beautifulsoup4 lxml
```

**Extract slide text + speaker notes.** Speaker notes carry content that is not on the slides and not spoken aloud — never skip them; on this deck's interactive companion they hold the hexokinase/glucokinase Km values and a question's answer key. Recurse into groups (`shape_type == 6`) and handle `sh.has_table`.

```python
from pptx import Presentation
prs = Presentation("02 - Enzymes and Enzyme Kinetics/Lecture 02_Bagh_Enzyme and enzyme kinetics.pptx")
for i, slide in enumerate(prs.slides, 1):
    # print shape text; recurse groups; read tables
    if slide.has_notes_slide:
        print(slide.notes_slide.notes_text_frame.text)
```

**Render slides to PNG and actually look at them** — well over half the teaching content in this lecture is in graphs that carry no extractable text.
```bash
soffice --headless --convert-to pdf --outdir . "02 - Enzymes and Enzyme Kinetics/Lecture 02_Bagh_Enzyme and enzyme kinetics.pptx"
```
```python
import fitz
d = fitz.open("Lecture 02_Bagh_Enzyme and enzyme kinetics.pdf")
for i, p in enumerate(d, 1): p.get_pixmap(dpi=110).save(f"pages/s{i:02d}.png")
```
`MuPDF error: format error: No common ancestor in structure tree` is harmless; the render succeeds.

**Extract or re-crop figures.** Some images sit in *placeholders*, not `Picture` shapes, so a `shape_type == 13` filter misses them — wrap `sh.image` in try/except across **all** shapes. For anything low-resolution or surrounded by dead space, crop it out of the rendered slide PDF instead, which also captures overlaid text boxes the embedded image lacks:

```python
p = d[24]; r = p.rect   # slide 25, 0-indexed
p.get_pixmap(dpi=300, clip=fitz.Rect(r.width*0.28, r.height*0.10,
                                     r.width*0.53, r.height*0.99)).save("fig.png")
```

**Build the PDF** with WeasyPrint: `HTML(filename="guide.html").write_pdf("out.pdf")`. Keep the HTML, CSS and figures folder in the same directory so relative paths resolve.

**Markdown version.** Use the converter already written for this house style — don't rebuild it:

```bash
cd "02 - Enzymes and Enzyme Kinetics"
python3 ../_Prompts/html_to_md.py "Lecture 02 - STUDY GUIDE v2 (html source).html" \
                                  "Lecture 02 - Enzymes and Enzyme Kinetics - STUDY GUIDE v2.md"
```

It handles `.map` → fenced code block, `.must`/`.vs`/`.clin`/`.legend` → labelled blockquotes, `<figure>` → image + italic caption, sup/sub → Unicode, table captions → bold paragraphs, and strips every class/style/span so pandoc emits clean pipe tables. If you add a new CSS class, extend the script to match. Verify with `grep -c "<span\|<div\|class=" <output>.md` — it must return 0.

**Verify your own output.** Render the finished PDF back to PNGs, build a PIL contact sheet, and *look at it* — that is how Lecture 01's orphaned table caption and two illegibly-shrunk figures were caught. Also measure per-page bottom whitespace numerically to find pages a `break-inside: avoid` block has half-emptied:

```python
a = np.array(img.convert("L"))[:730]          # exclude the running footer
last = np.where(a.min(axis=1) < 200)[0].max() # last row containing ink
```

Report the final page count.

**Duplicate-fact audit — do this before the PDF build, and do it properly.** It is the one check the Lecture 01 build skipped, and it is why that guide still repeats itself. Grepping cannot find these, because a duplicate is usually the *same fact in different words*. So read the main body once with no other goal: for every `.must` mark, every table row, and every figure caption, ask *"is this fact stated anywhere else in the main body?"* — checking prose above and below it, the orientation map, and any other table. Delete the weaker instance. Then extract the facts and check mechanically for near-duplicates:

```python
# rough but effective: pull every table cell, list item, band and caption,
# normalize, and flag pairs sharing a high proportion of content words
import re, itertools
from bs4 import BeautifulSoup
soup = BeautifulSoup(open("guide.html").read(), "lxml")
body = soup.find("h2")                       # main body only; stop at the self-test
units = [n.get_text(" ", strip=True) for n in soup.select("td, li, .must, figcaption, p")]
STOP = set("the a an of to in is are and or for by with that this it as be on".split())
key = lambda s: {w for w in re.findall(r"[a-z]+", s.lower()) if w not in STOP}
for a, b in itertools.combinations([u for u in units if len(u) > 25], 2):
    ka, kb = key(a), key(b)
    if ka and kb and len(ka & kb) / min(len(ka), len(kb)) > 0.6:
        print("POSSIBLE DUPLICATE\n  ", a[:110], "\n  ", b[:110], "\n")
```

Expect false positives; judge each one. **Report the count of duplicates you removed** when you report back.

**Self-edit pass before you build the PDF.** Reread your draft once with Rule 5 in hand and cut wordiness you missed on the first pass. Expect to remove 10–15% on this pass alone. Removing *words*, never facts. Then grep your own HTML for Rule 1 and Rule 5 violations before you ship — this catches real ones:

```bash
grep -o -i -E "she (said|stressed|emphasi[sz]ed)|dr\.? bagh|the slide|the deck|slide [0-9]+|speaker note|note that|in other words|essentially|basically|it is worth noting" guide.html | sort | uniq -c
```

---

## 8. Reading the sources

- The transcript is a rough auto-transcription with heavy phonetic garbling. **Normalize silently.** Expect at minimum: `kynise`/`kinise` → kinase, `exocinise`/`hexokinise` → hexokinase, `glucoinise`/`glucynise` → glucokinase, `alosic`/`alostric`/`elostosteric` → allosteric, `mikaelis`/`michalis` → Michaelis, `linweaver`/`line weaver` → Lineweaver, `burk`/`burke` → Burk, `coalent` → covalent, `zyosin` → zymogen, `apoenzyme`/`apo enzyme` → apoenzyme, `co factor` → cofactor, `substrait` → substrate, `troponin`/`troponine` → troponin, `mithotrexate` → methotrexate. Work out any others from context.
- **Repetition count in the transcript is the emphasis signal** — use it to assign Tier 1, then discard the observation. It never appears in the output.
- Phrases that flag high-yield material: "please know that," "kindly remember," "don't mess up there," "very very important," "always and always," "please don't pick."
- **Expect stale artifacts in the deck**: leftover title text boxes that contradict their slide, images cropped mid-content, and — this bit the Lecture 01 build — a bullet that misclassifies something it introduced correctly elsewhere. Work out the intended content and present it whole.
- **Verify every numeric claim** about Km, Vmax, and graph intercepts against Lippincott Ch. 5 before you state it. Transcribed numbers are the least reliable part of these sources and the most damaging to get wrong.
- Use Lippincott Ch. 5 to fill genuine gaps and supply mechanism — the induced-fit vs lock-and-key models, the enzyme classification system, the derivation behind the Michaelis-Menten assumptions, and the clinical-enzyme panel (troponin, CK-MB, ALT/AST, amylase/lipase, ALP) with their time courses. **Do not expand scope beyond what the lecture covers** — Lecture 01's regulation material belongs to Lecture 01, and enzyme *regulation* mechanisms are largely that lecture's territory; cross-reference rather than duplicate.

---

## 9. Deliverables

Write into `/Users/yoelplutchok/Desktop/Biochem_Fall/02 - Enzymes and Enzyme Kinetics/`:

1. `Lecture 02 - Enzymes and Enzyme Kinetics - STUDY GUIDE v2.pdf` ← **primary**
2. `Lecture 02 - Enzymes and Enzyme Kinetics - STUDY GUIDE v2.md`
3. `Lecture 02 - STUDY GUIDE v2 (html source).html` and `.css`
4. Reuse `Lecture_02_figures/` for images; add to it only if needed

**Do not overwrite or delete the v1 files** — I want to compare before retiring them.

Afterwards, update `README.md`: move Lecture 02 to v2 in the "Study guides built so far" table with its page count, and clear the Lecture 02 entry from "Known gaps."

At the end, report to me in chat (not in the document):
- Final page count, broken down by section
- **How many duplicate statements the Rule 4 audit caught, and which instance you kept in each case**
- Every error you silently corrected, and what you corrected it to
- Anything in the sources you judged ambiguous and how you resolved it
- Confirmation that nothing from the deck, speaker notes, or transcript was dropped — say how you checked

If anything about the brief is genuinely ambiguous, ask before building rather than guessing.

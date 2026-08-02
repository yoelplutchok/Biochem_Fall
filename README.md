# Medical Biochemistry & Genetics I — Fall 2026

One folder per lecture, each holding **the slide deck and its matching transcript together**. Folders are numbered in **course order**, which is *not* the same as the numbering in the original filenames.

## Week 1

| Folder | Delivered | Instructor | Original file no. | Transcript |
|---|---|---|---|---|
| `01 - Overview of Metabolic Pathways` | Tue 8/4, 1–2 PM | Bagh | Lecture 01 | ✅ |
| `02 - Enzymes and Enzyme Kinetics` | Tue 8/4, 1–2 PM | Bagh | Lecture 02 | ✅ |
| `03 - Electron Transport Chain` | Thu 8/6, 8:30–10 AM | Bagh | **Lecture 06** | ✅ |
| `04 - Signal Transduction` | Thu 8/6, 8:30–10 AM | Bagh | **Lecture 07** | ✅ |
| `05 - Carbohydrate Digestion` | Thu 8/6, 8:30–10 AM | Binstock | **Lecture 8** | ❌ **missing** |
| `Primer 1 - Thermodynamics` | Thu 8/6 (with ETC) | Kamath | **Primer 04** | ✅ |
| `Primer 2 - Carbohydrate Structure` | Thu 8/6 (with carb digestion) | Kamath | **Primer 05** | ✅ |

Course-order numbering is confirmed by the interactive-session deck, whose title slides read *"Lecture 03: Electron Transport Chain"* and *"Lecture 04: Signal transduction."*

**Foundation Exam #1 — Mon 8/17, 11 AM–1 PM** covers all seven items above.

## Shared folders

- **`_Interactive Sessions`** — the two "Pre discussion Week 1" decks. These contain **exam-style practice questions tagged to numbered learning objectives**, plus clinical vignettes. Highest-value exam proxy in the repo.
  - *Overview and enzyme PE IS* → **slides 2–12 cover lecture 01** (Questions 1–2); **slides 13–23 cover lecture 02** (Questions 3–5)
  - *ETC Signal Tr Carb Dig* (57 slides) → **2–16** Primer 1 + lecture 03 (Questions 1–3, all tagged to ETC objective 5); **17–36** lecture 04 (Questions 4–6); **37–57** Primer 2 + lecture 05 (Questions 7–9)
- **`_Course Documents`** — syllabus
- **`_Prompts`** — reusable prompts for generating the study guides, plus `html_to_md.py` (the HTML→markdown converter for v2-style guides). `PROMPT_FOR_LECTURE_03_WEB.md` and `PROMPT_FOR_LECTURE_04_WEB.md` are **web-only** briefs: one self-contained `index.html` per lecture served from GitHub Pages, with word-count budgets in place of page counts and no PDF or markdown pipeline.

## Study guides built so far

| Lecture | Version | Pages | Files |
|---|---|---|---|
| `01 - Overview of Metabolic Pathways` | **v2 — current** | 15 | PDF + MD + HTML/CSS source + figures |
| `01 - Overview of Metabolic Pathways` | v1 — superseded, kept for comparison | 22 | PDF + MD + HTML/CSS source |
| `02 - Enzymes and Enzyme Kinetics` | **v2 — current** | 18 | PDF + MD + HTML/CSS source + figures |
| `02 - Enzymes and Enzyme Kinetics` | v1 — superseded, kept for comparison | 24 | PDF + MD + HTML/CSS source |
| `02 - Enzymes and Enzyme Kinetics` | **web v2 — current** | — | `index.html` + `figures/` (GitHub Pages) |
| `03 - Electron Transport Chain` | **web v2 — current** | — | `index.html` + `figures/` (GitHub Pages) |
| `03 - Electron Transport Chain` | v1 — superseded print HTML | — | HTML/CSS + PDF + MD |

Each guide's `.html`, `.css` and `Lecture_NN_figures/` must stay in the same folder — the HTML references them with relative paths. The PDF is self-contained.

**Web editions.** Lectures 02 and 03 are published as responsive web pages on GitHub Pages — self-test answers hidden behind a per-question reveal, a contents rail that tracks your position and shows each objective's ★ count, and dark mode. They read properly on a phone. Each is one self-contained `index.html` plus a `figures/` folder of WebP images downscaled to 1200px.

Lecture 01 also has a web edition, still hosted as a Claude artifact rather than on Pages:
https://claude.ai/code/artifact/501dda1a-7e89-4d97-91ed-ec9203b83654

The Lecture 02 web edition is a **rewrite, not a port** of its print guide: the orientation section was rebuilt around why an enzyme can only lower activation energy and why that reduces the lecture to two numbers, and roughly a dozen passages gained the reasoning behind a fact that the print version only asserted. It is the reference for what a web edition should read like.

**v2 is the house style.** It reads as a self-contained textbook chapter rather than a report about a lecture: no meta-references to the slides, the deck or the instructor; each fact stated exactly once; source errors corrected silently; emphasis carried by a three-tier visual system instead of repetition. Its CSS (`Lecture 01 - STUDY GUIDE v2 (html source).css`) is the one to reuse and extend — it adds `.must` (★ MUST KNOW bands), `.vs` (confusable-pair boxes), `.legend`, `.map`, `figure.side`/`figure.tall`, and `table.long` to the v1 sheet. The Lecture 02 sheet extends it again with `tr.must`, `.vs.must` and `.ms`, so a MUST KNOW mark can sit on the fact's own home — a table row, a VS box or a figure caption — instead of being repeated in a band beneath it. `_Prompts/html_to_md.py` converts any guide built on that CSS to clean GitHub-flavoured markdown.

## File format notes

- Every deck is now available as **`.pptx`**. The two originally-legacy `.ppt` files (Enzymes, Signal Transduction) were converted with LibreOffice; **the original `.ppt` files were kept alongside** in case the conversion lost any formatting.
- Slide counts: Overview 41 · Enzymes 55 · ETC 49 · Signal Transduction 45 · Carb Digestion 53 · Thermodynamics 20 · Carb Structure 20 · Interactive (ETC/ST/Carb) 57 · Interactive (Overview/Enzyme) 23

## GitHub Pages

Site root is this folder. Front door: repo Pages URL → `index.html`. Lecture web guides:

`…/02%20-%20Enzymes%20and%20Enzyme%20Kinetics/`
`…/03%20-%20Electron%20Transport%20Chain/`

Slide decks (`.pptx`/`.ppt`), `_extract/`, and `pages/` are gitignored to keep the repo light; they remain on disk locally.

## Known gaps

1. **No transcript for Carbohydrate Digestion** (Binstock). All other six lectures have one. The `carbohydrate.md` file that was on the Desktop is the **Carbohydrate *Structure* primer** (Kamath), not digestion — it has been filed under `Primer 2`.
2. Lectures **02** and **03** have web guides on Pages. Lectures **04–05** and both **primers** have no guide yet. Lecture **01** still needs a Pages port of its Claude artifact web edition.

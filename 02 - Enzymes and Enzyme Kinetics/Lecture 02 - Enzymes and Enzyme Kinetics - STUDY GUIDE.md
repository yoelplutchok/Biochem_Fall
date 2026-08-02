# Enzymes and Enzyme Kinetics

*Medical Biochemistry & Genetics I · Lecture 02 — Dr. Shilpika Bagh, MBBS, MD · Week 1, Session 1 · Tue 8/4, 1–2 PM*

- **Required reading:** Lippincott Illustrated Reviews: Biochemistry Ch. 5 (Enzymes) · Panini, Medical Biochemistry: An Essential Textbook 2e, Ch. 5
- **Suggested:** Marks' Basic Medical Biochemistry 5e, Ch. 8
- **Assessed on:** Foundation Exam \#1 — Sun 8/17, 11 AM–1 PM (also covers: metabolic pathway overview, ETC/uncouplers/inhibitors/ROS, thermodynamics primer, signal transduction, carbohydrate digestion, carbohydrate structures)
- **Deck:** 55 slides · delivered in the same session as Lecture 1

**What this lecture actually is.** Almost everything here reduces to two numbers and what moves them. **V<sub>max</sub>** is the ceiling — how fast the reaction goes when every enzyme molecule is working flat out — and it is set by *how many enzyme molecules you have*. **K<sub>m</sub>** is the substrate concentration that gets you halfway to that ceiling, and it is set by *how tightly the enzyme holds its substrate*. Every inhibitor, activator, isoenzyme, and regulatory mechanism in this lecture is classified by which of those two it moves and which it leaves alone. Dr. Bagh's own instruction for graph questions is to stop panicking and read the axes first, then the shape of the curve, then ask what changed — that procedure answers most of the questions this material generates.

She stated her learning objectives up front and said *"pay close attention to your learning objectives because they are tied to your questions."* This guide is organized as her five objectives, in her order.

## Objective 1 · Terms, classes of enzymes, and clinical uses of enzymes

### 1.1 What an enzyme is

> **CONCEPT**
>
> An enzyme does not make a reaction happen that couldn't happen — it makes a reaction that *would* happen eventually happen *now*. Every reaction has an energy hill between reactants and products (the transition state). Only molecules that happen to carry enough energy get over it, and at body temperature that is very few of them. An enzyme provides an alternate route with a lower hill, so a far larger fraction of molecules clear it per second. It does this by binding the substrate and *stabilizing the transition state* — holding the substrate in the strained, half-broken geometry it has to pass through anyway. The enzyme is not consumed and comes out unchanged, which is why a small amount of it turns over an enormous amount of substrate.

> **MEMORIZE**
>
> - **Enzyme** — a biocatalyst; speeds the rate of a chemical reaction without itself undergoing change.
> - **Substrate** — the molecule being transformed. **Product** — the result of the transformation.
> - **Active site** — pocket or cleft formed by protein folding; contains the side chains that bind substrate and perform catalysis. Substrate binding causes a conformational change (**induced fit**).
> - **In nearly all cases enzymes are PROTEIN.** The exception: **ribozymes**, which are RNA molecules that catalyze reactions with other RNAs.
> - Enzymes provide three things: **speed, specificity, and regulatory control**.
> - Rate enhancement: 10<sup>3</sup>–10<sup>8</sup>× over the uncatalyzed reaction.

> **PRECISION**
>
> Dr. Bagh added a distinction the slide does not make: *"sometimes the active site is the substrate binding site, sometimes the active site may not be the substrate binding site."* The standard usage is that the active site contains both the substrate-binding residues and the catalytic residues; they are two functional roles within one pocket, not two separate places. The point she is protecting is that a **regulatory (allosteric) site is a different site entirely** — that distinction is the one the exam tests, and it arrives in Objective 5.

### 1.2 Holoenzyme, apoenzyme, cofactor, coenzyme

> **CONCEPT**
>
> The twenty amino acid side chains are chemically limited — they are good at acid–base chemistry and not much else. They cannot carry electrons, transfer one-carbon units, or hold a positive charge strong enough to polarize a carbonyl. So enzymes that need that chemistry rent it: they recruit a non-protein partner that supplies the chemistry the protein cannot. The protein contributes specificity and positioning; the partner contributes the reactive capability. Neither works alone, which is exactly why the naming has three terms — the protein alone (**apoenzyme**, inactive), the partner, and the working assembly (**holoenzyme**).

**Holoenzyme = Apoenzyme (protein) + non-protein part  ·  apoenzyme alone is inactive**

**The non-protein part**

| Type | Chemical nature | Behavior | Examples |
|----|----|----|----|
| **Cofactor** | **Inorganic** — a metal ion | Enzymes requiring one are called **metalloenzymes** | Fe<sup>2+</sup>, Mg<sup>2+</sup>, Zn<sup>2+</sup>, Cu<sup>2+</sup> · **Carbonic anhydrase** requires **Zn<sup>2+</sup>** · **Lysyl oxidase** requires **Cu<sup>2+</sup>** |
| **Coenzyme:** · co-substrate | **Organic** small molecule | **Transiently** associated; **dissociates in an altered state** (it is chemically changed and must be regenerated elsewhere) | **NAD<sup>+</sup>**, **Coenzyme A** |
| **Coenzyme:** · prosthetic group | **Organic** small molecule | **Permanently** associated; **returns to its original state** on the enzyme (regenerated in place, never leaves) | **FAD**, **Biotin** |

> **MEMORIZE — she called this "very very important"**
>
> **Coenzymes are derived from vitamins.** She named three and said the exam will later ask you to link vitamin → active form/coenzyme → enzyme → pathway:
>
> - **NAD<sup>+</sup>** ← vitamin **B3, niacin**
> - **FAD** ← vitamin **B2, riboflavin**
> - **Biotin** ← vitamin B7 (itself the vitamin)

> **TRAP**
>
> **Co-substrate vs. prosthetic group is decided by whether it leaves and whether it leaves *changed*.** NAD<sup>+</sup> picks up electrons, floats off as NADH, and is re-oxidized somewhere else — co-substrate. FAD picks up electrons, becomes FADH<sub>2</sub>, and is re-oxidized while still bolted to the same enzyme — prosthetic group. This is the whole distinction; "tightly bound" is a consequence, not the definition.

### 1.3 How enzymes accelerate a reaction — and what they leave untouched

![Free energy diagram showing activation energy of catalyzed and uncatalyzed reactions with unchanged ΔG](Lecture_02_figures/fig7_activation_energy.png)

*The one energy diagram to know. Blue = uncatalyzed, red = catalyzed. The enzyme lowers the peak (E a ) but both curves start and end at the same heights, so ΔG is identical. Slide 6 · Lippincott Fig. 5.4*

> **CONCEPT**
>
> Look at the diagram as a landscape with two fixed endpoints. The **height difference between start and finish** is ΔG — it is a property of the molecules themselves, and no catalyst can touch it. What the enzyme changes is the **height of the pass you must climb to get between them**. Dr. Bagh's phrasing: *"only this uphill is a problem; once the uphill is gone, the downhill is easy."*
>
> Because the enzyme lowers the barrier **from both directions equally**, it accelerates the forward and reverse reactions by the same factor. That is precisely why K<sub>eq</sub> cannot move: K<sub>eq</sub> is the *ratio* of forward to reverse rate, and multiplying both by the same number leaves the ratio alone. An enzyme changes **how fast equilibrium is reached, never where equilibrium sits.**

> **MEMORIZE**
>
> - **Free energy of activation (ΔG<sup>‡</sup>, E<sub>a</sub>)** = the energy difference between the reactants and the high-energy intermediate (**transition state, T\***) that occurs during product formation. A ↔ T\* → B
> - Enzymes **lower the free energy of activation** so substrate reaches the transition state more easily.
> - **Enzymes DO NOT alter: ΔG, ΔG°′ (standard free energy change), or the equilibrium constant K<sub>eq</sub>.**

> **TRAP — this is the classic distractor pair**
>
> "Lowers activation energy" and "makes the reaction more favorable" are **different claims**, and the exam writes distractors out of confusing them. An enzyme cannot make an endergonic reaction exergonic, cannot change ΔG or ΔG°′, cannot shift the equilibrium position, and cannot change the amount of product present at equilibrium. It changes **only the rate**. If an answer choice says an enzyme changes ΔG, K<sub>eq</sub>, or the direction of a reaction — it is wrong, every time.

### 1.4 The six classes of enzymes

> **CONCEPT**
>
> The classification asks one question: **what happened to the substrate?** Electrons moved → oxidoreductase. A group moved from one molecule to another → transferase. A bond was broken *using water* → hydrolase. A bond was broken *without* water and without oxidation → lyase. The atoms rearranged without anything entering or leaving → isomerase. Two molecules were joined *and it cost ATP* → ligase. Work through those five questions in order and every enzyme lands in exactly one bin.

**EC classes — she said "don't mess with the number," meaning know the order 1–6**

| EC | Class | Reaction catalyzed | Example from the slide |
|----|----|----|----|
| **1** | **Oxidoreductase** | Oxidation–reduction: one substrate oxidized, the other reduced | **Lactate dehydrogenase**: lactate + NAD<sup>+</sup> → pyruvate + NADH + H<sup>+</sup> |
| **2** | **Transferase** | Transfer of a C-, N-, or P-containing **group** | **Serine hydroxymethyltransferase**: serine + THF → glycine · **Hexokinase** (transfers phosphoryl from ATP) |
| **3** | **Hydrolase** | Cleavage of bonds **by addition of water** | **Urease**: urea + H<sub>2</sub>O → CO<sub>2</sub> + 2 NH<sub>3</sub> |
| **4** | **Lyase** | Cleavage of C–C, C–S, and certain C–N bonds **without water** | **Pyruvate decarboxylase**: pyruvate → acetaldehyde + CO<sub>2</sub> |
| **5** | **Isomerase** | Rearrangement of optical or geometric **isomers** | **Methylmalonyl-CoA mutase**: methylmalonyl-CoA → succinyl-CoA |
| **6** | **Ligase** | Formation of bonds between C and O, S, or N, **coupled to hydrolysis of a high-energy phosphate (ATP)** | **Pyruvate carboxylase**: pyruvate + CO<sub>2</sub> + ATP → oxaloacetate + ADP + P<sub>i</sub> |

> **TRAP — transferase vs. ligase**
>
> Both can involve ATP, and that is the whole trap. A **ligase** uses ATP hydrolysis as an *energy source* to join two separate molecules into one. A **kinase** (a transferase) takes the **phosphoryl group itself** off ATP and puts it on the substrate — ATP is the *donor*, not the fuel. So hexokinase is a **transferase**, not a ligase, even though ATP appears in the equation. Her rule: **"kinases always add phosphate."** Mnemonic for the order: *Over The Hill, Little Indian Lady* — Oxidoreductase, Transferase, Hydrolase, Lyase, Isomerase, Ligase.

> **In-class Question 1 (slide 15)**
>
> Hexokinase catalyzes Glucose + ATP → Glucose 6-phosphate + ADP. It may be classified as a(n):
>
> 1.  Oxidoreductase
> 2.  Transferase
> 3.  Hydrolase
> 4.  Lyase
> 5.  Isomerase
> 6.  Ligase
>
> **Answer: B — Transferase.** A phosphoryl *group* is transferred from ATP to glucose. **Why the others fail:** **A** — no atom changes oxidation state. **C** — water is neither consumed nor produced. **D** — nothing is cleaved without water; a bond is made, not broken. **E** — glucose and glucose-6-P are not isomers; a phosphate was added. **F** — the ATP tempts you, but a ligase joins two substrates together using ATP as fuel; here ATP *is* the group donor.

### 1.5 Clinical enzymology — why enzymes are measured in blood

> **CONCEPT**
>
> Enzymes are concentrated *inside* cells and have no job in plasma. The small amount normally present in serum is the steady-state leak from ordinary cell turnover — release balanced by clearance. When a tissue is injured by infection, toxin, poison, or ischemia, its membranes fail and its intracellular contents dump into the circulation, and the serum level jumps far above that steady state. So the measurement is not really an assay of enzyme function — it is an **assay of membrane integrity in a specific tissue**. That is also why specificity matters: an enzyme present in many tissues tells you damage happened but not where; an enzyme concentrated in one tissue tells you the address.

**Principal serum enzymes used in diagnosis (slide 10, Harper's Table 7–2) — the aminotransferase rows were boxed in red on the slide**

| Serum enzyme | Major diagnostic use |
|----|----|
| **Aspartate aminotransferase (AST, SGOT)** | Listed on the slide as **myocardial infarction** (see the precision note below) |
| **Alanine aminotransferase (ALT, SGPT)** | **Viral hepatitis** — highly concentrated in and highly specific for **liver** |
| Amylase | Acute pancreatitis |
| Lipase | Acute pancreatitis |
| Ceruloplasmin | Hepatolenticular degeneration (**Wilson disease**) |
| **Creatine kinase (CK)** | Muscle disorders and myocardial infarction |
| γ-Glutamyl transpeptidase (GGT) | Various liver diseases |
| **Lactate dehydrogenase (LDH), isozymes** | Myocardial infarction |
| Acid phosphatase | Metastatic carcinoma of the **prostate** |
| Alkaline phosphatase, isozymes | Various **bone** disorders, **obstructive liver** disease |

> **CLINICAL — the case she told**
>
> **Mushroom poisoning** (the slide's photograph; *Amanita*-type hepatotoxicity) causes hepatocellular damage. The slide's inset graph shows the time course after ingestion: **ALT rises first and steeply**, peaking around 36 hours at \>20× the upper normal value, while **bilirubin rises later and more slowly**. A rise in **both ALT and bilirubin** is the signature of **hepatocellular jaundice** — the cells are being destroyed (ALT leak) *and* losing their ability to conjugate and excrete bilirubin. Both ALT and AST rise in liver damage; **ALT is the more liver-specific of the two.**

> **PRECISION — the AST row is a legacy entry**
>
> This table is old. AST was used as a cardiac marker decades ago, but AST is present in heart, liver, skeletal muscle, kidney, and red cells, and it has been **completely replaced by troponin for myocardial infarction**. In current practice both AST and ALT are read as **liver** enzymes (the AST:ALT ratio is used to characterize the pattern of liver injury). Dr. Bagh taught them as the hepatic pair, which is correct; the slide table is the outdated part. **Answer the slide's version if the question is clearly drawn from it, but do not carry "AST = MI" into clinical reasoning.**

### 1.6 Isoenzymes — locating the damaged tissue

> **CONCEPT**
>
> Isoenzymes solve the specificity problem. They are different protein molecules that catalyze the **same reaction** but are built from different subunits encoded by different genes, so they differ in amino acid sequence — and therefore in **net charge**. Different charge means they **separate on electrophoresis**. Different tissues express characteristic proportions of them. So instead of "some tissue was damaged," a serum isoenzyme *pattern* tells you **which** tissue, because you are effectively reading the tissue's expression signature in the blood.
>
> Her electrophoresis reasoning, which she wanted you to reconstruct rather than memorize: these enzymes are **negatively charged**, so they migrate **toward the anode (+)**. The most negative species travels furthest toward the positive pole — that is CK-1 (BB) and LDH-1. Numbering runs in order of decreasing migration toward the anode.

> **MEMORIZE — Creatine kinase (CK): a dimer of B and M subunits, three isoenzymes**
>
> - **CK-1 = BB** — brain
> - **CK-2 = MB** — **predominant in cardiac muscle**; myocardium is the only tissue with \>5% of its CK as MB
> - **CK-3 = MM** — **predominant in skeletal muscle**
> - A rise of **CK-2 (MB) as a fraction of total CK** indicates cardiac damage — the ratio matters, not just the absolute value.

> **MEMORIZE — Lactate dehydrogenase (LDH): a tetramer of H and M subunits, five isoenzymes**
>
> - **LDH-1 = HHHH** — predominant in **heart**
> - **LDH-2 = HHHM** — **predominant in normal serum**
> - LDH-3 = HHMM  ·  LDH-4 = HMMM
> - **LDH-5 = MMMM** — predominant in **liver**

**Normal serum: LDH-2 \> LDH-1  ·  Myocardial infarction **flips** it: LDH-1 \> LDH-2  ·  Hepatic damage: **LDH-5** rises**

> **CLINICAL — markers of myocardial infarction, and why they changed**
>
> **Cardiac troponin T and troponin I have superseded both LDH and CK-MB** as the diagnostic markers of MI: they are more **sensitive and more specific**, and cardiac troponin I in particular is essentially cardiac-exclusive. The figure shows why the LDH flip is now a historical exam fact rather than a clinical tool.

![Plasma CK-MB and cardiac troponin over days after myocardial infarction](Lecture_02_figures/fig8_ckmb_troponin.png)

*CK-MB vs. cardiac troponin after MI. CK-MB peaks at ~24 h and is back below the reference limit by ~72 h; troponin rises to a much higher multiple and stays elevated for days, which is what makes it useful in a patient who presents late. Slide 13*

> **PRECISION — a specimen-handling detail from her speaker notes**
>
> **Hemolysis releases LDH from red blood cells** and will falsely elevate serum LDH, confounding the isoenzyme pattern. Blood samples for LDH must be handled with care. This is the kind of pre-analytical detail that appears as a "why is this lab result wrong?" question.

> **MEMORIZE — Review of Objective 1 (her slide 14, verbatim content)**
>
> - Define: enzyme, substrate, product, cofactor, coenzyme, holoenzyme, apoenzyme
> - Enzymes accelerate a chemical reaction by **lowering the activation energy**
> - Enzymes **DO NOT change either ΔG or the equilibrium constant**
> - There are **six classes** of enzymes based on the type of reaction they catalyze
> - **Tissue enzymes detected in blood serve as markers for tissue damage**

## Objective 2 · Michaelis-Menten enzyme kinetics; K<sub>m</sub> and V<sub>max</sub>

### 2.1 The model

> **CONCEPT**
>
> Michaelis and Menten's insight was that catalysis is not a collision, it is a **two-step process with an obligatory intermediate**. The enzyme must first *capture* the substrate (reversibly, forming ES), and only then can it *convert* it. Everything about enzyme kinetics falls out of that: velocity is set by how much ES exists at any moment, because only ES makes product. Add more substrate and you push more enzyme into the ES form — until every enzyme molecule is already in the ES form, at which point adding substrate does nothing, because there is no free enzyme left to capture it. That saturation point is V<sub>max</sub>, and the existence of saturation is the single feature that separates enzyme kinetics from ordinary chemical kinetics.

**E + S ⇄ k 2 k 1 ES → k 3 E + P v = k 3 \[ES\]**

> **MEMORIZE**
>
> - The model **ignores the reverse reaction** (E + P → ES). This is legitimate because we use **initial velocities**: at the start, essentially no product exists, so there is nothing to run backwards and **no product inhibition**.
> - Velocity of the forward reaction is **directly proportional to \[ES\]**: v = k<sub>3</sub>\[ES\].
> - **K<sub>m</sub> is the ratio of the rate constants for breakdown of ES over formation of ES** — the Michaelis constant.
>
> **K M = (k 2 + k 3) / (k 1) v o = (V max \[S\]) / (K m + \[S\])**
>
> - **v<sub>o</sub>** = initial reaction velocity  ·  **V<sub>max</sub>** = maximal velocity  ·  **K<sub>m</sub>** = Michaelis constant  ·  **\[S\]** = substrate concentration
> - She said explicitly: **you are not deriving this equation.** Know what each term means and how the equation behaves at the extremes.

> **CONCEPT — Why K m and affinity run in opposite directions — the one thing that makes the rest automatic**
>
> Read the formula literally. The numerator, **k<sub>2</sub> + k<sub>3</sub>**, is every way the ES complex *falls apart* — either backwards to E + S, or forwards to E + P. The denominator, **k<sub>1</sub>**, is the rate at which ES *forms*. So K<sub>m</sub> is a **ratio of losing the substrate to catching it**.
>
> A **large K<sub>m</sub>** means ES falls apart much faster than it forms — the enzyme keeps dropping its substrate. To keep half the enzyme population occupied despite that, you must flood it with substrate. Hence high K<sub>m</sub> = **low affinity** and a high half-saturating concentration. A **small K<sub>m</sub>** means the enzyme grabs and holds, so a trace of substrate is enough to keep half of it busy: low K<sub>m</sub> = **high affinity**. The inverse relationship is not a rule to memorize — it is what the formula says.

**Low K<sub>m</sub> → HIGH affinity   ·   High K<sub>m</sub> → LOW affinity   (she said "please memorize" this five separate times)**

### 2.2 The two graphs

![Michaelis-Menten hyperbola and Lineweaver-Burk double reciprocal plot with intercepts labeled](Lecture_02_figures/fig1_mm_lineweaver.png)

*The same data, two ways. A — v vs. \[S\] is a hyperbola ; the low-\[S\] arm is first order, the plateau is zero order. B — 1/v vs. 1/\[S\] is a straight line , so K m and V max can be read off the intercepts instead of estimated from a curve. Slide 19*

> **CONCEPT — Why the Lineweaver-Burk plot exists at all**
>
> The hyperbola never actually reaches V<sub>max</sub> — it creeps toward it asymptotically. So you cannot read V<sub>max</sub> off the curve by eye, and since K<sub>m</sub> is defined *relative* to V<sub>max</sub>, an error in V<sub>max</sub> propagates straight into K<sub>m</sub>. Taking reciprocals of both axes converts the hyperbola into a straight line, and a straight line can be extrapolated confidently to its intercepts. You get both constants from a ruler.
>
> The cost, which the slide flags: you are plotting **reciprocals**, so the points at low \[S\] — the least accurate measurements — become the largest 1/\[S\] values and dominate the fit. **A small experimental error produces a large error in the graphically determined K<sub>m</sub> and V<sub>max</sub>.**

> **MEMORIZE — Lineweaver-Burk (double-reciprocal) plot**
>
> **(1) / (v) = (K m) / (V max) · (1) / (\[S\]) + (1) / (V max)**
>
> - **x-intercept = −1 / K<sub>m</sub>**
> - **y-intercept = 1 / V<sub>max</sub>**
> - **slope = K<sub>m</sub> / V<sub>max</sub>**
> - Given an intercept value you can compute the constant — she asked "why not?" Take the reciprocal.

> **TRAP — Her graph procedure — she repeated it seven times, use it**
>
> **"Don't panic when it comes to a graph."** Every time: (1) read the **y-axis**, (2) read the **x-axis**, (3) read the **shape of the curve**. v vs. \[S\] and hyperbolic → a Michaelis-Menten enzyme. v vs. \[S\] and sigmoid → an allosteric enzyme. 1/v vs. 1/\[S\] and a straight line → a double-reciprocal plot. Only then ask what moved. She also said you **do not need to draw** these graphs — you need to **recognize** them.

### 2.3 K<sub>m</sub>, and the other kinetic parameters

> **MEMORIZE — Michaelis constant (K m )**
>
> - **Definition: the substrate concentration at which the initial reaction velocity equals ½ V<sub>max</sub>.** It is a **concentration**, with units of concentration — not a velocity, not a ratio, not a time.
> - Characteristic of a **particular enzyme with a particular substrate**; it is a **constant for that enzyme**.
> - A measure of the **affinity** of the enzyme for that substrate (inversely — see above).
> - **Reflects the natural substrate** of an enzyme: the physiologic substrate is generally the one with the lowest K<sub>m</sub>.
> - **K<sub>m</sub> does NOT vary with enzyme concentration.** Add or remove enzyme and K<sub>m</sub> is unchanged — affinity is a property of one molecule, not of how many you have.

> **MEMORIZE — V max , k cat , and activity units**
>
> - **V<sub>max</sub> depends on the amount of enzyme, \[E<sub>t</sub>\]** — and, unlike K<sub>m</sub>, on nothing about affinity.
> - **k<sub>cat</sub> = the turnover number** = moles of product formed **per second per mole of catalytic center**. Typically 10<sup>2</sup>–10<sup>4</sup> s<sup>−1</sup>.
> - **Unit of enzyme activity** — e.g., µmol (or mmol) of product per minute.
> - **Specific activity = units / mg protein.** Because it normalizes activity to total protein, it is a measure of the **purity** of an enzyme preparation — her phrasing: *"specific activity shows the purity of the enzyme, because enzymes are protein in nature."*

> **CONCEPT — The relationship that ties k cat and V max together**
>
> **V<sub>max</sub> = k<sub>cat</sub> × \[E<sub>t</sub>\].** At saturation every enzyme molecule is cycling as fast as it possibly can, which is k<sub>cat</sub>; total output is that rate times the number of workers. This single equation is the reason V<sub>max</sub> is the parameter that reports **enzyme quantity**: k<sub>cat</sub> is fixed by the protein's chemistry, so the only way to move V<sub>max</sub> is to change how many enzyme molecules are present. Keep that in hand — in Objective 4 it explains, in one step, why noncompetitive inhibition, suicide inhibition, and repression all lower V<sub>max</sub> and why induction raises it.

> **PRECISION — three refinements the lecture left loose**
>
> - **K<sub>m</sub> is not literally a dissociation constant.** K<sub>m</sub> = (k<sub>2</sub>+k<sub>3</sub>)/k<sub>1</sub>, whereas true binding affinity is K<sub>d</sub> = k<sub>2</sub>/k<sub>1</sub>. They coincide only when catalysis is slow relative to release (k<sub>3</sub> ≪ k<sub>2</sub>). "K<sub>m</sub> measures affinity" is the exam's answer and is directionally right; the caveat is why careful sources say K<sub>m</sub> *reflects* affinity.
> - **V<sub>max</sub> is approached, not reached.** The slide says "this increase in rate occurs until V<sub>max</sub> is reached." Mathematically v = V<sub>max</sub>\[S\]/(K<sub>m</sub>+\[S\]) equals V<sub>max</sub> only at infinite \[S\]. In practice at \[S\] = 100×K<sub>m</sub> you are at 99%, which is why "zero order" is a fair description.
> - **k<sub>cat</sub>/K<sub>m</sub> is catalytic efficiency** — not asked on these slides, but distinct from k<sub>cat</sub> alone (turnover number). If a question contrasts "turnover number" with "catalytic efficiency," they are not synonyms.

## Objective 3 · Factors that affect enzyme activity

**The five factors: substrate concentration · enzyme concentration · temperature · pH · activators/inhibitors**

### 3.1 Substrate concentration — first order, zero order, mixed order

> **CONCEPT — read the hyperbola as two different worlds joined by a bend**
>
> The shape of the curve is not decorative; it is two distinct kinetic regimes.
>
> **Far left (\[S\] ≪ K<sub>m</sub>):** substrate is scarce and most enzyme molecules are sitting empty. The limiting event is an enzyme *finding* a substrate molecule, so doubling \[S\] doubles how often that happens and doubles the velocity. Velocity is **proportional to \[S\]** — **first order**.
>
> **Far right (\[S\] ≫ K<sub>m</sub>):** every active site is already occupied; there is a queue. The limiting event is now the enzyme's own catalytic cycle, which has a fixed speed. Adding more substrate lengthens the queue but changes nothing about throughput. Velocity is **independent of \[S\]** — **zero order**, and it equals V<sub>max</sub>.
>
> **The bend in between** is the **mixed-order** region, and **K<sub>m</sub> sits inside it** — which is exactly why K<sub>m</sub> is the useful descriptor of an enzyme: it marks where the enzyme transitions from responsive to saturated.

> **MEMORIZE — the same idea in the equation (her alternate route to the same conclusion)**
>
> She deliberately gave both the graphical and the algebraic derivation, "so that you know what makes you learn best."
>
> - **When \[S\] ≫ K<sub>m</sub>:** K<sub>m</sub> becomes negligible in the denominator, so v<sub>o</sub> = V<sub>max</sub>\[S\]/\[S\] → **v<sub>o</sub> = V<sub>max</sub>**. Zero order.
> - **When \[S\] ≪ K<sub>m</sub>:** \[S\] becomes negligible in the denominator, so **v<sub>o</sub> = (V<sub>max</sub>/K<sub>m</sub>) · \[S\]** — velocity proportional to \[S\]. First order.

> **MEMORIZE — she paired these with the transporters and said "keep them together"**
>
> |  | \[S\] ≪ K<sub>m</sub> | \[S\] ≫ K<sub>m</sub> |
> |----|----|----|
> | **Velocity** | Proportional to \[S\] | Independent of \[S\]; v = V<sub>max</sub> |
> | **Order** | **First order** ("proportional") | **Zero order** ("constant") |
> | **Paired transporter** | **GLUT2** — liver and pancreas | **GLUT1 and GLUT3** — brain and RBC |

> **CONCEPT — Why that transporter pairing makes sense**
>
> **GLUT2** is a low-affinity, high-capacity transporter in liver and pancreas. Its job is to move glucose *in proportion to* how much is in the blood, so the liver stores when there is a surplus and the β-cell can *sense* the glucose level — a sensor must not be saturated at normal concentrations or it reports the same number at every glucose. Proportional response = first order.
>
> **GLUT1 and GLUT3** serve brain and RBC, tissues that cannot be without glucose for a moment. Their transporters are saturated at normal blood glucose, so uptake is **constant** and continues undiminished even when blood glucose falls. Constant supply = zero order. This is a design decision, not a coincidence, and the same logic returns in the next section with the enzymes behind those transporters.

### 3.2 Enzyme concentration, temperature, and pH

> **MEMORIZE — the three remaining factors and their curve shapes**
>
> - **Enzyme concentration — a straight line.** When substrate is unlimited, reaction velocity is **directly proportional to \[E\]**. Her speaker note gives the application: this is **why you can quantify an enzyme in plasma, serum, or tissue by measuring its activity** — activity is a valid proxy for amount only because the relationship is linear.
> - **Temperature — a bell curve.** Velocity rises with temperature to a peak, then falls with further increase (**denaturation**). **Optimum for most human enzymes: 35–40 °C.** Exception: **thermostable DNA polymerases** (e.g. *Taq*, used in PCR).
> - **pH — a bell curve.** pH changes the **ionic charge of amino acid side chains**, which alters catalytic function; extremes denature the enzyme. Most human enzymes are optimal near **physiologic pH ~7.4**.
>
> | Enzyme with a non-neutral pH optimum | Optimum pH |
> |--------------------------------------|------------|
> | **Pepsin** (stomach)                 | **1–2**    |
> | Acid phosphatase                     | 4–5        |
> | **Trypsin** (pancreatic)             | **5–7**    |
> | Alkaline phosphatase                 | **9–10**   |

> **CONCEPT — Why the temperature and pH curves are bells rather than plateaus**
>
> Two opposing effects overlap. Raising temperature increases the fraction of molecules with enough energy to clear the activation barrier, so velocity climbs. But the enzyme is a folded protein held together by weak non-covalent interactions, and the same thermal energy eventually shakes it apart. The peak is where the second effect overtakes the first. pH works the same way in charge terms: catalysis needs specific side chains in specific protonation states, so there is one pH where the maximum number of them are correct, and moving away in *either* direction removes some and eventually denatures the fold outright. **An optimum always implies two competing processes.**

> **PRECISION — the trypsin number is unusual**
>
> The slide lists trypsin's optimum as **5–7**. Most sources put trypsin's optimum at **pH 7.5–8.5**, matching the alkaline environment of the duodenum where bicarbonate neutralizes gastric acid — and Dr. Bagh herself described trypsin verbally as "a pancreatic enzyme which has an optimum alkaline pH," contradicting her own slide. The concept she is testing (acidic pepsin vs. alkaline trypsin) is the point. **Learn the contrast; if a question asks for a number, the slide's numbers are the exam's source.**

### 3.3 Hexokinase vs. glucokinase — the worked example she said "will come back again and again"

![Enzyme activity vs glucose concentration for hexokinase and glucokinase with fasting blood glucose band](Lecture_02_figures/fig5_hexokinase_glucokinase.png)

*Two enzymes, one reaction, opposite designs. The orange band is fasting blood glucose (~5 mM). Hexokinase is already saturated there; glucokinase is barely started, and its K m (~10 mM) sits above the fasting range. Slide 29 · Marks' Fig. 8.13*

> **CONCEPT — kinetics chosen to match the job**
>
> Both enzymes do the identical chemistry: glucose + ATP → glucose-6-phosphate + ADP, the first step of glucose utilization, and the step that traps glucose inside the cell (G6P is charged and cannot cross the membrane back out). They differ in *when* they do it, and that difference is entirely K<sub>m</sub> and V<sub>max</sub>.
>
> **Brain and RBC must never be without glucose.** Their enzyme, **hexokinase**, therefore has a **low K<sub>m</sub> = high affinity**: it is saturated at, and even well below, normal blood glucose, so uptake continues at full speed during fasting. Its **low V<sub>max</sub>** is a feature, not a limitation — these tissues should take what they need, not hoard. (Hexokinase is also inhibited by its own product, G6P, which enforces that.)
>
> **The liver is a buffer and the pancreas is a sensor** — neither should act at fasting glucose. Their enzyme, **glucokinase**, has a **high K<sub>m</sub> = low affinity**, sitting deliberately *above* the circulating concentration, so it is nearly idle between meals and switches on only when portal glucose is high after a meal. Its **high V<sub>max</sub>** then lets the liver clear a large load quickly. In the pancreatic β-cell the same property makes glucokinase the **"glucose sensor" that sets the threshold for insulin secretion** — a sensor is only useful if it is unsaturated across the physiologic range.

**Slide 29, with the speaker-note detail folded in**

|  | Hexokinase | Glucokinase |
|----|----|----|
| **K<sub>m</sub>** | **Low** (~0.05 mM) → **high affinity** | **High** (~10 mM) → **low affinity** |
| **V<sub>max</sub>** | **Low** | **High** |
| **Tissue** | Most tissues — **brain and RBC** | **Liver** & **islet cells of pancreas** |
| **Paired GLUT** | **GLUT1 and GLUT3** — zero order | **GLUT2** — first order |
| **Her label** | The enzyme of **high affinity** | The enzyme of **high efficiency** |
| **Purpose** | Guarantee glucose use even when blood glucose is low | Trap glucose after meals; set the insulin-secretion threshold |

> **TRAP — do not cross the pairs**
>
> She warned repeatedly: *"keep them together, don't mix and mess them up."* The two stacks are **Brain/RBC → GLUT1&3 → zero order → hexokinase → low K<sub>m</sub> → high affinity → low V<sub>max</sub>** and **Liver/pancreas → GLUT2 → first order → glucokinase → high K<sub>m</sub> → low affinity → high V<sub>max</sub>**. Note the deliberate cross-over that makes this confusing: the tissue with the *zero-order transporter* has the *low-K<sub>m</sub>* enzyme. Both facts say the same thing — **brain and RBC are built to take glucose unconditionally**.

> **In-class Question 2 (slide 32)**
>
> Hexokinase in human red blood cells has a K<sub>m</sub> of 0.1 mM for glucose. Normal plasma glucose is 5 mM. At this glucose concentration, which statement about hexokinase is correct?
>
> 1.  It is operating at 50% of V<sub>max</sub>
> 2.  It is 50% saturated with glucose
> 3.  Raising plasma glucose to 10 mM will double the enzyme velocity
> 4.  It is operating at 100% of V<sub>max</sub>
> 5.  Lowering plasma glucose to 3 mM will lower the enzyme velocity
>
> **Answer: D.** Her point was that **no calculation is required**: K<sub>m</sub> = 0.1, \[S\] = 5, so **\[S\] ≫ K<sub>m</sub>** → zero order → the enzyme is at V<sub>max</sub>. **Why the others fail:** **A** and **B** both describe \[S\] = K<sub>m</sub> = 0.1 mM, fifty-fold below the actual concentration (and note A and B are restatements of each other, so neither can be the single answer). **C** — in the zero-order region, raising \[S\] changes nothing. **E** — 3 mM is still thirty-fold above K<sub>m</sub>, still saturating.

> **PRECISION**
>
> Strictly, v = 5/(0.1+5) = **98%** of V<sub>max</sub>, not 100%. "Operating at 100% of V<sub>max</sub>" is the intended answer and the only defensible choice offered, but if a question ever asks for the exact fraction, use the equation rather than the approximation.

## Objective 4 · Competitive, noncompetitive, and suicide inhibition

> **CONCEPT — The organizing idea — read this before the details and the table becomes unnecessary**
>
> There are only **two ways to slow an enzyme**, and each moves exactly one parameter.
>
> **(1) Block the door.** Put a molecule that looks like the substrate into the active site. It is a fair fight decided by numbers, so at any given \[S\] a fraction of the enzyme is tied up and you need *more* substrate to reach half-maximal velocity: **K<sub>m</sub> rises**. But it is a fight you can win by flooding the field — pour on enough substrate and the inhibitor is displaced entirely, so the ceiling is untouched: **V<sub>max</sub> unchanged**. This is **competitive**.
>
> **(2) Remove workers from the payroll.** Bind somewhere else and disable the enzyme whether or not substrate is present. Extra substrate is irrelevant — a disabled enzyme is disabled. Functionally you now have **fewer enzyme molecules**, and since V<sub>max</sub> = k<sub>cat</sub>\[E<sub>t</sub>\], the ceiling drops: **V<sub>max</sub> falls**. But the enzyme molecules that remain are perfectly normal and bind substrate exactly as well as before: **K<sub>m</sub> unchanged**. This is **noncompetitive** — and it is also, for the identical reason, what **suicide (irreversible) inhibition** and **repression** look like.
>
> So the real question on any inhibition item is not "which of four rows do I recall" but **"can the substrate fight back?"** Yes → competitive, K<sub>m</sub>↑. No → the enzyme pool shrank, V<sub>max</sub>↓.

> **MEMORIZE — the reversible / irreversible split is defined by bond type**
>
> - **Reversible inhibition — NON-covalent** attachment of the inhibitor, either at the active site or elsewhere. Dilution dissociates it and activity recovers. Two types taught: **competitive** and **noncompetitive**.
> - **Irreversible ("suicide") inhibition — COVALENT** attachment of the inhibitor at the active site.
> - An inhibitor is defined as a compound that **decreases the velocity of the catalyzed reaction by binding to the ENZYME** — not to the substrate and not to the product.

> **TRAP — she called this "very very important" and got it backwards once herself**
>
> **Irreversible = covalent. Reversible = non-covalent.** In the transcript she says at one point *"if there is a reversible binding the binding has to be covalent"* — a slip of the tongue; she states the correct version four other times in the same passage. Covalent bonds are strong and permanent, which is exactly why that binding is irreversible. If a stem tells you an inhibitor binds covalently, you already know: **irreversible → V<sub>max</sub> down, K<sub>m</sub> unchanged.**

### 4.1 Competitive inhibition

![Competitive inhibition: Michaelis-Menten and Lineweaver-Burk plots](Lecture_02_figures/fig3_competitive_kinetics.png)

*Competitive inhibition. A — the hyperbola shifts right (apparent K m increased) but climbs to the same V max . B — the double-reciprocal lines meet on the y-axis at 1/V max . Slide 37 · Lippincott Fig. 5.12*

> **MEMORIZE**
>
> - **Structural similarity between substrate and inhibitor** — the inhibitor is a **structural analog** of the substrate. This is the defining feature.
> - Inhibitor binds the **same site as the substrate — the active site**; the two **compete** for it.
> - **K<sub>m</sub> increases** — affinity of the enzyme for substrate decreases in the presence of inhibitor; inhibition **can be overcome by increasing \[S\]**.
> - **V<sub>max</sub> unchanged** — the number of enzyme molecules available to bind substrate is unchanged.
> - Possible complexes: **E–S** and **E–I**. **There is no ESI complex in competitive inhibition** — the two cannot occupy the site at once.
> - On the double-reciprocal plot: **shared y-intercept**; as \[I\] rises the line **rotates upward and its x-intercept moves right** toward zero. **The inhibitor line is always above the control line.**

> **CLINICAL — competitive inhibitors as drugs**
>
> - **Statins** (lovastatin, simvastatin, atorvastatin, pravastatin) are structural analogs of HMG-CoA and competitively inhibit **HMG-CoA reductase**, the **rate-limiting enzyme of cholesterol biosynthesis**. Inhibiting hepatic cholesterol synthesis lowers plasma cholesterol. She used this as the cleanest illustration of "structural similarity is the basis of competitive inhibition."
> - **Methotrexate (MTX)** is a folate analog and a competitive inhibitor of **dihydrofolate reductase (DHFR)**, the enzyme that produces **tetrahydrofolate (THF)**. THF is required for thymidylate and purine synthesis, hence for **cell division** — so MTX is an **anticancer (chemotherapy)** drug and a **disease-modifying drug in rheumatoid arthritis**.

### 4.2 Noncompetitive inhibition

![Noncompetitive inhibition: Michaelis-Menten and Lineweaver-Burk plots](Lecture_02_figures/fig4_noncompetitive_kinetics.png)

*Noncompetitive inhibition. A — the hyperbola flattens to a lower V max while K m stays where it was. B — the double-reciprocal lines meet on the x-axis at −1/K m . Slide 41 · Lippincott Fig. 5.14*

> **MEMORIZE**
>
> - **No structural analogy** between substrate and inhibitor.
> - Inhibitor binds at a site **other than the substrate binding site** and prevents catalytic activity.
> - It can bind **either the free enzyme (E) or the enzyme–substrate complex (ES)** — this is why substrate is no defense.
> - **The ESI complex forms but cannot produce product.** The presence of an ESI complex is the structural giveaway that distinguishes this from competitive inhibition.
> - **V<sub>max</sub> decreases** — the number of enzyme molecules available to bind substrate decreases.
> - **K<sub>m</sub> unchanged** — inhibition **cannot be overcome by increasing \[S\]**.
> - On the double-reciprocal plot: **shared x-intercept**; the line **moves up** (y-intercept 1/V<sub>max</sub> gets larger), and again **the inhibitor line is above the control line**.

> **TRAP — Her fastest discriminator — she gave it three times, and it is genuinely the quickest route**
>
> **On the hyperbolic curve, look for what CHANGED. On the Lineweaver-Burk plot, look for what is UNCHANGED** — i.e., which intercept the two lines share.
>
> - Lines share the **y-intercept** → V<sub>max</sub> is unchanged → **competitive**.
> - Lines share the **x-intercept** → K<sub>m</sub> is unchanged → **noncompetitive** (or irreversible).
>
> And in both cases the inhibited line sits **above** the control line, because inhibition lowers v and 1/v is therefore larger. A "below the control line" answer choice is describing an *activator*.

> **CLINICAL**
>
> **Physostigmine** is given on the slide as a **noncompetitive inhibitor of acetylcholinesterase**, the enzyme that terminates cholinergic neurotransmission by hydrolyzing acetylcholine. She flagged acetylcholinesterase as an enzyme you will meet again in pharmacology. *(See the reconciliation table — the real pharmacology of physostigmine is not noncompetitive.)*

### 4.3 Irreversible / suicide inhibition

> **MEMORIZE**
>
> - Inhibitor binds the enzyme **covalently at the active site** and **decreases the concentration of active enzyme \[E<sub>t</sub>\]**.
> - **Lowers V<sub>max</sub> · No change in K<sub>m</sub> · Kinetics identical to noncompetitive inhibition.**
> - Increasing \[S\] will **not** allow substrate to outcompete the inhibitor.

> **CLINICAL — irreversible inhibitors**
>
> - **Aspirin** — analgesic and anti-inflammatory. **Covalently** acetylates **cyclooxygenase (COX-1 and COX-2)**, inhibiting **prostaglandin synthesis**.
> - **Disulfiram (Antabuse)** — irreversibly binds **acetaldehyde dehydrogenase (AcDH)**. Ethanol → (alcohol dehydrogenase) → **acetaldehyde** → (AcDH) → acetate; block the second step and **acetaldehyde accumulates**, producing the flushing, nausea and sick feeling that conditions patients with chronic alcohol use to avoid alcohol.
> - **Poisons:** **cyanide** (deferred — returns with the electron transport chain), **nerve gas**, **organophosphates**.

> **PRECISION — "irreversible" and "suicide" are not exactly synonyms**
>
> The slide uses them interchangeably and the exam will follow the slide. Strictly, a **suicide (mechanism-based) inhibitor** is a narrower category: an unreactive compound that the enzyme's own catalytic machinery **converts into a reactive species**, which then covalently kills the enzyme that made it — the enzyme commits suicide by doing its job. All suicide inhibitors are irreversible; not all irreversible inhibitors are suicide inhibitors (lead binding cysteine thiols, for instance, is simply covalent chemistry).

### 4.4 The comparison, and the master diagram

**Slide 43 — the comparison she wants you to be able to reproduce cold**

| Parameter | Competitive | Noncompetitive | Irreversible / suicide |
|----|----|----|----|
| **Binding at** | **Active site** | **Other site** | Active site |
| **Bond** | Non-covalent | Non-covalent | **Covalent** |
| **Structural analog of substrate?** | **Yes** | **No** | — |
| **V<sub>max</sub>** | **Unchanged** | **Decreased** | **Decreased** |
| **K<sub>m</sub>** | **Increased** | **Unchanged** | **Unchanged** |
| **Can excess substrate overcome it?** | **Yes** | **No** | **No** |
| **ESI complex?** | No | Yes | No (enzyme is dead) |
| **Shared Lineweaver-Burk intercept** | **y** (1/V<sub>max</sub>) | **x** (−1/K<sub>m</sub>) | **x** (−1/K<sub>m</sub>) |
| **Examples** | Statins, methotrexate | Physostigmine | Aspirin, disulfiram, cyanide, organophosphates |

![Michaelis-Menten curve with arrows labeling induction, repression/noncompetitive inhibition, competitive inhibition, and activation](Lecture_02_figures/fig2_curve_shift_map.png)

*Every process in this lecture, as a direction of movement. Up = induction · down = repression or noncompetitive inhibition · right = competitive inhibition · left = activation. Slide 44*

> **CONCEPT — How to use that diagram — it collapses two objectives into one picture**
>
> Vertical movement is a **V<sub>max</sub>** change, so it is always a change in the **number of working enzyme molecules**. **Up = induction** (more enzyme synthesized). **Down = repression** (less enzyme synthesized) **or noncompetitive/irreversible inhibition** (existing enzyme disabled) — she pointed out explicitly that **repression and noncompetitive inhibition are kinetically indistinguishable** on this axis, and that is a legitimate exam trap.
>
> Horizontal movement is a **K<sub>m</sub>** change, so it is always a change in **affinity**. **Right = K<sub>m</sub> increased = lower affinity = competitive inhibition.** **Left = K<sub>m</sub> decreased = higher affinity = activation.** Her one-line version: *"if the curve moves right, K<sub>m</sub> increases, low affinity, that's inhibition; if the curve moves left, K<sub>m</sub> decreases, high affinity, that's activation."*

> **In-class Question 3 (slide 48)**
>
> A noncompetitive inhibitor of an enzyme:
>
> 1.  Increases K<sub>m</sub> with no change in V<sub>max</sub>
> 2.  Decreases K<sub>m</sub> and decreases V<sub>max</sub>
> 3.  Decreases V<sub>max</sub>
> 4.  Increases V<sub>max</sub>
> 5.  Increases K<sub>m</sub> and increases V<sub>max</sub>
>
> **Answer: C — Decreases V max** (with K<sub>m</sub> unchanged). **Why the others fail:** **A** is the definition of **competitive** inhibition — the single most common wrong answer, because it is a true statement about the wrong thing. **B** describes **uncompetitive** inhibition, which was not taught in this lecture but is a real category (see below). **D** and **E** are impossible: **no inhibitor raises V<sub>max</sub>**, since inhibition means less product per unit time.

> **PRECISION — uncompetitive inhibition was not taught, but you should recognize the name**
>
> Slide 34 lists only competitive and noncompetitive under "reversible." A third reversible type exists: **uncompetitive** inhibition, in which the inhibitor binds **only the ES complex** (never free enzyme). Because it drags ES out of the equilibrium, it **decreases both V<sub>max</sub> and K<sub>m</sub>** — leaving V<sub>max</sub>/K<sub>m</sub> constant, so its Lineweaver-Burk lines are **parallel** to the control. That is the origin of distractor B above. **You are not responsible for it in this lecture**, but "decreases both" and "parallel lines" are the fingerprints if it ever appears.

> **MEMORIZE — Review of Objective 4 (her slide 47, verbatim content)**
>
> - Inhibitors of Michaelis-Menten enzymes are classified into **reversible (competitive, noncompetitive)** and **irreversible (suicide)** types
> - **Competitive inhibitors increase K<sub>m</sub> without affecting V<sub>max</sub>**
> - **Noncompetitive inhibitors lower V<sub>max</sub> without affecting K<sub>m</sub>**
> - **The kinetics of suicide (irreversible) inhibitors resemble those of noncompetitive inhibitors**

## Objective 5 · Allosteric modulation of enzyme activity

### 5.1 Where allosteric regulation sits among the regulatory mechanisms

> **CONCEPT**
>
> A cell can control an enzyme's output on two very different timescales, and the mechanisms sort cleanly by which one they use. **Changing how many enzyme molecules exist** requires transcription, translation, or proteolysis — that takes **hours to days**, so it is the long-term lever. **Changing how well the existing molecules work** requires only a small molecule to bind or a phosphate to be added — that takes **seconds to minutes**, so it is the short-term lever. Allosteric regulation is the fastest of the fast: no covalent chemistry at all, just a molecule binding and letting go.

**Slide 50 — enzyme regulation, both timescales**

| Long-term (hours–days): changes \[E\] | Short-term (seconds–minutes): changes activity per enzyme |
|----|----|
| **Induction** — \[E\] ↑ · **Repression** — \[E\] ↓ · **Degradation** by the **ubiquitin/proteasome** pathway and the **lysosomal** pathway | Effect of **substrate concentration** · **Product inhibition** · **Activation of pre-existing pools of inactive pro-enzymes** (zymogens) to produce active enzymes · **Reversible covalent modification** (e.g. phosphorylation/dephosphorylation) · **Allosteric regulation** · **Compartmentalization** |

### 5.2 Allosteric enzymes

> **CONCEPT — why the curve is sigmoid, and why that means "no K m "**
>
> An allosteric enzyme has **several subunits**, each with an active site, and the subunits are physically coupled: a conformational change in one is transmitted through the protein to the others. That coupling is **cooperativity**, and it is what bends the curve into an S.
>
> At low \[S\] the whole oligomer sits in a low-affinity conformation and responds sluggishly — the shallow foot of the S. Once a few sites fill, the conformational change propagates and flips the remaining subunits into a high-affinity state, so the next substrate molecules bind far more readily and velocity climbs steeply — the middle of the S. Then saturation flattens it. The functional payoff is that an allosteric enzyme behaves like a **switch** rather than a dial: a small change in substrate or effector concentration across the steep region produces a large change in flux, which is exactly the behavior you want at a control point.
>
> This also explains the claim that allosteric enzymes "do not have a K<sub>m</sub>." K<sub>m</sub> is defined inside the Michaelis-Menten framework, which assumes **independent, non-interacting active sites**. Cooperative sites violate that assumption, so the derivation does not apply and the constant it produces does not exist. The *concentration* giving half-maximal velocity obviously still exists — it is just called **K<sub>0.5</sub>** (or S<sub>0.5</sub>) instead, and you can see it labeled on the figure below.

> **MEMORIZE — features of allosteric enzymes**
>
> - **Multimeric** — made of several subunits (usually; almost always in practice).
> - **Frequently catalyze the committed step**, early in a pathway. In lecture she described this as the **branch point**, and the slide diagram shows an allosteric enzyme placed at exactly such a branch.
> - **Do NOT follow Michaelis-Menten kinetics.**
> - **Do NOT have a K<sub>m</sub>.**
> - Plot of v vs. \[S\] is **SIGMOID** — contrast with the **hyperbolic** curve of a Michaelis-Menten (non-allosteric) enzyme.
> - Deferred by her to a later lecture: **hemoglobin** as the model allosteric *protein* showing the same cooperativity.

> **CONCEPT — Why the committed step is the right place to regulate**
>
> The committed step is the **first irreversible step unique to a pathway** — the last point at which a metabolite can still be diverted somewhere useful. Regulating after it means the cell has already paid for intermediates it cannot repurpose. Regulating before it means throttling a shared precursor and starving other pathways. So the committed step is the only place where the control is both effective and free of collateral damage. At a genuine branch point the same argument holds: control the entry to each branch and you allocate flux without waste.

### 5.3 Allosteric effectors

> **MEMORIZE**
>
> - Allosteric enzymes bind **small, physiologically important molecules** called **allosteric effectors (modulators)**.
> - Effectors bind **non-covalently**, at a site **different from the catalytic site**.
> - Binding causes **conformational changes transmitted through the bulk of the protein** to the catalytically active site(s).
> - Effectors may be **inhibitors (negative)** or **activators (positive)**.
> - Modulators alter, up or down, either:
>   - the **catalytic activity** — **V-type** (V<sub>max</sub> changes, K<sub>0.5</sub> constant), or
>   - the **affinity for substrate** — **K-type** (K<sub>0.5</sub> changes, V<sub>max</sub> constant).

![Allosteric modulation: panel A V-type effectors change Vmax, panel B K-type effectors change K0.5](Lecture_02_figures/fig6_allosteric_v_and_k_type.png)

*Two ways to modulate an allosteric enzyme. A — V-type: the curves reach different V max values but share one K 0.5 . B — K-type: same V max , three different K 0.5 values. Note the axis label: K 0.5 , not K m . Slide 53 · Lippincott Fig. 5.16*

> **TRAP — allosteric effector vs. noncompetitive inhibitor**
>
> Both bind away from the active site and both are non-covalent, so stems can be written to look alike. The separations: an **allosteric enzyme** is **multimeric**, gives a **sigmoid** curve, and has **no K<sub>m</sub>**; a negative allosteric effector can lower V<sub>max</sub> *or* raise K<sub>0.5</sub> *or* both, and there are **positive** effectors that **increase** activity. A **noncompetitive inhibitor** acts on a **Michaelis-Menten** enzyme with a **hyperbolic** curve, lowers V<sub>max</sub> only, and has **no positive counterpart**. If the curve in the stem is sigmoid, you are in Objective 5, not Objective 4.

> **CLINICAL — Clinical / integrative — glycogen metabolism (slide 54), reasoned rather than memorized**
>
> Her method here was to ask **what the pathway is for** and let the effectors follow. Deferred to the glycogen lecture, but the logic is the exam-relevant part.
>
> - **Glycogen phosphorylase** (glycogen breakdown) — **negative:** ATP, glucose, glucose-6-P. **Positive:** Ca<sup>2+</sup> and AMP.
> - **Glycogen synthase** (glycogen synthesis) — **positive:** glucose-6-P.
>
> **Why:** the purpose of glycogen degradation **in muscle** is to make ATP. High **AMP** is the signal that ATP is being consumed, so AMP activates breakdown; **ATP** itself and **glucose-6-P** signal that supply is adequate, so they shut it off. **Ca<sup>2+</sup>** is the contraction signal — muscle that is contracting needs fuel now. For synthesis, **glucose-6-P is the starting material**, so abundant starting material is a positive signal to build. Notice the same molecule, glucose-6-P, is **negative for breakdown and positive for synthesis** — one signal, two opposite and mutually consistent effects.

> **PRECISION — the slide's effector list mixes two tissues**
>
> The slide's figure has two panels, **A = liver** and **B = muscle**, but the bullet list beside it merges them. In the figure, **Ca<sup>2+</sup> and AMP activate phosphorylase in the MUSCLE panel**, not the liver panel; the liver panel shows **glucose** as a negative effector, which is a hepatic-specific control tied to the liver's job of exporting glucose rather than burning it. Dr. Bagh's spoken version consistently placed AMP-driven glycogen breakdown **in muscle**, which matches the figure.

> **MEMORIZE — Review of Objective 5 (her slide 55, verbatim content)**
>
> Allosteric enzymes: usually **multisubunit**; catalyze **committed steps** in metabolic pathways; **do not follow Michaelis-Menten kinetics**; **do not have K<sub>m</sub>**. Allosteric modulators **non-covalently** bind to a site **other than the active site** and affect the **conformation** of the enzyme.

## Where the lecture was imprecise — reconciled

Slides are usually the source of truth for how a question is *written*; the transcript is usually the more careful biochemistry. Where they diverge, both versions are given here.

| What was said / shown | What is precisely true | Does it matter for the exam? |
|----|----|----|
| **"K<sub>m</sub> is a measure of the affinity of the enzyme for that substrate"** (slide 20) | K<sub>m</sub> = (k<sub>2</sub>+k<sub>3</sub>)/k<sub>1</sub>; true binding affinity is K<sub>d</sub> = k<sub>2</sub>/k<sub>1</sub>. They are equal only when k<sub>3</sub> ≪ k<sub>2</sub>. K<sub>m</sub> also varies **inversely** with affinity, which the slide bullet does not state on the same line as the definition. | **Yes, for the inverse direction.** "Low K<sub>m</sub> = high affinity" is heavily tested. The K<sub>d</sub> caveat is not. |
| **"This increase in rate occurs until V<sub>max</sub> is reached"** (slide 25) | V<sub>max</sub> is approached **asymptotically** and reached only at infinite \[S\]. The hyperbola never touches the plateau. | Minor. "Zero order" is still the correct description of the plateau region. |
| **"Allosteric enzymes do not have K<sub>m</sub>"** (slides 51, 55) | Correct as stated — K<sub>m</sub> is a Michaelis-Menten quantity and the derivation does not apply to cooperative sites. But a half-saturating concentration still exists and is called **K<sub>0.5</sub> / S<sub>0.5</sub>** — it is printed on her own slide 53. | **Yes.** Answer "no K<sub>m</sub>" if asked directly; recognize K<sub>0.5</sub> if it appears on a graph. |
| **Transcript: "if there is a reversible binding the binding has to be covalent"** | Reversed. **Irreversible = covalent; reversible = non-covalent.** She states it correctly four other times in the same passage — a verbal slip, not a belief. | **Yes — high yield.** She called covalent-binding-equals-irreversible "very very important." |
| **Transcript: "hexokinase, enzyme of high efficiency, is required in brain and RBC"** | Slip. **Hexokinase is the enzyme of high AFFINITY** (low K<sub>m</sub>, low V<sub>max</sub>). Glucokinase is the enzyme of high efficiency (high V<sub>max</sub>). She says the correct pairing several times immediately before and after. | **Yes.** This pair is a standing exam favorite. |
| **Transcript, on competitive inhibition: "when you increase substrate concentration, which parameter increases? K<sub>m</sub>"** | Garbled compression. K<sub>m</sub> increases **because the inhibitor is competing for the active site**, not because you added substrate. Adding substrate is how you *overcome* the inhibition. Two separate facts got fused into one sentence. | Conceptually yes; the endpoint she wants (competitive → K<sub>m</sub>↑, reversible by excess substrate) is correct. |
| **Physostigmine as a "noncompetitive inhibitor" of acetylcholinesterase** (slide 42) | Pharmacologically incorrect. Physostigmine is a **carbamate** that binds the **active site** and carbamylates the catalytic serine — it is an active-site-directed, **pseudo-irreversible** inhibitor, not a noncompetitive one. Lippincott's own noncompetitive example is **oxypurinol on xanthine oxidase**. | **Answer the slide** if physostigmine is named. Do not carry the classification into pharmacology. |
| **Slide 10 table: AST → "myocardial infarction"** | Legacy entry. AST is non-specific (heart, liver, muscle, kidney, RBC) and has been entirely replaced by **troponin** for MI. Today AST and ALT are read as the **hepatic** pair, as Dr. Bagh taught them verbally. | **Answer the slide** only if the question is clearly built from that table; otherwise troponin is the MI answer. |
| **Trypsin optimum pH "5–7"** (slide 31) | Most sources give **7.5–8.5**, consistent with the alkaline duodenum — and with her own spoken description of trypsin as having "an optimum alkaline pH." | The **contrast** (acidic pepsin vs. alkaline trypsin) is what is tested. Use the slide's number only if a numeric answer is demanded. |
| **Transcript: allosteric enzymes "catalyze the branch point"** vs. **slide: "committed step"** | Both describe real regulatory positions; **committed step** is the standard term and the one on the slide and in Lippincott. Her slide diagram happens to show an allosteric enzyme at a branch, so the two are consistent there. | Use **"committed step"** as the answer. |
| **Question 2's answer, "operating at 100% of V<sub>max</sub>"** (slide 32) | At \[S\] = 5 mM with K<sub>m</sub> = 0.1 mM, v = 98% of V<sub>max</sub>. "100%" is the intended and only defensible option offered. | No — pick D. Use the equation only if a stem asks for the numeric fraction. |
| **Slide 34 lists only competitive and noncompetitive as reversible types** | Incomplete. **Uncompetitive** (binds ES only; ↓V<sub>max</sub> and ↓K<sub>m</sub>; parallel Lineweaver-Burk lines) and **mixed** inhibition also exist. | Not taught, so not required — but "decreases both" appeared as a distractor in her own Question 3. |
| **Slide 17: "the Michaelis-Menten model ignores the reverse reaction"** | More precisely, it ignores **E + P → ES**. This is justified by measuring **initial** velocities, when \[P\] ≈ 0. The E + S ⇄ ES step is explicitly reversible in the model. | Low. Know *why* initial velocity is used: no product yet, so no product inhibition. |

## Rapid review — two-column recall sheet

Keyword-level recall only; the explanations live in the body above. **Bold** = always/never rule or high-yield discrimination point.

### Definitions

- Enzyme = biocatalyst, unchanged by reaction
- Enzymes are **protein** — except **ribozymes (RNA)**
- Holoenzyme = apoenzyme + non-protein part; **apoenzyme alone is inactive**
- Cofactor = inorganic (metal) → metalloenzyme
- Coenzyme = organic; co-substrate (**leaves altered**: NAD<sup>+</sup>, CoA) vs prosthetic group (**stays, returns to original state**: FAD, biotin)
- NAD<sup>+</sup> ← B3 niacin · FAD ← B2 riboflavin
- Carbonic anhydrase — Zn<sup>2+</sup> · Lysyl oxidase — Cu<sup>2+</sup>
- Induced fit; active site = binding + catalytic residues

### Energetics

- Enzymes **lower E<sub>a</sub>** (free energy of activation) by stabilizing the transition state T\*
- **Enzymes NEVER change ΔG, ΔG°′, or K<sub>eq</sub>**
- They change **rate to equilibrium, never position of equilibrium**; forward and reverse accelerated equally

### Six classes (know the order 1–6)

- 1 Oxidoreductase — redox (LDH)
- 2 Transferase — group transfer (**all kinases**; hexokinase)
- 3 Hydrolase — cleavage **using water** (urease)
- 4 Lyase — cleavage **without water** (pyruvate decarboxylase)
- 5 Isomerase — rearrangement (methylmalonyl-CoA mutase)
- 6 Ligase — **joins two molecules, costs ATP** (pyruvate carboxylase)
- **ATP present ≠ ligase**: kinase transfers the phosphoryl group itself → transferase

### Clinical enzymology

- Serum enzymes come from **normal cell turnover**; a rise = tissue damage
- ALT — **most liver-specific**; ALT + bilirubin ↑ = hepatocellular jaundice (mushroom poisoning)
- Amylase, lipase — pancreatitis · Ceruloplasmin — Wilson
- Acid phosphatase — prostate · Alk phos — bone, obstructive liver
- Isoenzymes: same reaction, different sequence → **separable by electrophoresis**; negatively charged → migrate to **anode (+)**
- CK: **CK-1 BB brain · CK-2 MB heart · CK-3 MM skeletal**
- LDH: **LDH-1 HHHH heart · LDH-2 HHHM normal · LDH-5 MMMM liver**
- **Normal LDH-2 \> LDH-1; MI flips to LDH-1 \> LDH-2**
- **Troponin T/I have superseded CK-MB and LDH for MI** — more sensitive and specific
- Hemolysis falsely raises LDH

### Michaelis-Menten

- E + S ⇄ ES → E + P; **v = k<sub>3</sub>\[ES\]**
- v<sub>o</sub> = V<sub>max</sub>\[S\] / (K<sub>m</sub> + \[S\])
- **K<sub>m</sub> = (k<sub>2</sub> + k<sub>3</sub>) / k<sub>1</sub>**
- **K<sub>m</sub> = \[S\] at ½ V<sub>max</sub>** — a concentration
- **LOW K<sub>m</sub> = HIGH affinity · HIGH K<sub>m</sub> = LOW affinity**
- **K<sub>m</sub> NEVER varies with \[E\]**; V<sub>max</sub> always does
- **V<sub>max</sub> = k<sub>cat</sub> × \[E<sub>t</sub>\]** — depends only on enzyme amount
- k<sub>cat</sub> = turnover number = mol product/s per mol catalytic centre
- Specific activity = units/mg protein = **purity**
- Initial velocity used → **no product inhibition**

### Lineweaver-Burk

- 1/v = (K<sub>m</sub>/V<sub>max</sub>)(1/\[S\]) + 1/V<sub>max</sub>
- **x-int = −1/K<sub>m</sub> · y-int = 1/V<sub>max</sub> · slope = K<sub>m</sub>/V<sub>max</sub>**
- Straight line; but reciprocals **magnify experimental error**
- **Inhibitor line is ALWAYS above the control line**

### Order of reaction

- **\[S\] ≪ K<sub>m</sub> → first order**, v ∝ \[S\] → **GLUT2, liver + pancreas**
- **\[S\] ≫ K<sub>m</sub> → zero order**, v = V<sub>max</sub> → **GLUT1 & 3, brain + RBC**
- Region around K<sub>m</sub> = mixed order

### Other factors

- \[E\]: **straight line**, v ∝ \[E\] — basis of measuring enzymes in serum
- Temperature: **bell curve**; optimum **35–40 °C**; exception **thermostable DNA polymerase**
- pH: **bell curve**; alters **charge on side chains**; most optimal ~7.4
- Pepsin 1–2 · acid phosphatase 4–5 · trypsin 5–7 (slide) · alk phos 9–10

### Hexokinase vs glucokinase

- **HK: low K<sub>m</sub>, low V<sub>max</sub>** — brain, RBC, most tissues; GLUT1/3; "high affinity"
- **GK: high K<sub>m</sub> (~10 mM), high V<sub>max</sub>** — liver + pancreatic islets; GLUT2; "high efficiency"
- GK is the β-cell **glucose sensor** setting the insulin threshold
- Both: glucose + ATP → G6P (traps glucose in the cell)

### Inhibition — the two questions

- **Can excess substrate overcome it? Yes → competitive. No → V<sub>max</sub> falls.**
- **Reversible = non-covalent · Irreversible = COVALENT**
- Inhibitor binds the **enzyme**, never substrate or product

### Competitive

- **Structural analog** of substrate; binds the **active site**
- **K<sub>m</sub> ↑ · V<sub>max</sub> unchanged**
- **NO ESI complex**
- L-B: **shared y-intercept**; curve shifts **right**
- **Statins** → HMG-CoA reductase (rate-limiting, cholesterol synthesis)
- **Methotrexate** → DHFR → ↓THF; chemo + rheumatoid arthritis

### Noncompetitive

- **No structural analogy**; binds a site **other than** the active site
- Binds **free E and ES**; **ESI complex forms but makes no product**
- **V<sub>max</sub> ↓ · K<sub>m</sub> unchanged**
- L-B: **shared x-intercept**; curve shifts **down**
- Physostigmine → acetylcholinesterase *(per slide)*

### Irreversible / suicide

- **Covalent**, at the active site; ↓ \[E<sub>t</sub>\]
- **Kinetics identical to noncompetitive: V<sub>max</sub> ↓, K<sub>m</sub> unchanged**
- **Aspirin** → COX-1/COX-2 → ↓ prostaglandins
- **Disulfiram** → acetaldehyde dehydrogenase → acetaldehyde accumulates
- Poisons: cyanide, nerve gas, organophosphates

### Reading the curves

- **Hyperbola → look for what CHANGED. Lineweaver-Burk → look for what is UNCHANGED.**
- **Up = induction · Down = repression OR noncompetitive/irreversible**
- **Right = competitive inhibition (K<sub>m</sub>↑) · Left = activation (K<sub>m</sub>↓)**
- **Repression and noncompetitive inhibition look identical kinetically**
- Procedure: y-axis → x-axis → shape → what moved

### Allosteric enzymes

- **Multimeric · committed step · SIGMOID curve · NO K<sub>m</sub>** (use **K<sub>0.5</sub>**)
- Sigmoid because of **cooperativity** between subunits
- Hyperbolic = M-M/non-allosteric; sigmoid = allosteric
- Effectors: **non-covalent**, bind a site **≠ catalytic site**, cause **conformational change**; may be **+ or −**
- **V-type** alters V<sub>max</sub> · **K-type** alters affinity (K<sub>0.5</sub>)
- Hemoglobin = allosteric protein, same cooperativity (later lecture)

### Enzyme regulation

- **Long term (hours–days, changes \[E\]):** induction, repression, degradation via **ubiquitin/proteasome** and **lysosomal** pathways
- **Short term (seconds–minutes):** \[S\], product inhibition, zymogen activation, reversible covalent modification, allosteric regulation, compartmentalization
- Glycogen phosphorylase: **− ATP, glucose, G6P; + Ca<sup>2+</sup>, AMP** (muscle)
- Glycogen synthase: **+ G6P**

## Self-test — 15 questions

1.  An enzyme lowers the activation energy of a reaction. What happens to K<sub>eq</sub>?
    **Answer: Nothing — enzymes accelerate forward and reverse equally and never change ΔG, ΔG°′, or K eq .**
2.  NAD<sup>+</sup> vs. FAD: which is a co-substrate and which a prosthetic group, and what is the criterion?
    **Answer: NAD + = co-substrate (dissociates in an altered state); FAD = prosthetic group (permanently bound, returns to its original state on the enzyme).**
3.  Write K<sub>m</sub> in terms of rate constants, and use it to explain why high K<sub>m</sub> means low affinity.
    **Answer: K m = (k 2 +k 3 )/k 1 — ES breakdown over ES formation. A high ratio means the enzyme loses substrate faster than it captures it, so more substrate is needed to half-saturate it.**
4.  Hexokinase catalyzes glucose + ATP → G6P + ADP. Which EC class, and why is it not a ligase?
    **Answer: Transferase (class 2). A ligase joins two molecules using ATP as an energy source; a kinase transfers the phosphoryl group of ATP itself.**
5.  Which two parameters does an inhibitor never change simultaneously in the direction "K<sub>m</sub> up, V<sub>max</sub> up"?
    **Answer: That combination is impossible — no inhibitor raises V max . It is a throwaway distractor.**
6.  Two Lineweaver-Burk lines intersect on the y-axis. What kind of inhibition, and which parameter changed?
    **Answer: Competitive — shared y-intercept means V max is unchanged; K m increased.**
7.  Two Lineweaver-Burk lines intersect on the x-axis. What kind of inhibition?
    **Answer: Noncompetitive (or irreversible/suicide) — shared x-intercept means K m is unchanged; V max decreased.**
8.  Why is suicide inhibition kinetically identical to noncompetitive inhibition?
    **Answer: Both remove enzyme molecules from the working pool. Since V max = k cat \[E t \], V max falls; the surviving enzyme is normal, so K m is unchanged.**
9.  A patient's serum shows LDH-1 \> LDH-2. What does this indicate, and what marker would actually be ordered today?
    **Answer: Myocardial infarction (the normal pattern is LDH-2 \> LDH-1). Today: cardiac troponin T or I.**
10. Blood glucose is 5 mM. Hexokinase K<sub>m</sub> = 0.1 mM; glucokinase K<sub>m</sub> ≈ 10 mM. Which enzyme is saturated, and what does that accomplish?
    **Answer: Hexokinase — \[S\] ≫ K m , zero order. It guarantees brain and RBC take up glucose at full rate even when blood glucose falls. Glucokinase is largely idle until glucose rises after a meal.**
11. Name the transporter pairing for first-order and zero-order kinetics.
    **Answer: First order (\[S\] ≪ K m ): GLUT2, liver and pancreas. Zero order (\[S\] ≫ K m ): GLUT1 and GLUT3, brain and RBC.**
12. An enzyme's v vs. \[S\] curve is sigmoid. What can you immediately say about it?
    **Answer: It is allosteric: multimeric, cooperative, does not follow Michaelis-Menten kinetics, has no K m (use K 0.5 ), and probably catalyzes a committed step.**
13. Distinguish a V-type from a K-type allosteric modulator.
    **Answer: V-type changes V max (catalytic activity) at constant K 0.5 ; K-type changes K 0.5 (substrate affinity) at constant V max .**
14. Two processes shift the hyperbola downward. Name both and explain why they cannot be told apart from the curve alone.
    **Answer: Repression (less enzyme synthesized) and noncompetitive/irreversible inhibition (existing enzyme disabled). Both reduce the number of functioning enzyme molecules, so both lower V max with K m unchanged.**
15. Which is more liver-specific, ALT or AST — and what does a simultaneous rise in bilirubin add?
    **Answer: ALT. A rise in both ALT and bilirubin indicates hepatocellular jaundice — the cells are being destroyed and are also failing to handle bilirubin.**

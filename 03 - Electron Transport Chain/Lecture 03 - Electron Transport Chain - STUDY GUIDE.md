# The Electron Transport Chain

*Medical Biochemistry & Genetics I · Lecture 03 — Dr. Shilpika Bagh, MBBS, MD · Oxidative phosphorylation, uncouplers, inhibitors, and ROS*

- **Assessed on:** Foundation Exam \#1 — Sun 8/17, 11 AM–1 PM (with metabolic pathway overview, thermodynamics primer, enzymes/kinetics, signal transduction, carbohydrate digestion and structures)
- **Deck:** 49 slides, titled "Lecture 06" in the source file · 5 stated learning objectives
- **Note:** This guide is built from the lecture transcript as the primary source, with the slide deck used to supply exact figures, names, numbers, and the content that existed only as diagrams. It contains no images by design — every diagram has been re-typeset as text.

**What this lecture actually is.** You have spent the previous lectures breaking food down. That process does not directly make ATP — it makes **reduced coenzymes**, NADH and FADH<sub>2</sub>, which are batteries holding electrons at high energy. This lecture is about how the cell cashes those batteries in. The electrons are walked down a staircase of carriers in the inner mitochondrial membrane, each with a greater appetite for electrons than the last, and the energy released at three of those steps is used to pump protons out of the matrix. The protons then fall back in through one specific channel, and that fall is what makes ATP. Everything else in the lecture — the poisons, the uncouplers, the fever, the cherry-red skin — is a consequence of interfering with either the staircase or the proton circuit.

Dr. Bagh opened with her standard instruction: *"the learning objectives are tied to your concepts, they are your guide."* This guide follows her five objectives in order. Her other recurring instruction — *"first know normal, then only you can know abnormal"* — is why the inhibitors come last, after each complex's normal job is fixed in place.

## Objective 1 · Reducing equivalents, redox potential (E<sub>0</sub>′), ΔE<sub>0</sub>′, and its relationship to ΔG<sub>0</sub>′

### 1.1 Biological oxidation is loss of reducing equivalents

> **CONCEPT**
>
> The general chemistry definition of oxidation is **gain of oxygen or loss of hydrogen**. In the body, the version that matters is the second one — and Dr. Bagh's point is that when a metabolite loses hydrogen, it is really losing **two protons and two electrons**, and it is the *electrons* that carry the energy. Bundle them together and call them **reducing equivalents**; now "oxidation" and "handing off reducing equivalents" are the same sentence.
>
> This reframing is what makes the rest of the lecture possible. Nothing is ever oxidized in isolation — if one molecule loses reducing equivalents, something else must gain them. So every biological oxidation is really a **pair** of half-reactions, and the whole chain that follows is just a queue of such pairs.

> **MEMORIZE**
>
> - **Oxidation** = gain of O<sub>2</sub> *or* loss of H<sub>2</sub>. **Biological oxidation** = loss of H<sub>2</sub> = loss of **2H<sup>+</sup> + 2e<sup>−</sup>** = **loss of reducing equivalents**.
> - **Reducing equivalent = (proton + electron).**
> - Biological oxidation is **exergonic**; the energy released is Gibbs free energy, and it is trapped **stepwise** as ATP.
> - The enzymes that run these reactions are **oxidoreductases**, subclass **dehydrogenases** — one substrate oxidized, one reduced.
> - What gets oxidized: the **macronutrients** (carbohydrate, lipid, protein). What gets reduced: the **coenzymes** (NAD<sup>+</sup>, FAD), supplied by **micronutrients** — i.e. vitamins.
> - **NAD<sup>+</sup> ← vitamin B3 (niacin)**  ·  **FAD ← vitamin B2 (riboflavin)**. Carried over from the enzymes lecture.
> - **NADH is an indirect reflection of ATP status.** NADPH is *not* — NADPH is for anabolism (carried over from Lecture 1: "NADPH is never a source of ATP").

    THE WHOLE LECTURE IN ONE LINE

      macronutrients ──oxidised──> reduced coenzymes ──> ETC ──> O2 ──> H2O
       (carb/lipid/protein)         (NADH+H+, FADH2)      │
                                                             └──> ATP
                                            and NAD+/FAD are regenerated for reuse

***Two products, not one.** The chain makes ATP *and* it hands back oxidised NAD<sup>+</sup>/FAD. Dr. Bagh stressed the second one: without regeneration, oxidation upstream stops for want of an acceptor.*

### 1.2 Redox potential (E<sub>0</sub>′) — the single organizing quantity

> **CONCEPT — this is the concept everything else hangs on**
>
> **E<sub>0</sub>′ is a measure of how badly a redox pair wants electrons**, measured under standard conditions (1 M each of oxidant and reductant, pH 7). Low E<sub>0</sub>′ = weak appetite for electrons; high E<sub>0</sub>′ = strong appetite. That is the entire definition, and it behaves exactly like intuition says it should: **electrons move from a carrier that wants them less to a carrier that wants them more.**
>
> Her repeated formulation: **the redox potential of the acceptor is always higher than that of the donor** — *"then only the electrons will move forward and the reaction will take place."* Because of that, ΔE<sub>0</sub>′ is defined **acceptor minus donor**, and a spontaneous transfer always gives a positive ΔE<sub>0</sub>′.
>
> Now extend it: if you can chain *one* transfer this way, you can chain many. Line up carriers **in order of increasing redox potential** and electrons will run the whole length of the line on their own, releasing energy at every step. That is literally what the electron transport chain is, and it is why oxygen — with the highest redox potential of anything in the series — sits at the end.

> **MEMORIZE**
>
> - **E<sub>0</sub>′** = standard redox potential of a compound; measured at **1 M oxidant and reductant, pH 7**.
> - **Low E<sub>0</sub>′ → low affinity for electrons. High E<sub>0</sub>′ → high affinity for electrons.**
> - **ΔE<sub>0</sub>′ = E<sub>0</sub>′(acceptor) − E<sub>0</sub>′(donor)**
> - Electrons flow toward the **more positive** standard reduction potential.
> - ETC components are arranged **in order of increasing redox potential**, spanning about **1.1 volts** from negative to more positive.
> - **Oxygen is the best electron acceptor — the highest reduction potential in the series (+0.82 V).**

**The redox ladder (slide 29) — read it top to bottom as the direction electrons travel**

| Redox pair | E<sub>0</sub>′ (volts) | Where it sits |
|----|----|----|
| NAD<sup>+</sup> / NADH | **− 0.32** | entry, Complex I |
| FMN / FMNH<sub>2</sub> | − 0.30 | inside Complex I |
| FAD / FADH<sub>2</sub> | **− 0.22** | entry, Complex II |
| Cytochrome b (Fe<sup>3+</sup>/Fe<sup>2+</sup>) | \+ 0.07 | Complex III |
| Coenzyme Q | \+ 0.10 | mobile carrier |
| Cytochrome c<sub>1</sub> | \+ 0.23 | Complex III |
| Cytochrome c | \+ 0.25 | mobile carrier |
| Cytochrome a | \+ 0.29 | Complex IV |
| ½ O<sub>2</sub> / H<sub>2</sub>O | **+ 0.82** | **terminal acceptor** |

> **TRAP — note where FAD enters**
>
> FAD/FADH<sub>2</sub> sits at **−0.22 V**, a full 0.10 V *above* NAD<sup>+</sup>/NADH at −0.32 V. FADH<sub>2</sub> therefore starts its descent from a lower rung of the staircase, and the drop it can pay for is correspondingly smaller. Hold onto this — it is the reason, three objectives from now, that FADH<sub>2</sub> yields **2 ATP** and NADH yields **3**. The number is not arbitrary; it is written into this table.

### 1.3 Converting a voltage into an energy: ΔG<sub>0</sub>′ = −nFΔE<sub>0</sub>′

> **MEMORIZE — the equation and every term in it**
>
> **ΔG 0 ′ = − n F ΔE 0 ′**
>
> - **ΔG<sub>0</sub>′** = standard free energy change
> - **n** = number of **electrons** transferred in the reaction
> - **F** = Faraday constant = **23.06 kcal/V** (per mole of electrons)
> - **ΔE<sub>0</sub>′** = standard redox potential change

> **CONCEPT — Why the minus sign is there — and why it is not a trick**
>
> The two conventions run in opposite directions, and the minus sign is what reconciles them. A **positive** ΔE<sub>0</sub>′ means the acceptor genuinely wants the electrons more than the donor does, so the transfer happens on its own — it is spontaneous. But in thermodynamics the marker of a spontaneous process is a **negative** ΔG. Same physical fact, opposite sign convention. The minus sign simply translates between them.
>
> The practical consequence, stated on her key-points slide: **the more positive the ΔE, the more negative the ΔG** — the bigger the gap in electron appetite between two carriers, the more energy that single step releases. This is the reason the chain can afford to make ATP at some steps and not others.

> **MEMORIZE — her key points slide, verbatim content**
>
> - **Electron-transfer reactions are a source of free energy.**
> - Low redox potential = low affinity for electrons.
> - The difference in redox potential between acceptor and donor **determines the magnitude of ΔG**.
> - Electron transfer reactions can be **linked in series in order of increasing redox potential** — her analogy: **an electrical circuit**.

## Objective 2 · The carriers of reducing equivalents, and the energy yield from NADH

### 2.1 Mitochondrial architecture — four compartments, and why each matters

    MITOCHONDRIAL ANATOMY — the geography every later concept depends on

      ╔══════════════════════════════════════════════════╗
      ║  OUTER MEMBRANE — permeable                       ║
      ║ ┌──────────────────────────────────────────────┐ ║
      ║ │  INTERMEMBRANE SPACE  ← H+ pumped out here  │ ║   more acidic, positive
      ║ │ ╔══════════════════════════════════════════╗ │ ║
      ║ │ ║ INNER MEMBRANE — semipermeable, folded   ║ │ ║ ← ETC + ATP synthase
      ║ │ ║   into cristae; IMPERMEABLE to H+       ║ │ ║   live here
      ║ │ ║                                          ║ │ ║
      ║ │ ║   MATRIX — soluble; TCA cycle runs here  ║ │ ║   less acidic, negative
      ║ │ ║   reducing equivalents are generated here ║ │ ║
      ║ │ ╚══════════════════════════════════════════╝ │ ║
      ║ └──────────────────────────────────────────────┘ ║
      ╚══════════════════════════════════════════════════╝

***Two facts do all the work later:** the inner membrane is **impermeable to H<sup>+</sup>** (so a pumped proton cannot simply drift back), and it is **folded into cristae** (surface area for a great many copies of the chain). Uncouplers destroy the first property; that is their entire mechanism.*

> **MEMORIZE**
>
> - The mitochondrion is **the major energy-generating compartment** of most eukaryotic cells.
> - **Reducing equivalents are generated in the matrix** (TCA cycle — the common final oxidation pathway for carbohydrate, lipid and protein). **Electron transport and ATP synthesis happen in the inner membrane.**
> - Mitochondria contain **their own DNA and ribosomes**. **mtDNA is maternally inherited** and in humans **encodes 13 proteins of the ETC**.
> - More **NADH + H<sup>+</sup>** is produced than FADH<sub>2</sub> — she stressed that NAD<sup>+</sup> is the more-used acceptor of the two.

> **CLINICAL — why maternal inheritance is worth remembering**
>
> Because mtDNA encodes 13 ETC subunits and is inherited **only from the mother**, mitochondrial ETC disorders show a distinctive pedigree: **an affected mother passes it to all of her children; an affected father passes it to none.** The tissues that fail first are the ones with the highest ATP demand — **nerve and muscle**. That inheritance pattern is a favourite exam hook, and it follows directly from a fact stated in one line on slide 11.

### 2.2 Getting cytosolic reducing equivalents into the matrix

> **CONCEPT**
>
> NADH generated inside the matrix has a short walk to the chain. But NADH generated **in the cytosol** — glycolysis is the example she flagged for a later lecture — faces the same impermeable inner membrane that makes the proton gradient possible. NADH cannot cross it. So the cell does not move the NADH; it moves the *reducing equivalents*, handing the electrons to a carrier that *can* cross, and reloading them onto an acceptor on the far side. That is what a shuttle is.

> **MEMORIZE**
>
> Two shuttles transfer **extramitochondrial (cytosolic) reducing equivalents** into the mitochondrion:
>
> - **Glycerophosphate shuttle**
> - **Malate–aspartate shuttle**
>
> Named only, and explicitly deferred by her to the glycolysis lecture. Know the two names and what problem they solve.

### 2.3 The energy yield from one NADH — the calculation she said you must be able to do

> **CONCEPT — How to run this calculation without memorizing it**
>
> Her whole method is: **look at the overall equation and ask who accepts the reducing equivalents.** That identifies the acceptor; the other pair is the donor; then subtract, and feed the result into ΔG<sub>0</sub>′ = −nFΔE<sub>0</sub>′. There is nothing else to it.

    WORKED EXAMPLE — oxidation of one NADH by oxygen (slide 14)

      Overall:   NADH + H+ + ½O2  ──>  NAD+ + H2O

      Two redox pairs:
         NADH + H+  ⇄  NAD+ + 2H+ + 2e−       E0′ = − 0.32 V   (donor)
         ½O2 + 2H+ + 2e−  ⇄  H2O           E0′ = + 0.82 V   (acceptor)

      Step 1   ΔE0′ = acceptor − donor = (+0.82) − (−0.32) = + 1.14 V
      Step 2   ΔG0′ = − n F ΔE0′ = − (2)(23.06)(1.14) = − 52.6 kcal/mol
      Step 3   ATP costs 7.3 kcal/mol  →  52.6 / 7.3 ≈ 7 ATP if 100 % efficient

      Actual yield: 3 ATP   →   efficiency ≈ 22/52.6 ≈ 40 %; the balance is heat

***n = 2, always, for one NADH** — two electrons per reducing-equivalent pair. The commonest arithmetic slip on this calculation is using n = 1.*

> **TRAP — "7 ATP" is a hypothetical, not a yield**
>
> The 7 is what you would get at **100% efficiency**, and the slide says so in parentheses. The real answer to "how many ATP does one NADH give" is **3** (by this course's convention). If a stem gives you −52.6 kcal and asks for ATP yield, read carefully whether it is asking for the **thermodynamic maximum** (7) or the **physiological yield** (3). Both numbers are on the same slide precisely because the gap between them — energy lost as heat — is the point.

## Objective 3 · The sequence of ETC components, and ROS production

### 3.1 The architecture: 5 fixed complexes, 2 mobile carriers

> **MEMORIZE — the frame she repeated at least six times**
>
> - **Location: the inner mitochondrial membrane.**
> - **5 fixed complexes** (I–IV plus **Complex V = the ATP synthase complex**, also called the **F<sub>0</sub>F<sub>1</sub> complex**).
> - **2 mobile carriers: Coenzyme Q (lipid-soluble) and Cytochrome c (water-soluble).**
> - Complexes are arranged in **order of increasing redox potential**, spanning **~1.1 V**.
> - **ATP is made at Complexes I, III, and IV.** These are the three **coupling sites**.
> - **Complex II is NOT a coupling site and does not make ATP.** No protons are pumped through Complex II.

    THE CHAIN, IN ORDER — with the two entry points and three pumps

     NADH-linked substrates                     FADH2-linked substrates
     (pyruvate, α-KG, isocitrate, malate)       (succinate)
            │                                          │
            v                                          v
       ┌─────────┐                              ┌─────────┐
       │COMPLEX I│  FMN, 7 Fe–S                 │COMPLEX II│  FAD, 2 Fe–S
       │  PUMPS H⁺│                              │ no pump │   ← bypasses Complex I
       └────┬────┘                              └────┬────┘
            └──────────────┬───────────────────────-─┘
                           v
                   Coenzyme Q (mobile, lipid-soluble)  ← accepts from BOTH I and II
                           │
                           v
                     ┌──────────┐
                     │COMPLEX III│  Cyt b (b562, b566), Cyt c₁, 1 Fe–S
                     │  PUMPS H⁺ │
                     └─────┬────┘
                           v
                  Cytochrome c (mobile, water-soluble)
                           │
                           v
                     ┌──────────┐
                     │ COMPLEX IV│  Cyt a, Cyt a₃, Cu
                     │  PUMPS H⁺ │
                     └─────┬────┘
                           v
                     ½O2 + 2H+ ──> H2O

     Electron flow is UNIDIRECTIONAL — there is no backward flow.

***The one asymmetry that generates most of the exam questions:** NADH-linked substrates pass through I, III and IV — **three** pumps, **3 ATP**. FADH<sub>2</sub>-linked substrates enter at Complex II and **bypass Complex I** — **two** pumps, **2 ATP**.*

### 3.2 Each complex: name it, and know its one job

> **CONCEPT — her framework, which makes the inhibitors free**
>
> She insisted that for every complex you should be able to state **one thing: what it hands to what.** Not the internal electron gymnastics — she explicitly said *"we are not going into details of this, all you need to know is the function."* The payoff is that once you know the job, you can derive the effect of any inhibitor without memorizing it: **block a complex, and whatever that complex was supposed to reduce simply does not get reduced.** She drilled exactly that question after each complex.

**The four complexes — the "function" column is the one to memorize**

| Complex | Names | Prosthetic groups | Function: passes reducing equivalents… | Coupling site? |
|----|----|----|----|----|
| **I** | **NADH dehydrogenase** · **NADH:Q oxidoreductase** · \>25 polypeptides — **largest complex** | **FMN** · **7 Fe–S** centres | **from NADH+H<sup>+</sup> → Coenzyme Q** · NADH + CoQ → CoQH<sub>2</sub> + NAD<sup>+</sup> | **YES** — 1 ATP |
| **II** | **Succinate dehydrogenase** · **FADH<sub>2</sub>:Q oxidoreductase** · 4 polypeptides | **FAD** (covalently bound) · **2 Fe–S** | **from FADH<sub>2</sub> → Coenzyme Q** · FADH<sub>2</sub> + CoQ → CoQH<sub>2</sub> + FAD | **NO** — no H<sup>+</sup> pumped, no ATP |
| **III** | **CoQH<sub>2</sub>:Cyt c oxidoreductase** · (the **bc<sub>1</sub>** complex) · 6 polypeptides | **Cyt b** (2 hemes: b562, b566) · **Cyt c<sub>1</sub>** · **1 Fe–S** | **from CoQH<sub>2</sub> → Cytochrome c** | **YES** — 1 ATP |
| **IV** | **Cytochrome c oxidase** · **Cyt c:O<sub>2</sub> oxidoreductase** · 13 polypeptides | **Cyt a and Cyt a<sub>3</sub>** · each with one **Cu** atom | **from Cytochrome c → O<sub>2</sub>**, reducing it to **H<sub>2</sub>O** | **YES** — 1 ATP |

> **TRAP — her own "pay attention on that" pairs**
>
> She pointed out that the complexes come in look-alike pairs and told you what separates them:
>
> - **I vs II** — both feed Coenzyme Q, both carry a flavin and Fe–S. **Complex I has FMN; Complex II has FAD.**
> - **III vs IV** — both are cytochrome complexes. **Complex III has cytochrome bc<sub>1</sub>; Complex IV has cytochrome aa<sub>3</sub>.**
> - **Complex IV is the only complex that requires copper**, so **copper deficiency impairs Complex IV.** She tied this back to the enzymes lecture: **lysyl oxidase** also requires copper. Her mnemonic pairing — "no lysyl oxidase and copper, and no copper and Complex IV."

> **MEMORIZE — the two mobile carriers**
>
> - **Coenzyme Q (ubiquinone)** — the **only lipid-soluble** component; an **isoprenoid** unit and an **intermediate of cholesterol synthesis**. Accepts hydrogen atoms **from both Complex I (via FMNH<sub>2</sub>) and Complex II (via FADH<sub>2</sub>)** — it is the convergence point of the two entry routes.
> - **Cytochrome c** — **water-soluble**; a soluble protein of the **intermembrane space** that donates electrons to the **copper ions of Complex IV**.
> - **Cytochromes are heme proteins** — she noted that "hemeprotein" is an alternative name you may see. Types: cytochromes a, b, c.

> **CONCEPT — Why Complex II cannot be a coupling site — the reasoning, not the fact**
>
> Look back at the redox ladder. Complex I receives electrons at **−0.32 V** (NADH) and delivers them to CoQ at **+0.10 V** — a drop of **0.42 V**. Complex II receives them at **−0.22 V** (FADH<sub>2</sub>) and delivers to the same CoQ — a drop of only **0.32 V**. Complex II's step is shallower, and the energy it releases is **not enough to pay for pumping protons across the membrane**. It simply passes the electrons along.
>
> So Complex II has no proton pump, contributes nothing to the gradient, and contributes nothing to ATP. Everything that enters through it forfeits the Complex I pump as well, because it enters *after* that point. Hence **2 ATP instead of 3** — a direct consequence of where FAD sits on the ladder.

### 3.3 Reactive oxygen species from the chain

> **MEMORIZE**
>
> - **Superoxide (O<sub>2</sub><sup>•−</sup>) is produced during normal ETC function** — this is ordinary metabolism, not pathology.
> - It leaks from two specific places: **FMN in Complex I** and **ubiquinone in Complex III**.
> - ROS include **O<sub>2</sub><sup>•−</sup>, H<sub>2</sub>O<sub>2</sub>, and OH<sup>•</sup>**; other sources on the slide were radiation, inflammation, high pO<sub>2</sub>, smog (O<sub>3</sub>, NO<sub>2</sub>), chemicals and drugs, reperfusion injury, and aging. The endpoint is the **injured cell**.
> - She **explicitly deferred** the detoxification machinery to the **HMP shunt / pentose phosphate** lecture. Note the deferral; don't chase it.

> **CONCEPT — Why the leak happens exactly where it does**
>
> Complexes I and III are the two places where an electron sits, briefly, on a carrier that holds it **one at a time** — a flavin semiquinone in Complex I, a ubisemiquinone in Complex III. Molecular oxygen is diffusing freely through the membrane and is an excellent electron acceptor. If an electron escapes from one of those single-electron intermediates before the complex can pass it on properly, O<sub>2</sub> grabs it — and O<sub>2</sub> plus one electron *is* superoxide. This is the unavoidable cost of using oxygen as the terminal acceptor, which is why every aerobic cell also carries antioxidant defences.

## Objective 4 · ATP synthesis and the energy yield of the ETC

### 4.1 Oxidative vs. substrate-level phosphorylation

> **MEMORIZE**
>
> - **Oxidative phosphorylation** = transfer of electrons from reduced coenzymes through the respiratory chain to **O<sub>2</sub>, the final acceptor of reducing equivalents**, with the released energy trapped as ATP. **Coupling of oxidation with phosphorylation.** Requires **ETC + mitochondria + oxygen**.
> - **Substrate-level phosphorylation** = ATP made **without** the ETC, where the substrate itself carries enough energy. Example flagged for later: **glycolysis**.

### 4.2 The chemiosmotic theory — the mechanism

> **CONCEPT — how a falling electron becomes a phosphate bond**
>
> The problem the cell has to solve is a translation problem. Electron transfer releases energy in one currency (redox); ATP stores it in another (a phosphoanhydride bond). Those two things cannot touch each other directly. The chemiosmotic theory is the answer: **convert the redox energy into a proton gradient, then convert the proton gradient into ATP.** The gradient is the intermediate currency, and it is physically a gradient across a membrane — which is why the membrane has to be impermeable for any of this to work.
>
> Concretely: as electrons fall through Complexes I, III and IV, each of those complexes uses the released energy to **pump H<sup>+</sup> out of the matrix into the intermembrane space**. Because the inner membrane will not let protons back through, they accumulate. That builds **two** gradients at once, and the exam cares about both: a **chemical gradient (ΔpH)** — more acidic outside — and an **electrical gradient (ΔΨ)** — the matrix side becomes **negative**. Together they are the **proton-motive force**, and both of them pull the protons back toward the matrix.
>
> The only route back is through **F<sub>0</sub>, the channel of the ATP synthase complex**. Protons flowing through it drive a **conformational change** in the F<sub>1</sub> head, and that conformational change is what forces **P<sub>i</sub> onto ADP**. That is the coupling — not a chemical intermediate, but a circuit.

    THE PROTON CIRCUIT (chemiosmotic theory)

      INTERMEMBRANE SPACE     ←── H⁺ ── H⁺ ── H⁺ ──┐        high [H⁺], acidic, positive
            ▲       ▲       ▲                      │
       ╔════╪═══════╪═══════╪══════════════════════╪════╗
       ║   I III IV          II       V (F₀F₁)  ║  INNER MEMBRANE
       ║  pump pump pump no pump       │      ║  impermeable to H⁺
       ╚════╪═══════╪═══════╪══════════════════════╪════╝
            │       │       │                      ▼
      MATRIX  e⁻ flow releases energy         H⁺ returns  →  ADP + Pᵢ → ATP
                                                              low [H⁺], negative
    OUT through the pumps (I, III, IV)  ·  BACK IN through F₀ of Complex V
      The two legs together are the PROTON CIRCUIT. Break either leg and the whole thing stops.

***Note Complex II sits in the membrane but has no arrow.** That single visual fact is the entire explanation for P:O = 2 versus 3.*

### 4.3 P:O ratio

> **MEMORIZE**
>
> - **P:O ratio = the number of ATP produced per atom of oxygen reduced** (per ½ mol O<sub>2</sub> consumed). She gave this definition explicitly.
> - Substrate oxidized via **NAD-linked dehydrogenases** → **3 mol ATP per ½ mol O<sub>2</sub>** → **P:O = 3**
> - Substrate oxidized via **FAD-linked dehydrogenases** → **2 mol ATP per ½ mol O<sub>2</sub>** → **P:O = 2**
> - NAD-linked examples named on the slide: **pyruvate, α-ketoglutarate, isocitrate, malate**. FAD-linked: **succinate**.

### 4.4 Respiratory control — why the chain doesn't just run all the time

> **CONCEPT**
>
> Once the gradient exists, it pushes back. Pumping another proton out means working *against* an already-steep gradient, and past a certain steepness the complexes can no longer do it — so electron flow stalls. The only way to relieve that back-pressure is to **let protons back in through ATP synthase**, which requires **ADP and P<sub>i</sub> to be available** as substrates.
>
> The result is a self-regulating system that is exactly as fast as the cell's ATP demand: plenty of ADP (cell is spending energy) → protons flow back → gradient relaxes → chain runs → O<sub>2</sub> consumed. Little ADP because everything is already ATP (cell is satisfied) → nowhere for protons to go → gradient stays steep → chain stalls → O<sub>2</sub> consumption falls. **The chain is demand-driven, and ADP is the demand signal.**

> **MEMORIZE**
>
> **Rate of oxidative phosphorylation ∝ (\[ADP\] \[P i \]) / (\[ATP\])**
>
> - Once the electrochemical gradient is formed, **further transport of reducing equivalents is inhibited unless the gradient is discharged by ATP synthesis**.
> - This is **respiratory control**, and it depends on the **availability of ADP and P<sub>i</sub>**.
> - It controls both the **speed of ATP synthesis and oxygen consumption** — the two move together.

> **TRAP — she warned about this explicitly**
>
> *"Does the ratio of ATP to ADP, or ADP to ATP? You have to be careful what they are asking — they can reverse it too."* Work it out from the concept rather than the memorized fraction: **ADP is the "go" signal.** High ADP (i.e. high ADP/ATP, low ATP/ADP) → chain speeds up. High ATP → chain slows down. If you reason from "ADP means the cell needs ATP," you cannot be caught by the inversion.

## Objective 5 · Inhibitors and uncouplers

> **CONCEPT — The organizing idea — three mechanisms, but only two outcomes**
>
> Everything in this objective is a lesion in the proton circuit, and there are exactly three places to put one.
>
> **(A) Block electron flow through a complex.** No electrons falling → no energy → no pumping → no gradient → no ATP. Oxygen is never reached, so O<sub>2</sub> consumption stops too.
>
> **(B) Block the proton's return path through ATP synthase.** Now protons are pumped out but cannot come back. The gradient builds until the back-pressure is so great the pumps stall — and when pumping stalls, **electron flow stalls with it**. This is respiratory control working exactly as designed, and it is why blocking ATP synthase shuts down the ETC even though the ETC itself is untouched. **Same three arrows down as (A).**
>
> **(C) Put a hole in the membrane for protons.** This is categorically different. Protons now return *without* passing through ATP synthase, so the gradient can never build — which means **there is never any back-pressure**. The chain, freed from respiratory control, *"does not know when to stop"* and runs flat out. ETC function **up**, O<sub>2</sub> consumption **up**, and ATP **down**, because the energy bypasses the turbine entirely and leaves as **heat**.
>
> So: **A and B look identical; C is the odd one out, and the only one that splits the arrows.** If you remember nothing else from this objective, remember that uncouplers are the only agents that *increase* oxygen consumption.

**The comparison table (slide 48) — reproduce this from memory**

| Agent | Mechanism | ETC function | O<sub>2</sub> consumption | ATP synthesis |
|----|----|----|----|----|
| **A. Inhibitors of ETC complexes** · Rotenone, antimycin, CO, CN<sup>−</sup> | Block **electron flow** through complexes | ↓ decreased | ↓ decreased | ↓ decreased |
| **B. Inhibitors of oxidative phosphorylation** · Oligomycin, atractyloside | Block **H<sup>+</sup> flow** through the ATP synthase (F<sub>0</sub>F<sub>1</sub>) complex | ↓ decreased | ↓ decreased | ↓ decreased |
| **C. Uncouplers** · 2,4-DNP, 2,4-DNC, thermogenin, aspirin toxicity | **Increase permeability** of the inner membrane to H<sup>+</sup> | **↑ INCREASED** | **↑ INCREASED** | ↓ decreased |

### 5.1 Inhibitors of the ETC complexes, by site

**Slide 39 and the Harper's figure on slide 48**

| Blocked step | Inhibitors | Identity / notes |
|----|----|----|
| **Complex I → CoQ** | **Amobarbital** (a **barbiturate**) · **Rotenone** · **Piericidin A** | Amobarbital — sedative · Rotenone — **insecticide and fish poison**; not fatal to humans, has stomach-irritant properties causing vomiting · Piericidin A — antibiotic |
| **Complex II → CoQ** | **Malonate** · **Carboxin**, TTFA | **Malonate is a competitive inhibitor of succinate dehydrogenase** — a structural analog of succinate, tying straight back to the enzymes lecture · Carboxin — agricultural fungicide |
| **Complex III → Cyt c** | **Antimycin A** · **Dimercaprol** (BAL) | Dimercaprol = British Anti-Lewisite; used clinically as a **chelator for arsenic, mercury and lead** poisoning |
| **Complex IV → O<sub>2</sub>** | **Carbon monoxide (CO)** · **Cyanide (CN<sup>−</sup>)** · **H<sub>2</sub>S** | The two clinically important ones — see below. · **Cyanide antidotes: amyl nitrite / nitrites, thiosulfate** |

> **TRAP — Her exam drill — "first know normal, then know abnormal"**
>
> She asked the same question after every complex, and it is the fastest way to answer any ETC inhibitor item. **Take the complex's normal job and negate it:**
>
> - Complex I blocked → **will CoQ be reduced? No.**
> - Complex II blocked → **will CoQ be reduced? No.**
> - Complex III blocked → **can CoQH<sub>2</sub> be oxidized? No.** (Note the direction — she flagged this one as the easy place to answer carelessly, because the question is phrased about the *reduced* carrier being oxidized, not the other way round.)
> - Complex IV blocked → **will oxygen be reduced? No.**
>
> A general consequence worth stating: everything **upstream** of a block stays **reduced** (electrons pile up behind the dam), and everything **downstream** stays **oxidized** (nothing arrives).

### 5.2 Carbon monoxide vs. cyanide — the highest-yield discrimination in the lecture

> **CONCEPT — one difference explains everything else**
>
> Both poisons hit **Complex IV, at cytochrome a<sub>3</sub>**. The distinction that generates every other difference is **which oxidation state of the iron they bind, and how tightly**. CO binds the **ferrous (Fe<sup>2+</sup>)** form **non-covalently** — so it can be competed off, and you treat by flooding the patient with the competitor, oxygen. Cyanide binds the **ferric (Fe<sup>3+</sup>)** form, and she taught this binding as **covalent and not reversible** — so you cannot compete it off, and the only strategy is to offer the cyanide **a more attractive Fe<sup>3+</sup> elsewhere in the body** and let it leave with that instead. That is precisely what the antidote does.

|  | Carbon monoxide (CO) | Cyanide (CN<sup>−</sup>) |
|----|----|----|
| **Binds** | **Fe<sup>2+</sup> (ferrous)** of heme in Cyt a<sub>3</sub> | **Fe<sup>3+</sup> (ferric)** of heme in Cyt a<sub>3</sub> |
| **Bond** | **Non-covalent → reversible** | **Covalent → not reversible** (as taught) |
| **Second target** | **Also binds hemoglobin** — this is what kills | Complex IV only |
| **Sources / history** | Burning furnaces in closed spaces, camping lanterns in a closed tent, automobile exhaust, suicide attempts | **Sodium nitroprusside** (IV antihypertensive — **releases cyanide as a by-product**); **cyanogenic glycosides**: cassava (manioc), bitter almonds, pits of cherry/apple/apricot |
| **Sign** | **Cherry-red skin / cyanosis** | **Flushed / cherry-red**; death from **tissue asphyxia, especially CNS** |
| **Treatment** | **100 % oxygen / hyperbaric oxygen** — out-competes CO because the bond is non-covalent | **Amyl nitrite** (or nitrites) → makes **methemoglobin**; then **sodium thiosulfate**. Also hydroxocobalamin. **Act within minutes.** |

    WHY THE CYANIDE ANTIDOTE WORKS — follow the Fe³⁺

      Problem:   CN⁻  ──binds──>  Fe³⁺ of Complex IV   →  ETC stops  →  cell death

      Step 1     Give amyl nitrite
      Step 2     Nitrite oxidises haemoglobin iron:  Hb(Fe²⁺) ──> metHb(Fe³⁺)
      Step 3     Now the blood is full of competing Fe³⁺ sites.
                 CN⁻ binds metHb instead of Complex IV  →  cyanmethaemoglobin
      Step 4     Sodium thiosulfate converts it to thiocyanate  ──>  excreted

      Logic: you cannot pull cyanide OFF Complex IV, so you give it
             somewhere better to go BEFORE it gets there.

***The cost of the antidote:** methemoglobin cannot carry oxygen. You are deliberately disabling some haemoglobin to save the entire electron transport chain — a trade worth making, but the reason nitrite therapy is not innocuous.*

> **CLINICAL — why CO is lethal at 50% when anemia at 50% is not**
>
> This was a question posed directly on slide 40, and it is pure integration with the haemoglobin material. Losing half your haemoglobin to anaemia leaves the remaining half working **normally** — it loads oxygen in the lung and **unloads it in the tissues**. Losing half to CO is worse than useless, because **CO binding to one heme makes the remaining hemes hold their oxygen more tightly**: it shifts haemoglobin to the **relaxed (R) conformation**, shifts the **oxygen-binding curve to the left**, and changes the normal **sigmoid shape toward a hyperbola**. The affected haemoglobin **cannot release oxygen to the tissues.** So the patient has both a Complex IV block and a delivery failure at once.
>
> CO's affinity for haemoglobin is roughly **220× that of oxygen** (slide 40; she said 210 verbally — see the reconciliation table).

### 5.3 Inhibitors of oxidative phosphorylation

> **MEMORIZE**
>
> - **Oligomycin** — an antibiotic. **Inhibits ATP synthase**; blocks the **F<sub>0</sub>F<sub>1</sub> ATPase** by blocking **conduction of H<sup>+</sup> through F<sub>0</sub>**. Prevents ATP manufacture **with decreased oxygen consumption** — that last clause is the exam point.
> - **Atractyloside** — a plant glycoside. **Inhibits translocation of ADP and ATP** across the inner membrane (the adenine nucleotide translocase). Different target, same net effect: ADP cannot reach the synthase, so the gradient cannot discharge.

### 5.4 Uncouplers

> **MEMORIZE**
>
> - **Mechanism: leakage of H<sup>+</sup> across the inner membrane, collapsing the electrochemical proton gradient.** They **dissociate oxidation from phosphorylation** — hence the name.
> - **2,4-Dinitrophenol (2,4-DNP)** — binds protons and **readily diffuses across the inner membrane**, losing the energy as **heat**. Causes electron transport to proceed **rapidly without producing a proton gradient**.
> - Others named: **dinitrocresol (2,4-DNC)**, **pentachlorophenol**, **CCCP** (chlorocarbonyl cyanide phenylhydrazone).
> - **Aspirin / salicylates in high doses (toxicity) are uncouplers** — this is why salicylate overdose causes **fever**.
> - **Thermogenin (uncoupling protein, UCP1) in brown adipose tissue is the natural, physiological uncoupler.**

> **CONCEPT — Why an uncoupler makes you hot — and why that is the whole clinical story**
>
> In a normally coupled mitochondrion the energy of oxidation is captured in ATP; only the inefficiency (~60%) escapes as heat. An uncoupler removes the capture step entirely. The chain still runs — faster than ever, since nothing is holding it back — and **100% of the energy of oxidation now leaves as heat**. The patient burns substrate at maximum rate, makes no ATP from it, and cannot shed the heat fast enough. **Hyperthermia** is the presenting problem, and it is also what kills.

> **CLINICAL — 2,4-DNP as a diet drug, and brown fat as the same trick used well**
>
> Her speaker note is blunt: **2,4-DNP "had people falling dead while on this diet drug — they died of hyperthermia."** The logic is seductive and genuinely correct: burn fuel, make no ATP, lose weight. The problem is that there is no dose control over body temperature, and the therapeutic window is effectively nonexistent. This is why the answer to "can uncouplers be used as anti-obesity drugs?" is a qualified no.
>
> **Brown adipose tissue does the same thing on purpose and safely**, because it is regulated. **Thermogenin** spans the inner membrane and acts as a **proton conductance pathway**, transporting protons back into the matrix and dissipating the gradient as heat. This is **non-shivering thermogenesis**, and it matters most in the **newborn**, who cannot shiver effectively and must protect the vital organs.

## Where the lecture was imprecise — reconciled

The transcript is a rough auto-transcription and has been silently normalized throughout (*"exagonic"* → exergonic, *"phosphorilation"* → phosphorylation, *"redux"* → redox, *"christe"* → cristae, *"co-enzyme"* → coenzyme, *"attractioside"* → atractyloside, *"oligyin/algyin"* → oligomycin, *"ditrophenol"* → dinitrophenol, *"thermogenine"* → thermogenin, *"metoglobin"* → methemoglobin, *"flush sinosis"* → flushed cyanosis, *"nasin"* → niacin, *"lysol oxidase"* → lysyl oxidase, *"cassava/Gari"* retained as spoken). The entries below are substantive, not transcription noise.

| What was said / shown | What is precisely true | Does it matter for the exam? |
|----|----|----|
| **P:O = 3 for NADH, 2 for FADH<sub>2</sub>** (slides 18, 35) | These are the classical integer values. Measured proton stoichiometry gives **≈2.5 ATP per NADH and ≈1.5 per FADH<sub>2</sub>**, because the number of protons pumped is not an exact multiple of the number needed per ATP. Current editions of most textbooks use the decimal values. | **Use 3 and 2 for this course.** She taught the integers exclusively and every calculation on the slides uses them. Recognize 2.5/1.5 if another source uses them. |
| **Transcript: "carbon monoxide has high affinity to bind to heme than oxygen, 210 times more"** | Her slide says **220 times**. Published values range ~200–250×. The two numbers are her own slide vs. her own speech. | Low. **Quote 220** if a number is demanded — it is what is written on the slide. |
| **Transcript: "Thermogenin is an unnatural uncoupler in your body"** | Slip (and a transcription artifact). Thermogenin is the **natural / physiological** uncoupler — her slide says "a natural uncoupler," and she says "natural" correctly elsewhere in the same passage. | Yes, but only as a reading error. Thermogenin is **physiological**. |
| **Transcript: "malignant hypertension — diastolic more than systolic"** | As transcribed this is not a meaningful statement; diastolic pressure is never above systolic. **Malignant hypertension** is severe hypertension (typically diastolic \>120–130 mmHg) **with acute end-organ damage**. The relevant point for this lecture is simply that it is treated with **IV sodium nitroprusside**, which releases cyanide. | Not for biochemistry. **The examinable link is nitroprusside → cyanide release.** |
| **Cyanide binds Fe<sup>3+</sup> of Complex IV "covalently"** (slide 43, and repeated verbally) | The bond is a **coordinate (dative) bond** to the ferric heme iron, not a classical covalent bond, and it is in principle reversible — which is exactly why sequestering agents work at all. Her clinical point is sound: it is far too tight to displace with oxygen, so treat it as irreversible at the bedside. | **Answer "covalent" if contrasted with CO's "non-covalent."** That contrast is the tested discrimination and the treatment logic follows from it correctly. |
| **"Complex I has 7 Fe–S centres"** (slide 19 and speaker notes) | Counts vary by source (commonly quoted as 6–8 iron–sulfur clusters). Her deck states 7 twice, including in the speaker notes. | Low. **Use her numbers** — Complex I: FMN + 7 Fe–S; Complex II: FAD + 2 Fe–S; Complex III: 1 Fe–S. |
| **ETC components "in order of increasing redox potential"** — presented as strictly monotonic | Nearly true, with one visible exception **in her own table**: **cytochrome b sits at +0.07 V, below Coenzyme Q at +0.10 V**, yet comes after it in the sequence. This is real — cytochrome b is part of the Q cycle inside Complex III and carries electrons on a branch, not straight down the ladder. | Low, but do not be thrown if you notice it. **The overall direction — negative to positive, ending at O<sub>2</sub> — is the examinable claim.** |
| **"Uncouplers abolish the proton circuit"** | Precisely, they abolish the **gradient**, not the pumping. The complexes keep pumping — harder than ever — but the protons leak straight back without passing through ATP synthase. Saying the circuit is "abolished" is shorthand for "short-circuited." | Conceptually yes: the reason O<sub>2</sub> consumption **rises** is that pumping continues and is never opposed. |
| **Slide 41: "Respiration inhibitor ions block the ETC and are always effective in decreasing oxygen uptake"** | True for inhibitors, and a useful "always" — but note it is **false for uncouplers**, which raise oxygen uptake. The sentence is safe only because it is scoped to inhibitors. | **Yes.** "Always decreases oxygen uptake" is true of inhibitors and is exactly the wrong answer for an uncoupler. |
| **ATP yield of NADH given as "7 if 100 % efficient"** (slide 14) | A thermodynamic ceiling, not a yield. Actual = 3 ATP ≈ 22 kcal of the 52.6 kcal available ≈ **40 % efficiency**; the rest is heat. | **Yes — read the stem carefully.** "Maximum possible" = 7; "how many are actually made" = 3. |
| **Complex II described as having "no protons pumped"** and separately as "not a coupling site" | These are the same fact stated two ways, not two facts. No pumping → no contribution to the gradient → no ATP attributable to that step. | Yes — but as one idea. It is why FADH<sub>2</sub> yields 2 rather than 3. |

## Rapid review — two-column recall sheet

Keyword-level recall only; explanations live in the body above. **Bold** = always/never rule or high-yield discrimination point.

### Redox basics

- **Reducing equivalent = proton + electron (2H<sup>+</sup> + 2e<sup>−</sup>)**
- Oxidation = gain O<sub>2</sub> **or** loss H<sub>2</sub>; biological oxidation = **loss of reducing equivalents**
- Enzymes: **oxidoreductases / dehydrogenases**
- NAD<sup>+</sup> ← **B3 niacin** · FAD ← **B2 riboflavin**
- **NADH reflects ATP status; NADPH does not** (NADPH = anabolism)
- More **NADH** made than FADH<sub>2</sub>

### Redox potential

- **E<sub>0</sub>′ = affinity for electrons**, at 1 M oxidant + reductant, **pH 7**
- **Low E<sub>0</sub>′ = low affinity · High E<sub>0</sub>′ = high affinity**
- **Electrons flow toward MORE POSITIVE E<sub>0</sub>′**
- **ΔE<sub>0</sub>′ = acceptor − donor**; acceptor is **always** higher
- **ΔG<sub>0</sub>′ = −nFΔE<sub>0</sub>′**; F = **23.06 kcal/V**; n = number of **electrons**
- **More positive ΔE → more negative ΔG**
- ETC spans **~1.1 V**, arranged in **increasing** E<sub>0</sub>′
- **O<sub>2</sub> has the highest E<sub>0</sub>′ (+0.82) — best acceptor**
- NAD<sup>+</sup>/NADH **−0.32** · FAD/FADH<sub>2</sub> **−0.22** · CoQ +0.10 · Cyt c +0.25

### NADH energy calculation

- ΔE<sub>0</sub>′ = +0.82 − (−0.32) = **+1.14 V**
- ΔG<sub>0</sub>′ = −(2)(23.06)(1.14) = **−52.6 kcal/mol**
- ATP = **7.3 kcal/mol** → **7 ATP if 100 % efficient**
- **Actual = 3 ATP (~40 % efficiency)**

### Mitochondrion

- Outer membrane **permeable**; inner **semipermeable**, folded into **cristae**
- **Inner membrane is IMPERMEABLE to H<sup>+</sup>** — the whole gradient depends on it
- **Matrix** = TCA cycle = where reducing equivalents are made
- **Inner membrane** = ETC + ATP synthase
- **mtDNA is maternally inherited; encodes 13 ETC proteins**
- Cytosolic equivalents need shuttles: **glycerophosphate**, **malate–aspartate**

### ETC architecture

- **5 fixed complexes + 2 mobile carriers**, inner mitochondrial membrane
- **Complex V = ATP synthase = F<sub>0</sub>F<sub>1</sub> complex**
- **Coupling sites: I, III, IV**
- **Complex II is NOT a coupling site — no H<sup>+</sup> pumped, no ATP**
- **CoQ = lipid-soluble**, isoprenoid, cholesterol-synthesis intermediate; accepts from **I and II**
- **Cyt c = water-soluble**, intermembrane space, donates to **Cu of Complex IV**
- Cytochromes = **heme proteins** (a, b, c)
- **Electron flow is unidirectional**

### The four complexes

- **I** — NADH dehydrogenase / NADH:Q oxidoreductase; **FMN + 7 Fe–S**; largest, \>25 chains; **NADH → CoQ**
- **II** — succinate dehydrogenase / FADH<sub>2</sub>:Q oxidoreductase; **FAD + 2 Fe–S**; **FADH<sub>2</sub> → CoQ**; **no ATP**
- **III** — CoQH<sub>2</sub>:Cyt c oxidoreductase, **bc<sub>1</sub>**; **Cyt b (b562, b566) + Cyt c<sub>1</sub> + 1 Fe–S**; **CoQH<sub>2</sub> → Cyt c**
- **IV** — cytochrome c oxidase, Cyt c:O<sub>2</sub> oxidoreductase; **Cyt a + a<sub>3</sub>, Cu**; **Cyt c → O<sub>2</sub> → H<sub>2</sub>O**
- **I vs II: FMN vs FAD** · **III vs IV: bc<sub>1</sub> vs aa<sub>3</sub>**
- **Only Complex IV needs copper → Cu deficiency impairs Complex IV** (cf. lysyl oxidase)

### ROS

- **Superoxide is made during NORMAL ETC function**
- **Leaks from FMN in Complex I and ubiquinone in Complex III**
- ROS: **O<sub>2</sub><sup>•−</sup>, H<sub>2</sub>O<sub>2</sub>, OH<sup>•</sup>**; detox deferred to HMP shunt lecture

### Oxidative phosphorylation

- **Oxidative phosphorylation = ATP made WITH the ETC** (needs mitochondria + O<sub>2</sub>)
- **Substrate-level phosphorylation = ATP WITHOUT the ETC** (e.g. glycolysis)
- **Chemiosmotic theory:** I, III, IV pump H<sup>+</sup> **out** → gradient → H<sup>+</sup> back **in** through **F<sub>0</sub>** → conformational change → **ADP + P<sub>i</sub> → ATP**
- Two gradients: **ΔpH** (acidic outside) + **ΔΨ** (**matrix negative**)
- **P:O = ATP per atom of oxygen reduced**
- **NADH → P:O = 3** (pyruvate, α-KG, isocitrate, malate)
- **FADH<sub>2</sub> → P:O = 2** (succinate) — **bypasses Complex I**

### Respiratory control

- Rate ∝ **\[ADP\]\[P<sub>i</sub>\] / \[ATP\]**
- **ADP is the "go" signal**; high ATP slows the chain
- Gradient cannot discharge without **ADP + P<sub>i</sub>**
- Controls **both ATP synthesis and O<sub>2</sub> consumption**
- **Watch for the ratio being inverted in the stem**

### The three lesions

- **ETC inhibitors** — block electron flow: **ETC ↓, O<sub>2</sub> ↓, ATP ↓**
- **ATP synthase inhibitors** — block H<sup>+</sup> return: **ETC ↓, O<sub>2</sub> ↓, ATP ↓** (same, via back-pressure)
- **UNCOUPLERS** — H<sup>+</sup> leak: **ETC ↑, O<sub>2</sub> ↑, ATP ↓** + **HEAT**
- **Uncouplers are the ONLY agents that increase O<sub>2</sub> consumption**

### Inhibitors by site

- **I** — **rotenone** (insecticide/fish poison), **amobarbital**/barbiturates, piericidin A
- **II** — **malonate** (**competitive** inhibitor of SDH), carboxin, TTFA
- **III** — **antimycin A**, dimercaprol (BAL)
- **IV** — **CO, CN<sup>−</sup>, H<sub>2</sub>S**
- **ATP synthase** — **oligomycin** (blocks H<sup>+</sup> through F<sub>0</sub>)
- **ADP/ATP translocase** — **atractyloside**
- Rule: **upstream of a block stays reduced, downstream stays oxidized**

### CO vs cyanide

- Both hit **Complex IV, cytochrome a<sub>3</sub>**
- **CO → Fe<sup>2+</sup>, NON-covalent → reversible → 100 % / hyperbaric O<sub>2</sub>**
- **CN<sup>−</sup> → Fe<sup>3+</sup>, covalent → amyl nitrite → metHb(Fe<sup>3+</sup>) sequesters CN<sup>−</sup> → thiosulfate → thiocyanate → excreted**
- CO also binds Hb (**220×** O<sub>2</sub>): shifts curve **LEFT**, sigmoid → hyperbolic, **cannot offload O<sub>2</sub>**
- CN<sup>−</sup> sources: **nitroprusside**, **cassava**, bitter almonds, fruit pits
- Both: **cherry-red**

### Uncouplers

- **2,4-DNP** — former diet drug, **fatal hyperthermia**
- 2,4-DNC, pentachlorophenol, CCCP
- **Aspirin/salicylate overdose = uncoupler → fever**
- **Thermogenin (UCP1), brown adipose tissue = the NATURAL uncoupler**; non-shivering thermogenesis, critical in the **newborn**

## Self-test — 15 questions

1.  Define a reducing equivalent, and restate "biological oxidation" using it.
    **Answer: A proton plus an electron. Biological oxidation = loss of H 2 = loss of 2H + + 2e − = loss of reducing equivalents.**
2.  In which direction do electrons move along a redox series, and how is ΔE<sub>0</sub>′ defined?
    **Answer: Toward the more positive (higher) standard redox potential — the acceptor always exceeds the donor. ΔE 0 ′ = E 0 ′(acceptor) − E 0 ′(donor).**
3.  Why does ΔG<sub>0</sub>′ = −nFΔE<sub>0</sub>′ carry a minus sign?
    **Answer: A positive ΔE 0 ′ means spontaneous, and spontaneity is signalled by a negative ΔG. The sign converts between two opposite conventions.**
4.  Calculate ΔE<sub>0</sub>′ and ΔG<sub>0</sub>′ for NADH + H<sup>+</sup> + ½O<sub>2</sub> → NAD<sup>+</sup> + H<sub>2</sub>O.
    **Answer: ΔE 0 ′ = +0.82 − (−0.32) = +1.14 V. ΔG 0 ′ = −(2)(23.06)(1.14) = −52.6 kcal/mol. Enough for 7 ATP at 100% efficiency; actually yields 3.**
5.  Where in the mitochondrion are reducing equivalents generated, and where are they spent?
    **Answer: Generated in the matrix (TCA cycle); spent in the inner membrane, where the ETC and ATP synthase sit.**
6.  A disease is caused by a mutation in an ETC subunit encoded by mtDNA. What inheritance pattern do you expect?
    **Answer: Maternal — an affected mother transmits to all offspring, an affected father to none. mtDNA encodes 13 ETC proteins.**
7.  Name the five complexes' jobs in one line each.
    **Answer: I: NADH → CoQ. II: FADH 2 → CoQ. III: CoQH 2 → cytochrome c. IV: cytochrome c → O 2 → H 2 O. V: ATP synthase, H + back in → ATP.**
8.  Which complex is not a coupling site, and why does that follow from the redox ladder?
    **Answer: Complex II. FADH 2 enters at −0.22 V rather than −0.32 V, so the drop to CoQ is too small to pay for pumping protons. No pump → no ATP → P:O = 2.**
9.  Which two prosthetic-group differences separate the look-alike complexes?
    **Answer: Complex I has FMN, Complex II has FAD. Complex III has cytochrome bc 1 , Complex IV has cytochrome aa 3 (plus copper).**
10. A patient is copper deficient. Which ETC complex is impaired, and which other enzyme from the enzymes lecture shares this requirement?
    **Answer: Complex IV (cytochrome c oxidase) — the only copper-requiring complex. Lysyl oxidase, in collagen processing, also requires Cu 2+ .**
11. Where is superoxide produced during normal electron transport?
    **Answer: Leaking from FMN in Complex I and from ubiquinone in Complex III.**
12. State the chemiosmotic theory in one sentence, and name the two components of the gradient.
    **Answer: Complexes I, III and IV pump H + out of the matrix; the protons return through F 0 of ATP synthase, and that flow drives a conformational change that joins ADP and P i . The gradient has a chemical component (ΔpH, acidic outside) and an electrical one (ΔΨ, matrix negative).**
13. Oligomycin blocks ATP synthase, not the ETC. Why does oxygen consumption still fall?
    **Answer: Protons cannot return, so the gradient builds until back-pressure stalls the pumps; electron flow stops with them. This is respiratory control, and it is why ETC inhibitors and ATP synthase inhibitors give identical arrows.**
14. An agent increases ETC function and oxygen consumption but decreases ATP. What class is it, what is the mechanism, and what is the clinical consequence?
    **Answer: An uncoupler. It makes the inner membrane permeable to H + , so no gradient forms and no back-pressure exists — the chain runs unchecked and the energy leaves as heat. Consequence: hyperthermia. Examples: 2,4-DNP, salicylate overdose, thermogenin (physiological).**
15. A patient is found unconscious after eating improperly processed cassava. Which complex is inhibited, at which iron oxidation state, and what is the antidote logic?
    **Answer: Cyanide inhibits Complex IV at the Fe 3+ of cytochrome a 3 . Because that binding cannot be competed off, amyl nitrite is given to convert hemoglobin to methemoglobin (Fe 3+ ), which sequesters cyanide; thiosulfate then converts it to thiocyanate for excretion. Contrast CO, which binds Fe 2+ non-covalently and is treated with 100% or hyperbaric oxygen.**

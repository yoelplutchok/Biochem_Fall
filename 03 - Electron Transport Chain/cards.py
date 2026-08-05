# -*- coding: utf-8 -*-
"""Learn deck — BIOCHEM L06, Electron Transport Chain (Bagh Shilpika, MBBS MD).

Built from the reviewed .knowledge.md extraction. The lecture deck's own figures
were not available, so the three diagrams that carry the most weight (chain layout,
redox ladder, proton circuit) are drawn here as inline SVG.
"""

# ---------------------------------------------------------------- diagrams

SVG_CHAIN = """<div class="fig"><svg viewBox="0 0 800 340" xmlns="http://www.w3.org/2000/svg">
<rect x="0" y="0" width="800" height="340" fill="var(--figbg)"/>
<text x="14" y="24" font-size="12" font-weight="700" fill="var(--svd)">INTERMEMBRANE SPACE &#8212; low pH, high [H&#8314;], outside (+)</text>
<rect x="0" y="110" width="800" height="120" fill="var(--sv1)" stroke="var(--svl)" stroke-width="1.2"/>
<text x="14" y="330" font-size="12" font-weight="700" fill="var(--svd)">MATRIX &#8212; high pH, low [H&#8314;], inside (&#8722;)</text>

<rect x="42" y="98" width="96" height="144" rx="10" fill="var(--sv2)" stroke="var(--svl)" stroke-width="1.5"/>
<text x="90" y="160" font-size="17" font-weight="700" text-anchor="middle" fill="var(--svt)">I</text>
<text x="90" y="180" font-size="10.5" text-anchor="middle" fill="var(--svd)">FMN</text>
<text x="90" y="194" font-size="10.5" text-anchor="middle" fill="var(--svd)">7 Fe&#8211;S</text>

<rect x="168" y="150" width="86" height="92" rx="10" fill="var(--sv3)" stroke="var(--svl)" stroke-width="1.5"/>
<text x="211" y="188" font-size="17" font-weight="700" text-anchor="middle" fill="var(--svt)">II</text>
<text x="211" y="206" font-size="10.5" text-anchor="middle" fill="var(--svd)">FAD</text>
<text x="211" y="220" font-size="10.5" text-anchor="middle" fill="var(--svd)">2 Fe&#8211;S</text>

<ellipse cx="300" cy="170" rx="30" ry="20" fill="var(--sv4)" stroke="var(--svl)" stroke-width="1.5"/>
<text x="300" y="175" font-size="13" font-weight="700" text-anchor="middle" fill="var(--svt)">CoQ</text>

<rect x="348" y="98" width="96" height="144" rx="10" fill="var(--sv2)" stroke="var(--svl)" stroke-width="1.5"/>
<text x="396" y="160" font-size="17" font-weight="700" text-anchor="middle" fill="var(--svt)">III</text>
<text x="396" y="180" font-size="10.5" text-anchor="middle" fill="var(--svd)">cyt b, c&#8321;</text>
<text x="396" y="194" font-size="10.5" text-anchor="middle" fill="var(--svd)">1 Fe&#8211;S</text>

<circle cx="482" cy="88" r="21" fill="var(--sv4)" stroke="var(--svl)" stroke-width="1.5"/>
<text x="482" y="93" font-size="12" font-weight="700" text-anchor="middle" fill="var(--svt)">c</text>

<rect x="520" y="98" width="96" height="144" rx="10" fill="var(--sv2)" stroke="var(--svl)" stroke-width="1.5"/>
<text x="568" y="160" font-size="17" font-weight="700" text-anchor="middle" fill="var(--svt)">IV</text>
<text x="568" y="180" font-size="10.5" text-anchor="middle" fill="var(--svd)">cyt a&#183;a&#8323;</text>
<text x="568" y="194" font-size="10.5" text-anchor="middle" fill="var(--svd)">Cu</text>

<rect x="676" y="112" width="58" height="118" rx="8" fill="var(--sv2)" stroke="var(--svl)" stroke-width="1.5"/>
<circle cx="705" cy="256" r="26" fill="var(--sv2)" stroke="var(--svl)" stroke-width="1.5"/>
<text x="705" y="178" font-size="12" font-weight="700" text-anchor="middle" fill="var(--svt)">F&#8320;</text>
<text x="705" y="261" font-size="12" font-weight="700" text-anchor="middle" fill="var(--svt)">F&#8321;</text>
<text x="705" y="100" font-size="11" font-weight="700" text-anchor="middle" fill="var(--svd)">V</text>

<g stroke="var(--acc)" stroke-width="2.4" fill="none">
<path d="M90 96 L90 62"/><path d="M396 96 L396 62"/><path d="M568 96 L568 62"/>
</g>
<g fill="var(--acc)">
<path d="M90 50 l6 14 h-12 z"/><path d="M396 50 l6 14 h-12 z"/><path d="M568 50 l6 14 h-12 z"/>
</g>
<text x="90" y="44" font-size="12" font-weight="700" text-anchor="middle" fill="var(--acc)">H&#8314;</text>
<text x="396" y="44" font-size="12" font-weight="700" text-anchor="middle" fill="var(--acc)">H&#8314;</text>
<text x="568" y="44" font-size="12" font-weight="700" text-anchor="middle" fill="var(--acc)">H&#8314;</text>
<text x="211" y="128" font-size="12" font-weight="700" text-anchor="middle" fill="var(--warn)">no H&#8314;</text>

<path d="M705 62 L705 236" stroke="var(--acc2)" stroke-width="2.4" fill="none"/>
<path d="M705 248 l6 -14 h-12 z" fill="var(--acc2)"/>
<text x="705" y="52" font-size="12" font-weight="700" text-anchor="middle" fill="var(--acc2)">H&#8314;</text>
<text x="705" y="300" font-size="11.5" font-weight="700" text-anchor="middle" fill="var(--acc2)">ADP+Pi&#8594;ATP</text>

<g stroke="var(--svl)" stroke-width="1.6" fill="none" stroke-dasharray="4 3">
<path d="M138 170 L268 170"/><path d="M254 178 L272 172"/><path d="M330 170 L346 170"/>
<path d="M444 140 L462 100"/><path d="M502 100 L520 140"/>
</g>
<text x="90" y="268" font-size="11.5" text-anchor="middle" fill="var(--svd)">NADH</text>
<text x="211" y="268" font-size="11.5" text-anchor="middle" fill="var(--svd)">succinate</text>
<text x="568" y="268" font-size="11.5" text-anchor="middle" fill="var(--svd)">&#189;O&#8322;&#8594;H&#8322;O</text>
<text x="90" y="286" font-size="11" font-weight="700" text-anchor="middle" fill="var(--acc2)">ATP</text>
<text x="396" y="286" font-size="11" font-weight="700" text-anchor="middle" fill="var(--acc2)">ATP</text>
<text x="568" y="286" font-size="11" font-weight="700" text-anchor="middle" fill="var(--acc2)">ATP</text>
</svg></div>"""

SVG_LADDER = """<div class="fig"><svg viewBox="0 0 620 330" xmlns="http://www.w3.org/2000/svg">
<rect x="0" y="0" width="620" height="330" fill="var(--figbg)"/>
<line x1="120" y1="24" x2="120" y2="300" stroke="var(--svl)" stroke-width="1.5"/>
<text x="26" y="20" font-size="11.5" font-weight="700" fill="var(--svd)">E&#8320;&#8242; (V)</text>
<text x="150" y="20" font-size="11.5" font-weight="700" fill="var(--svd)">electrons flow DOWN the page &#8594; up the potential scale</text>

<g font-size="12.5" fill="var(--svt)">
<circle cx="120" cy="46" r="5" fill="var(--acc)"/><text x="88" y="51" text-anchor="end" fill="var(--svd)">&#8722;0.32</text><text x="138" y="51">NAD&#8314; / NADH</text>
<circle cx="120" cy="76" r="5" fill="var(--acc)"/><text x="88" y="81" text-anchor="end" fill="var(--svd)">&#8722;0.30</text><text x="138" y="81">FMN / FMNH&#8322; &#8212; Complex I</text>
<circle cx="120" cy="106" r="5" fill="var(--acc)"/><text x="88" y="111" text-anchor="end" fill="var(--svd)">&#8722;0.22</text><text x="138" y="111">FAD / FADH&#8322; &#8212; Complex II</text>
<circle cx="120" cy="142" r="5" fill="var(--warn)"/><text x="88" y="147" text-anchor="end" fill="var(--svd)">+0.07</text><text x="138" y="147">cytochrome b &#8212; the exception</text>
<circle cx="120" cy="172" r="5" fill="var(--acc)"/><text x="88" y="177" text-anchor="end" fill="var(--svd)">+0.10</text><text x="138" y="177">coenzyme Q</text>
<circle cx="120" cy="202" r="5" fill="var(--acc)"/><text x="88" y="207" text-anchor="end" fill="var(--svd)">+0.23</text><text x="138" y="207">cytochrome c&#8321;</text>
<circle cx="120" cy="228" r="5" fill="var(--acc)"/><text x="88" y="233" text-anchor="end" fill="var(--svd)">+0.25</text><text x="138" y="233">cytochrome c</text>
<circle cx="120" cy="254" r="5" fill="var(--acc)"/><text x="88" y="259" text-anchor="end" fill="var(--svd)">+0.29</text><text x="138" y="259">cytochrome a</text>
<circle cx="120" cy="292" r="6.5" fill="var(--acc2)"/><text x="88" y="297" text-anchor="end" fill="var(--svd)">+0.82</text><text x="138" y="297" font-weight="700">&#189;O&#8322; / H&#8322;O &#8212; the best acceptor</text>
</g>
<path d="M60 46 L60 286" stroke="var(--acc2)" stroke-width="2" fill="none"/>
<path d="M60 298 l5 -13 h-10 z" fill="var(--acc2)"/>
<text x="46" y="176" font-size="11.5" font-weight="700" fill="var(--acc2)" transform="rotate(-90 46 176)" text-anchor="middle">span 1.14 V</text>
</svg></div>"""

SVG_CIRCUIT = """<div class="fig"><svg viewBox="0 0 700 300" xmlns="http://www.w3.org/2000/svg">
<rect x="0" y="0" width="700" height="300" fill="var(--figbg)"/>
<rect x="60" y="60" width="580" height="180" rx="90" fill="none" stroke="var(--sv4)" stroke-width="22"/>
<text x="350" y="34" font-size="12.5" font-weight="700" text-anchor="middle" fill="var(--svd)">OUTSIDE (+) &#183; intermembrane space &#183; acidic</text>
<text x="350" y="160" font-size="12.5" font-weight="700" text-anchor="middle" fill="var(--svd)">INSIDE (&#8722;) &#183; matrix &#183; alkaline</text>
<text x="350" y="182" font-size="11.5" text-anchor="middle" fill="var(--svd)">the bilayer is impermeable to H&#8314;</text>

<rect x="330" y="42" width="230" height="36" rx="8" fill="var(--sv2)" stroke="var(--svl)" stroke-width="1.4"/>
<text x="445" y="65" font-size="12.5" font-weight="700" text-anchor="middle" fill="var(--svt)">respiratory chain &#183; I, III, IV</text>
<path d="M445 96 L445 84" stroke="var(--acc)" stroke-width="2.4"/>
<path d="M445 74 l5 13 h-10 z" fill="var(--acc)"/>
<text x="500" y="112" font-size="12" font-weight="700" fill="var(--acc)">H&#8314; pumped OUT</text>

<rect x="118" y="42" width="150" height="36" rx="8" fill="var(--sv2)" stroke="var(--svl)" stroke-width="1.4"/>
<text x="193" y="65" font-size="12.5" font-weight="700" text-anchor="middle" fill="var(--svt)">F&#8320;F&#8321; ATP synthase</text>
<path d="M193 78 L193 92" stroke="var(--acc2)" stroke-width="2.4"/>
<path d="M193 102 l5 -13 h-10 z" fill="var(--acc2)"/>
<text x="90" y="112" font-size="12" font-weight="700" fill="var(--acc2)">H&#8314; back IN</text>
<text x="193" y="132" font-size="12" font-weight="700" text-anchor="middle" fill="var(--acc2)">ADP + Pi &#8594; ATP</text>

<text x="350" y="222" font-size="12.5" font-weight="700" text-anchor="middle" fill="var(--svt)">gradient = &#916;pH  +  electrical potential &#916;&#936;</text>
<text x="350" y="266" font-size="12" text-anchor="middle" fill="var(--warn)">oligomycin blocks F&#8320; &#183; uncouplers punch a second hole straight through the bilayer</text>
</svg></div>"""


# ---------------------------------------------------------------- cards

CARDS = [

# ================================================== 1. Biological oxidation
dict(sec="Biological oxidation",
     q="In one sentence, what does the electron transport chain actually do?",
     a="""<p>Electrons <k>fall down a redox gradient</k> from reduced coenzymes to oxygen, and
the energy released on the way down is captured as a <k>proton gradient</k>, which is then
cashed in for <k>ATP</k>.</p>""" + SVG_CHAIN + """
<p class=tip>Hold onto this shape. Every complex is a step on that fall, and every poison in
the second half of the lecture is a way of interrupting it at one specific step.</p>""",
     img=["slide19_1.jpg"]),

dict(sec="Biological oxidation",
     q="How do catabolism and anabolism relate through ATP &mdash; and what is NADH telling you?",
     a="""<div class=chain>catabolism breaks down foodstuff &#8594; yields large amounts of ATP &#8594; anabolism consumes it</div>
<p><b>NADH</b> is an <k>indirect reflection of the ATP state of the body</k>. A high level of
reduced coenzyme in the matrix means a good energy state.</p>
<p><b>NADPH</b> is <k>not</k> a reflection of ATP &mdash; it is the hydrogen source for anabolism.</p>
<p class=tip>The extra <b>P</b> in NAD<b>P</b>H is for <b>P</b>roduction &mdash; building things, not
powering them. This distinction shows up once here and never gets repeated, which is exactly
why it gets missed.</p>"""),

dict(sec="Biological oxidation",
     q="Anabolism needs carbon, hydrogen and energy. What supplies each?",
     a="""<table class=t>
<tr><th>Requirement</th><th>Supplied by</th></tr>
<tr><td>Energy</td><td><k>ATP</k> &mdash; the universal requirement</td></tr>
<tr><td>Carbon</td><td><k>acetyl-CoA</k></td></tr>
<tr><td>Hydrogen</td><td><k>NADPH</k></td></tr>
<tr><td>Hormonal drive</td><td><k>insulin</k>, the major anabolic hormone</td></tr>
</table>
<p class=tip>She flagged that exceptions to the insulin rule exist and are taught later &mdash;
so don't over-generalise "insulin = anabolic" into an absolute.</p>"""),

dict(sec="Biological oxidation",
     q="What is oxidation in general chemistry, and how is that definition <b>narrowed</b> inside the body?",
     a="""<p>Generally, oxidation is <b>gain of oxygen</b> or <b>loss of hydrogen</b>.</p>
<p>In the body only the second half applies: <k>biological oxidation is loss of hydrogen</k>,
and the hydrogen leaves as <k>2H&#8314; + 2e&#8315;</k>.</p>
<div class=chain>biological oxidation &#8594; loses reducing equivalents &#8594; exergonic &#8594; releases Gibbs free energy &#8594; trapped stepwise as ATP</div>
<p class=tip>This is the definitional spine of the lecture &mdash; she states it about five separate
times. Every later idea is a consequence of it.</p>"""),

dict(sec="Biological oxidation",
     q="What is a <b>reducing equivalent</b>?",
     a="""<p>One <k>proton plus one electron</k>. In practice the lecture always speaks in pairs:
<k>2H&#8314; + 2e&#8315;</k>.</p>
<p>So biological oxidation can be restated as <b>loss of reducing equivalents</b>.</p>
<p class=tip>The phrase is used as a unit of currency for the rest of the lecture. When she asks
"what is the acceptor of reducing equivalents?" she is asking "what takes the electrons?"</p>"""),

dict(sec="Biological oxidation",
     q="In metabolism, what gets <b>oxidised</b> and what gets <b>reduced</b>?",
     a="""<p>The <k>substrates</k> oxidised are the macronutrients: carbohydrate, lipid, protein.<br>
The <k>coenzymes</k> are what get reduced &mdash; and those coenzymes come from micronutrients.</p>
<table class=t>
<tr><th>Vitamin</th><th>Becomes</th></tr>
<tr><td>B2 &mdash; riboflavin</td><td><k>FAD</k></td></tr>
<tr><td>B3 &mdash; niacin</td><td><k>NAD&#8314;</k> and NADP&#8314;</td></tr>
</table>
<div class=chain>AH&#8322; + NAD&#8314;/FAD &#8594; A + NADH+H&#8314; / FADH&#8322;</div>
<p class=tip>Macronutrients are burned; micronutrients are the vehicles that carry the electrons
away. That is the whole reason a vitamin deficiency can present as an energy problem.</p>"""),

dict(sec="Biological oxidation",
     q="Which enzyme class catalyses biological oxidation, and why is it named that way?",
     a="""<p>Class <k>oxidoreductase</k>, subclass <k>dehydrogenase</k>.</p>
<p>Named as a pair because in every one of these reactions <b>one intermediate is oxidised while
the other is reduced</b> &mdash; the two always happen together.</p>
<p class=tip>Subclass "dehydrogenase" is literally "removes hydrogen", which is the biological
definition of oxidation. The names are consistent, not arbitrary.</p>"""),

dict(sec="Biological oxidation",
     q="After a round of oxidation, is there more NADH or more FADH&#8322; in the matrix &mdash; and why does it matter?",
     a="""<p>More <k>NADH+H&#8314;</k>, because <b>NAD&#8314; is a greater acceptor of reducing
equivalents than FAD</b>.</p>
<p class=tip>This is the reason the NAD-linked pathway dominates the ATP yield of the cell. Keep it
in mind when you meet the P:O ratios &mdash; the higher-yielding route is also the busier one.</p>"""),

# ================================================== 2. Redox potential
dict(sec="Redox &amp; free energy",
     q="Define a redox reaction, and name the roles of the two partners.",
     a="""<p>Transfer of electrons from a <k>donor (reductant)</k> to an <k>acceptor (oxidant)</k>.</p>
<table class=t>
<tr><th>Role</th><th>What happens to it</th></tr>
<tr><td>Reductant / donor</td><td>gets <k>oxidised</k></td></tr>
<tr><td>Oxidant / acceptor</td><td>gets <k>reduced</k></td></tr>
</table>
<p class=tip>The names read backwards on purpose: the reduct<b>ant</b> is the one that reduc<b>es</b>
something else, so it is itself oxidised.</p>"""),

dict(sec="Redox &amp; free energy",
     q="Work through the ethanol example: <b>NAD&#8314; + ethanol &#8594; NADH + H&#8314; + acetaldehyde</b>. Who is who?",
     a="""<p><k>Ethanol</k> is the reductant (donor). <k>NAD&#8314;</k> is the oxidant (acceptor).</p>
<p>Oxidation half-reaction: NADH + H&#8314; &#8652; NAD&#8314; + 2H&#8314; + 2e&#8315;<br>
Reduction half-reaction: acetaldehyde + 2H&#8314; + 2e&#8315; &#8652; ethanol</p>
<p>The two <b>redox pairs</b> are <k>NADH&#8211;NAD&#8314;</k> and <k>acetaldehyde&#8211;ethanol</k>.</p>
<p class=tip>Read left to right as written and ethanol loses hydrogen &mdash; loss of hydrogen is
biological oxidation, so ethanol is the one being oxidised. You never have to memorise which is
which; you can read it off.</p>"""),

dict(sec="Redox &amp; free energy",
     q="What is <b>E&#8320;&#8242;</b>, and what does a low value mean?",
     a="""<p>The standard redox potential: a measure of a redox pair's <k>affinity for electrons</k>
under standard conditions (1 M oxidant and reductant, pH 7).</p>
<table class=t>
<tr><th>E&#8320;&#8242;</th><th>Means</th><th>Position in the chain</th></tr>
<tr><td>Low (negative)</td><td><k>low</k> affinity for electrons</td><td>the donor end &mdash; NAD&#8314;/NADH at &#8722;0.32</td></tr>
<tr><td>High (positive)</td><td><k>high</k> affinity for electrons</td><td>the acceptor end &mdash; O&#8322; at +0.82</td></tr>
</table>
<p class=tip>This one inverts under pressure. High potential = high <b>pull</b>. Oxygen has the
strongest pull and therefore sits at the very end.</p>"""),

dict(sec="Redox &amp; free energy",
     q="Which way do electrons move between two carriers, and what is <b>&#916;E&#8320;&#8242;</b>?",
     a="""<p>Electrons move from <k>lower E&#8320;&#8242; to higher E&#8320;&#8242;</k> &mdash;
"electrons flow to a more positive standard reduction potential."</p>
<div class=chain>&#916;E&#8320;&#8242; = E&#8320;&#8242;(acceptor) &#8722; E&#8320;&#8242;(donor)</div>
<p>The acceptor's potential is <k>always higher</k> than the donor's, otherwise the electrons would
not move forward at all.</p>
<p class=tip>She restates "acceptor minus donor" at least seven times &mdash; it is the single most
repeated line in the lecture, and it is the rule that generates the order of the complexes, the
E&#8320;&#8242; table, and why oxygen is last.</p>"""),

dict(sec="Redox &amp; free energy",
     q="Write the equation linking redox potential to free energy, and define every symbol.",
     a="""<div class=chain>&#916;G&#8320;&#8242; = &#8722;nF&#916;E&#8320;&#8242;</div>
<table class=t>
<tr><th>Symbol</th><th>Meaning</th></tr>
<tr><td>&#916;G&#8320;&#8242;</td><td>standard free energy change, kcal</td></tr>
<tr><td>n</td><td>number of electrons transferred</td></tr>
<tr><td>F</td><td>Faraday constant = <k>23.06 kcal/V</k></td></tr>
<tr><td>&#916;E&#8320;&#8242;</td><td>standard redox potential change, volts</td></tr>
</table>
<p>Corollary: the <b>more positive</b> the &#916;E&#8320;&#8242;, the <b>more negative</b> the
&#916;G&#8320;&#8242;.</p>
<p class=tip>The minus sign in the formula <i>is</i> the flip. A spontaneous reaction has negative
&#916;G and therefore positive &#916;E&#8320;&#8242; &mdash; if you ever lose track, rebuild it from
the minus sign rather than guessing.</p>"""),

dict(sec="Redox &amp; free energy",
     q="Calculate the free energy available from oxidising one NADH, and compare it with the actual ATP yield.",
     a="""<p>Overall: NADH + H&#8314; + &#189;O&#8322; &#8594; NAD&#8314; + H&#8322;O. The acceptor is
<b>oxygen</b>.</p>
<table class=t>
<tr><td>E&#8320;&#8242; donor (NAD&#8314;/NADH)</td><td>&#8722;0.32 V</td></tr>
<tr><td>E&#8320;&#8242; acceptor (&#189;O&#8322;/H&#8322;O)</td><td>+0.82 V</td></tr>
<tr><td>&#916;E&#8320;&#8242;</td><td>+0.82 &#8722; (&#8722;0.32) = <k>+1.14 V</k></td></tr>
<tr><td>&#916;G&#8320;&#8242;</td><td>&#8722;(2)(23.06)(1.14) = <k>&#8722;52.6 kcal</k></td></tr>
<tr><td>&#916;G&#8320;&#8242; of ATP</td><td>&#8722;7.3 kcal/mol</td></tr>
<tr><td>Theoretical yield</td><td>52.6 / 7.3 &#8776; <k>7 ATP</k> at 100% efficiency</td></tr>
<tr><td>Actual yield</td><td><k>3 ATP</k> &#8594; efficiency &#8776; 42%</td></tr>
</table>
<p class=tip>Her framing: "look at the equation, see who is the acceptor of reducing equivalent."
Once you identify the acceptor, the rest is arithmetic. The gap between 7 and 3 <i>is</i> the
efficiency of the chain &mdash; the rest leaves as heat.</p>"""),

dict(sec="Redox &amp; free energy",
     q="Recite the redox potential ladder from NAD&#8314; to oxygen.",
     a=SVG_LADDER + """
<p>Total span &#8722;0.32 &#8594; +0.82 = <k>1.14 V</k>, which the deck rounds to "a span of 1.1 volt."</p>
<p class=tip>The pattern is easier than the numbers: <b>every flavin/nicotinamide carrier is
negative, every cytochrome is positive, and oxygen is off the scale at +0.82.</b></p>
<p class=warn>Cytochrome b at <b>+0.07</b> sits <i>below</i> coenzyme Q at <b>+0.10</b>, yet
electrons flow CoQ &#8594; cyt b. That uphill step inside Complex III is real (it is driven by the
membrane electric field, not the redox gradient). For this exam, still answer <b>"arranged in order
of increasing redox potential"</b> &mdash; but know cytochrome b is the exception if she pushes.</p>"""),

dict(sec="Redox &amp; free energy",
     q="Summarise Objective 1 in four statements.",
     a="""<p><k>1.</k> Electron-transfer reactions are a source of free energy.<br>
<k>2.</k> Low redox potential = low affinity for electrons.<br>
<k>3.</k> The <b>difference</b> in redox potential between acceptor and donor determines the
magnitude of &#916;G.<br>
<k>4.</k> Electron transfers can be linked in series in order of increasing redox potential.</p>
<p class=tip>The deck's own analogy for point 4 is an <b>electrical circuit</b> &mdash; components
wired in series, each dropping a little voltage, with the drop doing work.</p>"""),

# ================================================== 3. Mitochondrion
dict(sec="The mitochondrion",
     q="Describe the compartments of the mitochondrion, and say what happens in each.",
     a="""<table class=t>
<tr><th>Part</th><th>Property / job</th></tr>
<tr><td>Outer membrane</td><td><k>permeable</k></td></tr>
<tr><td>Intermembrane space</td><td>where H&#8314; accumulates; home of cytochrome c</td></tr>
<tr><td>Inner membrane</td><td><k>semipermeable</k>, folded into <k>cristae</k>; site of electron transport <b>and</b> ATP synthesis</td></tr>
<tr><td>Matrix</td><td>soluble; where <k>reducing equivalents are generated</k></td></tr>
</table>
<p>The chain sits oriented <b>toward the matrix side</b> of the inner membrane, with the
phosphorylating complexes projecting into the matrix.</p>
<p class=tip>Two membranes with different permeabilities is the entire physical basis of
chemiosmosis. If the inner membrane leaked H&#8314; the way the outer one does, no gradient could
form &mdash; which is exactly what an uncoupler produces.</p>""",
     img=["slide11_1.jpg", "slide17_1.jpg"]),

dict(sec="The mitochondrion",
     q="What do you need to know about mitochondrial DNA?",
     a="""<p>Mitochondria have their own <b>genome and their own ribosomes</b>.</p>
<p>mtDNA is <k>maternally inherited</k>, and in humans it encodes <k>13 proteins of the ETC</k>.</p>
<p class=tip>13 is also the subunit count of Complex IV &mdash; a coincidence, but a useful one to
hang both numbers on.</p>"""),

dict(sec="The mitochondrion",
     q="Why do reduced coenzymes end up concentrated in the matrix in the first place?",
     a="""<p>Because the <k>citric acid cycle</k> &mdash; the <b>common</b> pathway for complete
oxidation of carbohydrate, lipid and protein &mdash; operates <k>in the matrix</k>.</p>
<div class=chain>fat / carbohydrate / protein &#8594; acetyl-CoA &#8594; citric acid cycle &#8594; 2H &#8594; respiratory chain</div>
<p>Fatty acids also feed reducing equivalents in directly via <b>&#946;-oxidation</b>.</p>
<p class=tip>The chain is deliberately placed in the wall of the compartment where its fuel is
made. Substrate and machinery are one diffusion step apart.</p>""",
     img=["slide12_1.jpg"]),

dict(sec="The mitochondrion",
     q="Reducing equivalents made in the <b>cytosol</b> can't cross the inner membrane. How do they get in?",
     a="""<p>By one of two shuttles:</p>
<p><k>1. Glycerophosphate shuttle</k><br><k>2. Malate&#8211;aspartate shuttle</k></p>
<p class=tip>Named only here &mdash; she explicitly defers the detail to the glycolysis lecture. For
now, all that matters is that a shuttle is <i>required</i>, because the inner membrane is
semipermeable.</p>"""),

dict(sec="The mitochondrion",
     q="Besides NADH and succinate, what else feeds electrons into coenzyme Q?",
     a="""<table class=t>
<tr><th>Feeder</th><th>Route into Q</th></tr>
<tr><td>Glycerol 3-phosphate</td><td>its own Fp(FAD)FeS</td></tr>
<tr><td>Choline</td><td>FAD/FeS-linked, direct to Q</td></tr>
<tr><td>Acyl-CoA (&#946;-oxidation), sarcosine, dimethylglycine</td><td><k>ETF</k> &mdash; electron-transferring flavoprotein</td></tr>
</table>
<p>NAD-linked feeders include pyruvate, &#945;-ketoglutarate, proline, 3-hydroxyacyl-CoA,
3-hydroxybutyrate, glutamate, malate and isocitrate.</p>
<p class=warn>The FADH&#8322; from fatty-acid &#946;-oxidation does <b>not</b> enter through
Complex II &mdash; it enters via <k>ETF</k>. Assuming "all FADH&#8322; goes through Complex II" will
cost you later, in the fatty-acid oxidation lecture.</p>""",
     img=["slide18_1.jpg"]),

# ================================================== 4. The chain
dict(sec="The chain &amp; its carriers",
     q="Lay out the electron transport chain: how many parts, where, in what order?",
     a="""<p>In the <k>inner mitochondrial membrane</k>: <k>5 fixed complexes</k> and
<k>2 mobile carriers</k>, spanning <k>1.1 volt</k>.</p>
<div class=chain>NADH &#8594; I &#8594; CoQ &#8592; II &#8592; succinate<br>CoQ &#8594; III &#8594; cyt c &#8594; IV &#8594; &#189;O&#8322; &#8594; H&#8322;O</div>
<p>Complexes I&#8211;IV run in order of increasing redox potential. Each complex hands off to a
relatively smaller mobile carrier. Flow is <k>unidirectional &mdash; no backward flow</k>.</p>
<p><b>Complex V is the ATP synthase and is <k>not</k> a coupling site.</b></p>
<p class=tip>Coupling site = a complex that pumps protons and therefore yields ATP. That is
<b>I, III and IV</b>. Complex II is the odd one out; Complex V is the machine, not a pump.</p>""",
     img=["slide19_1.jpg"]),

dict(sec="The chain &amp; its carriers",
     q="Why are the complexes arranged in that particular order, and why is oxygen last?",
     a="""<p>Because redox potential reflects <b>affinity for electrons</b>, and the acceptor's
potential must exceed the donor's for electrons to move forward. Arrange the components by
increasing E&#8320;&#8242; and you have automatically arranged them in flow order.</p>
<p><k>Oxygen has the highest reduction potential (+0.82 V)</k> &mdash; it is the best and therefore
the final electron acceptor.</p>
<p class=tip>This also tells you what a blockage does: everything <b>upstream</b> of a block stays
<b>reduced</b> (nothing will take its electrons), everything <b>downstream</b> stays
<b>oxidised</b> (nothing is delivering any).</p>"""),

dict(sec="The chain &amp; its carriers",
     q="Describe <b>coenzyme Q</b> &mdash; what it is, where it sits, what it accepts.",
     a="""<p>A mobile carrier and the <k>only lipid-soluble</k> component of the chain. An
isoprenoid unit, and an <k>intermediate of cholesterol synthesis</k>.</p>
<p>It accepts hydrogen atoms from <b>FMNH&#8322; of Complex I</b> and from <b>FADH&#8322; of
Complex II</b>, and sits between I/II and III.</p>
<p class=tip>Being lipid-soluble is what lets it live <i>inside</i> the membrane and shuttle
laterally between complexes. It is also the collection point &mdash; every substrate route in the
lecture converges on Q.</p>"""),

dict(sec="The chain &amp; its carriers",
     q="Describe <b>cytochrome c</b> &mdash; what it is, where it sits, what it donates to.",
     a="""<p>A mobile carrier and a <k>water-soluble</k> cytochrome &mdash; a soluble protein of the
<k>intermembrane space</k>. It sits between Complex III and Complex IV, and donates electrons to
the <b>copper ions of Complex IV</b>.</p>
<p class=tip>Q is lipid and lives in the membrane; c is water and lives in the fluid space. Q is
upstream, c is downstream. Get those two axes right and you can't swap them.</p>"""),

dict(sec="The chain &amp; its carriers",
     q="Contrast the two mobile carriers directly.",
     a="""<table class=t>
<tr><th></th><th>Coenzyme Q</th><th>Cytochrome c</th></tr>
<tr><td>Solubility</td><td><k>lipid</k>-soluble</td><td><k>water</k>-soluble</td></tr>
<tr><td>Lives</td><td>within the membrane</td><td>intermembrane space</td></tr>
<tr><td>Position</td><td>between I/II and III</td><td>between III and IV</td></tr>
<tr><td>Chemistry</td><td>isoprenoid quinone; cholesterol-synthesis intermediate</td><td>hemeprotein, Fe&#178;&#8314;/Fe&#179;&#8314;</td></tr>
</table>
<p class=tip>Q is a <b>q</b>uinone &mdash; greasy, so it dissolves in fat. Both letters and both
positions run in order: <b>Q before c</b>.</p>"""),

dict(sec="The chain &amp; its carriers",
     q="What is the other name for a cytochrome, and what does its iron do?",
     a="""<p>Cytochromes a, b and c are <k>hemeproteins</k> &mdash; "the other name for cytochrome is
hemeprotein, don't forget that."</p>
<p>The iron, both in cytochromes and in Fe&#8211;S centres, cycles between <k>Fe&#178;&#8314; and
Fe&#179;&#8314;</k>.</p>
<p class=tip>That cycling is the whole mechanism: accepting an electron reduces Fe&#179;&#8314; to
Fe&#178;&#8314;, passing it on re-oxidises it. It is also why the two Complex IV poisons are
distinguished by <i>which</i> oxidation state they bind.</p>"""),

# ================================================== 5. The complexes
dict(sec="The four complexes",
     q="<b>Complex I</b> &mdash; names, composition, reaction, function.",
     a="""<p>Names: NADH dehydrogenase complex; <k>NADH:Q oxidoreductase</k>.</p>
<table class=t>
<tr><td>Size</td><td>the <k>largest</k> complex, &gt;25 polypeptides</td></tr>
<tr><td>Prosthetic group</td><td><k>FMN</k></td></tr>
<tr><td>Iron&#8211;sulfur</td><td><k>7 Fe&#8211;S centres</k></td></tr>
<tr><td>Reaction</td><td>NADH + H&#8314; + CoQ &#8594; CoQH&#8322; + NAD&#8314;</td></tr>
<tr><td>Coupling site?</td><td><k>Yes</k> &mdash; ATP is made here</td></tr>
</table>
<p><b>Function &mdash; the examinable statement:</b> <k>passes reducing equivalents from NADH to
CoQ</k>.</p>
<p>Electron path: NADH &#8594; FMNH&#8322; &#8594; a succession of Fe&#8211;S centres &#8594; CoQH&#8322;.</p>
<p class=tip>She explicitly deprioritised the internal Fe&#8211;S mechanism &mdash; "we are not going
into details, all you need to know is the function." Learn the one-line function statement
verbatim; skip the internals.</p>
<p class=tip>If you want the proton bookkeeping from the figure: reducing FMN takes one proton from
the matrix, transfer to the first Fe&#8211;S centre releases <b>2H&#8314;</b> into the intermembrane
space, and reducing UQ to UQH&#8322; takes up <b>2 more</b> from the matrix. One or two additional
protons cross by a mechanism that is not understood.</p>""",
     img=["slide20_1.jpg"]),

dict(sec="The four complexes",
     q="<b>Complex II</b> &mdash; names, composition, function, and the one fact she repeated six times.",
     a="""<p>Names: FADH&#8322; dehydrogenase complex; FADH&#8322;:Q oxidoreductase;
<k>succinate dehydrogenase</k>.</p>
<table class=t>
<tr><td>Size</td><td>4 polypeptides &mdash; the smallest</td></tr>
<tr><td>Prosthetic group</td><td><k>FAD</k>, <b>covalently</b> bound</td></tr>
<tr><td>Iron&#8211;sulfur</td><td><k>2 Fe&#8211;S centres</k></td></tr>
<tr><td>Substrate</td><td><k>succinate &#8594; fumarate</k>, electrons to ubiquinone</td></tr>
<tr><td>Protons pumped</td><td><k>none</k></td></tr>
</table>
<p class=warn><k>Complex II is NOT a coupling site. It does not synthesise ATP.</k> Substrates
entering here <b>bypass Complex I</b>, which is why their P:O ratio is 2 rather than 3.</p>
<p class=tip>It is also the only enzyme that belongs to both the citric acid cycle and the
respiratory chain &mdash; succinate dehydrogenase is physically part of both.</p>"""),

dict(sec="The four complexes",
     q="<b>Complex III</b> &mdash; name, composition, reaction, function.",
     a="""<p>Name: <k>CoQH&#8322;:cytochrome c oxidoreductase</k>.</p>
<table class=t>
<tr><td>Size</td><td>6 polypeptides</td></tr>
<tr><td>Cytochromes</td><td><k>cytochrome b and cytochrome c&#8321;</k> (bc&#8321;)</td></tr>
<tr><td>Cytochrome b hemes</td><td>2 &mdash; b562 and b566</td></tr>
<tr><td>Iron&#8211;sulfur</td><td>1 Fe&#8211;S centre</td></tr>
<tr><td>Reaction</td><td>CoQH&#8322; + cyt c(Fe&#179;&#8314;) &#8594; CoQ + cyt c(Fe&#178;&#8314;)</td></tr>
<tr><td>H&#8314; translocated</td><td>2H&#8314;</td></tr>
<tr><td>Coupling site?</td><td><k>Yes</k></td></tr>
</table>
<p><b>Function:</b> <k>passes reducing equivalents from CoQH&#8322; to cytochrome c</k>.</p>
<p class=warn>Phrase the inhibition outcome carefully: if Complex III is blocked,
<k>CoQH&#8322; cannot be oxidised</k>. She specifically warned about the direction &mdash; upstream
of a block, things stay <i>reduced</i>.</p>"""),

dict(sec="The four complexes",
     q="<b>Complex IV</b> &mdash; names, composition, reaction, function.",
     a="""<p>Names: <k>cytochrome c:O&#8322; oxidoreductase</k>; <k>cytochrome c oxidase</k>.</p>
<table class=t>
<tr><td>Size</td><td>13 polypeptides</td></tr>
<tr><td>Metals</td><td>a <k>copper</k>- and heme(Fe)-containing protein</td></tr>
<tr><td>Cytochromes</td><td><k>cytochrome a and a&#8323;</k>, each with one Cu atom</td></tr>
<tr><td>Reaction</td><td>cyt c(Fe&#178;&#8314;) + &#189;O&#8322; &#8594; cyt c(Fe&#179;&#8314;) + H&#8322;O</td></tr>
<tr><td>H&#8314; translocated</td><td>2H&#8314;</td></tr>
<tr><td>Coupling site?</td><td><k>Yes</k></td></tr>
</table>
<p><b>Function:</b> <k>passes reducing equivalents from cytochrome c to oxygen, reducing it to
water</k>.</p>
<p class=warn>This is the <k>only complex requiring copper</k>, so <b>copper deficiency impairs
Complex IV</b>. She said this twice and volunteered the cross-link: copper is also required by
<b>lysyl oxidase</b> in collagen cross-linking &mdash; "no lysyl oxidase and copper, and no copper
and Complex IV."</p>"""),

dict(sec="The four complexes",
     q="<b>Complex V</b> &mdash; what is it, what are its parts, and why isn't it a coupling site?",
     a="""<p>The <k>ATP synthase</k>, also called the <k>F&#8320;F&#8321; complex</k>.</p>
<table class=t>
<tr><td><k>F&#8320;</k></td><td>the membrane-embedded proton <b>channel</b> &mdash; oligomycin's target</td></tr>
<tr><td><k>F&#8321;</k></td><td>the matrix-side catalytic <b>knob</b></td></tr>
</table>
<p>Protons pass through the channel; as it moves it changes conformation, and that conformational
change causes Pi to bind to ADP.</p>
<p class=warn>Complex V is <k>not a coupling site</k> &mdash; it does not pump protons outward, it
lets them back in. Both II and V fail to be coupling sites, for opposite reasons:
<b>II can't (too little energy released), V won't (it runs them the other way to make ATP).</b></p>
<p class=tip>F-<b>O</b> = the <b>O</b>pening in the membrane. That mnemonic also tells you where
oligomycin binds.</p>"""),

dict(sec="The four complexes",
     q="Build the composition table for all four complexes side by side.",
     a="""<table class=t>
<tr><th></th><th>I</th><th>II</th><th>III</th><th>IV</th></tr>
<tr><td>Flavin / cytochromes</td><td><k>FMN</k></td><td><k>FAD</k></td><td><k>b, c&#8321;</k></td><td><k>a, a&#8323;</k></td></tr>
<tr><td>Fe&#8211;S centres</td><td>7</td><td>2</td><td>1</td><td>0</td></tr>
<tr><td>Polypeptides</td><td>&gt;25</td><td>4</td><td>6</td><td>13</td></tr>
<tr><td>Copper</td><td>&#8212;</td><td>&#8212;</td><td>&#8212;</td><td><k>yes</k></td></tr>
<tr><td>Coupling site</td><td><k>yes</k></td><td><k>no</k></td><td><k>yes</k></td><td><k>yes</k></td></tr>
</table>
<p class=tip>Fe&#8211;S runs <b>7, 2, 1, 0</b> &mdash; a clean descending sequence. Copper appears
only at IV, at the very end, where oxygen is.</p>"""),

dict(sec="The four complexes",
     q="She warned that <b>I and II look alike</b>. What actually separates them?",
     a="""<table class=t>
<tr><th>Complex I</th><th>Complex II</th></tr>
<tr><td><k>FMN</k></td><td><k>FAD</k></td></tr>
<tr><td>7 Fe&#8211;S</td><td>2 Fe&#8211;S</td></tr>
<tr><td>pumps H&#8314;, <k>is</k> a coupling site</td><td>pumps nothing, <k>not</k> a coupling site</td></tr>
<tr><td>takes electrons from NADH</td><td>takes electrons from succinate</td></tr>
</table>
<p class=tip><b>F-M-N</b> for the <b>F</b>irst complex. Or: I goes with <b>N</b>ADH (both have an
N); II goes with succin<b>A</b>te and F<b>A</b>D.</p>"""),

dict(sec="The four complexes",
     q="She warned that <b>III and IV look alike</b>. What actually separates them?",
     a="""<table class=t>
<tr><th>Complex III</th><th>Complex IV</th></tr>
<tr><td>cytochromes <k>b and c&#8321;</k> (bc&#8321;)</td><td>cytochromes <k>a and a&#8323;</k> (aa&#8323;)</td></tr>
<tr><td>no copper</td><td><k>copper</k></td></tr>
<tr><td>hands off to cytochrome c</td><td>hands off to <k>oxygen</k></td></tr>
</table>
<p class=tip>The cytochrome alphabet runs backwards down the chain &mdash; <b>b, c&#8321;, c, then a,
a&#8323;</b> &mdash; and <b>a</b> is last because <b>a</b> is for <b>a</b>ir.</p>"""),

dict(sec="The four complexes",
     q="Where does the chain leak <b>reactive oxygen species</b>, and which ones?",
     a="""<p><k>Superoxide is produced during normal ETC operation</k> &mdash; normal metabolism is
itself a source of ROS. It leaks from:</p>
<p><k>FMN in Complex I</k><br><k>Ubiquinone in Complex III</k></p>
<p>The named species are <b>O&#8322;&#8226;&#8315; (superoxide), H&#8322;O&#8322;, and OH&#8226;</b>.
Other triggers: radiation, inflammation, high pO&#8322;, smog, chemicals and drugs, reperfusion
injury, aging.</p>
<p class=tip>She introduced this only &mdash; the full treatment is deferred to the hexose
monophosphate shunt lecture. Know the two leak points and the three species.</p>""",
     img=["slide30_1.jpg"]),

# ================================================== 6. ATP synthesis
dict(sec="ATP synthesis",
     q="Define <b>oxidative phosphorylation</b>, and say what three things it requires.",
     a="""<p>Transfer of electrons from reduced coenzymes through the respiratory chain to
O&#8322;, with the energy released trapped as ATP. <k>O&#8322; is the final acceptor of reducing
equivalents.</k></p>
<p>The <b>coupling</b> of oxidation with phosphorylation <i>is</i> oxidative phosphorylation.</p>
<p>Requires all three: <k>the ETC</k>, <k>mitochondria</k>, <k>oxygen</k>.</p>
<p class=tip>That word "coupling" is doing real work. It is why an inhibitor of phosphorylation
also shuts down oxidation &mdash; and why an <i>un</i>coupler does the opposite.</p>"""),

dict(sec="ATP synthesis",
     q="How does <b>substrate-level</b> phosphorylation differ?",
     a="""<table class=t>
<tr><th></th><th>Substrate-level</th><th>Oxidative</th></tr>
<tr><td>Needs the ETC?</td><td><k>no</k></td><td>yes</td></tr>
<tr><td>Needs mitochondria?</td><td><k>no</k></td><td>yes</td></tr>
<tr><td>Needs oxygen?</td><td><k>no</k></td><td>yes</td></tr>
<tr><td>Example</td><td>glycolysis</td><td>the respiratory chain</td></tr>
</table>
<p>It works when the energy at the substrate level is itself high enough to phosphorylate ADP
directly.</p>
<p class=tip>Three noes and three yeses &mdash; it's a clean split. This is also why a red blood
cell, which has no mitochondria, can still make ATP.</p>"""),

dict(sec="ATP synthesis",
     q="State the <b>chemiosmotic theory</b>.",
     a=SVG_CIRCUIT + """
<p>The most accepted theory of oxidative phosphorylation. The inner mitochondrial membrane is the
<k>coupling membrane</k> and is <k>impermeable to H&#8314;</k>.</p>
<p>H&#8314; from oxidation cannot cross the lipid bilayer, so it is <b>pumped out</b> through the
protein complexes &mdash; at <k>Complexes I, III and IV only</k>. The intermembrane space becomes
low pH and positive; the matrix stays high pH and <b>negative on the inner face</b>.</p>
<p>The only way back in is through <k>F&#8320;F&#8321;</k>, and that return drives ATP synthesis.</p>
<p class=tip>Read it as a circuit: the chain is the pump, the membrane is the dam, the synthase is
the turbine. Everything in the inhibitor section is a way of breaking one of those three.</p>"""),

dict(sec="ATP synthesis",
     q="The proton gradient has two components. Name them.",
     a="""<p><k>&#916;pH</k> &mdash; the chemical gradient (acidic outside, alkaline inside).<br>
<k>&#916;&#936;</k> &mdash; the electrical potential (outside positive, inside negative).</p>
<p class=tip>Both store energy, and an uncoupler collapses both at once by carrying H&#8314; across
the bilayer. Naming both is often what a question is fishing for when it says "electrochemical
gradient."</p>"""),

dict(sec="ATP synthesis",
     q="Define the <b>P:O ratio</b> and give the two values, with the reason for the difference.",
     a="""<p>Definition: the number of ATP produced <k>per atom of oxygen reduced</k>.</p>
<table class=t>
<tr><th>Substrate type</th><th>ATP per &#189; O&#8322;</th><th>P:O</th><th>Coupling sites used</th></tr>
<tr><td><k>NAD-linked</k> dehydrogenases</td><td>3</td><td><k>3</k></td><td>I, III, IV</td></tr>
<tr><td><k>FAD-linked</k> dehydrogenases</td><td>2</td><td><k>2</k></td><td>III, IV only</td></tr>
</table>
<p><b>Why:</b> FAD-linked substrates enter at Complex II and <k>bypass Complex I</k> &mdash; they
skip one coupling site, so they lose one ATP.</p>
<p class=tip>The slide marks ATP three times &mdash; beneath I, III and IV &mdash; and never beneath
II. That absent mark is the whole explanation.</p>"""),

dict(sec="ATP synthesis",
     q="Which named substrates are NAD-linked, and which is FAD-linked?",
     a="""<p><k>NAD-linked (P:O = 3):</k> pyruvate, &#945;-ketoglutarate, isocitrate, malate.</p>
<p><k>FAD-linked (P:O = 2):</k> succinate.</p>
<p class=tip>Succinate is the one to anchor, because it is also the substrate of Complex II /
succinate dehydrogenase. If a question names succinate anywhere, Complex II is in play.</p>"""),

dict(sec="ATP synthesis",
     q="What is <b>respiratory control</b>, and what determines the rate?",
     a="""<p>Once the electrochemical gradient is formed, further transport of reducing equivalents
is <k>inhibited</k> unless the gradient is discharged by ATP synthesis &mdash; and discharge
depends on the availability of <k>ADP and Pi</k>.</p>
<div class=chain>rate of oxidative phosphorylation &#8733; [ADP][Pi] / [ATP]</div>
<p>ADP and Pi on top, ATP on the bottom. This controls both the <b>speed of ATP synthesis</b> and
<b>oxygen consumption</b>.</p>
<p>Her worked reasoning: if [ATP]/[ADP] is high in the matrix, the chain <k>slows down</k> &mdash;
you already have enough ATP.</p>
<p class=warn>Her verbatim exam warning: <b>"Does the ratio of ATP to ADP, or ADP to ATP? You have
to be careful what they are asking. They can reverse it too."</b> Read the ratio in the stem before
you answer up or down.</p>"""),

# ================================================== 7. Inhibitors
dict(sec="Inhibitors",
     q="There are three ways to interfere with this system. Name the classes and their outcomes.",
     a="""<table class=t>
<tr><th>Class</th><th>Mechanism</th><th>ETC</th><th>O&#8322; use</th><th>ATP</th></tr>
<tr><td><k>A.</k> Inhibitors of ETC complexes</td><td>block electron flow through I&#8211;IV</td><td>&#8595;</td><td>&#8595;</td><td>&#8595;</td></tr>
<tr><td><k>B.</k> Inhibitors of oxidative phosphorylation</td><td>block H&#8314; flow through F&#8320;F&#8321;, or block ADP/ATP transport</td><td>&#8595;</td><td>&#8595;</td><td>&#8595;</td></tr>
<tr><td><k>C.</k> Uncouplers</td><td>increase inner-membrane permeability to H&#8314;</td><td><k>&#8593;</k></td><td><k>&#8593;</k></td><td>absent</td></tr>
</table>
<p><b>A and B are identical in outcome, because oxidation and phosphorylation are tightly
coupled.</b> C is the odd one out.</p>
<p class=tip>An uncoupler is the <b>only</b> agent in the entire lecture that makes an arrow point
<b>up</b>. If a question shows increased oxygen consumption with no ATP, you are looking at class C
and nothing else.</p>
<p class=warn>This table ships <i>blank</i> on her slide &mdash; every cell above comes from what
she said aloud. It is also the section she returned to four separate times.</p>""",
     img=["slide48_1.jpg"]),

dict(sec="Inhibitors",
     q="Walk the chain from left to right and name what blocks each step.",
     a="""<table class=t>
<tr><th>Step blocked</th><th>Agents</th></tr>
<tr><td>succinate &#8594; Complex II</td><td><k>malonate</k> (competitive)</td></tr>
<tr><td>Complex I &#8594; Q</td><td><k>piericidin A, amobarbital, rotenone</k></td></tr>
<tr><td>Complex II &#8594; Q</td><td><k>carboxin, TTFA</k></td></tr>
<tr><td>Complex III &#8594; cyt c</td><td><k>BAL (dimercaprol), antimycin A</k></td></tr>
<tr><td>Complex IV &#8594; O&#8322;</td><td><k>H&#8322;S, CO, CN&#8315;</k></td></tr>
<tr><td>ADP+Pi &#8594; ATP</td><td><k>oligomycin</k></td></tr>
<tr><td>the membrane itself</td><td><k>uncouplers</k></td></tr>
</table>
<p class=tip>Look at the figure: there are <b>three separate ADP+Pi &#8594; ATP arcs</b>, beneath
Complexes I, III and IV &mdash; and <b>none</b> beneath Complex II. That missing arc is the visual
proof of why Complex II is not a coupling site.</p>""",
     img=["slide48_1.jpg"]),

dict(sec="Inhibitors",
     q="Name the <b>Complex I</b> inhibitors and what each one is.",
     a="""<p>All block the step Complex I &#8594; CoQ, so <b>CoQ cannot be reduced</b>.</p>
<table class=t>
<tr><td><k>Amobarbital</k></td><td>a barbiturate &mdash; sedative</td></tr>
<tr><td><k>Piericidin A</k></td><td>an antibiotic</td></tr>
<tr><td><k>Rotenone</k></td><td>insecticide and fish poison</td></tr>
</table>
<p class=tip>Rotenone is <b>not fatal to humans</b> &mdash; its stomach-irritant properties cause
vomiting before a lethal dose is absorbed.</p>"""),

dict(sec="Inhibitors",
     q="Name the <b>Complex II</b> inhibitors, and say which one has a named mechanism.",
     a="""<p>All block the step Complex II &#8594; CoQ.</p>
<table class=t>
<tr><td><k>Carboxin</k></td><td>systemic agricultural fungicide / seed treatment</td></tr>
<tr><td><k>TTFA</k></td><td>&#8212;</td></tr>
<tr><td><k>Malonate</k></td><td>a <k>competitive inhibitor of succinate dehydrogenase</k></td></tr>
</table>
<p class=tip>Malonate is the only inhibitor in the whole lecture with a <i>competitive</i>
mechanism named &mdash; and there is a reason: malonate structurally resembles succinate, so it
occupies the same site. Ma<b>lon</b>ate vs succ<b>in</b>ate.</p>"""),

dict(sec="Inhibitors",
     q="Name the <b>Complex III</b> inhibitors.",
     a="""<p>Both block the step Complex III &#8594; cytochrome c, so <b>CoQH&#8322; cannot be
oxidised</b>.</p>
<p><k>Dimercaprol</k> (BAL, British anti-Lewisite)<br><k>Antimycin A</k></p>
<p class=tip>Dimercaprol was developed at Oxford in WWII as the antidote to Lewisite. It is now
used for arsenic, mercury and lead poisoning (and formerly for <b>Wilson's disease</b>) &mdash; so
it is both a therapeutic chelator and, at the mitochondrion, a poison. It is also the active
ingredient in Fintrol, a piscicide.</p>""",
     img=["slide48_1.jpg"]),

dict(sec="Inhibitors",
     q="Name the <b>Complex IV</b> inhibitors.",
     a="""<p>All block the step Complex IV &#8594; O&#8322;, so <b>oxygen cannot be reduced</b>.</p>
<p><k>H&#8322;S</k> &#183; <k>Carbon monoxide</k> &#183; <k>Cyanide</k></p>
<p>Cyanide antidotes: <b>amyl nitrite</b> / <b>thiosulfates</b>.</p>
<p class=tip>This is the group that matters clinically, because it is the group that kills people.
The next section takes CO and cyanide apart.</p>"""),

dict(sec="Inhibitors",
     q="What is <b>oligomycin</b>, and exactly where does it act?",
     a="""<p>An <b>antibiotic</b> and an inhibitor of <k>ATP synthase</k>. It blocks the F&#8320;F&#8321;
ATPase by blocking <k>conduction of H&#8314; through F&#8320;</k>.</p>
<p>Result: ATP cannot be manufactured, and <b>oxygen consumption falls</b>.</p>
<p class=tip>Oxygen consumption falls even though oligomycin never touches the chain itself. That is
respiratory control doing its job: the gradient can't discharge, so electron transport backs up and
stops. It is the clearest demonstration in the lecture that the two halves are coupled.</p>"""),

dict(sec="Inhibitors",
     q="What is <b>atractyloside</b>, and how is its target different from oligomycin's?",
     a="""<p>Atractyloside inhibits <k>translocation of ADP and ATP</k> &mdash; it acts on the
<k>adenine nucleotide translocase</k>, which exchanges cytosolic ADP&#179;&#8315; for mitochondrial
ATP&#8308;&#8315;.</p>
<table class=t>
<tr><th>Agent</th><th>Target</th></tr>
<tr><td><k>Oligomycin</k></td><td>H&#8314; conduction through <b>F&#8320;</b> of the synthase itself</td></tr>
<tr><td><k>Atractyloside</k></td><td>the <b>transporter</b>, not the synthase</td></tr>
<tr><td><b>Mersalyl</b></td><td>the separate phosphate transporter (carries H&#8322;PO&#8324;&#8315; with H&#8314;)</td></tr>
</table>
<p class=tip>Oligo<b>mycin</b> is an antibi<b>otic</b> acting on the machine; a<b>tract</b>yloside
blocks the <b>tract</b>. Same three outcome arrows, different lesion.</p>
<p class=warn>Starving the synthase of ADP has the same effect as jamming it &mdash; which is why
both sit in class B with identical outcomes.</p>""",
     img=["slide44_1.jpg"]),

dict(sec="Inhibitors",
     q="If Complex III is inhibited, what happens to CoQH&#8322; &mdash; and state the general rule.",
     a="""<p>CoQH&#8322; <k>cannot be oxidised</k>. It piles up in the reduced form.</p>
<p><b>General rule:</b> everything <k>upstream</k> of a block stays <k>reduced</k>; everything
<k>downstream</k> stays <k>oxidised</k>.</p>
<p class=warn>Her exact words: "You have to be careful what you infer &mdash; when there is an
inhibitor of complex 3, <i>can CoQH&#8322; be oxidised?</i> No." The trap is answering "CoQ cannot
be reduced," which is what a Complex I or II inhibitor does.</p>"""),

# ================================================== 8. CO and cyanide
dict(sec="Carbon monoxide &amp; cyanide",
     q="How does <b>carbon monoxide</b> poison the electron transport chain?",
     a="""<p>It binds <k>Fe&#178;&#8314;</k> in the heme of <b>cytochrome a&#8323;</b>, inhibiting
Complex IV.</p>
<p>The binding to heme is <k>non-covalent</k> &mdash; and therefore <k>reversible</k> with 100%
oxygen therapy or <b>hyperbaric oxygen</b>.</p>
<p class=tip>Reversibility is not a detail, it is the treatment. Because CO sits on a reversible
site, you can out-compete it by flooding the system with oxygen. Cyanide gives you no such option.</p>"""),

dict(sec="Carbon monoxide &amp; cyanide",
     q="What does CO do to <b>hemoglobin</b>, separately from what it does to Complex IV?",
     a="""<p>Its affinity for Hb is <k>220 times</k> that of oxygen. It binds tightly but reversibly
to the hemoglobin iron, and then:</p>
<p>&#8226; causes the <b>remaining heme sites to bind oxygen with high affinity</b><br>
&#8226; shifts hemoglobin to the <k>relaxed (R) conformation</k><br>
&#8226; shifts the oxygen-binding curve <k>to the left</k><br>
&#8226; flattens the normal sigmoid toward a <b>hyperbola</b></p>
<p class=tip>CO attacks on two fronts at once &mdash; it stops the tissue using oxygen (Complex IV)
<i>and</i> stops the blood delivering it (hemoglobin). Most poisons only get one.</p>""",
     img=["slide40_1.jpg"]),

dict(sec="Carbon monoxide &amp; cyanide",
     q="Why does 50% carboxyhemoglobin kill, when a patient with <b>50% anemia</b> walks around?",
     a="""<p>In anemia the remaining hemoglobin still <k>releases</k> oxygen to the tissues normally.</p>
<p>In CO poisoning the affected hemoglobin <k>cannot release oxygen to the tissues</k>, because CO
bound at one heme prevents the other hemes from offloading O&#8322;.</p>
<p>So oxygen <b>delivery</b> collapses even where saturation looks adequate.</p>
<p class=tip>On the dissociation curve: at tissue pO&#8322; (&#8776; 3.5&#8211;4.5 kPa) the anemic
curve is still descending steeply &mdash; oxygen is being released &mdash; while the COHb curve is
already flat. Same saturation number, opposite physiology. This is the exam form of "left shift."</p>""",
     img=["slide40_1.jpg"]),

dict(sec="Carbon monoxide &amp; cyanide",
     q="What is the clinical picture and history of CO poisoning?",
     a="""<p>Sign: <k>cherry-red</k> skin discolouration.</p>
<p>Typical history: <b>burning furnaces in a closed space</b>, automobile pollution, suicide
attempt.</p>
<p>Treatment: <k>100% oxygen / hyperbaric oxygen</k>.</p>
<p class=warn>Do <b>not</b> use skin colour to distinguish CO from cyanide. Cyanide also turns the
skin pink, from cyanide&#8211;hemoglobin complexes. Use the <b>history</b> and the <b>iron oxidation
state</b> instead.</p>""",
     img=["slide41_2.jpg"]),

dict(sec="Carbon monoxide &amp; cyanide",
     q="How does <b>cyanide</b> poison the chain, and why is it so much worse than CO?",
     a="""<p>It binds <k>Fe&#179;&#8314;</k> in the heme of cytochrome a&#8323; and prevents oxygen
reduction &mdash; the terminal step of electron transport.</p>
<p>The binding is <k>covalent</k> and <k>cannot be reversed</k>. Mitochondrial respiration and ATP
production cease, giving <b>rapid cell death</b> from <k>tissue asphyxia, especially in the CNS</k>.</p>
<p class=warn>Because the bond is irreversible, there is no equivalent of hyperbaric oxygen. The
only viable strategy is to intercept cyanide <i>before</i> it reaches the complex &mdash; and
"you have to act within minutes."</p>
<p class=tip>C-<b>O</b> has two letters &#8594; Fe<b>&#178;</b>&#8314;. C-<b>N</b>-&#8315; has three
&#8594; Fe<b>&#179;</b>&#8314;.</p>"""),

dict(sec="Carbon monoxide &amp; cyanide",
     q="Where does cyanide poisoning actually come from?",
     a="""<p><k>Sodium nitroprusside</k> &mdash; an IV antihypertensive that <b>releases cyanide
ions</b>. Cyanide levels must be monitored in patients on it.</p>
<p><k>Cyanogenic glycosides</k> in food: bitter almonds; the pits of cherry, apple and apricot; and
<k>cassava (manioc)</k>.</p>
<p>Cassava must be <b>dried, soaked, rinsed or baked</b> before consumption.</p>
<p class=tip>The fatal dose can be as low as <b>1.5 mg/kg</b>. High inhaled concentrations cause
coma with seizures, apnea and cardiac arrest within minutes; lower doses give weakness, giddiness,
headache, vertigo and confusion. Chronic low-level exposure &mdash; cassava as a staple in tropical
Africa &mdash; raises blood cyanide and causes weakness.</p>"""),

dict(sec="Carbon monoxide &amp; cyanide",
     q="Explain the <b>cyanide antidotes</b> and the logic behind them.",
     a="""<table class=t>
<tr><th>Antidote</th><th>Mechanism</th></tr>
<tr><td><k>Amyl nitrite</k></td><td>oxidises hemoglobin Fe&#178;&#8314; to <k>methemoglobin</k> Fe&#179;&#8314;, which sequesters circulating cyanide for excretion</td></tr>
<tr><td><k>Sodium thiosulfate</k></td><td>an alternative sequestering agent &mdash; a sulfur donor</td></tr>
</table>
<p><b>The logic:</b> because the Complex IV binding is covalent and irreversible, the only strategy
left is to <k>intercept cyanide in the circulation before it reaches the complex</k>.</p>
<p class=tip>The antidote works by deliberately creating a <i>decoy</i> Fe&#179;&#8314; in the blood
that competes with cytochrome a&#8323;'s Fe&#179;&#8314;. Ni<b>trite</b> oxidises; thio<b>sulfate</b>
donates <b>sulfur</b>, converting cyanide to harmless <b>thiocyanate</b> for excretion in urine.</p>
<p class=warn>Answer <b>amyl nitrite / sodium thiosulfate</b> as taught &mdash; the question is
testing the methemoglobin mechanism. Current clinical practice actually prefers
<b>hydroxocobalamin</b>; carry that for the wards, not for this exam.</p>"""),

dict(sec="Carbon monoxide &amp; cyanide",
     q="Put carbon monoxide and cyanide side by side.",
     a="""<table class=t>
<tr><th></th><th>Carbon monoxide</th><th>Cyanide</th></tr>
<tr><td>Target</td><td colspan="2">Complex IV, cytochrome a&#8323; &mdash; the same site</td></tr>
<tr><td>Iron bound</td><td><k>Fe&#178;&#8314;</k></td><td><k>Fe&#179;&#8314;</k></td></tr>
<tr><td>Bond</td><td><k>non-covalent</k></td><td><k>covalent</k></td></tr>
<tr><td>Reversible?</td><td>yes</td><td>no</td></tr>
<tr><td>Second target</td><td>hemoglobin (COHb)</td><td>&#8212;</td></tr>
<tr><td>Treatment</td><td>100% O&#8322; / hyperbaric</td><td>amyl nitrite or thiosulfate</td></tr>
<tr><td>Treatment logic</td><td>displace it from a reversible site</td><td>intercept it upstream</td></tr>
<tr><td>Urgency</td><td>urgent</td><td><b>minutes</b></td></tr>
<tr><td>Skin</td><td>cherry-red</td><td>pink/flushed</td></tr>
<tr><td>History</td><td>closed space, combustion, car exhaust</td><td>nitroprusside, untreated cassava, bitter almonds</td></tr>
</table>
<p class=tip>Everything above the "iron bound" line is identical. The <b>oxidation state and the
bond type</b> are the only real discriminators &mdash; and they generate every difference below
them, including the treatments.</p>"""),

dict(sec="Carbon monoxide &amp; cyanide",
     q="A married couple are found dead in a tightly closed tent at Crater Lake, with a propane camping lantern burning inside. Cause?",
     a="""<p><k>Carbon monoxide poisoning</k>, with cherry-red discolouration.</p>
<p>CO binds Fe&#178;&#8314; of cytochrome a&#8323; and of hemoglobin. <b>Combustion in an enclosed
space</b> is the classic history.</p>
<p class=tip>Any burning device plus any sealed space is CO until proven otherwise &mdash; lantern,
furnace, generator, charcoal grill, car in a garage.</p>"""),

dict(sec="Carbon monoxide &amp; cyanide",
     q="A 65-year-old man with malignant hypertension is found dead at home. A glass contains reddish-brown material identified as <b>sodium nitroprusside</b>. How did it kill him?",
     a="""<p>Nitroprusside is an IV antihypertensive that <k>releases cyanide ions</k>.</p>
<p>The cyanide binds Fe&#179;&#8314; of cytochrome a&#8323;, halting electron transport and ATP
production &#8594; tissue asphyxia.</p>
<p class=warn>The clinical takeaway she wanted: <b>cyanide levels must be monitored in patients on
nitroprusside.</b> This is a drug you will actually prescribe.</p>"""),

dict(sec="Carbon monoxide &amp; cyanide",
     q="Three patients are admitted in Lagos after a cassava-based meal ('Gari') &mdash; vomiting, abdominal pain, unconscious, renal failure, then cardiopulmonary arrest. Cause?",
     a="""<p><k>Cyanide poisoning</k> from <b>cyanogenic glycosides</b> in improperly processed
cassava.</p>
<p>Cyanogenic foods must be <k>dried, soaked, rinsed or baked</k> before consumption.</p>
<p class=tip>Cassava is a dietary staple across tropical Africa, so this is both an acute poisoning
and a chronic public-health problem &mdash; chronic low-level exposure raises blood cyanide and
causes weakness.</p>""",
     img=["slide42_1.jpg"]),

# ================================================== 9. Uncouplers
dict(sec="Uncouplers",
     q="What is an <b>uncoupler</b>, mechanistically?",
     a="""<p>An agent that causes <k>leakage of H&#8314; across the inner membrane</k>, collapsing
the electrochemical proton gradient &mdash; it <k>dissociates oxidation from phosphorylation</k>.</p>
<p>An energetically favourable electron transport system is uncoupled from an energetically
favourable phosphorylation system by a substance that simply dissipates the gradient.</p>
<p class=tip>It doesn't inhibit anything. It gives H&#8314; a <b>second way home</b> &mdash; one
that bypasses the turbine. The chain keeps running; the ATP just never gets made.</p>"""),

dict(sec="Uncouplers",
     q="Why do uncouplers make ETC function and oxygen consumption go <b>up</b>?",
     a="""<p>Because they <k>abolish respiratory control</k>. Normally the chain stops when the
gradient is full and the ATP/ADP ratio is high. With a second leak path the gradient never builds,
so &mdash; in her words &mdash; <k>"the ETC does not know when to stop."</k></p>
<div class=chain>ETC function &#8593; &#183; oxygen consumption &#8593; &#183; ATP synthesis absent</div>
<p>The untrapped oxidation energy is released as <k>heat</k>, so <b>uncouplers raise body
temperature</b>.</p>
<p class=tip>Trace it from the respiratory-control formula: the chain is throttled by the gradient,
and you just removed the throttle. Heat is what free energy becomes when nothing captures it.</p>"""),

dict(sec="Uncouplers",
     q="Name the uncouplers.",
     a="""<p><k>2,4-dinitrophenol (DNP)</k> &mdash; the archetype<br>
<k>Dinitrocresol</k><br>
<k>Pentachlorophenol</k><br>
<k>CCCP</k> &mdash; carbonyl cyanide m-chlorophenylhydrazone<br>
<k>Aspirin/salicylate in high doses</k><br>
<k>Thermogenin</k> &mdash; brown adipose tissue</p>
<p class=tip>The first four are poisons, the fifth is a drug at toxic dose, and the sixth is you.
All six do exactly the same thing.</p>
<p class=tip>The slide writes CCCP as "chlorocarbanoyl cyanide phenylhydrazone" &mdash; the word
order is scrambled. The compound is <b>carbonyl cyanide m-chlorophenylhydrazone</b>. Recognise it;
the mechanism is identical to DNP's.</p>
<p class=warn>High-dose salicylate uncoupling is why <b>fever</b> is a feature of aspirin overdose
&mdash; the drug is generating heat inside mitochondria.</p>"""),

dict(sec="Uncouplers",
     q="How does <b>2,4-dinitrophenol</b> work, and why isn't it an anti-obesity drug?",
     a="""<p>DNP binds protons and readily <k>diffuses across the inner mitochondrial membrane</k>,
losing the energy as heat. It carries H&#8314; from the low-pH intermembrane space to the high-pH
matrix in its protonated form, then returns deprotonated &mdash; over and over.</p>
<p>Electron transport therefore proceeds at a rapid rate <k>without production of a proton
gradient</k>.</p>
<p class=warn>It <i>was</i> marketed as a diet drug. People "fell dead while on this diet drug
&mdash; they died of <k>hyperthermia</k>." Burning fuel without capturing it is exactly what weight
loss would need, and exactly what cooks you. The temperature rise is the barrier.</p>""",
     img=["slide46_1.jpg"]),

dict(sec="Uncouplers",
     q="What is <b>thermogenin</b>, and what is it for?",
     a="""<p>Brown fat contains a unique protein &mdash; <k>uncoupling protein / thermogenin</k>
(UCP1). It <b>spans the inner mitochondrial membrane</b> and acts as a <k>proton conductance
pathway</k>, transporting protons back into the matrix.</p>
<p>As the gradient dissipates, large amounts of energy are released as <k>heat</k>.</p>
<p>Physiological purpose: to protect vital organs, <k>especially in the newborn</k>.</p>
<p class=tip>Thermogenin is a channel <b>parallel to, and separate from, F&#8320;F&#8321;</b> &mdash;
it is a second return path, not an inhibitor of the synthase. A newborn can't shiver effectively,
so brown fat generates heat chemically instead.</p>""",
     img=["slide47_1.jpg"]),

dict(sec="Uncouplers",
     q="Thermogenin and DNP have the same mechanism. What separates them?",
     a="""<table class=t>
<tr><th>Thermogenin</th><th>2,4-DNP</th></tr>
<tr><td><k>endogenous</k> membrane protein</td><td><k>exogenous</k> small molecule</td></tr>
<tr><td>brown adipose tissue</td><td>ingested</td></tr>
<tr><td>physiological role &mdash; newborn thermogenesis</td><td>no role &mdash; killed dieters</td></tr>
</table>
<p>Both dissipate the gradient as heat, by exactly the same trick.</p>
<p class=tip>The mechanism is morally neutral; only the regulation differs. Thermogenin is switched
on when the body wants heat. DNP is on all the time, everywhere.</p>"""),

dict(sec="Uncouplers",
     q="A tissue shows <b>increased</b> oxygen consumption, <b>increased</b> electron flow, and <b>no</b> ATP production. Which class of agent, and what else would you expect?",
     a="""<p><k>Class C &mdash; an uncoupler.</k> It is the only class in the lecture that makes
anything increase.</p>
<p>Also expect <k>raised body temperature</k>, because the untrapped energy leaves as heat.</p>
<p class=tip>Compare the alternative: an ETC inhibitor or an oxidative-phosphorylation inhibitor
would give you <b>all three arrows down</b>, and those two are indistinguishable from the outcome
columns alone &mdash; you'd have to name the agent to tell them apart.</p>"""),

# ================================================== 10. Exam notes
dict(sec="Answering as taught",
     q="Three places where the lecture's numbers differ from current textbooks &mdash; what do you write on the exam?",
     a="""<table class=t>
<tr><th>Point</th><th>As taught &#8212; <b>use this</b></th><th>Current standard</th></tr>
<tr><td>P:O ratios</td><td><k>3 (NAD-linked), 2 (FAD-linked)</k></td><td>&#8776; 2.5 and 1.5</td></tr>
<tr><td>Complex subunits</td><td><k>I &gt;25 &#183; II 4 &#183; III 6 &#183; IV 13</k></td><td>I &#8776;45, III &#8776;11, IV 13</td></tr>
<tr><td>Cyanide antidote</td><td><k>amyl nitrite / sodium thiosulfate</k></td><td>hydroxocobalamin preferred</td></tr>
</table>
<p class=warn>Answer as taught. The deck, its Harper's source, and the lecturer are all consistent,
and the whole P:O section is built on the integers &mdash; do not "correct" it.</p>
<p class=tip>But know both. USMLE-style question banks often use 2.5/1.5, and the derived figure of
30&#8211;32 ATP per glucose rather than 36&#8211;38. Know which room you're in.</p>"""),

dict(sec="Answering as taught",
     q="What are the four one-line <b>function statements</b> she said were the core of the lecture?",
     a="""<p><k>Complex I</k> passes reducing equivalents from <b>NADH to CoQ</b>.<br>
<k>Complex II</k> passes reducing equivalents from <b>FADH&#8322;/succinate to CoQ</b>.<br>
<k>Complex III</k> passes reducing equivalents from <b>CoQH&#8322; to cytochrome c</b>.<br>
<k>Complex IV</k> passes reducing equivalents from <b>cytochrome c to oxygen</b>, reducing it to
water.</p>
<p class=tip>After each complex she said "that's what you need to know about each complex." She
stated each of these three times. If you learn nothing else verbatim, learn these four.</p>"""),

]

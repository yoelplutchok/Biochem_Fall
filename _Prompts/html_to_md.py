"""HTML -> GitHub-flavoured markdown for v2-style study guides.

Usage:  python3 html_to_md.py "<guide>.html" "<guide>.md"

Run it from the lecture folder so relative image paths survive. Handles the v2
CSS vocabulary: .map -> fenced code block, .must / .vs / .clin / .legend ->
labelled blockquotes, <figure> -> image + italic caption, sup/sub -> Unicode,
table captions -> bold paragraphs, and strips every class/style/span so pandoc
emits clean pipe tables instead of div soup.
"""
import io, re, subprocess, sys
from bs4 import BeautifulSoup, NavigableString

if len(sys.argv) < 3:
    sys.exit(__doc__)
SRC, OUT = sys.argv[1], sys.argv[2]

soup = BeautifulSoup(io.open(SRC, encoding="utf-8").read(), "lxml")

def text_of(node):
    """Flatten a node to text, turning <br> into newline and nbsp into space."""
    h = str(node)
    h = re.sub(r"<br\s*/?>", "\n", h, flags=re.I)
    t = BeautifulSoup(h, "lxml").get_text()
    return t.replace(" ", " ").replace(" ", " ")

def new_tag(name, **kw):
    return soup.new_tag(name, **kw)

SUP = str.maketrans("0123456789+-−", "⁰¹²³⁴⁵⁶⁷⁸⁹⁺⁻⁻")
SUB = str.maketrans("0123456789+-−", "₀₁₂₃₄₅₆₇₈₉₊₋₋")

# sup/sub -> unicode where the content is purely digits/signs
for tag, table in (("sup", SUP), ("sub", SUB)):
    for n in soup.find_all(tag):
        t = n.get_text()
        if t and all(ch in "0123456789+-−" for ch in t):
            n.replace_with(NavigableString(t.translate(table)))

# strip presentational spans
for sp in soup.find_all("span"):
    if sp.get("class") and ("ans" in sp["class"] or "h" in sp["class"] or "tag" in sp["class"] or "vshead" in sp["class"] or "lbl" in sp["class"]):
        continue
    sp.unwrap()

# table captions -> bold paragraph before the table; drop table classes
for t in soup.find_all("table"):
    cap = t.find("caption")
    if cap:
        p = soup.new_tag("p"); st = soup.new_tag("strong")
        st.string = cap.get_text(" ", strip=True)
        p.append(st)
        t.insert_before(p)
        cap.decompose()
    for a in ("class", "style"):
        if t.has_attr(a): del t[a]
for el in soup.find_all(True):
    if el.name in ("td", "th", "tr", "p", "li", "ol", "ul") and el.has_attr("style"):
        del el["style"]
# row/cell classes (e.g. tr.must, td.hi) are presentational; the star that marks
# a must-know row is already a literal character in the row's first cell
for el in soup.find_all(["tr", "td", "th"]):
    if el.has_attr("class"):
        del el["class"]

maps = []

# ---------- .map -> fenced code placeholder ----------
for i, m in enumerate(soup.select("div.map")):
    block = text_of(m)
    block = "\n".join(l.rstrip() for l in block.split("\n"))
    block = "\n".join(l for l in block.split("\n") if l.strip() or True)
    block = re.sub(r"\n\s*\n", "\n", block).strip("\n")
    block = block.replace("except\ngluconeogenesis", "except gluconeogenesis")
    maps.append(block)
    p = new_tag("p")
    p.string = "%%MAP%d%%" % i
    m.replace_with(p)

# ---------- <u> discriminator -> bold ----------
for u in soup.find_all("u"):
    u.name = "strong"

# ---------- .must -> blockquote ----------
# NB: a .vs.must box is a marked confusable-pair box, not a standalone band --
# leave it for the .vs handler below, which adds the star to its header.
for d in soup.select("div.must"):
    if "vs" in (d.get("class") or []):
        continue
    bq = new_tag("blockquote")
    p = new_tag("p")
    tag = d.find("span", class_="tag")
    if tag:
        tag.decompose()
    st = new_tag("strong"); st.string = "★ MUST KNOW — "
    p.append(st)
    for c in list(d.contents):
        p.append(c.extract())
    bq.append(p)
    d.replace_with(bq)

# ---------- .vs -> blockquote with paired lines ----------
for d in soup.select("div.vs"):
    bq = new_tag("blockquote")
    head = d.find("div", class_="vshead")
    ptitle = new_tag("p")
    st = new_tag("strong")
    label = "★ MUST KNOW · VS — " if "must" in (d.get("class") or []) else "VS — "
    title = re.sub(r"\s+", " ", head.get_text(" ", strip=True)) if head else ""
    st.string = label + title.lstrip("★ ").strip()
    ptitle.append(st)
    bq.append(ptitle)
    for tr in d.select("table tr"):
        for td in tr.find_all("td"):
            p = new_tag("p")
            hspan = td.find("span", class_="h")
            if hspan:
                st = new_tag("strong")
                st.string = hspan.get_text(strip=True) + " — "
                hspan.decompose()
                p.append(st)
            for c in list(td.contents):
                p.append(c.extract())
            bq.append(p)
    d.replace_with(bq)

# ---------- .clin / .legend -> blockquote ----------
for cls, label in (("clin", "CLINICAL"), ("legend", "HOW TO READ THIS")):
    for d in soup.select("div." + cls):
        bq = new_tag("blockquote")
        lbl = d.find("span", class_="lbl")
        cap = lbl.get_text(strip=True).upper() if lbl else label
        if lbl:
            lbl.decompose()
        first = new_tag("p")
        st = new_tag("strong"); st.string = cap + " — "
        first.append(st)
        bq.append(first)
        for c in list(d.contents):
            if isinstance(c, NavigableString) and not c.strip():
                c.extract(); continue
            if getattr(c, "name", None) == "p":
                for cc in list(c.contents):
                    first.append(cc.extract())
                c.decompose()
            else:
                bq.append(c.extract())
        d.replace_with(bq)

# ---------- header ----------
hdr = soup.find("div", class_="hdr")
if hdr:
    kicker = hdr.find("div", class_="kicker")
    h1 = hdr.find("h1")
    sub = hdr.find("div", class_="sub")
    wrap = new_tag("div")
    nh = new_tag("h1"); nh.string = h1.get_text(strip=True); wrap.append(nh)
    for on in soup.select("span.onum"): pass
    for node in (kicker, sub):
        if node:
            p = new_tag("p"); em = new_tag("em")
            em.string = node.get_text(" ", strip=True)
            p.append(em); wrap.append(p)
    hdr.replace_with(wrap)

# ---------- figures ----------
for fig in soup.find_all("figure"):
    wrap = new_tag("div")
    img = fig.find("img")
    cap = fig.find("figcaption")
    if img:
        p = new_tag("p"); p.append(img.extract()); wrap.append(p)
    if cap:
        p = new_tag("p"); em = new_tag("em")
        for c in list(cap.contents):
            em.append(c.extract())
        p.append(em); wrap.append(p)
    fig.replace_with(wrap)

# ---------- self-test answers ----------
for a in soup.select("span.ans"):
    st = new_tag("strong"); st.string = "Answer: "
    a.insert(0, st)
    a.unwrap()

# ---------- tables: <br> -> " · ", drop colgroup ----------
for t in soup.find_all("table"):
    for cg in t.find_all("colgroup"):
        cg.decompose()
    for br in t.find_all("br"):
        br.replace_with(NavigableString(" · "))
    for cell in t.find_all(["td", "th"]):
        span = cell.get("colspan")
        if span and span.isdigit() and int(span) > 1:
            del cell["colspan"]
            for _ in range(int(span) - 1):
                extra = new_tag(cell.name)
                cell.insert_after(extra)

# ---------- headings: fold .onum into plain text ----------
for h in soup.find_all(["h2", "h3", "h4"]):
    txt = h.get_text(" ", strip=True)
    txt = re.sub(r"\s*/\s*", " · ", txt, count=1)
    txt = re.sub(r"\s+", " ", txt).strip()
    h.clear()
    h.append(NavigableString(txt))

# ---------- unwrap layout divs ----------
for sel in ("div.cheat", "div.two-col", "div.metagrid"):
    for d in soup.select(sel):
        d.unwrap()

body = soup.body
html = body.decode_contents()

pr = subprocess.run(["pandoc", "-f", "html", "-t", "gfm", "--wrap=none"],
                    input=html, capture_output=True, text=True)
if pr.returncode:
    sys.exit(pr.stderr)
md = pr.stdout

# reinsert maps as fenced blocks
for i, block in enumerate(maps):
    md = md.replace("%%MAP%d%%" % i, "```text\n" + block + "\n```")

md = re.sub(r"\n{3,}", "\n\n", md)
md = md.replace("<div>", "").replace("</div>", "")
io.open(OUT, "w", encoding="utf-8").write(md.strip() + "\n")
print("wrote", OUT, len(md.split()), "words")

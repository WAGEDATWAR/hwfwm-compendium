"""Build wiki-tier list tables (essences, confluences, awakening stones, gods, monsters) from wiki/pages.json.
Outputs markdown fragments next to this script: wiki_essence_table.md, wiki_confluence_table.md,
wiki_stone_table.md, wiki_gods_table.md, wiki_monster_tables.md. Cross-marks entries found in the book text."""
import json, re, os, io, sys, collections

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
HERE = os.path.dirname(os.path.abspath(__file__))
BASE = os.path.abspath(os.path.join(HERE, "..", ".."))
ST = os.path.join(BASE, "src", "Source_Text")
P = json.load(open(os.path.join(HERE, "wiki", "pages.json"), encoding="utf-8"))


def clean(t):
    t = re.sub(r"<ref[^>]*?/>|<ref.*?</ref>|<[^>]+>", "", t)
    t = re.sub(r"\[\[([^\]|]+)\|([^\]]+)\]\]", r"\2", t)
    t = re.sub(r"\[\[([^\]]+)\]\]", r"\1", t)
    t = re.sub(r"\{\{[^}]*\}\}|'''|''", "", t)
    return re.sub(r"\s+", " ", t).strip()


def sections(text):
    cur = ""
    out = collections.OrderedDict()
    for ln in text.split("\n"):
        m = re.match(r"^=+\s*(.*?)\s*=+\s*$", ln)
        if m:
            cur = clean(m.group(1))
            out.setdefault(cur, [])
            continue
        out.setdefault(cur, []).append(ln)
    return out


def bullets(lines):
    return [clean(l[1:]) for l in lines if l.startswith("*") and clean(l[1:])]


def cite(f):
    return "Book %d, chapter %d, line %d" % f if f else ""


def scan(names, suffix_rx):
    """first (book, ch, line) where '<name> <suffix>' occurs in the chapter files."""
    low = {n.lower(): n for n in names}
    rx = re.compile(r"\b(" + "|".join(re.escape(n) for n in sorted(low, key=len, reverse=True)) + r")" + suffix_rx, re.I)
    first = {}
    for b in range(1, 14):
        d = os.path.join(ST, "Book_%02d" % b)
        for fn in sorted(os.listdir(d)):
            ch = int(re.match(r"Ch_(\d+)_", fn).group(1))
            for i, l in enumerate(open(os.path.join(d, fn), encoding="utf-8").read().split("\n"), 1):
                for m in rx.finditer(l):
                    k = m.group(1).lower()
                    if k not in first:
                        first[k] = (b, ch, i)
    return first


# ------------------------------------------------------------ essences and confluences
E = P["Essences"]
rar = {}
cur = None
for ln in E.split("\n"):
    m = re.search(r"colspan=\"?\d+\"?\s*\|\s*'''([^']+)'''", ln)
    if m:
        cur = m.group(1)
        continue
    if "== Confluence" in ln:
        cur = None
    if cur:
        for m in re.finditer(r"\[\[([^\]|]+?) \(Essence\)(?:\|[^\]]*)?\]\]", ln):
            rar.setdefault(m.group(1), cur)
kc = E[E.find("=== Known Confluence Essences ==="):E.find("==Restricted Essences==")]
CONF = {}
for blk in kc.split("\n|-"):
    b = blk.strip("\n")
    m = re.match(r"\|\[\[([^\]|]+?) \(Essence\)", b)
    if not m:
        continue
    cells = re.split(r"\n\|", b)
    held = clean(cells[1]) if len(cells) > 1 else ""
    combos = [clean(x[1:]) for x in b.split("\n") if x.startswith("*")]
    CONF[m.group(1)] = (held, combos)
pages = sorted(t[:-len(" (Essence)")] for t in P if t.endswith("(Essence)"))
names = sorted(set(pages) | set(rar) | set(CONF))
first = scan(names, r" essences?\b")


def pageinfo(n):
    t = P.get(n + " (Essence)", "")
    ab, us, co = [], [], []
    for h, ls in sections(t).items():
        hl = h.lower()
        if "abilit" in hl:
            ab += bullets(ls)
        elif "user" in hl:
            us += bullets(ls)
        elif "combination" in hl:
            co += bullets(ls)
    return ab, us, co


out = ["| Essence | Rarity (wiki) | Known abilities (wiki) | Known users (wiki) | In the book text |", "|---|---|---|---|---|"]
n_ess = 0
for n in names:
    if n in CONF and n not in rar:
        continue
    ab, us, co = pageinfo(n)
    ab_s = "; ".join(re.sub(r"\s*\(.*?\)", "", a) for a in ab[:6] if a != "N/A") + (" …" if len(ab) > 6 else "")
    us_s = ", ".join(u.split(" (")[0] for u in us[:4] if u != "N/A") + (" …" if len(us) > 4 else "")
    out.append("| %s | %s | %s | %s | %s |" % (n, rar.get(n, "not rated"), ab_s.replace("|", "/"), us_s.replace("|", "/"), cite(first.get(n.lower()))))
    n_ess += 1
open(os.path.join(HERE, "wiki_essence_table.md"), "w", encoding="utf-8").write("\n".join(out))
cl = ["| Confluence | Held by (wiki) | Known combinations (wiki) | In the book text |", "|---|---|---|---|"]
for n in sorted(CONF):
    held, combos = CONF[n]
    cl.append("| %s | %s | %s | %s |" % (n, held.replace("|", "/"), ("; ".join(combos[:6]) + (" …" if len(combos) > 6 else "")).replace("|", "/"), cite(first.get(n.lower()))))
open(os.path.join(HERE, "wiki_confluence_table.md"), "w", encoding="utf-8").write("\n".join(cl))
print("essences", n_ess, "confluences", len(CONF), collections.Counter(rar.values()))

# ------------------------------------------------------------ awakening stones
stones = sorted(t for t in P if t.startswith("Awakening Stone of") or t.startswith("Awakening Stones of") or t.startswith("Divine Awakening Stone"))
sn = [re.sub(r"^(Divine )?Awakening Stones? of (the )?", "", t) for t in stones]
sfirst = scan(sn, r"\b")
sl = ["| Stone | Rarity (wiki) | Description (wiki) | Abilities it has given (wiki) | In the book text |", "|---|---|---|---|---|"]
for t, short in zip(stones, sn):
    txt = P[t]
    m = re.search(r"\(unranked, (\w+)\)|\(transcendent rank, (\w+)\)", txt)
    rr = (m.group(1) or m.group(2)) if m else "not rated"
    m2 = re.search(r"''([^']+)''", txt)
    desc = clean(m2.group(1)) if m2 else ""
    desc = re.sub(r"^An awakening stone (that|of|containing|crafted by)?\s*", "", desc)
    ab = []
    for h, ls in sections(txt).items():
        if "abilit" in h.lower():
            ab += [re.sub(r"\s*\(.*$", "", b) for b in bullets(ls)]
    sl.append("| %s | %s | %s | %s | %s |" % (t.replace("Awakening Stones of", "Awakening Stone of"), rr, desc[:110].replace("|", "/"), "; ".join(ab[:5]) + (" …" if len(ab) > 5 else ""), ""))
open(os.path.join(HERE, "wiki_stone_table.md"), "w", encoding="utf-8").write("\n".join(sl))
print("stones", len(stones))

# ------------------------------------------------------------ gods
G = P["Gods"]
gods = []
GR = re.compile(r"^(?:<big>)?\s*(?:\[\[([^\]|]+)(?:\|[^\]]*)?\]\]|([A-Za-z ]+?))\s*(?:</big>)?\s*-\s*First mentioned in Book (\d+) (?:Epilogue )?Chapter (\d+)")
for ln in G[G.find("==Known gods=="):].split("\n"):
    m = GR.match(ln)
    if m:
        nm = re.sub(r" \(God\)", "", (m.group(1) or m.group(2)).strip())
        gods.append((nm, m.group(3), m.group(4), "Epilogue" in ln))
gl = ["| God (wiki list) | First mentioned (wiki) | In the book text |", "|---|---|---|"]
alt = "|".join(re.escape(g[0]) for g in gods)
grx = re.compile(r"\b(?:god|goddess|temple|church|priests?|priestess|clergy)(?: of| to)? (?:the )?(%s)\b|\b(%s)'?s? (?:church|temple|priests?)" % (alt, alt), re.I)
gfirst = {}
for b in range(1, 14):
    d = os.path.join(ST, "Book_%02d" % b)
    for fn in sorted(os.listdir(d)):
        ch = int(re.match(r"Ch_(\d+)_", fn).group(1))
        for i, l in enumerate(open(os.path.join(d, fn), encoding="utf-8").read().split("\n"), 1):
            for m in grx.finditer(l):
                k = (m.group(1) or m.group(2)).lower()
                gfirst.setdefault(k, (b, ch, i))
for name, bk, chn, epi in gods:
    gl.append("| %s | Book %s, %s %s in the wiki numbering | %s |" % (name, bk, "epilogue chapter" if epi else "chapter", chn, cite(gfirst.get(name.lower()))))
mg = P.get("Minor Gods", "")
minor = [clean(x[1:]) for x in mg.split("\n") if x.startswith("*")]
open(os.path.join(HERE, "wiki_gods_table.md"), "w", encoding="utf-8").write("\n".join(gl) + "\n\nMINOR: " + ", ".join(minor))
print("gods", len(gods), "minor", len(minor))

# ------------------------------------------------------------ monsters
ml = []
for t in sorted(P):
    if re.match(r"(Lesser|Iron|Bronze|Silver|Gold|Diamond) Rank Monsters|Normal Rank Monsters", t):
        names_m = [clean(x) for x in P[t].split("\n") if x.strip() and not x.startswith(("=", "[[Category", "Bronze rank", "Iron rank", "Silver rank", "Gold rank", "Diamond rank", "Lesser"))]
        names_m = [x for x in names_m if x and not x.endswith(".")]
        ml.append((t, names_m))
with open(os.path.join(HERE, "wiki_monster_tables.md"), "w", encoding="utf-8") as f:
    for t, nm in ml:
        f.write("%s: %s\n" % (t, "; ".join(nm)))
print("monster pages", [(t, len(n)) for t, n in ml])

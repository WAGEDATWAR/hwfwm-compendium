import re, os, json, sys
base = r"C:\Users\Gabriel\Documents\World Stuff\HWFWM Compendium"
st = base + r"\src\Source_Text"
idx = json.load(open("chapter_index.json"))
files = {}
for n, l in idx.items():
    for (num, title, fn, nl, m) in l:
        files[(int(n), num)] = (os.path.join(st, "Book_%02d" % int(n), fn), title)
cache = {}
def lines(n, ch):
    k = (n, ch)
    if k not in cache:
        if k not in files:
            cache[k] = None
        else:
            cache[k] = (open(files[k][0], encoding="utf-8").read().split("\n"), files[k][1])
    return cache[k]
STOP = set("the and was were that this with from have had his her their they for are not but who which when after before into over under about also than then there here him them its out one two".split())
def terms(t):
    return {w for w in re.findall(r"[a-z]{4,}", t.lower().replace("\u2019", "'")) if w not in STOP}
CIT = re.compile(r"Book (\d+), Ch(\d+) L(\d+)(?:-(\d+))?")
NOTE = re.compile(r"notes?,? Books? [\d, and-]+|notes, Book \d+")
skipdocs = set(sys.argv[1:])
newfiles = []
for folder in ("07_Characters", "04_Peoples_and_Cultures", "09_Items_and_Artefacts", "10_Roleplay_Support"):
    for fn0 in sorted(os.listdir(base + "\\" + folder)):
        if not fn0.endswith(".md"):
            continue
        t = open(base + "\\" + folder + "\\" + fn0, encoding="utf-8").read()
        if len(t.split("\n")) > 2 and "facts carry a reference" in t.split("\n")[2]:
            newfiles.append((folder + "/" + fn0, t))
rows = []
low = []
for fn, t in newfiles:
    for ln in t.split("\n"):
        if not ln.startswith("- "):
            continue
        cits = CIT.findall(ln)
        claim = re.sub(r"\s*\([^()]*(Book \d+, Ch\d+ L\d+|notes)[^()]*\)", "", ln[2:]).strip()
        for (b, c, lo, hi) in cits:
            b, c, lo = int(b), int(c), int(lo)
            hi = int(hi) if hi else lo
            ch = lines(b, c)
            if ch is None:
                low.append((fn, "NO CHAPTER", b, c, lo, claim[:80]))
                continue
            txt = " ".join(ch[0][max(0, lo - 1):hi + 1])
            ct = terms(claim)
            lt = terms(txt)
            frac = len(ct & lt) / max(1, len(ct))
            conf = "verified"
            if frac < 0.2:
                low.append((fn, round(frac, 2), b, c, lo, claim[:90]))
            rows.append(dict(doc=fn, sec="", claim=claim[:300], tag="Book %d" % b, tier="book", book=str(b), ch=c, title=ch[1], lo=lo, hi=hi, score=round(frac, 2), method="written", state=False, conf=conf, note=""))
        if not cits and "notes" in ln:
            m = re.search(r"notes, Books? (\d+)", ln)
            if m:
                rows.append(dict(doc=fn, sec="", claim=claim[:300], tag="notes, Book " + m.group(1), tier="notes", book=m.group(1), ch=None, title="(from chapter notes)", lo=None, hi=None, score=0, method="notes", state=False, conf="notes-confirmed", note="b" + m.group(1)))

exec(open("tlrows.py", encoding="utf-8").read())
exec(open("allrows.py", encoding="utf-8").read())
json.dump(rows, open("new_rows.json", "w"))
print(len(newfiles), "files;", len(rows), "rows;", len(low), "low-overlap")
for x in low:
    print(x)

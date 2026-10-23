import sys, re, json, glob, os, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
base = r"C:\Users\Gabriel\AppData\Local\Temp\claude\C--Users-Gabriel-Documents-Gmod-Projects-Gmod-Decompilation\08b70dbf-6f0b-4b6b-a18f-242cc3f1fe96\scratchpad"
books = {os.path.basename(f)[:-4]: open(f, encoding="utf-8", errors="replace").read() for f in glob.glob(base + r"\books\b*.txt")}
notes = {os.path.basename(f)[:-3]: open(f, encoding="utf-8", errors="replace").read() for f in glob.glob(base + r"\notes\b*.md")}
wiki = json.load(open(base + r"\wiki\pages.json", encoding="utf-8", errors="replace"))
wpages = wiki.items() if isinstance(wiki, dict) else [(str(i), v) for i, v in enumerate(wiki)]
wtexts = []
for k, v in wpages:
    t = v if isinstance(v, str) else json.dumps(v, ensure_ascii=False)
    wtexts.append((str(k)[:40], t))

def snip(text, m, w=110):
    a = max(0, m.start() - w)
    b = min(len(text), m.end() + w)
    return text[a:b].replace("\n", " ")

def search(term, maxshow=2):
    rx = re.compile(term, re.I)
    print("=== %s" % term)
    for name, store in (("BOOK", books), ("NOTES", notes)):
        hits = []
        total = 0
        for k in sorted(store, key=lambda x: int(re.sub(r"\D", "", x) or 0)):
            ms = list(rx.finditer(store[k]))
            total += len(ms)
            if ms and len(hits) < maxshow:
                hits.append("%s: %s" % (k, snip(store[k], ms[0])))
        print("  %s total=%d" % (name, total))
        for h in hits:
            print("    -", h[:330])
    total = 0
    hits = []
    for title, t in wtexts:
        ms = list(rx.finditer(t))
        total += len(ms)
        if ms and len(hits) < maxshow:
            hits.append("%s: %s" % (title, snip(t, ms[0])))
    print("  WIKI total=%d" % total)
    for h in hits:
        print("    -", h[:330])

for term in sys.argv[1:]:
    search(term)

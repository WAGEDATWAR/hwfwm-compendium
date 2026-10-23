import sys, re, json, glob, os, io, collections, pickle
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
base = r"C:\Users\Gabriel\AppData\Local\Temp\claude\C--Users-Gabriel-Documents-Gmod-Projects-Gmod-Decompilation\08b70dbf-6f0b-4b6b-a18f-242cc3f1fe96\scratchpad"
cache = base + r"\audit_index.pkl"

WORD = re.compile(r"[a-z0-9][a-z0-9'’\-]*")

def norm(t):
    return t.lower().replace("’", "'")

def build():
    wins = []  # (tier, label, text)
    for f in sorted(glob.glob(base + r"\books\b*.txt")):
        lab = os.path.basename(f)[:-4]
        for ln in open(f, encoding="utf-8", errors="replace"):
            ln = ln.strip()
            if len(ln) > 20:
                if len(ln) > 900:
                    for i in range(0, len(ln), 500):
                        wins.append(("B", lab, norm(ln[i:i + 900])))
                else:
                    wins.append(("B", lab, norm(ln)))
    for f in sorted(glob.glob(base + r"\notes\b*.md")):
        lab = os.path.basename(f)[:-3]
        for ln in open(f, encoding="utf-8", errors="replace"):
            ln = ln.strip()
            if len(ln) > 20:
                for i in range(0, len(ln), 350):
                    wins.append(("N", lab, norm(ln[i:i + 700])))
    w = json.load(open(base + r"\wiki\pages.json", encoding="utf-8", errors="replace"))
    items = w.items() if isinstance(w, dict) else enumerate(w)
    for k, v in items:
        t = v if isinstance(v, str) else json.dumps(v, ensure_ascii=False)
        t = t.replace("\\n", "\n")
        for ln in t.split("\n"):
            ln = ln.strip()
            if len(ln) > 20:
                for i in range(0, len(ln), 350):
                    wins.append(("W", str(k)[:30], norm(ln[i:i + 700])))
    inv = collections.defaultdict(set)
    for idx, (_, _, tx) in enumerate(wins):
        for tok in set(WORD.findall(tx)):
            inv[tok].add(idx)
    return wins, dict(inv)

if os.path.exists(cache):
    wins, inv = pickle.load(open(cache, "rb"))
else:
    wins, inv = build()
    pickle.dump((wins, inv), open(cache, "wb"))

STOP = set("the a an and or of to in on at for with by from as is are was were be been it its this that these those his her their they he she we you i not but if then than so such into about over under up down out also may can could would should will shall has have had do does did one two three four five first second third other more most some any all each every many much very just only often usually later still both between during after before until while who whom which what when where why how there here s".split())

def terms_of(claim):
    toks = WORD.findall(norm(claim))
    out = []
    for t in toks:
        t2 = t.strip("-'")
        if len(t2) < 3 or t2 in STOP:
            continue
        if t2 in inv:
            out.append(t2)
        else:
            # singular/plural light stemming
            if t2.endswith("s") and t2[:-1] in inv:
                out.append(t2[:-1])
            else:
                out.append("§" + t2)  # unseen
    return out

def check(claim, k=int(os.environ.get('K','5'))):
    terms = terms_of(claim)
    seen = [t for t in terms if not t.startswith("§")]
    unseen = [t[1:] for t in terms if t.startswith("§")]
    # choose rarest k seen terms
    seen = sorted(set(seen), key=lambda t: len(inv[t]))[:k]
    if not seen:
        return "?", 0, 0, unseen
    cnt = collections.Counter()
    for t in seen:
        for i in inv[t]:
            cnt[i] += 1
    best = {}
    for i, c in cnt.items():
        tier = wins[i][0]
        if tier not in best or c > best[tier]:
            best[tier] = c
    FR = float(os.environ.get('FR','0.6'))
    need = max(2, int(len(seen) * FR + 0.5)) if len(seen) >= 2 else 1
    for tier in ("B", "N", "W"):
        if best.get(tier, 0) >= need:
            return tier, best[tier], len(seen), unseen
    return "-", max(best.values()) if best else 0, len(seen), unseen

def sentences(text):
    out = []
    for para in text.split("\n"):
        p = para.strip()
        if not p or p.startswith("#") or p.startswith("|---") or p.startswith("---"):
            continue
        for s in re.split(r"(?<=[.;:])\s+(?=[A-Z*\[(\"])", p):
            s = s.strip()
            if len(s) > 25:
                out.append(s)
    return out

if __name__ == "__main__":
    path = sys.argv[1]
    mode = sys.argv[2] if len(sys.argv) > 2 else "bad"
    text = open(path, encoding="utf-8").read()
    n = collections.Counter()
    for s in sentences(text):
        tier, c, k, unseen = check(s)
        n[tier] += 1
        show = (mode == "all") or (mode == "bad" and tier in ("-", "?", "W", "N")) or (mode == "none" and tier in ("-", "?"))
        if show:
            print("[%s %d/%d]%s %s" % (tier, c, k, (" UNSEEN:" + ",".join(unseen[:4])) if unseen else "", s[:330]))
    print("SUMMARY", dict(n))

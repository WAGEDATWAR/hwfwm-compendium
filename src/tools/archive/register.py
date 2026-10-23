import re, os, json, math, collections
base = r"C:\Users\Gabriel\Documents\World Stuff\HWFWM Compendium"
st = base + r"\src\Source_Text"
idx = json.load(open("chapter_index.json"))

def norm(t):
    t = t.lower()
    t = re.sub(r"[\u2018\u2019\u201c\u201d\ufffd`]", "'", t)
    return t

WORD = re.compile(r"[a-z0-9][a-z0-9'\-]*")
STOP = set("the a an and or of to in on at for with by from as is are was were be been it its this that these those his her their they he she we you not but if then than so such into about over under up down out also may can could would should will has have had do does did one two three four five first second third other more most some any all each every many much very just only often usually later still both between during after before until while who which what when where there here book books notes note wiki confirmed chapter ch".split())

# load chapters: per book list of (num,title,fn,lines(norm))
chapters = {}
for n in range(1, 14):
    lst = []
    for (num, title, fn, nl, merged) in idx[str(n)]:
        txt = open(os.path.join(st, "Book_%02d" % n, fn), encoding="utf-8").read().split("\n")
        lst.append((num, title, fn, txt))
    chapters[n] = lst

# idf per book over paragraph lines (+ title line offset: file line 1 is header, so file line = index+1)
df = {}
inv = {}  # book -> term -> set of (ci, li)
for n, lst in chapters.items():
    d = collections.Counter()
    iv = collections.defaultdict(list)
    total = 0
    for ci, (num, title, fn, lines) in enumerate(lst):
        for li, ln in enumerate(lines):
            if len(ln) < 15:
                continue
            total += 1
            for w in set(WORD.findall(norm(ln))):
                d[w] += 1
                iv[w].append((ci, li))
    df[n] = (d, total)
    inv[n] = iv

def terms(claim):
    out = []
    for w in WORD.findall(norm(claim)):
        w = w.strip("-'")
        if len(w) < 3 or w in STOP:
            continue
        out.append(w)
    return list(dict.fromkeys(out))

def locate(claim, n):
    lst = chapters[n]
    # exact quote
    for q in re.findall(r"[\u201c\"]([^\u201d\"]{12,})[\u201d\"]", claim):
        qn = norm(q).strip(" .,!?")
        if len(qn) < 12:
            continue
        for ci, (num, title, fn, lines) in enumerate(lst):
            for li, ln in enumerate(lines):
                if qn in norm(ln):
                    return num, title, li + 1, li + 1, 1.0, "quote"
    d, total = df[n]
    iv = inv[n]
    ts = [t for t in terms(claim) if t in d]
    if not ts:
        return None
    w = {t: math.log((total + 1) / (d[t] + 1)) for t in ts}
    ts = sorted(ts, key=lambda t: -w[t])[:10]
    denom = sum(w[t] for t in ts)
    cand = collections.defaultdict(set)
    for t in ts:
        if d[t] > 400:
            continue
        for (ci, li) in iv[t]:
            cand[(ci, li // 3)].add(t)
            cand[(ci, li // 3 - 1)].add(t)
    best = None
    for key, s in cand.items():
        sc = sum(w[t] for t in s) / denom
        if best is None or sc > best[0]:
            best = (sc, key)
    if not best:
        return None
    sc, (ci, blk) = best
    num, title, fn, lines = lst[ci]
    lo = max(0, blk * 3)
    # tighten to lines that contain any matched term
    hits = [li for li in range(lo, min(len(lines), lo + 6)) if any(t in norm(lines[li]) for t in ts)]
    if hits:
        lo, hi = hits[0] + 1, hits[-1] + 1
    else:
        lo, hi = lo + 1, lo + 3
    return num, title, lo, hi, round(sc, 2), "terms"

TAG = re.compile(r"\(((?:Books?|notes?|chapter notes|wiki)[^()]*)\)", re.I)
BOOKS = re.compile(r"Books? ((?:\d+(?:\s*[-–]\s*\d+)?(?:,\s*|\s+and\s+|\s*&\s*)?)+)")
STATE = re.compile(r"\b(die[sd]?|killed|kills|death|dead|becomes|became|gains?|gained|loses|lost|reach(?:es|ed)?|promot\w+|born|married|engaged|joins?|joined|leaves|left|returns?|returned|evolves?|evolved|replaced|destroyed|created|founded|arrives?|arrived|sealed|freed|captured|demoted)\b", re.I)

skip = {"TODO_Verification.md", "Change_Log.md", "00_Project_Structure.md", "Source_Map.md", "Source_Register.md"}
rows = []
for root, dirs, files in os.walk(base):
    if "Source_Text" in root:
        continue
    for f in sorted(files):
        if not f.endswith(".md") or f in skip:
            continue
        p = os.path.join(root, f)
        rel = os.path.relpath(p, base).replace("\\", "/")
        text = open(p, encoding="utf-8").read()
        section = ""
        for ln in text.split("\n"):
            if ln.startswith("#"):
                section = ln.lstrip("# ").strip()[:60]
                continue
            if not TAG.search(ln):
                continue
            # split line into clauses ending at tag
            pieces = re.split(r"(?<=\))(?=[;.]\s|\s+[A-Z*])", ln)
            for pc in re.split(r"(?<=[.;])\s+(?=[A-Z*\[(\"\u201c])", ln):
                for m in TAG.finditer(pc):
                    tag = m.group(1)
                    bm = BOOKS.search(tag)
                    if not bm:
                        continue
                    nums = []
                    for part in re.split(r",|\band\b|&", bm.group(1)):
                        part = part.strip()
                        if re.match(r"^\d+\s*[-–]\s*\d+$", part):
                            a, b = re.split(r"[-–]", part)
                            nums += list(range(int(a), int(b) + 1))
                        elif part.isdigit():
                            nums.append(int(part))
                    nums = [x for x in nums if 1 <= x <= 13]
                    claim = TAG.sub("", pc).strip(" -*")
                    claim = re.sub(r"\*\*|\s+", " ", claim).strip()
                    if len(claim) < 15:
                        continue
                    tier = "book" if re.match(r"(?i)books?", tag) and "notes" not in tag.lower() and "wiki" not in tag.lower() else ("notes" if "notes" in tag.lower() else "wiki")
                    if len(nums) > 3:
                        loc = [(None, None, None, None, 0, "range")]
                        nums_use = nums
                        rows.append(dict(doc=rel, sec=section, claim=claim[:300], tag=tag, tier=tier, book=",".join(map(str, nums)), ch=None, title="(multi-book tag; not auto-located)", lo=None, hi=None, score=0, method="range", state=bool(STATE.search(claim))))
                        continue
                    for n in nums:
                        r = locate(claim, n)
                        if r:
                            num, title, lo, hi, sc, how = r
                            rows.append(dict(doc=rel, sec=section, claim=claim[:300], tag=tag, tier=tier, book=str(n), ch=num, title=title, lo=lo, hi=hi, score=sc, method=how, state=bool(STATE.search(claim))))
                        else:
                            rows.append(dict(doc=rel, sec=section, claim=claim[:300], tag=tag, tier=tier, book=str(n), ch=None, title="(not located)", lo=None, hi=None, score=0, method="none", state=bool(STATE.search(claim))))
json.dump(rows, open("register_rows.json", "w"))
print(len(rows), collections.Counter(r["method"] for r in rows), sum(1 for r in rows if r["score"] >= 0.7), sum(1 for r in rows if r["state"]))

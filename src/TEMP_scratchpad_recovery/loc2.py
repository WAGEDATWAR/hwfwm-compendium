import re, os, sys, json, math
sys.stdout = __import__("io").TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
exec(open("newrows.py", encoding="utf-8").read().split("skipdocs")[0])
# usage: python3 loc2.py BOOK specfile ; spec lines "ChA[-ChB] || description"
b = int(sys.argv[1])
K = int(os.environ.get("K", "2")); W = int(os.environ.get("W", "190"))
chs = sorted(c for (bb, c) in files if bb == b)
df = {}
N = 0
paras = {}
for c in chs:
    ls = lines(b, c)[0]
    paras[c] = [(i + 1, l) for i, l in enumerate(ls) if i >= 2 and l.strip()]
    for (i, l) in paras[c]:
        N += 1
        for t in terms(l):
            df[t] = df.get(t, 0) + 1
def idf(t):
    return math.log((N + 1) / (df.get(t, 0) + 1)) + 0.1
for spec in open(sys.argv[2], encoding="utf-8").read().split("\n"):
    spec = spec.strip()
    if not spec or spec.startswith("#"):
        continue
    chs_s, desc = [s.strip() for s in spec.split("||", 1)]
    m = re.match(r"(\d+)(?:-(\d+))?$", chs_s)
    lo, hi = int(m.group(1)), int(m.group(2) or m.group(1))
    dt = terms(desc)
    tot = sum(idf(t) for t in dt) or 1
    best = []
    for c in range(lo, hi + 1):
        for (i, l) in paras.get(c, []):
            lt = terms(l)
            sc = sum(idf(t) for t in dt & lt) / tot
            if sc > 0:
                best.append((sc, c, i, l))
    best.sort(key=lambda x: -x[0])
    print("[%s | %s]" % (chs_s, desc[:70]))
    for sc, c, i, l in best[:K]:
        print("   %.2f Ch%d L%d: %s" % (sc, c, i, l[:W].replace("\n", " ")))

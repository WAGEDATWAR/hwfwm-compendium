import re, os, json, sys
sys.stdout = __import__("io").TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
exec(open("newrows.py", encoding="utf-8").read().split("skipdocs")[0])
reg = json.load(open("register_final.json"))
by = {}
for r in reg:
    if r.get("ch") and r["conf"] in ("verified",) and "Master_Timeline" not in r["doc"]:
        by.setdefault((int(r["book"]), r["ch"]), []).append(r)
CUE = [
 (1, re.compile(r"\b(\w+) (years?|decades?) (later|ago|since|before|after|earlier|had passed)", re.I)),
 (2, re.compile(r"\b(\w+) months? (later|ago|since|before|after|earlier|had passed|old)|\bmonths? (had passed|later|ago)", re.I)),
 (3, re.compile(r"\b(\w+) weeks? (later|ago|since|before|after|earlier|had passed)|\b(next|following|last) (week|month|year)", re.I)),
 (4, re.compile(r"\b(spring|summer|autumn|winter)\b|\b(\w+) days? (later|ago|since|before|after|earlier|had passed)|\b(next|following) (day|morning)\b|\bthree days\b", re.I)),
]
b = int(sys.argv[1])
lo_ch = int(sys.argv[2]) if len(sys.argv) > 2 else 0
hi_ch = int(sys.argv[3]) if len(sys.argv) > 3 else 9999
nums = sorted(c for (bb, c) in files if bb == b and lo_ch <= c <= hi_ch)
for c in nums:
    ch = lines(b, c)
    ls, title = ch
    print("## B%d Ch%d %s" % (b, c, title))
    # opening
    for i in range(2, min(len(ls), 8)):
        if ls[i].strip():
            print("  OPEN L%d: %s" % (i + 1, ls[i].strip()[:240]))
            break
    # cues
    hits = []
    for pr, rx in CUE:
        for i, l in enumerate(ls[2:], 3):
            m = rx.search(l)
            if m:
                s = max(0, m.start() - 70)
                hits.append((pr, i, l[s:m.end() + 60].replace("\n", " ")))
    hits.sort(key=lambda x: (x[0], x[1]))
    seen = 0
    for pr, i, t in hits[:3]:
        print("  CUE L%d: ...%s..." % (i, t))
    for r in sorted(by.get((b, c), []), key=lambda r: r["lo"] or 0)[:6]:
        print("  REG L%s [%s]: %s" % (r["lo"], r["doc"].split("/")[-1][:-3], r["claim"][:150]))

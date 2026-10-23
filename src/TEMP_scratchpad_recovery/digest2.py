import re, os, json, sys
sys.stdout = __import__("io").TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
exec(open("newrows.py", encoding="utf-8").read().split("skipdocs")[0])
CUE = [
 (1, re.compile(r"\b(\w+) (years?|decades?) (later|ago|since|before|after|earlier|had passed)", re.I)),
 (2, re.compile(r"\b(\w+) months? (later|ago|since|before|after|earlier|had passed|old)|\bmonths? (had passed|later|ago)", re.I)),
 (3, re.compile(r"\b(\w+) weeks? (later|ago|since|before|after|earlier|had passed)|\b(next|following|last) (week|month|year)", re.I)),
 (4, re.compile(r"\b(spring|summer|autumn|winter)\b|\b(\w+) days? (later|ago|since|before|after|earlier|had passed)", re.I)),
]
b = int(sys.argv[1])
lo_ch = int(sys.argv[2]) if len(sys.argv) > 2 else 0
hi_ch = int(sys.argv[3]) if len(sys.argv) > 3 else 9999
N = int(os.environ.get("N", "2")); W = int(os.environ.get("W", "250"))
nums = sorted(c for (bb, c) in files if bb == b and lo_ch <= c <= hi_ch)
for c in nums:
    ls, title = lines(b, c)
    body = [(i + 1, l.strip()) for i, l in enumerate(ls) if i >= 2 and l.strip()]
    print("## Ch%d %s (%d lines)" % (c, title, len(ls)))
    shown = set()
    for (i, l) in body[:N]:
        print("  L%d: %s" % (i, l[:W])); shown.add(i)
    hits = []
    for pr, rx in CUE:
        for (i, l) in body:
            m = rx.search(l)
            if m and i not in shown:
                s = max(0, m.start() - 60)
                hits.append((pr, i, l[s:m.end() + 50]))
    hits.sort(key=lambda x: (x[0], x[1]))
    for pr, i, t in hits[:2]:
        print("  cue L%d: ..%s.." % (i, t))
    if len(body) > N:
        for (i, l) in body[-N:]:
            if i not in shown:
                print("  L%d: %s" % (i, l[:W]))

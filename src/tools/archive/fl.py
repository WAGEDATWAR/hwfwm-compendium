import re, os, sys, json
sys.stdout = __import__("io").TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
exec(open("newrows.py", encoding="utf-8").read().split("skipdocs")[0])
# usage: python3 fl.py BOOK specfile ; spec lines: "key || ChA[-ChB] || regex"
b = int(sys.argv[1])
W = int(os.environ.get("W", "170")); K = int(os.environ.get("K", "2"))
for spec in open(sys.argv[2], encoding="utf-8").read().split("\n"):
    spec = spec.strip()
    if not spec or spec.startswith("#"):
        continue
    key, chs, rx = [s.strip() for s in spec.split("||")]
    m = re.match(r"(\d+)(?:-(\d+))?$", chs)
    lo, hi = int(m.group(1)), int(m.group(2) or m.group(1))
    R = re.compile(rx, re.I)
    out = []
    for c in range(lo, hi + 1):
        ch = lines(b, c)
        if not ch:
            continue
        for i, l in enumerate(ch[0][2:], 3):
            mm = R.search(l)
            if mm:
                s = max(0, mm.start() - 60)
                out.append("Ch%d L%d: %s" % (c, i, l[s:s + W].replace("\n", " ")))
                if len(out) >= K:
                    break
        if len(out) >= K:
            break
    print("[%s]" % key)
    for o in out:
        print("   " + o)
    if not out:
        print("   -- none")

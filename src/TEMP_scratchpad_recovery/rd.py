import sys, os, re, glob
st = r"C:\Users\Gabriel\Documents\World Stuff\HWFWM Compendium\src\Source_Text"
sys.stdout = __import__("io").TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
def path(b, c):
    return glob.glob(os.path.join(st, "Book_%02d" % b, "Ch_%03d_*.txt" % c)) or glob.glob(os.path.join(st, "Book_%02d" % b, "Ch_%d_*.txt" % c))
if sys.argv[1] == "r":   # rd.py r B C [lo hi] [W]
    b, c = int(sys.argv[2]), int(sys.argv[3])
    lo = int(sys.argv[4]) if len(sys.argv) > 4 else 1
    hi = int(sys.argv[5]) if len(sys.argv) > 5 else 99999
    W = int(sys.argv[6]) if len(sys.argv) > 6 else 700
    f = path(b, c)[0]
    for i, l in enumerate(open(f, encoding="utf-8").read().split("\n"), 1):
        if lo <= i <= hi and l.strip():
            print(f"{i}: {l[:W]}")
elif sys.argv[1] == "g":  # rd.py g REGEX B1 B2 [W] [maxhits]
    rx = re.compile(sys.argv[2], re.I)
    b1, b2 = int(sys.argv[3]), int(sys.argv[4])
    W = int(sys.argv[5]) if len(sys.argv) > 5 else 300
    mx = int(sys.argv[6]) if len(sys.argv) > 6 else 80
    n = 0
    for b in range(b1, b2 + 1):
        d = os.path.join(st, "Book_%02d" % b)
        for fn in sorted(os.listdir(d)):
            c = int(re.match(r"Ch_(\d+)_", fn).group(1))
            for i, l in enumerate(open(os.path.join(d, fn), encoding="utf-8").read().split("\n"), 1):
                if rx.search(l):
                    m = rx.search(l); s = max(0, m.start() - W // 3)
                    print(f"B{b} Ch{c} L{i}: {l[s:s+W]}"); n += 1
                    if n >= mx: sys.exit()

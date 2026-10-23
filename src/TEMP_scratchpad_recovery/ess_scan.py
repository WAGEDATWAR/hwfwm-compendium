import re, os, collections, sys
st = r"C:\Users\Gabriel\Documents\World Stuff\HWFWM Compendium\src\Source_Text"
rx = re.compile(r"\b([A-Z][a-z]+(?: [A-Z][a-z]+)?|[a-z]+) essences?\b")
cnt = collections.Counter(); first = {}
for b in range(1, 14):
    d = os.path.join(st, "Book_%02d" % b)
    for fn in sorted(os.listdir(d)):
        m = re.match(r"Ch_(\d+)_", fn)
        ch = int(m.group(1))
        for i, l in enumerate(open(os.path.join(d, fn), encoding="utf-8").read().split("\n"), 1):
            for mm in rx.finditer(l):
                w = mm.group(1).lower()
                cnt[w] += 1
                first.setdefault(w, (b, ch, i))
for w, c in cnt.most_common(400):
    print(c, w, first[w])

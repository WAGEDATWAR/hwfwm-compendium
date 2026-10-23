import os
base = r"C:\Users\Gabriel\Documents\World Stuff\HWFWM Compendium"
log = []

def rep(doc, pairs):
    p = os.path.join(base, doc.replace("/", "\\"))
    t = open(p, encoding="utf-8").read()
    for old, new in pairs:
        n = t.count(old)
        if n != 1:
            print("!! %s: %d matches for %r" % (doc, n, old[:70]))
            continue
        t = t.replace(old, new)
        log.append((doc, new))
    open(p, "w", encoding="utf-8").write(t)

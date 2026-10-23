import re, sys, os, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
base = r"C:\Users\Gabriel\Documents\World Stuff\HWFWM Compendium"
CITED = re.compile(r"Ch\d+ L\d+")
KEY = re.compile(r"Books? \d|notes|wiki")

def groups(ln):
    out = []
    stack = []
    for i, ch in enumerate(ln):
        if ch == "(":
            stack.append(i)
        elif ch == ")" and stack:
            s = stack.pop()
            if not stack:
                out.append((s, i + 1))
    return out

def old_tags(ln):
    res = []
    for s, e in groups(ln):
        g = ln[s:e]
        if KEY.search(g) and not CITED.search(g):
            res.append((s, e, g))
    return res

if __name__ == "__main__":
    nowiki = "--nowiki" in sys.argv
    for doc in [a for a in sys.argv[1:] if not a.startswith("--")]:
        p = os.path.join(base, doc.replace("/", "\\"))
        for i, ln in enumerate(open(p, encoding="utf-8").read().split("\n"), 1):
            if ln.startswith(("Status:", "Spoiler", "Sources:", "Related:", "Valid")):
                continue
            ts = [t for t in old_tags(ln) if not (nowiki and t[2] == "(wiki)")]
            if not ts:
                continue
            print("%s:%d" % (os.path.basename(doc), i))
            for s, e, g in ts:
                st = ln.rfind(". ", 0, s)
                st = max(st + 2, s - 260, 0)
                print("   [%s] ...%s" % (g[:140], ln[st:s]))

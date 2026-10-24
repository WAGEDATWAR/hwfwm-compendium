"""Gather a reading dossier for one character from the chapter files (build plan item 2E.4).
Usage: python3 dossier.py "REGEX" [per_band]
Prints mention counts by book, then per book band (1-3, 4-6, 7-9, 10-13): narration lines that open with the name,
appearance lines, and lines naming relatives or ranks, each with its cite. A reading aid, not output for the files."""
import re, os, io, sys

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
HERE = os.path.dirname(os.path.abspath(__file__))
ST = os.path.abspath(os.path.join(HERE, "..", "Source_Text"))
rx = re.compile(sys.argv[1])
per = int(sys.argv[2]) if len(sys.argv) > 2 else 8
APP = re.compile(r"\b(hair|eyes|tall|short|skin|wore|dressed|build|face|scales|robes|armour|beard|smile|voice|accent|grin|frame|muscular|slender|elf|leonid|celestine|human)\b", re.I)
REL = re.compile(r"\b(mother|father|son|daughter|wife|husband|brother|sister|uncle|aunt|nephew|niece|friend|rival|enemy|boss|teammate|lover|girlfriend|boyfriend|cousin|grandfather|grandmother|ex-)\b", re.I)
bands = {"1-3": (1, 3), "4-6": (4, 6), "7-9": (7, 9), "10-13": (10, 13)}
counts = {}
data = {k: {"open": [], "app": [], "rel": []} for k in bands}
for b in range(1, 14):
    d = os.path.join(ST, "Book_%02d" % b)
    for fn in sorted(os.listdir(d)):
        ch = int(re.match(r"Ch_(\d+)_", fn).group(1))
        for i, l in enumerate(open(os.path.join(d, fn), encoding="utf-8").read().split("\n"), 1):
            m = rx.search(l)
            if not m:
                continue
            counts[b] = counts.get(b, 0) + 1
            band = next(k for k, (lo, hi) in bands.items() if lo <= b <= hi)
            cite = "B%d Ch%d L%d" % (b, ch, i)
            t = l.strip()[:300]
            if m.start() < 40 and len(l) > 90 and not l.lstrip().startswith("“"):
                data[band]["open"].append((cite, t))
            if APP.search(l) and len(l) > 80 and not l.lstrip().startswith("“"):
                data[band]["app"].append((cite, t))
            if REL.search(l) and len(l) > 70:
                data[band]["rel"].append((cite, t))
print("MENTIONS by book:", dict(sorted(counts.items())), "total", sum(counts.values()))


def pick(lst, n):
    if len(lst) <= n:
        return lst
    step = len(lst) / n
    return [lst[int(i * step)] for i in range(n)]


for k in bands:
    for kind in ("open", "app", "rel"):
        lst = data[k][kind]
        if not lst:
            continue
        print("--- %s %s (%d)" % (k, kind, len(lst)))
        for cite, t in pick(lst, per if kind != "rel" else max(3, per // 2)):
            print(cite + ": " + t)

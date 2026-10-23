"""List the weak register rows with the text of the lines they cite (used by build plan item 1.3)."""
import json, os, sys, io
HERE = os.path.dirname(os.path.abspath(__file__))
BASE = os.path.abspath(os.path.join(HERE, "..", ".."))


def line(b, c, lo, hi):
    d = os.path.join(BASE, "src", "Source_Text", "Book_%02d" % b)
    f = [x for x in os.listdir(d) if x.startswith("Ch_%03d_" % c) or x.startswith("Ch_%04d_" % c)]
    t = open(os.path.join(d, f[0]), encoding="utf-8").read().split("\n")
    return " / ".join(t[i - 1][:300] for i in range(lo, min(hi, lo + 2) + 1) if i - 1 < len(t))


if __name__ == "__main__":
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
    r = json.load(open(os.path.join(HERE, "register_new.json"), encoding="utf-8"))
    n = 0
    for x in r:
        if x["check"] != "weak":
            continue
        n += 1
        print("#%d %s | %s" % (n, x["doc"], x["sec"]))
        print("CLAIM:", x["claim"][:500])
        for ref in x["refs"]:
            print("  B%d Ch%d L%d-%d [%s]: %s" % (ref[0], ref[1], ref[2], ref[3], ref[4], line(ref[0], ref[1], ref[2], ref[3])))
        print()

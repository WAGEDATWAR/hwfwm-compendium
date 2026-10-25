"""List the near-graded register rows of a folder with the text of the lines they cite (build plan item 5.1, manual pass).

Usage: python3 src/tools/near_dump.py DOC_PREFIX [START] [COUNT]
Prints COUNT rows from START (default 0, 40). Each row shows the claim and, for every citation, the cited lines (300 characters each).
"""
import json, os, sys, io
from common import lines, HERE


def main():
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
    pref = sys.argv[1]
    start = int(sys.argv[2]) if len(sys.argv) > 2 else 0
    count = int(sys.argv[3]) if len(sys.argv) > 3 else 40
    rows = [x for x in json.load(open(os.path.join(HERE, "register_new.json"), encoding="utf-8"))
            if x["check"] == "near" and x["doc"].startswith(pref)]
    print("%d near rows under %s" % (len(rows), pref))
    for i, x in enumerate(rows[start:start + count], start):
        print("\n#%d %s | %s" % (i, x["doc"], x["sec"]))
        print("CLAIM:", x["claim"][:600])
        for ref in x["refs"]:
            d = lines(ref[0], ref[1])
            if not d:
                continue
            ls = d[0]
            lo, hi = ref[2], min(ref[3], ref[2] + 3)
            for k in range(lo, hi + 1):
                if k - 1 < len(ls):
                    print("  B%d Ch%d L%d: %s" % (ref[0], ref[1], k, ls[k - 1][:300]))


if __name__ == "__main__":
    main()

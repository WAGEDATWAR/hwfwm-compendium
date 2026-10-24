"""Second-pass verification (build plan item 5.1): an independent check from the word-overlap grade.

For every register row with a book citation it tests, against the cited lines plus two lines either side:
  quote   every quoted string in the claim (6+ characters, split at ellipses) appears in the text;
  number  every number of two or more digits in the claim appears in the text as digits or words;
  name    every capitalised word that is not at the start of a sentence appears in the text (reported only with --names).
Rows carrying a reviewed/wiki/notes grade are skipped. Output: src/tools/verify2_report.md, one block per failing row.

Usage: python3 src/tools/verify2.py [--names] [--doc PREFIX]
"""
import json, os, re, sys
from common import lines, HERE

NUMW = {"twenty": 20, "thirty": 30, "forty": 40, "fifty": 50, "sixty": 60, "seventy": 70, "eighty": 80, "ninety": 90,
        "hundred": 100, "thousand": 1000, "million": 10 ** 6}
UNITS = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9, "ten": 10,
         "eleven": 11, "twelve": 12, "thirteen": 13, "fourteen": 14, "fifteen": 15, "sixteen": 16, "seventeen": 17,
         "eighteen": 18, "nineteen": 19}
NAME_SKIP = set("""Book Chapter Ch The This That These Those When After Before While Jason Level Era Eras Iron Bronze Silver Gold
Diamond Later He She They It His Her Their Its In On At As If But And Or Not No Yes One Two Three Four Five Six Seven Eight Nine Ten
Once Because Since Until Where What Who Why How Both Each Some All Any Most Many Only Even Still Then There Here Now Also
Earth Pallimustus Society Adventure Magic Church Temple Order Guild Council Network Cabal Builder Healer Knowledge""".split())


def norm(t):
    t = t.lower().replace("’", "'").replace("‘", "'").replace("“", '"').replace("”", '"')
    t = t.replace("—", " ").replace("–", " ").replace("…", "...")
    return re.sub(r"[^a-z0-9']+", " ", t).strip()


def window(refs):
    txt = []
    for r in refs:
        b, c, lo, hi = r[0], r[1], r[2], r[3]
        d = lines(b, c)
        if not d:
            continue
        ls = d[0]
        txt.append(" ".join(ls[max(0, lo - 3): min(len(ls), hi + 2)]))
    return " ".join(txt)


def numbers_in(t):
    out = set()
    for m in re.findall(r"\d[\d,]*", t):
        out.add(int(m.replace(",", "")))
    words = re.findall(r"[a-z]+", t.lower())
    for i, w in enumerate(words):
        if w in UNITS:
            out.add(UNITS[w])
        if w in NUMW:
            v = NUMW[w]
            if i and words[i - 1] in UNITS:
                v *= UNITS[words[i - 1]]
            out.add(v)
            if i and words[i - 1] in NUMW and NUMW[words[i - 1]] < v:
                pass
        if w in NUMW and NUMW[w] < 100 and i + 1 < len(words) and words[i + 1] in UNITS:
            out.add(NUMW[w] + UNITS[words[i + 1]])
    return out


def locate(row, phrase):
    """Find a quoted phrase elsewhere in the cited chapters: returns 'Bn Chm Lk' or ''."""
    p = norm(phrase)
    for r in row["refs"]:
        d = lines(r[0], r[1])
        if not d:
            continue
        for i, l in enumerate(d[0]):
            if p in norm(l):
                return "B%d Ch%d L%d" % (r[0], r[1], i + 1)
        for i in range(len(d[0]) - 1):
            if p in norm(d[0][i] + " " + d[0][i + 1]):
                return "B%d Ch%d L%d-%d" % (r[0], r[1], i + 1, i + 2)
    return ""


def best_span(row, phrase):
    """Closest span of the cited window to a phrase: (ratio, raw text)."""
    import difflib
    q = norm(phrase).split()
    if not q:
        return 0.0, ""
    best = (0.0, "")
    for r in row["refs"]:
        d = lines(r[0], r[1])
        if not d:
            continue
        ls = d[0]
        raw = " ".join(ls[max(0, r[2] - 3): min(len(ls), r[3] + 2)]).split()
        nw = [norm(w) for w in raw]
        k = len(q)
        for a in range(len(raw)):
            for n in (k - 1, k, k + 1, k + 2):
                if n < 1 or a + n > len(raw):
                    continue
                s = " ".join(nw[a:a + n]).strip()
                sc = difflib.SequenceMatcher(None, " ".join(q), s).ratio()
                if sc > best[0]:
                    best = (sc, " ".join(raw[a:a + n]))
    return best


def check(row, names):
    claim = row["claim"]
    text = window(row["refs"])
    nt = norm(text)
    fails = []
    for q in ([] if re.search(r"\(notes|, notes|notes, Book|notes", claim) else re.findall(r"[\"“]([^\"”]*)[\"”]", claim)):
        for part in re.split(r"\.\.\.|…", q):
            p = norm(part)
            if len(p) >= 6 and p not in nt:
                loc = locate(row, part)
                sc, sp = best_span(row, part)
                fails.append("quote: " + part.strip()[:80] + (" [found at %s]" % loc if loc else " [not in cited chapters]") + " ~%.2f: %s" % (sc, sp[:100]))
    stripped = re.sub(r"(?i)(?<![a-z])(?:books? \d+(?:\s*(?:-|to|and)\s*\d+)?|ch\d+(?:-\d+)?|L\d+(?:-\d+)?)", " ", claim)
    cn = {n for n in numbers_in(stripped) if n >= 10 and not 2000 <= n <= 2045}
    if cn:
        tn = numbers_in(text)
        miss = sorted(n for n in cn if n not in tn and not (n in range(1900, 2100) and False))
        if miss:
            fails.append("number: " + ", ".join(str(n) for n in miss))
    if names:
        cl = re.sub(r"\([^)]*\)", " ", claim)
        for m in re.finditer(r"(?<![.!?:] )(?<!^)\b([A-Z][a-z]{3,})\b", cl):
            w = m.group(1)
            if w in NAME_SKIP:
                continue
            if w.lower() not in nt:
                fails.append("name: " + w)
    return sorted(set(fails))


def main():
    names = "--names" in sys.argv
    pref = sys.argv[sys.argv.index("--doc") + 1] if "--doc" in sys.argv else ""
    rows = json.load(open(os.path.join(HERE, "register_new.json"), encoding="utf-8"))
    out, n = [], 0
    for r in rows:
        if "misconception" in r["sec"].lower() or r["check"] in ("reviewed", "wiki", "notes") or not r["refs"] or not r["doc"].startswith(pref):
            continue
        n += 1
        f = check(r, names)
        if f:
            out.append((r, f))
    lines_out = ["# Second-pass verification report", "",
                 "Generated by src/tools/verify2.py (build plan item 5.1). %d rows checked, %d flagged." % (n, len(out)), ""]
    for i, (r, f) in enumerate(out, 1):
        lines_out.append("#%d %s | %s" % (i, r["doc"], r["sec"]))
        lines_out.append("  CLAIM: " + r["claim"][:260])
        lines_out.append("  REFS: " + "; ".join("B%d Ch%d L%d-%d" % tuple(x[:4]) for x in r["refs"]))
        lines_out.append("  FLAGS: " + " | ".join(f))
        lines_out.append("")
    open(os.path.join(HERE, "verify2_report.md"), "w", encoding="utf-8", newline="\n").write("\n".join(lines_out) + "\n")
    print("%d rows checked, %d flagged (see src/tools/verify2_report.md)" % (n, len(out)))
    by = {}
    for r, f in out:
        k = r["doc"].split("/")[0]
        by[k] = by.get(k, 0) + 1
    for k in sorted(by, key=by.get, reverse=True):
        print(by[k], k)


if __name__ == "__main__":
    main()

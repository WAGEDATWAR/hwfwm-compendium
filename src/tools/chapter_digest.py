"""Generate 08_History_and_Timeline/Chapter_Digest_Book_NN.md from chapter_index.json and the per-book timelines.

For each chapter the digest lists the number, the (cleaned) title, and up to two sentences taken from the rows of
Book_NN_Timeline.md whose own citation names that chapter. Sentences that quote more than eight words in a row are
skipped, so the digest never reproduces passages. Chapters with no usable sentence are marked "title only".

Usage: python3 src/tools/chapter_digest.py        write all thirteen files
"""
import json, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
BASE = os.path.abspath(os.path.join(HERE, "..", ".."))
HIST = os.path.join(BASE, "08_History_and_Timeline")
IDX = json.load(open(os.path.join(HERE, "chapter_index.json"), encoding="utf-8"))

CITE = re.compile(r"\(Book (\d+), Ch(\d+)(?:[^)]*)\)\s*$")
# Sentences the register marked weak (their cited line does not support them); they are skipped until the
# timeline row is tightened. Keys are (book, chapter, text fragment).
SKIP = [
    (12, 65, "not physically present"),
    (13, 951, "The 2038 date appears"),
]
QUOTE = re.compile(r"[\"“]([^\"”]+)[\"”]")


def clean_title(t):
    t = t.replace("�", "'")
    return re.sub(r"\s+", " ", t).strip()


def split_sentences(cell):
    cell = cell.strip()
    out, buf, depth = [], "", 0
    for i, ch in enumerate(cell):
        buf += ch
        if ch == "(":
            depth += 1
        elif ch == ")":
            depth = max(0, depth - 1)
        elif ch == "." and depth == 0:
            nxt = cell[i + 1:i + 3]
            if nxt == "" or nxt[0] == " ":
                out.append(buf.strip())
                buf = ""
    if buf.strip():
        out.append(buf.strip())
    return out


def long_quote(s):
    return any(len(q.split()) > 8 for q in QUOTE.findall(s))


def rows(book):
    path = os.path.join(HIST, "Book_%02d_Timeline.md" % book)
    res = []
    for line in open(path, encoding="utf-8"):
        if not line.startswith("|"):
            continue
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if len(cells) < 3:
            continue
        res.append(cells[-1])
    return res


def build(book):
    by_ch = {}
    for cell in rows(book):
        for s in split_sentences(cell):
            m = CITE.search(s.rstrip("."))
            if not m or int(m.group(1)) != book:
                # tolerate a cite followed by the full stop
                m = re.search(r"\(Book (\d+), Ch(\d+)[^)]*\)\.?$", s)
                if not m:
                    continue
            if int(m.group(1)) != book:
                continue
            by_ch.setdefault(int(m.group(2)), []).append(s)
    return by_ch


def main():
    for key in sorted(IDX, key=int):
        book = int(key)
        chapters = IDX[key]
        by_ch = build(book)
        covered = 0
        lines = []
        for rec in chapters:
            num, title = rec[0], clean_title(rec[1])
            sents = [s for s in by_ch.get(num, []) if not long_quote(s)
                     and not any(b == book and c == num and frag in s for b, c, frag in SKIP)]
            picked, total = [], 0
            for s in sents:
                if total + len(s) > 420 and picked:
                    break
                picked.append(s)
                total += len(s)
                if len(picked) == 2:
                    break
            if picked:
                covered += 1
                body = " ".join(picked)
            else:
                body = "Title only; no summary yet (Book %d, Ch%d)." % (book, num)
            lines.append("- **Ch%d, %s**: %s" % (num, title, body))
        first, last = chapters[0][0], chapters[-1][0]
        head = """# Chapter Digest: Book %d

Status: Draft (first pass; sentences are taken from Book_%02d_Timeline.md, whose rows cite the chapter lines; chapters marked "title only" have no row yet)
Spoiler level: %s
Valid from: Book %d, Ch%d
Valid through: Book %d, Ch%d
Sources: Book %d (chapter files, via the timeline)
Related: Book_%02d_Timeline.md, Master_Timeline.md, ../Appendices/Source_Map.md

## 1. How to use this digest

One entry per chapter, in book order: the chapter number and title, then up to two sentences from the timeline with their citations. Use it to find which chapter covers an event, then open the chapter file or the timeline for detail. It quotes no passages. Coverage in this book: %d of %d chapters have a summary sentence; the rest are titles only.

## 2. Chapters

""" % (book, book, "1" if book <= 3 else ("2" if book <= 9 else "3"), book, first, book, last, book, book, covered, len(chapters))
        out = os.path.join(HIST, "Chapter_Digest_Book_%02d.md" % book)
        open(out, "w", encoding="utf-8", newline="\n").write(head + "\n".join(lines) + "\n")
        print("Book %d: %d chapters, %d with summary" % (book, len(chapters), covered))


if __name__ == "__main__":
    main()

"""Export the compendium as one Markdown file per spoiler level (build plan item 5.5, Decision 3).

For a requested level N the exporter keeps a document only when its header level is N or lower, cuts every tagged section
(<!-- level:M -->) above N, and then holds back any line (paragraph, bullet or table row) that cites a book of a later level
or names a term listed in lorebook.py as belonging to a later level. That second step is a safety net for summaries that
are written at a lower header level than their last sentences; the held-back lines are written to held_back.txt.

Output: src/exports/markdown/HWFWM_Compendium_level0.md ... level3.md and held_back.txt
Level 0 = public setting, 1 = Books 1-3, 2 = Books 1-9, 3 = Books 1-13.
Usage: python3 src/tools/export_levels.py
"""
import os, re, sys, io
from spoiler_tags import baseline
from lorebook import visible, docs, LEVEL2, LEVEL3, book_level, BASE

OUT = os.path.join(BASE, "src", "exports", "markdown")
EXTRA = ["10_Roleplay_Support", "Appendices/Glossary.md", "Appendices/Name_Index.md", "Appendices/Open_Questions.md",
         "Appendices/Wiki_Reference_Lists.md"]
SKIP = re.compile(r"(^|/)(00_|Chapter_Digest|Book_\d\d_Timeline)")
HEADER = re.compile(r"^(Status|Spoiler level|Valid from|Valid through|Sources|Related):")
LABEL = ["public setting only", "Books 1-3", "Books 1-9", "Books 1-13"]
HELD = []


def doc_list():
    seen = set()
    for rel in docs():
        seen.add(rel)
        yield rel
    for f in EXTRA:
        p = os.path.join(BASE, f)
        if os.path.isfile(p):
            if f not in seen:
                yield f
            continue
        for root, _, files in sorted(os.walk(p)):
            for fn in sorted(files):
                rel = os.path.relpath(os.path.join(root, fn), BASE).replace("\\", "/")
                if fn.endswith(".md") and not SKIP.search(rel) and rel not in seen:
                    yield rel


def too_late(line, level):
    """True when the line cites a book above the level or names a term of a later level."""
    for m in re.finditer(r"Books? (\d+)", line):
        if book_level(int(m.group(1))) > max(level, 1):
            return True
    terms = (LEVEL2 + LEVEL3) if level <= 1 else LEVEL3 if level == 2 else []
    low = line.lower()
    return any(w.lower() in low for w in terms)


def clean_links(line):
    return re.sub(r"\[([^\]]*)\]\([^)]*\.md[^)]*\)", r"\1", line)


def render(rel, text, level):
    lines = visible(text, level)
    out = []
    for l in lines:
        if HEADER.match(l):
            continue
        if level < 3 and l.strip() and not l.startswith("# ") and too_late(l, level):
            HELD.append((level, rel, l.strip()[:90]))
            continue
        if l.startswith("#"):
            l = "#" + l
        out.append(clean_links(l))
    body = "\n".join(out).strip()
    body = re.sub(r"\n{3,}", "\n\n", body)
    return body


def main():
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
    os.makedirs(OUT, exist_ok=True)
    texts = []
    for rel in doc_list():
        t = open(os.path.join(BASE, rel), encoding="utf-8").read()
        texts.append((rel, t, baseline(t)))
    for level in range(4):
        parts, toc, n = [], [], 0
        for rel, t, base in texts:
            if base is None or base > level:
                continue
            body = render(rel, t, level)
            if len(body) < 80:
                continue
            title = body.split("\n", 1)[0].lstrip("# ").strip()
            n += 1
            toc.append("- %s" % title)
            parts.append(body)
        head = ("# He Who Fights With Monsters: Compendium (spoiler level %d, %s)\n\n"
                "Exported from the compendium by `src/tools/export_levels.py`. A derived copy: it is not a source, and the "
                "compendium files are the place to correct anything. It holds %d documents cleared to level %d. Facts carry "
                "the reference form \"Book N, ChX LY\" where the book text shows them; \"notes\" and \"wiki\" mark the lower tiers. "
                "Lines that cite a later book or name a later-level term were held back; see held_back.txt.\n\n"
                "## Contents\n\n%s\n\n---\n\n") % (level, LABEL[level], n, level, "\n".join(toc))
        path = os.path.join(OUT, "HWFWM_Compendium_level%d.md" % level)
        with open(path, "w", encoding="utf-8", newline="\n") as f:
            f.write(head + "\n\n---\n\n".join(parts) + "\n")
        print("level %d: %d documents, %d KB, %d lines held back" % (
            level, n, os.path.getsize(path) // 1024, len([h for h in HELD if h[0] == level])))
    with open(os.path.join(OUT, "held_back.txt"), "w", encoding="utf-8", newline="\n") as f:
        f.write("Lines left out of a lower-level export because they cite a later book or name a later-level term (level, document, start of line).\n")
        for lv, doc, s in sorted(set(HELD)):
            f.write("%d\t%s\t%s\n" % (lv, doc, s))


if __name__ == "__main__":
    main()

"""Spoiler-level tags for sections inside a document.

Tag form (HTML comments, so files read normally):
    <!-- level:2 -->
    ## Later developments
    ...
    <!-- /level -->
Untagged text carries the document's header level (the first digit of its "Spoiler level:" line). A tagged section
has the given level (0-3) and must not be lower than the header level. Tags may nest only when the inner level is
at least the outer level.

Functions
    parse(text)               -> (tags, errors): tags are (start_line, end_line, level) with 1-based lines
    baseline(text)            -> header level as an int, or None for "mixed" and indexes
    retrofit(path, write)     -> proposed (heading, level) tags for sections that are above the header level
Usage: python3 src/tools/spoiler_tags.py [--write]   propose (or apply) tags for headings such as
       "Later developments" or "(Level N)" in every compendium document.
"""
import os, re, sys, io

HERE = os.path.dirname(os.path.abspath(__file__))
BASE = os.path.abspath(os.path.join(HERE, "..", ".."))
OPEN = re.compile(r"^<!--\s*level:(\S+)\s*-->\s*$")
CLOSE = re.compile(r"^<!--\s*/level\s*-->\s*$")
HEADING = re.compile(r"^(#{2,4}) (.+)$")
CITE = re.compile(r"Book (\d+), Ch\d+")


def baseline(text):
    m = re.search(r"^Spoiler level:\s*(\d)", text, re.M)
    return int(m.group(1)) if m else None


def book_level(b):
    return 1 if b <= 3 else 2 if b <= 9 else 3


def parse(text):
    tags, errors, stack = [], [], []
    base = baseline(text)
    for i, ln in enumerate(text.split("\n"), 1):
        m = OPEN.match(ln.strip())
        if m:
            lv = m.group(1)
            if not re.fullmatch(r"[0-3]", lv):
                errors.append((i, "level tag with an invalid level: " + lv))
                lv = None
            else:
                lv = int(lv)
                if base is not None and lv < base:
                    errors.append((i, "tagged level %d is lower than the header level %d" % (lv, base)))
                if stack and stack[-1][1] is not None and lv < stack[-1][1]:
                    errors.append((i, "nested tag level %d is lower than the enclosing level %d" % (lv, stack[-1][1])))
            stack.append((i, lv))
        elif CLOSE.match(ln.strip()):
            if not stack:
                errors.append((i, "closing level tag without an opening tag"))
            else:
                s, lv = stack.pop()
                tags.append((s, i, lv))
    for s, lv in stack:
        errors.append((s, "level tag is never closed"))
    return tags, errors


def propose(text):
    """Headings that should carry a tag: (line_index, depth, level, title)."""
    base = baseline(text)
    if base is None:
        return []
    lines = text.split("\n")
    out = []
    for i, ln in enumerate(lines):
        m = HEADING.match(ln)
        if not m:
            continue
        depth, title = len(m.group(1)), m.group(2)
        if i > 0 and OPEN.match(lines[i - 1].strip()):
            continue
        level = None
        lm = re.search(r"\(Level (\d)(?:\s*[-/]\s*(\d))?", title) or re.search(r"\*\*\(Level (\d)(?:\s*[-/]\s*(\d))?", title)
        if lm:
            level = max(int(g) for g in lm.groups() if g)
        elif re.search(r"Later developments|\(spoilers\)|\(Spoilers\)", title):
            j = i + 1
            while j < len(lines) and not (HEADING.match(lines[j]) and len(HEADING.match(lines[j]).group(1)) <= depth):
                j += 1
            books = [int(b) for b in CITE.findall("\n".join(lines[i:j]))]
            level = book_level(max(books)) if books else None
        if level is not None and level > base:
            out.append((i, depth, level, title))
    return out


def apply(text, props):
    lines = text.split("\n")
    # apply from the bottom so earlier indexes stay valid
    for i, depth, level, title in sorted(props, reverse=True):
        j = i + 1
        while j < len(lines) and not (HEADING.match(lines[j]) and len(HEADING.match(lines[j]).group(1)) <= depth) \
                and not lines[j].startswith("<!-- files:") and not OPEN.match(lines[j].strip()):
            j += 1
        k = j
        while k - 1 > i and lines[k - 1].strip() == "":
            k -= 1
        lines.insert(k, "")
        lines.insert(k + 1, "<!-- /level -->")
        lines.insert(i, "<!-- level:%d -->" % level)
    return "\n".join(lines)


def documents():
    for root, dirs, files in os.walk(BASE):
        dirs[:] = [d for d in dirs if d not in ("src", ".git")]
        for f in files:
            rel = os.path.relpath(os.path.join(root, f), BASE).replace("\\", "/")
            if f.endswith(".md") and rel not in ("00_Project_Structure.md",) and not rel.startswith("TODO") \
                    and rel not in ("Appendices/Source_Register.md", "Appendices/Source_Map.md", "Appendices/Change_Log.md"):
                yield rel


if __name__ == "__main__":
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
    write = "--write" in sys.argv
    n = 0
    for rel in documents():
        p = os.path.join(BASE, *rel.split("/"))
        text = open(p, encoding="utf-8").read()
        props = propose(text)
        if not props:
            continue
        for i, d, lv, t in props:
            print("%s: line %d level %d  %s" % (rel, i + 1, lv, t[:70]))
            n += 1
        if write:
            open(p, "w", encoding="utf-8").write(apply(text, props))
    print(("tagged %d sections" if write else "%d sections to tag (rerun with --write)") % n)

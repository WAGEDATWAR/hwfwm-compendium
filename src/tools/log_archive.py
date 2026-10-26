"""Keep Appendices/Change_Log.md to the current and the previous month (build plan item 5.8).

An entry starts at a bold line that ends with a date, for example "**Title (2026-10-23)**", and runs to the next such line or to
"## Pending index updates". Entries dated before the first day of the previous month move to Appendices/Change_Log_YYYY-MM.md
(created with a header, or appended to), in their original order.

Usage: python3 src/tools/log_archive.py [--today YYYY-MM-DD] [--dry]
"""
import os, re, sys, datetime

HERE = os.path.dirname(os.path.abspath(__file__))
APP = os.path.abspath(os.path.join(HERE, "..", "..", "Appendices"))
ENTRY = re.compile(r"^\*\*.*\((\d{4})-(\d{2})-(\d{2})\)\*\*\s*$")
HEADER = """# Change Log: %s

Status: Working document (closed archive of one month)
Spoiler level: 0 (no setting facts; this is a record of work)
Valid from: %s
Valid through: %s
Sources: project history
Related: Change_Log.md, ../00_Project_Structure.md, ../TODO_Verification.md

Entries of %s moved out of `Change_Log.md` by `src/tools/log_archive.py`. The wording is unchanged.

"""


def main():
    today = datetime.date.today()
    if "--today" in sys.argv:
        today = datetime.date.fromisoformat(sys.argv[sys.argv.index("--today") + 1])
    prev = (today.replace(day=1) - datetime.timedelta(days=1)).replace(day=1)
    path = os.path.join(APP, "Change_Log.md")
    lines = open(path, encoding="utf-8").read().split("\n")
    end = next(i for i, l in enumerate(lines) if l.startswith("## Pending index updates"))
    first = next(i for i, l in enumerate(lines) if ENTRY.match(l))
    blocks, cur = [], None
    for i in range(first, end):
        m = ENTRY.match(lines[i])
        if m:
            cur = [datetime.date(int(m.group(1)), int(m.group(2)), int(m.group(3))), []]
            blocks.append(cur)
        cur[1].append(lines[i])
    move = [b for b in blocks if b[0] < prev]
    keep = [b for b in blocks if b[0] >= prev]
    print("%d entries, %d to archive (before %s), %d kept" % (len(blocks), len(move), prev, len(keep)))
    if not move or "--dry" in sys.argv:
        return
    months = {}
    for d, ls in move:
        months.setdefault((d.year, d.month), []).append("\n".join(ls).strip("\n"))
    for (y, mth), items in sorted(months.items()):
        name = "%04d-%02d" % (y, mth)
        ap = os.path.join(APP, "Change_Log_%s.md" % name)
        body = "\n\n".join(items) + "\n"
        if os.path.exists(ap):
            open(ap, "a", encoding="utf-8", newline="\n").write("\n" + body)
        else:
            open(ap, "w", encoding="utf-8", newline="\n").write(HEADER % (name, name + "-01", name, name) + body)
        print("wrote Change_Log_%s.md (%d entries)" % (name, len(items)))
    new = lines[:first] + ["\n".join(sum((b[1] for b in keep), [])).strip("\n"), ""] + lines[end:]
    note = "Older months are in `Change_Log_YYYY-MM.md` files in this folder."
    text = "\n".join(new)
    if note not in text:
        text = text.replace("\n## Log\n", "\n## Log\n\n" + note + "\n", 1)
    open(path, "w", encoding="utf-8", newline="\n").write(text)


if __name__ == "__main__":
    main()

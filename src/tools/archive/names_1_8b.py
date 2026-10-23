import os, re
B = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", ".."))


def insert_sorted(path, letter, name, line, glossary):
    p = os.path.join(B, *path.split("/"))
    lines = open(p, encoding="utf-8").read().split("\n")
    key = "**%s**" % name
    if any(l.startswith(("- " + key, key)) for l in lines):
        return
    sec = [i for i, l in enumerate(lines) if l.strip() == "## " + letter or (letter in "UVWXYZ" and l.strip() == "## U-Z")][0]
    j, pos, last = sec + 1, None, sec
    pat = r"\*\*(.+?)\*\*" if glossary else r"- \*\*(.+?)\*\*"
    while j < len(lines) and not lines[j].startswith("## "):
        m = re.match(pat, lines[j])
        if m:
            last = j
            if pos is None and m.group(1).lower() > name.lower():
                pos = j
        j += 1
    if glossary:
        if pos is not None:
            lines[pos:pos] = [line, ""]
        else:
            lines[last + 1:last + 1] = ["", line]
    else:
        lines.insert(pos if pos is not None else last + 1, line)
    open(p, "w", encoding="utf-8").write("\n".join(lines))


G = "Appendices/Glossary.md"
N = "Appendices/Name_Index.md"
insert_sorted(G, "A", "Ancestral Majesty", "**Ancestral Majesty**: the form of address for Soramir Rimaros, used by Vesper and Liara (Book 7, Ch21 L65-66) and by a branch director (Book 7, Ch42 L6). **[2]**", True)
insert_sorted(G, "H", "Hump", "**Hump**: a nickname for Humphrey Geller (Book 1, Ch82 L18). **[1]**", True)
insert_sorted(G, "S", "Soph", "**Soph**: a nickname for Sophie Wexler (Book 1, Ch84 L74). **[1]**", True)
insert_sorted(G, "S", "Shades, the", "**Shades, the**: Shade's several bodies speaking as one (Book 2, Ch57 L29). **[1]**", True)
insert_sorted(N, "B", "Bruce Corwin", "- **Bruce Corwin** (B4): joins Jason's party on the aircraft mission and shoots down rockets (Book 4, Ch47 L37-43; Book 4, Ch48 L83).", False)
insert_sorted(N, "C", "Cas Vin Baral", "- **Cas Vin Baral** (B11): silver-rank messenger used for ritual materials by the gold-rankers (Book 11, Ch7 L14; Book 11, Ch12 L56).", False)
insert_sorted(N, "R", "Relia Vin Vala", "- **Relia Vin Vala** (B11): silver-rank messenger, the pick of the bunch (Book 11, Ch13 L4).", False)

# name_scan: more words that are not names
p = os.path.join(B, "src", "tools", "name_scan.py")
s = open(p, encoding="utf-8").read()
if "Mum Americans Batman" not in s:
    s = s.replace("Pallimustus\"\"\".split())", "Pallimustus Mum Americans Batman Voltron Airwolf\"\"\".split())")
    open(p, "w", encoding="utf-8").write(s)
print("ok")

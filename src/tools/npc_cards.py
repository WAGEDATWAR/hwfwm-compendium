"""Generate NPC cards from the character files (build plan item 4.2).

Reads every individual file in 07_Characters (not the group files) and writes four files to
10_Roleplay_Support/NPC_Cards/, banded by the book in which the character first appears (1-3, 4-6, 7-9, 10-13).
Each card has: role (first sentence of the summary), appearance, voice cue, secret or spoiler note, and the valid-from /
valid-through range, all copied from the character file with their citations. Cards whose spoiler level is above the
file's header level are wrapped in level tags. Re-run after editing a character file.

Usage: python3 src/tools/npc_cards.py
"""
import os, re

HERE = os.path.dirname(os.path.abspath(__file__))
BASE = os.path.abspath(os.path.join(HERE, "..", ".."))
CH = os.path.join(BASE, "07_Characters")
OUT = os.path.join(BASE, "10_Roleplay_Support", "NPC_Cards")

SKIP = {"00_Characters_Overview.md", "Jason_Asano.md", "Familiars.md",
        "Baseph_and_the_Rimaros_Children.md", "Hannah_and_Claire_Adeah.md"}
BANDS = [(1, 3, "Books_01-03", "Books 1-3"), (4, 6, "Books_04-06", "Books 4-6"),
         (7, 9, "Books_07-09", "Books 7-9"), (10, 13, "Books_10-13", "Books 10-13")]
TAG_RE = re.compile(r"<!--\s*/?level[^>]*-->")


def clean(t):
    t = TAG_RE.sub("", t)
    t = re.sub(r"\s+", " ", t).strip()
    return t


def sentences(t):
    out, buf, depth = [], "", 0
    for i, ch in enumerate(t):
        buf += ch
        if ch == "(":
            depth += 1
        elif ch == ")":
            depth = max(0, depth - 1)
        elif ch == "." and depth == 0 and (i + 1 == len(t) or t[i + 1] == " "):
            out.append(buf.strip())
            buf = ""
    if buf.strip():
        out.append(buf.strip())
    return out


def trim(t, limit=330, n=2):
    t = clean(t)
    t = re.sub(r"^[-*]\s+", "", t)
    ss = sentences(t)
    out, total = [], 0
    for s in ss[:n]:
        if out and total + len(s) > limit:
            break
        out.append(s)
        total += len(s)
    res = " ".join(out) if out else t[:limit]
    if res.count("(") != res.count(")"):
        res = t[:limit].rsplit(".", 1)[0] + "."
    return res


def sections(text):
    parts, cur, name = {}, [], None
    for line in text.split("\n"):
        m = re.match(r"^##\s+(?:\d+\.\s+)?(.+)$", line)
        if m:
            if name is not None:
                parts[name] = "\n".join(cur)
            name, cur = m.group(1).strip(), []
        elif name is not None:
            cur.append(line)
    if name is not None:
        parts[name] = "\n".join(cur)
    return parts


def first_block(sec):
    """First non-empty paragraph or bullet of a section."""
    for chunk in re.split(r"\n\s*\n", sec.strip()):
        c = clean(chunk.split("\n")[0] if chunk.lstrip().startswith("-") else chunk)
        if c and not c.startswith("#"):
            return c
    return ""


def find(parts, *keys):
    for k, v in parts.items():
        kl = k.lower()
        if any(key in kl for key in keys):
            return v
    return ""


def header(text, field):
    m = re.search(r"^%s:\s*(.+)$" % field, text, re.M)
    return m.group(1).strip() if m else ""


def level_of(s):
    digits = re.findall(r"[0-3]", s[:60])
    return max(int(d) for d in digits) if digits else 0


def book_of(s, default=1):
    m = re.search(r"Book\s+(\d+)", s)
    return int(m.group(1)) if m else default


def card(fn):
    text = open(os.path.join(CH, fn), encoding="utf-8").read()
    name = re.match(r"#\s+(.+)", text).group(1).strip()
    lvl = level_of(header(text, "Spoiler level"))
    vfrom, vthru = header(text, "Valid from"), header(text, "Valid through")
    start = book_of(vfrom)
    parts = sections(text)
    role = trim(first_block(find(parts, "summary")), 300, 2) or "Role not stated in the file."
    app = find(parts, "appearance")
    app = trim(first_block(app), 260, 1) if app.strip() else "Not described in the character file."
    voice = ""
    m = re.search(r"\*\*Voice \(condensed\)\*\*:\s*(.+)", text)
    if m:
        voice = trim(m.group(1), 260, 2)
    else:
        rp = find(parts, "roleplay")
        voice = trim(first_block(rp), 260, 2) if rp.strip() else "See the character file."
    sec = find(parts, "secret", "spoiler")
    secret = trim(first_block(sec), 260, 2) if sec.strip() else "Nothing recorded."
    link = "../../07_Characters/%s" % fn
    body = ["### %s" % name,
            "",
            "Valid from %s to %s. Spoiler level %d. Character file: [%s](%s)." % (
                vfrom or "unknown", vthru or "unknown", lvl, name, link),
            "",
            "- **Role**: %s" % role,
            "- **Appearance**: %s" % app,
            "- **Voice**: %s" % voice,
            "- **Secret or spoiler note**: %s" % secret,
            ""]
    return start, lvl, name, "\n".join(body)


def main():
    cards = {}
    for fn in sorted(os.listdir(CH)):
        if not fn.endswith(".md") or fn in SKIP:
            continue
        start, lvl, name, body = card(fn)
        cards.setdefault(start, []).append((name, lvl, body))
    os.makedirs(OUT, exist_ok=True)
    for lo, hi, slug, label in BANDS:
        items = []
        for b in range(lo, hi + 1):
            items += cards.get(b, [])
        items.sort(key=lambda x: x[0])
        top = max([l for _, l, _ in items] + [0])
        header_level = {1: 1, 2: 2, 3: 3}.get(hi // 3 if hi <= 9 else 3, 3)
        header_level = 1 if hi <= 3 else (2 if hi <= 9 else 3)
        lines = ["# NPC Cards: Characters First Appearing in %s" % label, "",
                 "Status: Draft (generated by src/tools/npc_cards.py from the character files; each field repeats the file's own cited text)",
                 "Spoiler level: %d" % header_level,
                 "Valid from: Book %d" % lo,
                 "Valid through: Book 13",
                 "Sources: character files in 07_Characters (see each card)",
                 "Related: ../NPC_Rosters_by_Era.md, ../Tone_and_Voice.md, ../Spoiler_Management.md, ../../07_Characters/00_Characters_Overview.md",
                 "", "## 1. How to use these cards", "",
                 "One card per character, in alphabetical order. Each gives the role, appearance, a voice cue and the character's secret or spoiler note, with citations copied from the character file. For the full picture open the linked file. A card whose spoiler level is higher than this file's is wrapped in a level tag.",
                 "", "## 2. Cards", ""]
        for name, lvl, body in items:
            if lvl > header_level:
                lines += ["<!-- level:%d -->" % lvl, body.rstrip(), "<!-- /level -->", ""]
            else:
                lines += [body.rstrip(), ""]
        path = os.path.join(OUT, "NPC_Cards_%s.md" % slug)
        open(path, "w", encoding="utf-8", newline="\n").write("\n".join(lines) + "\n")
        print("%s: %d cards" % (slug, len(items)))


if __name__ == "__main__":
    main()

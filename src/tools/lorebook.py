"""Derive roleplay lorebooks from the compendium (build plan item 5.4).

The lorebook is a derived product, never a source (00_Project_Structure.md, section 2). This script regenerates it from the
compendium documents, one JSON file per spoiler level, in the SillyTavern / Chub world-info layout of the earlier lorebook
(src/tools/archive/hwfwm_lorebook.json). A file for level N holds only what a reader cleared to level N may see:
documents whose header level is above N are left out, and tagged sections (<!-- level:M -->) above N are cut.

Each entry is one document: its Summary section, then bullets from its fact-like sections up to a size cap, with the
"(Book N, ChX LY)" citations removed to save tokens. Keys are the document title, the title without brackets and, for
characters, the first and last name. Entries are ordered by folder so that the world and magic rules come first.

Output: src/exports/lorebook/hwfwm_lorebook_level0.json ... level3.json
Usage: python3 src/tools/lorebook.py
"""
import json, os, re, sys, io
from spoiler_tags import baseline, parse

HERE = os.path.dirname(os.path.abspath(__file__))
BASE = os.path.abspath(os.path.join(HERE, "..", ".."))
OUT = os.path.join(BASE, "src", "exports", "lorebook")
FOLDERS = ["01_World_Primer.md", "02_Cosmology_and_Powers", "03_Magic_and_Adventuring", "04_Peoples_and_Cultures",
           "05_Organisations", "06_Places", "07_Characters", "08_History_and_Timeline", "09_Items_and_Artefacts"]
SKIP_NAME = re.compile(r"^(00_|Chapter_Digest|Book_\d\d_Timeline|Minor_Cast)")
FACT_SECTIONS = ("facts", "how it works", "powers", "personality", "background", "key events", "society", "history", "relationships")
CAP = 1500
HEADER_FIELD = re.compile(r"^(Status|Spoiler level|Valid from|Valid through|Sources|Related):")
# Terms that mark facts first learned at level 2 (Books 4-9) or level 3 (Books 10-13). A sentence holding one is left out of a
# lorebook below that level, because some summaries are written at a lower header level than their last sentences. Each
# dropped sentence is reported, so the document can be fixed or tagged.
LEVEL2 = ["astral king", "astral kingdom", "astral throne", "astral gate", "System Administrator", "Spirit Vault", "Global Defense",
          "Global Defence", "transformation zone", "Starlight", "Makassar", "One Day War"]
LEVEL3 = ["Zithis", "Unorthodoxy", "Cosmic Throne", "Sundered", "sundering", "soul forge", "Network founder", "Knowledge's plan",
          "Disguise", "New Water", "Boko is destroyed", "administrator of the System", "System withdrawal"]
DROPPED = []


def book_level(b):
    return 1 if b <= 3 else 2 if b <= 9 else 3


def keep_sentence(s, level, doc):
    """False when the sentence names a Book, or a term, that belongs to a level above `level`."""
    for m in re.finditer(r"Books? (\d+)", s):
        if book_level(int(m.group(1))) > max(level, 1):
            DROPPED.append((level, doc, s[:90]))
            return False
    terms = (LEVEL2 + LEVEL3) if level <= 1 else LEVEL3 if level == 2 else []
    for w in terms:
        if w.lower() in s.lower():
            DROPPED.append((level, doc, s[:90]))
            return False
    return True


def filter_text(t, level, doc):
    parts = re.split(r"(?<=[.!?])\s+(?=[A-Z\"])", t)
    return " ".join(p for p in parts if keep_sentence(p, level, doc))
STOP = {"the", "of", "and", "from", "with", "house", "church", "guild", "lord", "lady", "king", "queen"}


def strip_cites(t):
    """remove parentheticals that hold a citation, innermost first, and tidy the spacing."""
    for _ in range(4):
        t = re.sub(r"\s*\([^()]*(?:Book \d+, Ch\d+|Book \d+|notes|wiki|per [A-Z][A-Za-z_]+\.md|\.md)[^()]*\)", "", t)
    t = re.sub(r"`([^`]*)`", r"\1", t)
    t = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", t)
    t = re.sub(r"\*\*|\*", "", t)
    t = re.sub(r"\s+([,.;:])", r"\1", t)
    return re.sub(r"[ \t]+", " ", t).strip()


def visible(text, level):
    """lines of a document with tagged sections above `level` removed, tag comments dropped."""
    lines = text.split("\n")
    tags, _ = parse(text)
    hidden = set()
    for s, e, lv in tags:
        try:
            high = int(lv) > level
        except ValueError:
            high = False
        if high:
            hidden.update(range(s, e + 1))
    out = []
    for i, l in enumerate(lines, 1):
        if i in hidden or re.match(r"^<!--\s*/?level", l):
            continue
        out.append(l)
    return out


def sections(lines):
    cur, out = "", {}
    for l in lines:
        m = re.match(r"^##+\s+(?:[0-9A-Za-z]+\.\s+)?(.+)$", l)
        if m:
            cur = m.group(1).strip().lower()
            out.setdefault(cur, [])
            continue
        out.setdefault(cur, []).append(l)
    return out


def build_content(lines, level, doc):
    secs = sections(lines)
    summ = ""
    for k, v in secs.items():
        if k.startswith("summary"):
            summ = " ".join(x.strip() for x in v if x.strip())
            break
    if not summ:
        first = next((k for k, v in secs.items() if k != "" and any(x.strip() for x in v)), None)
        body = [x for x in (secs.get("", []) + (secs[first] if first else [])) if x.strip() and not HEADER_FIELD.match(x) and not x.startswith("#")]
        summ = " ".join(x.strip() for x in body[:6] if not x.startswith(("-", "|")))
    text = filter_text(strip_cites(summ), level, doc)
    bullets = []
    for k, v in secs.items():
        if any(f in k for f in FACT_SECTIONS):
            for x in v:
                x = x.strip()
                if x.startswith("- "):
                    b = filter_text(strip_cites(x[2:]), level, doc)
                    if len(b) > 25:
                        bullets.append(b)
    for b in bullets:
        if len(text) + len(b) + 3 > CAP:
            break
        text += " " + b if text.endswith(".") else "; " + b
    if len(text) > CAP:
        cut = text[:CAP]
        text = cut[:cut.rfind(". ") + 1] if ". " in cut else cut
    return text.strip()


def keys_for(path, title):
    ks = [title]
    plain = re.sub(r"\s*\(.*?\)", "", title).strip()
    if plain != title:
        ks.append(plain)
    if path.startswith("07_Characters") and "/" in path:
        parts = [p for p in re.split(r"[\s-]+", plain) if len(p) >= 4 and p.lower() not in STOP]
        if len(parts) >= 2:
            ks += [parts[0], parts[-1]]
    seen, out = set(), []
    for k in ks:
        if k.lower() not in seen:
            seen.add(k.lower())
            out.append(k)
    return out


def docs():
    for f in FOLDERS:
        p = os.path.join(BASE, f)
        if os.path.isfile(p):
            yield f
            continue
        for root, _, files in os.walk(p):
            for fn in sorted(files):
                if fn.endswith(".md") and not SKIP_NAME.match(fn):
                    yield os.path.relpath(os.path.join(root, fn), BASE).replace("\\", "/")


def entry(uid, keys, comment, content, order):
    return {"uid": uid, "key": keys, "keysecondary": [], "comment": comment, "content": content, "constant": False,
            "selective": False, "selectiveLogic": 0, "order": order, "position": 1, "disable": False, "addMemo": True,
            "excludeRecursion": True, "probability": 100, "displayIndex": uid, "useProbability": True,
            "secondary_keys": [], "keys": keys, "id": uid, "priority": order, "insertion_order": order, "enabled": True,
            "name": comment, "extensions": {"depth": 4, "weight": order, "addMemo": True, "probability": 100, "displayIndex": uid,
                                            "selectiveLogic": 0, "useProbability": True, "characterFilter": None,
                                            "excludeRecursion": True},
            "case_sensitive": False, "depth": 4, "characterFilter": None}


def main():
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
    os.makedirs(OUT, exist_ok=True)
    texts = {}
    for rel in docs():
        t = open(os.path.join(BASE, rel), encoding="utf-8").read()
        texts[rel] = (t, baseline(t))
    for level in range(4):
        entries, uid = {}, 0
        for rel, (t, base) in texts.items():
            if base is None or base > level:
                continue
            lines = visible(t, level)
            title = lines[0].lstrip("# ").strip() if lines and lines[0].startswith("#") else os.path.basename(rel)[:-3]
            content = build_content(lines, level, rel)
            if len(content) < 60:
                continue
            uid += 1
            order = 10 + 5 * FOLDERS.index(rel.split("/")[0]) if rel.split("/")[0] in FOLDERS else 10
            entries[str(uid)] = entry(uid, keys_for(rel, title), title, content, order)
        book = {"name": "He Who Fights With Monsters | Compendium Lorebook (spoiler level %d)" % level,
                "description": "Derived from the HWFWM compendium (not a source). Spoiler level %d: %s. Book text takes precedence over the fan wiki; this file is regenerated by src/tools/lorebook.py." % (
                    level, ["public setting only", "Books 1-3", "Books 1-9", "Books 1-13"][level]),
                "is_creation": False, "scan_depth": 3, "token_budget": 4096, "recursive_scanning": False,
                "extensions": {}, "entries": entries}
        path = os.path.join(OUT, "hwfwm_lorebook_level%d.json" % level)
        with open(path, "w", encoding="utf-8", newline="\n") as f:
            json.dump(book, f, ensure_ascii=False, indent=1)
        print("level %d: %d entries, %d KB, %d sentences held back" % (level, len(entries), os.path.getsize(path) // 1024, len([d for d in DROPPED if d[0] == level])))


if __name__ == "__main__":
    main()
    with open(os.path.join(OUT, "held_back.txt"), "w", encoding="utf-8", newline="\n") as f:
        f.write("Sentences left out of a lorebook because they name a later book or term (level, document, start of sentence).\n")
        for lv, doc, s in sorted(set(DROPPED)):
            f.write("%d\t%s\t%s\n" % (lv, doc, s))

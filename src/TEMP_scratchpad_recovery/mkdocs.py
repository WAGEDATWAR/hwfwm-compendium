import json, collections, re
base = r"C:\Users\Gabriel\Documents\World Stuff\HWFWM Compendium"
rows = [r for r in json.load(open("register_rows.json")) if not r["claim"].lstrip().startswith("|")]
idx = json.load(open("chapter_index.json"))

def conf(r):
    if r["method"] == "quote":
        return "exact"
    if r["method"] == "range":
        return "unlocated"
    if r["ch"] is None:
        return "unlocated"
    return "probable" if r["score"] >= 0.7 else "candidate"

def ref(r):
    if r["conf"] == "notes-confirmed":
        return "notes " + r["note"].split(";")[0][:22]
    if r["ch"] is None:
        return "B%s (no chapter)" % r["book"]
    return "B%s Ch%d L%d-%d" % (int(r["book"]), r["ch"], r["lo"], r["hi"]) if r["lo"] != r["hi"] else "B%s Ch%d L%d" % (int(r["book"]), r["ch"], r["lo"])

import os
dec = {}
for ln in open("decisions.tsv", encoding="utf-8"):
    p = ln.rstrip(chr(10)).split(chr(9))
    if len(p) >= 6:
        if p[0] in dec and p[5] == "unlocated":
            continue
        dec[p[0]] = p
titles = {(int(n), c[0]): c[1] for n, l in idx.items() for c in l}
for i, r in enumerate(rows, 1):
    r["id"] = "R%04d" % i
    r["conf"] = conf(r)
    r["note"] = ""
    if r["id"] in dec:
        d = dec[r["id"]]
        if d[5] == "notes":
            r["ch"] = None; r["conf"] = "notes-confirmed"; r["note"] = d[6] if len(d) > 6 else ""
            r["title"] = "(confirmed in chapter notes or wiki, book lines not found)"
            continue
        if d[5] == "n/a":
            r["drop"] = True
            continue
        if d[5] == "unlocated":
            r["ch"] = None; r["conf"] = "unlocated"; r["note"] = d[6] if len(d) > 6 else "Read; not found in the chapter files."
            r["title"] = "(not found after reading)"
            continue
        r["book"] = d[1]; r["ch"] = int(d[2]); r["lo"] = int(d[3]); r["hi"] = int(d[4])
        r["conf"] = d[5]; r["note"] = d[6] if len(d) > 6 else ""
        r["title"] = titles.get((int(d[1]), int(d[2])), r["title"])

# ---- Source_Text/README.md
out = ["# Source Text: chapter files", "",
 "The book text split into one file per chapter, grouped by book. Files are plain text. Line 1 of each file is a header (`BOOK n | Chapter c | Title`); the story text starts on line 3, and each line is one paragraph. Reference format: `B7 Ch31 L12-15` means Book 7, chapter 31, lines 12 to 15 of that chapter file (line numbers as `grep -n` prints them).", "",
 "Notes:",
 "- Book 13 chapters keep the serial numbers used in the source (950 to 1024); Books 1-12 use the numbering in each book's contents list.",
 "- Book 5 chapter 4 (\"Breakneck Pace\") has no heading in the source text; its text sits at the end of `Ch_003_A_Modern_Myth.txt` (the file header says so).",
 "- Some books (for example 7 and 9) contain damaged punctuation (`\ufffd` for curly quotes); text is reproduced as found.",
 "- Searching tips: `grep -rn \"phrase\" Book_07/` for a whole book; `grep -n \"phrase\" Book_07/Ch_031*` for one chapter.",
 "- These files are the top tier of the source hierarchy (Book Files > Chapter Summaries > Wiki). Do not edit them.", "",
 "## Chapter index", ""]
for n in range(1, 14):
    lst = idx[str(n)]
    out.append("### Book %d (%d chapter files)" % (n, len(lst)))
    out.append("")
    out.append("Folder: `Book_%02d/`" % n)
    out.append("")
    out.append("| Ch | Title | File | Lines |")
    out.append("|---|---|---|---|")
    for (num, title, fn, nl, merged) in lst:
        t = title + (" (also contains ch%s)" % ",".join(map(str, merged)) if merged else "")
        out.append("| %d | %s | %s | %d |" % (num, t, fn, nl))
    out.append("")
open(base + r"\src\Source_Text\README.md", "w", encoding="utf-8").write("\n".join(out))

# ---- Source_Register.md
_rt = set(json.load(open("retagged_ids.json")))
for r in rows:
    if r["id"] in _rt and not r["tag"].lower().startswith("notes"):
        r["tag"] = "notes, " + r["tag"]
        r["tier"] = "notes"
rows = [r for r in rows if not r.get("drop")]
_nr = json.load(open("new_rows.json")) if os.path.exists("new_rows.json") else []
_n0 = 640
for _i, _r in enumerate(_nr):
    _r["id"] = "R%04d" % (_n0 + _i)
    rows.append(_r)
by = collections.OrderedDict()
for r in rows:
    by.setdefault(r["doc"], []).append(r)
c = collections.Counter(r["conf"] for r in rows)
reg = ["# Source Register", "",
 "Status: Draft (generated from every tier-tagged claim in the compendium; locations are automatic and graded)",
 "Spoiler level: 3 (references reveal where events occur)",
 "Valid from: Book 1", "Valid through: Book 13",
 "Sources: `Source_Text/` (book chapter files)",
 "Related: Source_Map.md, ../Source_Text/README.md", "",
 "Every claim in the compendium that carries a \"(Book N)\", \"(notes, Book N)\" or \"(wiki)\" tag with a book number is listed here with the book chapter and lines where the supporting text should be. Reference format `B7 Ch31 L12-15` (see `Source_Text/README.md`).", "",
 "**Confidence of the location**",
 "- **exact**: a quoted phrase in the claim was found verbatim at that line (%d entries)." % c["exact"],
 "- **probable**: the rare terms of the claim cluster in those lines (%d entries). Read the lines to confirm before relying on it." % c["probable"],
 "- **candidate**: best partial match only (%d entries). Treat as a starting point for narrowing." % c["candidate"],
 "- **verified**: read at the cited lines and confirmed (%d entries); **partial**: the lines support part of the claim, the note says which (%d); **mismatch**: the claim's citation disagrees with the text (%d)." % (c["verified"], c["partial"], c["mismatch"]),
 "- **notes-confirmed**: the claim is confirmed in the chapter notes or the wiki (named in the note) but the book lines were not found; the document tags it \"notes\" or \"wiki\" (%d entries)." % c["notes-confirmed"],
 "- **unlocated**: tag spans several books or no match (%d entries)." % c["unlocated"], "",
 "Tier: **book** = tag cites the book text; **notes** = the claim was taken from the chapter summaries (check the book text when narrowing); **wiki** = wiki only. State-change flag **S** marks claims about something being gained, lost, born, killed, changed or joined, for the per-book change log in Source_Map.md.", "",
 "When a location is narrowed or confirmed by reading the chapter, change its confidence to **verified**, correct the reference, and add the date and a note.", ""]
for doc, lst in by.items():
    reg.append("## %s" % doc)
    reg.append("")
    reg.append("| ID | Claim | Tag | Reference | Chapter title | Conf. | S | Note |")
    reg.append("|---|---|---|---|---|---|---|---|")
    for r in lst:
        cl = r["claim"].replace("|", "/")
        reg.append("| %s | %s | %s | %s | %s | %s | %s | %s |" % (r["id"], cl, r["tag"].replace("|", "/"), ref(r), r["title"].replace("|", "/"), r["conf"], "S" if r["state"] else "", r["note"].replace("|", "/")))
    reg.append("")
open(base + r"\Appendices\Source_Register.md", "w", encoding="utf-8").write("\n".join(reg))
json.dump(rows, open("register_final.json", "w"))
print(c, len(by))

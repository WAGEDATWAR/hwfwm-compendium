import json,collections,re
base=r"C:\Users\Gabriel\Documents\World Stuff\HWFWM Compendium"
rows=json.load(open("register_final.json"))
def ref(r):
    if r["ch"] is None: return "B%s"%r["book"]
    return "B%s Ch%d L%d-%d"%(int(r["book"]),r["ch"],r["lo"],r["hi"])
m=["# Source Map","",
"Status: Draft (framework and first harvest; all existing tier tags are registered, none yet re-read chapter by chapter)",
"Spoiler level: 3","Valid from: Book 1","Valid through: Book 13",
"Sources: `Source_Text/` chapter files; `Source_Register.md`",
"Related: Source_Register.md, ../Source_Text/README.md, ../08_History_and_Timeline/Master_Timeline.md, ../00_Project_Structure.md","",
"## 1. Purpose","",
"The Source Map ties compendium claims to book, chapter and lines so that facts can be traced, narrowed and re-checked, and so that changes over the series (a death, a gain, a loss, a change of allegiance) are recorded with the book where they happen. It is the working backbone for the Master Timeline and the character files.","",
"## 2. How the pieces fit","",
"- `Source_Text/Book_NN/Ch_NNN_Title.txt`: the book text, one file per chapter (index in `Source_Text/README.md`).",
"- `Appendices/Source_Register.md`: one row per tagged claim in the compendium (ID `R0001`...), with its location, location confidence and a state-change flag.",
"- This file: the rules, the log of narrowed results (section 4), the per-book change log harvested from the register (section 5), and the timeline thread (section 6).","",
"## 3. Rules","",
"1. Reference format: `B7 Ch31 L12-15` (book, chapter, lines of the chapter file).",
"2. Hierarchy stays Book Files > Chapter Summaries > Wiki. A register row whose tag is **notes** or **wiki** should be narrowed to a book location when possible; once it is, retag the claim in its document to \"Book N\".",
"3. Location grades: exact, probable, candidate, unlocated, **verified** (read at the lines and confirmed). Only verified rows count as settled references.",
"4. When a claim is narrowed, update its row in the register and add a line to section 4 below. When a document claim is added or changed, add or update its row the same session (section 10 of the structure document).",
"5. If the lines do not support the claim, mark the row **contradicted**, correct the document and log the correction in `Change_Log.md`.","",
"## 4. Narrowing log","",
"| Date | Register ID | Result | Note |","|---|---|---|---|",
"| 2026-10-20 | (all) | Register created | 656 rows harvested automatically from existing tags; none yet marked verified. |","",
"## 5. Change log by book (state changes harvested from the register)","",
"Candidate entries only: each is a claim flagged as a gain, loss, death, birth, move or change. Confirm the chapter before treating the order as settled.",""]
ch=[r for r in rows if r["state"] and r["ch"] is not None and r["book"].isdigit() and (r["doc"].startswith("07_")or r["doc"].startswith("08_") or r["doc"].startswith("05_") or r["doc"].startswith("06_") or r["doc"].startswith("02_"))]
byb=collections.defaultdict(list)
for r in ch: byb[int(r["book"])].append(r)
for n in sorted(byb):
    m.append("### Book %d"%n);m.append("")
    m.append("| Order | Subject (document) | Change | Reference | ID | Conf. |");m.append("|---|---|---|---|---|---|")
    for r in sorted(byb[n],key=lambda r:(r["ch"],r["lo"])):
        subj=r["doc"].split("/")[-1][:-3].replace("_"," ")
        m.append("| Ch%d | %s | %s | %s | %s | %s |"%(r["ch"],subj,r["claim"][:160].replace("|","/"),ref(r),r["id"],r["conf"]))
    m.append("")
m+=["## 6. Timeline thread","",
"The Master Timeline (`08_History_and_Timeline/Master_Timeline.md`) should be rebuilt as an ordered thread of register IDs: every dated or ordered event gets a row here with book, chapter and lines, so the order within a book follows chapter order and cross-book intervals can be checked against the cited lines. Anchors already established in the Master Timeline are to be located first (this has not yet been done):","",
"- Jason's birthday (1 April 1994) and the arrival in late November 2017.",
"- Return to Earth in early June 2019; the April 2020 birthday; departure from Earth in autumn 2021; Book 13 in 2038.",
"- The Book 7 statement that the surge was \"some five years overdue\" (Book 7; register entry in `01_World_Primer.md`).","",
"| Event | Date or interval | Reference | Status |","|---|---|---|---|","| (to be filled as anchors are located) | | | |",""]
open(base+r"\Appendices\Source_Map.md","w",encoding="utf-8").write("\n".join(m))
print(len(ch),{n:len(v) for n,v in byb.items()})

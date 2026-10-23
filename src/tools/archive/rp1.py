exec(open("rp_base.py", encoding="utf-8").read())

write("00_Roleplay_Overview", "Roleplay Support: Overview", "0", "1", "13",
 "Books 1-13 (chapter files); this folder uses the compendium's own documents for detail",
 "Era_Selection.md, Spoiler_Management.md, ../01_World_Primer.md, ../08_History_and_Timeline/Master_Timeline.md, ../00_Project_Structure.md",
 "How to pick a period to play in and how to keep later-book knowledge out of earlier scenes.",
 "- **Pick the era first** (`Era_Selection.md`): it fixes the calendar, the rank scale, who is present and what dangers are live. The calendar anchors are in `../08_History_and_Timeline/Master_Timeline.md`.\n- **Then pick the spoiler level** (`Spoiler_Management.md`): level 0 for public setting, 1 for Books 1-3, 2 for Books 4-9, 3 for Books 10-13 and the ending (`../00_Project_Structure.md`, section 6).\n- **Use the character and place files**, each of which states when a fact starts being true and cites chapter lines; do not give a character knowledge from a later level.\n- **Treat the books as the authority**: where a document says \"notes\" or \"wiki\", that fact is not yet confirmed in the book text.\n- **Planned in this folder**: plot hooks, NPC rosters by era, and tone and voice notes.",
 "Start from the era table, then check each character's \"valid from\" book before you let them appear.")
print("ok")

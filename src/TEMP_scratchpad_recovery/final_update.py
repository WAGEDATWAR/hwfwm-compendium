import re
root = r"C:\Users\Gabriel\Documents\World Stuff\HWFWM Compendium"

# --- Name Index additions (reuse the sorted insert from index_update) ---
exec(open(r"C:\Users\Gabriel\AppData\Local\Temp\claude\C--Users-Gabriel-Documents-Gmod-Projects-Gmod-Decompilation\08b70dbf-6f0b-4b6b-a18f-242cc3f1fe96\scratchpad\index_update.py", encoding="utf-8").read().split("glossary = [")[0])
names = [
    ("E", "- **Erigo Fin Desca** (B10): messenger remade as the Builder's new prime vessel after Shako was taken by the Sundered Throne."),
    ("H", "- **Hess Jor Nasala** (B9): silver messenger subordinate to Jes Fin Kaal."),
    ("U-Z", "- **Vesta Carmis Zell** (B9): messenger who speaks for the astral king behind the natural array's plot."),
    ("U-Z", "- **Zithis Carrow Vayel** (B8): the messenger raised at sixteen to replace the original Builder."),
]
# the Name Index uses 'U-Z' for the last section; insert and keep rough alphabetical order
insert_sorted(root + r"\Appendices\Name_Index.md", names, None)
print("names added")

# --- Change Log ---
p = root + r"\Appendices\Change_Log.md"
s = open(p, encoding="utf-8").read()
a = "**Appendices and housekeeping**"
assert a in s
add = """**Cosmology and Powers (`02_Cosmology_and_Powers/`)**
- Added `00_Cosmology_Overview.md`, `Great_Astral_Beings.md`, `Gods_and_Churches.md` and `Astral_Kings_and_Messengers.md`. Items marked "confirmed" in the documents were checked against the book text while writing (dumpling soup, the sundering's factions, Rules of Intrusion, Zithis Carrow Vayel, Erigo Fin Desca, the gestalt nature of messengers, Dominion on kneeling, Hana Shavar's role). Everything else comes from the lorebook and wiki and is flagged.
- Status: **Draft (partly checked)**; the unchecked items are in `TODO_Verification.md`, section D.

"""
s = s.replace(a, add + a)
s = s.replace("- Revised `Appendices/Name_Index.md`: added Gordon Truffett, Holly Macrossan, Neiman Bassingthwaite, Todd Halverson.",
              "- Revised `Appendices/Name_Index.md`: added Gordon Truffett, Holly Macrossan, Neiman Bassingthwaite, Todd Halverson, Erigo Fin Desca, Hess Jor Nasala, Vesta Carmis Zell, Zithis Carrow Vayel.")
s = s.replace("- Revised `00_Project_Structure.md`: section 3 (layout marked with what exists), section 9 (new notes), section 11 (next documents).",
              "- Revised `00_Project_Structure.md`: section 3 (layout marked with what exists), section 9 (new notes), section 10 (change-log practice), section 11 (next documents; Cosmology is now started).")
open(p, "w", encoding="utf-8").write(s)
print("change log updated")

# --- TODO: add section D ---
p = root + r"\TODO_Verification.md"
s = open(p, encoding="utf-8").read()
s += """
## D. Cosmology and Powers (02_Cosmology_and_Powers), first draft

Checked against the book text while writing: dumpling soup; which great astral beings stood apart from or opposed the Sundering; the Rules of Intrusion; Zithis Carrow Vayel and Erigo Fin Desca; messengers' gestalt nature; Hana Shavar's role; Dominion on kneeling; Voices of the Will and Colin's awakening.

Still unchecked (lorebook or wiki claims):
- Cosmology: the "universes as seeds" model; the fundamental realm and reality cores as batteries; Interstice's gold-rank entry terms; the Keeper's inability to affect the past (Shade).
- Great astral beings: the full list and domains (Legion as life, Whisper in Corners, Word in the Silence, Seeker of Songs); the nameless functionary GABs; hierophants as former vessels; the Reaper's stance on the Sundering (conflicting hints); the World-Phoenix as the former Boundary; Helsveth as prime vessel; the pacts between the Builder, Reaper and World-Phoenix.
- Gods: the full list of gods; what gods cannot do; the Church of Death's tally; Death's pact details; the Hero essence replacing the confluence (wiki); Hero sanctioning himself; Undeath's high priest and avatar; Knowledge's Book 13 plan (the briefing at Asano Academy).
- Astral kings and messengers: the wiki's prerequisites; the silver cap and seal; "Kneel" as the message; messengers' physical description; resurrection failing on messengers; "budding"; Jamis Fran Muskar as a Council of Kings avatar and what the debt is; Marek's leadership of the Unorthodoxy.
"""
open(p, "w", encoding="utf-8").write(s)
print("todo updated")

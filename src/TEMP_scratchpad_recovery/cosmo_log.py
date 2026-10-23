root = r"C:\Users\Gabriel\Documents\World Stuff\HWFWM Compendium"

# TODO: replace section D
p = root + r"\TODO_Verification.md"
s = open(p, encoding="utf-8").read()
i = s.index("## D. Cosmology and Powers")
s = s[:i] + """## D. Cosmology and Powers (02_Cosmology_and_Powers)

Remaining unconfirmed (lorebook or wiki claims kept hedged in the files):
- Cosmology: whether universes are "seeds" and reality cores are "batteries"; that not even the Keeper can affect the past (Shade).
- Great astral beings: the domains of Legion (life), the Whisper in Corners, the Word in the Silence and the Seeker of Songs; the lorebook's description of "the nameless" as functionaries of life, death, time and matter; that their true state is mindless and alien; the pacts between the Builder, Reaper and World-Phoenix; Gordon being created by the All-Devouring Eye.
- Gods: the full list of gods; that gods cannot enter Jason's realm or affect his mind in his domains, and cannot reveal other gods' deceptions; the Hero essence replacing the confluence; Gary's death about a year after the Cup; Death returning the resurrection power in Book 12; the Church of Undeath's high priest Garth Larosse and the sanctioning of its avatar; Disguise recruiting the Network's founder; Knowledge becoming "just God" of Earth.
- Astral kings and messengers: the wiki's list of astral-king prerequisites; the silver cap and the seal that siphons potential; "Kneel" as the message; messengers being "budded"; Jamis Fran Muskar as a Council of Kings avatar and the nature of Zithis's debt; whether Marek leads the Unorthodoxy; Voices of the Will reaching gold as a rule.
""" + "\n"
open(p, "w", encoding="utf-8").write(s)

# Change Log
p = root + r"\Appendices\Change_Log.md"
s = open(p, encoding="utf-8").read()
a = "- Status: **Draft (partly checked)**; the unchecked items are in `TODO_Verification.md`, section D.\n"
assert a in s
s = s.replace(a, a + """- Verification pass on all four Cosmology files against the book text. Corrected: the dumpling-soup chapter is Book 1 chapter 69, not Book 3 (also fixed in `06_Places/Astral_Spaces/00_Astral_Overview.md`); Interstice admits gold-rankers only as menial workers; the fundamental realm is what the books call node space. Confirmed and added: the World-Phoenix's own account of sanctioning itself from the Boundary, the Reaper's vessel Velius, Helsveth as the World-Phoenix's vessel, hierophants (Books 3, 7), Disguise creating the Order of Redeeming Light (Book 10), Death's appearance and the pact's terms, Hero sanctioning himself, Knowledge's description and invasion plan, the third of her priests who are spies, the cube leaving Gabrielle Pellin's chest, the brand and the rise of astral kings who were messengers, the Council of Kings, Vesta Carmis Zell as Tera's astral king master, and the alabaster, gold-eyed, winged appearance of messengers. Removed or hedged: Marek as Unorthodoxy leader, the silver cap and seal, "budded", the Hero confluence claim.
- Status after the pass: **Draft (verified in part)**; remaining items are in `TODO_Verification.md`, section D.
""")
open(p, "w", encoding="utf-8").write(s)
print("log updated")

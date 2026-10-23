p = r"C:\Users\Gabriel\Documents\World Stuff\HWFWM Compendium\00_Project_Structure.md"
s = open(p, encoding="utf-8").read()

# Section 3: record what exists
a = "Folders are created only when their first document is written."
assert a in s
s = s.replace(a, a + """

**What exists now** (see `Appendices/Change_Log.md` for the history):

- Done as drafts: `01_World_Primer.md`; `Appendices/Glossary.md`, `Name_Index.md`, `Change_Log.md`; `08_History_and_Timeline/Master_Timeline.md`; `03_Magic_and_Adventuring/Magic_and_Adventuring.md` (one combined document in place of the two planned files); `06_Places/` (overview, Greenstone, Vitesse, Rimaros, Yaresh, Cyrion, `Earth/`, `Astral_Spaces/`).
- Working files at the root: `TODO_Verification.md` (claims not yet confirmed against the book text).
- Not started: `02_Cosmology_and_Powers/`, `04_Peoples_and_Cultures/`, `05_Organisations/`, `07_Characters/`, `09_Items_and_Artefacts/`, `10_Roleplay_Support/`, and the Open Questions and Source Map appendices.""")

# Section 9: additions
a = "- **Wiki timeline errors**: Asano Village timing, some month counts."
assert a in s
s = s.replace(a, a + """
- **Butterflies of Makassar** *(resolved)*: the name news broadcasts give to the public spectacle of Gordon's Harbinger of Doom swarm over the Makassar undead (Book 5).
- **Greenstone's status** *(resolved)*: a colony settled from Estercost, not part of Estercost proper (Books 11-12).
- **Open claims**: the remaining unconfirmed details for the Places and Magic documents are listed in `TODO_Verification.md`.""")

# Section 10: strengthen the chain
a = "- Keep a **Change Log** in `Appendices/` listing each document added or revised, with the date."
assert a in s
s = s.replace(a, "- Keep a **Change Log** in `Appendices/Change_Log.md` listing each document added or revised, with the date. Update it at the end of every writing or verification session, not afterwards.")

# Section 11: replace
i = s.index("## 11. Immediate next documents")
s = s[:i] + """## 11. Immediate next documents

1. **02_Cosmology_and_Powers/**: the astral realm, great astral beings, the Builder and the Cosmic Throne, gods, messengers, astral kings and authority. The hardest subject to write accurately; check each claim against the book text as it is written.
2. **05_Organisations/**: Adventure Society, Magic Society, Alchemy and Artifice Associations, Burning Violet, Sapphire Crown, the churches, Network, Cabal, EOA, the Order of the Reaper.
3. **07_Characters/**: core cast first.
4. Third verification pass for `06_Places/` and the remaining checks for `03_Magic_and_Adventuring/` (see `TODO_Verification.md`).
5. **04_Peoples_and_Cultures/**, **09_Items_and_Artefacts/**, **10_Roleplay_Support/**.
6. Open Questions and Source Map appendices.
"""
open(p, "w", encoding="utf-8").write(s)
print("structure updated")

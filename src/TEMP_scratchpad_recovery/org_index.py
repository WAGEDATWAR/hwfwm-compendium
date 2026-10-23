exec(open(r"C:\Users\Gabriel\AppData\Local\Temp\claude\C--Users-Gabriel-Documents-Gmod-Projects-Gmod-Decompilation\08b70dbf-6f0b-4b6b-a18f-242cc3f1fe96\scratchpad\index_update.py", encoding="utf-8").read().split("glossary = [")[0])
root = r"C:\Users\Gabriel\Documents\World Stuff\HWFWM Compendium"

glossary = [
    ("A", "**Action quota**: the minimum work every adventurer must complete during a monster surge, assigned at the jobs hall; guilds receive about sixty percent of the quotas. See *contribution board*. **[2]**"),
    ("A", "**Aristocratic Faction**: Yaresh's bloc of wealthy aristocrats and merchant barons who own most of the land and deliberately build power on money and influence rather than personal power. **[2]**"),
    ("C", "**Contribution board**: the Adventure Society's incentive ladder during a surge; work beyond the quota earns points on weekly and overall leaderboards with rewards at the end of each week and of the surge. **[2]**"),
    ("F", "**Flames of Redemption**: the Order of Redeeming Light's rite; an extreme modification of lesser vampirism that leaves members with a lack of imagination. **[2]**"),
    ("G", "**Global Defense Network (GDN)**: the public name of the Network after the monster waves began on Earth; later one of its fragments. **[2]**"),
    ("L", "**Living document**: the Magic Society's marble-and-gold tablet, connected to a central record, listing every known essence and combination. **[0]**"),
    ("M", "**Magical Research Association (MRA)**: the open-access research body Clive founds as a rival to the Magic Society. **[2/3]**"),
    ("P", "**Pure servitor**: an essence user implanted with a purified clockwork core by the Order of Redeeming Light; magically controlled and unable to use essence abilities. **[2]**"),
    ("R", "**Restricted list**: the Adventure Society's list of essences and combinations judged dangerous to the public (Death, Corrupt, Sacrifice, Undeath, Succubus and others); holders cannot join the Society. **[0]**"),
    ("S", "**Sapphire Crown**: the Storm Kingdom's royal guild, whose non-royal members serve periodically in the royal guard and are examined quarterly. **[2]**"),
]
names = [
    ("C", "- **Calcifer Bynes** (B10): Aristocratic Faction political figure in Yaresh; son of Gormanston."),
    ("G", "- **Genevieve Picot** (B1): deputy director of the Greenstone Adventure Society."),
    ("G", "- **Gormanston Bynes** (B10): prominent member of Yaresh's Aristocratic Faction."),
    ("M", "- **Marcus Hargrave Xenoria** (B10): Continental Council envoy and adventurer sent to Yaresh."),
    ("P", "- **Pochard Finn** (B1): Magic Society deputy, Clive's boss in Greenstone."),
    ("T", "- **Tabitha Gert** (B2): strict Adventure Society official who leads the Continental Council inquiry into Greenstone."),
]
insert_sorted(root + r"\Appendices\Glossary.md", glossary, None)
insert_sorted(root + r"\Appendices\Name_Index.md", names, None)

# Change log
p = root + r"\Appendices\Change_Log.md"
s = open(p, encoding="utf-8").read()
a = "**Appendices and housekeeping**"
add = """**Organisations (`05_Organisations/`)**
- Added `00_Organisations_Overview.md`, `Adventure_Society.md`, `Magic_Society_and_Associations.md`, `Guilds_and_Houses.md`, `Earth_Powers.md`, `Cults_and_Orders.md`. Items marked "confirmed" were checked against the book text while writing.
- Findings that corrected earlier documents: the Adventure Society badge is an iron medallion with the sword-and-rod-over-a-shield emblem (restored in Magic and Adventuring); about three in ten adventurers are in a guild, one in ten in a high-end guild, and guilds receive sixty percent of surge quotas (Book 7; restored in Magic and Adventuring); the Aristocratic Faction exists under that name (Book 10; added to `06_Places/Yaresh.md`); Nitra's steam engines run on fire and water quintessence (Book 11; `06_Places/Earth/Nitra.md`); each continent appears to have its own continental council (Rakesh and Cyrion; `06_Places/00_Places_Overview.md`).
- Status: **Draft (partly checked)**; unchecked items are in `TODO_Verification.md`, section E.

"""
assert a in s
s = s.replace(a, add + a, 1)
s = s.replace("Pending index updates", "Pending index updates", 1)
open(p, "w", encoding="utf-8").write(s)

# Structure doc: section 3 'exists' and section 11
p = root + r"\00_Project_Structure.md"
s = open(p, encoding="utf-8").read()
a = "- Not started: `02_Cosmology_and_Powers/`, `04_Peoples_and_Cultures/`, `05_Organisations/`, `07_Characters/`, `09_Items_and_Artefacts/`, `10_Roleplay_Support/`, and the Open Questions and Source Map appendices."
assert a in s
s = s.replace(a, "- Started: `02_Cosmology_and_Powers/` (overview, great astral beings, gods and churches, astral kings and messengers) and `05_Organisations/` (overview, Adventure Society, Magic Society and associations, guilds and houses, Earth's powers, cults and orders).\n- Not started: `04_Peoples_and_Cultures/`, `07_Characters/`, `09_Items_and_Artefacts/`, `10_Roleplay_Support/`, and the Open Questions and Source Map appendices.")
i = s.index("## 11. Immediate next documents")
s = s[:i] + """## 11. Immediate next documents

1. **07_Characters/**: core cast first (Jason, Rufus, Gary, Farrah, Humphrey, Sophie, Belinda, Clive, Neil, Danielle, Zara, Dawn, Shade, Colin, Gordon, Stash, Nik, Emi, Anna, Boris, Knowledge), then supporting cast.
2. **04_Peoples_and_Cultures/**: races and natures, societies, daily life, food, law.
3. Verification passes still owed: the third Places pass, the remaining Magic and Adventuring checks, the remaining Cosmology and Organisations checks (see `TODO_Verification.md`).
4. **09_Items_and_Artefacts/** and **10_Roleplay_Support/**.
5. Open Questions and Source Map appendices.
"""
open(p, "w", encoding="utf-8").write(s)
print("all updated")

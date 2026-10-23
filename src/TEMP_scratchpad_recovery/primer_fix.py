p = r"C:\Users\Gabriel\Documents\World Stuff\HWFWM Compendium\01_World_Primer.md"
s = open(p, encoding="utf-8").read()
reps = [
 ("Status: Draft\n", "Status: Draft (audited claim by claim against the book text, chapter notes and wiki; claims found in none of the three were removed; remaining unsourced items are listed in TODO_Verification.md)\n"),
 ("Sources: Books 1-13 (chapter notes), fan wiki for lists", "Sources: book text, chapter notes, fan wiki"),
 ("typical lifespans run from about 60-75 years (normal) to about a hundred (bronze), two hundred (silver), five hundred (gold), and indefinite at diamond;",
  "essence users age slower: bronze-rankers can live well past a hundred, silvers can double that, gold-rankers live for centuries, and it is rumoured that diamond-rankers cannot die of old age (Book 1, Rufus);"),
 ("| Diamond | Category 5 | Ageless; the peak of mortal power; few exist |", "| Diamond | Category 5 | The peak of mortal power; few exist; rumoured not to die of old age |"),
 ("| Gold | Category 4 | No need to breathe; centuries-long life; advancement now needs insight, not just fighting |", "| Gold | Category 4 | No need to breathe; centuries-long life |"),
 ("Major gods govern broad domains (Ocean, Storm, War, Knowledge, Healer, Dominion, Hero, Death), minor gods narrower ones (Farmer, Mason, Grocer, Hygiene, Fertility, Hearth). Evil or hidden gods are Deceit, Destruction, Pain, Undeath, Discord.",
  "Gods named in the books include Knowledge, Healer, Dominion, Hero, Death, Fertility, Hearth, Destruction, Discord, Undeath and Pain, with Purity (or Disguise) a special case; see `02_Cosmology_and_Powers/Gods_and_Churches.md`."),
 ("a servant race grown on birthing trees, bred into obedience and capped at silver by a brand placed in the soul.", "a servant race grown on birthing trees, bound by a brand placed in the soul that enforces rank limits (notes, Books 10-11)."),
 ("is a fragment of an essence that cannot be assembled into a full essence. It is used in rituals, alchemy, forging and as fuel.", "appears as gems of an essence's theme (for example Dark Quintessence Gems, Book 1) and is used in crafting."),
 ("**Quintessence**: fragment of an essence.", "**Quintessence**: crafting gems of an essence's theme."),
 ("branch offices run by political directors.", "branch offices run by directors."),
 ("pirates, McKean's vine, Knowledge", "pirates, Elizabeth's blood weapons, Knowledge"),
 ("Reaper (death's finality)", "Reaper (death's finality)"),
]
for a, b in reps:
    if a not in s:
        print("MISSING:", a[:60])
    s = s.replace(a, b)
open(p, "w", encoding="utf-8").write(s)

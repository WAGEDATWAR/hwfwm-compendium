base = r"C:\Users\Gabriel\Documents\World Stuff\HWFWM Compendium"

def edit(rel, pairs):
    p = base + "\\" + rel
    s = open(p, encoding="utf-8").read()
    for a, b in pairs:
        if a not in s:
            print("MISSING in", rel, ":", a[:70])
        s = s.replace(a, b, 1)
    open(p, "w", encoding="utf-8").write(s)

edit("01_World_Primer.md", [
 ("Rank-ups depend on all abilities reaching the next rank.", "A person cannot advance until all attributes have reached the next rank (Book 5)."),
 ("**Soul crests** are tattoo-like identifiers verified by the Adventure Society.", "**Soul crests** are magical tattoos printed on the soul, which appear on the body (Book 2)."),
])

entry = """**Audit of early documents (`01_World_Primer.md`, `Appendices/Glossary.md`, `Appendices/Name_Index.md`, `03_Magic_and_Adventuring/Magic_and_Adventuring.md`)**
- Audited claim by claim against the book text, chapter notes and wiki, per the user's instruction; nothing was kept on the strength of the lorebook.
- Name Index: first-appearance books corrected and unsupported descriptions removed (for example Amos and Orin Pensinata first appear in Book 7, Gerling's death in Book 6 is removed, Dawn is the First Servant and hierophant of the World-Phoenix, the Garret Headingway kidnapping is removed, Valdis is no longer listed as a Geller).
- Glossary: reworded or removed the Adventurer attribution (Jason's Book 12 speech, not Rufus), the blood parasite / blood oak / blood root vine entry (the vine is a Book 2 Pallimustus monster; blood oaks are Elizabeth's Earth weapons per Jason's Book 13 guess), the Brand entry (rank limits are a function of the brand, Boris, Book 11), the Reaper entry (Shade is one of its shadows, not its child), the Defier of the Will entry (negates the Astral Nexus's influence, Book 12), the Umber entry, the EOA, Cabal, Network and Quintessence entries; dumpling soup is tagged Book 1.
- Primer: lifespans now follow Book 1 (bronze well past a hundred, silver double that, gold centuries, diamond rumoured not to die of old age) instead of the 60-75 / 100 / 200 / 500 figures; the god-domain lists were cut to gods named in the books; messengers are "bound by a brand that enforces rank limits" rather than "capped at silver"; "McKean's vine", "political directors" and the quintessence "fragment" description removed; rank-ups depend on attributes (Book 5); soul crests are soul tattoos (Book 2).
- Magic and Adventuring (sections 1-7 and 15-19): restricted-essence paragraph rewritten from Books 1-2 (the Sacrifice-confluence contracts and "Doom unrestricted" claims removed); Dragon, Garuda, Prosperity, Onslaught and Master examples re-tagged; lifespan table follows Book 1; the invented rank-up timings and "wall at high silver" removed; resurrection, soul crest and time-magic wording sourced; the Death-goddess pact, undeath and vampire-sickness lines removed.
- Status: **audited**; remaining open items are listed in `TODO_Verification.md`, sections B and G.

"""
edit("Appendices/Change_Log.md", [("## Pending index updates", entry + "## Pending index updates")])

edit("TODO_Verification.md", [
 ("### Not yet re-checked\n- Sections 1-7 and 15-19 (essences, confluences, stones, abilities, attributes, ranks, cores; souls and healing, unusual magic, Earth's version, changes over the series, roleplay notes) beyond the spot checks.\n",
  "### Open after the audit\n- Sections 1-7 and 15-19 were audited; the \"essence revelation\" gold-rank claim rests on the wiki only, the silver killing-blow and ~200-year figures on the wiki, and the Cabal tier grading on the wiki.\n- Whether the books anywhere describe a \"wall\" at high silver beyond the core-user stall (Book 1).\n"),
 ("## G. Audit of early documents\n\n`01_World_Primer.md`, `Appendices/Glossary.md`, `Appendices/Name_Index.md` and parts of `03_Magic_and_Adventuring/Magic_and_Adventuring.md` were drafted before the source hierarchy was restated, mainly from the chapter notes and the lorebook. Each claim should be traced to the book text, notes or wiki and tagged accordingly; any claim found only in the lorebook should be removed. The Primer's geography and history sections and the Glossary's entries on gods, astral beings and messengers should be audited first.\n",
  "## G. Audit of early documents\n\nThe Primer, Glossary, Name Index and Magic and Adventuring sections 1-7 and 15-19 have been audited against the three tiers (see the Change Log). Still open:\n- Primer sections 9-12 (cosmos, institutions, geography) were checked for the riskiest claims only; sentence-level tier tags are not yet added to the Primer.\n- Glossary: the Echo spirit, Hierophant and Immortal Crest entries are supported but lack tier tags; the EOA entry rests on notes and wiki only.\n- Name Index: entries not touched in the audit (supporting cast without a description) have not been re-read against the books.\n- Whether Jason's \"thumbs-up\" coin wording matches the books exactly (Primer section 7).\n"),
])

# structure doc note
edit("00_Project_Structure.md", [])

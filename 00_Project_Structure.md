# HWFWM Compendium: Project Structure and Working Guide

*This document organises the project. It is the file to open first when deciding what to write next, where something belongs, or how to write it.*

## 1. Purpose and scope

The compendium is a reference for running roleplay in the world of *He Who Fights With Monsters* (Shirtaloon), Books 1-13. It describes the setting: what exists, how it works, who is who, what happened and why it matters in play. It is **not a game system**. It contains no dice, stat blocks, balance rules or point costs; where the books give rank names or ability names, those appear as world facts, not mechanics.

Goals:
- Be accurate to the books (the sources of truth), with the fan wiki as a secondary aid.
- Be detailed enough that a game master or a language-model roleplay can run any part of the world without consulting the novels.
- Be modular: each document stands alone, links to others, and can be updated without rewriting the rest.
- Be safe to use at any point of the story: every fact is tagged with when it becomes true and how spoiler-heavy it is.

## 2. Source hierarchy and conflict policy

1. **Book text** (the 13 transcripts) always wins.
2. **Chapter summaries** (per-book notes made while reading) are working summaries; confirm anything important against the book text.
3. **The fan wiki** fills gaps and gives lists (essence names, stone lists) but has known errors and an incomplete timeline.
4. **The lorebook JSON** (`hwfwm_lorebook.json`) is **not a source**. It is a derived product that is updated after this compendium has been built and verified. Never cite it, never copy a claim from it without checking tiers 1-3, and never tag a claim "(lorebook)".

Every claim in a compendium document should be traceable to one of the first three tiers. Tag the weaker tiers explicitly: **(Book N, confirmed)** for the book text, **(chapter notes)** for the summaries, **(wiki)** for the wiki. A claim found in no tier is removed or listed in `TODO_Verification.md` as unsourced.

When sources conflict, write the book version, and record the disagreement in `Appendices/Open_Questions.md` rather than silently choosing.

## 3. Folder layout (planned)

```
HWFWM Compendium/
  00_Project_Structure.md        (this file)
  01_World_Primer.md             foundation: the world in one document
  02_Cosmology_and_Powers/       astral realm, great astral beings, gods, astral kings, authority, the Cosmic Throne, messengers
  03_Magic_and_Adventuring/      essences, confluences, awakening stones, abilities, ranks, auras, familiars, items, rituals, skill books, monsters
  04_Peoples_and_Cultures/       one file per people (humans, elves, leonids, celestines, draconians, smoulder and brighthearts, runics, merfolk, valash, outworlders...), plus daily life, food and clothing, religion in practice, law and indenture, and an economy document (money, spirit coins, wages, trade, farms, cost of living)
  05_Organisations/              Adventure Society, Magic Society, Alchemy Association, guilds, churches, Network, Cabal, EOA, EDJI, Order of the Reaper...
  06_Places/                     one file per region or city (Greenstone, Vitesse, Rimaros, Yaresh, Cyrion, Earth sites, astral spaces, Jason's domains)
  07_Characters/                 one file per major character, plus group files for minor characters
  08_History_and_Timeline/       `Master_Timeline.md` (overview and calendar) plus `Book_01_Timeline.md` to `Book_13_Timeline.md` (line-cited events per book); era guides, wars and crises still to come
  09_Items_and_Artefacts/        named weapons, regalia, relics, consumables, recurring materials
  10_Roleplay_Support/           era selection, secrets and spoiler management, plot hooks, NPC rosters, tone and voice notes
  src/Source_Text/               book text, one file per chapter (Book_01 to Book_13) with README index
  Appendices/                    glossary, name index, open questions, source map, source register, change log
```

Folders are created only when their first document is written.

**What exists now** (see `Appendices/Change_Log.md` for the history):

- Done as drafts: `01_World_Primer.md`; `Appendices/Glossary.md`, `Name_Index.md`, `Change_Log.md`; `08_History_and_Timeline/Master_Timeline.md`; `03_Magic_and_Adventuring/` (21 topic files plus `00_Magic_Overview.md` and the wiki-tier `Wiki_Reference_Lists.md`: essences, confluences, awakening stones, abilities, afflictions, ranks, cores and training, auras, familiars, rituals, skill books, materials, monsters, the profession, souls and healing, astral spaces and surges, unique magic and Earth's magic); `06_Places/` (overview, Greenstone, Vitesse, Rimaros, Yaresh, Cyrion, `Earth/`, `Astral_Spaces/`).
- Working files at the root: `TODO_Verification.md` (claims not yet confirmed against the book text).
- Started: `02_Cosmology_and_Powers/` (overview, great astral beings, gods and churches, astral kings and messengers) and `05_Organisations/` (overview, Adventure Society, Magic Society and associations, guilds and houses, Earth's powers, cults and orders).
- Started: `07_Characters/` (core cast of the guide drafted: Jason, Rufus, Farrah, Gary, Humphrey, Sophie, Belinda, Clive, Neil, the familiars, Emi, Nik, Danielle, Zara, Dawn, Anna, Boris, Knowledge).
- Started: `04_Peoples_and_Cultures/` (see the Change Log for the files written).
- Started: `09_Items_and_Artefacts/` (overview, soul-bound items and regalia, tokens and relics, consumables, awakening stones, cloud constructs, the Builder's door).
- Started: `10_Roleplay_Support/` (overview, era selection, spoiler management; plot hooks, NPC rosters, tone and voice written).
- Written: `Appendices/Open_Questions.md` (21 cited questions the books leave open) and `Appendices/Source_Map.md`.

## 4. Document categories and what each should contain

| Category | Contents | Default length |
|---|---|---|
| Primer / overview | Plain-language introduction, common facts, FAQs | 3-8 pages |
| Topic reference | One concept in depth (e.g. "Auras", "Resurrection") | 2-6 pages |
| Place file | Geography, history, society, notable people, what it is like to be there, hooks | 2-5 pages |
| Character file | Who they are, appearance, manner, abilities as world facts, history by period, relationships, voice, secrets | 1-4 pages |
| Organisation file | Purpose, structure, membership, methods, key figures, relations, history | 2-4 pages |
| Era guide | State of the world at a chosen point, who is where, what is known and unknown | 3-6 pages |
| Item file | Appearance, origin, properties as fiction, owner history | half page |
| Appendix | Index, glossary, source map, open questions | varies |

## 5. Standard templates

**Header block for every document**

```
# Title
Status: Draft | Reviewed | Verified
Spoiler level: 0 | 1 | 2 | 3   (see section 6)
Valid from: Book N (earliest point where this is true)
Valid through: Book N / present
Sources: B1 ch..., B7 ch... (book and chapter references, or "wiki")
Related: [links to other compendium files]
```

**Character file sections**: Summary / Appearance / Personality and voice / Powers and skills as world facts / Background / Timeline of involvement / Relationships / Secrets and spoiler notes / Roleplay notes.

**Place file sections**: Summary / Location and layout / Society and rule / Magic level / History / Notable people / Customs and daily life / Dangers and opportunities / Hooks.

**Organisation file sections**: Summary / Purpose / Structure and ranks of membership / Methods / Key figures by period / Relationships / History / Hooks.

**Topic file sections**: Summary / How it works / Variations and exceptions / Examples from the books / Common misconceptions in-world / Changes over time.

## 6. Spoiler levels

Because the series changes the nature of its world over thirteen books, every fact is tagged with a level so a scene can be set at any point.

- **Level 0**: public knowledge of the setting at any time (customs, ranks, ordinary monsters).
- **Level 1**: events and facts known inside Books 1-3 (Greenstone-era, the Reaper trials, the Builder cult).
- **Level 2**: Books 4-9 (Earth return, silver, Rimaros, messengers, Yaresh).
- **Level 3**: Books 10-13 (Death Pact, the zone, the Cosmic Throne, the System, Knowledge's plan). Includes the ending.

When writing, put level-2 and level-3 facts in clearly marked sections ("Later developments") rather than in the main text.

## 7. Style rules

- Prose, present tense for how the world is; past tense for history. No note shorthand ("->", "w/", abbreviations).
- Name every person once in full, then by their usual name.
- Prefer concrete detail from the books (colours, phrasing, habits) over generalisation.
- Distinguish **fact**, **in-world belief** and **rumour** explicitly. Many things characters say are wrong or lies.
- Use the series' own terms and spellings (see the glossary in the primer). Spellings that vary in the text: Hurin/Huren, Jonah/Jonas, Hendren/Herston; choose the form most used and note the variant once.
- No mechanics: do not invent numbers for damage, probabilities or costs. Quote numbers only where the books give them as world facts (lifespans, population, timeframes, distances, coin exchange rates).
- Do not copy long passages from the books; summarise and paraphrase.

## 8. Build order (recommended)

1. **01_World_Primer.md** (done in this pass): the foundation.
2. **Appendices/Glossary** and **Name Index**: grows continually.
3. **08 Timeline**: a verified master timeline, with ages, durations and an explicit list of timing conflicts.
4. **03 Magic and Adventuring**: essences and confluences, awakening stones, ranks, auras, familiars, rituals, skill books, monsters. These underpin everything else.
5. **02 Cosmology and Powers**: astral realm, great astral beings and their vessels, gods, astral kings, messengers, authority, the Cosmic Throne. This is the hardest subject to write accurately.
6. **05 Organisations** and **06 Places** in order of narrative importance: Greenstone, Vitesse, Rimaros, Yaresh, Cyrion; Adventure Society, Magic Society, Burning Violet, Network, Cabal; Earth sites.
7. **07 Characters**: starting with the core cast (Jason, Rufus, Gary, Farrah, Humphrey, Sophie, Belinda, Clive, Neil, Danielle, Zara, Dawn, Shade, Colin, Gordon, Stash, Nik, Emi, Anna, Boris, Knowledge), then supporting cast, then minor characters in grouped files.
8. **09 Items** and **10 Roleplay Support**: era guides, plot hooks, secrets sheets.

## 9. Open questions and known inconsistencies (running list)

These come from reading the books and should be resolved or documented in the timeline file.

- **Length of the Cardinas zone and Jason's soul battle (Book 11)** *(revised)*: the book gives "months" for the zone (Nik is "six months old" at Book 11, Ch50 L15) and chains separate intervals for Part II (a year, almost a year, two years, two years); the earlier nine-month and twelve-year figures were wiki-based and are not asserted. See `08_History_and_Timeline/Book_11_Timeline.md`.
- **Gary's death timing**: "about a year" after the Cup of Heroes in the notes; confirm exact chapter wording (Book 11, Ch74).
- **Clan hiding period (Book 12)**: described as "half a decade" in one place and "two years" in another.
- **Jason's father**: Ken Asano (not Hiro); Hiro is an uncle and Shiro another uncle.
- **Zara and the Storm King** *(resolved)*: Emiliano is her brother and also her adoptive cousin; both statements are accurate.
- **Spelling variants**: Hurin/Huren, Jonah/Jonas, Hendren/Herston, Daryll/Darryl, Carlivexistrix/Carli.
- **Soul forge**: Jason's realm lacks one until the Book 11 reintegration, although Book 8 and Book 12 appendices list soul forge among the Relics of the King.
- **Age of earthlings' arrival** *(resolved)*: "fifteen years ago" (Pallimustus speakers, about 2037) and "seventeen years ago" (Lenora Coleman on Earth, 2038) are rounded statements about the same autumn-2021 event; see `08_History_and_Timeline/Master_Timeline.md`, section 12.
- **Wiki timeline errors**: Asano Village timing (the text says about six months of building), the surge delay (five years, not fifteen), and the Book 5-6 month counts, which do not fit the seasonal cues; see the Master Timeline.
- **Butterflies of Makassar** *(resolved)*: the name news broadcasts give to the public spectacle of Gordon's Harbinger of Doom swarm over the Makassar undead (Book 5).
- **Greenstone's status** *(resolved)*: a colony settled from Estercost, not part of Estercost proper (Books 11-12).
- **Open claims**: the remaining unconfirmed details for the Places and Magic documents are listed in `TODO_Verification.md`.

## 10. Maintenance practices

- Keep the **Source Register** (`Appendices/Source_Register.md`) current: add or update a row for every new tier-tagged claim with its `B# Ch# L#` reference, and log narrowed results in `Appendices/Source_Map.md`.
- Keep a **Change Log** in `Appendices/Change_Log.md` listing each document added or revised, with the date. Update it at the end of every writing or verification session, not afterwards.
- After writing any file, update the **Name Index** and add any new terms to the **Glossary**.
- Mark each document's Status; a document is "Verified" only after being checked against the book text.
- When a later book changes something, do not delete the earlier fact; add a dated "Later developments" note.

## 11. Immediate next documents

State of the project (2026-10-22): every numbered section has had a verification pass and the open work is organised in tiers in `TODO_Build_Plan.md`; `TODO_Verification.md` holds unconfirmed claims. The earlier list below is kept for reference and is superseded by the build plan where they differ.

1. **Remaining notes-tier claims**: a handful of claims (each marked "not located" in its document, e.g. Zara's adoption and kiss, Musin's elf/gold notes, Farrah's aura lessons, Anna's Book 12 recruitment) across the character and places files still rest on chapter notes because the book lines were not found after a second narrowing pass (the Book 13 founder/Noreth reveal, Elizabeth in Venice, the spirit-vault gardens, the Sky Link island and others were moved to book lines) (listed as notes rows in the Source Register); the wiki tier now consists of the deliberate lists in `03_Magic_and_Adventuring/Wiki_Reference_Lists.md` and the gods table in `Gods_and_Churches.md`. The 01 World Primer was verified on 2026-10-22 (its sections 8-12 stay summaries of the topic documents). The 04 and 09 documents were verified on 2026-10-22. The 10_Roleplay_Support files were verified the same day. Every numbered section has now had a verification pass; the open work is the follow-up lists below, grow the book cross-references in the wiki lists, and re-check the Cosmology files against Book 12 and Book 13 statements about the Cosmic Throne and the System.
2. **06_Places/ follow-up**: every smaller place named in the books with more than a passing mention is now written (`Minor_Places/`, 16 files) and the earlier-notes claims are settled. Remaining: places named only once (the Great Southern Continent, Casallini, Lindover Mill, Leust's neighbours), which the Overview lists; add files if later scenes give them substance.
3. **07_Characters/**: every recurring figure from `TODO_Verification.md` section B has a file or a grouped entry, and Name_Index, Glossary and the NPC rosters were updated on 2026-10-22. Still open: the wider cast named only in passing (use `Minor_Cast/` for them), plus the Moon's Edge leadership and Sigrid's "Father" questions in the Change_Log.
4. **08_History_and_Timeline/**: place the Book 12 closing chapters (Ch62 to Ch67: the Earth arrival, the artefact-site battle and the reunion with Emi), add a second detail pass on Books 12 and 13, and write the era guides (the Builder cult, the Rimaros surge and the Battle of Yaresh, the Cardinas expedition and zone, the Earth vampire war).
5. **03_Magic_and_Adventuring/**: grow `Essence_Catalogue.md` toward every essence the books name, extend the bestiary in `Monsters.md` by rank and region, and cross-check the 09 item files against the new topic files.
6. **04_Peoples_and_Cultures/**: remaining regional cultures (Dreisil, Kazlahk, Jayapura, the Ustei homeland), clothing and food by region. Culture files still to write (noted 2026-10-22): Girlano, Sadi Andali, Zartos, the Dragon Lands and Vitesse; merfolk (one line only) and goblins/fairies (Earth-side only) need more text.
7. **09_Items_and_Artefacts/ and 10_Roleplay_Support/**: more items and hooks; extend rosters when new character files are added. Item gaps noted 2026-10-22: Hegemon's Dominion as its own entry, Jason's dimensional storage and portals, Emir's other items, guild and Adventure Society badges.
8. **Source checking**: read the rows graded weak in `Appendices/Source_Register.md` (about 36) and spot-check the keyword-generated state-change list in `Source_Map.md`. Rebuild both with `src/tools/build_register.py` after editing any document.
9. Keep `Appendices/Open_Questions.md`, `TODO_Verification.md`, the Glossary and the Name Index current as questions are settled and new terms are written.

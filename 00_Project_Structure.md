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
2. **Chapter summaries** (per-book notes made while reading, kept in `src/Chapter_Notes/`) are working summaries; confirm anything important against the book text.
3. **The fan wiki** fills gaps and gives lists (essence names, stone lists) but has known errors and an incomplete timeline.
4. **The lorebook JSON** (`hwfwm_lorebook.json`, now in `src/tools/archive/`) is **not a source**. It is a derived product that is updated after this compendium has been built and verified. Never cite it, never copy a claim from it without checking tiers 1-3, and never tag a claim "(lorebook)".

Every claim in a compendium document should be traceable to one of the first three tiers. Tag the weaker tiers explicitly: **(Book N, confirmed)** for the book text, **(chapter notes)** for the summaries, **(wiki)** for the wiki. A claim found in no tier is removed or listed in `TODO_Verification.md` as unsourced.

When sources conflict, write the book version, and record the disagreement in `Appendices/Open_Questions.md` rather than silently choosing.

## 3. Folder layout and current state

```
HWFWM Compendium/
  00_Project_Structure.md        this file
  01_World_Primer.md             foundation: the world in one document
  02_Cosmology_and_Powers/       astral realm, great astral beings, gods, astral kings, messengers
  03_Magic_and_Adventuring/      essences, confluences, awakening stones, abilities, ranks, auras, familiars, rituals, skill books, monsters, wiki-tier lists
  04_Peoples_and_Cultures/       one file per people, regional cultures, daily life, religion in practice, law and indenture, economy
  05_Organisations/              Adventure Society, Magic Society and associations, guilds and houses, Earth's powers, cults and orders
  06_Places/                     cities and regions; Earth/, Astral_Spaces/ and Minor_Places/ subfolders
  07_Characters/                 one file per character; Minor_Cast/ holds grouped files for lesser figures
  08_History_and_Timeline/       Master_Timeline.md plus Book_01_Timeline.md to Book_13_Timeline.md (line-cited events per book)
  09_Items_and_Artefacts/        named weapons, regalia, relics, consumables, recurring materials
  10_Roleplay_Support/           era selection, spoiler management, plot hooks, NPC rosters, tone and voice
  Appendices/                    glossary, name index, open questions, source register, source map, change log
  TODO_Verification.md           claims not yet confirmed against the book text
  TODO_Build_Plan.md             everything still to build, in tiers
  src/Source_Text/               book text, one file per chapter (Book_01 to Book_13) with README index; not committed to git
  src/Chapter_Notes/             per-book chapter summaries (the "notes" tier)
  src/tools/                     scripts and data that build and check the compendium (see its README.md); archive/ holds retired scripts
```

**State of the project** (2026-10-22; the Change_Log has the history):

| Area | Files | State |
|---|---|---|
| `01_World_Primer.md` | 1 | Verified against the book text; sections 8-12 are summaries of the topic files |
| `02_Cosmology_and_Powers` | 4 | Verified once; thin for the importance of the topic |
| `03_Magic_and_Adventuring` | 22 | Verified; essence and monster lists incomplete; wiki-tier lists marked |
| `04_Peoples_and_Cultures` | 22 | Verified; several regional cultures unwritten |
| `05_Organisations` | 6 | Verified once; thin |
| `06_Places` | 34 | Third verification pass done; 16 smaller places written |
| `07_Characters` | 137 | Core cast verified; recent files verified by cite |
| `08_History_and_Timeline` | 14 | Per-book timelines done; Book 12 closing chapters not yet placed |
| `09_Items_and_Artefacts` | 7 | Verified; narrow |
| `10_Roleplay_Support` | 6 | Verified; no era packs |
| `Appendices` | 6 | Source Register and Source Map are generated by `src/tools/build_register.py` |

The Source Register currently holds about 3,750 graded rows (most "ok", about 50 "weak", 16 wiki and 1 notes row). `Appendices/Open_Questions.md` holds 24 numbered entries, several now resolved or narrowed.

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
Status: Draft | Reviewed | Verified   (current files use "Draft (...)" followed by a note on how they were checked)
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

**Spoiler tags.** A document's header level (the first digit of its `Spoiler level:` line) is the level of its untagged text. A section that needs a higher level is wrapped in a pair of HTML comments, which do not render:

```
<!-- level:3 -->
## Later developments (spoilers)
...
<!-- /level -->
```

Rules: the level is 0-3; a tagged section may not be lower than the header level; tags may nest only when the inner level is at least the outer level; open and close tags must balance. Indexes and files whose header says "mixed" carry no tags. Use tags wherever a file mixes levels; a file whose header level already covers everything needs none. `src/tools/lint.py` checks the tags, and `src/tools/spoiler_tags.py` proposes tags for headings such as "Later developments" or "(Level N)" (the level of a "Later developments" section is taken from the latest book cited in it: Books 1-3 give 1, Books 4-9 give 2, Books 10-13 give 3). The planned export tool (build plan item 5.5) will keep a tagged section only when its level is at or below the level requested.

## 7. Style rules

- Prose, present tense for how the world is; past tense for history. No note shorthand ("->", "w/", abbreviations).
- Name every person once in full, then by their usual name.
- Prefer concrete detail from the books (colours, phrasing, habits) over generalisation.
- Distinguish **fact**, **in-world belief** and **rumour** explicitly. Many things characters say are wrong or lies.
- Use the series' own terms and spellings (see the glossary in the primer). Spellings that vary in the text: Hurin/Huren, Jonah/Jonas, Hendren/Hedron, Daryll/Darryl, Carlivexistrix/Carli, Sigrid Freyn/Volaire; choose the form most used and note the variant once in the Glossary's variants table (`Appendices/Glossary.md`, last section).
- No mechanics: do not invent numbers for damage, probabilities or costs. Quote numbers only where the books give them as world facts (lifespans, population, timeframes, distances, coin exchange rates).
- Do not copy long passages from the books; summarise and paraphrase.

## 8. Build order

The original recommended order has been followed: the primer; the glossary and name index; the timeline; magic; cosmology; organisations and places; characters; items and roleplay support. Every numbered section now exists and has had at least one verification pass. What remains is organised in tiers in `TODO_Build_Plan.md`: tooling and hygiene first, then closing open items, then the thin reference areas (cosmology, organisations, cultures, characters), then era guides and roleplay products.

## 9. Open questions and known inconsistencies (running list)

The cited questions live in `Appendices/Open_Questions.md` (24 entries); unconfirmed claims live in `TODO_Verification.md`. The items below are the ones that shape how the project is written.

- **Length of the Cardinas zone and Jason's soul battle (Book 11)** *(narrowed)*: about six to eleven months for the zone (Nik is "six months old" at Book 11, Ch50 L15; Gary is "almost a year" past the Cup of Heroes at Book 11, Ch68 L703); the Part II intervals (a year, almost a year, two years, two years) are on separate clocks. The earlier wiki-based nine-month and twelve-year figures are not asserted. See `08_History_and_Timeline/Book_11_Timeline.md` and Open_Questions 15.
- **Gary's death timing** *(resolved)*: "Almost a year later" after he became a demigod (Book 11, Ch68 L703); Book 11 has no Ch74.
- **Clan hiding period** *(resolved)*: "two years" (Book 11, Ch68 L2260) and "half a decade" (Book 12, Ch1 L93) are snapshots at different dates; see the Master Timeline, section 7.
- **Jason's father**: Ken Asano (not Hiro); Hiro is an uncle and Shiro another uncle.
- **Zara and the Storm King** *(resolved)*: Emiliano is her brother and also her adoptive cousin; both statements are accurate.
- **Spelling variants**: see section 7.
- **Soul forge** *(resolved)*: Jason's realm lacks one until the Book 11 reintegration (Book 10, Ch53 L17), and the Relics of the King gift gives access to the astral throne, astral gate and soul forge only "to limited degrees" (Book 12, Ch67 L198), so the appendix lists do not conflict.
- **Book 12 present** *(narrowed)*: the roundings of "fifteen", "seventeen" and "almost twenty" years fit a Pallimustus tour in late 2037 to early 2038, with the Earth arrival and Book 13 in 2038 ("seventeen years" and Jason's forty-four years, Book 12, Ch67 L65, L113); see Open_Questions 18 and `08_History_and_Timeline/Master_Timeline.md`, section 12.
- **Wiki timeline errors**: Asano Village timing (the text says about six months of building), the surge delay (five years, not fifteen), and the Book 5-6 month counts, which do not fit the seasonal cues; see the Master Timeline.
- **Butterflies of Makassar** *(resolved)*: the name news broadcasts give to the public spectacle of Gordon's Harbinger of Doom swarm over the Makassar undead (Book 5).
- **Greenstone's status** *(resolved)*: a colony settled from Estercost, not part of Estercost proper (Books 11-12).

## 10. Maintenance practices

- Keep the **Source Register** (`Appendices/Source_Register.md`) and **Source Map** current by running `python3 src/tools/build_register.py` after any document edit; both files are generated, so never edit them by hand. Read any new "weak" rows it reports.
- Keep a **Change Log** in `Appendices/Change_Log.md` listing each document added or revised, with the date. Update it at the end of every writing or verification session, not afterwards.
- After writing any file, update the **Name Index** and add any new terms to the **Glossary**, and list the file in its folder's overview.
- Mark each document's Status; a document is "Verified" only after being checked against the book text.
- When a later book changes something, do not delete the earlier fact; add a dated "Later developments" note.
- **Version control**: the folder is a git repository with a private GitHub remote (`origin`, branch `main`). `src/Source_Text/` is ignored because the book text is copyrighted; do not add it to any commit. Commit after each completed build-plan item with a message naming the item; tag a release (`0.0.2`, `0.1.0`, and so on) when a tier or a section reaches a stable state. The wiki cache and generated pickles in `src/tools/` are also ignored.
- **Tools**: all scripts live in `src/tools/` and run from any directory (see `src/tools/README.md`). Write document-generating scripts to a file and run them rather than pasting them into a shell heredoc, because apostrophes in prose break heredocs.

## 11. Next steps

The open work is listed in tiers in `TODO_Build_Plan.md` (tooling and hygiene, closing open items, thin reference areas, history and synthesis, roleplay products, quality assurance, stretch goals) and the unconfirmed claims in `TODO_Verification.md`. Do the plan's Tier 0 first, then Tier 1. When an item lands, mark it done in the plan, log it in `Appendices/Change_Log.md`, rebuild the register and commit.

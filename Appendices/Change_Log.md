# Change Log

Status: Working document (kept current after every writing session)
Spoiler level: 0 (no setting facts; this is a record of work)
Valid from: project start
Valid through: ongoing
Sources: project history
Related: ../00_Project_Structure.md (sections 3, 9, 10, 11), ../TODO_Verification.md

## How this log works

The project guide (section 10) requires a change log in `Appendices/` that lists each document added or revised, with the date. Use these rules when adding entries:

1. **One line per document per session.** Name the file by its path from the compendium root, say whether it was **Added**, **Revised** or **Verified**, and describe the change in a sentence.
2. **Record the cause of a revision**: a correction from the user, a book-text check, a source conflict, or an addition of new content.
3. **Record each verification pass** (which sources, which claims) and say what remains in `TODO_Verification.md`.
4. **Update the maintenance chain after every document**: Name Index, Glossary, this log, the Status line in the document's header, and the "Immediate next documents" list in the project guide.
5. **Do not delete earlier facts when later books change them**; add a "Later developments" note and log it here.
6. **Dates** are the session date. Entries from the first sessions were reconstructed from the file history; where a session date was not recorded they carry the date of the first full session in which the work was confirmed.

Status values used in headers: Draft (written, not yet checked against the book text), Reviewed (read through for consistency), Verified (every claim checked against the book text).

## Log

### 2026-10-20

**Lorebook (outside the compendium, `World Stuff/hwfwm_lorebook.json`)**
- Revised: rebuilt after removing the implied Vincent Trenslow and Rufus relationship at the user's request (the books only imply it). Now 598 entries.

**Foundation**
- Added `00_Project_Structure.md`: purpose, source hierarchy, folder layout, templates, spoiler levels, style rules, build order, open questions, maintenance practices.
- Added `01_World_Primer.md`: the foundation primer.
- Added `Appendices/Glossary.md`: first draft of roughly 200 entries with spoiler tags and a spelling-variants table.
- Added `Appendices/Name_Index.md`: first draft of roughly 250 names.
- Added `08_History_and_Timeline/Master_Timeline.md`: timeline in months since arrival, with ages and rank markers.
- Revised the Name Index and Master Timeline after a check against the book text: Lorelei Grantham's first appearance, Mr North's first appearance, Adrien Barbou's fate wording, the Earthlings' arrival moved to Book 7, Makassar recorded as Jason's third death and Shako's kill as the fourth.

**Magic and Adventuring**
- Added `03_Magic_and_Adventuring/Magic_and_Adventuring.md` as a single combined document (19 parts). The project guide had planned two files, `Essences_and_Confluences` and `Ranks_Auras_and_Abilities`; one document was written instead. Split it when it becomes unwieldy.
- Revised after a first book-text check of confluences, racial gifts, ranks, lifespans and core use: corrected Onslaught's user, removed unverified Mystic and Charlatan recipes, attached the Garuda confluence to Taika, restored that most core users do not reach gold but some do, and noted that monster names appear in the books while rank groupings are approximate.
- Revised after a second check of sections 8-14 (auras, rituals, mirage chambers, sky link and water link, adventuring practice, astral spaces): removed unsupported figures and items, corrected the sky link naming, expanded the mirage chamber text.
- Status: **Draft (spot-checked)**. Sections 1-7 and 15-19 remain to be re-checked.

**Places (`06_Places/`)**
- Added `00_Places_Overview.md`, `Greenstone.md`, `Vitesse.md`, `Rimaros.md`, `Yaresh.md`, `Cyrion.md`.
- Added `Earth/00_Earth_Overview.md`, `Casselton_and_Asano_Village.md`, `Incursion_Sites.md`, `Nitra.md`, `Saint-Etienne.md`, `Artefact_Site_One.md`.
- Added `Astral_Spaces/00_Astral_Overview.md`, `Desert_Astral_Space.md`, `City_of_Fallen_Echoes.md`, `Reaper_Trials_Boarding_Vessel.md`, `Spirit_Vault_and_Astral_Kingdom.md`, `Transformation_Zones.md`.
- First verification pass: corrected Greenstone's Fortress, tunnels and duke; Rimaros's islands and central landmass; Hana Shavar's placement; Cyrion's indentured house guards; Earth sites' population and survivor figures; zone and astral details.
- Second verification pass (book text, all 06_Places files): confirmed or corrected the items listed in the TODO's earlier sections, including Greenstone as a colony of Estercost, the Queen of Estercost, fallen world-engineer golems beyond Cyrion, Asano Village's tunnels and its special-interest status, the Broken Hill figures, Todd Halverson, the artefact site's destruction of its town, Ascension's Gate, the turquoise lagoon, New Water and the Duke of Boko, and Rexion's ring of temples.
- Revised `Earth/Incursion_Sites.md` at the user's instruction: the Butterflies of Makassar are the name for the public spectacle of Gordon's Harbinger of Doom swarm; the book text (Book 5) was used to describe it.
- Status: **Draft (twice spot-checked)**. A third pass remains; see `TODO_Verification.md`, section A.

**Cosmology and Powers (`02_Cosmology_and_Powers/`)**
- Added `00_Cosmology_Overview.md`, `Great_Astral_Beings.md`, `Gods_and_Churches.md` and `Astral_Kings_and_Messengers.md`. Items marked "confirmed" in the documents were checked against the book text while writing (dumpling soup, the sundering's factions, Rules of Intrusion, Zithis Carrow Vayel, Erigo Fin Desca, the gestalt nature of messengers, Dominion on kneeling, Hana Shavar's role). Everything else comes from the lorebook and wiki and is flagged.
- Status: **Draft (partly checked)**; the unchecked items are in `TODO_Verification.md`, section D.
- Verification pass on all four Cosmology files against the book text. Corrected: the dumpling-soup chapter is Book 1 chapter 69, not Book 3 (also fixed in `06_Places/Astral_Spaces/00_Astral_Overview.md`); Interstice admits gold-rankers only as menial workers; the fundamental realm is what the books call node space. Confirmed and added: the World-Phoenix's own account of sanctioning itself from the Boundary, the Reaper's vessel Velius, Helsveth as the World-Phoenix's vessel, hierophants (Books 3, 7), Disguise creating the Order of Redeeming Light (Book 10), Death's appearance and the pact's terms, Hero sanctioning himself, Knowledge's description and invasion plan, the third of her priests who are spies, the cube leaving Gabrielle Pellin's chest, the brand and the rise of astral kings who were messengers, the Council of Kings, Vesta Carmis Zell as Tera's astral king master, and the alabaster, gold-eyed, winged appearance of messengers. Removed or hedged: Marek as Unorthodoxy leader, the silver cap and seal, "budded", the Hero confluence claim.
- Status after the pass: **Draft (verified in part)**; remaining items are in `TODO_Verification.md`, section D.

**Organisations (`05_Organisations/`)**
- Added `00_Organisations_Overview.md`, `Adventure_Society.md`, `Magic_Society_and_Associations.md`, `Guilds_and_Houses.md`, `Earth_Powers.md`, `Cults_and_Orders.md`. Items marked "confirmed" were checked against the book text while writing.
- Findings that corrected earlier documents: the Adventure Society badge is an iron medallion with the sword-and-rod-over-a-shield emblem (restored in Magic and Adventuring); about three in ten adventurers are in a guild, one in ten in a high-end guild, and guilds receive sixty percent of surge quotas (Book 7; restored in Magic and Adventuring); the Aristocratic Faction exists under that name (Book 10; added to `06_Places/Yaresh.md`); Nitra's steam engines run on fire and water quintessence (Book 11; `06_Places/Earth/Nitra.md`); each continent appears to have its own continental council (Rakesh and Cyrion; `06_Places/00_Places_Overview.md`).
- Status: **Draft (partly checked)**; unchecked items are in `TODO_Verification.md`, section E.
- Verification pass on the remaining Organisations items against the book text. Confirmed and added: field testing at the start of every month and the monthly patrol rota; Instructors Trenslow and Spalding; Jason's gold diamond badge; Pochard Finn as de facto director of Greenstone's Magic Society; Lorelei Grantham's path from Continental Council researcher (Book 3) through the Rakesh research wing (Book 6) to MRA Vice Chancellor (Book 12) and her portal network project; Neiman Bassingthwaite and the Burning Violet crisis, including Team Biscuit's withdrawal; Gormanston Bynes's thoughts, Juniper and Calcifer Bynes; Mr North as a rune spider and the founder's familiar; Boris's role in betraying the founder to the early societies; the former Mrs South; Marie Finnegan as the recently expelled Zurich director with seven reality cores; the churches' bargain with the vorger; Zato, Timos and Beaufort; Melody Jain, Sendira and Laront. Corrected: Noreth did not betray the founder to "the American branch" in the text I read.
- Status after the pass: **Draft (verified in part)**; remaining items in `TODO_Verification.md`, section E.

**History and Timeline (`08_History_and_Timeline/`)**
- Revised `Master_Timeline.md` (second version) against the book text and the confirmations made since it was written. Added a calendar-anchors section (born 1 April 1994; arrival late November 2017; return early June 2019; the age-26 birthday in April 2020; departure in autumn 2021; Book 13 in 2038) derived from statements in Books 1, 4, 5, 10, 12 and 13, and marked book-confirmed rows with [book].
- Corrections: the surge delay was "some five years overdue" (Book 7), not fifteen; the Network's founder's familiar, Mr North, was betrayed with Boris's help to the early magic societies, not "the American societies"; Broken Hill's dead are Jason's estimate of ten to fifteen thousand, with over nineteen thousand survivors; the order in Book 5 is Broken Hill, then the April birthday scene, then Makassar, Jason's silver rank, Kostroma, and the deaths of Kaito, Asya and Greg; the "System withdrawal at Cyrion" is now the System withdrawal for slavery and indenture regions; the departure from Earth is placed in autumn 2021 rather than the wiki's M49; the Earthlings' "fifteen versus seventeen years", the Book 3 winter question and the "fifteen versus sixteen years away" conflict are resolved as roundings and hemisphere seasons.
- Also revised for consistency: `01_World_Primer.md` (surge overdue by about five years) and `00_Project_Structure.md` (section 9 open questions updated).
- Status: **Draft (anchors verified; later month counts approximate)**; remaining items in `TODO_Verification.md`, section F.

**Source-hierarchy correction (user instruction)**
- The user stated that the lorebook is not a source: the hierarchy of truth is book files, then chapter summaries, then the wiki, and the lorebook is updated only after the compendium is verified. Earlier documents had cited the lorebook as a fallback source and marked claims "(lorebook)".
- Revised `00_Project_Structure.md` section 2 to state this rule, require tier tags ("Book N", "notes", "wiki") and forbid "(lorebook)" tags.
- Searched every claim tagged "(lorebook)" across `02_Cosmology_and_Powers/`, `05_Organisations/`, `06_Places/`, `07_Characters/` and `08_History_and_Timeline/` against the book text, chapter notes and wiki. Claims found in a tier were retagged with it; claims found in none were removed or recorded in `TODO_Verification.md`. Examples of removals: the World-Phoenix's appearance, the Shade body count of two hundred, the Hero-confluence assertion as fact, the Quilido Centre at Nitra, the fifteen-year hardening of the artefact site, the Aristocratic Faction's lorebook-only members, the "mindless and alien" description of great astral beings.
- Examples of newly confirmed items: Kazlahk University of Medicine and Zartos (Books 7 and 11), Pochard Finn's directorship (Book 11), the Asano Village tunnel ending at Jason's cloud house on the seabed (Book 5), the Cabal's holding of Africa and Russia (Book 6), Dawn's "best case" (Book 5), Legion as the administrator of life's rules (Book 8), the compact between the Builder, Reaper and World-Phoenix (notes, Book 6), Sophie's engagement to Humphrey (notes, Book 11).
- Rewrote `Gods_and_Churches.md` and all of `07_Characters/` so that every claim carries a tier tag.
- Recorded the correction as a standing memory note for future sessions.
- Status: all `(lorebook)` tags removed from the compendium except where this log names them. `TODO_Verification.md` section G flags that the Primer, Glossary, Name Index and early Magic and Adventuring text still need a claim-by-claim audit.

**Characters (`07_Characters/`)**
- Added `00_Characters_Overview.md`, `Jason_Asano.md`, `Rufus_Remore.md`, `Farrah_Hurin.md`, `Gary.md`, `Humphrey_Geller.md`, `Sophie_Wexler.md`, `Belinda_Callahan.md`, `Clive_Standish.md`, `Neil_Davone.md` and `Familiars.md` (Shade, Colin, Gordon and Stash). First versions leaned on the lorebook; rewritten the same session using only the book text, notes and wiki.
- Restored in `03_Magic_and_Adventuring/Magic_and_Adventuring.md`: Mystic is Swift + Balance + Wind (Book 2); Belinda's essences are Magic, Trap and Adept (Book 2); Clive's Karmic confluence is Magic, Rune and Balance (Book 2).
- Added `Emi_and_Nik.md`, `Danielle_Geller.md`, `Zara_Rimaros.md`, `Dawn.md`, `Anna_Tilden.md`, `Boris_Ket_Lundi.md` and `Knowledge.md`, each written only from the book text, chapter notes and wiki, with tier tags.
- Corrected using the chapter notes: Belinda is married to Estella Warnock in Book 13 (notes), Sophie is engaged to Humphrey (notes, Book 11), Humphrey's dragon confluence is Might, Magic and Wing (notes, Book 13).
- Status: **Draft (sourced)**. The core cast listed in the project guide is now drafted; supporting cast and minor characters are next. Not yet done for characters: updating the Name Index entries for new people.

**Appendices and housekeeping**
- Added `TODO_Verification.md`: the running list of unconfirmed claims; rewritten to hold only unconfirmed items.
- Added this change log (`Appendices/Change_Log.md`). It had been planned in the project guide but was not built until now.
- Revised `Appendices/Glossary.md`: added Butterflies of Makassar, Dimensional ulceration, Harbinger of Doom, Ring gate, Special-interest territory, World engineer.
- Revised `Appendices/Name_Index.md`: added Gordon Truffett, Holly Macrossan, Neiman Bassingthwaite, Todd Halverson, Erigo Fin Desca, Hess Jor Nasala, Vesta Carmis Zell, Zithis Carrow Vayel.
- Revised `00_Project_Structure.md`: section 3 (layout marked with what exists), section 9 (new notes), section 10 (change-log practice), section 11 (next documents; Cosmology is now started).

**Audit of early documents (`01_World_Primer.md`, `Appendices/Glossary.md`, `Appendices/Name_Index.md`, `03_Magic_and_Adventuring/Magic_and_Adventuring.md`)**
- Audited claim by claim against the book text, chapter notes and wiki, per the user's instruction; nothing was kept on the strength of the lorebook.
- Name Index: first-appearance books corrected and unsupported descriptions removed (for example Amos and Orin Pensinata first appear in Book 7, Gerling's death in Book 6 is removed, Dawn is the First Servant and hierophant of the World-Phoenix, the Garret Headingway kidnapping is removed, Valdis is no longer listed as a Geller).
- Glossary: reworded or removed the Adventurer attribution (Jason's Book 12 speech, not Rufus), the blood parasite / blood oak / blood root vine entry (the vine is a Book 2 Pallimustus monster; blood oaks are Elizabeth's Earth weapons per Jason's Book 13 guess), the Brand entry (rank limits are a function of the brand, Boris, Book 11), the Reaper entry (Shade is one of its shadows, not its child), the Defier of the Will entry (negates the Astral Nexus's influence, Book 12), the Umber entry, the EOA, Cabal, Network and Quintessence entries; dumpling soup is tagged Book 1.
- Primer: lifespans now follow Book 1 (bronze well past a hundred, silver double that, gold centuries, diamond rumoured not to die of old age) instead of the 60-75 / 100 / 200 / 500 figures; the god-domain lists were cut to gods named in the books; messengers are "bound by a brand that enforces rank limits" rather than "capped at silver"; "McKean's vine", "political directors" and the quintessence "fragment" description removed; rank-ups depend on attributes (Book 5); soul crests are soul tattoos (Book 2).
- Magic and Adventuring (sections 1-7 and 15-19): restricted-essence paragraph rewritten from Books 1-2 (the Sacrifice-confluence contracts and "Doom unrestricted" claims removed); Dragon, Garuda, Prosperity, Onslaught and Master examples re-tagged; lifespan table follows Book 1; the invented rank-up timings and "wall at high silver" removed; resurrection, soul crest and time-magic wording sourced; the Death-goddess pact, undeath and vampire-sickness lines removed.
- Status: **audited**; remaining open items are listed in `TODO_Verification.md`, sections B and G.

**Source text, Source Map and Source Register (user suggestion)**
- Split the 13 book files into one text file per chapter under `Source_Text/Book_01` to `Book_13` (987 chapter files; index and reference format in `Source_Text/README.md`). Book 5 chapter 4 has no heading in the source and sits inside the chapter 3 file; Book 13 keeps its serial chapter numbers (950-1024).
- Added `Appendices/Source_Register.md`: every tier-tagged claim in the compendium (639 rows, IDs R0001-R0639) with book, chapter and line reference, graded exact (86), probable (183) or candidate (370). Locations were found automatically and none is yet marked verified.
- Added `Appendices/Source_Map.md`: rules for references, the narrowing log, a per-book change log of 91 candidate state changes (deaths, gains, losses, moves), and the plan for threading the Master Timeline through register IDs.
- Status: **framework and first harvest**. Next: narrow the candidate rows chapter by chapter, locate the timeline anchors, and retag notes-only claims to Book N where the text is found.

**Timeline anchors and first narrowing (Source Map)**
- Located 30 Master Timeline anchors in the chapter files and read each at its lines (ages, the November-to-June gap, 1 April birthday, 2038 and 2020 references, surge timing, Broken Hill and Makassar figures, Kostroma, seasons, the One Day War interval); results are in `Appendices/Source_Map.md` section 6. The Asano Village build time was not found.
- Narrowed 64 state-change rows in `Appendices/Source_Register.md`: 44 verified, 20 partial. Thirteen rows could not be found at all after reading (listed in the Source Map narrowing log) and stay open.
- `07_Characters/Dawn.md`: the kill-and-loot line is now tied to Book 8 (the quote) and Book 5 (the replacement avatar), and her true body is tagged Book 7 instead of notes.
- Resolved: "Rules of Intrusion" is Book 12's wording and Book 13 says "Laws of Intrusion"; the Primer should keep "Rules" and note the variant.

**Narrowing of Characters and Magic register rows (Source Register)**
- Read every register row for `07_Characters/` and `03_Magic_and_Adventuring/` at its candidate lines: 116 verified, 106 partial and 144 unlocated across the register (the unlocated total includes rows in other documents that were reviewed or are multi-book tags). Each partial row carries a note saying which part of the claim the lines support.
- Rows now read are logged in `Appendices/Source_Map.md` (narrowing log); the change log by book (section 5) was rebuilt from the updated register.
- Not yet read: `02_Cosmology_and_Powers/` (75 rows), `05_Organisations/` (77), `06_Places/` (51), `08_History_and_Timeline/` (7), Appendices (16) and the Primer (12).

**Narrowing of Cosmology, Organisations and Places register rows (Source Register)**
- Read every register row for `02_Cosmology_and_Powers/`, `05_Organisations/` and `06_Places/` at its candidate lines. Register-wide: 221 verified, 177 partial, 206 unlocated, 35 still only automatic (Primer 12, Timeline 7, Appendices 16).
- Found: the Book 4 Inventory description says only the owner may enter the space and others cannot be invited (B4 Ch2 L70-73); `06_Places/Astral_Spaces/Spirit_Vault_and_Astral_Kingdom.md` describes entry by trust. The document should say which book each applies to (see TODO section H).

**Spirit Vault rules and the last register rows**
- `06_Places/Astral_Spaces/Spirit_Vault_and_Astral_Kingdom.md`: entry rules now follow the books. In Book 4 Ch2 the Inventory space can be entered only by Jason ("others cannot be invited"); the Spirit Vault (Book 4 Ch57) admits only those who implicitly trust him and can be sealed; Erika, Emi, Ken and Hiro could enter, and later Farrah, Asya and Ian (Book 5 Ch44); the storage gate admits "those you allow" (Book 6 Ch13).
- Read the remaining Primer, Timeline and Appendices register rows. Register now: 240 verified, 187 partial, 212 unlocated (this includes multi-book tags that were never auto-located), 0 automatic only.

**Unlocated register rows, hand-searched**
- Searched the unlocated rows by hand: 25 further claims were found and tied to chapter lines (for example the rabbit Nik at B11 Ch8 L102, Reality Hegemon at B6 Ch15 L45, "diplomacy is war" at B12 Ch23 L79, Hero's lack of subordinates at B1 Ch48 L92).
- Removed 18 spoiler-level label rows from the register (they are labels, not claims).
- Retagged 41 claims in `05_Organisations/`, `06_Places/`, `07_Characters/`, `02_Cosmology_and_Powers/`, `03_Magic_and_Adventuring/` and `01_World_Primer.md` from "(Book N)" to "(notes, Book N)" because the book lines were not found; 33 more are listed in `TODO_Verification.md` section H for manual handling.
- Register now: 259 verified, 242 partial, 120 unlocated (621 rows).

**Section H items (33 unretagged claims)**
- Found in the chapter files and verified or marked partial: Gary "almost silver" (B3 Ch21 L60), Geller tower (B11 Ch68 L1935), Clive "venerate" (B1 Ch85 L51), Belinda joins Clive (B2 Ch12 L6), Rufus bronze (B1 Ch15 L92), Roland as "the grandfather who means so much" (B12 Ch45 L97), Sophie's Mana Wellspring (B2 Ch61 L146), Lenora's "seventeen years ago" (B12 Ch67 L65), and others.
- Corrected: `07_Characters/Jason_Asano.md` now cites Book 1 (iron) and Book 3 Ch29 (bronze regional gate) for Path of Shadows; the range of "roughly two hundred kilometres" is confirmed at Book 4, Ch1 L67 (an earlier version of this entry wrongly said the figure was not in the books; the line had been cut off in a search display). `03_Magic_and_Adventuring/Magic_and_Adventuring.md` cites notes for silver (continental) and gold (global). Jason becomes an astral king in Book 8 (Ch65), not Book 9.
- Retagged to notes: astral-space hazards (Books 1-3), the Cardinas wave, Jason's university stint, Rufus's gold rank, Zara's rank.
- Register: 277 verified, 248 partial, 95 unlocated (620 rows).

**Third Places pass (chapter files)**
- `06_Places/Astral_Spaces/City_of_Fallen_Echoes.md`: trial sequence rewritten from Book 2 Ch44, 57, 58 and 60 (choice, capability, wisdom/courage, intellect, resolve, hidden insight trial).
- `06_Places/Vitesse.md`: the Geller tower stands in Vitesse. `06_Places/Rimaros.md`: Pelli is the mayor of Palisaros. `06_Places/Yaresh.md` and `Cyrion.md`: the Duke of Yaresh and the Queen of Estercost are not named in the chapters read. `06_Places/00_Places_Overview.md` and `Greenstone.md`: Boko's destruction and New Water sourced (Book 12 Ch32-33, 39); Sadi Andali and Jayapura sourced. `06_Places/Earth/Artefact_Site_One.md`: open question on the Ascension's Gate island recorded.
- `TODO_Verification.md` section A rewritten with what remains.

**Partial register rows upgraded (Places, Cosmology, Organisations, Magic)**
- Read the unread part of about 90 partial rows and upgraded them to verified; the register now stands at 351 verified, 176 partial and 93 unlocated.
- Corrections to documents: `02_Cosmology_and_Powers/Gods_and_Churches.md` (Hana Shavar runs operations from Jason's cloud palace in Book 10, not relief in Book 9; the sanction-of-Purity theory is Carlos's, not Dawn's), `05_Organisations/Adventure_Society.md` (Lucian, not Pochard, asks for the three-star farm contract), `05_Organisations/Earth_Powers.md` (the Network had four blocs at Nitra, including the Global Defence Network).

**Partial register rows upgraded (Characters)**
- Read the unread parts of about 65 Characters rows and upgraded them to verified. Register now: 428 verified, 99 partial, 93 unlocated.
- Corrections to documents: `07_Characters/Clive_Standish.md` ("Sorry. Where were we?" is Book 11; the archbishop's "heretic" exchange is Book 2 Ch21), `07_Characters/Danielle_Geller.md` (Lamprey fight is a speed duel at B3 Ch24, not "time powers"; forward-only time travel and "Time Witch of Vitesse" now cite Book 6 and Book 12), `07_Characters/Emi_and_Nik.md` (the nine floating cubes are Book 11, not Book 13), `07_Characters/Jason_Asano.md` (Mario Kart line and Palpatine joke now cite chapters).
- Still partial: claims whose second half is from the notes only (for example Anna's helicopter and Steering Committee roles, Sophie's six years with one essence, Emi's "Princess of the Asano clan").

**Unlocated rows searched a second time**
- Searched all 93 unlocated rows again by hand with fresh queries; found book lines for about 25 (for example Cartise, Isart and Arcazitlan, Archchancellor Standish, the Palpatine joke, Dawn's projected face, Nik calling Jason "Dad", Melody leading the Order, the Alchemy Association and the miracle potion recipe).
- Corrections to documents: `06_Places/00_Places_Overview.md` (Isart is a Book 9 city Emir sends Jason to, not the site of Emir's Book 2 contest; Cartise and Arcazitlan sourced), `02_Cosmology_and_Powers/Great_Astral_Beings.md` (removed the unsourced "likes 'that boy'" clause for the Celestial Book), `05_Organisations/Magic_Society_and_Associations.md` (Clive's title is first seen in Book 12 Ch1), `07_Characters/Dawn.md` (cottage in a bubble at B7 Ch8; projected face at B9 Ch6).
- The unlocated rows that remain are claims whose only support is the chapter notes (tagged "notes, Book N" in the documents); they stay in the register as unlocated until a book line is found. Register now: 442 verified, 110 partial, 68 unlocated.

**Review of partial and notes-only rows**
- Checked the unlocated rows against the chapter notes and the wiki clause by clause. Claims confirmed there are now graded **notes-confirmed** in the register (the document tag stays "notes" or "wiki"); a few more were found in the book text. Register now: 460 verified, 114 partial, 24 notes-confirmed, 16 unlocated.
- Claims found in none of the three tiers were removed from the documents: Rufus's "measured and courteous" voice and his gold rank (Book 11 calls him the strongest combatant below gold; no gold rank found), Zara's iron rank when she meets Jason, the Jason "irreverent speeches" line, and the Familiars line about recalling shadow bodies.
- Other corrections: Emi's cubes and tunnels, Colin's "tuck right in" line (Book 11, Ch33 L50), Gary's Vitesse origin (Book 1, Ch30 L47).

**Supporting cast (07_Characters, one file per character)**
- Added 55 individual character files: the Asano family (Ken, Cheryl, Erika, Kaito, Amy, Hiro, Taika, Yumi, Akari), the Remore and Geller families (Gabriel, Arabelle, Roland, Gwydion Remore; Keith, Henrietta, Rick, Phoebe Geller), Emir and his circle (Emir Bahadir, Constance, Jory Tillman, Gabrielle Pellin), Greenstone officials and crime lords (Vincent Trenslow, Elspeth Arella, Lucian Lamprey, Pochard Finn, Clarissa Ventress, Cole Silva, Adris Dorgan), the Mercers (Thalia, Cassandra, Thadwick), Builder-cult and Purity figures (Zato, Shako, Timos, Cressida and Landemere Vane, Melody Jain), Earth figures (Mr North, Gerling, Elizabeth, Simon McKean, Lenora Coleman, Itsuki Tiwari, Nigel Thornton, Craig Vermillion), and Pallimustus figures (Liara Rimaros, Soramir, Allayeth, Charist, Carlos Quilido, Hana Shavar, Musin Heath, Marek Nior Vargas, Tera Jun Casta, Jamis Fran Muskar). A first grouped Asano family file was replaced by individual files at the user's request.
- Each fact cites "Book N, ChX LY"; the citations were parsed into new register rows (R0640 onward), graded probable when the cited lines share terms with the claim, and 6 low-overlap citations were checked by hand. Facts only in the chapter notes are tagged "notes".
- Corrected an earlier log entry: Path of Shadows' "roughly two hundred kilometres" range is confirmed at Book 4, Ch1 L67 (the Jason file now cites it).

**Line-by-line check of the new supporting-cast files**
- Printed every citation in the 55 new character files beside its cited chapter lines and read them. All were supported; seven wording errors were fixed: Elizabeth (the vampire-leader remark is a Cabal member's, not Rufus's; the Book 6 rituals are defensive rituals against vorger, not against Jason), Elspeth Arella (Book 12 shows her in her office, not explicitly still director), Hiro (Jason plans the gold sale; he lifts the bar later), Kaito (Jason and Akari ride in his helicopter; the text does not say he flies it), Taika ("nearly silver" is notes-only).
- All parsed rows for these files are now graded verified (the six earlier low-overlap citations were also read).

**04_Peoples_and_Cultures (started) and the structure plan**
- `00_Project_Structure.md` section 3: the `04_Peoples_and_Cultures/` entry now lists one file per people plus daily life, food and clothing, religion in practice, law and indenture, and an **economy document**; section 11 updated.
- Added 14 files: `00_Peoples_Overview.md`, `Humans.md`, `Elves.md`, `Leonids.md`, `Celestines.md`, `Draconians.md`, `Smoulder_and_Brighthearts.md`, `Runics.md`, `Valash.md`, `Outworlders.md`, `Daily_Life.md`, `Religion_in_Practice.md`, `Law_and_Indenture.md` and `Economy_and_Money.md`. Each fact cites "Book N, ChX LY"; the citations were parsed into the register and every cited line was read beside its claim (a few line numbers were corrected).
- Also corrected `05_Organisations/Adventure_Society.md`: both Lucian (asks for a three-star contract, Book 1, Ch42 L67) and Pochard ("the Adventure Society will make it three-star", L68) speak, so the earlier attribution to Pochard was partly right.
- Not yet written for 04: clothing and food by region.

### 04 regional cultures and missing peoples
- Added to `04_Peoples_and_Cultures/`: `Estercost_Culture.md`, `Storm_Kingdom_Culture.md`, `Yaresh_Culture.md`, `Pranay_Culture.md`, `Kurdansk_Culture.md`, `Ustei.md`, `Merfolk.md`, `Goblins_and_Fairies.md`. Every fact cites "(Book N, ChX LY)" and each cited line was read against the claim.
- Merfolk rest on a single line (Book 3, Ch69 L509); the file records the gap rather than filling it. Goblins and fairies appear only as Earth-side transformed people, Cabal beings and a small fairy manifestation, so no native culture is claimed.
- A Book 12 Ch58 "merman" remark is an Earth joke about a person, so it was not used for merfolk.
- Register after these files: 851 verified, 114 partial, 38 notes-confirmed, 16 unlocated.

### Timeline consistency pass and annotation conversion
- Rewrote `08_History_and_Timeline/Master_Timeline.md`: every old "[book]" marker is now a "(Book N, ChX LY)" citation checked against the cited lines; items from notes or the wiki are marked as such.
- Corrected the Book 5 order. Book 5 opens about nine months after the June 2019 return (Book 5, Ch3 L170), so about March 2020 (M28), after a roughly six-month walkabout (Book 5, Ch8 L5). Asano Village was built over the preceding six months (Book 5, Ch5 L59) and the grid blackouts were still localised with a wider failure expected in about two months (Book 5, Ch3 L19); the earlier "M26-M27 grid shutdown, then village" ordering is removed.
- New data points: bronze timing (Book 5, Ch3 L170, L212), zone and Gary durations (Book 11, Ch48 L22; Ch60 L3; Ch68 L703), "around twenty years" for Book 12 (Book 12, Ch7 L78; Ch13 L36), the 1948 Fortress discovery (Book 4, Ch51 L30), the vampire war statements (Book 13, Ch988 L26; Ch995 L14; Ch998 L105; Ch1002 L69; Ch1023 L12). Twenty-one rows were added to `Source_Map.md` section 6.
- Annotation conversion: in other documents 57 single-citation lines with a register-verified location had their old "(Book N)" or "(notes, Book N)" tag replaced by "(Book N, ChX LY)". About 350 old-format tags remain; most sit in lines with several claims, where one register row covers the whole sentence, so they need a clause-by-clause pass rather than an automatic one (see `TODO_Verification.md`).
- Fixed the register generator: new-document rows (04, 07 and the timeline) were counted in the header totals but not written to `Source_Register.md`; they now appear. Register totals: 924 verified, 114 partial, 38 notes-confirmed, 16 unlocated.

### Old-format tag conversion, 01 to 03
- Converted every remaining "(Book N)", "(Book N, confirmed)" and similar tag in `01_World_Primer.md`, `02_Cosmology_and_Powers/` (all five files) and `03_Magic_and_Adventuring/Magic_and_Adventuring.md` to "(Book N, ChX LY)", locating each clause's own line instead of reusing the sentence-level register row. "(notes, ...)" and "(wiki)" tags were left, since they are the current format for those tiers.
- Corrections found while locating lines: "sentient miniature universes" and "gods are like regional managers" are Dawn's words to Jason (Book 8, Ch67 L53), not Jason's lecture; the "different path from anyone he cares about" exchange is with Arabelle, not Dawn (Book 9, Ch41 L81); the Cosmic Throne's sundering is told by Raythe and Velius in Book 11 (Ch64 L24-27) and by Jason in Book 13 (Ch1017 L6-8), not by Clive or Knowledge; "great astral beings cannot interact with physical reality directly" is Clive in Book 2 (Ch21 L112), not Book 3; the "Mario Kart shortcuts" line is Book 1, Ch77 L10; Vesta Carmis Zell "felt one of her seals disappear" (Book 9, Ch102 L66-67), not "feels her silver seal vanish"; Hess's "instinct to kneel" is Book 10, Ch16 L48. The reality-core claim now cites Book 6, Ch1 L20, and the vague "Earth's magic did not support monsters until the Grid failed" is replaced by what Book 5, Ch8 L44-47 says about the grid intercepting incursions.
- Weakened: the Fundamental Realm Authority Token "returned in the deal" is now stated as entering Jason's inventory (Book 8, Ch49 L89-91) with the deal link marked unchecked.
- Still not located: Vincent's rule that no stones drop for monsters above the killer's rank (Magic and Adventuring); it is marked in the text.
- Old-format tags remain in 05, 06, 07 and the Glossary (about 280 by the scanner count, some of them labels rather than claims).

### Old-format tag conversion, 05 and 06
- Converted the remaining "(Book N)" and "(Book N, confirmed)" tags in all six `05_Organisations/` files and in `06_Places/` (overview, Greenstone, Cyrion, Rimaros, Vitesse, Yaresh, the five Earth files and the Astral Spaces files) to "(Book N, ChX LY)". "(notes, ...)" and "(wiki)" tags stay; section-heading labels such as "(Book 5)" are labels, not claims.
- Corrections and weakenings while locating lines: Earth Powers no longer says the Taskforce is "led by" Lenora Coleman (she is the designated liaison, Book 13, Ch989 L48); Vermillion's "seventy years" as a vampire is marked not located; the Greenstone claim that the Old City's mayor answers to the Duke is marked unchecked (Book 12, Ch29 L38 gives only the mayor); the Fundamental Realm token and Vincent's "stones for kills" rule stay marked as unlocated; the Spirit Vault entry now cites the line for each stage (Book 4, Ch2 L70; Ch30 L45; Ch57 L59; Book 6, Ch13 L79; Book 8, Ch49 L105); Rimaros "adoptive cousin" is left to the notes.
- Old-format tags remaining: 07_Characters and the Glossary.

### Old-format tag conversion, 07 core characters and Glossary
- Converted the old tags in the seventeen core character files (Jason, Rufus, Farrah, Sophie, Humphrey, Neil, Clive, Danielle, Dawn, Gary, Belinda, Boris, Anna, Emi and Nik, Knowledge, Zara, Familiars) and in the Glossary to "(Book N, ChX LY)". The 55 individual files written later already used the new format.
- Corrections: Jason's abilities Castigate, Verdict, Punition, Feast of Absolution and Midnight Eyes are first awakened in Book 1 (Ch8 L35, Ch87 L85, Ch99 L24, Ch78 L54, Ch22 L84), not in the later books the old tags named; his father's landscape-architect line is Book 2, Ch11 L41; Gary's growl is Book 1, Ch9 L121; the Reaper's offer to bring Farrah back and the Reaper-World-Phoenix negotiation stay as notes claims (the cited lines do not state them); Belinda's Old City childhood with Sophie is marked notes (the cited line only shows her working with Clive).
- Remaining old-format items are notes or wiki tags, section labels, and a few unlocated claims listed in `TODO_Verification.md`. The Source Register rows were not regenerated for the new line citations.

### Source Register regeneration and partial-row recheck
- The register generator now reads every "(Book N, ChX LY)" citation in the documents (04, 05, 06, 07, 08 and the earlier folders), so each converted citation has a row; a fix also makes new-document rows appear in `Source_Register.md` (they had been counted in the header but not listed). Line-level rows carry the note "line-level citation pass". IDs from R0640 are regenerated on every run and are not stable; cite chapter and line, not the ID, outside the register.
- Rechecked the 114 older partial rows by reading each cited passage: 82 became verified (often with a better line), 24 were re-marked notes-confirmed because the cited lines do not state the claim (Landemere's Clockwork King goal, Vermillion's seventy years, Elizabeth's ancient vampires, Umber as Shade's brother, Danielle's advice quotes, and similar), and 8 duplicates or replaced claims were dropped. Ten new line-level rows with low clause overlap were read and marked verified.
- Document wording changed to match the text: Adventure Society field assessment and Greenstone corruption, Earth Powers methods and Finnegan, Guilds and Houses (Academy graduates), Danielle (sits with Gwydion at a table, not at the shaft bottom), Dawn (the Reaper "was the one who offered"), Emi (Matrix Beam is notes only), Gary (plate armour; hammer, shield and runes are notes), Zara (Vesper is her aunt; the brother is an adopted cousin).
- Register totals: 1,096 verified, 62 notes-confirmed, 16 unlocated, 0 partial.

### Notes-only and unlocated claims searched against the book text
- Searched the chapter files for the 16 unlocated rows and the 62 notes-confirmed rows. Found lines for 36 of them and upgraded the claims to "(Book N, ChX LY)": for example Amy as "de facto mayor" (Book 5, Ch44 L3), Cheryl as a realtor (Book 4, Ch24 L42), Gerling as Elizabeth's blood slave (Book 11, Ch68 L2267), Emir's essences (Book 2, Ch5 L88), Danielle investigating Jason at Gabriel's request (Book 1, Ch48 L101-102), Keith and Rick and Hannah at the Book 12 reunion (Book 12, Ch15 L6-7), Arash on Dominion (Book 1, Ch45 L14-18), Belinda and Estella as wife and wife (Book 13, Ch1011 L23), Clive and Lorelei (Book 13, Ch997 L32), Zara's storms and gold rank (Book 12, Ch0 L14; Ch12 L3), Knowledge's half-millennium plan (Book 13, Ch1017 L14).
- Removed or reworded because the book text does not support them: Rufus "confronts Farrah's killer"; Zara "claims publicly that Jason proposed" (the text only says she was matched with a House Irios member); the Cardinas wave in Incursion Sites; "general rule that astral spaces can kill"; "further personnel are named in the notes".
- Still notes-only (51 rows, kept with "(notes, ...)" tags): Vermillion's seventy years, Elizabeth's ancient vampires, Danielle's age of fifty and her advice quotes, Musin Heath as an elf and core-user, Jory as Belinda's ex and dean, Boris as a Cabal founder in Congo, Zara's affinities, and similar.
- Register totals: 1,125 verified, 51 notes-confirmed, 0 unlocated, 0 partial.

### Individual supporting characters, batch 2
- Added individual files in `07_Characters/`: Hester Maharala, Korinne Pescos, Jonah Geller, Gilbert Bertinelli, Ian Evans, Asya Karadeniz, Greg, Travis Noble, Estella Warnock, Natalie Park, Holly Macrossan, Velius, Raythe, Vesta Carmis Zell, Jes Fin Kaal, Fal Vin Garath, Benella, Kasper Irios, Jota Withers, Argy (Emmett Dillivan) and Pelli. Every fact cites "(Book N, ChX LY)"; the overview table and Name_Index were updated, and Name_Index no longer calls Asya Jason's lover.
- Register after these files: 1,272 verified, 51 notes-confirmed.
- Noted for checking: Name_Index calls Gabrielle Pellin "Travis's wife" and Ian Evans a doctor; no book line found for either (`TODO_Verification.md`).

### 09_Items_and_Artefacts started
- Added `09_Items_and_Artefacts/`: `00_Items_Overview.md`, `Soul_Bound_Items_and_Regalia.md`, `Tokens_Stones_and_Relics.md` and `Consumables_and_Trial_Rewards.md`. Every fact cites "(Book N, ChX LY)"; the Glossary gained entries for the Regalia, the Triune, astral blessing tokens, the Fundamental Realm Authority Token and the Lesser Miracle Potion.
- Corrections: the wiki name "Hegemon's Will" for the reforged Dread Salvation is not in the text searched and is marked wiki; the Fundamental Realm Authority Token was looted from the destroyed artefacts (Book 8, Ch50 L94-95), and Dawn says he must give it back (Book 8, Ch51 L68-70), so the earlier "crafted by the World-Phoenix in Book 6" claim in `Great_Astral_Beings.md` is replaced (the Book 6 item is a different one for establishing the link).
- Register: 1,324 verified, 51 notes-confirmed.

### 09 additions: awakening stones, cloud palaces, the Builder's door
- Added `Awakening_Stones.md`, `Cloud_Constructs_and_Palaces.md` and `The_Builders_Door_and_Fundament_Gate.md` to `09_Items_and_Artefacts/`, each fact cited to a chapter line. The door is described by Mr North as an astral construct that appears as a portal (Book 5, Ch41 L24-26) and the Fundament Gate is the ring of stones Jason absorbs (Book 5, Ch41 L52-62).

### 10_Roleplay_Support started
- Added `10_Roleplay_Support/00_Roleplay_Overview.md`, `Era_Selection.md` (seven eras with calendar anchors, scale, live dangers and turning points) and `Spoiler_Management.md` (the four levels, thirteen main secrets with the line where each first surfaces, and belief-versus-fact examples). Every claim cites a chapter line. The Primer's era section now links to them.
- Still to write for 10: plot hooks, NPC rosters by era, tone and voice notes.

### 10_Roleplay_Support: plot hooks and rosters
- Added `Plot_Hooks.md` (open situations for seven eras, each tied to a chapter line, with a question and no invented resolution) and `NPC_Rosters_by_Era.md` (who can appear in each era with one presence line each). Corrected Nik's Book 13 overwatch cite to Ch996 L5-9.
- Register: 1,581 verified, 51 notes-confirmed. Still to write for 10: tone and voice notes.

### Tone and voice notes
- Added `10_Roleplay_Support/Tone_and_Voice.md` (the series' register, forms of address, and a cued voice note for twenty speakers) and a condensed "Voice" line in the roleplay notes of sixteen character files (Jason, Rufus, Farrah, Gary, Humphrey, Sophie, Clive, Neil, Belinda, Danielle, Dawn, Zara, Boris, Knowledge, Emir, Familiars). Every cue cites a chapter line.
- Register: 1,637 verified, 51 notes-confirmed. 10_Roleplay_Support now has all planned documents.

### TODO rewrite, character backlog and Open Questions
- Rewrote `TODO_Verification.md`: removed finished work (tag conversion, register partials and unlocated rows, the 09 and 10 documents, the characters already written) and regrouped what remains into notes-only claims, documents still to write, facts the books may settle, and the Master Timeline.
- Recorded the supporting-character backlog in `TODO_Verification.md` section B (about eighty Name_Index figures without a file, grouped by priority).
- Added `Appendices/Open_Questions.md`: 21 questions the books leave open, each with what is known (chapter line) and what is not.

### 2026-10-21

**Characters (consistency pass)**
- Added `07_Characters/Emi_Evans_Asano.md` and `07_Characters/Nik_Asano.md`, splitting the combined `Emi_and_Nik.md` (deleted) at the user's request. Both were rebuilt from the book text. Corrections to the old combined file: Emi was not the first person Jason told (he told Erika and Ian first, Book 4, Ch28 L126, L154); her Book 5 birthday party was the day Jason evacuated the family (Book 5, Ch9 L23); she chose not to be an adventurer (Book 5, Ch53 L80); her confluence is Resonant (Book 11, Ch68 L1568); Nik was created by the transformation zone with the Healer's gift (Book 11, Ch61 L16) and named from "Lehenik" (Book 11, Ch23 L42); he was "five, maybe" when Jason left (Book 12, Ch15 L47) and reaches gold (Book 13, Ch998 L4). The "straw hat" and "gold-rank stealth" claims were dropped as unverified.
- Revised `Erika_Asano.md`, `Ian_Evans.md`, `00_Characters_Overview.md`, `00_Project_Structure.md` and the Name Index for the split.

**Timeline**
- Added `08_History_and_Timeline/Book_01_Timeline.md` to `Book_13_Timeline.md`: one line-cited file per book, each checked with a citation-overlap pass. Books 12 and 13 cite the chapter numbering of the source files (Book 12 runs Ch0 to Ch67, Book 13 Ch950 to Ch1024). Book 12's closing pirate battle and the Emi reunion are not placed because their lines were not verified in this pass.
- Rewrote `08_History_and_Timeline/Master_Timeline.md` as an overview (series table, month-count corrections, the Pallimustus calendar, links to character and place files, updated conflicts).
- Corrections made on the way, each from the book text: Jason's death is about M15 to M16 (Book 3, Ch62 L96), not M18 (M18 is the return to Earth, Book 4, Ch3 L112); Book 2 starts about M4 (Book 2, Ch9 L67); Kaito's death is about M30 to M31, not M36; the Battle of Yaresh is no later than about early 2023 because Jason is 29 in Book 10 (Book 10, Ch33 L76); Cardinas zone length is "months", not a fixed nine.
- Found an open tension and recorded it instead of resolving it: Emi is fifteen when Rufus arrives (Book 11, Ch68 L782) but the sword line says "six years" (Book 11, Ch68 L115).

**Register**
- Re-ran the register pipeline. A bug in `allrows.py` (a loop variable shadowed the chapter-file map) had silently skipped citations to chapters not already loaded; fixed. 3,437 rows verified, 51 notes-confirmed, none partial.

**Magic and Adventuring (expanded to the document specification)**
- Replaced the single combined `03_Magic_and_Adventuring/Magic_and_Adventuring.md` with 21 topic files in the standard topic format (Summary, How it works, Variations and exceptions, Examples from the books, Common misconceptions, Changes over time): `00_Magic_Overview.md`, `Essences.md`, `Essence_Catalogue.md`, `Confluences.md`, `Awakening_Stones.md`, `Abilities_and_Attributes.md`, `Afflictions_Boons_and_Damage.md`, `Jason_Power_Set_Reference.md`, `Ranks_and_Advancement.md`, `Monster_Cores_and_Training.md`, `Auras.md`, `Familiars_Summons_and_Conjurations.md`, `Rituals_Arrays_and_Formations.md`, `Skill_Books_and_Learning.md`, `Alchemy_Artifice_and_Magical_Materials.md`, `Monsters.md`, `Adventuring_Profession.md`, `Souls_Death_and_Healing.md`, `Astral_Spaces_Zones_and_Surges.md`, `Unusual_and_Unique_Magic.md` and `Earth_Magic.md`. Every statement was re-read against the chapter files; each file was checked with the citation-overlap pass.
- Corrections from the book text relative to the old combined file: no wiki "essence revelations" or "combat trance" claim (not found in the text); the "ability to use skill books" belongs to Jason's Mysterious Stranger gift (Book 1, Ch7 L55-60); stones are graded one to five stars by the Magic Society with five rarity stages, not "common to legendary" by the Adventure Society (Book 2, Ch9 L9); renewal is "second-highest rarity" (Book 6, Ch13 L68), which the wiki's rarity scale calls Epic (an earlier version of this entry wrongly called that a conflict); the Garuda confluence has two routes, bird and wing (Book 4, Ch65 L22, L28); the stones-for-kills rule is Book 1, Ch91 L34; Earth's ranks are named after spirit coin colours (Book 4, Ch21 L33); a "Giant Slayer" title was not found and was dropped.
- Repointed the Related lines of 22 documents in `02`, `04`, `05`, `06`, `07` and `09` to the new files, resolved the stones-for-kills open item in `05_Organisations/Adventure_Society.md` and `TODO_Verification.md`, and updated `00_Project_Structure.md` (the 03 entry, the revised Book 11 duration note in section 9, and the new section 11 priorities).
- Register: removed the old combined file's rows and re-ran the pipeline (4,257 rows verified, 50 notes-confirmed, none partial). Fixed a path in the helper scripts after `Source_Text` moved to `src/Source_Text`.

**Source Register and Source Map (full rebuild, 2026-10-22)**
- Found and removed: dozens of duplicate log rows in the Source Map (the pipeline appended a row on every run), about 2,500 register claims cut off mid-parenthesis, 246 rows whose tag and book disagreed (for example a Book 11 Rufus claim filed under Book 1), rows of the deleted `Emi_and_Nik.md`, and "verified" grades that had been assigned by word overlap rather than by reading.
- Rebuilt both files from the documents with `src/TEMP_scratchpad_recovery/build_register.py`: one row per sentence or table row (3,082 rows in 192 documents), graded ok / near / weak / reviewed; the Source Map is now in story order (timeline thread, chapter index by book and chapter, state changes by book) with the source-checking log deduplicated.
- Fixed citations found on the way: Danielle_Geller.md (Ch47 L89), Farrah_Hurin.md (Ch19 L30), and bare chapter citations in Jason_Power_Set_Reference.md and Master_Timeline.md.
- Still to do: read the 34 rows graded weak (the review queue) and spot-check the state-change list in Source_Map section 6.

**Places (third verification pass, 2026-10-22)**
- Re-read all 19 documents in `06_Places/` against the chapter files and added line citations to previously uncited claims. Corrections from the book text: Hana Shavar is the High Priestess of the Church of the Healer for Yaresh (Book 9, Ch74 L43), not unconnected to it; Yaresh is not described as elf-run; Cyrion's "continental council" conflicts with Book 6, which puts it in Vitesse (both passages now cited); Vitesse's labour protections and Greenstone's "banished director" and "Clive's boss" claims were not found and were removed or marked unchecked; Earth's "magic desolation" phrase is not in the text; the Makassar death toll of 150,000 is Book 5, Ch30 L71, not "in eight days"; the artefact site's first director is Truffett who named it, and it has about nine thousand workers before the Book 12 evacuation (Book 12, Ch64 L21); the Cardinas zone length is "months", not nine; the Duke of Boko is not barred from New Water in the passage read (Book 12, Ch39 L61-65).
- Details still resting on earlier notes are marked "not rechecked" in the documents and listed in section 11 of the structure doc. Register rebuilt (3,181 rows).

**Cosmology and Organisations (verification pass, 2026-10-22)**
- Re-read `02_Cosmology_and_Powers/` and `05_Organisations/` against the chapter files and replaced wiki-tier and notes-tier claims with book lines where the text supports them: gods give essences and stones that return to them (Book 1, Ch21 L57; Book 3, Ch61 L11; Book 4, Ch11 L16); the Healer's church took over star seeds (Book 3, Ch21 L73); the astral-king prerequisites (Book 8, Ch65 L88; Book 10, Ch1 L52); the Builder's method (Book 2, Ch21 L106-112); the Order of the Reaper as assassins and a volunteer network (Book 2, Ch44 L72-78; Book 2, Ch60 L120-123); the Adventure Society application, badge and notices (Book 1, Ch38 L118-149; Book 1, Ch62 L44-54; Book 1, Ch57 L33).
- Open questions settled: Adrien Barbou is the second Mr East (Book 5, Ch8 L28; Ch30 L43; Ch32 L5); Death did return the resurrection power (Book 12, Ch8 L10); a Cup of Heroes drinker's confluence becomes a Demigod essence, not a Hero essence (Book 10, Ch86 L70).
- Not found in the text and left marked as wiki or earlier notes: the wiki's list of about forty gods (replaced by a text-scanned list), Hero's wiki essence, the Order's "iron-only" trials, messengers enslaving essence users, Grantham's sympathy for Clive.

**Wiki and notes tiers (2026-10-22)**
- Narrowed notes-tier and wiki-tier claims to book lines where the text supports them (Anna Tilden, Boris Ket Lundi, Craig Vermillion, Danielle Geller, Rufus Remore, Zara Rimaros, Knowledge, Taika, Neil Davone, Familiars, Jason Asano, Belinda Callahan, Glossary): for example Shade's body counts at iron and bronze are in Jason's Book 12 sheet (Book 12, Ch67 L229-232), Rufus's water-walking boots and two-second "speed of light" power are Book 1, Ch16 L38 and Ch108 L99, and Boris says "I'm from Earth, Asano" (Book 11, Ch31 L87). Claims still resting on notes (for example Musin Heath's species, Neil's tea lands, Hegemon's Will) stay marked.
- Added `03_Magic_and_Adventuring/Wiki_Reference_Lists.md`: the wiki's lists of essences (147, with rarity, abilities and users), confluences (96, with known combinations), awakening stones (32) and monsters by rank, each tier-marked and cross-referenced to the first book line where the text names it; and the wiki's list of 43 gods in `02_Cosmology_and_Powers/Gods_and_Churches.md`. The lists are generated by `src/TEMP_scratchpad_recovery/compose_wiki.py` (which runs `wiki_lists.py`) from the cached wiki pages. The register now has about sixteen notes rows and the deliberate wiki-list rows; the policy is that wiki facts fill list-shaped gaps once the book content is transferred, always tier-marked.

**Notes-tier second narrowing pass (2026-10-22)**
- Moved to book lines: Network founder and Noreth/Mr North (Book 13, Ch1017 L19-24, L39), Elizabeth in Venice (Book 11, Ch68 L2256-2266), spirit-vault gardens (Book 4, Ch57 L3-10; Book 8, Ch2 L57-63), the Sky Link island as Ascension's Gate (Book 12, Ch39 L47, Ch56 L3-4; Book 13, Ch1020 L95, Ch1023 L103; Open_Questions #12 updated), Kaito's resemblance (Book 13, Ch950 L33), the Davone tea lands (Book 2, Ch23 L17) and Zara as a former princess (Book 9, Ch40 L21).
- Still marked notes with a "not located" statement: Zara's adoption and name, Rufus's height, Elizabeth's Book 6 note, the Book 4 mirror scene. Third batch: Hegemon's Will and the Gary/Virid reforge (Book 7, Ch2 L71-74; Ch54 L108-120; Virid Martine, Book 6, Ch47 L270), Knowledge's half-millennium plan (Book 13, Ch1015 L78), Anna (Book 6, Ch23-24; Book 12, Ch1, Ch3, Ch22), Rufus's assessment and meditation lessons, Neil's hesitation (Book 2, Ch27 L46, L112), Zara meeting Emi, Erika and Ken (Book 13, Ch956 L40-41), Musin as Yaresh director. Register rebuilt: 1 notes row and 15 wiki rows (the deliberate wiki lists plus a few wiki asides) remain; several claims stay tagged notes with an explicit "not located" statement.

**Notes "not located" follow-up (2026-10-22)**
- Located: Zara's adoption, Nareen name and withdrawal (Book 9, Ch40 L13, L18, L72); Zara's kiss (Book 13, Ch1004 L44-52, promenade walk Ch956 L3); Musin an elf (Book 10, Ch9 L37); Farrah's perception training (Book 1, Ch40 L31, L50-52; Ch41 L35); Anna at Nitra (Book 6, Ch1 L4, L27; Ch24 L4) and the recruitment talk (Book 12, Ch26 L76; Ch40 L20); Jason's mirror scene (Book 4, Ch25 L44-45); Elizabeth keeping peace (Book 6, Ch39 L71-74); Vesper aged sixty-seven, niece of Pelli (Book 7, Ch15 L110-113; corrects the notes' "descendant").
- Still not located: Rufus's height, Musin's rank and core use, Anna's System confirmation and GDN delegation role, Elizabeth leading vampires separate from the Cabal, Vesper's silver rank, Vitesse's magic density (wiki).

**World Primer verification pass (2026-10-22)**
- Checked the primer against the book text and added references for the calendar, map differences, Gramid Passage, surge cycle, Greenstone density, Earth's membrane, Network categories, ranks table, coin ratios, racial gifts, celestine origin, valash and lehenik, Interstice, dumpling soup, Red Table and the regional names.
- Corrected: "Jason repairs the Cosmic Throne" (the throne is left empty and cannot be restored, Book 11, Ch65 L8; Book 12, Ch1 L34); "Jason is sealed" (replaced by the walk to the standing stones, Book 13, Ch1024 L153); Greenstone's "magic trams" (Jason's guess; loop terminals); Team Biscuit's name (a familiar picked it, Book 10, Ch47 L78); Silver rank "killing blow no longer kills" (fights through lethal blows, Book 5, Ch1 L38); Network "category 0-5" ranks (categories follow coin colour); Red Table (a blood cult, not a criminal network); Interstice "diamond-ranker entry" (not found, removed); the "to be written" pointer to the timelines.
- Left to the topic documents: sections 8-12 descriptions of peoples, gods, organisations and places are summaries; their cites are in those files.

**04 Peoples and Cultures verification pass (2026-10-22)**
- Re-read about eighty cited lines across all 22 files in `04_Peoples_and_Cultures/` against the book text; every checked cite supports its claim except the four fixed here: Jason's three gold coins (the text does not say they fund Jory's facility; Book 1, Ch61 L63-65 and Book 3, Ch16 L81 now stated separately), the Healer stripping essences (Book 4, Ch11 L16 says gods in general; the Healer is notes-only), the Sadi Andali "price" (Ben asks Jason, Book 12, Ch52 L41) and Gary Sharpton as "young" (the text shows him designing a vehicle, Book 12, Ch62 L4-9).
- Register grades for 04 were already all ok or near; the only claim still tagged notes is the Healer line.
- Gaps unchanged: merfolk (one line), goblins and fairies (Earth-side only), no files yet for Girlano, Sadi Andali, Zartos, Dragon Lands or Vitesse culture.

**09 Items and Artefacts verification pass (2026-10-22)**
- Re-read about seventy cited lines across the seven files in `09_Items_and_Artefacts/`; item windows, ranks, rarities, effects and quotes match the text. Fixed: the Venice yacht cite (Book 6, Ch4 L53, not L52); the Asano Village cloud house (the text shows Farrah preparing a seafloor site with a tramway, not the house sitting there; Book 5, Ch5 L106-118); and Soul_Bound_Items_and_Regalia's closing line, which called Gary's reforging an open thread although Book 7 resolves it (Book 7, Ch2 L73-74; Ch54 L108-120).
- No notes-tier or wiki-tier claims remain in 09. Items not yet covered: Hegemon's Dominion as its own entry, Jason's dimensional storage and portals, Emir's other items, guild and Society badges.

**10 Roleplay Support verification pass (2026-10-22)**
- Re-read about 130 cited lines across the six files in `10_Roleplay_Support/` and name-checked the 70 roster citations. Almost all hold. Fixed: Carlos Quilido's cite (Book 10, Ch9 L10), Dawn's voice note (dry and composed, not "teasing"), the Purity sanction cite (Book 8, Ch48 L39-41), Nik's voice note (the bleeped rabbit, named in Book 11, Ch23 L42) and the vampire-war hook heading ("nearing its end" was an interpretation).
- Voice notes are judgments tied to one quoted line each; they are not exhaustive. No notes-tier or wiki-tier claims remain in 10.
- Future work noted in section 11: 04 culture files and 09 item gaps.

**Places follow-up (2026-10-22)**
- New files in `06_Places/Minor_Places/`: Zartos, Rakesh, Hornis, Boko, Sadi Andali, Arcazitlan, Isart, Cartise, Jayapura, each built from the chapter files with line cites.
- Settled the "from earlier notes" Places claims: the Nitra pagoda, arches and city dimensions (Book 6, Ch5 L53; Ch19 L21; Ch23 L48, L56), the astral kingdom's lagoon town and ten-storey pagoda (Book 8, Ch65 L29-31), zone sealing (Book 6, Ch1 L83; Ch3 L5, L39), Barbou's aperture seals (Book 4, Ch51 L60-68), Gerling's and Noreth's fates (Noreth dead by Book 7, Ch48 L36; Gerling keeps returning, Book 13, Ch1007-1008, and is Elizabeth's blood slave in Book 11, Ch68 L2267), and Keene at the artefact site (Book 12, Ch67 L47). Not found: that aura and perception are sealed inside a zone.
- Corrected the Overview's Zartos entry (not a desert city; the text says subterranean, celestine).
- Added Open_Questions 22: Rakesh and Vitesse both host a "continental council"; likely one per continent but never stated.

**Places follow-up, second batch (2026-10-22)**
- New files in `06_Places/Minor_Places/`: Dragon_Lands, Girlano, Oleyu, Leust, Kazlahk, Kurdansk (with Dreisil) and Palisaros, each from the chapter files with line cites. The Great Southern Continent is named only once (Book 9, Ch25 L4), so it has no file.
- Noted a small tension: Marta Fries's friend faked her death "two decades" before Book 6 (Book 6, Ch47 L510) while Book 9 dates Melody Jain's story "around a quarter of a century" ago (Book 9, Ch27 L24); both are loose figures.

**Characters follow-up (2026-10-22)**
- New individual files in `07_Characters/` (32): Callum Morse, Valdis Volaire, Sigrid Freyn, Dustin Kettering, Lorelei Grantham, Vincent and Chloe Baudrillard, Noriko Asano, Li Li Mei, Ketevan Arziani, Miles Cotezee, Marcus Hargrave Xenoria, Gormanston Bynes, Hess Jor Nasala, Marla, Adrien Barbou, Marie Finnegan, Umber, Helsveth, Erigo Fin Desca, Zithis Carrow Vayel, Garth Larosse, Amos Pensinata, the Adeah twins, Audrey Blaine, Hassan Dukhtar, Anisa Lasalle, Nicolas Hendren, Beth Cavendish, Killian Laurent, Padma Parsell, Trenchant Moore and Jeni Kavaloa.
- Four grouped files in `07_Characters/Minor_Cast/` for the lesser figures named in TODO_Verification (Books 1-3, 4-6, 7-9, 10-13).
- Noted name variants: Nicolas Hendren / "Hedron" (Book 3, Ch1 L106), Sigrid Freyn / Volaire, and two Beauforts (Thadwick's father and the Builder cult commander, Book 10, Ch72 L41). Sigrid calls the Mirror King "Father" in Book 3, Ch5 L51-53 although she later marries Valdis; not explained.
- Not yet written: Orin Pensinata's own file, Order of Redeeming Light individuals beyond the group entry, Mose Cavendish, Hudson Kettering, Niko, Emily, Lance, Dara, Zareen and Joseph as individuals. Name_Index and Glossary have not been updated for these new files.

**Characters known-gaps pass (2026-10-22)**
- New: Orin_Pensinata, Baseph_and_the_Rimaros_Children, Minor_Cast_Order_of_Redeeming_Light and Minor_Cast_Remore_Academy_and_Greenstone_Teams.
- Fates found: Amos Pensinata survives (Book 11, Ch55 L3; Ch68 L378); Orin is his nephew and a member of Team Storm Shredder; Adrien Barbou is implied dead by Farrah (Book 13, Ch968 L45-54); Killian Laurent is captured in Book 9 (Ch5) and Jason guesses he is held by the Magic Society (Book 10, Ch58 L106).
- Name_Index entries added or linked for all new files; Glossary adds Moon's Edge, Mr East, Red Table, Team Shining Scabbard, Team Storm Shredder and Team Biscuit; NPC rosters list the new figures by era. Name_Index corrected: Umber is Shade's brother (Book 13, Ch1024 L101).
- Still open: who leads Moon's Edge (Miriam's team in Book 11, Ch46 L11 versus Allayeth in Book 12, Ch16 L8) and why Sigrid calls the Mirror King "Father".

**Discrepancy pass and build plan (2026-10-22)**
- Resolved: who leads Moon's Edge (Miriam Vance leads; Allayeth raised and supervises it, Book 10, Ch51 L43; Ch59 L17); Sigrid's "Father" (Hastor, the king's portal specialist, Book 3, Ch5 L49-53); Gerling's part at Saint-Étienne (Mr North names Shako and Chen as the ones who placed the device, Book 6, Ch35 L78-80; Gerling entered through Barbou); the Emi-age tension (different moments, see Open_Questions 19a); Melody's "quarter century" against Marta's "two decades" (the story began 25 years ago, the faked death was 20 years ago).
- Narrowed: Cardinas zone length (about six to eleven months), the Book 12 present (2037), the Old City mayor (the Duke is the ruler; the mayor answering to him is an inference), the System withdrawal (Jason's act; the trigger is not stated).
- Corrected: Ramona of Moon's Edge is not linked to the Order of Redeeming Light's Ramona in the text; Allayeth, Yaresh_Culture and the Glossary no longer say she leads the team.
- New: `07_Characters/Miriam_Vance.md` (a major Book 10-11 commander who had no file), `TODO_Build_Plan.md` (tiered build plan), Open_Questions 23 and 24.

**Tools folder cleanup, build plan item 0.2 (2026-10-22)**
- Renamed the living scratchpad `src/TEMP_scratchpad_recovery` to `src/tools`; earlier Change_Log entries that mention the old name refer to this folder.
- Kept 12 working tools and their data in `src/tools`, moved 210 one-off scripts and intermediate files to `src/tools/archive/`, wrote `src/tools/README.md`, and moved the chapter summaries to `src/Chapter_Notes/`.
- Made the tools path-independent (no hard-coded absolute paths or reliance on the working directory); `cc2.py` and `loc2.py` now use the new `common.py` instead of the retired `newrows.py`.
- Verified: `build_register.py` reproduces 3,746 rows with identical grade counts, and `compose_wiki.py` changes no document.

**Structure document refresh, build plan item 0.3 (2026-10-22)**
- Rewrote sections 3, 8, 9, 10 and 11 of `00_Project_Structure.md`: the folder layout now matches the repository (including `src/tools`, `src/Chapter_Notes`, the two TODO files and the Minor_Places and Minor_Cast subfolders), "What exists now" became a state table, the build order records that every section has been built and verified, section 9 carries the narrowed Cardinas-length and Book 12 date entries, and section 10 adds version-control and tool practices. Section 11 now points to `TODO_Build_Plan.md`.
- Corrected the spelling-variant list (Hendren/Hedron, not Herston) and pointed section 2 to the new locations of the chapter notes and the archived lorebook.

**Document linter, build plan item 0.5 (2026-10-22)**
- Added `src/tools/lint.py` (header fields, spoiler values, cite existence and line ranges, Related links, cite form, shorthand, folder-overview coverage). It runs at the end of `build_register.py` and writes `src/tools/lint_report.md`; a seeded test document triggered every check.
- First run found 4 errors and 19 warnings; all fixed: 15 cites written without the comma ("Book 9 Ch29 L17") were standardised to "Book 9, Ch29 L17" in 10 files, the Master_Timeline Related line was corrected, the Peoples Overview now lists the four life-and-society files, and "mixed" is allowed as a spoiler value for the Glossary, Name_Index and Characters Overview. Result: 256 documents, 0 errors, 0 warnings.

**Register deltas, build plan item 0.6 (2026-10-22)**
- `build_register.py` now compares each run with the previous `register_new.json` (new module `src/tools/delta.py`) and prints one line: rows added, removed, edited and regraded, and newly weak or cleared weak rows. Details go to `src/tools/register_delta.md` (not committed). Tested by adding a deliberately unsupported sentence to a character file (flagged as a new weak row) and by rewording a sentence (reported as an edit), then reverting both.

**Build plan decisions recorded (2026-10-22)**
- The four open decisions in `TODO_Build_Plan.md` were settled by the project owner and written into the plan: full individual character files where the material justifies one (grouped files only for little-known figures), the chapter digest is committed, spoiler-level exports use tagged sections where convenient, and the Wiki Reference Lists move to `Appendices/` after the cross-reference matcher improves. New item 0.9 (spoiler tag syntax and linter support) was added; items 2E.2, 3.6, 5.3 and 5.5 carry the decisions.

**Generated overviews and variants table, build plan items 0.7 and 0.8 (2026-10-22)**
- 0.7: new `src/tools/overviews.py` generates the file index of every folder overview between `<!-- files:start -->` and `<!-- files:end -->` markers (link, spoiler level, first sentence of the Summary, and the entry names of group files). It covers 12 overviews, including two new ones (`08_History_and_Timeline/00_History_Overview.md` and `Appendices/00_Appendices_Overview.md`), recursive for `06_Places` and `07_Characters`. The hand-written file tables in the Characters and Places overviews were replaced by the generated block. `build_register.py` regenerates the lists, and `lint.py` reports an out-of-date list as an error (tested with a stray file). The linter now ignores HTML comments when it looks for shorthand.
- 0.8: the Glossary's variants section is now three tables: 16 spelling variants with where each occurs and a note, nine same-name-different-people cases, and three false variants (Culie, Asarno, Zardoz). Found by scanning the chapter text for near-duplicate names. Corrected on the way: Minor_Cast Books 1-3 no longer implies the Book 12 Darryl is the Book 1 Darryl.

**Spoiler tags, build plan item 0.9 (2026-10-22)**
- Defined the tag form (`<!-- level:N -->` ... `<!-- /level -->`) and its rules in section 6 of `00_Project_Structure.md`; added `src/tools/spoiler_tags.py` (parser, proposer, retrofitter) and linter checks for balance, invalid levels, nesting and the header-level rule (tested with a deliberately broken file).
- Retrofitted 21 sections in 15 files where the section level exceeded the header level: the primer (9.4, 9.5), the Cosmology overview, Gods_and_Churches (five god sections), Great_Astral_Beings, Awakening_Stones, Essences, Essence_Catalogue, Cults_and_Orders, Guilds_and_Houses, Magic_Society_and_Associations, Greenstone, Boko, the Astral overview, Spirit_Vault_and_Astral_Kingdom and Knowledge. Where a heading says "Level 2/3" or "2-3" the higher level is used.
- Not retrofitted: files whose header already covers all content, and files with mixed levels but no marked section (for example the 2026-10-22 character files, whose header carries the highest level they need). Those can be split into tagged sections later if a use appears; build plan item 5.5 depends on the tags.

**Book 12 closing chapters placed in the timeline, build plan item 1.1 (2026-10-22)**
- `Book_12_Timeline.md`, section 7: replaced the four-row stub with line-cited rows for Ch58 to Ch67 (the American officials' warning and Jason's plan for a staged demonstration, the artefact site and Lenora, the Jakaar crew and the Asano clan hosting them, the arrival, the pirate battle in three stages, the aftermath, Gary Sharpton, Emi and the three appendices). Removed the "not placed until verified" note.
- Dating: added the seventeen-year count (Book 12, Ch67 L42, L65) and Jota's "forty-four years ago" (Book 12, Ch67 L113) to the time anchors. The Earth arrival is now placed in 2038 and the Pallimustus tour in late 2037 to early 2038 (previously the whole book was given as 2037). Updated Open_Questions 18, `Master_Timeline.md` (series table, month-count table, conflicts list), `00_Project_Structure.md` and `TODO_Verification.md` to match. The gap between the tour and the arrival is still not stated.

**Second detail pass on the Book 12 and 13 timelines, build plan item 1.2 (2026-10-22)**
- `Book_12_Timeline.md`: added rows for the twelve chapters that had none (Ch4, Ch18, Ch19, Ch25, Ch31, Ch35, Ch41, Ch42, Ch44, Ch45, Ch52, Ch57), plus Ch3's second scene. The new rows cover the Saint-Etienne vampire kill seen by Nigel, the Valdis duel in the Yaresh arena, the Segurado aftermath, Li Mei and Jamis in Boko, Anna in the French domain, the Burning Violet intake, the Headingway delegation, and the pirate admiral's briefing of Jota that explains how the Earth ambush was set up.
- `Book_13_Timeline.md`: added rows for the twenty-three chapters that had none (Ch961, 962, 965, 966, 967, 970, 976, 978, 979, 981, 983, 984, 986, 989, 990, 993, 1002, 1005, 1007, 1010, 1011, 1014, 1016), covering the planning meetings, the Pakistan manifestation, the Swiss and Network operations, the Belgrade offensive and the McKean castle.
- Every chapter of Books 12 and 13 now has at least one cited row. Chapters with several scenes still carry one or two rows each, so a finer pass (one row per scene) is still possible; it was not forced here to avoid rows with weak line anchors.

**Weak register rows cleared, build plan item 1.3 (2026-10-22)**
- The register had 54 weak rows (the plan counted 52). All are now graded ok or near, so the weak count is zero.
- Method: for each row the cited lines were printed (`src/tools/weak_dump.py`) and the claim was either split so that each cite sits beside the clause it supports, rewritten to quote or paraphrase the cited line (voice cues in the character files, the Tone_and_Voice facts, timeline anchors), or given better cites (Primer section 7: Old City plumbing at Book 1, Ch71 L7, the Vitesse palace plants at Book 2, Ch40 L3 and the Rimaros sky islands at Book 7, Ch7 L3). Roleplay judgements remain as plain sentences without a cite, with a quoted cue line after them.
- `TODO_Build_Plan.md` is now excluded from the register like `TODO_Verification.md`; it is a working list, and its cites were being graded as claims (three of the weak rows).
- No claim was strengthened beyond its cite. Where a cite did not carry the whole sentence, the unsupported part was left as an uncited sentence or marked as an inference (for example that the Old City mayor answers to the Duke).

**Remaining notes and wiki lines settled, build plan item 1.4 (2026-10-22)**
- Located or narrowed against the chapters: Elizabeth leading vampires separate from the Cabal (`Earth_Powers.md`, Book 6, Ch47 L27 to L28), Rufus's height (`Rufus_Remore.md`, "tall and lean", Book 7, Ch9 L6), Vesper's silver rank (`Zara_Rimaros.md`, Book 7, Ch15 L74 and Ch21 L32), Anna's System scene (`Anna_Tilden.md`: she is shown a System Administrator window, not asked to confirm; Book 12, Ch42 L99 to L101) and her GDN role (go-between only; membership is not stated).
- Musin Heath's rank and core use are not stated anywhere in the chapters (`Musin_Heath.md`); the notes claim is dropped and the text-based description kept.
- `Neil_Davone.md`: the wiki lines are replaced by book lines (Thadwick's lackey; Cassandra is not Neil's ex-girlfriend, he admired her and she was Jason's girlfriend). The wiki "ex?" line was a mis-assignment.
- `Name_Index.md` and `Gabrielle_Pellin.md`: Gabrielle Pellin as Travis Noble's wife and Ian Evans as a doctor now carry book lines; the Gabrielle file gains the Book 12 and 13 marriage facts.

**Open questions retested against the text, build plan item 1.5 (2026-10-22)**
- Resolved: 4 (the silver cap is a function of the messenger brand, Book 11, Ch25 L51-53), 9 (the Firmamental Bridge Anchor is a single-use item that establishes the bridge, Book 8, Ch51 L66), 10 (Jason trades the authority token back to the Builder, Book 8, Ch54 L54, L99) and 11 (the fake Purity brought the founder into his church as payment, Book 13, Ch1017 L17-19).
- Narrowed: 1 (the northern astral space failed and the oases could no longer feed the tribes, Book 1, Ch97 L19-21), 2 (Marek leads a band that subordinates itself to Boris, not the movement), 3 (the Unorthodoxy has many astral kings, one named by Navise's king, Book 12, Ch26 L19), 5 (the debt is owed to the Council of Kings for the ritual magic and ends with the planet's move), 6 (a sanction changes an immortal; self-sanction means retire and be reborn), 8 (Legion, the Celestial Book and the Reaper's domains), 19 (the renewed war is "two years" old at Book 13, Ch995 L69, so the earlier timeline note that it was missing is withdrawn) and 20.
- Still open: 7 stays resolved; 13 (a figure for Vitesse's magic; more context added); 22 is rewritten as a recorded inconsistency, because Book 6 (Ch47 L604) puts the council in Vitesse and Book 7 (Ch43 L58) puts it in Cyrion; the compendium avoids naming a city. This feeds build plan item 1.6.
- `Book_13_Timeline.md` and `Master_Timeline.md` now cite the Ch995 line instead of the open note.

**Shorter-term inconsistencies ruled on, build plan item 1.6 (2026-10-22)**
- Added a "Text inconsistencies and rulings" table to the Glossary's variants section: the Garuda route (one change of plan, Book 4, Ch65 L22 and L28), the Inevitability stone's two ability names (use Inevitable Demise; the effect line says Inescapable Doom), Melody Jain's quarter century against two decades (different moments), the clan's hiding period (two years, half a decade and more than a decade are snapshots at different dates) and the continental council's seat (a true inconsistency: Vitesse, Rakesh or Cyrion; do not name a city).
- One-line rulings added in `Confluences.md`, `Awakening_Stones.md`, `Tokens_Stones_and_Relics.md`, `Melody_Jain.md` and `Master_Timeline.md`. Hendren/Hedron and the two Beauforts were already in the variants tables.
- `00_Project_Structure.md` section 9: Gary's death timing ("almost a year later", Book 11, Ch68 L703; Book 11 has no Ch74), the clan hiding period and the soul forge listing are marked resolved.

**Unwritten short entries, build plan item 1.7 (2026-10-22)**
- New in `09_Items_and_Artefacts/`: `Hegemons_Will_and_Dominion.md` (the scabbard Hegemon's Dominion as its own entry, with the sword's invocations and the Book 11 reforging as a level 3 section; it notes that the item screen lists corrosive damage for Ruin while the invocation message says necrotic), `Dimensional_Storage_and_Portals.md` (inventory, bags, storage limits, portal rules and networks), `Badges_and_Guild_Membership.md` (how badges are made, tracked and replaced; the Book 12 diamond badge; the Burning Violet guild) and `Desert_Transport_Skimmers_and_Barges.md` (Emir's skimmers and sand barges, the Ustei war barge).
- Glossary entries for Hegemon's Will / Dominion and Burning Violet now point to the new files. The folder overview was regenerated. Orin Pensinata already has a full file, and Hudson Kettering keeps his grouped entry because a search of Books 3 to 13 finds no further appearance.
- The register gains 68 rows, all ok or near, no weak rows.

**Missing-name scan, build plan item 1.8 (2026-10-22)**
- Added `src/tools/name_scan.py` (documented in the tools README and in `00_Project_Structure.md` section 10). The default scan lists capitalised mid-sentence words used 15 or more times in the chapters and absent from every compendium document; it now reports none. The stricter `--index` scan lists words absent from the Name Index and Glossary and currently finds 160 (mostly ordinary capitalised words such as "Moderate" and places already documented elsewhere); it is a worklist for the Name Index, not a failure.
- Triaged the 17 names from the 2026-10-22 scan into entries: Madam Landry, Janice, Ernest Geller, Jerrick and Imran Keane (`Minor_Cast_Books_1-3.md`); Thanh, Ingrid, Loth, Night Stalker and Higgy (`Minor_Cast_Books_4-6.md`); Merrick Harlowe, Eric Maldonado, Rangel and Tellez, Carilo, Emresh and Lancet de Varco (`Minor_Cast_Books_7-9.md`); Finneus Gallow, Geneva Andros and Kol Kelis Vel (`Minor_Cast_Books_10-13.md`). Rejector is a Glossary term (Jason's title among Builder cultists). Later-book facts in the lower-level files sit inside level 2 or 3 tags.
- Also covered the scan's remaining hits: Glossary entries for Ancestral Majesty (Soramir Rimaros), the nicknames Hump and Soph, and "the Shades"; Name Index entries for Bruce Corwin, Cas Vin Baral and Relia Vin Vala. All 20 new Name Index lines carry a pointer or cites.

**Authority and sanctioning, build plan item 2A.1 (2026-10-22)**
- New `02_Cosmology_and_Powers/Authority_and_Sanctioning.md` in the Topic template: what authority is (set-state against potential-state, Book 8, Ch57), why it must be traded and cannot be taken (Book 8, Ch52 and Ch54), the role of will and affinity (Book 11, Ch33), and sanctioning with its cases (the original Builder, the Boundary and the World-Phoenix, Shade, Hero, Purity, Undeath's avatar), its limits (Jason cannot sanction a god, Book 13, Ch1024 L141) and the confusion with the Sanction affliction. Book 11-13 material is in level 3 tags.
- Cross-links added in `Great_Astral_Beings.md` and `00_Cosmology_Overview.md`. The folder overview was regenerated.
- Observed: Shade has no individual character file and is covered only in `Familiars.md`; this belongs with the character promotions in Tier 2E.

**Familiars folder, on request (2026-10-22)**
- New `07_Characters/Familiars/` with individual entries for the familiars that have a personality: Shade, Colin, Gordon (Jason's), Stash (Humphrey's), Onslow (Clive's) and Shimmer (Belinda's). Each has a summary, line-cited facts and a "using this in a story" note, with Books 4 to 9 material under level 2 tags and Books 10 to 13 under level 3 tags. `Familiars.md` stays as the overview and links to them.
- Character files now list their familiars: Jason (Shade, Colin, Gordon), Humphrey (Stash), Clive (Onslow), Belinda (Shimmer and an echo spirit), Landemere Vane (the native familiar Jason met first, Book 5, Ch40 L81) and Autumn Leal in `Minor_Cast_Books_7-9.md` (a lost bonded companion and a new hydra familiar). Name_Index entries point to the new files; Carlivexistrix (Stash's mother) is added.
- Gordon's file notes the human "Other Gordon" of Books 4 and 5 to avoid confusion. Umber keeps his own file in `07_Characters/`.
- The convention is recorded in `00_Project_Structure.md`: every character file lists the character's familiars.

**The Cosmic Throne and the System, build plan item 2A.2 (2026-10-22)**
- New `02_Cosmology_and_Powers/Cosmic_Throne_and_the_Sundering.md`: what the throne regulated, the pacts that replaced it, who stood aside, why the Builder and the nameless made the repair necessary, the conditions on the repair (empty throne, a candidate with a throne connection, no servants of great astral beings), the risks, the Book 11 restoration scene and the Book 12 and 13 aftermath.
- New `02_Cosmology_and_Powers/The_System.md`: the Book 11 announcement, Jason's imprint on the throne, the default and expanding features, the System Administrator gift and its limits, the withdrawal over indenture and the diamond-rankers' position, and the Book 13 alerts.
- Both files are level 3 throughout. Cross-links added to `00_Cosmology_Overview.md` and the Glossary.

**The Rules of Intrusion, build plan item 2A.3 (2026-10-22)**
- New `02_Cosmology_and_Powers/The_Rules_of_Intrusion.md` (level 3): the rules' scope (holy wars and dimensional invasion), closed worlds, rank-based flexibility and pretexts, invitations and the host-guest principle, the stricter regime since the throne was restored, Knowledge's need for a holy war, and why the Earth bridge anchor sits outside Jason's domains. Cross-linked from the Cosmology overview.

**The deep astral and Interstice, build plan item 2A.4 (2026-10-22)**
- New `02_Cosmology_and_Powers/The_Deep_Astral_and_Interstice.md`: Clive's dumpling-soup account, astral spaces, why Jason's body ceased to exist, Interstice as shown at Book 3, Ch69, Dawn's and Jota's descriptions of it, the regions of the deep astral, travel in dimension ships and the dock into the astral from Jason's kingdom. Books 5 to 9 material is under level 2 tags and Books 11 to 13 under level 3 tags.

**The Unorthodoxy and the Council of Kings, build plan item 2A.5 (2026-10-22)**
- New `02_Cosmology_and_Powers/The_Unorthodoxy.md` (origin, hiding, birthing planets, its own astral kings, the overcharged-mana secret, members and associates, the Earth colony) and `The_Council_of_Kings.md` (what it is and is not, membership and rivals, Vesta Carmis Zell's changing position, Jamis Fran Muskar's role, the détente with the originals, and the Boko and Book 13 episodes). Both are level 3. `Astral_Kings_and_Messengers.md` now points to them.
- Member lists are limited to the named figures in the text; the full Council membership is not given anywhere, which is recorded in Open_Questions 3.

**One file per major god, build plan item 2A.6 (2026-10-22)**
- New folder `02_Cosmology_and_Powers/Gods/` with `Knowledge.md`, `Death.md`, `The_Healer.md`, `Hero.md`, `Purity_and_Disguise.md`, `Dominion.md`, `Undeath.md`, `Fertility.md`, `Destruction.md`, plus two stubs, `Hearth.md` and `Pain_and_Discord.md`, which record everything the text says (very little). Discord has no entry of its own: the text names it only as a hidden god. Each file has line-cited facts, with later-book material under level 2 or 3 tags, and a note on using the god in a story. `Gods_and_Churches.md` now links to them.
- Open_Questions 6 (Hero's sanction) is resolved: Hero plans to sanction himself to add a gentler miracle option and make the relics of dead demigods usable (Book 11, Ch68 L707-709).
- Observed: Death appears as a woman, a pale male elf and a plain woman in different scenes; the files record all three.

## Pending index updates

Names and terms from the Places and Magic documents that are still missing from the Glossary or Name Index (add when next touching those files): Argy (Palisaros resident), Hester (Emir's portaler, first named Book 1), Jacinta Adeline (already indexed; check spelling), Keane (Rimaros adventurer), Casallini (Girlano border city), the Ustei (nomad tribe; Book 1), Medallion of Escape, Summoner's Die: Form, Immortal Crest, Spirit Vault (as a term), Sky Link Company, Stable and Unstable Genesis Cores (partly under *Genesis core*).

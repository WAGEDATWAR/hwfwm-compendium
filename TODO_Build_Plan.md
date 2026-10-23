# Build Plan TODO

Status: Working list (written 2026-10-22 after the verification passes on 01, 02-10; companion to `TODO_Verification.md`)
Related: 00_Project_Structure.md, TODO_Verification.md, Appendices/Open_Questions.md, Appendices/Change_Log.md

**How this file differs from `TODO_Verification.md`.** That file lists claims that are unconfirmed. This file lists everything still to build, grouped in tiers by how much the project depends on it. Work the tiers in order unless an item says otherwise; items inside a tier can be done in any order. Items marked **(suggested)** are additions beyond the original structure document that I judge worth doing. Sizes are rough: S = under an hour of work, M = a few hours, L = a day or more.

**Standing rules for every item** (from `00_Project_Structure.md`): book text beats chapter notes beats wiki; cite as "(Book N, ChX LY)" against `src/Source_Text/`; one file per character; no game mechanics or invented numbers; mark spoiler levels; after any edit run `src/tools/build_register.py`; update Change_Log, Name_Index, Glossary, Open_Questions and the structure document's section 11 when an item lands.

## State of the project (2026-10-22)

| Area | Files | State |
|---|---|---|
| `01_World_Primer.md` | 1 | Verified against the book text; sections 8-12 are summaries |
| `02_Cosmology_and_Powers` | 4 | Verified once; thin for the importance of the topic |
| `03_Magic_and_Adventuring` | 22 | Verified; essence and monster lists incomplete |
| `04_Peoples_and_Cultures` | 22 | Verified; several cultures unwritten |
| `05_Organisations` | 6 | Verified once; thin |
| `06_Places` | 34 | Third verification pass done; 16 smaller places written |
| `07_Characters` | 137 (incl. 6 grouped minor-cast files) | Core cast verified; 2026-10-22 files verified by cite only |
| `08_History_and_Timeline` | 14 | Per-book timelines done; Book 12 closing chapters unplaced |
| `09_Items_and_Artefacts` | 7 | Verified; narrow |
| `10_Roleplay_Support` | 6 | Verified; no era packs |
| `Appendices` | 6 | Source Register and Map generated; Name_Index and Glossary current to the new files |

Register: 3,445 ok, 210 near, 52 weak, 22 reviewed, 16 wiki, 1 notes rows. The project folder is **not under version control** and the only backup is the folder itself.

---

## Tier 0: Safety, hygiene and tooling (do first; all are quick and protect the rest)

- **0.1 Put the folder under version control (suggested, S).** Run `git init`, add a `.gitignore` for `src/tools/wiki/` and generated JSON, and commit. Reason: the compendium has been edited by hundreds of scripted and manual replacements; there is no way to undo a bad pass. Acceptance: a first commit exists and `git log` shows the Change_Log dates as tags.
- **0.2 (Done 2026-10-22) Move the living scratchpad to a final name (S).** `src/tools` holds `build_register.py`, `rd.py`, `who.py`, `cc2.py`, `wiki_lists.py`, `compose_wiki.py`, `mkchar.py`, `grplib.py` and the one-off `apply_*.py` and `b*.py` scripts. Rename to something permanent (for example `src/tools`), delete or archive the one-off scripts (`apply_notes.py`, `apply_primer.py`, `b1.py` to `b9.py`, `write_places*.py`, `fix_*.py`, `idx.py`) into `src/tools/archive/`, write a README listing each tool, and update the memory note in `feedback_scratchpad_location.md`. Keep the rule that the old Gmod scratchpad is never used.
- **0.3 (Done 2026-10-22) Refresh the stale parts of `00_Project_Structure.md` (S).** Section 3's "What exists now" list is out of date (it still says 21 open questions and lists drafts that are now verified), and section 11 repeats work now done. Rewrite section 3 as a table that matches the state table above, and shorten section 11 to point at this file.
- **0.4 Refresh `TODO_Verification.md` after every pass (S, recurring).** Done on 2026-10-22; keep resolved items marked "(Resolved)" for one pass, then delete.
- **0.5 (Done 2026-10-22) Write a document linter (suggested, M).** A script that checks every compendium `.md`: header block present with Status, Spoiler level, Valid from, Valid through, Sources and Related; spoiler level is 0-3; every `(Book N, ChX LY)` cite names a chapter and line that exist in `src/Source_Text/`; relative links in Related resolve; no leftover shorthand ("->", "w/"); file is listed in its folder's overview. Report findings to a file, not the console. Acceptance: zero errors on the current tree, and the script runs inside `build_register.py`.
- **0.6 (Done 2026-10-22) Make the register builder report deltas (S).** Print rows added, removed and newly weak since the previous run, so a pass shows only what it changed.
- **0.7 (Done 2026-10-22) Add a per-folder overview check (S).** `06_Places/00_Places_Overview.md`, `07_Characters/00_Characters_Overview.md`, `04.../00_Peoples_Overview.md` and the others must list every file in their folder. Generate the lists from the folder contents so they cannot drift.
- **0.8 (Done 2026-10-22) Spelling and naming variants register (suggested, S).** One table in the Glossary's variants section for every in-text variant found so far: Hendren/Hedron, Sigrid Freyn/Volaire, Hurin/Huren, Jonah/Jonas, Beaufort (two people), Mose/Moses if any, Kaal/Kaal's title. Record the form used and why.
- **0.9 (Done 2026-10-22) Spoiler tag syntax and linter support (suggested, M; decision 3).** Define one tag form for spoiler-level sections inside a file, for example an HTML comment pair `<!-- level:2 -->` ... `<!-- /level -->` around the existing "Later developments" sections and any other section above the file's header level (comments do not render, so the files read normally). Document the form in section 6 of `00_Project_Structure.md`, add a linter check that tags are balanced, that levels are 0-3 and that no tagged section is lower than the file's header level, and retrofit the existing files section by section, starting with the 2026-10-22 character files. Only retrofit where it is convenient: a file whose header level already covers everything needs no tags.

## Tier 1: Close what is already open (small, high value, removes ambiguity)

- **1.1 (Done 2026-10-22) Place the Book 12 closing chapters in the timeline (M).** Ch62-67: the Earth arrival, the artefact-site battle, Lenora, the reunion with Emi, the appendix (Ch67). Add rows to `Book_12_Timeline.md` and `Master_Timeline.md` with cites. Known open point: the Book 12 present is set in 2037 (Open_Questions 18); record it in the timeline header.
- **1.2 (Done 2026-10-22) Second detail pass on Books 12 and 13 timelines (M).** Both are line-cited but sparse for their length (Book 13 has chapters up to 1024). Aim for one row per scene.
- **1.3 (Done 2026-10-22) Clear the 52 weak register rows (M).** Open the list in `Source_Register.md`; most are voice-note judgments in `Tone_and_Voice.md` and character files. For each: confirm the cite, tighten the claim, or move the judgment to a plainly marked "Roleplay notes" sentence with no cite. Targets: `Tone_and_Voice.md` (4), `Callum_Morse.md` (2), `Danielle_Geller.md` (2), `Book_08_Timeline.md` (2), `Book_13_Timeline.md` (2), and the 1-row files.
- **1.4 (Done 2026-10-22) Settle the remaining notes and wiki lines (S-M).** The seven "not located" claims in `TODO_Verification.md` section A; upgrade the Neil/Cassandra wiki lines to Book 1, Ch110 L17 and Book 2, Ch27 L57; check the Name_Index entries for Gabrielle Pellin as Travis's wife and Ian Evans as a doctor.
- **1.5 (Done 2026-10-22) Resolve or document the remaining open questions (M).** Of the 24 entries in `Open_Questions.md`, items 14-19a, 23 and 24 are now narrowed or resolved. Still genuinely open and to be tested again against the text: 1-6, 8-11, 13, 19, 20, 22. Items 4, 5 and 11 may be answerable in Book 13's briefing chapters (Ch1015-1017); 22 (the two continental councils) may be answerable from Book 6 Ch47 context; 13 (Vitesse's magic density) may need a different search (look for ratings given as "tier" or comparisons to Cyrion).
- **1.6 (Done 2026-10-22) Check the shorter-term inconsistencies list (S).** Garuda route (Book 4, Ch65 L22 vs L28); Inescapable Doom versus Inevitable Demise for the same ability (Book 2, Ch13 L62 vs L66); Hendren/Hedron; Melody's "quarter century" versus Marta's "two decades" (different events, now recorded); the two Beauforts. Each needs a one-line ruling in the relevant file and the Glossary variants table.
- **1.7 (Done 2026-10-22) Unwritten short entries (S each).** Hegemon's Dominion (its own item entry), Jason's dimensional storage and portals, Emir's other vehicles, guild and Adventure Society badges (09); Orin Pensinata and Hudson Kettering have group entries but could use a short note each in `Minor_Cast/` if they appear again.
- **1.8 (Done 2026-10-22) Add a missing-name scan to the tools (suggested, S).** The 2026-10-22 scan of capitalised words in the chapter files that appear 15+ times and nowhere in the compendium found: Thanh, Geneva, Maldonado, Landry, Ingrid, Janice, Carilo, Merrick, Kelis, Emresh, Loth, Gallow, Higgy, Ernest, Lancet, Stalker, Rejector (a Book 3 term). Triage each into a character, place or term entry; save the scan script and re-run it after each content tier.

## Tier 2: Core reference content that is thin or missing

### 2A. Cosmology and powers (`02_Cosmology_and_Powers`, only 4 files)
Add topic files in this order, each with the Topic template (Summary / How it works / Variations / Examples / Misconceptions / Changes over time):
- **2A.1 (Done 2026-10-22) Authority and sanctioning (M).** Book 8-13 passages on authority as the currency of transcendent beings, sanctions (Purity, the old Builder, Hero's planned self-sanction), and Jason's domains as "set-state authority" (Book 8, Ch57 L64-67).
- **2A.2 (Done 2026-10-22) The Cosmic Throne, the Sundering and the System (L).** Raythe and Velius's account (Book 11, Ch64-65), Jason's briefing (Book 13, Ch1017), the throne "could never be restored" (Book 12, Ch1 L34), the System as Jason's interface made universal (Book 12, Ch1 L36), the System Administrator gift and the withdrawal over indenture (Book 12, Ch50). One file for the Throne, one for the System.
- **2A.3 (Done 2026-10-22) The Rules of Intrusion (S).** Book 12, Ch63 L5-7 and Book 13, Ch1017 L44.
- **2A.4 (Done 2026-10-22) The deep astral and Interstice (S).** Dumpling soup (Book 1, Ch69 L85) and Interstice (Book 3, Ch69 L219-222).
- **2A.5 (Done 2026-10-22) The Unorthodoxy and the Council of Kings (M).** Both appear in `Astral_Kings_and_Messengers.md` but deserve their own files with member lists (Open_Questions 2-4).
- **2A.6 (Done 2026-10-22) One file per major god (L, suggested).** Knowledge, Death, Healer, Hero, Purity/Disguise, Dominion, Undeath, Fertility, Hearth, Pain, Destruction, Discord. The existing `Gods_and_Churches.md` is a list; individual files can hold clergy, rules, miracles and conflicts, each marked by spoiler level.
- **2A.7 (Done 2026-10-23) Great astral beings, one file each (M, suggested).** World-Phoenix, Builder (original and new), Reaper, Celestial Book, Legion, All-Devouring Eye, Keeper of Moments, Seeker of Songs, Whisper in Corners, Word in the Silence; at least stubs with their known vessels.

### 2B. Organisations (`05_Organisations`, only 6 files)
- **2B.1 (Done 2026-10-23) Network (M).** Founding (Book 13, Ch1017), the Grid, categories, committees (Mr North, Mrs West, Mr/Mrs East and South in Book 5), branches (Sydney, Lyon, Berlin, Zurich), public name GDN.
- **2B.2 (Done 2026-10-23) Cabal (M).** Its leaders, vampire lords (Elizabeth, Wassily, Klaus, Magdalyn), old founders and the messenger link (Book 13, Ch954 L3-6).
- **2B.3 (Done 2026-10-23) Engineers of Ascension (M).** Noreth's leadership (Book 13, Ch1017 L39-40), Plan A and B, Gerling, Barbou.
- **2B.4 (Done 2026-10-23) EDJI and the post-reveal institutions (M).** The multinational taskforce, the UN Office of Supernatural Affairs (Anna, Holly Macrossan), the Joint Magitech Weapons Research Institute, the Asano clan's organisation (Yumi, Ketevan, Noriko's old clan).
- **2B.5 (Done 2026-10-23) Order of the Reaper and Cult of the Reaper (M).** The history told in Book 9, Ch27 and Book 10, Ch36; Callum's, Melody's and Marta's roles; Open_Questions 20.
- **2B.6 (Done 2026-10-23) Alchemy Association, Mirage Chamber Association, Magical Research Association (S each).** Each is mentioned in `Magic_Society_and_Associations.md`; split out with cites.
- **2B.7 Churches as organisations (M).** One short file per church that appears as an institution: Healer, Knowledge, Purity (and the Lasalle family), Dominion, Death, Undeath, Hero.
- **2B.8 Guilds (M).** Burning Violet, Sapphire Crown, Team Shining Scabbard's backers; the guild quota system (Book 7, Ch12).
- **2B.9 Noble houses (M).** Geller, Remore, Mercer, Rimaros, Headingway, Kettering, Davone, Amouz.

### 2C. Magic and adventuring (`03_Magic_and_Adventuring`)
- **2C.1 Grow `Essence_Catalogue.md` toward every essence the books name (L).** Use the existing scan (`ess_scan.py`, `wiki_lists.py`) to list essences named in chapter files, then add a line with the first book cite for each. Keep wiki-only essences in `Wiki_Reference_Lists.md`.
- **2C.2 Extend `Monsters.md` by region and rank (L).** Add apocalypse beasts, bone feasters, spider moles, fergax, hydras, rejectors, nightmare hags and the other named monsters with stated ranks (each with one cite).
- **2C.3 Individual ability files for each main character's power set (M, suggested).** Jason's is in `Jason_Power_Set_Reference.md`; add Sophie, Humphrey, Rufus, Gary, Farrah, Clive, Belinda, Neil, Emi, Taika using the party-interface lines in the chapter files.
- **2C.4 Titles and blessings (M, suggested).** Giant Slayer, Resolute, Indomitable, Godless Prophet and the title effects on auras (primer section 5).
- **2C.5 Reconcile 09 with 03 (S).** Make sure every item type in `09_Items_and_Artefacts` is explained in a 03 topic file, and cross-link them.

### 2D. Peoples and cultures (`04_Peoples_and_Cultures`)
- **2D.1 Culture files still unwritten (M each):** Girlano, Sadi Andali, Zartos, the Dragon Lands (draconian homeland), Vitesse, the Mirror Kingdom, Dreisil as a nation, Boko, Jayapura (beyond the Pranay file), the Ustei homeland.
- **2D.2 Thin people files (S-M):** Merfolk (one line only), Goblins and Fairies (Earth-side), Runics, Valash, plus a new file for the lehenik (Nik's kind, Book 11, Ch23 L42 and Book 13, Ch991 L5) and the messengers as a people (cross-link to 02).
- **2D.3 Clothing, food, festivals and transport by region (M).** Collect every line that describes a meal, outfit or festival (the Rimaros festival of Book 9 Ch3, Yaresh, Kurdansk, Pranay, Estercost).
- **2D.4 Education (M, suggested).** Remore Academy, the Magic Society research wing, Kazlahk University of Medicine, Jason's school in Book 13.
- **2D.5 Calendar, holidays, naming customs (S, suggested).** The six-day week, the five extra days, palindromic names in Rimaros (Book 7, Ch18 L42), titles and forms of address (`Tone_and_Voice.md` has a start).

### 2E. Characters (`07_Characters`)
- **2E.1 Unfiled Name_Index entries (S each):** Adam Cosgrove, Arash, Argrave Mericulato, Barry Sinise, Ben Headingway, Brian, Calcifer Bynes, Cassie, Crivens, Dara Rimaros (covered in a family file; add a stub), Daryll, Delia DeWitt, Dink, Durrum, Fiorella, Franklin, Haliastur, Hiram, Jali Corrik Fen, Jamar, Ketis, Koa, Tabitha Gert, Vandrick Macarro, and Mr North / Noreth (has Mr_North.md; add the Noreth alias to its title).
- **2E.2 Characters with many lines but no individual file (M each).** Candidates from counts: Lorenn (Cardinas), Kalif, Rosa, Valetta and Alice (Moon's Edge), Calcifer Bynes, Durrum and Kurik (brightheart earth aspects), Duke of Boko, Remy (Finnegan's portal specialist), Lindy, Magdalyn (vampire lord), Wassily and Klaus, Michael Mills (general), Barstow, Miriam Coyle, Natala (Jota's first officer), Hastor (Sigrid's father), Esteban Galo. Triage by hit count with `who.py`. **Decision 1:** write a full individual file for any character with enough material to fill the character template (rule of thumb: about 15 or more distinct cited facts, or a role across more than one book) and keep grouped `Minor_Cast/` entries only for characters with little information. Review every current grouped entry against that rule, promote those that qualify (candidates: Hudson Kettering, Niko, Emily, Dara and Zareen Rimaros, Sendira, Laront, Beaufort the cult commander, Kreegle, Killian's later scenes, Hils Jaramaris), and move a promoted entry's facts into the new file and delete it from the group file.
- **2E.3 Re-verify the 2026-10-22 character files (M, suggested).** Those 32 files and four group files were verified by cite only (each cited line was read when written). Run `cc2.py` at a lower threshold and sample 3 cites per file against the chapter text.
- **2E.4 Bring older character files up to the new standard (L).** The earlier ~80 supporting files are mostly 3-line stubs (Pelli, Itsuki Tiwari). Expand each to the full character template (Appearance, Voice, Relationships, Secrets, Roleplay) in order of narrative importance.
- **2E.5 Relationship files (M, suggested).** Family trees (Asano, Remore, Geller, Mercer, Rimaros royals, Evans/Asano line), romances and rivalries, teams and their members by era (Team Biscuit, Moon's Edge, Storm Shredder, Shining Scabbard, Rick's team, Beth's team). Generate from the character files' cites where possible.
- **2E.6 Character "knowledge state" tables (M, suggested).** For each core character, a table of what they know about Jason's origin, the System, Knowledge's plan and the Earth link at the end of each book. This supports roleplay and spoiler discipline.

### 2F. Places (`06_Places`)
- **2F.1 Places named only once:** the Great Southern Continent, Casallini, Lindover Lumber Mill, Clementson's property, Oleyu's river (add only if later scenes give them substance).
- **2F.2 Missing region overviews (M each, suggested):** the Africa-like continent (Greenstone, Boko, Rakesh, Hornis, Oleyu, Zartos, Sadi Andali), Estercost's continent, the Great Southern Continent, the Storm Kingdom's islands.
- **2F.3 Jason's domains (M):** Nitra, Saint-Étienne, Casselton Beach, Asano Village and the astral kingdom are written; collect the "set-state authority" and domain-rule passages into one `Domains.md` (suggested).
- **2F.4 A locations-by-era table (S, suggested):** which places exist and in what state in each era (Boko before and after, Cartise ruined, Yaresh before and after the battle).
- **2F.5 Vitesse magic density (S):** see Tier 1.5; the check may remain open.

### 2G. Items (`09_Items_and_Artefacts`)
Items listed in 1.7 plus: the Trap Weaver Battle Robe, soul forge, Rexion's array-powered citadel, avatars of doom as items, artefact-site weapons, the clockwork kings, the Rejector, the transformation-zone treasures (reality cores, genesis cores), and the Book 13 bridge anchor and Firmamental Bridge Anchor.

## Tier 3: History and synthesis (builds on tiers 1 and 2)

- **3.1 Era guides (L, from the structure document).** One 3-6 page guide each: the Builder cult in Greenstone; the Reaper trials; Earth and the monster waves; the Rimaros surge; the Battle of Yaresh; the Cardinas expedition and zone; the Earth vampire war; the return and bridge. Each states what is known and unknown at the chosen point, who is where, and the spoiler level.
- **3.2 War and crisis files (M each).** The One Day War (Book 7, Ch66 L27), the Messenger War, the Battle of Yaresh, the Boko evacuation, the vampire war (Open_Questions 19).
- **3.3 A consolidated Master Timeline v2 (M).** Rebuild `Master_Timeline.md` from the per-book files, with a month-count table, rank/level checkpoints for core characters and the corrections already found. The Book 11 Part II intervals still need a combined clock decision (TODO_Verification section D).
- **3.4 Rank and progression tracks (M, suggested).** For Jason and the core team: the book and chapter where each rank, essence, confluence and major ability was gained (the Jason Power Set file is a start).
- **3.5 Who-knows-what-when matrix (M, suggested).** Rows are secrets (Jason's origin, the Builder, the System, Knowledge's plan, the Network founder); columns are books; cells give the line where each group learns it. Feeds `Spoiler_Management.md`.
- **3.6 A chapter digest (L, suggested).** One or two sentences per chapter for all ~987 chapters, with cite, as `08_History_and_Timeline/Chapter_Digest_Book_NN.md`. This turns the corpus into a lookup layer and makes every later verification pass faster. Generate a first draft with the chapter-title index already in `Source_Map.md` section 5. **Decision 2:** the digest is committed to the repository. It is the project's own short summary (one or two sentences and a cite per chapter, no quoted passages), so it is safe to push; keep it out of any export that would reproduce chapter text.
- **3.7 Recurring motifs and in-world sayings (S-M, suggested).** Phrases used as incantations ("Feed me your sins"), running jokes (biscuits, Handsome Doctor) and cultural references, with cites; supports `Tone_and_Voice.md`.

## Tier 4: Roleplay and use-ready products

- **4.1 Era starter packs (L).** For each era in `Era_Selection.md`: one page of setting, three starting situations from `Plot_Hooks.md`, a cast list with voice cues, dangers, what the characters know, and spoiler-safe language for the narrator.
- **4.2 NPC cards (M, suggested).** A half-page card per recurring NPC with appearance, voice cue, goal, secret and valid-from/through, generated from the character files.
- **4.3 Expand `Plot_Hooks.md` to 3-5 hooks per era, with a branching-outcome note (M).** Keep the rule that hooks state no outcome the books do not give.
- **4.4 Secrets and rumours sheets (M).** Per era, the true facts, the common beliefs and the lies in circulation (Emir's account of the Order against Shade's, the churches' story of Purity).
- **4.5 Spoiler-safe summaries (M, suggested).** A one-page summary of each of the four spoiler levels that a narrator can read before a session without learning later facts.
- **4.6 Quick-reference sheets (S-M, suggested).** One page each for: ranks and lifespans; the coin table; forms of address; the calendar and festivals; the churches and what they do.
- **4.7 A "what changes between eras" diff (M, suggested).** For Greenstone, Vitesse, Rimaros and Yaresh: the place before and after the major events.

## Tier 5: Quality assurance and long-run maintenance

- **5.1 A second full verification pass on each section, using a different reader (L each).** Method as before: read each cited line, confirm it supports the claim, grade near/weak rows. Suggested order: 07 (largest), 06, 03, 08, 05, 02, 04, 09, 10, 01.
- **5.2 Spot-check `Source_Map.md` section 6, the keyword-generated state-change list (M).**
- **5.3 Wiki list refresh (M).** Re-run `wiki_lists.py` and `compose_wiki.py` when the wiki cache is refreshed; extend the book cross-references in `Wiki_Reference_Lists.md` (the current matcher only finds "<name> essence" patterns). **Decision 4:** once the cross-reference matcher is improved (for example by also matching phrases such as "<name> confluence", "stone of <name>" and "god of <name>", and by checking spellings in `Name_Index.md`), move `03_Magic_and_Adventuring/Wiki_Reference_Lists.md` to `Appendices/Wiki_Reference_Lists.md`: change the output path in `compose_wiki.py`, the Related lines that point at it, and the references in the Change_Log, Glossary and Gods_and_Churches.
- **5.4 Lorebook derivation (M, per structure document section 2).** The lorebook JSON is derived and not a source. After Tiers 1-2 are done, regenerate it from the compendium and not the other way round.
- **5.5 Exports (S-M, suggested).** A script that concatenates the compendium into one Markdown or PDF per spoiler level (0 only, 0-1, 0-2, all), so a narrator can hand a player only what they should read. **Decision 3:** exports respect spoiler levels through tagged sections inside each file (item 0.9) where tags are convenient, falling back to the file's header level elsewhere; the exporter keeps a section only when its level is at or below the requested level.
- **5.6 Link and anchor checks in CI-style script (S).** Part of the linter in 0.5.
- **5.7 Redundancy audit (M, suggested).** The same fact is stated in several documents (calendar, coin table, the Network's founding). Pick one home file for each, replace the repeats with pointers, and record the home in the Glossary.
- **5.8 Change_Log housekeeping (S).** The log now exceeds 340 lines; split into one file per month and keep the last two months in `Change_Log.md`.
- **5.9 Accessibility and style pass (M, suggested).** Check style rules in section 7 of the structure document (full names on first use, past tense for history, no shorthand), and normalise headings across character and place files.

## Tier 6: Stretch goals (only after Tiers 0-3)

- **6.1 Text-form maps and distance tables (M, suggested).** The books give relative positions; build text maps of Greenstone's districts, Vitesse's garden towers, Rimaros's islands and Yaresh, with only distances the text states.
- **6.2 A quote bank (M, suggested, copyright-limited).** Short quotes (under fifteen words) that capture voice, with cites, only where `Tone_and_Voice.md` needs them; no long passages.
- **6.3 Wiki-versus-book discrepancy log (M, suggested).** Record every point where the fan wiki differs from the chapter text (the Hegemon's Will name, the 150-year siphon, nine months for the zone), so future readers know which tier to trust.
- **6.4 Pronunciation and naming notes (S, suggested).** Only where the text gives them.
- **6.5 Multiple-timeline alignment (M).** A table of Earth and Pallimustus calendars side by side with the five extra days and the six-day week.
- **6.6 A book-by-book "what a new reader needs" summary (M).** Four-paragraph recaps at each spoiler level for reading order guidance.

---

## Dependencies and order of work

1. Tier 0 first (items 0.1, 0.2, 0.5 protect everything else).
2. Tier 1 next; items 1.1 and 1.2 unlock the era guides in Tier 3.
3. Tier 2 can run in parallel by folder. Do 2B and 2A before 3.1, 3.2 (they supply the organisation and cosmos references the era guides link to).
4. 3.6 (chapter digest) pays for itself if done before the second verification pass in 5.1.
5. Tier 4 products depend on Tier 2E and 3.
6. Run the register builder and the linter at the end of every item; log the item in `Appendices/Change_Log.md`.

## Decisions made (2026-10-22)

1. **Characters**: full individual files for characters with enough information to justify one; grouped files only for minor characters with little information (see 2E.2 for the rule of thumb and the promotion review).
2. **Chapter digest (3.6)**: committed to the repository.
3. **Spoiler-level exports (5.5)**: tagged sections inside each file, used where convenient (see 0.9); the header level covers the rest.
4. **Wiki Reference Lists**: to move under `Appendices/` after the cross-reference matcher is improved (see 5.3); no move yet.

No open decisions remain. Add new ones here as they arise.

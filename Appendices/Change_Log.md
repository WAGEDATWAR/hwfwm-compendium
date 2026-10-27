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
6. **Housekeeping (build plan item 5.8)**: this file keeps the entries of the current and the previous month; `python3 src/tools/log_archive.py` moves older months to `Change_Log_YYYY-MM.md`. Because the whole project so far falls in October 2026, the first three days were archived by hand as `Change_Log_2026-10-20_to_22.md`.
7. **Dates** are the session date. Entries from the first sessions were reconstructed from the file history; where a session date was not recorded they carry the date of the first full session in which the work was confirmed.

Status values used in headers: Draft (written, not yet checked against the book text), Reviewed (read through for consistency), Verified (every claim checked against the book text).

## Log

Entries from 2026-10-20 to 2026-10-22 are in `Change_Log_2026-10-20_to_22.md`. Entries from 2026-10-23 on follow.

**Great astral beings, one file each, build plan item 2A.7 (2026-10-23)**
- New folder `02_Cosmology_and_Powers/Great_Astral_Beings/` with `World_Phoenix.md`, `The_Builder.md` (original and new), `The_Reaper.md`, `Celestial_Book.md`, `Legion.md`, `All_Devouring_Eye.md` and `Keeper_of_Moments.md`, plus stubs `Seeker_of_Songs.md`, `Whisper_in_Corners.md` and `Word_in_the_Silence.md`, which record every thing the text says. Each carries line-cited facts with later-book material under level 2 or 3 tags. `Great_Astral_Beings.md` links to them.

**The Network, build plan item 2B.1 (2026-10-23)**
- New `05_Organisations/The_Network.md`: the federation structure (International Committee, branches, steering committees, divisions, tactical teams), spirit coin supply, categories and cores, the Grid and the concealed Saint-Étienne sector, going public as the GDN and the split into four blocs. Book 13 material is under level 3 tags. `Earth_Powers.md` points to it.
- The plan's "committees (Mr North, Mrs West, Mr/Mrs East and South)" are the EOA's four cardinals, not Network committees; they belong with item 2B.3.

**The Cabal, build plan item 2B.2 (2026-10-23)**
- New `05_Organisations/The_Cabal.md`: nature and structure, the Book 5 to 6 growth, vampire rush and splintering, and the Book 10 to 13 schism, territory, Boris's leadership and the named vampire lords. Book 10 to 13 material is under level 3 tags. `Earth_Powers.md` and the Glossary point to it.
- No individual files exist for Wassily, Klaus or Magdalyn; the text gives them little beyond their names (Book 6, Ch40 L18; Book 13, Ch1009 L81).

**The Engineers of Ascension, build plan item 2B.3 (2026-10-23)**
- New `05_Organisations/Engineers_of_Ascension.md`: nature and aims, the Four Cardinals, Barbou's rise to Mr East, the Grid plan and Mrs South's refusal, splintering after the sabotage, and the Book 13 account of Noreth, Plans A and B, Audrey Blaine, North's vault and the superhero legacy. Book 13 material is under level 3 tags. `Earth_Powers.md` points to it.
- Gerling is a Network category four, not an EOA member; he appears as the EOA's opponent and is covered in his own file.

**The EDJI and post-reveal institutions, build plan item 2B.4 (2026-10-23)**
- New `05_Organisations/EDJI_and_Post_Reveal_Institutions.md` (level 3): national Supernatural Affairs bodies, the UN Office (Anna Tilden, Holly Macrossan), the Asano Village taskforce under Lenora Coleman, Jason's proposal and the Saint-Étienne Summit Accords, the EDJI and the Quilido Procedure, the Joint Magitech Weapons Research Institute, and the Asano clan as an organisation (Yumi, Ketevan, Noriko). `Earth_Powers.md` points to it.
- The Accords are cited only from Book 13 mentions; their negotiation is not narrated in the lines read.

**The Order and Cult of the Reaper, build plan item 2B.5 (2026-10-23)**
- New `05_Organisations/Order_and_Cult_of_the_Reaper.md` (header level 1, later material under tags): the old Order, the cult/order split, the Book 9 Ch27 account of the order's return (Melody Jain, Marta Fries, Callum Morse), the Reaper's own view (Book 11), and the Book 13 reveals about the joint-churches attack and Umber. `Cults_and_Orders.md` points to it.
- Open_Questions 20 is unchanged: Umber's claim that he has been "building up their numbers" (Book 13, Ch1024 L123) is recorded, but the order's present strength is still not stated.

**Alchemy, Mirage Chamber and Magical Research Associations, build plan item 2B.6 (2026-10-23)**
- New `05_Organisations/Alchemy_Association.md`, `Mirage_Chamber_Association.md` and `Magical_Research_Association.md`, each line-cited and short. `Magic_Society_and_Associations.md` points to them.
- The Mirage Chamber Association is named only in Book 2, Ch73 (Jayapura); the Geller chamber in Greenstone is a family facility. The Artifice Association has no file because the text gives it almost nothing; its mentions are recorded in the Alchemy file.

**Churches as organisations, build plan item 2B.7 (2026-10-23)**
- New folder `05_Organisations/Churches/` with `Church_of_the_Healer.md`, `Church_of_Knowledge.md`, `Church_of_Purity.md` (with the Lasalle family), `Church_of_Dominion.md`, `Church_of_Death.md`, `Church_of_Undeath.md` and `Church_of_Hero.md`. Each records institutional facts (temples, clergy, roles, relations), and leaves the gods themselves to the existing `Gods/` files. `Gods_and_Churches.md` links to them.
- Observed: the archbishop of Purity is Nicolas Hendren in Book 2, Ch19 and Book 3, Ch31, "Herston" in Book 2, Ch21 L21, and "Hedron" in Book 3, Ch1 L106 (Purity_and_Disguise.md follows that spelling); the Purity church file records the inconsistency and uses Hendren.
- The Hero temple in Book 12, Ch13 is in the Worship Ring of Outer Rexion, not Yaresh.

**Guilds, build plan item 2B.8 (2026-10-23)**
- New folder `05_Organisations/Guilds/` with `Burning_Violet.md`, `Sapphire_Crown.md`, `Guild_Quotas_and_Contribution.md` (Book 7, Ch12 and related lines) and `Team_Shining_Scabbard.md`. `Guilds_and_Houses.md` points to them.
- Observed: the text names no "backers" for Team Shining Scabbard other than the Mirror Kingdom's royal family; it is a royal-backed team, not a guild. The file records this.

**Noble houses, build plan item 2B.9 (2026-10-23)**
- New folder `05_Organisations/Noble_Houses/` with `House_Geller.md`, `House_Remore.md` (with the Remore Academy), `House_Mercer.md`, `House_Rimaros.md`, `House_Headingway.md`, `House_Kettering.md`, `House_Davone.md` and `House_Amouz.md`. The Kettering and Davone files are short because the text gives those families little. `Guilds_and_Houses.md` points to them.
- Observed: Hudson and Dustin Kettering are both called Ketterings (Book 2, Ch15 L44; Book 2, Ch29 L8); their relationship is not stated.

**Essence catalogue growth, build plan item 2C.1 (2026-10-23)**
- `Essence_Catalogue.md` gains a "More essences named in the text" section with 28 essences and their first cites: moon, sand, dimension, undeath, rat, plant, growth, bow, duck, whip, cloth, iron, transmutation, hunger, pure, skunk, light, wood, paper, frog, arsenal, song, axe, tooth, spear, skirmish and garuda. Rows from Books 4 to 9 are under a level 2 tag and those from Books 10 to 13 under level 3.
- New `src/tools/ess_lists.py` finds essence lists in the chapter files and writes `ess_lists_report.md`. The scan is noisy; the report is a working list, and each row added was read against the line.
- Not all essences are caught: the scan only finds essences named in a list or beside the word "essence". Single mentions in other phrasing may remain; `Wiki_Reference_Lists.md` still holds the wiki-only ones.

**Monsters by rank, build plan item 2C.2 (2026-10-23)**
- `Monsters.md` bestiary gains 11 level-1 rows (marsh wyrm, fergax, clockwork cat, silver constructs, clockwork king, mountain wyrm, umbral snake, oasis tyrant, elemental tyrant, stormshard pangolin, bronze apes), 7 level-2 rows (jungle troll, vortex elemental, silver black lizard, bone feaster, smoke dragon, desolation locust, nightmare hag second appearance) and a level-3 note on the elemental tyrant. Each has one cite.
- Not added because the text states no rank in the lines read: reef giant, reef kraken, mud lord, emperor ooze, belch bug, bog shambler, mangrove snatcher, margoll, pixelax, rat gorger, spotted tree cat, siege golem, grizzard and stormspire drake (wiki-only ranks stay in `Wiki_Reference_Lists.md`). "Rejector" is a title, not a monster, in the lines read.
- New `src/tools/monster_scan.py` writes a noisy working list of "X-rank <name>" phrases; the rows above were read against the lines.

**Power sets for the main characters, build plan item 2C.3 (2026-10-23)**
- New folder `03_Magic_and_Adventuring/Power_Sets/` with ten files: Sophie Wexler, Humphrey Geller, Clive Standish, Neil Davone, Belinda Callahan, Taika, Rufus Remore, Gary, Farrah Hurin and Emi Evans-Asano. Where the System shows an ability window (Books 2, 3, 8, 9 and 10), the file gives its type, cost, cooldown, iron effect and later-rank effects with the cite. Rufus, Gary, Farrah and Emi are described from narration, because the lines read show no System windows for them.
- The "party interface" lines in the chapter files are few (awakenings, racial gift evolutions and party-range notices); the ability windows come from the ability-review scenes (Book 2, Ch42-68; Book 3, Ch38-49; Book 8, Ch7-22; Book 9, Ch59, Ch93).
- Observed: Spirit Reaper (Book 2, Ch64 L72-75) is introduced after a line naming Humphrey but is a magic essence ability, which Humphrey lacks; it is recorded under Clive with the discrepancy noted. Gary's essence list varies (Book 9, Ch82 L22; Book 10, Ch67 L122; Book 10, Ch79 L63); his golem is called foundry and forge golem.
- Not done: silver and gold rewrites for abilities the text never shows; Jason's set remains in `Jason_Power_Set_Reference.md`.

**Titles and blessings, build plan item 2C.4 (2026-10-23)**
- New `03_Magic_and_Adventuring/Titles_and_Blessings.md`: the seven titles the text shows with their window text (Godless Prophet, Resolute, Spirit Warrior, Indomitable, Giant Slayer, Reality Hegemon, Keeper of the Cycle), how Jason explains titles in Book 13, and how blessings, tokens and star seeds differ, with the World-Phoenix blessing, Farrah's chain of blessings and Sophie's Boundary Breaker. `Auras.md` points to it.
- Titles are shown only for Jason (and Delia's Resolute in Book 13); the text gives no list for others.

**Reconcile 09 with 03, build plan item 2C.5 (2026-10-23)**
- `Alchemy_Artifice_and_Magical_Materials.md` gains section 7, "Item types and where they are described", with a one-line explanation and cite for each item type in `09_Items_and_Artefacts/` (badges, bags and storage, soul-bound items, cloud constructs, desert transport, consumables, awakening stones, tokens, and the Book 5 to 8 items under a level 2 tag).
- Every 09 file now links back to its 03 topic file in Related, and the 03 files for awakening stones, adventuring, astral spaces, Jason's set, titles and unusual magic link to their 09 files.

**Culture files, build plan item 2D.1 (2026-10-23)**
- New in `04_Peoples_and_Cultures/`: `Girlano_Culture.md`, `Sadi_Andali_Culture.md`, `Zartos_Culture.md`, `Dragon_Lands_Culture.md`, `Vitesse_Culture.md`, `Mirror_Kingdom_Culture.md`, `Dreisil_Culture.md`, `Boko_Culture.md`, `Jayapura_Culture.md` and `Ustei_Homeland_Culture.md`. Each is a culture-lens file linking to its place file; where the text says little (Girlano, Sadi Andali, Zartos, Dreisil, the Dragon Lands) the file says so and lists what is not stated.
- Observed: the Mirror Kingdom is "small, affluent and geographically blessed" (Book 2, Ch51 L8) but a Book 13 line puts it "so far north that the ice never thaws" (Book 13, Ch1022 L51); both are recorded in the file. Dreisil is named only in Book 6, Ch47 L390 and L392.

**Thin people files, build plan item 2D.2 (2026-10-23)**
- `Merfolk.md`, `Goblins_and_Fairies.md`, `Runics.md` and `Valash.md` gain further cited facts (runics: civilisation-building species, spellcasters, kinship with smoulders; valash: Zolit Kreen's story; goblins and fairies: Cabal beings in human form). Merfolk stays at one real reference; a scan finds no other.
- New `Lehenik.md` (Nik's kind, Book 11, Ch23 L42 to Book 13, Ch991 L5) and `Messengers_as_a_People.md` (society, hierarchy, names, with a pointer to the 02 file). The messenger-name pattern (Vin, Fin, Fran, Carmis, Ket) is an observation, not a rule stated by the text.

**Clothing, food, festivals and transport by region, build plan item 2D.3 (2026-10-23)**
- New `04_Peoples_and_Cultures/Clothing_Food_Festivals_and_Transport_by_Region.md`: the festivals the text names (Greenstone's flower wine festival, the Rimaros post-surge festival of Book 9, Ch2-4, a Kurdansk parade, a wall-completion feast), then Rimaros, Yaresh, Kurdansk, Pranay and Vitesse entries. It is a selection of the clearest cited lines, not every meal in the series, and says so.
- Not found: names for festivals other than the flower wine festival; recipes by region.

**Education, build plan item 2D.4 (2026-10-23)**
- New `04_Peoples_and_Cultures/Education.md`: the Remore Academy and Geller training, Magic Society research wings and temple libraries, Boko's universities, the Kazlahk University of Medicine (KazMed), the Magical Research Association, the Asano clan's schools, the Asano Academy on Earth and New Water's schools, with cites.
- "Jason's school in Book 13" is taken to be the Asano Academy (Book 13, Ch1016 L106); his Earth schooling is the Casselton Educational Institute (Book 2, Ch11 L37).

**Calendar, holidays and naming customs, build plan item 2D.5 (2026-10-23)**
- New `04_Peoples_and_Cultures/Calendar_Holidays_and_Naming_Customs.md`: the twelve-month calendar, five extra days and six-day week, the "super-simple" day names (only Fifthday and Fourthday appear), Rimaros palindromic names (Book 7, Ch18 L42), mononyms, forms of address with cites. The text names no Pallimustus religious holiday in the lines read; festivals are in `Clothing_Food_Festivals_and_Transport_by_Region.md`.

**Unfiled Name_Index entries, build plan item 2E.1 (2026-10-23)**
- Entries added to the Minor_Cast group files: Books 1-3 (Arash, Dink, Hiram, Ketis, Tabitha Gert, Crivens, Adam Cosgrove), Books 4-6 (Franklin), Books 7-9 (Argrave Mericulato, Haliastur, Dara Rimaros), Books 10-13 (Calcifer Bynes, Jali Corrik Fen, Durrum, Barry Sinise, Brian, Cassie, Daryll, Delia DeWitt, Fiorella, Jamar, Koa, Vandrick Macarro, Ben Headingway). `Mr_North.md` already carries the Noreth alias in its title.
- Corrections noted: the Name_Index calls Arash a juice vendor and Haliastur the Garuda, but the lines read show Arash as a runic man in the temple district and do not link Haliastur to Taika's confluence; the entries say so. Franklin is a peaceful Cabal vampire who regrets not following Vermillion, not a manservant.

**Promotions from grouped entries, build plan item 2E.2 (2026-10-23)**
- Triage by line and chapter counts (a scan of the chapter files), applying the rule of thumb of about 15 cited facts or a role across more than one book. New individual files in `07_Characters/`: `Lorenn.md`, `Jameela.md`, `Beaufort_Builder_Cult_Commander.md`, `Sendira.md`, `Remy.md`, `Kalif.md`, `Hudson_Kettering.md`, `Zareen_Rimaros.md`, `Durrum.md`, `Lorus.md` and `Michael_Mills.md` and `Rosa_Liselos.md` (the scout of Team Storm Shredder). The grouped entries for Beaufort, Durrum, Michael Mills, Sendira and Hudson Kettering were deleted from the group files (their facts are in the new files) and the group files link to them in Related.
- Reviewed and kept grouped (under about 15 facts, or one short scene): Niko, Emily, Laront, Kreegle, Hils Jaramaris, Barstow, Calcifer Bynes (covered with Gormanston_Bynes.md), Jali Corrik Fen, Natala, Hastor (one chapter, 8 lines), Esteban Galo, Valetta and Alice (Moon's Edge, 5 lines), Kurik (7 lines, one chapter), Magdalyn, Wassily and Klaus (covered in The_Cabal.md; 11-13 lines each), Miriam Coyle (1 line) and the Duke of Boko (see House and Boko files). Dara stays in the Rimaros group file with a stub, and Zareen gets a file.

**Re-verification of the 2026-10-22 character files, build plan item 2E.3 (2026-10-23)**
- Ran `cc2.py` over the 32 individual files and the four group files at a raised overlap threshold (0.35 for the flag list: 76 flagged cites; 0.45 for the group files), then compared a further sample of three unflagged cites per file (threshold 0.7) with the chapter text. Every flagged cite was read against its claim.
- Two errors fixed: `Nicolas_Hendren.md` cited Book 3, Ch59 L112 (Belinda's Power Thief) for his force wave, now Book 3, Ch59 L103; `Audrey_Blaine.md` cited Book 13, Ch998 L109 (a description of Gerling) for her research directorship, which Ch992 L116 supports alone.
- Everything else read matched: low overlap scores were paraphrase, not mismatch. The check does not test whether a claim is complete, only whether the cited line supports it.

**Older character files brought up to the template, build plan item 2E.4, first batch (2026-10-24)**
- Revised to the full character template (Appearance, Personality and voice, Powers, Background, Timeline, Relationships, Secrets, Roleplay), with line-cited facts and spoiler tags: `Mr_North.md`, `Emir_Bahadir.md`, `Liara_Rimaros.md`, `Taika.md`, `Gerling.md`, `Erika_Asano.md`, `Jory_Tillman.md`, `Carlos_Quilido.md`, `Arabelle_Remore.md`, `Rick_Geller.md`, `Thadwick_Mercer.md`, `Travis_Noble.md`, `Hiro_Asano.md`. Ordered by first-name mention count; Boris Ket Lundi was skipped.
- Added `src/tools/dossier.py`, which samples narration, appearance and relationship lines per book band with cites.
- Corrections made while writing: Mr North's briefing is Jason telling Anna (Book 13, Ch987 L16); several cites that did not support their clause were removed or split.
- Not done: the remaining stub files, in the order Asya Karadeniz, Allayeth, Melody Jain, Vincent Trenslow, Vincent Baudrillard, Kaito Asano, Nigel Thornton and onward. Recorded as 2E.4b in `TODO_Build_Plan.md`.

**Older character files brought up to the template, build plan item 2E.4b, second batch (2026-10-24)**
- Revised to the full template with line-cited facts: `Asya_Karadeniz.md` (header level raised to 2: she dies in Book 5), `Allayeth.md`, `Melody_Jain.md`, `Kaito_Asano.md` (level raised to 2, Valid through Book 13), `Nigel_Thornton.md` (level raised to 3 for Books 12-13).
- Reviewed and left as they were because the text gives little more: `Vincent_Trenslow.md` (one Book 1 scene run plus two cameos) and `Vincent_Baudrillard.md` (one Book 13 chapter).
- Remaining stubs for 2E.4b start at Marek Nior Vargas, Akari Asano, Soramir, Garth Larosse, Zato, Gabriel Remore, Gabrielle Pellin, Ian Evans, Constance.

**Older character files brought up to the template, build plan item 2E.4b, remaining batches (2026-10-24)**
- Revised to the full character template (Appearance, Personality and voice, Powers, Background, Timeline, Relationships, Secrets, Roleplay), keeping every earlier cited fact and adding line-cited facts read from the chapters: `Akari_Asano.md`, `Marek_Nior_Vargas.md`, `Soramir.md`, `Garth_Larosse.md`, `Zato.md`, `Gabriel_Remore.md`, `Gabrielle_Pellin.md`, `Constance.md`, `Ian_Evans.md`, `Shako.md`, `Elizabeth.md`, `Thalia_Mercer.md`, `Tera_Jun_Casta.md`, `Simon_McKean.md`, `Craig_Vermillion.md`, `Pelli.md`, `Cassandra_Mercer.md`, `Landemere_Vane.md`, `Roland_Remore.md`, `Korinne_Pescos.md`, `Chloe_Baudrillard.md`, `Musin_Heath.md`, `Jeni_Kavaloa.md`, `Greg.md`, `Amy_Asano.md`, `Yumi_Asano.md`, `Itsuki_Tiwari.md`, `Ken_Asano.md`, `Cheryl_Asano.md`, `Charist.md`, `Hana_Shavar.md`, `Keith_Geller.md`, `Elspeth_Arella.md`, `Henrietta_Geller.md`, `Phoebe_Geller.md`, `Clarissa_Ventress.md`, `Cressida_Vane.md`, `Timos.md`, `Adris_Dorgan.md`, `Cole_Silva.md`, `Pochard_Finn.md`, `Lenora_Coleman.md`, `Lucian_Lamprey.md`, `Hassan_Dukhtar.md`, `Jamis_Fran_Muskar.md`, `Gwydion_Remore.md`, `Argy.md`, `Erigo_Fin_Desca.md`, `Hess_Jor_Nasala.md`, `Kasper_Irios.md`, `Miles_Cotezee.md`, `Natalie_Park.md`, `Vincent_Trenslow.md`, `Raythe.md`, `Holly_Macrossan.md`, `Jota_Withers.md`, `Marie_Finnegan.md`, `Trenchant_Moore.md`, `Helsveth.md`, `Gilbert_Bertinelli.md`, `Benella.md`, `Velius.md`, `Zithis_Carrow_Vayel.md`, `Padma_Parsell.md`, `Fal_Vin_Garath.md`, `Marla.md`, `Estella_Warnock.md`, `Jonah_Geller.md`, `Jes_Fin_Kaal.md`, `Marcus_Hargrave_Xenoria.md`, `Audrey_Blaine.md`, `Umber.md`, `Nicolas_Hendren.md`, `Vesta_Carmis_Zell.md`, `Ketevan_Arziani.md`, `Sigrid_Freyn.md`, `Orin_Pensinata.md`, `Killian_Laurent.md`, `Gormanston_Bynes.md`, `Hester_Maharala.md`, `Beth_Cavendish.md`, `Vincent_Baudrillard.md`, `Noriko_Asano.md`, `Lorelei_Grantham.md`, `Anisa_Lasalle.md`, `Li_Li_Mei.md`. Spoiler levels corrected where the header sat below the content (Asya, Kaito, Akari, Nigel and others).
- Fixes found along the way: Akari is Itsuki Tiwari's wife (Book 13, Ch1004), which the two older files had not said; the Network's Keith and Humphrey's father Keith Geller are now told apart; several relationship lines that overstated their cites were reworded.
- Left in their earlier layout because they already hold 6 or more cited facts and the section numbering differs only cosmetically: `Dawn.md`, `Anna_Tilden.md`, `Boris_Ket_Lundi.md`, `Knowledge.md`, and the grouped files `Baseph_and_the_Rimaros_Children.md` and `Hannah_and_Claire_Adeah.md`. The 2E.2 individual files (Lorenn, Remy, Sendira and the rest) and the Minor_Cast group files were already complete.

**Relationship files, build plan item 2E.5 (2026-10-24)**
- Added `07_Characters/Relationships/` with `Family_Trees.md` (Asano and Evans line, Remore, Geller, Mercer circle, Rimaros royal house), `Romances_and_Rivalries.md` (marriages, break-ups, standing rivalries) and `Teams_by_Era.md` (Team Biscuit, Rick's, Beth's, Padma's, Shining Scabbard, Storm Shredder, Moon's Edge, Emir's old team, Nigel's unit). Every link is drawn from a cited line in the character files, with a few re-read in the chapters.
- Not stated in the lines read, and noted as such in the files: how the Japanese Asano patriarch's line connects to Ken and Hiro, any romance between Jason and Farrah, and a full Moon's Edge roster. The Noriko/Yumi "matriarch" overlap stays an open point.

**Character knowledge-state tables, build plan item 2E.6 (2026-10-24)**
- Added `07_Characters/Relationships/Knowledge_States.md`: for eleven core characters, the earliest scene showing them know that Jason is an outworlder, use the party interface, know the Earth link and know Knowledge's plan, grouped in four book bands. The System as a world event (Book 11 end, Book 12) is described separately.
- Method: first evidence, not full proof; blanks mean no scene was found in the lines read. Open points recorded: first-telling scenes for Sophie, Belinda, Neil and Gary, and the team's grasp of the Earth link before Book 9. The Book 13 lecture (Ch1017) is the first scene where Knowledge's plan is laid out to a group.

**Places named only once, build plan item 2F.1 (2026-10-24)**
- Added `06_Places/Minor_Places/Casallini.md` (Girlano's border city, Book 8 ambush on Sophie) and `Lindover_and_Clementson_Properties.md` (the Book 1 fergax land-grab), each linked from its neighbouring file (`Girlano.md`, `Leust.md`).
- Checked against the text and left alone: Oleyu already has its file (`Oleyu.md`, with the river left as an open question, Book 6, Ch47 L838); the Great Southern Continent appears once, in the team's route plan (Book 9, Ch25 L4), with no scene, so no file was added, as the plan instructs.
- Correction in `Cressida_Vane.md`: Jason's remark in Book 1, Ch97 L122 confirms her head was smashed open; the file now says she is killed.

**Region overviews, build plan item 2F.2 (2026-10-24)**
- Added `06_Places/Regions/` with `Africa_like_Continent.md` (Greenstone, Hornis, Boko, Rakesh, Oleyu, Zartos, Sadi Andali, Leust; the Great Southern Continent noted as one route mention), `Estercost_Continent.md` (Cyrion, Vitesse, Kazlahk, links to Greenstone, Rakesh and Dreisil) and `Storm_Kingdom_Islands.md` (the three public islands, Jaitari, Palisaros, Girlano and Casallini on its southern border). Each gathers facts the place files already cite and lists open questions.
- Left unplaced and recorded as open: which continent Zartos, Sadi Andali, Cartise and Arcazitlan lie on; whether Dreisil is on Estercost's continent.

**Jason's domains, build plan item 2F.3 (2026-10-24)**
- Added `06_Places/Domains.md`: the rules for Jason's domains in one place (made of set-state authority, claiming by zone, perception inside, sin afflictions, gods unable to spy, portal tracking, divine-ground and temple rules from Book 13) with a table pointing to each domain's place file. Drawn from passages in Books 6, 8, 9, 11, 12 and 13, cross-linked to `Authority_and_Sanctioning.md` and `Transformation_Zones.md`.

**Locations by era, build plan item 2F.4 (2026-10-24)**
- Added `06_Places/Locations_by_Era.md`: for the places that change (Greenstone, Boko, Cartise, Yaresh and Cardinas, Rimaros, the Earth sites, Estercost and a few others), their state in each of the seven eras from `Era_Selection.md`, with cites drawn from the place files. Open: whether other Era 1-2 places changed state by Era 7, and the timing of Cartise's fall.

**Vitesse magic density, build plan item 2F.5 (2026-10-24)**
- Searched the chapter text for Vitesse's density and found a rank band rather than a figure: typical monsters silver, as many golds as bronzes, occasional diamonds (Book 1, Ch30 L43-44); surge precursors show as gold-rank increases (Book 3, Ch26 L13); no adventurer below silver operates unsupervised (Book 12, Ch43 L68). Updated `Vitesse.md`, `00_Places_Overview.md`, `Regions/Estercost_Continent.md` and Open_Questions item 13 (narrowed, not closed). The wiki-only claim in the overview was replaced by the book evidence.

**Items, build plan item 2G (2026-10-24)**
- Added `09_Items_and_Artefacts/Jasons_Combat_Robes.md` (Trap Weaver Battle Robe and the Dark Hydra Robe), `Soul_Forge.md` and `Reality_and_Genesis_Cores.md`. Added "the Rejector" to `03_Magic_and_Adventuring/Titles_and_Blessings.md` as a name given by enemies.
- Checked and found already covered elsewhere, so no new file: the Firmamental Bridge Anchor and bridge anchors (`Tokens_Stones_and_Relics.md`, `The_Builders_Door_and_Fundament_Gate.md`); the clockwork kings (`Monsters.md`, `Cults_and_Orders.md`); Rexion's citadel (`Spirit_Vault_and_Astral_Kingdom.md`); artefact-site weapons (`Earth/Artefact_Site_One.md`). Avatars of doom are familiars, covered under `Familiars.md`.

**Era guides, build plan item 3.1 (2026-10-24)**
- Added `08_History_and_Timeline/Era_Guides/` with eight guides: `Builder_Cult_in_Greenstone.md`, `Reaper_Trials.md`, `Earth_and_the_Monster_Waves.md`, `Rimaros_Surge.md`, `Battle_of_Yaresh.md`, `Cardinas_Expedition_and_Zone.md`, `Earth_Vampire_War.md` and `The_Return_and_the_Bridge.md`. Each gives the summary, the world at the start, key events with cites, who is where, what is known and unknown and the spoiler level, assembled from the per-book timelines and the character, place and item files.
- Length is shorter than the plan's 3-6 pages (about 600-1,000 words each); they are meant as starting points and link to the timelines for detail.
- Open: the era guides do not repeat plot hooks; hooks stay in `Plot_Hooks.md` (item 4.3).

**War and crisis files, build plan item 3.2 (2026-10-24)**
- Added `08_History_and_Timeline/Crises/` with `One_Day_War.md` (the War of Four Cities, Book 7), `Boko_Evacuation.md` (Book 12), `Messenger_War.md` (Books 7-13) and `Vampire_War.md` (collects the duration statements behind Open_Questions item 19 and points to the era guide). The Battle of Yaresh is covered by `Era_Guides/Battle_of_Yaresh.md` and the Messenger War file; no separate crisis file was written for it.
- Open: casualty numbers for the One Day War and Boko; the first vampire war's length.

**Master Timeline version 2, build plan item 3.3 (2026-10-24)**
- Extended `08_History_and_Timeline/Master_Timeline.md` with four new sections instead of rewriting it, since the existing sections 1-7 already held the verified anchors: section 8 (month-count summary by book), section 9 (rank and level checkpoints for core characters, each with the first cited line), section 10 (the Book 11 Part II clock) and section 11 (corrections recorded in later passes).
- Decision recorded in section 10: a working convention (editorial, not a book statement) places Jason's void departure in late 2023 and runs the Earth-side threads from Rufus and Taika's arrival; Emi's "fifteen" is treated as the outlier. The void threads stay on their own clock. Open_Questions is unchanged.

**Rank and progression tracks, build plan item 3.4 (2026-10-24)**
- Added `03_Magic_and_Adventuring/Progression_Tracks.md`: the first line for each of Jason's four essences, his twenty abilities, his rank steps and other major gains, and a table for Sophie, Belinda, Clive and a few others. Sanguine Horror, Haemorrhage, Castigate, Punition and Verdict are given as "first shown" because the awakening message was not found. Gold rank is dated only by the later report of a day of golden light.
- Gary, Rufus, Farrah, Taika, Humphrey and Neil's full tracks are not in this file; their character files hold what is known.

**Who-knows-what-when matrix, build plan item 3.5 (2026-10-24)**
- Added `10_Roleplay_Support/Who_Knows_What_When.md`: seven secrets (Jason an outworlder, Jason an astral king, the Order's survival, the Builder's identity and plan, the Network founder and the door, the System and Knowledge's plan, Jason's deaths) against groups of people, with the earliest cited scene and a book band for each. Linked from `Spoiler_Management.md`. It complements the per-character tables in `Relationships/Knowledge_States.md`.
- Dashes mark cells where no scene was found.

**Chapter digest, build plan item 3.6, first pass (2026-10-24)**
- Added `src/tools/chapter_digest.py` and the thirteen files `08_History_and_Timeline/Chapter_Digest_Book_01.md` to `Chapter_Digest_Book_13.md`. Each lists every chapter (987 in all) with its cleaned title and up to two sentences from the per-book timeline whose own citation names that chapter; sentences with long quotations are skipped, so no passages are reproduced. About 917 of 987 chapters have a summary sentence; the other 70 are marked "title only".
- Two timeline rows the register flagged weak (Book 12, Ch65; Book 13, Ch951) are skipped by the generator until those rows are tightened.
- Remaining work, recorded as item 3.6b in the plan: write summary sentences for the title-only chapters by reading them, and add a second sentence where only one exists.

**Recurring motifs and in-world sayings, build plan item 3.7 (2026-10-24)**
- Added `10_Roleplay_Support/Motifs_and_Sayings.md`: "Feed me your sins" with the chapters where it recurs, the biscuits, Handsome Doctor, pants, Clive's non-existent wife, sausage sizzle, chuunibyou and Captain Tremendous gags, and the Star Wars, Mario Kart and other pop-culture references, each with cites and no reproduced passages. Cross-linked from the voice notes' purpose; open question: Jason's other casting phrases.

**Chapter digest gaps filled, build plan item 3.6b (2026-10-24)**
- Read a sample of lines from each of the 70 title-only chapters and added a cited one- or two-sentence summary for each, held in `src/tools/digest_fill.py` and written as an "Additional chapter rows" section at the end of the matching `Book_NN_Timeline.md` (Books 1-11 and 13). All 987 chapters now have a digest entry.
- These sentences come from a sample of each chapter's lines, not a full read, so they are less complete than the older timeline rows; a few register rows are marked "near". The Book 12 Ch65 and Book 13 Ch951 original rows are still to be tightened.

**Era starter packs, build plan item 4.1 (2026-10-24)**
- Added `10_Roleplay_Support/Starter_Packs/` with seven packs, one per era in `Era_Selection.md`: Greenstone, Bronze and the Builder, Earth, Rimaros, Yaresh, Cardinas and the Return. Each has the setting, three starting situations drawn from `Plot_Hooks.md`, a cast list with voice cues, live dangers, what the characters know (from the knowledge tables), spoiler-safe narrator language and what to leave closed. All facts come from earlier cited files; no new book reading was done.

**NPC cards, build plan item 4.2 (2026-10-24)**
- Added `src/tools/npc_cards.py` and four files in `10_Roleplay_Support/NPC_Cards/` (Books 1-3, 4-6, 7-9, 10-13 by first appearance) with 138 cards: role, appearance, voice cue, secret or spoiler note and valid-from/through, copied with citations from the individual character files. Group files (Familiars, Baseph and the Rimaros children, Hannah and Claire) and Jason are not carded.
- The generator exposed three character-file lines whose cites did not support their wording (Elizabeth, Itsuki Tiwari, Korinne Pescos); they were reworded. The "goal" field in the plan has no source field in the character files, so the cards give role instead.

**Plot hooks expanded, build plan item 4.3 (2026-10-24)**
- `10_Roleplay_Support/Plot_Hooks.md` already held four to six hooks per era, so the expansion added a fifth hook for Era 6 (the echo array, Book 10, Ch72 L58) and a new section 3: per era, the fixed points the books establish (each cited) and two or three branching directions for every hook, marked as table-top suggestions and not book facts. The old "Using this in a story" section is now section 4.

**Secrets and rumours by era, build plan item 4.4 (2026-10-24)**
- Added `10_Roleplay_Support/Secrets_and_Rumours.md`: for each of the seven eras, a table of true facts, common beliefs and cover stories or rumours, each with a cited line. Level 3 header because Era 7 truths reach Book 13. Items the books did not support cleanly (Zara's public claim) were left out; open question noted for further Jason rumours.

**Spoiler-safe summaries, build plan item 4.5 (2026-10-24)**
- Added `10_Roleplay_Support/Spoiler_Safe_Summaries/` with one page per spoiler level (Level_0_Public_Setting, Level_1_Books_1-3, Level_2_Books_4-9, Level_3_Books_10-13). Each page uses only facts at or below its level, with cites already used elsewhere, and ends with a "Do not state" list. Linked from `Spoiler_Management.md`.

**Quick-reference sheets, build plan item 4.6 (2026-10-24)**
- Added `10_Roleplay_Support/Quick_Reference/` with five one-page sheets: Ranks_and_Lifespans, Coin_Table, Forms_of_Address, Calendar_and_Festivals and Churches_at_a_Glance. Each repeats lines already cited in the topic files; the coin table derives the lesser-coin values from the quoted ratios. Linked from `Tone_and_Voice.md`.

**Place changes between eras, build plan item 4.7 (2026-10-24)**
- Added `10_Roleplay_Support/Place_Changes_Between_Eras.md`: before-and-after tables for Greenstone (with Boko), Vitesse, Rimaros and Yaresh, each row keyed to a period and a cited line. Rows the books do not cover (Greenstone in Eras 3-6) say so. Linked from `Era_Selection.md`.

**Second verification pass begun, build plan item 5.1 (2026-10-24)**
- Added `src/tools/verify2.py`, an independent check of every register row (quoted text and numbers against the cited lines, with a closest-span suggestion). First run: 9,252 rows checked, 487 flagged, 347 after the first fixes; roughly 100 of the rest are benign (quote split by a speech tag) and the timelines' numbers are chapter numbers or derived figures.
- Fixed 20 claims whose quotation marks surrounded a paraphrase or a wrong line: Anisa Lasalle, Carlos Quilido, Emir Bahadir, Gary, Dawn, Taika, Farrah Hurin (and her power set), Zara Rimaros, Hiro Asano, Jason Asano, Gerling, Estella Warnock, Jes Fin Kaal, Hannah and Claire Adeah, Thadwick Mercer, Remy and Church of Purity. NPC cards regenerated.
- Still open under 5.1: the remaining flagged rows in `src/tools/verify2_report.md` (about 245 after filtering benign ones, 104 of them in `08_History_and_Timeline`, mostly line-reference drift), and the manual reading pass by section.

**Second verification pass, second batch, build plan item 5.1 (2026-10-24)**
- `src/tools/verify2.py` refined (compound number words, ability-block window, timeline labels and appendix bookkeeping no longer flagged). Flags fell from 347 to 185; the rest are quotes split by a speech tag, derived figures (ages, month counts) and numbers given in words, each checked by sample.
- Fixed about 45 more claims: quotation marks around paraphrases or inexact wording (timelines and digests: Thadwick, Order "make connections", Voices of the Will, Clive's bronze message, Gerling, the Builder fortress-city; Magic: soul-bound items, undeath confluences, auras, Dawn's link account, coin colour, skill books; Cosmology, organisations and places: Purity council wording, House Rimaros hair, Order cleansing fire, "dragon mouth"), wrong or missing line references (twelve towers, Nik's age, Hiro, Zara, Sophie's debt age, Humphrey's age, the 119 outworlders, Starlight Angel, artefact site workers) and one factual slip: Keane says iron-rankers, not bronze, may not hunt alone in high-magic areas (Motifs_and_Sayings).
- Status: automated pass complete across all 9,251 book-cited rows; the section-by-section reading pass in the plan (07, 06, 03, 08, 05, 02, 04, 09, 10, 01) is still to do, now with a shorter queue.

**Manual reading pass on 07_Characters, build plan item 5.1 (2026-10-25)**
- Added `src/tools/near_dump.py` (prints near-graded register rows with the cited lines). Read all 174 near rows of `07_Characters` against the chapter text. 166 were supported (the overlap grade was low because the claim summarises a longer passage). Eight were corrected: Audrey Blaine ("now her employer" was unsupported; the line shows Jason introducing her to the team), Liara Rimaros ("short leash" was unsupported), Marie Finnegan ("captor" was not in the line), Rick Geller (Jonah is called his friend in the line, so "cousin" became "teammate"), and the Voice cues of Zara Rimaros and Knowledge, which held only a citation and now hold a quotation. NPC cards regenerated.
- Next in the 5.1 order: 06_Places, 03, 08, 05, 02, 04, 09, 10, 01.

**Manual reading pass on 06, 03, 08, 05, 02, 04, 09 and 01, build plan item 5.1 (2026-10-25)**
- Read the near-graded rows of 06_Places (21), 03_Magic_and_Adventuring (85), 08_History_and_Timeline (106), 05_Organisations (14), 02_Cosmology_and_Powers (20), 04_Peoples_and_Cultures (11), 09_Items_and_Artefacts (1) and 01_World_Primer (9) against the chapter text. Almost all were supported. Corrections: House Geller (the garden tower is in Vitesse and the fortified estate outside Cyrion; the old line swapped places and cities), Cyrion (the continental-council seat now cites both Book 7 and the Vitesse line), Vampire War (old vampires wake from reality-core blood, not from transformation events), Rimaros Surge (Ledev and Vesper's deaths cite Ch66 L36), and The Unorthodoxy (Erigo admits he was once part of it and has moved on).
- Not read line by line: the near rows in 10_Roleplay_Support outside the NPC cards (written from already-cited lines this month) and 13 in Appendices (bookkeeping counts). 5.1 is otherwise complete; the register has no weak rows and `verify2.py` leaves only benign flags.

**Source_Map section 6 spot-check, build plan item 5.2 (2026-10-25)**
- Found that the state-change list in `Appendices/Source_Map.md` section 6 had been empty since build plan item 1.3: four word-boundary escapes in `src/tools/build_register.py` (the keyword pattern and the book-name check) had been saved as backspace characters, so the pattern never matched. Restored them; the list now holds 189 entries (24 register rows were re-parsed with the corrected book-name check, none changed grade).
- Spot-checked 25 entries across Books 1-13 against the cited lines: all 25 citations support their claims; about five are not state changes (rules or descriptions that contain a keyword), which the section's introduction now says.

**Wiki list matcher improved and list moved, build plan item 5.3 (2026-10-25)**
- `src/tools/wiki_lists.py` now reads the chapter files once and matches "<name> essence", "<name> confluence", "essence of <name>" (essences and confluences) and "stone(s) of <name>" (stones); the stone table also had its book column left blank by a bug, now filled. Cross-references in `Wiki_Reference_Lists.md` rose from 90 to 129 (essences 67, confluences 34, stones 28). The wiki cache itself was not refreshed (no new fetch); rerun `fetchwiki.py`, `wiki_lists.py` and `compose_wiki.py` when it is.
- Moved `03_Magic_and_Adventuring/Wiki_Reference_Lists.md` to `Appendices/Wiki_Reference_Lists.md` (Decision 4). `compose_wiki.py` writes the new path and its Related line uses `../` paths; the links in `00_Magic_Overview.md`, `Essence_Catalogue.md`, `Monsters.md` and `src/tools/README.md` were updated. Earlier Change_Log entries keep the old path as history. The Glossary and `Gods_and_Churches.md` held no link to the file.
- Not done: a spelling check against `Name_Index.md` for wiki names the books spell differently.

**Lorebook derived from the compendium, build plan item 5.4 (2026-10-25)**
- Added `src/tools/lorebook.py` and `src/exports/lorebook/` with four world-info files, one per spoiler level (64, 136, 212 and 348 entries). Each entry is a compendium document's Summary plus fact bullets, citations removed, tagged sections above the file's level cut. The earlier hand-made lorebook stays in `src/tools/archive/` and was not used.
- The summaries of some documents mention later events without a level tag (for example Boko, Jason Asano, the All-Devouring Eye). The generator holds back sentences that name a later book or a listed later-level term and writes them to `held_back.txt` (48, 87 and 75 sentences for levels 0-2). Those documents should get level tags; not done here.
- `src/exports/README.md` explains the files and their limits.

**Spoiler-level exports, build plan item 5.5 (2026-10-25)**
- Added `src/tools/export_levels.py` and `src/exports/markdown/` with four Markdown files (levels 0 to 3: 70, 147, 230 and 379 documents, 0.2 to 1.4 MB). Rule from Decision 3: keep a document when its header level is at or below the requested level, cut tagged sections above it, then hold back lines that cite a later book or name a later-level term (638, 827 and 549 lines for levels 0 to 2, listed in `held_back.txt`). Markdown only: no PDF tool is installed.
- Leak check on the lower files: no hits for Zithis, Cosmic Throne, Sundered, System Administrator, Network founder, astral king or transformation zone below level 2, and none for the level 3 terms at level 2. The keyword list is a safety net, not a proof.

**Link and anchor checks, build plan item 5.6 (2026-10-25)**
- `src/tools/lint.py` gained two checks: an error when a Markdown link `[text](path.md#anchor)` points to a missing file or a heading that does not exist (GitHub-style anchors), and a warning when a backticked `Name.md` matches no file in the compendium or `src` (placeholders such as `Book_NN_Timeline.md` are skipped). The linter already checked the Related line, cites and tags; this closes the body-link gap.
- First run over all 425 documents: 618 body links, none broken, and no stale backticked names. A temporary file with a bad link, a bad anchor and a missing name produced the expected two errors and one warning. The linter runs at the end of every `build_register.py`, which is the CI-style entry point.

**Redundancy audit, build plan item 5.7 (2026-10-26)**
- Added `src/tools/redundancy_report.py` (writes `src/tools/redundancy_report.md`): 193 clusters where three or more documents cite the same book line. Most are deliberate (folder overviews, power sets, derived sheets, character and place files that each tell their part), so the report is a triage list.
- Settled the three examples named in the plan and four more, and recorded the homes in a new Glossary table ("Home files for repeated facts"): the calendar (Calendar_Holidays_and_Naming_Customs.md), coin values (Economy_and_Money.md), the Network's founding (The_Network.md, new section 6), ranks and lifespans, spoiler secrets, the gods list and the wiki lists.
- Repeats replaced by pointers: the calendar sentences in `Daily_Life.md` and `01_World_Primer.md` (and a pointer added in `Master_Timeline.md`, which keeps its dated convention), and the long "Origins" bullet in `Earth_Powers.md`, whose text moved to `The_Network.md` section 6 with the Book 13 part under a level-3 tag (the bullet had mixed Book 4 and Book 13 facts under a lower header level). Coin values were already told once; the timelines cite chapters and stay.
- Not done: the other clusters. Candidates worth a later look are the church lines repeated across Gods_and_Churches, the church files and Religion_in_Practice, and the Vitesse and Greenstone descriptions repeated across the Places and Peoples files.

**Change log housekeeping, build plan item 5.8 (2026-10-26)**
- Moved the entries of 2026-10-20 to 2026-10-22 (424 lines, wording unchanged) to `Appendices/Change_Log_2026-10-20_to_22.md`; `Change_Log.md` fell from 693 to about 280 lines and keeps a pointer. The plan asked for one file per month keeping the last two, but the whole project so far lies inside October 2026, so that rule alone would have moved nothing; the first three days were archived by hand and rule 6 of "How this log works" records it.
- Added `src/tools/log_archive.py`, which applies the monthly rule from now on: entries dated before the previous month move to `Change_Log_YYYY-MM.md` (dry run with `--dry`, test date with `--today`). `build_register.py` and `lint.py` skip all `Appendices/Change_Log*.md` files (the archive's old cites had briefly entered the register). Dry runs for 2026-11-10 and 2026-12-05 behave as intended (nothing moves, then all 59 entries move).

**Style and accessibility pass, build plan item 5.9 (2026-10-26)**
- Added `src/tools/style_check.py` (writes `src/tools/style_report.md`): note shorthand and abbreviations (e.g., i.e., etc., vs, cf., approx, "&", "~", "w/", arrows, TBD), the character heading template (a full nine-section form or a short Summary, Facts, Roleplay notes form), variant spellings used without a note, skipped heading levels, and tables without a header row. The testable parts of section 7 of the structure guide; past tense for history and "name everyone in full once" need a reader and were not checked.
- First run: 13 shorthand hits, 22 character files outside both templates, 5 unnoted variants, no heading or table problems. Fixed: "e.g." (Primer, Glossary) and "~" (Book 1 timeline day ranges) reworded; Hedron noted as the line's spelling in `Purity_and_Disguise.md`; Anna Tilden, Boris Ket Lundi and Knowledge converted to the full template (existing content moved, thin sections say what the lines show or that nothing is recorded); Dawn gained a Background section, Zara Rimaros a Secrets section (level-3 tag), and the Jason Asano timeline heading lost "(summary)". The 19 short-form character files are now an accepted second template (Summary, Facts, Roleplay notes), as are group files such as `Familiars.md`. Final run: 0 hits in every category. Chapter-title ampersands and the documented variant notes are exempt.
- Place files keep their varied section names (Society and rule, Hooks, Dangers and hooks and so on); only the checks above apply to them.

**Text maps and distance tables, build plan item 6.1 (2026-10-26)**
- Added `06_Places/Text_Maps_and_Distances.md`: for Greenstone, Vitesse, Rimaros and Yaresh, a schematic text map and a table of stated distances. The books give almost no distances (Greenstone: two days plus a couple of days by boat, and the hundred-kilometre and hundreds-of-kilometres figures from the Builder's astral space; Vitesse: none; Rimaros: 120 km from Jason's cloud house on Arnote to the palace above Livaros, and four months to Yaresh; Yaresh: a dozen kilometres across the city, ten kilometres to a fight, hours to the camps, two hours to the array chamber), so most rows say "none stated". Diagrams carry no figures. Cardinas and Rexion are under a level-3 tag.

**Quote bank, build plan item 6.2 (2026-10-27)**
- Added `10_Roleplay_Support/Quote_Bank.md`: 22 short quotations (all under fifteen words, longest twelve) for 19 speakers, each with the trait it shows and its line, drawn only from lines `Tone_and_Voice.md` already cites. Checked with `verify2.py`: one benign flag, a line split by a speech tag. Speakers the voice notes describe without a short quotable line (Gary's growl, Neil, Humphrey) are left to their character files, and the file says so.

## Pending index updates

Names and terms from the Places and Magic documents that are still missing from the Glossary or Name Index (add when next touching those files): Argy (Palisaros resident), Hester (Emir's portaler, first named Book 1), Jacinta Adeline (already indexed; check spelling), Keane (Rimaros adventurer), Casallini (Girlano border city), the Ustei (nomad tribe; Book 1), Medallion of Escape, Summoner's Die: Form, Immortal Crest, Spirit Vault (as a term), Sky Link Company, Stable and Unstable Genesis Cores (partly under *Genesis core*).

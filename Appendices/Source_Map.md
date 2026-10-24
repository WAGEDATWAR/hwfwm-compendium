# Source Map

Status: Draft (sections 1 to 3 and 7 are written by hand; sections 4 to 6 are regenerated from the compendium by `build_register.py` so they always match the documents)
Spoiler level: 3
Valid from: Book 1
Valid through: Book 13
Sources: `src/Source_Text/` chapter files; `Source_Register.md`
Related: Source_Register.md, ../src/Source_Text/README.md, ../08_History_and_Timeline/Master_Timeline.md, ../00_Project_Structure.md

## 1. Purpose

The Source Map ties compendium claims to book, chapter and lines so that facts can be traced, narrowed and re-checked. Where the Source Register is organised by document, the map is organised by the story: sections 4 to 6 run in book, chapter and line order, which is story order.

## 2. How the pieces fit

- `src/Source_Text/Book_NN/Ch_NNN_Title.txt`: the book text, one file per chapter.
- `Appendices/Source_Register.md`: one row per cited claim in the compendium, graded for how well the cited lines support it.
- This file: the rules, the timeline thread (section 4), the chapter index (section 5), the state-change list (section 6) and the log of source-checking work (section 7).
- The register and sections 4 to 6 are regenerated together by `src/tools/build_register.py`; run it after editing any document.

## 3. Rules

1. Reference format: `B7 Ch31 L12-15` (book, chapter, lines of the chapter file). In documents the form is `(Book 7, Ch31 L12-15)`.
2. Hierarchy stays Book Files > Chapter Summaries > Wiki. A claim tagged `notes` or `wiki` should be narrowed to a book location when possible and retagged `Book N`.
3. Grades are heuristic (see the Check column key in the register). Rows graded **weak** are the review queue; **reviewed** rows were read by a person.
4. If lines do not support a claim, correct the document and log the correction in `Change_Log.md`.
5. When a document is added, renamed or removed, rebuild the register. Do not edit the generated tables by hand.

## 4. Timeline thread

Dated or ordered facts and intervals that fix the calendar, in story order by first reference. The per-book timelines in `08_History_and_Timeline/` use these anchors; the Master Timeline summarises them.

| Event | Date or interval | Reference | Check |
|---|---|---|---|
| Pallimustus calendar: twelve months of thirty days plus five extra days | calendar | B1 Ch22 L19 | verified |
| Jason's age at arrival | 23 | B1 Ch25 L43; B13 Ch950 L29 ("the age Jason had been when he was pulled into Pallimustus") | verified |
| Monster surge every ten years; current surge "some five years overdue" | 10 / 5 years | B1 Ch31 L71; B7 Ch1 L56 | verified |
| Summer moving into autumn before the Leust conspiracy | about Feb-Mar 2018 | B1 Ch93 L5 | verified |
| 419 time-displaced priests released | M5 | B2 Ch63 L9 | verified |
| Winter in Greenstone at the start of Book 3 | southern winter 2018 | B3 Ch1 L14 | verified |
| Reaper-trial space: twelve towers, eight kilometres apart | M12 (wiki) | B3 Ch36 L36 | verified |
| Jason leaves Earth / returns | late November; early June, "a year and a half later" | B4 Ch3 L112 | verified |
| EOA seized Perth and Melbourne | before B4 | B4 Ch9 L76 | verified (Sydney: still to locate) |
| Dimensional spaces last forty-three hours (record fifty-one) | baseline | B4 Ch37 L70; B4 Ch5 L127 | verified |
| Fortress found 1948, grid sector offline about seventy years | before Book 4 | B4 Ch51 L30, L37 | verified |
| Grid blackouts still localised at Book 5's start; wide-scale loss expected in "two more months" | about March 2020 | B5 Ch3 L8-19 | verified |
| Book 5 opens about nine months after the return; bronze "for a year"; iron to bronze "a year and a quarter" | about March 2020 | B5 Ch3 L170, L212 | verified |
| Asano Village built in about six months (bushland "six months ago") | before Book 5 opens | B5 Ch5 L59, L104 | verified |
| Walkabout: Jason "ran away from his family for six months" | about M22-M28 | B5 Ch8 L5 | verified |
| Network partnerships with governments "over the last few years" before the monster waves | before spring 2020 | B5 Ch13 L37 | verified |
| Network publicly known as the Global Defense Network "in the weeks since the monster waves began" | spring 2020 | B5 Ch17 L7 | verified |
| Broken Hill: estimated ten to fifteen thousand dead; over nineteen thousand survivors | spring 2020 | B5 Ch18 L83; B5 Ch21 L101 | verified |
| Jason's birthday | 1 April ("April Fool's Day"); just turned 26, birthday "last week" | B5 Ch20 L24-26 | verified |
| "You come back ten months ago" | Jeremy, about April 2020 | B5 Ch24 L61 | verified |
| Makassar: one and a half million people, category-three space | after the birthday | B5 Ch25 L82 | verified |
| "Butterflies of Makassar" news name | after Makassar | B5 Ch32 L4 | verified |
| Kostroma sealed in a dome (first transformation zone) | Book 5 | B5 Ch44 L48-49 | verified |
| Dimensional ulceration named by Dawn | end of Book 5 | B5 Ch68 L30 | verified |
| Shako kills Jason (fourth death); Dawn cites the broken compact | Book 6 | B6 Ch18 L6 | verified |
| One month since the Nitra dome came down | Book 6 | B6 Ch23 L3 | verified |
| Cold winter day in Europe (atomic device) | Book 6 | B6 Ch31 L4 | verified |
| Shako and Chen place the device in the Saint-Étienne aperture | Book 6 winter | B6 Ch35 L80 | verified |
| Farewell in France on a warm autumn day | autumn 2021 by anchors | B6 Ch47 L155 | verified |
| Church of Death certificate "died four times. So far." | Book 7 | B7 Ch17 L104 | verified |
| Outworlders appear naked and hairless in craters | Book 7 | B7 Ch33 L114 | verified |
| 119 outworlders arrive at once | Book 7 | B7 Ch36 L86 | verified |
| "It had been a month since" the One Day War | after the war | B7 Ch66 L27 | verified |
| Jason's age in Book 10 | 29 | B10 Ch33 L76 | verified |
| Zone duration: "next few months, maybe as much as a year"; shaft tamed "months after" | Cardinas zone | B11 Ch48 L22; B11 Ch60 L3 | verified |
| "Rumble in the Jungle" is the song name | Book 11 | B11 Ch68 L173-175 | verified |
| Messengers "only months old" appear over the stone circle on Earth | M74 | B11 Ch68 L469-473 | verified |
| Gary "almost a year later" a haggard figure | after the Cardinas zone | B11 Ch68 L703 | verified |
| Magic unknown "less than fifteen years ago"; Jason absent "sixteen years" | about 15-16 years | B12 Ch2 L107; B13 Ch972 L51, L61 | verified |
| Priests freed "around twenty years ago"; "almost twenty years" | Book 12 | B12 Ch7 L78; B12 Ch13 L36 | verified |
| Ustei came south "three years, give or take" before the Earthlings | about 2018 vs 2021 | B12 Ch30 L9 | verified |
| 74 Earthlings to return, about thirty not | about 2037 | B12 Ch53 L57 | verified |
| Cosmic Throne restored | Books 12-13 | B12 Ch63 L9; B13 Ch1019 L46 | verified |
| Jason born on Earth forty-four years before the Book 12 scenes; no fighter twenty years ago | 44 / 20 years | B12 Ch67 L113 | verified |
| Book 13 year | 2038 ("in 2038") | B13 Ch951 L50 | verified |
| Transformation-zone events "like those in 2020" | 2020 | B13 Ch964 L41 | verified |
| Vampire war "back in full swing"; "off and on for decades"; ended "these last few months" | Book 13 | B13 Ch988 L26; B13 Ch1002 L69; B13 Ch1023 L12 | verified |
| Magitech Institute "last two years"; no McKean trace for "more than four years" | Book 13 | B13 Ch995 L14; B13 Ch998 L105 | verified |
| Earth and Pallimustus time synchronised | | B11 Ch63 L80 | verified |
| Shade reaches silver "almost two months" before Broken Hill | | B5 Ch18 L22 | verified |

Note: "Rules of Intrusion" is the Book 12 wording (B12 Ch63 L5, L7, L45); Book 13 says "Laws of Intrusion" (B13 Ch987 L38, Ch1017 L44, Ch1020 L98). Documents should use "Rules" and mention "Laws" as the Book 13 variant.

## 5. Chapter index

Every chapter the compendium cites, with the documents that cite it and the lines they use. Documents are abbreviated to the file name; the full path is in the register.

### Book 1

| Chapter | Title | Cited by (lines) | Rows |
|---|---|---|---|
| Ch1 | Strange Business | Book_01_Timeline L3, L11, L16, L23, L103; Chapter_Digest_Book_01 L3, L11, L23; Jason_Asano L8-10, L76-81, L108; Motifs_and_Sayings L19; 01_World_Primer L23, L65; Unusual_and_Unique_Magic L37-43, L82-89, L93, L96-99; World_Phoenix L86; Cheryl_Asano L88 … | 27 |
| Ch2 | Of Course Magic is a Thing | Book_01_Timeline L7, L13, L43, L62; Chapter_Digest_Book_01 L7, L13, L43, L62; Monster_Cores_and_Training L32; 01_World_Primer L50-53; Monsters L57, L70 | 12 |
| Ch3 | Local Cuisine | Book_01_Timeline L8, L17, L41-45; Chapter_Digest_Book_01 L8, L17, L41-45; Motifs_and_Sayings L13-18; Elves L43 | 8 |
| Ch4 | Cannibals and Spelunking | Book_01_Timeline L3, L45; Chapter_Digest_Book_01 L3, L45; Goblins_and_Fairies L26; Awakening_Stones L40; Awakening_Stones L44 | 7 |
| Ch5 | Wizard | Book_01_Timeline L22, L26-27, L54; Chapter_Digest_Book_01 L22, L54 | 5 |
| Ch6 | Potent Potable | Book_01_Timeline L3-6; Chapter_Digest_Book_01 L3-6; 01_World_Primer L15, L50; Alchemy_Artifice_and_Magical_Materials L46, L53-54, L54 | 7 |
| Ch7 | Spoils | Alchemy_Artifice_and_Magical_Materials L17-21, L68; Soul_Bound_Items_and_Regalia L17-21; Alchemy_Association L25; Jason_Asano L26; Book_01_Timeline L38; Chapter_Digest_Book_01 L38; Skill_Books_and_Learning L41-43, L46, L50-51, L55-58, L60; 01_World_Primer L68 … | 14 |
| Ch8 | Dark Magic | Progression_Tracks L32, L35, L57; Book_01_Timeline L32, L35, L59; Chapter_Digest_Book_01 L32, L35, L59; Abilities_and_Attributes L34, L35, L62; Awakening_Stones L35, L51-57; Jason_Asano L35, L37; Jason_Power_Set_Reference L62; Skill_Books_and_Learning L88-93 | 18 |
| Ch9 | Escape | Calendar_Holidays_and_Naming_Customs L28, L53; Cressida_Vane L47, L47-50, L47-54, L54; Book_01_Timeline L47; Chapter_Digest_Book_01 L47; Landemere_Vane L47-50, L47-54, L54; Era_Selection L50; Era_1_Greenstone L50, L121; Gary L121 … | 18 |
| Ch10 | The Evil Pit of Evil | Book_01_Timeline L23; Chapter_Digest_Book_01 L23; Skill_Books_and_Learning L38 | 3 |
| Ch11 | Dashing Heroics | Gary L4-6; Awakening_Stones L17, L17-20; Rufus_Remore L49, L51; NPC_Rosters_by_Era L49; NPC_Cards_Books_01-03 L49, L65; Book_01_Timeline L64, L80, L91-92; Chapter_Digest_Book_01 L64, L80, L91-92; Cressida_Vane L65, L65-83, L80, L81-83 … | 22 |
| Ch12 | Sanguine Horror | Farrah_Hurin L11; NPC_Rosters_by_Era L11; NPC_Cards_Books_01-03 L11; Skill_Books_and_Learning L15; Monsters L70; Book_01_Timeline L72; Chapter_Digest_Book_01 L72 | 7 |
| Ch13 | This is the Part Where We Step Back | Minor_Cast_Books_1-3 L3; Glossary L3; Landemere_Vane L13; Cressida_Vane L55; NPC_Cards_Books_01-03 L55; Book_01_Timeline L90, L107; Chapter_Digest_Book_01 L90, L107 | 9 |
| Ch14 | Worlds Apart | Book_01_Timeline L3-7, L35; Chapter_Digest_Book_01 L3-7, L35; Leonids L14; Gary L14; NPC_Rosters_by_Era L14; NPC_Cards_Books_01-03 L14; Cressida_Vane L17; Minor_Cast_Books_1-3 L18 | 10 |
| Ch15 | Outworlder | Book_01_Timeline L3-6, L81; Chapter_Digest_Book_01 L3-6, L81; Knowledge_States L21; Skill_Books_and_Learning L41, L113; Elves L50, L51; Leonids L50, L84; Outworlders L50, L74-76; 00_Peoples_Overview L56 … | 31 |
| Ch16 | Rescue Party | Gary_Power_Set L28; Gary L28; Rufus_Remore L31-36, L38; Rufus_Remore_Power_Set L38; 01_World_Primer L49; Glossary L51; Zartos_Culture L53-58, L57; Zartos L53-58, L57 … | 14 |
| Ch17 | A Conservative Pillage | Book_01_Timeline L3-6, L34, L72; Chapter_Digest_Book_01 L3-6, L34, L72; Alchemy_Artifice_and_Magical_Materials L21; Ken_Asano L31; Gary_Power_Set L56-61, L61; Gary L58-61; Farrah_Hurin_Power_Set L72; 01_World_Primer L106 … | 15 |
| Ch18 | One of Us | Book_01_Timeline L3, L83; Chapter_Digest_Book_01 L3, L83; 01_World_Primer L5; Glossary L5 | 6 |
| Ch19 | I Want a Lava Cannon | Farrah_Hurin L1, L30; Book_01_Timeline L4, L15, L27, L34; Chapter_Digest_Book_01 L4, L15, L27, L34; Ranks_and_Advancement L28, L42, L43; 00_Magic_Overview L30, L34, L40, L45-56, L50; Confluences L30, L31; Essence_Catalogue L30, L68, L75; Essences L30, L31, L33, L45-56, L48-50, L50 … … | 56 |
| Ch20 | By the Power of Grayskull | Book_01_Timeline L3-8, L42, L104; Chapter_Digest_Book_01 L3-8, L42, L104; Confluences L19, L97-104, L110; Essences L19, L42-44, L44, L52, L53, L84 …; Essence_Catalogue L20, L42-44, L49-50, L97, L104; Undeath L21; Adventure_Society L44, L104-110; Abilities_and_Attributes L52 … | 34 |
| Ch21 | I Have the Power | Essence_Catalogue L3, L6, L7, L49, L50, L61 …; Essences L3, L4, L6, L10-11, L36-37, L44 …; Progression_Tracks L4, L7, L47, L50, L54-59, L61 …; Book_01_Timeline L5, L48; Chapter_Digest_Book_01 L5, L48; Abilities_and_Attributes L6, L7, L15, L49, L50, L61 …; Awakening_Stones L7, L36-37; Confluences L53-54, L57 … | 54 |
| Ch22 | Apocalypse Stone | Essences L9, L38-41, L68; Ranks_and_Advancement L9, L33, L50-51, L55, L58, L60 …; 01_World_Primer L19, L20, L58; Calendar_Holidays_and_Naming_Customs L19; Daily_Life L19; Book_01_Timeline L19, L128; Chapter_Digest_Book_01 L19, L128; Master_Timeline L19 … | 63 |
| Ch23 | I May have Made a Huge Mistake | Rituals_Arrays_and_Formations L15, L16-17, L27, L30, L31-32, L32 …; Farrah_Hurin_Power_Set L15-17; Farrah_Hurin L15-17; Tone_and_Voice L15-17; NPC_Cards_Books_01-03 L15-17; Era_1_Greenstone L15-17; Familiars_Summons_and_Conjurations L35-37, L36, L37, L38-39, L42-44, L61 …; Skill_Books_and_Learning L36 … | 31 |
| Ch24 | Astral Space | Book_01_Timeline L4, L5; Chapter_Digest_Book_01 L4, L5; 01_World_Primer L34; Astral_Spaces_Zones_and_Surges L38; Alchemy_Artifice_and_Magical_Materials L40, L48 | 8 |
| Ch25 | Blasphemy is Kind of My Thing | Book_01_Timeline L3; Chapter_Digest_Book_01 L3; Daily_Life L13; Adventure_Society L17; Jason_Asano L43; Master_Timeline L43; Spoiler_Management L43 | 7 |
| Ch26 | Waterfall | Minor_Cast_Books_1-3 L4-5, L12; Book_01_Timeline L60, L64; Chapter_Digest_Book_01 L60, L64 | 6 |
| Ch27 | Water, Fall | Book_01_Timeline L3-7, L26, L58, L96; Chapter_Digest_Book_01 L3-7, L26, L58, L96; Minor_Cast_Books_1-3 L15; Abilities_and_Attributes L28; Monsters L91, L94-96; Monster_Cores_and_Training L94 | 13 |
| Ch28 | How Did You All Fit In There? | Book_01_Timeline L3-6, L73; Chapter_Digest_Book_01 L3-6, L73; Monsters L83; Afflictions_Boons_and_Damage L93 | 6 |
| Ch29 | That’s What Adventurers Do | Book_01_Timeline L5; Chapter_Digest_Book_01 L5; Afflictions_Boons_and_Damage L15, L15-16, L16; Colin L23; Monsters L79; Monster_Cores_and_Training L79-81; Skill_Books_and_Learning L87 | 9 |
| Ch30 | Closing the Door Too Hard | Anisa_Lasalle L26, L86-93; Monsters L43, L44; Greenstone L43; Vitesse L43, L44, L48, L55; 00_Places_Overview L43-44; Master_Timeline L43-44; Estercost_Continent L44; Open_Questions L44 … | 28 |
| Ch31 | Taming the Beast | Astral_Spaces_Zones_and_Surges L4, L71, L73-74, L74; Alchemy_Artifice_and_Magical_Materials L27, L27-28; Gary_Power_Set L40; Book_01_Timeline L69-73, L71-73, L74, L85; Chapter_Digest_Book_01 L69-73, L85; 01_World_Primer L71; Master_Timeline L71; 00_Magic_Overview L71-74, L96-98 … | 30 |
| Ch32 | Monster Hunting For Beginners | Book_01_Timeline L26; Chapter_Digest_Book_01 L26; Monsters L40; 01_World_Primer L52; Alchemy_Artifice_and_Magical_Materials L57; Adventure_Society L87 | 6 |
| Ch33 | Mistrun River | Book_01_Timeline L21, L31, L74; Chapter_Digest_Book_01 L21, L31 | 5 |
| Ch34 | Waving the Flag For Secular Morality | Book_01_Timeline L34, L57; Chapter_Digest_Book_01 L34, L57; Motifs_and_Sayings L34; Abilities_and_Attributes L39; Afflictions_Boons_and_Damage L40, L47 | 8 |
| Ch35 | Greenstone | Alchemy_Artifice_and_Magical_Materials L10, L21, L22, L23, L63; Jory_Tillman L10, L21, L57, L63; NPC_Rosters_by_Era L10-12; Greenstone L15, L19, L59; Book_01_Timeline L15; Chapter_Digest_Book_01 L15; Era_1_Greenstone L19, L59; Souls_Death_and_Healing L22, L23, L63 … | 24 |
| Ch36 | The Island | Book_01_Timeline L7, L71; Chapter_Digest_Book_01 L7, L71; Alchemy_Artifice_and_Magical_Materials L28, L72; Alchemy_Association L28; Jory_Tillman L28; Greenstone L68, L71-72, L89, L95, L98; Economy_and_Money L71; Open_Questions L71 … | 17 |
| Ch37 | A Good Adventurer and a Great One | Book_01_Timeline L3; Chapter_Digest_Book_01 L3; House_Geller L3-4; Calendar_Holidays_and_Naming_Customs L8; Greenstone L21; Danielle_Geller L21, L43-55; Education L40; Mirage_Chamber_Association L41-43, L43 … | 15 |
| Ch38 | Just Another Adventurer | Greenstone L3; Skill_Books_and_Learning L11; Church_of_the_Healer L34; Book_01_Timeline L41, L56; Chapter_Digest_Book_01 L41, L56; Jason_Asano L45, L55; Adventuring_Profession L52; Alchemy_Artifice_and_Magical_Materials L52 … | 37 |
| Ch39 | Training | Monster_Cores_and_Training L30; Greenstone L32-33, L34; Motifs_and_Sayings L65; Abilities_and_Attributes L70-71; Afflictions_Boons_and_Damage L70-71; Skill_Books_and_Learning L109, L110, L112, L115, L117; Education L117; Awakening_Stones L137, L147-148, L150, L154 … | 22 |
| Ch40 | Eyebeams and the Ethics of Adventuring | Book_01_Timeline L3; Chapter_Digest_Book_01 L3; Skill_Books_and_Learning L26; Jason_Asano L31, L50-52; Farrah_Hurin L31-35; Abilities_and_Attributes L37; Auras L37-41, L44, L46, L46-48, L50, L52 …; Afflictions_Boons_and_Damage L41, L42 … | 22 |
| Ch41 | Vulnerable and Exposed | Book_01_Timeline L27; Chapter_Digest_Book_01 L27; Jason_Asano L35; Church_of_Purity L87 | 4 |
| Ch42 | This is the Pits | Book_01_Timeline L21, L26, L30; Chapter_Digest_Book_01 L21, L26, L30; Greenstone L21-23, L22, L29; Magic_Society_and_Associations L25, L30, L58, L64; Lucian_Lamprey L25-26, L26, L30; Elves L25-30, L30; NPC_Rosters_by_Era L25-30, L30, L44; Plot_Hooks L25-30, L58, L64 … | 34 |
| Ch43 | Nightingale | Clothing_Food_Festivals_and_Transport_by_Region L5; Daily_Life L5; Celestines L18; Sophie_Wexler L18; NPC_Rosters_by_Era L18, L29; NPC_Cards_Books_01-03 L18, L29; Clarissa_Ventress L29; Lucian_Lamprey L47, L69 … | 14 |
| Ch44 | Complimentary Ointment | Book_01_Timeline L3, L14; Chapter_Digest_Book_01 L3, L14; Vincent_Trenslow L23, L24, L24-28, L28; Minor_Cast_Books_1-3 L40; Gods_and_Churches L68 | 10 |
| Ch45 | So Much For Atheism | 01_World_Primer L4; Gods_and_Churches L4, L4-9, L18, L39; Religion_in_Practice L4, L5, L9, L18; Greenstone L4, L4-5; Daily_Life L5, L8; Clothing_Food_Festivals_and_Transport_by_Region L8; Runics L14, L14-18; Minor_Cast_Books_1-3 L14-18, L35-45 … | 26 |
| Ch46 | Blatant Manipulation | Gods_and_Churches L16; Knowledge L16, L22; Knowledge L16; Tone_and_Voice L16; NPC_Cards_Books_01-03 L16; Book_01_Timeline L22, L33, L111; Chapter_Digest_Book_01 L22; Knowledge_States L22-50 | 11 |
| Ch47 | Mirage Chamber | Book_01_Timeline L36; Chapter_Digest_Book_01 L36; NPC_Rosters_by_Era L36, L89; Danielle_Geller L87-89, L89; Humphrey_Geller L88-89; Tone_and_Voice L88-89, L89; NPC_Cards_Books_01-03 L88-89, L89; Era_1_Greenstone L88-89, L89 | 13 |
| Ch48 | An Endless, Inescapable Nightmare | Rituals_Arrays_and_Formations L3; Mirage_Chamber_Association L3, L7, L13, L16; Book_01_Timeline L49; Chapter_Digest_Book_01 L49; Gods_and_Churches L92; Hero L92; Rufus_Remore L92-96; Gabriel_Remore L101-102 … | 15 |
| Ch49 | A Voice From Home | Greenstone L5; Book_01_Timeline L26-27, L98; Chapter_Digest_Book_01 L26-27, L98; Daily_Life L27; Gabriel_Remore L27; Pochard_Finn L27; Danielle_Geller L42; Knowledge_States L42 … | 13 |
| Ch50 | The Full Keanu | Skill_Books_and_Learning L20-22, L22, L41, L65-73, L67, L69 …; The_Reaper L40; Book_01_Timeline L40-41; Chapter_Digest_Book_01 L40-41; Great_Astral_Beings L41; Greenstone L85-91, L103, L104; Clarissa_Ventress L92, L92-96, L93, L96; Cole_Silva L92, L96 … | 28 |
| Ch51 | Song of the Nightingale | Book_01_Timeline L11; Chapter_Digest_Book_01 L11; Cole_Silva L37; Secrets_and_Rumours L37 | 4 |
| Ch52 | Pain | Book_01_Timeline L4-6, L15, L47-64; Chapter_Digest_Book_01 L4-6, L15, L47-64; Mirage_Chamber_Association L5; Jason_Asano L7-11; Greenstone L46; Clarissa_Ventress L57 | 10 |
| Ch53 | Nightlife | Book_01_Timeline L4; Chapter_Digest_Book_01 L4; NPC_Rosters_by_Era L45-49; Thalia_Mercer L45-62, L47-49, L54; Thadwick_Mercer L54; Cassandra_Mercer L60; Clarissa_Ventress L70 | 9 |
| Ch54 | Field Assessment | Vincent_Trenslow L29, L30, L32, L32-33, L35-60, L41 …; NPC_Cards_Books_01-03 L29; Adventure_Society L33, L35, L36; Calendar_Holidays_and_Naming_Customs L36; Book_01_Timeline L36; Chapter_Digest_Book_01 L36; NPC_Rosters_by_Era L36; Tone_and_Voice L36 … | 19 |
| Ch55 | Rune Tortoise | Book_01_Timeline L3-5, L67-75; Chapter_Digest_Book_01 L3-5, L67-75 | 4 |
| Ch56 | Gary’s Gift | House_Geller L6; Skill_Books_and_Learning L18, L47; Onslow L24; Gary L46-51; Soul_Bound_Items_and_Regalia L47, L49-52; Book_01_Timeline L49, L77; Chapter_Digest_Book_01 L49, L77; Alchemy_Artifice_and_Magical_Materials L49-52 … | 16 |
| Ch57 | Rainbow Smoke | Book_01_Timeline L4-8, L41, L60; Chapter_Digest_Book_01 L4-8, L41, L60; Awakening_Stones L21; Adventuring_Profession L33; Adventure_Society L33 | 9 |
| Ch58 | A Man of Malevolent Intellect | Book_01_Timeline L3, L19, L85, L118; Chapter_Digest_Book_01 L3, L19; Monsters L40; Jasons_Combat_Robes L40 | 8 |
| Ch59 | Falling Short | Alchemy_Artifice_and_Magical_Materials L8; Book_01_Timeline L17, L18, L27; Chapter_Digest_Book_01 L17, L18, L27; Clothing_Food_Festivals_and_Transport_by_Region L30; Daily_Life L30 | 9 |
| Ch60 | Making Music | Book_01_Timeline L30, L34; Chapter_Digest_Book_01 L30 | 3 |
| Ch61 | Trade Hall | Book_01_Timeline L17; Chapter_Digest_Book_01 L17; Adventuring_Profession L32; Greenstone L32; Awakening_Stones L36; Alchemy_Artifice_and_Magical_Materials L40, L129; Landemere_Vane L41; Alchemy_Association L56 … | 25 |
| Ch62 | Have Some Damn Adventures | Book_01_Timeline L5, L44, L67; Chapter_Digest_Book_01 L44, L67; Badges_and_Guild_Membership L44, L46, L47, L47-48, L61; Adventure_Society L46, L47, L47-54, L61, L81-85, L91; Alchemy_Artifice_and_Magical_Materials L46-47; Adventuring_Profession L55-59, L61, L64, L66, L68-70, L70 …; Unusual_and_Unique_Magic L55-59; Vincent_Trenslow L61-93 … | 33 |
| Ch63 | Sunk-Cost Fallacy | Motifs_and_Sayings L6; Adventuring_Profession L54, L77, L81; Book_01_Timeline L108; Chapter_Digest_Book_01 L108 | 6 |
| Ch64 | Take My Wife, Please | Adventuring_Profession L3, L5, L12, L81; Adventure_Society L3; Book_01_Timeline L3-7, L85; Chapter_Digest_Book_01 L3-7, L85; Minor_Cast_Books_1-3 L5, L83; Alchemy_Artifice_and_Magical_Materials L12; Awakening_Stones L80, L81; House_Geller L80 … | 18 |
| Ch65 | Curious Urges | Gilbert_Bertinelli L6; Book_01_Timeline L50, L60, L99; Chapter_Digest_Book_01 L50, L60, L99; Adventure_Society L60; Elspeth_Arella L60; NPC_Rosters_by_Era L60; Era_1_Greenstone L60; Auras L91 … | 17 |
| Ch66 | A Stronger Weapon Than the One in Your Hand | Phoebe_Geller L3, L4, L30; Family_Trees L3-4; Humphrey_Geller L3-6, L58, L58-62; Calendar_Holidays_and_Naming_Customs L4; House_Geller L4, L18, L27; NPC_Cards_Books_01-03 L4, L58; Book_01_Timeline L7; Chapter_Digest_Book_01 L7 … | 22 |
| Ch67 | This is What it Means to Fight Me | Jonah_Geller L14, L14-15, L66; NPC_Cards_Books_01-03 L14-15; Hannah_and_Claire_Adeah L15, L18-33, L71-95, L126-128; NPC_Rosters_by_Era L15; Glossary L15; Book_01_Timeline L95; Chapter_Digest_Book_01 L95; Rick_Geller L99 | 13 |
| Ch68 | Good News For Clive | Familiars_Summons_and_Conjurations L20, L22; Book_01_Timeline L65, L102, L106; Chapter_Digest_Book_01 L65, L102, L106; Knowledge_States L81; Who_Knows_What_When L81; Clive_Standish L92-94; Tone_and_Voice L92-94; Era_1_Greenstone L92-94 … | 15 |
| Ch69 | Dumpling Soup | Motifs_and_Sayings L37; Onslow L56; Skill_Books_and_Learning L84; 01_World_Primer L85; 00_Cosmology_Overview L85-91; Glossary L85-96; 00_Astral_Overview L85-107, L97-99; 00_Characters_Overview L85-107 … | 26 |
| Ch70 | Rewards | Book_01_Timeline L47; Chapter_Digest_Book_01 L47 | 2 |
| Ch71 | A Bit of Poo | Greenstone L3, L38; Beth_Cavendish L3; Book_01_Timeline L3, L48; Chapter_Digest_Book_01 L3, L48; 01_World_Primer L7; Minor_Cast_Books_1-3 L16, L23, L25; Runics L40; Glossary L53 … | 14 |
| Ch72 | Rat Race | Book_01_Timeline L11, L24; Chapter_Digest_Book_01 L11, L24; Colin L32 | 5 |
| Ch73 | A Grim Sword to Live By | Book_01_Timeline L25-28, L57; Chapter_Digest_Book_01 L25-28, L57; Monsters L46-51; Essence_Catalogue L48, L49, L51 | 8 |
| Ch74 | Doing Better | Humphrey_Geller L70; Book_01_Timeline L70; Chapter_Digest_Book_01 L70 | 3 |
| Ch75 | Progress | Colin L12, L14; Familiars_Summons_and_Conjurations L27-28, L33; Book_01_Timeline L33, L69; Chapter_Digest_Book_01 L33, L69; Motifs_and_Sayings L62; Skill_Books_and_Learning L72 | 10 |
| Ch76 | Preparations | Gilbert_Bertinelli L3-5; Romances_and_Rivalries L3-5; Book_01_Timeline L13, L23, L58; Chapter_Digest_Book_01 L13, L23; Minor_Cast_Books_1-3 L15; Alchemy_Artifice_and_Magical_Materials L43, L49; Dimensional_Storage_and_Portals L43, L49, L58; Alchemy_Association L100 | 14 |
| Ch77 | Group Cohesion | Knowledge L8; Pain_and_Discord L8; Gods_and_Churches L10; Knowledge L10; Knowledge_States L10; Motifs_and_Sayings L10; Thadwick_Mercer L46, L46-57, L47; House_Mercer L47 … | 18 |
| Ch78 | Jason Has the Good Biscuits | Motifs_and_Sayings L1, L85-96; Book_01_Timeline L31; Chapter_Digest_Book_01 L31; Glossary L44; Progression_Tracks L54; Jason_Asano L54; Familiars L84, L84-85; Stash L84, L85-88 | 11 |
| Ch79 | Sand Everywhere | Book_01_Timeline L3-8, L24; Chapter_Digest_Book_01 L3-8, L24 | 4 |
| Ch80 | It’s Not Work if You Love What You Do | Minor_Cast_Remore_Academy_and_Greenstone_Teams L5-48; Knowledge_States L7; Who_Knows_What_When L7; Alchemy_Artifice_and_Magical_Materials L21, L43, L104; Economy_and_Money L21, L23, L27-28, L37, L39, L40-41 …; House_Mercer L28, L77; Clothing_Food_Festivals_and_Transport_by_Region L40; Daily_Life L40 … | 25 |
| Ch81 | Crazy Desperation Move | Book_01_Timeline L3, L44; Chapter_Digest_Book_01 L3, L44; Ustei L43; Ustei_Homeland_Culture L43 | 6 |
| Ch82 | Choices | Book_01_Timeline L8; Chapter_Digest_Book_01 L8; Glossary L18; Minor_Cast_Books_1-3 L31, L82; Alchemy_Artifice_and_Magical_Materials L57; Gods_and_Churches L73; Fertility L73; House_Mercer L101 | 9 |
| Ch83 | It Makes No Difference to the Ant | Ustei L4; Book_01_Timeline L4, L55; Chapter_Digest_Book_01 L4, L55; Era_Selection L4; Plot_Hooks L4; Era_1_Greenstone L4; Open_Questions L4; NPC_Rosters_by_Era L23 … | 15 |
| Ch84 | Injury & Death | Book_01_Timeline L41, L82; Chapter_Digest_Book_01 L41, L82; Monsters L55, L56, L57; 00_Magic_Overview L57; Glossary L74; Badges_and_Guild_Membership L101 | 10 |
| Ch85 | Because I’m an Adventurer | Book_01_Timeline L3-7, L59; Chapter_Digest_Book_01 L3-7, L59; Skill_Books_and_Learning L8; Clive_Standish_Power_Set L17, L22-26; Celestial_Book L22, L26; Titles_and_Blessings L22, L47; 00_Peoples_Overview L22-26, L35, L39, L41, L47; Humans L22-26, L35 … | 23 |
| Ch86 | Some Kind of Secret | Book_01_Timeline L9, L123; Chapter_Digest_Book_01 L9, L123; Greenstone L25; Draconians L31; Runics L31, L40; 00_Peoples_Overview L40; Clive_Standish L115-116 | 10 |
| Ch87 | Can’t Lose | Motifs_and_Sayings L32; Badges_and_Guild_Membership L39; Book_01_Timeline L51, L85; Chapter_Digest_Book_01 L51, L85; Monsters L53; Jason_Asano L85; Abilities_and_Attributes L91; Awakening_Stones L91 … | 23 |
| Ch88 | The Nature of Absolution | Education L3; House_Geller L3, L9; House_Remore L3; Book_01_Timeline L25, L46; Chapter_Digest_Book_01 L25, L46; Humphrey_Geller_Power_Set L25-30, L94-96, L97; Skill_Books_and_Learning L80-85; Humphrey_Geller L94-106 … | 16 |
| Ch89 | Anti-Pirate Operations | Cassandra_Mercer L3; Book_01_Timeline L3-5, L50, L77; Chapter_Digest_Book_01 L3-5, L50, L77; Ustei L50, L50-51, L68; Ustei_Homeland_Culture L50; Plot_Hooks L50; Era_1_Greenstone L50; Open_Questions L50 … | 27 |
| Ch90 | The Path to Bronze | Ustei_Homeland_Culture L8-9, L14, L42, L44; Hudson_Kettering L11, L16, L49; Minor_Cast_Remore_Academy_and_Greenstone_Teams L13, L15; Book_01_Timeline L14; Chapter_Digest_Book_01 L14; Desert_Transport_Skimmers_and_Barges L14; Minor_Cast_Books_1-3 L32; Beth_Cavendish L61 | 14 |
| Ch91 | Life & Death | Book_01_Timeline L5, L53; Chapter_Digest_Book_01 L5; Adventuring_Profession L34; Awakening_Stones L34; Adventure_Society L34; Alchemy_Artifice_and_Magical_Materials L58; Alchemy_Association L58; Clothing_Food_Festivals_and_Transport_by_Region L64 | 9 |
| Ch92 | Unusual Contract | Book_01_Timeline L12, L65; Chapter_Digest_Book_01 L12, L65; Ustei_Homeland_Culture L12-16, L30, L36; Economy_and_Money L32; Law_and_Indenture L32, L33-34, L36; Plot_Hooks L32; Era_1_Greenstone L32; Ustei L36 … | 20 |
| Ch93 | Truth | Leust L3, L5, L5-6, L5-8, L22, L24 …; Africa_like_Continent L3, L22; Daily_Life L5; 00_Places_Overview L5; Locations_by_Era L5; Book_01_Timeline L5, L69, L73, L80; Chapter_Digest_Book_01 L5, L69, L73, L80; Master_Timeline L5 … | 36 |
| Ch94 | Consequences | Gods_and_Churches L3, L3-7; Religion_in_Practice L3; Church_of_the_Healer L3; Greenstone L3; Book_01_Timeline L3, L70; Chapter_Digest_Book_01 L3, L70; The_Healer L3-7; Neil_Davone L3-7 … | 19 |
| Ch95 | Punishment | Church_of_the_Healer L8; Minor_Cast_Books_1-3 L16, L46; Motifs_and_Sayings L51; Souls_Death_and_Healing L69, L126; Book_01_Timeline L78, L90; Chapter_Digest_Book_01 L78, L90; The_Healer L84-86, L90-95, L106-109, L120-126; Dominion L87, L94, L101, L103-104 … | 24 |
| Ch96 | You Don’t Get a Third | Church_of_the_Healer L16; Essences L18; Book_01_Timeline L24, L47; Chapter_Digest_Book_01 L24, L47 | 6 |
| Ch97 | Integrity is Sexy | Dominion L7; Book_01_Timeline L17, L29, L93; Chapter_Digest_Book_01 L17, L29; Open_Questions L19-21; Ustei_Homeland_Culture L21, L23; House_Geller L50; House_Mercer L50; Lindover_and_Clementson_Properties L97, L97-124 … | 18 |
| Ch98 | The Point of Money and Power | Desert_Transport_Skimmers_and_Barges L4; House_Mercer L20; Cassandra_Mercer L35; Romances_and_Rivalries L35; Book_01_Timeline L57, L70; Chapter_Digest_Book_01 L57, L70; Adventure_Society L63; Minor_Cast_Books_1-3 L63 … | 11 |
| Ch99 | Someone Else’s Game | Progression_Tracks L24; Jason_Asano L24, L67-70; Book_01_Timeline L36, L43, L61; Clothing_Food_Festivals_and_Transport_by_Region L39; Monsters L61; Chapter_Digest_Book_01 L61; Abilities_and_Attributes L65; Essence_Catalogue L67-70 … | 15 |
| Ch100 | Legwork | Desert_Astral_Space L8; Book_01_Timeline L69, L79; Chapter_Digest_Book_01 L69, L79; Auras L85 | 6 |
| Ch101 | Fantasy World Goodness | Book_01_Timeline L4, L64, L98; Chapter_Digest_Book_01 L4, L64, L98; Minor_Cast_Books_1-3 L9; Auras L16; Ranks_and_Advancement L16; Alchemy_Artifice_and_Magical_Materials L64, L103; Emir_Bahadir L64, L103; Cloud_Constructs_and_Palaces L64, L103 … | 21 |
| Ch102 | You Fight Like Me | 01_World_Primer L11; 00_Places_Overview L11; Hornis L11; Africa_like_Continent L11; Book_01_Timeline L57; Chapter_Digest_Book_01 L57; Runics L72; Church_of_the_Healer L73 … | 9 |
| Ch103 | Silver Hair | Auras L16; Rituals_Arrays_and_Formations L44; Clive_Standish_Power_Set L44; Clive_Standish L44; Book_01_Timeline L53, L64; Chapter_Digest_Book_01 L53, L64; Greenstone L120; Afflictions_Boons_and_Damage L130 | 10 |
| Ch104 | An Outcome That Satisfies | Jory_Tillman L4; Book_01_Timeline L16, L88; Chapter_Digest_Book_01 L16, L88; Astral_Spaces_Zones_and_Surges L60-61, L61; Danielle_Geller L60-61; Adris_Dorgan L65, L65-88, L88; NPC_Rosters_by_Era L68; Greenstone L88 … | 14 |
| Ch105 | You Aren’t in Control of What Happens Next | Book_01_Timeline L5-6, L33, L57, L66; Chapter_Digest_Book_01 L5-6, L33; Law_and_Indenture L66 | 7 |
| Ch106 | Something Shady | Book_01_Timeline L3-6, L82; Chapter_Digest_Book_01 L3-6, L82; Minor_Cast_Books_1-3 L8; Elspeth_Arella L80-83, L82; Romances_and_Rivalries L82 | 8 |
| Ch107 | All the Good People We Can Get | Desert_Astral_Space L3, L76; Book_01_Timeline L27; Chapter_Digest_Book_01 L27; Minor_Cast_Books_1-3 L49; Badges_and_Guild_Membership L51 | 6 |
| Ch108 | You Don’t Have the Strength | Cloud_Constructs_and_Palaces L3; Knowledge_States L6; Who_Knows_What_When L6; Book_01_Timeline L26, L72; Chapter_Digest_Book_01 L26, L72; Essences L28; Greenstone L35; Emir_Bahadir L35 … | 21 |
| Ch109 | The Tyranny of Rank | Hester_Maharala L6, L7-9; NPC_Rosters_by_Era L6; Boko_Culture L7-21, L21; Locations_by_Era L7-21; Boko L7-21, L9, L21; Desert_Astral_Space L8; Open_Questions L8; Africa_like_Continent L9 … | 21 |
| Ch110 | Help Arrives | 00_Astral_Overview L3; Desert_Transport_Skimmers_and_Barges L4, L13; Book_01_Timeline L6, L7, L16, L17, L27, L32 …; Chapter_Digest_Book_01 L6, L7; Essence_Catalogue L10, L20; Dustin_Kettering L17; Thadwick_Mercer L17, L20; Neil_Davone L40 … | 24 |
| Ch111 | Strange Star | Book_01_Timeline L19, L41, L78; Chapter_Digest_Book_01 L19, L41, L78; Astral_Spaces_Zones_and_Surges L24, L28; 00_Astral_Overview L28; Thalia_Mercer L42; Emir_Bahadir L76; Monsters L79 | 12 |
| Ch112 | The Accumulation of a Life | Book_01_Timeline L14, L26, L52; Chapter_Digest_Book_01 L14, L26, L52; Dimensional_Storage_and_Portals L17; Rufus_Remore_Power_Set L44; Boko L52; Gods_and_Churches L96 | 10 |
| Ch113 | You Need to Work on Making Enemies | Boko_Culture L21, L28; Boko L21, L28; Africa_like_Continent L21; Locations_by_Era L28; Book_01_Timeline L36, L41, L65, L75; Chapter_Digest_Book_01 L36, L41, L65; Farrah_Hurin L41; Builder_Cult_in_Greenstone L41 … | 25 |

### Book 2

| Chapter | Title | Cited by (lines) | Rows |
|---|---|---|---|
| Ch1 | Climbing Mountains | Cloud_Constructs_and_Palaces L3; Book_02_Timeline L4, L90; Chapter_Digest_Book_02 L4, L90; Skill_Books_and_Learning L47; Law_and_Indenture L77; Jory_Tillman L77; Sophie_Wexler L77-80; Tone_and_Voice L77-80 … | 13 |
| Ch2 | Nothing Can Hurt You Like Hope | Book_02_Timeline L21, L23, L58, L60, L100; Chapter_Digest_Book_02 L21, L23, L58, L60 | 9 |
| Ch3 | See You in Court | Adris_Dorgan L3, L4; Elspeth_Arella L3, L3-6, L4, L4-6; NPC_Cards_Books_01-03 L3; Education L22; Church_of_Knowledge L22; Law_and_Indenture L43; Book_02_Timeline L53, L76, L77; Chapter_Digest_Book_02 L53, L76 | 15 |
| Ch4 | Six-Month Lease | Book_02_Timeline L7, L24, L111; Chapter_Digest_Book_02 L7, L24, L111; Builder_Cult_in_Greenstone L7, L24; Hannah_and_Claire_Adeah L10 | 9 |
| Ch5 | The Perks of Being an Essence User | Book_02_Timeline L37, L116; Chapter_Digest_Book_02 L37, L116; Sophie_Wexler_Power_Set L37-41, L82-87; Sophie_Wexler L37-41, L82-87; Education L38; Danielle_Geller L46; Essence_Catalogue L65, L82-87; Confluences L82-87, L83, L87 … | 21 |
| Ch6 | This is the Moment | Book_02_Timeline L3; Chapter_Digest_Book_02 L3; Builder_Cult_in_Greenstone L3; 01_World_Primer L5; Rituals_Arrays_and_Formations L41, L43; Abilities_and_Attributes L43; Awakening_Stones L43; Essence_Catalogue L56 | 9 |
| Ch7 | Iron Rank | Book_02_Timeline L28, L116; Chapter_Digest_Book_02 L28, L116; Dimensional_Storage_and_Portals L47; Clive_Standish L62; Lucian_Lamprey L62; Rituals_Arrays_and_Formations L117, L130; Sophie_Wexler_Power_Set L118, L123, L133, L152, L158; Progression_Tracks L118-153 … | 17 |
| Ch8 | Getting Stoned | Sophie_Wexler_Power_Set L22, L40, L98, L122, L173; Book_02_Timeline L28; Chapter_Digest_Book_02 L28; Afflictions_Boons_and_Damage L44; Abilities_and_Attributes L45, L170-171, L171, L174-175; Confluences L45-49; Motifs_and_Sayings L93; Emir_Bahadir L168 … | 17 |
| Ch9 | Children | Awakening_Stones L9, L17, L17-18, L29, L38, L40 …; Essence_Catalogue L9, L17, L21; Essences L21; Clive_Standish L21; 01_World_Primer L30-31; Abilities_and_Attributes L31-35; Book_02_Timeline L51, L67; Chapter_Digest_Book_02 L51, L67 … | 27 |
| Ch10 | Star Seed | Adventure_Society L16; Minor_Cast_Books_1-3 L16; Jonah_Geller L26-50; Plot_Hooks L26-50; House_Geller L28; Book_02_Timeline L51, L62; Chapter_Digest_Book_02 L51, L62; Builder_Cult_in_Greenstone L51 … | 19 |
| Ch11 | It’s About How You Use It | Cassandra_Mercer L3; Book_02_Timeline L3; Chapter_Digest_Book_02 L3; Education L37; Jason_Asano L41; Beth_Cavendish L54; Kaito_Asano L61, L65; Family_Trees L65 | 9 |
| Ch12 | We End Here | Belinda_Callahan L6; Book_02_Timeline L82, L88, L102; Chapter_Digest_Book_02 L82, L102; Secrets_and_Rumours L82-88; Badges_and_Guild_Membership L83 | 8 |
| Ch13 | Poison Pill | Book_02_Timeline L8, L60, L95, L128; Chapter_Digest_Book_02 L8, L60, L95; Neil_Davone L19; Tokens_Stones_and_Relics L57, L60, L62, L66, L76-78; Gods_and_Churches L60, L103; 00_Items_Overview L60; Awakening_Stones L60; Awakening_Stones L60-62, L62, L66, L70, L71-76, L76-78 … … | 30 |
| Ch14 | Let’s Just Fight Monsters | Hornis L16, L116; Africa_like_Continent L16; Book_02_Timeline L20, L35; Chapter_Digest_Book_02 L20; Jason_Asano L35; Jasons_Combat_Robes L58; Jonah_Geller L116 | 9 |
| Ch15 | Damage You Shouldn’t Walk Away From | Badges_and_Guild_Membership L10; Hornis L25; Minor_Cast_Books_1-3 L27; Book_02_Timeline L29; Chapter_Digest_Book_02 L29; Adventuring_Profession L38; House_Kettering L44, L54; Dustin_Kettering L44 … | 13 |
| Ch16 | Picking Out the Good Ones | Church_of_the_Healer L73; Book_02_Timeline L75; Chapter_Digest_Book_02 L75; Builder_Cult_in_Greenstone L75; Secrets_and_Rumours L75 | 5 |
| Ch17 | Events Loom Large | Rick_Geller L10; Family_Trees L10; House_Geller L23-24; Purity_and_Disguise L31; Mirage_Chamber_Association L51, L60; Boko_Culture L60; Boko L60, L61; Hornis L60, L61 … | 18 |
| Ch18 | What the Geller Name is Worth | Book_02_Timeline L3, L39, L54; Chapter_Digest_Book_02 L3, L39, L54; Rituals_Arrays_and_Formations L11; Clive_Standish L25-27 | 8 |
| Ch19 | Cleansed | Book_02_Timeline L31; Chapter_Digest_Book_02 L31; Dimensional_Storage_and_Portals L60; Church_of_Purity L73, L79-80, L99; Nicolas_Hendren L73; Minor_Cast_Books_1-3 L73; NPC_Rosters_by_Era L73; Era_2_Bronze_and_the_Builder L73 … | 14 |
| Ch20 | It Just Takes Practise | Calendar_Holidays_and_Naming_Customs L3; Cheryl_Asano L18; Jason_Asano L18; Book_02_Timeline L23; Chapter_Digest_Book_02 L23; Familiars L29; Stash L29, L31; Mirage_Chamber_Association L88 | 9 |
| Ch21 | World Building | Jasons_Combat_Robes L12; Adventuring_Profession L14; Jonah_Geller L19; Thalia_Mercer L19; Book_02_Timeline L19, L23, L26, L92, L94, L123; Chapter_Digest_Book_02 L19, L23, L26; Builder_Cult_in_Greenstone L19-28, L123; Who_Knows_What_When L19-28, L123 … | 47 |
| Ch22 | Fabulous Prizes | Hornis L76; Book_02_Timeline L82, L90, L146; Chapter_Digest_Book_02 L82, L90; Reaper_Trials L82, L90; Clive_Standish L127-129 | 9 |
| Ch23 | Any Team Except Yours | Calendar_Holidays_and_Naming_Customs L3; Book_02_Timeline L6; Chapter_Digest_Book_02 L6; Neil_Davone L17; Alchemy_Artifice_and_Magical_Materials L72 | 5 |
| Ch24 | More Than One Clown | Book_02_Timeline L3, L38; Chapter_Digest_Book_02 L3, L38; Auras L13; Dimensional_Storage_and_Portals L13; Constance L22; Phoebe_Geller L27, L72; NPC_Cards_Books_01-03 L27 | 10 |
| Ch25 | Resurrection | Book_02_Timeline L3, L39, L53; Chapter_Digest_Book_02 L3, L39, L53; Alchemy_Artifice_and_Magical_Materials L24-26; Consumables_and_Trial_Rewards L24-26, L35; Builder_Cult_in_Greenstone L35-41; Era_2_Bronze_and_the_Builder L35-41; Church_of_Knowledge L37; Great_Astral_Beings L37-45 … | 41 |
| Ch26 | Manifestation | Book_02_Timeline L19; Chapter_Digest_Book_02 L19; Goblins_and_Fairies L99 | 3 |
| Ch27 | Potential | Hornis L4; Adris_Dorgan L4; Progression_Tracks L25; Sophie_Wexler_Power_Set L25; Book_02_Timeline L25, L44; Chapter_Digest_Book_02 L25, L44; House_Kettering L41; House_Mercer L41, L41-43 … | 29 |
| Ch28 | Weaponising a Barbecue | Book_02_Timeline L3-6, L43; Chapter_Digest_Book_02 L3-6, L43; Hudson_Kettering L13; Vincent_Trenslow L13; Gabrielle_Pellin L25-30; Humphrey_Geller L25-30, L32; Romances_and_Rivalries L25-30; 00_Magic_Overview L44, L56 … | 26 |
| Ch29 | This Town Ain’t Big Enough | Book_02_Timeline L3, L9; Chapter_Digest_Book_02 L3, L9; Hannah_and_Claire_Adeah L6-8; Adventuring_Profession L8; House_Kettering L8; Dustin_Kettering L8, L9, L59, L69; Rick_Geller L8, L69; Teams_by_Era L8 … | 21 |
| Ch30 | The Second-Best Iron Ranker | Hudson_Kettering L4, L15; Minor_Cast_Remore_Academy_and_Greenstone_Teams L16; Book_02_Timeline L32; Chapter_Digest_Book_02 L32; Rick_Geller L51; Neil_Davone_Power_Set L52, L53; Neil_Davone L52-54; Clive_Standish_Power_Set L53 … | 14 |
| Ch31 | Arrival | Book_02_Timeline L4, L21; Chapter_Digest_Book_02 L4, L21; Emir_Bahadir L90; NPC_Cards_Books_01-03 L90 | 6 |
| Ch32 | Full Jason | Glossary L12; Desert_Transport_Skimmers_and_Barges L38; Dimensional_Storage_and_Portals L38; House_Geller L39; Minor_Cast_Books_1-3 L41; Arabelle_Remore L52; Gabriel_Remore L52; Book_02_Timeline L52, L58 … | 26 |
| Ch33 | Versatile | Vitesse L6; Rufus_Remore L6; Family_Trees L6; Book_02_Timeline L94; Chapter_Digest_Book_02 L94; Motifs_and_Sayings L94 | 6 |
| Ch34 | I Don’t Like This Plan | Book_02_Timeline L10, L19, L45, L47, L80, L91; Chapter_Digest_Book_02 L10, L19, L45, L47; Emir_Bahadir L44; Reaper_Trials L45-47; Hester_Maharala L55; NPC_Cards_Books_01-03 L55; 01_World_Primer L58, L73; Pranay_Culture L58 … | 20 |
| Ch35 | Impossible to Subdue | Book_02_Timeline L5-9, L27, L52; Chapter_Digest_Book_02 L5-9, L27, L52; Cole_Silva L97 | 7 |
| Ch36 | The Price We Pay Doesn’t Matter | Minor_Cast_Books_1-3 L19-25; Book_02_Timeline L36, L68; Chapter_Digest_Book_02 L36, L68; Builder_Cult_in_Greenstone L36; Callum_Morse L79; NPC_Cards_Books_01-03 L79 | 8 |
| Ch37 | Make the Most of It | Book_02_Timeline L24, L31, L33, L55, L62; Chapter_Digest_Book_02 L24, L31, L33, L55; Builder_Cult_in_Greenstone L24, L31, L33; Secrets_and_Rumours L24; Cults_and_Orders L31; Landemere_Vane L67; Cressida_Vane L78; Emir_Bahadir L95 … | 19 |
| Ch38 | Wake | Book_02_Timeline L4, L40, L61, L69; Chapter_Digest_Book_02 L4, L40; Reaper_Trials L4, L40, L69; Elspeth_Arella L5; Lucian_Lamprey L19; Pochard_Finn L19; Arabelle_Remore L23; Glossary L23 … | 27 |
| Ch39 | I Can’t Trust Any of It | House_Geller L7; Book_02_Timeline L8, L11; Chapter_Digest_Book_02 L8, L11; Minor_Cast_Remore_Academy_and_Greenstone_Teams L12, L37; Padma_Parsell L13, L42; NPC_Cards_Books_01-03 L13; Draconians L15, L34; Dragon_Lands_Culture L15, L34 | 14 |
| Ch40 | Legacy | 01_World_Primer L3; Book_02_Timeline L27, L57, L59, L63; Chapter_Digest_Book_02 L27, L57, L59, L63; Emir_Bahadir L54, L65; Reaper_Trials L57, L57-63, L63; Alchemy_Artifice_and_Magical_Materials L61, L80; Desert_Transport_Skimmers_and_Barges L80, L81 | 18 |
| Ch41 | A Rash Decision | Book_02_Timeline L4, L67; Chapter_Digest_Book_02 L4, L67; Reaper_Trials L4; Cassandra_Mercer L35; Builder_Cult_in_Greenstone L67; Thadwick_Mercer L80, L80-89; Timos L88-89, L89; NPC_Cards_Books_01-03 L89 | 12 |
| Ch42 | It’s A Good One | Neil_Davone_Power_Set L40; Book_02_Timeline L52, L77; Chapter_Digest_Book_02 L52, L77; Clive_Standish_Power_Set L52-62; Familiars_Summons_and_Conjurations L70; Stash L70; Dimensional_Storage_and_Portals L79; Alchemy_Artifice_and_Magical_Materials L86 … | 11 |
| Ch43 | The City of Fallen Echoes | Book_02_Timeline L7, L95; Chapter_Digest_Book_02 L7, L95; Dimensional_Storage_and_Portals L24; Monsters L56; Knowledge_States L94; Reaper_Trials L95 | 8 |
| Ch44 | Shade | Gilbert_Bertinelli L8; Familiars L37, L93; Book_02_Timeline L39, L57, L76, L85, L87, L93 …; Chapter_Digest_Book_02 L39, L57; Reaper_Trials L39, L72-78, L76, L105; City_of_Fallen_Echoes L39-41, L41-45, L47, L57-59, L119-128; Shade L65, L93, L119; Cults_and_Orders L72-78, L85-89, L99-109 … | 40 |
| Ch45 | Seriously Hardcore | Monsters L7; City_of_Fallen_Echoes L7; Book_02_Timeline L30, L52; Chapter_Digest_Book_02 L30, L52; Reaper_Trials L52; Sophie_Wexler L69-72; Tone_and_Voice L69-72; NPC_Cards_Books_01-03 L69-72 … | 11 |
| Ch46 | Mixed Medication | Minor_Cast_Books_1-3 L42; Book_02_Timeline L50, L61; Chapter_Digest_Book_02 L50, L61 | 5 |
| Ch47 | Giving People Choices | Book_02_Timeline L30; Chapter_Digest_Book_02 L30; Adventuring_Profession L59; Monsters L59 | 4 |
| Ch48 | A Well-Informed Man | Book_02_Timeline L43; Chapter_Digest_Book_02 L43; Minor_Cast_Remore_Academy_and_Greenstone_Teams L58; Adventuring_Profession L61; Valdis_Volaire L77; NPC_Rosters_by_Era L77 | 6 |
| Ch49 | The Danger is Us | Book_02_Timeline L22; Chapter_Digest_Book_02 L22; Gabriel_Remore L66; Emir_Bahadir L67 | 4 |
| Ch50 | Surplus to Requirements | Book_02_Timeline L5; Chapter_Digest_Book_02 L5; Knowledge_States L8; Era_1_Greenstone L8; Neil_Davone_Power_Set L56, L65; Abilities_and_Attributes L57 | 7 |
| Ch51 | A Worse Plan | Book_02_Timeline L3, L26, L40, L70; Chapter_Digest_Book_02 L3, L26, L40, L70; Mirror_Kingdom_Culture L8; Valdis_Volaire L8, L9-10, L17, L28, L32, L42 …; Glossary L8; Monsters L41; Knowledge_States L83; Alchemy_Artifice_and_Magical_Materials L98 | 20 |
| Ch52 | No One Has That Coming | Calendar_Holidays_and_Naming_Customs L32; Book_02_Timeline L34, L51, L71; Chapter_Digest_Book_02 L34, L51, L71; Reaper_Trials L34, L71; Afflictions_Boons_and_Damage L51; Jory_Tillman L72 | 11 |
| Ch53 | Part of Being a Team | Book_02_Timeline L13, L64; Chapter_Digest_Book_02 L13, L64; Reaper_Trials L13, L64; Vitesse_Culture L27; Motifs_and_Sayings L27; Open_Questions L27; Monsters L28-29, L29; Minor_Cast_Books_1-3 L64 … | 13 |
| Ch54 | Making a Spectacle of Himself | Book_02_Timeline L6, L70, L122; Chapter_Digest_Book_02 L6, L70; Hudson_Kettering L18, L85; Motifs_and_Sayings L93; Reaper_Trials L122 | 9 |
| Ch55 | Team Change | Glossary L3-4; Book_02_Timeline L9, L12; Chapter_Digest_Book_02 L9, L12; Reaper_Trials L9-12, L12, L69; Sigrid_Freyn L58; NPC_Cards_Books_01-03 L58; Valdis_Volaire L63; Padma_Parsell L69 | 12 |
| Ch56 | Company Worth Keeping | Sigrid_Freyn L5-14; Book_02_Timeline L13, L57, L73, L82; Chapter_Digest_Book_02 L13, L73; Reaper_Trials L13, L73, L82; Hudson_Kettering L41; Essence_Catalogue L43; Essences L92, L93; Awakening_Stones L93, L94 … | 17 |
| Ch57 | He Who Fights With Monsters | City_of_Fallen_Echoes L29, L68, L70; Glossary L29; Awakening_Stones L31, L31-33; Awakening_Stones L36; Valdis_Volaire L63; Monsters L68; 00_Astral_Overview L68; Book_02_Timeline L68, L93, L142 … | 17 |
| Ch58 | Irreconcilable Ideals | City_of_Fallen_Echoes L9-24, L70-74, L100-102; Book_02_Timeline L35, L41, L62, L102; Chapter_Digest_Book_02 L35, L41; Reaper_Trials L41, L102; Consumables_and_Trial_Rewards L53-56, L102-104; The_Healer L77-78 | 14 |
| Ch59 | Meanwhile, Two Weeks Ago in Greenstone… | Book_02_Timeline L3, L22, L115; Chapter_Digest_Book_02 L3, L22; Builder_Cult_in_Greenstone L3-22; Thadwick_Mercer L4, L4-36; Minor_Cast_Books_1-3 L4, L15, L22, L35-36; Family_Trees L4; Glossary L4; Thalia_Mercer L22, L82-84, L83, L84 … | 29 |
| Ch60 | Take the Loot and Go | Book_02_Timeline L13, L50, L120, L179; Chapter_Digest_Book_02 L13, L50; The_Reaper L15; City_of_Fallen_Echoes L54-56; Reaper_Trials L120; Who_Knows_What_When L120; Spoiler_Management L120-122; Open_Questions L120-122, L185 … | 16 |
| Ch61 | Making an Exit | Beth_Cavendish L51; Valdis_Volaire L74; NPC_Cards_Books_01-03 L74; Unusual_and_Unique_Magic L130, L130-147, L138-142, L141, L144, L144-147 …; Book_02_Timeline L131, L144, L147; Chapter_Digest_Book_02 L131, L144, L147; Clive_Standish_Power_Set L144; Humans L144, L147 … | 29 |
| Ch62 | Shallow Earth | Clothing_Food_Festivals_and_Transport_by_Region L3; Book_02_Timeline L3, L24; Chapter_Digest_Book_02 L3, L24; Danielle_Geller L24; Henrietta_Geller L24; Keith_Geller L24; Family_Trees L24; Romances_and_Rivalries L24 … | 17 |
| Ch63 | Relief | Book_02_Timeline L9; Chapter_Digest_Book_02 L9; Reaper_Trials L9; Era_Selection L9; Plot_Hooks L9; Era_1_Greenstone L9; Awakening_Stones L25, L73, L115; Sophie_Wexler_Power_Set L25, L30-31 … | 32 |
| Ch64 | Glory | Awakening_Stones L3-5; Book_02_Timeline L3-5, L72; Chapter_Digest_Book_02 L3-5, L72; Familiars_Summons_and_Conjurations L5, L15; Progression_Tracks L5; Gordon L12; Neil_Davone_Power_Set L42, L55-62; Neil_Davone L55 … | 21 |
| Ch65 | Display of Gratitude | Book_02_Timeline L18, L22, L47, L78, L85, L95-96; Chapter_Digest_Book_02 L18, L22, L47; Zara_Rimaros L55; Dominion L75-76; Reaper_Trials L78, L85; Titles_and_Blessings L85; Jason_Asano L85; Auras L85-86, L86-87 … | 25 |
| Ch66 | The Person I Decided to Be | Auras L8; Book_02_Timeline L8, L27; Chapter_Digest_Book_02 L8, L27; Awakening_Stones L66; Sophie_Wexler_Power_Set L68, L79, L93, L111; Rituals_Arrays_and_Formations L90; Dominion L104-106; Gods_and_Churches L105 | 13 |
| Ch67 | You Have Friends to Help You | Rituals_Arrays_and_Formations L3, L162; Sophie_Wexler_Power_Set L6, L18, L51; The_Reaper L45; Progression_Tracks L49, L99, L119; Book_02_Timeline L49, L168; Chapter_Digest_Book_02 L49, L168; Belinda_Callahan_Power_Set L103, L123; Unusual_and_Unique_Magic L113 | 16 |
| Ch68 | Blob Body | Progression_Tracks L4, L36; Belinda_Callahan_Power_Set L8, L17, L40-45, L50, L56; Book_02_Timeline L36, L129; Chapter_Digest_Book_02 L36, L129; Belinda_Callahan L39-45 | 12 |
| Ch69 | Particular Appetites | Killian_Laurent L12; Zara_Rimaros L16, L17-19, L18; NPC_Cards_Books_01-03 L16, L17-19; Book_02_Timeline L17, L25, L95; Chapter_Digest_Book_02 L17, L25, L95; Tone_and_Voice L17-19; Era_4_Rimaros L17-19; Family_Trees L18 … | 25 |
| Ch70 | Domineering, Territorial and Robust | Clothing_Food_Festivals_and_Transport_by_Region L3; Jayapura_Culture L3; Pranay_Culture L3; Jayapura L3; Stash L11; Essences L30; Souls_Death_and_Healing L33-35, L36, L37-38, L39, L42, L44; 01_World_Primer L34-42 … | 17 |
| Ch71 | More Shady as We Go Along | Neil_Davone L14; NPC_Cards_Books_01-03 L14; Book_02_Timeline L26, L43, L103; Chapter_Digest_Book_02 L26, L103; Familiars_Summons_and_Conjurations L50; Belinda_Callahan L50; Shimmer L50; Belinda_Callahan_Power_Set L57, L70, L90 | 13 |
| Ch72 | Magnificent Entity | Familiars L15; Shade L28; Book_02_Timeline L28, L29, L98; Chapter_Digest_Book_02 L28, L29; Reaper_Trials L28; Familiars_Summons_and_Conjurations L57, L133; Belinda_Callahan L62; Shimmer L62 … | 14 |
| Ch73 | I Try to Find the Truth, But That’s Your Hiding Place | Pranay_Culture L3; Mirage_Chamber_Association L3, L4, L5, L6, L10-12, L14; 00_Places_Overview L3; Jayapura L3, L4, L4-5, L62; Jayapura_Culture L4, L6, L7-8, L10, L12-14, L62; Monster_Cores_and_Training L8-12; Adventuring_Profession L14, L37; Tokens_Stones_and_Relics L58 … | 24 |
| Ch74 | The Last Reward | Book_02_Timeline L4, L14, L34; Chapter_Digest_Book_02 L4, L14, L34; Clothing_Food_Festivals_and_Transport_by_Region L14; Jayapura_Culture L14; Jayapura L14; Reaper_Trials L14; Constance L18; Alchemy_Artifice_and_Magical_Materials L34-46, L40-50, L41, L45, L72, L72-74 … … | 23 |
| Ch75 | Impossible Wasn’t Enough | Book_02_Timeline L3-5, L50, L65, L68, L90; Chapter_Digest_Book_02 L3-5, L50; Adris_Dorgan L42; Neil_Davone L67; Henrietta_Geller L68, L69, L70; NPC_Cards_Books_01-03 L70; Familiars L75-79, L81-84; Familiars_Summons_and_Conjurations L83 … | 17 |
| Ch76 | Eclipse | Arabelle_Remore L3, L17-39, L39; Constance L3, L55; Emir_Bahadir L3; Teams_by_Era L3, L8; Book_02_Timeline L3, L51, L58, L71, L74, L76 …; Chapter_Digest_Book_02 L3, L51; Builder_Cult_in_Greenstone L3, L58; Callum_Morse L7, L7-46, L40, L41 … | 30 |

### Book 3

| Chapter | Title | Cited by (lines) | Rows |
|---|---|---|---|
| Ch1 | A Question You Don’t Yet Know to Ask | Alchemy_Artifice_and_Magical_Materials L5, L100; Book_02_Timeline L14; Book_03_Timeline L14, L18, L46; Chapter_Digest_Book_03 L14, L18; Era_Selection L14, L105; Era_2_Bronze_and_the_Builder L14, L105; Knowledge_States L21; Arabelle_Remore L73 … | 46 |
| Ch2 | Looking Forward | Jory_Tillman L16; Book_03_Timeline L17, L64, L105; Chapter_Digest_Book_03 L17, L64; Gilbert_Bertinelli L59-62, L64; Jason_Asano L59-64; Essence_Catalogue L62; Emir_Bahadir L65; Jasons_Combat_Robes L75 … | 13 |
| Ch3 | Adventurers Are People Too | Knowledge L14; Book_03_Timeline L50; Chapter_Digest_Book_03 L50; Teams_by_Era L70-82, L76-81; Era_2_Bronze_and_the_Builder L70-82; Mirror_Kingdom_Culture L73-80; Team_Shining_Scabbard L76, L78, L80, L81; Romances_and_Rivalries L76-81 … | 13 |
| Ch4 | Valkyrie | Valdis_Volaire L3, L7; Gordon L28; Familiars L28-32; Onslow L29; Neil_Davone L29-32; Stash L31; Shimmer L32; Clive_Standish_Power_Set L33 … | 16 |
| Ch5 | Departures | Tone_and_Voice L9; Era_1_Greenstone L9; Mirror_Kingdom_Culture L20, L23, L34-36, L40-48, L50; Calendar_Holidays_and_Naming_Customs L23, L35; Valdis_Volaire L42-50; Open_Questions L49-53; Sigrid_Freyn L49-58, L57-58; Book_03_Timeline L50, L70 … | 26 |
| Ch6 | No Pot of Gold | Book_03_Timeline L3-5, L15, L20; Chapter_Digest_Book_03 L3-5, L15, L20; Plot_Hooks L18, L43; Era_2_Bronze_and_the_Builder L18, L43; Gary_Power_Set L35; Henrietta_Geller L43 | 12 |
| Ch7 | The Glory of Success or the Price of Failure | Henrietta_Geller L3, L28; Book_03_Timeline L3, L5, L97; Chapter_Digest_Book_03 L3, L5; Monsters L5; Adventure_Society L55; Dimensional_Storage_and_Portals L85; Zato L88-89; Builder_Cult_in_Greenstone L88-89 … | 17 |
| Ch8 | Adequate | Beth_Cavendish L19; Hester_Maharala L25; Familiars_Summons_and_Conjurations L33; Monsters L35; Essences L37-44; Essence_Catalogue L38; Book_03_Timeline L58; Chapter_Digest_Book_03 L58 … | 11 |
| Ch9 | Trash Bonanza | Henrietta_Geller L27; Book_03_Timeline L53; Chapter_Digest_Book_03 L53; Essence_Catalogue L63 | 4 |
| Ch10 | Strangeness | Book_03_Timeline L3, L23; Chapter_Digest_Book_03 L3, L23; Rituals_Arrays_and_Formations L5; Monsters L21; Clive_Standish_Power_Set L23 | 7 |
| Ch11 | Full Circle | Book_03_Timeline L3-7, L26; Chapter_Digest_Book_03 L3-7, L26; Belinda_Callahan_Power_Set L27, L45, L52, L58-60; Shimmer L68; Rituals_Arrays_and_Formations L90 | 10 |
| Ch12 | Regretting it Later | Book_03_Timeline L16, L95; Chapter_Digest_Book_03 L16, L95 | 4 |
| Ch13 | Swat | Monsters L5-6, L17; Book_03_Timeline L14, L17; Chapter_Digest_Book_03 L14, L17; Gordon L38 | 7 |
| Ch14 | The Purpose of the Adventure Society | Souls_Death_and_Healing L9; Book_03_Timeline L9, L81; Chapter_Digest_Book_03 L9, L81; Alchemy_Artifice_and_Magical_Materials L18; Jasons_Combat_Robes L27-29; Familiars_Summons_and_Conjurations L78; Adventuring_Profession L79; Titles_and_Blessings L81-83, L83 … | 15 |
| Ch15 | Elven Storage Solutions | Monsters L17; Progression_Tracks L21, L47; Master_Timeline L21; Abilities_and_Attributes L47; Ranks_and_Advancement L47, L56; Book_03_Timeline L47; Chapter_Digest_Book_03 L47 | 9 |
| Ch16 | Disbanded | Book_03_Timeline L6, L7; Chapter_Digest_Book_03 L6, L7; Master_Timeline L7; Killian_Laurent L16-43, L43, L70; Alchemy_Association L80; Magic_Society_and_Associations L80; Economy_and_Money L81; Jory_Tillman L81, L82 … | 15 |
| Ch17 | The Man Behind the Mouth | Book_03_Timeline L3, L16; Chapter_Digest_Book_03 L3, L16; Builder_Cult_in_Greenstone L3; Killian_Laurent L13-26; NPC_Rosters_by_Era L14; Era_2_Bronze_and_the_Builder L14; Alchemy_Artifice_and_Magical_Materials L26; Cole_Silva L56-60 … | 11 |
| Ch18 | Search | Book_03_Timeline L3-4, L6-7; Chapter_Digest_Book_03 L3-4, L6-7; Cole_Silva L128; Killian_Laurent L130 | 6 |
| Ch19 | Defiance | Book_03_Timeline L3, L92; Chapter_Digest_Book_03 L3, L92; Rituals_Arrays_and_Formations L37; Killian_Laurent L78 | 6 |
| Ch20 | Hanging Around | Book_03_Timeline L9, L41; Chapter_Digest_Book_03 L9, L41; Builder_Cult_in_Greenstone L9; Abilities_and_Attributes L17; Roland_Remore L25; Family_Trees L25 | 8 |
| Ch21 | What Doesn’t Kill You | The_Healer L46, L73; Book_03_Timeline L59, L60, L97, L102; Chapter_Digest_Book_03 L59, L60, L97, L102; Gary L60; Gods_and_Churches L73; Church_of_the_Healer L73; Unusual_and_Unique_Magic L105-111; Ranks_and_Advancement L109, L110 … | 26 |
| Ch22 | Lingering Doubts | Church_of_the_Healer L3, L35; Carlos_Quilido L3, L6, L11, L35, L73; Vincent_Trenslow L3; Book_03_Timeline L5, L13; Chapter_Digest_Book_03 L5, L13; NPC_Cards_Books_01-03 L6; Church_of_Purity L35; The_Healer L73 | 15 |
| Ch23 | Scars | Book_03_Timeline L18, L19; Chapter_Digest_Book_03 L18, L19; Rituals_Arrays_and_Formations L19, L32; Carlos_Quilido L36, L63 | 8 |
| Ch24 | I Won’t Let Them Turn Me Into That | Killian_Laurent L3; Plot_Hooks L3; Era_2_Bronze_and_the_Builder L3; Hornis L12-17, L17; Africa_like_Continent L17; Danielle_Geller L23; Lucian_Lamprey L23, L48; Auras L30 … | 24 |
| Ch25 | Putting the Band Back Together | Cole_Silva L3; Killian_Laurent L4; Plot_Hooks L4; Book_03_Timeline L9, L25; Chapter_Digest_Book_03 L9, L25; Rituals_Arrays_and_Formations L38 | 8 |
| Ch26 | Nothing Speaks Louder Than Power | Book_03_Timeline L4, L17, L76; Chapter_Digest_Book_03 L4, L17; Gary_Power_Set L9; Education L9; House_Remore L9; Vitesse L13; Builder_Cult_in_Greenstone L76 | 10 |
| Ch27 | My Name is Jason Asano | Book_03_Timeline L3, L15, L62; Chapter_Digest_Book_03 L3, L15; Plot_Hooks L62 | 6 |
| Ch28 | While They Watch Me Kill You | Book_03_Timeline L72; Chapter_Digest_Book_03 L72; Ranks_and_Advancement L78; Motifs_and_Sayings L87 | 4 |
| Ch29 | Inherently Corrupting | Jason_Asano L22-35; Abilities_and_Attributes L23; Progression_Tracks L23; Era_Selection L23; Era_2_Bronze_and_the_Builder L23; Souls_Death_and_Healing L46; Knowledge_States L73-76; Book_03_Timeline L93, L107, L108, L113 … | 16 |
| Ch30 | Beholden to No One | Hester_Maharala L21; Book_03_Timeline L28, L36; Chapter_Digest_Book_03 L28, L36 | 5 |
| Ch31 | Evil Detector | Cults_and_Orders L25-27; Glossary L45; Book_03_Timeline L50, L56; Chapter_Digest_Book_03 L50, L56; Builder_Cult_in_Greenstone L56; Church_of_Purity L57; Church_of_the_Healer L57; Nicolas_Hendren L57 … | 11 |
| Ch32 | The World Needs People Like You | Jasons_Combat_Robes L45, L45-46, L48-49; Book_03_Timeline L48, L66, L88; Chapter_Digest_Book_03 L48, L66; Jayapura_Culture L65; Jayapura L65; Ranks_and_Advancement L88; The_Healer L101; Titles_and_Blessings L105, L106 … | 17 |
| Ch33 | I’m Very Big on Cowardice | Book_03_Timeline L4, L13, L45; Chapter_Digest_Book_03 L4, L13; Rufus_Remore L11-12; Dimensional_Storage_and_Portals L62 | 7 |
| Ch34 | More Powerful Than We Anticipated | Book_03_Timeline L3, L16, L28; Chapter_Digest_Book_03 L3, L16; Titles_and_Blessings L7; Timos L10; Builder_Cult_in_Greenstone L16-28; 01_World_Primer L60; 00_Places_Overview L60; Vitesse L60 … | 13 |
| Ch35 | Fate Can’t Wait to Kill Us All | Book_03_Timeline L4, L71; Chapter_Digest_Book_03 L4, L71; Builder_Cult_in_Greenstone L4; Badges_and_Guild_Membership L43, L45 | 7 |
| Ch36 | Running Towards Something | Era_Selection L36; Era_2_Bronze_and_the_Builder L36; Monsters L50; Book_03_Timeline L90; Chapter_Digest_Book_03 L90 | 5 |
| Ch37 | Greenhouse Flowers | Ranks_and_Advancement L9; 00_Astral_Overview L9; Clive_Standish L13; Clive_Standish_Power_Set L32; Book_03_Timeline L32; Chapter_Digest_Book_03 L32 | 6 |
| Ch38 | A Man Transformed | Abilities_and_Attributes L5; Progression_Tracks L5, L95, L110; Book_03_Timeline L5, L95, L110; Chapter_Digest_Book_03 L5, L95, L110; Rituals_Arrays_and_Formations L30; Clive_Standish_Power_Set L38, L60, L68, L78, L97; Onslow L54; Master_Timeline L110 | 18 |
| Ch39 | The Worst Possible Option | Dimensional_Storage_and_Portals L37; Book_03_Timeline L80; Chapter_Digest_Book_03 L80 | 3 |
| Ch40 | Brave Little Tailor | Monsters L11, L47; Humphrey_Geller_Power_Set L63, L72, L80; Neil_Davone_Power_Set L95, L108; Clive_Standish_Power_Set L118; Belinda_Callahan_Power_Set L131; Book_03_Timeline L138; Chapter_Digest_Book_03 L138 | 11 |
| Ch41 | Terms of the Pact | Anisa_Lasalle L51-76, L53; NPC_Cards_Books_01-03 L53; Glossary L66; Timos L73; Zato L73; Book_03_Timeline L84; Chapter_Digest_Book_03 L84 | 8 |
| Ch42 | Trading Safety Today For Death Tomorrow | Book_03_Timeline L6; Chapter_Digest_Book_03 L6; Builder_Cult_in_Greenstone L6 | 3 |
| Ch43 | Stalwart | Book_03_Timeline L3-6, L23; Chapter_Digest_Book_03 L3-6, L23; Humphrey_Geller_Power_Set L7, L42-44, L46, L54, L58, L66-68 …; Neil_Davone_Power_Set L16; 00_Magic_Overview L69; Clive_Standish_Power_Set L79; Belinda_Callahan_Power_Set L147 | 17 |
| Ch44 | I’m Sick of Fighting Magic Rocks | Book_03_Timeline L25; Chapter_Digest_Book_03 L25; Motifs_and_Sayings L57; Neil_Davone_Power_Set L129 | 4 |
| Ch45 | Crossing the Threshold | Book_03_Timeline L16, L72, L79, L90; Chapter_Digest_Book_03 L16, L72; Progression_Tracks L90; Master_Timeline L90; Builder_Cult_in_Greenstone L90; Jayapura L100 | 10 |
| Ch46 | Anyone Can Be Useful | Book_03_Timeline L26; Chapter_Digest_Book_03 L26; Timos L55; Zato L60; Thadwick_Mercer L61; Gordon L95, L96 | 7 |
| Ch47 | A Series of Familiar Powers | Book_03_Timeline L3; Chapter_Digest_Book_03 L3; Monsters L4 | 3 |
| Ch48 | It’s Not About Killing Monsters | Book_03_Timeline L3-6, L53; Chapter_Digest_Book_03 L3-6, L53; Jasons_Combat_Robes L10; Neil_Davone_Power_Set L46; Clive_Standish_Power_Set L54, L62 | 8 |
| Ch49 | Sin Eater | Neil_Davone_Power_Set L4, L17; Sophie_Wexler L15; Shade L45; Book_03_Timeline L77; Chapter_Digest_Book_03 L77 | 6 |
| Ch50 | The Most Dangerous Thing in the Dark | Book_03_Timeline L3-4, L54-61; Chapter_Digest_Book_03 L3-4, L54-61 | 4 |
| Ch51 | The Boss Comes to Town | Neil_Davone_Power_Set L8; Book_03_Timeline L32, L85, L93; Chapter_Digest_Book_03 L32, L85; Timos L85; Builder_Cult_in_Greenstone L85-93; Cults_and_Orders L91, L105; Glossary L114 | 11 |
| Ch52 | It’s Very Complicated and You All Need to Go Away | Book_03_Timeline L66; Chapter_Digest_Book_03 L66 | 2 |
| Ch53 | Strong Foundations | Book_03_Timeline L12, L36, L58; Chapter_Digest_Book_03 L12, L36, L58; Neil_Davone_Power_Set L59; Progression_Tracks L68, L69; Master_Timeline L68-69 | 10 |
| Ch54 | A Valiant Death | Book_03_Timeline L10, L19; Chapter_Digest_Book_03 L10, L19; Builder_Cult_in_Greenstone L19; Nicolas_Hendren L21; Anisa_Lasalle L23-24 | 7 |
| Ch55 | Ambitions | Book_03_Timeline L71, L95; Chapter_Digest_Book_03 L71 | 3 |
| Ch56 | Faith and Glory | Book_03_Timeline L14, L18; Chapter_Digest_Book_03 L14, L18; Nicolas_Hendren L57, L71 | 6 |
| Ch57 | Thadwick | Great_Astral_Beings L4; Book_03_Timeline L13; Chapter_Digest_Book_03 L13; Thadwick_Mercer L15; Knowledge L87; Jason_Asano L87; Motifs_and_Sayings L87; Tone_and_Voice L87 … | 10 |
| Ch58 | The True Danger | Nicolas_Hendren L3, L47; Book_03_Timeline L3, L4, L15, L16, L19; Chapter_Digest_Book_03 L4, L15, L16; Humphrey_Geller_Power_Set L20; Anisa_Lasalle L30; Shimmer L60 | 13 |
| Ch59 | Forsaken Place | Afflictions_Boons_and_Damage L38; Purity_and_Disguise L45; Jasons_Combat_Robes L87; Belinda_Callahan_Power_Set L91, L105; Neil_Davone_Power_Set L101; Nicolas_Hendren L103; Book_03_Timeline L118, L123, L126; Chapter_Digest_Book_03 L118, L123, L126 … | 15 |
| Ch60 | Being What he Needs to Be | Anisa_Lasalle L5; NPC_Cards_Books_01-03 L5, L12; Shade L8; Nicolas_Hendren L12, L32; Book_03_Timeline L12, L47; Chapter_Digest_Book_03 L12, L47; Zato L37; Cults_and_Orders L38 | 12 |
| Ch61 | A Significantly More Dangerous Entity | Cults_and_Orders L3; Book_03_Timeline L8; Chapter_Digest_Book_03 L8; Gods_and_Churches L11; Essences L11; Glossary L23-26 | 6 |
| Ch62 | Losing the Battle to Win the War | Era_Selection L23; Era_2_Bronze_and_the_Builder L23; Great_Astral_Beings L33; Spoiler_Management L33; Book_03_Timeline L96; Chapter_Digest_Book_03 L96; Master_Timeline L96 | 7 |
| Ch63 | War of Adaptation | Book_03_Timeline L3; Chapter_Digest_Book_03 L3; Humphrey_Geller_Power_Set L25; The_Builder L45 | 4 |
| Ch64 | The Hero of This Story | Book_03_Timeline L123; Chapter_Digest_Book_03 L123 | 2 |
| Ch65 | Good News, Bad News | Book_03_Timeline L79, L96; Chapter_Digest_Book_03 L79, L96; Builder_Cult_in_Greenstone L79; Secrets_and_Rumours L79; Era_2_Bronze_and_the_Builder L79 | 7 |
| Ch66 | Here We Are | Zato L45; Onslow L46-47; Book_03_Timeline L47; Chapter_Digest_Book_03 L47; Belinda_Callahan_Power_Set L48 | 5 |
| Ch67 | Outmatched | Cults_and_Orders L6; Book_03_Timeline L39, L56; Chapter_Digest_Book_03 L39, L56; Builder_Cult_in_Greenstone L39; Zato L69, L69-100, L100; NPC_Cards_Books_01-03 L69; Belinda_Callahan_Power_Set L73; Afflictions_Boons_and_Damage L93 … | 14 |
| Ch68 | The Power of Friendship | Progression_Tracks L13-16; Titles_and_Blessings L13-16; Celestines L14; Book_03_Timeline L14, L42; Chapter_Digest_Book_03 L14, L42; Sophie_Wexler L14-15; Sophie_Wexler_Power_Set L15; Zato L46, L46-61, L58-60, L60 … | 15 |
| Ch69 | A War of Stolen Moments | Book_03_Timeline L38, L42, L60, L91, L108, L129 …; Chapter_Digest_Book_03 L38, L42, L60; Builder_Cult_in_Greenstone L42, L279, L378; Plot_Hooks L42, L279, L900; Onslow L97; Tokens_Stones_and_Relics L108; Hester_Maharala L186; Death L189 … | 134 |

### Book 4

| Chapter | Title | Cited by (lines) | Rows |
|---|---|---|---|
| Ch1 | A Better Pants Solution | Titles_and_Blessings L33-35; Progression_Tracks L34; Book_04_Timeline L34, L38, L63; Chapter_Digest_Book_04 L34, L38; Earth_and_the_Monster_Waves L38; 00_Places_Overview L39; 00_Earth_Overview L39; Casselton_and_Asano_Village L39 … | 15 |
| Ch2 | Time to Front Up | Book_04_Timeline L8, L74; Chapter_Digest_Book_04 L8, L74; Earth_and_the_Monster_Waves L8; 01_World_Primer L11; Essence_Catalogue L18; Monsters L18; Jason_Asano L22; Titles_and_Blessings L22-24, L25, L26, L44, L45 … | 30 |
| Ch3 | The Single Greatest Thing on This Planet | Shade L28, L83; Death L30; Order_and_Cult_of_the_Reaper L30; Souls_Death_and_Healing L34, L36, L38, L40; Titles_and_Blessings L46, L48, L70; World_Phoenix L66; Book_04_Timeline L80, L108, L112, L126; Chapter_Digest_Book_04 L80, L108 … | 46 |
| Ch4 | Some Secrets Change You Forever | Casselton_and_Asano_Village L8; Book_04_Timeline L8, L87, L94; Chapter_Digest_Book_04 L8, L87, L94; Earth_and_the_Monster_Waves L8, L87, L94; Taika L17, L27; Hiro_Asano L52, L52-54; Secrets_and_Rumours L87, L94; Cheryl_Asano L105 … | 19 |
| Ch5 | It Would Be Weirder If Magic Wasn’t Responsible | Earth_Powers L3; Anna_Tilden L5-7, L111-112; Ketevan_Arziani L10; Earth_Magic L13; Ranks_and_Advancement L13-14; 01_World_Primer L13-16; Shade L33; Taika L40 … | 13 |
| Ch6 | Not the Regular Sort of Dangerous | 00_Earth_Overview L78; Book_04_Timeline L91, L105; Chapter_Digest_Book_04 L91, L105 | 5 |
| Ch7 | Boogie Man | Ken_Asano L10; Family_Trees L10; Kaito_Asano L11; Greg L42; Book_04_Timeline L42; Chapter_Digest_Book_04 L42; Craig_Vermillion L49-50; Auras L92 | 8 |
| Ch8 | More Plausible Than the Reality | Book_04_Timeline L3-7, L84; Chapter_Digest_Book_04 L3-7, L84; Hiro_Asano L47; Ketevan_Arziani L83 | 6 |
| Ch9 | I Suggest You Be Very Polite | Hiro_Asano L18, L76; Shade L21; Book_04_Timeline L58, L65, L93; Chapter_Digest_Book_04 L65, L93; Earth_Powers L76; Engineers_of_Ascension L76; 00_Earth_Overview L76; Master_Timeline L76 … | 17 |
| Ch10 | A Leather Coat and Tight, Black Pants | Book_04_Timeline L7; Chapter_Digest_Book_04 L7; Craig_Vermillion L63, L127; Earth_Powers L116, L127; The_Cabal L127, L133 | 8 |
| Ch11 | A Knife in Its Sheath | Earth_Magic L4, L8, L10, L14, L19-22, L21; Earth_Powers L4, L8, L19, L21, L101; Craig_Vermillion L4, L124; Master_Timeline L4; Glossary L4-8; The_Network L8, L19; 00_Magic_Overview L9-10; Gods_and_Churches L16 … | 39 |
| Ch12 | Underworld Bargain | Engineers_of_Ascension L4, L41; Book_04_Timeline L16-17, L51; Chapter_Digest_Book_04 L16-17, L51; Hiro_Asano L41 | 7 |
| Ch13 | Time to Rip Off the Band-Aid | Engineers_of_Ascension L3; Hiro_Asano L3, L3-4; NPC_Cards_Books_04-06 L3-4; Craig_Vermillion L52-54, L54; Taika L80; Book_04_Timeline L94-95, L96; Chapter_Digest_Book_04 L94-95, L96 | 11 |
| Ch14 | Bullets, Bikes and Blood | Book_04_Timeline L3-5, L33, L50; Chapter_Digest_Book_04 L3-5, L33, L50; Jasons_Combat_Robes L28 | 7 |
| Ch15 | A Good Friend and a Very Bad Enemy | Incursion_Sites L12; Book_04_Timeline L12, L13; Chapter_Digest_Book_04 L12, L13; Earth_and_the_Monster_Waves L12; Motifs_and_Sayings L12; The_Cabal L70 | 8 |
| Ch16 | Flavour Text | Book_04_Timeline L4, L14, L61; Chapter_Digest_Book_04 L4, L14; Taika L44; Earth_Magic L108 | 7 |
| Ch17 | Time For Context | Taika L42; NPC_Cards_Books_04-06 L42; Book_04_Timeline L113, L126; Chapter_Digest_Book_04 L113, L126 | 6 |
| Ch18 | Brown Trousers Time | Book_04_Timeline L3, L57; Chapter_Digest_Book_04 L3, L57; Who_Knows_What_When L29; Era_3_Earth L29; Monster_Cores_and_Training L36; Shade L40; Monsters L114; Earth_Magic L122 | 10 |
| Ch19 | The Complete Set | Book_04_Timeline L23, L78, L91; Chapter_Digest_Book_04 L23, L78, L91; 01_World_Primer L36; The_Network L48, L56; Who_Knows_What_When L69; Era_3_Earth L69 | 11 |
| Ch20 | More Valuable Than a Life | Book_04_Timeline L26, L55-56, L111; Chapter_Digest_Book_04 L26, L55-56, L111 | 6 |
| Ch21 | Uncontrolled Factor | Book_04_Timeline L3, L7; Chapter_Digest_Book_04 L3, L7; 01_World_Primer L31-33; Earth_Magic L33; Ranks_and_Advancement L33; Essence_Catalogue L135; Monsters L136, L137 | 10 |
| Ch22 | Agendas | Hiro_Asano L33; Book_04_Timeline L83-85; Chapter_Digest_Book_04 L83-85; Earth_and_the_Monster_Waves L83-85 | 4 |
| Ch23 | Hegemons | 01_World_Primer L26; Earth_Magic L26; Book_04_Timeline L27; Chapter_Digest_Book_04 L27; Dawn L31-39 | 5 |
| Ch24 | Guilty Conscience | Book_04_Timeline L32, L66; Chapter_Digest_Book_04 L32, L66; Shade L33; Cheryl_Asano L42; Kaito_Asano L101, L101-126 | 8 |
| Ch25 | Uncommon Mistake | Book_04_Timeline L10; Chapter_Digest_Book_04 L10; Motifs_and_Sayings L11-12; Alchemy_Artifice_and_Magical_Materials L20; Rituals_Arrays_and_Formations L20; Kaito_Asano L44; NPC_Cards_Books_01-03 L44; Emi_Evans_Asano L60, L60-66 … | 13 |
| Ch26 | It’s Complicated | Erika_Asano L29, L71; Book_04_Timeline L29, L59; Chapter_Digest_Book_04 L29, L59; Kaito_Asano L45, L47-50; Amy_Asano L45-48, L46, L47; NPC_Cards_Books_04-06 L46, L71; Family_Trees L47; Romances_and_Rivalries L47-50 … | 18 |
| Ch27 | A Big Dose of Normal | Book_04_Timeline L3, L97, L167; Ken_Asano L41, L41-44, L44, L109; Kaito_Asano L55, L55-70; Amy_Asano L74; Chapter_Digest_Book_04 L97; Earth_and_the_Monster_Waves L97; NPC_Cards_Books_01-03 L109; Emi_Evans_Asano L171 | 14 |
| Ch28 | Moppet | Anna_Tilden L48; Emi_Evans_Asano L126, L135-139, L154; Book_04_Timeline L126, L139; Chapter_Digest_Book_04 L126, L139; Earth_and_the_Monster_Waves L139 | 9 |
| Ch29 | Always Tell the Truth if You Can Get Away With It | Emi_Evans_Asano L43, L45-54, L69-73, L103; Book_04_Timeline L45, L103; Chapter_Digest_Book_04 L45, L103 | 8 |
| Ch30 | Discretion is a Good Idea | Erika_Asano L4; Book_04_Timeline L5, L38; Chapter_Digest_Book_04 L5, L38; Spirit_Vault_and_Astral_Kingdom L45, L49; Hiro_Asano L74; NPC_Cards_Books_04-06 L74 | 9 |
| Ch31 | The Cold Eyes of a Stranger | Cheryl_Asano L3, L3-6, L6; Ian_Evans L3; Family_Trees L3; Emi_Evans_Asano L25; Book_04_Timeline L25, L48; Chapter_Digest_Book_04 L25, L48; 01_World_Primer L48; Earth_Magic L48 … | 15 |
| Ch32 | Looking Down the Point of a Sword | Emi_Evans_Asano L4, L19; Shade L21; All_Devouring_Eye L36; Book_04_Timeline L36; Chapter_Digest_Book_04 L36 | 6 |
| Ch33 | What Your Uncle Has Been Telling You | Ken_Asano L38; Book_04_Timeline L43, L76-77, L77, L102; Chapter_Digest_Book_04 L43, L77; Knowledge_States L82 | 8 |
| Ch34 | The Moments That Decide Who You Are | Erika_Asano L5; Emi_Evans_Asano L14; Book_04_Timeline L42; Chapter_Digest_Book_04 L42; Kaito_Asano L131 | 5 |
| Ch35 | I’m Mysterious Now | Book_04_Timeline L8; Chapter_Digest_Book_04 L8; Cheryl_Asano L52, L53, L84; Family_Trees L52; The_Network L117; Confluences L123 | 8 |
| Ch36 | Hardline Position | Order_and_Cult_of_the_Reaper L8; Book_04_Timeline L34, L153; Chapter_Digest_Book_04 L34, L153; Anna_Tilden L35; Asya_Karadeniz L37, L37-41, L39, L41, L77; NPC_Rosters_by_Era L37; Era_3_Earth L37; Nigel_Thornton L74 … | 18 |
| Ch37 | Otherwise Best Avoided | Souls_Death_and_Healing L14; Astral_Spaces_Zones_and_Surges L63, L79; 00_Earth_Overview L70; Incursion_Sites L70; The_Network L78; Earth_Magic L79; Book_04_Timeline L103; Chapter_Digest_Book_04 L103 | 9 |
| Ch38 | Terms | Gordon L26; Book_04_Timeline L45; Chapter_Digest_Book_04 L45 | 3 |
| Ch39 | Section | Book_04_Timeline L3-4, L6; Chapter_Digest_Book_04 L3-4, L6; Incursion_Sites L28; Astral_Spaces_Zones_and_Surges L55; Earth_Magic L55; Nigel_Thornton L65; NPC_Cards_Books_04-06 L65; Minor_Cast_Books_4-6 L76 | 10 |
| Ch40 | Core Users | The_Network L3-4, L9, L32; Book_04_Timeline L3-4, L37; Chapter_Digest_Book_04 L3-4, L37; Nigel_Thornton L22, L61; Astral_Spaces_Zones_and_Surges L33; Minor_Cast_Books_4-6 L63; Abilities_and_Attributes L72; Unusual_and_Unique_Magic L72 | 13 |
| Ch41 | What You Call Observing | Confluences L6; Essence_Catalogue L6; Monsters L18, L32; Incursion_Sites L18, L32; Book_04_Timeline L19, L55; Chapter_Digest_Book_04 L19, L55; Farrah_Hurin_Power_Set L31; Farrah_Hurin L31 … | 19 |
| Ch42 | Not the Monster | Book_04_Timeline L3, L26, L66; Chapter_Digest_Book_04 L3, L26, L66; Minor_Cast_Books_4-6 L27; Glossary L27; Abilities_and_Attributes L44; Confluences L44 | 10 |
| Ch43 | Letting Him Run Rampant | The_Network L3, L58; Book_04_Timeline L3; Chapter_Digest_Book_04 L3; Essences L10; Asya_Karadeniz L24-25; Earth_Magic L33; Saint-Etienne L58; Adrien_Barbou L58 … | 10 |
| Ch44 | Old Testament Power | Erika_Asano L3; Taika L3; Cheryl_Asano L54-59, L56, L59; The_Network L82; Book_04_Timeline L133, L143; Chapter_Digest_Book_04 L133, L143 | 10 |
| Ch45 | My Turn | Book_04_Timeline L17, L94; Chapter_Digest_Book_04 L17, L94; Cheryl_Asano L73-76, L76; Shade L81; Ken_Asano L82 | 8 |
| Ch46 | Visually Distinctive Henchman | Book_04_Timeline L46, L100; Chapter_Digest_Book_04 L46, L100; Shade L78; The_Network L80; Ketevan_Arziani L82; NPC_Rosters_by_Era L82; NPC_Cards_Books_04-06 L82; Earth_Magic L90 | 10 |
| Ch47 | Of Course It Was Him | Book_04_Timeline L12, L50; Chapter_Digest_Book_04 L12, L50; Ketevan_Arziani L28; Name_Index L37-43 | 6 |
| Ch48 | The Price of Transgression | Book_04_Timeline L16, L21; Chapter_Digest_Book_04 L16, L21; Name_Index L83 | 5 |
| Ch49 | The Time For Bold, Decisive Men | Book_04_Timeline L3, L5, L51, L93, L99; Chapter_Digest_Book_04 L3, L5, L93, L99; Remy L3-4, L7, L9-10, L11, L16-18, L19-26 … | 16 |
| Ch50 | Technical Issue | Book_04_Timeline L9, L84; Chapter_Digest_Book_04 L9, L84; Emi_Evans_Asano L53-62; Shade L76 | 6 |
| Ch51 | The Long Game | The_Network L8, L30-37, L35; Minor_Cast_Books_4-6 L10; Book_04_Timeline L10, L30, L45, L72; Chapter_Digest_Book_04 L10, L30, L45; Glossary L10; Saint-Etienne L28, L28-30, L60-68; Locations_by_Era L28-37; Master_Timeline L30, L37 … | 26 |
| Ch52 | A Moment For Drastic Measures | Saint-Etienne L22-23; Progression_Tracks L37; Book_04_Timeline L37; Chapter_Digest_Book_04 L37; Asya_Karadeniz L83; Minor_Cast_Books_4-6 L84; Adrien_Barbou L94 | 7 |
| Ch53 | Foiled Plans | Book_04_Timeline L3, L4, L20, L55; Chapter_Digest_Book_04 L3, L4; Minor_Cast_Books_4-6 L75 | 7 |
| Ch54 | Quite the Year | Book_04_Timeline L39; Chapter_Digest_Book_04 L39; Glossary L88 | 3 |
| Ch55 | Full Houseboat | Arabelle_Remore L3; Book_04_Timeline L5, L8, L93; Chapter_Digest_Book_04 L5, L8; Earth_and_the_Monster_Waves L8; Amy_Asano L58 | 8 |
| Ch56 | A Wizard Did It | Book_04_Timeline L22, L35; Chapter_Digest_Book_04 L22, L35; Who_Knows_What_When L22; Emi_Evans_Asano L46; Family_Trees L46 | 7 |
| Ch57 | The King of Everyone | Spirit_Vault_and_Astral_Kingdom L3-10, L59; Emi_Evans_Asano L33-39, L34-36; Domains L59; Book_04_Timeline L100; Chapter_Digest_Book_04 L100 | 7 |
| Ch58 | I Came Back to Show You Wonders | Titles_and_Blessings L19; Emi_Evans_Asano L75; Book_04_Timeline L95, L126; Chapter_Digest_Book_04 L95, L126 | 6 |
| Ch59 | Mercy | The_Network L4, L11; Asya_Karadeniz L7; Book_04_Timeline L11, L48; Chapter_Digest_Book_04 L11, L48; Ketevan_Arziani L13; Anna_Tilden L35 | 9 |
| Ch60 | Ideal Circumstances | Incursion_Sites L18, L59-65; Book_04_Timeline L18; Chapter_Digest_Book_04 L18 | 4 |
| Ch61 | The Blood and Death Guy | Farrah_Hurin_Power_Set L18, L33, L34; Book_04_Timeline L92; Chapter_Digest_Book_04 L92 | 5 |
| Ch62 | A Lot of Anomalies | Incursion_Sites L23; Book_04_Timeline L83; Chapter_Digest_Book_04 L83 | 3 |
| Ch63 | Pitch Meetings | Book_04_Timeline L8, L25; Chapter_Digest_Book_04 L8, L25; NPC_Rosters_by_Era L25; Li_Li_Mei L25-28 | 6 |
| Ch64 | Moving Forward | Confluences L57, L70; Essence_Catalogue L70; Book_04_Timeline L80, L82; Chapter_Digest_Book_04 L80, L82 | 7 |
| Ch65 | Flemish Baroque | Confluences L22, L28, L29; Taika L22, L30; Glossary L22, L28; Essence_Catalogue L22-27, L27, L28; Taika_Power_Set L22-27; Humphrey_Geller_Power_Set L28; Book_04_Timeline L84; Chapter_Digest_Book_04 L84 | 14 |
| Ch66 | Not Ready to Leave | Asya_Karadeniz L59; Greg L59, L59-66, L66; NPC_Cards_Books_04-06 L59, L64; Craig_Vermillion L64; Book_04_Timeline L82; Chapter_Digest_Book_04 L82 | 9 |
| Ch67 | Decision | Book_04_Timeline L27; Chapter_Digest_Book_04 L27 | 2 |
| Ch68 | What You Have to Do | Book_04_Timeline L59, L139, L170; Chapter_Digest_Book_04 L59, L139, L170; Earth_and_the_Monster_Waves L59, L139; Secrets_and_Rumours L59; Who_Knows_What_When L59, L139; Era_3_Earth L59, L139; Earth_Magic L59-61, L63-65; 01_World_Primer L79, L97, L131-135 … | 22 |
| Ch69 | The Direction We Want Them to Go | Erika_Asano L70; Ian_Evans L70; NPC_Cards_Books_04-06 L70; Essence_Catalogue L83, L102, L106; Confluences L102, L106; Book_04_Timeline L106; Chapter_Digest_Book_04 L106 | 10 |
| Ch70 | The Dangers of What I Do | Book_04_Timeline L7, L24; Chapter_Digest_Book_04 L7, L24; Essence_Catalogue L8; Gary_Power_Set L44; Farrah_Hurin_Power_Set L48; Cheryl_Asano L86 | 8 |
| Ch71 | We Were All Monsters | Confluences L4-5, L30, L36; Book_04_Timeline L6, L36, L72; Chapter_Digest_Book_04 L6, L36, L72; Essence_Catalogue L30, L36; Kaito_Asano L62 | 12 |
| Ch72 | Options | Essence_Catalogue L22-23; Amy_Asano L25; Auras L38; Confluences L76, L83; Book_04_Timeline L85; Chapter_Digest_Book_04 L85; Ken_Asano L86 | 8 |
| Ch73 | I Need Time | Book_04_Timeline L39; Chapter_Digest_Book_04 L39; Emi_Evans_Asano L77; Auras L92, L93, L95-100; Ranks_and_Advancement L92; Mirror_Kingdom_Culture L98 | 8 |
| Ch74 | Walkabout | Auras L6, L10, L12-13, L14; Ranks_and_Advancement L8; Mirror_Kingdom_Culture L12; Book_04_Timeline L12, L32, L65; Chapter_Digest_Book_04 L12, L32, L65; Emi_Evans_Asano L32, L145; Yumi_Asano L40, L43; Family_Trees L40, L43 … | 19 |

### Book 5

| Chapter | Title | Cited by (lines) | Rows |
|---|---|---|---|
| Ch1 | Too Valuable to Lose | Minor_Cast_Books_4-6 L15-17, L35, L85; Essence_Catalogue L17; Book_05_Timeline L21, L38; 01_World_Primer L38; Chapter_Digest_Book_05 L38; Alchemy_Artifice_and_Magical_Materials L49; Monster_Cores_and_Training L51-52, L53; Skill_Books_and_Learning L51-52 … | 13 |
| Ch2 | All I Can Do is My Best | Chloe_Baudrillard L9, L44, L44-85, L51-53, L85; Book_05_Timeline L9, L108, L126; Chapter_Digest_Book_05 L9, L126; NPC_Cards_Books_04-06 L44; Emi_Evans_Asano L116 | 12 |
| Ch3 | A Modern Myth | Engineers_of_Ascension L5, L8-12, L9, L51; Book_05_Timeline L5, L57, L170, L212; Chapter_Digest_Book_05 L5, L57; Earth_and_the_Monster_Waves L5, L170; Mr_North L5-12; Earth_Powers L8-12; Plot_Hooks L8-19; Secrets_and_Rumours L57 … | 27 |
| Ch5 | Grand Tour | Book_05_Timeline L7, L59, L66, L104; Chapter_Digest_Book_05 L7, L59, L66, L104; 00_Magic_Overview L11; Earth_Magic L11; Rituals_Arrays_and_Formations L11; Ken_Asano L59; Earth_and_the_Monster_Waves L59; Emi_Evans_Asano L59-68 … | 19 |
| Ch6 | New Groove | Book_05_Timeline L48, L69; Chapter_Digest_Book_05 L48, L69; Monsters L85 | 5 |
| Ch7 | Get to the Chopper | Essence_Catalogue L8, L14, L16, L42; Asya_Karadeniz L12, L21-23; Greg L12; NPC_Rosters_by_Era L12; Confluences L14, L16, L64-66; Book_05_Timeline L16; Chapter_Digest_Book_05 L16; Adrien_Barbou L96 | 14 |
| Ch8 | What’s Left of Your Principles | Book_04_Timeline L5; Book_05_Timeline L5, L35, L44, L54; Chloe_Baudrillard L12; Earth_Powers L14-18, L28, L39; NPC_Rosters_by_Era L14-18; Mr_North L14-67, L24, L58-60, L62-67; Engineers_of_Ascension L26-28, L44-47, L50-51, L53, L54, L62 …; Open_Questions L28, L39 … | 32 |
| Ch9 | Contingencies | Book_05_Timeline L5, L23, L40, L80; Chapter_Digest_Book_05 L5, L23; Emi_Evans_Asano L23; Anna_Tilden L52; Ketevan_Arziani L67 | 9 |
| Ch10 | Humanity | Book_05_Timeline L6, L52; Chapter_Digest_Book_05 L6, L52; NPC_Rosters_by_Era L17; Audrey_Blaine L17-33, L24; NPC_Cards_Books_04-06 L24 | 8 |
| Ch11 | Media Blitz | Book_05_Timeline L12; Chapter_Digest_Book_05 L12; Motifs_and_Sayings L12; Secrets_and_Rumours L12; Who_Knows_What_When L12; Era_3_Earth L12; Amy_Asano L82 | 7 |
| Ch12 | Grandmotherly Advice | Akari_Asano L18, L27, L83; NPC_Cards_Books_04-06 L18; Yumi_Asano L84; Book_05_Timeline L100; Chapter_Digest_Book_05 L100 | 7 |
| Ch13 | A Bloke With Vast Cosmic Power | Book_05_Timeline L35, L41, L73; Chapter_Digest_Book_05 L35, L41; Earth_and_the_Monster_Waves L35; Master_Timeline L37; Asya_Karadeniz L75 | 8 |
| Ch14 | A Very Long To-Do List | Earth_Magic L3; Book_05_Timeline L8, L77; Chapter_Digest_Book_05 L8, L77; Kaito_Asano L37, L37-49; Confluences L61; Essence_Catalogue L61; Akari_Asano L61-66; NPC_Rosters_by_Era L61-66 | 11 |
| Ch15 | Another Step Forward | Akari_Asano L3, L47; Progression_Tracks L50; Book_05_Timeline L50; Chapter_Digest_Book_05 L50 | 5 |
| Ch16 | Tactical Flexibility | Earth_Magic L78; Book_05_Timeline L78; Chapter_Digest_Book_05 L78; Familiars L103-108; Shade L103-108 | 5 |
| Ch17 | Broken | Incursion_Sites L3; Earth_Magic L7; Earth_Powers L7; The_Network L7, L8-9; 00_Earth_Overview L7; Era_Selection L7; Spoiler_Management L7; Era_3_Earth L7 … | 17 |
| Ch18 | Never Enough | Book_05_Timeline L22, L41, L78; Chapter_Digest_Book_05 L22, L78; Incursion_Sites L82, L83; Kaito_Asano L83 | 8 |
| Ch19 | Media Landscape | Minor_Cast_Books_10-13 L10; Glossary L10; Book_05_Timeline L26, L99; Earth_and_the_Monster_Waves L26; Open_Questions L76; Chapter_Digest_Book_05 L99 | 7 |
| Ch20 | Instability | Dawn L21, L21-24, L22, L40-41, L65-67; NPC_Cards_Books_01-03 L21; NPC_Rosters_by_Era L21-24; Era_3_Earth L21-24, L25; Book_05_Timeline L24, L25-26, L26, L41, L117; Chapter_Digest_Book_05 L24, L25-26, L41; Master_Timeline L24, L24-26; Tone_and_Voice L24, L25 … | 27 |
| Ch21 | Supernatural | Akari_Asano L24, L106; Book_05_Timeline L32; Chapter_Digest_Book_05 L32 | 4 |
| Ch22 | Arms Race | Book_05_Timeline L46, L48; Chapter_Digest_Book_05 L46, L48; Who_Knows_What_When L46-48; Earth_and_the_Monster_Waves L48 | 6 |
| Ch23 | Sword-Fighting With No Shirt On | Book_05_Timeline L37, L94; Chapter_Digest_Book_05 L37, L94 | 4 |
| Ch24 | Candid and Authentic | Tone_and_Voice L3-5; Era_3_Earth L3-5; Emi_Evans_Asano L4, L9, L12-16; Book_05_Timeline L4, L61; Chapter_Digest_Book_05 L4, L61; NPC_Cards_Books_04-06 L4, L9; Erika_Asano L28; The_Cabal L32 … | 14 |
| Ch25 | Warmth and Levity | Monster_Cores_and_Training L5, L6, L6-8, L10; Ranks_and_Advancement L15; Progression_Tracks L23; Book_05_Timeline L23, L94; Chapter_Digest_Book_05 L23, L94; Abilities_and_Attributes L23-25, L26, L27; 01_World_Primer L26-27; Asya_Karadeniz L54 … | 16 |
| Ch26 | An Intelligent King | Book_05_Timeline L9, L17; Chapter_Digest_Book_05 L9; Incursion_Sites L17; Remy L39-44; Akari_Asano L50 | 6 |
| Ch27 | Hunted | Book_05_Timeline L3; Chapter_Digest_Book_05 L3; Minor_Cast_Books_4-6 L24-26, L36-37; Colin L57 | 5 |
| Ch28 | Gamble | Book_05_Timeline L4-11, L70, L86; Chapter_Digest_Book_05 L4-11, L70; Incursion_Sites L86 | 6 |
| Ch29 | Dying of Thirst in the Desert | Book_05_Timeline L19, L65, L68; Chapter_Digest_Book_05 L19, L65; Titles_and_Blessings L68; Jason_Asano L68-72; Soul_Bound_Items_and_Regalia L77-80 | 8 |
| Ch30 | Enough Power | Titles_and_Blessings L30; Earth_Powers L43; Open_Questions L43; Book_05_Timeline L57; Chapter_Digest_Book_05 L57; Gilbert_Bertinelli L58; Jasons_Combat_Robes L58; Farrah_Hurin L61 … | 9 |
| Ch31 | Silver | Era_Selection L1; Era_3_Earth L1; Progression_Tracks L6; Book_05_Timeline L6, L34, L121, L135, L164; Chapter_Digest_Book_05 L6, L34; Master_Timeline L6; Earth_and_the_Monster_Waves L6; Emi_Evans_Asano L134-135 … | 23 |
| Ch32 | Old Affairs | Earth_Powers L5; Engineers_of_Ascension L5, L8; Open_Questions L5; Mr_North L8; Incursion_Sites L11; Book_05_Timeline L23; Chapter_Digest_Book_05 L23; Essence_Catalogue L29-30 | 9 |
| Ch33 | End Run | Book_05_Timeline L3, L104; Chapter_Digest_Book_05 L3, L104 | 4 |
| Ch34 | Giving Face | Emi_Evans_Asano L3; Book_05_Timeline L66; Chapter_Digest_Book_05 L66; Earth_and_the_Monster_Waves L66; Akari_Asano L70, L70-100, L100; Ken_Asano L70; Family_Trees L70 | 9 |
| Ch35 | Not In a Position to Criticise | Book_05_Timeline L21; Chapter_Digest_Book_05 L21; Calendar_Holidays_and_Naming_Customs L71 | 3 |
| Ch36 | Honour | Noriko_Asano L3, L11-16, L32, L89; Family_Trees L3; Book_05_Timeline L3, L33; Chapter_Digest_Book_05 L3, L33; NPC_Rosters_by_Era L3; NPC_Cards_Books_04-06 L3; Ketevan_Arziani L33; Akari_Asano L63 … | 14 |
| Ch37 | They Get to See What I’m Like | Book_05_Timeline L28, L51; Chapter_Digest_Book_05 L28, L51; Noriko_Asano L92; Family_Trees L92 | 6 |
| Ch38 | Fanboy | Itsuki_Tiwari L5, L5-92, L6, L7, L50; NPC_Cards_Books_04-06 L5; Book_05_Timeline L41; Chapter_Digest_Book_05 L41; Confluences L50; Essence_Catalogue L50 | 10 |
| Ch39 | A Very Bad Mistake | Itsuki_Tiwari L3, L70; Family_Trees L3; Book_05_Timeline L15, L88; Chapter_Digest_Book_05 L15, L88; Asya_Karadeniz L110; Yumi_Asano L125 | 9 |
| Ch40 | An Unexpected Direction | Itsuki_Tiwari L3; Emi_Evans_Asano L3-18; Book_05_Timeline L18, L79; Chapter_Digest_Book_05 L18, L79; 00_Cosmology_Overview L49-50; Mr_North L66, L68, L72, L74-78, L78-86, L79 …; NPC_Cards_Books_04-06 L68, L78-86; Earth_Powers L79, L79-83 … | 24 |
| Ch41 | Parade of Delights | Book_05_Timeline L3-8, L85; Chapter_Digest_Book_05 L3-8, L85; Alchemy_Artifice_and_Magical_Materials L24-26, L52-62; Mr_North L24-26, L33, L103; The_Builders_Door_and_Fundament_Gate L24-26, L28, L52-62, L62-64; Tone_and_Voice L33; Era_3_Earth L33 | 15 |
| Ch42 | Collateral Damage | Itsuki_Tiwari L43; Reality_and_Genesis_Cores L54; Book_05_Timeline L59; Chapter_Digest_Book_05 L59; Secrets_and_Rumours L59; Who_Knows_What_When L59 | 6 |
| Ch43 | I Intend to Do Damage | Book_05_Timeline L3, L71, L75; Chapter_Digest_Book_05 L3, L75; Nigel_Thornton L14; Reality_and_Genesis_Cores L66; Emi_Evans_Asano L85-90; Church_of_the_Healer L94; Jory_Tillman L94 | 10 |
| Ch44 | A Chance to Control the Narrative | Amy_Asano L3; NPC_Rosters_by_Era L3; Era_3_Earth L3, L48-49; Asya_Karadeniz L17, L45; Greg L17; Kaito_Asano L17; Teams_by_Era L17; Spirit_Vault_and_Astral_Kingdom L44-45 … | 31 |
| Ch45 | You Shouldn’t Lie to Your Wife | Book_05_Timeline L3, L38; Chapter_Digest_Book_05 L3, L38; Consumables_and_Trial_Rewards L9-11; Plot_Hooks L9-11; Era_3_Earth L9-11; Earth_and_the_Monster_Waves L11; Reality_and_Genesis_Cores L11, L23 | 10 |
| Ch46 | The Decision Has Been Made | Itsuki_Tiwari L16; Book_05_Timeline L63, L91; Chapter_Digest_Book_05 L63, L91; Minor_Cast_Books_4-6 L86 | 6 |
| Ch47 | First Priority | Book_05_Timeline L9; Chapter_Digest_Book_05 L9; Gerling L26, L29, L29-30, L30, L102, L106 …; NPC_Cards_Books_04-06 L26; Engineers_of_Ascension L29-30; Greg L37; Minor_Cast_Books_4-6 L102; Reality_and_Genesis_Cores L111 | 14 |
| Ch48 | Node Space | The_Network L18, L50, L57; Book_05_Timeline L43, L90, L103; Chapter_Digest_Book_05 L43, L90; Reality_and_Genesis_Cores L71; Gerling L103 | 10 |
| Ch49 | Loaded For Battle | Reality_and_Genesis_Cores L22; Gordon L43; Book_05_Timeline L45; Chapter_Digest_Book_05 L45 | 4 |
| Ch50 | Going For Gold | Book_05_Timeline L30, L84; Chapter_Digest_Book_05 L30, L84; Gerling L35, L35-41, L41, L71; Farrah_Hurin_Power_Set L36, L38 | 10 |
| Ch51 | Prepare For The Rematch | Minor_Cast_Books_4-6 L8; Book_05_Timeline L28, L127; Chapter_Digest_Book_05 L28, L127; Emi_Evans_Asano L33; Greg L40; Kaito_Asano L40; Romances_and_Rivalries L40; Teams_by_Era L40 … | 24 |
| Ch52 | Finish the Job | Book_05_Timeline L3, L68; Chapter_Digest_Book_05 L3, L68; Master_Timeline L3; Kaito_Asano L20; Family_Trees L20; Noriko_Asano L68; Earth_and_the_Monster_Waves L68 | 9 |
| Ch53 | Inevitability | Book_05_Timeline L13, L67, L80; Chapter_Digest_Book_05 L13, L67; Reality_and_Genesis_Cores L31; Emi_Evans_Asano L79, L80, L80-85, L82, L86 | 11 |
| Ch54 | The Edge of Madness | Emi_Evans_Asano_Power_Set L8, L13; Emi_Evans_Asano L8, L13; Rituals_Arrays_and_Formations L11; The_Cabal L25; Book_05_Timeline L45, L50; Chapter_Digest_Book_05 L45, L50; 00_Peoples_Overview L52; Goblins_and_Fairies L52, L55 | 13 |
| Ch55 | Trying to Be Merciful | Book_05_Timeline L3; Chapter_Digest_Book_05 L3; Craig_Vermillion L78-81; Vampire_War L92; Earth_Vampire_War L92; Earth_and_the_Monster_Waves L92; Reality_and_Genesis_Cores L92; Era_3_Earth L92 | 8 |
| Ch56 | Appreciation | Erika_Asano L7, L47; Family_Trees L7; Book_05_Timeline L24, L69; Chapter_Digest_Book_05 L24, L69; Asya_Karadeniz L24-26; Greg L26; Order_and_Cult_of_the_Reaper L69 | 10 |
| Ch57 | Brooding Loner | The_Cabal L8, L9-10, L16; Astral_Spaces_Zones_and_Surges L11; Minor_Cast_Books_4-6 L12, L14-15; Book_05_Timeline L16, L44; Chapter_Digest_Book_05 L16, L44 | 10 |
| Ch58 | High Maintenance | Greg L3, L3-14, L14; NPC_Cards_Books_04-06 L3-14; Book_05_Timeline L20, L105; Chapter_Digest_Book_05 L20, L105; Motifs_and_Sayings L20 | 9 |
| Ch59 | Treachery or Cowardice | Book_05_Timeline L30; Chapter_Digest_Book_05 L30; The_Cabal L32 | 3 |
| Ch60 | Comely Wenches | Farrah_Hurin_Power_Set L37, L46, L48, L50, L68; Book_05_Timeline L63; Chapter_Digest_Book_05 L63; Reality_and_Genesis_Cores L64 | 8 |
| Ch61 | A Lot Like a Guess | Book_05_Timeline L27; Chapter_Digest_Book_05 L27; Goblins_and_Fairies L52; Reality_and_Genesis_Cores L72 | 4 |
| Ch62 | It’s Okay to Laugh | Book_05_Timeline L55; Chapter_Digest_Book_05 L55; The_Cabal L60 | 3 |
| Ch63 | Dignified Moment | Book_05_Timeline L3; Chapter_Digest_Book_05 L3 | 2 |
| Ch64 | When Someone is Under Your Gun | Valdis_Volaire L24; Book_05_Timeline L31; Chapter_Digest_Book_05 L31; Minor_Cast_Books_4-6 L68; Titles_and_Blessings L128 | 5 |
| Ch65 | When, Not If | Minor_Cast_Books_4-6 L18; Book_05_Timeline L31, L56, L66; Earth_Vampire_War L41; Reality_and_Genesis_Cores L41; Chapter_Digest_Book_05 L56, L66 | 8 |
| Ch66 | Not Entirely Ethical | Book_05_Timeline L5, L17, L48; Chapter_Digest_Book_05 L5, L17; Vampire_War L8; Earth_Vampire_War L8; Earth_and_the_Monster_Waves L8; World_Phoenix L36 | 9 |
| Ch67 | Ahead of Schedule | Book_05_Timeline L4, L31, L75; Chapter_Digest_Book_05 L4, L31; Earth_Vampire_War L39-45 | 6 |
| Ch68 | Open Wound | Book_05_Timeline L3, L30, L68; Chapter_Digest_Book_05 L3, L30; Reality_and_Genesis_Cores L8; Gerling L14; Glossary L30; Transformation_Zones L34-38; Astral_Spaces_Zones_and_Surges L68; Earth_Magic L68 … | 15 |

### Book 6

| Chapter | Title | Cited by (lines) | Rows |
|---|---|---|---|
| Ch1 | Looting a House as it Burns Down Around You | Gerling L3, L13; Book_06_Timeline L3, L4, L32, L72, L85; Chapter_Digest_Book_06 L3, L4; Era_3_Earth L3; Anna_Tilden L4, L27; Earth_and_the_Monster_Waves L4; NPC_Rosters_by_Era L4; The_Network L15-16, L25, L25-27 … | 26 |
| Ch2 | Domain | Monsters L10, L31; Book_06_Timeline L12, L34; Chapter_Digest_Book_06 L12, L34; Astral_Spaces_Zones_and_Surges L15; Spirit_Vault_and_Astral_Kingdom L15; Transformation_Zones L15; Reality_and_Genesis_Cores L21, L36, L39 | 12 |
| Ch3 | Needs of the Moment | Transformation_Zones L5, L39; Domains L28; Book_06_Timeline L39, L67; Chapter_Digest_Book_06 L39, L67 | 7 |
| Ch4 | A Beautiful Woman and a Sack of Cash | Alchemy_Artifice_and_Magical_Materials L6-8; Soul_Bound_Items_and_Regalia L6-8, L29-39, L34-37, L35-38, L40, L42-50 …; Glossary L6-8, L26-38; Jason_Asano L29-36; Book_06_Timeline L30, L40, L68; Chapter_Digest_Book_06 L30, L40; 00_Items_Overview L33; Cloud_Constructs_and_Palaces L42-50, L53 … | 23 |
| Ch5 | You Have to Be True to Yourself | Reality_and_Genesis_Cores L9; Astral_Spaces_Zones_and_Surges L32, L48; Locations_by_Era L41; Spirit_Vault_and_Astral_Kingdom L41, L53; Nitra L41; Book_06_Timeline L41, L72; Chapter_Digest_Book_06 L41, L72; Earth_and_the_Monster_Waves L41 … | 14 |
| Ch6 | One More Secret | Book_06_Timeline L7; Chapter_Digest_Book_06 L7; Li_Li_Mei L16-21; Gerling L26; Minor_Cast_Books_4-6 L31; Glossary L31; Reality_and_Genesis_Cores L35 | 7 |
| Ch7 | Instinct is All We Have | Book_06_Timeline L22; Chapter_Digest_Book_06 L22; Minor_Cast_Books_4-6 L22-23, L72; Reality_and_Genesis_Cores L76 | 5 |
| Ch8 | Step Back | Book_06_Timeline L3; Chapter_Digest_Book_06 L3; Reality_and_Genesis_Cores L3; Gerling L48; Monsters L73 | 5 |
| Ch9 | Guns & Money | Book_06_Timeline L7, L43; Chapter_Digest_Book_06 L7, L43 | 4 |
| Ch10 | Old Habit | Book_06_Timeline L3-5, L19-25; Chapter_Digest_Book_06 L3-5, L19-25; Domains L5; Cloud_Constructs_and_Palaces L34; 01_World_Primer L41; Calendar_Holidays_and_Naming_Customs L41; Daily_Life L41 | 9 |
| Ch11 | It’s Still Not About Killing Monsters | Book_06_Timeline L14; Chapter_Digest_Book_06 L14; Monsters L43 | 3 |
| Ch12 | Open to the Unanticipated | Book_06_Timeline L7, L59; Chapter_Digest_Book_06 L7, L59; Nitra L41, L59 | 6 |
| Ch13 | I’m Going to Bet on Myself | Book_06_Timeline L3, L77; Chapter_Digest_Book_06 L3, L77; Essence_Catalogue L68, L69; Confluences L69; Spirit_Vault_and_Astral_Kingdom L79 | 8 |
| Ch14 | No Perfect Options | Auras L6; Ranks_and_Advancement L6; Book_06_Timeline L31, L74; Chapter_Digest_Book_06 L31, L74; Unusual_and_Unique_Magic L78, L79, L80, L82; Confluences L79; Essence_Catalogue L79; Keeper_of_Moments L80 … | 15 |
| Ch15 | Stillness | Book_06_Timeline L3-7, L40; Chapter_Digest_Book_06 L3-7, L40; Monsters L4; Titles_and_Blessings L45; Nitra L45; Jason_Asano L45 | 8 |
| Ch16 | Whatever We Face | Essence_Catalogue L35; Nitra L60; Book_06_Timeline L60, L83; Chapter_Digest_Book_06 L60, L83 | 6 |
| Ch17 | You Really Aren’t Local | Book_06_Timeline L13, L37, L71; Chapter_Digest_Book_06 L13, L37; Earth_and_the_Monster_Waves L13, L37; Plot_Hooks L37; Era_3_Earth L37; Shako L41, L41-62, L43, L62, L68 | 14 |
| Ch18 | A Sliver of Hope | Dawn L3-9; Shako L4, L27, L79, L79-84; The_Builder L6; Book_06_Timeline L6, L39, L138; Chapter_Digest_Book_06 L6, L39; Earth_and_the_Monster_Waves L6; The_Builders_Door_and_Fundament_Gate L11, L30-36, L39, L124; World_Phoenix L65 … | 20 |
| Ch19 | End-User Licence Agreement | Shako L5; Spirit_Vault_and_Astral_Kingdom L21, L62; Book_06_Timeline L21, L65; Chapter_Digest_Book_06 L21, L65; Minor_Cast_Books_4-6 L27; Gerling L35; Goblins_and_Fairies L40 | 10 |
| Ch20 | Negotiations | Book_06_Timeline L38, L81; Chapter_Digest_Book_06 L38, L81; Earth_and_the_Monster_Waves L81 | 5 |
| Ch21 | Another Day for Vampires | Book_06_Timeline L4, L31, L63, L76; Chapter_Digest_Book_06 L4, L31 | 6 |
| Ch22 | Less Freud and More God of Healing | Book_06_Timeline L5, L52; Chapter_Digest_Book_06 L5, L52 | 4 |
| Ch23 | Little Cost in Exploring | Book_06_Timeline L3, L31; Chapter_Digest_Book_06 L3; Era_Selection L3; Plot_Hooks L3; Era_3_Earth L3; Domains L9; Anna_Tilden L15; Emi_Evans_Asano L31 … | 14 |
| Ch24 | Intentions | Anna_Tilden L3, L4, L5; Book_06_Timeline L6; Chapter_Digest_Book_06 L6; Gods_and_Churches L86; Minor_Cast_Books_1-3 L87 | 7 |
| Ch25 | I Need That Song to Play Out | Minor_Cast_Books_1-3 L18-21; Yumi_Asano L55; The_Cabal L60-64, L61; Book_06_Timeline L79, L102; Chapter_Digest_Book_06 L79, L102; Earth_Powers L98-99; Mr_North L107-113, L117 | 11 |
| Ch26 | Wash Them First | Farrah_Hurin L9; Tone_and_Voice L9; NPC_Cards_Books_01-03 L9; Adrien_Barbou L9-20; Book_06_Timeline L63, L71; Chapter_Digest_Book_06 L63, L71; Earth_and_the_Monster_Waves L63; Confluences L94 … | 12 |
| Ch27 | The Language of Passion | Book_06_Timeline L51; Chapter_Digest_Book_06 L51; Earth_and_the_Monster_Waves L51 | 3 |
| Ch28 | Forthright Honesty | Travis_Noble L36, L36-37, L65; Book_06_Timeline L36; Chapter_Digest_Book_06 L36; Earth_and_the_Monster_Waves L36; NPC_Rosters_by_Era L36; Minor_Cast_Books_4-6 L37-39 | 8 |
| Ch29 | Pertinent Factor | Colin L10; Minor_Cast_Books_4-6 L13; Glossary L32; Travis_Noble L52; Book_06_Timeline L84; Chapter_Digest_Book_06 L84 | 6 |
| Ch30 | More of a Focus on Nipples | Engineers_of_Ascension L29, L58-60; Book_06_Timeline L29; Chapter_Digest_Book_06 L29; Gerling L29-44; Adrien_Barbou L40-43; Open_Questions L43; Mr_North L56-58 | 8 |
| Ch31 | The Job That’s in Front of You | Book_06_Timeline L4, L62; Chapter_Digest_Book_06 L4, L62; Era_Selection L4; Plot_Hooks L4 | 6 |
| Ch32 | Going Suspiciously Well | Book_06_Timeline L42, L51, L72; Chapter_Digest_Book_06 L42, L51 | 5 |
| Ch33 | One of Asano’s Secrets | Book_06_Timeline L6; Chapter_Digest_Book_06 L6 | 2 |
| Ch34 | Swarm Against Swarm | Book_06_Timeline L6, L51; Chapter_Digest_Book_06 L6, L51 | 4 |
| Ch35 | Necessary Evil | Mr_North L6; Book_06_Timeline L15, L112; Chapter_Digest_Book_06 L15, L112; The_Deep_Astral_and_Interstice L39, L39-40; World_Phoenix L42; Velius L50; Open_Questions L68, L78-80; Glossary L73 … | 14 |
| Ch36 | Balls | Gerling L33; Book_06_Timeline L73; Chapter_Digest_Book_06 L73 | 3 |
| Ch37 | Which One of Us is the Villain | Henrietta_Geller L93; Book_06_Timeline L93; Chapter_Digest_Book_06 L93 | 3 |
| Ch38 | That Passion Didn’t Come From Nowhere | Mr_North L3, L71; Book_06_Timeline L21; Chapter_Digest_Book_06 L21; Gordon L35; Minor_Cast_Books_4-6 L76-81 | 6 |
| Ch39 | The Upstart Magician | Book_06_Timeline L12; Chapter_Digest_Book_06 L12; Incursion_Sites L25; Saint-Etienne L25; Monster_Cores_and_Training L25-27, L27; Minor_Cast_Books_4-6 L25-27; Earth_Powers L71-74 | 8 |
| Ch40 | Too Much Over Pride | The_Cabal L18; Book_06_Timeline L18; Chapter_Digest_Book_06 L18; Earth_Vampire_War L18; Domains L30 | 5 |
| Ch41 | Trust All the Way | Book_06_Timeline L8, L39, L111; Chapter_Digest_Book_06 L8, L39; Elizabeth L81, L81-82, L82; NPC_Cards_Books_04-06 L81; Calendar_Holidays_and_Naming_Customs L116-117 | 10 |
| Ch42 | Time to Choose | Gerling L20, L66; Adrien_Barbou L22; NPC_Cards_Books_04-06 L22; Book_06_Timeline L101; Chapter_Digest_Book_06 L101 | 6 |
| Ch43 | Four-Score Men | Gerling L7; Book_06_Timeline L18, L48; Chapter_Digest_Book_06 L18, L48; Ranks_and_Advancement L52; Saint-Etienne L71; Adrien_Barbou L75 | 8 |
| Ch44 | The Very Opposite of Fantastical | Book_06_Timeline L4; Chapter_Digest_Book_06 L4; Emir_Bahadir L12; Elizabeth L21; Saint-Etienne L25-31; Open_Questions L25-31 | 6 |
| Ch45 | Small Mercies | Saint-Etienne L3; Book_06_Timeline L34; Chapter_Digest_Book_06 L34; Elizabeth L39, L39-40; Earth_Vampire_War L39-40 | 6 |
| Ch46 | Salus Mundi Suprema Lex Esto | Titles_and_Blessings L28; Monsters L31; Saint-Etienne L31; Book_06_Timeline L31, L53, L81, L104; Chapter_Digest_Book_06 L31, L53; Domains L104; Mr_North L112-113, L112-127, L117-125; Gerling L112-127 | 14 |
| Ch47 | Something Other Than Human | 01_World_Primer L3, L390, L623, L703; Book_06_Timeline L3, L4, L5, L14, L16, L93 …; Chapter_Digest_Book_06 L3, L4; Earth_and_the_Monster_Waves L3, L155, L941; Plot_Hooks L3, L155; Master_Timeline L4, L155; Vampire_War L5; Earth_Vampire_War L5 … | 187 |

### Book 7

| Chapter | Title | Cited by (lines) | Rows |
|---|---|---|---|
| Ch1 | Of Course He Doesn’t Have Pants | Book_07_Timeline L5, L30, L56; Chapter_Digest_Book_07 L5, L56; Rimaros_Surge L5, L30, L56; Era_Selection L5, L16, L56; Kaito_Asano L15; NPC_Cards_Books_01-03 L15; Farrah_Hurin L16; Spirit_Vault_and_Astral_Kingdom L18 … | 22 |
| Ch2 | Connotations | Book_07_Timeline L13, L76; Chapter_Digest_Book_07 L13, L76; Zartos L71, L71-72, L71-75, L75; Zartos_Culture L71-72, L75; Gary L71-74; Jason_Asano L73-74; Soul_Bound_Items_and_Regalia L73-74; Celestines L75 … | 17 |
| Ch3 | What a Monster Surge Feels Like | Jory_Tillman L3; Book_07_Timeline L29, L42, L51; Chapter_Digest_Book_07 L29, L42, L51; 00_Places_Overview L44-47; Rimaros L44-47; Storm_Kingdom_Islands L44-47; Storm_Kingdom_Culture L47, L82; Rimaros_Surge L51 | 13 |
| Ch4 | Strategic Doctrine | Book_07_Timeline L6; Chapter_Digest_Book_07 L6; Jory_Tillman L25, L76; NPC_Cards_Books_01-03 L25; Knowledge L58; Shimmer L78 | 7 |
| Ch5 | I’ve Seen Your Best | Book_07_Timeline L13, L56; Chapter_Digest_Book_07 L13, L56; Rimaros_Surge L13, L56; Adventuring_Profession L25; Era_4_Rimaros L56, L65; Storm_Kingdom_Culture L65, L67, L69; Era_Selection L65; Rimaros L67 … | 16 |
| Ch6 | Responsible Dad | Motifs_and_Sayings L13-29; Belinda_Callahan L42; Tone_and_Voice L42; NPC_Cards_Books_01-03 L42; Onslow L52; Stash L87; Book_07_Timeline L88; Chapter_Digest_Book_07 L88 | 8 |
| Ch7 | Surge Protocols | 01_World_Primer L3, L70; Burning_Violet L53; Farrah_Hurin L53; Guilds_and_Houses L53-54; Book_07_Timeline L58, L64; Chapter_Digest_Book_07 L58, L64; Rimaros_Surge L58, L64; Death L64 … | 23 |
| Ch8 | Disappointed or Relieved | Dawn L3; Book_07_Timeline L36, L82; Chapter_Digest_Book_07 L36, L82; One_Day_War L36; Rimaros_Surge L36; Who_Knows_What_When L36; Era_4_Rimaros L36 | 9 |
| Ch9 | More Paperwork | Church_of_Knowledge L3-4; Knowledge L4; Education L4; Religion_in_Practice L4, L9; Rufus_Remore L6, L18; Book_07_Timeline L7, L25, L88; Chapter_Digest_Book_07 L7, L25; NPC_Rosters_by_Era L7 … | 26 |
| Ch10 | Multi-Talented | Rimaros L5; Storm_Kingdom_Islands L5; Monsters L19; Ranks_and_Advancement L19; Alchemy_Artifice_and_Magical_Materials L38; Book_07_Timeline L52; Chapter_Digest_Book_07 L52; Church_of_Death L55 … | 10 |
| Ch11 | Don’t Say You Weren’t Warned | Book_07_Timeline L5; Chapter_Digest_Book_07 L5; Rimaros_Surge L5; Who_Knows_What_When L5; Era_4_Rimaros L5; Clothing_Food_Festivals_and_Transport_by_Region L62; Liara_Rimaros L65; Titles_and_Blessings L73-75, L75, L78 … | 15 |
| Ch12 | Contribution | Adventure_Society L14-15, L23; Adventuring_Profession L15, L23; Guild_Quotas_and_Contribution L15, L17, L19, L19-21, L21, L23; Economy_and_Money L15-21; Alchemy_Association L19; Tone_and_Voice L22-23; Era_1_Greenstone L22-23; Book_07_Timeline L23, L57, L69 … | 25 |
| Ch13 | Small-Town Lifestyle | NPC_Rosters_by_Era L18, L51; Argy L18-20, L20, L24, L28, L28-32, L31 …; Palisaros L20-35, L33, L34, L35; Pelli L28, L28-99, L51, L74, L99; Rimaros L28-30; Era_4_Rimaros L31, L51; Locations_by_Era L33; Book_07_Timeline L75 … | 26 |
| Ch14 | I Don’t Need to Invent Ice Cream | Book_07_Timeline L9, L44; Chapter_Digest_Book_07 L9, L44; Emir_Bahadir L21; Knowledge_States L29; Glossary L41; Clothing_Food_Festivals_and_Transport_by_Region L52; Jayapura_Culture L52; Jayapura L52 … | 11 |
| Ch15 | Remaining Unremarkable | Runics L5; Church_of_Knowledge L40; Book_07_Timeline L40, L77; Chapter_Digest_Book_07 L40, L77; Pelli L65-71, L67, L67-71; Family_Trees L67, L110-113; Zara_Rimaros L74, L110-113, L114-115 | 14 |
| Ch16 | A Damn Fine Way to Start Off a War | Burning_Violet L3, L9; Book_07_Timeline L3, L51, L75; Chapter_Digest_Book_07 L3, L51; Miles_Cotezee L3-75; Church_of_the_Healer L6; Jory_Tillman L6; Ken_Asano L42; Rimaros_Surge L51 … | 14 |
| Ch17 | It Will Not Be Fine | Clothing_Food_Festivals_and_Transport_by_Region L3, L16; House_Rimaros L3, L22; Liara_Rimaros L3, L14, L15, L19-20, L20; Book_07_Timeline L3, L104, L111; Chapter_Digest_Book_07 L3, L111; Era_4_Rimaros L3; Family_Trees L14, L19-20; Romances_and_Rivalries L19-20 … | 37 |
| Ch18 | A Story of War | Clothing_Food_Festivals_and_Transport_by_Region L3; Book_07_Timeline L25, L42, L48; Chapter_Digest_Book_07 L25, L42, L48; Pelli L28; NPC_Cards_Books_07-09 L28, L49; Soramir L41-42, L41-49, L49; Calendar_Holidays_and_Naming_Customs L42; Storm_Kingdom_Culture L42 … | 29 |
| Ch19 | Any Help They Can Get | Book_07_Timeline L21, L71; Chapter_Digest_Book_07 L21, L71; Guild_Quotas_and_Contribution L62, L73; Minor_Cast_Books_7-9 L95 | 7 |
| Ch20 | Little Man Problems | Minor_Cast_Books_7-9 L21, L84; Adventuring_Profession L23; Dimensional_Storage_and_Portals L23; Book_07_Timeline L47; Chapter_Digest_Book_07 L47; Gods_and_Churches L54 | 7 |
| Ch21 | Enemies Even I Would Fear | Fertility L3, L3-5; Storm_Kingdom_Culture L11; Guilds_and_Houses L11; Sapphire_Crown L11, L12, L13, L15, L32; House_Rimaros L11; Rimaros L12; NPC_Rosters_by_Era L13; Era_4_Rimaros L13 … | 23 |
| Ch22 | True Elites | Gabriel_Remore L81; Book_07_Timeline L92; Chapter_Digest_Book_07 L92; Trenchant_Moore L93 | 4 |
| Ch23 | Diligent and Considerate | Book_07_Timeline L9; Chapter_Digest_Book_07 L9 | 2 |
| Ch24 | That Doesn’t Make the Pebble Important | Vitesse L3; House_Geller L4; Book_07_Timeline L37; Chapter_Digest_Book_07 L37 | 4 |
| Ch25 | They Don’t Send Their Best People | Vitesse L3; Open_Questions L3; Miles_Cotezee L4; Book_07_Timeline L4, L78; Chapter_Digest_Book_07 L4, L78; 00_Places_Overview L77; Arcazitlan L77, L77-78, L78; Rimaros_Surge L78 … | 14 |
| Ch26 | An Old Friend That He Had No Time For | Book_07_Timeline L7; Chapter_Digest_Book_07 L7; Colin L22; Gordon L29; Arcazitlan L48 | 5 |
| Ch27 | Never Underestimate Adventurers | Book_07_Timeline L21; Chapter_Digest_Book_07 L21 | 2 |
| Ch28 | Better Strange Than Scary | Arcazitlan L3; Book_07_Timeline L7, L107; Chapter_Digest_Book_07 L7, L107; Alchemy_Artifice_and_Magical_Materials L106 | 6 |
| Ch29 | Going Overland | Book_07_Timeline L7; Chapter_Digest_Book_07 L7; Arcazitlan L8 | 3 |
| Ch30 | Small | Minor_Cast_Books_7-9 L5-17; Book_07_Timeline L28, L36; Chapter_Digest_Book_07 L28, L36 | 5 |
| Ch31 | Uneasy Allies | Book_07_Timeline L9; Chapter_Digest_Book_07 L9; Afflictions_Boons_and_Damage L10; Confluences L12; Ken_Asano L12; Arcazitlan L42 | 6 |
| Ch32 | Supply Chain Problems | Melody_Jain L7, L7-8, L8; Book_07_Timeline L7; Chapter_Digest_Book_07 L7; NPC_Cards_Books_04-06 L7-8; Minor_Cast_Books_7-9 L51, L86 | 8 |
| Ch33 | The Hitting-It-a-Bunch Plan | Book_07_Timeline L17, L112; Chapter_Digest_Book_07 L17, L112 | 4 |
| Ch34 | I Liked the Fighting Better | Book_07_Timeline L77; Chapter_Digest_Book_07 L77 | 2 |
| Ch35 | That Usually is My Day | Book_07_Timeline L8; Chapter_Digest_Book_07 L8; Gods_and_Churches L39; Trenchant_Moore L72 | 4 |
| Ch36 | Unyielding Faith | Henrietta_Geller L8; The_Deep_Astral_and_Interstice L14; Book_07_Timeline L47; Chapter_Digest_Book_07 L47; Messenger_War L47; Miles_Cotezee L65; Outworlders L86; Master_Timeline L86 … | 11 |
| Ch37 | Something He Could Never Get Back | Book_07_Timeline L3, L57, L59; Chapter_Digest_Book_07 L3, L57; Monster_Cores_and_Training L4; Knowledge_States L6; Taika L25; Monsters L59; Alchemy_Association L62; Rimaros L64 | 11 |
| Ch38 | Dignified Young Adventurer | Astral_Spaces_Zones_and_Surges L6; Adventuring_Profession L7; Guild_Quotas_and_Contribution L7; Runics L10; Liara_Rimaros L91; Book_07_Timeline L92, L98; Chapter_Digest_Book_07 L92, L98 | 9 |
| Ch39 | I Can Do Sleazy | Fertility L74; Book_07_Timeline L79; Chapter_Digest_Book_07 L79 | 3 |
| Ch40 | An Object Lesson in Foolish Risks | Rimaros L4; Storm_Kingdom_Islands L4; Book_07_Timeline L7, L9; Chapter_Digest_Book_07 L7, L9; Education L26; Alchemy_Artifice_and_Magical_Materials L54 | 8 |
| Ch41 | Murky Waters | Kasper_Irios L3, L3-10, L3-46, L11-12, L26, L41 …; Book_07_Timeline L3, L73; Chapter_Digest_Book_07 L3, L73; NPC_Rosters_by_Era L3; NPC_Cards_Books_07-09 L26; Palisaros L61 | 14 |
| Ch42 | Integrity is Forever | Glossary L6; Book_07_Timeline L29, L92; Chapter_Digest_Book_07 L29, L92; Minor_Cast_Books_7-9 L61 | 6 |
| Ch43 | How Deep a Hole | Vitesse L18, L58; Rimaros L47; Minor_Cast_Books_7-9 L47; Estercost_Culture L58; Cyrion L58; Glossary L58; Open_Questions L58; Danielle_Geller L61, L61-62 … | 15 |
| Ch44 | The Part That Knows How to Quit | Book_07_Timeline L3-5, L23, L30; Chapter_Digest_Book_07 L3-5, L23; Adventuring_Profession L7; Pain_and_Discord L23; Amos_Pensinata L30; Taika L61; Travis_Noble L61 | 10 |
| Ch45 | Bad Apples | NPC_Rosters_by_Era L54; Book_07_Timeline L61; Chapter_Digest_Book_07 L61; Education L79; Fertility L106; House_Geller L106 | 6 |
| Ch46 | Idiot Plan | Book_07_Timeline L19, L40; Chapter_Digest_Book_07 L19, L40; Soramir L74, L74-98, L86, L98; Trenchant_Moore L74, L81; Roland_Remore L78 | 11 |
| Ch47 | The Days They Sing Songs About | Jeni_Kavaloa L33, L33-60, L39, L41-49, L60; Book_07_Timeline L33, L39; Chapter_Digest_Book_07 L33, L39; Rimaros_Surge L33; NPC_Rosters_by_Era L33, L39, L54; NPC_Cards_Books_07-09 L33; Teams_by_Era L33-60; Amos_Pensinata L39 … | 25 |
| Ch48 | The Source of the Madness | Orin_Pensinata L7; Korinne_Pescos L16; Jeni_Kavaloa L21; Book_07_Timeline L33, L45, L58; Chapter_Digest_Book_07 L33, L45; Saint-Etienne L36; Mr_North L36 | 10 |
| Ch49 | A Fair Fight | Book_07_Timeline L21; Chapter_Digest_Book_07 L21; Jeni_Kavaloa L39 | 3 |
| Ch50 | Put the Mask Back On | The_Builders_Door_and_Fundament_Gate L8; Book_07_Timeline L15, L55; Chapter_Digest_Book_07 L15, L55; Korinne_Pescos L51 | 6 |
| Ch51 | I Don’t Think You’re Angry | Jeni_Kavaloa L5; Book_07_Timeline L5, L90; Chapter_Digest_Book_07 L5, L90; Rimaros_Surge L5 | 6 |
| Ch52 | Staying with Friends | Minor_Cast_Books_7-9 L50; Book_07_Timeline L51, L66; Chapter_Digest_Book_07 L51, L66; Leonids L66; Outworlders L66; Liara_Rimaros L71; Soramir L71; Rimaros L73 … | 11 |
| Ch53 | Meanwhile, Two Weeks Ago in Vitesse | Book_07_Timeline L12, L38, L75; Chapter_Digest_Book_07 L12, L38; Trenchant_Moore L102 | 6 |
| Ch54 | Hegemon’s Will | Celestines L87; Dawn L87; Spoiler_Management L87; NPC_Cards_Books_01-03 L87; Zartos L108-120; Gary L108-120; Jason_Asano L108-120; Soul_Bound_Items_and_Regalia L108-120 … | 29 |
| Ch55 | A Story About a Magic Trowel | The_Deep_Astral_and_Interstice L16; Knowledge_States L20; Emi_Evans_Asano_Power_Set L35; Farrah_Hurin_Power_Set L35; Emi_Evans_Asano L35; Book_07_Timeline L40, L79; Chapter_Digest_Book_07 L40, L79; Landemere_Vane L64, L64-79 … | 14 |
| Ch56 | What It Sent Us | Soramir L6; NPC_Cards_Books_07-09 L6; Book_07_Timeline L62, L74; Chapter_Digest_Book_07 L62, L74; Master_Timeline L62; Church_of_Knowledge L62-66; Travis_Noble L71; Rimaros_Surge L74 … | 12 |
| Ch57 | I Am Not Jason Asano | Book_07_Timeline L3, L27; Chapter_Digest_Book_07 L3, L27; Rimaros_Surge L3; Stash L34; House_Geller L72; House_Remore L72 | 8 |
| Ch58 | That Powerful and That Old | Dimensional_Storage_and_Portals L10; Sendira L38; Minor_Cast_Order_of_Redeeming_Light L38; Book_07_Timeline L38, L76; Chapter_Digest_Book_07 L38, L76; Rimaros_Surge L38; Melody_Jain L38-46; Sophie_Wexler L38-46 … | 11 |
| Ch59 | One Battle at a Time | Book_07_Timeline L8, L86, L124, L129; Chapter_Digest_Book_07 L8, L86; Runics L65; House_Kettering L65; Dustin_Kettering L65; Rick_Geller L65, L65-72, L122; Rimaros_Surge L65-72, L86; Minor_Cast_Books_7-9 L73 … | 21 |
| Ch60 | No One Telling Me I Can’t | Great_Astral_Beings L27; Religion_in_Practice L27; Dawn L27, L27-30; Soramir L27; Book_07_Timeline L27, L94; Chapter_Digest_Book_07 L27, L94; Alchemy_Association L94; Rimaros_Surge L94 … | 13 |
| Ch61 | A Lot More Steps | Palisaros L59, L60; Book_07_Timeline L66; Chapter_Digest_Book_07 L66 | 4 |
| Ch62 | A Normal Man | Rimaros L3, L43; Book_07_Timeline L38, L43; Chapter_Digest_Book_07 L38, L43; Estella_Warnock L41, L79; NPC_Rosters_by_Era L79 | 9 |
| Ch63 | This One Time | Book_07_Timeline L26; Chapter_Digest_Book_07 L26; World_Phoenix L111 | 3 |
| Ch64 | Between Mortal and Something Else | One_Day_War L10-12, L14, L15-16, L17, L18, L20-25 …; Book_07_Timeline L14, L40, L72; Chapter_Digest_Book_07 L14, L40; Rimaros L21; Storm_Kingdom_Islands L21; Pelli L25 | 16 |
| Ch65 | Stand at the Front | Locations_by_Era L6; Soramir L6; One_Day_War L17-19, L18, L20, L21, L27, L28-30 …; Book_07_Timeline L19, L21, L77; Chapter_Digest_Book_07 L19, L21; Rimaros_Surge L21; Travis_Noble L44 | 21 |
| Ch66 | The End of the World | Book_07_Timeline L4, L9, L27, L36, L96; Chapter_Digest_Book_07 L9, L27; Arabelle_Remore L18; Book_08_Timeline L27; Master_Timeline L27; One_Day_War L27, L29, L33, L34, L36, L37-44 …; Rimaros_Surge L27; Era_Selection L27 … | 24 |

### Book 8

| Chapter | Title | Cited by (lines) | Rows |
|---|---|---|---|
| Ch1 | Band of Misfits | Book_08_Timeline L3, L7, L54; Chapter_Digest_Book_08 L3, L7; Mr_North L57 | 6 |
| Ch2 | The Pile of Disturbing Things | Book_08_Timeline L34, L53; Chapter_Digest_Book_08 L34, L53; Church_of_the_Healer L49; Arabelle_Remore L49; Spirit_Vault_and_Astral_Kingdom L57-63 | 7 |
| Ch3 | Information Exchange | Book_08_Timeline L33, L34, L39, L65; Minor_Cast_Books_7-9 L38; Minor_Cast_Order_of_Redeeming_Light L38, L39-58; Chapter_Digest_Book_08 L39, L65 | 9 |
| Ch4 | Tampering With That Kind of Power | Book_08_Timeline L3, L83; Chapter_Digest_Book_08 L3, L83; Knowledge_States L92-104; Dawn L116 | 6 |
| Ch5 | You Don’t Have it in You | Estella_Warnock L7; Book_08_Timeline L7; Chapter_Digest_Book_08 L7 | 3 |
| Ch6 | Good Luck Fighting Evil | Book_08_Timeline L4, L16, L21; Chapter_Digest_Book_08 L4, L21; Church_of_Knowledge L6; Gabrielle_Pellin L6; Travis_Noble L6; Monsters L21 | 9 |
| Ch7 | Special Boy | Liara_Rimaros L4; Book_08_Timeline L4; Chapter_Digest_Book_08 L4; Rimaros_Surge L4; Clive_Standish_Power_Set L36, L48, L60, L61; Neil_Davone_Power_Set L49, L50, L60, L100 | 12 |
| Ch8 | Strictly Necessary | Book_08_Timeline L12; Chapter_Digest_Book_08 L12; Belinda_Callahan_Power_Set L22, L33, L43, L67; Sophie_Wexler_Power_Set L54 | 7 |
| Ch9 | Opportunists | Book_08_Timeline L3, L11; Chapter_Digest_Book_08 L3, L11; Rimaros_Surge L3, L11; Minor_Cast_Books_7-9 L11; Minor_Cast_Order_of_Redeeming_Light L11, L30, L49; Glossary L11; Sendira L14, L17, L21; Monster_Cores_and_Training L35-36, L37 … | 22 |
| Ch10 | A Bland Kind of Alchemy | Book_08_Timeline L5; Chapter_Digest_Book_08 L5; Purity_and_Disguise L24; Onslow L29; Stash L29; Colin L30; Neil_Davone_Power_Set L31; Belinda_Callahan_Power_Set L41 | 8 |
| Ch11 | Ideal Enemy | Book_08_Timeline L8, L9; Chapter_Digest_Book_08 L8, L9; Sophie_Wexler_Power_Set L13, L23, L32, L42, L52, L66 … | 12 |
| Ch12 | Trying to Kill Jason Again | Adventuring_Profession L5; Confluences L5; Essence_Catalogue L5; Book_08_Timeline L5, L59; Chapter_Digest_Book_08 L5, L59; Clive_Standish_Power_Set L30; Carlos_Quilido L61 | 9 |
| Ch13 | Here to Steal | Sendira L3, L6, L51, L54; Book_08_Timeline L6; Chapter_Digest_Book_08 L6; Minor_Cast_Order_of_Redeeming_Light L47-51 | 7 |
| Ch14 | Not Really a Rules Guy | Book_08_Timeline L13, L24, L31, L60; Chapter_Digest_Book_08 L13, L24; Titles_and_Blessings L24; Sendira L59, L67, L70-72; Minor_Cast_Order_of_Redeeming_Light L71 | 11 |
| Ch15 | A Comparison He Could Avoid | Book_08_Timeline L30, L56; Chapter_Digest_Book_08 L30, L56; Domains L47 | 5 |
| Ch16 | Portal Logistics | Book_08_Timeline L19, L28; Chapter_Digest_Book_08 L19, L28; Minor_Cast_Books_7-9 L28; Minor_Cast_Order_of_Redeeming_Light L28; Sendira L29, L82, L85-92; Dimensional_Storage_and_Portals L90 | 10 |
| Ch17 | It Won’t Be a Good Reason | Minor_Cast_Order_of_Redeeming_Light L5, L29; Book_08_Timeline L5, L23; Chapter_Digest_Book_08 L5, L23; Killian_Laurent L8, L28; Fertility L12; Sapphire_Crown L19; Gods_and_Churches L45; The_Healer L45 … | 13 |
| Ch18 | Bait and Switch | Cults_and_Orders L3-6; Melody_Jain L3-6, L8; NPC_Rosters_by_Era L3-6; Era_4_Rimaros L3-6; Minor_Cast_Books_7-9 L4-25, L68; Minor_Cast_Order_of_Redeeming_Light L4-34, L14, L68; Sendira L8, L80; Book_08_Timeline L21 … | 17 |
| Ch19 | That Kind of Power Can Be Lonely | Book_08_Timeline L29, L51; Chapter_Digest_Book_08 L29, L51; Authority_and_Sanctioning L40; Great_Astral_Beings L40; World_Phoenix L54 | 7 |
| Ch20 | Blame | Liara_Rimaros L3, L11, L14-57, L21, L57; Cults_and_Orders L4; House_Amouz L4, L14-19, L53; Minor_Cast_Books_7-9 L4; Book_08_Timeline L4; Chapter_Digest_Book_08 L4; Plot_Hooks L4; Era_4_Rimaros L4 … | 16 |
| Ch21 | Speed | Book_08_Timeline L8; Chapter_Digest_Book_08 L8; Sophie_Wexler_Power_Set L12, L23, L36; Celestines L40 | 6 |
| Ch22 | Delicate Flowers | Sophie_Wexler_Power_Set L13, L37; Book_08_Timeline L36; Chapter_Digest_Book_08 L36; Celestines L37; Sophie_Wexler L37-38 | 6 |
| Ch23 | Hope | Book_08_Timeline L28; Chapter_Digest_Book_08 L28; Essence_Catalogue L31 | 3 |
| Ch24 | Preferred Option | Casallini L21, L21-30, L22, L24-25, L25, L26 …; 01_World_Primer L22; Girlano_Culture L22, L22-23, L24-25, L26; Girlano L22, L22-23, L23, L24-25, L25, L26; Storm_Kingdom_Islands L22, L25, L26; Book_08_Timeline L22, L58; Chapter_Digest_Book_08 L22, L58; Adventure_Society L22-25 | 26 |
| Ch25 | Sloppy Mistake | Motifs_and_Sayings L28; Gordon L48; Casallini L117-130, L119, L127-130, L133-138, L136; Girlano_Culture L119, L120, L136; Girlano L120; Book_08_Timeline L130; Chapter_Digest_Book_08 L130; Secrets_and_Rumours L135 … | 15 |
| Ch26 | Criteria | Dimensional_Storage_and_Portals L5; Casallini L7, L39, L39-72, L43-45, L54, L66; Liara_Rimaros L15; Book_08_Timeline L23; Chapter_Digest_Book_08 L23; Minor_Cast_Books_7-9 L29; Girlano_Culture L39; Storm_Kingdom_Islands L43-45 | 13 |
| Ch27 | A Matter of Values | Book_08_Timeline L10, L26; Chapter_Digest_Book_08 L10, L26; Callum_Morse L26; Emir_Bahadir L34; Arabelle_Remore L88 | 7 |
| Ch28 | A Little Damage | Book_08_Timeline L14, L38; Chapter_Digest_Book_08 L14, L38; House_Geller L45; Palisaros L59 | 6 |
| Ch29 | Infiltrating the Stronghold | Book_08_Timeline L22; Chapter_Digest_Book_08 L22; Minor_Cast_Order_of_Redeeming_Light L26-29; Minor_Cast_Books_7-9 L28; Belinda_Callahan_Power_Set L49-56; Belinda_Callahan L49-56 | 6 |
| Ch30 | Coming in Hot | Book_08_Timeline L3, L36, L54; Chapter_Digest_Book_08 L3, L36; Rimaros_Surge L3 | 6 |
| Ch31 | We Are Fighting Monsters | Hegemons_Will_and_Dominion L6; Book_08_Timeline L28, L33, L55; Chapter_Digest_Book_08 L33, L55; Rimaros_Surge L33 | 7 |
| Ch32 | Just Some Administrator | Book_08_Timeline L8; Chapter_Digest_Book_08 L8 | 2 |
| Ch33 | Family Issues | Sendira L16, L22; Cults_and_Orders L18-19; Book_08_Timeline L21, L74, L79; Chapter_Digest_Book_08 L21, L74; Minor_Cast_Order_of_Redeeming_Light L24, L45, L47; Minor_Cast_Books_7-9 L45, L64; Baseph_and_the_Rimaros_Children L64 | 14 |
| Ch34 | A Power That You’ve Overlooked | Melody_Jain L28, L28-84; Order_and_Cult_of_the_Reaper L41; Book_08_Timeline L41, L108; Hegemons_Will_and_Dominion L63; Chapter_Digest_Book_08 L108 | 7 |
| Ch35 | Nostalgia | Book_08_Timeline L12; Chapter_Digest_Book_08 L12 | 2 |
| Ch36 | Saving the Day With the Power of Quips | Essence_Catalogue L3, L4; Book_08_Timeline L66; Chapter_Digest_Book_08 L66 | 4 |
| Ch37 | Keep it Light | Clothing_Food_Festivals_and_Transport_by_Region L63; Baseph_and_the_Rimaros_Children L77; Book_08_Timeline L82; Chapter_Digest_Book_08 L82 | 4 |
| Ch38 | Enough to Kill You With Power to Spare | Book_08_Timeline L27, L42; Chapter_Digest_Book_08 L27, L42 | 4 |
| Ch39 | A Significantly Different Paradigm | Dimensional_Storage_and_Portals L16; Book_08_Timeline L42, L104, L204, L234; Chapter_Digest_Book_08 L42, L104; Clive_Standish_Power_Set L73, L222; The_Healer L146 | 10 |
| Ch40 | Something Drastic | Belinda_Callahan L7-13; Book_08_Timeline L12, L34; Chapter_Digest_Book_08 L12, L34; Liara_Rimaros L29 | 6 |
| Ch41 | Ridiculous New Soul Power | Book_08_Timeline L6, L58; Chapter_Digest_Book_08 L6, L58; Pelli L18; Carlos_Quilido L58, L64 | 7 |
| Ch42 | The Awakening of Mr Asano | Melody_Jain L5, L5-7; Book_08_Timeline L18, L28, L32; Chapter_Digest_Book_08 L18, L32; Stash L35; Korinne_Pescos L45 | 9 |
| Ch43 | We’re Adventurers | Gods_and_Churches L48-53; Religion_in_Practice L48-53; Spoiler_Management L48-53; Dominion L60; Book_08_Timeline L90; Chapter_Digest_Book_08 L90 | 6 |
| Ch44 | The Person in My Care | Book_08_Timeline L18, L50, L53; Chapter_Digest_Book_08 L18, L50; Minor_Cast_Order_of_Redeeming_Light L29-40; Rimaros L50 | 7 |
| Ch45 | I Love a Hypocrite | Minor_Cast_Books_7-9 L4; Book_08_Timeline L17; Chapter_Digest_Book_08 L17; Knowledge_States L61 | 4 |
| Ch46 | I’ve Told You Everything | Book_08_Timeline L50, L76; Chapter_Digest_Book_08 L50, L76 | 4 |
| Ch47 | Faith is Soul-Deep | Arabelle_Remore L37; Book_08_Timeline L37; Chapter_Digest_Book_08 L37 | 3 |
| Ch48 | Lest He Become a Monster Himself | Purity_and_Disguise L14, L16, L22, L22-26, L32; Gods_and_Churches L22-26, L40-60; Religion_in_Practice L22-26; Church_of_Purity L32; Spoiler_Management L39-41; Secrets_and_Rumours L41; Book_08_Timeline L42, L96; Chapter_Digest_Book_08 L42, L96 … | 19 |
| Ch49 | Quite a Lot of System Windows | Book_08_Timeline L50, L87, L106; Chapter_Digest_Book_08 L50, L87; Rimaros_Surge L87, L105; Great_Astral_Beings L89-91; Astral_Kings_and_Messengers L105; Progression_Tracks L105; Domains L105; Spirit_Vault_and_Astral_Kingdom L105 … | 17 |
| Ch50 | Reasons to Quietly Dread | Mr_North L52; Book_08_Timeline L65, L89; Chapter_Digest_Book_08 L65, L89; Rimaros_Surge L65; Familiars L82; Tone_and_Voice L82; 00_Items_Overview L87; Alchemy_Artifice_and_Magical_Materials L87-91 … | 17 |
| Ch51 | Authority | Open_Questions L30, L66, L68-74; Great_Astral_Beings L68-70; Tokens_Stones_and_Relics L68-70; Glossary L68-70; Book_08_Timeline L93; Chapter_Digest_Book_08 L93 | 8 |
| Ch52 | The Kind of Pain I’m Used To | Authority_and_Sanctioning L9, L11, L11-12, L51, L53, L56-57 …; Domains L11; Palisaros L20; Storm_Kingdom_Islands L20; Book_08_Timeline L49; Chapter_Digest_Book_08 L49; Shako L56, L56-60, L59-60 | 19 |
| Ch53 | A New Man | Authority_and_Sanctioning L24, L29; Book_08_Timeline L29; Chapter_Digest_Book_08 L29 | 4 |
| Ch54 | Negotiating Position | Shako L13, L115; Authority_and_Sanctioning L15-16, L17, L18-19, L19, L54, L60-61 …; The_Builder L19, L89-94; World_Phoenix L24-29, L112; Open_Questions L54, L60-61, L99; Book_08_Timeline L63, L99; Chapter_Digest_Book_08 L63, L99; Rimaros_Surge L63 | 21 |
| Ch55 | No Points of Conflict | Book_08_Timeline L4, L47; Chapter_Digest_Book_08 L4, L47; Great_Astral_Beings L25-31, L92, L92-93; Authority_and_Sanctioning L31-32; Umber L85-86, L86; Shade L85-86; Glossary L85-89; The_Deep_Astral_and_Interstice L92 … | 20 |
| Ch56 | Quite Enough Transcendent Beings | Book_08_Timeline L35; Chapter_Digest_Book_08 L35; Rimaros_Surge L35; Plot_Hooks L35; Dominion L47-48, L53-54; Church_of_Dominion L47-48 | 7 |
| Ch57 | Flavours of Authority | Authority_and_Sanctioning L25, L27, L33-35, L35, L62, L66 …; Domains L25, L66, L70; 00_Cosmology_Overview L25-35; The_Builders_Door_and_Fundament_Gate L28, L64-67; Knowledge_States L53-59, L56; Who_Knows_What_When L53-59; Book_08_Timeline L62; Chapter_Digest_Book_08 L62 … | 19 |
| Ch58 | Mythmaking Was Within Expectations | Calendar_Holidays_and_Naming_Customs L19; Book_08_Timeline L19, L34; Chapter_Digest_Book_08 L19, L34; Master_Timeline L19 | 6 |
| Ch59 | Dodging the Topic | Book_08_Timeline L6, L57; Chapter_Digest_Book_08 L6, L57; Rimaros_Surge L6; Dominion L36 | 6 |
| Ch60 | A Power That Did Not Belong to the World | Abilities_and_Attributes L5; Auras L5; Confluences L5; Book_08_Timeline L13; Chapter_Digest_Book_08 L13 | 5 |
| Ch61 | A Gentleman Doesn’t Tell | Carlos_Quilido L3; Book_08_Timeline L91; Chapter_Digest_Book_08 L91 | 3 |
| Ch62 | Recalibrate Their Expectations | Liara_Rimaros L28-32, L30, L39, L59; Family_Trees L28-39; Baseph_and_the_Rimaros_Children L32, L36, L39, L51; Zareen_Rimaros L32, L36, L54-59; Minor_Cast_Books_7-9 L32, L32-40, L39; Book_08_Timeline L32, L52; Chapter_Digest_Book_08 L32; NPC_Rosters_by_Era L32 … | 24 |
| Ch63 | Deeds of Legend | Baseph_and_the_Rimaros_Children L3; Minor_Cast_Books_7-9 L3; Book_08_Timeline L3-8, L76; Chapter_Digest_Book_08 L3-8; Secrets_and_Rumours L76; Zareen_Rimaros L106; Callum_Morse L140 | 8 |
| Ch64 | A King Needs a Throne | Book_08_Timeline L15, L47; Chapter_Digest_Book_08 L15, L47; Astral_Kings_and_Messengers L72-80; Messengers_as_a_People L72-80 | 6 |
| Ch65 | What Light Does | Book_08_Timeline L8, L31, L88, L94; Spirit_Vault_and_Astral_Kingdom L29-31, L30; Chapter_Digest_Book_08 L31, L94; Jason_Asano L85-93; Astral_Kings_and_Messengers L88; 00_Astral_Overview L88; Rimaros_Surge L88; Who_Knows_What_When L88 … | 17 |
| Ch66 | Why Anyone Would Pick You | Book_08_Timeline L44; Chapter_Digest_Book_08 L44 | 2 |
| Ch67 | Astral Emperor | Astral_Kings_and_Messengers L53; The_Deep_Astral_and_Interstice L53; Book_08_Timeline L53, L97; Chapter_Digest_Book_08 L53, L97 | 6 |
| Ch68 | Goodbyes | Book_08_Timeline L9, L50, L113; Chapter_Digest_Book_08 L9, L50 | 5 |

### Book 9

| Chapter | Title | Cited by (lines) | Rows |
|---|---|---|---|
| Ch1 | Don’t Show Up to the Fancy Party in Shorts | Book_09_Timeline L3-6, L103; Chapter_Digest_Book_09 L3-6, L103; Jonah_Geller L39; Minor_Cast_Books_7-9 L49, L50; Rick_Geller L59, L59-111, L83, L111; Phoebe_Geller L83 | 12 |
| Ch2 | What She Was Willing to Do | Clothing_Food_Festivals_and_Transport_by_Region L16-19, L20; Book_09_Timeline L18, L28, L76; Chapter_Digest_Book_09 L18, L76; Cole_Silva L84; Lucian_Lamprey L84; Builder_Cult_in_Greenstone L84; Killian_Laurent L85; Domains L107 | 12 |
| Ch3 | More Than Just a Name | Clothing_Food_Festivals_and_Transport_by_Region L3; Book_09_Timeline L56, L90; Chapter_Digest_Book_09 L56, L90; Rufus_Remore L59; Minor_Cast_Books_7-9 L75, L86; Rimaros L81-82; Storm_Kingdom_Islands L81-82 | 10 |
| Ch4 | The Making of That Man | Killian_Laurent L11, L11-39; Book_09_Timeline L11; Chapter_Digest_Book_09 L11; Minor_Cast_Books_7-9 L16 | 5 |
| Ch5 | A Lesson of Days Gone | Sapphire_Crown L3; House_Amouz L3; House_Rimaros L3; Liara_Rimaros L3; Family_Trees L3; Book_09_Timeline L4, L76; Chapter_Digest_Book_09 L4, L76; Ranks_and_Advancement L55 | 10 |
| Ch6 | Dear John | Dawn L17; Jason_Asano L17; Motifs_and_Sayings L17; Tone_and_Voice L17; Taika L41; Book_09_Timeline L41; Chapter_Digest_Book_09 L41; Battle_of_Yaresh L41 … | 12 |
| Ch7 | This Doesn’t Feel Glorious | Sapphire_Crown L4; Minor_Cast_Books_7-9 L33, L46, L92; Book_09_Timeline L33; Chapter_Digest_Book_09 L33 | 6 |
| Ch8 | El Demonio Que Hace Trofeos de los Hombres | Book_09_Timeline L3-12, L25; Chapter_Digest_Book_09 L3-12, L25; Minor_Cast_Books_7-9 L6, L12; Motifs_and_Sayings L30 | 7 |
| Ch9 | Occasionally Carnivorous | Minor_Cast_Books_7-9 L19, L57-58, L58, L62, L63; Book_09_Timeline L24, L42; Chapter_Digest_Book_09 L24, L42 | 9 |
| Ch10 | If You’re Going to Punish Someone | Essence_Catalogue L102; Minor_Cast_Books_7-9 L102, L103, L106; Book_09_Timeline L106; Chapter_Digest_Book_09 L106 | 6 |
| Ch11 | One More Loyalty to Balance | Book_09_Timeline L5; Chapter_Digest_Book_09 L5; Church_of_Death L44; Zareen_Rimaros L51, L53; Liara_Rimaros L53; Baseph_and_the_Rimaros_Children L60; Minor_Cast_Books_7-9 L60 | 8 |
| Ch12 | That Boy In the Tent | Book_09_Timeline L14; Chapter_Digest_Book_09 L14; Zareen_Rimaros L89, L108 | 4 |
| Ch13 | A Difficult Child | Minor_Cast_Books_7-9 L3; Book_09_Timeline L3; Chapter_Digest_Book_09 L3; Clothing_Food_Festivals_and_Transport_by_Region L3-25, L19-25; Zareen_Rimaros L45; Messenger_War L52; Gabrielle_Pellin L84-85; Church_of_Knowledge L85 … | 13 |
| Ch14 | All Singer and No Song | Storm_Kingdom_Islands L4; Soramir L4; Family_Trees L4; Book_09_Timeline L4; Chapter_Digest_Book_09 L4; Liara_Rimaros L5; House_Remore L7; Carlos_Quilido L7 … | 10 |
| Ch15 | Hefty Nuggets | Minor_Cast_Books_7-9 L14, L53, L67; Zareen_Rimaros L16, L103; Book_09_Timeline L114; Chapter_Digest_Book_09 L114 | 7 |
| Ch16 | Following Your Convictions to Your Death | Liara_Rimaros L3; Zareen_Rimaros L3; Book_09_Timeline L29; Chapter_Digest_Book_09 L29; Minor_Cast_Books_4-6 L50; Glossary L50 | 6 |
| Ch17 | The God in This Scenario | Sapphire_Crown L8; Book_09_Timeline L61; Chapter_Digest_Book_09 L61 | 3 |
| Ch18 | The Only Person Who Thinks It’s Obvious | Book_09_Timeline L3; Chapter_Digest_Book_09 L3; Zareen_Rimaros L15; Essence_Catalogue L54; Vitesse L70; Roland_Remore L70; Sapphire_Crown L98 | 7 |
| Ch19 | Uncharacteristic Sincerity | Melody_Jain L3; Sophie_Wexler L3-6; Book_09_Timeline L31; Chapter_Digest_Book_09 L31 | 4 |
| Ch20 | The Only Wound You Can Truly Suffer | Confluences L12; Rufus_Remore_Power_Set L12, L12-13, L14, L16, L20; Unusual_and_Unique_Magic L15; Essence_Catalogue L16; Education L26-27; House_Remore L26-27, L57; Book_09_Timeline L62; Chapter_Digest_Book_09 L62 | 13 |
| Ch21 | Mother’s Favourite | Book_09_Timeline L4, L47, L91; Chapter_Digest_Book_09 L4, L47; House_Davone L5; Knowledge_States L12; House_Geller L18, L20; Education L20; Jory_Tillman L32 | 11 |
| Ch22 | A Good Friend to Have | Book_09_Timeline L18; Chapter_Digest_Book_09 L18 | 2 |
| Ch23 | Put the Extraordinary Aside | Soramir L11; Astral_Kings_and_Messengers L44; Messenger_War L44; Who_Knows_What_When L44; Era_5_Yaresh L44; Book_09_Timeline L84; Chapter_Digest_Book_09 L84 | 7 |
| Ch24 | A Chance For Some Relative Quiet | Book_09_Timeline L30, L44, L49; Chapter_Digest_Book_09 L30, L49; Amos_Pensinata L35; Orin_Pensinata L35, L49; Master_Timeline L44; Korinne_Pescos L49-52; Teams_by_Era L49-52; Kalif L50, L52-55, L58, L64 … | 16 |
| Ch25 | Surplus to Requirements | 00_Places_Overview L4; Hornis L4; Africa_like_Continent L4; Book_09_Timeline L4; Chapter_Digest_Book_09 L4; Korinne_Pescos L31, L31-63, L58, L89; Kasper_Irios L79; Orin_Pensinata L79 | 11 |
| Ch26 | Bad at Crime | Girlano_Culture L3; Girlano L3; Book_09_Timeline L26, L64; Chapter_Digest_Book_09 L26, L64; Master_Timeline L26; Battle_of_Yaresh L26; Era_5_Yaresh L26; Thadwick_Mercer L57-58, L59 … | 16 |
| Ch27 | An Evil God Sitting on Her Shoulder | Carlos_Quilido L10; Celestial_Book L21; Order_and_Cult_of_the_Reaper L22-23, L24, L24-26, L26, L30, L47 …; Kurdansk_Culture L24; Melody_Jain L24; Glossary L24; Kurdansk L24-26; Fertility L26 … | 41 |
| Ch28 | A Responsibility as Much as a Privilege | Arabelle_Remore L3; Book_09_Timeline L31, L45, L108; Chapter_Digest_Book_09 L31, L45; The_Healer L44; Cults_and_Orders L45; Minor_Cast_Books_7-9 L45; Carlos_Quilido L47, L50; Orin_Pensinata L87-112 … | 14 |
| Ch29 | Fighting the Power | Rosa_Liselos L8; Book_09_Timeline L13, L14; Chapter_Digest_Book_09 L13, L14; Battle_of_Yaresh L13; Korinne_Pescos L14; Kalif L15; 00_Places_Overview L17; Locations_by_Era L17-18, L17-19 … | 15 |
| Ch30 | Make Jason Great Again | Book_09_Timeline L27, L119; Chapter_Digest_Book_09 L27, L119; Locations_by_Era L59; Cartise L59 | 6 |
| Ch31 | Neil’s Big Mouth | Locations_by_Era L11; Cartise L11; Book_09_Timeline L11, L40; Chapter_Digest_Book_09 L11, L40; Battle_of_Yaresh L11 | 7 |
| Ch32 | Rage, Authority and Otherworldly Power | Book_09_Timeline L15; Chapter_Digest_Book_09 L15 | 2 |
| Ch33 | Asset | Taika L14; Confluences L15; Humphrey_Geller_Power_Set L15; Taika_Power_Set L15; Humans L15; Humphrey_Geller L15; Book_09_Timeline L16; Chapter_Digest_Book_09 L16 … | 9 |
| Ch34 | The Thing You Practise With The Most | Book_09_Timeline L18, L74; Chapter_Digest_Book_09 L18, L74; Korinne_Pescos L74; Rosa_Liselos L86; Kalif L93 | 7 |
| Ch35 | Just to Prove You Could | Book_09_Timeline L11; Chapter_Digest_Book_09 L11; Cartise L60, L62 | 4 |
| Ch36 | A Matter of What You Want | Book_09_Timeline L3, L19, L57; Chapter_Digest_Book_09 L3, L19; Knowledge L21 | 6 |
| Ch37 | Where We End | Knowledge_States L24-28; Book_09_Timeline L48, L69; Chapter_Digest_Book_09 L48, L69 | 5 |
| Ch38 | People That You Didn’t Aggravate | Book_09_Timeline L5, L60; Chapter_Digest_Book_09 L5, L60; Travis_Noble L21 | 5 |
| Ch39 | Not You | Isart L12, L12-26, L16, L26; 00_Places_Overview L12-20; Book_09_Timeline L26, L91; Chapter_Digest_Book_09 L26, L91; Teams_by_Era L80; Korinne_Pescos L87 | 11 |
| Ch40 | Inventing a Man in Your Head | Book_09_Timeline L5; Chapter_Digest_Book_09 L5; Zara_Rimaros L7-13, L13, L18, L21, L55, L72; Family_Trees L18; Sapphire_Crown L43 | 10 |
| Ch41 | Doing Things That You Shouldn’t | Astral_Kings_and_Messengers L81; Korinne_Pescos L119; Teams_by_Era L119; Book_09_Timeline L119; Chapter_Digest_Book_09 L119; Battle_of_Yaresh L119; Era_5_Yaresh L119 | 7 |
| Ch42 | Quiet Professionalism | Book_09_Timeline L5, L31, L57, L74; Chapter_Digest_Book_09 L5, L57; Yaresh_Culture L26; 00_Places_Overview L26; Locations_by_Era L26, L80; Yaresh L26, L34; Era_Selection L26, L80; Era_5_Yaresh L26, L80 … | 28 |
| Ch43 | A Man of Many Talents | Yaresh_Culture L33; Yaresh L33; Estella_Warnock L33; Book_09_Timeline L33, L72; Chapter_Digest_Book_09 L33, L72; Battle_of_Yaresh L33, L72; Clothing_Food_Festivals_and_Transport_by_Region L64, L85 | 11 |
| Ch44 | The Same Thing as Telling the Truth | Yaresh_Culture L3; Clothing_Food_Festivals_and_Transport_by_Region L16; Minor_Cast_Books_7-9 L25, L60; Book_09_Timeline L25; Chapter_Digest_Book_09 L25 | 6 |
| Ch45 | The Point of Sacrifice | Book_09_Timeline L4, L58; Chapter_Digest_Book_09 L4, L58; Taika_Power_Set L10; 01_World_Primer L57; 00_Peoples_Overview L57; Valash L57, L58 | 9 |
| Ch46 | What You Want Instead of What You Need | Clothing_Food_Festivals_and_Transport_by_Region L5; Daily_Life L5; Elves L5; Valash L5, L6, L12; Minor_Cast_Books_7-9 L5-12; Book_09_Timeline L12, L32; Chapter_Digest_Book_09 L12, L32; Benella L40, L44, L44-51, L51 … | 16 |
| Ch47 | Settling Differences With a Nice Chat | Book_09_Timeline L3-6, L29-36; Chapter_Digest_Book_09 L3-6, L29-36; Benella L25, L49 | 6 |
| Ch48 | The Sex Magic Thing | Sophie_Wexler L12; Book_09_Timeline L42; Chapter_Digest_Book_09 L42 | 3 |
| Ch49 | The Power and the Control | Dominion L28-29; Church_of_Dominion L28-29; Book_09_Timeline L79, L80, L81; Chapter_Digest_Book_09 L79, L80, L81 | 8 |
| Ch50 | Distant Power | Emir_Bahadir L27; Book_09_Timeline L27; Chapter_Digest_Book_09 L27; Constance L49, L51, L68, L92; Master_Timeline L51 | 8 |
| Ch51 | Who You Truly Are | Emir_Bahadir L6-11, L11, L14; Purity_and_Disguise L15-17; Book_09_Timeline L32; Chapter_Digest_Book_09 L32 | 6 |
| Ch52 | The Genuine Article | Astral_Kings_and_Messengers L5, L60; Messengers_as_a_People L5, L42, L60; Fal_Vin_Garath L20-28, L36, L36-44, L42-44; Era_5_Yaresh L20-28; Benella L20-29; Book_09_Timeline L32; Chapter_Digest_Book_09 L32; Battle_of_Yaresh L32 … | 15 |
| Ch53 | Stories About Fungus | Book_09_Timeline L11, L101; Chapter_Digest_Book_09 L101; Kalif L108; Rosa_Liselos L114, L118 | 6 |
| Ch54 | Vampire Monster Slaves | Book_09_Timeline L3, L64; Chapter_Digest_Book_09 L3, L64; Rosa_Liselos L8 | 5 |
| Ch55 | The Face of Insurmountable Power | Book_09_Timeline L3; Chapter_Digest_Book_09 L3; Messenger_War L3; Battle_of_Yaresh L3; Celestines L9; Messengers_as_a_People L12; Jes_Fin_Kaal L19, L27, L28; NPC_Rosters_by_Era L19 … | 12 |
| Ch56 | Even Though You Fear | Benella L4, L5, L20, L22, L22-26; Battle_of_Yaresh L4-20; Astral_Kings_and_Messengers L5, L5-8; Messengers_as_a_People L5; Fal_Vin_Garath L5, L5-7, L40; NPC_Rosters_by_Era L5; Plot_Hooks L5; Era_5_Yaresh L5, L14 … | 29 |
| Ch57 | Mockery | Book_09_Timeline L16; Chapter_Digest_Book_09 L16; Battle_of_Yaresh L16 | 3 |
| Ch58 | Die Immediately Without Prompting | Book_09_Timeline L45; Chapter_Digest_Book_09 L45; Battle_of_Yaresh L45; Era_Selection L50; Era_5_Yaresh L50 | 5 |
| Ch59 | The Old Groove | Book_09_Timeline L3, L23, L54; Chapter_Digest_Book_09 L3, L23, L54; Clive_Standish_Power_Set L4; Belinda_Callahan_Power_Set L13; Shimmer L67; Humphrey_Geller_Power_Set L71, L82 | 11 |
| Ch60 | Grisly Chore | Ranks_and_Advancement L7; Book_09_Timeline L15; Chapter_Digest_Book_09 L15; Neil_Davone_Power_Set L33 | 4 |
| Ch61 | Inferior | Book_09_Timeline L3; Chapter_Digest_Book_09 L3 | 2 |
| Ch62 | Apocalypse | Book_09_Timeline L22; Chapter_Digest_Book_09 L22; Astral_Kings_and_Messengers L23, L30, L30-34; Legion L23; Messenger_War L26; Battle_of_Yaresh L30-34; Plot_Hooks L30-34; Secrets_and_Rumours L30-34 … | 14 |
| Ch63 | Superior | Book_09_Timeline L23; Chapter_Digest_Book_09 L23 | 2 |
| Ch64 | Significantly More Powerful | 00_Astral_Overview L69, L88; Colin L90; Book_09_Timeline L96; Chapter_Digest_Book_09 L96 | 5 |
| Ch65 | Evil Lair | Book_09_Timeline L3-4, L63; Chapter_Digest_Book_09 L3-4, L63; Souls_Death_and_Healing L22-23; Astral_Kings_and_Messengers L23; Messengers_as_a_People L23; Celestial_Book L28-30; Open_Questions L30 | 9 |
| Ch66 | Imperfect Responses | Hess_Jor_Nasala L3, L39, L41; Jes_Fin_Kaal L3; Book_09_Timeline L3; Chapter_Digest_Book_09 L3; Messenger_War L3; Battle_of_Yaresh L3; NPC_Rosters_by_Era L3; NPC_Cards_Books_07-09 L3 | 10 |
| Ch67 | Triage | Book_09_Timeline L6; Chapter_Digest_Book_09 L6; Hearth L33 | 3 |
| Ch68 | Unquestionably Authoritarian | Book_09_Timeline L77; Chapter_Digest_Book_09 L77 | 2 |
| Ch69 | Voice of the Will | Book_09_Timeline L3-4, L55; Chapter_Digest_Book_09 L3-4, L55; Clive_Standish_Power_Set L17; Colin L55; Astral_Kings_and_Messengers L55-59; Familiars L55-59 | 8 |
| Ch70 | He Himself Does Not Become a Monster | Book_09_Timeline L3-5, L34; Chapter_Digest_Book_09 L3-5, L34 | 4 |
| Ch71 | An Egg Starting to Hatch | Book_09_Timeline L31; Chapter_Digest_Book_09 L31; Domains L35; The_Healer L38; Taika L43 | 5 |
| Ch72 | What the Swarm Came to Cure | Arabelle_Remore L25; Book_09_Timeline L46; Chapter_Digest_Book_09 L46 | 3 |
| Ch73 | A Mortal Perspective | Book_09_Timeline L41, L90; Chapter_Digest_Book_09 L41, L90; Secrets_and_Rumours L41; Motifs_and_Sayings L44 | 6 |
| Ch74 | Mr Asano Will See You Now | Gods_and_Churches L43; Church_of_the_Healer L43; Yaresh L43, L114; Hana_Shavar L43, L43-135, L71, L96; Book_09_Timeline L43; Chapter_Digest_Book_09 L43; Battle_of_Yaresh L43; Era_5_Yaresh L43 … | 13 |
| Ch75 | Hot Chocolate | Book_09_Timeline L25; Chapter_Digest_Book_09 L25 | 2 |
| Ch76 | Sadness Porridge | Hana_Shavar L4; Book_09_Timeline L88; Chapter_Digest_Book_09 L88; Battle_of_Yaresh L88 | 4 |
| Ch77 | The Better Adventurer | Minor_Cast_Books_7-9 L3, L13; Valash L4, L4-5, L6; Yaresh L13; Book_09_Timeline L13; Chapter_Digest_Book_09 L13; Battle_of_Yaresh L13; Secrets_and_Rumours L13 | 10 |
| Ch78 | Brave Because It Can Win | Taika L11; Minor_Cast_Books_7-9 L11-25; The_Deep_Astral_and_Interstice L25-27; World_Phoenix L28; Messengers_as_a_People L82; Vesta_Carmis_Zell L82; Book_09_Timeline L82; Chapter_Digest_Book_09 L82 … | 13 |
| Ch79 | A Man That Will Inspire Courage | Yaresh L5; Rufus_Remore_Power_Set L21; Book_09_Timeline L21; Chapter_Digest_Book_09 L21; Battle_of_Yaresh L21; Taika_Power_Set L43 | 6 |
| Ch80 | Luck That Good | Yaresh L3; Hana_Shavar L6, L6-13, L43; Gods_and_Churches L6-13; Book_09_Timeline L7; Chapter_Digest_Book_09 L7; Battle_of_Yaresh L7 | 8 |
| Ch81 | Nice and Grunty | Book_09_Timeline L5; Chapter_Digest_Book_09 L5; Knowledge_States L10; Yaresh L20; Onslow L23; Stash L35; 00_Magic_Overview L61; Souls_Death_and_Healing L61-63 | 8 |
| Ch82 | Breach | 00_Magic_Overview L22; Gary_Power_Set L22, L22-24; Book_09_Timeline L24; Chapter_Digest_Book_09 L24; Shimmer L36 | 6 |
| Ch83 | Gary Goes To Work | Book_09_Timeline L3-5, L18; Chapter_Digest_Book_09 L3-5, L18 | 4 |
| Ch84 | The Lady Shooting Hurricanes at People | Orin_Pensinata L9; Glossary L9; Onslow L23; Book_09_Timeline L50; Chapter_Digest_Book_09 L50 | 5 |
| Ch85 | Humphrey’s New Normal | Neil_Davone_Power_Set L16; Clive_Standish_Power_Set L32; Book_09_Timeline L50; Chapter_Digest_Book_09 L50; Progression_Tracks L53; Master_Timeline L53 | 6 |
| Ch86 | Not Enough Monsters to Fight | Marek_Nior_Vargas L16, L17, L22; Book_09_Timeline L16; Chapter_Digest_Book_09 L16; Messenger_War L16; Battle_of_Yaresh L16; Era_5_Yaresh L16 | 8 |
| Ch87 | The Difference in Conviction | Book_09_Timeline L3-5, L25; Chapter_Digest_Book_09 L3-5, L25; Onslow L24; Marek_Nior_Vargas L31, L34, L35; NPC_Cards_Books_07-09 L31 | 9 |
| Ch88 | Something to Turn the Tide | Book_09_Timeline L36; Chapter_Digest_Book_09 L36; Rufus_Remore_Power_Set L53 | 3 |
| Ch89 | The Strongest Arrow in His Quiver | Marek_Nior_Vargas L3; Rufus_Remore_Power_Set L22, L24; Book_09_Timeline L26; Chapter_Digest_Book_09 L26; Glossary L43; Motifs_and_Sayings L47; Elspeth_Arella L56 | 8 |
| Ch90 | Win a Fight | Fal_Vin_Garath L3; Jes_Fin_Kaal L3; Book_09_Timeline L3; Chapter_Digest_Book_09 L3; 00_Astral_Overview L4 | 5 |
| Ch91 | King of the Sky | Fal_Vin_Garath L3; Book_09_Timeline L3, L35; Chapter_Digest_Book_09 L3, L35 | 5 |
| Ch92 | A Pretty Creepy Dude | Taika L3; Book_09_Timeline L76; Chapter_Digest_Book_09 L76; Taika_Power_Set L82 | 4 |
| Ch93 | Security Oversight | Taika_Power_Set L4, L18, L28, L38, L48; Taika L27; NPC_Cards_Books_04-06 L27; Book_09_Timeline L67; Chapter_Digest_Book_09 L67; Calendar_Holidays_and_Naming_Customs L91-92 | 10 |
| Ch94 | I Have to Go Fight Evil | Book_09_Timeline L3, L30; Chapter_Digest_Book_09 L3, L30; Battle_of_Yaresh L3; Familiars L24-26; Amos_Pensinata L30; Gordon L92 | 8 |
| Ch95 | Stray Thought | Book_09_Timeline L3-6, L11, L41; Chapter_Digest_Book_09 L3-6, L11, L41; Astral_Kings_and_Messengers L15; 00_Astral_Overview L15; The_Deep_Astral_and_Interstice L16, L33 | 10 |
| Ch96 | Heretic | Book_09_Timeline L14; Chapter_Digest_Book_09 L14; Battle_of_Yaresh L14; Marek_Nior_Vargas L32 | 4 |
| Ch97 | An Extremely Annoying Catalyst | Onslow L49; Marek_Nior_Vargas L51; Who_Knows_What_When L51; Book_09_Timeline L74; Chapter_Digest_Book_09 L74; Battle_of_Yaresh L74; Raythe L80; Tone_and_Voice L80 … | 9 |
| Ch98 | Teaching Moment | Elves L4; Yaresh_Culture L4; Book_09_Timeline L4, L56; Chapter_Digest_Book_09 L4, L56; NPC_Rosters_by_Era L4; Allayeth L4-5; Battle_of_Yaresh L4-5; Plot_Hooks L4-5 … | 13 |
| Ch99 | Rigid Flaws | Book_09_Timeline L11; Chapter_Digest_Book_09 L11 | 2 |
| Ch100 | Doubt, Fear and Hesitation | Tera_Jun_Casta L19, L49, L49-72, L69; Era_5_Yaresh L19; Calendar_Holidays_and_Naming_Customs L23; Book_09_Timeline L51, L64; Chapter_Digest_Book_09 L64 | 9 |
| Ch101 | No | Tera_Jun_Casta L12-23; Book_09_Timeline L18; Chapter_Digest_Book_09 L18; Battle_of_Yaresh L18; Minor_Cast_Books_7-9 L54 | 5 |
| Ch102 | A Fight to the Pain | Book_09_Timeline L9; Chapter_Digest_Book_09 L9; Battle_of_Yaresh L9; Tera_Jun_Casta L54-67; Plot_Hooks L54-67; Open_Questions L55, L66-67; Vesta_Carmis_Zell L65, L65-67, L66-67; Astral_Kings_and_Messengers L66-67 … | 12 |
| Ch103 | One Ludicrous Encounter to the Next | Marek_Nior_Vargas L56, L114; Book_09_Timeline L64, L85; Chapter_Digest_Book_09 L64, L85; Battle_of_Yaresh L64, L85; Plot_Hooks L64; Yaresh L84; The_Unorthodoxy L114, L114-121, L117, L121; NPC_Cards_Books_07-09 L114 | 15 |
| Ch104 | The Foolish Choice | Marek_Nior_Vargas L3; Book_09_Timeline L5, L26, L27, L54, L62, L76 …; Chapter_Digest_Book_09 L5, L26, L27; Battle_of_Yaresh L5; Charist L29; Dustin_Kettering L54; Phoebe_Geller L54; Rick_Geller L54 … | 20 |

### Book 10

| Chapter | Title | Cited by (lines) | Rows |
|---|---|---|---|
| Ch1 | Aftermath | Tera_Jun_Casta L17; Marek_Nior_Vargas L49, L50; Book_10_Timeline L51; Chapter_Digest_Book_10 L51; Astral_Kings_and_Messengers L52; 00_Astral_Overview L52; Soul_Forge L52-55, L53; Vesta_Carmis_Zell L53 … | 16 |
| Ch2 | Harder Than They Have to Be | Book_10_Timeline L9, L65; Chapter_Digest_Book_10 L9, L65; Marek_Nior_Vargas L18, L20, L20-21; Tera_Jun_Casta L18, L20; NPC_Cards_Books_07-09 L18; Vesta_Carmis_Zell L19, L40; NPC_Rosters_by_Era L19; Plot_Hooks L19, L40 … | 17 |
| Ch3 | Developing Any Skill Takes Practise | The_Healer L11; Book_10_Timeline L24; Chapter_Digest_Book_10 L24; Gods_and_Churches L29; Elves L29; Church_of_the_Healer L29; Hana_Shavar L29, L68; Cloud_Constructs_and_Palaces L29 … | 10 |
| Ch4 | War Guilt Clause | Marek_Nior_Vargas L9; Book_10_Timeline L31; Chapter_Digest_Book_10 L31; Messenger_War L31; 01_World_Primer L53-55 | 5 |
| Ch5 | Primary Purpose | Book_10_Timeline L3, L24, L46; Chapter_Digest_Book_10 L3, L24; Colin L24; Gordon L24; 00_Cosmology_Overview L80-84; All_Devouring_Eye L94; World_Phoenix L100 | 10 |
| Ch6 | Everyone Has a Price | Book_10_Timeline L9; Chapter_Digest_Book_10 L9; Astral_Kings_and_Messengers L11; Allayeth L17; Romances_and_Rivalries L17 | 5 |
| Ch7 | Trust | Craig_Vermillion L5; Book_10_Timeline L6; Chapter_Digest_Book_10 L6; Allayeth L23; NPC_Cards_Books_07-09 L23; Calendar_Holidays_and_Naming_Customs L42-43 | 6 |
| Ch8 | Original Design Parameters | Travis_Noble L6; Church_of_Knowledge L9; Gabrielle_Pellin L9, L10, L26, L27, L46, L51 …; Romances_and_Rivalries L10; Fertility L37, L41; Book_10_Timeline L46; Chapter_Digest_Book_10 L46; NPC_Cards_Books_01-03 L51 … | 17 |
| Ch9 | Unstable | Book_10_Timeline L3-4, L38, L46; Chapter_Digest_Book_10 L3-4, L38, L46; Emir_Bahadir L4; Constance L9; Gods_and_Churches L10; Church_of_the_Healer L10; Gabrielle_Pellin L10, L12; NPC_Rosters_by_Era L10, L38 … | 22 |
| Ch10 | Dark Bargain | Musin_Heath L3; Book_10_Timeline L7; Chapter_Digest_Book_10 L7; Plot_Hooks L64; Secrets_and_Rumours L64; Era_5_Yaresh L64; Constance L80-81 | 7 |
| Ch11 | Decorum | Musin_Heath L4, L57; Book_10_Timeline L67; Chapter_Digest_Book_10 L67 | 4 |
| Ch12 | A Man of Principle | Arabelle_Remore L3, L25, L45; Book_10_Timeline L11; Chapter_Digest_Book_10 L11; Minor_Cast_Books_10-13 L11-14, L24-25, L26; Charist L41 | 9 |
| Ch13 | Experiment | Gabrielle_Pellin L18; Rick_Geller L26; Book_10_Timeline L36; Chapter_Digest_Book_10 L36; Charist L65 | 5 |
| Ch14 | Spanked | Allayeth L3; Gormanston_Bynes L3; NPC_Rosters_by_Era L3; Book_10_Timeline L8; Chapter_Digest_Book_10 L8; Yaresh_Culture L28-31, L33, L35; Era_Selection L28-35; Plot_Hooks L28-35 … | 18 |
| Ch15 | Better Ambitions | Astral_Kings_and_Messengers L3, L6, L9; The_Council_of_Kings L3, L3-62, L16-19, L30, L40, L43 …; The_Builder L3-4, L5; Great_Astral_Beings L5; Erigo_Fin_Desca L5, L5-26, L6-10, L10, L15-20, L25-26; Shako L5; NPC_Rosters_by_Era L5, L6; NPC_Cards_Books_10-13 L5 … | 38 |
| Ch16 | The Instinct to Kneel | Hess_Jor_Nasala L26, L26-53; Astral_Kings_and_Messengers L48; Messengers_as_a_People L48; Emir_Bahadir L59; Gormanston_Bynes L61, L62, L62-63; Book_10_Timeline L62; Chapter_Digest_Book_10 L62; NPC_Cards_Books_10-13 L62-63 … | 12 |
| Ch17 | Acceptable Terms | Book_10_Timeline L9, L39, L52; Chapter_Digest_Book_10 L9, L39; Cardinas_Expedition_and_Zone L39; Book_09_Timeline L52; Master_Timeline L52 | 8 |
| Ch18 | Actual Adventurers | Musin_Heath L71; Book_10_Timeline L92, L96; Chapter_Digest_Book_10 L92, L96; Dominion L129; Gormanston_Bynes L133, L137 | 8 |
| Ch19 | Bad Influence | Book_10_Timeline L3; Chapter_Digest_Book_10 L3; The_Healer L50-51, L57-62, L61 | 5 |
| Ch20 | Not Like the Ones We Know | Book_10_Timeline L8, L104; Chapter_Digest_Book_10 L8, L104 | 4 |
| Ch21 | A Juice Newton Situation | Book_10_Timeline L13, L26; Chapter_Digest_Book_10 L13, L26; Rufus_Remore L19-21; Taika L34; Essence_Catalogue L46; Taika_Power_Set L53, L63, L74, L85 | 11 |
| Ch22 | A More Practical Purpose | Book_10_Timeline L3, L112; Chapter_Digest_Book_10 L3, L112; Taika L67; Rufus_Remore_Power_Set L68; Charist L81; NPC_Cards_Books_07-09 L81 | 8 |
| Ch23 | Explicitly Antagonistic | Book_10_Timeline L3-6, L91; Chapter_Digest_Book_10 L3-6, L91; Allayeth L7; Charist L7; Romances_and_Rivalries L7 | 7 |
| Ch24 | Leap of Faith | Book_10_Timeline L9; Chapter_Digest_Book_10 L9 | 2 |
| Ch25 | Garden-Variety Arrogance | Book_10_Timeline L27, L74; Chapter_Digest_Book_10 L27, L74; Era_5_Yaresh L60; Allayeth L122 | 6 |
| Ch26 | How to Reach Gold Rank in Three Easy Steps | Book_10_Timeline L4; Chapter_Digest_Book_10 L4; Allayeth L35; Era_5_Yaresh L35; Zithis_Carrow_Vayel L54, L54-55; Who_Knows_What_When L54-55; Great_Astral_Beings L55; The_Builder L55 … | 11 |
| Ch27 | Nigh-Impossible Goal | Book_10_Timeline L3-16, L52, L80; Chapter_Digest_Book_10 L3-16, L52; Marek_Nior_Vargas L82 | 6 |
| Ch28 | We Should Probably Get You Out of Here | Amos_Pensinata L7; Book_10_Timeline L40; Chapter_Digest_Book_10 L40; Gods_and_Churches L56 | 4 |
| Ch29 | The Questions You’re Asking Don’t Matter | Book_10_Timeline L89; Chapter_Digest_Book_10 L89 | 2 |
| Ch30 | Political Price | Travis_Noble L13; Book_10_Timeline L63; Chapter_Digest_Book_10 L63; Cardinas_Expedition_and_Zone L63 | 4 |
| Ch31 | Ordinary Everyday Adventuring | Progression_Tracks L9; Book_10_Timeline L9, L55; Chapter_Digest_Book_10 L9, L55; Master_Timeline L9; Allayeth L49; Dominion L61; Gods_and_Churches L69-75; Religion_in_Practice L69-75 … | 12 |
| Ch32 | Drunken Lies and Mythic Legends | Book_10_Timeline L49; Chapter_Digest_Book_10 L49; Monsters L77 | 3 |
| Ch33 | Stash Wakes Up From a Nap | Craig_Vermillion L50; Book_09_Timeline L76; Book_10_Timeline L76, L108; Book_11_Timeline L76; Chapter_Digest_Book_10 L76, L108; Master_Timeline L76; Era_Selection L76; Era_5_Yaresh L76 … | 12 |
| Ch34 | Welcome Back, Colin | Colin L24, L72; Book_10_Timeline L39, L117; Chapter_Digest_Book_10 L39, L117; Thadwick_Mercer L118 | 7 |
| Ch35 | Optimism | Book_10_Timeline L13; Chapter_Digest_Book_10 L13; Magic_Society_and_Associations L36 | 3 |
| Ch36 | Mothers | Book_10_Timeline L11; Chapter_Digest_Book_10 L11; Melody_Jain L13, L13-14, L14; Order_and_Cult_of_the_Reaper L13-17; Church_of_Purity L14; Carlos_Quilido L14, L15-17, L16; NPC_Cards_Books_01-03 L14; NPC_Cards_Books_04-06 L14 … | 14 |
| Ch37 | The Whims of People Like Me | Book_10_Timeline L20; Chapter_Digest_Book_10 L20; House_Geller L49 | 3 |
| Ch38 | What’s Wrong With Simple | Gods_and_Churches L73; Jason_Asano L73; Book_10_Timeline L83; Chapter_Digest_Book_10 L83 | 4 |
| Ch39 | Faith is the Bane of Intellect | Carlos_Quilido L41, L49; Book_10_Timeline L45; Chapter_Digest_Book_10 L45; Purity_and_Disguise L45-46, L55-56; Gods_and_Churches L46-49 | 7 |
| Ch40 | Listing Off Animals | Book_10_Timeline L15, L39; Chapter_Digest_Book_10 L15, L39; Gods_and_Churches L16; Melody_Jain L22; Arabelle_Remore L43 | 7 |
| Ch41 | I’m Going to Change the Laws of Reality | Book_10_Timeline L3-7, L43, L47; Chapter_Digest_Book_10 L3-7, L43 | 5 |
| Ch42 | Exactly Where I Want to Be | Melody_Jain L3; Marek_Nior_Vargas L4; Book_10_Timeline L4; Chapter_Digest_Book_10 L4; Messenger_War L4; Astral_Kings_and_Messengers L7; Tera_Jun_Casta L7; Arabelle_Remore L14 … | 11 |
| Ch43 | An Impossible Act of Forgiveness | Book_10_Timeline L3, L13; Chapter_Digest_Book_10 L3, L13 | 4 |
| Ch44 | The Manner of Person One Will Be Dealing With | Book_10_Timeline L25; Chapter_Digest_Book_10 L25 | 2 |
| Ch45 | Because It’s Hard | Allayeth L82; Book_10_Timeline L108; Chapter_Digest_Book_10 L108 | 3 |
| Ch46 | Everything Adventurers Should Be | Book_10_Timeline L3, L31; Chapter_Digest_Book_10 L3, L31 | 4 |
| Ch47 | What is the Adventure Society | Book_10_Timeline L6, L76; Chapter_Digest_Book_10 L6, L76; Guilds_and_Houses L60-62; Gormanston_Bynes L60-63; Adventure_Society L76; Marcus_Hargrave_Xenoria L76, L76-78, L78; NPC_Rosters_by_Era L76; Era_5_Yaresh L76 … | 18 |
| Ch48 | Tradition and Decency | Gormanston_Bynes L4, L9-10; Marcus_Hargrave_Xenoria L10; Minor_Cast_Books_10-13 L15, L31, L41; Book_10_Timeline L57; Chapter_Digest_Book_10 L57 | 8 |
| Ch49 | Destiny | Book_10_Timeline L135; Chapter_Digest_Book_10 L135 | 2 |
| Ch50 | The Nightmares Never Really Go | Book_10_Timeline L3, L28; Chapter_Digest_Book_10 L3, L28; Marcus_Hargrave_Xenoria L51 | 5 |
| Ch51 | Unmistakeable | Hannah_and_Claire_Adeah L3, L9; Miriam_Vance L43; Teams_by_Era L43; Book_10_Timeline L43; Chapter_Digest_Book_10 L43; Glossary L43; Open_Questions L43; Minor_Cast_Books_10-13 L53-57, L60 | 10 |
| Ch52 | Money or the Box | Marcus_Hargrave_Xenoria L4-6; Tera_Jun_Casta L67; Book_10_Timeline L70; Chapter_Digest_Book_10 L70 | 4 |
| Ch53 | The Task You Can’t Seem to Manage | Book_10_Timeline L5; Chapter_Digest_Book_10 L5 | 2 |
| Ch54 | Worth Saving | Book_10_Timeline L38; Chapter_Digest_Book_10 L38 | 2 |
| Ch55 | Not Yet | Marek_Nior_Vargas L12; Book_10_Timeline L18; Chapter_Digest_Book_10 L18 | 3 |
| Ch56 | Sometimes, Violence is the Answer | Book_10_Timeline L3-4, L62; Chapter_Digest_Book_10 L3-4, L62 | 4 |
| Ch57 | Welcome Aboard | Book_10_Timeline L3, L60, L92; Chapter_Digest_Book_10 L3, L60; Cardinas_Expedition_and_Zone L3, L53; Soul_Forge L42, L46, L48; The_Reaper L60; Gabriel_Remore L92, L92-93, L93, L101; Teams_by_Era L92; Emir_Bahadir L93 … | 18 |
| Ch58 | Quick and Clean | Callum_Morse L7; Book_10_Timeline L47; Chapter_Digest_Book_10 L47; Gormanston_Bynes L58; Marcus_Hargrave_Xenoria L58-61; Killian_Laurent L106; NPC_Cards_Books_01-03 L106 | 7 |
| Ch59 | What We’re Walking Into | Allayeth L4, L17; Constance L4; Gabriel_Remore L4, L39; Miriam_Vance L4, L17; Teams_by_Era L4, L5, L17; Era_6_Cardinas L4, L5, L17; Carlos_Quilido L5; Hana_Shavar L5 … | 26 |
| Ch60 | What Kind of Adventurer | Marcus_Hargrave_Xenoria L13-46; Book_10_Timeline L14, L42; Chapter_Digest_Book_10 L14, L42; Cardinas_Expedition_and_Zone L14; Monsters L42 | 7 |
| Ch61 | Gary’s Old Team | Monsters L19; Book_10_Timeline L20; Chapter_Digest_Book_10 L20; Shimmer L28; Onslow L30; Miriam_Vance L45 | 6 |
| Ch62 | Hit Points | Book_10_Timeline L28; Chapter_Digest_Book_10 L28 | 2 |
| Ch63 | Surplus to Requirements | Book_10_Timeline L3, L52; Chapter_Digest_Book_10 L3, L52; Glossary L16 | 5 |
| Ch64 | Pride | Book_10_Timeline L3-5, L18; Chapter_Digest_Book_10 L3-5, L18; Amos_Pensinata L9; Orin_Pensinata L9; Glossary L9; Miriam_Vance L22 | 8 |
| Ch65 | The Greatest Enemy of All | Yaresh L3; Book_10_Timeline L3, L30; Chapter_Digest_Book_10 L3, L30; Cardinas_Expedition_and_Zone L3, L30; Plot_Hooks L3-6; Era_6_Cardinas L3-6, L9, L30; Lorenn L4-8, L9, L16-24, L34, L38; Smoulder_and_Brighthearts L6, L9 … | 32 |
| Ch66 | Taking the Position of a God | Book_10_Timeline L12, L85; Chapter_Digest_Book_10 L12, L85; Dominion L43; Gabriel_Remore L66, L87; Hana_Shavar L84; Destruction L84-86, L90-93, L94-97, L101, L103, L104; Constance L85; Gods_and_Churches L103 | 16 |
| Ch67 | Confident Guesses | Constance L14, L15; Knowledge L19-23; Destruction L34; Miriam_Vance L64; Book_10_Timeline L105; Chapter_Digest_Book_10 L105; Gary_Power_Set L122 | 8 |
| Ch68 | You Don’t Do it Blindly | Miriam_Vance L10; Taika_Power_Set L14, L26; Book_10_Timeline L68; Chapter_Digest_Book_10 L68; Beaufort_Builder_Cult_Commander L93 | 6 |
| Ch69 | Of a Mind to Kill You | Beaufort_Builder_Cult_Commander L3-4, L5, L6, L21, L42; Smoulder_and_Brighthearts L4; Book_10_Timeline L4; Chapter_Digest_Book_10 L4; Miriam_Vance L19 | 9 |
| Ch70 | Humungous Hairy Hands | Beaufort_Builder_Cult_Commander L6; Onslow L20; Book_10_Timeline L22; Chapter_Digest_Book_10 L22; Dustin_Kettering L38; Rick_Geller L38; Stash L38; Phoebe_Geller L42, L42-44 | 9 |
| Ch71 | Echoes of the Dead | Book_10_Timeline L39; Chapter_Digest_Book_10 L39; Glossary L39; Beaufort_Builder_Cult_Commander L48-60; Smoulder_and_Brighthearts L52; Runics L63 | 6 |
| Ch72 | Citadel | Book_10_Timeline L3, L58; Chapter_Digest_Book_10 L3, L58; Marla L28, L28-38; 01_World_Primer L31; Locations_by_Era L31; Yaresh L31; Era_Selection L31; Era_6_Cardinas L31, L58 … | 23 |
| Ch73 | The Impossible | Book_10_Timeline L3, L32; Chapter_Digest_Book_10 L3, L32; Beaufort_Builder_Cult_Commander L4, L10, L18; Marla L7-51; Secrets_and_Rumours L32; Lorenn L35, L45-47, L57; Destruction L54, L55 | 14 |
| Ch74 | Everything in My Power | Lorenn L25, L42, L57; Book_10_Timeline L31; Chapter_Digest_Book_10 L31 | 5 |
| Ch75 | Control the Pot | Book_10_Timeline L17; Chapter_Digest_Book_10 L17; Destruction L25 | 3 |
| Ch76 | It Happens Because I Want It To | Miriam_Vance L3; Soul_Forge L40-41; Book_10_Timeline L45; Chapter_Digest_Book_10 L45; Cardinas_Expedition_and_Zone L45; Lorenn L62-75 | 6 |
| Ch77 | More Urgent With Your Warning | Lorenn L7; Book_10_Timeline L67; Chapter_Digest_Book_10 L67 | 3 |
| Ch78 | A Little Bit Odd | Destruction L22, L27; Church_of_Undeath L27, L38, L70; Book_10_Timeline L27; Chapter_Digest_Book_10 L27; Constance L28; Gods_and_Churches L32, L38; Undeath L38; Church_of_Death L38 … | 22 |
| Ch79 | Dubious Alliance | Onslow L3; Gabriel_Remore L33, L44; Boris_Ket_Lundi L44-54; Glossary L52-54; Messengers_as_a_People L54; Gary_Power_Set L63; The_Unorthodoxy L82, L82-100, L98, L99-100, L100, L102; Book_10_Timeline L86, L112 … | 18 |
| Ch80 | Come Like a Tsunami | Book_10_Timeline L29, L42; Chapter_Digest_Book_10 L29, L42; Cardinas_Expedition_and_Zone L29, L42; Soul_Forge L29; Secrets_and_Rumours L29; Miriam_Vance L33; Church_of_Undeath L40, L42, L43; Garth_Larosse L42, L45 … | 17 |
| Ch81 | Put Up or Shut Up | Book_10_Timeline L3-5, L15; Chapter_Digest_Book_10 L3-5, L15; Glossary L34; Jes_Fin_Kaal L36; Soul_Forge L36 | 7 |
| Ch82 | Miracle | Arabelle_Remore L4; Miriam_Vance L58; Death L61-72, L62, L65, L76, L77-78; Gods_and_Churches L62, L72; Book_10_Timeline L62; Chapter_Digest_Book_10 L62; Cardinas_Expedition_and_Zone L62 | 12 |
| Ch83 | Death Knows How to Wait | Dominion L55; Book_10_Timeline L61; Chapter_Digest_Book_10 L61; Cardinas_Expedition_and_Zone L61; Death L64, L69; Jason_Asano L67-73; Titles_and_Blessings L69-70, L71; Gods_and_Churches L75-78 | 10 |
| Ch84 | Sometimes They Do | Book_10_Timeline L85; Chapter_Digest_Book_10 L85 | 2 |
| Ch85 | Fighting Alone | Death L5, L12, L15, L33; Purity_and_Disguise L33-35, L40; Miriam_Vance L38; Gods_and_Churches L40; Undeath L40, L63, L70; Book_10_Timeline L68; Chapter_Digest_Book_10 L68 | 13 |
| Ch86 | Insufficient Vessel | Book_10_Timeline L19, L61; Chapter_Digest_Book_10 L19, L61; Cardinas_Expedition_and_Zone L19; Hero L45, L47-50, L52, L53, L59-63, L67-72; Gods_and_Churches L59, L67-70; NPC_Rosters_by_Era L59; Tokens_Stones_and_Relics L59-61; Plot_Hooks L59-61 … | 23 |
| Ch87 | Twin Flames | Undeath L19; Book_10_Timeline L50; Chapter_Digest_Book_10 L50; Cardinas_Expedition_and_Zone L50 | 4 |
| Ch88 | Naught But Faith | Book_10_Timeline L23, L80; Chapter_Digest_Book_10 L23, L80; Garth_Larosse L58; Gods_and_Churches L58-63; Jameela L65, L70, L76, L97; Undeath L70-73, L73, L74-76, L77-85, L89-91; Destruction L85; Marla L116 | 17 |
| Ch89 | Thinking Like an Adventurer | Hero L26-40, L70-75, L77-83, L83; Gods_and_Churches L54; Purity_and_Disguise L71-73; Book_10_Timeline L79; Chapter_Digest_Book_10 L79; Marla L89-95 | 9 |
| Ch90 | Dread and Crushing Despair | Kalif L5-9; Book_10_Timeline L17; Chapter_Digest_Book_10 L17; Korinne_Pescos L51 | 4 |
| Ch91 | Avatar and Demigod | Gabriel_Remore L6; Book_10_Timeline L46; Chapter_Digest_Book_10 L46; Cardinas_Expedition_and_Zone L46; Jameela L63 | 5 |
| Ch92 | What He Wants For Himself | Book_10_Timeline L14, L42; Chapter_Digest_Book_10 L14, L42; Cardinas_Expedition_and_Zone L14; Motifs_and_Sayings L42; Emir_Bahadir L44; Jameela L46, L51, L84; Church_of_Undeath L65; Garth_Larosse L65-66, L66 | 13 |

### Book 11

| Chapter | Title | Cited by (lines) | Rows |
|---|---|---|---|
| Ch1 | What Makes Them Our Enemies | Gods_and_Churches L9; Book_11_Timeline L15, L37, L39, L58; Chapter_Digest_Book_11 L15, L39; Cardinas_Expedition_and_Zone L15, L39; Era_6_Cardinas L15, L64; Astral_Spaces_Zones_and_Surges L15-17, L16, L17, L36, L38-39, L38-42 …; 00_Magic_Overview L16; Earth_Magic L16, L36 … | 30 |
| Ch2 | Share the Responsibility | Domains L4; Book_11_Timeline L4; Chapter_Digest_Book_11 L4; The_Unorthodoxy L38, L75; Open_Questions L75; Dominion L81 | 7 |
| Ch3 | Contrition Born at the Point of a Sword | Book_11_Timeline L19, L46; Chapter_Digest_Book_11 L19, L46 | 4 |
| Ch4 | Overestimating the Length | Hana_Shavar L21; Kalif L21; Marla L21; Book_11_Timeline L21, L57; Chapter_Digest_Book_11 L21, L57; Cardinas_Expedition_and_Zone L21; Gods_and_Churches L85 | 9 |
| Ch5 | Good Friends | Book_11_Timeline L8, L63; Chapter_Digest_Book_11 L8, L63; Cardinas_Expedition_and_Zone L8 | 5 |
| Ch6 | Lackeys | Book_11_Timeline L13; Chapter_Digest_Book_11 L13; Korinne_Pescos L13-16, L13-20, L19; NPC_Cards_Books_07-09 L13-16; Minor_Cast_Books_10-13 L50; Messengers_as_a_People L55; House_Mercer L57, L58, L59, L61; Thadwick_Mercer L57, L59, L61 … | 22 |
| Ch7 | Yellow Bell | Name_Index L14; Book_11_Timeline L36, L82; Chapter_Digest_Book_11 L36, L82 | 5 |
| Ch8 | Rock Climbing | Undeath L20; Church_of_Undeath L20; Garth_Larosse L20; Book_11_Timeline L21, L45, L102; Chapter_Digest_Book_11 L21, L45; Dustin_Kettering L23; Neil_Davone L23-24; Domains L54 … | 16 |
| Ch9 | Grunts and Sizzling Noises | Church_of_Undeath L100; Book_11_Timeline L108; Chapter_Digest_Book_11 L108; Cardinas_Expedition_and_Zone L108 | 4 |
| Ch10 | The Man Who Commands the Lightning | Lorus L7, L8, L12, L16-20, L49; Durrum L8, L9, L10-13, L14, L16-20, L46; Book_11_Timeline L12; Chapter_Digest_Book_11 L12; Cardinas_Expedition_and_Zone L12 | 14 |
| Ch11 | Style Over Substance | Book_11_Timeline L3-6, L50; Chapter_Digest_Book_11 L3-6, L50; Durrum L6, L35, L44, L57, L62, L79 …; Dustin_Kettering L6, L43-49, L49; Lorus L7, L31, L53, L64, L67, L71-73 …; Church_of_Undeath L48; NPC_Cards_Books_01-03 L49 | 26 |
| Ch12 | Precise Control | Durrum L6, L65, L74-84, L106; Book_11_Timeline L19; Chapter_Digest_Book_11 L19; Name_Index L56; NPC_Cards_Books_10-13 L65 | 8 |
| Ch13 | Impostor Syndrome | Book_11_Timeline L4; Chapter_Digest_Book_11 L4; Name_Index L4; Belinda_Callahan L4-7; Jory_Tillman L61 | 5 |
| Ch14 | Gauntlet | Book_11_Timeline L3-5, L6, L27; Chapter_Digest_Book_11 L3-5, L6, L27; Minor_Cast_Books_10-13 L10, L20 | 8 |
| Ch15 | Creepy Stuff | Book_11_Timeline L3-7, L68; Chapter_Digest_Book_11 L3-7, L68 | 4 |
| Ch16 | Group Dynamics | Book_11_Timeline L29; Chapter_Digest_Book_11 L29; Lorenn L70, L77 | 4 |
| Ch17 | As Many as We Can Get | Transformation_Zones L10, L27, L33; Lorenn L14, L39; Book_11_Timeline L27, L33; Chapter_Digest_Book_11 L27, L33; Cardinas_Expedition_and_Zone L27; Era_6_Cardinas L33; Marla L80; Beaufort_Builder_Cult_Commander L83 | 13 |
| Ch18 | Alienness and Familiarity | Transformation_Zones L4; Book_11_Timeline L4; Chapter_Digest_Book_11 L4; Master_Timeline L4; Korinne_Pescos L29; NPC_Cards_Books_07-09 L29; Durrum L52 | 7 |
| Ch19 | The Reason We Have To | Book_11_Timeline L19; Chapter_Digest_Book_11 L19; Miriam_Vance L56; Cardinas_Expedition_and_Zone L56 | 4 |
| Ch20 | A Bitter Cup | Book_11_Timeline L3; Chapter_Digest_Book_11 L3; Onslow L19; Stash L19 | 4 |
| Ch21 | Good Leader | Book_11_Timeline L9; Chapter_Digest_Book_11 L9; Cardinas_Expedition_and_Zone L9; Rick_Geller L104 | 4 |
| Ch22 | I Want Those Things For You | Great_Astral_Beings L11; Velius L11; Raythe L12; Keeper_of_Moments L21-22, L29-32; All_Devouring_Eye L29, L38; Helsveth L32; Book_11_Timeline L66; Chapter_Digest_Book_11 L66 | 10 |
| Ch23 | Small, Easy or Inconsequential | Book_11_Timeline L3-6, L65; Chapter_Digest_Book_11 L3-6, L65; Calendar_Holidays_and_Naming_Customs L33; Nik_Asano L38, L42; 01_World_Primer L42; Lehenik L42, L44, L45-46; Tone_and_Voice L42; Beaufort_Builder_Cult_Commander L78 | 13 |
| Ch24 | Another Astral King | Church_of_Undeath L5; Jameela L28, L43; House_Remore L50; Garth_Larosse L59; Boris_Ket_Lundi L69, L85; Book_11_Timeline L85; Chapter_Digest_Book_11 L85; Messenger_War L85 … | 19 |
| Ch25 | Unorthodoxy | The_Unorthodoxy L47, L47-57, L49-51, L53-55, L56-57; Open_Questions L47-55, L49-57, L51, L53; 01_World_Primer L49-51; Astral_Kings_and_Messengers L51, L53; Messengers_as_a_People L51; Book_11_Timeline L51; Chapter_Digest_Book_11 L51; Cardinas_Expedition_and_Zone L51 … | 19 |
| Ch26 | Messengers Don’t Have Hearts | Jameela L20, L26; Secrets_and_Rumours L82; Book_11_Timeline L96; Chapter_Digest_Book_11 L96 | 5 |
| Ch27 | Will He Be Broken | Book_11_Timeline L38; Chapter_Digest_Book_11 L38; Zithis_Carrow_Vayel L55; Garth_Larosse L67; Jameela L69 | 5 |
| Ch28 | Risking Everything | Garth_Larosse L4; Death L16; Undeath L16; Book_11_Timeline L40; Chapter_Digest_Book_11 L40 | 5 |
| Ch29 | A Dangerous Power | Cults_and_Orders L3; Gods_and_Churches L3-5; Garth_Larosse L12; Astral_Kings_and_Messengers L31; Book_11_Timeline L31; Chapter_Digest_Book_11 L31 | 6 |
| Ch30 | Bit of an Odd Bloke | Book_11_Timeline L6; Chapter_Digest_Book_11 L6; Garth_Larosse L56, L66 | 4 |
| Ch31 | Asking For a Lot of Trust | Book_11_Timeline L3, L67; Chapter_Digest_Book_11 L3, L67; Boris_Ket_Lundi L69, L87 | 6 |
| Ch32 | It Used to Be Completely Dark | Book_11_Timeline L8; Chapter_Digest_Book_11 L8; Orin_Pensinata L73-74, L74; Teams_by_Era L73-74; Korinne_Pescos L74; Rosa_Liselos L74; Miriam_Vance L75; Cardinas_Expedition_and_Zone L75 … | 10 |
| Ch33 | He Likes to Name-Drop | Familiars_Summons_and_Conjurations L4; Book_11_Timeline L4; Chapter_Digest_Book_11 L4; Authority_and_Sanctioning L9-13, L140, L140-157, L152-153, L155-157, L157; Miriam_Vance L20; Open_Questions L20; Familiars L50; Undeath L99 … | 16 |
| Ch34 | He Isn’t Always Evil and He is Not Always Wrong | Book_11_Timeline L15, L33, L124; Chapter_Digest_Book_11 L15, L124; Master_Timeline L33; 00_Cosmology_Overview L97, L103; Great_Astral_Beings L97, L103; All_Devouring_Eye L97 | 11 |
| Ch35 | New Power and a Freshly Cooked Batch of Smugness | Book_11_Timeline L39; Chapter_Digest_Book_11 L39; Cardinas_Expedition_and_Zone L39; Undeath L42-47; Authority_and_Sanctioning L43-47, L43-48; Death L45-46 | 7 |
| Ch36 | Instinctively Protected | Book_11_Timeline L3; Chapter_Digest_Book_11 L3; Cardinas_Expedition_and_Zone L3; Earth_Powers L7, L8; EDJI_and_Post_Reveal_Institutions L8, L13, L54; Yumi_Asano L8, L8-12, L9; NPC_Rosters_by_Era L8; Locations_by_Era L9 … | 21 |
| Ch37 | No Limit | Book_11_Timeline L58; Chapter_Digest_Book_11 L58 | 2 |
| Ch38 | The Hegemon | Nik_Asano L3, L33; Book_11_Timeline L61; Chapter_Digest_Book_11 L61 | 4 |
| Ch39 | Miracles Work on a Different Scale | Book_11_Timeline L3; Chapter_Digest_Book_11 L3 | 2 |
| Ch40 | Right Now | The_Unorthodoxy L58, L111-113; Book_11_Timeline L68; Chapter_Digest_Book_11 L68 | 4 |
| Ch41 | Leadership Isn’t Easy | Book_11_Timeline L59; Chapter_Digest_Book_11 L59; Destruction L97 | 3 |
| Ch42 | A Decision Made Poorly and in Haste | The_Unorthodoxy L8-9, L11, L24-26, L28, L29-30; Domains L9; Who_Knows_What_When L9; Book_11_Timeline L38; Chapter_Digest_Book_11 L38; Earth_Vampire_War L38; The_Cabal L40, L42-44, L59-65, L63, L128; 00_Earth_Overview L40, L63 … | 19 |
| Ch43 | Binaries | Book_11_Timeline L14, L131; Chapter_Digest_Book_11 L14, L131; Soul_Forge L97; Cardinas_Expedition_and_Zone L131 | 6 |
| Ch44 | When We Worry the Most | The_Unorthodoxy L14; Book_11_Timeline L64; Chapter_Digest_Book_11 L64 | 3 |
| Ch45 | Paranoid | Book_11_Timeline L3-5, L45; Chapter_Digest_Book_11 L3-5, L45 | 4 |
| Ch46 | Academically Unsound | Minor_Cast_Books_7-9 L11; Minor_Cast_Order_of_Redeeming_Light L11; Glossary L11; Book_11_Timeline L17, L20; Chapter_Digest_Book_11 L17, L20; Fertility L29; Nik_Asano L30-33, L32 | 10 |
| Ch47 | Not All of Us Are Demigods | Book_11_Timeline L3-7, L104; Chapter_Digest_Book_11 L3-7, L104; Amos_Pensinata L64 | 5 |
| Ch48 | The Price | Book_11_Timeline L22, L62; Chapter_Digest_Book_11 L22, L62; Cardinas_Expedition_and_Zone L22, L30 | 6 |
| Ch49 | Guaranteed to Become Enemies | Book_11_Timeline L69; Chapter_Digest_Book_11 L69; The_Unorthodoxy L71; Open_Questions L71; Miriam_Vance L79; Amos_Pensinata L86 | 6 |
| Ch50 | Assuming We Win | Arabelle_Remore L6; Nik_Asano L10-25, L15; Book_11_Timeline L11, L15, L56; Chapter_Digest_Book_11 L11, L56; Cardinas_Expedition_and_Zone L11, L15; Transformation_Zones L15; Master_Timeline L15; Open_Questions L15 | 13 |
| Ch51 | Don’t Throw Our Dead Friend’s Stuff Out of a Tortoise | Transformation_Zones L3; Book_11_Timeline L3; Chapter_Digest_Book_11 L3; Beaufort_Builder_Cult_Commander L45; Lorenn L61; Miriam_Vance L64 | 6 |
| Ch52 | Beware of Chicken | Miriam_Vance L10; Taika L29; Fertility L54; Book_11_Timeline L104; Chapter_Digest_Book_11 L104 | 5 |
| Ch53 | A Better Adventurer | Book_11_Timeline L8; Chapter_Digest_Book_11 L8; Onslow L12; Miriam_Vance L25; Nik_Asano L56 | 5 |
| Ch54 | The Only Way It Can Win | Beaufort_Builder_Cult_Commander L5-9; Amos_Pensinata L18-21, L56; Book_11_Timeline L61; Chapter_Digest_Book_11 L61 | 5 |
| Ch55 | When Violence Is Easy and Words Are Hard | Amos_Pensinata L3; Miriam_Vance L3; Book_11_Timeline L25; Chapter_Digest_Book_11 L25 | 4 |
| Ch56 | A Cocktail of Ignorance, Arrogance and Ambition | Soul_Forge L20; Book_11_Timeline L48; Chapter_Digest_Book_11 L48 | 3 |
| Ch57 | Different Enough | Lorenn L17; Nik_Asano L26-41; Gary L60; Book_11_Timeline L60; Chapter_Digest_Book_11 L60; Tone_and_Voice L60; NPC_Cards_Books_01-03 L60 | 7 |
| Ch58 | Everything I Need | Book_11_Timeline L91; Chapter_Digest_Book_11 L91 | 2 |
| Ch59 | The Work of Higher Beings | Book_11_Timeline L10; Chapter_Digest_Book_11 L10 | 2 |
| Ch60 | Heroes Cheat All the Time | Era_Selection L3; Era_6_Cardinas L3, L13; Open_Questions L3; Book_11_Timeline L5, L48; Chapter_Digest_Book_11 L5, L48; Sapphire_Crown L9; House_Rimaros L9; Church_of_Hero L13, L24 … | 23 |
| Ch61 | You Know It’s Trouble | Raythe L8, L8-11; Velius L8; NPC_Rosters_by_Era L8; Nik_Asano L16; Family_Trees L16; Book_11_Timeline L16; Chapter_Digest_Book_11 L16; Master_Timeline L16 … | 14 |
| Ch62 | Steve, Lord of Undeath | Destruction L18; Undeath L28, L39, L77; Umber L36; Gwydion_Remore L40; Book_11_Timeline L89; Chapter_Digest_Book_11 L89; Cardinas_Expedition_and_Zone L89; Era_6_Cardinas L89 … | 11 |
| Ch63 | Time Travel is the Worst | Fertility L14; Book_11_Timeline L39, L98; Chapter_Digest_Book_11 L39, L98; 00_Cosmology_Overview L76, L98, L100; The_Deep_Astral_and_Interstice L78-80; Master_Timeline L80; Keeper_of_Moments L98, L100; Raythe L98 | 13 |
| Ch64 | Unique in the Entire Cosmos | Great_Astral_Beings L9, L49; Keeper_of_Moments L9, L47, L49; Raythe L9; Velius L9, L51; Book_11_Timeline L23; Chapter_Digest_Book_11 L23; Cosmic_Throne_and_the_Sundering L24, L24-25, L47, L49, L58-66, L83 …; 00_Cosmology_Overview L24-27, L49 … | 28 |
| Ch65 | A Power That No One and Nothing Should Have | Cosmic_Throne_and_the_Sundering L3, L6, L8, L8-9, L20, L28 …; 01_World_Primer L8; Book_11_Timeline L8, L34; Chapter_Digest_Book_11 L8, L34; Master_Timeline L8; Cardinas_Expedition_and_Zone L8; World_Phoenix L34-36; Undeath L43 … | 35 |
| Ch66 | Party to Betrayal | Beaufort_Builder_Cult_Commander L5-17, L24-31; Book_11_Timeline L22, L89; Chapter_Digest_Book_11 L22, L89; Cardinas_Expedition_and_Zone L89; Plot_Hooks L89; Open_Questions L95 | 9 |
| Ch67 | Farewells | Book_11_Timeline L5; Chapter_Digest_Book_11 L5; Gods_and_Churches L6; Open_Questions L9; Tera_Jun_Casta L12; NPC_Cards_Books_07-09 L12; The_Unorthodoxy L18; Nik_Asano L19 … | 13 |
| Ch68 | Compassionate Strangers | Hegemons_Will_and_Dominion L103-106; Book_11_Timeline L115, L412, L703, L782, L918, L1034 …; Chapter_Digest_Book_11 L115, L2540; Master_Timeline L115, L412, L703, L782, L918, L1031 …; Open_Questions L115, L159, L703, L707-709, L782, L1580; Legion L159, L161, L178, L229, L238, L261 …; Seeker_of_Songs L159, L175, L236, L2164, L2530-2531; Whisper_in_Corners L159, L231, L2160, L2180 … | 312 |

### Book 12

| Chapter | Title | Cited by (lines) | Rows |
|---|---|---|---|
| Ch0 | Don’t Tell Humphrey | Zara_Rimaros L14; Teams_by_Era L14; Book_12_Timeline L19; Chapter_Digest_Book_12 L19; The_Return_and_the_Bridge L19 | 5 |
| Ch1 | Why He Hasn’t | Cosmic_Throne_and_the_Sundering L3, L22, L26, L28, L30, L34; Raythe L5-11; Book_12_Timeline L10, L53; Chapter_Digest_Book_12 L10, L53; Great_Astral_Beings L26; 01_World_Primer L34, L36; The_System L34-36, L38, L44, L46, L54; Anna_Tilden L36, L80 … | 45 |
| Ch2 | If We Can’t Change For the Better | Book_12_Timeline L7, L107; Chapter_Digest_Book_12 L7; Raythe L9; Miles_Cotezee L50; Calendar_Holidays_and_Naming_Customs L52; Magical_Research_Association L52, L56, L60-68; Yumi_Asano L102; Master_Timeline L107 … | 17 |
| Ch3 | We’re All Stuck in a Hole | Nigel_Thornton L3, L4, L5, L6; Book_12_Timeline L3, L5, L7, L13, L82; Chapter_Digest_Book_12 L3, L7, L13, L82; Era_7_The_Return L3; Teams_by_Era L3-5; Earth_Powers L3-8; Anna_Tilden L7; Earth_Vampire_War L7, L13 … | 20 |
| Ch4 | A Silent City | Book_12_Timeline L3, L14, L28, L40, L49; Chapter_Digest_Book_12 L3, L14, L40, L49; Saint-Etienne L20, L41; Nigel_Thornton L23, L23-28, L23-48 | 14 |
| Ch5 | The Fundamental Things | Vampire_War L70; Earth_Vampire_War L70-76; Domains L76; Era_7_The_Return L76; Book_12_Timeline L89; Chapter_Digest_Book_12 L89; The_Return_and_the_Bridge L89; Magic_Society_and_Associations L99 … | 9 |
| Ch6 | You Don’t Want Glory | The_Deep_Astral_and_Interstice L3; Gods_and_Churches L18-22; Minor_Cast_Books_10-13 L23, L29-30; Book_12_Timeline L23; Chapter_Digest_Book_12 L23; Fertility L27 | 7 |
| Ch7 | The Power Looming Over Us All | Book_12_Timeline L8, L78; Chapter_Digest_Book_12 L8; The_Return_and_the_Bridge L8; Undeath L14; Fertility L46-48; Church_of_Undeath L52; Master_Timeline L78 | 8 |
| Ch8 | The Topic of Pants | Death L4, L8-13, L15; Gods_and_Churches L10, L19; Open_Questions L10, L19; Book_12_Timeline L19; Chapter_Digest_Book_12 L19; The_System L70-71, L100-102; Outworlders L100; Jason_Asano L100, L100-104 … | 16 |
| Ch9 | Butchery | Carlos_Quilido L4, L19; Shade L7; Minor_Cast_Books_7-9 L14; Book_12_Timeline L16; Chapter_Digest_Book_12 L16 | 6 |
| Ch10 | Just Some Guy | The_System L14; Book_12_Timeline L14, L74; Chapter_Digest_Book_12 L14, L74; Knowledge_States L14-17; Plot_Hooks L14-17; Spoiler_Management L14-17; 00_Cosmology_Overview L17-22; Nigel_Thornton L59, L60 … | 17 |
| Ch11 | On a Whim | Marla L6; Book_12_Timeline L6; Chapter_Digest_Book_12 L6; The_Return_and_the_Bridge L6; Locations_by_Era L46, L110; Spirit_Vault_and_Astral_Kingdom L46, L110; Domains L113 | 9 |
| Ch12 | Mandatory Team Activity | Zara_Rimaros L3, L10, L17-20, L20; Book_12_Timeline L3, L20; Chapter_Digest_Book_12 L3, L20; NPC_Rosters_by_Era L3, L75; Storm_Kingdom_Culture L17, L19; Locations_by_Era L17-20; Family_Trees L17-20; Rimaros L19 … | 20 |
| Ch13 | Try Not to Bring Down Civilisation | Church_of_Hero L3-4, L10-11; Gods_and_Churches L5, L67; Church_of_Undeath L7; Domains L34; Spirit_Vault_and_Astral_Kingdom L34; Book_12_Timeline L36, L73; Chapter_Digest_Book_12 L36, L73; Master_Timeline L36 … | 19 |
| Ch14 | We Have Forever | Book_12_Timeline L11; Chapter_Digest_Book_12 L11; 01_World_Primer L19 | 3 |
| Ch15 | Like an Adventurer | Book_12_Timeline L3, L47, L64; Chapter_Digest_Book_12 L3, L64; The_Return_and_the_Bridge L3; Hannah_and_Claire_Adeah L6; Family_Trees L6; Romances_and_Rivalries L6, L8; Keith_Geller L7; Team_Shining_Scabbard L8, L8-9 … | 27 |
| Ch16 | People Think You’re Blowing Up Cities | Yaresh_Culture L8; Allayeth L8; Charist L8; Era_5_Yaresh L8; Open_Questions L8; Magical_Research_Association L10; Mirror_Kingdom_Culture L11; Team_Shining_Scabbard L11 … | 15 |
| Ch17 | We Need to Put a Stop to It | Book_12_Timeline L19; Chapter_Digest_Book_12 L19; Dominion L27; Locations_by_Era L55-73; Valdis_Volaire L55-73, L56; NPC_Cards_Books_01-03 L56 | 7 |
| Ch18 | A Lunatic’s Nightmare | Book_12_Timeline L6, L16, L37, L45, L70; Chapter_Digest_Book_12 L6, L16, L37, L45 | 9 |
| Ch19 | When People See My Powers | Book_12_Timeline L6, L9, L58, L61, L73, L81; Chapter_Digest_Book_12 L6, L9; Essence_Catalogue L48 | 9 |
| Ch20 | Listening For Whispers | Sigrid_Freyn L9; Teams_by_Era L9; The_System L21-22; Book_12_Timeline L42, L85; Chapter_Digest_Book_12 L42, L85 | 7 |
| Ch21 | Defier | Farrah_Hurin_Power_Set L43-46; Farrah_Hurin L43-46; Glossary L43-46; Book_12_Timeline L61; Chapter_Digest_Book_12 L61; Master_Timeline L61; The_Return_and_the_Bridge L61; Era_7_The_Return L61 … | 10 |
| Ch22 | Vast Cosmic Power Types | Alchemy_Association L3; Magical_Research_Association L3; Book_12_Timeline L27, L56; Master_Timeline L27; Chapter_Digest_Book_12 L56; Anna_Tilden L73-74 | 7 |
| Ch23 | Objectives | Magical_Research_Association L3-4; Alchemy_Artifice_and_Magical_Materials L25; Book_12_Timeline L25; Chapter_Digest_Book_12 L25; Danielle_Geller L79; Tone_and_Voice L79; NPC_Cards_Books_01-03 L79; Era_7_The_Return L79 | 8 |
| Ch24 | The Protection of a Dictator | Knowledge L3; 01_World_Primer L6; Book_12_Timeline L13; Chapter_Digest_Book_12 L13 | 4 |
| Ch25 | You Want Your Adventurers Happy | Book_12_Timeline L3, L5, L63, L66; Chapter_Digest_Book_12 L3, L5, L63, L66; Danielle_Geller L7 | 9 |
| Ch26 | Making Things Worse | Dragon_Lands L5, L5-6, L6, L7, L9, L10-11 …; Book_12_Timeline L5, L16, L68; Chapter_Digest_Book_12 L5, L16; Draconians L5-6; Dragon_Lands_Culture L5-6, L7, L9, L11, L12; Locations_by_Era L5-7; The_Council_of_Kings L18, L20, L29, L30; The_Unorthodoxy L19, L27 … | 32 |
| Ch27 | Sometimes We Need Scars | Minor_Cast_Books_1-3 L5; Book_12_Timeline L12, L19, L45; Chapter_Digest_Book_12 L12, L19; Boko_Evacuation L12; The_Return_and_the_Bridge L12; Alchemy_Artifice_and_Magical_Materials L19; Astral_Spaces_Zones_and_Surges L19; Belinda_Callahan L23 … | 18 |
| Ch28 | That’s What Adventurers Do | Vincent_Trenslow L3; Book_12_Timeline L3, L41, L76; Chapter_Digest_Book_12 L3, L41; NPC_Cards_Books_01-03 L3 | 7 |
| Ch29 | A Matter of Mindset | Alchemy_Association L9; House_Davone L15; Elspeth_Arella L24-32, L32; Romances_and_Rivalries L32; Greenstone L38, L59-60; Adris_Dorgan L38, L48; Open_Questions L38; Book_12_Timeline L40, L65 … | 25 |
| Ch30 | Posturing Children | Ustei L9; Ustei_Homeland_Culture L9; Open_Questions L9; Boko_Culture L71; Boko L71; Li_Li_Mei L71-74, L80; Boko_Evacuation L71-81; Secrets_and_Rumours L75 … | 11 |
| Ch31 | This Is Not a Cliff | Book_12_Timeline L3, L7, L11, L62, L97; Chapter_Digest_Book_12 L3, L7, L11, L62, L97; Li_Li_Mei L3-12; Boko_Evacuation L3-12; Boko_Culture L34; Education L34, L79; Boko L34; Essence_Catalogue L118 | 17 |
| Ch32 | Cook the Crap Out of Some Toast | Book_12_Timeline L8; Chapter_Digest_Book_12 L8; Boko_Evacuation L13, L15-17, L19-21, L24-26, L29, L37-54 …; Locations_by_Era L15-29; Boko L15-29, L91; Li_Li_Mei L18; Arabelle_Remore L35; Messenger_War L49-53 … | 19 |
| Ch33 | The Benevolence of a Nightmare God | 01_World_Primer L3; Boko_Culture L3, L7; Greenstone L3; Locations_by_Era L3, L3-4; Boko L3, L3-4, L7; Boko_Evacuation L3, L4, L5-6, L6, L7, L9-10 …; Era_Selection L3; Plot_Hooks L3 … | 39 |
| Ch34 | Pretext | Colin L6; Book_12_Timeline L35, L57; Chapter_Digest_Book_12 L35, L57; Boko_Evacuation L35; Estercost_Culture L64 | 7 |
| Ch35 | Eternity Awaits Us | Book_12_Timeline L6, L8, L11, L66, L84, L88; Chapter_Digest_Book_12 L6, L8, L11, L66, L84, L88; Messenger_War L6, L66, L88; Boko_Evacuation L6-8, L66, L84, L88; The_Return_and_the_Bridge L6-11; The_Council_of_Kings L11, L66, L68-70, L81 | 24 |
| Ch36 | A Time to Slumber | Book_12_Timeline L3; Chapter_Digest_Book_12 L3; Boko_Evacuation L3, L4, L6; Locations_by_Era L3-5; Boko L3-5; Messenger_War L6; Motifs_and_Sayings L7-8; Jamis_Fran_Muskar L35 … | 11 |
| Ch37 | I Know You Can't Control Yourself Any Longer | Book_12_Timeline L36, L128; Chapter_Digest_Book_12 L36, L128; Badges_and_Guild_Membership L128; Adventure_Society L128-131 | 6 |
| Ch38 | Truly Outrageous Things | House_Davone L9; Locations_by_Era L49; Hornis L49; Minor_Cast_Books_1-3 L49, L61; Minor_Cast_Books_10-13 L49, L61; Book_12_Timeline L61; Chapter_Digest_Book_12 L61 | 9 |
| Ch39 | A Framework For Leadership | Nik_Asano L3, L15, L30-35, L31; Family_Trees L15; NPC_Cards_Books_10-13 L15, L31; Lehenik L17, L19-20; Boko_Culture L37, L80, L110; Locations_by_Era L37, L61; Boko L37, L40, L61, L80, L80-91, L85-89 …; Africa_like_Continent L37 … | 33 |
| Ch40 | It’s More Complicated Than That | Book_12_Timeline L5, L6; Chapter_Digest_Book_12 L5, L6; EDJI_and_Post_Reveal_Institutions L6, L15; Anna_Tilden L20; Ketevan_Arziani L52 | 8 |
| Ch41 | A Long Few Days | Book_12_Timeline L3, L7, L42, L45, L61; Chapter_Digest_Book_12 L3, L7, L42, L45; Earth_Vampire_War L3-9; Ketevan_Arziani L3-14; Craig_Vermillion L13; Saint-Etienne L27; Locations_by_Era L28; Ian_Evans L28 | 15 |
| Ch42 | A Thing That Makes the Car Work | Book_12_Timeline L4, L21, L65, L70, L72, L82; Chapter_Digest_Book_12 L4, L21, L65, L70; The_System L92, L99-101; Anna_Tilden L99, L100, L104; Knowledge_States L99; Who_Knows_What_When L99; Era_7_The_Return L99 | 18 |
| Ch43 | A Long Time Coming | Minor_Cast_Books_10-13 L16, L31-34; Open_Questions L46, L47; Nik_Asano L46-50; Estercost_Culture L47; Vitesse_Culture L47, L48, L52, L53, L54, L64; Vitesse L47, L48, L64, L68; Book_12_Timeline L62, L64; Chapter_Digest_Book_12 L62, L64 … | 27 |
| Ch44 | A Big Juicy Hole | Book_12_Timeline L4, L20, L62; Chapter_Digest_Book_12 L4, L20, L62; Vitesse L13, L112; Badges_and_Guild_Membership L20; Burning_Violet L26, L82; Guilds_and_Houses L26-30; Belinda_Callahan L34; Adventure_Society L98 … | 15 |
| Ch45 | A Sense of Responsibility | Book_12_Timeline L3, L55, L62; Chapter_Digest_Book_12 L3, L55, L62; Badges_and_Guild_Membership L3, L8, L14; Burning_Violet L6, L12, L14, L95; Vitesse_Culture L12-14; House_Remore L12-14; Guilds_and_Houses L14; Roland_Remore L56, L97 … | 22 |
| Ch46 | Trouble Always Knows Where to Find Me | Cassandra_Mercer L3, L3-4, L4, L20; Henrietta_Geller L3; Book_12_Timeline L3, L15, L105; Chapter_Digest_Book_12 L3, L15, L105; Romances_and_Rivalries L20; Glossary L54; Gods_and_Churches L89 | 14 |
| Ch47 | Tactical Playbook | Monsters L3; Book_12_Timeline L4; Chapter_Digest_Book_12 L4; Stash L61 | 4 |
| Ch48 | I Don’t Blow Up Cities on Purpose | Estercost_Culture L3, L22, L53; Cyrion L3, L4, L4-5, L22, L53; Estercost_Continent L3, L4-5, L22; Book_12_Timeline L3, L5; Chapter_Digest_Book_12 L3, L5; Locations_by_Era L4-5; Glossary L5; Li_Li_Mei L26 … | 21 |
| Ch49 | Following Through on Bad Ideas | Estercost_Culture L3; Storm_Kingdom_Culture L3; Book_12_Timeline L3; Chapter_Digest_Book_12 L3; Minor_Cast_Books_10-13 L3-5; Orin_Pensinata L5; Zara_Rimaros L7; Teams_by_Era L7 … | 11 |
| Ch50 | Heavily Compromised Baked Goods | Clothing_Food_Festivals_and_Transport_by_Region L3; Estercost_Culture L3; House_Headingway L3; Minor_Cast_Books_10-13 L3, L43-52, L120-126; Glossary L3; The_System L13-16, L28, L28-29, L29; Book_12_Timeline L15, L28, L43; Chapter_Digest_Book_12 L15, L28 … | 33 |
| Ch51 | The Line Between Mortal and Immortal | The_System L3, L13, L59, L76-77, L82-84; Locations_by_Era L3; Book_12_Timeline L3; Chapter_Digest_Book_12 L3; The_Return_and_the_Bridge L3; Minor_Cast_Books_10-13 L3-23; Clothing_Food_Festivals_and_Transport_by_Region L11; Estercost_Culture L13 … | 20 |
| Ch52 | A Petty Tyranny | Book_12_Timeline L3, L6, L8, L35, L44, L48; Chapter_Digest_Book_12 L3, L6, L8, L35; House_Headingway L6; Minor_Cast_Books_10-13 L6, L49, L50-62, L72; Calendar_Holidays_and_Naming_Customs L7; The_System L24, L30; Sadi_Andali_Culture L35-37, L41, L74; Sadi_Andali L35-37, L36-41, L41, L74 … | 30 |
| Ch53 | Reason Eighty-Seven | House_Headingway L3, L5, L6, L7, L8, L10 …; Cyrion L3; Book_12_Timeline L5, L24, L32, L57; Chapter_Digest_Book_12 L5, L32; Sadi_Andali_Culture L7; Sadi_Andali L7; Minor_Cast_Books_10-13 L8, L58-63, L61-62, L81; Daily_Life L32 … | 33 |
| Ch54 | Having Strangers Come Along | Minor_Cast_Books_10-13 L3-6; Book_12_Timeline L16, L29; Chapter_Digest_Book_12 L16, L29; Glossary L29; Nik_Asano L33-34 | 7 |
| Ch55 | Take Things Slow | Book_12_Timeline L21, L90; Chapter_Digest_Book_12 L21, L90 | 4 |
| Ch56 | The End of What Can Be Productively Achieved Here | Artefact_Site_One L3-4, L124; Open_Questions L3-4; 01_World_Primer L4; Travis_Noble L10; Liara_Rimaros L117; Zareen_Rimaros L117; Book_12_Timeline L117; Chapter_Digest_Book_12 L117 … | 13 |
| Ch57 | Someone Got Sucked Off | 00_Cosmology_Overview L3; The_Deep_Astral_and_Interstice L3, L4, L5-7, L9-10, L20; 00_Astral_Overview L3; Jota_Withers L3, L7-12, L14; Book_12_Timeline L3, L7, L22, L24, L36, L58; Chapter_Digest_Book_12 L3, L7, L22, L36; The_Return_and_the_Bridge L3; Era_Selection L3 … | 31 |
| Ch58 | A City With No Dawn | The_Deep_Astral_and_Interstice L39; Gabrielle_Pellin L41; Book_12_Timeline L41; Chapter_Digest_Book_12 L41; Name_Index L41; Merfolk L42-43; Emi_Evans_Asano L49; Craig_Vermillion L78-103, L89-90, L97, L103 | 11 |
| Ch59 | A Clark Kent Problem | Book_12_Timeline L5, L17, L24, L39, L60, L66 …; Chapter_Digest_Book_12 L5, L17, L24, L39; Master_Timeline L5; Glossary L5; Essence_Catalogue L9; Taika L35; The_Return_and_the_Bridge L60-72; Era_7_The_Return L60-72 | 19 |
| Ch60 | God-King | Book_12_Timeline L6, L10, L19, L33, L62, L93; Chapter_Digest_Book_12 L6, L10, L19; The_Return_and_the_Bridge L6-10; Cosmic_Throne_and_the_Sundering L16; World_Phoenix L16, L19-20; Reality_and_Genesis_Cores L28; The_Rules_of_Intrusion L52, L52-54; The_Deep_Astral_and_Interstice L68, L70-71 | 18 |
| Ch61 | Jason’s Arrival Inevitably Caused a Massive Problem | Book_12_Timeline L3, L17, L18, L29, L55, L105 …; Chapter_Digest_Book_12 L3, L55; Artefact_Site_One L16, L17, L18, L21, L22, L25 …; Lenora_Coleman L16, L22, L25; 00_Earth_Overview L17, L21; 00_Places_Overview L21; EDJI_and_Post_Reveal_Institutions L22; Minor_Cast_Books_10-13 L103-104 | 24 |
| Ch62 | It Sets a Tone | Book_12_Timeline L3, L4, L51, L98, L101, L117; Chapter_Digest_Book_12 L4, L51, L98, L101, L117; Leonids L4-9; Gary L4-9; Taika L4-9; Lenora_Coleman L28, L54, L80; Artefact_Site_One L45, L53; Minor_Cast_Books_10-13 L45, L64 | 21 |
| Ch63 | We Already Know Who You Are | Book_12_Timeline L3, L15, L16, L42, L61, L79 …; Chapter_Digest_Book_12 L3, L15; The_Rules_of_Intrusion L5, L6, L7, L9, L45; 01_World_Primer L7; 00_Cosmology_Overview L7; Cosmic_Throne_and_the_Sundering L9; Jota_Withers L16-19; The_Return_and_the_Bridge L16-19 … | 30 |
| Ch64 | Good Luck in Your Battle | Minor_Cast_Books_10-13 L12; The_Rules_of_Intrusion L20; Artefact_Site_One L21, L22-24; Book_12_Timeline L21, L48, L60, L74, L87, L93 …; Chapter_Digest_Book_12 L21, L48, L96; Lenora_Coleman L24; Jota_Withers L76, L76-79 | 19 |
| Ch65 | Second Chance to Make a First Impression | Minor_Cast_Books_10-13 L4; Book_12_Timeline L11, L53, L55; Chapter_Digest_Book_12 L53, L55 | 6 |
| Ch66 | The Right Move | Book_12_Timeline L5, L13, L34, L53, L62, L63 …; Chapter_Digest_Book_12 L5, L13; The_Return_and_the_Bridge L5-11; Dimensional_Storage_and_Portals L6; Lenora_Coleman L18-34; Hegemons_Will_and_Dominion L63-66, L67 | 16 |
| Ch67 | A Lot of Things to Do | Book_12_Timeline L5, L19, L22, L30, L42, L51 …; Chapter_Digest_Book_12 L5, L19, L22, L30, L51, L55; Astral_Kings_and_Messengers L23; Messengers_as_a_People L23; Artefact_Site_One L44-47; Master_Timeline L65, L113; Open_Questions L65, L113; Emi_Evans_Asano L146-149, L149 … | 109 |

### Book 13

| Chapter | Title | Cited by (lines) | Rows |
|---|---|---|---|
| Ch950 | A Person the Other Used to Know | Emi_Evans_Asano_Power_Set L27; Amy_Asano L27, L27-30, L28, L29, L30; Emi_Evans_Asano L27; The_Return_and_the_Bridge L27-41; Kaito_Asano L29, L33; Family_Trees L29; Romances_and_Rivalries L29, L30; Master_Timeline L29 … | 20 |
| Ch951 | Messy but Delicious | Book_13_Timeline L3-6, L50, L70; Chapter_Digest_Book_13 L3-6, L70; Nik_Asano L4-11, L7, L11; Dimensional_Storage_and_Portals L25; Hearth L33; Education L38-40; Book_12_Timeline L50; Master_Timeline L50 … | 20 |
| Ch952 | All Your Well-Learned Politesse | Book_13_Timeline L35; Chapter_Digest_Book_13 L35 | 2 |
| Ch953 | Perfect Humanoid Specimens | Book_13_Timeline L3; Chapter_Digest_Book_13 L3; Anna_Tilden L9; Engineers_of_Ascension L23; Sigrid_Freyn L39; Zareen_Rimaros L50-51, L56; Liara_Rimaros L51; Emi_Evans_Asano_Power_Set L84 … | 13 |
| Ch954 | Misgivings | Earth_Powers L3-6; Astral_Kings_and_Messengers L4; The_Cabal L4; Boris_Ket_Lundi L4, L5-6, L7-12, L9, L20; Goblins_and_Fairies L5; Messengers_as_a_People L5; The_Unorthodoxy L6, L6-7, L9; The_Council_of_Kings L7 … | 26 |
| Ch955 | The Unadulterated Jason | Book_13_Timeline L63; Chapter_Digest_Book_13 L63 | 2 |
| Ch956 | Emergent Situation | Zara_Rimaros L3, L40, L41; Romances_and_Rivalries L3; Minor_Cast_Books_4-6 L23; Emi_Evans_Asano L26, L56-58; Book_13_Timeline L41; Chapter_Digest_Book_13 L41 | 9 |
| Ch957 | When the Screaming Began | Book_13_Timeline L32; Chapter_Digest_Book_13 L32 | 2 |
| Ch958 | A Lot Harder Than Anticipated | Familiars_Summons_and_Conjurations L25; Familiars L25; Book_13_Timeline L25; Chapter_Digest_Book_13 L25; Hannah_and_Claire_Adeah L39, L61; Sigrid_Freyn L39; Glossary L39, L68; Humphrey_Geller L48 … | 17 |
| Ch959 | Without Consequences | Lorelei_Grantham L3; NPC_Rosters_by_Era L3, L60; Engineers_of_Ascension L36-38, L38, L92, L96; Audrey_Blaine L50, L60; Book_13_Timeline L59; Chapter_Digest_Book_13 L59; The_Cabal L114 | 12 |
| Ch960 | What It Will Do to Itself | Spirit_Vault_and_Astral_Kingdom L3; Emi_Evans_Asano L3-5; EDJI_and_Post_Reveal_Institutions L14; Locations_by_Era L14; Casselton_and_Asano_Village L14; Glossary L14-16; Li_Li_Mei L16; Book_13_Timeline L16, L23 … | 11 |
| Ch961 | The Scary Demigod Side | Book_13_Timeline L3, L6, L58; Chapter_Digest_Book_13 L3, L6; Natalie_Park L8; NPC_Rosters_by_Era L8; Era_7_The_Return L8; Lenora_Coleman L11; Minor_Cast_Books_10-13 L59; Glossary L73 | 11 |
| Ch962 | I Know What You Are | Book_13_Timeline L5, L6, L44, L62; Chapter_Digest_Book_13 L5, L6; The_Return_and_the_Bridge L5; Melody_Jain L56 | 8 |
| Ch963 | Minimum Collateral Damage | Hannah_and_Claire_Adeah L24; Glossary L24; Book_13_Timeline L56, L96; Chapter_Digest_Book_13 L56, L96; The_Reaper L57; Gary L63-68 | 8 |
| Ch964 | Expanding His Influence | Marie_Finnegan L3, L3-6, L3-36, L36; NPC_Rosters_by_Era L3; NPC_Cards_Books_10-13 L3; The_Network L9; Book_13_Timeline L9; Chapter_Digest_Book_13 L9; Master_Timeline L41 | 10 |
| Ch965 | This Is Kind of How Team Biscuit Operates | Book_13_Timeline L3, L42, L50, L71; Chapter_Digest_Book_13 L3, L42; Zara_Rimaros L86 | 7 |
| Ch966 | A Cultural Experience | Onslow L3; Book_13_Timeline L3, L4, L41, L55; Chapter_Digest_Book_13 L3, L4; Nik_Asano L71 | 8 |
| Ch967 | What I Present to the World | Book_13_Timeline L3, L10, L32; Chapter_Digest_Book_13 L3, L10; Minor_Cast_Books_10-13 L18-57; Gerling L25; NPC_Cards_Books_04-06 L25 | 8 |
| Ch968 | A Brief but Firm Reminder | Book_13_Timeline L4; Chapter_Digest_Book_13 L4; Adrien_Barbou L34-38, L45-54, L47-54, L54 | 6 |
| Ch969 | Good Lord | Book_13_Timeline L3; Chapter_Digest_Book_13 L3; Zara_Rimaros L56-63; Natalie_Park L88 | 4 |
| Ch970 | The Wisdom These Situations Demand | Engineers_of_Ascension L3, L16-18; The_Network L3, L5-13, L7; Book_13_Timeline L3, L29; Chapter_Digest_Book_13 L3, L29; Simon_McKean L38; Natalie_Park L52 | 11 |
| Ch971 | All the Fuel It Needed | Vincent_Baudrillard L3, L3-28, L3-56, L50, L51-52, L52 …; NPC_Rosters_by_Era L3, L49; NPC_Cards_Books_10-13 L3; Emi_Evans_Asano L30, L49; Romances_and_Rivalries L49; Era_7_The_Return L49; Education L51; House_Remore L51 … | 19 |
| Ch972 | Little Umbrellas | Book_13_Timeline L51; Chapter_Digest_Book_13 L51; Master_Timeline L51; Open_Questions L51; Emi_Evans_Asano L78, L78-82; NPC_Cards_Books_04-06 L78 | 7 |
| Ch973 | A Cruelty or a Mercy | Book_13_Timeline L24; Chapter_Digest_Book_13 L24; Messenger_War L24, L85; Gerling L46, L49; Marie_Finnegan L49; Remy L73-82; Elizabeth L82; Tera_Jun_Casta L85 | 10 |
| Ch974 | Most Practical Purposes | Natalie_Park L31; Minor_Cast_Books_10-13 L52; Book_13_Timeline L78; Chapter_Digest_Book_13 L78 | 4 |
| Ch975 | Your Terms Are Acceptable | Book_13_Timeline L3; Chapter_Digest_Book_13 L3; Minor_Cast_Books_10-13 L4; Earth_Powers L8, L19-24; Plot_Hooks L19-24; Era_7_The_Return L19-24; Marie_Finnegan L22, L22-24, L24; NPC_Cards_Books_10-13 L24 … | 13 |
| Ch976 | How Much Punishment They Could Live Through | Book_13_Timeline L5, L63, L80; Chapter_Digest_Book_13 L5, L63, L80; Minor_Cast_Books_10-13 L6; Master_Timeline L45; Gordon L49 | 9 |
| Ch977 | Getting Complicated Fast | Remy L48, L96-111, L118-125; Minor_Cast_Books_10-13 L107; Book_13_Timeline L126; Chapter_Digest_Book_13 L126 | 6 |
| Ch978 | Implications For Your Work | Book_13_Timeline L3, L13, L21; Chapter_Digest_Book_13 L3, L13, L21 | 6 |
| Ch979 | Unequivocally My Thing | Book_13_Timeline L3, L64, L76; Chapter_Digest_Book_13 L3, L64, L76; Emi_Evans_Asano L7, L17, L59; Nigel_Thornton L22; Marie_Finnegan L64, L64-72, L72; Remy L72; Earth_Vampire_War L72; Secrets_and_Rumours L72 … | 18 |
| Ch980 | The Only Cure is Death | Emi_Evans_Asano L73-77; Afflictions_Boons_and_Damage L93; Book_13_Timeline L93; Chapter_Digest_Book_13 L93 | 4 |
| Ch981 | What Forever Means | Book_13_Timeline L3, L5, L7, L11; Chapter_Digest_Book_13 L3, L5, L7, L11; Gordon L26, L37, L52; Shade L33-35, L37, L51, L62; The_Reaper L37, L62-64; Umber L37, L37-64, L62-64; Colin L37, L51, L52; The_Deep_Astral_and_Interstice L47 … | 25 |
| Ch982 | The Stuff of Faith and Madness | Book_13_Timeline L4; Chapter_Digest_Book_13 L4; EDJI_and_Post_Reveal_Institutions L30; Earth_Powers L30; Anna_Tilden L30; Holly_Macrossan L30, L42; NPC_Rosters_by_Era L30; Era_7_The_Return L30 | 9 |
| Ch983 | Something Worse | Book_13_Timeline L3, L15, L24, L84, L92; Chapter_Digest_Book_13 L3, L15, L24; Earth_Vampire_War L3, L15; Holly_Macrossan L62; Merfolk L113; Marie_Finnegan L113 | 13 |
| Ch984 | What Slumbers Under the Mountain | Book_13_Timeline L3, L12, L62; Chapter_Digest_Book_13 L3, L12; Marie_Finnegan L34; Remy L73 | 7 |
| Ch985 | Better Natures | Book_13_Timeline L3; Chapter_Digest_Book_13 L3; Remy L9, L18; Marie_Finnegan L32, L32-102 | 6 |
| Ch986 | The Deaths We Failed to Prevent | Book_13_Timeline L3, L6, L27; Chapter_Digest_Book_13 L3, L6, L27; Craig_Vermillion L27 | 7 |
| Ch987 | Consistent Agent of Chaos | Audrey_Blaine L10; Engineers_of_Ascension L12, L14, L24, L28, L35; Mr_North L12, L14, L16, L22-24, L27-28, L28; Book_13_Timeline L16, L37, L63; Chapter_Digest_Book_13 L16, L37; Secrets_and_Rumours L16; The_Rules_of_Intrusion L38; Vampire_War L63 … | 21 |
| Ch988 | If You Can’t Keep Up | Carlos_Quilido L4; Elizabeth L4; Ian_Evans L4; Vampire_War L26; Era_Selection L26; Plot_Hooks L26; Era_7_The_Return L26; Open_Questions L26 … | 13 |
| Ch989 | A Man Fought Monsters | Book_13_Timeline L3, L50, L68; Chapter_Digest_Book_13 L3, L50, L68; Minor_Cast_Books_10-13 L3-5, L9, L12, L50, L90; Essence_Catalogue L9; Earth_Powers L48; NPC_Rosters_by_Era L48; Era_7_The_Return L48 | 15 |
| Ch990 | Monstrous on the Inside | Book_13_Timeline L3, L21, L38, L65, L86; Chapter_Digest_Book_13 L3, L21; Titles_and_Blessings L61-65, L66-70, L70; Minor_Cast_Books_10-13 L66-70 | 11 |
| Ch991 | This Offer Kind of Sucks | Raythe L3, L3-42; Book_13_Timeline L3; Chapter_Digest_Book_13 L3; NPC_Cards_Books_07-09 L3; Era_7_The_Return L3; Lehenik L5; Keeper_of_Moments L7-11, L60-62, L66-68, L84-86; The_Rules_of_Intrusion L34 | 12 |
| Ch992 | Battle of the Plants | Book_13_Timeline L62; Chapter_Digest_Book_13 L62; The_Deep_Astral_and_Interstice L63; Authority_and_Sanctioning L63-64; Audrey_Blaine L116; Lorelei_Grantham L122-124; Romances_and_Rivalries L122-124 | 7 |
| Ch993 | True to Yourself | Book_13_Timeline L3, L109; Chapter_Digest_Book_13 L3, L109; Vampire_War L81; Earth_Vampire_War L81 | 6 |
| Ch994 | Not Open to Outside Consultation | EDJI_and_Post_Reveal_Institutions L39, L40, L45, L51, L53, L59-61 …; Earth_Powers L39; Holly_Macrossan L39; Book_13_Timeline L51; Chapter_Digest_Book_13 L51; Essence_Catalogue L78 | 12 |
| Ch995 | Symposium | EDJI_and_Post_Reveal_Institutions L14, L15-16, L57, L84; Miriam_Vance L14; Travis_Noble L14; Glossary L14; Book_13_Timeline L57, L69, L76; Chapter_Digest_Book_13 L57, L76; Earth_Vampire_War L57; Minor_Cast_Books_4-6 L64 … | 18 |
| Ch996 | The More I Listen, The More I Hear | NPC_Rosters_by_Era L3; Era_7_The_Return L3; Nik_Asano L5-9, L181; Book_13_Timeline L71; Chapter_Digest_Book_13 L71 | 6 |
| Ch997 | The Man Who Fought the Monsters | Progression_Tracks L11; Emi_Evans_Asano L11; Nik_Asano L11, L23; Master_Timeline L11; Sophie_Wexler L28-31; Clive_Standish L32; NPC_Rosters_by_Era L32; Neil_Davone L37-38 … | 13 |
| Ch998 | Sitting on a Volcano | Emi_Evans_Asano L3-4, L4; Emi_Evans_Asano_Power_Set L4; Nik_Asano L4; Book_13_Timeline L4, L99; Chapter_Digest_Book_13 L4, L99; Master_Timeline L4; Natalie_Park L105; Plot_Hooks L105 … | 13 |
| Ch999 | An Interesting Message | Cassandra_Mercer L3; Thalia_Mercer L3; Book_13_Timeline L3; Chapter_Digest_Book_13 L3; NPC_Cards_Books_01-03 L3; The_Council_of_Kings L77 | 6 |
| Ch1000 | Cosmic Tyrant Warlord Cult Leader | Jamis_Fran_Muskar L3; NPC_Cards_Books_10-13 L3; Era_7_The_Return L3; Boris_Ket_Lundi L3-7; The_Council_of_Kings L34-36, L36, L38, L40, L74; The_Unorthodoxy L36, L65-74, L65-76; Book_13_Timeline L37; Chapter_Digest_Book_13 L37 … | 16 |
| Ch1001 | It’s All Quite Australian | Michael_Mills L3, L4, L6, L7, L91, L91-94 …; Book_13_Timeline L6; Chapter_Digest_Book_13 L6; Master_Timeline L6; EDJI_and_Post_Reveal_Institutions L6-7, L8, L9, L44, L45, L46 …; Rufus_Remore L8; NPC_Rosters_by_Era L8; Earth_Magic L8-9, L9 … | 37 |
| Ch1002 | The One Who Gets to Decide | Book_13_Timeline L3, L68; Chapter_Digest_Book_13 L3, L68; Domains L5; Yumi_Asano L23, L31; Family_Trees L23; NPC_Cards_Books_04-06 L31; Simon_McKean L40-42; Michael_Mills L42, L49, L55, L65 … | 19 |
| Ch1003 | Stare Down the Devil | Simon_McKean L4-92, L9, L31, L47, L86; Jamis_Fran_Muskar L25, L26; Messenger_War L25; Nik_Asano L67-72, L72; NPC_Cards_Books_10-13 L72; Reality_and_Genesis_Cores L85; Book_13_Timeline L91; Chapter_Digest_Book_13 L91 … | 15 |
| Ch1004 | Scheduling Your Callous Dumping | Akari_Asano L3, L3-9, L5-23, L16; NPC_Cards_Books_04-06 L3, L16, L20; Family_Trees L4-5; Itsuki_Tiwari L4-24, L5, L18, L20; Master_Timeline L5; Romances_and_Rivalries L5-23, L44-52; Book_13_Timeline L18; Chapter_Digest_Book_13 L18 … | 18 |
| Ch1005 | A Distant God | Book_13_Timeline L3, L10, L80; Chapter_Digest_Book_13 L3, L10, L80; Ken_Asano L65-95, L83; Simon_McKean L104, L121; NPC_Cards_Books_10-13 L121 | 11 |
| Ch1006 | What You Gave Us Was Never Freedom | Craig_Vermillion L3; Simon_McKean L15, L60; EDJI_and_Post_Reveal_Institutions L31; Book_13_Timeline L34; Chapter_Digest_Book_13 L34; Plot_Hooks L59; Earth_Vampire_War L60; Era_7_The_Return L60 | 9 |
| Ch1007 | That Will Keep Them Dead | Book_13_Timeline L3, L6, L13, L41; Chapter_Digest_Book_13 L3, L6, L13; Earth_Vampire_War L3-5, L16; Vampire_War L3-16; Nigel_Thornton L16; Tone_and_Voice L22; Minor_Cast_Books_4-6 L39; Itsuki_Tiwari L43, L43-44, L43-46, L45 … | 21 |
| Ch1008 | A Sufficient Spectacle | Simon_McKean L5-33, L20-27, L33; Book_13_Timeline L10; Chapter_Digest_Book_13 L10; Vampire_War L20-27; Earth_Vampire_War L20-27, L33; Saint-Etienne L31-33; Gerling L33; Era_7_The_Return L33 … | 13 |
| Ch1009 | Kung-Fu Wizard is Not a Verb | Book_13_Timeline L4; Chapter_Digest_Book_13 L4; The_Cabal L81 | 3 |
| Ch1010 | Dangerously Exposing Myself | Simon_McKean L3; Book_13_Timeline L3, L5, L61, L69; Chapter_Digest_Book_13 L3, L5, L61, L69 | 9 |
| Ch1011 | Join Me, and Together We Could Rule the World! | Book_13_Timeline L18, L25, L44, L69; Chapter_Digest_Book_13 L18, L25, L44, L69; Vampire_War L18-44; Earth_Vampire_War L18-44; Belinda_Callahan L23; Estella_Warnock L23; Romances_and_Rivalries L23; NPC_Rosters_by_Era L23 … | 15 |
| Ch1012 | We Have to Kill Clive | Gordon L26; Book_13_Timeline L64; Chapter_Digest_Book_13 L64 | 3 |
| Ch1013 | Something Jasony | Book_13_Timeline L34; Chapter_Digest_Book_13 L34; Vampire_War L34; Earth_Vampire_War L34; Plot_Hooks L34 | 5 |
| Ch1014 | A Satisfying Day | Book_13_Timeline L3, L17, L34, L72, L91; Chapter_Digest_Book_13 L3, L17, L34; The_System L28-30; Gerling L72; Simon_McKean L75 | 11 |
| Ch1015 | A Fight She’s Already Won | Colin L26; EDJI_and_Post_Reveal_Institutions L39; Li_Li_Mei L40; Nik_Asano L48; The_Cabal L49; Book_13_Timeline L49; Chapter_Digest_Book_13 L49; Master_Timeline L49 … | 12 |
| Ch1016 | Worse Things | Hassan_Dukhtar L3, L3-31, L23-31, L31; Book_13_Timeline L3, L21, L107, L119; Chapter_Digest_Book_13 L3, L21, L107, L119; NPC_Cards_Books_10-13 L3; Jason_Asano L21; NPC_Rosters_by_Era L23; Rufus_Remore L23-27; Romances_and_Rivalries L23-27, L74 … | 29 |
| Ch1017 | A Room Full of Hands | Knowledge_States L3-50, L13-47, L31-32, L33, L40; The_Return_and_the_Bridge L4-47; Book_13_Timeline L5; Chapter_Digest_Book_13 L5; 00_Cosmology_Overview L6-8; Spoiler_Management L6-8, L14-24; Cosmic_Throne_and_the_Sundering L9, L9-11; The_Builder L9-11, L27 … | 65 |
| Ch1018 | I Don’t Need Hope | Book_13_Timeline L52; Chapter_Digest_Book_13 L52 | 2 |
| Ch1019 | Blatantly Ignoring Laws | Book_13_Timeline L3; Chapter_Digest_Book_13 L3; EDJI_and_Post_Reveal_Institutions L64 | 3 |
| Ch1020 | Adventurer | Book_13_Timeline L4; Chapter_Digest_Book_13 L4; The_System L6-7, L9, L11; Yumi_Asano L19; NPC_Cards_Books_04-06 L19; Michael_Mills L85, L91; Glossary L85-91; EDJI_and_Post_Reveal_Institutions L91 … | 18 |
| Ch1021 | The One Way I Know to Kill a God | Book_13_Timeline L4; Chapter_Digest_Book_13 L4; The_Return_and_the_Bridge L4; The_Cabal L36; EDJI_and_Post_Reveal_Institutions L40; Cosmic_Throne_and_the_Sundering L69-71 | 6 |
| Ch1022 | While We Have the Chance | Book_13_Timeline L3; Chapter_Digest_Book_13 L3; Erika_Asano L17; Hiro_Asano L19; Rimaros L20; Knowledge L25; Church_of_Knowledge L25; Dimensional_Storage_and_Portals L35 … | 14 |
| Ch1023 | Broken What Matters Most | Book_13_Timeline L3, L12; Chapter_Digest_Book_13 L3; The_Return_and_the_Bridge L3; Era_7_The_Return L3; Vampire_War L12; Open_Questions L12, L103; Kaito_Asano L33; Artefact_Site_One L103 … | 17 |
| Ch1024 | The Next Time We Meet | Book_13_Timeline L3, L82; Chapter_Digest_Book_13 L3, L82; Roland_Remore L14, L35; Soramir L14; Artefact_Site_One L57; Helsveth L75-81; NPC_Cards_Books_01-03 L75-81, L118-125; World_Phoenix L90 … | 36 |

## 6. State changes by book

Claims in the Cosmology, Organisations, Places and Characters documents that describe a death, birth, arrival, departure, gain, transformation or similar change, where the first reference grades **ok**. In story order. This list is generated by keyword and is a starting point for a change log, not a settled one.


## 7. Source-checking log

The history of the checking work, oldest first. Entries refer to earlier register states (their row IDs no longer exist). The register was rebuilt from the documents in the pass of 2026-10-22, which removed duplicate and cut-off rows and the rows of a deleted document.

| Date | Scope | Result | Note |
|---|---|---|---|
| 2026-10-20 | (all) | Register created | 639 rows harvested automatically from existing tags; none yet marked verified. |
| 2026-10-20 | (anchors) | Timeline anchors located | 30 anchors read at the lines; see section 6. Asano Village build time not found. |
| 2026-10-20 | R0017-R0620 (state-change rows) | 64 rows read at the lines | 44 verified, 20 partial, 0 mismatch (R0361 resolved: the quote is B8 Ch4 L116). Unlocated after reading: R0147, R0207, R0272, R0309, R0321, R0354-R0355, R0476, R0479, R0527, R0603, R0610-R0611. |
| 2026-10-20 | 07_Characters, 03_Magic (all rows) | Every row read at its candidate lines | Characters and Magic rows: 116 verified, 106 partial, 144 unlocated after reading, 0 not yet read (multi-book or table rows). Whole register: 145 verified, 112 partial, 144 unlocated, 84 probable, 127 candidate, 27 exact. |
| 2026-10-21 | TODO section H (33 items) | Each item searched; claims found, retagged or corrected | 24 claims found in the chapter files (e.g. B3 Ch21 L60 Gary almost silver, B3 Ch29 L35 Path of Shadows regional gate, B12 Ch67 L65 seventeen years); 8 retagged to notes; Path of Shadows range in Jason_Asano.md corrected (the two-hundred-kilometre figure was not in the books). |
| 2026-10-21 | Unlocated rows | Hand-searched; 18 spoiler-level labels removed from the register; 41 claims retagged from Book N to notes, Book N because the book lines were not found | Whole register now: 259 verified, 242 partial, 120 unlocated. 33 more unlocated claims could not be retagged automatically (listed in TODO section H). Spirit Vault rules resolved (R0257). |
| 2026-10-21 | 01_Primer, 08_Timeline, Appendices; Spirit Vault rules | Remaining rows read; Inventory/Spirit Vault entry rules resolved | Whole register now: 240 verified, 187 partial, 212 unlocated (including multi-book tags), 0 automatic only. Resolved R0257: Inventory (B4 Ch2 L70) only Jason; Spirit Vault (B4 Ch57 L59) those who implicitly trust him, sealable; B5 Ch44 L44-45 who could enter; B6 Ch13 L79 gate admits those he allows. |
| 2026-10-21 | 02_Cosmology, 05_Organisations, 06_Places (all rows) | Every row read at its candidate lines | Cosmology 47 verified / 22 partial / 21 unlocated; Organisations 41 / 31 / 18; Places 14 / 17 / 23. Whole register: 221 verified, 177 partial, 206 unlocated, 35 not yet read (Primer, Timeline, Appendices). Open conflict: R0257 (B4 Ch2 L70-73) says only the owner may enter the Inventory space. |

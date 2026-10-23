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
| Ch1 | Strange Business | Book_01_Timeline L3, L11, L16, L23, L103; Ken_Asano L4, L88; Jason_Asano L8-10, L76-81, L108; 01_World_Primer L23, L65; Unusual_and_Unique_Magic L37-43, L82-89, L93, L96-99; Cheryl_Asano L88; 00_Items_Overview L103-107; Tokens_Stones_and_Relics L103-107 … | 21 |
| Ch2 | Of Course Magic is a Thing | Monster_Cores_and_Training L32; 01_World_Primer L50-53; Monsters L57, L70 | 4 |
| Ch3 | Local Cuisine | Elves L43 | 1 |
| Ch4 | Cannibals and Spelunking | Goblins_and_Fairies L26; Awakening_Stones L40; Awakening_Stones L44 | 3 |
| Ch5 | Wizard | Book_01_Timeline L22, L26-27, L54 | 3 |
| Ch6 | Potent Potable | Book_01_Timeline L3-6; 01_World_Primer L15, L50; Alchemy_Artifice_and_Magical_Materials L46, L53-54, L54 | 6 |
| Ch7 | Spoils | Soul_Bound_Items_and_Regalia L17-21; Jason_Asano L26; Book_01_Timeline L38; Skill_Books_and_Learning L41-43, L46, L50-51, L55-58, L60; 01_World_Primer L68; Alchemy_Artifice_and_Magical_Materials L68; Glossary L68-69 | 11 |
| Ch8 | Dark Magic | Book_01_Timeline L32, L35, L59; Abilities_and_Attributes L34, L35, L62; Awakening_Stones L35, L51-57; Jason_Asano L35, L37; Jason_Power_Set_Reference L62; Skill_Books_and_Learning L88-93 | 12 |
| Ch9 | Escape | Book_01_Timeline L47; Cressida_Vane L47-50; Landemere_Vane L47-50; Era_Selection L50; Gary L121; Tone_and_Voice L121; Leonids L131 | 7 |
| Ch10 | The Evil Pit of Evil | Book_01_Timeline L23; Skill_Books_and_Learning L38 | 2 |
| Ch11 | Dashing Heroics | Gary L4-6; Awakening_Stones L17, L17-20; Rufus_Remore L49, L51; NPC_Rosters_by_Era L49; Book_01_Timeline L64, L80, L91-92; Minor_Cast_Books_1-3 L73; Glossary L73; Cressida_Vane L80, L81-83 | 13 |
| Ch12 | Sanguine Horror | Farrah_Hurin L11; NPC_Rosters_by_Era L11; Skill_Books_and_Learning L15; Monsters L70; Book_01_Timeline L72 | 5 |
| Ch13 | This is the Part Where We Step Back | Minor_Cast_Books_1-3 L3; Glossary L3; Book_01_Timeline L90, L107 | 4 |
| Ch14 | Worlds Apart | Leonids L14; Gary L14; NPC_Rosters_by_Era L14; Minor_Cast_Books_1-3 L18 | 4 |
| Ch15 | Outworlder | Skill_Books_and_Learning L41, L113; Elves L50, L51; Leonids L50, L84; Outworlders L50, L74-76; 00_Peoples_Overview L56; Humans L56; Essences L57, L58, L112, L113, L114; Ranks_and_Advancement L58, L85, L100 … | 25 |
| Ch16 | Rescue Party | Gary L28; Rufus_Remore L31-36, L38; 01_World_Primer L49; Glossary L51; Zartos L53-58, L57; 00_Places_Overview L57; Book_01_Timeline L95 | 9 |
| Ch17 | A Conservative Pillage | Alchemy_Artifice_and_Magical_Materials L21; Ken_Asano L31; Gary L58-61; 01_World_Primer L106; Daily_Life L106 | 5 |
| Ch18 | One of Us | Book_01_Timeline L3, L83; 01_World_Primer L5; Glossary L5 | 4 |
| Ch19 | I Want a Lava Cannon | Farrah_Hurin L1, L30; Ranks_and_Advancement L28, L42, L43; Confluences L30, L31; Essence_Catalogue L30, L68, L75; Essences L30, L31, L33, L45-56, L48-50, L50 …; 00_Magic_Overview L34, L40, L45-56, L50; Monsters L34, L35, L35-36, L36, L37-38, L40 …; Adventuring_Profession L36, L37-38, L38 … | 46 |
| Ch20 | By the Power of Grayskull | Confluences L19, L97-104, L110; Essences L19, L42-44, L44, L52, L53, L84 …; Essence_Catalogue L42-44, L49-50, L97, L104; Adventure_Society L44, L104-110; Abilities_and_Attributes L52; 00_Magic_Overview L84-86; Magic_Society_and_Associations L95-102 | 23 |
| Ch21 | I Have the Power | Essence_Catalogue L3, L6, L7, L49, L50, L61 …; Essences L3, L4, L6, L10-11, L36-37, L44 …; Book_01_Timeline L5, L48; Abilities_and_Attributes L6, L7, L15, L49, L50, L61 …; Awakening_Stones L7, L36-37; Confluences L53-54, L57; Gods_and_Churches L57; 00_Magic_Overview L57, L59-60 … | 40 |
| Ch22 | Apocalypse Stone | Essences L9, L38-41, L68; Ranks_and_Advancement L9, L33, L50-51, L55, L58, L60 …; 01_World_Primer L19, L20, L58; Daily_Life L19; Book_01_Timeline L19, L128; Master_Timeline L19; Auras L31-33, L35; Awakening_Stones L38-42, L45, L71, L72, L75, L76-77 … … | 55 |
| Ch23 | I May have Made a Huge Mistake | Rituals_Arrays_and_Formations L15, L16-17, L27, L30, L31-32, L32 …; Farrah_Hurin L15-17; Tone_and_Voice L15-17; Familiars_Summons_and_Conjurations L35-37, L36, L37, L38-39, L42-44, L61 …; Skill_Books_and_Learning L36; Awakening_Stones L61; Abilities_and_Attributes L62; Book_01_Timeline L66 | 25 |
| Ch24 | Astral Space | Book_01_Timeline L4, L5; 01_World_Primer L34; Astral_Spaces_Zones_and_Surges L38; Alchemy_Artifice_and_Magical_Materials L40, L48 | 6 |
| Ch25 | Blasphemy is Kind of My Thing | Book_01_Timeline L3; Daily_Life L13; Adventure_Society L17; Jason_Asano L43; Master_Timeline L43; Spoiler_Management L43 | 6 |
| Ch26 | Waterfall | Book_01_Timeline L60, L64 | 2 |
| Ch27 | Water, Fall | Abilities_and_Attributes L28; Monsters L91, L94-96; Monster_Cores_and_Training L94 | 4 |
| Ch28 | How Did You All Fit In There? | Afflictions_Boons_and_Damage L93 | 1 |
| Ch29 | That’s What Adventurers Do | Book_01_Timeline L5; Afflictions_Boons_and_Damage L15, L15-16, L16; Monsters L79; Monster_Cores_and_Training L79-81; Skill_Books_and_Learning L87 | 7 |
| Ch30 | Closing the Door Too Hard | Anisa_Lasalle L26, L86-93; Monsters L43, L44; Greenstone L43; Vitesse L44, L48; Leonids L47; Gary L47; Rufus_Remore L57-60, L88-93; Familiars L85, L89 … | 16 |
| Ch31 | Taming the Beast | Astral_Spaces_Zones_and_Surges L4, L71, L73-74, L74; Alchemy_Artifice_and_Magical_Materials L27, L27-28; Book_01_Timeline L69-73, L71-73, L74, L85; 01_World_Primer L71; Master_Timeline L71; 00_Magic_Overview L71-74, L96-98; Monster_Cores_and_Training L96, L98, L100, L102, L108-122, L110-114 …; Ranks_and_Advancement L96, L100 … | 27 |
| Ch32 | Monster Hunting For Beginners | Book_01_Timeline L26; Monsters L40; 01_World_Primer L52; Alchemy_Artifice_and_Magical_Materials L57; Adventure_Society L87 | 5 |
| Ch33 | Mistrun River | Book_01_Timeline L21, L31, L74 | 3 |
| Ch34 | Waving the Flag For Secular Morality | Book_01_Timeline L34, L57; Abilities_and_Attributes L39; Afflictions_Boons_and_Damage L40, L47 | 5 |
| Ch35 | Greenstone | Alchemy_Artifice_and_Magical_Materials L10, L21, L22, L23, L63; Jory_Tillman L10-12; NPC_Rosters_by_Era L10-12; Greenstone L15, L19, L59; Book_01_Timeline L15; Souls_Death_and_Healing L22, L23, L63; Essences L23; Astral_Spaces_Zones_and_Surges L31 … | 17 |
| Ch36 | The Island | Book_01_Timeline L7, L71; Alchemy_Artifice_and_Magical_Materials L28, L72; Greenstone L68, L71-72, L89, L95, L98; Economy_and_Money L71; Open_Questions L71; 01_World_Primer L72; Jason_Asano L87 | 13 |
| Ch37 | A Good Adventurer and a Great One | Book_01_Timeline L3; Greenstone L21; Danielle_Geller L21, L43-55; Rituals_Arrays_and_Formations L41-55; Daily_Life L83; Adventure_Society L93; Minor_Cast_Books_1-3 L98; Glossary L109 | 9 |
| Ch38 | Just Another Adventurer | Greenstone L3; Skill_Books_and_Learning L11; Book_01_Timeline L41, L56; Jason_Asano L45, L55; Adventuring_Profession L52; Alchemy_Artifice_and_Magical_Materials L52; Magic_Society_and_Associations L52; Tone_and_Voice L55 … | 23 |
| Ch39 | Training | Monster_Cores_and_Training L30; Greenstone L32-33, L34; Abilities_and_Attributes L70-71; Afflictions_Boons_and_Damage L70-71; Skill_Books_and_Learning L109, L110, L112, L115, L117; Awakening_Stones L137, L147-148, L150, L154; Book_01_Timeline L137, L154; Auras L152 | 17 |
| Ch40 | Eyebeams and the Ethics of Adventuring | Book_01_Timeline L3; Skill_Books_and_Learning L26; Jason_Asano L31, L50-52; Farrah_Hurin L31-35; Abilities_and_Attributes L37; Auras L37-41, L44, L46, L46-48, L50, L52 …; Afflictions_Boons_and_Damage L41, L42; Monster_Cores_and_Training L48 | 21 |
| Ch41 | Vulnerable and Exposed | Book_01_Timeline L27; Jason_Asano L35 | 2 |
| Ch42 | This is the Pits | Book_01_Timeline L21, L26, L30; Greenstone L21-23, L22, L29; Magic_Society_and_Associations L25, L30, L58, L64; Elves L25-30, L30; Lucian_Lamprey L25-30; NPC_Rosters_by_Era L25-30, L30, L44; Plot_Hooks L25-30, L58, L64; Pochard_Finn L30 … | 24 |
| Ch43 | Nightingale | Daily_Life L5; Celestines L18; Sophie_Wexler L18; NPC_Rosters_by_Era L18, L29; Clarissa_Ventress L29; Book_01_Timeline L67 | 7 |
| Ch44 | Complimentary Ointment | Book_01_Timeline L3, L14; Vincent_Trenslow L23; Gods_and_Churches L68 | 4 |
| Ch45 | So Much For Atheism | 01_World_Primer L4; Gods_and_Churches L4, L4-9, L18, L39; Religion_in_Practice L4, L5, L9, L18; Greenstone L4, L4-5; Daily_Life L5, L8; Runics L14, L14-18; Book_01_Timeline L38; Knowledge L40 | 17 |
| Ch46 | Blatant Manipulation | Gods_and_Churches L16; Knowledge L16; Tone_and_Voice L16; Book_01_Timeline L22, L33, L111 | 6 |
| Ch47 | Mirage Chamber | Book_01_Timeline L36; NPC_Rosters_by_Era L36, L89; Danielle_Geller L87-89, L89; Humphrey_Geller L88-89; Tone_and_Voice L88-89, L89 | 8 |
| Ch48 | An Endless, Inescapable Nightmare | Rituals_Arrays_and_Formations L3; Book_01_Timeline L49; Gods_and_Churches L92; Rufus_Remore L92-96; Gabriel_Remore L101-102; Spoiler_Management L101-102 | 6 |
| Ch49 | A Voice From Home | Greenstone L5; Book_01_Timeline L26-27, L98; Daily_Life L27; Gabriel_Remore L27; Danielle_Geller L42 | 6 |
| Ch50 | The Full Keanu | Skill_Books_and_Learning L20-22, L22, L41, L65-73, L67, L69 …; Book_01_Timeline L40-41; Great_Astral_Beings L41; Greenstone L85-91, L103, L104; Cole_Silva L92; Sophie_Wexler L92; Era_Selection L92; NPC_Rosters_by_Era L92 … | 18 |
| Ch51 | Song of the Nightingale | Book_01_Timeline L11 | 1 |
| Ch52 | Pain | Jason_Asano L7-11; Greenstone L46 | 2 |
| Ch53 | Nightlife | Book_01_Timeline L4; Cassandra_Mercer L45-49; Thalia_Mercer L45-49, L54; NPC_Rosters_by_Era L45-49 | 5 |
| Ch54 | Field Assessment | Thadwick_Mercer L17; Vincent_Trenslow L29; Adventure_Society L33, L35, L36; Book_01_Timeline L36; NPC_Rosters_by_Era L36; Tone_and_Voice L36; Alchemy_Artifice_and_Magical_Materials L52 | 9 |
| Ch56 | Gary’s Gift | Skill_Books_and_Learning L18, L47; Gary L46-51; Soul_Bound_Items_and_Regalia L47, L49-52; Book_01_Timeline L49, L77; Jason_Asano L49-52; 00_Items_Overview L49-52; Afflictions_Boons_and_Damage L53, L54 | 11 |
| Ch57 | Rainbow Smoke | Awakening_Stones L21; Adventuring_Profession L33; Adventure_Society L33 | 3 |
| Ch58 | A Man of Malevolent Intellect | Book_01_Timeline L3, L19, L85, L118; Monsters L40 | 5 |
| Ch59 | Falling Short | Alchemy_Artifice_and_Magical_Materials L8; Book_01_Timeline L18; Daily_Life L30 | 3 |
| Ch60 | Making Music | Book_01_Timeline L30, L34 | 2 |
| Ch61 | Trade Hall | Book_01_Timeline L17; Adventuring_Profession L32; Greenstone L32; Awakening_Stones L36; Alchemy_Artifice_and_Magical_Materials L40, L129; Economy_and_Money L63-65, L65, L114; 01_World_Primer L65; NPC_Rosters_by_Era L76 … | 13 |
| Ch62 | Have Some Damn Adventures | Book_01_Timeline L5, L44, L67; Badges_and_Guild_Membership L44, L46, L47, L47-48, L61; Adventure_Society L46, L47, L47-54, L61, L81-85, L91; Adventuring_Profession L55-59, L61, L64, L66, L68-70, L70 …; Unusual_and_Unique_Magic L55-59; Vincent_Trenslow L61-93; Era_Selection L66-67 | 27 |
| Ch63 | Sunk-Cost Fallacy | Adventuring_Profession L54, L77, L81; Book_01_Timeline L108 | 4 |
| Ch64 | Take My Wife, Please | Adventuring_Profession L3, L5, L12, L81; Adventure_Society L3; Minor_Cast_Books_1-3 L5; Alchemy_Artifice_and_Magical_Materials L12; Awakening_Stones L80, L81; Awakening_Stones L80, L81, L82 | 12 |
| Ch65 | Curious Urges | Gilbert_Bertinelli L6; Book_01_Timeline L50, L60, L99; Adventure_Society L60; Elspeth_Arella L60; NPC_Rosters_by_Era L60; Auras L91; Gods_and_Churches L130; Anisa_Lasalle L132 | 10 |
| Ch66 | A Stronger Weapon Than the One in Your Hand | Phoebe_Geller L3-4; Humphrey_Geller L3-6, L58, L58-62; Book_01_Timeline L7; Hannah_and_Claire_Adeah L31; Rick_Geller L58-62, L61, L62; Adventuring_Profession L60; Jonah_Geller L72-78 | 11 |
| Ch67 | This is What it Means to Fight Me | Jonah_Geller L14-15, L66; Hannah_and_Claire_Adeah L15, L18-33, L71-95, L126-128; NPC_Rosters_by_Era L15; Glossary L15; Book_01_Timeline L95 | 9 |
| Ch68 | Good News For Clive | Familiars_Summons_and_Conjurations L20, L22; Book_01_Timeline L65, L102, L106; Clive_Standish L92-94; Tone_and_Voice L92-94; Alchemy_Artifice_and_Magical_Materials L114 | 8 |
| Ch69 | Dumpling Soup | Skill_Books_and_Learning L84; 01_World_Primer L85; 00_Cosmology_Overview L85-91; Glossary L85-96; 00_Astral_Overview L85-107, L97-99; 00_Characters_Overview L85-107; Clive_Standish L85-107; Familiars L85-107 … | 15 |
| Ch70 | Rewards | Book_01_Timeline L47 | 1 |
| Ch71 | A Bit of Poo | Greenstone L3, L38; Beth_Cavendish L3; 01_World_Primer L7; Runics L40; Glossary L53; Monsters L65 | 7 |
| Ch72 | Rat Race | Book_01_Timeline L11, L24 | 2 |
| Ch73 | A Grim Sword to Live By | Book_01_Timeline L25-28, L57; Monsters L46-51; Essence_Catalogue L49, L51 | 5 |
| Ch74 | Doing Better | Humphrey_Geller L70; Book_01_Timeline L70 | 2 |
| Ch75 | Progress | Familiars_Summons_and_Conjurations L27-28, L33; Book_01_Timeline L33, L69; Skill_Books_and_Learning L72 | 5 |
| Ch76 | Preparations | Gilbert_Bertinelli L3-5; Book_01_Timeline L13, L23, L58; Dimensional_Storage_and_Portals L43, L49, L58 | 7 |
| Ch77 | Group Cohesion | Gods_and_Churches L10; Knowledge L10; Book_01_Timeline L50, L51; Economy_and_Money L51; Adventuring_Profession L60 | 6 |
| Ch78 | Jason Has the Good Biscuits | Book_01_Timeline L31; Glossary L44; Jason_Asano L54; Familiars L84, L84-85 | 5 |
| Ch80 | It’s Not Work if You Love What You Do | Minor_Cast_Remore_Academy_and_Greenstone_Teams L5-48; Alchemy_Artifice_and_Magical_Materials L21, L43, L104; Economy_and_Money L21, L23, L27-28, L37, L39, L40-41 …; Daily_Life L40; Greenstone L42; 00_Astral_Overview L42; Book_01_Timeline L62; Law_and_Indenture L78 | 18 |
| Ch81 | Crazy Desperation Move | Book_01_Timeline L3, L44; Ustei L43 | 3 |
| Ch82 | Choices | Book_01_Timeline L8; Alchemy_Artifice_and_Magical_Materials L57; Gods_and_Churches L73 | 3 |
| Ch83 | It Makes No Difference to the Ant | Ustei L4; Book_01_Timeline L4, L55; Era_Selection L4; Plot_Hooks L4; Open_Questions L4; NPC_Rosters_by_Era L23; Beth_Cavendish L23-43; Minor_Cast_Remore_Academy_and_Greenstone_Teams L38 … | 11 |
| Ch84 | Injury & Death | Book_01_Timeline L41, L82; Monsters L55, L57; 00_Magic_Overview L57; Badges_and_Guild_Membership L101 | 6 |
| Ch85 | Because I’m an Adventurer | Skill_Books_and_Learning L8; 00_Peoples_Overview L22-26, L35, L39, L41, L47; Humans L22-26, L35; Clive_Standish L22-26, L51; Smoulder_and_Brighthearts L45; Great_Astral_Beings L51; Rituals_Arrays_and_Formations L60 | 13 |
| Ch86 | Some Kind of Secret | Book_01_Timeline L9, L123; Greenstone L25; Draconians L31; Runics L31; 00_Peoples_Overview L40; Clive_Standish L115-116 | 7 |
| Ch87 | Can’t Lose | Badges_and_Guild_Membership L39; Book_01_Timeline L51, L85; Monsters L53; Jason_Asano L85; Abilities_and_Attributes L91; Awakening_Stones L91; Essences L91; Afflictions_Boons_and_Damage L97, L99 … | 14 |
| Ch88 | The Nature of Absolution | Book_01_Timeline L25, L46; Skill_Books_and_Learning L80-85; Humphrey_Geller L94-106; Awakening_Stones L118-125; Afflictions_Boons_and_Damage L132 | 6 |
| Ch89 | Anti-Pirate Operations | Book_01_Timeline L3-5, L50, L77; Ustei L50, L50-51, L68; Plot_Hooks L50; Open_Questions L50; Beth_Cavendish L53-85, L77; Minor_Cast_Remore_Academy_and_Greenstone_Teams L54, L63, L72, L85; Smoulder_and_Brighthearts L63 | 15 |
| Ch90 | The Path to Bronze | Minor_Cast_Remore_Academy_and_Greenstone_Teams L12, L13, L15; Book_01_Timeline L14; Desert_Transport_Skimmers_and_Barges L14; Beth_Cavendish L61 | 6 |
| Ch91 | Life & Death | Book_01_Timeline L5, L53; Adventuring_Profession L34; Awakening_Stones L34; Adventure_Society L34; Alchemy_Artifice_and_Magical_Materials L58 | 6 |
| Ch92 | Unusual Contract | Book_01_Timeline L12, L65; Economy_and_Money L32; Law_and_Indenture L32, L33-34, L36; Plot_Hooks L32; Ustei L36; Leust L59-65, L61, L63; Minor_Cast_Books_1-3 L65; Skill_Books_and_Learning L95 | 13 |
| Ch93 | Truth | Leust L3, L5, L5-6, L5-8, L22, L24 …; Daily_Life L5; 00_Places_Overview L5; Book_01_Timeline L5, L69, L73, L80; Master_Timeline L5; Era_Selection L5; Minor_Cast_Books_1-3 L24-29; Familiars_Summons_and_Conjurations L41 … | 19 |
| Ch94 | Consequences | Gods_and_Churches L3, L3-7; Religion_in_Practice L3; Greenstone L3; Book_01_Timeline L3, L70; Neil_Davone L3-7; Plot_Hooks L3-7; Leust L8-13, L58; Minor_Cast_Books_1-3 L16, L25-58 | 12 |
| Ch95 | Punishment | Souls_Death_and_Healing L69, L126; Book_01_Timeline L78, L90; Gods_and_Churches L90-94, L94, L104; Gary L104 | 8 |
| Ch96 | You Don’t Get a Third | Essences L18; Book_01_Timeline L24, L47 | 3 |
| Ch97 | Integrity is Sexy | Book_01_Timeline L17, L29, L93; Open_Questions L19-21 | 4 |
| Ch98 | The Point of Money and Power | Desert_Transport_Skimmers_and_Barges L4; Book_01_Timeline L57, L70; Adventure_Society L63; Minor_Cast_Books_1-3 L63; Badges_and_Guild_Membership L82 | 6 |
| Ch99 | Someone Else’s Game | Jason_Asano L24, L67-70; Emir_Bahadir L36; Book_01_Timeline L36, L43, L61; Monsters L61; Abilities_and_Attributes L65; Essence_Catalogue L67-70; Monster_Cores_and_Training L155; Afflictions_Boons_and_Damage L166, L169 … | 13 |
| Ch100 | Legwork | Desert_Astral_Space L8; Book_01_Timeline L69, L79; Auras L85 | 4 |
| Ch101 | Fantasy World Goodness | Book_01_Timeline L4, L64, L98; Minor_Cast_Books_1-3 L9; Auras L16; Ranks_and_Advancement L16; Emir_Bahadir L64; Cloud_Constructs_and_Palaces L64, L103; NPC_Rosters_by_Era L64 | 10 |
| Ch102 | You Fight Like Me | 01_World_Primer L11; 00_Places_Overview L11; Hornis L11; Book_01_Timeline L57; Auras L93 | 5 |
| Ch103 | Silver Hair | Auras L16; Rituals_Arrays_and_Formations L44; Clive_Standish L44; Book_01_Timeline L53, L64; Greenstone L120; Afflictions_Boons_and_Damage L130 | 7 |
| Ch104 | An Outcome That Satisfies | Book_01_Timeline L16, L88; Astral_Spaces_Zones_and_Surges L60-61, L61; Danielle_Geller L60-61; Adris_Dorgan L68; NPC_Rosters_by_Era L68; Greenstone L88 | 8 |
| Ch105 | You Aren’t in Control of What Happens Next | Book_01_Timeline L5-6, L33, L57, L66; Law_and_Indenture L66 | 5 |
| Ch107 | All the Good People We Can Get | Desert_Astral_Space L3, L76; Book_01_Timeline L27; Minor_Cast_Books_1-3 L49; Badges_and_Guild_Membership L51 | 5 |
| Ch108 | You Don’t Have the Strength | Cloud_Constructs_and_Palaces L3; Book_01_Timeline L26, L72; Essences L28; Greenstone L35; Emir_Bahadir L35; Danielle_Geller L35-37; Desert_Astral_Space L90, L97; Farrah_Hurin L94 … | 11 |
| Ch109 | The Tyranny of Rank | Hester_Maharala L6, L7-9; NPC_Rosters_by_Era L6; Boko L7-21, L9, L21; Desert_Astral_Space L8; Open_Questions L8; Book_01_Timeline L10; Desert_Transport_Skimmers_and_Barges L21; Rufus_Remore L23 … | 12 |
| Ch110 | Help Arrives | 00_Astral_Overview L3; Desert_Transport_Skimmers_and_Barges L4, L13; Book_01_Timeline L6, L7, L16, L17, L27, L32 …; Dustin_Kettering L17; Essence_Catalogue L20; Neil_Davone L40; Danielle_Geller L51 | 14 |
| Ch111 | Strange Star | Book_01_Timeline L19, L41, L78; Astral_Spaces_Zones_and_Surges L24, L28; 00_Astral_Overview L28 | 6 |
| Ch112 | The Accumulation of a Life | Book_01_Timeline L14, L26, L52; Dimensional_Storage_and_Portals L17; Boko L52; Gods_and_Churches L96 | 6 |
| Ch113 | You Need to Work on Making Enemies | Boko L21, L28; Book_01_Timeline L36, L41, L65, L75; Farrah_Hurin L41; Era_Selection L41; NPC_Rosters_by_Era L41; Desert_Astral_Space L45; Desert_Transport_Skimmers_and_Barges L45, L52; Dimensional_Storage_and_Portals L58 … | 14 |

### Book 2

| Chapter | Title | Cited by (lines) | Rows |
|---|---|---|---|
| Ch1 | Climbing Mountains | Emir_Bahadir L3; Cloud_Constructs_and_Palaces L3; Book_02_Timeline L4, L90; Skill_Books_and_Learning L47; Law_and_Indenture L77; Sophie_Wexler L77-80; Tone_and_Voice L77-80; Constance L112, L124 … | 11 |
| Ch2 | Nothing Can Hurt You Like Hope | Book_02_Timeline L21, L23, L58, L60, L100 | 5 |
| Ch3 | See You in Court | Law_and_Indenture L43; Book_02_Timeline L53, L76, L77 | 4 |
| Ch4 | Six-Month Lease | Book_02_Timeline L7, L24, L111; Hannah_and_Claire_Adeah L10; Cassandra_Mercer L19-29 | 5 |
| Ch5 | The Perks of Being an Essence User | Book_02_Timeline L37, L116; Sophie_Wexler L37-41, L82-87; Danielle_Geller L46; Confluences L82-87, L83, L87; Essence_Catalogue L82-87; Essences L82-87; Emir_Bahadir L88; Awakening_Stones L105, L105-107, L108-110 | 14 |
| Ch6 | This is the Moment | Book_02_Timeline L3; 01_World_Primer L5; Rituals_Arrays_and_Formations L41, L43; Abilities_and_Attributes L43; Awakening_Stones L43; Essence_Catalogue L56 | 7 |
| Ch7 | Iron Rank | Book_02_Timeline L28, L116; Dimensional_Storage_and_Portals L47; Clive_Standish L62; Rituals_Arrays_and_Formations L117, L130; Sophie_Wexler L129; Afflictions_Boons_and_Damage L162 | 8 |
| Ch8 | Getting Stoned | Book_02_Timeline L28; Afflictions_Boons_and_Damage L44; Abilities_and_Attributes L45, L170-171, L171, L174-175; Confluences L45-49; Emir_Bahadir L168; Cloud_Constructs_and_Palaces L168; Sophie_Wexler L170-173 | 10 |
| Ch9 | Children | Awakening_Stones L9, L17, L17-18, L29, L38, L40 …; Essence_Catalogue L9, L17, L21; Essences L21; Clive_Standish L21; 01_World_Primer L30-31; Abilities_and_Attributes L31-35; Book_02_Timeline L51, L67; Master_Timeline L67 … | 19 |
| Ch10 | Star Seed | Adventure_Society L16; Jonah_Geller L26-50; Plot_Hooks L26-50; Book_02_Timeline L51, L62; Open_Questions L51; Badges_and_Guild_Membership L85; Greenstone L92; Anisa_Lasalle L92, L102 … | 11 |
| Ch11 | It’s About How You Use It | Book_02_Timeline L3; Jason_Asano L41 | 2 |
| Ch12 | We End Here | Belinda_Callahan L6; Book_02_Timeline L82, L88, L102; Badges_and_Guild_Membership L83 | 5 |
| Ch13 | Poison Pill | Book_02_Timeline L8, L60, L95, L128; Neil_Davone L19; Tokens_Stones_and_Relics L57, L60, L62, L66, L76-78; Gods_and_Churches L60, L103; 00_Items_Overview L60; Awakening_Stones L60; Awakening_Stones L60-62, L62, L66, L70, L71-76, L76-78 …; 00_Magic_Overview L60-90 … | 27 |
| Ch14 | Let’s Just Fight Monsters | Hornis L16, L116; Book_02_Timeline L20, L35; Jason_Asano L35; Jonah_Geller L116 | 6 |
| Ch15 | Damage You Shouldn’t Walk Away From | Badges_and_Guild_Membership L10; Hornis L25; Minor_Cast_Books_1-3 L27; Book_02_Timeline L29; Adventuring_Profession L38; Dustin_Kettering L44; Minor_Cast_Remore_Academy_and_Greenstone_Teams L44 | 7 |
| Ch16 | Picking Out the Good Ones | Book_02_Timeline L75 | 1 |
| Ch17 | Events Loom Large | Boko L60, L61; Hornis L60, L61; Book_02_Timeline L61, L109, L113 | 7 |
| Ch18 | What the Geller Name is Worth | Rituals_Arrays_and_Formations L11; Clive_Standish L25-27 | 2 |
| Ch19 | Cleansed | Book_02_Timeline L31; Dimensional_Storage_and_Portals L60; Nicolas_Hendren L73; NPC_Rosters_by_Era L73; Rituals_Arrays_and_Formations L77, L79; Emir_Bahadir L93 | 7 |
| Ch20 | It Just Takes Practise | Cheryl_Asano L18; Jason_Asano L18; Book_02_Timeline L23; Familiars L29 | 4 |
| Ch21 | World Building | Adventuring_Profession L14; Book_02_Timeline L19, L23, L26, L92, L94, L123; Glossary L21; Consumables_and_Trial_Rewards L26-28; Era_Selection L26-28; Spoiler_Management L26-28, L112; Great_Astral_Beings L26-30, L36, L106-112, L112; Clive_Standish L94-98 … | 20 |
| Ch22 | Fabulous Prizes | Hornis L76; Book_02_Timeline L82, L90, L146; Clive_Standish L127-129 | 5 |
| Ch23 | Any Team Except Yours | Book_02_Timeline L6; Neil_Davone L17; Alchemy_Artifice_and_Magical_Materials L72 | 3 |
| Ch24 | More Than One Clown | Book_02_Timeline L3, L38; Auras L13; Dimensional_Storage_and_Portals L13 | 4 |
| Ch25 | Resurrection | Book_02_Timeline L3, L39, L53; Consumables_and_Trial_Rewards L24-26, L35; Great_Astral_Beings L37-45; Cults_and_Orders L37-45, L73, L73-74; Ranks_and_Advancement L49; Souls_Death_and_Healing L51, L53, L54, L55, L57-58, L59; Outworlders L57, L59, L61; Familiars_Summons_and_Conjurations L59 … | 25 |
| Ch26 | Manifestation | Book_02_Timeline L19; Goblins_and_Fairies L99 | 2 |
| Ch27 | Potential | Hornis L4; Book_02_Timeline L25, L44; Dustin_Kettering L41, L57; Neil_Davone L41-43, L41-48, L43, L46, L57, L59 …; Cassandra_Mercer L43-48; Tone_and_Voice L46 | 14 |
| Ch28 | Weaponising a Barbecue | Gabrielle_Pellin L25-30; Humphrey_Geller L25-30, L32; Confluences L44, L56; Essence_Catalogue L44, L56; Essences L44, L56; Neil_Davone L44; NPC_Rosters_by_Era L44; Familiars_Summons_and_Conjurations L46, L48 … | 14 |
| Ch29 | This Town Ain’t Big Enough | Book_02_Timeline L3, L9; Hannah_and_Claire_Adeah L6-8; Adventuring_Profession L8; Dustin_Kettering L8, L9, L59, L69; NPC_Rosters_by_Era L8 | 9 |
| Ch30 | The Second-Best Iron Ranker | Minor_Cast_Remore_Academy_and_Greenstone_Teams L4, L15, L16, L22; Book_02_Timeline L32; Neil_Davone L52-54; Clive_Standish L53; Beth_Cavendish L80 | 8 |
| Ch31 | Arrival | Book_02_Timeline L4, L21 | 2 |
| Ch32 | Full Jason | Glossary L12; Desert_Transport_Skimmers_and_Barges L38; Dimensional_Storage_and_Portals L38; Arabelle_Remore L52; Gabriel_Remore L52; Book_02_Timeline L52, L58; Confluences L67-72; Essences L67-72 … | 14 |
| Ch33 | Versatile | Vitesse L6; Rufus_Remore L6; Book_02_Timeline L94 | 3 |
| Ch34 | I Don’t Like This Plan | Book_02_Timeline L10, L19, L45, L47, L80, L91; Hester_Maharala L55; 01_World_Primer L58, L73; Pranay_Culture L58; Ranks_and_Advancement L73; Callum_Morse L91; NPC_Rosters_by_Era L91 | 13 |
| Ch36 | The Price We Pay Doesn’t Matter | Book_02_Timeline L36, L68; Callum_Morse L79 | 3 |
| Ch37 | Make the Most of It | Book_02_Timeline L24, L31, L33, L55, L62; Cults_and_Orders L31; Landemere_Vane L67; Anisa_Lasalle L105-114 | 8 |
| Ch38 | Wake | Book_02_Timeline L4, L40, L61, L69; Glossary L23; Draconians L29; Leonids L29; Padma_Parsell L35, L40-41, L42, L43, L65, L84; NPC_Rosters_by_Era L65; Farrah_Hurin L69 | 15 |
| Ch39 | I Can’t Trust Any of It | Book_02_Timeline L8, L11; Minor_Cast_Remore_Academy_and_Greenstone_Teams L12, L37; Padma_Parsell L13; Draconians L15, L34 | 7 |
| Ch40 | Legacy | 01_World_Primer L3; Book_02_Timeline L27, L57, L59, L63; Alchemy_Artifice_and_Magical_Materials L61; Desert_Transport_Skimmers_and_Barges L80, L81 | 8 |
| Ch41 | A Rash Decision | Book_02_Timeline L4, L67 | 2 |
| Ch42 | It’s A Good One | Book_02_Timeline L52, L77; Familiars_Summons_and_Conjurations L70; Dimensional_Storage_and_Portals L79; Alchemy_Artifice_and_Magical_Materials L86; 01_World_Primer L96 | 6 |
| Ch43 | The City of Fallen Echoes | Book_02_Timeline L7, L95; Dimensional_Storage_and_Portals L24; Monsters L56 | 4 |
| Ch44 | Shade | Gilbert_Bertinelli L8; Familiars L37, L93; Book_02_Timeline L39, L57, L76, L85, L87, L93 …; City_of_Fallen_Echoes L39-41, L41-45, L47, L57-59, L119-128; Cults_and_Orders L72-78, L85-89, L99-109; Spoiler_Management L72-78; Consumables_and_Trial_Rewards L120-123, L127-129; Glossary L127-129 … | 23 |
| Ch45 | Seriously Hardcore | Monsters L7; City_of_Fallen_Echoes L7; Book_02_Timeline L30, L52; Sophie_Wexler L69-72; Tone_and_Voice L69-72 | 6 |
| Ch46 | Mixed Medication | Book_02_Timeline L50, L61 | 2 |
| Ch47 | Giving People Choices | Book_02_Timeline L30; Adventuring_Profession L59; Monsters L59 | 3 |
| Ch48 | A Well-Informed Man | Book_02_Timeline L43; Minor_Cast_Remore_Academy_and_Greenstone_Teams L58; Adventuring_Profession L61; Valdis_Volaire L77; NPC_Rosters_by_Era L77 | 5 |
| Ch49 | The Danger is Us | Book_02_Timeline L22 | 1 |
| Ch50 | Surplus to Requirements | Book_02_Timeline L5; Abilities_and_Attributes L57 | 2 |
| Ch51 | A Worse Plan | Valdis_Volaire L8, L9-10, L17, L28, L32, L42 …; Glossary L8; Alchemy_Artifice_and_Magical_Materials L98 | 9 |
| Ch52 | No One Has That Coming | Book_02_Timeline L34, L51, L71; Afflictions_Boons_and_Damage L51 | 4 |
| Ch53 | Part of Being a Team | Book_02_Timeline L13, L64; Vitesse L27; Open_Questions L27; Monsters L28-29, L29; Alchemy_Artifice_and_Magical_Materials L70 | 7 |
| Ch54 | Making a Spectacle of Himself | Book_02_Timeline L6, L70, L122 | 3 |
| Ch55 | Team Change | Glossary L3-4; Book_02_Timeline L9, L12; Sigrid_Freyn L58; Valdis_Volaire L63; Padma_Parsell L69 | 6 |
| Ch56 | Company Worth Keeping | Sigrid_Freyn L5-14; Book_02_Timeline L13, L57, L73, L82; Essences L92, L93; Awakening_Stones L93, L94 | 9 |
| Ch57 | He Who Fights With Monsters | City_of_Fallen_Echoes L29, L68, L70; Awakening_Stones L31, L31-33; Awakening_Stones L36; Valdis_Volaire L63; Monsters L68; 00_Astral_Overview L68; Book_02_Timeline L68, L93, L142 | 12 |
| Ch58 | Irreconcilable Ideals | City_of_Fallen_Echoes L9-24, L70-74, L100-102; Book_02_Timeline L35, L41, L62, L102; Consumables_and_Trial_Rewards L53-56, L102-104 | 9 |
| Ch59 | Meanwhile, Two Weeks Ago in Greenstone… | Book_02_Timeline L3, L22, L115; Minor_Cast_Books_1-3 L4, L22; Glossary L4; Confluences L83; Essence_Catalogue L83; Cults_and_Orders L87; NPC_Rosters_by_Era L87; Timos L87-90, L106-110 … | 13 |
| Ch60 | Take the Loot and Go | Book_02_Timeline L13, L50, L120, L179; City_of_Fallen_Echoes L54-56; Spoiler_Management L120-122; Open_Questions L120-122, L185; Cults_and_Orders L120-123; Tokens_Stones_and_Relics L173-179 | 10 |
| Ch61 | Making an Exit | Beth_Cavendish L51; Valdis_Volaire L74; Unusual_and_Unique_Magic L130, L130-147, L138-142, L141, L144, L144-147 …; Book_02_Timeline L131, L144, L147; Humans L144, L147; Elves L145; Celestines L146; Sophie_Wexler L146 … | 20 |
| Ch62 | Shallow Earth | Book_02_Timeline L3, L24; Danielle_Geller L24; Henrietta_Geller L24; Keith_Geller L24; Familiars L50 | 6 |
| Ch63 | Relief | Book_02_Timeline L9; Era_Selection L9; Awakening_Stones L25, L73, L115; Tokens_Stones_and_Relics L37-38, L45-47, L65-82; 00_Items_Overview L38; Glossary L45-47; Awakening_Stones L65; Familiars_Summons_and_Conjurations L73, L92, L100, L115 … | 17 |
| Ch64 | Glory | Awakening_Stones L3-5; Familiars_Summons_and_Conjurations L5, L15; Neil_Davone L55; Awakening_Stones L72; Essences L124-126; Monster_Cores_and_Training L151 | 7 |
| Ch65 | Display of Gratitude | Book_02_Timeline L18, L22, L47, L78, L85, L95-96; Zara_Rimaros L55; Jason_Asano L85; Auras L85-86, L86-87; Confluences L94; Essence_Catalogue L94; Adventure_Society L96; Awakening_Stones L96 | 14 |
| Ch66 | The Person I Decided to Be | Auras L8; Awakening_Stones L66; Rituals_Arrays_and_Formations L90; Gods_and_Churches L105 | 4 |
| Ch67 | You Have Friends to Help You | Rituals_Arrays_and_Formations L3, L162; Book_02_Timeline L49, L168; Unusual_and_Unique_Magic L113 | 5 |
| Ch68 | Blob Body | Book_02_Timeline L36, L129; Belinda_Callahan L39-45 | 3 |
| Ch69 | Particular Appetites | Killian_Laurent L12; Zara_Rimaros L16, L17-19, L18; Book_02_Timeline L17, L25, L95; Tone_and_Voice L17-19; Hester_Maharala L64, L65-66, L69-72; Pranay_Culture L65; 00_Places_Overview L65-66; Jayapura L65-66, L66 … | 16 |
| Ch70 | Domineering, Territorial and Robust | Pranay_Culture L3; Jayapura L3; Essences L30; Souls_Death_and_Healing L33-35, L36, L37-38, L39, L42, L44; 01_World_Primer L34-42; Auras L37; Hester_Maharala L70; Book_02_Timeline L103 | 13 |
| Ch71 | More Shady as We Go Along | Neil_Davone L14; Book_02_Timeline L26, L43, L103; Familiars_Summons_and_Conjurations L50 | 5 |
| Ch72 | Magnificent Entity | Familiars L15; Book_02_Timeline L28, L29, L98; Familiars_Summons_and_Conjurations L57, L133 | 6 |
| Ch73 | I Try to Find the Truth, But That’s Your Hiding Place | Pranay_Culture L3; 00_Places_Overview L3; Jayapura L3, L4, L4-5, L62; Monster_Cores_and_Training L8-12; Adventuring_Profession L14, L37; Tokens_Stones_and_Relics L58; Book_02_Timeline L92 | 11 |
| Ch74 | The Last Reward | Book_02_Timeline L4, L14, L34; Jayapura L14; Soul_Bound_Items_and_Regalia L34-46; 00_Items_Overview L36, L45-46; 00_Magic_Overview L40-50; Alchemy_Artifice_and_Magical_Materials L40-50, L41, L45, L72, L72-74, L74; Cloud_Constructs_and_Palaces L43 | 15 |
| Ch75 | Impossible Wasn’t Enough | Book_02_Timeline L3-5, L50, L65, L68, L90; Neil_Davone L67; Familiars L75-79, L81-84; Familiars_Summons_and_Conjurations L83; Monsters L89 | 10 |
| Ch76 | Eclipse | Book_02_Timeline L3, L51, L58, L71, L74, L76 …; Callum_Morse L7, L7-46, L40, L41; Glossary L40; Rufus_Remore L71 | 13 |

### Book 3

| Chapter | Title | Cited by (lines) | Rows |
|---|---|---|---|
| Ch1 | A Question You Don’t Yet Know to Ask | Alchemy_Artifice_and_Magical_Materials L5, L100; Book_02_Timeline L14; Book_03_Timeline L14, L18, L46; Era_Selection L14, L105; Callum_Morse L77-82; Beth_Cavendish L86; Glossary L86, L106; Padma_Parsell L87 … | 28 |
| Ch2 | Looking Forward | Book_03_Timeline L17, L64, L105; Gilbert_Bertinelli L59-62, L64; Jason_Asano L59-64 | 6 |
| Ch3 | Adventurers Are People Too | Book_03_Timeline L50; Valdis_Volaire L80 | 2 |
| Ch4 | Valkyrie | Valdis_Volaire L3, L7; Familiars L28-32; Neil_Davone L29-32; Sigrid_Freyn L36, L43; NPC_Rosters_by_Era L43; Glossary L43; Book_03_Timeline L44 | 9 |
| Ch5 | Departures | Emir_Bahadir L9; Tone_and_Voice L9; Valdis_Volaire L42-50; Sigrid_Freyn L49-53, L57-58; Open_Questions L49-53; Book_03_Timeline L50, L70; Familiars_Summons_and_Conjurations L69, L70, L71; Jayapura L83 | 12 |
| Ch6 | No Pot of Gold | Henrietta_Geller L18, L43; Plot_Hooks L18, L43 | 4 |
| Ch7 | The Glory of Success or the Price of Failure | Henrietta_Geller L3; Book_03_Timeline L3, L5, L97; Monsters L5; Thadwick_Mercer L41; Adventure_Society L55; Dimensional_Storage_and_Portals L85; Zato L88-89; Cults_and_Orders L89 … | 13 |
| Ch8 | Adequate | Beth_Cavendish L19; Hester_Maharala L25; Familiars_Summons_and_Conjurations L33; Essences L37-44; Essence_Catalogue L38; Book_03_Timeline L58; Afflictions_Boons_and_Damage L76 | 7 |
| Ch9 | Trash Bonanza | Book_03_Timeline L53 | 1 |
| Ch10 | Strangeness | Rituals_Arrays_and_Formations L5; Monsters L21 | 2 |
| Ch11 | Full Circle | Rituals_Arrays_and_Formations L90 | 1 |
| Ch12 | Regretting it Later | Book_03_Timeline L16, L95 | 2 |
| Ch13 | Swat | Book_03_Timeline L14, L17 | 2 |
| Ch14 | The Purpose of the Adventure Society | Souls_Death_and_Healing L9; Book_03_Timeline L9, L81; Alchemy_Artifice_and_Magical_Materials L18; Familiars_Summons_and_Conjurations L78; Adventuring_Profession L79; Auras L82, L83; Abilities_and_Attributes L98; Ranks_and_Advancement L98 | 10 |
| Ch15 | Elven Storage Solutions | Monsters L17; Abilities_and_Attributes L47; Ranks_and_Advancement L47, L56; Book_03_Timeline L47 | 5 |
| Ch16 | Disbanded | Book_03_Timeline L6, L7; Killian_Laurent L16-43, L70; Magic_Society_and_Associations L80; Economy_and_Money L81; Jory_Tillman L81 | 7 |
| Ch17 | The Man Behind the Mouth | Book_03_Timeline L3, L16; Killian_Laurent L13-26, L14; NPC_Rosters_by_Era L14; Alchemy_Artifice_and_Magical_Materials L26; Cole_Silva L56-60; Magic_Society_and_Associations L60 | 8 |
| Ch18 | Search | Killian_Laurent L130 | 1 |
| Ch19 | Defiance | Book_03_Timeline L3, L92; Rituals_Arrays_and_Formations L37; Killian_Laurent L78 | 4 |
| Ch20 | Hanging Around | Book_03_Timeline L9, L41; Abilities_and_Attributes L17; Roland_Remore L25 | 4 |
| Ch21 | What Doesn’t Kill You | Book_03_Timeline L59, L60, L97, L102; Gary L60; Gods_and_Churches L73; Unusual_and_Unique_Magic L105-111; Ranks_and_Advancement L109, L110; Auras L110, L151-152, L153; Abilities_and_Attributes L121, L136; Jason_Asano L149 | 15 |
| Ch22 | Lingering Doubts | Book_03_Timeline L5, L13 | 2 |
| Ch23 | Scars | Book_03_Timeline L18, L19; Rituals_Arrays_and_Formations L19, L32 | 4 |
| Ch24 | I Won’t Let Them Turn Me Into That | Killian_Laurent L3; Plot_Hooks L3; Hornis L12-17, L17; Danielle_Geller L23; Lucian_Lamprey L23, L48; Auras L30; Callum_Morse L35; Cole_Silva L48 … | 15 |
| Ch25 | Putting the Band Back Together | Killian_Laurent L4; Book_03_Timeline L9, L25; Rituals_Arrays_and_Formations L38 | 4 |
| Ch26 | Nothing Speaks Louder Than Power | Book_03_Timeline L4, L17, L76 | 3 |
| Ch27 | My Name is Jason Asano | Book_03_Timeline L3, L15, L62; Plot_Hooks L62 | 4 |
| Ch28 | While They Watch Me Kill You | Book_03_Timeline L72; Ranks_and_Advancement L78 | 2 |
| Ch29 | Inherently Corrupting | Jason_Asano L22-35; Abilities_and_Attributes L23; Era_Selection L23; Souls_Death_and_Healing L46; Book_03_Timeline L93, L107, L108, L113; Dimensional_Storage_and_Portals L97 | 9 |
| Ch30 | Beholden to No One | Hester_Maharala L21; Book_03_Timeline L28, L36 | 3 |
| Ch31 | Evil Detector | Cults_and_Orders L25-27; Book_03_Timeline L50, L56; Nicolas_Hendren L57 | 4 |
| Ch32 | The World Needs People Like You | Book_03_Timeline L48, L66, L88; Jayapura L65; Ranks_and_Advancement L88 | 5 |
| Ch33 | I’m Very Big on Cowardice | Book_03_Timeline L4, L13, L45; Rufus_Remore L11-12; Dimensional_Storage_and_Portals L62 | 5 |
| Ch34 | More Powerful Than We Anticipated | Book_03_Timeline L3, L16, L28; Timos L10; 01_World_Primer L60; 00_Places_Overview L60 | 6 |
| Ch35 | Fate Can’t Wait to Kill Us All | Book_03_Timeline L4, L71; Badges_and_Guild_Membership L43, L45 | 4 |
| Ch36 | Running Towards Something | Era_Selection L36; Monsters L50; Book_03_Timeline L90 | 3 |
| Ch37 | Greenhouse Flowers | Ranks_and_Advancement L9; 00_Astral_Overview L9; Clive_Standish L13; Book_03_Timeline L32 | 4 |
| Ch38 | A Man Transformed | Abilities_and_Attributes L5; Book_03_Timeline L5, L95, L110; Rituals_Arrays_and_Formations L30 | 5 |
| Ch39 | The Worst Possible Option | Dimensional_Storage_and_Portals L37; Book_03_Timeline L80 | 2 |
| Ch40 | Brave Little Tailor | Monsters L11; Book_03_Timeline L138 | 2 |
| Ch41 | Terms of the Pact | Anisa_Lasalle L51-76, L53; Glossary L66; Book_03_Timeline L84 | 4 |
| Ch42 | Trading Safety Today For Death Tomorrow | Book_03_Timeline L6 | 1 |
| Ch43 | Stalwart | Book_03_Timeline L23 | 1 |
| Ch44 | I’m Sick of Fighting Magic Rocks | Book_03_Timeline L25 | 1 |
| Ch45 | Crossing the Threshold | Book_03_Timeline L16, L72, L79, L90; Jayapura L100 | 5 |
| Ch46 | Anyone Can Be Useful | Book_03_Timeline L26; Thadwick_Mercer L60; Zato L60 | 3 |
| Ch47 | A Series of Familiar Powers | Book_03_Timeline L3 | 1 |
| Ch49 | Sin Eater | Sophie_Wexler L15; Book_03_Timeline L77 | 2 |
| Ch51 | The Boss Comes to Town | Book_03_Timeline L32, L85, L93; Cults_and_Orders L91, L105 | 5 |
| Ch52 | It’s Very Complicated and You All Need to Go Away | Book_03_Timeline L66 | 1 |
| Ch53 | Strong Foundations | Book_03_Timeline L12, L36, L58 | 3 |
| Ch54 | A Valiant Death | Book_03_Timeline L10, L19; Nicolas_Hendren L21; Anisa_Lasalle L23-24 | 4 |
| Ch55 | Ambitions | Book_03_Timeline L71, L95 | 2 |
| Ch56 | Faith and Glory | Book_03_Timeline L14, L18; Nicolas_Hendren L57, L71 | 4 |
| Ch57 | Thadwick | Great_Astral_Beings L4; Book_03_Timeline L13; Jason_Asano L87; Tone_and_Voice L87 | 4 |
| Ch58 | The True Danger | Nicolas_Hendren L3, L47; Book_03_Timeline L3, L4, L15, L16, L19; Anisa_Lasalle L30 | 8 |
| Ch59 | Forsaken Place | Afflictions_Boons_and_Damage L38; Nicolas_Hendren L112; Book_03_Timeline L118, L123, L126 | 5 |
| Ch60 | Being What he Needs to Be | Anisa_Lasalle L5; Nicolas_Hendren L12, L32; Book_03_Timeline L12, L47; Zato L37; Cults_and_Orders L38 | 7 |
| Ch61 | A Significantly More Dangerous Entity | Cults_and_Orders L3; Book_03_Timeline L8; Gods_and_Churches L11; Essences L11; Glossary L23-26 | 5 |
| Ch62 | Losing the Battle to Win the War | Era_Selection L23; Great_Astral_Beings L33; Spoiler_Management L33; Book_03_Timeline L96; Master_Timeline L96 | 5 |
| Ch63 | War of Adaptation | Book_03_Timeline L3 | 1 |
| Ch64 | The Hero of This Story | Book_03_Timeline L123 | 1 |
| Ch65 | Good News, Bad News | Book_03_Timeline L79, L96 | 2 |
| Ch66 | Here We Are | Book_03_Timeline L47 | 1 |
| Ch67 | Outmatched | Cults_and_Orders L6; Thadwick_Mercer L6; Book_03_Timeline L39, L56; Afflictions_Boons_and_Damage L93; Ranks_and_Advancement L95; Unusual_and_Unique_Magic L95 | 7 |
| Ch68 | The Power of Friendship | Celestines L14; Book_03_Timeline L14, L42; Sophie_Wexler L14-15; Zato L59-61; Humphrey_Geller L61 | 6 |
| Ch69 | A War of Stolen Moments | Book_03_Timeline L38, L42, L60, L91, L108, L129 …; Tokens_Stones_and_Relics L108; Hester_Maharala L186; 01_World_Primer L219-222; 00_Astral_Overview L219-222, L223; Velius L233-237, L238, L245, L250-251; NPC_Rosters_by_Era L233-238, L920, L1036; Lorelei_Grantham L455, L759 … | 68 |

### Book 4

| Chapter | Title | Cited by (lines) | Rows |
|---|---|---|---|
| Ch1 | A Better Pants Solution | Book_04_Timeline L34, L38, L63; 00_Places_Overview L39; 00_Earth_Overview L39; Casselton_and_Asano_Village L39; Hiro_Asano L66; Jason_Asano L66-67, L67; NPC_Rosters_by_Era L66-67 | 10 |
| Ch2 | Time to Front Up | Book_04_Timeline L8, L74; 01_World_Primer L11; Essence_Catalogue L18; Monsters L18; Jason_Asano L22; Auras L23-24, L26; Souls_Death_and_Healing L25-26, L26, L50, L60; Unusual_and_Unique_Magic L39-40, L44, L45, L46-49 … | 19 |
| Ch3 | The Single Greatest Thing on This Planet | Souls_Death_and_Healing L34, L36, L38, L40; Book_04_Timeline L80, L108, L112, L126; 00_Earth_Overview L87; Casselton_and_Asano_Village L87; Jason_Asano L100, L112; Book_03_Timeline L112; Master_Timeline L112; Era_Selection L112 … | 24 |
| Ch4 | Some Secrets Change You Forever | Casselton_and_Asano_Village L8; Book_04_Timeline L8, L87, L94; Taika L27; Hiro_Asano L64, L114; Cheryl_Asano L105; NPC_Rosters_by_Era L105 | 9 |
| Ch5 | It Would Be Weirder If Magic Wasn’t Responsible | Earth_Powers L3; Anna_Tilden L5-7, L111-112; Ketevan_Arziani L10; Earth_Magic L13; Ranks_and_Advancement L13-14; 01_World_Primer L13-16; Master_Timeline L113; Astral_Spaces_Zones_and_Surges L127 … | 10 |
| Ch6 | Not the Regular Sort of Dangerous | 00_Earth_Overview L78; Book_04_Timeline L91, L105 | 3 |
| Ch7 | Boogie Man | Greg L42; Book_04_Timeline L42; Craig_Vermillion L49-50; Auras L92 | 4 |
| Ch8 | More Plausible Than the Reality | Ketevan_Arziani L83 | 1 |
| Ch9 | I Suggest You Be Very Polite | Book_04_Timeline L58, L65, L93; Earth_Powers L76; 00_Earth_Overview L76; Master_Timeline L76; Era_Selection L76; Plot_Hooks L76; Craig_Vermillion L105 | 9 |
| Ch10 | A Leather Coat and Tight, Black Pants | Book_04_Timeline L7; Earth_Powers L116, L127; Craig_Vermillion L127 | 4 |
| Ch11 | A Knife in Its Sheath | Earth_Magic L4, L8, L10, L14, L19-22, L21; Earth_Powers L4, L8, L19, L21, L101; Craig_Vermillion L4; Master_Timeline L4; Glossary L4-8; 00_Magic_Overview L9-10; Gods_and_Churches L16; Essences L16 … | 22 |
| Ch12 | Underworld Bargain | Book_04_Timeline L16-17, L51 | 2 |
| Ch13 | Time to Rip Off the Band-Aid | Book_04_Timeline L94-95, L96 | 2 |
| Ch14 | Bullets, Bikes and Blood | Book_04_Timeline L50 | 1 |
| Ch15 | A Good Friend and a Very Bad Enemy | Incursion_Sites L12; Book_04_Timeline L12, L13 | 3 |
| Ch16 | Flavour Text | Book_04_Timeline L4, L14, L61; Earth_Magic L108 | 4 |
| Ch17 | Time For Context | Book_04_Timeline L113, L126 | 2 |
| Ch18 | Brown Trousers Time | Book_04_Timeline L3, L57; Monster_Cores_and_Training L36; Earth_Magic L122 | 4 |
| Ch19 | The Complete Set | Book_04_Timeline L23, L78, L91; 01_World_Primer L36 | 4 |
| Ch20 | More Valuable Than a Life | Book_04_Timeline L26, L55-56, L111 | 3 |
| Ch21 | Uncontrolled Factor | Book_04_Timeline L3, L7; 01_World_Primer L31-33; Earth_Magic L33; Ranks_and_Advancement L33; Essence_Catalogue L135; Monsters L136 | 7 |
| Ch22 | Agendas | Book_04_Timeline L83-85 | 1 |
| Ch23 | Hegemons | 01_World_Primer L26; Earth_Magic L26; Book_04_Timeline L27; Craig_Vermillion L31-39; Dawn L31-39 | 5 |
| Ch24 | Guilty Conscience | Book_04_Timeline L32, L66; Cheryl_Asano L42 | 3 |
| Ch25 | Uncommon Mistake | Book_04_Timeline L10; Alchemy_Artifice_and_Magical_Materials L20; Rituals_Arrays_and_Formations L20; Kaito_Asano L44-45; Emi_Evans_Asano L60, L60-66; Open_Questions L60 | 7 |
| Ch26 | It’s Complicated | Book_04_Timeline L29, L59; Amy_Asano L47 | 3 |
| Ch27 | A Big Dose of Normal | Book_04_Timeline L3, L97, L167; Emi_Evans_Asano L171 | 4 |
| Ch28 | Moppet | Anna_Tilden L48; Emi_Evans_Asano L126, L135-139, L154; Book_04_Timeline L126, L139 | 6 |
| Ch29 | Always Tell the Truth if You Can Get Away With It | Emi_Evans_Asano L43, L45-54, L69-73, L103; Book_04_Timeline L45, L103 | 6 |
| Ch30 | Discretion is a Good Idea | Book_04_Timeline L5, L38; Spirit_Vault_and_Astral_Kingdom L45, L49 | 4 |
| Ch31 | The Cold Eyes of a Stranger | Emi_Evans_Asano L25; Book_04_Timeline L25, L48; 01_World_Primer L48; Earth_Magic L48; Ranks_and_Advancement L48; Minor_Cast_Books_4-6 L48; Name_Index L77 | 8 |
| Ch32 | Looking Down the Point of a Sword | Emi_Evans_Asano L4, L19; Book_04_Timeline L36 | 3 |
| Ch33 | What Your Uncle Has Been Telling You | Book_04_Timeline L43, L76-77, L77, L102 | 4 |
| Ch34 | The Moments That Decide Who You Are | Emi_Evans_Asano L14; Book_04_Timeline L42 | 2 |
| Ch35 | I’m Mysterious Now | Book_04_Timeline L8; Confluences L123 | 2 |
| Ch36 | Hardline Position | Book_04_Timeline L34, L153; Anna_Tilden L35; NPC_Rosters_by_Era L37; Asya_Karadeniz L37-41; Earth_Magic L77; Monster_Cores_and_Training L77; Minor_Cast_Books_4-6 L139-145 | 8 |
| Ch37 | Otherwise Best Avoided | Souls_Death_and_Healing L14; Astral_Spaces_Zones_and_Surges L63, L79; 00_Earth_Overview L70; Incursion_Sites L70; Earth_Magic L79; Book_04_Timeline L103 | 7 |
| Ch38 | Terms | Book_04_Timeline L45 | 1 |
| Ch39 | Section | Incursion_Sites L28; Astral_Spaces_Zones_and_Surges L55; Earth_Magic L55 | 3 |
| Ch40 | Core Users | Astral_Spaces_Zones_and_Surges L33; Abilities_and_Attributes L72; Unusual_and_Unique_Magic L72 | 3 |
| Ch41 | What You Call Observing | Confluences L6; Essence_Catalogue L6; Incursion_Sites L18, L32; Book_04_Timeline L19, L55; Farrah_Hurin L31; Nigel_Thornton L89-97; NPC_Rosters_by_Era L91; Earth_Powers L91-97 | 10 |
| Ch42 | Not the Monster | Book_04_Timeline L3, L26, L66; Minor_Cast_Books_4-6 L27; Glossary L27; Abilities_and_Attributes L44; Confluences L44 | 7 |
| Ch43 | Letting Him Run Rampant | Book_04_Timeline L3; Essences L10; Earth_Magic L33; Saint-Etienne L58; Adrien_Barbou L58; NPC_Rosters_by_Era L58 | 6 |
| Ch44 | Old Testament Power | Book_04_Timeline L133, L143 | 2 |
| Ch45 | My Turn | Book_04_Timeline L17, L94; Cheryl_Asano L76 | 3 |
| Ch46 | Visually Distinctive Henchman | Book_04_Timeline L46, L100; Ketevan_Arziani L82; NPC_Rosters_by_Era L82; Earth_Magic L90 | 5 |
| Ch47 | Of Course It Was Him | Book_04_Timeline L12, L50; Ketevan_Arziani L28 | 3 |
| Ch48 | The Price of Transgression | Book_04_Timeline L16, L21 | 2 |
| Ch49 | The Time For Bold, Decisive Men | Book_04_Timeline L3, L5, L51, L93, L99 | 5 |
| Ch50 | Technical Issue | Book_04_Timeline L9, L84; Emi_Evans_Asano L53-62 | 3 |
| Ch51 | The Long Game | Minor_Cast_Books_4-6 L10; Book_04_Timeline L10, L30, L45, L72; Glossary L10; Saint-Etienne L28, L28-30, L60-68; Master_Timeline L30, L37; Earth_Powers L30-37; Plot_Hooks L30-37; Earth_Magic L35 … | 17 |
| Ch52 | A Moment For Drastic Measures | Saint-Etienne L22-23; Book_04_Timeline L37; Minor_Cast_Books_4-6 L84; Adrien_Barbou L94 | 4 |
| Ch53 | Foiled Plans | Book_04_Timeline L3, L4, L20, L55; Minor_Cast_Books_4-6 L75 | 5 |
| Ch54 | Quite the Year | Book_04_Timeline L39; Glossary L88 | 2 |
| Ch55 | Full Houseboat | Book_04_Timeline L5, L8, L93 | 3 |
| Ch56 | A Wizard Did It | Book_04_Timeline L22, L35; Emi_Evans_Asano L46 | 3 |
| Ch57 | The King of Everyone | Spirit_Vault_and_Astral_Kingdom L3-10, L59; Emi_Evans_Asano L33-39, L34-36; Book_04_Timeline L100 | 5 |
| Ch58 | I Came Back to Show You Wonders | Emi_Evans_Asano L75; Book_04_Timeline L95, L126 | 3 |
| Ch59 | Mercy | Book_04_Timeline L11, L48; Ketevan_Arziani L13; Anna_Tilden L35 | 4 |
| Ch60 | Ideal Circumstances | Incursion_Sites L18, L59-65; Book_04_Timeline L18 | 3 |
| Ch61 | The Blood and Death Guy | Book_04_Timeline L92 | 1 |
| Ch62 | A Lot of Anomalies | Incursion_Sites L23; Book_04_Timeline L83 | 2 |
| Ch63 | Pitch Meetings | Book_04_Timeline L8, L25; NPC_Rosters_by_Era L25; Li_Li_Mei L25-28 | 4 |
| Ch64 | Moving Forward | Confluences L57, L70; Essence_Catalogue L70; Book_04_Timeline L80, L82 | 5 |
| Ch65 | Flemish Baroque | Confluences L22, L28, L29; Glossary L22, L28; Essence_Catalogue L22-27, L27, L28; Book_04_Timeline L84 | 9 |
| Ch66 | Not Ready to Leave | Book_04_Timeline L82 | 1 |
| Ch67 | Decision | Book_04_Timeline L27 | 1 |
| Ch68 | What You Have to Do | Book_04_Timeline L59, L139, L170; Earth_Magic L59-61, L63-65; 01_World_Primer L79, L97, L131-135 | 8 |
| Ch69 | The Direction We Want Them to Go | Confluences L102, L106; Essence_Catalogue L102, L106; Book_04_Timeline L106 | 5 |
| Ch70 | The Dangers of What I Do | Book_04_Timeline L7, L24 | 2 |
| Ch71 | We Were All Monsters | Confluences L4-5, L30, L36; Book_04_Timeline L6, L36, L72; Essence_Catalogue L30, L36 | 8 |
| Ch72 | Options | Essence_Catalogue L22-23; Auras L38; Confluences L76, L83; Book_04_Timeline L85 | 5 |
| Ch73 | I Need Time | Book_04_Timeline L39; Emi_Evans_Asano L77; Auras L92, L93, L95-100; Ranks_and_Advancement L92 | 6 |
| Ch74 | Walkabout | Auras L6, L10, L12-13, L14; Ranks_and_Advancement L8; Book_04_Timeline L12, L32, L65; Emi_Evans_Asano L32, L145; Yumi_Asano L43 | 11 |

### Book 5

| Chapter | Title | Cited by (lines) | Rows |
|---|---|---|---|
| Ch1 | Too Valuable to Lose | Book_05_Timeline L21, L38; 01_World_Primer L38; Alchemy_Artifice_and_Magical_Materials L49; Monster_Cores_and_Training L51-52, L53; Skill_Books_and_Learning L51-52; Earth_Magic L51-53 | 8 |
| Ch2 | All I Can Do is My Best | Chloe_Baudrillard L9, L85; Vincent_Baudrillard L9; Book_05_Timeline L9, L108, L126; Emi_Evans_Asano L116 | 7 |
| Ch3 | A Modern Myth | Book_05_Timeline L5, L57, L170, L212; Earth_Powers L8-12; Plot_Hooks L8-19; Confluences L77; Essence_Catalogue L77; Ian_Evans L126, L130; Emi_Evans_Asano L127; Chloe_Baudrillard L130, L146 … | 17 |
| Ch5 | Grand Tour | Book_05_Timeline L7, L59, L66, L104; 00_Magic_Overview L11; Earth_Magic L11; Rituals_Arrays_and_Formations L11; Emi_Evans_Asano L59-68; Ranks_and_Advancement L82; Casselton_and_Asano_Village L83-89, L106-113; Farrah_Hurin L83-89 … | 13 |
| Ch6 | New Groove | Book_05_Timeline L48, L69 | 2 |
| Ch7 | Get to the Chopper | Essence_Catalogue L8, L14, L16; Asya_Karadeniz L12, L21-23; Greg L12; NPC_Rosters_by_Era L12; Confluences L14, L16, L64-66; Book_05_Timeline L16; Adrien_Barbou L96 | 12 |
| Ch8 | What’s Left of Your Principles | Book_04_Timeline L5; Book_05_Timeline L5, L35, L44, L54; Mr_North L14-15; Earth_Powers L14-18, L28, L39; NPC_Rosters_by_Era L14-18; Open_Questions L28, L39; Adrien_Barbou L35; Glossary L35 … | 16 |
| Ch9 | Contingencies | Book_05_Timeline L5, L23, L40, L80; Emi_Evans_Asano L23; Anna_Tilden L52; Ketevan_Arziani L67 | 7 |
| Ch10 | Humanity | Book_05_Timeline L6, L52; NPC_Rosters_by_Era L17; Audrey_Blaine L17-33, L24 | 5 |
| Ch11 | Media Blitz | Book_05_Timeline L12; Amy_Asano L82 | 2 |
| Ch12 | Grandmotherly Advice | Akari_Asano L18-24, L27; Book_05_Timeline L100 | 3 |
| Ch13 | A Bloke With Vast Cosmic Power | Book_05_Timeline L35, L41, L73; Master_Timeline L37; Greg L74; Asya_Karadeniz L74-75 | 6 |
| Ch14 | A Very Long To-Do List | Earth_Magic L3; Book_05_Timeline L8, L77; Kaito_Asano L37; Greg L42; Confluences L61; Essence_Catalogue L61; Akari_Asano L61-66; NPC_Rosters_by_Era L61-66 | 9 |
| Ch15 | Another Step Forward | Book_05_Timeline L50 | 1 |
| Ch16 | Tactical Flexibility | Earth_Magic L78; Book_05_Timeline L78; Familiars L103-108 | 3 |
| Ch17 | Broken | Incursion_Sites L3; Earth_Magic L7; Earth_Powers L7; 00_Earth_Overview L7; Era_Selection L7; Spoiler_Management L7; Book_05_Timeline L11, L28 | 8 |
| Ch18 | Never Enough | Book_05_Timeline L22, L41, L78; Incursion_Sites L82, L83 | 5 |
| Ch19 | Media Landscape | Minor_Cast_Books_10-13 L10; Glossary L10; Book_05_Timeline L26, L99; Open_Questions L76 | 5 |
| Ch20 | Instability | Dawn L21, L21-24, L22, L40-41, L65-67; NPC_Rosters_by_Era L21-24; Book_05_Timeline L24, L25-26, L26, L41, L117; Master_Timeline L24, L24-26; Tone_and_Voice L24, L25; Jason_Asano L24-26, L25 | 17 |
| Ch21 | Supernatural | Book_05_Timeline L32 | 1 |
| Ch22 | Arms Race | Book_05_Timeline L46, L48 | 2 |
| Ch23 | Sword-Fighting With No Shirt On | Book_05_Timeline L37, L94 | 2 |
| Ch24 | Candid and Authentic | Tone_and_Voice L3-5; Emi_Evans_Asano L4, L9, L12-16; Book_05_Timeline L4, L61; Dimensional_Storage_and_Portals L135; Akari_Asano L140 | 8 |
| Ch25 | Warmth and Levity | Monster_Cores_and_Training L5, L6, L6-8, L10; Ranks_and_Advancement L15; Book_05_Timeline L23, L94; Abilities_and_Attributes L23-25, L26, L27; 01_World_Primer L26-27; Incursion_Sites L82 | 12 |
| Ch26 | An Intelligent King | Book_05_Timeline L9, L17; Incursion_Sites L17 | 3 |
| Ch27 | Hunted | Book_05_Timeline L3 | 1 |
| Ch28 | Gamble | Incursion_Sites L86; Book_05_Timeline L86 | 2 |
| Ch29 | Dying of Thirst in the Desert | Book_05_Timeline L19, L65, L68; Jason_Asano L68-72; Soul_Bound_Items_and_Regalia L77-80 | 5 |
| Ch30 | Enough Power | Earth_Powers L43; Open_Questions L43; Book_05_Timeline L57; Gilbert_Bertinelli L58; Farrah_Hurin L61; Incursion_Sites L71 | 6 |
| Ch31 | Silver | Era_Selection L1; Book_05_Timeline L6, L34, L121, L135, L164; Emi_Evans_Asano L134-135; Confluences L147; Essence_Catalogue L147; Ranks_and_Advancement L147; Incursion_Sites L170; Afflictions_Boons_and_Damage L176, L176-181, L179, L181 … | 17 |
| Ch32 | Old Affairs | Earth_Powers L5; Open_Questions L5; Incursion_Sites L11; Book_05_Timeline L23; Essence_Catalogue L29-30 | 5 |
| Ch33 | End Run | Book_05_Timeline L3, L104 | 2 |
| Ch34 | Giving Face | Emi_Evans_Asano L3; Book_05_Timeline L66 | 2 |
| Ch35 | Not In a Position to Criticise | Book_05_Timeline L21 | 1 |
| Ch36 | Honour | Noriko_Asano L3, L11-16, L32, L89; Book_05_Timeline L3, L33; NPC_Rosters_by_Era L3; Ketevan_Arziani L33; Rituals_Arrays_and_Formations L84 | 9 |
| Ch37 | They Get to See What I’m Like | Book_05_Timeline L28, L51; Noriko_Asano L92 | 3 |
| Ch38 | Fanboy | Itsuki_Tiwari L5, L50; Book_05_Timeline L41; Confluences L50; Essence_Catalogue L50 | 5 |
| Ch39 | A Very Bad Mistake | Book_05_Timeline L15, L88 | 2 |
| Ch40 | An Unexpected Direction | Emi_Evans_Asano L3-18; Book_05_Timeline L18, L79; 00_Cosmology_Overview L49-50; Earth_Powers L79, L79-83; Mr_North L79-83; Adrien_Barbou L86 | 8 |
| Ch41 | Parade of Delights | The_Builders_Door_and_Fundament_Gate L24-26, L28, L52-62, L62-64; Tone_and_Voice L33 | 5 |
| Ch42 | Collateral Damage | Book_05_Timeline L59 | 1 |
| Ch43 | I Intend to Do Damage | Book_05_Timeline L3, L71, L75; Emi_Evans_Asano L85-90 | 4 |
| Ch44 | A Chance to Control the Narrative | Amy_Asano L3; NPC_Rosters_by_Era L3; Spirit_Vault_and_Astral_Kingdom L44-45; Asya_Karadeniz L45; Ian_Evans L45; Book_05_Timeline L46, L56; 00_Magic_Overview L48; Astral_Spaces_Zones_and_Surges L48, L48-52, L51, L52 … | 21 |
| Ch45 | You Shouldn’t Lie to Your Wife | Book_05_Timeline L3, L38; Consumables_and_Trial_Rewards L9-11; Plot_Hooks L9-11 | 4 |
| Ch46 | The Decision Has Been Made | Book_05_Timeline L63, L91; Minor_Cast_Books_4-6 L86 | 3 |
| Ch47 | First Priority | Book_05_Timeline L9; Minor_Cast_Books_4-6 L102 | 2 |
| Ch48 | Node Space | Book_05_Timeline L43, L90, L103 | 3 |
| Ch49 | Loaded For Battle | Book_05_Timeline L45 | 1 |
| Ch50 | Going For Gold | Book_05_Timeline L30, L84 | 2 |
| Ch51 | Prepare For The Rematch | Minor_Cast_Books_4-6 L8; Book_05_Timeline L28, L127; Emi_Evans_Asano L33; Asya_Karadeniz L40, L52; Greg L40; NPC_Rosters_by_Era L40, L48, L52 | 10 |
| Ch52 | Finish the Job | Book_05_Timeline L3, L68; Master_Timeline L3; Kaito_Asano L20; Noriko_Asano L68 | 5 |
| Ch53 | Inevitability | Book_05_Timeline L13, L67, L80; Kaito_Asano L67; Emi_Evans_Asano L79, L80, L80-85, L82, L86 | 9 |
| Ch54 | The Edge of Madness | Emi_Evans_Asano L8, L13; Rituals_Arrays_and_Formations L11; Book_05_Timeline L45, L50; 00_Peoples_Overview L52; Goblins_and_Fairies L52, L55 | 8 |
| Ch55 | Trying to Be Merciful | Book_05_Timeline L3 | 1 |
| Ch56 | Appreciation | Erika_Asano L7; Book_05_Timeline L24, L69; Asya_Karadeniz L24-26; Greg L26 | 5 |
| Ch57 | Brooding Loner | Astral_Spaces_Zones_and_Surges L11; Book_05_Timeline L16, L44 | 3 |
| Ch58 | High Maintenance | Greg L14; Book_05_Timeline L20, L105 | 3 |
| Ch59 | Treachery or Cowardice | Book_05_Timeline L30 | 1 |
| Ch60 | Comely Wenches | Book_05_Timeline L63 | 1 |
| Ch61 | A Lot Like a Guess | Book_05_Timeline L27 | 1 |
| Ch62 | It’s Okay to Laugh | Book_05_Timeline L55 | 1 |
| Ch63 | Dignified Moment | Book_05_Timeline L3 | 1 |
| Ch64 | When Someone is Under Your Gun | Valdis_Volaire L24; Book_05_Timeline L31 | 2 |
| Ch65 | When, Not If | Book_05_Timeline L31, L56, L66 | 3 |
| Ch66 | Not Entirely Ethical | Book_05_Timeline L5, L17, L48 | 3 |
| Ch67 | Ahead of Schedule | Book_05_Timeline L4, L31, L75 | 3 |
| Ch68 | Open Wound | Book_05_Timeline L3, L30, L68; Glossary L30; Transformation_Zones L34-38; Astral_Spaces_Zones_and_Surges L68; Earth_Magic L68; Nitra L68, L69; Book_06_Timeline L68 | 10 |

### Book 6

| Chapter | Title | Cited by (lines) | Rows |
|---|---|---|---|
| Ch1 | Looting a House as it Burns Down Around You | Book_06_Timeline L3, L4, L32, L72, L85; Anna_Tilden L4, L27; NPC_Rosters_by_Era L4; Glossary L16-21; 00_Cosmology_Overview L20; Consumables_and_Trial_Rewards L20; Earth_Powers L22-30; Transformation_Zones L83 | 13 |
| Ch2 | Domain | Monsters L10, L31; Book_06_Timeline L12, L34; Astral_Spaces_Zones_and_Surges L15; Spirit_Vault_and_Astral_Kingdom L15; Transformation_Zones L15 | 7 |
| Ch3 | Needs of the Moment | Transformation_Zones L5, L39; Book_06_Timeline L39, L67 | 4 |
| Ch4 | A Beautiful Woman and a Sack of Cash | Soul_Bound_Items_and_Regalia L6-8, L29-39, L34-37, L35-38, L40, L42-50 …; Glossary L6-8, L26-38; Jason_Asano L29-36; Book_06_Timeline L30, L40, L68; 00_Items_Overview L33; Cloud_Constructs_and_Palaces L42-50, L53; Emi_Evans_Asano L65 | 20 |
| Ch5 | You Have to Be True to Yourself | Astral_Spaces_Zones_and_Surges L32, L48; Spirit_Vault_and_Astral_Kingdom L41, L53; Nitra L41; Book_06_Timeline L41, L72; Li_Li_Mei L59 | 8 |
| Ch6 | One More Secret | Book_06_Timeline L7; Li_Li_Mei L16-21; Gerling L31; Minor_Cast_Books_4-6 L31; Glossary L31 | 5 |
| Ch7 | Instinct is All We Have | Book_06_Timeline L22; Minor_Cast_Books_4-6 L22-23, L72; Gerling L80 | 4 |
| Ch8 | Step Back | Book_06_Timeline L3; Monsters L73 | 2 |
| Ch9 | Guns & Money | Book_06_Timeline L7, L43 | 2 |
| Ch10 | Old Habit | Cloud_Constructs_and_Palaces L34; 01_World_Primer L41; Daily_Life L41 | 3 |
| Ch11 | It’s Still Not About Killing Monsters | Book_06_Timeline L14; Monsters L43 | 2 |
| Ch12 | Open to the Unanticipated | Book_06_Timeline L7, L59; Nitra L41, L59 | 4 |
| Ch13 | I’m Going to Bet on Myself | Book_06_Timeline L3, L77; Essence_Catalogue L68, L69; Confluences L69; Spirit_Vault_and_Astral_Kingdom L79 | 6 |
| Ch14 | No Perfect Options | Auras L6; Ranks_and_Advancement L6; Book_06_Timeline L31, L74; Unusual_and_Unique_Magic L78, L79, L80, L82; Confluences L79; Essence_Catalogue L79; Danielle_Geller L80-82; 00_Cosmology_Overview L82 | 12 |
| Ch15 | Stillness | Monsters L4; Nitra L45; Jason_Asano L45 | 3 |
| Ch16 | Whatever We Face | Essence_Catalogue L35; Nitra L60; Book_06_Timeline L60, L83 | 4 |
| Ch17 | You Really Aren’t Local | Book_06_Timeline L13, L37, L71; Shako L41, L43 | 5 |
| Ch18 | A Sliver of Hope | Dawn L3-9; Book_06_Timeline L6, L39, L138; The_Builders_Door_and_Fundament_Gate L11, L30-36, L39, L124; Shako L79, L79-84; Great_Astral_Beings L79-80, L124; 00_Cosmology_Overview L124 | 13 |
| Ch19 | End-User Licence Agreement | Spirit_Vault_and_Astral_Kingdom L21, L62; Book_06_Timeline L21, L65; Minor_Cast_Books_4-6 L27 | 5 |
| Ch20 | Negotiations | Book_06_Timeline L38, L81 | 2 |
| Ch21 | Another Day for Vampires | Book_06_Timeline L4, L31, L63, L76 | 4 |
| Ch22 | Less Freud and More God of Healing | Book_06_Timeline L5, L52 | 2 |
| Ch23 | Little Cost in Exploring | Book_06_Timeline L3, L31; Era_Selection L3; Plot_Hooks L3; Anna_Tilden L15; Emi_Evans_Asano L31; Spirit_Vault_and_Astral_Kingdom L48, L56; 00_Peoples_Overview L91; Goblins_and_Fairies L91 | 10 |
| Ch24 | Intentions | Anna_Tilden L3, L4, L5; Book_06_Timeline L6; Gods_and_Churches L86 | 5 |
| Ch25 | I Need That Song to Play Out | Book_06_Timeline L79, L102; Earth_Powers L98-99 | 3 |
| Ch26 | Wash Them First | Farrah_Hurin L9; Tone_and_Voice L9; Adrien_Barbou L9-20; Book_06_Timeline L63, L71; Confluences L94; Essence_Catalogue L94; Essences L97 | 8 |
| Ch27 | The Language of Passion | Book_06_Timeline L51 | 1 |
| Ch28 | Forthright Honesty | Book_06_Timeline L36; NPC_Rosters_by_Era L36; Travis_Noble L36-37 | 3 |
| Ch29 | Pertinent Factor | Glossary L32; Book_06_Timeline L84 | 2 |
| Ch30 | More of a Focus on Nipples | Book_06_Timeline L29; Adrien_Barbou L40-43; Open_Questions L43 | 3 |
| Ch31 | The Job That’s in Front of You | Travis_Noble L4; Book_06_Timeline L4, L62; Era_Selection L4; Plot_Hooks L4 | 5 |
| Ch32 | Going Suspiciously Well | Book_06_Timeline L42, L51, L72 | 3 |
| Ch33 | One of Asano’s Secrets | Book_06_Timeline L6; Gerling L28 | 2 |
| Ch34 | Swarm Against Swarm | Book_06_Timeline L6, L51 | 2 |
| Ch35 | Necessary Evil | Book_06_Timeline L15, L112; Open_Questions L68, L78-80; Glossary L73; Saint-Etienne L80 | 6 |
| Ch36 | Balls | Book_06_Timeline L73 | 1 |
| Ch37 | Which One of Us is the Villain | Book_06_Timeline L93 | 1 |
| Ch38 | That Passion Didn’t Come From Nowhere | Book_06_Timeline L21; Minor_Cast_Books_4-6 L76-81 | 2 |
| Ch39 | The Upstart Magician | Book_06_Timeline L12; Incursion_Sites L25; Saint-Etienne L25; Monster_Cores_and_Training L25-27, L27; Minor_Cast_Books_4-6 L25-27; Earth_Powers L71-74 | 7 |
| Ch40 | Too Much Over Pride | Book_06_Timeline L18 | 1 |
| Ch41 | Trust All the Way | Book_06_Timeline L8, L39, L111 | 3 |
| Ch42 | Time to Choose | Adrien_Barbou L22; Gerling L66; Book_06_Timeline L101 | 3 |
| Ch43 | Four-Score Men | Book_06_Timeline L18, L48; Ranks_and_Advancement L52; Saint-Etienne L71; Adrien_Barbou L75 | 5 |
| Ch44 | The Very Opposite of Fantastical | Book_06_Timeline L4; Saint-Etienne L25-31; Open_Questions L25-31 | 3 |
| Ch45 | Small Mercies | Saint-Etienne L3; Book_06_Timeline L34; Elizabeth L39-40 | 3 |
| Ch46 | Salus Mundi Suprema Lex Esto | Saint-Etienne L31; Book_06_Timeline L31, L53, L81, L104 | 5 |
| Ch47 | Something Other Than Human | 01_World_Primer L3, L390, L623, L703; Book_06_Timeline L3, L4, L5, L14, L16, L93 …; Master_Timeline L4, L155; Anna_Tilden L16-18; Earth_Powers L27; Adrien_Barbou L46; Hiro_Asano L53; Yumi_Asano L58 … | 118 |

### Book 7

| Chapter | Title | Cited by (lines) | Rows |
|---|---|---|---|
| Ch1 | Of Course He Doesn’t Have Pants | Book_07_Timeline L5, L30, L56; Era_Selection L5, L16, L56; Farrah_Hurin L16; Spirit_Vault_and_Astral_Kingdom L18; Zartos L30; 01_World_Primer L56; 00_Magic_Overview L56; Astral_Spaces_Zones_and_Surges L56 … | 13 |
| Ch2 | Connotations | Book_07_Timeline L13, L76; Zartos L71, L71-72, L71-75, L75; Gary L71-74; Jason_Asano L73-74; Soul_Bound_Items_and_Regalia L73-74; Celestines L75; 00_Places_Overview L75 | 11 |
| Ch3 | What a Monster Surge Feels Like | Book_07_Timeline L29, L42, L51; Rimaros L44-47; Storm_Kingdom_Culture L47, L82 | 6 |
| Ch4 | Strategic Doctrine | Book_07_Timeline L6 | 1 |
| Ch5 | I’ve Seen Your Best | Book_07_Timeline L13, L56; Adventuring_Profession L25; Storm_Kingdom_Culture L65, L67, L69; Era_Selection L65; Rimaros L67; Zara_Rimaros L68-69 | 9 |
| Ch6 | Responsible Dad | Belinda_Callahan L42; Tone_and_Voice L42; Book_07_Timeline L88 | 3 |
| Ch7 | Surge Protocols | 01_World_Primer L3, L70; Farrah_Hurin L53; Guilds_and_Houses L53-54; Book_07_Timeline L58, L64; Storm_Kingdom_Culture L70, L72, L78; Rimaros L70, L70-72, L78; Palisaros L70 | 13 |
| Ch8 | Disappointed or Relieved | Dawn L3; Book_07_Timeline L36, L82 | 3 |
| Ch9 | More Paperwork | Religion_in_Practice L4, L9; Rufus_Remore L6, L18; Book_07_Timeline L7, L25, L88; NPC_Rosters_by_Era L7; Gabrielle_Pellin L7-8; Tone_and_Voice L18; Gods_and_Churches L99; Minor_Cast_Books_7-9 L113 | 12 |
| Ch10 | Multi-Talented | Rimaros L5; Monsters L19; Ranks_and_Advancement L19; Alchemy_Artifice_and_Magical_Materials L38; Book_07_Timeline L52; Adventure_Society L124-129 | 6 |
| Ch11 | Don’t Say You Weren’t Warned | Book_07_Timeline L5; Awakening_Stones L75 | 2 |
| Ch12 | Contribution | Adventure_Society L14-15, L23; Adventuring_Profession L15, L23; Economy_and_Money L15-21; Tone_and_Voice L22-23; Book_07_Timeline L23, L57, L69; Plot_Hooks L23; Miles_Cotezee L69; NPC_Rosters_by_Era L69 | 12 |
| Ch13 | Small-Town Lifestyle | NPC_Rosters_by_Era L18, L51; Argy L18-20, L20, L24, L28; Palisaros L20-35, L33, L34, L35; Pelli L28, L28-30, L51; Rimaros L28-30; Book_07_Timeline L75 | 15 |
| Ch14 | I Don’t Need to Invent Ice Cream | Book_07_Timeline L9, L44; Glossary L41; Jayapura L52 | 4 |
| Ch15 | Remaining Unremarkable | Book_07_Timeline L40, L77; Zara_Rimaros L74, L110-113, L114-115 | 5 |
| Ch16 | A Damn Fine Way to Start Off a War | Miles_Cotezee L3, L75; Book_07_Timeline L3, L51, L75; Dimensional_Storage_and_Portals L73 | 6 |
| Ch17 | It Will Not Be Fine | Liara_Rimaros L3; Book_07_Timeline L3, L104, L111; Baseph_and_the_Rimaros_Children L20; Minor_Cast_Books_7-9 L20, L116; Gods_and_Churches L104; Religion_in_Practice L104; Jason_Asano L104, L104-105; Shako L104 … | 14 |
| Ch18 | A Story of War | Book_07_Timeline L25, L42, L48; Soramir L41-42; Storm_Kingdom_Culture L42; NPC_Rosters_by_Era L42, L66-72; Pelli L43; Guilds_and_Houses L66-72, L70; Zara_Rimaros L66-72; Plot_Hooks L66-72 … | 15 |
| Ch19 | Any Help They Can Get | Book_07_Timeline L21, L71 | 2 |
| Ch20 | Little Man Problems | Minor_Cast_Books_7-9 L21; Adventuring_Profession L23; Dimensional_Storage_and_Portals L23; Book_07_Timeline L47; Gods_and_Churches L54 | 5 |
| Ch21 | Enemies Even I Would Fear | Storm_Kingdom_Culture L11; Guilds_and_Houses L11; Rimaros L12; NPC_Rosters_by_Era L13; Trenchant_Moore L13-14, L15-18, L21-25; Zara_Rimaros L32; Book_07_Timeline L32 | 9 |
| Ch22 | True Elites | Book_07_Timeline L92; Trenchant_Moore L93 | 2 |
| Ch23 | Diligent and Considerate | Book_07_Timeline L9 | 1 |
| Ch24 | That Doesn’t Make the Pebble Important | Vitesse L3; Book_07_Timeline L37 | 2 |
| Ch25 | They Don’t Send Their Best People | Open_Questions L3; Miles_Cotezee L4; Book_07_Timeline L4, L78; 00_Places_Overview L77; Arcazitlan L77, L77-78, L78 | 8 |
| Ch26 | An Old Friend That He Had No Time For | Book_07_Timeline L7; Arcazitlan L48 | 2 |
| Ch27 | Never Underestimate Adventurers | Book_07_Timeline L21 | 1 |
| Ch28 | Better Strange Than Scary | Arcazitlan L3; Book_07_Timeline L7, L107; Alchemy_Artifice_and_Magical_Materials L106 | 4 |
| Ch29 | Going Overland | Book_07_Timeline L7; Arcazitlan L8 | 2 |
| Ch30 | Small | Book_07_Timeline L28, L36 | 2 |
| Ch31 | Uneasy Allies | Book_07_Timeline L9; Afflictions_Boons_and_Damage L10; Confluences L12; Arcazitlan L42 | 4 |
| Ch32 | Supply Chain Problems | Book_07_Timeline L7 | 1 |
| Ch33 | The Hitting-It-a-Bunch Plan | Book_07_Timeline L17, L112 | 2 |
| Ch34 | I Liked the Fighting Better | Book_07_Timeline L77 | 1 |
| Ch35 | That Usually is My Day | Book_07_Timeline L8; Gods_and_Churches L39; Trenchant_Moore L72 | 3 |
| Ch36 | Unyielding Faith | Book_07_Timeline L47; Miles_Cotezee L65; Outworlders L86; Master_Timeline L86; Era_Selection L86; Plot_Hooks L86 | 6 |
| Ch37 | Something He Could Never Get Back | Book_07_Timeline L3, L57, L59; Monster_Cores_and_Training L4; Rimaros L64 | 5 |
| Ch38 | Dignified Young Adventurer | Astral_Spaces_Zones_and_Surges L6; Adventuring_Profession L7; Book_07_Timeline L92, L98 | 4 |
| Ch39 | I Can Do Sleazy | Book_07_Timeline L79 | 1 |
| Ch40 | An Object Lesson in Foolish Risks | Rimaros L4; Book_07_Timeline L7, L9; Alchemy_Artifice_and_Magical_Materials L54 | 4 |
| Ch41 | Murky Waters | Kasper_Irios L3, L11-12, L26, L40-41; Book_07_Timeline L3, L73; NPC_Rosters_by_Era L3; Palisaros L61 | 8 |
| Ch42 | Integrity is Forever | Book_07_Timeline L29, L92; Minor_Cast_Books_7-9 L61 | 3 |
| Ch43 | How Deep a Hole | Vitesse L18, L58; Rimaros L47; Minor_Cast_Books_7-9 L47; Estercost_Culture L58; Cyrion L58; Glossary L58; Open_Questions L58; Danielle_Geller L61, L61-62 … | 12 |
| Ch44 | The Part That Knows How to Quit | Adventuring_Profession L7; Book_07_Timeline L23, L30; Amos_Pensinata L30; Travis_Noble L61-62 | 5 |
| Ch45 | Bad Apples | NPC_Rosters_by_Era L54; Book_07_Timeline L61 | 2 |
| Ch46 | Idiot Plan | Book_07_Timeline L19, L40; Trenchant_Moore L81 | 3 |
| Ch47 | The Days They Sing Songs About | Jeni_Kavaloa L33, L41-49, L60; Book_07_Timeline L33, L39; NPC_Rosters_by_Era L33, L39, L54; Amos_Pensinata L39; Orin_Pensinata L39, L51-53, L72; Glossary L39; Korinne_Pescos L54, L59; Dimensional_Storage_and_Portals L62 | 16 |
| Ch48 | The Source of the Madness | Orin_Pensinata L7; Korinne_Pescos L16; Book_07_Timeline L33, L45, L58; Saint-Etienne L36 | 6 |
| Ch49 | A Fair Fight | Book_07_Timeline L21; Jeni_Kavaloa L39 | 2 |
| Ch50 | Put the Mask Back On | The_Builders_Door_and_Fundament_Gate L8; Book_07_Timeline L15, L55; Korinne_Pescos L51 | 4 |
| Ch51 | I Don’t Think You’re Angry | Jeni_Kavaloa L5; Book_07_Timeline L5, L90 | 3 |
| Ch52 | Staying with Friends | Minor_Cast_Books_7-9 L50; Book_07_Timeline L51, L66; Leonids L66; Outworlders L66; Rimaros L73 | 6 |
| Ch53 | Meanwhile, Two Weeks Ago in Vitesse | Book_07_Timeline L12, L38, L75; Trenchant_Moore L102 | 4 |
| Ch54 | Hegemon’s Will | Celestines L87; Dawn L87; Spoiler_Management L87; Zartos L108-120; Gary L108-120; Jason_Asano L108-120; Soul_Bound_Items_and_Regalia L108-120; Hegemons_Will_and_Dominion L118-119, L120, L121, L123, L124, L125 … … | 25 |
| Ch55 | A Story About a Magic Trowel | Emi_Evans_Asano L35; Book_07_Timeline L40, L79; Landemere_Vane L64-79; 01_World_Primer L75; Glossary L75 | 6 |
| Ch56 | What It Sent Us | Book_07_Timeline L62, L74; Master_Timeline L62 | 3 |
| Ch57 | I Am Not Jason Asano | Book_07_Timeline L3, L27 | 2 |
| Ch58 | That Powerful and That Old | Dimensional_Storage_and_Portals L10; Minor_Cast_Order_of_Redeeming_Light L38; Book_07_Timeline L38, L76; Melody_Jain L38-46; Sophie_Wexler L38-46; Trenchant_Moore L53 | 7 |
| Ch59 | One Battle at a Time | Book_07_Timeline L8, L86, L124, L129; Dustin_Kettering L65; Minor_Cast_Books_7-9 L73; Tone_and_Voice L81-83 | 7 |
| Ch60 | No One Telling Me I Can’t | Great_Astral_Beings L27; Religion_in_Practice L27; Dawn L27, L27-30; Soramir L27; Book_07_Timeline L27, L94 | 7 |
| Ch61 | A Lot More Steps | Palisaros L59, L60; Book_07_Timeline L66 | 3 |
| Ch62 | A Normal Man | Rimaros L3, L43; Book_07_Timeline L38, L43; Estella_Warnock L41, L79; NPC_Rosters_by_Era L79 | 7 |
| Ch63 | This One Time | Book_07_Timeline L26 | 1 |
| Ch64 | Between Mortal and Something Else | Book_07_Timeline L14, L40, L72; Rimaros L21 | 4 |
| Ch65 | Stand at the Front | Book_07_Timeline L19, L21, L77 | 3 |
| Ch66 | The End of the World | Book_07_Timeline L4, L9, L27, L36, L96; Book_08_Timeline L27; Master_Timeline L27; Era_Selection L27; Minor_Cast_Books_7-9 L60 | 9 |

### Book 8

| Chapter | Title | Cited by (lines) | Rows |
|---|---|---|---|
| Ch1 | Band of Misfits | Book_08_Timeline L3, L7, L54 | 3 |
| Ch2 | The Pile of Disturbing Things | Book_08_Timeline L34, L53; Arabelle_Remore L49; Spirit_Vault_and_Astral_Kingdom L57-63 | 4 |
| Ch3 | Information Exchange | Book_08_Timeline L33, L34, L39, L65; Minor_Cast_Books_7-9 L38; Minor_Cast_Order_of_Redeeming_Light L38, L39-58 | 7 |
| Ch4 | Tampering With That Kind of Power | Book_08_Timeline L3, L83; Dawn L116 | 3 |
| Ch5 | You Don’t Have it in You | Estella_Warnock L7; Book_08_Timeline L7 | 2 |
| Ch6 | Good Luck Fighting Evil | Book_08_Timeline L4, L16, L21; Monsters L21 | 4 |
| Ch7 | Special Boy | Book_08_Timeline L4 | 1 |
| Ch8 | Strictly Necessary | Book_08_Timeline L12 | 1 |
| Ch9 | Opportunists | Book_08_Timeline L3, L11; Minor_Cast_Books_7-9 L11; Minor_Cast_Order_of_Redeeming_Light L11, L17, L30, L49, L50; Glossary L11; Monster_Cores_and_Training L35-36, L37; Cults_and_Orders L40; Era_Selection L40; Plot_Hooks L40 | 14 |
| Ch10 | A Bland Kind of Alchemy | Book_08_Timeline L5 | 1 |
| Ch11 | Ideal Enemy | Book_08_Timeline L8, L9 | 2 |
| Ch12 | Trying to Kill Jason Again | Adventuring_Profession L5; Confluences L5; Essence_Catalogue L5; Book_08_Timeline L5, L59 | 5 |
| Ch13 | Here to Steal | Book_08_Timeline L6; Minor_Cast_Order_of_Redeeming_Light L47-51, L51 | 3 |
| Ch14 | Not Really a Rules Guy | Book_08_Timeline L13, L24, L31, L60; Minor_Cast_Order_of_Redeeming_Light L71 | 5 |
| Ch15 | A Comparison He Could Avoid | Book_08_Timeline L30, L56 | 2 |
| Ch16 | Portal Logistics | Book_08_Timeline L19, L28; Minor_Cast_Books_7-9 L28; Minor_Cast_Order_of_Redeeming_Light L28, L86; Dimensional_Storage_and_Portals L90 | 6 |
| Ch17 | It Won’t Be a Good Reason | Minor_Cast_Order_of_Redeeming_Light L5, L29; Book_08_Timeline L5, L23; Killian_Laurent L8, L28; Gods_and_Churches L45 | 7 |
| Ch18 | Bait and Switch | Cults_and_Orders L3-6; Melody_Jain L3-6; NPC_Rosters_by_Era L3-6; Minor_Cast_Books_7-9 L4-25, L68; Minor_Cast_Order_of_Redeeming_Light L4-34, L14, L68; Book_08_Timeline L21 | 9 |
| Ch19 | That Kind of Power Can Be Lonely | Book_08_Timeline L29, L51; Great_Astral_Beings L40 | 3 |
| Ch20 | Blame | Cults_and_Orders L4; Minor_Cast_Books_7-9 L4; Book_08_Timeline L4; Plot_Hooks L4 | 4 |
| Ch21 | Speed | Book_08_Timeline L8; Celestines L40 | 2 |
| Ch22 | Delicate Flowers | Book_08_Timeline L36; Celestines L37; Sophie_Wexler L37-38 | 3 |
| Ch23 | Hope | Book_08_Timeline L28 | 1 |
| Ch24 | Preferred Option | 01_World_Primer L22; Girlano L22, L22-23, L23, L24-25, L25, L26; Book_08_Timeline L22, L58; Adventure_Society L22-25 | 10 |
| Ch25 | Sloppy Mistake | Girlano L120; Book_08_Timeline L130 | 2 |
| Ch26 | Criteria | Dimensional_Storage_and_Portals L5; Book_08_Timeline L23; Minor_Cast_Books_7-9 L29 | 3 |
| Ch27 | A Matter of Values | Book_08_Timeline L10, L26; Callum_Morse L26 | 3 |
| Ch28 | A Little Damage | Book_08_Timeline L14, L38; Palisaros L59 | 3 |
| Ch29 | Infiltrating the Stronghold | Book_08_Timeline L22; Minor_Cast_Order_of_Redeeming_Light L26-29; Minor_Cast_Books_7-9 L28; Carlos_Quilido L44; Belinda_Callahan L49-56 | 5 |
| Ch30 | Coming in Hot | Book_08_Timeline L3, L36, L54 | 3 |
| Ch31 | We Are Fighting Monsters | Hegemons_Will_and_Dominion L6; Book_08_Timeline L28, L33, L55 | 4 |
| Ch32 | Just Some Administrator | Book_08_Timeline L8 | 1 |
| Ch33 | Family Issues | Minor_Cast_Order_of_Redeeming_Light L15, L24, L45, L47; Cults_and_Orders L18-19; Book_08_Timeline L21, L74, L79; Minor_Cast_Books_7-9 L45, L64; Baseph_and_the_Rimaros_Children L64 | 11 |
| Ch34 | A Power That You’ve Overlooked | Book_08_Timeline L41, L108; Hegemons_Will_and_Dominion L63 | 3 |
| Ch35 | Nostalgia | Book_08_Timeline L12 | 1 |
| Ch36 | Saving the Day With the Power of Quips | Essence_Catalogue L3, L4; Book_08_Timeline L66 | 3 |
| Ch37 | Keep it Light | Baseph_and_the_Rimaros_Children L77; Book_08_Timeline L82 | 2 |
| Ch38 | Enough to Kill You With Power to Spare | Book_08_Timeline L27, L42 | 2 |
| Ch39 | A Significantly Different Paradigm | Dimensional_Storage_and_Portals L16; Book_08_Timeline L42, L104, L204, L234 | 5 |
| Ch40 | Something Drastic | Belinda_Callahan L7-13; Book_08_Timeline L12, L34 | 3 |
| Ch41 | Ridiculous New Soul Power | Book_08_Timeline L6, L58; Carlos_Quilido L58 | 3 |
| Ch42 | The Awakening of Mr Asano | Book_08_Timeline L18, L28, L32 | 3 |
| Ch43 | We’re Adventurers | Gods_and_Churches L48-53; Religion_in_Practice L48-53; Spoiler_Management L48-53; Book_08_Timeline L90 | 4 |
| Ch44 | The Person in My Care | Book_08_Timeline L18, L50, L53; Minor_Cast_Order_of_Redeeming_Light L29-40; Rimaros L50 | 5 |
| Ch45 | I Love a Hypocrite | Minor_Cast_Books_7-9 L4; Book_08_Timeline L17 | 2 |
| Ch46 | I’ve Told You Everything | Book_08_Timeline L50, L76 | 2 |
| Ch47 | Faith is Soul-Deep | Arabelle_Remore L31; Book_08_Timeline L37 | 2 |
| Ch48 | Lest He Become a Monster Himself | Gods_and_Churches L22-26, L40-60; Religion_in_Practice L22-26; Spoiler_Management L39-41; Book_08_Timeline L42, L96 | 6 |
| Ch49 | Quite a Lot of System Windows | Book_08_Timeline L50, L87, L106; Great_Astral_Beings L89-91; Astral_Kings_and_Messengers L105; Spirit_Vault_and_Astral_Kingdom L105; Era_Selection L105; Spoiler_Management L105 | 8 |
| Ch50 | Reasons to Quietly Dread | Book_08_Timeline L65, L89; Familiars L82; Tone_and_Voice L82; 00_Items_Overview L87; Tokens_Stones_and_Relics L87-91, L94-95, L97-100; Glossary L87-91; Zithis_Carrow_Vayel L89-95; Great_Astral_Beings L94-95 … | 12 |
| Ch51 | Authority | Open_Questions L30, L66, L68-74; Great_Astral_Beings L68-70; Tokens_Stones_and_Relics L68-70; Glossary L68-70; Book_08_Timeline L93 | 7 |
| Ch52 | The Kind of Pain I’m Used To | Palisaros L20; Book_08_Timeline L49 | 2 |
| Ch53 | A New Man | Book_08_Timeline L29 | 1 |
| Ch54 | Negotiating Position | Open_Questions L54, L60-61, L99; Book_08_Timeline L63, L99 | 5 |
| Ch55 | No Points of Conflict | Book_08_Timeline L4, L47; Great_Astral_Beings L25-31, L92, L92-93; Umber L85-86, L86; Glossary L85-89; Open_Questions L92; Familiars L92-93 | 10 |
| Ch56 | Quite Enough Transcendent Beings | Book_08_Timeline L35 | 1 |
| Ch57 | Flavours of Authority | 00_Cosmology_Overview L25-35; The_Builders_Door_and_Fundament_Gate L28, L64-67; Book_08_Timeline L62 | 4 |
| Ch58 | Mythmaking Was Within Expectations | Book_08_Timeline L19, L34; Master_Timeline L19 | 3 |
| Ch59 | Dodging the Topic | Book_08_Timeline L6, L57 | 2 |
| Ch60 | A Power That Did Not Belong to the World | Abilities_and_Attributes L5; Auras L5; Confluences L5; Book_08_Timeline L13 | 4 |
| Ch61 | A Gentleman Doesn’t Tell | Book_08_Timeline L91 | 1 |
| Ch62 | Recalibrate Their Expectations | Liara_Rimaros L28-32; Baseph_and_the_Rimaros_Children L32, L36, L39, L51; Minor_Cast_Books_7-9 L32, L32-40; Book_08_Timeline L32, L52; NPC_Rosters_by_Era L32; Zara_Rimaros L32-36; Storm_Kingdom_Culture L36; Palisaros L60 | 13 |
| Ch63 | Deeds of Legend | Baseph_and_the_Rimaros_Children L3; Minor_Cast_Books_7-9 L3; Book_08_Timeline L76; Callum_Morse L140 | 4 |
| Ch64 | A King Needs a Throne | Book_08_Timeline L15, L47; Astral_Kings_and_Messengers L72-80 | 3 |
| Ch65 | What Light Does | Book_08_Timeline L8, L31, L88, L94; Spirit_Vault_and_Astral_Kingdom L29-31, L30; Jason_Asano L85-93; Astral_Kings_and_Messengers L88; 00_Astral_Overview L88 | 9 |
| Ch66 | Why Anyone Would Pick You | Book_08_Timeline L44 | 1 |
| Ch67 | Astral Emperor | Astral_Kings_and_Messengers L53; Book_08_Timeline L53, L97 | 3 |
| Ch68 | Goodbyes | Book_08_Timeline L9, L50, L113 | 3 |

### Book 9

| Chapter | Title | Cited by (lines) | Rows |
|---|---|---|---|
| Ch1 | Don’t Show Up to the Fancy Party in Shorts | Jonah_Geller L39; Minor_Cast_Books_7-9 L49 | 2 |
| Ch2 | What She Was Willing to Do | Book_09_Timeline L18, L28, L76; Killian_Laurent L85 | 4 |
| Ch3 | More Than Just a Name | Book_09_Timeline L56, L90; Rufus_Remore L59; Minor_Cast_Books_7-9 L75, L86; Rimaros L81-82 | 6 |
| Ch4 | The Making of That Man | Killian_Laurent L11, L11-39; Book_09_Timeline L11; Minor_Cast_Books_7-9 L16 | 4 |
| Ch5 | A Lesson of Days Gone | Book_09_Timeline L4, L76; Killian_Laurent L4-99; Ranks_and_Advancement L55 | 4 |
| Ch6 | Dear John | Dawn L17; Jason_Asano L17; Tone_and_Voice L17; Book_09_Timeline L41; Amos_Pensinata L47, L48; NPC_Rosters_by_Era L47 | 7 |
| Ch7 | This Doesn’t Feel Glorious | Book_09_Timeline L33 | 1 |
| Ch9 | Occasionally Carnivorous | Book_09_Timeline L24, L42 | 2 |
| Ch10 | If You’re Going to Punish Someone | Minor_Cast_Books_7-9 L102; Book_09_Timeline L106 | 2 |
| Ch11 | One More Loyalty to Balance | Book_09_Timeline L5; Baseph_and_the_Rimaros_Children L60 | 2 |
| Ch12 | That Boy In the Tent | Book_09_Timeline L14 | 1 |
| Ch13 | A Difficult Child | Minor_Cast_Books_7-9 L3; Book_09_Timeline L3 | 2 |
| Ch14 | All Singer and No Song | Book_09_Timeline L4; Kasper_Irios L11 | 2 |
| Ch15 | Hefty Nuggets | Book_09_Timeline L114 | 1 |
| Ch16 | Following Your Convictions to Your Death | Book_09_Timeline L29; Minor_Cast_Books_4-6 L50; Glossary L50 | 3 |
| Ch17 | The God in This Scenario | Book_09_Timeline L61 | 1 |
| Ch18 | The Only Person Who Thinks It’s Obvious | Book_09_Timeline L3; Vitesse L70 | 2 |
| Ch19 | Uncharacteristic Sincerity | Melody_Jain L3; Sophie_Wexler L3-6; Book_09_Timeline L31 | 3 |
| Ch20 | The Only Wound You Can Truly Suffer | Confluences L12; Unusual_and_Unique_Magic L15; Essence_Catalogue L16; Book_09_Timeline L62 | 4 |
| Ch21 | Mother’s Favourite | Book_09_Timeline L4, L47, L91 | 3 |
| Ch22 | A Good Friend to Have | Book_09_Timeline L18 | 1 |
| Ch23 | Put the Extraordinary Aside | Astral_Kings_and_Messengers L44; Book_09_Timeline L84 | 2 |
| Ch24 | A Chance For Some Relative Quiet | Book_09_Timeline L30, L44, L49; Amos_Pensinata L35; Orin_Pensinata L35, L49; Master_Timeline L44; Korinne_Pescos L49-52 | 8 |
| Ch25 | Surplus to Requirements | 00_Places_Overview L4; Hornis L4; Book_09_Timeline L4; Korinne_Pescos L31-63, L58; Orin_Pensinata L79 | 6 |
| Ch26 | Bad at Crime | Girlano L3; Book_09_Timeline L26, L64; Master_Timeline L26 | 4 |
| Ch27 | An Evil God Sitting on Her Shoulder | Kurdansk_Culture L24; Melody_Jain L24; Glossary L24; Kurdansk L24-26; Book_09_Timeline L26, L63; Callum_Morse L63, L91 | 8 |
| Ch28 | A Responsibility as Much as a Privilege | Book_09_Timeline L31, L45, L108; Cults_and_Orders L45; Minor_Cast_Books_7-9 L45; Orin_Pensinata L87-112 | 6 |
| Ch29 | Fighting the Power | Book_09_Timeline L13, L14; 00_Places_Overview L17; Cartise L17-18, L18-19 | 5 |
| Ch30 | Make Jason Great Again | Book_09_Timeline L27, L119; Cartise L59 | 3 |
| Ch31 | Neil’s Big Mouth | Cartise L11; Book_09_Timeline L11, L40 | 3 |
| Ch32 | Rage, Authority and Otherworldly Power | Book_09_Timeline L15 | 1 |
| Ch33 | Asset | Confluences L15; Humans L15; Humphrey_Geller L15; Taika L15; Book_09_Timeline L16; Pranay_Culture L19 | 6 |
| Ch34 | The Thing You Practise With The Most | Book_09_Timeline L18, L74 | 2 |
| Ch35 | Just to Prove You Could | Book_09_Timeline L11; Cartise L60, L62 | 3 |
| Ch36 | A Matter of What You Want | Book_09_Timeline L3, L19, L57 | 3 |
| Ch37 | Where We End | Book_09_Timeline L48, L69 | 2 |
| Ch38 | People That You Didn’t Aggravate | Book_09_Timeline L5, L60 | 2 |
| Ch39 | Not You | Isart L12, L12-26, L16, L26; 00_Places_Overview L12-20; Book_09_Timeline L26, L91 | 7 |
| Ch40 | Inventing a Man in Your Head | Book_09_Timeline L5; Zara_Rimaros L7-13, L13, L18, L21, L55, L72 | 7 |
| Ch41 | Doing Things That You Shouldn’t | Astral_Kings_and_Messengers L81; Book_09_Timeline L119 | 2 |
| Ch42 | Quiet Professionalism | Book_09_Timeline L5, L31, L57, L74; Yaresh_Culture L26; 00_Places_Overview L26; Yaresh L26, L34; Era_Selection L26, L80; Plot_Hooks L80; Amos_Pensinata L90 | 12 |
| Ch43 | A Man of Many Talents | Yaresh_Culture L33; Yaresh L33; Estella_Warnock L33; Book_09_Timeline L33, L72 | 5 |
| Ch44 | The Same Thing as Telling the Truth | Yaresh_Culture L3; Book_09_Timeline L25 | 2 |
| Ch45 | The Point of Sacrifice | Book_09_Timeline L4, L58; Taika L10; 01_World_Primer L57; 00_Peoples_Overview L57; Valash L57, L58 | 7 |
| Ch46 | What You Want Instead of What You Need | Daily_Life L5; Elves L5; Valash L5, L6; Minor_Cast_Books_7-9 L5-12; Book_09_Timeline L12, L32; Benella L40, L44 | 9 |
| Ch47 | Settling Differences With a Nice Chat | Benella L25, L49 | 2 |
| Ch48 | The Sex Magic Thing | Sophie_Wexler L12; Book_09_Timeline L42 | 2 |
| Ch49 | The Power and the Control | Book_09_Timeline L79, L80, L81 | 3 |
| Ch50 | Distant Power | Book_09_Timeline L27 | 1 |
| Ch51 | Who You Truly Are | Book_09_Timeline L32 | 1 |
| Ch52 | The Genuine Article | Astral_Kings_and_Messengers L5, L60; Fal_Vin_Garath L20-28, L36, L42-44; Benella L20-29; Book_09_Timeline L32 | 7 |
| Ch53 | Stories About Fungus | Book_09_Timeline L11, L101 | 2 |
| Ch54 | Vampire Monster Slaves | Book_09_Timeline L3, L64 | 2 |
| Ch55 | The Face of Insurmountable Power | Book_09_Timeline L3; Celestines L9; Jes_Fin_Kaal L19, L27, L28; NPC_Rosters_by_Era L19 | 6 |
| Ch56 | Even Though You Fear | Benella L4, L5, L20, L22-26; Astral_Kings_and_Messengers L5, L5-8; Fal_Vin_Garath L5, L5-7; NPC_Rosters_by_Era L5; Plot_Hooks L5; Tone_and_Voice L13, L14; Jes_Fin_Kaal L14, L22-26; Hess_Jor_Nasala L40, L75, L101 … | 19 |
| Ch57 | Mockery | Book_09_Timeline L16 | 1 |
| Ch58 | Die Immediately Without Prompting | Book_09_Timeline L45; Era_Selection L50 | 2 |
| Ch60 | Grisly Chore | Ranks_and_Advancement L7; Book_09_Timeline L15 | 2 |
| Ch61 | Inferior | Book_09_Timeline L3 | 1 |
| Ch62 | Apocalypse | Book_09_Timeline L22; Astral_Kings_and_Messengers L23, L30, L30-34; Spoiler_Management L30-34 | 5 |
| Ch63 | Superior | Book_09_Timeline L23 | 1 |
| Ch64 | Significantly More Powerful | 00_Astral_Overview L69, L88; Book_09_Timeline L96 | 3 |
| Ch65 | Evil Lair | Souls_Death_and_Healing L22-23; Astral_Kings_and_Messengers L23; Open_Questions L30 | 3 |
| Ch66 | Imperfect Responses | Hess_Jor_Nasala L3, L39, L41; Book_09_Timeline L3; NPC_Rosters_by_Era L3 | 5 |
| Ch67 | Triage | Book_09_Timeline L6 | 1 |
| Ch68 | Unquestionably Authoritarian | Book_09_Timeline L77 | 1 |
| Ch69 | Voice of the Will | Astral_Kings_and_Messengers L55-59; Familiars L55-59 | 2 |
| Ch71 | An Egg Starting to Hatch | Book_09_Timeline L31; Taika L43 | 2 |
| Ch72 | What the Swarm Came to Cure | Book_09_Timeline L46 | 1 |
| Ch73 | A Mortal Perspective | Book_09_Timeline L41, L90 | 2 |
| Ch74 | Mr Asano Will See You Now | Gods_and_Churches L43; Yaresh L43, L114; Book_09_Timeline L43 | 4 |
| Ch75 | Hot Chocolate | Book_09_Timeline L25 | 1 |
| Ch76 | Sadness Porridge | Book_09_Timeline L88 | 1 |
| Ch77 | The Better Adventurer | Minor_Cast_Books_7-9 L3; Yaresh L13; Book_09_Timeline L13 | 3 |
| Ch78 | Brave Because It Can Win | Vesta_Carmis_Zell L82; Book_09_Timeline L82; NPC_Rosters_by_Era L82; Confluences L107; Awakening_Stones L126-129, L129 | 6 |
| Ch79 | A Man That Will Inspire Courage | Yaresh L5; Book_09_Timeline L21 | 2 |
| Ch80 | Luck That Good | Yaresh L3; Gods_and_Churches L6-13; Hana_Shavar L6-13; Book_09_Timeline L7 | 4 |
| Ch81 | Nice and Grunty | Book_09_Timeline L5; Yaresh L20; 00_Magic_Overview L61; Souls_Death_and_Healing L61-63 | 4 |
| Ch82 | Breach | Book_09_Timeline L24 | 1 |
| Ch84 | The Lady Shooting Hurricanes at People | Orin_Pensinata L9; Glossary L9; Book_09_Timeline L50 | 3 |
| Ch85 | Humphrey’s New Normal | Book_09_Timeline L50 | 1 |
| Ch86 | Not Enough Monsters to Fight | Marek_Nior_Vargas L16; Book_09_Timeline L16 | 2 |
| Ch87 | The Difference in Conviction | Marek_Nior_Vargas L31 | 1 |
| Ch88 | Something to Turn the Tide | Book_09_Timeline L36 | 1 |
| Ch89 | The Strongest Arrow in His Quiver | Book_09_Timeline L26; Glossary L43 | 2 |
| Ch90 | Win a Fight | Book_09_Timeline L3; 00_Astral_Overview L4 | 2 |
| Ch92 | A Pretty Creepy Dude | Book_09_Timeline L76 | 1 |
| Ch93 | Security Oversight | Book_09_Timeline L67 | 1 |
| Ch94 | I Have to Go Fight Evil | Book_09_Timeline L3, L30; Familiars L24-26; Amos_Pensinata L30 | 4 |
| Ch95 | Stray Thought | Astral_Kings_and_Messengers L15; 00_Astral_Overview L15 | 2 |
| Ch96 | Heretic | Book_09_Timeline L14 | 1 |
| Ch97 | An Extremely Annoying Catalyst | Book_09_Timeline L74; Raythe L80; Tone_and_Voice L80 | 3 |
| Ch98 | Teaching Moment | Elves L4; Yaresh_Culture L4; Book_09_Timeline L4, L56; NPC_Rosters_by_Era L4; Allayeth L4-5; Charist L4-6 | 7 |
| Ch99 | Rigid Flaws | Book_09_Timeline L11 | 1 |
| Ch100 | Doubt, Fear and Hesitation | Tera_Jun_Casta L19, L49; Book_09_Timeline L51, L64 | 4 |
| Ch101 | No | Book_09_Timeline L18 | 1 |
| Ch102 | A Fight to the Pain | Book_09_Timeline L9; Tera_Jun_Casta L54-67; Open_Questions L55, L66-67; Vesta_Carmis_Zell L65, L66-67; Astral_Kings_and_Messengers L66-67 | 7 |
| Ch103 | One Ludicrous Encounter to the Next | Book_09_Timeline L64, L85; Yaresh L84; Marek_Nior_Vargas L114 | 4 |
| Ch104 | The Foolish Choice | Marek_Nior_Vargas L3; Book_09_Timeline L5, L26, L27, L54, L62, L76 …; Charist L29; Dustin_Kettering L54; Phoebe_Geller L54; Rick_Geller L54; Astral_Kings_and_Messengers L84; Yaresh L84 | 14 |

### Book 10

| Chapter | Title | Cited by (lines) | Rows |
|---|---|---|---|
| Ch1 | Aftermath | Book_10_Timeline L51; Astral_Kings_and_Messengers L52; 00_Astral_Overview L52; Vesta_Carmis_Zell L53; NPC_Rosters_by_Era L53; Open_Questions L53; Hannah_and_Claire_Adeah L77-80 | 7 |
| Ch2 | Harder Than They Have to Be | Book_10_Timeline L9, L65; Vesta_Carmis_Zell L19, L40; NPC_Rosters_by_Era L19; Plot_Hooks L19, L40 | 7 |
| Ch3 | Developing Any Skill Takes Practise | Book_10_Timeline L24; Gods_and_Churches L29; Elves L29; Hana_Shavar L29; Cloud_Constructs_and_Palaces L29; NPC_Rosters_by_Era L29 | 6 |
| Ch4 | War Guilt Clause | Book_10_Timeline L31; 01_World_Primer L53-55 | 2 |
| Ch5 | Primary Purpose | Book_10_Timeline L3, L24, L46; 00_Cosmology_Overview L80-84 | 4 |
| Ch6 | Everyone Has a Price | Book_10_Timeline L9; Astral_Kings_and_Messengers L11 | 2 |
| Ch7 | Trust | Book_10_Timeline L6 | 1 |
| Ch8 | Original Design Parameters | Book_10_Timeline L46 | 1 |
| Ch9 | Unstable | Gods_and_Churches L10; NPC_Rosters_by_Era L10, L38; Musin_Heath L37, L38; Book_10_Timeline L38; Jes_Fin_Kaal L49 | 7 |
| Ch10 | Dark Bargain | Musin_Heath L3; Book_10_Timeline L7; Plot_Hooks L64 | 3 |
| Ch11 | Decorum | Musin_Heath L4; Book_10_Timeline L67 | 2 |
| Ch12 | A Man of Principle | Book_10_Timeline L11 | 1 |
| Ch13 | Experiment | Book_10_Timeline L36 | 1 |
| Ch14 | Spanked | Gormanston_Bynes L3; NPC_Rosters_by_Era L3; Book_10_Timeline L8; Yaresh_Culture L28-31, L33, L35; Era_Selection L28-35; Plot_Hooks L28-35; Guilds_and_Houses L33-35; Yaresh L33-35 … | 11 |
| Ch15 | Better Ambitions | Astral_Kings_and_Messengers L3, L6, L9; Great_Astral_Beings L5; Erigo_Fin_Desca L5, L10, L15-20, L25-26; NPC_Rosters_by_Era L5, L6; Jamis_Fran_Muskar L6, L9; Book_10_Timeline L6; Vesta_Carmis_Zell L8, L30-43; Zithis_Carrow_Vayel L9 … | 18 |
| Ch16 | The Instinct to Kneel | Hess_Jor_Nasala L26-53; Astral_Kings_and_Messengers L48; Gormanston_Bynes L61, L62-63; Book_10_Timeline L62 | 5 |
| Ch17 | Acceptable Terms | Book_10_Timeline L9, L39, L52; Book_09_Timeline L52; Master_Timeline L52 | 5 |
| Ch18 | Actual Adventurers | Book_10_Timeline L92, L96; Gormanston_Bynes L133, L137 | 4 |
| Ch19 | Bad Influence | Book_10_Timeline L3 | 1 |
| Ch20 | Not Like the Ones We Know | Book_10_Timeline L8, L104 | 2 |
| Ch21 | A Juice Newton Situation | Book_10_Timeline L13, L26; Rufus_Remore L19-21 | 3 |
| Ch22 | A More Practical Purpose | Book_10_Timeline L3, L112 | 2 |
| Ch24 | Leap of Faith | Book_10_Timeline L9 | 1 |
| Ch25 | Garden-Variety Arrogance | Book_10_Timeline L27, L74 | 2 |
| Ch26 | How to Reach Gold Rank in Three Easy Steps | Book_10_Timeline L4; Zithis_Carrow_Vayel L54-55; Great_Astral_Beings L55; Master_Timeline L55; Spoiler_Management L55 | 5 |
| Ch27 | Nigh-Impossible Goal | Book_10_Timeline L80 | 1 |
| Ch28 | We Should Probably Get You Out of Here | Amos_Pensinata L7; Book_10_Timeline L40; Gods_and_Churches L56 | 3 |
| Ch29 | The Questions You’re Asking Don’t Matter | Book_10_Timeline L89 | 1 |
| Ch30 | Political Price | Book_10_Timeline L63 | 1 |
| Ch31 | Ordinary Everyday Adventuring | Book_10_Timeline L9, L55; Master_Timeline L9; Gods_and_Churches L69-75; Religion_in_Practice L69-75; Spoiler_Management L69-75; Glossary L74 | 7 |
| Ch32 | Drunken Lies and Mythic Legends | Book_10_Timeline L49; Monsters L77 | 2 |
| Ch33 | Stash Wakes Up From a Nap | Book_09_Timeline L76; Book_10_Timeline L76, L108; Book_11_Timeline L76; Master_Timeline L76; Era_Selection L76; Familiars L109; Spirit_Vault_and_Astral_Kingdom L109-111 | 8 |
| Ch34 | Welcome Back, Colin | Book_10_Timeline L39, L117 | 2 |
| Ch35 | Optimism | Book_10_Timeline L13; Magic_Society_and_Associations L36 | 2 |
| Ch36 | Mothers | Book_10_Timeline L11; Cults_and_Orders L14-17; Spoiler_Management L14-17 | 3 |
| Ch37 | The Whims of People Like Me | Book_10_Timeline L20 | 1 |
| Ch38 | What’s Wrong With Simple | Gods_and_Churches L73; Jason_Asano L73; Book_10_Timeline L83 | 3 |
| Ch39 | Faith is the Bane of Intellect | Book_10_Timeline L45; Gods_and_Churches L46-49 | 2 |
| Ch40 | Listing Off Animals | Book_10_Timeline L15, L39; Gods_and_Churches L16 | 3 |
| Ch41 | I’m Going to Change the Laws of Reality | Book_10_Timeline L47 | 1 |
| Ch42 | Exactly Where I Want to Be | Marek_Nior_Vargas L4; Book_10_Timeline L4; Astral_Kings_and_Messengers L7; Tera_Jun_Casta L7; Estella_Warnock L39, L41 | 6 |
| Ch43 | An Impossible Act of Forgiveness | Book_10_Timeline L3, L13 | 2 |
| Ch44 | The Manner of Person One Will Be Dealing With | Book_10_Timeline L25 | 1 |
| Ch45 | Because It’s Hard | Book_10_Timeline L108 | 1 |
| Ch46 | Everything Adventurers Should Be | Book_10_Timeline L3, L31 | 2 |
| Ch47 | What is the Adventure Society | Book_10_Timeline L6, L76; Guilds_and_Houses L60-62; Gormanston_Bynes L60-63; Adventure_Society L76; Marcus_Hargrave_Xenoria L76, L78; NPC_Rosters_by_Era L76; 01_World_Primer L78; Familiars L78 … | 11 |
| Ch48 | Tradition and Decency | Gormanston_Bynes L4, L9-10; Marcus_Hargrave_Xenoria L10; Book_10_Timeline L57 | 4 |
| Ch49 | Destiny | Book_10_Timeline L135 | 1 |
| Ch50 | The Nightmares Never Really Go | Book_10_Timeline L3, L28; Marcus_Hargrave_Xenoria L51 | 3 |
| Ch51 | Unmistakeable | Hannah_and_Claire_Adeah L3, L9; Miriam_Vance L43; Book_10_Timeline L43; Glossary L43; Open_Questions L43 | 6 |
| Ch52 | Money or the Box | Marcus_Hargrave_Xenoria L4-6; Book_10_Timeline L70 | 2 |
| Ch53 | The Task You Can’t Seem to Manage | Book_10_Timeline L5 | 1 |
| Ch54 | Worth Saving | Book_10_Timeline L38 | 1 |
| Ch55 | Not Yet | Book_10_Timeline L18 | 1 |
| Ch57 | Welcome Aboard | Book_10_Timeline L3, L60, L92 | 3 |
| Ch58 | Quick and Clean | Callum_Morse L7; Book_10_Timeline L47; Gormanston_Bynes L58; Marcus_Hargrave_Xenoria L58-61; Killian_Laurent L106 | 5 |
| Ch59 | What We’re Walking Into | Miriam_Vance L4, L17; Book_10_Timeline L5, L47; Marcus_Hargrave_Xenoria L12; Yaresh_Culture L17; Allayeth L17; Glossary L17; Open_Questions L17; Jes_Fin_Kaal L38 | 10 |
| Ch60 | What Kind of Adventurer | Marcus_Hargrave_Xenoria L13-46; Book_10_Timeline L14, L42 | 3 |
| Ch61 | Gary’s Old Team | Monsters L19; Book_10_Timeline L20; Miriam_Vance L45 | 3 |
| Ch62 | Hit Points | Book_10_Timeline L28 | 1 |
| Ch63 | Surplus to Requirements | Book_10_Timeline L3, L52; Glossary L16 | 3 |
| Ch64 | Pride | Amos_Pensinata L9; Orin_Pensinata L9; Glossary L9; Miriam_Vance L22 | 4 |
| Ch65 | The Greatest Enemy of All | Yaresh L3; Book_10_Timeline L3, L30; Plot_Hooks L3-6; Smoulder_and_Brighthearts L6, L9; Marla L9, L24; NPC_Rosters_by_Era L9, L30; Cults_and_Orders L30; Minor_Cast_Books_10-13 L30, L39 … | 15 |
| Ch66 | Taking the Position of a God | Book_10_Timeline L12, L85; Gods_and_Churches L103 | 3 |
| Ch67 | Confident Guesses | Miriam_Vance L64; Book_10_Timeline L105 | 2 |
| Ch68 | You Don’t Do it Blindly | Miriam_Vance L10; Book_10_Timeline L68 | 2 |
| Ch69 | Of a Mind to Kill You | Minor_Cast_Books_10-13 L3-5; Smoulder_and_Brighthearts L4; Book_10_Timeline L4; Miriam_Vance L19 | 4 |
| Ch70 | Humungous Hairy Hands | Book_10_Timeline L22; Dustin_Kettering L38 | 2 |
| Ch71 | Echoes of the Dead | Book_10_Timeline L39; Glossary L39; Smoulder_and_Brighthearts L52 | 3 |
| Ch72 | Citadel | Book_10_Timeline L3, L58; Marla L28-38; 01_World_Primer L31; Yaresh L31; Era_Selection L31; Minor_Cast_Books_1-3 L41; Minor_Cast_Books_10-13 L41; Glossary L41 | 9 |
| Ch73 | The Impossible | Marla L7-51 | 1 |
| Ch74 | Everything in My Power | Book_10_Timeline L31 | 1 |
| Ch75 | Control the Pot | Book_10_Timeline L17 | 1 |
| Ch76 | It Happens Because I Want It To | Miriam_Vance L3; Book_10_Timeline L45 | 2 |
| Ch77 | More Urgent With Your Warning | Book_10_Timeline L67 | 1 |
| Ch78 | A Little Bit Odd | Book_10_Timeline L27; Gods_and_Churches L32, L38; Hana_Shavar L38; Era_Selection L38; Plot_Hooks L38; Cults_and_Orders L38-41; Arabelle_Remore L52; Gabriel_Remore L52-89 | 9 |
| Ch79 | Dubious Alliance | Boris_Ket_Lundi L44-54; Glossary L52-54; Book_10_Timeline L86, L112 | 4 |
| Ch80 | Come Like a Tsunami | Book_10_Timeline L29, L42; Miriam_Vance L33; Garth_Larosse L42; NPC_Rosters_by_Era L42 | 5 |
| Ch81 | Put Up or Shut Up | Glossary L34; Jes_Fin_Kaal L36 | 2 |
| Ch82 | Miracle | Miriam_Vance L58; Gods_and_Churches L62, L72; Book_10_Timeline L62 | 4 |
| Ch83 | Death Knows How to Wait | Book_10_Timeline L61; Jason_Asano L67-73; Gods_and_Churches L75-78 | 3 |
| Ch84 | Sometimes They Do | Book_10_Timeline L85 | 1 |
| Ch85 | Fighting Alone | Miriam_Vance L38; Gods_and_Churches L40; Book_10_Timeline L68 | 3 |
| Ch86 | Insufficient Vessel | Book_10_Timeline L19, L61; Gods_and_Churches L59, L67-70; NPC_Rosters_by_Era L59; Tokens_Stones_and_Relics L59-61; Plot_Hooks L59-61; Confluences L67-70, L67-72; Essence_Catalogue L67-70; Abilities_and_Attributes L71-72 | 11 |
| Ch87 | Twin Flames | Book_10_Timeline L50 | 1 |
| Ch88 | Naught But Faith | Book_10_Timeline L23, L80; Garth_Larosse L58; Gods_and_Churches L58-63; Marla L116 | 5 |
| Ch89 | Thinking Like an Adventurer | Gods_and_Churches L54; Book_10_Timeline L79; Marla L89-95 | 3 |
| Ch90 | Dread and Crushing Despair | Book_10_Timeline L17 | 1 |
| Ch91 | Avatar and Demigod | Book_10_Timeline L46 | 1 |
| Ch92 | What He Wants For Himself | Book_10_Timeline L14, L42; Garth_Larosse L65-66 | 3 |

### Book 11

| Chapter | Title | Cited by (lines) | Rows |
|---|---|---|---|
| Ch1 | What Makes Them Our Enemies | Gods_and_Churches L9; Book_11_Timeline L15, L37, L39, L58; Astral_Spaces_Zones_and_Surges L15-17, L16, L17, L36, L38-39, L38-42 …; 00_Magic_Overview L16; Earth_Magic L16, L36; Era_Selection L16; 00_Cosmology_Overview L22-24; Spirit_Vault_and_Astral_Kingdom L54, L64 … | 20 |
| Ch2 | Share the Responsibility | Book_11_Timeline L4; Open_Questions L75 | 2 |
| Ch3 | Contrition Born at the Point of a Sword | Book_11_Timeline L19, L46 | 2 |
| Ch4 | Overestimating the Length | Marla L21; Book_11_Timeline L21, L57; Gods_and_Churches L85 | 4 |
| Ch5 | Good Friends | Book_11_Timeline L8, L63 | 2 |
| Ch6 | Lackeys | Book_11_Timeline L13; Minor_Cast_Books_1-3 L59; Neil_Davone L60, L63; Glossary L62; Dustin_Kettering L64 | 6 |
| Ch7 | Yellow Bell | Book_11_Timeline L36, L82 | 2 |
| Ch8 | Rock Climbing | Book_11_Timeline L21, L45, L102; Dustin_Kettering L23; Neil_Davone L23-24; Nik_Asano L102, L102-106; Tone_and_Voice L102, L102-106 | 9 |
| Ch9 | Grunts and Sizzling Noises | Book_11_Timeline L108 | 1 |
| Ch10 | The Man Who Commands the Lightning | Book_11_Timeline L12 | 1 |
| Ch11 | Style Over Substance | Dustin_Kettering L6, L43-49, L49 | 3 |
| Ch12 | Precise Control | Book_11_Timeline L19 | 1 |
| Ch13 | Impostor Syndrome | Book_11_Timeline L4; Belinda_Callahan L4-7 | 2 |
| Ch16 | Group Dynamics | Book_11_Timeline L29 | 1 |
| Ch17 | As Many as We Can Get | Transformation_Zones L10, L27, L33; Book_11_Timeline L27, L33; Marla L80 | 6 |
| Ch18 | Alienness and Familiarity | Transformation_Zones L4; Book_11_Timeline L4; Master_Timeline L4 | 3 |
| Ch19 | The Reason We Have To | Book_11_Timeline L19; Miriam_Vance L56 | 2 |
| Ch20 | A Bitter Cup | Book_11_Timeline L3 | 1 |
| Ch21 | Good Leader | Book_11_Timeline L9 | 1 |
| Ch22 | I Want Those Things For You | Great_Astral_Beings L11; Velius L11; Raythe L12; Helsveth L32; Book_11_Timeline L66 | 5 |
| Ch23 | Small, Easy or Inconsequential | Nik_Asano L38, L42; 01_World_Primer L42; Tone_and_Voice L42; Minor_Cast_Books_10-13 L78 | 5 |
| Ch24 | Another Astral King | Boris_Ket_Lundi L69, L85; Book_11_Timeline L85; Vesta_Carmis_Zell L85-86; Astral_Kings_and_Messengers L86; Open_Questions L86 | 6 |
| Ch25 | Unorthodoxy | Open_Questions L47-55, L49-57, L51, L53; 01_World_Primer L49-51; Astral_Kings_and_Messengers L51, L53; Book_11_Timeline L51; NPC_Rosters_by_Era L51; Spoiler_Management L51; Glossary L51 | 11 |
| Ch26 | Messengers Don’t Have Hearts | Book_11_Timeline L96 | 1 |
| Ch27 | Will He Be Broken | Book_11_Timeline L38; Zithis_Carrow_Vayel L55 | 2 |
| Ch28 | Risking Everything | Book_11_Timeline L40 | 1 |
| Ch29 | A Dangerous Power | Cults_and_Orders L3; Gods_and_Churches L3-5; Astral_Kings_and_Messengers L31; Book_11_Timeline L31 | 4 |
| Ch30 | Bit of an Odd Bloke | Book_11_Timeline L6 | 1 |
| Ch31 | Asking For a Lot of Trust | Book_11_Timeline L3; Boris_Ket_Lundi L69, L87 | 3 |
| Ch32 | It Used to Be Completely Dark | Book_11_Timeline L8; Orin_Pensinata L73-74; Miriam_Vance L75 | 3 |
| Ch33 | He Likes to Name-Drop | Familiars_Summons_and_Conjurations L4; Book_11_Timeline L4; Miriam_Vance L20; Open_Questions L20; Familiars L50; 00_Cosmology_Overview L112 | 6 |
| Ch34 | He Isn’t Always Evil and He is Not Always Wrong | Book_11_Timeline L15, L33, L124; Master_Timeline L33; 00_Cosmology_Overview L97, L103; Great_Astral_Beings L97, L103 | 8 |
| Ch35 | New Power and a Freshly Cooked Batch of Smugness | Book_11_Timeline L39 | 1 |
| Ch36 | Instinctively Protected | Book_11_Timeline L3; Earth_Powers L7, L8; NPC_Rosters_by_Era L8; Yumi_Asano L8-12; Nitra L12; Nik_Asano L40-42, L40-45; Familiars L43; Tone_and_Voice L43 … | 11 |
| Ch37 | No Limit | Book_11_Timeline L58 | 1 |
| Ch38 | The Hegemon | Nik_Asano L3, L33; Book_11_Timeline L61 | 3 |
| Ch39 | Miracles Work on a Different Scale | Book_11_Timeline L3 | 1 |
| Ch40 | Right Now | Book_11_Timeline L68 | 1 |
| Ch41 | Leadership Isn’t Easy | Book_11_Timeline L59 | 1 |
| Ch42 | A Decision Made Poorly and in Haste | Elizabeth L38; Book_11_Timeline L38; 00_Earth_Overview L40, L63; Earth_Powers L59-65 | 5 |
| Ch43 | Binaries | Book_11_Timeline L14, L131 | 2 |
| Ch44 | When We Worry the Most | Minor_Cast_Books_10-13 L39; Book_11_Timeline L64 | 2 |
| Ch46 | Academically Unsound | Minor_Cast_Books_7-9 L11; Minor_Cast_Order_of_Redeeming_Light L11; Glossary L11; Book_11_Timeline L17, L20; Nik_Asano L30-33, L32 | 7 |
| Ch47 | Not All of Us Are Demigods | Amos_Pensinata L64 | 1 |
| Ch48 | The Price | Book_11_Timeline L22, L62 | 2 |
| Ch49 | Guaranteed to Become Enemies | Book_11_Timeline L69; Open_Questions L71; Miriam_Vance L79; Amos_Pensinata L86 | 4 |
| Ch50 | Assuming We Win | Nik_Asano L10-25, L15; Book_11_Timeline L11, L15, L56; Transformation_Zones L15; Master_Timeline L15; Open_Questions L15 | 8 |
| Ch51 | Don’t Throw Our Dead Friend’s Stuff Out of a Tortoise | Transformation_Zones L3; Book_11_Timeline L3; Miriam_Vance L64 | 3 |
| Ch52 | Beware of Chicken | Miriam_Vance L10; Book_11_Timeline L104 | 2 |
| Ch53 | A Better Adventurer | Book_11_Timeline L8; Miriam_Vance L25; Nik_Asano L56 | 3 |
| Ch54 | The Only Way It Can Win | Amos_Pensinata L18-21, L56; Book_11_Timeline L61 | 3 |
| Ch55 | When Violence Is Easy and Words Are Hard | Amos_Pensinata L3; Miriam_Vance L3; Book_11_Timeline L25 | 3 |
| Ch56 | A Cocktail of Ignorance, Arrogance and Ambition | Book_11_Timeline L48 | 1 |
| Ch57 | Different Enough | Nik_Asano L26-41; Gary L60; Book_11_Timeline L60; Tone_and_Voice L60 | 4 |
| Ch58 | Everything I Need | Book_11_Timeline L91 | 1 |
| Ch59 | The Work of Higher Beings | Book_11_Timeline L10 | 1 |
| Ch60 | Heroes Cheat All the Time | Era_Selection L3; Open_Questions L3; Book_11_Timeline L5, L48; Danielle_Geller L13; Gwydion_Remore L13, L22; NPC_Rosters_by_Era L13 | 8 |
| Ch61 | You Know It’s Trouble | Raythe L8; Velius L8; NPC_Rosters_by_Era L8; Nik_Asano L16; Book_11_Timeline L16; Master_Timeline L16 | 6 |
| Ch62 | Steve, Lord of Undeath | Umber L36; Book_11_Timeline L89 | 2 |
| Ch63 | Time Travel is the Worst | Book_11_Timeline L39, L98; 00_Cosmology_Overview L76, L98, L100; Master_Timeline L80 | 6 |
| Ch64 | Unique in the Entire Cosmos | Great_Astral_Beings L9, L49; Raythe L9; Velius L9; Book_11_Timeline L23; 00_Cosmology_Overview L24-27, L49; Spoiler_Management L24-27 | 8 |
| Ch65 | A Power That No One and Nothing Should Have | 01_World_Primer L8; Book_11_Timeline L8, L34; Master_Timeline L8; 00_Cosmology_Overview L55, L57-58, L75; Great_Astral_Beings L55, L57-59, L75; Raythe L55; Open_Questions L75 | 12 |
| Ch66 | Party to Betrayal | Book_11_Timeline L22, L89; Open_Questions L95 | 3 |
| Ch67 | Farewells | Book_11_Timeline L5; Gods_and_Churches L6; Carlos_Quilido L6; Open_Questions L9; Nik_Asano L19; Gwydion_Remore L20 | 6 |
| Ch68 | Compassionate Strangers | Hegemons_Will_and_Dominion L103-106; Book_11_Timeline L115, L412, L703, L782, L918, L1034 …; Master_Timeline L115, L703, L782, L918, L2260; Open_Questions L115, L159, L703, L707-709, L782, L1580; Great_Astral_Beings L171-175, L707-709, L1793-1795, L2209, L2209-2214, L2526 …; Boris_Ket_Lundi L305, L481, L493-498; Taika L305; Carlos_Quilido L367 … | 130 |

### Book 12

| Chapter | Title | Cited by (lines) | Rows |
|---|---|---|---|
| Ch0 | Don’t Tell Humphrey | Zara_Rimaros L14; Book_12_Timeline L19 | 2 |
| Ch1 | Why He Hasn’t | Raythe L5-11; Book_12_Timeline L10, L53; Great_Astral_Beings L26; 01_World_Primer L34, L36; Anna_Tilden L36, L80; Miles_Cotezee L53; Magic_Society_and_Associations L55-57, L55-59, L57, L58, L76; Gods_and_Churches L58 … | 19 |
| Ch2 | If We Can’t Change For the Better | Book_12_Timeline L7, L107; Raythe L9; Miles_Cotezee L50; Yumi_Asano L92; Master_Timeline L107; Spoiler_Management L107; Open_Questions L107 | 8 |
| Ch3 | We’re All Stuck in a Hole | Book_12_Timeline L3, L5, L7, L13, L82; Earth_Powers L3-8; Nigel_Thornton L3-8; Anna_Tilden L7 | 8 |
| Ch4 | A Silent City | Book_12_Timeline L3, L14, L28, L40, L49; Saint-Etienne L20, L41 | 7 |
| Ch5 | The Fundamental Things | Book_12_Timeline L89; Magic_Society_and_Associations L99 | 2 |
| Ch6 | You Don’t Want Glory | Gods_and_Churches L18-22; Book_12_Timeline L23 | 2 |
| Ch7 | The Power Looming Over Us All | Book_12_Timeline L8, L78; Master_Timeline L78 | 3 |
| Ch8 | The Topic of Pants | Gods_and_Churches L10, L19; Open_Questions L10, L19; Book_12_Timeline L19; Outworlders L100; Jason_Asano L100, L100-104; 00_Peoples_Overview L100-102, L103 | 10 |
| Ch9 | Butchery | Minor_Cast_Books_7-9 L14; Book_12_Timeline L16 | 2 |
| Ch10 | Just Some Guy | Book_12_Timeline L14, L74; Spoiler_Management L14-17; 00_Cosmology_Overview L17-22; Confluences L88, L91; 01_World_Primer L91; 00_Magic_Overview L91; Anna_Tilden L94 | 9 |
| Ch11 | On a Whim | Marla L6; Book_12_Timeline L6; Spirit_Vault_and_Astral_Kingdom L46, L110 | 4 |
| Ch12 | Mandatory Team Activity | Zara_Rimaros L3, L10, L17-20, L20; Book_12_Timeline L3, L20; NPC_Rosters_by_Era L3, L75; Storm_Kingdom_Culture L17, L19; Rimaros L19; Jason_Asano L20; Orin_Pensinata L61; Neil_Davone L75 … | 16 |
| Ch13 | Try Not to Bring Down Civilisation | Gods_and_Churches L5, L67; Spirit_Vault_and_Astral_Kingdom L34; Book_12_Timeline L36, L73; Master_Timeline L36; Era_Selection L36; Open_Questions L36 | 8 |
| Ch14 | We Have Forever | Book_12_Timeline L11; 01_World_Primer L19; Travis_Noble L61-63 | 3 |
| Ch15 | Like an Adventurer | Book_12_Timeline L3, L47, L64; Hannah_and_Claire_Adeah L6; Rick_Geller L6; Keith_Geller L7; Neil_Davone L8; Nik_Asano L8, L45-47; Sigrid_Freyn L8, L8-10, L10; Valdis_Volaire L8, L9 … | 17 |
| Ch16 | People Think You’re Blowing Up Cities | Yaresh_Culture L8; Allayeth L8; Charist L8; Open_Questions L8; Valdis_Volaire L11; Book_12_Timeline L11, L85; Jonah_Geller L83 | 8 |
| Ch17 | We Need to Put a Stop to It | Book_12_Timeline L19; Valdis_Volaire L55-73, L56 | 3 |
| Ch18 | A Lunatic’s Nightmare | Book_12_Timeline L6, L16, L37, L45, L70 | 5 |
| Ch19 | When People See My Powers | Book_12_Timeline L6, L9, L58, L61, L73, L81 | 6 |
| Ch20 | Listening For Whispers | Sigrid_Freyn L9; Book_12_Timeline L42, L85 | 3 |
| Ch21 | Defier | Farrah_Hurin L43-46; Glossary L43-46; Book_12_Timeline L61; Master_Timeline L61; Open_Questions L61; Yaresh_Culture L79 | 6 |
| Ch22 | Vast Cosmic Power Types | Book_12_Timeline L27, L56; Master_Timeline L27; Anna_Tilden L73-74 | 4 |
| Ch23 | Objectives | Alchemy_Artifice_and_Magical_Materials L25; Book_12_Timeline L25; Danielle_Geller L79; Tone_and_Voice L79 | 4 |
| Ch24 | The Protection of a Dictator | 01_World_Primer L6; Book_12_Timeline L13 | 2 |
| Ch25 | You Want Your Adventurers Happy | Book_12_Timeline L3, L5, L63, L66; Danielle_Geller L7 | 5 |
| Ch26 | Making Things Worse | Dragon_Lands L5, L5-6, L6, L7, L9, L10-11 …; Book_12_Timeline L5, L16, L68; Draconians L5-6; Open_Questions L19; Minor_Cast_Books_10-13 L19-36; Danielle_Geller L54; Anna_Tilden L76; Gods_and_Churches L80 | 18 |
| Ch27 | Sometimes We Need Scars | Book_12_Timeline L12, L19, L45; Alchemy_Artifice_and_Magical_Materials L19; Astral_Spaces_Zones_and_Surges L19; Greenstone L44; Elspeth_Arella L45 | 7 |
| Ch28 | That’s What Adventurers Do | Book_12_Timeline L3, L41, L76 | 3 |
| Ch29 | A Matter of Mindset | Greenstone L38, L59-60; Open_Questions L38; Book_12_Timeline L40, L65; 00_Places_Overview L59; Boko L60, L60-61, L61, L65, L73 | 11 |
| Ch30 | Posturing Children | Ustei L9; Open_Questions L9; Boko L71; Li_Li_Mei L71-74, L80; Book_12_Timeline L80 | 6 |
| Ch31 | This Is Not a Cliff | Book_12_Timeline L3, L7, L11, L62, L97; Li_Li_Mei L3-12; Boko L34 | 7 |
| Ch32 | Cook the Crap Out of Some Toast | Book_12_Timeline L8; Boko L15-29, L91; Li_Li_Mei L18 | 4 |
| Ch33 | The Benevolence of a Nightmare God | 01_World_Primer L3; Greenstone L3; Boko L3, L3-4, L7; Era_Selection L3; 00_Places_Overview L3-9; Book_12_Timeline L4, L16, L55; Astral_Kings_and_Messengers L51-55; Jamis_Fran_Muskar L51-55 | 12 |
| Ch34 | Pretext | Book_12_Timeline L35, L57; Estercost_Culture L64 | 3 |
| Ch35 | Eternity Awaits Us | Book_12_Timeline L6, L8, L11, L66, L84, L88 | 6 |
| Ch36 | A Time to Slumber | Book_12_Timeline L3; Boko L3-5; Open_Questions L51 | 3 |
| Ch37 | I Know You Can't Control Yourself Any Longer | Book_12_Timeline L36, L128; Badges_and_Guild_Membership L128; Adventure_Society L128-131 | 4 |
| Ch38 | Truly Outrageous Things | Hornis L49; Book_12_Timeline L61 | 2 |
| Ch39 | A Framework For Leadership | Nik_Asano L3, L15, L30-35, L31; Boko L37, L40, L61, L80, L80-91, L85-89 …; Artefact_Site_One L47; Open_Questions L47; 00_Places_Overview L61; Spirit_Vault_and_Astral_Kingdom L61, L61-65; Book_12_Timeline L61 | 17 |
| Ch40 | It’s More Complicated Than That | Book_12_Timeline L5, L6; Anna_Tilden L20; Ketevan_Arziani L52 | 4 |
| Ch41 | A Long Few Days | Book_12_Timeline L3, L7, L42, L45, L61; Ketevan_Arziani L3-14; Saint-Etienne L27 | 7 |
| Ch42 | A Thing That Makes the Car Work | Book_12_Timeline L4, L21, L65, L70, L72, L82; Anna_Tilden L99, L100, L104 | 9 |
| Ch43 | A Long Time Coming | Open_Questions L46, L47; Nik_Asano L46-50; Estercost_Culture L47; Book_12_Timeline L62, L64; Badges_and_Guild_Membership L62, L64; Guilds_and_Houses L64, L64-68; Vitesse L64 | 11 |
| Ch44 | A Big Juicy Hole | Book_12_Timeline L4, L20, L62; Vitesse L13, L112; Badges_and_Guild_Membership L20; Guilds_and_Houses L26-30; Belinda_Callahan L34; Adventure_Society L98; Minor_Cast_Books_10-13 L112 | 10 |
| Ch45 | A Sense of Responsibility | Book_12_Timeline L3, L55, L62; Badges_and_Guild_Membership L3, L8, L14; Guilds_and_Houses L14; Minor_Cast_Books_10-13 L64; Roland_Remore L97; Rufus_Remore L97 | 10 |
| Ch46 | Trouble Always Knows Where to Find Me | Book_12_Timeline L3, L15, L105; Glossary L54; Gods_and_Churches L89 | 5 |
| Ch47 | Tactical Playbook | Monsters L3; Book_12_Timeline L4 | 2 |
| Ch48 | I Don’t Blow Up Cities on Purpose | Estercost_Culture L3, L22, L53; Cyrion L3, L4, L4-5, L22, L53; Book_12_Timeline L3, L5; Glossary L5; Li_Li_Mei L26, L33; Cloud_Constructs_and_Palaces L26; Law_and_Indenture L53; Open_Questions L53 | 16 |
| Ch49 | Following Through on Bad Ideas | Estercost_Culture L3; Storm_Kingdom_Culture L3; Book_12_Timeline L3; Minor_Cast_Books_10-13 L3-5; Orin_Pensinata L5; Zara_Rimaros L7; Kurdansk_Culture L77; Kurdansk L77 | 8 |
| Ch50 | Heavily Compromised Baked Goods | Estercost_Culture L3; Minor_Cast_Books_10-13 L3, L43-52, L120-126; Glossary L3; Book_12_Timeline L15, L28, L43; Law_and_Indenture L28; Era_Selection L28; Plot_Hooks L28; Open_Questions L28 … | 20 |
| Ch51 | The Line Between Mortal and Immortal | Book_12_Timeline L3; Estercost_Culture L13; Law_and_Indenture L13; Cyrion L13; Plot_Hooks L13; Open_Questions L13 | 6 |
| Ch52 | A Petty Tyranny | Book_12_Timeline L3, L6, L8, L35, L44, L48; Sadi_Andali L35-37, L36-41, L41, L74; Law_and_Indenture L35-41; 00_Places_Overview L35-41 | 12 |
| Ch53 | Reason Eighty-Seven | Cyrion L3; Book_12_Timeline L5, L24, L32, L57; Sadi_Andali L7; Daily_Life L32; Economy_and_Money L32; Plot_Hooks L57; Estercost_Culture L60; Minor_Cast_Books_1-3 L61 … | 13 |
| Ch54 | Having Strangers Come Along | Book_12_Timeline L16, L29; Glossary L29; Nik_Asano L33-34 | 4 |
| Ch55 | Take Things Slow | Book_12_Timeline L21, L90 | 2 |
| Ch56 | The End of What Can Be Productively Achieved Here | Artefact_Site_One L3-4, L124; Open_Questions L3-4; 01_World_Primer L4; Book_12_Timeline L117; Magic_Society_and_Associations L119; Lorelei_Grantham L119 | 7 |
| Ch57 | Someone Got Sucked Off | 00_Cosmology_Overview L3; 00_Astral_Overview L3; Jota_Withers L3, L7-12, L14; Book_12_Timeline L3, L7, L22, L24, L36, L58; Era_Selection L3; NPC_Rosters_by_Era L3; Plot_Hooks L12 | 14 |
| Ch58 | A City With No Dawn | Gabrielle_Pellin L41; Book_12_Timeline L41; Name_Index L41; Emi_Evans_Asano L49 | 4 |
| Ch59 | A Clark Kent Problem | Book_12_Timeline L5, L17, L24, L39, L60, L66 …; Master_Timeline L5; Glossary L5; Essence_Catalogue L9 | 12 |
| Ch60 | God-King | Book_12_Timeline L6, L10, L19, L33, L62, L93 | 6 |
| Ch61 | Jason’s Arrival Inevitably Caused a Massive Problem | Book_12_Timeline L3, L17, L18, L29, L55, L105 …; Artefact_Site_One L16, L17, L18, L21, L22, L25 …; Lenora_Coleman L16, L22, L25; 00_Earth_Overview L17, L21; 00_Places_Overview L21 | 20 |
| Ch62 | It Sets a Tone | Book_12_Timeline L3, L4, L51, L98, L101, L117; Leonids L4-9; Gary L4-9; Taika L4-9; Lenora_Coleman L28; Artefact_Site_One L45, L53 | 12 |
| Ch63 | We Already Know Who You Are | Book_12_Timeline L3, L15, L16, L42, L61, L79 …; 01_World_Primer L7; 00_Cosmology_Overview L7; Jota_Withers L16-19; Noriko_Asano L19, L30; Yumi_Asano L19; Plot_Hooks L19; Minor_Cast_Books_10-13 L43-53 | 15 |
| Ch64 | Good Luck in Your Battle | Minor_Cast_Books_10-13 L12; Artefact_Site_One L21, L22-24; Book_12_Timeline L21, L48, L60, L74, L87, L93 …; Jota_Withers L76-79 | 13 |
| Ch65 | Second Chance to Make a First Impression | Minor_Cast_Books_10-13 L4; Book_12_Timeline L11, L53, L55 | 4 |
| Ch66 | The Right Move | Book_12_Timeline L5, L13, L34, L53, L62, L63 …; Dimensional_Storage_and_Portals L6; Hegemons_Will_and_Dominion L63-66, L67 | 12 |
| Ch67 | A Lot of Things to Do | Book_12_Timeline L5, L19, L22, L30, L42, L51 …; Astral_Kings_and_Messengers L23; Artefact_Site_One L44-47; Master_Timeline L65, L113; Open_Questions L65, L113; Emi_Evans_Asano L146-149, L149; Jason_Power_Set_Reference L153-155, L157-160, L162-167, L168-169, L170-192, L175 …; Ranks_and_Advancement L154, L154-155, L155 … | 99 |

### Book 13

| Chapter | Title | Cited by (lines) | Rows |
|---|---|---|---|
| Ch950 | A Person the Other Used to Know | Erika_Asano L1-14; Emi_Evans_Asano L27; Amy_Asano L29; Kaito_Asano L29, L33; Master_Timeline L29; Book_13_Timeline L41; Artefact_Site_One L45; Minor_Cast_Books_4-6 L47 | 9 |
| Ch951 | Messy but Delicious | Nik_Asano L4-11, L7, L11; Dimensional_Storage_and_Portals L25; Book_12_Timeline L50; Book_13_Timeline L50; Master_Timeline L50; Era_Selection L50; Open_Questions L50 | 9 |
| Ch952 | All Your Well-Learned Politesse | Book_13_Timeline L35 | 1 |
| Ch953 | Perfect Humanoid Specimens | Book_13_Timeline L3; Anna_Tilden L9; Sigrid_Freyn L39; Chloe_Baudrillard L84; Emi_Evans_Asano L84 | 5 |
| Ch954 | Misgivings | Earth_Powers L3-6; Astral_Kings_and_Messengers L4; Boris_Ket_Lundi L4, L5-6, L7-12, L9, L20; 00_Earth_Overview L9; Artefact_Site_One L17; Book_13_Timeline L17, L20; Dawn L19 | 12 |
| Ch955 | The Unadulterated Jason | Book_13_Timeline L63 | 1 |
| Ch956 | Emergent Situation | Zara_Rimaros L3, L40, L41; Minor_Cast_Books_4-6 L23; Emi_Evans_Asano L26, L56-58; Book_13_Timeline L41 | 7 |
| Ch957 | When the Screaming Began | Book_13_Timeline L32 | 1 |
| Ch958 | A Lot Harder Than Anticipated | Familiars_Summons_and_Conjurations L25; Familiars L25; Book_13_Timeline L25; Hannah_and_Claire_Adeah L39, L61; Sigrid_Freyn L39; Glossary L39, L68; Humphrey_Geller L48; Tone_and_Voice L48 … | 12 |
| Ch959 | Without Consequences | Lorelei_Grantham L3; NPC_Rosters_by_Era L3, L60; Audrey_Blaine L50, L60; Book_13_Timeline L59 | 6 |
| Ch960 | What It Will Do to Itself | Spirit_Vault_and_Astral_Kingdom L3; Emi_Evans_Asano L3-5; Casselton_and_Asano_Village L14; Glossary L14-16; Li_Li_Mei L16; Book_13_Timeline L16, L23 | 7 |
| Ch961 | The Scary Demigod Side | Book_13_Timeline L3, L6, L58; Natalie_Park L8; NPC_Rosters_by_Era L8; Minor_Cast_Books_10-13 L59; Glossary L73 | 7 |
| Ch962 | I Know What You Are | Book_13_Timeline L5, L6, L44, L62 | 4 |
| Ch963 | Minimum Collateral Damage | Hannah_and_Claire_Adeah L24; Glossary L24; Book_13_Timeline L56, L96; Gary L63-68 | 5 |
| Ch964 | Expanding His Influence | NPC_Rosters_by_Era L3; Marie_Finnegan L3-6, L36; Book_13_Timeline L9; Master_Timeline L41 | 5 |
| Ch965 | This Is Kind of How Team Biscuit Operates | Book_13_Timeline L3, L42, L50, L71; Zara_Rimaros L86 | 5 |
| Ch966 | A Cultural Experience | Book_13_Timeline L3, L4, L41, L55; Nik_Asano L71 | 5 |
| Ch967 | What I Present to the World | Book_13_Timeline L3, L10, L32; Minor_Cast_Books_10-13 L18-57 | 4 |
| Ch968 | A Brief but Firm Reminder | Book_13_Timeline L4; Adrien_Barbou L34-38, L45-54, L47-54, L54 | 5 |
| Ch969 | Good Lord | Book_13_Timeline L3; Zara_Rimaros L56-63; Natalie_Park L88 | 3 |
| Ch970 | The Wisdom These Situations Demand | Book_13_Timeline L3, L29; Simon_McKean L38; Natalie_Park L52 | 4 |
| Ch971 | All the Fuel It Needed | NPC_Rosters_by_Era L3, L49; Vincent_Baudrillard L3-28, L50, L52, L55, L56; Emi_Evans_Asano L30, L49; Ian_Evans L49; Book_13_Timeline L66 | 11 |
| Ch972 | Little Umbrellas | Book_13_Timeline L51; Master_Timeline L51; Open_Questions L51; Emi_Evans_Asano L78, L78-82 | 5 |
| Ch973 | A Cruelty or a Mercy | Book_13_Timeline L24; Marie_Finnegan L49 | 2 |
| Ch974 | Most Practical Purposes | Natalie_Park L31; Book_13_Timeline L78 | 2 |
| Ch975 | Your Terms Are Acceptable | Book_13_Timeline L3; Earth_Powers L8, L19-24; Plot_Hooks L19-24; Marie_Finnegan L22, L24 | 6 |
| Ch976 | How Much Punishment They Could Live Through | Book_13_Timeline L5, L63, L80 | 3 |
| Ch977 | Getting Complicated Fast | Book_13_Timeline L126 | 1 |
| Ch978 | Implications For Your Work | Book_13_Timeline L3, L13, L21 | 3 |
| Ch979 | Unequivocally My Thing | Book_13_Timeline L3, L64, L76; Emi_Evans_Asano L7, L17, L59; Marie_Finnegan L64, L72 | 8 |
| Ch980 | The Only Cure is Death | Emi_Evans_Asano L73-77; Afflictions_Boons_and_Damage L93; Book_13_Timeline L93 | 3 |
| Ch981 | What Forever Means | Book_13_Timeline L3, L5, L7, L11; Umber L37, L62-64 | 6 |
| Ch982 | The Stuff of Faith and Madness | Book_13_Timeline L4; Earth_Powers L30; Anna_Tilden L30; Holly_Macrossan L30; NPC_Rosters_by_Era L30 | 5 |
| Ch983 | Something Worse | Book_13_Timeline L3, L15, L24, L84, L92 | 5 |
| Ch984 | What Slumbers Under the Mountain | Book_13_Timeline L3, L12, L62; Marie_Finnegan L34 | 4 |
| Ch985 | Better Natures | Book_13_Timeline L3; Marie_Finnegan L32-102 | 2 |
| Ch986 | The Deaths We Failed to Prevent | Book_13_Timeline L3, L6, L27 | 3 |
| Ch987 | Consistent Agent of Chaos | Audrey_Blaine L10; Book_13_Timeline L16, L37, L63; Open_Questions L63 | 5 |
| Ch988 | If You Can’t Keep Up | Era_Selection L26; Plot_Hooks L26; Open_Questions L26; Book_13_Timeline L40; Holly_Macrossan L52-54 | 5 |
| Ch989 | A Man Fought Monsters | Book_13_Timeline L3, L50, L68; Earth_Powers L48; NPC_Rosters_by_Era L48 | 5 |
| Ch990 | Monstrous on the Inside | Book_13_Timeline L3, L21, L38, L65, L86 | 5 |
| Ch991 | This Offer Kind of Sucks | Book_13_Timeline L3 | 1 |
| Ch992 | Battle of the Plants | Book_13_Timeline L62; Audrey_Blaine L116; Lorelei_Grantham L122-124 | 3 |
| Ch993 | True to Yourself | Book_13_Timeline L3, L109 | 2 |
| Ch994 | Not Open to Outside Consultation | Earth_Powers L39; Holly_Macrossan L39; Book_13_Timeline L51; Essence_Catalogue L78 | 4 |
| Ch995 | Symposium | Miriam_Vance L14; Travis_Noble L14; Glossary L14; Book_13_Timeline L57, L69, L76; Minor_Cast_Books_4-6 L64; Natalie_Park L69; Master_Timeline L69; Open_Questions L69 | 10 |
| Ch996 | The More I Listen, The More I Hear | NPC_Rosters_by_Era L3; Nik_Asano L5-9, L181; Book_13_Timeline L71 | 4 |
| Ch997 | The Man Who Fought the Monsters | Emi_Evans_Asano L11; Nik_Asano L11, L23; Sophie_Wexler L28-31; Clive_Standish L32; NPC_Rosters_by_Era L32; Neil_Davone L37-38; Book_13_Timeline L41 | 8 |
| Ch998 | Sitting on a Volcano | Emi_Evans_Asano L3-4, L4; Nik_Asano L4; Book_13_Timeline L4, L99; Master_Timeline L4; Natalie_Park L105; Plot_Hooks L105; Audrey_Blaine L109 | 9 |
| Ch999 | An Interesting Message | Thalia_Mercer L3; Book_13_Timeline L3 | 2 |
| Ch1000 | Cosmic Tyrant Warlord Cult Leader | Boris_Ket_Lundi L3-7; Book_13_Timeline L37; Simon_McKean L104 | 3 |
| Ch1001 | It’s All Quite Australian | Book_13_Timeline L6; Master_Timeline L6; Rufus_Remore L8; NPC_Rosters_by_Era L8; Earth_Magic L8-9, L9; Monster_Cores_and_Training L9, L10; Carlos_Quilido L9 | 9 |
| Ch1002 | The One Who Gets to Decide | Book_13_Timeline L3, L68; Yumi_Asano L23, L31; Simon_McKean L40; Open_Questions L64, L69; Master_Timeline L69 | 8 |
| Ch1003 | Stare Down the Devil | Minor_Cast_Books_10-13 L3; Nik_Asano L67-72, L72; Book_13_Timeline L91; Master_Timeline L91 | 5 |
| Ch1004 | Scheduling Your Callous Dumping | Book_13_Timeline L18; Zara_Rimaros L44-52 | 2 |
| Ch1005 | A Distant God | Book_13_Timeline L3, L10, L80 | 3 |
| Ch1006 | What You Gave Us Was Never Freedom | Book_13_Timeline L34; Plot_Hooks L59 | 2 |
| Ch1007 | That Will Keep Them Dead | Book_13_Timeline L3, L6, L13, L41; Tone_and_Voice L22; Itsuki_Tiwari L23; Nigel_Thornton L23, L45; Nik_Asano L48; Saint-Etienne L62 | 10 |
| Ch1008 | A Sufficient Spectacle | Book_13_Timeline L10; Saint-Etienne L31-33 | 2 |
| Ch1009 | Kung-Fu Wizard is Not a Verb | Book_13_Timeline L4 | 1 |
| Ch1010 | Dangerously Exposing Myself | Book_13_Timeline L3, L5, L61, L69 | 4 |
| Ch1011 | Join Me, and Together We Could Rule the World! | Book_13_Timeline L18, L25, L44, L69; Belinda_Callahan L23; Estella_Warnock L23; NPC_Rosters_by_Era L23; Minor_Cast_Books_10-13 L41; Nik_Asano L63 | 9 |
| Ch1012 | We Have to Kill Clive | Book_13_Timeline L64 | 1 |
| Ch1013 | Something Jasony | Book_13_Timeline L34 | 1 |
| Ch1014 | A Satisfying Day | Book_13_Timeline L3, L17, L34, L72, L91 | 5 |
| Ch1015 | A Fight She’s Already Won | Li_Li_Mei L40; Nik_Asano L48; Book_13_Timeline L49; Master_Timeline L49; 01_World_Primer L78; Jason_Asano L78 | 6 |
| Ch1016 | Worse Things | Hassan_Dukhtar L3, L23-31, L31; Book_13_Timeline L3, L21, L107, L119; Jason_Asano L21; NPC_Rosters_by_Era L23; Rufus_Remore L23-27; Farrah_Hurin L48; Gabrielle_Pellin L68, L74; Name_Index L68 … | 15 |
| Ch1017 | A Room Full of Hands | Book_13_Timeline L5; 00_Cosmology_Overview L6-8; Spoiler_Management L6-8, L14-24; Open_Questions L11, L15, L17-19, L18; Plot_Hooks L14; Jason_Asano L14-15; Great_Astral_Beings L14-16; Gods_and_Churches L14-20, L14-24 … | 28 |
| Ch1018 | I Don’t Need Hope | Book_13_Timeline L52 | 1 |
| Ch1019 | Blatantly Ignoring Laws | Book_13_Timeline L3 | 1 |
| Ch1020 | Adventurer | Book_13_Timeline L4; Minor_Cast_Books_10-13 L85; Glossary L85-91; Artefact_Site_One L95; Open_Questions L95 | 5 |
| Ch1021 | The One Way I Know to Kill a God | Book_13_Timeline L4 | 1 |
| Ch1022 | While We Have the Chance | Book_13_Timeline L3; Rimaros L20; Thadwick_Mercer L35, L62; Dimensional_Storage_and_Portals L35 | 5 |
| Ch1023 | Broken What Matters Most | Book_13_Timeline L3, L12; Open_Questions L12, L103; Artefact_Site_One L103; Gods_and_Churches L139; Gabrielle_Pellin L139; Knowledge L139 | 8 |
| Ch1024 | The Next Time We Meet | Book_13_Timeline L3, L82; Artefact_Site_One L57; Helsveth L75-81; Umber L100-104, L118, L118-127, L138; Name_Index L101; NPC_Rosters_by_Era L102; Familiars L127-130; 01_World_Primer L153 … | 15 |

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

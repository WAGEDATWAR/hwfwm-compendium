import io, os, sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
BASE = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".."))
p = os.path.join(BASE, "01_World_Primer.md")
s = open(p, encoding="utf-8").read()
E = [
("Status: Draft (audited claim by claim against the book text, chapter notes and wiki; claims found in none of the three were removed; remaining unsourced items are listed in TODO_Verification.md)",
 "Status: Draft (verification pass 2026-10-22: claims checked against the book text in `src/Source_Text/`; specific facts carry \"Book N, ChX LY\" references, and the fuller cites live in the topic documents this primer points to; wiki-only items are marked (wiki))"),
("Pallimustus is an alternate Earth whose continents are similar but not identical. Key differences: Africa is separate from Eurasia; a large landmass in Southeast Asia pushes into Australia and consumes New Zealand; Iberia and Arabia are missing, so the Mediterranean and Indian Ocean join through the **Gramid Passage**; Sri Lanka is huge (Pranay). It has two moons. The year has twelve months of thirty days plus five festival days (solstices, equinoxes and new year), and the year begins in spring; the week has six days. Time units (hours, minutes) match Earth's.",
 "Pallimustus is an alternate Earth whose continents are similar but not identical. Key differences: Africa is separate from Eurasia; a large landmass in Southeast Asia pushes into Australia and consumes New Zealand; Iberia and Arabia are missing; Sri Lanka is huge (Book 1, Ch1 L65) and is called Pranay (Book 2, Ch34 L58). The Mediterranean equivalent is the **Gramid Passage**, which joins directly to the Indian Ocean (Book 6, Ch47 L703). It has two moons (Book 1, Ch1 L23). The year has twelve months of thirty days plus five extra days for the solstices, equinoxes and new year, and the year begins in spring (Book 1, Ch22 L19); the week has six days (Book 6, Ch10 L41). Time units (hours, minutes) match Earth's (Book 1, Ch22 L20)."),
("cyclical events (roughly every ten years) when", "cyclical events (every ten years, Book 1, Ch31 L71) when"),
("Animals include **heidels** (two-headed, scaled, horned draught animals) in place of horses.",
 "Animals include **heidels** (horse-sized, scaled, two-headed and horned, Book 1, Ch17 L106) in place of horses."),
("Greenstone is low-magic (mid-iron density); Vitesse and Rimaros are high-magic; astral spaces and surges can be higher still.",
 "Greenstone is low-magic: \"mid-iron\" density, which Clive calls very low (Book 3, Ch34 L60). The wiki calls Vitesse much denser (wiki; no book figure), and the place files give what the books say about Rimaros and others. Astral spaces and surges can be higher still."),
("Earth is an older version of the same template with a thicker dimensional membrane, strengthened by the World-Phoenix, so it has little ambient magic.",
 "Earth is the same template with a more rigid dimensional membrane, which the World-Phoenix reinforced billions of years ago, so it has less ambient magic (Book 4, Ch68 L79, L97; Book 4, Ch2 L11)."),
("It uses \"category\" for ranks (0-5), calls holy damage \"luminous\", and calls quintessence \"affinity gems\".",
 "It names ranks by category, matched to the spirit-coin colour: category one is iron, two bronze, and a silver-ranker is category three (Book 4, Ch21 L31-33; Book 4, Ch31 L48); it grades events by category as well (Book 4, Ch5 L13-16). It says \"luminous\" for holy (Book 4, Ch19 L36) and \"affinity gems\" for quintessence (Book 4, Ch23 L26)."),
("A link made roughly five hundred years ago (by an Earth person who went to Pallimustus, struck a bargain with a god and returned) siphons magic from Pallimustus into Earth. It delayed Pallimustus's monster surge and slowly built magic on Earth.",
 "A link made roughly five hundred years ago siphons magic from Pallimustus into Earth: an Earth outworlder who had joined the fake Purity's church returned home with magic Knowledge had bargained from the messengers (Book 13, Ch1017 L19-21). The siphon delays Pallimustus's monster surges, and the delay makes the eventual breakthrough more dangerous (Book 4, Ch68 L131-135)."),
("In the early books the outcome for a combination is fixed and recorded by the Magic Society; later, after the Cosmic Throne is repaired, outcomes vary.",
 "In the early books the outcome for a combination is fixed (Book 1, Ch15; Book 1, Ch19 L30) and recorded by the Magic Society; by Book 12 the fixed combinations \"are starting to add variety\" (Book 12, Ch10 L91)."),
("A stone's rarity (one to five stars) and theme steer what it awakens;",
 "The Magic Society grades a stone one to five stars by how often it appears (see `03_Magic_and_Adventuring/Awakening_Stones.md`); the stone's theme steers what it awakens;"),
("(Jason's cooking is a recurring feature).",
 "(Jason's cooking is a recurring feature). A recovery potion tasting of strawberry schnapps appears in Book 1, Ch6 L50, and crystal wash in Book 1, Ch32 L52."),
("| Iron | Category 1 | All four essence slots filled. Body begins turning magical; can live on spirit coins; sense auras |",
 "| Iron | Category 1 | Four essences absorbed (Book 1, Ch15 L100). Digestion changes (Book 2, Ch34 L73); can live on spirit coins; sense auras |"),
("| Silver | Category 3 | A killing blow no longer kills; flight by aura becomes possible; the usual ceiling for core-users |",
 "| Silver | Category 3 | Can fight through blows that would be lethal to a bronze-ranker (Book 5, Ch1 L38); some abilities allow flight at silver (Book 2, Ch9 L30-31); the usual ceiling for core-users |"),
("| Gold | Category 4 | No need to breathe; centuries-long life |",
 "| Gold | Category 4 | No need to breathe (Book 2, Ch34 L73); centuries-long life (Book 1, Ch22 L58) |"),
("Some coins in Jason's hands bear a thumbs-up image of his face with the words \"PRODUCT OF JASON / G'DAY MATE\".",
 "Coins from Jason bear his face and the words \"PRODUCT OF JASON / G'DAY, MATE!\" (Book 1, Ch2 L50-53)."),
("100 lesser coins make one iron coin; each higher rank is ten times the last,",
 "100 lesser coins make one iron coin; each higher rank is ten times the last (Book 1, Ch36 L72; Book 1, Ch61 L65),"),
("Greenstone uses magic trams and public pumps;", "Greenstone has loop-terminal transit (Book 1, Ch45 L4);"),
("the Magic Society's **water link** (pools) and Farrah and Travis's **sky link** (relay-tower telephony).",
 "the Magic Society's **water link** (Book 2, Ch6 L5) and the **sky link** communication tablets, whose inventor appears in Book 12, Ch14 L19 (the Sky Link Company, Book 12, Ch56 L4)."),
("Each **nature** (race) has six inherent **racial gifts**", "Each **nature** (race) has exactly six inherent **racial gifts** (Book 1, Ch15 L65)"),
("not a natural race, but the children of two outworlders;", "not a natural race: two outworlders who have a child produce a celestine (Book 5, Ch44 L72);"),
("**valash** (transformed Earth humans), **Lehenik** (Jason's soul-realm people).",
 "**valash** (humans turned into them by transformation zones, Book 9, Ch45 L57), **lehenik** (Nik's kind, from a word for \"first\", Book 11, Ch23 L42)."),
("Interstice** is the oldest city-world at the cosmic centre, entered freely only by diamond-rankers.",
 "Interstice** is the oldest and largest city-world, with administrators and no rulers, where great astral beings do business in physical reality (Book 3, Ch69 L219-222)."),
("Clive explains the cosmos as **dumpling soup**:", "Clive explains the cosmos as **dumpling soup** (Book 1, Ch69 L85):"),
("They once sat under a **Cosmic Throne** and then sundered it; Jason repairs it in Book 11. **(Later: Book 11)**",
 "They once sat under a **Cosmic Throne** and then sundered it. In Book 11 the throne is left empty as a neutral arbiter (Book 11, Ch65 L8), and in Book 12 Jason learns it \"could never be restored to what it was\", with an echo of him imprinted on it (Book 12, Ch1 L34). **(Later: Book 11-12)**"),
("The **Red Table**: a criminal and cult network that includes blood cults.",
 "The **Red Table**: a blood cult with branches in remote areas (Book 1, Ch18 L5; Book 7, Ch55 L75)."),
("5. **Books 10-11**: the Cardinas expedition and the Death Pact; Undeath and the transformation zone; Gary's sacrifice; Jason's battle for the Cosmic Throne; Jason becomes the System.",
 "5. **Books 10-11**: the Cardinas expedition and the Death Pact; Undeath and the transformation zone; Gary's death; the aftermath of the sundered Cosmic Throne (Book 11, Ch64-65); Jason's interface becomes available to everyone with essences (Book 12, Ch1 L36)."),
("vampire war; Knowledge's plan; Jason is sealed.",
 "vampire war; Knowledge's plan (Book 13, Ch1015 L78); at the end Jason walks to the standing stones at Ascension's Gate (Book 13, Ch1024 L153)."),
("See `08_History_and_Timeline/` (to be written) for the verified master timeline.",
 "See `08_History_and_Timeline/Master_Timeline.md` and the per-book timelines for the verified chronology."),
("- **Team Biscuit** takes its name from Stash's blurted word when the team registered; Jason's biscuits are a running joke.",
 "- **Team Biscuit**: a familiar picked the team's name (Book 10, Ch47 L78; the wiki credits Stash); Jason's biscuits are a running joke (Book 1, Ch78)."),
]
bad = 0
for o, n in E:
    if o not in s:
        print("MISSING:", o[:70])
        bad += 1
        continue
    s = s.replace(o, n, 1)
open(p, "w", encoding="utf-8").write(s)
print("done, missing", bad)

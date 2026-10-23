import os
B = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", ".."))


def edit(rel, pairs):
    p = os.path.join(B, rel)
    s = open(p, encoding="utf-8").read()
    for o, n in pairs:
        assert o in s, (rel, o[:60])
        s = s.replace(o, n, 1)
    open(p, "w", encoding="utf-8").write(s)


T = "08_History_and_Timeline/Book_12_Timeline.md"
s = open(os.path.join(B, T), encoding="utf-8").read()
i = s.index("## 7. The bridge and the Earth arrival (Ch58 to Ch67)")
j = s.index("## 8. Notes on the interval")
new7 = """## 7. The bridge and the Earth arrival (Ch58 to Ch67)

The Earth chapters are the best-dated part of the book: Lenora and Jota's side of the story both give a count from the autumn-2021 departure and Jason's age (section 1).

| When | Chapters | Event |
|---|---|---|
| Sky Link island | Ch58 | Jason dines with Travis Noble and his wife Gabrielle, who is adjusting to the absence of her goddess (Book 12, Ch58 L41) |
| Days before the arrival | Ch59 | Two American officials, Darius Shepherd (Department of Supernatural Affairs) and Michael Glasser (State Department), portal to the city of Nitra in Asano clan territory, where the clan met them (Book 12, Ch59 L5, L39). Boris Ketland takes them on to Jason's hidden-business city of vampires (Book 12, Ch59 L17, L24) |
| Days before the arrival | Ch59 | They warn that a secret council of Earth's powers has made a deal to bring outsiders to remove Jason, with the United States cut out of the plan (Book 12, Ch59 L60, L66 to L72). Australia is a driving force; Russia and most of Africa are Cabal territory, Europe's vampires are an open question, China and the "True Network" are against Jason, and the GDC will stay out (Book 12, Ch59 L95, L98 to L106) |
| Days before the arrival | Ch59 | Jason asks Boris whether the council talks with the Jakaar pirates, then admits the matter is his doing (Book 12, Ch59 L115 to L117) |
| Days before the arrival | Ch60 | Jason explains the plan. A cult of the World-Phoenix paid him a visit, and the World-Phoenix owed him a favour for his stopping the Cosmic Throne from turning her back into the Boundary (Book 12, Ch60 L6, L10). The favour was to open the universe to gold-rankers while the ban on diamond-rankers stays until Jason reaches diamond, which also supplies an outside enemy (Book 12, Ch60 L19 to L20) |
| Days before the arrival | Ch60 | Anna Tilden, on the road to the city, hears Jason confirm that he engineered a situation for a demonstration of power (Book 12, Ch60 L33, L62 to L65, L79). Boris tells her that to his people Jason is an astral king, a god-king (Book 12, Ch60 L93) |
| Days before the arrival | Ch61 | On the cloud ship, Danielle Geller tells Jason that mixing friends and allies needs an org chart (Book 12, Ch61 L3 to L13). Jason and Zara talk about getting politics right on the ship's edge (Book 12, Ch61 L55 to L78) |
| Earth, the site | Ch61 | Lenora Coleman, Director of Operations for Dimensional Artefact Site One, and her deputy Barry have prepared for Jason's return for weeks (Book 12, Ch61 L17, L29). She and her predecessors oversaw a massive transformation of the site (Book 12, Ch61 L18). Anna Tilden, Rufus Remore and Taika Williams arrive at the building (Book 12, Ch61 L105 to L107) |
| Earth, the site | Ch62 | Anna, Rufus, Taika and Gary travel in a flying saucer carried by Taika in bird form (Book 12, Ch62 L4, L51). Lenora meets them at the doors, past the site's gold-rank security under Commander Higgins and Lord Willoughby, and waives the screening (Book 12, Ch62 L98, L101, L117) |
| Earth, the site | Ch63 | In Lenora's office, Anna and Rufus warn that her city will become a gold-rank battle zone; Jason will try to draw the fight into the desert (Book 12, Ch63 L3 to L5). Rufus gives Jason's arrival as "roughly three days" away (Book 12, Ch63 L15) |
| Earth, the pirates | Ch63 | Captain Jota Withers of the Jakaar fleet's dimension ship is hosted by the Asano clan of Noriko Asano, who dismisses Jason as an opportunist (Book 12, Ch63 L16 to L19, L41). His first officer Natala Spiro warns that Kreegle is stirring the crew (Book 12, Ch63 L42 to L48). Jota suspects Jason is more than he was described, citing a link to the former First Sister (Book 12, Ch63 L61 to L63) |
| Aboard the cloud ship | Ch63 | Jason tells Farrah he has prepared for this fight "for twenty years" (Book 12, Ch63 L79). She answers "We already know who you are" (Book 12, Ch63 L86) |
| Arrival day | Ch64 | The artefact city has been mostly evacuated of its nine thousand or so workers, and a security force stands about half a kilometre back from the site, with Rufus and Taika free to roam (Book 12, Ch64 L21, L48). Jota says Admiral Jakaar likes results (Book 12, Ch64 L96) |
| Arrival day | Ch64 | The standing stones light up and Jason's cloud ship appears from a sphere of light some four hundred and fifty metres across (Book 12, Ch64 L60 to L66). A second, militaristic ship, about eighty metres long against Jason's three hundred and more, follows and Jota and Natala fly out to meet Jason (Book 12, Ch64 L74 to L75) |
| Arrival day | Ch64 | Jason introduces himself and tells Jota he will not fight with them, and that their ship is forfeit; Jota says his crew has twenty-seven gold-rankers and that a mutiny is about to start (Book 12, Ch64 L87, L93, L103, L108 to L110) |
| The pirate battle | Ch65 | Jason, not physically present, stands alone against the crew, dims the sun by looking at it, and fights with his shadows, afflictions and the Hegemony aura (Book 12, Ch65 L11 to L12, L24 to L26, L31, L49 to L50). A harpoon with the Inescapable condition catches him; Belinda's tether then binds the pirates and Jason leaves an empty cloak (Book 12, Ch65 L53, L55) |
| The pirate battle | Ch66 | Team Biscuit and Farrah arrive in stage two of Jason's plan, using Sophie's Eternal Moment, Belinda's Force Tether and the attacks of Clive and Farrah (Book 12, Ch66 L5 to L11). Neil heals the hole in Jason's torso (Book 12, Ch66 L13 to L17) |
| The pirate battle | Ch66 | Jason drives the pirates apart with his sword and Humphrey's Unstoppable Force (Book 12, Ch66 L34 to L41). He changes the plan from killing them to taking them alive, to show Earth he is not the man who left (Book 12, Ch66 L53 to L55). Someone fears the display of power will worsen a religious turn (Book 12, Ch66 L62) |
| The pirate battle | Ch66 | Jason absorbs the Holy afflictions of Elenore Boatwell (Book 12, Ch66 L63 to L66). Jota and Natala withdraw from the space over the standing stones before combat (Book 12, Ch66 L76). Jason's ship is a temple (Book 12, Ch66 L82). Neil is told to put down the drone (Book 12, Ch66 L87) |
| After the battle | Ch67 | The pirates are rounded up and Jason says they will go to his prison planet, which holds messenger armies that surrendered to him (Book 12, Ch67 L5, L19, L22) |
| After the battle | Ch67 | Higgins confronts Jason's companions; Jason steps through Shade into the bunker and meets Lenora and Anna (Book 12, Ch67 L30, L51, L55 to L58). He says the people who vanished seventeen years ago are to be brought home and presses his point with his aura (Book 12, Ch67 L64 to L66, L78 to L83) |
| After the battle | Ch67 | Jason meets Gary Sharpton, the young lion man named for his friend, and asks him to come and work on the dimension ship (Book 12, Ch67 L90 to L102) |
| After the battle | Ch67 | Jota and Natala, held on Jason's cloud ship, are told Jason is an astral nexus and that a system window reads "System Administrator" (Book 12, Ch67 L107, L119, L132 to L137). Jota says Jason was born on Earth forty-four years ago (Book 12, Ch67 L113) |
| After the battle | Ch67 | Danielle Geller tells Jason there are many decisions waiting; he promises to return (Book 12, Ch67 L141 to L145) |
| The reunion | Ch67 | Emi, coming out of a bakery, meets Jason as he steps out of a black archway, and he greets her as "Moppet" (Book 12, Ch67 L146 to L149) |
| Appendices | after Ch67 | Appendix I is Jason's character sheet as a gold-rank prime avatar (Astral Nexus), 38 percent towards diamond (Book 12, Ch67 L153 to L155). Appendix II lists the astral nexus inherent gifts (Book 12, Ch67 L194 to L200). Appendix III lists his essence abilities at gold rank (Book 12, Ch67 L201 to L203) |

Chapters 59 to 61 and 62 overlap in time: Ch61 closes with the visitors at Lenora's door, and Ch62 opens aboard the saucer before they arrive (Book 12, Ch61 L105 to L107; Book 12, Ch62 L3).

"""
s = s[:i] + new7 + s[j:]
open(os.path.join(B, T), "w", encoding="utf-8").write(s)

edit(T, [
    ("- **On Earth**: ", "- **Since the Earthlings vanished (about seventeen years)**: Lenora speaks of the people who vanished \"seventeen years ago\" (Book 12, Ch67 L65), and Travis asks whether Earth has done weapons research \"in the last seventeen years\" (Book 12, Ch67 L42).\n- **Jason's age**: Jota says Jason was born on Earth \"forty-four years ago\" (Book 12, Ch67 L113). With the birthday on 1 April 1994 (see Master_Timeline, section 1) that puts the Earth arrival after 1 April 2038.\n- **On Earth**: "),
    ("- **The present**: the roundings above fit a Book 12 present in 2037, with Book 13 (2038) following within about a year (Open_Questions 18).\n- **The tail of the book** takes in the arrival at Earth. The year is given in Book 13 as 2038 (see `Book_13_Timeline.md`).",
     "- **The present**: the Pallimustus chapters (about fifteen years since Jason left, almost twenty since the arrival) fit late 2037 to early 2038. The Earth arrival (Ch64 to Ch67) is best placed in 2038: autumn 2021 plus seventeen years and Jason's forty-fourth year both point there, and Book 13 gives 2038 (Book 13, Ch951 L50). The time between the Pallimustus tour and the Earth arrival is not stated. See Open_Questions 18.\n- **The tail of the book** takes in the arrival at Earth; Rufus gives the arrival as \"roughly three days\" away at the briefing in Ch63 (Book 12, Ch63 L15). Book 13 follows, also in 2038 (see `Book_13_Timeline.md`)."),
])

edit("08_History_and_Timeline/Master_Timeline.md", [
    ("| 12 | Pallimustus tour and the Earth arrival | about fifteen years after Jason left (late 2030s) | \"Fifteen years\" (Book 12, Ch21 L61); \"twenty years\" since the arrival (Book 12, Ch7 L78) | `Book_12_Timeline.md` |",
     "| 12 | Pallimustus tour (late 2037 to early 2038), then the Earth arrival and the pirate battle at Dimensional Artefact Site One (2038) | about fifteen years after Jason left | \"Fifteen years\" (Book 12, Ch21 L61); \"twenty years\" since the arrival (Book 12, Ch7 L78); \"seventeen years\" since the Earthlings vanished and Jason \"born forty-four years ago\" (Book 12, Ch67 L65, L113) | `Book_12_Timeline.md` |"),
    ("| Book 12 \"now\" | \"M-count\" | about fifteen years after the departure, late 2030s; Book 13 is 2038 | Book 12, Ch21 L61; Book 13, Ch951 L50 |",
     "| Book 12 \"now\" | \"M-count\" | Pallimustus tour late 2037 to early 2038; Earth arrival 2038; Book 13 is 2038 | Book 12, Ch21 L61; Book 12, Ch67 L65, L113; Book 13, Ch951 L50 |"),
    ("- **Open - Book 12 present**: the dates imply the Book 12 events fall in late 2037 to 2038, but the book itself never gives a year before Book 13's 2038 (Book 13, Ch951 L50).",
     "- **Narrowed - Book 12 present**: the Pallimustus chapters fit late 2037 to early 2038 by their roundings, and the Earth arrival is best placed in 2038 because the book counts \"seventeen years\" from the Earthlings' vanishing (Book 12, Ch67 L65) and Jason's forty-fourth year (Book 12, Ch67 L113), with Book 13 at 2038 (Book 13, Ch951 L50). The book never states a year or the gap between the tour and the arrival."),
    ("which fits Book 2 at about M5 (April 2018) and Book 12 in late 2037 or 2038.", "which fits Book 2 at about M5 (April 2018) and the Pallimustus part of Book 12 in late 2037 or early 2038."),
])

edit("Appendices/Open_Questions.md", [
    ("18. **When is the Book 12 present?** *(Narrowed in the 2026-10-22 pass.)*", "18. **When is the Book 12 present?** *(Narrowed in the 2026-10-22 passes.)*"),
    ("All the roundings fit if Book 12 is set in 2037, with Book 13 following within about a year; the compendium uses that. Not known: the exact month.",
     "The Pallimustus chapters fit late 2037 to early 2038. The Earth arrival fits 2038 better: Lenora and Jason count \"seventeen years\" from the Earthlings' vanishing in autumn 2021 (Book 12, Ch67 L65), and Jota says Jason was born \"forty-four years ago\" (Book 12, Ch67 L113), which with a 1 April 1994 birth is April 2038 or later. The compendium uses 2037 to early 2038 for the tour and 2038 for the arrival. Not known: the exact month or the gap between the two."),
])

edit("00_Project_Structure.md", [
    ("fit a Book 12 present in 2037 and Book 13 in 2038;", "fit a Pallimustus tour in late 2037 to early 2038, with the Earth arrival and Book 13 in 2038 (\"seventeen years\" and Jason's forty-four years, Book 12, Ch67 L65, L113);"),
])
edit("TODO_Verification.md", [
    ("- (Narrowed) Book 12's present is set in 2037 by the combined roundings (Open_Questions 18); the exact month and the date of Jason's arrival on Earth are not stated.",
     "- (Narrowed) The Pallimustus tour falls in late 2037 to early 2038 and the Earth arrival in 2038 (\"seventeen years\" and \"forty-four years\", Book 12, Ch67 L65, L113; Open_Questions 18); the exact month and the gap between them are not stated."),
])
edit("TODO_Build_Plan.md", [
    ("- **1.1 Place the Book 12 closing chapters in the timeline (M).**", "- **1.1 (Done 2026-10-22) Place the Book 12 closing chapters in the timeline (M).**"),
])
edit("Appendices/Change_Log.md", [("## Pending index updates", """**Book 12 closing chapters placed in the timeline, build plan item 1.1 (2026-10-22)**
- `Book_12_Timeline.md`, section 7: replaced the four-row stub with line-cited rows for Ch58 to Ch67 (the American officials' warning and Jason's plan for a staged demonstration, the artefact site and Lenora, the Jakaar crew and the Asano clan hosting them, the arrival, the pirate battle in three stages, the aftermath, Gary Sharpton, Emi and the three appendices). Removed the "not placed until verified" note.
- Dating: added the seventeen-year count (Book 12, Ch67 L42, L65) and Jota's "forty-four years ago" (Book 12, Ch67 L113) to the time anchors. The Earth arrival is now placed in 2038 and the Pallimustus tour in late 2037 to early 2038 (previously the whole book was given as 2037). Updated Open_Questions 18, `Master_Timeline.md` (series table, month-count table, conflicts list), `00_Project_Structure.md` and `TODO_Verification.md` to match. The gap between the tour and the arrival is still not stated.

## Pending index updates""")])
print("ok")

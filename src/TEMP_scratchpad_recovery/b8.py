import os, io, sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
BASE = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".."))
OUT = os.path.join(BASE, "07_Characters", "Minor_Cast")
os.makedirs(OUT, exist_ok=True)


def grp(fn, title, lvl, vf, vt, src, rel, intro, entries):
    t = "# %s\n\nStatus: Draft (book text; facts carry a reference \"Book N, ChX LY\" to Source_Text; \"notes\" marks chapter-summary-only facts)\nSpoiler level: %s\nValid from: %s\nValid through: %s\nSources: %s\nRelated: %s\n\n## 1. Summary\n\n%s\n\n## 2. Entries\n\n" % (title, lvl, vf, vt, src, rel, intro)
    for name, facts in entries:
        t += "### %s\n\n" % name + "\n".join("- " + f for f in facts) + "\n\n"
    t += "## 3. Using this in a story\n\nThese are minor figures: give each one only the facts above. A character with more scenes belongs in its own file in `../`.\n"
    open(os.path.join(OUT, fn), "w", encoding="utf-8").write(t)
    print("wrote", fn)


grp("Minor_Cast_Books_1-3.md", "Minor Cast: Books 1-3", "1", "Book 1", "Book 12", "Books 1-3 and later mentions (chapter files)",
    "../00_Characters_Overview.md, ../Gilbert_Bertinelli.md, ../Thadwick_Mercer.md, ../Thalia_Mercer.md",
    "Recurring minor figures of the Greenstone books that have no file of their own.",
    [("Albert Bertinelli (\"Bert\")", ["A clerk at the Adventure Society who introduces himself as Albert and says his brother was Bertram, \"feel free to just call me Bert\" (Book 1, Ch37 L98); he records Jason's contracts at the jobs hall (Book 1, Ch64 L5; Book 1, Ch107 L49).",
                                      "He mentions the lumber mill owner's fergax complaint (Book 1, Ch92 L65) and later remarks on the fate of Jason's early captors (Book 3, Ch24 L60)."]),
     ("Genevieve Picot", ["Deputy director of the Adventure Society branch, an elf who looks uncharacteristically aged for a silver-ranker (Book 1, Ch98 L63; Book 6, Ch47 L369).",
                          "She meets Jason and Elspeth in a black parlour in Book 2 (Book 2, Ch59 L22)."]),
     ("Darryl Caruthers", ["A cultist who loudly demands worship in the Vane estate (\"the magic of Darryl Caruthers\", Book 1, Ch11 L73) and says \"I'm the Darryl\" (Book 1, Ch14 L18).",
                           "In Book 12 a Darryl among the Earth refugees ranked up without cores and grows naturally powerful (Book 12, Ch53 L61); the text checked does not state they are the same man."]),
     ("Beaufort Mercer", ["The Duke of Greenstone's brother (Book 1, Ch101 L9), Thalia's husband (Book 2, Ch59 L4) and Thadwick's father, who facilitated a Mercer scheme (Book 2, Ch15 L27) and raised Thadwick himself (Book 11, Ch6 L59).",
                          "Jason notes in Book 10 that the Builder cult's Beaufort shares his name but not his villainy (Book 10, Ch72 L41)."]),
     ("Dean Tuckell and Clementson", ["Dean Tuckell is an iron-rank adventurer who summons monsters at the Clementson mill for Thadwick Mercer (Book 1, Ch94 L25-58). Clementson is the mill owner, a normal-rank man (Book 1, Ch94 L16).",
                                      "Kyle Lindover, the leonid mill owner, is the victim of the fergax contract (Book 1, Ch93 L24-29)."])])

grp("Minor_Cast_Books_4-6.md", "Minor Cast: Books 4-6", "2", "Book 4", "Book 13", "Books 4-6 and later mentions (chapter files)",
    "../00_Characters_Overview.md, ../Gerling.md, ../Nigel_Thornton.md, ../Anna_Tilden.md",
    "Minor Network, government and Earth figures of the Earth books that have no file of their own.",
    [("Kylie Chen", ["A bronze-rank Network operative suited to quiet scouting rather than combat (Book 4, Ch42 L27)."]),
     ("Chen (category four)", ["An older Network category four with \"aggravating shield powers\" who goes into the Slovakia dome with Gerling and two Chinese category fours (Book 6, Ch6 L31; Book 6, Ch7 L22-23); he kills anomalies fast with beak-like finger strikes (Book 6, Ch7 L72).",
                              "Whether he is the same person as Kylie Chen is not stated (she is bronze in Book 4)."]),
     ("Gordon Truffett", ["The government representative at the negotiations with Jason, a man with no magic (Book 4, Ch36 L139-145). He takes command on site as a government figure in Book 11 (Book 11, Ch68 L476) and needs publicity in Book 13 (Book 13, Ch950 L47)."]),
     ("Emerson Cleary", ["Deputy Director of the Network and Gerling's handler, angry that Jason escaped Berlin (Book 4, Ch53 L75; Book 5, Ch46 L86; Book 5, Ch51 L8; Book 6, Ch19 L27).",
                         "Gerling says he is better than past handlers who treated him like a monster in a pit (Book 5, Ch47 L102)."]),
     ("Gladys Erstweller", ["A silver-rank (category three) Earth healer who gives her name to Jason's team (Book 4, Ch31 L48); in 2038 she treats Nanna's Alzheimer's and lectures with Neil (Book 13, Ch956 L23; Book 13, Ch995 L64)."]),
     ("Hector De Lange", ["A Belgian official of the International Committee who runs the Saint-Étienne operation (Book 4, Ch51 L10; Book 4, Ch52 L84). A different Hector appears in Book 9 among those intimidated by the royal family (Book 9, Ch16 L50)."]),
     ("Todd \"The Necromancer\" Halverson", ["A silver-ranker with 94 percent core taint and the territory claimant in the Saint-Étienne zone (Book 6, Ch39 L25-27; Book 6, Ch38 L76-81)."])])

grp("Minor_Cast_Books_7-9.md", "Minor Cast: Books 7-9", "2", "Book 7", "Book 12", "Books 7-9 and later mentions (chapter files)",
    "../00_Characters_Overview.md, ../Liara_Rimaros.md, ../Pelli.md, ../Melody_Jain.md, ../../06_Places/Rimaros.md",
    "Minor Storm Kingdom, Rimaros society and Purity-order figures with no file of their own.",
    [("Zila Rimaros", ["A diamond-rank member of the Rimaros royal house who oversees checks of the most prestigious visitors (Book 7, Ch52 L50), stands by the throne with Soramir (Book 7, Ch59 L73) and with Soramir smashes the defences of an aristocratic house that protested (Book 7, Ch66 L60). A speaker refers to her as \"Aunt Zila\" (Book 7, Ch17 L116)."]),
     ("Baseph and the Rimaros children", ["Baseph is Liara's husband, silver rank (Book 7, Ch17 L20; Book 8, Ch62 L32). He hammers a pipe to draw raiders in a trap (Book 8, Ch33 L64) and holds Liara's hand under the table (Book 8, Ch63 L3).",
                                          "Their children are Dara (eldest), Zareen (middle) and Joseph (youngest and only son), all silver (Book 8, Ch62 L32-40)."]),
     ("Gibson Amouz", ["Liara's husband's cousin \"Gibbie\" (Book 8, Ch20 L4), originally of the Amouz family, who managed an underwater mining operation (Book 8, Ch26 L29). He is held by the Purity order and freed (Book 8, Ch45 L4), and by Book 9 floats unconscious in a containment tank for recovery (Book 9, Ch28 L45; Book 12, Ch9 L14)."]),
     ("Alejandro Albericci", ["Proprietor of the tailor shop Sensual Attire for the Sensual Gentleman in Rimaros, with formidable society connections (Book 7, Ch42 L61; Book 9, Ch3 L75); he adjusts the formalwear for the celebration ball (Book 9, Ch13 L3). A priest named Aldrich \"Al\" Albericci appears in Book 7 (Book 7, Ch9 L113); the relation is not stated."]),
     ("Havi Estos", ["An information broker who owns a building through layers of paperwork (Book 7, Ch43 L47). In Book 9 he promises Killian Laurent for a price (Book 9, Ch3 L86) and is carried off unconscious (Book 9, Ch4 L16)."]),
     ("Autumn Leal", ["An adventurer Jason met before reaching Rimaros, with a frog essence and a frog familiar ritual (Book 7, Ch20 L21; Book 9, Ch1 L49; Book 9, Ch10 L102)."]),
     ("Zolit Kreen", ["A valash outworlder in Yaresh with a silver-rank aura and no core use (Book 9, Ch46 L5-12), later held in the campus prison (Book 9, Ch77 L3)."]),
     ("Order of Redeeming Light personnel", ["Members named in Book 8: Sendira, Fila and Ramona, all women, Ramona once a celestine (Book 8, Ch9 L11); Rhett and Jaime, silver-rank members who stand apart from the compelled majority (Book 8, Ch16 L28; Book 8, Ch29 L28); Caitlyn, Heston, Marika and Elise, who challenge Melody Jain (Book 8, Ch18 L4-25); Kelleigh, Melody's cell member (Book 8, Ch18 L68); Laront, an ordinary Purity priest who never passed the flames (Book 8, Ch3 L38).",
                                                   "Ramona later joins Miriam's team, Moon's Edge, as a gold-ranker (Book 11, Ch46 L11). Caitlyn's group thinks pain purifies the soul (Book 8, Ch33 L45)."])])

grp("Minor_Cast_Books_10-13.md", "Minor Cast: Books 10-13", "3", "Book 10", "Book 13", "Books 10-13 (chapter files)",
    "../00_Characters_Overview.md, ../Allayeth.md, ../Jota_Withers.md, ../../05_Organisations/Earth_Powers.md",
    "Minor figures of the Yaresh, Cardinas and return books with no file of their own.",
    [("Beaufort (Builder cult commander)", ["A gold-rank elf who heads the Cult of the Builder's forces, gave up his essence powers and is a semi-artificial monstrosity with a fifteen-foot metal skeleton war form (Book 10, Ch65 L30; Book 10, Ch69 L3-5).",
                                             "He calls Jason \"the Defier\", allies with the brighthearts and Jason's expedition and leads the cultists in Book 11 (Book 10, Ch65 L39; Book 11, Ch23 L78; Book 11, Ch44 L39). He shares his name with Thadwick Mercer's father, but is not him (Book 10, Ch72 L41)."]),
     ("Hils Jaramaris", ["The Storm Kingdom's ambassador to Estercost, a silver-ranker who used to adventure with his friend Orin, who went on to travel with Asano (Book 12, Ch49 L3-5)."]),
     ("Garret Headingway", ["An upper-echelon member of House Headingway, one of Estercost's pre-eminent families (Book 12, Ch50 L3), who is held in a suppression collar in Sadi Andali (Book 12, Ch50 L120-126). A different Garret leads a superhero team in Book 5 (Book 5, Ch19 L10)."]),
     ("Neiman Bassingthwaite", ["The chief membership officer of a guild in Cyrion who deals with Jason and is not on the guild master's side (Book 12, Ch44 L112; Book 12, Ch45 L64)."]),
     ("Kreegle", ["A pirate rabble-rouser aboard Jota Withers's ship who plots against him and wants to return to Jakaar triumphant (Book 12, Ch63 L43-53; Book 12, Ch64 L12; Book 12, Ch65 L4)."]),
     ("Navise Den Rigal", ["A Voice of the Will serving a minor astral king who is secretly one of the Unorthodoxy's rare astral kings (Book 12, Ch26 L19-36)."]),
     ("Jacinta Adeline", ["Director of the Adventure Society's Cyrion branch, in one of the organisation's most political posts, who confronts Danielle after the System's withdrawal message (Book 12, Ch50 L43-52)."]),
     ("Barstow", ["The CIA director who briefs the international group on Pakistan and Jason (Book 13, Ch961 L59; Book 13, Ch967 L18-57)."]),
     ("General Michael Mills", ["A general who leads a Book 13 meeting and raises the idea that McKean siphons power from Jason's domains (Book 13, Ch1003 L3; Book 13, Ch1011 L41), and enters a later meeting in an EDJI service dress uniform (Book 13, Ch1020 L85)."])])

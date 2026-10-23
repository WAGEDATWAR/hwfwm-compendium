import io, os, sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
BASE = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".."))
OUT = os.path.join(BASE, "06_Places", "Minor_Places")
os.makedirs(OUT, exist_ok=True)

HEAD = """# {title}

Status: Draft (book text; facts carry a reference "Book N, ChX LY" to Source_Text)
Spoiler level: {lvl}
Valid from: {vf}
Valid through: {vt}
Sources: {src}
Related: ../00_Places_Overview.md, ../../01_World_Primer.md (section 12){rel}

"""

FILES = {}

FILES["Zartos.md"] = ("Zartos", "2", "Book 1", "Book 7", "Book 1, Ch16; Book 7, Ch2", ", ../../07_Characters/Gary.md", """## 1. Summary

Zartos is a subterranean city built around an underground river, largely populated by celestines, and the home of the diamond-rank smith Virid, Gary's mentor (Book 7, Ch2 L71, L75). It is named early as a celestine centre and appears on the page only when Gary and Virid reforge Jason's sword there.

## 2. Location and layout

- A city built around an underground river (Book 7, Ch2 L75). Its region is not stated in the lines checked.
- Virid keeps a personal smithy in the city, "the best place to forge a great work" (Book 7, Ch2 L71-72).

## 3. Society and rule

- **Peoples**: "Zartos has a large celestine community" (Book 1, Ch16 L57); the city is "largely populated by celestines" (Book 7, Ch2 L75).
- No ruler or institution is named in the lines checked.

## 4. Magic level

Not stated. A diamond-ranker lives and works there (Book 7, Ch2 L71).

## 5. History

- Book 1: Gary and Farrah mention Zartos on the road; Rufus has not been there, though his brother recommended it (Book 1, Ch16 L53-58).
- Book 7: after Jason's death the team waits in Zartos while Gary and Virid examine and reforge Dread Salvation, a collaboration that Jason's soul-bond guides (Book 7, Ch2 L71-75); the sword returns as Hegemon's Will (Book 7, Ch54 L108-120).

## 6. Notable people

Virid Martine (Book 6, Ch47 L270), diamond-rank weaponsmith and Gary's mentor (Book 7, Ch1 L30; Book 7, Ch2 L71).

## 7. Customs and daily life

Nothing further is established; the team's stay is described only as a reunion while the smiths work (Book 7, Ch2 L75).

## Open questions

- Where Zartos lies, and who governs it.
""")

FILES["Rakesh.md"] = ("Rakesh", "2", "Book 6", "Book 6", "Book 6, Ch47", ", ../../05_Organisations/Adventure_Society.md, ../../05_Organisations/Magic_Society_and_Associations.md", """## 1. Summary

Rakesh is a populous, caste-divided city on the north coast of the Africa-like continent, home of the Adventure Society's continental council and of the continent's largest Magic Society and Adventure Society strongholds (Book 6, Ch47 L623). It is where the Magic Society holds Clive in all but name and where Danielle meets Carlivexistrix.

## 2. Location and layout

- **Setting**: on the north coast; a desert gulch with a hidden Builder-cult portal lies a few dozen kilometres south (Book 6, Ch47 L623, L651).
- **Buildings**: desert stone, plastered and painted in large, coordinated murals, each district's dominant colour grading into the next (Book 6, Ch47 L709).
- **Campus**: one sprawling campus joins the largest Magic Society and Adventure Society strongholds on the continent (Book 6, Ch47 L623).
- **Link to Vitesse**: Danielle teleports Humphrey and Sophie across the Gramid Passage from Vitesse to Rakesh (Book 6, Ch47 L703).

## 3. Society and rule

- **Caste system**: society is divided into castes, and the caste system justifies holding someone seen as lowly against their will (Book 6, Ch47 L658); it dismisses Belinda as unimportant (Book 6, Ch47 L660).
- **Culture**: busy but quiet streets, a local culture that values calm decorum, most people on foot or in animal-drawn carriages (Book 6, Ch47 L710).
- **The Magic Society branch**: one of the most powerful on the continent; officials there have power and connections, so consequences come from the Adventure Society, not other branches (Book 6, Ch47 L841). The campus prevents portals outside designated zones (Book 6, Ch47 L656).
- **The Adventure Society**: the continental council sits here (Book 6, Ch47 L623). Vitesse is also described as the seat of a continental council (Book 6, Ch47 L604); the text reads most simply as one council per continent, with Rakesh serving the Africa-like continent and Vitesse the continent of Estercost, but it never states this.

## 4. Magic level

Enough to support floating platforms, a common sight, unlike low-magic Greenstone (Book 6, Ch47 L707).

## 5. History

- Book 6: Clive is recruited from Greenstone by Lorelei Grantham, Vice-Dean of the astral magic research department, and finds himself a prisoner of the campus; he and Belinda spend about two months planning an escape through the Builder cult's portal network (Book 6, Ch47 L656-662). He later lodges a protest in Oleyu about his treatment by the Rakesh branch (Book 6, Ch47 L841-842). The Rakesh Magic Society wants the cult's astral magic, not the fight against it (Book 6, Ch47 L865).

## 6. Notable people

Lorelei Grantham (Vice-Dean), Lady Ajus (an official interested in Clive's research) (Book 6, Ch47 L662); Carlivexistrix, whom Danielle will not keep waiting (Book 6, Ch47 L704-706).

## 7. Customs and daily life

Floating platforms for essence users, from standing discs to floating palanquins (Book 6, Ch47 L710); calm public manners (Book 6, Ch47 L710).

## Open questions

- Whether the continental council at Rakesh and the one at Vitesse are two bodies for two continents (see section 3).
""")

FILES["Hornis.md"] = ("Hornis", "1", "Book 1", "Book 12", "Books 1-3 and 9; Book 12 mentions", ", ../Greenstone.md", """## 1. Summary

Hornis is a port city on the coast south and around from Greenstone, reached overland through the delta, the veldt and then south (Book 1, Ch102 L11; Book 3, Ch24 L17). It is Greenstone's nearest rival port, used for smuggling and escapes, and a stop on the team's route home in Book 9.

## 2. Location and layout

- **Location**: "a port city, like Greenstone, south and around the coast"; the overland route runs east into the veldt and then south (Book 3, Ch24 L17).
- **Port**: smuggled goods can come in "through the port in Hornis or the one here in Greenstone" (Book 2, Ch14 L16).

## 3. Society and rule

- **Adventure Society**: Hornis has a branch that mounts large searches (Book 2, Ch22 L76).
- **Magic Society**: Hornis has its own Magic Society people (Book 2, Ch17 L61) and a mirage chamber that Danielle helped rebuild and maintains (Book 2, Ch17 L60).
- **Underworld**: the Big Three's influence is a factor in Greenstone; Sophie plans to buy her way past it in Hornis (Book 1, Ch102 L11).

## 4. Magic level

Not stated.

## 5. History

- Book 1: Sophie plans to flee through the delta and the veldt to Hornis with the spirit coin vault's money (Book 1, Ch102 L11).
- Book 2: smuggled materials are traced to shipments into Hornis before being moved to private vessels (Book 2, Ch27 L4); Jonah's team is found in Hornis on a boat bound for distant shores (Book 2, Ch14 L116; Book 2, Ch15 L25).
- Book 3: Lucian Lamprey hopes to escape to Hornis through a contact (Book 3, Ch24 L12-17).
- Book 9: the team's route home runs south, across the Great Southern Continent, then north to Hornis on the way to Greenstone, Vitesse and Cyrion (Book 9, Ch25 L4).
- Book 12: a Greenstone resident says Hornis is the furthest south he has been (Book 12, Ch38 L49).

## 6. Notable people

None named in the lines checked.

## Open questions

- Distance and travel time to Greenstone (the overland route is only described, not measured).
""")

FILES["Boko.md"] = ("Boko", "0 for sections 1-8; 3 for the Later developments", "Book 1", "Book 12", "Books 1-2 and 12", ", ../Greenstone.md", """## 1. Summary

Boko is an old desert city of academics and artists to the north of Greenstone, with a native population, a Duke, an Adventure Society branch and a Magic Society presence (Book 12, Ch29 L60-61; Book 1, Ch113 L28; Book 2, Ch17 L61). Jason first arrives there by portal at the end of the Ustei expedition. In Book 12 it is destroyed when he is assassinated there.

## 2. Location and layout

- **Setting**: "A city to the north of here. A lot older than Greenstone, with a population native to the area" (Book 12, Ch29 L60). Hester's portal range limits mean Boko is about an hour's recovery from Greenstone by portal (Book 1, Ch109 L9).
- **Look**: desert stone like Old City, with drier air (Book 1, Ch109 L21).
- **Coast**: Boko was a coastal city but never a port like Greenstone, with no natural harbour (Book 12, Ch39 L37, L40; Book 1, Ch113 L21).
- **Gardens and universities**: beautiful architecture and gardens; a warehouse district far from the gardens and universities (Book 12, Ch30 L71; Book 12, Ch31 L34).
- **Temples**: floating temples shielded by their gods survived the destruction (Book 12, Ch33 L3; Book 12, Ch39 L37).

## 3. Society and rule

- **The scholars**: "Scholars of the arts. Painting, poetry, sculpture, dance"; people travel from across the continent to visit its theatres (Book 12, Ch29 L61).
- **People**: almost entirely human and very dark-skinned, with local fashion loose and breathable, calmer than the Ustei's (Book 1, Ch113 L21; Book 12, Ch39 L80).
- **Rule**: a Duke of Boko, a silver-ranker through cores, as is normal for political leaders (Book 12, Ch39 L80); noble houses exist (Book 12, Ch39 L110).
- **Adventurers**: the Adventure Society has a branch (Book 1, Ch113 L28), but Boko "was not a strong adventuring city" (Book 12, Ch33 L7).
- **Trouble**: a movement against intellectuals among low-rankers began in Boko proper before it spread out (Book 12, Ch29 L65); officials suspect more sinister backing and a power base shift to Greenstone and Boko (Book 12, Ch29 L73).

## 4. Magic level

Not stated. It has a mirage chamber that Danielle helped rebuild (Book 2, Ch17 L60).

## 5. History

- Book 1: the Adventure Society returns the Ustei captives to Boko, where Jason arrives through Hester's portal; he, Gary and Rufus explore it (Book 1, Ch109 L7-21; Book 1, Ch112 L52; Book 1, Ch113 L21).
- Book 12: Li Li Mei lives in Boko and is being hunted (Book 12, Ch30 L71). After the assassination the city is evacuated, the blast containment zone gives out and the city is gone; most of its ninety thousand people are evacuated (Book 12, Ch32 L15-29; Book 12, Ch33 L3-4). They shelter in Jason's astral kingdom (Book 12, Ch36 L3-5). The crater becomes a harbour (Book 12, Ch39 L37), and Jason names the astral city New Water, not Boko (Book 12, Ch39 L61, L85-89).

## 6. Notable people

The Duke of Boko (Book 12, Ch32 L91; Book 12, Ch39 L80-91); Li Li Mei (Book 12, Ch30 L71).

## 7. Customs and daily life

Theatres, painting, poetry and dance draw visitors (Book 12, Ch29 L61); local dress is loose and breathable (Book 1, Ch113 L21).

## Later developments (spoilers)

The destruction, evacuation and the Duke's refusal to rebuild elsewhere are Level 3 (Book 12, Ch32-39).

## Open questions

- Whether the rebuilt Boko has begun by the end of Book 13.
""")

FILES["Sadi_Andali.md"] = ("Sadi Andali", "3", "Book 12", "Book 12", "Book 12, Ch50-53", ", ../../04_Peoples_and_Cultures/Law_and_Indenture.md", """## 1. Summary

Sadi Andali is "a little dirtball country", famously almost lawless, where slave markets sell unusual and restricted goods and the Adventure Society keeps no branch (Book 12, Ch50 L126-128; Book 12, Ch52 L35-37). It matters in Book 12 because the System's withdrawal from slave-holding regions turns attention on it.

## 2. Location and layout

- A captive guesses "Eastern desert?" and a fellow prisoner answers "Obviously", so the country is in or near an eastern desert (Book 12, Ch50 L125-126). Cells there are mud brick, reinforced (Book 12, Ch50 L124).

## 3. Society and rule

- **Law**: "famous for being almost lawless"; the Adventure Society has no branch and only sends people in to sweep for illegal research and restricted essences, finding plenty of both (Book 12, Ch50 L128).
- **Slave trade**: unusual products move through its slave markets (Book 12, Ch52 L35-37); Ben asks whether destroying the Sadi Andali slave trade is Jason's price (Book 12, Ch52 L41).
- **Reach**: events "all across Sadi Andali" are set against the great and noble houses of Cyrion (Book 12, Ch52 L74).

## 4. History

- Book 12: Garret and Patterson wake in suppression collars in Sadi Andali (Book 12, Ch50 L120-126); Garret's experience there may have knocked some sense into him, according to Percival (Book 12, Ch53 L7).

## 5. Notable people

Patterson and Garret (Book 12, Ch50 L120-128); Ben (Book 12, Ch52 L36-41).

## Open questions

- Its capital, government and borders; the text gives only the description above.
""")

FILES["Arcazitlan.md"] = ("Arcazitlan", "2", "Book 7", "Book 7", "Book 7, Ch25-31", ", ../Rimaros.md", """## 1. Summary

Arcazitlan is a fortress town dug into the wall of a rocky gorge in jungle country, where Jason arrives alone at the start of the surge and fights bone feasters (Book 7, Ch25 L77-78). Its region is not named in the lines checked.

## 2. Location and layout

- **Setting**: a fortified town "dug high into the wall of a rocky gorge", reached by adventurers because airships would be crushed against the wall by the gorge's gusts (Book 7, Ch25 L77).
- **Interior**: stone chambers and claustrophobic corridors, favouring defence over comfort; civilians sheltering from the surge are packed in (Book 7, Ch28 L3).
- **Defences**: magical sensors throughout the gorge (Book 7, Ch26 L48) and wind-blade runes (Book 7, Ch31 L42); a military command post watches the fight below (Book 7, Ch26 L48).
- **Roads**: a well-maintained network runs through the surrounding jungles and hills (Book 7, Ch29 L8).

## 3. Society and rule

A militia commander runs the fort (Book 7, Ch26 L48). Adventurers make deliveries (Book 7, Ch25 L77).

## 4. History

- Book 7: Jason lands nearby after dropping from the sky, reaches the fort during a night attack by bone feasters (emaciated, eyeless humanoid monsters with large mouths) and helps defend it (Book 7, Ch25 L77-78); he leaves by road with Shade as a land skimmer (Book 7, Ch29 L8).

## 5. Dangers and opportunities

Surge monsters in the gorge and jungle (Book 7, Ch25 L78); the fort's inaccessibility is both defence and difficulty (Book 7, Ch25 L77).

## Open questions

- Which kingdom holds it, and how far it lies from Rimaros.
""")

FILES["Isart.md"] = ("Isart", "2", "Book 9", "Book 9", "Book 9, Ch39", "", """## 1. Summary

Isart is named once: a city on Jason's procession south where Emir asks to meet him to discuss a job and bring the person who made the cloud flasks (Book 9, Ch39 L12-26).

## 2. Facts

- Emir says there is "a city called Isart that you should arrive at on your procession south" (Book 9, Ch39 L12), will meet Jason there when the detour is done (Book 9, Ch39 L16), will arrive in about two weeks and bring the maker of the cloud flasks (Book 9, Ch39 L26).
- No later scene in the chapter files shows Jason reaching Isart, and nothing describes the city.

## Open questions

- Where Isart is, whether the meeting happens, and what the job is.
""")

FILES["Cartise.md"] = ("Cartise", "2", "Book 9", "Book 9", "Book 9, Ch29-35", "", """## 1. Summary

Cartise was a river city and the major hub of trade and travel in its area, destroyed just before the great surge when the Builder cult claimed a nearby astral space and a diamond-rank monster then overwhelmed the city (Book 9, Ch29 L17-18). Jason's team clears monsters from its ruins in Book 9.

## 2. Facts

- **Before**: "the river city of Cartise", the major hub for trade and travel in the area (Book 9, Ch29 L17-18). It had many adventurers who now protect the fortress towns (Book 9, Ch35 L62).
- **The fall**: the Builder cult claimed a nearby astral space, which separated from the world with widespread destruction; a diamond-rank monster manifested shortly after and overwhelmed the city; most people were evacuated to towns along the river (Book 9, Ch29 L17-18).
- **After**: the ruins look like London after the Blitz, with blocks reduced to fist-sized rubble (Book 9, Ch30 L59). Refugees overpopulate the surrounding towns and the loss strains logistics (Book 9, Ch29 L18-19; Book 9, Ch35 L60).
- **Clearing the ruins**: Jason's team sweeps a route guided by an Adventure Society functionary named Vestine, as one of several teams (Book 9, Ch31 L11).

## Open questions

- Which river and region; the text names the city but not the land.
""")

FILES["Jayapura.md"] = ("Jayapura", "1", "Book 2", "Book 7", "Book 2, Ch69-74; Book 3", ", ../../04_Peoples_and_Cultures/Pranay_Culture.md", """## 1. Summary

Jayapura is a port on the northern coast of Pranay, the large southern land equivalent to Sri Lanka, and the birthplace of Hester (Book 2, Ch69 L65-66). Jason's team stays several days after the Reaper trial to awaken abilities, summon familiars and get tattoos (Book 2, Ch74 L14).

## 2. Location and layout

- **Setting**: one of the important sea-trade ports on Pranay's northern coast, in a world with no Arabian Peninsula (Book 2, Ch69 L65-66).
- **Arrival**: Hester opens a portal into the city; Jason and Sophie, with astral affinities, are unaffected by the transition (Book 2, Ch69 L66).
- **Mirage chamber complex**: larger and more sophisticated than the Geller chamber in Greenstone, with concurrent chambers, because the magic is denser (Book 2, Ch73 L3).
- **Mystic Quarter and markets**: floating discs for sale in the Mystic Quarter (Book 3, Ch5 L83); markets the team visits (Book 3, Ch32 L65).

## 3. Society and rule

- **Mirage Chamber Association**: owns the complex, has close ties to the Magic Society, Adventure Society and local government and holds significant power (Book 2, Ch73 L4-5).
- **Entertainment**: essence users fight one another or illusions for a paying audience (Book 2, Ch73 L4).

## 4. Magic level

Higher than Greenstone; it allows advanced dimensional effects (Book 2, Ch73 L3).

## 5. Customs and daily life

Those who can afford them ride platter-sized floating discs (Book 2, Ch70 L3); the team finds new customs and food (Book 2, Ch74 L14); Jason remembers kulfi-like ice cream there (Book 7, Ch14 L52). A nondescript tattoo parlour run by Tilly is where Jason gets his crest (Book 2, Ch73 L62).

## 6. History

Book 2: the visit after the Reaper trial (Book 2, Ch69-74). Book 3: the team's mirage-arena memories inform their confidence (Book 3, Ch45 L100).

## Open questions

- Its rulers, and how large it is; only the Mirage Chamber Association's role is described.
""")

for fn, (title, lvl, vf, vt, src, rel, body) in FILES.items():
    txt = HEAD.format(title=title, lvl=lvl, vf=vf, vt=vt, src=src, rel=rel) + body
    open(os.path.join(OUT, fn), "w", encoding="utf-8").write(txt)
    print("wrote", fn)

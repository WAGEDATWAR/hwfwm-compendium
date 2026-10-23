import io, os, sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
BASE = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".."))
OUT = os.path.join(BASE, "06_Places", "Minor_Places")

HEAD = """# {title}

Status: Draft (book text; facts carry a reference "Book N, ChX LY" to Source_Text)
Spoiler level: {lvl}
Valid from: {vf}
Valid through: {vt}
Sources: {src}
Related: ../00_Places_Overview.md, ../../01_World_Primer.md (section 12){rel}

"""

F = {}

F["Dragon_Lands.md"] = ("The Dragon Lands", "3", "Book 12", "Book 12", "Book 12, Ch26", ", ../../04_Peoples_and_Cultures/Draconians.md", """## 1. Summary

The Dragon Lands are the Pallimustus version of Antarctica: an island continent that is not icy but volcanic, the native land of the draconians (Book 12, Ch26 L5). Jason's sky ship passes over it in Book 12.

## 2. Location and layout

- **Setting**: an island continent named for its "dragon mouth" flame geysers (Book 12, Ch26 L5-6).
- **Land**: dark stone mountains rise from green lowlands of forest and vast farmland laid out like a map, with a climate Jason compares to Scotland or Ireland (Book 12, Ch26 L7).
- **Geology**: subterranean apertures lead to a realm of fire, giving active volcanoes, steaming hot springs and the geysers (Book 12, Ch26 L6).

## 3. Society and rule

- **Peoples**: draconians (Book 12, Ch26 L5); they are called isolationist and are not welcoming to strangers, and trade through proxies outside their lands (Book 12, Ch26 L10-11).
- **Trade**: agricultural products are the second-largest trade through Greenstone's port, after low-rank spirit coins (Book 12, Ch26 L11). Most nations tariff the goods heavily over political issues, which makes them a luxury food (Book 12, Ch26 L12).

## 4. Magic level

The magic leaking from the astral spaces has earth affinity as well as fire; it draws ash from the sky into the ground and makes the farmland famously rich, the best place for gold-rank cooking ingredients (Book 12, Ch26 L9).

## 5. History

Book 12: the team's sky ship approaches the coast and later leaves the Dragon Lands' airspace quickly after a conversation with Anna Tilden (Book 12, Ch26 L7, L77-79).

## Open questions

- Its government and cities; the text gives only the geography above.
""")

F["Girlano.md"] = ("Girlano", "2", "Book 8", "Book 9", "Book 8, Ch24-25; Book 9, Ch26", ", ../Rimaros.md", """## 1. Summary

Girlano is a landlocked inland nation south of the Storm Kingdom, ostensibly a kingdom but controlled by cartels that produce heavily controlled or banned substances, with a puppet government (Book 8, Ch24 L22-23). It is a smuggling region on the Storm Kingdom's border.

## 2. Location and layout

- **Position**: inland, to the south of the Storm Kingdom, whose coast it comes close to; from a tall hill the Sea of Storms can be seen (Book 8, Ch24 L22, L26).
- **Border city**: Casallini (Book 8, Ch24 L25).
- **Border country**: jungle-covered hills with many semi-hidden smuggling paths between the border and the shore (Book 8, Ch24 L26).

## 3. Society and rule

- **Cartels**: the illicit leadership keeps its position through under-the-table deals with powerful groups in neighbouring countries, which prop up the puppet government while their own governments pay lip service to suppression (Book 8, Ch24 L23).
- **Trade**: the rare plants and minerals of the region are what the cartels exploit, and strong public sanctions and border controls surround the nation (Book 8, Ch24 L22).
- **Adventure Society**: it ignores borders and politics and keeps monsters out of population centres, so long as its work is not interfered with (Book 8, Ch24 L24-25).
- **Reputation**: Liara calls it "a stain full of drug dealers and smugglers" (Book 8, Ch25 L120); Belinda finds it "famously sketchy" and tempting (Book 9, Ch26 L3).

## 4. History

- Book 8: Sophie heads toward Girlano and Casallini on a specialised delivery (Book 8, Ch24 L25).
- Book 9: the team turns east at the coast, not south toward Girlano (Book 9, Ch26 L3).

## Open questions

- Its ruler and capital; only the border region is described.
""")

F["Oleyu.md"] = ("Oleyu", "2", "Book 6", "Book 6", "Book 6, Ch47", ", Rakesh.md", """## 1. Summary

Oleyu is an unremarkable border city on a river, "pleasant, prosperous, and moderately sized", built on river trade with a mid-range level of magic (Book 6, Ch47 L840).

## 2. Facts

- **Position**: Clive's route follows a river to "the border city of Oleyu", where the Rakesh Magic Society branch's area of influence ends (Book 6, Ch47 L838).
- **Standing**: not as big or important as Rakesh or Vitesse, or unusual like Greenstone (Book 6, Ch47 L840).
- **Magic Society building**: Clive lodges a protest here over his treatment by the Rakesh branch, without optimism (Book 6, Ch47 L841-842).

## Open questions

- Which border it lies on, and which river.
""")

F["Leust.md"] = ("Leust", "1", "Book 1", "Book 1", "Book 1, Ch92-94", ", ../Greenstone.md", """## 1. Summary

Leust is one of the largest and richest towns in the delta, with paved roads and stone buildings instead of mud brick (Book 1, Ch93 L5). Jason stays there while investigating a fergax contract in the nearby lumber region.

## 2. Location and layout

- **Town**: mostly yellow desert stone, with some green stone buildings; the water affinity of green stone keeps interiors cool, and Jason stays at a large green stone inn (Book 1, Ch93 L5-6).
- **Lumber region**: on the south side of the river in the eastern delta, the furthest part from the city; more solid ground than marsh, laid out like a forestry reserve with trees in neat rows, saplings and cleared fields (Book 1, Ch93 L3, L22). Wagons carry lumber to Leust (Book 1, Ch93 L22).

## 3. Society and rule

- **Industry**: lumber; the land rights are heavily regulated (Book 1, Ch92 L63), and the lumber region is one of the few places in the delta where lumber-worthy trees grow (Book 1, Ch92 L61).
- **Mill owners**: Kyle Lindover, a leonid larger than Gary, owns the Lindover Lumber Mill and shut it after repeated fergax sightings (Book 1, Ch93 L24, L28); his family stays with her parents in Greenstone (Book 1, Ch93 L29).

## 4. History

Book 1: Jason takes an unusual contract to hunt a fergax that is never found (Book 1, Ch92 L59-65), stays in Leust (Book 1, Ch93 L5-8), finds the Clementson property and the adventurer Dean Tuckell summoning monsters, and learns that Thadwick Mercer set it up (Book 1, Ch94 L8-13, L58).

## Open questions

- Its exact position in the delta relative to Greenstone.
""")

F["Kazlahk.md"] = ("Kazlahk", "3", "Book 11", "Book 11", "Book 11, Ch68", ", ../../04_Peoples_and_Cultures/Estercost_Culture.md", """## 1. Summary

Kazlahk is a wealthy coastal city on the eastern border of Estercost, surrounded by desert and used for spirit coin farms, with a famously scalding climate (Book 11, Ch68 L1380-1381).

## 2. Location and layout

- **Setting**: "a city of sandstone, palm trees and money", on Estercost's eastern border, surrounded by desert (Book 11, Ch68 L1380).
- **Coast**: gorgeous beaches lined with the massive houses of coin barons and major adventuring families; a luxury resort for merchants, adventurers and nobility (Book 11, Ch68 L1381-1382).

## 3. Society and rule

- **Wealth**: its spirit coins and sea trade; as with Greenstone, the empty desert is a premium site for spirit coin farms, but the higher magic makes for more valuable denominations (Book 11, Ch68 L1380-1381).
- **Kazlahk University of Medicine**: the most notable beach institution; healing studies focus on essence and ritual magic over alchemy because the Magic Society and Adventure Society fund them, with some money from the Healer's church (Book 11, Ch68 L1382-1383). Its School of Alchemical Efficiency appears in a disclaimer (Book 11, Ch68 L1397).

## 4. History

Book 11: the group considers a detour to Kazlahk on the way to Estercost (Book 11, Ch68 L1377, L1380).

## Open questions

- Its ruler or council; only its wealth and institutions are described.
""")

F["Kurdansk.md"] = ("Kurdansk", "2", "Book 6", "Book 12", "Book 6, Ch47; Book 9, Ch27; Book 12, Ch49", ", ../../04_Peoples_and_Cultures/Kurdansk_Culture.md", """## 1. Summary

Kurdansk is a river city in the People's Holy Federation of Dreisil and Sophie Wexler's birthplace (Book 6, Ch47 L390). It has a busy skyport, an entertainment quarter in a former warehouse district, many dark-skinned, silver-haired celestines and prisons that hold criminals for years (Book 6, Ch47 L436, L459, L508; Book 12, Ch49 L77). For the culture see `../../04_Peoples_and_Cultures/Kurdansk_Culture.md`.

## 2. Location and layout

- **Nation**: the People's Holy Federation of Dreisil (Book 6, Ch47 L390). Humphrey remarks that the more a nation calls itself free and righteous, the more tyrannical it is (Book 6, Ch47 L392).
- **Entertainment quarter**: a former warehouse district by the Kurdan River docks, now the most viable site for large theatre halls, "a heady mix of pleasure, criminality and money" (Book 6, Ch47 L436).
- **Skyport**: busy, with towers where airships dock; Emir's cloud ship recovers its full function there (Book 6, Ch47 L459).
- **Houses**: narrow row houses wedged together (Book 6, Ch47 L508).

## 3. Society and rule

- **Peoples**: celestines with dark skin and silver hair are common (Book 6, Ch47 L437, L508).
- **Law**: the city locks criminals up for years, which a Book 12 speaker calls costly to run (Book 12, Ch49 L77).

## 4. History

- Book 6: Emir tells Sophie she was born in Kurdansk (Book 6, Ch47 L386-390); the team searches the city, and Marta Fries, a silver-rank celestine and friend of Melody Jain, escapes through a hidden panel Melody once used to fake her death, about two decades earlier (Book 6, Ch47 L508-510).
- Book 9: Melody Jain's story begins in Kurdansk about twenty-five years before; she and Sophie's father were both secret members of organisations, the Order of the Reaper among them (Book 9, Ch27 L24-26).

## Open questions

- Its size and ruler, and the Federation's structure.
""")

F["Palisaros.md"] = ("Palisaros", "2", "Book 7", "Book 9", "Book 7, Ch13, Ch41, Ch61; Book 8, Ch28, Ch52, Ch62", ", ../Rimaros.md", """## 1. Summary

Palisaros is a small laid-back town on the island of Arnote in the Storm Kingdom, arranged along a lagoon and the clifftop above it, where Jason settles his cloud house (Book 7, Ch13 L33; Book 8, Ch28 L59; Book 8, Ch52 L20).

## 2. Location and layout

- **Island**: Arnote, the quiet residential island of Rimaros's three public islands (Book 7, Ch7 L70; Book 8, Ch28 L59).
- **Lagoon and cliff**: the town lies along the lagoon shore and the clifftop bordering it, with a waterfall and a river spilling over the cliff (Book 8, Ch28 L59).
- **Houses**: colourful, two or three storeys, with open space, covered walkways, balconies and awnings, and hidden magical amenities (Book 7, Ch13 L35).
- **Jason's house**: his cloud house stands on a clifftop near the river, with an invisible barrier along the cliff edge (Book 8, Ch52 L20).

## 3. Society and rule

- **Residents**: mostly normals, irons and bronzes using cores, with a few silver and gold auras, and many caramel-skinned celestines (Book 7, Ch13 L34).
- **Pace**: small-town, with none of the residents in a rush, calmer than busy Livaros (Book 7, Ch13 L33).
- **Mayor**: Pelli, a member of the royal family but separate from them, living a relatively humble life as a core user (Book 7, Ch61 L59; Book 8, Ch62 L60).
- **Guide**: Argy shows visitors the saloon, eateries and market (Book 7, Ch13 L35).

## 4. History

- Book 7: Jason meets Argy and Pelli in the town and settles there (Book 7, Ch13 L20-35; Book 7, Ch41 L61); during the surge only Jason and Pelli remain to defend it, and Jason leaves shortly after his team (Book 7, Ch61 L60).
- Book 8: Vidal rides into the lagoon to find Wexler's team staying in a house by the waterfall (Book 8, Ch28 L59).

## Open questions

- Population and layout beyond the clifftop and lagoon.
""")

for fn, (title, lvl, vf, vt, src, rel, body) in F.items():
    open(os.path.join(OUT, fn), "w", encoding="utf-8").write(HEAD.format(title=title, lvl=lvl, vf=vf, vt=vt, src=src, rel=rel) + body)
    print("wrote", fn)

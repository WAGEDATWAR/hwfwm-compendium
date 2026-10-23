import os
base = r"C:\Users\Gabriel\Documents\World Stuff\HWFWM Compendium\04_Peoples_and_Cultures"
os.makedirs(base, exist_ok=True)
HDR = """# {name}

Status: Draft (book text; facts carry a reference "Book N, ChX LY" to Source_Text; "notes" marks chapter-summary-only facts)
Spoiler level: {spoil}
Valid from: Book {vf}
Valid through: Book {vt}
Sources: {src}
Related: {rel}

## 1. Summary

{summary}

## 2. Facts

{facts}

## 3. Using this in a story

{rp}
"""
def write(fn, name, spoil, vf, vt, src, rel, summary, facts, rp):
    open(os.path.join(base, fn + ".md"), "w", encoding="utf-8").write(HDR.format(name=name, spoil=spoil, vf=vf, vt=vt, src=src, rel=rel, summary=summary, facts=facts, rp=rp))

write("00_Peoples_Overview", "Peoples of Pallimustus: Overview", "0 for Books 1-4; 2 for the Book 12 change to \"nature\"", "1", "12",
 "Books 1, 2, 3, 5, 6, 9, 12 (chapter files)",
 "../01_World_Primer.md, Humans.md, Elves.md, Leonids.md, Celestines.md, Draconians.md, Smoulder_and_Brighthearts.md, Runics.md, Valash.md, Outworlders.md",
 "The civilisation-building peoples of Pallimustus, what a racial gift is, and the peoples that are not native to the world. Each people has its own file.",
 "- **Civilisation-building peoples**: Jason's team finds bodies of \"every civilisation-building species: humans, elves and leonids, celestines, runic, smoulder and draconians\" in the Book 1 desert astral space (Book 1, Ch86 L40).\n- **Where they live**: the Greenstone region is human-dominated, while a port city shows \"all kinds of people\" (Book 1, Ch15 L56).\n- **Racial gifts**: \"Every race has six racial gifts\"; for humans they are an affinity for special attacks, faster essence advancement and latent powers that adapt to the person's essences (Book 1, Ch85 L35). A racial gift can change in \"racial power evolution\"; the latent human gifts are blank slates guaranteed to do so (Book 1, Ch85 L39). Triggers are often a traumatic event, a near-fatal fight or long habit (Book 1, Ch85 L41); a god's blessing, or that of a great astral being, can trigger it (Book 1, Ch85 L47; Book 1, Ch85 L22-26).\n- **Sharing gifts**: the Magic Society prizes the details of racial gifts, and Humphrey advises Jason to keep his to himself and trade them for favours (Book 1, Ch38 L72).\n- **Other peoples named**: merfolk (\"Merfolk are not fish... They happen to be very sensual people\", Book 3, Ch69 L509), goblins, fairies and valash, the last three appearing as forms taken by people changed in Earth's transformation zones (Book 5, Ch54 L52; Book 6, Ch23 L91; Book 9, Ch45 L57).\n- **Not native**: outworlders and valash are not native to Pallimustus (see Outworlders.md and Valash.md); messengers are covered in the Cosmology files.\n- **From race to nature**: in Book 12 Jason's character screen says \"nature\" instead of \"race\" and calls him a \"prime avatar of an astral nexus\"; Shade suggests that \"race\" is a term Jason took from games and cannot cover the breadth of people the System now serves (Book 12, Ch8 L100-102). Jason keeps the six powers that used to be racial gifts (Book 12, Ch8 L103).",
 "Treat race as a matter of body, gifts and culture, not value: gifts are real advantages, but anyone's gifts can evolve. Greenstone scenes are human-heavy; ports, Vitesse and Yaresh are mixed.")

write("Humans", "Humans", "0", "1", "13", "Books 1, 2, 3, 5, 12 (chapter files)",
 "00_Peoples_Overview.md, Outworlders.md, ../03_Magic_and_Adventuring/Magic_and_Adventuring.md",
 "The most common people of Pallimustus and Earth's native people, with gifts that favour special attacks and fast essence advancement.",
 "- **Racial gifts**: an affinity for special attacks, essences that advance more rapidly than others', and latent powers that adapt to the essences (Book 1, Ch85 L35). The latent gifts are dormant until awakened and then take a form based on the person's essences (Book 1, Ch38 L73).\n- **Evolution**: Clive's blessing from the Celestial Book changes his human special attack affinity into a spell affinity (Book 1, Ch85 L22-26); his Human Ambition becomes Thirst for Knowledge and Humphrey's Special Attack Affinity becomes Attack of the Mirage Dragon (Book 2, Ch61 L144, L147). Taika's human abilities have been replaced with outworlder ones (Book 9, Ch33 L15).\n- **Distribution**: the Greenstone region is human-dominated (Book 1, Ch15 L56).\n- **Humans and outworlders**: an outworlder who has a child with another species produces offspring of that species, so a human and an outworlder have a human child (Book 5, Ch44 L72).\n- **Lifespan**: essence users age slower; bronze-rankers can live well past a hundred, silvers double that and gold-rankers live for centuries (Book 1, Ch22 L58).",
 "Humans are the default people of the delta and of every Earth scene; their gifts reward specialised, skilled builds.")

write("Elves", "Elves", "0", "1", "13", "Books 1, 2, 3, 9, 10 (chapter files)",
 "00_Peoples_Overview.md, Humans.md, ../06_Places/Yaresh.md",
 "Elves are powerful spellcasters whose healing magic is unparalleled.",
 "- **Reputation**: \"Elves are powerful spell casters and their skill with healing magic is unparalleled\" (Book 1, Ch15 L50).\n- **Aptitude**: the elven aptitude is for spells rather than the special attacks humans favour (Book 3, Ch1 L90).\n- **Racial gift**: Neil's elf racial ability, Life Affinity, evolves into Life Guard (Book 2, Ch61 L145).\n- **Local families**: Greenstone has local elf families; Lucian Lamprey is an elf banished there who is not one of them (Book 1, Ch42 L25-30), and Pochard Finn is an elf and a local (Book 1, Ch42 L30).\n- **Elf fashion**: \"flowing, tapered lines\" (Book 9, Ch46 L5).\n- **Notable elves**: Allayeth and Charist, Yaresh's two diamond-rank elves (Book 9, Ch98 L4); Hana Shavar, High Priestess of the Healer (Book 10, Ch3 L29); Elspeth Arella, director of the Greenstone Adventure Society (Book 1, Ch83 L45).\n- **Predation**: cannibals in Book 1 discuss elves as food (Book 1, Ch3 L43; Book 1, Ch15 L51).",
 "Good for healers, spellcasters and long-lived local power brokers; elf aristocrats tend to hold municipal office.")

write("Leonids", "Leonids", "0", "1", "13", "Books 1, 2, 7, 12 (chapter files)",
 "00_Peoples_Overview.md, ../07_Characters/Gary.md",
 "Lion-headed, furred, strong and fast people; Gary is the best-known leonid.",
 "- **Strength and stamina**: \"Members of his leonid race are stronger and faster than us, and that's only the beginning of what leonids can do\" (Book 1, Ch15 L50); a leonid needs far more exertion than others to tire, another racial gift (Book 1, Ch15 L84).\n- **Appearance**: a huge \"lion man\" whose voice is growly by default (Book 1, Ch9 L131); Gary is \"so huge he made bodybuilders look like they w[ere small]\" (Book 1, Ch14 L14). He is covered in fur (Book 1, Ch15 L84).\n- **Size**: draconians are larger even than male leonids (Book 2, Ch38 L29).\n- **Mixed company**: a leonid, an elf and a celestine are among the eleven people who emerge from Dawn's cottage in Book 7 (Book 7, Ch52 L66).\n- **Notable leonids**: Gary Xandier, a Vitesse adventurer (Book 1, Ch30 L47), and the young Gary Sharpton in Book 12 (Book 12, Ch62 L4-9).",
 "Leonids are natural front-liners: expect size, endurance and a deep voice.")

write("Celestines", "Celestines", "0", "1", "13", "Books 1, 2, 3, 5, 6, 7, 8, 9 (chapter files)",
 "00_Peoples_Overview.md, Outworlders.md, ../07_Characters/Sophie_Wexler.md, ../07_Characters/Dawn.md",
 "Metallic-haired, metallic-eyed people with an astral affinity, produced when two outworlders have a child.",
 "- **Appearance**: Sophie has chocolate skin and shining silver hair, her eyes matching it exactly, \"the matching metallics a giveaway trait of the celestine race\" (Book 1, Ch43 L18). In Kurdansk many celestines have dark skin and silver hair (Book 6, Ch47 L508).\n- **Astral affinity**: astral affinity is a celestine racial gift (Book 1, Ch15 L76-80); celestines are similar to elves and humans (Book 1, Ch15 L78). The rare Child of the Celestial Wind appears only in races with astral affinity, on Pallimustus meaning celestines, or potentially outworlders (Book 8, Ch21 L40).\n- **Origin**: Dawn says two outworlders who have a child produce a celestine, and celestines propagate with their own kind; she is herself a child of two outworlders (Book 5, Ch44 L72).\n- **Gift evolutions**: Sophie's Mana Integrity becomes Mana Wellspring (Book 2, Ch61 L146), her Astral Affinity becomes Boundary Breaker (Book 3, Ch68 L14) and her Celestial Swiftness becomes Princess of the Firmament (Book 8, Ch22 L37).\n- **Communities**: Zartos is a subterranean city largely populated by celestines (Book 7, Ch2 L75).\n- **Messengers**: messengers are about half again as tall as a celestine, and their servants take care never to imply the resemblance (Book 9, Ch55 L9).\n- **Dawn's true form**: a celestine with ruby eyes and hair (Book 7, Ch54 L87).",
 "Celestines are visibly striking and often the children of the outworlder arrivals; their culture is as varied as any people's.")

write("Draconians", "Draconians", "0", "2", "12", "Books 1, 2, 12 (chapter files)",
 "00_Peoples_Overview.md, ../06_Places/00_Places_Overview.md",
 "Large, scaled humanoids who claim descent from dragons and whose homeland is the Dragon Lands.",
 "- **Appearance**: \"a member of the rare draconian race, larger even than male leonids and covered in glossy scales\", the colour of dark leaves, green moving into purple (Book 2, Ch38 L29); Maximilian is the tallest person in Greenstone, with a long hairless head and glossy scales (Book 2, Ch39 L15). A draconian skull is distinctive enough to identify skeletons (Book 1, Ch86 L31).\n- **Pride in descent**: draconians \"took pride in their claimed dragon ancestry and often had issues with other races wielding the dragon essence\" (Book 2, Ch39 L34).\n- **Homeland**: the Dragon Lands, Pallimustus's version of Antarctica, \"the native land of the large, scaled humanoids known as draconians\", with active volcanoes, hot springs and \"dragon mouth\" geysers from subterranean apertures to a realm of fire (Book 12, Ch26 L5-6).\n- **Rarity**: draconians are rare in Greenstone, where Maximilian is the only one present at a gathering (Book 2, Ch39 L15).",
 "A draconian is a rare, imposing figure; mention of a dragon essence in their company is a social risk.")

write("Smoulder_and_Brighthearts", "Smoulder and Brighthearts", "0 for Book 1; 3 for Cardinas", "1", "11", "Books 1, 10, 11 (chapter files)",
 "00_Peoples_Overview.md, ../06_Places/Astral_Spaces/Transformation_Zones.md",
 "Dark-skinned people with glowing red eyes and affinities for earth and fire; the brighthearts are the smoulder of the deep underground realm of Cardinas.",
 "- **Smoulder**: \"They have natural affinities for earth and fire\"; a smoulder friend of Humphrey's parents has the wind essence and his earth affinity evolved into an air affinity (Book 1, Ch85 L45). Niko, a member of Beth's team, has dark skin, glowing red eyes and jet-black hair (Book 1, Ch89 L63).\n- **Brighthearts**: in Book 10 fewer than ten thousand of the brightheart smoulder survive, crammed in the citadel cavern (Book 10, Ch65 L6). Marla is a fire aspect with skin markings, eyes and hair the yellow-orange of steel in a forge; Lorenn, an ash aspect, has smoky greys (Book 10, Ch65 L9).\n- **War form**: Beaufort prefers his fifteen-foot metal skeleton \"war form\" but must meet the brightheart smoulders in a form they will accept (Book 10, Ch69 L4).\n- **Home**: the largest chamber of the underground realm was home to most brightheart smoulders (Book 10, Ch71 L52).",
 "Smoulder adventurers are ordinary Pallimustus people; brighthearts are a besieged, deep-living society that welcomes outsiders only after great loss.")

write("Runics", "Runics", "0", "1", "13", "Book 1 (chapter files)",
 "00_Peoples_Overview.md, ../02_Cosmology_and_Powers/Gods_and_Churches.md",
 "Short, stocky, hairless people with deep-blue skin and naturally glowing runes.",
 "- **Appearance**: \"short and stocky, with skin of such a deep blue it was almost black\", no hair and covered in faintly glowing, tattoo-like markings that are natural to the race (Book 1, Ch45 L14).\n- **Rarity**: they are \"a rarity in Greenstone\" (Book 1, Ch45 L14); a runic barman in Old City is stocky and hairless with blue-black skin and glowing runes (Book 1, Ch71 L40).\n- **Bones**: the runes show faintly on their bones; a short, broad skeleton in the desert astral space is identified as a runic by them (Book 1, Ch86 L31).\n- **Notable**: Arash, a runic Jason meets in the temple district, explains Dominion's role (notes, Book 1).",
 "A runic in a scene stands out in Greenstone; their glowing marks make hiding difficult.")

write("Valash", "Valash", "2", "5", "9", "Books 5, 6, 9 (chapter files)",
 "00_Peoples_Overview.md, Outworlders.md, ../06_Places/Astral_Spaces/Transformation_Zones.md",
 "A skinny, chihuahua-headed species that is not native to Pallimustus; humans are turned into valash by Earth's transformation zones.",
 "- **Origin**: Jason had only seen valash when Earth's transformation zones turned humans into them (Book 9, Ch45 L57); they are \"a skinny sapient species not native to Pallimustus\" (Book 9, Ch46 L5).\n- **Appearance**: \"skinny bodies and Chihuahua-like heads\", shorter than Jason (Book 9, Ch45 L58; Book 9, Ch46 L5).\n- **Outworlders**: the valash Jason meets in Yaresh is an outworlder with a silver-rank aura and no sign of core use (Book 9, Ch45 L58; Book 9, Ch46 L6).\n- **Fashion**: his fitted white suit is not in the local style and \"would have been more at home in a Miami nightclub in the eighties\" (Book 9, Ch46 L5).",
 "Valash on Pallimustus are almost always outworlders from Earth's zones; they read as foreign and out of place.")

write("Outworlders", "Outworlders", "0 for the concept; 2 for the Book 7 arrivals", "1", "12", "Books 1, 2, 5, 7, 12 (chapter files)",
 "00_Peoples_Overview.md, Celestines.md, Valash.md, ../07_Characters/Jason_Asano.md",
 "People whose souls re-entered a physical reality, manifesting a new body; they carry unusual gifts and cannot be easily tracked.",
 "- **Definition**: Clive: \"An outworlder is someone whose soul has re-entered a physical reality, reflexively manifesting a body for itself\" (Book 2, Ch25 L57); the body is \"akin to that of a monster, or a summoned familiar\", physical substance forged from raw magic, between the astral and the physical (Book 2, Ch25 L59).\n- **How it happens**: natural magical phenomena connecting two realities drag someone through; their body is annihilated in the astral and their soul reconstitutes one (Book 2, Ch25 L61).\n- **Advantages**: Farrah says outworlders \"might have their advantages\", and Jason's abilities (map, interface, astral affinity) are outworlder abilities (Book 1, Ch15 L50, L74-76).\n- **Children**: an outworlder with another species produces offspring of that species; two outworlders produce a celestine (Book 5, Ch44 L72).\n- **Arrivals**: a hundred and nineteen outworlders arrive at once in Book 7 (Book 7, Ch36 L86); two outworlders among the eleven people in Dawn's cottage are bronze rank (Book 7, Ch52 L66).\n- **Jason**: his character screen lists him as a formerly human outworlder until Book 12 (Book 12, Ch8 L100).",
 "Outworlders are fish out of water: a body that is partly astral, gifts nobody can explain, and an arrival story that usually involves loss.")
print("ok")

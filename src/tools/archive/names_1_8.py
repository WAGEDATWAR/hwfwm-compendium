import os, re
B = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", ".."))
MC = "07_Characters/Minor_Cast/"


def add_entries(fname, text):
    p = os.path.join(B, *(MC + fname).split("/"))
    s = open(p, encoding="utf-8").read()
    marker = "## 3. Using this in a story"
    assert marker in s
    if text.split("\n")[0] in s:
        return
    s = s.replace(marker, text.rstrip("\n") + "\n\n" + marker, 1)
    open(p, "w", encoding="utf-8").write(s)


add_entries("Minor_Cast_Books_1-3.md", """### Madam Landry

- The landlady of the Greenstone inn where Jason lodges, who berates a tall man in scholar's robes in her lounge (Book 1, Ch64 L83). Jason calls her "a small business owner who works very hard to run a quality establishment" (Book 1, Ch82 L82).
<!-- level:3 -->
- By Book 12 she finds second-tier adventurers the perfect clientele for long-term tenancy (Book 12, Ch27 L5).
<!-- /level -->

### Janice

- Jory's teenage receptionist and assistant at his shop (Book 1, Ch44 L40; Book 1, Ch106 L8). Jason pleads with her for crystal wash (Book 1, Ch76 L15).
<!-- level:3 -->
- A Janice manages a patisserie in Vitesse in Book 11 (Book 11, Ch68 L2060); the text does not say she is the same person.
<!-- /level -->

### Ernest Geller

- A Geller team leader who looks like Humphrey, with the same height and broad shoulders; Jason does not assume a close relation (Book 1, Ch80 L90). He makes a "teaching moment" of his team's choices (Book 1, Ch82 L31), leads the team at the sand barge battle (Book 1, Ch90 L32) and later guards Jonah Geller (Book 2, Ch19 L73).

### Jerrick

- The burly thug adventurer, toughest of those Thadwick Mercer took under his auspices (Book 1, Ch95 L16); he fights with a spiked sphere on a chain (Book 1, Ch95 L46) and is quietly struck off the Adventure Society roll afterwards (Book 1, Ch97 L101).

### Imran Keane

- A guardian-type who conjures heavy armour and a huge shield, added to a party with Jory in the Reaper trials (Book 2, Ch46 L42) and then to Jason's party (Book 2, Ch53 L64).
""")

add_entries("Minor_Cast_Books_4-6.md", """### Thanh

- A category-three member of the capture team that hunts Jason through a large city in Book 5; his light essence gives him the speed to keep up and the aura to light the slum town (Book 5, Ch1 L15-17). Jason's aura stops his dead (Book 5, Ch1 L35), and Jason ends the fight with a threat to his soul (Book 5, Ch1 L85).

### Ingrid

- The head of the security team at the base where Travis is put in charge of the Special Munition Stockpile Division (Book 6, Ch28 L37-39). Jason says she gives off an Anisa vibe (Book 6, Ch29 L13).

### Loth

- A silver-rank dino-man who chose his own name, leading almost thirty dino-monsters through the Makassar proto-space in search of the unknown being behind the rainbow smoke (Book 5, Ch27 L24-26). He loses control of them as Jason's afflictions spread (Book 5, Ch27 L36-37).

### Night Stalker

- A bronze-rank vampire who fights beside Craig Vermillion and Franklin (Book 5, Ch64 L68) and calls himself the Night Stalker; Farrah threatens to put him down for it (Book 5, Ch65 L18).

### Higgy

- A member of Nigel Thornton's team who, with Darcy and Jonno, takes and gives the big hits (Book 4, Ch39 L76). He conjures a shield and prefers Higgy to "Captain America" (Book 4, Ch40 L63).
<!-- level:3 -->
- He is still with the team in Book 12, steering a conversation back on topic (Book 12, Ch3 L38), and in Book 13 calls "CONTACT!" as the squad guards Itsuki (Book 13, Ch1007 L39).
<!-- /level -->
""")

add_entries("Minor_Cast_Books_7-9.md", """### Merrick Harlowe

- The commander of a fort, a minor local lord and a silver-rank core user, who watches the first shab fall to the town's defences with little joy (Book 7, Ch19 L95). Melody Jain works on his sympathies (Book 7, Ch20 L84; Book 7, Ch32 L51, L86).

### Eric Maldonado

- The organiser behind the hunt for Jason in Book 9. He has sunk favours and most of his surge earnings into it (Book 9, Ch9 L57-58) and hired a costly tracker and an Adventure Society communications official (Book 9, Ch9 L58, L62). Shade judges his team the best prepared of the hunters (Book 9, Ch9 L19).

### Rangel and Tellez

- Two team leaders hunting Jason in the jungle (Book 9, Ch7 L33, L46). Rangel admits he stole Maldonado's plan (Book 9, Ch7 L92), and Jason takes four people from his group (Book 9, Ch9 L63).

### Carilo

- A healer in Rangel's party, told to cleanse a poisoned teammate (Book 9, Ch8 L6) before Jason drags him into the scrub (Book 9, Ch8 L12).

### Emresh

- A thug and loan collector in Yaresh who kicks Jason on the floor while Bellory fetches the repayment (Book 9, Ch44 L25, L60). He is silver rank and pushes past others in a crisis (Book 9, Ch101 L54).

### Lancet de Varco

- A tournament duellist of House de Varco and sometime adventurer, well known in the mirage arenas (Book 9, Ch15 L14), who is touchy about being called a coward (Book 9, Ch15 L53, L67).
""")

add_entries("Minor_Cast_Books_10-13.md", """### Finneus Gallow

- A monster-core user from Gormanston's aristocratic faction, confronted by Marcus over who keeps Adventure Society membership after the messenger invasion (Book 10, Ch48 L15, L31, L41).

### Geneva Andros

- Director of the Network's Geneva branch (Book 13, Ch974 L52; Book 13, Ch975 L4). She is the only silver-ranker among the gold-rankers Jason fights on the flying bus (Book 13, Ch976 L6) and accuses Bussinger of turning traitor (Book 13, Ch977 L107).

### Kol Kelis Vel

- A gold-rank messenger in the Cardinas zone alongside Galis Jay Vahal (Book 11, Ch6 L50). Belinda's hidden circle leaves her badly hurt (Book 11, Ch14 L10, L20).
""")


NAMES = {
"Madam Landry": ("L", "(B1): landlady of Jason's inn in Greenstone. See `07_Characters/Minor_Cast/Minor_Cast_Books_1-3.md`."),
"Janice": ("J", "(B1): Jory's teenage receptionist. See `07_Characters/Minor_Cast/Minor_Cast_Books_1-3.md`."),
"Ernest Geller": ("E", "(B1): Geller team leader. See `07_Characters/Minor_Cast/Minor_Cast_Books_1-3.md`."),
"Jerrick": ("J", "(B1): Thadwick Mercer's burly thug adventurer. See `07_Characters/Minor_Cast/Minor_Cast_Books_1-3.md`."),
"Imran Keane": ("K", "(B2): guardian-type with heavy armour and a huge shield. See `07_Characters/Minor_Cast/Minor_Cast_Books_1-3.md`."),
"Thanh": ("T", "(B5): category-three capture-team member with a light essence. See `07_Characters/Minor_Cast/Minor_Cast_Books_4-6.md`."),
"Ingrid": ("I", "(B6): head of the stockpile security team. See `07_Characters/Minor_Cast/Minor_Cast_Books_4-6.md`."),
"Loth": ("L", "(B5): silver-rank dino-man in the Makassar proto-space. See `07_Characters/Minor_Cast/Minor_Cast_Books_4-6.md`."),
"Night Stalker": ("N", "(B5): bronze-rank vampire with Craig Vermillion. See `07_Characters/Minor_Cast/Minor_Cast_Books_4-6.md`."),
"Higgy": ("H", "(B4): member of Nigel Thornton's team. See `07_Characters/Minor_Cast/Minor_Cast_Books_4-6.md`."),
"Merrick Harlowe": ("M", "(B7): fort commander and silver-rank core user. See `07_Characters/Minor_Cast/Minor_Cast_Books_7-9.md`."),
"Eric Maldonado": ("M", "(B9): organiser of the hunt for Jason. See `07_Characters/Minor_Cast/Minor_Cast_Books_7-9.md`."),
"Rangel": ("R", "(B9): team leader in the hunt for Jason; with Tellez. See `07_Characters/Minor_Cast/Minor_Cast_Books_7-9.md`."),
"Tellez": ("T", "(B9): team leader in the hunt for Jason; with Rangel. See `07_Characters/Minor_Cast/Minor_Cast_Books_7-9.md`."),
"Carilo": ("C", "(B9): healer in Rangel's party. See `07_Characters/Minor_Cast/Minor_Cast_Books_7-9.md`."),
"Emresh": ("E", "(B9): loan-collecting thug in Yaresh. See `07_Characters/Minor_Cast/Minor_Cast_Books_7-9.md`."),
"Lancet de Varco": ("L", "(B9): House de Varco duellist. See `07_Characters/Minor_Cast/Minor_Cast_Books_7-9.md`."),
"Finneus Gallow": ("F", "(B10): monster-core user of Gormanston's aristocratic faction. See `07_Characters/Minor_Cast/Minor_Cast_Books_10-13.md`."),
"Geneva Andros": ("G", "(B13): director of the Network's Geneva branch. See `07_Characters/Minor_Cast/Minor_Cast_Books_10-13.md`."),
"Kol Kelis Vel": ("K", "(B11): gold-rank messenger in the Cardinas zone. See `07_Characters/Minor_Cast/Minor_Cast_Books_10-13.md`."),
}


def insert_sorted(path, letter_of, entries):
    p = os.path.join(B, *path.split("/"))
    lines = open(p, encoding="utf-8").read().split("\n")
    for name, (letter, rest) in entries.items():
        line = "- **%s** %s" % (name, rest)
        if any(l.startswith("- **%s**" % name) for l in lines):
            continue
        # find section
        sec = None
        for i, l in enumerate(lines):
            if l.startswith("## ") and (l[3:].strip() == letter or (l[3:].strip() == "U-Z" and letter in "UVWXYZ")):
                sec = i
                break
        assert sec is not None, (name, letter)
        j = sec + 1
        last = sec
        pos = None
        while j < len(lines) and not lines[j].startswith("## "):
            m = re.match(r"- \*\*(.+?)\*\*", lines[j])
            if m:
                last = j
                if pos is None and m.group(1).lower() > name.lower():
                    pos = j
            j += 1
        lines.insert(pos if pos is not None else last + 1, line)
    open(p, "w", encoding="utf-8").write("\n".join(lines))


insert_sorted("Appendices/Name_Index.md", None, NAMES)

# Glossary term
p = os.path.join(B, "Appendices", "Glossary.md")
g = open(p, encoding="utf-8").read()
if "**Rejector**" not in g:
    ln = "**Rejector**: the name Builder cultists give Jason (Book 3, Ch31 L45; Book 3, Ch51 L114). **[1]**"
    lines = g.split("\n")
    sec = [i for i, l in enumerate(lines) if l.strip() == "## R"][0]
    j = sec + 1
    pos = None
    last = sec
    while j < len(lines) and not lines[j].startswith("## "):
        m = re.match(r"\*\*(.+?)\*\*", lines[j])
        if m:
            last = j
            if pos is None and m.group(1).lower() > "rejector":
                pos = j
        j += 1
    lines[(pos if pos is not None else last + 2):(pos if pos is not None else last + 2)] = [ln, ""]
    open(p, "w", encoding="utf-8").write("\n".join(lines))
print("ok")

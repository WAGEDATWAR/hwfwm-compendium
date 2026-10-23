import os, re
B = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", ".."))
P = os.path.join(B, "Appendices", "Open_Questions.md")
lines = open(P, encoding="utf-8").read().split("\n")

NEW = {
"1.": "1. **Why did the Ustei come south?** *(Narrowed in the build plan 1.5 pass.)* Known: they raid spirit coin convoys far from home and are nomads from a region to the north (Book 1, Ch83 L4; Book 1, Ch89 L50), and they came south about three years before the Earthlings (Book 12, Ch30 L9). The Adventure Society learned the cause: the desert astral space was failing, the waterfall shutting off in brief isolated instances near the city and much worse in the north, until the oases connected to it could no longer support all the nomad tribes (Book 1, Ch97 L19-21). The tribe was shipped back north in its sand barge (Book 1, Ch109 L8). Not known: the homeland's name, or what disrupted the northern astral space.",
"2.": "2. **Does Marek Nior Vargas lead the Unorthodoxy?** *(Narrowed in the build plan 1.5 pass.)* Known: Marek served Vesta Carmis Zell until recently (Book 10, Ch1 L53) and Jason calls his group \"Marek's Unorthodoxy\" with \"victory or death\" energy (Book 11, Ch2 L75; Book 11, Ch66 L95). It is Boris who explains the movement to messengers and who passes as a branded servant of Vesta Carmis Zell (Book 11, Ch25 L47-55), and Marek's people subordinate themselves to Boris as the Unorthodoxy's \"messiah\" (Book 11, Ch49 L71; Book 11, Ch67 L9). Not known: Marek's standing in the wider movement; the text shows him leading a band, not the whole.",
"3.": "3. **Who does the Unorthodoxy include among astral kings?** *(Narrowed in the build plan 1.5 pass.)* Known: the Council of Kings does not know that Boris is Unorthodoxy, nor how many kings are outside it (Book 11, Ch24 L86); Boris says the original astral kings were not messengers, that the Unorthodoxy has astral kings, and that there are \"too many astral kings for anyone to keep track of\", with the Unorthodoxy ones \"slipping back into the general population\" (Book 11, Ch25 L49-57). One is the king of Navise Den Rigal, a \"rare\" Unorthodoxy king (Book 12, Ch26 L19). Not known: how many, or who besides this one.",
"4.": "4. **Are messengers strictly capped at silver?** *(Resolved in the build plan 1.5 pass.)* No: the cap is a function of the brand. Before the brand there were no limits on rank, and the brand was instituted by messengers who became astral kings (Book 11, Ch25 L51); only at diamond rank can a messenger begin to resist the brand (Book 11, Ch25 L53). A silver-rank seal caps Tera Jun Casta (Book 9, Ch102 L55, L66-67).",
"5.": "5. **What is the debt of Zithis Carrow Vayel?** *(Narrowed in the build plan 1.5 pass.)* Known: while the Builder's world engineers prepare to move the planet, Jamis says \"When this task is complete, the price is paid. Zithis Carrow Vayel will have fulfilled his debt to us\" (Book 10, Ch15 L9), and Erigo says the messengers' ritualists provided \"some low-level ritual magic\" as a service for a reward (Book 10, Ch15 L21-22). So the debt is owed to the astral kings of the Council, for that magic, and ends with the move. Not known: what he owed beyond the magic.",
"6.": "6. **What is Hero's sanction?** *(Narrowed in the build plan 1.5 pass.)* Known: Gwydion tells Gary that Hero has decided to sanction himself and has long considered it (Book 11, Ch68 L707-709). A sanction changes an immortal in some way (Book 13, Ch1017 L11), and Jason says Purity would have sanctioned himself, \"essentially retiring himself and being reborn\" (Book 13, Ch1017 L15). Not known: what Hero becomes or when.",
"8.": "8. **What do the lesser-named great astral beings govern?** *(Narrowed in the build plan 1.5 pass.)* Known: Legion administers the cosmic rules that govern life itself (Book 8, Ch55 L92); the Celestial Book locked off essence combinations after the sundering (Book 11, Ch68 L1580) and is venerated through a loose network tied to the Magic Society and the Church of Knowledge (Book 9, Ch65 L30); the Reaper is the god of finality of death (Book 2, Ch25 L67). The Celestial Book, the Seeker of Songs, the Whisper in Corners and Legion take part in the Book 11 gathering (Book 11, Ch65 L75; Book 11, Ch68 L159). Not known: the domains of the Whisper in Corners, the Word in the Silence and the Seeker of Songs.",
"9.": "9. **What does the Firmamental Bridge Anchor do?** *(Resolved in the build plan 1.5 pass.)* Dawn identifies it as something Jason can use to establish the bridge, and says using it consumes the authority in the item, so it is single-use and the great astral beings will not object to it (Book 8, Ch51 L66). Jason also calls it a \"firmament bridge anchor\" (Book 8, Ch51 L30).",
"10.": "10. **Why can Jason not keep the Fundamental Realm Authority Token?** *(Resolved in the build plan 1.5 pass.)* Dawn says it is a major demonstration of the Builder's failure and that great astral beings will not tolerate a mortal holding it, so he must give it back (Book 8, Ch51 L68-74). Jason trades it for concessions, including one opening of the way into the fundamental realm, and transfers the authority to the Builder (Book 8, Ch54 L54, L60-61, L99).",
"11.": "11. **How did Disguise take part in recruiting the Network's founder?** *(Resolved in the build plan 1.5 pass.)* Jason explains that Knowledge helped Disguise pose as Purity and, in return for help including the elimination of Purity's troublesome followers, \"the fake Purity brought an outworlder from Earth into his church\" (Book 13, Ch1017 L17-19). Not known: how the founder was chosen.",
"13.": "13. **How strong is Vitesse's magic?** Known: it is a high-magic city whose manifestations are powerful and frequent (Book 12, Ch43 L47), the magic around it is strong enough for a cloud ship to fly (Book 12, Ch43 L46), and iron-rankers in high-magic areas are not allowed to hunt alone (Book 2, Ch53 L27). Vehicles that need a special power in weak-magic Greenstone run on ambient magic in high-magic zones (Book 7, Ch25 L3). Not known: a figure.",
"19.": "19. **How long has the vampire war lasted?** *(Narrowed in the build plan 1.5 pass.)* Known: the first vampire war \"ended without conclusion\" when both sides were exhausted and the vampires got nuclear weapons (Book 13, Ch987 L63); the war was back \"in full swing\" (Book 13, Ch988 L26) and a character places the symposium \"two years into the renewed vampire war\" (Book 13, Ch995 L69). Jason says the operation will bring it to a final conclusion (Book 13, Ch1002 L64), and it ended in the months before the farewell (Book 13, Ch1023 L12). Simon McKean says it has been fought \"off and on for decades\" (Book 13, Ch1002 L69). Not known: the first war's length.",
"20.": "20. **Where does the Order of the Reaper survive?** Known: a coalition of churches wiped out the original order centuries ago (Book 2, Ch25 L73; Book 13, Ch1017 L18); the new structure persists as a volunteer network of quiet allies, with the trials as a lure (Book 2, Ch60 L120-122), and Jason fears \"the Order of the Reaper that still existed\" (Book 2, Ch60 L185). Not known: its present strength or members beyond Shade.",
"22.": "22. **Where does the Adventure Society's continental council sit?** *(Narrowed in the build plan 1.5 pass; the text disagrees with itself.)* Known: Book 6 puts it in Vitesse, \"rather than the capital city, Cyrion\" (Book 6, Ch47 L604); Book 6 also calls Rakesh, on the north coast of the Africa-like continent, \"the home of the Adventure Society's continental council\" (Book 6, Ch47 L623); Book 7 calls Cyrion \"home to the Adventure Society's continental council\" (Book 7, Ch43 L58). Greenstone's inquiries come from \"the Continental Council\" (Book 2, Ch10 L51; Book 12, Ch36 L51). Rakesh sits on Greenstone's continent and Vitesse and Cyrion on Estercost's, so two councils (one per continent) are possible, but Vitesse against Cyrion is a direct conflict inside Estercost that the text never explains. Compendium rule: use \"the continental council\" without naming a city unless the story needs one.",
}
out = []
hit = set()
for l in lines:
    m = re.match(r"^(\d+a?\.) \*\*", l)
    if m and m.group(1) in NEW:
        out.append(NEW[m.group(1)]); hit.add(m.group(1))
    else:
        out.append(l)
assert hit == set(NEW), set(NEW) - hit
open(P, "w", encoding="utf-8").write("\n".join(out))


def edit(rel, pairs):
    p = os.path.join(B, *rel.split("/"))
    s = open(p, encoding="utf-8").read()
    for o, n in pairs:
        assert o in s, (rel, o[:70])
        s = s.replace(o, n, 1)
    open(p, "w", encoding="utf-8").write(s)


edit("08_History_and_Timeline/Book_13_Timeline.md", [(
    "- **Open note**: the chapter-summary notes mention a \"two years into the renewed vampire war\" line at Ch995; the lines checked here (the symposium exchange and the report of Bahrain's vanished government) do not show it, so it is not asserted.",
    "- **The renewed vampire war**: a character places the symposium \"two years into the renewed vampire war\" (Book 13, Ch995 L69). The first vampire war ended without conclusion (Book 13, Ch987 L63), and the renewed phase ended in the months before the farewell (Book 13, Ch1023 L12).")])
edit("08_History_and_Timeline/Master_Timeline.md", [(
    "The \"two years into the renewed vampire war\" line from the chapter notes was not found at Ch995 (see `Book_13_Timeline.md`).",
    "The renewed war is placed \"two years\" in at Book 13, Ch995 L69 (see `Book_13_Timeline.md`).")])
print("ok")

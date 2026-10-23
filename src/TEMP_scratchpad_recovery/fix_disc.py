import os, io, sys
from mkchar import mk, BASE

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace") if False else sys.stdout


def edit(rel, pairs):
    p = os.path.join(BASE, rel)
    s = open(p, encoding="utf-8").read()
    for o, n in pairs:
        if o not in s:
            print("MISSING", rel, o[:60])
            continue
        s = s.replace(o, n, 1)
    open(p, "w", encoding="utf-8").write(s)
    print("ok", rel)


mk("Miriam_Vance.md", "Miriam Vance", "3", "Book 10", "Book 11", "Books 10, 11 (chapter files)",
   "Allayeth.md, Jason_Asano.md, Clive_Standish.md, ../06_Places/Astral_Spaces/Transformation_Zones.md",
   "The gold-rank leader of Team Moon's Edge and Tactical Commander of the Cardinas expedition, who shares overall command with Jason.",
   ["Introduced as \"the leader of Team Moon's Edge, Miriam Vance\" (Book 10, Ch59 L17). Moon's Edge is a team of six women, all gold rank, raised and supervised by Allayeth from early in their careers (Book 10, Ch51 L43; Book 10, Ch59 L4).",
    "She is the expedition's Tactical Commander and tells Jason no when he wants to add his butterflies to a messy flying battle (Book 10, Ch61 L45; Book 10, Ch69 L19). Her gold-rank senses read Jason's emotions through his aura (Book 10, Ch68 L10).",
    "She notices how Allayeth acts around Jason (Book 10, Ch64 L22), questions him about astral kings and the goddess (Book 10, Ch65 L60; Book 10, Ch67 L64), and argues with him over command (Book 10, Ch76 L3). Death addresses her by name (Book 10, Ch85 L38).",
    "She runs the withdrawal through the citadel tunnels as overall commander (Book 10, Ch82 L58) and sets the defensive perimeter (Book 10, Ch80 L33).",
    "In Book 11 she is the zone's co-commander with Jason (Book 11, Ch19 L56; Book 11, Ch49 L79), directs Moon's Edge to destroy the tree crystals (Book 11, Ch51 L64; Book 11, Ch52 L10) and protects the non-combatants in Ramona's invisibility sphere when Amos Pensinata goes into the orb (Book 11, Ch53 L25; Book 11, Ch55 L3).",
    "Her team \"was the most powerful force on the battlefield other than the cloud buildings and the two divine entities\" (Book 11, Ch32 L75).",
    "Jason introduces her to Gordon, his avatar of doom (Book 11, Ch33 L20). A different Miriam, Miriam Coyle, heads a magitech weapons institute in Book 13 (Book 13, Ch995 L14)."],
   "Disciplined, direct and unwilling to take chaos on trust; she argues with Jason as an equal.",
   timeline=["Book 10: leads Moon's Edge on the Cardinas expedition (Book 10, Ch59-85).", "Book 11: co-commands the zone (Book 11, Ch19-57)."])

edit("07_Characters/Sigrid_Freyn.md", [
    ("When the Mirror King collects Valdis, Sigrid greets him as \"Father\" and confirms \"He is my father\" (Book 3, Ch5 L51-53); the text does not explain this given her later marriage to Valdis.",
     "When the Mirror King collects Valdis, Sigrid greets Hastor, the king's portal specialist, as \"Father\" and confirms \"He is my father\" (Book 3, Ch5 L49-53, L57-58); the king himself is her father-in-law after her marriage (Book 12, Ch15 L8-10)."),
    ("open_q=", "open_q="),
    ("- Why she calls the Mirror King \"Father\" in Book 3.", "- Whether Hastor is still the king's portal specialist in Book 12; the text calls the specialist only \"the Mirror King's own portal specialist\" (Book 12, Ch15 L8)."),
    ("Valdis's father the Mirror King is her father-in-law;", "Hastor is her father;"),
])
edit("07_Characters/Allayeth.md", [
    ("she raised the team Moon's Edge herself (Book 12, Ch16 L8).",
     "she raised the team Moon's Edge herself (Book 12, Ch16 L8), though Miriam Vance leads it (Book 10, Ch59 L17)."),
])
edit("04_Peoples_and_Cultures/Yaresh_Culture.md", [
    ("who leads Moon's Edge (Book 12, Ch16 L8)", "who raised the all-woman team Moon's Edge, led by Miriam Vance (Book 12, Ch16 L8; Book 10, Ch59 L17)"),
])
edit("Appendices/Glossary.md", [
    ("**Moon's Edge**: team that includes Miriam and Ramona (Book 11, Ch46 L11) and is led by Allayeth in Book 12 (Book 12, Ch16 L8); the sources differ on who leads it. **[3]**",
     "**Moon's Edge**: Yaresh team of six gold-rank women raised by Allayeth and led by Miriam Vance (Book 10, Ch51 L43; Book 10, Ch59 L17); members include Ramona the ritualist and shield specialist, Valetta and the berserker Alice (Book 10, Ch63 L16; Book 10, Ch71 L39; Book 10, Ch81 L34). **[3]**"),
])
edit("07_Characters/Minor_Cast/Minor_Cast_Order_of_Redeeming_Light.md", [
    (" She later projects a dome in Miriam's team, Moon's Edge (Book 11, Ch46 L11).", " A Ramona on Miriam Vance's team, Moon's Edge, is a gold-rank shield specialist and ritualist (Book 11, Ch46 L11); the text does not link her to this Ramona, so treat them as two people."),
])
edit("07_Characters/Minor_Cast/Minor_Cast_Books_7-9.md", [
    ("Ramona later joins Miriam's team, Moon's Edge, as a gold-ranker (Book 11, Ch46 L11). ", "A Ramona on Miriam Vance's team, Moon's Edge, is a different person unless the text says otherwise (Book 11, Ch46 L11). "),
])
edit("06_Places/Greenstone.md", [
    (", answering to the Duke,", " (the Duke rules the city, Book 1, Ch36 L71; that the mayor answers to him is an inference),"),
])

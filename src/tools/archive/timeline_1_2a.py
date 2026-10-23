import os
B = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", ".."))
P = os.path.join(B, "08_History_and_Timeline", "Book_12_Timeline.md")
s = open(P, encoding="utf-8").read().split("\n")


def after(prefix, rows, before=False):
    global s
    idx = [i for i, l in enumerate(s) if l.startswith(prefix)]
    assert len(idx) == 1, (prefix, idx)
    k = idx[0] if before else idx[0] + 1
    s[k:k] = rows


after("| Return | Ch3 |", [
    "| Return | Ch3 | Nigel's nine-person team, working mostly for Anna Tilden, is embedded in France watching the edge of Saint-Étienne for something big (Book 12, Ch3 L7, L13, L82) |",
    "| Return | Ch4 | The sky over the old clan territory turns orange and blue under a huge eye, and Nigel Thornton goes in alone while his team falls back (Book 12, Ch4 L3, L14 to L17). Jason shrouds him in mist and answers, \"Can't really talk, Nigel; I'm in the middle of a thing\" (Book 12, Ch4 L28 to L31). Jason drains the vampires' blood, and the blood rain turned to light leaves Nigel alone in a silent city (Book 12, Ch4 L40, L49 to L53) |",
])
after("| Yaresh | Ch17 to Ch19 |", [
    "| Yaresh | Ch18 | In the mirage chamber, Jason fills the arena with darkness and shadow-armed figures while Prince Valdis, a gold-rank sword master, fights through them (Book 12, Ch18 L6 to L12). Jason's attacks inflict Sin, which Valdis's Sword Soul absorbs (Book 12, Ch18 L16, L37, L45). Valdis's Cross Slash passes through Jason's body (Book 12, Ch18 L70) |",
    "| Yaresh | Ch19 | Jason's body reforms from strands of blood, and his cloak becomes a portal that his attacks vanish into (Book 12, Ch19 L6 to L7). Emir and Constance watch from the lobby (Book 12, Ch19 L9). Jason drains the afterimages' life force and then challenges Valdis to a sword duel (Book 12, Ch19 L58, L61, L73 to L75). Valdis yields when his Sword Soul gives out (Book 12, Ch19 L81) |",
])
after("| Touring south | Ch24 |", [
    "| Touring south | Ch25 | After the battle, General Millicent Marks on the Segurado magic tower meets Danielle Geller, who asks to be called Danielle (Book 12, Ch25 L3, L5 to L12). The Team Biscuit cook, John Miller, feeds her at a stall (Book 12, Ch25 L63, L66) |",
])
after("| Greenstone | Ch32 |", [
    "| Boko | Ch31 | Li Mei stands frozen as Jason, with Estella and Belinda nearby, comes to meet her (Book 12, Ch31 L3, L7, L11 to L12). Jason tells her they are there to decide what happens to her, and asks about an operation the local authorities fear is raising an undead army (Book 12, Ch31 L62, L97) |",
], before=True)
after("| Boko | Ch34 |", [
    "| Boko | Ch35 | Jamis Fran Muskar of the Council of Kings meets Jason to apologise for the deaths in Boko and says the two will know each other for longer than time can measure (Book 12, Ch35 L6, L8, L11). Jason refuses a proposal to blunt his fury by giving up areas, and refuses to slaughter a quarter of a million messengers to restore his ghost phoenix form (Book 12, Ch35 L66, L84, L88) |",
])
after("| Earth, meanwhile | Ch40 |", [
    "| Earth, meanwhile | Ch41 | Ketevan drives Anna and Susan through the French domain, where the vampires' occupation has been cleaned up and the astral space is still partly inhabited (Book 12, Ch41 L3, L7 to L9). Nigel tells of the blood rain and of Jason's avatar finding him afterwards, and of talking about the team joining the clan (Book 12, Ch41 L42, L45). Jason explains a transformation zone as \"a scab, over an open wound in the side of the universe\" (Book 12, Ch41 L61) |",
    "| Earth, meanwhile | Ch42 | In a park, Anna sees a grown Emi and the leonid Gary (Book 12, Ch42 L4 to L5, L11 to L13). After three days of briefings, Anna and Susan discuss whether Jason is straight with them (Book 12, Ch42 L21, L65, L70). Jason, in a pink flowered apron in their guest-house kitchen, repeats his job offer to Anna (Book 12, Ch42 L72, L82) |",
])
after("| Vitesse | Ch43 |", [
    "| Vitesse | Ch44 | The guild's intake clerk Monica interviews Jason for Burning Violet membership, noting the application goes to an executive for an in-depth interview (Book 12, Ch44 L4, L20). She mentions that the Gellers' Casselton Beach facility has produced exceptional adventurers (Book 12, Ch44 L62) |",
    "| Vitesse | Ch45 | Lord Neiman Bassingthwaite apologises for the reception and warns of two factions in the guild executive, saying Jason's membership could be the flashpoint (Book 12, Ch45 L3 to L4, L8, L12, L14). Arabelle and Gabriel Remore join the discussion (Book 12, Ch45 L55, L62) |",
])
after("| System withdrawal | Ch51 |", [
    "| System withdrawal | Ch52 | Ben Headingway leads nine adventurers from the noble houses of Cyrion with missing people to Jason's cloud palace, refusing to enter where Jason has all the power (Book 12, Ch52 L3, L6, L8). Jason says he does not have their people and points them to Sadi Andali (Book 12, Ch52 L35). The search of a desert town there turns up none of the family members (Book 12, Ch52 L44, L48) |",
])
after("| Sky Link island | Ch58 |", [
    "| Interstice | Ch57 | Jota Withers, a pirate captain raised in the feeder programme of a peripheral universe, reflects on his life and his ship's transition into the Jakaar fleet's holdout (Book 12, Ch57 L3, L7, L22). His pirate admiral Aractus hands him a file on a world sealed to anyone over silver rank, now opened to gold-rankers by the World-Phoenix (Book 12, Ch57 L36 to L38). An outworlder was \"sucked off\" the restricted world a couple of years ago and is heading back, and the locals' invitation lets the pirates in free of the rules (Book 12, Ch57 L58 to L62) |",
    "| Jason's ship | Ch57 | Melody, recovering in a cloud bed after living in Jason's soul realm for years, is reunited with Sophie; the healers expect a slow but full recovery (Book 12, Ch57 L24 to L28, L30) |",
], before=True)
open(P, "w", encoding="utf-8").write("\n".join(s))
print("ok")

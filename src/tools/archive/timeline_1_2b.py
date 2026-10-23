import os
B = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", ".."))
P = os.path.join(B, "08_History_and_Timeline", "Book_13_Timeline.md")
s = open(P, encoding="utf-8").read().split("\n")


def after(prefix, rows, before=False):
    global s
    idx = [i for i, l in enumerate(s) if l.startswith(prefix)]
    assert len(idx) == 1, (prefix, idx)
    k = idx[0] if before else idx[0] + 1
    s[k:k] = rows


R = "Book 13, "
after("| Asano Village | Ch960 |", [
    "| Asano Village | Ch961 | In the village auditorium, Clive, Audrey and others brief the clan on the vampires' blood oaks, which make splitting up teams more dangerous (Book 13, Ch961 L3 to L5). The first plan, an alpha-strike on vampire strongholds to seize nuclear devices, is no longer viable after the Melbourne event (Book 13, Ch961 L6 to L7). Jason meets a circle of officials, intelligence directors and faction heads that includes Boris for the Cabal (Book 13, Ch961 L58) |",
    "| Asano Village | Ch962 | A formal expedition of intelligence officers and scientists tours Jason's astral kingdom under the Concierge (Book 13, Ch962 L5). Sophie's mother Melody Jain, out of her coma after surgery to remove the substance that had influenced her mind, is back on her feet (Book 13, Ch962 L6). Arbour is a city in a volcanic caldera in the icy north of the planet, and Melody lives in a treehouse there (Book 13, Ch962 L44, L62) |",
])
after("| Weeks of the return | Ch964 |", [
    "| Weeks of the return | Ch965 | Monsters pour out of the manifestation in Pakistan, silver rank mostly and gold at one in a hundred (Book 13, Ch965 L3). Elizabeth asks whether it is a monster wave (Book 13, Ch965 L42). Humphrey rolls his summoner's dice on the dam and calls up giant toads (Book 13, Ch965 L50, L71) |",
    "| Weeks of the return | Ch966 | Onslow's shell has become a command post and triage tent (Book 13, Ch966 L3). Jason lands exhausted but uninjured (Book 13, Ch966 L4 to L5). Elsewhere, Marie pours Elizabeth a glass of blood from a decanter in a ritual circle, and a speaker recalls warning the conspirators after what Jason did to the vampires in France and Slovenia (Book 13, Ch966 L41, L55) |",
    "| Weeks of the return | Ch967 | Jason, recovering from the spiritual strain of holding shut the rip in the universe, cooks for friends and family on a deck over the gorge (Book 13, Ch967 L3 to L4). The visiting delegations reach New Water and Arbour (Book 13, Ch967 L10). American officials decide to approach Jason through friendship (Book 13, Ch967 L32) |",
])
after("| Weeks of the return | Ch969 |", [
    "| Weeks of the return | Ch970 | Farrah briefs a room of specialists on how the Engineers of Ascension's sabotage of the grid ended the secrecy of magic (Book 13, Ch970 L3 to L5). A team reports a possible transformation-zone site in the western Pyrenees, no more than eleven months old (Book 13, Ch970 L29) |",
])
after("| Months after return | Ch975 |", [
    "| Months after return | Ch976 | Jason fights the gold-rank Amstutz and others on and around a bus while the silver-rank Geneva watches (Book 13, Ch976 L5 to L7). His afflictions multiply until the gold-rankers weaken, and Bussinger watches as he touches the survivors with his sword (Book 13, Ch976 L63, L80) |",
])
after("| Months after return | Ch977 |", [
    "| Months after return | Ch978 | Jason tells Geneva that he intends to round up everyone involved, and that his contingencies are to limit the damage if he conquers the world (Book 13, Ch978 L3 to L8). The team works on the vault, and Danielle stresses the moral high ground for the forceful intervention (Book 13, Ch978 L13, L21) |",
    "| Months after return | Ch979 | Both of Jason's territories on Earth have a central tower, and the Saint-Étienne tower's face changes often (Book 13, Ch979 L3 to L6, L9). Investigators find that Marie Finnegan ran a tight operation with few in the know, and that part of it sits on a submarine (Book 13, Ch979 L64, L76) |",
])
after("| Months after return | Ch980 |", [
    "| Months after return | Ch981 | With Bussinger now working with Carlos, Jason takes time alone in Slovakia among his board games (Book 13, Ch981 L3, L5 to L6). Shade tells him not to feel aggrieved for Jack Gerling, whose trapped soul would be tortured (Book 13, Ch981 L7, L11) |",
])
after("| Months after return | Ch982 |", [
    "| Months after return | Ch983 | On Elizabeth's order Gerling opens a box in the submarine's testing room, and a red tentacle spears him (Book 13, Ch983 L3, L15). Elizabeth punches through the hull to leave (Book 13, Ch983 L24). On a plane, Sophie and Jason save passengers when the front of the aircraft bursts open (Book 13, Ch983 L84, L92) |",
    "| Months after return | Ch984 | Elizabeth is pinned to a wall after a sword smashes Marie's stone slab, and two intruders take her away (Book 13, Ch984 L3 to L10). In a hologram meeting, CIA Director Barstow reports no consensus on action against the vampires (Book 13, Ch984 L12 to L13). Zara leads Marie and the other prisoners to a portal, where Jason appears (Book 13, Ch984 L62 to L66) |",
])
after("| Months after return | Ch985 |", [
    "| Months after return | Ch986 | Zara and Jason eat in a bistro in the vampire city, and she expects a new, wider vampire war because Elizabeth has seeded hidden weapons (Book 13, Ch986 L3, L6). Craig Vermillion arrives (Book 13, Ch986 L27) |",
])
after("| Months after return | Ch988 |", [
    "| Months after return | Ch989 | Delia DeWitt, a young Global Defence Network essence user, faces a manifestation that appeared in the grounds of a cathedral (Book 13, Ch989 L3 to L6). Lenora Coleman and Barry Sinise in the old mayoral residence see a dark figure speak with Jason's voice (Book 13, Ch989 L50, L68) |",
    "| Months after return | Ch990 | Jason heals Delia with a potion of Jory's, explains forcible turnings and the window to purge the vampiric curse, and calls her scars the mark of a defining choice (Book 13, Ch990 L3 to L5, L21, L65). He learns that the attack was one of several along the edge of vampire-held territory (Book 13, Ch990 L86) |",
])
after("| Later | Ch992 |", [
    "| Later | Ch993 | Jason and Raythe talk on the deck of his house in the waterfall gorge (Book 13, Ch993 L3 to L5). Jason tells Danielle that the diamond-rank messenger who came to kill him and arrived at his feet already dead was Raythe (Book 13, Ch993 L109) |",
])
after("| Later | Ch1001 |", [
    "| Later | Ch1002 | Lieutenant Bradley Noble, a military liaison, walks the clan's cloud city and sees Jason appear in a conference room, where Yumi scolds him as \"Grandmother\" (Book 13, Ch1002 L3 to L6, L30 to L32). Jason promises to explain everything once Simon McKean and the vampires are dealt with (Book 13, Ch1002 L68) |",
])
after("| Operation planned | Ch1004 |", [
    "| Operation planned | Ch1005 | Jason walks with his father in the clan's Slovakian tower and is told that people feel his presence but rarely see him, so he might hold a bowling night (Book 13, Ch1005 L3, L10 to L16). He then heads for the portal to the astral space of the refugee vampires and their city of night (Book 13, Ch1005 L80) |",
])
after("| Operation | Ch1006 |", [
    "| Operation | Ch1007 | The offensive against Belgrade, the largest European city under full vampire control, begins with a bombardment and a drop of enhanced soldiers (Book 13, Ch1007 L3 to L5). Prince Valdis lands with the paratroopers, and blood-red vines break through the asphalt (Book 13, Ch1007 L6, L13). Underground, Nigel reports silver-rank vampires and no lords yet (Book 13, Ch1007 L41) |",
])
after("| McKean's castle | Ch1009 |", [
    "| McKean's castle | Ch1010 | Simon McKean watches Jason and two familiars walk the tunnels of his complex beneath the French castle, with the third familiar, an apocalypse beast, wandering above (Book 13, Ch1010 L3, L5). Jason defeats the gold-rank vampires and ends the massacre with a spell (Book 13, Ch1010 L61, L69) |",
    "| McKean's castle | Ch1011 | Farrah, Belinda and others infiltrate the facility and find research on grafting vampire flesh onto blood oaks (Book 13, Ch1011 L18, L25, L44). Gerling waits in the dark of a bunker beneath blood-dripping vines (Book 13, Ch1011 L69) |",
])
after("| McKean's castle | Ch1013 |", [
    "| McKean's castle | Ch1014 | Jason hangs trapped in blood vines while Gerling confronts him (Book 13, Ch1014 L3 to L5). The cloud ship warns of turbulence as Jason exerts the influence of his true self, and the castle rises from the earth (Book 13, Ch1014 L17, L34). Jason touches Gerling's forehead and he liquefies (Book 13, Ch1014 L72). McKean sees a vortex of rainbow light where the portal had been (Book 13, Ch1014 L91) |",
])
after("| Briefing | Ch1017 |", [
    "| Briefing | Ch1016 | Rufus sits at an outdoor tea house with Clive, Lorelei and a Pakistani man whom Jason takes for a doctor, until Jason arrives (Book 13, Ch1016 L3, L21). Jason's close circle gathers at the Academy, with the messengers Tera Jun Casta and Jali Corrik Fen wary of Boris (Book 13, Ch1016 L107, L119) |",
], before=True)
open(P, "w", encoding="utf-8").write("\n".join(s))
print("ok")

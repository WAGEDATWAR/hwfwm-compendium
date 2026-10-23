import os
BASE = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".."))
C = os.path.join(BASE, "07_Characters")


def edit(fn, pairs):
    p = os.path.join(C, fn)
    s = open(p, encoding="utf-8").read()
    for o, n in pairs:
        if o not in s:
            print("MISSING", fn, o[:60])
            continue
        s = s.replace(o, n, 1)
    open(p, "w", encoding="utf-8").write(s)
    print("ok", fn)


edit("Amos_Pensinata.md", [
    ("- Orin Pensinata is named in Book 9 as leading a team that stays outside while others go below (Book 9, Ch24 L48); no relation is stated in the lines checked.",
     "- His nephew is Orin Pensinata (Book 7, Ch47 L39; see `Orin_Pensinata.md`); he joins Jason's journey partly because Orin insisted on coming (Book 9, Ch24 L35).\n- Jason extracts him from his attempted \"suicide-by-messenger\" and the gold-rankers escape into Jason's soul realm (Book 11, Ch55 L3). After the zone he takes Orin and the scout Rosa back to Rimaros (Book 11, Ch68 L378)."),
    ("- His fate after entering the orb (Book 11, Ch54) and his relation to Orin Pensinata.",
     "- What he tells Jason in the dinghy (Book 11, Ch49 L86) is not summarised here."),
    ("In Book 11 he does not flee with the other gold-rankers but goes into the water orb",
     "In Book 11 he grows troubled (Book 11, Ch49 L86), does not flee with the other gold-rankers but goes into the water orb"),
])

edit("Adrien_Barbou.md", [
    ("tells Anna to retire the \"bad apple\" excuse (Book 13, Ch968 L34-38).",
     "tells Anna to retire the \"bad apple\" excuse (Book 13, Ch968 L34-38). Jason brought him out of the zone alive; Mr North asked for a quick death and Jason left the decision to Farrah, who describes disposing of bodies without denying what she did (Book 13, Ch968 L45-54), so Anna concludes \"Barbou isn't alive\" (Book 13, Ch968 L54). In Book 6 Anna did not know his fate (Book 6, Ch47 L46)."),
    ("- His final fate is not found in the lines checked.",
     "- Farrah never says outright that she killed him; the scene implies it (Book 13, Ch968 L47-54)."),
])

edit("Killian_Laurent.md", [
    ("Havi plans to deliver him on a plate (Book 9, Ch4 L11-12).",
     "Havi plans to deliver him on a plate, but Killian captures Havi first (Book 9, Ch4 L11-39). Jason's team then takes Killian and chains him in a ritual array; Jason tells him \"I hope we never see each other again\" (Book 9, Ch5 L4-99). In Book 10 Jason guesses he is in a Magic Society basement, parcelling out information to stay alive (Book 10, Ch58 L106)."),
    ("- His final fate is not found in the lines checked.",
     "- Where he is held after Book 9 and whether he escapes; Book 10, Ch58 L106 is only Jason's guess."),
])

edit("Minor_Cast/Minor_Cast_Books_7-9.md", [
    ("- **Order of Redeeming Light personnel**", "- **Order of Redeeming Light personnel**") ,
])

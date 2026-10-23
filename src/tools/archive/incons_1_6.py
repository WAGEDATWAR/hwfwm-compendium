import os
B = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", ".."))


def edit(rel, pairs):
    p = os.path.join(B, *rel.split("/"))
    s = open(p, encoding="utf-8").read()
    for o, n in pairs:
        if o not in s and n in s:
            continue
        assert o in s, (rel, o[:70])
        s = s.replace(o, n, 1)
    open(p, "w", encoding="utf-8").write(s)


edit("03_Magic_and_Adventuring/Confluences.md", [(
    "| Garuda | might, swift, bird; or might, wing | Taika (Book 4, Ch65 L22, L28; Book 9, Ch78 L107) |",
    "| Garuda | might, swift, bird (Taika's first choice); might, swift, wing (what Jason traded for) | Taika (Book 4, Ch65 L22, L28; Book 9, Ch78 L107). The two passages are one change of plan, not a contradiction |")])
edit("09_Items_and_Artefacts/Tokens_Stones_and_Relics.md", [(
    "crafted by a god to bestow a specific aura power (Book 2, Ch13 L60).",
    "crafted by a god to bestow a specific aura power (Book 2, Ch13 L60). The stone's effect line names the ability [Inescapable Doom] (Book 2, Ch13 L62) but its ability description names [Inevitable Demise] (Book 2, Ch13 L66); the compendium uses Inevitable Demise and treats the other as a variant, since no later list shows either.")])
edit("03_Magic_and_Adventuring/Awakening_Stones.md", [(
    "a Divine Awakening Stone of Inevitability, to bestow an aura power (Book 2, Ch13 L60-62),",
    "a Divine Awakening Stone of Inevitability, to bestow an aura power (Book 2, Ch13 L60-62; the ability is [Inescapable Doom] in one line and [Inevitable Demise] in another, Book 2, Ch13 L62, L66),")])
edit("07_Characters/Melody_Jain.md", [(
    "- Faked her death twenty years before Book 6, using a wall panel in Marta Fries's house in Kurdansk (Book 6, Ch47 L510-513).",
    "- Faked her death twenty years before Book 6, using a wall panel in Marta Fries's house in Kurdansk (Book 6, Ch47 L510-513). Arabelle dates the start of the same story \"around a quarter of a century ago\" (Book 9, Ch27 L24); the two figures count different moments (the story's beginning, then the faked death) and are consistent.")])
edit("08_History_and_Timeline/Master_Timeline.md", [(
    "- **Open - clan hiding period**: \"half a decade\" is confirmed (Book 12, Ch1 L93); \"two years\" is unchecked.",
    "- **Resolved - clan hiding period**: the figures are snapshots at different dates, not a conflict. The clan \"had not been heard from in two years\" at the end of Book 11 (Book 11, Ch68 L2260), \"half a decade\" at the opening of Book 12 (Book 12, Ch1 L93), and the city of Nitra shows \"more than a decade of abandonment\" by the Book 12 arrival (Book 12, Ch59 L5).")])
edit("00_Project_Structure.md", [
    ("- **Gary's death timing**: \"about a year\" after the Cup of Heroes in the notes; confirm the exact wording (Book 11, Ch74).",
     "- **Gary's death timing** *(resolved)*: \"Almost a year later\" after he became a demigod (Book 11, Ch68 L703); Book 11 has no Ch74."),
    ("- **Clan hiding period (Book 12)**: described as \"half a decade\" in one place and \"two years\" in another.",
     "- **Clan hiding period** *(resolved)*: \"two years\" (Book 11, Ch68 L2260) and \"half a decade\" (Book 12, Ch1 L93) are snapshots at different dates; see the Master Timeline, section 7."),
    ("- **Soul forge**: Jason's realm lacks one until the Book 11 reintegration, although Book 8 and Book 12 appendices list soul forge among the Relics of the King.",
     "- **Soul forge** *(resolved)*: Jason's realm lacks one until the Book 11 reintegration (Book 10, Ch53 L17), and the Relics of the King gift gives access to the astral throne, astral gate and soul forge only \"to limited degrees\" (Book 12, Ch67 L198), so the appendix lists do not conflict."),
])
edit("Appendices/Glossary.md", [(
    "### Not variants",
    """### Text inconsistencies and rulings

| Item | The two readings | Ruling |
|---|---|---|
| Taika's garuda route | might, swift, bird (Book 4, Ch65 L22) against might, swift, wing (Book 4, Ch65 L28) | One change of plan: Jason traded for the wing essence. Not a contradiction |
| The Inevitability stone's ability | [Inescapable Doom] (Book 2, Ch13 L62) against [Inevitable Demise] (Book 2, Ch13 L66) | Use Inevitable Demise; treat Inescapable Doom as a variant |
| Melody Jain's dates | "a quarter of a century ago" (Book 9, Ch27 L24) against two decades (Book 6, Ch47 L510) | Different moments of one story; consistent |
| The clan's hiding | two years (Book 11, Ch68 L2260), half a decade (Book 12, Ch1 L93), more than a decade (Book 12, Ch59 L5) | Snapshots at different dates |
| Seat of the Adventure Society's continental council | Vitesse (Book 6, Ch47 L604), Rakesh (Book 6, Ch47 L623), Cyrion (Book 7, Ch43 L58) | An inconsistency in the text; do not name a city (Open_Questions 22) |

### Not variants""")])
print("ok")

root = r"C:\Users\Gabriel\Documents\World Stuff\HWFWM Compendium"

def sub(rel, pairs):
    p = root + "\\" + rel
    s = open(p, encoding="utf-8").read()
    for a, b in pairs:
        assert a in s, (rel, a[:70])
        s = s.replace(a, b)
    open(p, "w", encoding="utf-8").write(s)

sub(r"03_Magic_and_Adventuring\Magic_and_Adventuring.md", [
 ("- **Badges** (rank-coloured medallions, e.g. Rufus's bronze one) are touched to a posted notice to copy it onto paper;",
  "- **Badges** are circular medallions embossed with the Society's sword and rod crossed over a shield (an iron one for a new member such as Jason, a bronze one for Rufus, Book 1, confirmed) and are touched to a posted notice to copy it onto paper;"),
 ("- **Guilds** such as Burning Violet and Sapphire Crown are adventuring guilds that appear throughout the books.",
  "- **Guilds** such as Burning Violet and Sapphire Crown recruit elites. During the Book 7 surge Rufus says that in a city like Livaros about three in ten adventurers are in a guild and one in ten in a high-end guild, yet guilds are given sixty percent of the quotas (confirmed). See `05_Organisations/Adventure_Society.md`."),
])

sub(r"06_Places\Yaresh.md", [
 (" The lorebook mentions a powerful Aristocratic Faction; the books I searched do not use that term.",
  " The Aristocratic Faction, a bloc of wealthy aristocrats and merchant barons who own most of the land and provide most of the jobs, is the dominant political force in the region (Book 10, confirmed); see `05_Organisations/Guilds_and_Houses.md`."),
])

sub(r"06_Places\00_Places_Overview.md", [
 ("The Adventure Society's continental council sits in Cyrion (Book 6).",
  "Book 6 places the continental council of the Africa-like continent at Rakesh, and a different passage places an Adventure Society continental council in Cyrion, so there appears to be one council per continent."),
])

sub(r"06_Places\Earth\Nitra.md", [
 ("Whether it is powered by steam on fire and water quintessence is unchecked.",
  "Its steam engines are driven by a mix of fire and water quintessence, not coal, in a blend of Victorian and modern technology with magic that does not respect real physics (Book 11, confirmed)."),
])

sub(r"05_Organisations\Magic_Society_and_Associations.md", [
 ("(Book 7 mentions its public access suspended after the attack on Yaresh)", "(Belinda says in Book 10 that the chambers have been closed to the public since the attack on Yaresh)"),
])

# TODO: drop confirmed items and add Organisations section
p = root + r"\TODO_Verification.md"
s = open(p, encoding="utf-8").read()
removals = [
 "- Yaresh: the duke's name; whether an \"Aristocratic Faction\" exists under that or another name.\n",
 "- Nitra: quintessence-powered steam.\n",
 "- Guild proportions (about 30% of adventurers in guilds, 10% in high-end ones); guilds' share of contracts. Check Books 6-7 (Burning Violet) and 7-11 (Sapphire Crown).\n",
 "- The badge design (sword and rod over a shield); only rank-coloured medallions are confirmed.\n",
]
for r in removals:
    if r in s:
        s = s.replace(r, "")
    else:
        print("not found:", r[:60])
s = s.replace("- Which city holds the Geller family tower that appears in Book 11.\n", "- Which city holds the Geller family tower that appears in Book 11.\n- Yaresh: the duke's name (the Aristocratic Faction is now confirmed).\n")
s += """
## E. Organisations (05_Organisations), first draft

Checked against the book text while writing: the Adventure Society's emblem and iron badge; Vincent's explanation of stars; restricted essences barring membership; action quotas, the contribution board and guild shares (Book 7); Genevieve Picot, Tabitha Gert, Marcus Hargrave Xenoria; the living document; Rakesh's campus and castes; the MRA's role and funding (Book 12); Burning Violet's house, Roland Remore and the Remore Academy; the Sapphire Crown; the Aristocratic Faction (Book 10); EOA Cardinals; Vermillion on the Cabal and the Network's origins; the Order of the Reaper's grandmaster; Order of Redeeming Light and clockwork cores.

Still unchecked (lorebook or wiki):
- Adventure Society: monthly field assessments; the gold badge with a diamond symbol; joint scanning at application with a priest of Knowledge; instructors named Guy Spalding.
- Magic Society: Pochard Finn as Greenstone director after Lamprey; Alchemy and Artifice Associations' structure.
- MRA: Lorelei Grantham as Vice Chancellor; its transportation network.
- Burning Violet: the Book 12 application's outcome (Roland's lesson; Team Biscuit's withdrawal); Neiman Bassingthwaite's description.
- Aristocratic Faction: "drydock and burn the ship"; Juniper Bynes.
- Earth: the Network's four fragments; Marie Finnegan's role; the Founder and Noreth; Cabal holdings in Russia and Africa; Mrs South's fate; Mr East being replaced by Adrien Barbou.
- Cults: churches bargaining with vorger; the hidden-insight reveal about the Order; Zato and Timos details; Beaufort's role; Order of Redeeming Light personnel.
"""
open(p, "w", encoding="utf-8").write(s)
print("done")

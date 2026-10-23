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


edit("07_Characters/Musin_Heath.md", [(
    "his rank and core use are from the notes only (notes, Book 10; not located).",
    "his rank and core use are not stated in the chapters. He is a veteran administrator, not an expert at handling monsters, who calms an unruly room of silver-rankers by spreading his aura and imposing calm through aura suppression (Book 10, Ch10 L3).")])
edit("07_Characters/Anna_Tilden.md", [
    ("Anna's place in the GDN delegation is from the notes (notes, Book 6).",
     "Anna is asked to be go-between for a meeting arranged by the GDN (Book 6, Ch23 L15), and arrives at the GDN camp in a party of eight that includes former EOA members who joined the GDN (Book 6, Ch24 L3, L5 to L8); that she belongs to the GDN delegation is not stated."),
    ("that she confirms the System is Jason's interface is not located (notes, Book 12). The fact itself is stated to Jason in Book 12, Ch1 L36.",
     "she suspects the System could be some cosmic force rather than Jason (Book 12, Ch42 L99), and Jason answers with a System Administrator window, \"I'm being as open as I can, Anna\" (Book 12, Ch42 L100 to L101); she then provisionally accepts his offer (Book 12, Ch42 L104 to L106). The fact that his interface was made available to everyone is stated to Jason in Book 12, Ch1 L36."),
])
edit("05_Organisations/Earth_Powers.md", [(
    "that she leads vampires separate from the Cabal is from the notes (notes, Book 6).",
    "Anna describes a new leader among the vampires who has separated from the Cabal, and Jason answers \"I've met Elizabeth\" (Book 6, Ch47 L27 to L28). Later the Cabal is said to have unambiguously split from the vampire lords and those who followed them (Book 11, Ch68 L1496).")])
edit("07_Characters/Rufus_Remore.md", [(
    "The notes describe him as tall (notes, Book 1; no height is stated in the lines checked).",
    "He is \"tall and lean\" (Book 7, Ch9 L6) and a \"tall, leanly muscular adventurer\" (Book 9, Ch3 L59); no height in numbers is given.")])
edit("07_Characters/Zara_Rimaros.md", [(
    "which places her below gold (silver is the notes' figure, not located);",
    "which places her below gold, and she is silver rank (\"Vesper's silver-rank vision\", Book 7, Ch15 L74; \"Vesper was only silver rank to Liara's gold\", Book 7, Ch21 L32);")])
edit("07_Characters/Neil_Davone.md", [(
    "He was initially Thadwick Mercer's lackey and team mate; after Thadwick's fall he quit and joined Jason (wiki). The wiki calls Cassandra Mercer an \"ex? girlfriend\" (wiki).",
    "He was initially Thadwick Mercer's lackey and team mate (Book 1, Ch110 L40; Book 2, Ch75 L67); after the disastrous expedition Thadwick disbanded the team without notice and the two were glad to be free of being known as Thadwick's flunkeys (Book 2, Ch27 L57), and Neil then joined Jason's team (Book 11, Ch6 L63). Cassandra Mercer is not his ex: as a youth he admired Thadwick's older sister (Book 2, Ch27 L43), and he was angry that she chose Jason (Book 11, Ch6 L60). She was Jason's girlfriend and ended it (Book 2, Ch13 L19).")])
edit("07_Characters/Gabrielle_Pellin.md", [(
    "- In Book 13 a cube leaves her chest",
    "- By Book 12 she is Travis Noble's wife and is quiet, still getting used to the absence of her goddess (Book 12, Ch58 L41); in Book 13 Travis brings his wife Gabrielle Pellin breakfast in bed (Book 13, Ch1016 L68, L74).\n- In Book 13 a cube leaves her chest")])
edit("Appendices/Name_Index.md", [
    ("- **Gabrielle Pellin** (B1): Knowledge priestess; Travis's wife.",
     "- **Gabrielle Pellin** (B1): Knowledge acolyte, later priestess (Book 1, Ch38 L122); Travis Noble's wife (Book 12, Ch58 L41; Book 13, Ch1016 L68)."),
    ("- **Ian Evans** (B4): Erika's husband and Emi's father;",
     "- **Ian Evans** (B4): a doctor (Book 4, Ch31 L77), Erika's husband and Emi's father;"),
])
print("ok")

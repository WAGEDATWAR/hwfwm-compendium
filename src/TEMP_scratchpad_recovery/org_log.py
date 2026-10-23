root = r"C:\Users\Gabriel\Documents\World Stuff\HWFWM Compendium"

p = root + r"\TODO_Verification.md"
s = open(p, encoding="utf-8").read()
i = s.index("## E. Organisations (05_Organisations)")
s = s[:i] + """## E. Organisations (05_Organisations)

Remaining unconfirmed (lorebook or wiki claims kept hedged in the files):
- Adventure Society: the wiki's joint scanning at application with Magic Society officials and a priest of Knowledge; the meaning of the gold diamond badge.
- Magic Society: whether Pochard Finn later became Greenstone director; the Alchemy and Artifice Associations' internal structure; Lorelei Grantham's feelings for Clive.
- Burning Violet: whether Roland deliberately arranged Jason's application as a lesson or trap; Lord Bassingthwaite as the same person as Neiman Bassingthwaite.
- Aristocratic Faction: Gormanston being a core-free gold-ranker.
- Earth: the Network's four fragments; Marie Finnegan sabotaging the Grid to trigger zones; the founder and Noreth creating the Grid; the Cabal holding Russia and Africa as a whole; Mr East being replaced by Adrien Barbou.
- Cults: the Order of the Reaper surviving as a quiet network of volunteers (hidden-insight trial); the Order killing mad rulers and hunting necromancers; Zato's metal skin and Timos's details; remaining Order of Redeeming Light personnel (Fila, Ramona, Marika, Elise, Caitlyn, Heston, Kelleigh, Rhett and Jaime).
"""
open(p, "w", encoding="utf-8").write(s)

p = root + r"\Appendices\Change_Log.md"
s = open(p, encoding="utf-8").read()
a = "- Status: **Draft (partly checked)**; unchecked items are in `TODO_Verification.md`, section E.\n"
assert a in s
s = s.replace(a, a + """- Verification pass on the remaining Organisations items against the book text. Confirmed and added: field testing at the start of every month and the monthly patrol rota; Instructors Trenslow and Spalding; Jason's gold diamond badge; Pochard Finn as de facto director of Greenstone's Magic Society; Lorelei Grantham's path from Continental Council researcher (Book 3) through the Rakesh research wing (Book 6) to MRA Vice Chancellor (Book 12) and her portal network project; Neiman Bassingthwaite and the Burning Violet crisis, including Team Biscuit's withdrawal; Gormanston Bynes's thoughts, Juniper and Calcifer Bynes; Mr North as a rune spider and the founder's familiar; Boris's role in betraying the founder to the early societies; the former Mrs South; Marie Finnegan as the recently expelled Zurich director with seven reality cores; the churches' bargain with the vorger; Zato, Timos and Beaufort; Melody Jain, Sendira and Laront. Corrected: Noreth did not betray the founder to "the American branch" in the text I read.
- Status after the pass: **Draft (verified in part)**; remaining items in `TODO_Verification.md`, section E.
""")
open(p, "w", encoding="utf-8").write(s)
print("logged")

p = r"C:\Users\Gabriel\Documents\World Stuff\HWFWM Compendium\Appendices\Glossary.md"
lines = open(p, encoding="utf-8").read().split("\n")

new = {
 "**Adventurer**": "**Adventurer**: a person who hunts monsters and takes contracts. In Book 12 Jason defines the role as putting yourself between the bad things and those who need protection (notes, Book 12). **[0]**",
 "**Blood parasite / blood oak / blood root vine**": "**Blood root vine**: a plant-animal monster of Pallimustus (Book 2). **Blood oaks** are Elizabeth's weapons on Earth, per Jason's guess in Book 13 (notes). **[2/3]**",
 "**Brand (messenger)**": "**Brand (messenger)**: a mark in a messenger's soul; Boris (Book 11) says a messenger's rank limits are a function of the brand. **[2]**",
 "**Defier of the Will**: ": "**Defier of the Will**: a bond choice offered to Farrah in Book 12; it lets the holder negate the influence of the Astral Nexus in various ways and confers immortality (notes, Book 12). **[3]**",
 "**Engineers of Ascension (EOA)**": "**Engineers of Ascension (EOA)**: an Earth faction that works with the Network's Lyon branch (notes; wiki). **[2]**",
 "**Dumpling soup**": "**Dumpling soup**: Clive's model of the cosmos (Book 1, chapter 69). **[1]**",
 "**Cabal**": "**Cabal**: Earth's old magical society, with vampire members (Book 4; wiki). **[2]**",
 "**Network**": "**Network**: Earth's coalition of essence users (Books 4-6; wiki). **[2]**",
 "**Quintessence**": "**Quintessence**: elemental/essence crystal gems used in crafting (Book 1; wiki). **[0]**",
 "**Reaper, the**": "**Reaper, the**: great astral being of death's finality; Shade is one of its shadows (Book 11). **[1]**",
 "**Umber**": "**Umber**: Shade's brother, who plans against Jason in Book 13 (notes). **[3]**",
}
done = set()
for i, l in enumerate(lines):
    for k, v in new.items():
        if l.startswith(k):
            lines[i] = v
            done.add(k)
print("missing:", [k for k in new if k not in done])
s = "\n".join(lines)
s = s.replace("Status: Draft (in progress; Sections A-Z covered for Books 1-13 core terms)",
              "Status: Draft (audited against the book text, chapter notes and wiki; entries without support in those tiers were reworded or removed)")
s = s.replace("Sources: Books 1-13 (chapter notes), fan wiki for essence and stone lists",
              "Sources: book text, chapter notes, fan wiki")
open(p, "w", encoding="utf-8").write(s)

import io, os, sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
BASE = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".."))

EDITS = [
 ("05_Organisations/Earth_Powers.md",
  "The notes for Book 13 add that the founder returned to Earth with magic bargained from messengers, created the Network's secret societies and the Grid as a pressure-release valve, and was betrayed by his familiar to US secret societies at about the time of the American Revolution (notes, Book 13); the wiki calls him",
  "Jason's account in Book 13 adds that the founder, an outworlder brought into the fake Purity's church, returned to Earth with magic Knowledge had bargained from the messengers, built the web of secret societies and the Grid as a pressure-release valve for the rising magic (Book 13, Ch1017 L19-23), and was betrayed by his familiar Noreth, born on Pallimustus, who handed him to the US secret societies at a time Jason guesses was around the War of Independence (Book 13, Ch1017 L24); Noreth is Mr North, leader of the Engineers of Ascension (Book 13, Ch1017 L39); the wiki calls him"),
 ("05_Organisations/Earth_Powers.md",
  "Elizabeth leads ancient vampires separate from the Cabal (notes, Book 6).",
  "By Book 11 Elizabeth has taken over Venice and rules it among the vampire lords, who resent her policy of treating humans better and her warnings (Book 11, Ch68 L2256-2261, L2266); the Book 6 notes call her the leader of ancient vampires separate from the Cabal (notes, Book 6; not located in the Book 6 text)."),
 ("06_Places/Astral_Spaces/Spirit_Vault_and_Astral_Kingdom.md",
  "The notes add a blood section like an artery, a sin section of black, red, white and gold, and a dark section in an underground cave with luminescent fungus and silver grass (notes, Book 4); in Book 8 the notes list gardens by essence: blood (narrow red-flower paths like veins and arteries), dark (underground tunnels, luminescent fungus, rainbow butterflies) and sin (manicured black and white flowers) (notes, Book 8).",
  "The same passage describes a blood section of red flowers and blood-red flagstone like walking through an artery, a sin section of black, red, white and gold beds, a dark section in an underground cave with luminescent fungus and silver grass, and a doom section of trees and bushes, with a creek that runs through all of them to a waterfall and an underground fairy grotto (Book 4, Ch57 L3-10). In Book 8 Clive tours the same garden estate, where the essence sections intermingle, a subterranean network of fungus-lit tunnels runs under it, the sin garden is a manicured plot of black and white flowers and the doom areas are wild jungle (Book 8, Ch2 L57-63)."),
 ("06_Places/Earth/Artefact_Site_One.md",
  "The notes for Book 12 mark the Sky Link island as a place the team visits, and the notes for Book 13 say the Church of Knowledge annexed the island that became Ascension's Gate (notes, Books 12-13); that they are the same island is likely but not stated outright.",
  "The island is the one Jason and Farrah first reached years earlier, then uninhabited and ringed by the magical hurricane of the Sea of Storms, since bought and developed by the Sky Link Company (Book 12, Ch56 L3-4); Jason names it as the Pallimustus anchor point, an uninhabited island in the Storm Kingdom (Book 12, Ch39 L47) and in Book 13 says the Church of Knowledge has annexed it (Book 13, Ch1020 L95); it is renamed Ascension's Gate (Book 13, Ch1023 L103). The text never states the Sky Link name and the Ascension's Gate name for one island in a single sentence, but both describe the Storm Kingdom island the bridge is anchored on."),
 ("07_Characters/Kaito_Asano.md",
  "Jason sees a Kaito-like face in the mirror after ranking up (notes, Books 4 and 13).",
  "Jason's growing resemblance to his brother with each rank-up is something he stops begrudging after Kaito's death (Book 13, Ch950 L33); the Book 4 notes' version of the mirror scene is not located."),
 ("07_Characters/Neil_Davone.md",
  "holds tea lands in the Mistrun valley (notes, Book 2).",
  "holds tea lands in the Mistrun valley (Book 2, Ch23 L17, where a maid serves the family's blend)."),
 ("07_Characters/Zara_Rimaros.md",
  "withdraws from the succession; she is \"Zara Nareen\" after adoption into her mother's house (notes, Book 9).",
  "she is a former princess of the Storm Kingdom by Book 9 (Book 9, Ch40 L21); the \"Zara Nareen\" name and the adoption are from the notes (notes, Book 9; not located)."),
 ("07_Characters/Rufus_Remore.md",
  "The notes describe him as tall (notes, Book 1).",
  "The notes describe him as tall (notes, Book 1; no height is stated in the lines checked)."),
]

for rel, old, new in EDITS:
    p = os.path.join(BASE, rel)
    s = open(p, encoding="utf-8").read()
    if old not in s:
        print("MISSING", rel, old[:50])
        continue
    open(p, "w", encoding="utf-8").write(s.replace(old, new, 1))
    print("ok", rel)

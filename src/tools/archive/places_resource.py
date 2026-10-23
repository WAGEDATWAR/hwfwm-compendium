import re, glob, os
root = r"C:\Users\Gabriel\Documents\World Stuff\HWFWM Compendium"
STATUS = "Status: Draft (book text, chapter notes and wiki; tiers marked: \"Book N\" = checked in the book text, \"notes\" = chapter notes, \"wiki\" = fan wiki)"

# 1. Status lines for every file under 06_Places
for f in glob.glob(root + r"\06_Places\**\*.md", recursive=True):
    s = open(f, encoding="utf-8").read()
    lines = s.split("\n")
    changed = False
    for i, l in enumerate(lines):
        if l.startswith("Status: Draft (") and "lorebook" in l.lower():
            lines[i] = STATUS
            changed = True
    if changed:
        open(f, "w", encoding="utf-8").write("\n".join(lines))

def sub(rel, pairs):
    p = root + "\\" + rel
    s = open(p, encoding="utf-8").read()
    for a, b in pairs:
        assert a in s, (rel, a[:80])
        s = s.replace(a, b)
    open(p, "w", encoding="utf-8").write(s)

sub(r"06_Places\00_Places_Overview.md", [
 ("Sources: Books 1-13 (chapter notes, lorebook entries); fan wiki for the geography list", "Sources: Books 1-13 (book text and chapter notes); fan wiki for the geography list"),
 ("Its medical university, listed by the lorebook, is unchecked.", "Its notable institution is the Kazlahk University of Medicine (Book 11)."),
 ("it has a large celestine community (lorebook; the name occurs only in Books 1 and 7).", "it has a large celestine community (notes, Book 1); it is the home of the diamond-rank smith Virid Martine and his smithy, where Gary and Virid reforge Dread Salvation (Book 7; notes, Book 7)."),
 ("The lorebook records Greenstone as mid-iron density with low saturation and Vitesse as silver.", "Clive rates Greenstone's density as about mid-iron, \"which is very low\" (Book 3). The wiki says Vitesse's magic density is much greater than Greenstone's (wiki); the books give no figure for Vitesse."),
])

sub(r"06_Places\Astral_Spaces\00_Astral_Overview.md", [
 ("Interstice is described as the oldest and largest city-world, a flat plane at the cosmos's centre where only diamond-rankers enter freely. It contains districts belonging to great astral beings, including the Builder's and the Reaper's, and regions such as Glim (rainbow ice) and Fueros (the World-Phoenix's region, with red and yellow crystal spires). Boris Ket Lundi has visited; Jason has not as of the end of the series (lorebook; unchecked).",
  "The notes for Book 3 describe Interstice as the oldest and largest city-world, a flat plane, with an island region called Glim (rainbow ice) and districts belonging to great astral beings, including the Builder's and the Reaper's (notes, Book 3); the wiki says the Builder meets the Reaper and the World-Phoenix there to negotiate Jason's fate (wiki). Book 12 describes it from the viewpoint of Jota Withers (Book 12). Boris is to explain Interstice and the cosmic community to Anna (notes, Book 12)."),
])

sub(r"06_Places\Astral_Spaces\City_of_Fallen_Echoes.md", [
 ("the overall density rating given by the lorebook (gold, mostly iron and some bronze monsters) is unchecked.", "the space's overall density is not stated in the passages I checked."),
 ("The lorebook says wisdom grants a Medallion of Escape (a silver-rank, uncommon item; Jason uses one in Book 2) and a Lesser Miracle Potion (an iron-rank, legendary item; both items exist in Book 2, but which trial gives them is unchecked).",
  "The notes say the first trial cannot be failed and that choosing wisdom gives a Medallion of Escape (a silver-rank, uncommon item that projects the aura to evacuate and works only in the city) and a Lesser Miracle Potion (an iron-rank, legendary item), while the five virtues are courage, intellect, resolve, capability and wisdom (notes, Book 2; items confirmed in Book 2)."),
])

sub(r"06_Places\Astral_Spaces\Desert_Astral_Space.md", [
 ("The incident ties the Builder cult to the region and sets up Book 2. The lorebook's note that the network of nodes was disrupted is unchecked.", "The incident ties the Builder cult to the region and sets up Book 2."),
])

sub(r"06_Places\Astral_Spaces\Reaper_Trials_Boarding_Vessel.md", [
 (" The lorebook says the astral space drifts away after the inversion as a transcendent vehicle (unchecked).", ""),
])

# Spirit vault file: replace section 2 and fix others
p = root + r"\06_Places\Astral_Spaces\Spirit_Vault_and_Astral_Kingdom.md"
s = open(p, encoding="utf-8").read()
i = s.index("## 2. Evolution (lorebook timeline)")
j = s.index("## 3.")
s = s[:i] + """## 2. Evolution

Inventory (Book 1); the Spirit Vault, an inventory he can enter and which others can enter by trust (Book 4); a spirit domain (Book 6); a spirit realm that travels along the world link (Book 7 notes); an astral kingdom once the Astral Throne and Gate appear (Book 8); consolidation of the Cardinas zone with the Soul Forge and the forest city Arbour (Book 11 notes).

""" + s[j:]
open(p, "w", encoding="utf-8").write(s)

sub(r"06_Places\Astral_Spaces\Spirit_Vault_and_Astral_Kingdom.md", [
 ("The lorebook adds a blood section like an artery, a sin garden, a dark cave with luminescent fungus, doom trees, a creek from the astral, a fairy grotto and a central three-storey pagoda (those details unchecked).",
  "The notes add a blood section like an artery, a sin section of black, red, white and gold, and a dark section in an underground cave with luminescent fungus and silver grass (notes, Book 4); in Book 8 the notes list gardens by essence: blood (narrow red-flower paths like veins and arteries), dark (underground tunnels, luminescent fungus, rainbow butterflies) and sin (manicured black and white flowers) (notes, Book 8)."),
 ("the lorebook describes it as the forest city in the kingdom, formerly the corrupted birthing tree beneath the array, reborn as a person and nascent Voice of the Will, with redwood treehouses, light rail and a caldera valley (those details unchecked).",
  "the notes describe it as a tree city in Jason's astral kingdom with redwood tree mansions and light rail, with its own soul and avatar, formerly the corrupted World Tree or birthing tree (notes, Book 13); in Book 13 Jason and Emi stand on a platform in a tree mansion spanning several towering redwoods in Arbour (Book 13)."),
 ("The lorebook's \"without nobles\" is contradicted by the duke's presence and is withdrawn.", "The duke's presence contradicts any idea that it has no nobles."),
 ("- Whether the lorebook's \"Jason's true body is a universe\" matches Book 12.\n", ""),
])

sub(r"06_Places\Astral_Spaces\Transformation_Zones.md", [
 ("The lorebook's \"best case\" (a second uncuttable magic source) is unchecked.", "She adds that \"in the best case it will establish a second source of magic that will start feeding into this world\" (Book 5)."),
 ("The zone's length is given in the lorebook as about nine months (unchecked);", "The zone's overall length is not stated in the passages I checked (the wiki timeline has nine months);"),
])

sub(r"06_Places\Earth\Artefact_Site_One.md", [
 ("hardened over many years (fifteen years in the lorebook; Book 12 says magic became known less than fifteen years earlier).", "hardened over many years by a multinational coalition (Book 12)."),
 ("Whether it is the former Sky Link island (as the lorebook says) is unchecked.", "The notes for Book 12 mark the Sky Link island as a place the team visits, and the notes for Book 13 say the Church of Knowledge annexed the island that became Ascension's Gate (notes, Books 12-13); that they are the same island is likely but not stated outright."),
 (" The lorebook's \"within months\" deadline is unchecked.", ""),
])

sub(r"06_Places\Earth\Casselton_and_Asano_Village.md", [
 ("Whether the tunnel ends at a cloud-house dome (as the lorebook says) is unchecked.", "The long passage ends at Jason's cloud house, which sits at the bottom of the sea about two kilometres out, reached by a hidden tram (Book 5; notes, Book 5)."),
])

sub(r"06_Places\Earth\Incursion_Sites.md", [
 (" The lorebook's ogres, river hydras and giant toads are unchecked.", ""),
])

sub(r"06_Places\Earth\Nitra.md", [
 ("; the lorebook's \"Quilido Centre\" at Nitra is unconfirmed.", "."),
])

sub(r"06_Places\Vitesse.md", [
 ("The books do not give a figure for Vitesse. The lorebook's \"silver density\" and the claims about richer monster ecology and cheaper training are unchecked; what is confirmed is that magic here is far higher than Greenstone's (Greenstone being mid-iron).",
  "The books I searched give no figure for Vitesse; Gary and Farrah explain that Vitesse is a large city with a much greater magic density than the Greenstone area, which is why iron-rank adventurers there are not allowed to hunt alone (wiki, Chapter 30; Book 2: Keane says iron-rankers in areas of high magic density are not allowed to hunt by themselves)."),
])
print("places resourced")

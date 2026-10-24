"""Append gap-fill rows to the per-book timelines (build plan item 3.6b).

Each entry gives a chapter that had no timeline row, with one or two sentences whose citations name lines in that
chapter. The rows go in a section "Additional chapter rows" at the end of Book_NN_Timeline.md; chapter_digest.py then
picks them up. Safe to re-run: a book's section is rewritten, not duplicated.
"""
import os, re

BASE = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".."))
HIST = os.path.join(BASE, "08_History_and_Timeline")

ROWS = {
 1: {
  2: "Naked and bleeding, Jason finds his inventory and learns how looting a monster's body works (Book 1, Ch2 L7, L13, L62). He withdraws lesser spirit coins from the inventory (Book 1, Ch2 L43).",
  3: "Jason puts on the plain linen pants he is given (Book 1, Ch3 L17). A trowel's description names a blood cult, and he overhears men discussing captives (Book 1, Ch3 L8, L41-45).",
  4: "Jason crawls through a tight, slimy brick tunnel under the well (Book 1, Ch4 L3). He finds an awakening stone (Book 1, Ch4 L45).",
  14: "Farrah removes the collars from Rufus and Gary after an ambush by a local contact (Book 1, Ch14 L3-7). Jason finds an outfits tab in his inventory (Book 1, Ch14 L35).",
  15: "Jason walks the desert trail with Rufus, Farrah and Gary while they explain their world to him (Book 1, Ch15 L3-6). The heat overwhelms him before they rest (Book 1, Ch15 L81).",
  17: "Anisa is dismissive of Jason as the party plans to loot the cult manor (Book 1, Ch17 L3-6, L34). Farrah summons a creature in a powder circle (Book 1, Ch17 L72).",
  19: "On a terrace the team talks through monsters, magic manifestations and Jason's looting (Book 1, Ch19 L4, L27, L34). Anisa searches the manor study for letters linking the cult to other regions (Book 1, Ch19 L15).",
  20: "Rufus and Gary advise Jason on choosing essences, with Farrah as the example of power without versatility (Book 1, Ch20 L3-8). They check combinations and the Adventure Society's restricted list (Book 1, Ch20 L42, L104).",
  27: "Jason and Hiram fight a slow, crab-legged monster in a tunnel (Book 1, Ch27 L3-7, L26). His special attacks inflict bleeding and he gains ten iron-rank spirit coins (Book 1, Ch27 L58, L96).",
  28: "A rush of water throws Jason and Hiram out of the tunnel, and his cloak slows their fall (Book 1, Ch28 L3-6). He plans to use inexorable doom on the shabs (Book 1, Ch28 L73).",
  52: "Jason trains in the mirage chamber against five illusory attackers (Book 1, Ch52 L4-6, L15). Lucian receives Clarissa in his lounge to discuss Sophie's protection (Book 1, Ch52 L47-64).",
  55: "On the third morning of the field assessment the group stops in a town where Jason heals the sick (Book 1, Ch55 L3-5). Mobley's attempt to fight a monster goes badly (Book 1, Ch55 L67-75).",
  57: "Jason kills a trapped monster and Vincent teases him about affliction specialists (Book 1, Ch57 L4-8). Vincent briefs the candidates on a bark lurker and Jason waits in mangrove shadows as bait (Book 1, Ch57 L41, L60).",
  59: "Humphrey dispatches dog-headed monsters while Jason watches (Book 1, Ch59 L17). Vincent leads the group to help locals (Book 1, Ch59 L27).",
  64: "Jason takes one or two contracts a day from the jobs hall (Book 1, Ch64 L3-7). Clive apologises to a small woman who is scolding him (Book 1, Ch64 L85).",
  71: "Jason, in his battle robe, takes his first contract inside Old City (Book 1, Ch71 L3). In the Townhouse cellar he finds a man kneeling by a hole in the wall (Book 1, Ch71 L48).",
  79: "Sand elementals surround Humphrey's team and Phoebe shouts to break them up with powerful attacks (Book 1, Ch79 L3-8). Humphrey takes to the air with dragon wings (Book 1, Ch79 L24).",
  85: "Jason, Clive and Humphrey look for an entrance to a lair and consider a well-digging ritual (Book 1, Ch85 L3-7). Clive draws a ritual diagram (Book 1, Ch85 L59).",
  106: "Belinda explains a lock-breaking sequence to Clive at Jory's kitchen table (Book 1, Ch106 L3-6). Arella asks Jason what he wants in return for silence (Book 1, Ch106 L82).",
 },
 2: {
  18: "Rick leads Clive and Belinda through the Geller grounds (Book 2, Ch18 L3). Clive reactivates the control system of a rune-covered block (Book 2, Ch18 L39, L54).",
  28: "Jason brings Neil to the cloud palace for a welcome lunch (Book 2, Ch28 L3-6). Humphrey tells Neil about Farrah's fall (Book 2, Ch28 L43).",
  35: "Jason and Sophie walk an embankment road in the delta while he talks about standing out and trust (Book 2, Ch35 L5-9, L27, L52).",
  51: "Clive's team climbs a precarious tall building and Valdis crosses to fasten the other end (Book 2, Ch51 L3, L26). They fight a wingless dragon-like creature in a circle (Book 2, Ch51 L40, L70).",
  64: "Jason uses his final awakening stone for Avatar of Doom (Book 2, Ch64 L3-5). Humphrey receives the awakening stone of the Reaper (Book 2, Ch64 L72).",
  66: "Emir tells Jason that his aura signature has changed (Book 2, Ch66 L8). Emir shows him a scar (Book 2, Ch66 L27).",
 },
 3: {
  6: "A rainbow manifestation opens over Old City and Henrietta directs the adventurers who respond (Book 3, Ch6 L3-5). Filthy water geysers up and the team fights the monster (Book 3, Ch6 L15, L20).",
  10: "The team clears adventure notices town to town while Henrietta breaks down their weaknesses (Book 3, Ch10 L3). Belinda and Clive set rune traps for a monster (Book 3, Ch10 L23).",
  11: "The team faces six-legged desert horde lizards and Henrietta pairs Jason with Belinda (Book 3, Ch11 L3-7). Belinda casts Jason's spell on a second lizard (Book 3, Ch11 L26).",
  18: "Killian prepares to use the star seed on Jason hanging from a spike (Book 3, Ch18 L3-4). Silva asks how Killian learned a Builder cult ritual (Book 3, Ch18 L6-7).",
  43: "Spider constructs emerge from holes in the floor, and Clive and Belinda cast rune traps (Book 3, Ch43 L3-6).",
  48: "The team hears monsters approaching through the jungle and gathers on a stone platform (Book 3, Ch48 L3-6). Clive's first spell covers the platform, including summons (Book 3, Ch48 L53).",
  50: "Jason's recovery power heals the front line and he singles out the sturdier bronze-rank monsters (Book 3, Ch50 L3-4). Colin devours vampires while Clive keeps Onslow on the ground monsters (Book 3, Ch50 L54-61).",
 },
 4: {
  8: "Hiro finds Jason in his penthouse and Jason will not say what he is involved in (Book 4, Ch8 L3-7). Aram leads the Sydney incident investigation (Book 4, Ch8 L84).",
  14: "A bullet shatters the car's back window and Jason tells Taika to keep driving (Book 4, Ch14 L3-5). Jason's shadow rider carries him closer to the bikers (Book 4, Ch14 L33).",
  39: "Jason hammers out an agreement with Keith and Anna on his houseboat (Book 4, Ch39 L3-4). He still has family to tell (Book 4, Ch39 L6).",
  40: "Nigel briefs Jason on the Sydney branch's category-three contingent (Book 4, Ch40 L3-4). The force enters a jungle with a tower of crude brick (Book 4, Ch40 L37).",
 },
 5: {
  28: "King tells Jason he can hear through his vessel, and Jason says he is sorry for the circumstances of King's creation (Book 5, Ch28 L4-11). The proto-space reaches its final stage of dissolution (Book 5, Ch28 L70).",
  41: "Mr North argues that repairing the link between worlds is only the beginning (Book 5, Ch41 L3-8). The obsidian portal arch absorbs dust from the stones (Book 5, Ch41 L85).",
 },
 6: {
  10: "Jason expands his spirit domain from a rooftop into a city-like territory (Book 6, Ch10 L3-5). He holes up in a store to treat his wounds as anomalies converge (Book 6, Ch10 L19-25).",
  15: "Jason fights zombie cyborgs across industrial ruins (Book 6, Ch15 L3-7). He meditates to extend his aura into the territory (Book 6, Ch15 L40).",
 },
 7: {
  44: "Liara, Vesper, Trenchant and Liara's teammates assess Jason in a conference room (Book 7, Ch44 L3-5). Trenchant says he would run from an affliction skirmisher (Book 7, Ch44 L23).",
 },
 8: {
  63: "Liara's family dines in Jason's cloud house, and Jason tells how Liara's leak of his route led to a Purity ambush (Book 8, Ch63 L3-8).",
 },
 9: {
  1: "Jason convalesces after a rescue in a flooded mining complex where he opened a portal he should not have been able to (Book 9, Ch1 L3-6). Rick tells him the Adventure Society is open to him spending decades being nice and quiet (Book 9, Ch1 L103).",
  8: "Two adventuring teams in dense jungle are attacked by an unseen foe and Carilo is dragged into the scrub (Book 9, Ch8 L3-12). A blue-and-orange eyed figure appears overhead (Book 9, Ch8 L25).",
  47: "Zolit congratulates Jason in the fighters' locker room (Book 9, Ch47 L3-6). A prestigious underground figure joins Zolit and tells a story (Book 9, Ch47 L29-36).",
  59: "The team gets a brief respite from the worm-host elves (Book 9, Ch59 L3). Clive attaches ritual circles to their weapons, and rough edges show after years apart (Book 9, Ch59 L23, L54).",
  65: "Jason emerges from his soul space and Clive says the messengers were easier than expected (Book 9, Ch65 L3-4). A hidden slate-brick basement leads to a wide chamber (Book 9, Ch65 L63).",
  69: "Sophie argues for eradicating the worms rather than studying them (Book 9, Ch69 L3-4). Colin could use the devoured power of the World-Taker Worm Matriarch to awaken as a Voice of the Will (Book 9, Ch69 L55).",
  70: "Jason goes outside and takes in the bodies of the dead town (Book 9, Ch70 L3-5). He talks about the line he can go to without losing himself (Book 9, Ch70 L34).",
  83: "Barrier breaches spread across the city and Jason's team defends the entertainment district (Book 9, Ch83 L3-5). Gary leads a group and keeps it moving rather than securing kills (Book 9, Ch83 L18).",
  87: "Humphrey's second foray into the summons is far more powerful, though his Relentless Assault drains his mana (Book 9, Ch87 L3-5). Belinda uses Pit of the Reaper and her tethers (Book 9, Ch87 L25).",
  91: "Fal Vin Garath heads for the pyramid, sneering at his commander (Book 9, Ch91 L3). A harpoon drags him into the cloud stuff (Book 9, Ch91 L35).",
  95: "Jason enters Gordon's ritual diagram to prepare to become more fully an astral king (Book 9, Ch95 L3-6, L11). His soul declares itself and his aura floods the city (Book 9, Ch95 L41).",
 },
 10: {
  9: "Jason's team, with new member Taika, gathers at Emir's palace for a large meeting (Book 10, Ch9 L3-4). Ebson Jillet introduces himself as chief information officer of the combined holy forces (Book 10, Ch9 L46).",
  23: "Elemental messengers are captured and Charist's air vortex clears the cloud, revealing a massive shaft (Book 10, Ch23 L3-6). Rufus notes they have provoked the local authorities again (Book 10, Ch23 L91).",
  27: "Jason and Allayeth walk his garden estate and she asks about a spirit coin farm and about making enemies talk (Book 10, Ch27 L3-16). Allayeth says the messengers are still invading and killing her people (Book 10, Ch27 L52).",
  41: "Sophie enters Jason's soul realm and confronts him (Book 10, Ch41 L3-7). Jason says he can do things in the realm that violate the laws of reality (Book 10, Ch41 L43).",
  56: "Vesta Carmis Zell asks how many of her messengers Jason intends to steal (Book 10, Ch56 L3-4). Jali spits that it is better to be a pet than food (Book 10, Ch56 L62).",
  64: "Miriam Vance floats up to Jason over the shaft full of butterflies (Book 10, Ch64 L3-5). He says he is used to being betrayed by the people he works with (Book 10, Ch64 L18).",
  73: "Jason, Clive and Miriam sit in the council chamber with Beaufort, Lorenn and Marla (Book 10, Ch73 L3). Beaufort says the Builder still observes him and told him to exploit a weakness (Book 10, Ch73 L32).",
  81: "The first major breach of the wall comes on the fifth floor, and Gary smashes a shield mantis creature (Book 10, Ch81 L3-5). Clive sets ritual circles on nine platforms around the tree (Book 10, Ch81 L15).",
 },
 11: {
  11: "Brighthearts and cultists gather under a stone arch with Neil standing between the faction leaders (Book 11, Ch11 L3-6). Neil proposes moving as a lean, elite force (Book 11, Ch11 L50).",
  14: "Belinda hides in a floating hollow log with ritual traps set around the elemental forest (Book 11, Ch14 L3-5). A gold-ranker roars in pain and Belinda expects her to hunt them (Book 11, Ch14 L6, L27).",
  15: "Kol Kelis Vel stomps to the pond and sees through Belinda's illusion of Cas Vin Baral (Book 11, Ch15 L3-7). Belinda scolds that an ordinary person would be dead (Book 11, Ch15 L68).",
  23: "Jason walks a forest path with the unnamed rabbit and talks about names (Book 11, Ch23 L3-6). He says they must find the avatar before the Undeath high priest takes control of it (Book 11, Ch23 L65).",
  31: "In the Escher-like castle Garth trapped them in, Jason watches Garth cross a bridge (Book 11, Ch31 L3). Boris warns that the avatar is moving fast (Book 11, Ch31 L67).",
  45: "Lightning storms keep the adventurers working at the shattered array while Jason feeds its remains into his cloud flask (Book 11, Ch45 L3-5). A listener tells Mrs Remore her account of Jason is not hopeful (Book 11, Ch45 L45).",
  47: "Gary, Miriam and Arabelle defeat an odd round purple boss anomaly by draining its mana (Book 11, Ch47 L3-7). Miriam asks Jason to claim the territory so they can return to base (Book 11, Ch47 L104).",
  68: "Jason leaves the world after thanking Gary for the sword (Book 11, Ch68 L115). The book ends with the System message (Book 11, Ch68 L2540).",
 },
 13: {
  951: "Jason comforts a nervous Nik in a cloud ship corridor (Book 13, Ch951 L3-6). Emi's parents pry her off Nik while Hana and Jace look on (Book 13, Ch951 L70).",
 },
}

HEAD = "## Additional chapter rows (digest gap fill)"


def main():
    for book, rows in ROWS.items():
        path = os.path.join(HIST, "Book_%02d_Timeline.md" % book)
        text = open(path, encoding="utf-8").read()
        if HEAD in text:
            text = text[:text.index(HEAD)].rstrip() + "\n"
        lines = [HEAD, "",
                 "Rows added in the chapter-digest pass for chapters that had no timeline row. Each cites the chapter lines it summarises.",
                 "", "| When | Chapters | Event |", "|---|---|---|"]
        for ch in sorted(rows):
            lines.append("| Gap fill | Ch%d | %s |" % (ch, rows[ch]))
        text = text.rstrip() + "\n\n" + "\n".join(lines) + "\n"
        open(path, "w", encoding="utf-8", newline="\n").write(text)
        print("Book %d: %d rows" % (book, len(rows)))


if __name__ == "__main__":
    main()

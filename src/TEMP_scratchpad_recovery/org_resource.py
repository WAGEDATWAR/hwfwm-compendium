root = r"C:\Users\Gabriel\Documents\World Stuff\HWFWM Compendium"
STATUS = "Status: Draft (book text, chapter notes and wiki; tiers marked: \"Book N\" = checked in the book text, \"notes\" = chapter notes, \"wiki\" = fan wiki)"

def sub(rel, pairs):
    p = root + "\\" + rel
    s = open(p, encoding="utf-8").read()
    for a, b in pairs:
        assert a in s, (rel, a[:80])
        s = s.replace(a, b)
    open(p, "w", encoding="utf-8").write(s)

sub(r"05_Organisations\00_Organisations_Overview.md", [
 ("Status: Draft (compiled from the lorebook and chapter notes; claims marked \"confirmed\" were checked against the book text)", STATUS)])

sub(r"05_Organisations\Adventure_Society.md", [
 ("Status: Draft (lorebook, wiki and chapter notes; confirmed items marked)", STATUS),
 ("The lorebook adds that stars drop when rank rises, that three-star work involves politics and spirit coin farms (Book 1: Pochard says anything involving the farms is three-star), and (Book 12, confirmed) Jason is later given",
  "The notes add that stars drop when rank rises (notes, Book 1); Pochard says anything involving the spirit coin farms is three-star work (Book 1); and Jason is later given"),
 ("- **Restricted essences**: Death, Corrupt, Sacrifice, Undeath and Succubus are named in the lorebook; Rufus confirms Death. The Society offers rewards to remove such essences from circulation.",
  "- **Restricted essences**: Rufus says Death is restricted by itself (Book 1), and the Magic Society's living document shows one restricted combination, the Succubus essence, which takes two insanely rare essences (Book 1). The wiki lists Death, Corrupt, Sacrifice, Undeath and Succubus and says the Society offers rewards to remove such essences from circulation and posts contracts against users, such as a Greenstone pit fighter with the Sacrifice confluence (wiki)."),
 ])

sub(r"05_Organisations\Cults_and_Orders.md", [
 ("Status: Draft (lorebook and chapter notes; confirmed items marked)", STATUS),
 ("The lorebook adds that the Order killed mad rulers and hunted necromancers (unchecked).",
  "The notes record that the Order were royal assassins (a knife in the dark for fool or mad rulers) and hunters of undead and of the Unliving church's necromancers, accepted by nations and the Adventure Society until the churches destroyed them (notes, Book 2)."),
 ("The lorebook says the hidden insight trial reveals the Order survives as a quiet network of volunteers who match tasks to people of conscience (unchecked).",
  "The notes say the City of Fallen Echoes' final trial reveals that the Order now survives as a volunteer network of quiet allies who match jobs to people of conscience, and the trials are a lure with iron-only entry to keep out high-rank investigators (notes, Book 2)."),
 ("Landemere Vane summoned Jason by mistake; Dougall and Thadwick Mercer become vessels (lorebook).",
  "Landemere Vane summoned Jason by mistake while trying to summon a Clockwork King (Book 3). The Builder possesses Dougall's body, which breaks down if it uses more than silver-rank power (Book 3), and later Thadwick Mercer's (wiki)."),
 ("- **Church relation**: Purity's church quietly tolerated the cult via a wider accord (lorebook; consistent with Disguise's role).",
  "- **Church relation**: Purity's church works with the cult and is placed under inquiry by an ecumenical council of the other churches (Book 3; Disguise's role is covered in `Gods_and_Churches.md`)."),
 ("attempts on Gibson Amouz (lorebook).", "the capture of Gibson Amouz, a cousin of Liara's husband (Book 8), whom the Church of the Healer later recovers (Book 9)."),
 ("Other names are lorebook only.", "Further personnel are named in the notes (notes, Book 8)."),
 ("the lorebook names the high priest Garth Larosse, a zemravore", "its priests are led by Garth Larosse, a priest of Undeath and a zemravore"),
 ("- The Order of the Reaper's present state beyond the lorebook's account.", "- The Order of the Reaper's present state beyond the notes' account."),
])

sub(r"05_Organisations\Earth_Powers.md", [
 ("Status: Draft (lorebook, wiki and chapter notes; confirmed items marked)", STATUS),
 ("The lorebook and wiki add that the founder returned from Pallimustus after a bargain with a god and that he and Noreth created the Grid (unchecked).",
  "The notes for Book 13 add that the founder returned to Earth with magic bargained from messengers, created the Network's secret societies and the Grid as a pressure-release valve, and was betrayed by his familiar to US secret societies at about the time of the American Revolution (notes, Book 13); the wiki calls him the original creator of the Grid and the Network's founder (wiki)."),
 ("The lorebook describes four fragments: the US branch, the Chinese branch, the GDN (lower Network, EOA remnants and Cabal schismatics) and the largest group, which works with the Australian government (unchecked). ",
  "At the Nitra dome in Book 6 the notes list the factions as the Network (US branches and the old leadership), the True Network (ex-International Committee), and the Chinese branch (notes, Book 6). "),
 (" That she sabotaged the Grid to trigger zones is the lorebook's account and is unchecked. The lorebook's four fragments of the Network are also unchecked.",
  " Book 13 also says Finnegan's contacts with Elizabeth and McKean were critical to the plan (Book 13)."),
 ("The lorebook: the oldest and most reclusive magical power on Earth, \"old magic\", vampires, controlling old money; high-tier members hibernate; angel-like messengers (Boris Ket Lundi among them) were secretly among its leaders; vampire lords later split from it.",
  "Vermillion describes the Cabal as the oldest of Earth's three dominant magical forces, tied to the \"old magic\" of vampires and things older than history, with \"a tight grip on old money literally since the invention of money\" (Book 4); its tier-four members have entered hibernation (Book 4). Messengers hid among its leaders: \"even many amongst the Cabal had considered the angelic founders of their collective a myth\" (Book 13). Elizabeth leads ancient vampires separate from the Cabal (notes, Book 6)."),
])

sub(r"05_Organisations\Guilds_and_Houses.md", [
 ("Status: Draft (lorebook and chapter notes; confirmed items marked)", STATUS),
 ("Whether Roland deliberately arranged it as a lesson is a lorebook claim and is unchecked.", "Whether Roland deliberately arranged the interview as a lesson is not stated in the passages I read."),
])

sub(r"05_Organisations\Magic_Society_and_Associations.md", [
 ("Status: Draft (lorebook and chapter notes; confirmed items marked)", STATUS),
 ("Whether Pochard later became director is a lorebook claim and is unchecked.", "By Book 11 Pochard has become director: \"It's Director now, Standish. I haven't been deputy director for several years\" (Book 11)."),
 ("Her feelings for Clive are a lorebook claim.", "In Book 6 the notes describe her as sympathetic and as someone who likes Clive (notes, Book 6)."),
])
print("organisations resourced")

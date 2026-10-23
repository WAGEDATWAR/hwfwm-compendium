root = r"C:\Users\Gabriel\Documents\World Stuff\HWFWM Compendium"

def sub(rel, pairs):
    p = root + "\\" + rel
    s = open(p, encoding="utf-8").read()
    for a, b in pairs:
        assert a in s, (rel, a[:70])
        s = s.replace(a, b)
    open(p, "w", encoding="utf-8").write(s)

sub(r"05_Organisations\Adventure_Society.md", [
 ("- **Field assessment**: an instructor tests the candidate's physical abilities, essence abilities and judgement under pressure (Book 1, chapter 54). The wiki and lorebook describe it as monthly; the monthly schedule is unchecked.",
  "- **Field assessment**: an instructor tests the candidate's physical abilities, essence abilities and judgement under pressure (Book 1, chapter 54). Field testing takes place at the start of every month and candidates sign up at the administration desk (Book 1, confirmed). Vincent Trenslow and Guy Spalding both act as instructors (\"Instructor Trenslow\" and \"Instructor Spalding\"; Book 1, confirmed); Spalding is also Albert Bertinelli's supervisor. Adventurers also patrol outlying villages on a monthly rota, an unpopular punishment duty that means a month away from the city (Book 1, confirmed)."),
 ("and that Jason's badges include a gold one with a diamond symbol later (unchecked).",
  "and (Book 12, confirmed) Jason is later given a gold badge with a diamond symbol where one, two or three stars would normally be."),
 ("- The monthly schedule of assessments.\n- Exact meaning of the gold badge with a diamond symbol.\n", "- Exact meaning of the gold badge with a diamond symbol (Book 12 shows it; the text I read does not explain it).\n"),
])

sub(r"05_Organisations\Magic_Society_and_Associations.md", [
 ("- **Greenstone branch**: directed by Lucian Lamprey (corrupt; Books 1-3), later by Pochard Finn (lorebook). Clive works there under Pochard.",
  "- **Greenstone branch**: directed by Lucian Lamprey (corrupt; Books 1-3), who uses the Fortress as his office; his deputy director Pochard Finn is an elf and a local who runs the city campus and is \"the de facto director of Greenstone's Magic Society\" (Book 1, confirmed). Pochard is Clive's boss. Whether Pochard later became director is a lorebook claim and is unchecked."),
 ("- **Leadership**: Clive is Archchancellor (Book 11, confirmed). Lorelei Grantham, once his sympathetic vice-dean at the Magic Society, is Vice Chancellor (lorebook).",
  "- **Leadership**: Clive is Archchancellor (Book 11, confirmed). Lorelei Grantham is Vice Chancellor (Book 12, confirmed): she first appears in Book 3 as a researcher assigned to work with the Adventure Society's Continental Council, and in Book 6 she is an administrator in the Magic Society's astral magic research wing in Rakesh, where Clive is held. She runs the MRA in Clive's absence and has a portal network project (Book 12, confirmed). Her feelings for Clive are a lorebook claim."),
 ("a rumoured transportation network, the result", "a rumoured transportation network (the \"portal network project\" in Grantham's report), the result"),
])

sub(r"05_Organisations\Guilds_and_Houses.md", [
 ("- **Application** (Book 12): Jason is interviewed in Vitesse; the lorebook says Roland uses the occasion as a lesson and that Team Biscuit withdraws their memberships afterwards (unchecked beyond the opening of the chapter).",
  "- **Application** (Book 12, confirmed in part): the chief membership officer, Neiman Bassingthwaite, tells Jason his membership \"threatens to be the flashpoint that could set the whole guild ablaze\": people opposed to the Remore family's control of the guild see Roland looming over it, and Jason's closeness to the family and the Adventure Society's treatment of him as a diamond-ranker would inflame them. Gabriel Remore complains that his father treats the guild as a personal fiefdom. Roland meets Jason, tells him that to move in their circles he must \"move with consideration rather than emotion\", and Jason answers that power rules. Humphrey then tosses a pouch of guild pins on the table and announces that Team Biscuit withdraws from the guild. Whether Roland deliberately arranged it as a lesson is a lorebook claim and is unchecked."),
 ("Gormanston Bynes is a prominent member; his son Calcifer Bynes is a political figure who runs afoul of Jason. The lorebook adds that Gormanston wants to \"drydock and burn the ship\" and that his niece Juniper is a silver-ranker (unchecked).",
  "Gormanston Bynes is a prominent member. In his own thoughts (Book 10, confirmed) he has concluded that the faction is weak, foolish and oblivious to its path to self-destruction and that the ship must be drydocked and burned to ashes so a new one can be built. His niece Juniper reached silver rank at twenty-two during the surge. His son Calcifer Bynes is Director of the Office of External Affairs, insists on the style \"Lord Bynes\", and runs afoul of Arabelle and Jason."),
])

sub(r"05_Organisations\Earth_Powers.md", [
 ("The lorebook and wiki add that a gold-ranked Earth-born outworlder, \"the Founder\", returned from Pallimustus after a bargain with a god and, with his familiar Noreth, created the Grid; Noreth later betrayed him to the American branch. (The Founder and the bargain are Book 13 briefing material, unchecked here.)",
  "Book 13 (confirmed) calls the Network's founder Jason's \"outworlder predecessor\", whose schemes continue to play out unseen; his familiar was Mr North, a rune spider (North says in Book 5 that he \"was a rune spider, originally\"), and Boris worked with that familiar to betray the founder to the early magic societies that became the Network. The lorebook and wiki add that the founder returned from Pallimustus after a bargain with a god and that he and Noreth created the Grid (unchecked)."),
 ("Marie Finnegan, based in a chalet in Zermatt, Switzerland, is involved in the Book 13 plot (the lorebook says she sabotaged the Grid with a scientist to harvest reality cores; unchecked).",
  "Marie Finnegan, the recently expelled director of the Zurich Network branch, lives in a chalet in Zermatt, Switzerland, and is allied with the vampire queen Elizabeth and the scientist Simon McKean (head of the Earth researchers in the old workgroup) in the Book 13 plot; a dimensional bag holds seven reality cores (Book 13, confirmed). That she sabotaged the Grid to trigger zones is the lorebook's account and is unchecked. The lorebook's four fragments of the Network are also unchecked."),
 ("The lorebook says Mr East was replaced by Adrien Barbou, and that Mrs South (Audrey Blaine) was killed and replaced.",
  "A \"former Mrs South\" gave the Network information about the necromancer (Book 6, confirmed), so she left the EOA. That Mr East was replaced by Adrien Barbou is unchecked; in Book 5 Barbou stands with Mrs West's other flunkies, and in Book 6 Jason demands Barbou from Mr North, who refuses to give him up."),
 ("- **Mr North** (Noreth) is the true leader, very old and not fully human; he was once the Founder's familiar (Book 6, 13; the identification with the rune-spider familiar is lorebook).",
  "- **Mr North** (Noreth) is the true leader, very old and not fully human; he was a rune spider and the Founder's familiar (Books 5, 13, confirmed)."),
])

sub(r"05_Organisations\Cults_and_Orders.md", [
 ("The lorebook adds that they killed mad rulers and hunted necromancers, and that churches bargained with vorger to turn fleeing initiates into flesh abominations (unchecked).",
  "Shade explains (Book 2, confirmed) that the churches, locked out of the sealed astral space, made a second bargain with the vorger, deep-astral entities that can violate dimensional boundaries; the vorger have no physical substance, appear in swarms and warp the bodies of those they affect until the city gains another flesh abomination. The lorebook adds that the Order killed mad rulers and hunted necromancers (unchecked)."),
 ("- **Cult leaders**: Zato (silver-rank, becomes a metal-skinned zealot) and Timos (embedded in Greenstone) per the lorebook; Landemere Vane summoned Jason by mistake; Dougall and Thadwick Mercer become vessels. In Book 10 Beaufort leads the cult in Cardinas and joins Jason's alliance (lorebook).",
  "- **Cult leaders**: Zato, the last silver-ranker left in the cult's local forces (Book 3, confirmed), leads the evacuation of the island stronghold and decamps to the Vane Estate; Timos is an embedded cultist in Greenstone (Book 2, confirmed). Landemere Vane summoned Jason by mistake; Dougall and Thadwick Mercer become vessels (lorebook). In Book 10 Beaufort heads the Cult of the Builder's forces in Cardinas and is Lorenn's uneasy ally (confirmed): a gold-ranker who has given up his essence powers and is \"some manner of semi-artificial monstrosity\", though he looks like a beautiful blond elven man."),
 ("- **People** (lorebook): Melody Jain (local leader), Sendira (raid commander), Laront (priest) and others.",
  "- **People** (Book 8, confirmed): Melody Jain is the overall leader of the order's local operations, with her second Sendira and church adviser Laront (a Purity priest who never passed through the flames, so he can safely visit cities). Cell leaders are silver like their commanders, a source of constant tension; some resent Melody's use of the order for her own ends. Other names are lorebook only."),
])
print("org fixes applied")

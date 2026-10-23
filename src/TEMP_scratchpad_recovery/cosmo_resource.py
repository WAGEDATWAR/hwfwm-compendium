root = r"C:\Users\Gabriel\Documents\World Stuff\HWFWM Compendium"

def sub(rel, pairs):
    p = root + "\\" + rel
    s = open(p, encoding="utf-8").read()
    for a, b in pairs:
        assert a in s, (rel, a[:80])
        s = s.replace(a, b)
    open(p, "w", encoding="utf-8").write(s)

sub(r"02_Cosmology_and_Powers\Gods_and_Churches.md", [
 ("Carlos Quilido is a Healer priest (Books 9, 13).", "Carlos Quilido is a Healer priest who joins the Cardinas expedition (Book 11)."),
])

sub(r"02_Cosmology_and_Powers\00_Cosmology_Overview.md", [
 ("Status: Draft (compiled from the lorebook and chapter notes; the key claims marked \"confirmed\" were checked against the book text)",
  "Status: Draft (book text, chapter notes and wiki; tiers marked: \"Book N\" = checked in the book text, \"notes\" = chapter notes, \"wiki\" = fan wiki)"),
 ("Whether reality cores act as batteries, and whether universes are \"seeds\", are lorebook claims; in Book 11 a messenger says only that Jason \"is a seed that the World-Phoenix planted\".",
  "In Book 11 a messenger says Jason \"is a seed that the World-Phoenix planted\"; whether reality cores act as batteries and whether universes are \"seeds\" are not established in the text I checked."),
 ("Lorebook: it exists in a *set* state (put to a purpose, like a clay bowl or a spirit domain) and a *potential* state (raw, like enriched uranium).",
  "Jason's Book 8 lecture distinguishes a *set* state (authority put to a purpose, \"clay turned into a bowl\", as in his spirit domains) from a *potential* state (raw, like enriched uranium) (Book 8; notes, Book 8)."),
 ("Gordon's orrery rituals are an example (lorebook).", "Gordon's orrery ritual is an example: Jason is told that Gordon can use intrinsic-mandate magic, which operates on the same scale as a great astral being (Books 9-10)."),
 ("That the nameless are functionary GABs of life, death, time and matter, unbound while the Throne is sundered, is the lorebook's gloss.",
  "The notes describe the nameless as great astral beings who are functionaries of cosmic mechanics (life, death, time, matter), unbound without the throne (notes, Book 11)."),
 ("That not even the Keeper can affect the past is Shade's claim in the lorebook and is unchecked.", "Shade tells Jason that, for the Keeper, \"the past is inviolate\" (Book 6)."),
])

sub(r"02_Cosmology_and_Powers\Astral_Kings_and_Messengers.md", [
 ("Status: Draft (lorebook and notes; items marked \"confirmed\" were checked against the book text)",
  "Status: Draft (book text, chapter notes and wiki; tiers marked: \"Book N\" = checked in the book text, \"notes\" = chapter notes, \"wiki\" = fan wiki)"),
 ("- **What they are** (wiki, lorebook): immortal beings who rule a miniature universe, usually containing at least one solar system with planets, with complete control over its physics and magic, even over whether the beings inside can die.",
  "- **What they are**: \"what amounts to sentient miniature universes\" (Jason's lecture, Book 8); the wiki adds immortal beings who rule their own universe with complete control over its physics and magic, even over whether the beings inside can die (wiki)."),
 ("that messengers consider themselves the highest life in the cosmos and that their message is \"Kneel\" are lorebook claims.",
  "The notes record that messengers are messengers of astral kings, whose message is \"Kneel\", and that astral kings rule through them rather than invading in person (notes, Book 8)."),
 ("The lorebook's specific claim that messengers are capped at silver by a seal that siphons their potential, and that diamond messengers may become astral kings, is unchecked.",
  "A silver seal on messengers is mentioned in Book 9 (Vesta Carmis Zell \"feels her silver seal vanish\" when Jason frees Tera; notes, Book 9), and diamond messengers can begin to resist the brand (notes, Book 11). Whether messengers are strictly capped at silver is not established."),
 ("- **Birth**: the lorebook says messengers are \"budded\" like plants (unchecked).",
  "- **Birth**: Jason says messengers are \"budded, not born\" and are \"actually plants, which is kind of crazy\" (Book 12)."),
 ("Jamis Fran Muskar appears as a messenger speaking for a larger body (the lorebook calls him a Council of Kings avatar).",
  "Jamis Fran Muskar is an astral king whose avatar attends the Book 10 scene; his avatar stands out because its wings have been completely absorbed into his body (Book 10), and in Book 12 he angrily accuses messengers of defying \"the explicit instructions of the Council of Kings\" (Book 12)."),
 ("What the debt is, and what the Council of Kings is, are lorebook claims that remain unchecked.", "What the debt is remains unexplained in the text I checked."),
])

sub(r"02_Cosmology_and_Powers\Great_Astral_Beings.md", [
 ("Status: Draft (lorebook and notes; items marked \"confirmed\" were checked against the book text)",
  "Status: Draft (book text, chapter notes and wiki; tiers marked: \"Book N\" = checked in the book text, \"notes\" = chapter notes, \"wiki\" = fan wiki)"),
 ("they recruit others to act for them (Clive on the Builder, Book 3; the lorebook's wider description).", "they recruit others to act for them (Clive on the Builder, Book 3)."),
 ("- **Mortal form**: the lorebook says their true state is mindless and alien, but they enjoy mortal bodies (unchecked).", "- **Mortal form**: great astral beings enjoy mortal bodies (notes, Book 11)."),
 ("pacts between GABs (the lorebook names the Builder, Reaper and World-Phoenix) restrict their direct meddling.",
  "pacts between GABs restrict their direct meddling. Dawn tells Shako in Book 6 that by killing Jason he violated the compact between the Builder, the Reaper and the World-Phoenix (notes, Book 6)."),
 ("Gordon was created by it (lorebook).", "Gordon comes from its realm (Book 8)."),
 ("| Legion | Life (lorebook) | Came around. |", "| Legion | Administers the cosmic rules that govern life (Book 8) | Came around (Book 11). |"),
 ("The lorebook describes the nameless as functionary GABs that run cosmic mechanics (life, death, time, matter) and are unbound while the Throne is sundered; that gloss is unchecked.",
  "The notes describe the nameless as functionaries of cosmic mechanics (life, death, time, matter), unbound without the throne (notes, Book 11). In Book 12 Jason is told the nameless \"are unhappy, as they would be with anything short of complete cosmic anarchy\" (Book 12)."),
 ("Lorebook examples: Purity sanctioned himself by pouring his authority into an artefact; Shade sanctioned himself into the Shadow of the Hegemon; Hero sanctioned himself; the World-Phoenix sanctioned the Boundary into herself.",
  "Examples in the text: the Boundary sanctioned itself into the World-Phoenix (Book 11); Shade sanctioned himself into a Shadow of the Hegemon (Book 11); Hero decided to sanction himself (Book 11); Purity was likely about to sanction himself when Knowledge interfered, and the wiki says he expended his authority on a single artefact (Book 13; wiki)."),
 ("Clockwork Kings (the lorebook's native rulers of the Builder's world).", "Clockwork Kings, gold-rank native creatures of the Builder's world, dragon-like and not monsters, whose cores make the cult's clockwork cores (notes, Book 2)."),
 ("(lorebook; Book 8).", "(Book 6 and Book 8 notes)."),
 ("Appears in mortal form with red hair, white clothes with orange and fire wings (lorebook).", "She speaks of the Boundary in her own words in Book 11 (Book 11)."),
 ("later fights Jason in the Rumble in the Jungle and admires him (lorebook).", "in the Rumble in the Jungle, the soul-space battleground where Jason's team stands against the nameless great astral beings (Book 11)."),
 ("- **Prime vessel**: Helsveth (lorebook).", "- **Prime vessel**: Helsveth (Book 11)."),
])
print("cosmology resourced")

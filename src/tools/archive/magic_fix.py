p = r"C:\Users\Gabriel\Documents\World Stuff\HWFWM Compendium\03_Magic_and_Adventuring\Magic_and_Adventuring.md"
s = open(p, encoding="utf-8").read()

def rep(a, b):
    global s
    if a not in s:
        print("MISSING:", a[:70])
    s = s.replace(a, b)

rep("Status: Draft (spot-checked against the book text: confluences, racial gifts, ranks and lifespans, core use, monster names; other sections not yet verified; claims first drafted from the lorebook have not all been re-sourced, see TODO_Verification.md section G)",
    "Status: Draft (audited claim by claim against the book text, chapter notes and wiki; claims found in none of the three were removed, and remaining open items are in TODO_Verification.md section B)")
rep("Sources: Books 1-13 (chapter notes); fan wiki for essence, stone and confluence lists", "Sources: book text, chapter notes, fan wiki (essence, stone and confluence lists)")

# 1.5
rep("The Adventure Society and other bodies **restrict** essences judged too dangerous: Death, Corrupt, Sacrifice, Undeath and Succubus are examples. The Society pays for [Death] and [Corrupt] essences to take them out of circulation and has put contracts on users of the Sacrifice confluence. Restrictions are enforced by the Society's checks (a Knowledge priest can check at some temples) and the Magic Society's records. Jason's Doom confluence is unrestricted. Dark gods' followers sometimes use restricted essences.",
    "The Adventure Society keeps a list of **restricted** essences that pose an inherent threat to ordinary people, with Death at the top (Book 1); Undeath (Blood + Death + anything) and Succubus are restricted combinations (notes, Book 1). Society representatives offer good trades for restricted essences to take them off the market: Sophie trades a death essence for two epic awakening stones (Book 2).")

# 2
rep("  - **Dragon** (Humphrey; reached through Might + Wing, a supernatural-creature confluence): includes the Spartoi summons.",
    "  - **Dragon** (Humphrey, Book 1): Humphrey and Taika share the Might and Wing essences, which lead to a confluence based on a mythical creature (Book 9); Humphrey's familiar and the Spartoi summons belong to it.")
rep("  - **Garuda** (Taika; Might + Wing and a third essence): chosen instead of the Immortal confluence that Renewal would have brought.",
    "  - **Garuda** (Taika, Book 9): the Might and Wing route, as opposed to Humphrey's Dragon; in Book 4 Jason had planned to give Taika a Renewal essence for an Immortal confluence.")
rep("  - **Prosperity** (Shield + Growth + Renewal; Neil): short-lived shields, healing and cleansing; the essence is also the usual source of abilities that loot monsters and produce spirit coins.",
    "  - **Prosperity** (Shield + Growth + Renewal; Neil, Book 2): healing and cleansing, short-lived shields, and empowering allies and replenishing their mana and stamina.")
rep("  - **Onslaught**: an aggressive fighting confluence (Clive notes that swapping Balance for Might in a Mystic combination produces it); Thalia Mercer's essence informs both her powers and her inclinations.",
    "  - **Onslaught**: Clive notes that swapping Balance for Might in a Mystic combination produces it (Book 2); Thalia Mercer's Onslaught essence informs both her powers and her inclinations (Book 13).")
rep("  - **Master** (various skill combinations): swords and skill-heavy fighters (Valdis, Akari).",
    "  - **Master**: Valdis's sword, swift and adept (Book 3); Akari's sword, adept and magic (notes, Book 5); Woolzy's swift foot and knife (Book 4).")

# 5
rep("Each is raised by the essence abilities connected to it, and each has a rank (iron to diamond) with progress within the rank. A person's overall rank is limited by their lowest attribute. Past bronze, high Spirit sharpens senses; past silver, attributes become \"impossible for a normal person\".",
    "Each is raised by the essence abilities connected to it (an attribute advances in conjunction with the lowest-rank ability of its linked essence, Book 2), and each has a rank (iron to diamond) with progress within the rank. A person cannot advance further until all attributes have reached the next rank (Book 5). At silver, attributes become \"impossible for a normal rank person\" (wiki).")

# 6.1 table
rep("| Rank | Lifespan (wiki figures; not checked against the books) | Notes |", "| Rank | Lifespan (Book 1, Rufus) | Notes |")
rep("| Normal | ~60-75 years | Includes people with one to three essences |", "| Normal | ordinary lifespan | Includes people with one to three essences |")
rep("| Iron | decade or more longer | Four essences; purge; spirit-coin sustenance |", "| Iron | little difference noticeable | Four essences; purge; spirit-coin sustenance |")
rep("| Bronze | ~100 years | All abilities awakened and at bronze |", "| Bronze | well past a hundred | All abilities awakened and at bronze |")
rep("| Silver | ~200 years | Killing blows no longer kill; aura levitation |", "| Silver | double that (about two hundred, wiki) | Killing blows no longer kill (wiki); aura levitation |")
rep("| Gold | ~500 years | No need to breathe; revival only within a short window |", "| Gold | centuries | No need to breathe; resurrection possible only within minutes |")
rep("| Diamond | ageless | Peak of mortal power |", "| Diamond | rumoured not to die of old age | Peak of mortal power |")

# 6.2
rep("- **Gold**: breath is optional; centuries of life (the wiki gives about five hundred years). Advancement now needs **essence revelations** (insight into the concept behind each essence); monster fighting is a small part of progress, and core use makes revelation significantly harder. Some core users still reach gold (a bureaucrat in the books did), but most do not.",
    "- **Gold**: breath is optional; centuries of life. Advancement is said to need **essence revelations** (insight into the concept behind each essence; wiki), and core use makes this harder. Some core users still reach gold (the gold-rank director Musin Heath is one, notes Book 10), but most do not (Book 1).")
rep("- **Diamond**: ageless; rulers and sovereigns of their regions; \"after about half a millennium they are expected to step back\".",
    "- **Diamond**: rumoured not to die of old age (Book 1); mysterious figures who pursue goals known only to them, and for whom the idea of a higher authority is laughable (Book 1).")

# 6.4
rep("To rank up a person must have every ability at the next rank and all four essences filled; then \"a rank-up goo\" or a \"purge\" occurs: the body is rendered to light and rebuilt, expelling impurities, sometimes needing crystal wash to clean up. Changes are physical too: iron-rank people become healthier; gold bodies are idealised; faces and builds drift toward the person's self-image (Jason looks more like Kaito each rank). **Rank-ups take years**. Bronze to silver takes about five to ten years for most (three for the elites), Jason achieved it in about a year and a half at bronze; reaching gold takes longer for most.",
    "To rank up a person must have all attributes at the next rank (Book 5). Changes are physical too: souls act as a blueprint for the body and looks drift toward the person's self-image (Jason looks more like Kaito after ranking, notes Books 4 and 13). The first rank-up, to iron, includes a purge of impurities (Jason vomits pus, notes Book 1).")

# 6.5
rep("Silver 4-5 progress \"all but stops\": raw training is no longer enough. Allayeth describes it as a barrier of insight; peaceful, introspective people pass more easily. Those who rely on cores plateau. The concept is the essence's idea: each essence expresses an identity.",
    "Core-users stall by silver (Book 1), and the Quilido Procedure, which removes the taint of monster cores, is said to unlock silver-stuck veterans on Earth (notes, Book 13). The books searched give no other account of a \"wall\" at high silver.")

# 7
rep("Wealthy families sometimes pay for a cadre of core-fed gold-rankers, but adventurers, who produce wealth rather than consume it, are more respected. Per the wiki, core use also makes essence revelation much harder (Amos and Carlos, Book 9).",
    "")
rep("- **Cure**: the Quilido Procedure (developed by Carlos Quilido) slowly removes residual core effects; the Purity relic might do it instantly. **(Later: Book 12-13)**",
    "- **Cure**: the Quilido Procedure removes the taint of monster cores from an essence user; it is slow and resource-intensive (Book 13). Jason also mentions a relic fought over on Pallimustus that could purge residual monster cores (Book 13). **(Later: Book 13)**")

# 15
rep("**Resurrection** works only inside a short window and only at gold-rank healing; it fails on gestalts and is blocked by the Death goddess's pact for Jason.",
    "**Resurrection**: the soul lingers with the body from seconds to an hour and a gold-rank healer can reverse death in that grace period (notes, Book 2); by Book 9 Neil says it has been harder for a few years and, even at gold rank, allows only minutes. It does not work on messengers or anyone like them (gestalts; notes, Book 9).")
rep("- **Crests**: a soul crest, applied by a tattooist, identifies a person for the Adventure Society.", "- **Crests**: a soul crest is a magical tattoo printed on the soul, which appears on the body (Book 2); it lets a person be identified without relying on the aura (Book 3).")
rep("- **Undeath** is the corruption of the cycle; its priests are reviled; vampires are a related magical sickness.\n", "")

# 16
rep("Sophie's Boundary Breaker (from Astral Affinity; it removes the damage reduction from rank disparity)", "Sophie's Boundary Breaker (from Astral Affinity; it ignores rank-disparity resistances and aura-suppression bonuses, notes Book 3)")
rep("is forward-only; the Keeper of Moments polices time travel.", "can only go forward; the Keeper of Moments cannot affect the past (Book 6).")

# 17
rep("Earth's Network uses categories (0 to 5), affinity gems (quintessence), mana lamps and monster cores; its members rarely reach gold without cores. Cabal vampires are \"tiers\". Earth's magic did not support monsters until the Grid failed. After Jason's repairs the planet's magic is lower than Pallimustus's but permits lesser and iron monsters, essences and stones appearing directly; transformation zones transformed millions into magical races. Spirit coin farms and magitech arrived in the 2030s.",
    "Earth's Network uses categories (0 to 5), affinity gems (quintessence), mana lamps and monster cores. The Cabal's vampires are graded in tiers (wiki). Earth's magic did not support monsters until the Grid failed (Books 5-6); transformation zones change cities and their people into other races (Books 5, 6, 11).")

# 18
rep("- Resurrection becomes harder (Reaper and gods change the rules).", "- Resurrection has become harder (Neil, Book 9).")
rep("- The Builder withdraws (Book 8); messengers invade (Book 9).\n", "- Messengers appear in force at Yaresh (Book 9).\n")
rep("- Advancement research (Quilido Procedure, Tribulation Lightning) offers ways to clear core residue (Book 13).", "- Earth's advancement research (the Quilido Procedure) offers a way to clear core taint (Book 13); Bussinger's Tribulation Lightning purges her own afflictions by harming her (notes, Book 13).")
open(p, "w", encoding="utf-8").write(s)

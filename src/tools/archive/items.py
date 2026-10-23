import os
base = r"C:\Users\Gabriel\Documents\World Stuff\HWFWM Compendium\09_Items_and_Artefacts"
os.makedirs(base, exist_ok=True)
HDR = """# {name}

Status: Draft (book text; facts carry a reference "Book N, ChX LY" to Source_Text; "notes" marks chapter-summary-only facts)
Spoiler level: {spoil}
Valid from: Book {vf}
Valid through: Book {vt}
Sources: {src}
Related: {rel}

## 1. Summary

{summary}

## 2. Facts

{facts}

## 3. Using this in a story

{rp}
"""
def write(fn, name, spoil, vf, vt, src, rel, summary, facts, rp):
    open(os.path.join(base, fn + ".md"), "w", encoding="utf-8").write(HDR.format(name=name, spoil=spoil, vf=vf, vt=vt, src=src, rel=rel, summary=summary, facts=facts, rp=rp))

write("00_Items_Overview", "Items and Artefacts: Overview", "0 for Books 1-5; 2-3 for tokens and Book 8 onward", "1", "13",
 "Books 1, 2, 3, 5, 6, 8, 10 (chapter files)",
 "Soul_Bound_Items_and_Regalia.md, Tokens_Stones_and_Relics.md, Consumables_and_Trial_Rewards.md, ../04_Peoples_and_Cultures/Economy_and_Money.md, ../07_Characters/Jason_Asano.md",
 "How the story's items are described by the System: rank, rarity, kind, bound status and effect lines, and the main named items in Jason's possession.",
 "- **Item windows**: the System shows each item with a rank and rarity in the form \"Item: [Dread Salvation] (iron rank [growth], legendary)\", then a description, a kind in brackets and effect lines (Book 1, Ch56 L49-52). Unidentifiable items show question marks, such as the \"transcendent rank, legendary\" World-Phoenix Token with \"???\" effects (Book 1, Ch1 L103-107).\n- **Growth items** have a rank that can rise; soul-bound growth items are rare, Clive says, and the advancement requirements are \"usually quite prohibitive\" (Book 2, Ch74 L45-46).\n- **Bound items** \"cannot be used by anyone else\" (Book 2, Ch74 L36; Book 6, Ch4 L33).\n- **Currency items** are covered in `../04_Peoples_and_Cultures/Economy_and_Money.md`; essences and awakening stones in `../03_Magic_and_Adventuring/Magic_and_Adventuring.md`.\n- **Rarities seen**: common, uncommon, rare, epic, legendary, and \"unavailable\" for the Fundamental Realm Authority Token (Book 8, Ch50 L87).\n- **Tiers of power**: ordinary items are ranked iron to gold; astral blessing tokens and divine awakening stones are \"transcendent rank\" (Book 2, Ch63 L38; Book 2, Ch13 L60).",
 "Describe items the way the System does, in rank, rarity and bound status, and keep the question-marked transcendent items vague until a character earns the power to read them.")

write("Soul_Bound_Items_and_Regalia", "Soul-Bound Items and the Regalia of the Dark Hegemon", "0 for Books 1-5; 1 for the Book 6 set", "1", "6",
 "Books 1, 2, 5, 6 (chapter files)",
 "00_Items_Overview.md, ../07_Characters/Jason_Asano.md, ../07_Characters/Gary.md",
 "Jason's three soul-bound growth items, joined in Book 6 into the Regalia of the Dark Hegemon by the Soul-Imprinting Triune, plus the Robes of the Astral Verdict.",
 "- **Dread Salvation**: a sword \"crafted with gratitude, in hope it would be of the greatest use in the moment of greatest need\"; \"iron rank [growth], legendary\"; when an affliction special attack meets a physical immunity it gains Stone Cutter, and for a magical immunity Spell Breaker (Book 1, Ch56 L49-52). Gary made it, as a gift (Book 1, Ch56 L47).\n- **Dread Salvation in Book 6**: bronze rank, bound to Jason and sharing his ability to ignore rank disparity; it can be imbued with aura for damage at an ongoing mana cost; \"The original creator must demonstrate his growth and reforge the weapon\" (Book 6, Ch4 L72-77). The window says it \"must be reforged by the original craftsperson in order to advance further\" (Book 6, Ch4 L82). The wiki's name for the reforged sword, \"Hegemon's Will\", does not appear in the text searched (wiki).\n- **Cloud Flask**: iron rank growth item that Jason binds in Book 2; it creates cloud buildings and vehicles, with forms limited by rank (Book 2, Ch74 L34-46). By Book 6 it is silver rank, with the cloud house at iron, cloud vehicle at bronze and cloud palace at silver (Book 6, Ch4 L42-50). Its maker is \"some unknown diamond-rank craftsman\" (Book 6, Ch4 L40).\n- **Amulet of the Dark Guardian**: silver rank growth item, the last item produced by his old quest system, a reproduction of his personal crest on an obsidian chain (Book 6, Ch4 L29-39). Its boon Guardian's Blessing absorbs damage per affliction applied and can be given to another person by touch (Book 6, Ch4 L34-37).\n- **Soul-Imprinting Triune**: Jason receives it with a hoard of spirit coins in Book 5 (Book 5, Ch29 L77-80); it turns three soul-bound growth items into a set when all three are on his person (Book 6, Ch4 L6-8).\n- **Regalia of the Dark Hegemon**: the set bonuses are Hegemon's Authority from the amulet (allies in his aura resist aura suppression, and he can spend instances to strengthen his own suppression), a mist shroud from the cloud flask, and mana drain with Hegemon's Tribute from the sword (Book 6, Ch4 L35-38, L47, L79-80).\n- **Robes of the Astral Verdict**: bronze rank, rare cloth armour for summoners that boosts dimension spells, summon damage reduction and disruptive-force resistance (Book 1, Ch7 L17-21).",
 "Keep the three Regalia items together on his person; losing any one breaks the set. Gary's reforging is the open thread that the Regalia window itself states.")

write("Tokens_Stones_and_Relics", "Tokens, Stones and Relics", "2-3", "1", "10",
 "Books 1, 2, 3, 6, 8, 10 (chapter files)",
 "00_Items_Overview.md, ../02_Cosmology_and_Powers/Great_Astral_Beings.md, ../02_Cosmology_and_Powers/Gods_and_Churches.md",
 "Transcendent-rank items that mark the favour or authority of great astral beings and gods: astral blessing tokens, divine awakening stones, the Fundamental Realm Authority Token and the Cup of Heroes.",
 "- **Astral blessing tokens**: Clive says they are \"something great astral beings give out to bestow blessings, as signs of approval\"; they trigger racial gift evolutions, and are harmless, unlike star seeds (Book 2, Ch63 L45-47).\n- **World-Phoenix Token**: Jason finds it in his starting inventory, \"transcendent rank, legendary\", \"Uses remaining: 1/1\" with unreadable effects (Book 1, Ch1 L103-107). It is consumed in Book 3 (Book 3, Ch69 L108).\n- **Reaper Token**: an obsidian square engraved with a silver scythe, \"transcendent rank, legendary\" (Book 2, Ch63 L37-38). Jason takes the Scythe of the Reaper by placing his inventory window behind it, and the token is added (Book 2, Ch60 L173-179). It is melded into his body with the awakening stone of the Reaper in Clive's ritual and consumed (Book 2, Ch63 L65-82).\n- **Knowledge's token**: a small stone square like the World-Phoenix Token but washed-out blue, offered with two awakening stones (Book 2, Ch13 L57); Jason is told it would take him home and wonders whether to trust it (Book 2, Ch73 L58).\n- **Divine Awakening Stone of Inevitability**: \"transcendent rank, epic\", crafted by a god to bestow a specific aura power (Book 2, Ch13 L60). The Soul-Purgation Tablet (aura) removes an existing aura essence ability and cannot be forcibly used on another (Book 2, Ch13 L76-78).\n- **Fundamental Realm Authority Token**: \"transcendent rank, unavailable\", bound to Jason and usable only by him and Zithis Carrow Vayel; it lets the wielder open gates to the fundamental realm of any physical reality (Book 8, Ch50 L87-91). Jason looted it from the destroyed artefacts (Book 8, Ch50 L94-95). Dawn tells him \"You can't have this\" and that he will need to give it back (Book 8, Ch51 L68-70).\n- **Firmamental Bridge Anchor**: the other looted item, \"transcendent rank, legendary\", with unreadable effects and one use (Book 8, Ch50 L97-100).\n- **Cup of Heroes**: the god of heroes' offer of divine power; Gary \"has drunk from the Cup of Heroes\" and the window warns the divine power will work to leave his soul and rejoin the god (Book 10, Ch86 L59-61).",
 "These items are leverage between beings, not loot; their descriptions should stay incomplete until the owner is strong enough to read them.")

write("Consumables_and_Trial_Rewards", "Consumables, Trial Rewards and Crafting Materials", "0 for Books 1-3; 2 for Books 5-6", "1", "6",
 "Books 1, 2, 5, 6 (chapter files)",
 "00_Items_Overview.md, ../06_Places/Astral_Spaces/City_of_Fallen_Echoes.md, ../05_Organisations/Cults_and_Orders.md",
 "Single-use and crafting items: the City of Fallen Echoes rewards, clockwork cores, reality cores and star seeds.",
 "- **Lesser Miracle Potion**: \"iron rank, legendary\", \"Salvation in a bottle\", it fully restores health, mana and stamina but only works on normal and iron-rank people, and its lingering magic delays other recovery (Book 2, Ch44 L127-129).\n- **Medallion of Escape**: \"silver rank, uncommon\", evacuates the holder from the astral space when their aura is projected into it, and only works inside the City of Fallen Echoes (Book 2, Ch44 L120-123).\n- **Immortal Crest**: \"iron rank, rare\", lets a mystical tattooist draw out a soul crest and only works on an iron-rank essence user (Book 2, Ch58 L102-104).\n- **Summoner's Die: Form**: \"iron rank [growth], legendary\", it randomly alters the form of an iron-rank summon (Book 2, Ch58 L53-56).\n- **Clockwork Core**: \"iron rank, rare\", the core of an artificial monster that simplifies the materials and processes of a construct creature; clockwork cores are made by clockwork kings (Book 2, Ch25 L24-26, L35).\n- **Star seeds**: great astral beings, not gods, \"can send their followers star seeds\"; once implanted and germinated the body transforms, \"minor or major\" (Book 2, Ch21 L26-28).\n- **Reality cores**: roughly the size and shape of an ostrich egg, dark crystal glowing with transcendent light; one appears in each affected zone and the factions scramble for it (Book 5, Ch45 L9-11). They are the source of the transformation zones' treasures and are common in node space (Book 6, Ch1 L20).",
 "These rewards are meant to be spent. A potion or medallion is a story decision, not an inventory slot.")
print("ok")

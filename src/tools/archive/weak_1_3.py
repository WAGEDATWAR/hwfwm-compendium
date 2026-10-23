import os
B = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", ".."))


def edit(rel, pairs):
    p = os.path.join(B, *rel.split("/"))
    s = open(p, encoding="utf-8").read()
    for o, n in pairs:
        if o not in s and n in s:
            continue
        assert o in s, (rel, o[:70])
        s = s.replace(o, n, 1)
    open(p, "w", encoding="utf-8").write(s)


edit("01_World_Primer.md", [(
    "Greenstone has loop-terminal transit (Book 1, Ch45 L4); wealthy homes have magical plumbing and lighting; Vitesse has living plants on buildings; Rimaros is a city of floating islands.",
    "Greenstone has a loop terminal that opens onto a street of temples (Book 1, Ch45 L4). Only the wealthiest residents of Old City have magic-driven indoor plumbing (Book 1, Ch71 L7). Vitesse's cloud palace has lush plants growing out of its walls and columns (Book 2, Ch40 L3). Rimaros has islands floating in the sky (Book 7, Ch7 L3).")])
edit("03_Magic_and_Adventuring/00_Magic_Overview.md", [(
    "Book 4 moves to Earth, where ranks are tiers and the Grid contains the leaks (Book 4, Ch11 L4-22; Book 5, Ch5 L11).",
    "Book 4 moves to Earth, where magical ranks are named tiers that start at zero (Book 4, Ch11 L9-10). The Grid works as interconnected rituals built from the natural features of the world (Book 5, Ch5 L11).")])
edit("03_Magic_and_Adventuring/Abilities_and_Attributes.md", [(
    "Several abilities rank in the same stretch of Book 3 (Book 3, Ch21 L121, L136; Ch29 L23; Ch38 L5).",
    "Several abilities reach Bronze 0 in the same stretch of Book 3: [Sanguine Horror] (Book 3, Ch21 L121), [Hegemony] (Book 3, Ch21 L136), [Path of Shadows] (Book 3, Ch29 L23) and [Blade of Doom] (Book 3, Ch38 L5).")])
edit("03_Magic_and_Adventuring/Awakening_Stones.md", [(
    "(for example Book 1, Ch4 L40; Book 2, Ch5 L105-107; Book 2, Ch63 L25; Book 9, Ch78 L129).",
    "Examples: the stars (Book 1, Ch4 L40); eyes, hand and foot (Book 2, Ch5 L105-107); avatar, rebirth and celestial (Book 2, Ch63 L25); defiance (Book 9, Ch78 L129).")])
edit("03_Magic_and_Adventuring/Essences.md", [(
    "Sin is among the rarest (Book 1, Ch20 L104).",
    "Farrah says the sin essence is in the rarest category (Book 1, Ch20 L104).")])
edit("03_Magic_and_Adventuring/Monsters.md", [(
    "Transformation zones spawn anomalies (Book 6, Ch2 L10).",
    "Jason defeats a silver-rank living anomaly of the kind a transformation zone produces (Book 6, Ch2 L10, L31).")])
edit("06_Places/Greenstone.md", [
    (", and the Old City's mayor answers to him (Book 12, Ch29 L38 gives the mayor; that he answers to the Duke is unchecked).",
     ". Adris Dorgan, once a crime lord, is mayor of Old City by Book 12 (Book 12, Ch29 L38); that the mayor answers to the Duke is unchecked."),
    ("(the Duke rules the city, Book 1, Ch36 L71; that the mayor answers to him is an inference)",
     "(the Duke rules the city; that the mayor answers to him is an inference)"),
])
edit("06_Places/Yaresh.md", [(
    "Rufus (in Yaresh in Book 9, Ch42 L34).", "and Rufus, who is in Yaresh in Book 9 (Book 9, Ch42 L34).")])
edit("06_Places/Astral_Spaces/Spirit_Vault_and_Astral_Kingdom.md", [(
    "the flesh pit, a subterranean blood-and-flesh space tied to the Colin summoning stone (Book 10, Ch33 L109-111), and the Colin greenhouse.",
    "the flesh pit, and the Colin greenhouse. The flesh pit is where a sanguine horror was summoned and killed and the stone for Colin was looted, and it is now Colin's (Book 10, Ch33 L109-111).")])
edit("06_Places/Minor_Places/Kurdansk.md", [(
    "the city locks criminals up for years, which a Book 12 speaker calls costly to run (Book 12, Ch49 L77).",
    "the city locks criminals up for years, and a Book 12 speaker asks about the operating costs of such places (Book 12, Ch49 L77).")])

edit("07_Characters/Anisa_Lasalle.md", [(
    "Cold, righteous and quick to anger; she treats mercy as weakness (Book 1, Ch30 L26).",
    "Cold, righteous and quick to anger; she treats mercy as weakness. Farrah says Anisa killed a man before he could get a word out (Book 1, Ch30 L26).")])
edit("07_Characters/Anna_Tilden.md", [(
    "in Book 12 Nigel Thornton's team works for her and she sends him to Rexion (Book 12, Ch10 L94; the contract-operative detail is from notes, Book 12).",
    "Nigel Thornton's team is most often contracted by her (Book 12, Ch3 L7), and Nigel says he came to Rexion on her job (\"Anna Tilden. You know her, right?\", Book 12, Ch10 L94).")])
edit("07_Characters/Beth_Cavendish.md", [(
    "Competent and brisk, a clear team leader who gives orders without ceremony (Book 1, Ch89 L77).",
    "Competent and brisk, a clear team leader who gives orders without ceremony. She directs the team: \"We're going to move on the sand barge\" (Book 1, Ch89 L77).")])
edit("07_Characters/Belinda_Callahan.md", [(
    "Delighted by her own cleverness, and teasing. Cues: Book 2, Ch32 L72; Book 7, Ch6 L42.",
    "Delighted by her own cleverness, and teasing. Cues: \"Charlatan,\" she says with glee (Book 2, Ch32 L72); she urges Jason to find an excuse to head up on deck where Sophie can see him (Book 7, Ch6 L42).")])
edit("07_Characters/Boris_Ket_Lundi.md", [(
    "Measured and careful. Cue: Book 11, Ch68 L493-498.",
    "Measured and careful. Cue: \"I am unfortunately inclined to agree,\" he tells Taika, and says he will attempt to simplify their situation (Book 11, Ch68 L493-498).")])
edit("07_Characters/Callum_Morse.md", [
    ("- Book 13: part of the expedition (Book 13, Ch958 L75).",
     "- Book 13: part of the expedition, tracking a creature in a pipe with conjured rats (Book 13, Ch958 L75)."),
    ("Quiet, patient and unfazed; he lets a hard decision stand and speaks plainly (\"Sensible\", Book 2, Ch36 L79).",
     "Quiet, patient and unfazed; he lets a hard decision stand and speaks plainly. He answers a plan with \"Sensible\" (Book 2, Ch36 L79)."),
])
edit("07_Characters/Cheryl_Asano.md", [(
    "- Present when the family gathers in Book 4 (Book 4, Ch45 L76).",
    "- Present when the family gathers in Book 4, where Amy puts a restraining hand on Cheryl's arm (Book 4, Ch45 L76).")])
edit("07_Characters/Clive_Standish.md", [(
    "A lecturer who loses the thread and apologises. Cue: \"Where were we?\" (Book 11, Ch68 L748); eel jokes (Book 1, Ch68 L92-94).",
    "A lecturer who loses the thread and apologises. Cues: \"Sorry. Where were we? Right, formation interactivity\" (Book 11, Ch68 L748); \"Having a conversation with you is like wrestling an eel\" (Book 1, Ch68 L92-94).")])
edit("07_Characters/Danielle_Geller.md", [
    ("and teases her son at once when she hears a name: \"Gabrielle?\" (Book 1, Ch47 L89).",
     "and teases her son at once when she hears a name: \"Gabrielle?\", in a tone of having latched on to a weakness (Book 1, Ch47 L89)."),
    ("Blunt, quick to seize a weakness. Cues: Book 1, Ch47 L89; \"diplomacy is war\" (Book 12, Ch23 L79).",
     "Blunt, quick to seize a weakness. Cues: \"Gabrielle?\", asked as if she has latched on to a weakness (Book 1, Ch47 L89); \"I said that diplomacy is war, Jason, and wars have objectives\" (Book 12, Ch23 L79)."),
])
edit("07_Characters/Dawn.md", [(
    "Formal, with a teasing edge. Cue: Book 5, Ch20 L21-24.",
    "Formal, with a teasing edge. Cue: \"You realise that you could have asked that instead of punching my nose through my brain\" (Book 5, Ch20 L21).")])
edit("07_Characters/Dustin_Kettering.md", [(
    "- Book 10-11: fights in Cardinas with Neil and the brighthearts (Book 10, Ch70 L38; Book 11, Ch6-20).",
    "- Book 10-11: fights messengers on Rick's team, where Stash smashes him and Rick together (Book 10, Ch70 L38); in Book 11 he and Neil claim a territory as a defender-healer pair (Book 11, Ch8 L23).")])
edit("07_Characters/Emir_Bahadir.md", [(
    "Smooth, showy and fond of an entrance. Cues: Book 3, Ch5 L9; Book 3, Ch69 L509.",
    "Smooth, showy and fond of an entrance. Cues: Emir liked big entrances, as seen in the grandiose arrival of his crew (Book 3, Ch5 L9); \"Merfolk are not fish\" (Book 3, Ch69 L509).")])
edit("07_Characters/Hess_Jor_Nasala.md", [(
    "Deferential and careful; he speaks only when he has something worth saying (Book 9, Ch66 L41).",
    "Deferential and careful. He does not respond, knowing better than to talk for the sake of it (Book 9, Ch66 L41).")])
edit("07_Characters/Humphrey_Geller.md", [(
    "Precise, shy about romance, crisp when commanding. Cues: Book 1, Ch47 L88-89; Book 13, Ch958 L48.",
    "Precise, shy about romance, crisp when commanding. Cues: he turns white and shakes his head when Jason asks about Gabrielle (Book 1, Ch47 L88-89); in expedition leader mode he refers to his mother by name and issues her orders (Book 13, Ch958 L48).")])
edit("07_Characters/Knowledge.md", [(
    "the Church of Knowledge (funds the MRA, Book 12, Ch1 L58).",
    "the Church of Knowledge (one of the churches that contribute funding to the MRA, Book 12, Ch1 L58).")])
edit("07_Characters/Lorelei_Grantham.md", [(
    "- Book 3: introduces herself after the dome chamber events (Book 3, Ch69 L455).",
    "- Book 3: introduces herself as a researcher assigned to the Adventure Society's Continental Council (Book 3, Ch69 L455).")])
edit("07_Characters/Neil_Davone.md", [(
    "Tentative before committing. Cue: Book 2, Ch27 L46.",
    "Tentative before committing. Cue: Asano's visit left Neil uncertain, since the only real attraction to joining the team was Humphrey Geller (Book 2, Ch27 L46).")])
edit("07_Characters/Padma_Parsell.md", [(
    "Keen, grieving and quick to speak her mind (Book 2, Ch38 L35).",
    "Keen, grieving and quick to speak her mind. When Lance calls out under his breath, she ignores him (Book 2, Ch38 L35).")])
edit("07_Characters/Sigrid_Freyn.md", [(
    "Sensible and dry; she is the grown-up on a team of enthusiasts and defends her king's dignity (Book 12, Ch15 L10).",
    "Sensible and dry; she is the grown-up on a team of enthusiasts. She tells Valdis to be more respectful of his father and king (Book 12, Ch15 L10).")])
edit("07_Characters/Simon_McKean.md", [(
    "- Named again at the Ascension's Gate briefing (Book 13, Ch1002 L40).",
    "- Named again at the Ascension's Gate briefing, where Jason says going after him is their show (Book 13, Ch1002 L40 to L41).")])
edit("07_Characters/Sophie_Wexler.md", [(
    "Wary of kindness and silent about pain. Cues: Book 2, Ch1 L77-80; Book 2, Ch45 L69-72.",
    "Wary of kindness and silent about pain. Cues: she asks why Jason would do so much for them (Book 2, Ch1 L77-80); she grimaces silently through the pain of a broken arm (Book 2, Ch45 L69-72).")])
edit("07_Characters/Thadwick_Mercer.md", [(
    "- Appears again in Book 13 (Book 13, Ch1022 L35, L62).",
    "- Appears again in Book 13, talking about the object that resists dimensional storage and resting a hand on his spiked ruby-and-onyx blade (Book 13, Ch1022 L35, L62).")])
edit("07_Characters/Yumi_Asano.md", [(
    "- Present in Book 4 (Book 4, Ch74 L43).",
    "- Present in Book 4, raising her eyebrows at Jason (Book 4, Ch74 L43).")])
edit("07_Characters/Zara_Rimaros.md", [(
    "gold by Book 12 (Book 12, Ch12 L3);", "gold by Book 12: she stays in a suite fit for gold-rank adventurers (Book 12, Ch12 L3) and calls up a storm of gold-rank force (Book 13, Ch965 L86);")])
edit("07_Characters/Minor_Cast/Minor_Cast_Books_4-6.md", [(
    "He takes command on site as a government figure in Book 11 (Book 11, Ch68 L476) and needs publicity in Book 13 (Book 13, Ch950 L47).",
    "In Book 11 he snatches a phone and says he is onsite and taking command of operations (Book 11, Ch68 L476). In Book 13 he is said to need the publicity (Book 13, Ch950 L47).")])

edit("08_History_and_Timeline/Book_01_Timeline.md", [(
    "The text gives an explicit \"about two months\" at Ch62 L5, so the field assessment ends in late January 2018 by the calendar anchors.",
    "In his recording Jason says \"It's been about two months since I arrived here\" (Book 1, Ch62 L5). By the calendar anchors the field assessment therefore ends in late January 2018.")])
edit("08_History_and_Timeline/Book_04_Timeline.md", [(
    "from week 5 onward are counted from those anchors and from the \"last week\" remarks (Book 4, Ch50 L84; Book 4, Ch64 L82), not from stated dates.",
    "from week 5 onward are counted from those anchors and from the \"last week\" remarks, not from stated dates. Examples: \"last week, I got mildly kidnapped\" (Book 4, Ch50 L84); \"They started filming us last week\" (Book 4, Ch64 L82).")])
edit("08_History_and_Timeline/Book_08_Timeline.md", [
    ("- **Start**: the aftermath scenes of Book 7 are \"a month\" after the One Day War (Book 7, Ch66 L27); Book 8 starts in the same period, with Jason's team taking contracts again (Book 8, Ch1 L7).",
     "- **Start**: the aftermath scenes of Book 7 are a month after the One Day War (Book 7, Ch66 L27). Book 8 starts in the same period, with Jason on an expedition to the arid north coast (Book 8, Ch1 L7)."),
    ("- **End**: the book closes as the end of the monster surge approaches and Dawn leaves (Book 8, Ch68 L9).",
     "- **End**: the book closes as the end of the monster surge approaches. Dawn says she has lingered longer than she should and says goodbye at the gate (Book 8, Ch68 L9)."),
])
edit("08_History_and_Timeline/Book_09_Timeline.md", [(
    "anchored by the two-week schedules in Ch42, Ch43 and Ch49 (Book 9, Ch42 L31; Book 9, Ch43 L72; Book 9, Ch49 L80).",
    "anchored by the two-week schedules in Ch42, Ch43 and Ch49. Humphrey says Jason and Estella will remain in the city for two weeks (Book 9, Ch42 L31); Jason says \"See you in two weeks\" (Book 9, Ch43 L72); a speaker says he will not be available until the end of next week (Book 9, Ch49 L80).")])
edit("08_History_and_Timeline/Book_12_Timeline.md", [(
    "Ch61 closes with the visitors downstairs (Book 12, Ch61 L107), and Ch62 opens aboard the saucer before they arrive (Book 12, Ch62 L3).",
    "Ch61 closes with the assistant saying \"They're downstairs\" (Book 12, Ch61 L107), and Ch62 opens with Anna aboard the saucer, before the arrival (Book 12, Ch62 L3).")])
edit("08_History_and_Timeline/Book_13_Timeline.md", [
    ("the lines checked here (Ch995 L57, L76) do not show it, so it is not asserted.",
     "the lines checked here (the symposium exchange and the report of Bahrain's vanished government) do not show it, so it is not asserted."),
    ("- Book 13's present is 2038 (Book 13, Ch951 L50).",
     "- Book 13's present is 2038: a character asks how not knowing a kids' show in 2038 can be un-Australian (Book 13, Ch951 L50)."),
])
edit("08_History_and_Timeline/Master_Timeline.md", [(
    "| Book 12 \"now\" | \"M-count\" | Pallimustus tour late 2037 to early 2038; Earth arrival 2038 | Book 12, Ch21 L61; Book 12, Ch67 L65, L113 |",
    "| Book 12 \"now\" | \"M-count\" | Earth arrival 2038: \"seventeen years ago\" and \"forty-four years ago\" | Book 12, Ch67 L65, L113 |")])
edit("10_Roleplay_Support/Tone_and_Voice.md", [
    ("Nik's swearing is bleeped on the page (Book 11, Ch8 L102).",
     "Nik's swearing is bleeped on the page: \"[Bleep]ing rubes\" (Book 11, Ch8 L102)."),
    ("Jason jokes about kneeling to the Storm King and then answers a threat of execution flatly: \"Die on my feet\" (Book 7, Ch59 L81-83).",
     "Jason jokes about kneeling to the Storm King, and then answers a threat of execution flatly: \"Die on my feet. I've done it before\" (Book 7, Ch59 L81-83)."),
    ("sharp and political at thirteen (Book 5, Ch24 L3-5).",
     "sharp and political at thirteen, telling a reporter his story on mining deregulation was \"an exercise in buffoonery\" (Book 5, Ch24 L3-5)."),
    ("**Nik**: foul-mouthed, a rabbit in a top hat whose swearing is bleeped (Book 11, Ch8 L102-106; named Nik, Book 11, Ch23 L42). **Taika**: casual (\"bro\", Book 11, Ch68 L472).",
     "**Nik**: foul-mouthed, a four-foot rabbit in a top hat and tuxedo whose swearing is bleeped (Book 11, Ch8 L102-106). He says his name is \"NIK, no C\" (Book 11, Ch23 L42). **Taika**: casual, as in \"That legit sucked, bro\" (Book 11, Ch68 L472)."),
])
# the plan file is a working list, not a compendium document
p = os.path.join(B, "src", "tools", "build_register.py")
s = open(p, encoding="utf-8").read()
o = '"TODO_Verification.md", "00_Project_Structure.md"}'
assert o in s
open(p, "w", encoding="utf-8").write(s.replace(o, '"TODO_Verification.md", "TODO_Build_Plan.md", "00_Project_Structure.md"}', 1))
print("ok")

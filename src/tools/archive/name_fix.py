import re
p = r"C:\Users\Gabriel\Documents\World Stuff\HWFWM Compendium\Appendices\Name_Index.md"
s = open(p, encoding="utf-8").read()

new = {
 "Adam Cosgrove": "- **Adam Cosgrove** (B3 epilogue): Melbourne detective, thirty-one, who investigates the hole where Jason's apartment was and later warns Erika off investigating her brother (B4).",
 "Adrien Barbou": "- **Adrien Barbou** (B4): operations director of the Network's Lyon branch, who has Farrah held in a black site; later works with the EOA (the wiki calls him Mr East); Farrah says \"Barbou belongs to me\" (B6).",
 "Amos Pensinata": "- **Amos Pensinata** (B7): gold-rank adventurer with a soul-damaged, strong aura who teaches Jason aura skills; uncle of Orin.",
 "Argrave Mericulato": "- **Argrave Mericulato** (B7, named; B9): Adventure Society functionary in a Builder-cult role who triggers the naga egg.",
 "Autumn Leal": "- **Autumn Leal** (B7): adventurer Jason meets in Rimaros, with an exotic magical frog named Neil.",
 "Beth Cavendish": "- **Beth Cavendish** (B1): adventurer with her own team who knows Humphrey (B1); her team reaches bronze while Humphrey's is in the astral space (B3).",
 "Brian": "- **Brian** (B12): a priest of Dominion who greets Jason.",
 "Bussinger": "- **Bussinger** (B13): dark-haired Swiss Network gold-ranker in red and gold, with golden vambraces and gauntlets.",
 "Callum (Cal) Morse": "- **Callum (Cal) Morse** (B2): gold-rank stealth hunter and Emir's old teammate; reveals in B6 that he is part of the Cult of the Reaper.",
 "Carmen": "- **Carmen** (B6): avatar of doom of the Sundered Throne who \"just turns up\" to collect, taking Shako away on the Last Ferry (B6, B8).",
 "Cheryl Asano": "- **Cheryl Asano** (B1 mention; B4): Jason's mother.",
 "Colin": "- **Colin** (B1): Jason's apocalypse-leech swarm familiar.",
 "Dawn": "- **Dawn** (B3/4): First Servant of the World-Phoenix and its hierophant; also a painter of prophetic paintings (B4).",
 "Erika Asano": "- **Erika Asano** (B3 epilogue mention; B4): Jason's older sister, a television chef.",
 "Franklin": "- **Franklin** (B4): Cabal vampire.",
 "Gabriel Remore": "- **Gabriel Remore** (B1): Rufus's father, a fire swordsman.",
 "Garret Headingway": "- **Garret Headingway** (B12): upper-echelon member of House Headingway, one of Estercost's pre-eminent families.",
 "Gerling (Jack)": "- **Gerling (Jack)** (B5): US Network gold-ranker who kills Kaito, Asya and Greg (B5); later Elizabeth's blood slave (B12-13).",
 "Henrietta Geller": "- **Henrietta Geller** (B2): Humphrey's older sister, a summoner.",
 "Hester Maharala": "- **Hester Maharala** (B1 as Hester; B2 surname): Emir's portaler, from Jayapura on Pranay's northern coast.",
 "Ken Asano": "- **Ken Asano** (B1): Jason's father, a landscape architect.",
 "Kaito Asano": "- **Kaito Asano** (B2 mention; B4): Jason's brother, Amy's husband; killed in B5.",
 "Marcus Hargrave Xenoria": "- **Marcus Hargrave Xenoria** (B10): leonid adventurer deployed by the Adventure Society to Yaresh as the Continental Council's representative.",
 "Neil Davone": "- **Neil Davone** (B1): healer, Thadwick Mercer's former lackey, later Jason's healer.",
 "Orin Pensinata": "- **Orin Pensinata** (B7): silver-ranker; Amos's nephew.",
 "Padma Parsell": "- **Padma Parsell** (B2): Remore Academy cadet and graduate.",
 "Umber": "- **Umber** (B8 mention; B13): Shade's sibling or peer, who trapped him in an astral space for centuries (B8) and plots against Jason (B13).",
 "Valdis Volaire": "- **Valdis Volaire** (B2 mention; B3): prince of the Mirror Kingdom, a sword master, and the Mirror King's son.",
}

lines = s.split("\n")
done = set()
for i, l in enumerate(lines):
    for key, repl in new.items():
        if l.startswith("- **" + key + "**"):
            lines[i] = repl
            done.add(key)
missing = [k for k in new if k not in done]
print("missing:", missing)
s = "\n".join(lines)
s = s.replace("Status: Draft (first pass; roughly 250 names; to be expanded as character files are written)", "Status: Draft (audited against the book text, chapter notes and wiki; first appearances checked against the book text; descriptions retained only where the three tiers support them)")
s = s.replace("Sources: chapter notes, fan wiki", "Sources: book text (first appearances and descriptions), chapter notes, fan wiki")
open(p, "w", encoding="utf-8").write(s)

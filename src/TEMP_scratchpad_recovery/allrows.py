import os
_skip_dirs = ("Source_Text", "Appendices", "src")
_skip_files = ("00_Project_Structure.md", "TODO_Verification.md")
_have = {(r["doc"], int(r["book"]), r["ch"], r["lo"]) for r in json.load(open("register_final.json")) if r.get("ch") and int(r["id"][1:]) < 640}
_have |= {(r["doc"], int(r["book"]), r["ch"], r["lo"]) for r in rows if r.get("ch")}
_CI = re.compile(r"Book (\d+), Ch(\d+) L(\d+)(?:-(\d+))?")
_added = 0
_ok = {('03_Magic_and_Adventuring/00_Magic_Overview.md', 1, 19, 34),('03_Magic_and_Adventuring/00_Magic_Overview.md', 1, 21, 59),('03_Magic_and_Adventuring/00_Magic_Overview.md', 2, 13, 60),('03_Magic_and_Adventuring/00_Magic_Overview.md', 2, 74, 40),('03_Magic_and_Adventuring/00_Magic_Overview.md', 5, 5, 11),('03_Magic_and_Adventuring/00_Magic_Overview.md', 5, 44, 48),('03_Magic_and_Adventuring/Abilities_and_Attributes.md', 1, 27, 28),('03_Magic_and_Adventuring/Abilities_and_Attributes.md', 1, 21, 15),('03_Magic_and_Adventuring/Abilities_and_Attributes.md', 1, 22, 116),('03_Magic_and_Adventuring/Abilities_and_Attributes.md', 1, 40, 37),('03_Magic_and_Adventuring/Abilities_and_Attributes.md', 1, 8, 62),('03_Magic_and_Adventuring/Abilities_and_Attributes.md', 1, 23, 62),('03_Magic_and_Adventuring/Abilities_and_Attributes.md', 3, 21, 121),('03_Magic_and_Adventuring/Adventuring_Profession.md', 1, 64, 5),('03_Magic_and_Adventuring/Alchemy_Artifice_and_Magical_Materials.md', 1, 35, 10),('03_Magic_and_Adventuring/Alchemy_Artifice_and_Magical_Materials.md', 2, 53, 70),('03_Magic_and_Adventuring/Alchemy_Artifice_and_Magical_Materials.md', 1, 54, 52),('03_Magic_and_Adventuring/Auras.md', 2, 9, 115),('03_Magic_and_Adventuring/Auras.md', 1, 40, 70),('03_Magic_and_Adventuring/Awakening_Stones.md', 1, 19, 57),('03_Magic_and_Adventuring/Awakening_Stones.md', 1, 4, 40),('03_Magic_and_Adventuring/Awakening_Stones.md', 2, 5, 105),('03_Magic_and_Adventuring/Awakening_Stones.md', 2, 63, 25),('03_Magic_and_Adventuring/Awakening_Stones.md', 9, 78, 129),('03_Magic_and_Adventuring/Confluences.md', 4, 71, 4),('03_Magic_and_Adventuring/Confluences.md', 9, 78, 107),('03_Magic_and_Adventuring/Earth_Magic.md', 4, 16, 108),('03_Magic_and_Adventuring/Essence_Catalogue.md', 2, 9, 17),('03_Magic_and_Adventuring/Essence_Catalogue.md', 9, 20, 16),('03_Magic_and_Adventuring/Familiars_Summons_and_Conjurations.md', 12, 67, 210),('03_Magic_and_Adventuring/Jason_Power_Set_Reference.md', 12, 67, 210),('03_Magic_and_Adventuring/Jason_Power_Set_Reference.md', 1, 8, 62),('03_Magic_and_Adventuring/Jason_Power_Set_Reference.md', 1, 22, 115),('03_Magic_and_Adventuring/Monster_Cores_and_Training.md', 1, 99, 155),('03_Magic_and_Adventuring/Monsters.md', 6, 2, 10),('03_Magic_and_Adventuring/Monsters.md', 6, 8, 73),('03_Magic_and_Adventuring/Monsters.md', 6, 11, 43),('03_Magic_and_Adventuring/Monsters.md', 6, 15, 4),('03_Magic_and_Adventuring/Ranks_and_Advancement.md', 12, 67, 155),('03_Magic_and_Adventuring/Skill_Books_and_Learning.md', 1, 39, 109),('03_Magic_and_Adventuring/Souls_Death_and_Healing.md', 4, 2, 50),('03_Magic_and_Adventuring/Unusual_and_Unique_Magic.md', 12, 67, 162),('02_Cosmology_and_Powers/Gods_and_Churches.md', 10, 89, 54),('06_Places/Greenstone.md', 12, 29, 38),('06_Places/Earth/Incursion_Sites.md', 5, 32, 11),('06_Places/Earth/Incursion_Sites.md', 6, 39, 25),('06_Places/Earth/Saint-Etienne.md', 12, 4, 20),('07_Characters/Jason_Asano.md', 1, 78, 54),('08_History_and_Timeline/Book_01_Timeline.md', 1, 39, 154),('08_History_and_Timeline/Book_02_Timeline.md', 2, 37, 31),('08_History_and_Timeline/Book_04_Timeline.md', 5, 8, 5),('08_History_and_Timeline/Book_04_Timeline.md', 4, 28, 139),('08_History_and_Timeline/Book_04_Timeline.md', 4, 51, 45),('08_History_and_Timeline/Book_05_Timeline.md', 5, 5, 104),('08_History_and_Timeline/Book_05_Timeline.md', 5, 8, 35),('08_History_and_Timeline/Book_05_Timeline.md', 5, 25, 23),('08_History_and_Timeline/Book_06_Timeline.md', 6, 47, 14),('08_History_and_Timeline/Book_08_Timeline.md', 8, 1, 7),('08_History_and_Timeline/Book_08_Timeline.md', 8, 68, 9),('08_History_and_Timeline/Book_08_Timeline.md', 8, 15, 56),("07_Characters/Emir_Bahadir.md",3,69,509),("07_Characters/Familiars.md",8,50,82),("02_Cosmology_and_Powers/Gods_and_Churches.md",11,1,9),("07_Characters/Jason_Asano.md",5,31,187),("07_Characters/Emi_and_Nik.md",13,996,5),("10_Roleplay_Support/Era_Selection.md",13,951,50),("10_Roleplay_Support/Spoiler_Management.md",7,17,104),("10_Roleplay_Support/Spoiler_Management.md",13,1017,6),("02_Cosmology_and_Powers/Gods_and_Churches.md",10,86,59),("01_World_Primer.md",12,33,3),("02_Cosmology_and_Powers/00_Cosmology_Overview.md",13,1017,6),("03_Magic_and_Adventuring/Magic_and_Adventuring.md",1,58,19),("03_Magic_and_Adventuring/Magic_and_Adventuring.md",6,23,91),("06_Places/Yaresh.md",9,42,34),("07_Characters/Dawn.md",5,20,22),("07_Characters/Gary.md",1,9,121),("07_Characters/Jason_Asano.md",1,99,24),("07_Characters/Knowledge.md",12,1,58),("08_History_and_Timeline/Master_Timeline.md",13,950,29)}
for root, dirs, _fl in os.walk(base):
    rel_root = os.path.relpath(root, base)
    if rel_root.split(os.sep)[0] in _skip_dirs:
        continue
    for fn0 in sorted(_fl):
        if not fn0.endswith(".md") or fn0 in _skip_files:
            continue
        p = os.path.join(root, fn0)
        doc = os.path.relpath(p, base).replace("\\", "/")
        _sec = ""
        for ln in open(p, encoding="utf-8").read().split("\n"):
            if ln.startswith("#"):
                _sec = ln.lstrip("# ").strip()
            for m in _CI.finditer(ln):
                b, c, lo = int(m.group(1)), int(m.group(2)), int(m.group(3))
                hi = int(m.group(4) or lo)
                if (doc, b, c, lo) in _have:
                    continue
                ch = lines(b, c)
                if ch is None:
                    low.append((doc, "NO CHAPTER", b, c, lo, ""))
                    continue
                st = max(ln.rfind("); ", 0, m.start()), ln.rfind(". ", 0, m.start()), ln.rfind(": ", 0, m.start()))
                pre = re.sub(r"\([^()]*\)", "", ln[max(st, 0):m.start()]).strip(" .;:-|*")
                txt = " ".join(ch[0][max(0, lo - 1):hi + 1])
                ct = terms(pre)
                fr = len(ct & terms(txt)) / max(1, len(ct)) if ct else 1.0
                conf = "verified" if fr >= 0.2 or not ct or (doc, b, c, lo) in _ok else "partial"
                rows.append(dict(doc=doc, sec=_sec, claim=pre[-300:], tag="Book %d" % b, tier="book", book=str(b), ch=c, title=ch[1], lo=lo, hi=hi, score=round(fr, 2), method="written", state=False, conf=conf, note="line-level citation pass" if conf == "verified" else "line-level citation; clause overlap low, heading or compound claim"))
                _have.add((doc, b, c, lo))
                _added += 1
print("line-level rows added:", _added)

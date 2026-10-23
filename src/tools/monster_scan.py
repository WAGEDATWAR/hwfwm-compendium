"""List monster names the chapter files give a rank for (build plan item 2C.2).
Finds '<rank>-rank <name>' phrases and '<name>, a <rank>-rank monster/beast/creature' and 'the <name>s were <rank>-rank'.
Writes monster_scan_report.md: name | rank(s) | count | first cite | context. Review each row; the scan is noisy."""
import re, os, io, sys, collections

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
HERE = os.path.dirname(os.path.abspath(__file__))
ST = os.path.abspath(os.path.join(HERE, "..", "Source_Text"))
RANKS = "iron|bronze|silver|gold|diamond|transcendent|normal"
A = re.compile(r"\b(%s)[- ]rank(?:ed)? ((?:[a-z-]+ ){0,2}[a-z-]+)" % RANKS, re.I)
B = re.compile(r"\b([A-Za-z-]+(?: [A-Za-z-]+)?),? (?:a|an) (%s)[- ]rank(?:ed)? (?:monster|beast|creature|predator|construct|entity)" % RANKS, re.I)
STOP = set("adventurer adventurers essence user users ranker rankers core cores monster monsters spirit coin coins mage priest team teams elf human celestine leonid creature creatures beast beasts abilities ability aura auras power powers magic stone stones guard guards fighter fighters healer healers attack attacks version versions one ones level levels threshold threat threats warrior warriors soldier soldiers cultist cultists vampire vampires messenger messengers member members opponent opponents enemy enemies adventuring ritual rituals animal animals pack hunter hunters scout scouts mercenaries mercenary assassin assassins thief thieves leader leaders boss bosses master masters spell spells weapon weapons armour item items summon summons familiar familiars specialist specialists expert experts citizen citizens servant servants noble nobles".split())
rows = {}
for b in range(1, 14):
    d = os.path.join(ST, "Book_%02d" % b)
    for fn in sorted(os.listdir(d)):
        ch = int(re.match(r"Ch_(\d+)_", fn).group(1))
        for i, l in enumerate(open(os.path.join(d, fn), encoding="utf-8").read().split("\n"), 1):
            cands = []
            for m in A.finditer(l):
                words = m.group(2).lower().split()
                # take up to the first word that is a stopword, joined
                name = []
                for w in words:
                    if w in STOP or w in ("and", "or", "of", "to", "in", "with", "that", "who", "which", "was", "were", "is", "are", "had", "has", "from", "for", "on", "at", "by"):
                        break
                    name.append(w)
                if name:
                    cands.append((" ".join(name), m.group(1).lower()))
            for m in B.finditer(l):
                cands.append((m.group(1).lower(), m.group(2).lower()))
            for name, rank in cands:
                if len(name) < 3:
                    continue
                r = rows.setdefault(name, {"ranks": set(), "n": 0, "first": (b, ch, i), "ctx": l.strip()[:150]})
                r["ranks"].add(rank)
                r["n"] += 1
out = ["# Monster rank scan (working list; noisy)\n", "| name | rank(s) | count | first cite | context |", "|---|---|---|---|---|"]
for name, r in sorted(rows.items(), key=lambda kv: kv[1]["first"]):
    b, ch, i = r["first"]
    out.append("| %s | %s | %d | Book %d, Ch%d L%d | %s |" % (name, "/".join(sorted(r["ranks"])), r["n"], b, ch, i, r["ctx"].replace("|", "/")))
open(os.path.join(HERE, "monster_scan_report.md"), "w", encoding="utf-8").write("\n".join(out))
print(len(rows), "names")

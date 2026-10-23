"""List every essence name the chapter files attest, with first cite and who holds it.
Sources: (1) 'A, B, C and D essences' list sentences; (2) 'the X essence' / 'X essence' for names in the wiki table.
Writes ess_lists_report.md next to this script. Usage: python3 ess_lists.py"""
import re, os, io, sys, collections

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
HERE = os.path.dirname(os.path.abspath(__file__))
ST = os.path.abspath(os.path.join(HERE, "..", "Source_Text"))
STOP = set("the a an and or his her their its my your our this that these those with of for to from any every other some many most all only which what new first second third last two three four one single more less same each both own different certain several three normal regular ordinary basic common rare uncommon epic legendary unawakened awakened active passive their ten unique available free each".split())
LIST_RX = re.compile(r"((?:[A-Za-z'-]+(?:, | and |, and | or ))+[A-Za-z'-]+) essences?", re.I)
ONE_RX = re.compile(r"\b(?:the |a |an )?([A-Z][a-z]+|[a-z]+) essence\b")

wiki = set()
tbl = os.path.join(HERE, "wiki_essence_table.md")
if os.path.exists(tbl):
    for ln in open(tbl, encoding="utf-8"):
        c = [x.strip() for x in ln.split("|")]
        if len(c) > 2 and c[1] and c[1] not in ("Essence", "---"):
            wiki.add(c[1].lower())

first = {}
count = collections.Counter()
ctx = {}
for b in range(1, 14):
    d = os.path.join(ST, "Book_%02d" % b)
    for fn in sorted(os.listdir(d)):
        ch = int(re.match(r"Ch_(\d+)_", fn).group(1))
        for i, l in enumerate(open(os.path.join(d, fn), encoding="utf-8").read().split("\n"), 1):
            for m in LIST_RX.finditer(l):
                words = re.split(r", and |, | and | or ", m.group(1))
                words = [w.strip().lower() for w in words]
                # drop leading determiners in the first item
                words[0] = re.sub(r"^(?:the|his|her|their|my|your|our|with|of|its|a|an)\s+", "", words[0])
                words[0] = words[0].split(" ")[-1]
                for w in words:
                    if not w or w in STOP or " " in w:
                        continue
                    count[w] += 1
                    first.setdefault(w, (b, ch, i))
                    ctx.setdefault(w, l.strip()[:160])
            for m in ONE_RX.finditer(l):
                w = m.group(1).lower()
                if w in wiki and w not in STOP:
                    count[w] += 1
                    first.setdefault(w, (b, ch, i))
                    ctx.setdefault(w, l.strip()[:160])

out = ["# Essence names attested in the chapter files\n"]
for w in sorted(first, key=lambda x: first[x]):
    b, ch, i = first[w]
    out.append("| %s | Book %d, Ch%d L%d | %d | %s |" % (w, b, ch, i, count[w], ctx[w].replace("|", "/")))
open(os.path.join(HERE, "ess_lists_report.md"), "w", encoding="utf-8").write("\n".join(out))
print(len(first), "names; report written")

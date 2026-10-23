import re,sys,io,collections
sys.argv=[sys.argv[0]]
import audit
from audit import wins,inv,WORD,STOP,norm
txt=open(r"C:\Users\Gabriel\Documents\World Stuff\HWFWM Compendium\Appendices\Name_Index.md",encoding="utf-8").read()
def stem(t): return t[:-1] if t.endswith("s") and len(t)>4 else t
for l in txt.split("\n"):
    m=re.match(r"- \*\*(.+?)\*\* \((.+?)\):\s*(.*)",l)
    if not m: continue
    nm,tag,desc=m.groups()
    base=re.sub(r"\s*\([^)]*\)","",nm).replace('"The Necromancer" ',"").strip()
    ntoks=[t for t in WORD.findall(norm(base)) if t not in ("mr","mrs")]
    dtoks=[stem(t) for t in WORD.findall(norm(desc)) if len(t)>3 and t not in STOP]
    dtoks=[t for t in set(dtoks)]
    if not ntoks or not dtoks: continue
    # candidate windows: contain last name token (or full if single)
    key=ntoks[-1] if len(ntoks)>1 else ntoks[0]
    cand=set(inv.get(key,()))
    if len(ntoks)>1 and ntoks[0] in inv: cand&=inv[ntoks[0]] if (cand&inv[ntoks[0]]) else cand
    best=collections.defaultdict(int)
    for i in cand:
        tier,lab,tx=wins[i]
        toks=set(stem(x) for x in WORD.findall(tx))
        sc=sum(1 for d in dtoks if d in toks)
        if sc>best[tier]: best[tier]=sc
    tot=len(dtoks)
    bb=best.get("B",0);bn=best.get("N",0);bw=best.get("W",0)
    frac=max(bb,bn,bw)/tot
    if frac<0.5 or (bb/tot<0.3 and max(bn,bw)/tot<0.5):
        print("%-30s tot=%d B=%d N=%d W=%d | %s"%(nm[:30],tot,bb,bn,bw,desc[:130]))

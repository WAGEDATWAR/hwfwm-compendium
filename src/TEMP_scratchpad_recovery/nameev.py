import re,sys,io,collections
sys.argv=[sys.argv[0]]
import audit
from audit import wins,inv,WORD,STOP,norm
txt=open(r"C:\Users\Gabriel\Documents\World Stuff\HWFWM Compendium\Appendices\Name_Index.md",encoding="utf-8").read()
def stem(t): return t[:-1] if t.endswith("s") and len(t)>4 else t
start=int(__import__("os").environ.get("S","0")); end=int(__import__("os").environ.get("E","999"))
k=0
for l in txt.split("\n"):
    m=re.match(r"- \*\*(.+?)\*\* \((.+?)\):\s*(.*)",l)
    if not m: continue
    k+=1
    if k<start or k>end: continue
    nm,tag,desc=m.groups()
    base=re.sub(r"\s*\([^)]*\)","",nm).replace('"The Necromancer" ',"").strip()
    ntoks=[t for t in WORD.findall(norm(base)) if t not in ("mr","mrs")]
    dtoks=set(stem(t) for t in WORD.findall(norm(desc)) if len(t)>3 and t not in STOP)
    if not ntoks: continue
    key=ntoks[-1]
    cand=set(inv.get(key,()))
    if len(ntoks)>1 and ntoks[0] in inv and (cand&inv[ntoks[0]]): cand&=inv[ntoks[0]]
    best={}
    for i in cand:
        tier,lab,tx=wins[i]
        toks=set(stem(x) for x in WORD.findall(tx))
        sc=sum(1 for d in dtoks if d in toks)
        if tier not in best or sc>best[tier][0]: best[tier]=(sc,lab,tx,i)
    out="%d %s (%s): %s"%(k,nm,tag,desc[:110])
    print(out)
    for tier in ("B","N"):
        if tier in best:
            sc,lab,tx,i=best[tier]
            p=tx.find(key)
            print("    %s%d/%d %s: %s"%(tier,sc,len(dtoks),lab,tx[max(0,p-90):p+150].replace("\n"," ")))
            break

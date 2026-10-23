import json,re,os
os.environ["FR"]="0.7"
import audit
rows=json.load(open("register_final.json"))
sel=[r for r in rows if r["conf"]=="unlocated"]
seen=set()
for r in sel:
    claim=re.sub(r"\s+"," ",r["claim"])
    parts=[p.strip(" ,.:") for p in re.split(r";| : |, and |, while ",claim) if len(p.strip())>25]
    bad=[]
    for p in parts:
        t,c,k,u=audit.check(p,k=5)
        if t not in ("B","N","W"): bad.append(p)
    key=(r["doc"],claim[:60])
    if key in seen: continue
    seen.add(key)
    if bad: print("%s [%s] B%s\n   UNSUPPORTED CLAUSES: %s"%(r["id"],r["doc"].split("/")[-1][:22],r["book"]," || ".join(b[:110] for b in bad)))

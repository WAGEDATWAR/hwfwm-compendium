import json,re,sys
import audit
rows=json.load(open("register_final.json"))
sel=[r for r in rows if r["conf"]=="unlocated"]
import os
os.environ["FR"]="0.7"
out=[]
for r in sel:
    claim=r["claim"]
    # restrict to notes of that book + wiki: custom scoring
    tier,c,k,unseen=audit.check(claim,k=6)
    out.append((r["id"],tier,c,k,claim[:130].replace("\n"," "),r["doc"].split("/")[-1][:20]))
import collections
print(collections.Counter(o[1] for o in out))
for o in out:
    if o[1] not in ("B","N","W"): print(o)

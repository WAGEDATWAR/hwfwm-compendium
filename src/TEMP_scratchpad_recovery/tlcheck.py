import re,json,os,sys
exec(open("newrows.py",encoding="utf-8").read().split("skipdocs")[0])
t=open(base+r"\08_History_and_Timeline\Master_Timeline.md",encoding="utf-8").read()
seen=set()
for b,c,lo,hi in CIT.findall(t):
    k=(int(b),int(c),int(lo),int(hi or lo))
    if k in seen: continue
    seen.add(k)
    ch=lines(k[0],k[1])
    if ch is None: print("NO CH",k);continue
    txt=" | ".join(x[:170] for x in ch[0][k[2]-1:k[3]][:3])
    print("B%d Ch%d L%d-%d: %s"%(k[0],k[1],k[2],k[3],txt))

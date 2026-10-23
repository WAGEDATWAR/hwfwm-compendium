import sys,json,math,re,collections
from review import ch,df,inv,norm,WORD,STOP,rows
dec={}
for l in open("decisions.tsv",encoding="utf-8"):
    p=l.rstrip("\n").split("\t")
    if len(p)>=6: dec[p[0]]=p
# unresolved list: rows whose final conf is unlocated (decision unlocated) with numeric book
done_good={k for k,p in dec.items() if p[5]!="unlocated"}
ids=[]
for r in rows:
    p=dec.get(r["id"])
    if p and p[5]=="unlocated" and r["id"] not in done_good: ids.append(r["id"])
byid={r["id"]:r for r in rows}
skip_file="third_done.txt"
try: seen=set(open(skip_file).read().split())
except: seen=set()
def best(claim,n):
    d,tot=df[n];iv=inv[n]
    ts=[t.strip("-'") for t in WORD.findall(norm(claim))]
    ts=[t for t in dict.fromkeys(ts) if len(t)>2 and t not in STOP and t in d]
    w={t:math.log((tot+1)/(d[t]+1)) for t in ts}
    ts=sorted(ts,key=lambda t:-w[t])[:8]
    den=sum(w[t] for t in ts) or 1
    cand=collections.defaultdict(set)
    for t in ts:
        if d[t]>300: continue
        for ci,li in iv[t]:
            for b in (li//6,): cand[(ci,b)].add((t,li))
    out=[]
    for (ci,b),s in cand.items():
        terms={t for t,_ in s}
        sc=sum(w[t] for t in terms)/den
        out.append((sc,ci,sorted(li for _,li in s)))
    out.sort(reverse=True)
    res=[]
    for sc,ci,lis in out[:3]:
        num,title,lines=ch[n][ci]
        li=lis[0]
        res.append((round(sc,2),num,li+1,lines[li][:150]))
    return res
a=int(sys.argv[1]);b=int(sys.argv[2])
sel=[i for i in ids if i not in seen and byid[i]["book"].isdigit()][a:b]
print(len(ids),len([i for i in ids if i not in seen]))
for i in sel:
    r=byid[i]
    print("\n%s [%s] B%s: %s"%(i,r["doc"].split("/")[-1][:-3],r["book"],r["claim"][:160]))
    for x in best(r["claim"],int(r["book"])): print("   %.2f Ch%d L%d | %s"%x)

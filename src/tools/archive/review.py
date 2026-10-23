import re,os,json,math,collections,sys
base=r"C:\Users\Gabriel\Documents\World Stuff\HWFWM Compendium"
st=base+r"\src\Source_Text"
idx=json.load(open("chapter_index.json"))
rows=json.load(open("register_final.json"))
def norm(t): return re.sub(r"[\u2018\u2019\u201c\u201d\ufffd`]","'",t.lower())
WORD=re.compile(r"[a-z0-9][a-z0-9'\-]*")
STOP=set("the a an and or of to in on at for with by from as is are was were be been it its this that these those his her their they he she we you not but if then than so such into about over under up down out also may can could would should will has have had do does did one two three four five first second third other more most some any all each every many much very just only often usually later still both between during after before until while who which what when where there here book books notes note wiki confirmed chapter ch".split())
ch={}
for n in range(1,14):
    ch[n]=[(num,title,open(os.path.join(st,"Book_%02d"%n,fn),encoding="utf-8").read().split("\n")) for (num,title,fn,nl,m) in idx[str(n)]]
df={};inv={}
for n,l in ch.items():
    d=collections.Counter();iv=collections.defaultdict(list);tot=0
    for ci,(num,t,lines) in enumerate(l):
        for li,ln in enumerate(lines):
            if len(ln)<15: continue
            tot+=1
            for w in set(WORD.findall(norm(ln))): d[w]+=1; iv[w].append((ci,li))
    df[n]=(d,tot);inv[n]=iv
def top(claim,n,k=3):
    d,tot=df[n];iv=inv[n]
    ts=[w.strip("-'") for w in WORD.findall(norm(claim))]
    ts=[t for t in dict.fromkeys(ts) if len(t)>2 and t not in STOP and t in d]
    w={t:math.log((tot+1)/(d[t]+1)) for t in ts}
    ts=sorted(ts,key=lambda t:-w[t])[:10]
    den=sum(w.values()) and sum(w[t] for t in ts)
    cand=collections.defaultdict(set)
    for t in ts:
        if d[t]>400: continue
        for ci,li in iv[t]:
            for b in (li//3,li//3-1): cand[(ci,b)].add(t)
    sc=sorted(((sum(w[t] for t in s)/den,key) for key,s in cand.items()),reverse=True)[:k]
    out=[]
    for s,(ci,b) in sc:
        num,title,lines=ch[n][ci]
        lo=max(0,b*3)
        hit=[li for li in range(lo,min(len(lines),lo+6)) if any(t in norm(lines[li]) for t in ts)]
        li=hit[0] if hit else lo
        out.append((round(s,2),num,title[:30],li+1,(hit[-1]+1 if hit else li+1),lines[li][:170]))
    return out
if __name__=="__main__":
    a,b=int(sys.argv[1]),int(sys.argv[2])
    sel=[r for r in rows if r["state"] and r["ch"] is not None and r["book"].isdigit() and r["doc"][:3] in ("07_","08_","05_","06_","02_")]
    for r in sel[a:b]:
        print("\n%s [%s] B%s: %s"%(r["id"],r["doc"].split("/")[-1][:-3],r["book"],r["claim"][:170]))
        for t in top(r["claim"],int(r["book"])): print("   %.2f Ch%d %s L%d-%d | %s"%t)

import json,os,re
exec(open("newrows.py",encoding="utf-8").read().split("skipdocs")[0])
plan=json.load(open("conv_plan.json"))
done=0; low=[]
byf={}
for doc,ln_no,tag,(b,c,lo,hi) in plan: byf.setdefault(doc,[]).append((ln_no,tag,int(b),int(c),int(lo),int(hi)))
for doc,items in byf.items():
    p=os.path.join(base,doc.replace("/","\\"))
    L=open(p,encoding="utf-8").read().split("\n")
    for ln_no,tag,b,c,lo,hi in items:
        new="(Book %d, Ch%d L%d%s)"%(b,c,lo,"" if hi==lo else "-%d"%hi)
        assert L[ln_no-1].count(tag)==1,(doc,ln_no,tag)
        ch=lines(b,c)
        txt=" ".join(ch[0][max(0,lo-1):hi+1])
        claim=re.sub(r"\([^()]*\)","",L[ln_no-1])
        fr=len(terms(claim)&terms(txt))/max(1,len(terms(claim)))
        if fr<0.25: low.append((doc,ln_no,round(fr,2),new,claim[:110])); continue
        L[ln_no-1]=L[ln_no-1].replace(tag,new); done+=1
    open(p,"w",encoding="utf-8").write("\n".join(L))
print("converted",done,"skipped low",len(low))
for x in low: print(x)

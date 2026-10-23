import re,os
exec(open("newrows.py",encoding="utf-8").read().split("skipdocs")[0])
import glob
n=0
for p in glob.glob(base+"\**\*.md",recursive=True):
    if "Source_Text" in p or "Appendices" in p or "04_Peoples" in p: continue
    for i,ln in enumerate(open(p,encoding="utf-8").read().split("\n"),1):
        cits=CIT.findall(ln)
        if len(cits)!=1: continue
        b,c,lo,hi=cits[0]; b,c,lo=int(b),int(c),int(lo); hi=int(hi) if hi else lo
        ch=lines(b,c)
        if not ch: continue
        txt=" ".join(ch[0][max(0,lo-1):hi+1])
        cl=re.sub(r"\([^()]*\)","",ln); fr=len(terms(cl)&terms(txt))/max(1,len(terms(cl)))
        if 0.25<=fr<0.4:
            n+=1; print(os.path.relpath(p,base),i,round(fr,2)); print("  DOC:",cl[:200]); print("  SRC:",txt[:260])
print(n)

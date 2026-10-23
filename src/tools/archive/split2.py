import re,os,json
from split import parse
out=r"C:\Users\Gabriel\Documents\World Stuff\HWFWM Compendium\Source_Text"
os.makedirs(out,exist_ok=True)
def slug(s): return re.sub(r"[^A-Za-z0-9]+","_",s).strip("_")[:50]
index={}
for n in range(1,14):
    t=open(f"books/b{n}.txt",encoding="utf-8",errors="replace").read()
    chs=[]  # (num,title,start,bodystart)
    if n==13:
        for m in re.finditer(r"(?m)^Chapter (\d+): (.+)$",t):
            chs.append((int(m.group(1)),m.group(2).strip(),m.start(),m.end()+1))
    else:
        t,lines,toc,start=parse(n)
        pos=sum(len(l)+1 for l in lines[:start])
        # skip past end of toc: first body chapter 1 begins after last toc line
        last=toc[-1]
        ends=re.compile(r"(?m)^\s*%d\.\s+%s\s*$"%(last[0],re.escape(last[1]))).search(t)
        bodyst=ends.end() if ends else pos
        cur=bodyst
        for num,title in toc:
            tt=title.replace("’","'")
            pat=re.compile(r"(?<![\w])"+str(num)+r"\s+"+re.escape(tt).replace("'","['’�]").replace(r"\ ",r"\s+"),re.I)
            m=pat.search(t,cur)
            if m and (num==1 or True):
                chs.append((num,title,m.start(),m.end())); cur=m.end()
            else:
                chs.append((num,title,None,None))
        # chapter 1: starts at bodyst if missing
        fixed=[]
        for i,(num,title,s,b) in enumerate(chs):
            if s is None:
                if i==0: s=bodyst;b=bodyst
                else:
                    # place at previous start+0 -> merge: mark
                    s=None
            fixed.append([num,title,s,b])
        chs=fixed
    # resolve None by merging with previous chapter
    clean=[]
    for c in chs:
        if c[2] is None:
            clean.append((c[0],c[1],None,None))
        else: clean.append(tuple(c))
    d=os.path.join(out,"Book_%02d"%n); os.makedirs(d,exist_ok=True)
    starts=[(i,c) for i,c in enumerate(clean) if c[2] is not None]
    index[n]=[]
    for k,(i,c) in enumerate(starts):
        end=starts[k+1][1][2] if k+1<len(starts) else len(t)
        body=t[c[3]:end].strip("\n ")
        fn="Ch_%03d_%s.txt"%(c[0],slug(c[1]))
        merged=[x[0] for x in clean[i+1:] if x[2] is None and (k+1>=len(starts) or x[0]<starts[k+1][1][0])] if True else []
        head="BOOK %d | Chapter %d | %s\n"%(n,c[0],c[1])
        if merged: head+="(text also contains missing-heading chapters %s)\n"%merged
        open(os.path.join(d,fn),"w",encoding="utf-8").write(head+"\n"+body+"\n")
        index[n].append((c[0],c[1],fn,len(body.split("\n")),merged))
    print(n,len(starts),"files of",len(clean), "unsplit:",[c[0] for c in clean if c[2] is None])
json.dump(index,open("chapter_index.json","w"))

import re,sys,os
base=os.getcwd()
def parse(n):
    t=open(f"books/b{n}.txt",encoding="utf-8",errors="replace").read()
    lines=t.split("\n")
    # contents: lines "N. Title" at the start
    toc=[];i=0
    for i,l in enumerate(lines[:1500]):
        m=re.match(r"^\s*(\d{1,3})\.\s+(.+?)\s*$",l)
        if m: toc.append((int(m.group(1)),m.group(2)))
        elif toc and l.strip() and not re.match(r"^\s*\d",l): 
            if len(toc)>5: break
    start=i
    return t,lines,toc,start
if __name__=="__main__":
    for n in range(1,14):
        t,lines,toc,start=parse(n)
        # find positions sequentially
        pos=0;found=[];off=sum(len(l)+1 for l in lines[:start])
        pos=off
        for num,title in toc:
            pat=re.compile(r"(?<![\w])"+str(num)+r"\s+"+re.escape(title.replace("’","'")).replace("'","['’]").replace(r"\ ",r"\s+"),re.I)
            m=pat.search(t,pos)
            if m: found.append((num,title,m.start())); pos=m.end()
            else: found.append((num,title,None))
        miss=[f[:2] for f in found if f[2] is None]
        print(n,len(toc),"toc; missing",len(miss),miss[:4],"lines",len(lines))

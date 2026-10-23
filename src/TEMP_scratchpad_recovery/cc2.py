import re,sys,io,os
sys.stdout=io.TextIOWrapper(sys.stdout.buffer,encoding="utf-8",errors="replace")
exec(open("newrows.py",encoding="utf-8").read().split("skipdocs")[0])
CI=re.compile(r"Book (\d+), Ch(\d+) L(\d+)(?:-(\d+))?")
thr=float(os.environ.get("THR","0.2"))
for doc in sys.argv[1:]:
    p=os.path.join(base,doc.replace("/","\\"))
    for i,ln in enumerate(open(p,encoding="utf-8").read().split("\n"),1):
        for m in CI.finditer(ln):
            b,c,lo,hi=int(m.group(1)),int(m.group(2)),int(m.group(3)),int(m.group(4) or m.group(3))
            st=max(ln.rfind("); ",0,m.start()),ln.rfind(". ",0,m.start()),ln.rfind(": ",0,m.start()))
            pre=ln[max(st,0):m.start()]
            pre=re.sub(r"\([^()]*\)","",pre)
            ch=lines(b,c)
            if not ch: print("NOCH",doc,i,m.group(0)); continue
            txt=" ".join(ch[0][max(0,lo-1):hi+1])
            ct=terms(pre); fr=len(ct&terms(txt))/max(1,len(ct))
            if fr<thr: print("%s:%d %s fr=%.2f\n   CL:%s\n   SRC:%s"%(os.path.basename(doc),i,m.group(0),fr,pre[-150:],txt[:200]))

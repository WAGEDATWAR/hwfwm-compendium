import re,glob,os,io,sys
sys.stdout=io.TextIOWrapper(sys.stdout.buffer,encoding="utf-8",errors="replace")
base=r"C:\Users\Gabriel\AppData\Local\Temp\claude\C--Users-Gabriel-Documents-Gmod-Projects-Gmod-Decompilation\08b70dbf-6f0b-4b6b-a18f-242cc3f1fe96\scratchpad"
books={}
for f in glob.glob(base+r"\books\b*.txt"):
    books[int(re.sub(r"\D","",os.path.basename(f)))]=open(f,encoding="utf-8",errors="replace").read().lower().replace("’","'")
def first(name):
    n=name.lower().replace("’","'")
    for b in sorted(books):
        if n in books[b]: return b
    return None
txt=open(r"C:\Users\Gabriel\Documents\World Stuff\HWFWM Compendium\Appendices\Name_Index.md",encoding="utf-8").read()
for l in txt.split("\n"):
    m=re.match(r"- \*\*(.+?)\*\* \((.+?)\):",l)
    if not m: continue
    nm,tag=m.group(1),m.group(2)
    claimed=[int(x) for x in re.findall(r"B(\d+)",tag)]
    variants=[nm]
    paren=re.findall(r"\(([^)]+)\)",nm)
    base_nm=re.sub(r"\s*\([^)]*\)","",nm).strip()
    variants=[base_nm]
    parts=base_nm.split()
    if len(parts)>=2: variants.append(parts[-1]); 
    for p in paren: variants.append(p)
    res={}
    for v in variants:
        res[v]=first(v)
    fb=first(base_nm)
    if fb is None:
        lastname=first(parts[-1]) if len(parts)>1 else None
        firstname=first(parts[0])
        status="NOFULL last=%s first=%s"%(lastname,firstname)
    else:
        status="full=B%d"%fb
    if claimed and (fb is None or fb!=min(claimed)):
        print("MISMATCH",nm,"| claimed",tag,"|",status)

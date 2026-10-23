import re,os,sys,glob
ST=os.path.join(os.path.dirname(os.path.abspath(__file__)),"..","Source_Text")
def lines(b,c):
    d=os.path.join(ST,"Book_%02d"%b)
    for fn in os.listdir(d):
        if re.match(r"Ch_0*%d_"%c,fn): return open(os.path.join(d,fn),encoding="utf-8").read().split("\n")
    return []
items=[l.split("|") for l in open(sys.argv[1],encoding="utf-8").read().strip().split("\n")]
for name,b,c,lo in items:
    L=lines(int(b),int(c)); lo=int(lo)
    seg=" ".join(L[max(0,lo-3):lo+2])
    ok=all(re.search(w,seg,re.I) for w in name.split("&"))
    print("OK " if ok else "?? ",name,b,c,lo, "" if ok else "| "+L[lo-1][:150])

import sys,subprocess,io
sys.stdout=io.TextIOWrapper(sys.stdout.buffer,encoding="utf-8",errors="replace")
name=sys.argv[1]; n=int(sys.argv[2]) if len(sys.argv)>2 else 28
out=subprocess.run([sys.executable,"rd.py","g",name,"1","13","230","600"],capture_output=True,encoding="utf-8").stdout.strip().split("\n")
out=[l for l in out if l.strip()]
import re,collections
cnt=collections.Counter(re.match(r"B(\d+)",l).group(1) for l in out if re.match(r"B(\d+)",l))
print("TOTAL",len(out),"by book",dict(sorted(cnt.items(),key=lambda x:int(x[0]))))
if len(out)<=n: sel=out
else:
    step=len(out)/n; sel=[out[int(i*step)] for i in range(n)]
for l in sel: print(l[:250])

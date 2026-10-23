import sys,json
from review import top,rows
done={l.split("\t")[0] for l in open("decisions.tsv",encoding="utf-8") if l.strip()}
pre=sys.argv[1];a=int(sys.argv[2]);b=int(sys.argv[3])
sel=[r for r in rows if r["doc"].startswith(pre) and r["id"] not in done and r["book"].isdigit() and r["method"]!="range" and not r["claim"].startswith("|")]
if len(sys.argv)>4: print(len(sel))
else:
  for r in sel[a:b]:
    print("\n%s [%s] B%s: %s"%(r["id"],r["doc"].split("/")[-1][:-3],r["book"],r["claim"][:150]))
    for t in top(r["claim"],int(r["book"]),2): print("   %.2f Ch%d L%d-%d | %s"%(t[0],t[1],t[3],t[4],t[5][:140]))

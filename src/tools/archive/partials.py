import json,sys,io
sys.stdout=io.TextIOWrapper(sys.stdout.buffer,encoding="utf-8",errors="replace")
exec(open("newrows.py",encoding="utf-8").read().split("skipdocs")[0])
r=json.load(open("register_final.json"))
p=[a for a in r if a["conf"]=="partial" and int(a["id"][1:])<640]
lo,hi=int(sys.argv[1]),int(sys.argv[2])
for a in p[lo:hi]:
    ch=lines(int(a["book"]),a["ch"])
    s=max(1,a["lo"]-1); e=a["hi"]+2
    src=" | ".join(x[:230] for x in ch[0][s-1:e][:4])
    print("%s %s B%s Ch%s L%s-%s\n  CL: %s\n  NOTE: %s\n  SRC: %s"%(a["id"],a["doc"].split("/")[-1],a["book"],a["ch"],a["lo"],a["hi"],a["claim"][-220:],a["note"][:120],src))

import json,sys,io
sys.stdout=io.TextIOWrapper(sys.stdout.buffer,encoding="utf-8",errors="replace")
exec(open("newrows.py",encoding="utf-8").read().split("skipdocs")[0])
reg=json.load(open("register_final.json"))
for doc in sys.argv[1:]:
    for a in reg:
        if a["doc"]!=doc or int(a["id"][1:])>=640 or a["ch"] is None: continue
        ch=lines(int(a["book"]),a["ch"])
        txt=" | ".join(x[:260] for x in ch[0][a["lo"]-1:a["hi"]][:2]) if ch else "?"
        print("%s [%s] %s B%s Ch%s L%s-%s\n   CL: ...%s\n   SRC: %s"%(a["id"],a["tag"],a["conf"],a["book"],a["ch"],a["lo"],a["hi"],a["claim"][-170:],txt))

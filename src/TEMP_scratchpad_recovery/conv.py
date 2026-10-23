import re,json,os,sys,collections
base=r"C:\Users\Gabriel\Documents\World Stuff\HWFWM Compendium"
reg=json.load(open("register_final.json"))
TAG=re.compile(r"\((notes, )?(Books? [0-9][0-9, and-]*)\)")
def norm(s): return re.sub(r"[^a-z0-9]","",s.lower())
bydoc=collections.defaultdict(list)
for r in reg:
    if int(r["id"][1:])<640 and r["conf"] in("verified","exact") and r["ch"] is not None: bydoc[r["doc"]].append(r)
stat=collections.Counter(); out=[]
for doc,rs in bydoc.items():
    p=os.path.join(base,doc.replace("/","\\"))
    if not os.path.exists(p): stat["nofile"]+=1; continue
    for ln_no,ln in enumerate(open(p,encoding="utf-8").read().split("\n"),1):
        tags=list(TAG.finditer(ln))
        if not tags: continue
        for m in tags:
            if len(tags)>1: stat["multi-tag line"]+=1; continue
            if "Books" in m.group(2) : stat["multi-book"]+=1; continue
            pre=ln[:m.start()]
            pre=TAG.sub("",pre)
            cand=[r for r in rs if r["tag"].endswith(m.group(2).replace("Books","Book")) and norm(r["claim"])[-30:] and norm(r["claim"])[-30:] in norm(pre)]
            locs={(r["book"],r["ch"],r["lo"],r["hi"]) for r in cand}
            if len(locs)==1:
                stat["convertible"]+=1; out.append((doc,ln_no,m.group(0),locs.pop()))
            elif not locs: stat["no row"]+=1
            else: stat["ambiguous"]+=1
print(stat); json.dump(out,open("conv_plan.json","w"))

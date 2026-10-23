import json,collections,re
base=r"C:\Users\Gabriel\Documents\World Stuff\HWFWM Compendium\Appendices\Source_Map.md"
rows=json.load(open("register_final.json"))
def ref(r): return "B%s Ch%d L%d-%d"%(int(r["book"]),r["ch"],r["lo"],r["hi"])
ch=[r for r in rows if r["state"] and r["ch"] is not None and str(r["book"]).isdigit() and r["doc"][:3] in ("07_","08_","05_","06_","02_")]
byb=collections.defaultdict(list)
for r in ch: byb[int(r["book"])].append(r)
sec=["## 5. Change log by book (state changes harvested from the register)","","Candidate entries: each is a claim flagged as a gain, loss, death, birth, move or change. Only rows whose confidence is **verified** have been read at the cited lines; the others still need a chapter read before the order is treated as settled.",""]
for n in sorted(byb):
    sec+=["### Book %d"%n,"","| Chapter | Subject (document) | Change | Reference | ID | Conf. |","|---|---|---|---|---|---|"]
    for r in sorted(byb[n],key=lambda r:(r["ch"],r["lo"])):
        subj=r["doc"].split("/")[-1][:-3].replace("_"," ")
        sec.append("| Ch%d | %s | %s | %s | %s | %s |"%(r["ch"],subj,r["claim"][:150].replace("|","/"),ref(r),r["id"],r["conf"]))
    sec.append("")
s=open(base,encoding="utf-8").read()
a=s.index("## 5. Change log");b=s.index("## 6. Timeline thread")
s=s[:a]+"\n".join(sec)+"\n"+s[b:]
c=collections.Counter(r["conf"] for r in rows)
line="| 2026-10-21 | TODO section H (33 items) | Each item searched; claims found, retagged or corrected | 24 claims found in the chapter files (e.g. B3 Ch21 L60 Gary almost silver, B3 Ch29 L35 Path of Shadows regional gate, B12 Ch67 L65 seventeen years); 8 retagged to notes; Path of Shadows range in Jason_Asano.md corrected (the two-hundred-kilometre figure was not in the books). Register: %d verified, %d partial, %d unlocated. |"%(c["verified"],c["partial"],c["unlocated"])+chr(10)
s=s.replace("| 2026-10-20 | 07_Characters",line+"| 2026-10-20 | 07_Characters",1)
open(base,"w",encoding="utf-8").write(s)
print(c)

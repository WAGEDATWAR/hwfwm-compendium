import os,re
from tagsent import old_tags,base
tot={}
for r,d,f in os.walk(base):
    if "Source_Text" in r or r.endswith("Appendices"): continue
    for fn in f:
        if not fn.endswith(".md"): continue
        p=os.path.join(r,fn); n=0
        for ln in open(p,encoding="utf-8").read().split("\n"):
            if ln.startswith(("Status:","Spoiler","Sources:","Related:","Valid")): continue
            for s,e,g in old_tags(ln):
                if g=="(wiki)" or g.startswith("(Later") or g.startswith("(Level"): continue
                if re.match(r"\(notes[^()]*\)$",g): continue
                if ln.startswith("|") and re.match(r"\(Books? [\d, -]+\)$",g): continue
                n+=1
        if n: tot[os.path.relpath(p,base)]=n
for k,v in sorted(tot.items()): print(v,k)
print(sum(tot.values()))

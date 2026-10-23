import sys,os,io
from tagsent import old_tags,base
n=int(os.environ.get("W","55"))
for doc in [a for a in sys.argv[1:]]:
    p=os.path.join(base,doc.replace("/","\\"))
    for i,ln in enumerate(open(p,encoding="utf-8").read().split("\n"),1):
        if ln.startswith(("Status:","Spoiler","Sources:","Related:","Valid")): continue
        for s,e,g in old_tags(ln):
            if g=="(wiki)" or g.startswith(("(Later","(Level")) or g.startswith("(notes") and "Book" in g and False: continue
            print("%d|%s%s"%(i,ln[max(0,s-n):s],g))

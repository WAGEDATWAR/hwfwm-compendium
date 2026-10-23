import sys
rows=[l.split("|") for l in open(sys.argv[1],encoding="utf-8").read().strip().split("\n") if l.strip()]
with open("decisions.tsv","a",encoding="utf-8") as f:
    for r in rows:
        r=[x.strip() for x in r]
        f.write("\t".join(r)+"\n")
print(len(rows),"decisions added")

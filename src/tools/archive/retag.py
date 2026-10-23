import json, re, sys, collections
base = r"C:\Users\Gabriel\Documents\World Stuff\HWFWM Compendium"
rows = json.load(open("register_final.json"))
apply = len(sys.argv) > 1
NL = chr(10)
cands = [r for r in rows if r["conf"] == "unlocated" and r["tier"] == "book" and r["method"] != "range"
         and re.match(r"(?i)books? \d", r["tag"]) and not r["claim"].lower().startswith("spoiler")]
print(len(cands))
byd = collections.defaultdict(list)
for r in cands:
    byd[r["doc"]].append(r)
done = 0
miss = 0
log = []
for doc, lst in byd.items():
    p = base + "/" + doc
    s = open(p, encoding="utf-8").read()
    for r in lst:
        cl = re.sub(r"\s+", " ", r["claim"]).strip()
        tag = "(" + r["tag"] + ")"
        ws = re.findall(r"[A-Za-z0-9']+", cl)
        ok = False
        for n in (4, 3):
            if len(ws) < n:
                continue
            pat = re.compile(r"\W+".join(re.escape(w) for w in ws[-n:]))
            for m in pat.finditer(s):
                j = s.find(tag, m.end() - 1)
                nxt = s.find(NL, m.end())
                if j >= 0 and (nxt < 0 or j < nxt):
                    s = s[:j] + "(notes, " + r["tag"] + ")" + s[j + len(tag):]
                    ok = True
                    break
            if ok:
                break
        if ok:
            done += 1
            log.append(r["id"])
        else:
            miss += 1
            print("MISS", r["id"], doc, cl[:60])
    if apply:
        open(p, "w", encoding="utf-8").write(s)
print("retagged", done, "missed", miss)
json.dump(log, open("retagged_ids.json", "w"))

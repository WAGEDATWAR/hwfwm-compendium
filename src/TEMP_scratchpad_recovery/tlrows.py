TL = "08_History_and_Timeline/Master_Timeline.md"
_old = {(int(r["book"]), r["ch"], r["lo"]) for r in json.load(open("register_final.json")) if r["doc"] == TL and int(r["id"][1:]) < 640}
_tl = open(base + "\\08_History_and_Timeline\\Master_Timeline.md", encoding="utf-8").read()
_sec = ""
for ln in _tl.split("\n"):
    if ln.startswith("## "):
        _sec = ln[3:]
    isrow = ln.startswith("- ") or (ln.startswith("|") and not ln.startswith("|---") and not ln.startswith("| Month")) or re.match(r"\d\. ", ln)
    if not isrow:
        continue
    claim = re.sub(r"\s*\([^()]*Book \d+, Ch\d+ L\d+[^()]*\)", "", ln).strip("-| ").strip()
    for (b, c, lo, hi) in CIT.findall(ln):
        b, c, lo = int(b), int(c), int(lo)
        hi = int(hi) if hi else lo
        if (b, c, lo) in _old:
            continue
        ch = lines(b, c)
        if ch is None:
            low.append((TL, "NO CHAPTER", b, c, lo, claim[:80]))
            continue
        rows.append(dict(doc=TL, sec=_sec, claim=claim[:300], tag="Book %d" % b, tier="book", book=str(b), ch=c, title=ch[1], lo=lo, hi=hi, score=0, method="written", state=False, conf="verified", note="timeline pass"))

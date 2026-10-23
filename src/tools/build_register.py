"""Rebuild Appendices/Source_Register.md and Appendices/Source_Map.md from the compendium itself.

Usage: python3 build_register.py [--dry]
Reads: every compendium .md except the generated/working files; src/Source_Text chapter files;
       chapter_index.json; old_register.json (hand notes carried over); map_log.tsv; map_thread.tsv.
Writes: Appendices/Source_Register.md, Appendices/Source_Map.md, register_new.json
"""
import io, json, os, re, sys, collections

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
HERE = os.path.dirname(os.path.abspath(__file__))
BASE = os.path.abspath(os.path.join(HERE, "..", ".."))
ST = os.path.join(BASE, "src", "Source_Text")
EXCLUDE = {"Appendices/Source_Register.md", "Appendices/Source_Map.md", "Appendices/Change_Log.md",
           "TODO_Verification.md", "00_Project_Structure.md"}
HEADER_KEYS = ("Status:", "Spoiler level:", "Valid from:", "Valid through:", "Sources:", "Related:")

idx = json.load(open(os.path.join(HERE, "chapter_index.json"), encoding="utf-8"))
CH = {}
for b, lst in idx.items():
    for num, title, fn, nl, _ in lst:
        CH[(int(b), num)] = (title, os.path.join(ST, "Book_%02d" % int(b), fn))
_cache = {}


def chapter_lines(b, c):
    k = (b, c)
    if k not in CH:
        return None
    if k not in _cache:
        _cache[k] = open(CH[k][1], encoding="utf-8").read().split("\n")
    return _cache[k]


STOP = set("""the and was were that this with from have had his her their they for are not but who which when after before into
over under about also than then there here him them its out one two been would could should will what where while because
since only more most some such each both other another between during through again very just like said says say
book chapter line lines rank ranks ranked""".split())


def terms(t):
    t = t.lower().replace("’", "'")
    return {w for w in re.findall(r"[a-z]{4,}", t) if w not in STOP}


# ------------------------------------------------------------------ citations
CITE = re.compile(r"(?:Book (\d+), )?Ch(\d+) (L\d+(?:-L?\d+)?(?:, L\d+(?:-L?\d+)?)*)")
SPAN = re.compile(r"L(\d+)(?:-L?(\d+))?")


def find_cites(text, last_book):
    """Return (list of (start,end,book,ch,lo,hi)), last_book."""
    out = []
    for m in CITE.finditer(text):
        if m.group(1):
            last_book = int(m.group(1))
        else:
            pb = re.search(r"Books? (\d+)(?:\s*[-–]\s*\d+)?[\s,]*\(?$", text[max(0, m.start() - 24):m.start()])
            if pb:
                last_book = int(pb.group(1))
        if last_book is None:
            continue
        for s in SPAN.finditer(m.group(3)):
            lo = int(s.group(1)); hi = int(s.group(2) or lo)
            out.append((m.start(), m.end(), last_book, int(m.group(2)), lo, hi))
    return out, last_book


def strip_cites(text):
    """Remove citation expressions and the empty parentheses/commas they leave."""
    def _rep(m):
        pre = text[max(0, m.start() - 12):m.start()].lower()
        if m.group(1) and re.search(r"(in|at|from|of|by|during|until|since)\s+$", pre):
            return "Book " + m.group(1)
        return ""
    t = CITE.sub(_rep, text)
    t = re.sub(r"\((?:\s*(?:see|notes|wiki|and|also|compare|cf\.|for example|e\.g\.)?\s*[,;]?\s*)*\)", "", t)
    t = re.sub(r"\(\s*[;,]\s*", "(", t)
    t = re.sub(r"\s*[;,]\s*\)", ")", t)
    t = re.sub(r";\s*;", ";", t)
    t = re.sub(r"\(\s*\)", "", t)
    t = re.sub(r",\s*;", ";", t)
    t = re.sub(r",\s*\)", ")", t)
    t = re.sub(r"\(\s*,", "(", t)
    return t


NOTE_TAG = re.compile(r"\((notes[^)]*|wiki[^)]*)\)", re.I)


def clean(t):
    t = re.sub(r"\*\*|__|`", "", t)
    t = re.sub(r"(?<!\w)\*(?=\S)|(?<=\S)\*(?!\w)", "", t)
    t = re.sub(r"\[([^\]]+)\]\([^)]*\)", r"\1", t)
    t = re.sub(r"\s+", " ", t).strip()
    t = re.sub(r"\s+([,;:)])", r"\1", t)
    t = re.sub(r"\s+\.(?=\s|$)", ".", t)
    t = re.sub(r"\(\s+", "(", t)
    t = t.replace(" ,", ",")
    t = re.sub(r"(Cues?|Cited|Sources?):?[\s;,]*(?=\.|$)", "", t)
    t = re.sub(r":\s*;", ":", t)
    t = re.sub(r"\s+\.", ".", t)
    return t.strip(" -;,")


def cap(t, n=420):
    if len(t) <= n:
        return t
    cut = t[:n].rsplit(" ", 1)[0]
    return cut.rstrip(" ,;:(") + " …"


SENT = re.compile(r"(?<=[.!?])[\"”)]*\s+(?=[A-Z*\"“(\[])")


def sentences(line):
    """Split on sentence boundaries outside parentheses and double quotes; merge very short tails."""
    parts, start = [], 0
    for m in SENT.finditer(line):
        seg = line[start:m.end()]
        if seg.count("(") - seg.count(")") > 0:
            continue
        if seg.count('"') % 2 == 1 or seg.count("“") > seg.count("”"):
            continue
        parts.append(line[start:m.end()].strip())
        start = m.end()
    parts.append(line[start:].strip())
    parts = [p for p in parts if p]
    merged = []
    for p in parts:
        if merged and len(clean(strip_cites(p))) < 40:
            merged[-1] = merged[-1] + " " + p
        else:
            merged.append(p)
    return merged


# ------------------------------------------------------------------ documents
def doc_key(rel):
    parts = rel.split("/")
    top = parts[0]
    if len(parts) == 1:
        k0 = (0, top) if top.startswith("0") else (9, top)
    else:
        k0 = (1, top)
    out = [k0]
    for i, p in enumerate(parts[1:], 1):
        last = i == len(parts) - 1
        out.append((0 if (last and p.startswith("00_")) else (1 if last else 2), p))
    return out


def list_docs():
    docs = []
    for root, dirs, files in os.walk(BASE):
        rel_root = os.path.relpath(root, BASE).replace("\\", "/")
        if rel_root.split("/")[0] in ("src", "Source_Text", ".git", "TEMP_scratchpad_recovery"):
            continue
        for f in files:
            if f.endswith(".md"):
                rel = (f if rel_root == "." else rel_root + "/" + f)
                if rel not in EXCLUDE:
                    docs.append(rel)
    return sorted(docs, key=doc_key)


# ------------------------------------------------------------------ scoring
def score(claim, b, c, lo, hi):
    ls = chapter_lines(b, c)
    if ls is None:
        return None, "no such chapter"
    n = len(ls)
    if lo > n:
        return None, "line %d beyond end (%d lines)" % (lo, n)
    ct = terms(claim)
    if not ct:
        return (1.0, 1.0), ""
    a = max(0, lo - 1 - 1); z = min(n, hi + 1)
    near = terms(" ".join(ls[a:z]))
    s1 = len(ct & near) / len(ct)
    a2 = max(0, lo - 1 - 6); z2 = min(n, hi + 6)
    wide = terms(" ".join(ls[a2:z2]))
    s2 = len(ct & wide) / len(ct)
    return (s1, s2), ""


def grade(sc):
    if sc is None:
        return "bad"
    s1, s2 = sc
    if s1 >= 0.30:
        return "ok"
    if s1 >= 0.15 or s2 >= 0.30:
        return "near"
    return "weak"


RANKG = {"bad": 0, "weak": 1, "near": 2, "ok": 3}


def extract(rel):
    path = os.path.join(BASE, rel)
    lines = open(path, encoding="utf-8").read().split("\n")
    rows = []
    last_book = None
    sec = ""
    in_code = False
    for ln in lines:
        s = ln.strip()
        if s.startswith("```"):
            in_code = not in_code
            continue
        if in_code or not s:
            continue
        if s.startswith("#"):
            sec = clean(s.lstrip("# "))
            continue
        if s.startswith(HEADER_KEYS):
            continue
        if s.startswith("|"):
            cells = [c.strip() for c in s.strip("|").split("|")]
            if all(re.fullmatch(r":?-{2,}:?", c) or not c for c in cells):
                continue
            units = [" — ".join(c for c in cells if c)]
        else:
            body = re.sub(r"^(?:[-*]\s+|\d+\.\s+)", "", s)
            units = sentences(body)
        for u in units:
            cites, last_book = find_cites(u, last_book)
            tags = NOTE_TAG.findall(u)
            if not cites and not tags:
                continue
            claim = clean(strip_cites(NOTE_TAG.sub("", u))) if tags else clean(strip_cites(u))
            if not claim or len(claim) < 8:
                continue
            rows.append({"doc": rel, "sec": sec, "claim": claim, "cites": cites,
                         "tags": [t.strip() for t in tags]})
    return rows


def merge_cites(cites):
    seen, out = set(), []
    for _, _, b, c, lo, hi in cites:
        k = (b, c, lo, hi)
        if k not in seen:
            seen.add(k); out.append(k)
    return out


def tag_books(tags):
    bs = []
    for t in tags:
        for m in re.finditer(r"Books? (\d+)(?:\s*(?:-|to|and)\s*(\d+))?", t):
            a = int(m.group(1)); z = int(m.group(2) or a)
            bs += list(range(a, z + 1))
    return sorted(set(bs))


def main():
    old = json.load(open(os.path.join(HERE, "old_register.json"), encoding="utf-8"))
    old_by_doc = collections.defaultdict(list)
    for o in old:
        if o.get("note") and o["note"] != "line-level citation pass":
            old_by_doc[o["doc"]].append(o)
    rows = []
    for rel in list_docs():
        rows += extract(rel)
    out = []
    carried = 0
    for r in rows:
        refs = merge_cites(r["cites"])
        marks = []
        for (b, c, lo, hi) in refs:
            sc, err = score(r["claim"], b, c, lo, hi)
            marks.append((b, c, lo, hi, grade(sc), err, sc))
        if refs:
            best = max(marks, key=lambda m: RANKG[m[4]])[4]
            tier = "book"
        else:
            best = "notes" if any(t.lower().startswith("notes") for t in r["tags"]) else "wiki"
            tier = best
        note = ""
        ct = terms(r["claim"])
        for o in old_by_doc.get(r["doc"], []):
            ot = terms(o["claim"])
            if not ct or not ot:
                continue
            jac = len(ct & ot) / len(ct | ot)
            share = any((int(o["book"]), o["ch"], o["lo"]) == (b, c, lo) for (b, c, lo, hi) in refs) if refs else \
                (o["tier"] != "book")
            if jac >= 0.45 and share:
                note = o["note"]
                if best in ("weak", "near") and o["conf"] == "verified":
                    best = "reviewed"
                break
        if note:
            carried += 1
        out.append(dict(r, refs=marks, check=best, tier=tier, note=note, books=tag_books(r["tags"])))
    prev_path = os.path.join(HERE, "register_new.json")
    prev = json.load(open(prev_path, encoding="utf-8")) if os.path.exists(prev_path) else []
    json.dump([{k: v for k, v in o.items() if k not in ("cites",)} for o in out],
              open(prev_path, "w", encoding="utf-8"), default=str)
    cnt = collections.Counter(o["check"] for o in out)
    print(len(out), "rows;", dict(cnt), "carried notes:", carried)
    import delta
    print(delta.report(prev, json.load(open(prev_path, encoding="utf-8"))), "(see src/tools/register_delta.md)")
    if "--dry" in sys.argv:
        return out
    write_register(out, cnt)
    write_map(out, cnt)
    return out


def refstr(b, c, lo, hi):
    return "B%d Ch%d L%d%s" % (b, c, lo, "-%d" % hi if hi != lo else "")


def write_register(out, cnt):
    n = 0
    byd = collections.OrderedDict()
    for o in out:
        n += 1
        o["id"] = "R%04d" % n
        byd.setdefault(o["doc"], []).append(o)
    L = []
    L += ["# Source Register", "",
          "Status: Draft (rebuilt automatically from the compendium text; the Check column grades how well the cited lines overlap the claim, and only rows marked reviewed carry a human reading)",
          "Spoiler level: 3 (references reveal where events occur)",
          "Valid from: Book 1", "Valid through: Book 13",
          "Sources: `src/Source_Text/` (book chapter files)",
          "Related: Source_Map.md, ../src/Source_Text/README.md", "",
          "Every claim in the compendium that carries a line citation (`Book N, ChX LY`), a chapter-notes tag (`notes`) or a wiki tag (`wiki`) has a row here. A row is one sentence or one table row of a document; its claim text is that sentence with the citations removed, and its references are listed with a grade each. The register is regenerated by a script from the documents, so it always matches them; the **row IDs are renumbered at each rebuild**, so refer to a row by its document and reference, not its ID.",
          "",
          "**Reference format.** `B7 Ch31 L12-15` is Book 7, chapter 31, lines 12 to 15 of the chapter file under `src/Source_Text/`. Rows are in document order, documents in folder order.",
          "",
          "**Check column**",
          "- **ok**: at least 30 percent of the claim's distinctive words appear in the cited lines (or one line either side).",
          "- **near**: 15 to 30 percent in the cited lines, or 30 percent within six lines of them. Usually a summary of a longer passage or a list-style citation.",
          "- **weak**: under 15 percent. The citation may be correct but is not confirmed by the word overlap; read the lines. These rows are the review queue.",
          "- **bad**: the chapter or line does not exist.",
          "- **reviewed**: a person read the lines and confirmed the claim (kept from earlier passes; the note says what was checked).",
          "- **notes** / **wiki**: the claim is tagged as taken from the chapter summaries or the fan wiki and has no line reference; narrow it to the book text when possible, then retag it `Book N`.",
          "",
          "Each reference in the Cited lines column shows its own grade in brackets. The overlap grade is a heuristic: a high grade does not prove the claim, and a low one does not disprove it.",
          "",
          "**Totals**: " + ", ".join("%s %d" % (k, cnt[k]) for k in ("ok", "near", "weak", "bad", "reviewed", "notes", "wiki") if cnt.get(k)) + " (%d rows in %d documents)." % (len(out), len(byd)),
          ""]
    for doc, lst in byd.items():
        L += ["## " + doc, "", "| ID | Claim | Cited lines | Chapter | Check | Note |", "|---|---|---|---|---|---|"]
        for o in lst:
            cl = cap(o["claim"]).replace("|", "/")
            if o["refs"]:
                cited = "; ".join("%s (%s)" % (refstr(b, c, lo, hi), g) for (b, c, lo, hi, g, e, s) in o["refs"])
                seen, titles = set(), []
                for (b, c, lo, hi, g, e, s) in o["refs"]:
                    if (b, c) not in seen:
                        seen.add((b, c)); titles.append("B%d Ch%d %s" % (b, c, CH.get((b, c), ("?",))[0]))
                chap = "; ".join(titles[:4]) + (" …" if len(titles) > 4 else "")
                errs = [e for (b, c, lo, hi, g, e, s) in o["refs"] if e]
                nt = o["note"] + (" " if o["note"] and errs else "") + " ".join(errs)
            else:
                bk = ", ".join(str(b) for b in o["books"])
                cited = "(no lines) " + "; ".join(o["tags"])
                chap = ("Book " + bk) if bk else ""
                nt = o["note"]
            L.append("| %s | %s | %s | %s | %s | %s |" % (o["id"], cl, cited, chap.replace("|", "/"),
                                                       o["check"], nt.replace("|", "/").replace("\n", " ")))
        L.append("")
    open(os.path.join(BASE, "Appendices", "Source_Register.md"), "w", encoding="utf-8").write("\n".join(L))


# ------------------------------------------------------------------ source map
STATE = re.compile(r"(dies|died|death of|killed|kills|slain|marries|married|engaged to|"
                   r"reaches (?:iron|bronze|silver|gold|diamond)|reached (?:iron|bronze|silver|gold|diamond)|destroyed|destroys|resurrect\w*|"
                   r"sanction\w*|betray\w*|abolish\w*|sundered|reincarnat\w*|joins the|leaves the)", re.I)
STATE_DOCS = ("02_", "05_", "06_", "07_")


def story_key(refs):
    return min((b, c, lo) for (b, c, lo, hi, g, e, s) in refs)


def write_map(out, cnt):
    log = [l.rstrip("\n").split("\t") for l in open(os.path.join(HERE, "map_log.tsv"), encoding="utf-8") if l.strip()]
    thread = [l.rstrip("\n").split("\t") for l in open(os.path.join(HERE, "map_thread.tsv"), encoding="utf-8") if l.strip()]
    thread_notes = open(os.path.join(HERE, "map_thread_notes.md"), encoding="utf-8").read().strip()
    docs_n = len(set(o["doc"] for o in out))
    L = ["# Source Map", "",
         "Status: Draft (sections 1 to 3 and 7 are written by hand; sections 4 to 6 are regenerated from the compendium by `build_register.py` so they always match the documents)",
         "Spoiler level: 3", "Valid from: Book 1", "Valid through: Book 13",
         "Sources: `src/Source_Text/` chapter files; `Source_Register.md`",
         "Related: Source_Register.md, ../src/Source_Text/README.md, ../08_History_and_Timeline/Master_Timeline.md, ../00_Project_Structure.md", "",
         "## 1. Purpose", "",
         "The Source Map ties compendium claims to book, chapter and lines so that facts can be traced, narrowed and re-checked. Where the Source Register is organised by document, the map is organised by the story: sections 4 to 6 run in book, chapter and line order, which is story order.", "",
         "## 2. How the pieces fit", "",
         "- `src/Source_Text/Book_NN/Ch_NNN_Title.txt`: the book text, one file per chapter.",
         "- `Appendices/Source_Register.md`: one row per cited claim in the compendium, graded for how well the cited lines support it.",
         "- This file: the rules, the timeline thread (section 4), the chapter index (section 5), the state-change list (section 6) and the log of source-checking work (section 7).",
         "- The register and sections 4 to 6 are regenerated together by `src/tools/build_register.py`; run it after editing any document.", "",
         "## 3. Rules", "",
         "1. Reference format: `B7 Ch31 L12-15` (book, chapter, lines of the chapter file). In documents the form is `(Book 7, Ch31 L12-15)`.",
         "2. Hierarchy stays Book Files > Chapter Summaries > Wiki. A claim tagged `notes` or `wiki` should be narrowed to a book location when possible and retagged `Book N`.",
         "3. Grades are heuristic (see the Check column key in the register). Rows graded **weak** are the review queue; **reviewed** rows were read by a person.",
         "4. If lines do not support a claim, correct the document and log the correction in `Change_Log.md`.",
         "5. When a document is added, renamed or removed, rebuild the register. Do not edit the generated tables by hand.", ""]
    # section 4 thread
    rows = []
    for t in thread:
        m = re.search(r"B(\d+) Ch(\d+) L(\d+)", t[2])
        k = (int(m.group(1)), int(m.group(2)), int(m.group(3))) if m else (99, 0, 0)
        rows.append((k, t))
    rows.sort(key=lambda x: x[0])
    L += ["## 4. Timeline thread", "",
          "Dated or ordered facts and intervals that fix the calendar, in story order by first reference. The per-book timelines in `08_History_and_Timeline/` use these anchors; the Master Timeline summarises them.", "",
          "| Event | Date or interval | Reference | Check |", "|---|---|---|---|"]
    for k, t in rows:
        L.append("| %s |" % " | ".join(t[:4]))
    L += ["", thread_notes, ""]
    # section 5 chapter index
    chap = collections.defaultdict(lambda: collections.defaultdict(set))
    for o in out:
        for (b, c, lo, hi, g, e, s) in o["refs"]:
            chap[(b, c)][o["doc"]].add((lo, hi))
    L += ["## 5. Chapter index", "",
          "Every chapter the compendium cites, with the documents that cite it and the lines they use. Documents are abbreviated to the file name; the full path is in the register.", ""]
    cur = None
    for (b, c) in sorted(chap):
        if b != cur:
            cur = b
            L += ["### Book %d" % b, "", "| Chapter | Title | Cited by (lines) | Rows |", "|---|---|---|---|"]
        parts, nrows = [], 0
        for doc, spans in sorted(chap[(b, c)].items(), key=lambda kv: min(kv[1])):
            nm = doc.rsplit("/", 1)[-1][:-3]
            sp = sorted(spans)
            txt = ", ".join("L%d%s" % (lo, "-%d" % hi if hi != lo else "") for lo, hi in sp[:6]) + (" …" if len(sp) > 6 else "")
            parts.append("%s %s" % (nm, txt)); nrows += len(sp)
        L.append("| Ch%d | %s | %s | %d |" % (c, CH[(b, c)][0].replace("|", "/"), "; ".join(parts[:8]) + (" …" if len(parts) > 8 else ""), nrows))
        if (b, c) == max(k for k in chap if k[0] == b):
            L.append("")
    # section 6 state changes
    sc = []
    for o in out:
        if not o["doc"].startswith(STATE_DOCS) or not o["refs"] or o["check"] not in ("ok", "reviewed"):
            continue
        if not STATE.search(o["claim"]):
            continue
        good = [r for r in o["refs"] if r[4] == "ok"]
        if not good:
            continue
        sc.append((story_key(good), o, good[0]))
    sc.sort(key=lambda x: x[0])
    seen = set()
    L += ["## 6. State changes by book", "",
          "Claims in the Cosmology, Organisations, Places and Characters documents that describe a death, birth, arrival, departure, gain, transformation or similar change, where the first reference grades **ok**. In story order. This list is generated by keyword and is a starting point for a change log, not a settled one.", ""]
    cur = None
    for key, o, ref in sc:
        b, c, lo, hi = ref[0], ref[1], ref[2], ref[3]
        sig = (o["doc"], b, c, lo)
        if sig in seen:
            continue
        seen.add(sig)
        if b != cur:
            cur = b
            L += ["", "### Book %d" % b, "", "| Chapter | Subject (document) | Change | Reference |", "|---|---|---|---|"]
        L.append("| Ch%d | %s | %s | %s |" % (c, o["doc"].rsplit("/", 1)[-1][:-3].replace("_", " "), cap(o["claim"], 230).replace("|", "/"), refstr(b, c, lo, hi)))
    L += ["", "## 7. Source-checking log", "",
          "The history of the checking work, oldest first. Entries refer to earlier register states (their row IDs no longer exist). The register was rebuilt from the documents in the pass of 2026-10-22, which removed duplicate and cut-off rows and the rows of a deleted document.", "",
          "| Date | Scope | Result | Note |", "|---|---|---|---|"]
    for t in log:
        L.append("| %s |" % " | ".join(t[:4]))
    L.append("")
    open(os.path.join(BASE, "Appendices", "Source_Map.md"), "w", encoding="utf-8").write("\n".join(L))


if __name__ == "__main__":
    main()

# document lint (src/tools/lint.py): report errors and warnings after every build
import lint
_e, _w, _n = lint.run()
print("lint: %d documents, %d errors, %d warnings (see src/tools/lint_report.md)" % (_n, len(_e), len(_w)))

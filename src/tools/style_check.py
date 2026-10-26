"""Style and accessibility check for the compendium documents (build plan item 5.9).

Checks the rules in section 7 of 00_Project_Structure.md that a script can test, and the heading template of the character files:
  shorthand      abbreviations and note marks the style rules forbid: e.g., i.e., etc., vs, cf., approx, "&", "~", "w/", "->", "=>", TBD
  template       an individual character file must follow the full template (Summary, Appearance, Personality and voice, Powers and
                 skills as world facts, Background, Timeline of involvement, Relationships, Secrets and spoiler notes, Roleplay notes)
                 or the short template (Summary, Facts, Roleplay notes), each with optional extras such as Timeline of involvement and Open questions
  spelling       the variant spellings of the Glossary's variants table used outside that table, counted per file
  heading        a heading that skips a level (## to ####), or a table without a header separator row (a screen reader needs a header)
Writes src/tools/style_report.md and prints the counts. Usage: python3 src/tools/style_check.py
"""
import os, re, sys, io

HERE = os.path.dirname(os.path.abspath(__file__))
BASE = os.path.abspath(os.path.join(HERE, "..", ".."))
SKIP_PREFIX = ("Appendices/Source_", "Appendices/Change_Log", "src/", "Appendices/Wiki_Reference_Lists.md", "10_Roleplay_Support/NPC_Cards/")
SKIP_FILES = {"TODO_Build_Plan.md", "TODO_Verification.md", "00_Project_Structure.md"}
SHORTHAND = [("e.g.", r"(?<![A-Za-z])e\.g\."), ("i.e.", r"(?<![A-Za-z])i\.e\."), ("etc.", r"(?<![A-Za-z])etc\."), ("vs", r"(?<![A-Za-z])vs\.?\s"),
             ("cf.", r"(?<![A-Za-z])cf\."), ("approx", r"(?<![A-Za-z])approx(?![a-z])"), ("&", r" & "), ("~", r" ~\d"), ("w/", r" w/ "),
             ("->", r"->"), ("=>", r"=>"), ("TBD", r"(?<![A-Za-z_])(TBD|TODO)(?![A-Za-z_])")]
NO_AMP = ("08_History_and_Timeline/Chapter_Digest", "Appendices/Name_Index.md")
FULL = {"Summary", "Appearance", "Personality and voice", "Powers and skills as world facts", "Background", "Timeline of involvement",
        "Relationships", "Secrets and spoiler notes", "Roleplay notes"}
SHORT = {"Summary", "Facts", "Roleplay notes"}
# variant spellings (first form is the one to use); the Glossary table lists them
VARIANTS = {"Hurin": ["Huren"], "Jonah": ["Jonas"], "Hendren": ["Hedron", "Herston"]}
VARIANT_CONTEXT = re.compile(r"variant|spell|spelt|once|inconsisten|text gives|called", re.I)
GROUP_FILES = {"07_Characters/Familiars.md"}


def docs():
    for root, dirs, files in os.walk(BASE):
        dirs[:] = [d for d in dirs if d not in (".git", "src")]
        for f in files:
            rel = os.path.relpath(os.path.join(root, f), BASE).replace("\\", "/")
            if f.endswith(".md") and not rel.startswith(SKIP_PREFIX) and rel not in SKIP_FILES:
                yield rel


def clean(t):
    t = re.sub(r"<!--.*?-->", "", t, flags=re.S)
    t = re.sub(r"```.*?```", "", t, flags=re.S)
    return re.sub(r"`[^`\n]*`", "", t)


def main():
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
    out = {"shorthand": [], "template": [], "spelling": [], "heading": []}
    for rel in sorted(docs()):
        raw = open(os.path.join(BASE, rel), encoding="utf-8").read()
        t = clean(raw)
        in_glossary_variants = rel == "Appendices/Glossary.md"
        for name, pat in SHORTHAND:
            if name == "&" and rel.startswith(NO_AMP):
                continue  # chapter titles and names carry their own ampersands
            n = len(re.findall(pat, t))
            if n:
                out["shorthand"].append((rel, "%s x%d" % (name, n)))
        # heading levels and tables
        prev = 0
        for i, l in enumerate(t.split("\n"), 1):
            m = re.match(r"^(#{1,6}) ", l)
            if m:
                lv = len(m.group(1))
                if prev and lv > prev + 1:
                    out["heading"].append((rel, "line %d: heading jumps from level %d to %d" % (i, prev, lv)))
                prev = lv
        lines = t.split("\n")
        for i, l in enumerate(lines):
            if l.startswith("|") and (i == 0 or not lines[i - 1].startswith("|")):
                nxt = lines[i + 1] if i + 1 < len(lines) else ""
                if not re.match(r"^\|[\s:|-]+\|?\s*$", nxt):
                    out["heading"].append((rel, "table at line %d has no header separator row" % (i + 1)))
        # spelling variants
        if not in_glossary_variants and rel != "Appendices/Name_Index.md":
            for good, bads in VARIANTS.items():
                for b in bads:
                    n = sum(1 for ln in t.split("\n") if re.search(r"(?<![A-Za-z])" + b + r"(?![A-Za-z])", ln) and not VARIANT_CONTEXT.search(ln))
                    if n:
                        out["spelling"].append((rel, "%s x%d (use %s)" % (b, n, good)))
        # character template
        if rel.startswith("07_Characters/") and rel.count("/") == 1 and not rel.startswith("07_Characters/00_") and rel not in GROUP_FILES:
            heads = {re.sub(r"^[0-9]+[A-Z]?\.\s+", "", l[3:]).strip() for l in raw.split("\n") if l.startswith("## ")}
            if not (FULL <= heads or SHORT <= heads):
                missing = sorted(FULL - heads)
                out["template"].append((rel, "neither template: missing %s" % ", ".join(missing[:5])))
    L = ["# Style report", "", "Generated by `src/tools/style_check.py` (build plan item 5.9).", ""]
    for k, items in out.items():
        L += ["## %s (%d)" % (k, len(items)), ""]
        L += ["- `%s`: %s" % it for it in items] or ["None."]
        L.append("")
    open(os.path.join(HERE, "style_report.md"), "w", encoding="utf-8", newline="\n").write("\n".join(L))
    print({k: len(v) for k, v in out.items()}, "(see src/tools/style_report.md)")


if __name__ == "__main__":
    main()

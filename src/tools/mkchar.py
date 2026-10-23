import os, io, sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
BASE = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".."))
CH = os.path.join(BASE, "07_Characters")

def mk(fn, title, lvl, vf, vt, src, rel, summary, facts, roleplay, timeline=None, open_q=None):
    t = "# %s\n\nStatus: Draft (book text; facts carry a reference \"Book N, ChX LY\" to Source_Text; \"notes\" marks chapter-summary-only facts)\nSpoiler level: %s\nValid from: %s\nValid through: %s\nSources: %s\nRelated: %s\n\n## 1. Summary\n\n%s\n\n## 2. Facts\n\n" % (title, lvl, vf, vt, src, rel, summary)
    t += "\n".join("- " + f for f in facts) + "\n\n"
    n = 3
    if timeline:
        t += "## %d. Timeline of involvement\n\n" % n + "\n".join("- " + f for f in timeline) + "\n\n"; n += 1
    t += "## %d. Roleplay notes\n\n%s\n" % (n, roleplay)
    if open_q:
        t += "\n## Open questions\n\n" + "\n".join("- " + q for q in open_q) + "\n"
    open(os.path.join(CH, fn), "w", encoding="utf-8").write(t)
    print("wrote", fn)

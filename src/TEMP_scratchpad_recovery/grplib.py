import os, io, sys
BASE = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".."))
OUT = os.path.join(BASE, "07_Characters", "Minor_Cast")
os.makedirs(OUT, exist_ok=True)


def grp(fn, title, lvl, vf, vt, src, rel, intro, entries):
    t = "# %s\n\nStatus: Draft (book text; facts carry a reference \"Book N, ChX LY\" to Source_Text; \"notes\" marks chapter-summary-only facts)\nSpoiler level: %s\nValid from: %s\nValid through: %s\nSources: %s\nRelated: %s\n\n## 1. Summary\n\n%s\n\n## 2. Entries\n\n" % (title, lvl, vf, vt, src, rel, intro)
    for name, facts in entries:
        t += "### %s\n\n" % name + "\n".join("- " + f for f in facts) + "\n\n"
    t += "## 3. Using this in a story\n\nThese are minor figures: give each one only the facts above. A character with more scenes belongs in its own file in `../`.\n"
    open(os.path.join(OUT, fn), "w", encoding="utf-8").write(t)
    print("wrote", fn)



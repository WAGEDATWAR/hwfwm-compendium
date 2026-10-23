import os
P = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "..", "TODO_Build_Plan.md"))
s = open(P, encoding="utf-8").read()


def line_edit(prefix, addition):
    global s
    i = s.index(prefix)
    j = s.index("\n", i)
    s = s[:j] + " " + addition + s[j:]


# new item 0.9 after 0.8
i = s.index("- **0.8 Spelling and naming variants register")
j = s.index("\n", i)
s = s[:j + 1] + "- **0.9 Spoiler tag syntax and linter support (suggested, M; decision 3).** Define one tag form for spoiler-level sections inside a file, for example an HTML comment pair `<!-- level:2 -->` ... `<!-- /level -->` around the existing \"Later developments\" sections and any other section above the file's header level (comments do not render, so the files read normally). Document the form in section 6 of `00_Project_Structure.md`, add a linter check that tags are balanced, that levels are 0-3 and that no tagged section is lower than the file's header level, and retrofit the existing files section by section, starting with the 2026-10-22 character files. Only retrofit where it is convenient: a file whose header level already covers everything needs no tags.\n" + s[j + 1:]

line_edit("- **2E.2 Characters with many lines but no individual file",
          "**Decision 1:** write a full individual file for any character with enough material to fill the character template (rule of thumb: about 15 or more distinct cited facts, or a role across more than one book) and keep grouped `Minor_Cast/` entries only for characters with little information. Review every current grouped entry against that rule, promote those that qualify (candidates: Hudson Kettering, Niko, Emily, Dara and Zareen Rimaros, Sendira, Laront, Beaufort the cult commander, Kreegle, Killian's later scenes, Hils Jaramaris), and move a promoted entry's facts into the new file and delete it from the group file.")
line_edit("- **3.6 A chapter digest",
          "**Decision 2:** the digest is committed to the repository. It is the project's own short summary (one or two sentences and a cite per chapter, no quoted passages), so it is safe to push; keep it out of any export that would reproduce chapter text.")
line_edit("- **5.3 Wiki list refresh",
          "**Decision 4:** once the cross-reference matcher is improved (for example by also matching phrases such as \"<name> confluence\", \"stone of <name>\" and \"god of <name>\", and by checking spellings in `Name_Index.md`), move `03_Magic_and_Adventuring/Wiki_Reference_Lists.md` to `Appendices/Wiki_Reference_Lists.md`: change the output path in `compose_wiki.py`, the Related lines that point at it, and the references in the Change_Log, Glossary and Gods_and_Churches.")
line_edit("- **5.5 Exports",
          "**Decision 3:** exports respect spoiler levels through tagged sections inside each file (item 0.9) where tags are convenient, falling back to the file's header level elsewhere; the exporter keeps a section only when its level is at or below the requested level.")

i = s.index("## Open decisions that need the project owner")
s = s[:i] + """## Decisions made (2026-10-22)

1. **Characters**: full individual files for characters with enough information to justify one; grouped files only for minor characters with little information (see 2E.2 for the rule of thumb and the promotion review).
2. **Chapter digest (3.6)**: committed to the repository.
3. **Spoiler-level exports (5.5)**: tagged sections inside each file, used where convenient (see 0.9); the header level covers the rest.
4. **Wiki Reference Lists**: to move under `Appendices/` after the cross-reference matcher is improved (see 5.3); no move yet.

No open decisions remain. Add new ones here as they arise.
"""
open(P, "w", encoding="utf-8").write(s)
print("ok")

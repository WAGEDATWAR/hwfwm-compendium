import os
M = r"C:\Users\Gabriel\.claude\projects\C--Users-Gabriel-Documents-World-Stuff\memory"
if not os.path.isdir(M):
    M = r"C:\Users\Gabriel\.claude\projects\C--Users-Gabriel-Documents-World Stuff\memory"
print(M, os.path.isdir(M))
p = os.path.join(M, "feedback_scratchpad_location.md")
s = open(p, encoding="utf-8").read()
s = s.replace("working scripts live in the compendium's src/TEMP_scratchpad_recovery", "working scripts live in the compendium's src/tools")
s = s.replace("`HWFWM Compendium/src/TEMP_scratchpad_recovery` (the living scratchpad; rename allowed)",
              "`HWFWM Compendium/src/TEMP_scratchpad_recovery`, renamed on 2026-10-22 to `HWFWM Compendium/src/tools` (the living tools folder; see its README.md; retired scripts are in `src/tools/archive/`; chapter summaries are in `src/Chapter_Notes/`)")
s = s.replace("run and edit the helper scripts from `src/TEMP_scratchpad_recovery`", "run and edit the helper scripts in `src/tools` (they work from any directory)")
open(p, "w", encoding="utf-8").write(s)
p = os.path.join(M, "MEMORY.md")
s = open(p, encoding="utf-8").read().replace("use src/TEMP_scratchpad_recovery, never the old Gmod scratchpad", "use src/tools (renamed from TEMP_scratchpad_recovery), never the old Gmod scratchpad")
open(p, "w", encoding="utf-8").write(s)
print(open(p, encoding="utf-8").read())

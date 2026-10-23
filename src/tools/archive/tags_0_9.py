import os
B = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", ".."))


def edit(rel, pairs):
    p = os.path.join(B, rel)
    s = open(p, encoding="utf-8").read()
    for o, n in pairs:
        assert o in s, (rel, o[:50])
        s = s.replace(o, n, 1)
    open(p, "w", encoding="utf-8").write(s)


edit("00_Project_Structure.md", [(
    "When writing, put level-2 and level-3 facts in clearly marked sections (\"Later developments\") rather than in the main text.\n",
    """When writing, put level-2 and level-3 facts in clearly marked sections ("Later developments") rather than in the main text.

**Spoiler tags.** A document's header level (the first digit of its `Spoiler level:` line) is the level of its untagged text. A section that needs a higher level is wrapped in a pair of HTML comments, which do not render:

```
<!-- level:3 -->
## Later developments (spoilers)
...
<!-- /level -->
```

Rules: the level is 0-3; a tagged section may not be lower than the header level; tags may nest only when the inner level is at least the outer level; open and close tags must balance. Indexes and files whose header says "mixed" carry no tags. Use tags wherever a file mixes levels; a file whose header level already covers everything needs none. `src/tools/lint.py` checks the tags, and `src/tools/spoiler_tags.py` proposes tags for headings such as "Later developments" or "(Level N)" (the level of a "Later developments" section is taken from the latest book cited in it: Books 1-3 give 1, Books 4-9 give 2, Books 10-13 give 3). The planned export tool (build plan item 5.5) will keep a tagged section only when its level is at or below the level requested.
""")])
edit("src/tools/README.md", [("| `overviews.py` |", "| `spoiler_tags.py` | Spoiler-level tags: parses `<!-- level:N -->` ... `<!-- /level -->` sections, proposes tags for headings such as \"Later developments\" or \"(Level N)\" and, with `--write`, inserts them. `lint.py` uses its parser to check balance, levels and the header-level rule. |\n| `overviews.py` |")])
edit("TODO_Build_Plan.md", [("- **0.9 Spoiler tag syntax and linter support (suggested, M; decision 3).**", "- **0.9 (Done 2026-10-22) Spoiler tag syntax and linter support (suggested, M; decision 3).**")])
edit("Appendices/Change_Log.md", [("## Pending index updates", """**Spoiler tags, build plan item 0.9 (2026-10-22)**
- Defined the tag form (`<!-- level:N -->` ... `<!-- /level -->`) and its rules in section 6 of `00_Project_Structure.md`; added `src/tools/spoiler_tags.py` (parser, proposer, retrofitter) and linter checks for balance, invalid levels, nesting and the header-level rule (tested with a deliberately broken file).
- Retrofitted 21 sections in 15 files where the section level exceeded the header level: the primer (9.4, 9.5), the Cosmology overview, Gods_and_Churches (five god sections), Great_Astral_Beings, Awakening_Stones, Essences, Essence_Catalogue, Cults_and_Orders, Guilds_and_Houses, Magic_Society_and_Associations, Greenstone, Boko, the Astral overview, Spirit_Vault_and_Astral_Kingdom and Knowledge. Where a heading says \"Level 2/3\" or \"2-3\" the higher level is used.
- Not retrofitted: files whose header already covers all content, and files with mixed levels but no marked section (for example the 2026-10-22 character files, whose header carries the highest level they need). Those can be split into tagged sections later if a use appears; build plan item 5.5 depends on the tags.

## Pending index updates""")])
print("ok")

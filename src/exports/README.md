# Exports

Derived products. Nothing here is a source: never cite these files, and regenerate them from the compendium rather than editing them.

## lorebook/

Four world-info files for roleplay front ends (SillyTavern and Chub layout), one per spoiler level, made by `src/tools/lorebook.py`:

| File | Cleared to | Contents |
|---|---|---|
| `hwfwm_lorebook_level0.json` | public setting | documents with header level 0, tagged sections above level 0 cut |
| `hwfwm_lorebook_level1.json` | Books 1-3 | level 0-1 documents and sections |
| `hwfwm_lorebook_level2.json` | Books 1-9 | level 0-2 documents and sections |
| `hwfwm_lorebook_level3.json` | Books 1-13 | everything |

Each entry is one compendium document: its Summary and some fact bullets, about 1,500 characters at most, with citations removed. Keys are the document title and, for characters, the first and last name. `held_back.txt` lists the sentences left out of a lower-level file because they name a later book or a later-level term (some summaries are written at a lower header level than their last sentences); each is a candidate for a level tag in its document. The filter is a keyword list, so it is a safety net and not a guarantee: read an entry before giving a file to a table that has not read the later books.

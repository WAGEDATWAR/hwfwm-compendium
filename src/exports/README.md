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

## markdown/

One Markdown file per spoiler level, made by `src/tools/export_levels.py`: `HWFWM_Compendium_level0.md` (public setting, 70 documents), `level1` (Books 1-3, 147), `level2` (Books 1-9, 230) and `level3` (everything, 379). A document is kept when its header level is at or below the file's level, tagged sections above it are cut, and then any line that cites a later book or names a later-level term is held back (`held_back.txt`; none at level 3). The held-back step also removes some legitimate cited lines from the lower levels, so a level 0 or 1 file is thinner than its documents and is a handout, not a reference. Links between documents are reduced to their text. The exporter writes Markdown only; no PDF tool is installed here, so convert the Markdown if a PDF is needed.

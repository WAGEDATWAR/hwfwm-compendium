# Compendium tools

Scripts and data that build and check the compendium. This folder replaced `src/TEMP_scratchpad_recovery` on 2026-10-22. The old Gmod-Decompilation scratchpad must never be used. Run every tool from the compendium root, for example `python3 src/tools/rd.py r 1 1 1 5`; each tool finds its own data by path, so the working directory does not matter.

## Core tools

| Tool | What it does |
|---|---|
| `build_register.py` | Reads every compendium `.md` (except the generated and log files), grades each cited claim against `src/Source_Text/`, and writes `Appendices/Source_Register.md`, `Appendices/Source_Map.md` and `register_new.json`. Run after any document edit; it prints a delta line (rows added, removed, edited, regraded, newly weak) against the previous run and writes details to `src/tools/register_delta.md` (via `delta.py`). Reads `chapter_index.json`, `old_register.json` (hand notes carried over), `map_log.tsv`, `map_thread.tsv`, `map_thread_notes.md`. |
| `spoiler_tags.py` | Spoiler-level tags: parses `<!-- level:N -->` ... `<!-- /level -->` sections, proposes tags for headings such as "Later developments" or "(Level N)" and, with `--write`, inserts them. `lint.py` uses its parser to check balance, levels and the header-level rule. |
| `overviews.py` | Regenerates the file index inside each folder overview between the `files:start` and `files:end` markers; `--check` reports out-of-date lists. Runs inside `build_register.py`; `lint.py` fails when a list is stale. |
| `monster_scan.py` | Monster-rank scan (build plan item 2C.2): lists names that follow "<rank>-rank" in the chapter files, with first cite and context. Very noisy; used as a lead list only. Writes `monster_scan_report.md`. |
| `ess_lists.py` | Essence-name scan (build plan item 2C.1): finds essence names in list sentences ("A, B and C essences") and beside the word "essence" for wiki names, with first cite and a context line. Writes `ess_lists_report.md`; noisy, review each row against the line. |
| `name_scan.py` | Missing-name scan (build plan item 1.8): capitalised words that occur 15 or more times mid-sentence in the chapter files and are not covered in the compendium. `--index` counts a word as covered only if it is in the Name Index or Glossary; `--samples` prints a sample line. Writes `name_scan_report.md`. Re-run after each content tier. |
| `weak_dump.py` | Prints every weak register row with the text of the lines it cites, for tightening claims (build plan item 1.3). |
| `dossier.py` | `dossier.py "REGEX" N` samples narration, appearance and relationship lines mentioning a character per book band, with cites, for writing character files (build plan item 2E.4). |
| `delta.py` | Compares the previous and current register rows; used by `build_register.py`. Rows are matched on document and claim text; a removed and an added row that overlap by 45 percent count as an edit. |
| `lint.py` | Document linter. Checks headers (Status, Spoiler level, Valid from/through, Sources, Related), spoiler level values, that every `(Book N, ChX LY)` cite names a chapter and line that exist, that Related links resolve, cite format, leftover shorthand and folder-overview coverage. Writes `src/tools/lint_report.md`; also runs at the end of `build_register.py`. Target: zero errors and zero warnings. |
| `rd.py` | Read and search chapter text. `rd.py r BOOK CH LO HI WIDTH` prints lines; `rd.py g REGEX BOOK_FROM BOOK_TO WIDTH MAX` greps. |
| `who.py` | Samples every line that matches a name across all books: `who.py "REGEX" N` prints a count by book and N evenly spaced lines. |
| `cc2.py` | Citation checker: for each `(Book N, ChX LY)` cite in the given documents, reports claims whose terms overlap the cited lines below a threshold. `THR=0.30 python3 src/tools/cc2.py 01_World_Primer.md`. |
| `loc2.py` | Locator that ranks chapters for a description (`loc2.py BOOK SPECFILE`). |
| `chk.py` | Name checker: confirms that names occur near cited lines (`chk.py SPECFILE` with lines `name|book|chapter|line`). |
| `common.py` | Shared helpers (paths, chapter index, term overlap) used by `cc2.py` and `loc2.py`. |
| `mkchar.py`, `grplib.py` | Templates for writing a character file (`mk`) or a grouped minor-cast file (`grp`) in the standard layout. |
| `wiki_lists.py`, `compose_wiki.py` | Rebuild the wiki-tier lists in `03_Magic_and_Adventuring/Wiki_Reference_Lists.md` and the gods table in `02_Cosmology_and_Powers/Gods_and_Churches.md` from `wiki/pages.json`. |
| `fetchwiki.py` | Refreshes the fan-wiki cache in `wiki/` (ignored by git). |
| `ess_scan.py` | Counts "<name> essence" phrases in the chapter text. |

## Data in this folder

`chapter_index.json` (chapter titles and filenames), `old_register.json`, `map_log.tsv`, `map_thread.tsv`, `map_thread_notes.md` (inputs to the register and map), `register_new.json` (output), `wiki_*_table.md` (generated tables), `wiki/` (cached wiki pages; not committed).

## Related folders

- `src/Source_Text/`: the book text, one file per chapter. Not committed to git (copyright).
- `src/Chapter_Notes/`: the per-book chapter summaries (the "notes" tier), moved here from the old scratchpad.
- `archive/`: retired one-off scripts and intermediate files from earlier passes (document generators, audit scripts, lorebook builders, `hwfwm_lorebook.json`). Kept for reference only; they may reference paths that no longer exist.

## Conventions

- Cite as `(Book N, ChX LY)`. Mark other tiers `(notes, Book N)` and `(wiki)`.
- After a tool changes a document, run `build_register.py` and add a Change_Log entry.
- Scripts that write documents should be written to a file and run, not passed as shell heredocs, because apostrophes in the text break heredocs.

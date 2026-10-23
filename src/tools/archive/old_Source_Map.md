# Source Map

Status: Draft (framework and first harvest; all existing tier tags are registered, none yet re-read chapter by chapter)
Spoiler level: 3
Valid from: Book 1
Valid through: Book 13
Sources: `Source_Text/` chapter files; `Source_Register.md`
Related: Source_Register.md, ../Source_Text/README.md, ../08_History_and_Timeline/Master_Timeline.md, ../00_Project_Structure.md

## 1. Purpose

The Source Map ties compendium claims to book, chapter and lines so that facts can be traced, narrowed and re-checked, and so that changes over the series (a death, a gain, a loss, a change of allegiance) are recorded with the book where they happen. It is the working backbone for the Master Timeline and the character files.

## 2. How the pieces fit

- `Source_Text/Book_NN/Ch_NNN_Title.txt`: the book text, one file per chapter (index in `Source_Text/README.md`).
- `Appendices/Source_Register.md`: one row per tagged claim in the compendium (ID `R0001`...), with its location, location confidence and a state-change flag.
- This file: the rules, the log of narrowed results (section 4), the per-book change log harvested from the register (section 5), and the timeline thread (section 6).

## 3. Rules

1. Reference format: `B7 Ch31 L12-15` (book, chapter, lines of the chapter file).
2. Hierarchy stays Book Files > Chapter Summaries > Wiki. A register row whose tag is **notes** or **wiki** should be narrowed to a book location when possible; once it is, retag the claim in its document to "Book N".
3. Location grades: exact, probable, candidate, unlocated, **verified** (read at the lines and confirmed). Only verified rows count as settled references.
4. When a claim is narrowed, update its row in the register and add a line to section 4 below. When a document claim is added or changed, add or update its row the same session (section 10 of the structure document).
5. If the lines do not support the claim, mark the row **contradicted**, correct the document and log the correction in `Change_Log.md`.

## 4. Narrowing log

| Date | Register ID | Result | Note |
|---|---|---|---|
| 2026-10-21 | 02_Cosmology, 05_Organisations, 06_Places (all rows) | Every row read at its candidate lines | Cosmology 47 verified / 22 partial / 21 unlocated; Organisations 41 / 31 / 18; Places 14 / 17 / 23. Whole register: 221 verified, 177 partial, 206 unlocated, 35 not yet read (Primer, Timeline, Appendices). Open conflict: R0257 (B4 Ch2 L70-73) says only the owner may enter the Inventory space. |
| 2026-10-21 | 02_Cosmology, 05_Organisations, 06_Places (all rows) | Every row read at its candidate lines | Cosmology 47 verified / 22 partial / 21 unlocated; Organisations 41 / 31 / 18; Places 14 / 17 / 23. Whole register: 221 verified, 177 partial, 206 unlocated, 35 not yet read (Primer, Timeline, Appendices). Open conflict: R0257 (B4 Ch2 L70-73) says only the owner may enter the Inventory space. |
| 2026-10-21 | 01_Primer, 08_Timeline, Appendices; Spirit Vault rules | Remaining rows read; Inventory/Spirit Vault entry rules resolved | Whole register now: 240 verified, 187 partial, 212 unlocated (including multi-book tags), 0 automatic only. Resolved R0257: Inventory (B4 Ch2 L70) only Jason; Spirit Vault (B4 Ch57 L59) those who implicitly trust him, sealable; B5 Ch44 L44-45 who could enter; B6 Ch13 L79 gate admits those he allows. |
| 2026-10-21 | Unlocated rows | Hand-searched; 18 spoiler-level labels removed from the register; 41 claims retagged from Book N to notes, Book N because the book lines were not found | Whole register now: 259 verified, 242 partial, 120 unlocated. 33 more unlocated claims could not be retagged automatically (listed in TODO section H). Spirit Vault rules resolved (R0257). |
| 2026-10-21 | TODO section H (33 items) | Each item searched; claims found, retagged or corrected | 24 claims found in the chapter files (e.g. B3 Ch21 L60 Gary almost silver, B3 Ch29 L35 Path of Shadows regional gate, B12 Ch67 L65 seventeen years); 8 retagged to notes; Path of Shadows range in Jason_Asano.md corrected (the two-hundred-kilometre figure was not in the books). Register: 277 verified, 248 partial, 95 unlocated. |
| 2026-10-21 | TODO section H (33 items) | Each item searched; claims found, retagged or corrected | 24 claims found in the chapter files (e.g. B3 Ch21 L60 Gary almost silver, B3 Ch29 L35 Path of Shadows regional gate, B12 Ch67 L65 seventeen years); 8 retagged to notes; Path of Shadows range in Jason_Asano.md corrected (the two-hundred-kilometre figure was not in the books). Register: 278 verified, 248 partial, 94 unlocated. |
| 2026-10-21 | TODO section H (33 items) | Each item searched; claims found, retagged or corrected | 24 claims found in the chapter files (e.g. B3 Ch21 L60 Gary almost silver, B3 Ch29 L35 Path of Shadows regional gate, B12 Ch67 L65 seventeen years); 8 retagged to notes; Path of Shadows range in Jason_Asano.md corrected (the two-hundred-kilometre figure was not in the books). Register: 321 verified, 205 partial, 94 unlocated. |
| 2026-10-21 | TODO section H (33 items) | Each item searched; claims found, retagged or corrected | 24 claims found in the chapter files (e.g. B3 Ch21 L60 Gary almost silver, B3 Ch29 L35 Path of Shadows regional gate, B12 Ch67 L65 seventeen years); 8 retagged to notes; Path of Shadows range in Jason_Asano.md corrected (the two-hundred-kilometre figure was not in the books). Register: 345 verified, 182 partial, 93 unlocated. |
| 2026-10-21 | TODO section H (33 items) | Each item searched; claims found, retagged or corrected | 24 claims found in the chapter files (e.g. B3 Ch21 L60 Gary almost silver, B3 Ch29 L35 Path of Shadows regional gate, B12 Ch67 L65 seventeen years); 8 retagged to notes; Path of Shadows range in Jason_Asano.md corrected (the two-hundred-kilometre figure was not in the books). Register: 351 verified, 176 partial, 93 unlocated. |
| 2026-10-21 | TODO section H (33 items) | Each item searched; claims found, retagged or corrected | 24 claims found in the chapter files (e.g. B3 Ch21 L60 Gary almost silver, B3 Ch29 L35 Path of Shadows regional gate, B12 Ch67 L65 seventeen years); 8 retagged to notes; Path of Shadows range in Jason_Asano.md corrected (the two-hundred-kilometre figure was not in the books). Register: 428 verified, 99 partial, 93 unlocated. |
| 2026-10-21 | TODO section H (33 items) | Each item searched; claims found, retagged or corrected | 24 claims found in the chapter files (e.g. B3 Ch21 L60 Gary almost silver, B3 Ch29 L35 Path of Shadows regional gate, B12 Ch67 L65 seventeen years); 8 retagged to notes; Path of Shadows range in Jason_Asano.md corrected (the two-hundred-kilometre figure was not in the books). Register: 439 verified, 106 partial, 75 unlocated. |
| 2026-10-21 | TODO section H (33 items) | Each item searched; claims found, retagged or corrected | 24 claims found in the chapter files (e.g. B3 Ch21 L60 Gary almost silver, B3 Ch29 L35 Path of Shadows regional gate, B12 Ch67 L65 seventeen years); 8 retagged to notes; Path of Shadows range in Jason_Asano.md corrected (the two-hundred-kilometre figure was not in the books). Register: 442 verified, 110 partial, 68 unlocated. |
| 2026-10-21 | TODO section H (33 items) | Each item searched; claims found, retagged or corrected | 24 claims found in the chapter files (e.g. B3 Ch21 L60 Gary almost silver, B3 Ch29 L35 Path of Shadows regional gate, B12 Ch67 L65 seventeen years); 8 retagged to notes; Path of Shadows range in Jason_Asano.md corrected (the two-hundred-kilometre figure was not in the books). Register: 443 verified, 113 partial, 53 unlocated. |
| 2026-10-21 | TODO section H (33 items) | Each item searched; claims found, retagged or corrected | 24 claims found in the chapter files (e.g. B3 Ch21 L60 Gary almost silver, B3 Ch29 L35 Path of Shadows regional gate, B12 Ch67 L65 seventeen years); 8 retagged to notes; Path of Shadows range in Jason_Asano.md corrected (the two-hundred-kilometre figure was not in the books). Register: 458 verified, 113 partial, 26 unlocated. |
| 2026-10-21 | TODO section H (33 items) | Each item searched; claims found, retagged or corrected | 24 claims found in the chapter files (e.g. B3 Ch21 L60 Gary almost silver, B3 Ch29 L35 Path of Shadows regional gate, B12 Ch67 L65 seventeen years); 8 retagged to notes; Path of Shadows range in Jason_Asano.md corrected (the two-hundred-kilometre figure was not in the books). Register: 460 verified, 114 partial, 16 unlocated. |
| 2026-10-21 | TODO section H (33 items) | Each item searched; claims found, retagged or corrected | 24 claims found in the chapter files (e.g. B3 Ch21 L60 Gary almost silver, B3 Ch29 L35 Path of Shadows regional gate, B12 Ch67 L65 seventeen years); 8 retagged to notes; Path of Shadows range in Jason_Asano.md corrected (the two-hundred-kilometre figure was not in the books). Register: 460 verified, 114 partial, 16 unlocated. |
| 2026-10-21 | TODO section H (33 items) | Each item searched; claims found, retagged or corrected | 24 claims found in the chapter files (e.g. B3 Ch21 L60 Gary almost silver, B3 Ch29 L35 Path of Shadows regional gate, B12 Ch67 L65 seventeen years); 8 retagged to notes; Path of Shadows range in Jason_Asano.md corrected (the two-hundred-kilometre figure was not in the books). Register: 644 verified, 114 partial, 16 unlocated. |
| 2026-10-21 | TODO section H (33 items) | Each item searched; claims found, retagged or corrected | 24 claims found in the chapter files (e.g. B3 Ch21 L60 Gary almost silver, B3 Ch29 L35 Path of Shadows regional gate, B12 Ch67 L65 seventeen years); 8 retagged to notes; Path of Shadows range in Jason_Asano.md corrected (the two-hundred-kilometre figure was not in the books). Register: 786 verified, 114 partial, 16 unlocated. |
| 2026-10-21 | TODO section H (33 items) | Each item searched; claims found, retagged or corrected | 24 claims found in the chapter files (e.g. B3 Ch21 L60 Gary almost silver, B3 Ch29 L35 Path of Shadows regional gate, B12 Ch67 L65 seventeen years); 8 retagged to notes; Path of Shadows range in Jason_Asano.md corrected (the two-hundred-kilometre figure was not in the books). Register: 851 verified, 114 partial, 16 unlocated. |
| 2026-10-21 | TODO section H (33 items) | Each item searched; claims found, retagged or corrected | 24 claims found in the chapter files (e.g. B3 Ch21 L60 Gary almost silver, B3 Ch29 L35 Path of Shadows regional gate, B12 Ch67 L65 seventeen years); 8 retagged to notes; Path of Shadows range in Jason_Asano.md corrected (the two-hundred-kilometre figure was not in the books). Register: 924 verified, 114 partial, 16 unlocated. |
| 2026-10-21 | TODO section H (33 items) | Each item searched; claims found, retagged or corrected | 24 claims found in the chapter files (e.g. B3 Ch21 L60 Gary almost silver, B3 Ch29 L35 Path of Shadows regional gate, B12 Ch67 L65 seventeen years); 8 retagged to notes; Path of Shadows range in Jason_Asano.md corrected (the two-hundred-kilometre figure was not in the books). Register: 1001 verified, 124 partial, 16 unlocated. |
| 2026-10-21 | TODO section H (33 items) | Each item searched; claims found, retagged or corrected | 24 claims found in the chapter files (e.g. B3 Ch21 L60 Gary almost silver, B3 Ch29 L35 Path of Shadows regional gate, B12 Ch67 L65 seventeen years); 8 retagged to notes; Path of Shadows range in Jason_Asano.md corrected (the two-hundred-kilometre figure was not in the books). Register: 1081 verified, 38 partial, 16 unlocated. |
| 2026-10-21 | TODO section H (33 items) | Each item searched; claims found, retagged or corrected | 24 claims found in the chapter files (e.g. B3 Ch21 L60 Gary almost silver, B3 Ch29 L35 Path of Shadows regional gate, B12 Ch67 L65 seventeen years); 8 retagged to notes; Path of Shadows range in Jason_Asano.md corrected (the two-hundred-kilometre figure was not in the books). Register: 1087 verified, 10 partial, 16 unlocated. |
| 2026-10-21 | TODO section H (33 items) | Each item searched; claims found, retagged or corrected | 24 claims found in the chapter files (e.g. B3 Ch21 L60 Gary almost silver, B3 Ch29 L35 Path of Shadows regional gate, B12 Ch67 L65 seventeen years); 8 retagged to notes; Path of Shadows range in Jason_Asano.md corrected (the two-hundred-kilometre figure was not in the books). Register: 1096 verified, 0 partial, 16 unlocated. |
| 2026-10-21 | TODO section H (33 items) | Each item searched; claims found, retagged or corrected | 24 claims found in the chapter files (e.g. B3 Ch21 L60 Gary almost silver, B3 Ch29 L35 Path of Shadows regional gate, B12 Ch67 L65 seventeen years); 8 retagged to notes; Path of Shadows range in Jason_Asano.md corrected (the two-hundred-kilometre figure was not in the books). Register: 1125 verified, 0 partial, 0 unlocated. |
| 2026-10-21 | TODO section H (33 items) | Each item searched; claims found, retagged or corrected | 24 claims found in the chapter files (e.g. B3 Ch21 L60 Gary almost silver, B3 Ch29 L35 Path of Shadows regional gate, B12 Ch67 L65 seventeen years); 8 retagged to notes; Path of Shadows range in Jason_Asano.md corrected (the two-hundred-kilometre figure was not in the books). Register: 1272 verified, 0 partial, 0 unlocated. |
| 2026-10-21 | TODO section H (33 items) | Each item searched; claims found, retagged or corrected | 24 claims found in the chapter files (e.g. B3 Ch21 L60 Gary almost silver, B3 Ch29 L35 Path of Shadows regional gate, B12 Ch67 L65 seventeen years); 8 retagged to notes; Path of Shadows range in Jason_Asano.md corrected (the two-hundred-kilometre figure was not in the books). Register: 1272 verified, 0 partial, 0 unlocated. |
| 2026-10-21 | TODO section H (33 items) | Each item searched; claims found, retagged or corrected | 24 claims found in the chapter files (e.g. B3 Ch21 L60 Gary almost silver, B3 Ch29 L35 Path of Shadows regional gate, B12 Ch67 L65 seventeen years); 8 retagged to notes; Path of Shadows range in Jason_Asano.md corrected (the two-hundred-kilometre figure was not in the books). Register: 1323 verified, 1 partial, 0 unlocated. |
| 2026-10-21 | TODO section H (33 items) | Each item searched; claims found, retagged or corrected | 24 claims found in the chapter files (e.g. B3 Ch21 L60 Gary almost silver, B3 Ch29 L35 Path of Shadows regional gate, B12 Ch67 L65 seventeen years); 8 retagged to notes; Path of Shadows range in Jason_Asano.md corrected (the two-hundred-kilometre figure was not in the books). Register: 1324 verified, 0 partial, 0 unlocated. |
| 2026-10-21 | TODO section H (33 items) | Each item searched; claims found, retagged or corrected | 24 claims found in the chapter files (e.g. B3 Ch21 L60 Gary almost silver, B3 Ch29 L35 Path of Shadows regional gate, B12 Ch67 L65 seventeen years); 8 retagged to notes; Path of Shadows range in Jason_Asano.md corrected (the two-hundred-kilometre figure was not in the books). Register: 1363 verified, 0 partial, 0 unlocated. |
| 2026-10-21 | TODO section H (33 items) | Each item searched; claims found, retagged or corrected | 24 claims found in the chapter files (e.g. B3 Ch21 L60 Gary almost silver, B3 Ch29 L35 Path of Shadows regional gate, B12 Ch67 L65 seventeen years); 8 retagged to notes; Path of Shadows range in Jason_Asano.md corrected (the two-hundred-kilometre figure was not in the books). Register: 1448 verified, 2 partial, 0 unlocated. |
| 2026-10-21 | TODO section H (33 items) | Each item searched; claims found, retagged or corrected | 24 claims found in the chapter files (e.g. B3 Ch21 L60 Gary almost silver, B3 Ch29 L35 Path of Shadows regional gate, B12 Ch67 L65 seventeen years); 8 retagged to notes; Path of Shadows range in Jason_Asano.md corrected (the two-hundred-kilometre figure was not in the books). Register: 1448 verified, 2 partial, 0 unlocated. |
| 2026-10-21 | TODO section H (33 items) | Each item searched; claims found, retagged or corrected | 24 claims found in the chapter files (e.g. B3 Ch21 L60 Gary almost silver, B3 Ch29 L35 Path of Shadows regional gate, B12 Ch67 L65 seventeen years); 8 retagged to notes; Path of Shadows range in Jason_Asano.md corrected (the two-hundred-kilometre figure was not in the books). Register: 1578 verified, 3 partial, 0 unlocated. |
| 2026-10-21 | TODO section H (33 items) | Each item searched; claims found, retagged or corrected | 24 claims found in the chapter files (e.g. B3 Ch21 L60 Gary almost silver, B3 Ch29 L35 Path of Shadows regional gate, B12 Ch67 L65 seventeen years); 8 retagged to notes; Path of Shadows range in Jason_Asano.md corrected (the two-hundred-kilometre figure was not in the books). Register: 1581 verified, 0 partial, 0 unlocated. |
| 2026-10-21 | TODO section H (33 items) | Each item searched; claims found, retagged or corrected | 24 claims found in the chapter files (e.g. B3 Ch21 L60 Gary almost silver, B3 Ch29 L35 Path of Shadows regional gate, B12 Ch67 L65 seventeen years); 8 retagged to notes; Path of Shadows range in Jason_Asano.md corrected (the two-hundred-kilometre figure was not in the books). Register: 1635 verified, 2 partial, 0 unlocated. |
| 2026-10-21 | TODO section H (33 items) | Each item searched; claims found, retagged or corrected | 24 claims found in the chapter files (e.g. B3 Ch21 L60 Gary almost silver, B3 Ch29 L35 Path of Shadows regional gate, B12 Ch67 L65 seventeen years); 8 retagged to notes; Path of Shadows range in Jason_Asano.md corrected (the two-hundred-kilometre figure was not in the books). Register: 1637 verified, 0 partial, 0 unlocated. |
| 2026-10-21 | TODO section H (33 items) | Each item searched; claims found, retagged or corrected | 24 claims found in the chapter files (e.g. B3 Ch21 L60 Gary almost silver, B3 Ch29 L35 Path of Shadows regional gate, B12 Ch67 L65 seventeen years); 8 retagged to notes; Path of Shadows range in Jason_Asano.md corrected (the two-hundred-kilometre figure was not in the books). Register: 2485 verified, 7 partial, 0 unlocated. |
| 2026-10-21 | TODO section H (33 items) | Each item searched; claims found, retagged or corrected | 24 claims found in the chapter files (e.g. B3 Ch21 L60 Gary almost silver, B3 Ch29 L35 Path of Shadows regional gate, B12 Ch67 L65 seventeen years); 8 retagged to notes; Path of Shadows range in Jason_Asano.md corrected (the two-hundred-kilometre figure was not in the books). Register: 3419 verified, 18 partial, 0 unlocated. |
| 2026-10-21 | TODO section H (33 items) | Each item searched; claims found, retagged or corrected | 24 claims found in the chapter files (e.g. B3 Ch21 L60 Gary almost silver, B3 Ch29 L35 Path of Shadows regional gate, B12 Ch67 L65 seventeen years); 8 retagged to notes; Path of Shadows range in Jason_Asano.md corrected (the two-hundred-kilometre figure was not in the books). Register: 3437 verified, 0 partial, 0 unlocated. |
| 2026-10-21 | TODO section H (33 items) | Each item searched; claims found, retagged or corrected | 24 claims found in the chapter files (e.g. B3 Ch21 L60 Gary almost silver, B3 Ch29 L35 Path of Shadows regional gate, B12 Ch67 L65 seventeen years); 8 retagged to notes; Path of Shadows range in Jason_Asano.md corrected (the two-hundred-kilometre figure was not in the books). Register: 3437 verified, 0 partial, 0 unlocated. |
| 2026-10-21 | TODO section H (33 items) | Each item searched; claims found, retagged or corrected | 24 claims found in the chapter files (e.g. B3 Ch21 L60 Gary almost silver, B3 Ch29 L35 Path of Shadows regional gate, B12 Ch67 L65 seventeen years); 8 retagged to notes; Path of Shadows range in Jason_Asano.md corrected (the two-hundred-kilometre figure was not in the books). Register: 3437 verified, 0 partial, 0 unlocated. |
| 2026-10-21 | TODO section H (33 items) | Each item searched; claims found, retagged or corrected | 24 claims found in the chapter files (e.g. B3 Ch21 L60 Gary almost silver, B3 Ch29 L35 Path of Shadows regional gate, B12 Ch67 L65 seventeen years); 8 retagged to notes; Path of Shadows range in Jason_Asano.md corrected (the two-hundred-kilometre figure was not in the books). Register: 4250 verified, 42 partial, 0 unlocated. |
| 2026-10-21 | TODO section H (33 items) | Each item searched; claims found, retagged or corrected | 24 claims found in the chapter files (e.g. B3 Ch21 L60 Gary almost silver, B3 Ch29 L35 Path of Shadows regional gate, B12 Ch67 L65 seventeen years); 8 retagged to notes; Path of Shadows range in Jason_Asano.md corrected (the two-hundred-kilometre figure was not in the books). Register: 4292 verified, 0 partial, 0 unlocated. |
| 2026-10-21 | TODO section H (33 items) | Each item searched; claims found, retagged or corrected | 24 claims found in the chapter files (e.g. B3 Ch21 L60 Gary almost silver, B3 Ch29 L35 Path of Shadows regional gate, B12 Ch67 L65 seventeen years); 8 retagged to notes; Path of Shadows range in Jason_Asano.md corrected (the two-hundred-kilometre figure was not in the books). Register: 4257 verified, 0 partial, 0 unlocated. |
| 2026-10-20 | 07_Characters, 03_Magic (all rows) | Every row read at its candidate lines | Characters and Magic rows: 116 verified, 106 partial, 144 unlocated after reading, 0 not yet read (multi-book or table rows). Whole register: 145 verified, 112 partial, 144 unlocated, 84 probable, 127 candidate, 27 exact. |
| 2026-10-20 | R0017-R0620 (state-change rows) | 64 rows read at the lines | 44 verified, 20 partial, 0 mismatch (R0361 resolved: the quote is B8 Ch4 L116). Unlocated after reading: R0147, R0207, R0272, R0309, R0321, R0354-R0355, R0476, R0479, R0527, R0603, R0610-R0611. |
| 2026-10-20 | (anchors) | Timeline anchors located | 30 anchors read at the lines; see section 6. Asano Village build time not found. |
| 2026-10-20 | (all) | Register created | 639 rows harvested automatically from existing tags; none yet marked verified. |

## 5. Change log by book (state changes harvested from the register)

Candidate entries: each is a claim flagged as a gain, loss, death, birth, move or change. Only rows whose confidence is **verified** have been read at the cited lines; the others still need a chapter read before the order is treated as settled.

### Book 1

| Chapter | Subject (document) | Change | Reference | ID | Conf. |
|---|---|---|---|---|---|
| Ch1 | Jason Asano | Books 7-9 (level 2) : returns to Pallimustus as the great surge begins; the One Day War; becomes an astral king ; the Battle of Yaresh; takes in messe | B1 Ch1 L8-10 | R0490 | verified |
| Ch8 | Jason Asano | Books 12-13 (level 3) : a gold-rank "prime avatar of an astral nexus" who returns to Earth in 2038. | B1 Ch8 L37-37 | R0491 | verified |
| Ch11 | Sophie Wexler | Her mother is Melody Jain , who faked her death some twenty years earlier . | B1 Ch11 L49-49 | R0552 | verified |
| Ch11 | Sophie Wexler | Her mother is Melody Jain , who faked her death some twenty years earlier . | B1 Ch11 L51-51 | R0553 | verified |
| Ch22 | Adventure Society | Restricted essences : Rufus says Death is restricted by itself , and the Magic Society's living document shows one restricted combination, the Succubu | B1 Ch22 L55-60 | R0119 | verified |
| Ch23 | Humphrey Geller | Essences : the dragon confluence, reached through the might and wing essences . | B1 Ch23 L15-17 | R0439 | verified |
| Ch31 | Adventure Society | Restricted essences : Rufus says Death is restricted by itself , and the Magic Society's living document shows one restricted combination, the Succubu | B1 Ch31 L100-100 | R0118 | verified |
| Ch38 | Jason Asano | At the end of Book 13 Umber's ritual is designed to bind his consciousness into the prime avatar, and Jason walks to the standing stones knowingly, pr | B1 Ch38 L55-55 | R0496 | verified |
| Ch39 | Zara Rimaros | Firstborn daughter of the Storm King, called the Hurricane Princess ; her brother Emiliano becomes Storm King, and the notes for Book 13 call him her  | B1 Ch39 L119-123 | R0566 | verified |
| Ch43 | Zara Rimaros | Book 12 : meets Jason again after fifteen years ; has joined Team Biscuit . | B1 Ch43 L18-18 | R0574 | verified |
| Ch45 | Casselton and Asano Village | The long passage ends at Jason's cloud house, which sits at the bottom of the sea about two kilometres out, reached by a hidden tram . | B1 Ch45 L4-5 | R0239 | verified |
| Ch54 | Cults and Orders | Shade explains that the churches, locked out of the sealed astral space, made a second bargain with the vorger, deep-astral entities that can violate  | B1 Ch54 L35-35 | R0126 | verified |
| Ch54 | Earth Powers | The notes for Book 13 add that the founder returned to Earth with magic bargained from messengers, created the Network's secret societies and the Grid | B1 Ch54 L35-35 | R0143 | verified |
| Ch68 | Dawn | Book 6 : arrives in her true body to negotiate with the Builder after Shako kills Jason . | B1 Ch68 L94-94 | R0335 | verified |
| Ch85 | Dawn | Jason kills and loots one . | B1 Ch85 L51-51 | R0324 | verified |
| Ch99 | Knowledge | Jason's last word to her: "The next time we meet, Goddess, will be the day you die" . | B1 Ch99 L67-70 | R0501 | verified |
| Ch102 | Artefact Site One | The notes for Book 12 mark the Sky Link island as a place the team visits, and the notes for Book 13 say the Church of Knowledge annexed the island th | B1 Ch102 L11-11 | R0235 | verified |

### Book 2

| Chapter | Subject (document) | Change | Reference | ID | Conf. |
|---|---|---|---|---|---|
| Ch5 | Master Timeline | Roughly 500 years ago  : a new kind of magic appears on Earth and is collected into secret societies; the Network's founder, an Earth-born outworlder, | B2 Ch5 L82-87 | R0578 | verified |
| Ch22 | Dawn | Book 5 : arrives at Asano Village in a new avatar; explains the danger of transformation zones as dimensional ulceration; tells him the Reaper offered | B2 Ch22 L127-129 | R0334 | verified |
| Ch25 | Cults and Orders | The notes record that the Order were royal assassins (a knife in the dark for fool or mad rulers) and hunters of undead and of the Unliving church's n | B2 Ch25 L53-53 | R0127 | verified |
| Ch28 | Adventure Society | It serves as identification, lets the holder copy a notice by touching the medallion to it and then to a blank sheet , and lets the Society track kill | B2 Ch28 L56-56 | R0110 | verified |
| Ch32 | Clive Standish | Familiar : Onslow, a rune tortoise who sits at the prow of the airboat, carries Clive, and becomes a runic tattoo on his torso when called back . | B2 Ch32 L72-72 | R0296 | verified |
| Ch44 | Earth Powers | Reach : took Perth, then Melbourne, then moved on Sydney . | B2 Ch44 L72-78 | R0164 | verified |
| Ch45 | Master Timeline | Jason left Earth in  late November  and returned in  early June, a year and a half later   [book] . | B2 Ch45 L69-72 | R0576 | verified |
| Ch61 | Gary | In Book 6 he meets the gold-rank smith Virid Martine, who becomes his master . | B2 Ch61 L147-147 | R0429 | verified |
| Ch64 | Sophie Wexler | Racial gifts  (celestine): Mana Integrity evolves into Mana Wellspring , Astral Affinity into Boundary Breaker, which removes the damage reduction fro | B2 Ch64 L55-55 | R0546 | verified |
| Ch70 | Cults and Orders | The last grandmaster  : when the churches found the training facilities beneath Sky Scar Lake, the last grandmaster sent the initiates into a sealed a | B2 Ch70 L34-42 | R0128 | verified |
| Ch72 | Farrah Hurin | Rank : silver in Book 4 or 5; in Book 12 she is offered the choice of becoming a Voice of the Will or a Defier of the Will ; she accepts and becomes t | B2 Ch72 L15-15 | R0408 | verified |

### Book 3

| Chapter | Subject (document) | Change | Reference | ID | Conf. |
|---|---|---|---|---|---|
| Ch2 | Jason Asano | Level 2 : he has died four times by Book 6 (the Church of Death's certificate, Book 7; the card in Book 10); he is an astral king . | B3 Ch2 L64-64 | R0493 | verified |
| Ch4 | Gary | His characteristic line when facing death: "I don't want to be a ghost, rattling around in a hole" . | B3 Ch4 L28-32 | R0418 | verified |
| Ch4 | Sophie Wexler | Racial gifts  (celestine): Mana Integrity evolves into Mana Wellspring , Astral Affinity into Boundary Breaker, which removes the damage reduction fro | B3 Ch4 L29-32 | R0547 | verified |
| Ch31 | Earth Powers | A "former Mrs South" gave the Network information about the necromancer , so she left the EOA. | B3 Ch31 L25-27 | R0161 | verified |
| Ch34 | Casselton and Asano Village | Spoiler level: 1 for Casselton ; 2 for the Asano Village build; 3 for the later seizure and return | B3 Ch34 L60-60 | R0237 | verified |
| Ch49 | Master Timeline | (Level 3)  The notes for Book 13 add that the founder returned to Earth with magic bargained from messengers, built the secret societies and the Grid  | B3 Ch49 L15-15 | R0580 | verified |
| Ch68 | Master Timeline | Departure : Jason makes his farewells in France on a  warm autumn day   [book]  and leaves Earth with Farrah by the ritual circle at the Australian st | B3 Ch68 L14-15 | R0583 | verified |
| Ch69 | Emi and Nik | By Book 13 he has mapping powers more precise than Jason's tactical map and can relay powers and devices remotely; he wears a straw hat with ear holes | B3 Ch69 L1036-1040 | R0359 | verified |
| Ch69 | Familiars | He was the summoned familiar of the Order of the Reaper's last grandmaster, an outworlder with the dark essence, before he became Jason's . | B3 Ch69 L1036-1040 | R0365 | verified |

### Book 5

| Chapter | Subject (document) | Change | Reference | ID | Conf. |
|---|---|---|---|---|---|
| Ch5 | Humphrey Geller | Racial gift : his human gift Special Attack Affinity evolves into Attack of the Mirage Dragon (an illusory double of his attacks, Book 2) and later in | B5 Ch5 L83-89 | R0442 | verified |
| Ch16 | Farrah Hurin | Rank : silver in Book 4 or 5; in Book 12 she is offered the choice of becoming a Voice of the Will or a Defier of the Will ; she accepts and becomes t | B5 Ch16 L103-108 | R0407 | verified |

### Book 6

| Chapter | Subject (document) | Change | Reference | ID | Conf. |
|---|---|---|---|---|---|
| Ch18 | Familiars | Evolution (Level 3) : "Shadow of the Reaper [Shade] has sanctioned himself" and becomes a Shadow of the Hegemon . | B6 Ch18 L3-9 | R0372 | verified |
| Ch25 | 00 Places Overview | Hornis  is a port to the south, reached from Greenstone across the delta and the Veldt . | B6 Ch25 L98-99 | R0198 | verified |
| Ch47 | Clive Standish | A lecturer who loses the thread and apologises ("Sorry, where were we?", Book 1); he wants dumpling soup in the middle of his own lecture on the cosmo | B6 Ch47 L16-18 | R0286 | verified |

### Book 7

| Chapter | Subject (document) | Change | Reference | ID | Conf. |
|---|---|---|---|---|---|
| Ch6 | Clive Standish | Familiar : Onslow, a rune tortoise who sits at the prow of the airboat, carries Clive, and becomes a runic tattoo on his torso when called back . | B7 Ch6 L42-42 | R0297 | verified |
| Ch17 | Gods and Churches | Death certification : the Church of Death certifies deaths; in Book 7 an official is shown a certification that Jason has died four times "so far", an | B7 Ch17 L104-105 | R0056 | verified |
| Ch43 | Emi and Nik | He is "the key" Jason made to the zone's control network; his control knowledge returns when Jason rebuilds the cloud-house mesa from his memories . | B7 Ch43 L58-62 | R0356 | verified |

### Book 8

| Chapter | Subject (document) | Change | Reference | ID | Conf. |
|---|---|---|---|---|---|
| Ch49 | Great Astral Beings | Book 8 settlement : the Fundamental Realm Authority Token is returned in the deal that sees the Builder end his invasion of Pallimustus . | B8 Ch49 L89-91 | R0098 | verified |
| Ch50 | Astral Kings and Messengers | After the Astral Throne and Astral Gate appear , Jason's spirit realm becomes an astral kingdom. | B8 Ch50 L46-50 | R0038 | verified |

### Book 9

| Chapter | Subject (document) | Change | Reference | ID | Conf. |
|---|---|---|---|---|---|
| Ch29 | Artefact Site One | The notes for Book 12 mark the Sky Link island as a place the team visits, and the notes for Book 13 say the Church of Knowledge annexed the island th | B9 Ch29 L17-17 | R0236 | verified |
| Ch48 | Master Timeline | He was  23  at arrival  [book] ,  29  in Book 10  [book] , and was  born forty-four years before  the Earth scenes of Books 12-13  [book] . | B9 Ch48 L12-12 | R0577 | verified |

### Book 10

| Chapter | Subject (document) | Change | Reference | ID | Conf. |
|---|---|---|---|---|---|
| Ch33 | Farrah Hurin | Books 5-6 : builds the family compound's infrastructure and the Grid repairs, helps destroy a vampire hub, leaves Earth with Jason; of her captor Adri | B10 Ch33 L109-109 | R0411 | verified |
| Ch38 | Gods and Churches | Death certification : the Church of Death certifies deaths; in Book 7 an official is shown a certification that Jason has died four times "so far", an | B10 Ch38 L73-73 | R0057 | verified |
| Ch39 | Gods and Churches | Book 10 states that the Order of Redeeming Light was created by Disguise, a god masquerading as Purity: its Flames of Redemption are an extreme modifi | B10 Ch39 L46-49 | R0063 | verified |
| Ch82 | Gods and Churches | The goddess of death appears to Jason in the Cardinas death chamber as "a stocky, middle-aged woman with a colourful dress" with the warmth of "a matr | B10 Ch82 L62-62 | R0071 | verified |
| Ch83 | Gods and Churches | In return he gains the title Keeper of the Cycle: abilities that apply afflictions also apply ghost fire, mana drain degrades the animating force of u | B10 Ch83 L75-78 | R0072 | verified |

### Book 11

| Chapter | Subject (document) | Change | Reference | ID | Conf. |
|---|---|---|---|---|---|
| Ch8 | Sophie Wexler | Her mother is Melody Jain , who faked her death some twenty years earlier . | B11 Ch8 L23-24 | R0550 | verified |
| Ch8 | Familiars | Special attack : Humphrey's racial ability evolves into Attack of the Mirage Dragon . | B11 Ch8 L102-102 | R0392 | verified |
| Ch33 | 00 Cosmology Overview | Clive teaches that authority is the highest order of magic: the magic gods use for miracles and GABs use to regulate the mechanics of the cosmos, such | B11 Ch33 L112-112 | R0017 | verified |
| Ch57 | Jason Asano | At gold his "strange, nebulous eyes" draw attention, though they return to the dark eyes he had at iron when he meets Zara . | B11 Ch57 L60-60 | R0455 | verified |
| Ch65 | 00 Cosmology Overview | The notes describe the nameless as great astral beings who are functionaries of cosmic mechanics (life, death, time, matter), unbound without the thro | B11 Ch65 L57-61 | R0024 | verified |
| Ch65 | Great Astral Beings | The notes describe the nameless as functionaries of cosmic mechanics (life, death, time, matter), unbound without the throne . | B11 Ch65 L57-61 | R0091 | verified |
| Ch67 | Gods and Churches | Carlos Quilido is a Healer priest who joins the Cardinas expedition . | B11 Ch67 L6-6 | R0061 | verified |
| Ch68 | Danielle Geller | Book 1 : investigates Jason at Gabriel Remore's request and learns he is an outworlder ; leads the Greenstone expedition into the desert astral space, | B11 Ch68 L305-305 | R0318 | verified |
| Ch68 | Farrah Hurin | Pretty, with strawberry-blonde hair, a button nose and light skin, "startlingly cute" and clearly unhappy when freed from her cage . | B11 Ch68 L1104-1106 | R0394 | verified |

### Book 12

| Chapter | Subject (document) | Change | Reference | ID | Conf. |
|---|---|---|---|---|---|
| Ch3 | Magic Society and Associations | Behaviour  : the Society leverages its research and secrets for political power; many prominent academics stay with it for personal gain. | B12 Ch3 L3-8 | R0183 | verified |
| Ch6 | Gods and Churches | In Book 12 Gordon suggests asking Death to return the resurrection power Jason gave away . | B12 Ch6 L18-22 | R0073 | verified |
| Ch15 | Sophie Wexler | Her mother is Melody Jain , who faked her death some twenty years earlier . | B12 Ch15 L8-9 | R0551 | verified |
| Ch26 | Emi and Nik | By Book 13 he has mapping powers more precise than Jason's tactical map and can relay powers and devices remotely; he wears a straw hat with ear holes | B12 Ch26 L54-54 | R0358 | verified |
| Ch29 | Incursion Sites | The same effect returns in later books, including the Cardinas expedition , where it is again a beautiful and terrible wave. | B12 Ch29 L59-60 | R0240 | verified |
| Ch67 | Astral Kings and Messengers | Birth : Jason says messengers are "budded, not born" and are "actually plants, which is kind of crazy" . | B12 Ch67 L23-23 | R0046 | verified |

### Book 13

| Chapter | Subject (document) | Change | Reference | ID | Conf. |
|---|---|---|---|---|---|
| Ch954 | Danielle Geller | Book 1 : investigates Jason at Gabriel Remore's request and learns he is an outworlder ; leads the Greenstone expedition into the desert astral space, | B13 Ch954 L5-6 | R0317 | verified |
| Ch1001 | Cults and Orders | What it was  : an ancient cult of assassins who venerated the Reaper, "the finality of death". | B13 Ch1001 L9-9 | R0123 | verified |
| Ch1001 | Cults and Orders | What it was  : an ancient cult of assassins who venerated the Reaper, "the finality of death". | B13 Ch1001 L9-9 | R0124 | verified |
| Ch1016 | Knowledge | In Book 1 a statue is replaced by a woman with colourful clothes and Mediterranean features, beautiful yet "detached and untouchable", not holding the | B13 Ch1016 L21-21 | R0497 | verified |
| Ch1017 | Gods and Churches | Knowledge interfered; and a relic of Purity's divine power was left behind . | B13 Ch1017 L16-24 | R0065 | verified |
| Ch1023 | Gods and Churches | When Gabrielle Pellin refuses to believe it, a cube leaves her chest into Knowledge's hand, Gabrielle seizes, and Travis catches her . | B13 Ch1023 L139-139 | R0069 | verified |
| Ch1024 | Gods and Churches | Jason answers Knowledge's claim that she will be "the one true God" of his world with "The next time we meet, Goddess, will be the day you die" . | B13 Ch1024 L153-153 | R0070 | verified |

## 6. Timeline thread

The Master Timeline (`08_History_and_Timeline/Master_Timeline.md`) should be rebuilt as an ordered thread of register IDs: every dated or ordered event gets a row here with book, chapter and lines, so the order within a book follows chapter order and cross-book intervals can be checked against the cited lines. Anchors already established in the Master Timeline are to be located first (this has not yet been done):

- Jason's birthday (1 April 1994) and the arrival in late November 2017.
- Return to Earth in early June 2019; the April 2020 birthday; departure from Earth in autumn 2021; Book 13 in 2038.
- The Book 7 statement that the surge was "some five years overdue" (Book 7; register entry in `01_World_Primer.md`).

| Event | Date or interval | Reference | Status |
|---|---|---|---|
| Jason's age at arrival | 23 | B1 Ch25 L43; B13 Ch950 L29 ("the age Jason had been when he was pulled into Pallimustus") | verified |
| Jason leaves Earth / returns | late November; early June, "a year and a half later" | B4 Ch3 L112 | verified |
| Jason's birthday | 1 April ("April Fool's Day"); just turned 26, birthday "last week" | B5 Ch20 L24-26 | verified |
| "You come back ten months ago" | Jeremy, about April 2020 | B5 Ch24 L61 | verified |
| Jason's age in Book 10 | 29 | B10 Ch33 L76 | verified |
| Jason born on Earth forty-four years before the Book 12 scenes; no fighter twenty years ago | 44 / 20 years | B12 Ch67 L113 | verified |
| Book 13 year | 2038 ("in 2038") | B13 Ch951 L50 | verified |
| Transformation-zone events "like those in 2020" | 2020 | B13 Ch964 L41 | verified |
| Magic unknown "less than fifteen years ago"; Jason absent "sixteen years" | about 15-16 years | B12 Ch2 L107; B13 Ch972 L51, L61 | verified |
| Pallimustus calendar: twelve months of thirty days plus five extra days | calendar | B1 Ch22 L19 | verified |
| Monster surge every ten years; current surge "some five years overdue" | 10 / 5 years | B1 Ch31 L71; B7 Ch1 L56 | verified |
| Network publicly known as the Global Defense Network "in the weeks since the monster waves began" | spring 2020 | B5 Ch17 L7 | verified |
| Broken Hill: estimated ten to fifteen thousand dead; over nineteen thousand survivors | spring 2020 | B5 Ch18 L83; B5 Ch21 L101 | verified |
| Makassar: one and a half million people, category-three space | after the birthday | B5 Ch25 L82 | verified |
| Kostroma sealed in a dome (first transformation zone) | Book 5 | B5 Ch44 L48-49 | verified |
| Dimensional spaces last forty-three hours (record fifty-one) | baseline | B4 Ch37 L70; B4 Ch5 L127 | verified |
| EOA seized Perth and Melbourne | before B4 | B4 Ch9 L76 | verified (Sydney: still to locate) |
| Cold winter day in Europe (atomic device) | Book 6 | B6 Ch31 L4 | verified |
| Farewell in France on a warm autumn day | autumn 2021 by anchors | B6 Ch47 L155 | verified |
| "It had been a month since" the One Day War | after the war | B7 Ch66 L27 | verified |
| 119 outworlders arrive at once | Book 7 | B7 Ch36 L86 | verified |
| Ustei came south "three years, give or take" before the Earthlings | about 2018 vs 2021 | B12 Ch30 L9 | verified |
| 419 time-displaced priests released | M5 | B2 Ch63 L9 | verified |
| Reaper-trial space: twelve towers, eight kilometres apart | M12 (wiki) | B3 Ch36 L36 | verified |
| Winter in Greenstone at the start of Book 3 | southern winter 2018 | B3 Ch1 L14 | verified |
| Summer moving into autumn before the Leust conspiracy | about Feb-Mar 2018 | B1 Ch93 L5 | verified |
| Earth and Pallimustus time synchronised | | B11 Ch63 L80 | verified |
| "Rumble in the Jungle" is the song name | Book 11 | B11 Ch68 L173-175 | verified |
| Cosmic Throne restored | Books 12-13 | B12 Ch63 L9; B13 Ch1019 L46 | verified |
| Asano Village built in about six months (bushland "six months ago") | before Book 5 opens | B5 Ch5 L59, L104 | verified |
| Book 5 opens about nine months after the return; bronze "for a year"; iron to bronze "a year and a quarter" | about March 2020 | B5 Ch3 L170, L212 | verified |
| Walkabout: Jason "ran away from his family for six months" | about M22-M28 | B5 Ch8 L5 | verified |
| Grid blackouts still localised at Book 5's start; wide-scale loss expected in "two more months" | about March 2020 | B5 Ch3 L8-19 | verified |
| Network partnerships with governments "over the last few years" before the monster waves | before spring 2020 | B5 Ch13 L37 | verified |
| One month since the Nitra dome came down | Book 6 | B6 Ch23 L3 | verified |
| Shako kills Jason (fourth death); Dawn cites the broken compact | Book 6 | B6 Ch18 L6 | verified |
| Shako and Chen place the device in the Saint-Étienne aperture | Book 6 winter | B6 Ch35 L80 | verified |
| Dimensional ulceration named by Dawn | end of Book 5 | B5 Ch68 L30 | verified |
| "Butterflies of Makassar" news name | after Makassar | B5 Ch32 L4 | verified |
| Church of Death certificate "died four times. So far." | Book 7 | B7 Ch17 L104 | verified |
| Outworlders appear naked and hairless in craters | Book 7 | B7 Ch33 L114 | verified |
| 74 Earthlings to return, about thirty not | about 2037 | B12 Ch53 L57 | verified |
| Priests freed "around twenty years ago"; "almost twenty years" | Book 12 | B12 Ch7 L78; B12 Ch13 L36 | verified |
| Gary "almost a year later" a haggard figure | after the Cardinas zone | B11 Ch68 L703 | verified |
| Zone duration: "next few months, maybe as much as a year"; shaft tamed "months after" | Cardinas zone | B11 Ch48 L22; B11 Ch60 L3 | verified |
| Messengers "only months old" appear over the stone circle on Earth | M74 | B11 Ch68 L469-473 | verified |
| Vampire war "back in full swing"; "off and on for decades"; ended "these last few months" | Book 13 | B13 Ch988 L26; B13 Ch1002 L69; B13 Ch1023 L12 | verified |
| Magitech Institute "last two years"; no McKean trace for "more than four years" | Book 13 | B13 Ch995 L14; B13 Ch998 L105 | verified |
| Fortress found 1948, grid sector offline about seventy years | before Book 4 | B4 Ch51 L30, L37 | verified |
| Shade reaches silver "almost two months" before Broken Hill | | B5 Ch18 L22 | verified |

Note: "Rules of Intrusion" is the Book 12 wording (B12 Ch63 L5, L7, L45); Book 13 says "Laws of Intrusion" (B13 Ch987 L38, Ch1017 L44, Ch1020 L98). Documents should use "Rules" and mention "Laws" as the Book 13 variant.

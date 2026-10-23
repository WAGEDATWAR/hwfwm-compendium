# Timeline expansion progress (written for after-compaction recovery)
Task: user asked (1) split Emi/Nik [DONE: Emi_Evans_Asano.md, Nik_Asano.md; indexes updated; Emi_and_Nik.md deleted] (2) expand timeline greatly.
Method: per-book files 08_History_and_Timeline/Book_NN_Timeline.md (header like Book_01_Timeline.md; tables When|Chapters|Event with (Book N, ChX LY) cites; only claims supported by cited line).
Source of events: scratchpad/notes/bN.md (chapter notes); find lines with `K=2 W=200 python3 loc2.py N specfile` (spec lines "ChA-ChB || natural description"); check with `THR=0.25 python3 cc2.py 08_History_and_Timeline/Book_NN_Timeline.md`.
Time cues: grep Source_Text for "weeks/months/years ago|later", seasons. Do NOT invent day numbers.
Done: Books 1-10 (checked w/ cc2). KEY FINDINGS: Book 3 death ~M15-16 (Ch62 L96 'few months more than a year'; memorial >1 month before farewell Ch69 L894), Earth return early June 2019 (B4 Ch3 L112); Book 2 starts ~M4 (B2 Ch9 L67 'about four months'); astral space entered ~M10 (spring), 5 months in at B3 Ch55 L95; old Master 'M18 death' wrong. Workflow per book: Read notes/bN.md (2 pages), grep cues, write tN.txt spec for loc2.py (K=1), Read output, write Book_NN_Timeline.md, fix, cc2. TODO: Books 2-13, then rewrite Master_Timeline.md (link per-book files, add connections: characters/places/items), then run register pipeline (newrows->mkdocs->splice_map; add 08 docs fine since allrows walks all dirs), update Change_Log, TODO, Project_Structure, Name_Index if needed.
Corrections found en route (apply to character files?): Emi: Book 4 Ch28-29 reveal not first person; Ch5 Ch53 she chose not to be adventurer; Nik age ~5 when Jason left (B12 Ch15 L47).

Book4 dates: return early June 2019 (B4 Ch3 L112), Erika's party a Friday ~wk2, negotiation Tuesday; ends ~Sept 2019 with walkabout. Book5: opens ~Mar 2020 (B5 Ch3 L170 nine months), birthday Apr 1 (Ch20), Makassar Apr, Japan Apr-May, Gerling/Kaito's death ~June (funeral winter Ch52 L3), Nitra dome ~Oct 2020 (estimates). Kaito death = M30-31 not M36.

Book6: Nitra dome Oct 2020 (~2 weeks), Saint-Etienne zone winter, domain six months old at Ch47 L4, farewell warm autumn day Ch47 L155 (~Sept-Oct 2021). Pallimustus epilogues are in Ch47 L172-L1000 (Gary 2 years since memorial Ch47 L941). Remaining: Books 7-13 then Master.

Book7: don't use Day/Week labels unless stated; use 'Arrival/First days/Early/Mid-surge/Late surge'. Anchors: B7 Ch2 L76 (19 days), Ch18 L48, Ch57 L3, Ch62 L43, Ch66 L27. Next: Book 8.

Book8 ends ~Apr 2022 (surge ending soon, Dawn leaves). Next: Book 9.

Book9: Rimaros departure ~Apr 2022 (B9 Ch24 L44 half a year), monsoon 4 months, Yaresh battle ~Aug-Oct 2022. Next: Book 10.

Book10: Jason 29 at B10 Ch33 L76 (after 1 Apr 2023) => Yaresh battle <= ~Feb 2023; Book 9 note updated. Expedition Apr-mid 2023; zone starts end B10. Next: Book 11 (zone ~9 months wiki; 'almost a year' Ch68 L703), 12, 13, then Master rewrite.
Book11 DONE (cc2 ok). Next: Book 12, 13, Master.
Book12 DONE (cc2 ok, thin end). Next Book13 then Master.
Book13 DONE. Next: Master rewrite, pipeline, logs.
Master rewritten. Next: pipeline (newrows, mkdocs, splice_map), Change_Log, TODO, Structure, Open_Questions.
Pipeline run OK after fixing allrows 'files' shadow bug; 18 partials whitelisted. Next: Change_Log, TODO, Structure, Open_Questions.

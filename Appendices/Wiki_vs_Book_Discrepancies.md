# Wiki versus Book: Discrepancy Log

Status: Draft (book text and the fan wiki; each row names what the wiki says (wiki), what the chapter text says with its line, and which tier the compendium follows; the book text wins wherever the two differ)
Spoiler level: 3
Valid from: Book 1
Valid through: Book 13
Sources: Books 1-13 (chapter files); fan wiki cache (`src/tools/wiki/pages.json`)
Related: ../00_Project_Structure.md, Wiki_Reference_Lists.md, Open_Questions.md, Glossary.md, ../02_Cosmology_and_Powers/Gods_and_Churches.md, ../08_History_and_Timeline/Master_Timeline.md

## 1. Summary

A reader who meets a fan-wiki fact elsewhere can look it up here to see whether the chapter text agrees. The log holds the points where the wiki differs from the chapter files, or says something the chapter files do not, that the compendium has found so far. It is not a full comparison of the wiki with the series: the wiki cache holds about 1,500 pages and only the gods list, the essence, confluence and stone tables and the points below were compared. The source hierarchy stays: Book files, then chapter notes, then wiki.

## 2. Where the two differ

| Topic | The wiki says | The chapter text says | Follow |
|---|---|---|---|
| When the god of Death is first mentioned | Book 3, epilogue (wiki) | Clive says "our god of death" in Book 2 (Book 2, Ch25 L67) | the text |
| When the goddess of Earth is first mentioned | Book 12 (wiki numbering) | Arash mentions "the goddess of earth" in Book 1 (Book 1, Ch77 L21) | the text |
| How long gold-rankers live | "~500 years old" on the Ranks page (wiki) | "Gold rankers live for centuries" and no figure (Book 1, Ch22 L58) | the text; no number is given |
| How dense Vitesse's magic is | "much denser" than Greenstone, with no figure (wiki) | a rank band: silver typical, golds as common as bronzes, occasional diamond (Book 1, Ch30 L43-44) | the text |
| How long the Cardinas zone lasted | "nine months" (wiki) | bounds only: Nik is "six months old" (Book 11, Ch50 L15), Gary's divine power has "four to eight months" left (Book 11, Ch34 L33) and he is almost a year past the Cup of Heroes (Book 11, Ch68 L703) | the text's bounds; no total is given |
| Neil Davone and Cassandra Mercer | a line listing her as his ex-girlfriend, which the compendium found to be a mis-assignment | at thirteen he had a crush on her, four years his elder (Book 2, Ch27 L41-48) | the text |
| The gods Hearth and Refuge | listed as first mentioned at the Boko refugee scene (Book 12, chapter 39 in the wiki's numbering) | no scene, temple or priest for either god was found | wiki only, unconfirmed |
| Belinda and Estella's dating | wiki dates in Book 12 | the text shows them as wives by Book 13 (Book 13, Ch1011 L23) and no Book 12 dating date was found | the text for the marriage; the dates are wiki only |
| The Reaper gave the Way of the Reaper martial art | stated as fact | the text shows the order's skill book (Book 1, Ch50 L41) and does not say who gave it | wiki only, unconfirmed |
| Pain and Discord as evil or hidden gods | listed as evil or hidden gods | a speaker calls Discord one of the "dark gods" (Book 8, Ch48 L47) and Humphrey swears by "the goddess of pain" (Book 12, Ch26 L80); nothing more | partly supported |

## 3. Terms the text uses that earlier notes called missing

An earlier pass (the log of 2026-10-22) recorded "essence revelations" and "combat trance" as not found in the text. Both are in it, which this pass corrects:

- **Combat trance**: Jason and Akari discuss the combat trance he has "touched on" but cannot yet use (Book 6, Ch26 L71, L77), and he is still trying to master it in Book 7 (Book 7, Ch2 L98).
- **Essence revelation**: a character asks if Jason will chase "essence revelation again" (Book 9, Ch28 L75). The wiki's Ranks page says gold-rankers need essence revelations to progress; the text names the term once and does not explain a mechanism.
- **Hegemon's Will**: the text names the reforged sword (Book 7, Ch2 L89; Book 7, Ch54 L115). An earlier note had called the name wiki-only; it is a book name.

## 4. Structural differences

- **Chapter numbering**: the wiki numbers chapters through the whole series, for example "Chapter 514" (wiki), and the chapter files restart at each book. The gods table in `02_Cosmology_and_Powers/Gods_and_Churches.md` keeps the wiki's numbering in its own column, marked as the wiki's.
- **An example**: Book 7, Chapter 54, "Hegemon’s Will" (Book 7, Ch54 L1), is the wiki's chapter 514.
- **First mention**: the wiki records any mention of a god, while the compendium's text scan counts a god's church, temple or priests. A later text line against an earlier wiki one is therefore not a discrepancy; only an earlier text line is (the two gods in section 2).
- **Lists**: the wiki's gods, essences, confluences, stones and monsters are copied, tier-marked, into `Wiki_Reference_Lists.md`.

## 5. How to extend this log

1. When a wiki claim is checked against the chapters and the two differ, add a row to section 2 with the line.
2. When a note says a wiki term is "not found", search for the curly apostrophe and plain forms before recording it; the two entries in section 3 were missed because the search used one form.
3. Refresh the wiki cache with `fetchwiki.py` first if the comparison matters, then rerun `wiki_lists.py` and `compose_wiki.py`.

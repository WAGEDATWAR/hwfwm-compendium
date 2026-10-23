import os
B = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", ".."))
p = os.path.join(B, "Appendices", "Glossary.md")
s = open(p, encoding="utf-8").read()
i = s.index("## Spelling and naming variants")
new = """## Spelling and naming variants (use the first form)

The text itself is inconsistent in places. This section records each variant once, with the form the compendium uses, where the other form occurs and what kind of variant it is. Counts were taken over the chapter files on 2026-10-22.

| Preferred | Also seen | Where | Note |
|---|---|---|---|
| Farrah Hurin | Huren | wiki only | The chapter files always write Hurin (Book 4, Ch54 L88; \"the Hurins\", Book 2, Ch32 L12). |
| Jonah Geller | Jonas | Book 11, Ch6 L62 | One slip in 145 uses of Jonah. |
| Nicolas Hendren | Herston; Hedron | Book 2, Ch21 L21; Book 3, Ch1 L106 | The Purity archbishop; Hendren is used in 152 lines, each variant once. |
| Arabelle Remore | Arabella | Book 2, Ch38 L23 | Three uses of Arabella in 578 lines. |
| Gabriel Remore | Gabriele | Book 2, Ch76 L40 | One slip beside Arabelle's name. |
| Gabrielle Pellin | Gabriele | Book 1, Ch78 L44 | One slip; Gabrielle appears in the neighbouring lines. |
| Beth Cavendish | Cavenish | Book 3, Ch1 L86 | One slip. |
| Marek Nior Vargas | Marek Noir Vargas | Book 10, Ch31 L74 | The Nior spelling is used about 47 times. |
| Boris Ket Lundi | Boris Ketland | Book 10, Ch79 L52-54 | Ketland is the Earth alias; Ket Lundi is his real name. |
| Mr North | Noreth | Book 7, Ch14 L41 | Noreth is his own name (the founder's former familiar). |
| Velitraxistaasch | Stash | Book 1, Ch38 L58 | Stash is the familiar's preferred short form and appears far more often. |
| Carlivexistrix | Carli | Book 6, Ch47 L738 | She asks to be called Carli. |
| Gary Xandier | Gareth Xandier | Book 1, Ch37 L109 | Gary is short for Gareth; the compendium uses Gary Xandier. |
| Gary Sharpton | reincarnated Gary | Book 12 | The leonid who appears after Gary's death. |
| Sigrid Freyn | Sigrid Volaire | Book 3, Ch4 L43; Book 13, Ch958 L39 | Freyn is her own name; Volaire is her married name. |
| Mirror Kingdom | Kingdom of Mirrors | Book 2, Ch51 L8 | Mirror Kingdom is used about 13 times, Kingdom of Mirrors once. |
| Daryll | Darryl | Book 12, Ch54 L29; Book 12, Ch53 L62 | The troll were-crocodile Earthling is spelled Daryll about 12 times and Darryl about 3 times in Books 12-13; he is a different person from Darryl Caruthers (below). |

### Same name, different people

| Name | The people | Where |
|---|---|---|
| Beaufort | Beaufort Mercer (Thadwick's father) and the gold-rank elf who commands the Builder cult's forces | Book 2, Ch59 L4; Book 10, Ch65 L30; Book 10, Ch72 L41 |
| Claire | Claire Adeah (Rick Geller's healer) and Claire Davney (US Secretary of State) | Book 1, Ch67 L15; Book 13, Ch963 L24 |
| Miriam | Miriam Vance (Moon's Edge leader) and Miriam Coyle (head of the magitech weapons institute) | Book 10, Ch59 L17; Book 13, Ch995 L14 |
| Hector | Hector De Lange (International Committee) and a Hector who appears in the Book 9 royal audience | Book 4, Ch51 L10; Book 9, Ch16 L50 |
| Garret | the leader of the Book 5 superhero team and Garret Headingway | Book 5, Ch19 L10; Book 12, Ch50 L3 |
| Chen | Kylie Chen (bronze Network scout) and the category-four shield user in Slovakia (not shown to be the same) | Book 4, Ch42 L27; Book 6, Ch6 L31 |
| Ramona | the Order of Redeeming Light member and the Moon's Edge ritualist (not shown to be the same) | Book 8, Ch9 L11; Book 11, Ch46 L11 |
| Darryl | Darryl Caruthers, the Vane high priest killed in Book 1, and the Book 12-13 Earthling | Book 1, Ch11 L73; Book 1, Ch13 L3; Book 12, Ch53 L62 |
| Amos / Orin Pensinata | uncle and nephew, not variants of one name | Book 7, Ch47 L39 |

### Not variants

- **Culie**: Elseth Culie is a surname (Book 9, Ch89 L43), not a spelling of Clive.
- **Asarno**: \"Mr Asarno\" in Book 1, Ch71 L53 is how a speaker mangles Asano; four uses.
- **Zardoz**: Jason's joke in Book 1, Ch16 L51 about Zartos.
"""
s = s[:i] + new
open(p, "w", encoding="utf-8").write(s)
p = os.path.join(B, "00_Project_Structure.md")
t = open(p, encoding="utf-8").read()
t = t.replace("choose the form most used and note the variant once (the planned variants table is item 0.8 of `TODO_Build_Plan.md`).", "choose the form most used and note the variant once in the Glossary's variants table (`Appendices/Glossary.md`, last section).")
open(p, "w", encoding="utf-8").write(t)
print("ok")

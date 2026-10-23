root = r"C:\Users\Gabriel\Documents\World Stuff\HWFWM Compendium"

def sub(rel, pairs):
    p = root + "\\" + rel
    s = open(p, encoding="utf-8").read()
    for a, b in pairs:
        assert a in s, (rel, a[:70])
        s = s.replace(a, b)
    open(p, "w", encoding="utf-8").write(s)

# Primer: surge delay
sub("01_World_Primer.md", [
 ("The series' major surge begins in Book 7, long overdue because a magical link to Earth had been bleeding Pallimustus off.",
  "The series' major surge begins in Book 7, about five years overdue (Book 7), which the books connect to a magical link to Earth that had been bleeding Pallimustus off."),
])

# Structure doc section 9
sub("00_Project_Structure.md", [
 ("- **Age of earthlings' arrival**: \"fifteen years ago\" (Cyrion arc) against \"seventeen years\" (Artefact Site).",
  "- **Age of earthlings' arrival** *(resolved)*: \"fifteen years ago\" (Pallimustus speakers, about 2037) and \"seventeen years ago\" (Lenora Coleman on Earth, 2038) are rounded statements about the same autumn-2021 event; see `08_History_and_Timeline/Master_Timeline.md`, section 12."),
 ("- **Wiki timeline errors**: Asano Village timing, some month counts.",
  "- **Wiki timeline errors**: Asano Village timing (the text says about six months of building), the surge delay (five years, not fifteen), and the Book 5-6 month counts, which do not fit the seasonal cues; see the Master Timeline."),
])

# TODO: add timeline section
p = root + r"\TODO_Verification.md"
s = open(p, encoding="utf-8").read()
s = s.replace("- Master Timeline: finer month counts from Book 6 onward; the wiki's Book 5 month discrepancies.\n", "")
s += """
## F. Master Timeline (08_History_and_Timeline)

Verified against the book text and written into the document (see the Change Log): the calendar anchors (late-November departure, early-June return, 1 April birthday, ages 23, 26, 29 and 44, 2038 and "2020" zones), the surge being five years overdue, the Earthlings' count and what they did, the One Day War's "a month since", "almost a year later" for Gary, Rufus and Taika going to Earth with Boris, the cold-winter and warm-autumn cues in Book 6, and the death certificate in Books 7 and 10.

Still unchecked or open:
- Month counts after Book 5 (all wiki-based): the Grid shutdown, Kostroma at M29, Kaito's death at M36, the Book 6 zone months, the whole of Books 7-11 apart from the cues noted.
- Whether the Cardinas zone lasted nine months; whether the clan hid for "two years" as well as "half a decade"; "two years of renewed vampire war" in Book 13.
- The Book 1 and Book 3 event rows (Anisa's dismissal, Valkyrie match, Mr Sparrow, M12/M15/M17/M18 values): from chapter notes and the wiki.
- Whether Boko's destruction occurs in Book 12 as stated; the exact date of Book 12's Pallimustus present and of Jason's arrival on Earth.
- The wiki's "billions of years" and the siphon accelerating over the last 150 years (background rows).
- The statement in Book 12 that magic became known "less than fifteen years ago" against the 2020 monster waves.
"""
open(p, "w", encoding="utf-8").write(s)

# Change log
p = root + r"\Appendices\Change_Log.md"
s = open(p, encoding="utf-8").read()
a = "**Appendices and housekeeping**"
add = """**History and Timeline (`08_History_and_Timeline/`)**
- Revised `Master_Timeline.md` (second version) against the book text and the confirmations made since it was written. Added a calendar-anchors section (born 1 April 1994; arrival late November 2017; return early June 2019; the age-26 birthday in April 2020; departure in autumn 2021; Book 13 in 2038) derived from statements in Books 1, 4, 5, 10, 12 and 13, and marked book-confirmed rows with [book].
- Corrections: the surge delay was "some five years overdue" (Book 7), not fifteen; the Network's founder's familiar, Mr North, was betrayed with Boris's help to the early magic societies, not "the American societies"; Broken Hill's dead are Jason's estimate of ten to fifteen thousand, with over nineteen thousand survivors; the order in Book 5 is Broken Hill, then the April birthday scene, then Makassar, Jason's silver rank, Kostroma, and the deaths of Kaito, Asya and Greg; the "System withdrawal at Cyrion" is now the System withdrawal for slavery and indenture regions; the departure from Earth is placed in autumn 2021 rather than the wiki's M49; the Earthlings' "fifteen versus seventeen years", the Book 3 winter question and the "fifteen versus sixteen years away" conflict are resolved as roundings and hemisphere seasons.
- Also revised for consistency: `01_World_Primer.md` (surge overdue by about five years) and `00_Project_Structure.md` (section 9 open questions updated).
- Status: **Draft (anchors verified; later month counts approximate)**; remaining items in `TODO_Verification.md`, section F.

"""
assert a in s
s = s.replace(a, add + a, 1)
open(p, "w", encoding="utf-8").write(s)
print("maintenance done")

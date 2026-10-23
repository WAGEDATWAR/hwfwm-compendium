import os
B = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", ".."))
def edit(rel, pairs):
    p = os.path.join(B, rel); s = open(p, encoding="utf-8").read()
    for o, n in pairs:
        assert o in s, (rel, o[:60]); s = s.replace(o, n, 1)
    open(p, "w", encoding="utf-8").write(s)
edit("08_History_and_Timeline/Book_12_Timeline.md", [
 ("The Earth arrival (Ch64 to Ch67) is best placed in 2038: autumn 2021 plus seventeen years and Jason's forty-fourth year both point there, and Book 13 gives 2038 (Book 13, Ch951 L50). The time between",
  "The Earth arrival (Ch64 to Ch67) is best placed in 2038, because Lenora counts seventeen years from the vanishing (Book 12, Ch67 L65) and Jota gives Jason's age as forty-four (Book 12, Ch67 L113). Book 13 is dated 2038 (Book 13, Ch951 L50). The time between"),
 ("Chapters 59 to 61 and 62 overlap in time: Ch61 closes with the visitors at Lenora's door, and Ch62 opens aboard the saucer before they arrive (Book 12, Ch61 L105 to L107; Book 12, Ch62 L3).",
  "Ch61 closes with the visitors downstairs (Book 12, Ch61 L107), and Ch62 opens aboard the saucer before they arrive (Book 12, Ch62 L3)."),
])
edit("08_History_and_Timeline/Master_Timeline.md", [
 ("the Earth arrival is best placed in 2038 because the book counts \"seventeen years\" from the Earthlings' vanishing (Book 12, Ch67 L65) and Jason's forty-fourth year (Book 12, Ch67 L113), with Book 13 at 2038 (Book 13, Ch951 L50). The book never states a year or the gap between the tour and the arrival.",
  "the Earth arrival is best placed in 2038 because Lenora counts seventeen years from the Earthlings' vanishing (Book 12, Ch67 L65) and Jota gives Jason's age as forty-four (Book 12, Ch67 L113). Book 13 is dated 2038 (Book 13, Ch951 L50). The book never states a year or the gap between the tour and the arrival."),
 ("| Book 12 \"now\" | \"M-count\" | Pallimustus tour late 2037 to early 2038; Earth arrival 2038; Book 13 is 2038 | Book 12, Ch21 L61; Book 12, Ch67 L65, L113; Book 13, Ch951 L50 |",
  "| Book 12 \"now\" | \"M-count\" | Pallimustus tour late 2037 to early 2038; Earth arrival 2038 | Book 12, Ch21 L61; Book 12, Ch67 L65, L113 |"),
])

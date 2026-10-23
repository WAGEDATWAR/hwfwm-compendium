import os, re
B = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", ".."))


def edit(rel, pairs):
    p = os.path.join(B, *rel.split("/"))
    s = open(p, encoding="utf-8").read()
    for o, n in pairs:
        if o not in s and n in s:
            continue
        assert o in s, (rel, o[:70])
        s = s.replace(o, n, 1)
    open(p, "w", encoding="utf-8").write(s)


def before_heading(rel, heading, text):
    p = os.path.join(B, *rel.split("/"))
    s = open(p, encoding="utf-8").read()
    if text.split("\n")[0] in s:
        return
    assert heading in s, (rel, heading)
    s = s.replace(heading, text.rstrip("\n") + "\n\n" + heading, 1)
    open(p, "w", encoding="utf-8").write(s)


# Jason
edit("07_Characters/Jason_Asano.md", [
    ("- **Familiars**: Shade, Colin and Gordon (see Familiars.md).",
     "- **Familiars**: Shade, Colin and Gordon (see `Familiars/Shade.md`, `Familiars/Colin.md` and `Familiars/Gordon.md`, and the hub `Familiars.md`)."),
    ("- **Familiars**: Shade, Colin and Gordon.\n",
     "- **Familiars**: Shade (a shadow, butler and driver), Colin (an apocalypse leech swarm) and Gordon (an Avatar of Doom); full entries in `Familiars/`.\n"),
])
# Humphrey
edit("07_Characters/Humphrey_Geller.md", [
    ("- **Familiar**: Stash (Velitraxistaasch), a mirage dragon (Book 1, Ch38 L56-63).",
     "- **Familiar**: Stash (Velitraxistaasch), a bonded baby mirage dragon (Book 1, Ch38 L56-63); see `Familiars/Stash.md`.")])
# Clive
edit("07_Characters/Clive_Standish.md", [
    ("- **Familiar**: Onslow, a rune tortoise",
     "- **Familiar**: Onslow (see `Familiars/Onslow.md`), a rune tortoise")])
# Belinda
before_heading("07_Characters/Belinda_Callahan.md", "## 5. Background",
               "- **Familiars**: Shimmer, a summoned astral lantern (Book 2, Ch71 L50; Book 2, Ch72 L62; see `Familiars/Shimmer.md`), and an echo spirit that looks like a blurry version of her (Book 12, Ch27 L23).")
# Landemere Vane
before_heading("07_Characters/Landemere_Vane.md", "## 3. Roleplay notes",
               "- **Familiar**: Jason's first encounter with a native magical creature was Vane's familiar, which tried to take revenge for his death and fell victim to aging masonry (Book 5, Ch40 L81).")
# Autumn Leal
edit("07_Characters/Minor_Cast/Minor_Cast_Books_7-9.md", [
    ("- An adventurer Jason met before reaching Rimaros, with a frog essence and a frog familiar ritual (Book 7, Ch20 L21; Book 9, Ch1 L49; Book 9, Ch10 L102).",
     "- An adventurer Jason met before reaching Rimaros, with a frog essence and a frog familiar ritual (Book 7, Ch20 L21; Book 9, Ch1 L49; Book 9, Ch10 L102).\n- **Familiars**: she mourns her bonded companion (Book 9, Ch1 L50) and finds a new familiar, a long-tongue jumping hydra the size of a two-storey house that is closer to the frog-like end of the scale (Book 9, Ch10 L103, L106).")])
# Hub
edit("07_Characters/Familiars.md", [
    ("# The Familiars: Shade, Colin, Gordon and Stash\n",
     "# The Familiars: Shade, Colin, Gordon and Stash\n\nIndividual entries for the familiars with a personality are in the `Familiars/` folder: [Shade](Familiars/Shade.md), [Colin](Familiars/Colin.md), [Gordon](Familiars/Gordon.md), [Stash](Familiars/Stash.md), [Onslow](Familiars/Onslow.md) and [Shimmer](Familiars/Shimmer.md). This file stays as the overview.\n"),
    ("Related: 00_Characters_Overview.md, Jason_Asano.md, Humphrey_Geller.md, ../03_Magic_and_Adventuring/Familiars_Summons_and_Conjurations.md",
     "Related: 00_Characters_Overview.md, Jason_Asano.md, Humphrey_Geller.md, Clive_Standish.md, Belinda_Callahan.md, Umber.md, Familiars/Shade.md, Familiars/Colin.md, Familiars/Gordon.md, Familiars/Stash.md, Familiars/Onslow.md, Familiars/Shimmer.md, ../03_Magic_and_Adventuring/Familiars_Summons_and_Conjurations.md"),
])
# Magic Familiars file points to the characters
p = "03_Magic_and_Adventuring/Familiars_Summons_and_Conjurations.md"
s = open(os.path.join(B, p), encoding="utf-8").read()
if "07_Characters/Familiars" not in s and "../07_Characters/Familiars" not in s:
    m = re.search(r"^Related: (.*)$", s, re.M)
    s = s.replace(m.group(0), m.group(0) + ", ../07_Characters/Familiars.md", 1)
    open(os.path.join(B, p), "w", encoding="utf-8").write(s)
# Name index / glossary
ni = os.path.join(B, "Appendices", "Name_Index.md")
t = open(ni, encoding="utf-8").read()
for name, old, new in [
    ("Shade", "- **Shade** (B2): Jason's shadow familiar.", "- **Shade** (B2): Jason's shadow familiar. See `07_Characters/Familiars/Shade.md`."),
]:
    if old in t:
        t = t.replace(old, new, 1)
open(ni, "w", encoding="utf-8").write(t)
print("ok")

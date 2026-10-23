import re

base = r"C:\Users\Gabriel\Documents\World Stuff\HWFWM Compendium\Appendices"

def insert_sorted(path, new_entries, section_re):
    """Insert entries (each a single line starting with '- **Name**' or '**Term**') alphabetically in their letter section."""
    s = open(path, encoding="utf-8").read()
    for letter, entry in new_entries:
        m = re.search(r"^## %s\s*$" % re.escape(letter), s, re.M)
        assert m, (path, letter)
        start = m.end()
        nxt = re.search(r"^## |^---\s*$", s[start:], re.M)
        end = start + (nxt.start() if nxt else len(s) - start)
        block = s[start:end]
        lines = [l for l in block.split("\n")]
        key = lambda l: re.sub(r"[^a-z0-9 ]", "", re.sub(r"^- ", "", l).lower().replace("*", ""))
        entry_key = key(entry)
        # find insertion position among non-empty entry lines
        insert_at = None
        for idx, l in enumerate(lines):
            if l.startswith("**") or l.startswith("- **"):
                if key(l) > entry_key:
                    insert_at = idx
                    break
        if insert_at is None:
            # append after last entry line
            last = max(i for i, l in enumerate(lines) if l.startswith("**") or l.startswith("- **"))
            sep = "\n" if path.endswith("Name_Index.md") else "\n\n"
            lines.insert(last + 1, ("" if path.endswith("Name_Index.md") else "") + entry)
            if not path.endswith("Name_Index.md"):
                lines.insert(last + 1, "")
        else:
            if path.endswith("Name_Index.md"):
                lines.insert(insert_at, entry)
            else:
                lines.insert(insert_at, "")
                lines.insert(insert_at, entry)
        s = s[:start] + "\n".join(lines) + s[end:]
    open(path, "w", encoding="utf-8").write(s)

glossary = [
    ("B", "**Butterflies of Makassar**: the name broadcasters gave to the public spectacle in Book 5 in which Jason's familiar Gordon spread the *Harbinger of Doom* affliction through a horde of undead at Makassar. Filmed from high in the air, the swarm of blue and orange eye-patterned butterflies looked beautiful; it left only black-stained bones. Jason was credited with it, and it made many people fear what he might do. **[2]**"),
    ("D", "**Dimensional ulceration**: Dawn's term (Book 5) for a transformation zone forming in a space already coterminous with a proto-astral space: an open wound in the dimensional membrane. Its worst case is the collapse of the membrane and the annihilation of a world, possibly more. **[2]**"),
    ("H", "**Harbinger of Doom**: a stacking, unholy affliction applied through Gordon's orbs. It drains mana from the victim to conjure an incorporeal butterfly that seeks out nearby enemies, detonates with disruptive force when destroyed, and passes on every non-holy affliction of its host. It cannot be cleansed while any other non-holy affliction remains. See *Butterflies of Makassar*. **[2]**"),
    ("R", "**Ring gate**: a giant stone ring, about a hundred metres across, that anchors a physical bridge across the astral between two spaces; one rises over the crater in the Reaper-trials boarding vessel in Book 3. **[1]**"),
    ("S", "**Special-interest territory**: the Australian government's status (Book 13) for the standing stones and for Asano Village, managed by a multinational organisation. **[3]**"),
    ("W", "**World engineer**: one of the Builder's diamond-rank super-golems, comparable to a diamond-rank monster in size; dozens lie dormant in the Reaper-trials vessel (Book 3), and the toppled remains of others lie beyond Cyrion's outer wall (Book 12). **[1/3]**"),
]

names = [
    ("G", "- **Gordon Truffett** (B4): Network figure first named in Book 4; first Director of Operations of Dimensional Artefact Site One and, by Book 12, Australia's Prime Minister, known for fearmongering and for suggesting the seizure of Asano Village."),
    ("H", "- **Holly Macrossan** (B12/13): Annabeth Tilden's successor as UN Under-Secretary-General for Supernatural Affairs; later a liaison to the multinational taskforce for the Australian government."),
    ("N", "- **Neiman Bassingthwaite** (B12): Burning Violet's chief membership officer, an older gold-ranker."),
    ("T", "- **Todd \"The Necromancer\" Halverson** (B6): necromancer who got his start in Mr North's house; implicated in the Makassar undead."),
]

insert_sorted(base + r"\Glossary.md", glossary, None)
print("glossary done")

insert_sorted(base + r"\Name_Index.md", names, None)
print("names done")

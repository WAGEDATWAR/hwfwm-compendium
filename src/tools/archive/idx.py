import os, re, io, sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
BASE = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".."))
P = os.path.join(BASE, "Appendices", "Name_Index.md")
s = open(P, encoding="utf-8").read()
lines = s.split("\n")

# (name as shown in index, file, first book, one-line identification used if the entry is missing)
ENT = [
 ("Callum (Cal) Morse", "Callum_Morse.md", "B2", ""),
 ("Valdis Volaire", "Valdis_Volaire.md", "B2", "prince of the Kingdom of Mirrors and swordmaster."),
 ("Sigrid Freyn", "Sigrid_Freyn.md", "B2", "celestine healer; Valdis's team leader and wife (Sigrid Volaire in B13)."),
 ("Dustin Kettering", "Dustin_Kettering.md", "B1", "ice-armoured defender; Thadwick's offsider, then Rick's team."),
 ("Lorelei Grantham", "Lorelei_Grantham.md", "B3", "astral magic research official; Clive's partner by B13."),
 ("Vincent Baudrillard", "Vincent_Baudrillard.md", "B13", "French swordsman and Emi's love interest."),
 ("Chloe Baudrillard", "Chloe_Baudrillard.md", "B5", "French epidemiologist with Doctors Without Borders."),
 ("Noriko Asano", "Noriko_Asano.md", "B5", "matriarch of the old Asano clan."),
 ("Li Li Mei", "Li_Li_Mei.md", "B4", "Chinese silver-ranker; negotiator and later politician."),
 ("Ketevan Arziani", "Ketevan_Arziani.md", "B4", "Anna Tilden's assistant; later Yumi's chief of staff."),
 ("Miles Cotezee", "Miles_Cotezee.md", "B6", "Vitesse Adventure Society administrator."),
 ("Marcus Hargrave Xenoria", "Marcus_Hargrave_Xenoria.md", "B10", "leonid troubleshooter for the continental council."),
 ("Gormanston Bynes", "Gormanston_Bynes.md", "B10", "gold-rank elf; leader of Yaresh's Aristocratic Faction."),
 ("Hess Jor Nasala", "Hess_Jor_Nasala.md", "B9", "silver-rank messenger; Kaal's assistant."),
 ("Marla", "Marla.md", "B10", "brightheart military commander."),
 ("Adrien Barbou", "Adrien_Barbou.md", "B4", "Lyon operations director; second Mr East."),
 ("Marie Finnegan", "Marie_Finnegan.md", "B13", "expelled Zurich Network director."),
 ("Umber", "Umber.md", "B8", "Shade's brother and Knowledge's agent."),
 ("Helsveth", "Helsveth.md", "B3", "draconian World-Phoenix servant; successor as First Sister."),
 ("Erigo Fin Desca", "Erigo_Fin_Desca.md", "B10", "the Builder's prime vessel."),
 ("Zithis Carrow Vayel", "Zithis_Carrow_Vayel.md", "B8", ""),
 ("Garth Larosse", "Garth_Larosse.md", "B10", "High Priest of Undeath."),
 ("Amos Pensinata", "Amos_Pensinata.md", "B7", ""),
 ("Orin Pensinata", "Orin_Pensinata.md", "B7", ""),
 ("Hannah Adeah", "Hannah_and_Claire_Adeah.md", "B1", "elf archer on Rick's team; Rick's wife by B12."),
 ("Claire Adeah", "Hannah_and_Claire_Adeah.md", "B1", "elf healer on Rick's team; Hannah's twin."),
 ("Audrey Blaine", "Audrey_Blaine.md", "B5", "former Network member (\"Mrs South\"); Asano clan vampire researcher."),
 ("Hassan Dukhtar", "Hassan_Dukhtar.md", "B13", "Pakistani doctor; Jason's \"Handsome Doctor\" joke."),
 ("Anisa Lasalle", "Anisa_Lasalle.md", "B1", ""),
 ("Nicolas Hendren", "Nicolas_Hendren.md", "B2", "archbishop of Purity; killed in B3."),
 ("Beth Cavendish", "Beth_Cavendish.md", "B1", ""),
 ("Killian Laurent", "Killian_Laurent.md", "B2", ""),
 ("Padma Parsell", "Padma_Parsell.md", "B2", "Remore Academy cadet; Farrah's half-disciple."),
 ("Trenchant Moore", "Trenchant_Moore.md", "B7", "gold-rank human guard of the Sapphire Crown."),
 ("Jeni Kavaloa", "Jeni_Kavaloa.md", "B7", "gold-rank surge expedition leader."),
 ("Baseph", "Baseph_and_the_Rimaros_Children.md", "B7", "Liara's husband; children Dara, Zareen and Joseph."),
]

done = 0
for name, fn, b, ident in ENT:
    ptr = "see `07_Characters/%s`" % fn
    hit = [i for i, l in enumerate(lines) if l.startswith("- **" + name)]
    if hit:
        i = hit[0]
        if fn not in lines[i]:
            lines[i] = lines[i].rstrip() + (" " if lines[i].rstrip().endswith(".") else "; ") + ptr[0].upper() + ptr[1:] + "." if lines[i].rstrip().endswith(".") else lines[i].rstrip() + "; " + ptr + "."
        done += 1
        continue
    # insert new alphabetical entry inside its letter section
    letter = name[0].upper()
    start = None
    for i, l in enumerate(lines):
        if l.strip() == "## " + letter:
            start = i
            break
    if start is None:
        print("no section for", name)
        continue
    j = start + 1
    while j < len(lines) and not lines[j].startswith("## "):
        j += 1
    ins = j
    for k in range(start + 1, j):
        if lines[k].startswith("- **") and lines[k][4:].lower() > name.lower():
            ins = k
            break
    else:
        while ins - 1 > start and lines[ins - 1].strip() == "":
            ins -= 1
    lines.insert(ins, "- **%s** (%s): %s %s." % (name, b, ident.rstrip("."), ptr[0].upper() + ptr[1:]) if ident else "- **%s** (%s): %s." % (name, b, ptr[0].upper() + ptr[1:]))
    done += 1
open(P, "w", encoding="utf-8").write("\n".join(lines))
print("entries handled", done)

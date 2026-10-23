p = r"C:\Users\Gabriel\Documents\World Stuff\HWFWM Compendium\TODO_Verification.md"
s = open(p, encoding="utf-8").read()
i = s.index("## Places (06_Places)")
j = s.index("## Softened or removed but not disproved")
k = s.index("## Astral spaces (06_Places/Astral_Spaces)")

new_places = """## Places (06_Places) – second verification pass done

Confirmed in the second pass and written into the files: Greenstone is a colony of Estercost (Books 11-12) and Boko is older with a native population; the Mercer estate has a gate and guards; the Irios family controls Livaros's defences behind a dome barrier and designs Rimaros's defences; the smoke dragon and a city-sized kraken construct (Book 7); the Vitesse branch's Book 6 expedition against a Purity stronghold in northern Estercost; Argrave Mericulato as the Adventure Society functionary who triggers the naga egg; the Queen of Estercost; the System-withdrawal announcement for slavery and indenture regions; fallen world-engineer golems beyond Cyrion's outer wall; Kazlahk, Hornis, Pranay, Segurado, Girlano, Sadi Andali, Kurdansk, Jorganis and the Dragon Lands as described in the overview.

Remaining unconfirmed (kept hedged in the files):
- Vitesse magic level ("silver density"); the city of the Geller tower in Book 11; Zartos details (the name occurs only in Books 1 and 7); Kazlahk's medical university.
- Pelli's role in Palisaros; Yaresh's duke's name and the "Aristocratic Faction"; the Queen of Estercost's name.
- Boko's destruction wording (the Book 12 text confirms its character; the destruction itself was not re-read).
- Whether the Cyrion indenture situation is the single trigger for the System withdrawal.

"""

new_earth = """## Earth places (06_Places/Earth) – second verification pass done

Confirmed and written into the files: Asano Village tunnels (clifftop excavations as a front; a separate passage to the ocean and a glass seafloor tunnel; only Ken, Hiro, Emi and Farrah knew); the Book 13 special-interest territory arrangement for the village and the standing stones; Truffett as Prime Minister who proposed the seizure; Broken Hill's population (under 20,000 to almost 35,000) and Jason's 10-15,000 death estimate; Dorrigo's jungle trolls; Todd "The Necromancer" Halverson; Shako and Chen placing the device at Saint-Étienne; the nightmare hag as a diamond-rank fear-manifesting being; the EOA timeline (Perth, Melbourne, Sydney); Steamforge Circuit renamed; Nitra's city description; Carlos Quilido's research centre being in Jason's soul realm; Ascension's Gate as an island base of the Church of Knowledge; the Earth bridge end at the standing stones with weapons upgraded by Travis Noble; Boris's timing for the bridge.

Remaining unconfirmed:
- "Butterflies of Makassar" as a name (Book 12 jokes about "butterflies of death", which is Gordon's ability).
- Ogres, river hydras and giant toads at Dorrigo; the Network's public emergence three years before Book 4.
- Whether Asano Village's sea tunnel ends at a cloud-house dome; Saint-Étienne cloud-city details beyond the waterways; Gerling's role in triggering the Saint-Étienne zone.
- Artefact site: the roster of gold-rankers; whether the former Sky Link island is Ascension's Gate; the "within months" deadline.
- Nitra's quintessence-powered steam.

"""

new_astral = """## Astral spaces (06_Places/Astral_Spaces) – second verification pass done

Confirmed and written into the files: the turquoise lagoon and cerulean sky; the Lesser Miracle Potion (iron-rank, legendary) and Summoner's Die: Form (iron-rank growth, legendary) exist in Book 2; the constellation-panel puzzle; the sloth demon as gold-rank; the cult's planted beacon and astral bridge (Zato); Dawn's "dimensional ulceration" and worst-case description; New Water in Jason's kingdom with the Duke of Boko; Outer Rexion as a town around a shaft with a ring of temples; "My name is Arbour"; the pagoda design.

Remaining unconfirmed:
- Which Fallen Echoes trial gives the Medallion of Escape and Lesser Miracle Potion; the trial order; the space's overall monster density; the vessel's drift as a transcendent vehicle.
- Vault: three-storey pagoda, sin garden, blood artery section; the kingdom's fifteen-kilometre width, ten-storey pagoda, lagoon town; Arbour's treehouses and caldera; Rexion's array-powered citadel; "Wood Jason".
- The nine-month Cardinas zone duration (against the five-to-six-month collapse note); the dimensional-ulcer "best case"; the wiki's astral-king prerequisites; Interstice's named districts (Glim, Fueros).
- Node-network disruption after Book 1.
"""

s = s[:i] + new_places + new_earth + s[j:k] + new_astral
open(p, "w", encoding="utf-8").write(s)
print("todo updated")

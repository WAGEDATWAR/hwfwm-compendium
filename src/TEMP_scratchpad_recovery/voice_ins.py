import re,os
base=r"C:\Users\Gabriel\Documents\World Stuff\HWFWM Compendium\07_Characters"
V={
"Jason_Asano":"Dry, sarcastic and quick with modern references; polite to rank only when forced. Cue: \"Do I have to pay a wizard to identify items?\" (Book 1, Ch1 L108).",
"Rufus_Remore":"Courteous and formal, quick to apologise for discourtesy. Cue: his apology to Priestess Pellin (Book 7, Ch9 L18).",
"Farrah_Hurin":"A lecturer who turns blunt when angry. Cues: Book 1, Ch23 L15-17; \"Barbou belongs to me\" (Book 6, Ch26 L9).",
"Gary":"Deep, growling and plain-spoken. Cues: Book 1, Ch9 L121; \"rattling around in a hole\" (Book 11, Ch57 L60).",
"Humphrey_Geller":"Precise, shy about romance, crisp when commanding. Cues: Book 1, Ch47 L88-89; Book 13, Ch958 L48.",
"Sophie_Wexler":"Wary of kindness and silent about pain. Cues: Book 2, Ch1 L77-80; Book 2, Ch45 L69-72.",
"Clive_Standish":"A lecturer who loses the thread and apologises. Cue: \"Where were we?\" (Book 11, Ch68 L748); eel jokes (Book 1, Ch68 L92-94).",
"Neil_Davone":"Tentative before committing. Cue: Book 2, Ch27 L46.",
"Belinda_Callahan":"Delighted by her own cleverness, and teasing. Cues: Book 2, Ch32 L72; Book 7, Ch6 L42.",
"Danielle_Geller":"Blunt, quick to seize a weakness. Cues: Book 1, Ch47 L89; \"diplomacy is war\" (Book 12, Ch23 L79).",
"Dawn":"Formal, with a teasing edge. Cue: Book 5, Ch20 L21-24.",
"Zara_Rimaros":"Courtly, with a threat in the smile. Cue: Book 2, Ch69 L17-19.",
"Boris_Ket_Lundi":"Measured and careful. Cue: Book 11, Ch68 L493-498.",
"Knowledge":"Detached and untouchable in manner. Cue: Book 1, Ch46 L16.",
"Emir_Bahadir":"Smooth, showy and fond of an entrance. Cues: Book 3, Ch5 L9; Book 3, Ch69 L509.",
"Familiars":"Shade is butler-formal (Book 8, Ch50 L82; Book 11, Ch36 L43); Stash barks like a dog while a lizard (Book 1, Ch78 L84).",
}
for n,t in V.items():
    p=os.path.join(base,n+".md"); s=open(p,encoding="utf-8").read().split("\n")
    idx=[i for i,l in enumerate(s) if re.match(r"## \d+\. Roleplay notes",l)]
    if not idx: print("no header",n); continue
    i=idx[0]
    if any("Voice (condensed)" in l for l in s): continue
    s[i+1:i+1]=["","**Voice (condensed)**: %s See `../10_Roleplay_Support/Tone_and_Voice.md`."%t]
    open(p,"w",encoding="utf-8").write("\n".join(s))
print("done")

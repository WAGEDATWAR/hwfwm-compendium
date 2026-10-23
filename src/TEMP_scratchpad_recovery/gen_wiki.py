import json,re,sys
p=json.load(open('wiki/pages.json',encoding='utf-8',errors='replace'))
def fix(s): return s.replace('�',"'")
P={fix(k):v for k,v in p.items()}

def strip_templates(t):
    while True:
        n=re.sub(r'\{\{[^{}]*\}\}','',t,flags=re.S)
        if n==t: break
        t=n
    return t

def clean(t):
    t=re.sub(r'<ref[^>]*?/>|<ref.*?</ref>','',t,flags=re.S)
    t=re.sub(r'<!--.*?-->','',t,flags=re.S)
    t=strip_templates(t)
    def tbl(m):
        rows=[x.strip('| ').strip() for x in m.group(0).split('\n') if x.strip() and not x.startswith(('{|','|-','|}','!'))]
        return '\n'.join(rows)
    t=re.sub(r'\{\|.*?\|\}',tbl,t,flags=re.S)
    t=re.sub(r'\[\[(?:Category|File|Image):[^\]]*\]\]','',t)
    t=re.sub(r'\[\[(?:[^\]|]*\|)?([^\]]*)\]\]',r'\1',t)
    t=re.sub(r"'''?",'',t)
    t=re.sub(r'<[^>]+>','',t)
    t=re.sub(r'^Category:.*$','',t,flags=re.M)
    t=re.sub(r'__[A-Z]+__','',t)
    t=re.sub(r'^=+\s*(.*?)\s*=+\s*$',r'\1:',t,flags=re.M)
    t=re.sub(r'^\*\s*',' - ',t,flags=re.M)
    t=re.sub(r'\n{2,}','\n',t)
    return t.strip()

REDIR=re.compile(r'\s*#REDIRECT\s*\[?\[?([^\]\n]+)',re.I)
def resolve(title):
    m=REDIR.match(P[title])
    if m:
        tgt=fix(m.group(1).strip())
        if tgt in P: return tgt
    return title

out=[]
def add(name,keys,text,book=None):
    out.append({"name":name,"keys":keys,"text":text,"book":book})

rar_re=re.compile(r'\((?:unranked,\s*)?(Common|Uncommon|Rare|Epic|Legendary)[^)]*\)',re.I)
combo_re=re.compile(r"^[A-Z][A-Za-z' -]+(?:\s*\[[A-Za-z]+\])?(?:\s*(?:\+|,|/)\s*(?:and )?[A-Z][A-Za-z' -]+(?:\s*\[[A-Za-z]+\])?){2}(?:\s*=.*)?$")
for title in list(P):
    if not title.endswith('(Essence)'): continue
    raw=P[title]
    if REDIR.match(raw): continue
    base=title[:-len('(Essence)')].strip()
    t=clean(raw)
    m=rar_re.search(raw)
    rar=m.group(1).capitalize() if m else None
    low=(t+' '+raw).lower()
    is_conf=('confluence essence' in low and 'non-confluence' not in low) or 'category:confluence' in low
    desc=''
    for line in t.split('\n'):
        l=line.strip()
        if l and not l.endswith(':') and not l.startswith('-') and not l.startswith('System') and 'unranked' not in l[:40].lower() and len(l)>25 and not l.startswith('Known'):
            desc=l; break
    groups={}
    cur=None
    loose=[]
    for line in t.split('\n'):
        l=line.strip()
        if not l: continue
        item=l[2:].strip() if l.startswith('-') else l
        if item.endswith(':') and len(item)<60:
            cur=item.lower(); groups.setdefault(cur,[]); continue
        if l.startswith('-') and cur is not None:
            if item and item.upper()!='N/A': groups[cur].append(item)
        elif combo_re.match(l):
            loose.append(l)
    def grab(word):
        r=[]
        for k,v in groups.items():
            if word in k: r+=v
        return r
    abil=grab('abilit')[:12]; users=grab('user')[:8]; combos=grab('combination')[:8]
    if not combos: combos=loose[:6]
    kind='confluence essence' if is_conf else 'essence'
    text=f"{base} essence: {kind}"+(f" ({rar})" if rar and not is_conf else '')+'. '
    if desc and 'non-confluence' not in desc[:80]: text+=desc+' '
    if abil: text+='Known abilities: '+', '.join(abil)+'. '
    if combos: text+='Known combinations: '+'; '.join(combos)+'. '
    if users: text+='Known users: '+', '.join(users)+'.'
    add(f"{base} Essence",[f"{base} essence"]+([f"{base} confluence"] if is_conf else []),text.strip(),0)

for title,raw in P.items():
    if not (title.startswith('Awakening Stone of') or title.startswith('Divine Awakening Stone')): continue
    if REDIR.match(raw): continue
    t=clean(raw)
    mm=re.search(r'\(unranked,\s*([a-z]+)',raw,re.I)
    rar=mm.group(1).capitalize() if mm else None
    desc=''
    mm=re.search(r'An awakening stone that[^\n(]*',t)
    if mm: desc=mm.group(0).strip().rstrip('.')+'.'
    abil=[a for a in re.findall(r'^\s*- (.+)$',t,flags=re.M)][:8]
    text=f"{title}"+(f" ({rar})" if rar else '')+'. '
    if desc: text+=desc+' '
    if abil: text+='Abilities awakened by this stone in the books: '+'; '.join(abil)+'.'
    add(title,[title],text.strip(),0)

def page(title,keys,maxc=1500,name=None,book=0):
    if title not in P: print('MISSING',title,file=sys.stderr); return
    title2=resolve(title)
    t=clean(P[title2])
    t=re.sub(r'\n(?:References|See also|External links):.*','',t,flags=re.S)
    if len(t)>maxc:
        cut=t.rfind('.',0,maxc)
        t=t[:cut+1] if cut>maxc*0.6 else t[:maxc]
    add(name or title,keys,t,book)

pages=[
 ('Human',['human race','humans nature']),('Elf',['elf race','elves nature']),('Leonid',['leonid','leonids']),('Celestine',['celestine','celestines']),
 ('Draconian',['draconian','draconians']),('Smoulder',['smoulder','smoulders']),('Runic',['runic','runics']),('Merfolk',['merfolk']),
 ('Lehenik',['lehenik']),('Valash',['valash']),('Outworlder',['outworlder','outworlders']),
 ('Brightheart Smoulder',['brightheart','brighthearts']),('Garuda',['garuda']),('Races',['racial gifts','races']),
 ('Adventure Society',['Adventure Society']),('Adventure Society Badge',['Adventure Society badge','star rating']),
 ('Magic Society',['Magic Society']),('Alchemy Association',['Alchemy Association']),('The Red Table',['Red Table']),
 ('Spirit Coin',['spirit coin','spirit coins']),('Monster Core',['monster core','monster cores','core user']),('Reality Cores',['reality core','reality cores']),
 ('Monster surge',['monster surge','surge']),('Astral Space',['astral space','astral spaces']),('Proto-Astral Space',['proto-astral','proto astral']),
 ('Spirit Domain',['spirit domain','spirit realm']),('Akashic Speech',['Akashic Speech']),('Interstice',['Interstice']),
 ('Transcendent Beings',['transcendent beings','transcendent']),
 ('Astral Kings',['astral king','astral kings']),('Great Astral Beings',['great astral being','great astral beings']),
 ('The Builder',['Builder']),('The Celestial Book',['Celestial Book']),('The Keeper of Moments',['Keeper of Moments','Keeper of the Sands']),
 ('The Nameless',['nameless great astral']),('The Reaper',['Reaper']),('The Sundered Throne',['Sundered Throne','Cosmic Throne']),('The World-Phoenix',['World-Phoenix','World Phoenix']),
 ('Legion',['Legion']),('The All-Devouring Eye',['All-Devouring Eye']),('Keeper of the Cycle',['Keeper of the Cycle']),
 ('Hero',['Hero god','god of heroes']),('Healer',['Healer god','Church of the Healer']),('Dominion',['Dominion god']),('Knowledge',['Knowledge goddess','Church of Knowledge']),('Purity',['Purity god','Church of Purity']),('Liberty',['Liberty god','goddess Liberty']),('Vineyard',['Vineyard god']),
 ('Death (God)',['god of Death','goddess of Death']),('Undeath',['Undeath god']),('Minor Gods',['minor gods']),
 ('Vampires',['vampire','vampires']),('The Network',['The Network']),
 ('Zartos',['Zartos']),('Vitesse',['Vitesse']),('Pallimustus',['Pallimustus']),('Earth (Planet)',['Earth planet']),
 ('Rune Tortoise',['rune tortoise']),('Sanguine Horror',['sanguine horror']),('Apocalypse Beast',['apocalypse beast']),('Shab',['shab']),
 ('Soul Crest',['soul crest']),('Quintessence',['quintessence','affinity gem']),('Dimensional Bag',['dimensional bag']),
 ('Storm Kingdom',['Storm Kingdom']),('Mirage chamber',['mirage chamber']),
 ('Hydra',['hydra']),('Wendigo',['wendigo']),('Manticore',['manticore']),('Kraken',['kraken']),('Leviathan',['leviathan']),
 ('Fountain of Life',['Fountain of Life']),('Burning Violet Guild',['Burning Violet']),('Geller Family',['Geller family']),('Asano Family',['Asano family']),
 ('Team Biscuit',['Team Biscuit']),('Team Storm Shredder',['Team Storm Shredder']),('Team Moon\'s Edge',['Team Moon\'s Edge']),
 ('Crystal wash',['crystal wash']),("Jason’s Lemonade",['Jason\'s lemonade','lemonade']),
]
for item in pages:
    page(item[0],item[1])

json.dump(out,open('entries/wiki_entries.json','w',encoding='utf-8'),ensure_ascii=False,indent=1)
print(len(out),sum(len(x['text']) for x in out))

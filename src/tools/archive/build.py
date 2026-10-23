import sys,json,re,importlib
sys.path.insert(0,'entries')
OUT=sys.argv[1] if len(sys.argv)>1 else 'hwfwm_lorebook.json'
allentries=[]
for i in range(0,15):
    m=importlib.import_module(f'e{i}')
    allentries+=m.E
wiki=json.load(open('entries/wiki_entries.json',encoding='utf-8'))
wiki_ent=[{"name":w['name'],"keys":w['keys'],"text":w['text'],"book":0,"wiki":True} for w in wiki]

# fix known over-generic key sets
for x in allentries:
    if x['name'].startswith('The Healer, Dominion and Knowledge'):
        x['keys']=["Healer's Judgement","Divine Square","Knowledge temple","Dominion appears"]

def norm(s): return s.replace('�',"'").replace('’',"'")
merged={}
order=[]
def put(x):
    n=norm(x['name'])
    if n in merged:
        merged[n]['text']+="\n\n"+norm(x['text'])
        for k in x['keys']:
            if k not in merged[n]['keys']: merged[n]['keys'].append(k)
    else:
        merged[n]={"name":n,"keys":list(x['keys']),"text":norm(x['text']),"book":x.get('book'),"wiki":x.get('wiki',False)}
        order.append(n)
for x in allentries: put(x)
import e15
for name,keys,text,sup in e15.R:
    ks=list(keys)
    for sname in sup:
        sn=norm(sname)
        if sn in merged and sn!=norm(name):
            for k in merged[sn]['keys']:
                if k not in ks: ks.append(k)
            order.remove(sn); del merged[sn]
    n=norm(name)
    if n in merged:
        for k in merged[n]['keys']:
            if k not in ks: ks.append(k)
        merged[n]['text']=norm(text); merged[n]['keys']=ks
    else:
        merged[n]={"name":n,"keys":ks,"text":norm(text),"book":0,"wiki":False}; order.append(n)
# add wiki entries unless the same name exists in handwritten
for x in wiki_ent:
    if norm(x['name']) in merged: continue
    put(x)

# essences summary list (rarities) from wiki
ess=[w for w in wiki if w['name'].endswith(' Essence')]
rar={}
conf=[]
for w in ess:
    t=w['text']
    m=re.match(r'(.*?) essence: (confluence essence|essence)(?: \((\w+)\))?',t)
    if not m: continue
    base,kind,r=m.group(1),m.group(2),m.group(3)
    if kind.startswith('confluence'): conf.append(base)
    else: rar.setdefault(r or 'Unknown',[]).append(base)
lst="Known essence names by rarity (wiki-derived; combos vary in later books). "
for r in ['Common','Uncommon','Rare','Epic','Legendary','Unknown']:
    if r in rar: lst+=f"{r}: "+', '.join(sorted(rar[r]))+'. '
if conf: lst+="Confluence essences: "+', '.join(sorted(conf))+'.'
put({"name":"List of Known Essences","keys":["essence list","known essences","list of essences","what essences exist"],"text":lst,"book":0})

# drop useless entries (empty wiki essences)
final=[]
for n in order:
    x=merged[n]
    t=x['text'].strip()
    if x.get('wiki') and len(t)<70: continue
    if len(t)<25: continue
    final.append(x)

def mk(i,x):
    keys=[]
    for k in x['keys']:
        k=norm(k).strip()
        if k and k.lower() not in [z.lower() for z in keys]: keys.append(k)
    text=x['text']
    if x.get('book') and not text.startswith('(Book') and not text.startswith('BOOK'):
        pass
    return {"uid":i,"key":keys,"keysecondary":[],"comment":x['name'],"content":text,"constant":False,"selective":False,"selectiveLogic":0,"order":10,"position":1,"disable":False,"addMemo":True,"excludeRecursion":True,"probability":100,"displayIndex":i,"useProbability":True,"secondary_keys":[],"keys":keys,"id":i,"priority":10,"insertion_order":10,"enabled":True,"name":x['name'],"extensions":{"depth":4,"weight":10,"addMemo":True,"probability":100,"displayIndex":i,"selectiveLogic":0,"useProbability":True,"characterFilter":None,"excludeRecursion":True},"case_sensitive":False,"depth":4,"characterFilter":None}

entries={str(i):mk(i,x) for i,x in enumerate(final,1)}
doc={"name":"He Who Fights With Monsters | Complete Lorebook (Books 1-13)","description":"A comprehensive lorebook for the He Who Fights With Monsters LitRPG series (Shirtaloon), covering Books 1-13: world and magic system, essences, ranks, gods and great astral beings, characters, places, organisations, artefacts and per-book story events up to the end of Book 13. Book text takes precedence over the fan wiki where they conflict. Spoilers throughout.","is_creation":False,"scan_depth":3,"token_budget":4096,"recursive_scanning":False,"extensions":{"chub":{"expressions":None,"alt_expressions":None,"id":5205215,"full_path":"lorebooks/hwfwm/complete-lorebook","related_lorebooks":[],"background_image":"","preset":None,"extensions":[],"custom_css":None}},"entries":entries}
json.dump(doc,open(OUT,'w',encoding='utf-8'),ensure_ascii=False,indent=1)
print(len(entries),'entries; total chars',sum(len(v['content']) for v in entries.values()))
big=sorted(((len(v['content']),v['name']) for v in entries.values()),reverse=True)[:8]
print(big)

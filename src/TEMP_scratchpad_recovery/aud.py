import json,collections,os,re
r=json.load(open('register_final.json'))
c=collections.Counter()
for x in r:
    n=x['note']
    c['empty' if not n else ('lcp' if n=='line-level citation pass' else 'other')]+=1
print(c)
docs=collections.Counter(x['doc'] for x in r)
base="C:/Users/Gabriel/Documents/World Stuff/HWFWM Compendium"
missing=[d for d in docs if not os.path.exists(os.path.join(base,d))]
print("missing docs:",missing, len(docs))
nt=[x for x in r if x['tier']!='book']
for x in nt[:4]: print(json.dumps(x,ensure_ascii=False)[:350])
oth=[x for x in r if x['note'] and x['note']!='line-level citation pass']
print("other notes",len(oth))
cut=[x for x in r if x['claim'].count('(')>x['claim'].count(')')]
print("cut-off:",len(cut))
dup=collections.Counter((x['doc'],x['claim'][:80],x['ch'],x['lo']) for x in r)
print("dup identical:",sum(1 for k,v in dup.items() if v>1))
dup2=collections.Counter((x['doc'],x['claim'][:60]) for x in r)
print("same claim head in doc:",sum(1 for k,v in dup2.items() if v>1))
bad=[x for x in r if x['tag'].startswith('Book') and re.match(r'Book (\d+)',x['tag']) and int(re.match(r'Book (\d+)',x['tag']).group(1))!=int(x['book'])]
print("tag/book mismatch:",len(bad))
for x in bad[:6]: print(x['id'],x['tag'],x['book'],x['ch'],x['claim'][:90])

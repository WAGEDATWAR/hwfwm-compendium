import json,urllib.request,urllib.parse,os,time
B="https://he-who-fights-with-monsters.fandom.com/api.php?"
def get(p):
    p['format']='json'
    for i in range(4):
        try:
            r=urllib.request.Request(B+urllib.parse.urlencode(p),headers={'User-Agent':'Mozilla/5.0'})
            return json.load(urllib.request.urlopen(r,timeout=60))
        except Exception as e: time.sleep(2)
    raise
titles=[];c={}
while True:
    p={'action':'query','list':'allpages','aplimit':500,'apnamespace':0};p.update(c)
    j=get(p);titles+= [x['title'] for x in j['query']['allpages']]
    if 'continue' in j: c={'apcontinue':j['continue']['apcontinue']}
    else: break
print(len(titles))
pages={}
for i in range(0,len(titles),50):
    ch=titles[i:i+50]
    j=get({'action':'query','prop':'revisions','rvprop':'content','rvslots':'main','titles':'|'.join(ch)})
    for pg in j['query']['pages'].values():
        try: pages[pg['title']]=pg['revisions'][0]['slots']['main']['*']
        except: pass
json.dump(pages,open('wiki/pages.json','w'))
print(len(pages),sum(len(v) for v in pages.values()))

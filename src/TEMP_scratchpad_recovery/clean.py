import json,re,sys
p=json.load(open('wiki/pages.json'))
def clean(t):
    t=re.sub(r'<ref[^>]*?/>|<ref.*?</ref>','',t,flags=re.S)
    t=re.sub(r'<!--.*?-->','',t,flags=re.S)
    t=re.sub(r'\[\[(?:[^\]|]*\|)?([^\]]*)\]\]',r'\1',t)
    t=re.sub(r"'''?",'',t)
    t=re.sub(r'<[^>]+>','',t)
    t=re.sub(r'\n{3,}','\n\n',t)
    return t.strip()
if __name__=='__main__':
    for n in sys.argv[1:]:
        k=[x for x in p if x==n]
        if not k: print('MISSING',n);continue
        print('=====',n);print(clean(p[n]))

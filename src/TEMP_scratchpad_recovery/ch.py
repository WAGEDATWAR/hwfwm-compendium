import re,io,sys
sys.stdout=io.TextIOWrapper(sys.stdout.buffer,encoding="utf-8",errors="replace")
base=r"C:\Users\Gabriel\AppData\Local\Temp\claude\C--Users-Gabriel-Documents-Gmod-Projects-Gmod-Decompilation\08b70dbf-6f0b-4b6b-a18f-242cc3f1fe96\scratchpad"
name=sys.argv[1]; books=sys.argv[2].split(","); lim=int(sys.argv[3]) if len(sys.argv)>3 else 8
for b in books:
    t=open(base+rf"\notes\{b}.md",encoding="utf-8",errors="replace").read()
    n=0
    for m in re.finditer(r"[^\n]{0,140}"+name+r"[^\n]{0,260}",t,re.I):
        print(b,":",m.group(0)[:400]); n+=1
        if n>=lim: break
    print("---")

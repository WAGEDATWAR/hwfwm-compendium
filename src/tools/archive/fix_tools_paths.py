import os
T = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))


def sub(fn, pairs):
    p = os.path.join(T, fn)
    s = open(p, encoding="utf-8").read()
    for o, n in pairs:
        assert o in s, (fn, o[:50])
        s = s.replace(o, n, 1)
    open(p, "w", encoding="utf-8").write(s)
    print("ok", fn)


REL = 'st = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "Source_Text")'
sub("cc2.py", [('exec(open("newrows.py",encoding="utf-8").read().split("skipdocs")[0])', 'from common import *'),
               ('p=os.path.join(base,doc.replace("/","\\\\"))', 'p=os.path.join(base,*doc.split("/"))')])
sub("loc2.py", [('exec(open("newrows.py", encoding="utf-8").read().split("skipdocs")[0])', 'from common import *')])
sub("rd.py", [('st = r"C:\\Users\\Gabriel\\Documents\\World Stuff\\HWFWM Compendium\\src\\Source_Text"', REL)])
sub("ess_scan.py", [('st = r"C:\\Users\\Gabriel\\Documents\\World Stuff\\HWFWM Compendium\\src\\Source_Text"', REL)])
sub("chk.py", [('ST="../Source_Text"', 'ST=os.path.join(os.path.dirname(os.path.abspath(__file__)),"..","Source_Text")')])

base = r"C:\Users\Gabriel\AppData\Local\Temp\claude\C--Users-Gabriel-Documents-Gmod-Projects-Gmod-Decompilation\08b70dbf-6f0b-4b6b-a18f-242cc3f1fe96\scratchpad"
s = open(base + "\\cosmo_fix.py", encoding="utf-8").read()
head_end = s.index("def sub(")
head = s[:head_end]
sub_end = s.index("sub(r\"02_Cosmology_and_Powers")
helper = s[head_end:sub_end]
marker = "Gods_and_Churches.md"
k = s.index(marker)
k = s.rfind("sub(r\"", 0, k)
out = head + helper + s[k:]
open(base + "\\cosmo_fix2.py", "w", encoding="utf-8").write(out)
print("split ok")

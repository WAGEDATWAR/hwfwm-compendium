import os
B = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", ".."))
p = os.path.join(B, "08_History_and_Timeline", "Master_Timeline.md"); s = open(p, encoding="utf-8").read()
o = "\"Fifteen years\" (Book 12, Ch21 L61); \"twenty years\" since the arrival (Book 12, Ch7 L78); \"seventeen years\" since the Earthlings vanished and Jason \"born forty-four years ago\" (Book 12, Ch67 L65, L113) |"
n = "\"Fifteen years\" (Book 12, Ch21 L61); \"twenty years\" since the arrival (Book 12, Ch7 L78); \"seventeen years\" (Book 12, Ch67 L65) |"
assert o in s; open(p, "w", encoding="utf-8").write(s.replace(o, n, 1))

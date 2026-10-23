"""Shared helpers for the compendium tools: project paths, the chapter index, line access and term overlap."""
import os, re, json

HERE = os.path.dirname(os.path.abspath(__file__))
base = os.path.abspath(os.path.join(HERE, "..", ".."))
st = os.path.join(base, "src", "Source_Text")
idx = json.load(open(os.path.join(HERE, "chapter_index.json"), encoding="utf-8"))
files = {}
for n, l in idx.items():
    for (num, title, fn, nl, m) in l:
        files[(int(n), num)] = (os.path.join(st, "Book_%02d" % int(n), fn), title)
cache = {}


def lines(n, ch):
    k = (n, ch)
    if k not in cache:
        if k not in files:
            cache[k] = None
        else:
            cache[k] = (open(files[k][0], encoding="utf-8").read().split("\n"), files[k][1])
    return cache[k]


STOP = set("the and was were that this with from have had his her their they for are not but who which when after before into over under about also than then there here him them its out one two".split())


def terms(t):
    return {w for w in re.findall(r"[a-z]{4,}", t.lower().replace("\u2019", "'")) if w not in STOP}


CIT = re.compile(r"Book (\d+), Ch(\d+) L(\d+)(?:-(\d+))?")

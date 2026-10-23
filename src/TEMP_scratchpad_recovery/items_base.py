import os
base = r"C:\Users\Gabriel\Documents\World Stuff\HWFWM Compendium\09_Items_and_Artefacts"
os.makedirs(base, exist_ok=True)
HDR = """# {name}

Status: Draft (book text; facts carry a reference "Book N, ChX LY" to Source_Text; "notes" marks chapter-summary-only facts)
Spoiler level: {spoil}
Valid from: Book {vf}
Valid through: Book {vt}
Sources: {src}
Related: {rel}

## 1. Summary

{summary}

## 2. Facts

{facts}

## 3. Using this in a story

{rp}
"""
def write(fn, name, spoil, vf, vt, src, rel, summary, facts, rp):
    open(os.path.join(base, fn + ".md"), "w", encoding="utf-8").write(HDR.format(name=name, spoil=spoil, vf=vf, vt=vt, src=src, rel=rel, summary=summary, facts=facts, rp=rp))


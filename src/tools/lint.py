"""Document linter for the compendium.

Checks every compendium .md (not the generated register and map, the logs, the TODO files or the structure guide):
  ERROR  header block missing or incomplete (Status, Spoiler level, Valid from, Valid through, Sources, Related)
  ERROR  spoiler level does not start with 0-3 or "mixed" (mixed is for indexes whose entries carry their own level)
  ERROR  a "(Book N, ChX LY)" cite names a chapter or line that does not exist in src/Source_Text/
  ERROR  a Related link does not resolve to a file
  ERROR  a spoiler-level tag (<!-- level:N -->) is unbalanced, has an invalid level, or is lower than the header level
  ERROR  the generated file list in a folder overview is out of date (src/tools/overviews.py)
  ERROR  a Markdown link [text](path.md#anchor) points to a file or a heading that does not exist
  WARN   a backticked `Name.md` that matches no file in the compendium (a stale reference after a move or rename)
  WARN   a cite written in a non-standard form (for example "Book 9 Ch29 L17")
  WARN   leftover note shorthand ("->", " w/ ")
  WARN   a file in a folder that has an overview is not mentioned by that overview
Writes src/tools/lint_report.md and returns (errors, warnings, files_checked).
Usage: python3 src/tools/lint.py   (works from any directory)
"""
import os, re, sys, io
import spoiler_tags
from common import base, lines as chapter_lines

SKIP_FILES = {"00_Project_Structure.md", "TODO_Verification.md", "TODO_Build_Plan.md",
              "Appendices/Source_Register.md", "Appendices/Source_Map.md", "Appendices/Change_Log.md"}
SKIP_DIRS = {"src", ".git"}
HEADER_FIELDS = ["Status", "Spoiler level", "Valid from", "Valid through", "Sources", "Related"]
CITE = re.compile(r"Book (\d+), Ch(\d+) (L\d+(?:-L?\d+)?(?:, L\d+(?:-L?\d+)?)*)")
BAD_CITE = re.compile(r"Book (\d+) Ch(\d+) L\d+")
LREF = re.compile(r"L(\d+)(?:-L?(\d+))?")


def docs():
    out = []
    for root, dirs, files in os.walk(base):
        dirs[:] = [d for d in dirs if d not in SKIP_DIRS]
        for f in files:
            if f.endswith(".md"):
                rel = os.path.relpath(os.path.join(root, f), base).replace("\\", "/")
                if rel not in SKIP_FILES and not rel.startswith("Appendices/Change_Log"):
                    out.append(rel)
    return sorted(out)


def header(text):
    head = {}
    for ln in text.split("\n")[:20]:
        m = re.match(r"^(Status|Spoiler level|Valid from|Valid through|Sources|Related):\s*(.*)$", ln)
        if m:
            head[m.group(1)] = m.group(2)
    return head


def strip_code(text):
    text = re.sub(r"<!--.*?-->", "", text, flags=re.S)
    text = re.sub(r"```.*?```", "", text, flags=re.S)
    return re.sub(r"`[^`\n]*`", "", text)


def related_targets(val):
    out = []
    for tok in re.split(r",\s*(?![^()]*\))", val):
        tok = re.sub(r"\s*\(.*?\)", "", tok).strip().strip("`")
        if tok.endswith(".md") or "/" in tok and tok.endswith(".md"):
            out.append(tok)
    return out


LINK = re.compile(r"(?<!!)\[[^\]\n]*\]\(([^)\s]+)\)")
TICK_MD = re.compile(r"`([A-Za-z0-9_./-]+\.md)`")


def slug(h):
    """GitHub-style heading anchor."""
    h = re.sub(r"[`*_]", "", h.strip().lower())
    h = re.sub(r"[^a-z0-9 _-]", "", h)
    return h.replace(" ", "-")


_anchors = {}


def anchors(path):
    if path not in _anchors:
        s = set()
        for ln in open(path, encoding="utf-8").read().split("\n"):
            m = re.match(r"^#{1,6}\s+(.*)$", ln)
            if m:
                s.add(slug(m.group(1)))
        _anchors[path] = s
    return _anchors[path]


def known_md(ds):
    names = {os.path.basename(d) for d in ds} | {d for d in ds}
    for extra in ("00_Project_Structure.md", "TODO_Verification.md", "TODO_Build_Plan.md", "Appendices/Source_Register.md",
                  "Appendices/Source_Map.md", "Appendices/Change_Log.md", "README.md", "TL_PROGRESS.md"):
        names.add(extra)
        names.add(os.path.basename(extra))
    for root, dirs, files in os.walk(os.path.join(base, "src")):
        for f in files:
            if f.endswith(".md"):
                names.add(f)
    return names


def run(write=True):
    errors, warns = [], []
    ds = docs()
    known = known_md(ds)
    for rel in ds:
        path = os.path.join(base, *rel.split("/"))
        text = open(path, encoding="utf-8").read()
        head = header(text)
        for fld in HEADER_FIELDS:
            if fld not in head or not head[fld].strip():
                errors.append((rel, "missing header field: " + fld))
        sl = head.get("Spoiler level", "")
        if sl and not re.match(r"[0-3]|mixed", sl):
            errors.append((rel, "spoiler level does not start with 0-3: " + sl[:40]))
        for t in related_targets(head.get("Related", "")):
            if not os.path.exists(os.path.normpath(os.path.join(os.path.dirname(path), t))):
                errors.append((rel, "Related link not found: " + t))
        for ln, msg in spoiler_tags.parse(text)[1]:
            errors.append((rel, "spoiler tag, line %d: %s" % (ln, msg)))
        plain = strip_code(text)
        for m in CITE.finditer(text):
            b, c = int(m.group(1)), int(m.group(2))
            ch = chapter_lines(b, c)
            if not ch:
                errors.append((rel, "cite names a missing chapter: " + m.group(0)))
                continue
            n = len(ch[0])
            for lm in LREF.finditer(m.group(3)):
                hi = int(lm.group(2) or lm.group(1))
                lo = int(lm.group(1))
                if lo < 1 or hi > n or hi < lo:
                    errors.append((rel, "cite line out of range (chapter has %d lines): %s" % (n, m.group(0))))
                    break
        for m in LINK.finditer(plain):
            tgt = m.group(1)
            if re.match(r"[a-z]+:", tgt):
                continue
            fpart, _, frag = tgt.partition("#")
            dest = path if not fpart else os.path.normpath(os.path.join(os.path.dirname(path), fpart))
            if not os.path.exists(dest):
                errors.append((rel, "link target not found: " + tgt))
            elif frag and dest.endswith(".md") and frag.lower() not in anchors(dest):
                errors.append((rel, "link anchor not found: " + tgt))
        for m in TICK_MD.finditer(re.sub(r"```.*?```", "", text, flags=re.S)):
            nm = m.group(1)
            if "NN" in nm or "N_" in nm:
                continue
            if nm not in known and os.path.basename(nm) not in known and not os.path.exists(os.path.join(base, *nm.split("/"))):
                warns.append((rel, "backticked file not found: " + nm))
        for m in BAD_CITE.finditer(text):
            warns.append((rel, "non-standard cite form: " + m.group(0)))
        for i, ln in enumerate(plain.split("\n"), 1):
            if "->" in ln or " w/ " in ln:
                warns.append((rel, "shorthand on line %d: %s" % (i, ln.strip()[:60])))
    # overview coverage
    for rel in ds:
        d = os.path.dirname(rel)
        name = os.path.basename(rel)
        if not d or re.match(r"00_.*Overview\.md$", name):
            continue
        ovs = [f for f in os.listdir(os.path.join(base, *d.split("/"))) if re.match(r"00_.*Overview\.md$", f)]
        if not ovs:
            continue
        ov = open(os.path.join(base, *d.split("/"), ovs[0]), encoding="utf-8").read().lower()
        stem = name[:-3].lower()
        if stem not in ov and stem.replace("_", " ") not in ov:
            warns.append((rel, "not mentioned by " + d + "/" + ovs[0]))
    import overviews
    for ov in overviews.run(check=True):
        errors.append((ov, "generated file list is out of date: run python3 src/tools/overviews.py"))
    if write:
        L = ["# Lint report", "",
             "Generated by `src/tools/lint.py` (also run at the end of `build_register.py`). %d documents checked: %d errors, %d warnings." % (len(ds), len(errors), len(warns)), ""]
        for title, items in (("Errors", errors), ("Warnings", warns)):
            L += ["## " + title, ""]
            L += ["- `%s`: %s" % (f, m) for f, m in items] or ["None."]
            L.append("")
        open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "lint_report.md"), "w", encoding="utf-8").write("\n".join(L))
    return errors, warns, len(ds)


if __name__ == "__main__":
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
    e, w, n = run()
    print("lint: %d documents, %d errors, %d warnings (see src/tools/lint_report.md)" % (n, len(e), len(w)))

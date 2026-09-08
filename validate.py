#!/usr/bin/env python3
"""
Checks a Tutors course folder against the naming conventions in the reference
manual, before you spend a build on it.

    python3 validate.py            # checks the folder it sits in
    python3 validate.py ../other   # checks somewhere else

Catches the failures that produce a course which builds but renders wrong:
a talk whose PDF name does not match its markdown, a web link with no weburl,
a unit with no title file, spaces in a folder name.
"""

import sys
from pathlib import Path

IMG = {".png", ".jpg", ".jpeg", ".gif", ".svg"}

# folder prefix -> (needs a .md, needs a companion file of these types)
CARD_RULES = {
    "talk": {".pdf", ".marp"},      # or a videoid, handled below
    "paneltalk": {".pdf"},
    "tutorial": {".pdf", None},     # PDF tutorial or markdown-only tutorial
    "book": None,                   # multi-step lab, or a PDF lab
    "note": None,
    "panelnote": None,
    "web": {"weburl"},
    "github": {"githubid"},
    "archive": {".zip"},
    "notebook": {".ipynb"},
    "podcast": {"episode"},
    "panelvideo": {"videoid"},
}

CONTAINERS = ("topic", "unit", "side")

errors, warnings = [], []


def err(p, msg):
    errors.append(f"  ERROR  {p}\n         {msg}")


def warn(p, msg):
    warnings.append(f"  WARN   {p}\n         {msg}")


def md_files(d: Path):
    return [f for f in d.iterdir() if f.is_file() and f.suffix == ".md"]


def check_root(root: Path):
    if not (root / "course.md").exists():
        err(root, "course.md is mandatory \u2014 it supplies the course title.")
    if not (root / "properties.yaml").exists():
        err(root, "properties.yaml is mandatory \u2014 it must contain at least `credits:`.")
    else:
        text = (root / "properties.yaml").read_text(encoding="utf-8")
        if "credits" not in text:
            err(root / "properties.yaml", "no `credits:` entry; it renders as the course subtitle.")
    has_img = any((root / f"course{e}").exists() for e in IMG)
    props = (root / "properties.yaml").read_text(encoding="utf-8") if (root / "properties.yaml").exists() else ""
    if not has_img and "icon:" not in props:
        warn(root, "no course image and no `icon:` in properties.yaml; the course card will fall back to a default.")


def check_container(d: Path, kind: str):
    """topic / unit / side folders need exactly one .md carrying the title."""
    mds = md_files(d)
    if not mds:
        err(d, f"a {kind} folder needs a .md file holding its title (e.g. {kind}.md).")
    elif len(mds) > 1:
        warn(d, f"more than one .md at {kind} level: {[m.name for m in mds]}. Tutors reads one title.")


def check_card(d: Path, prefix: str):
    stem_mds = md_files(d)
    if not stem_mds:
        err(d, f"`{prefix}-*` folder has no .md file; the card has no title or summary.")
        return
    md = stem_mds[0]
    rule = CARD_RULES.get(prefix)
    if rule is None:
        return

    names = {f.name for f in d.iterdir() if f.is_file()}
    suffixes = {f.suffix for f in d.iterdir() if f.is_file()}

    # video-only talks are legal: a talk with a videoid and no PDF
    if prefix == "talk" and "videoid" in names:
        return
    if prefix == "tutorial" and None in rule:
        return  # markdown tutorial is fine

    wanted = {r for r in rule if r}
    matched = any((r in names) or (r in suffixes) for r in wanted)
    if not matched:
        pretty = ", ".join(sorted(wanted))
        err(d, f"`{prefix}-*` folder is missing its companion file ({pretty}).")
        return

    # name-matching rule: the payload must share the markdown file's stem
    for ext in (".pdf", ".marp", ".zip", ".ipynb"):
        payloads = [f for f in d.iterdir() if f.suffix == ext]
        for p in payloads:
            if p.stem != md.stem:
                err(p, f"filename must match `{md.name}` exactly \u2014 expected `{md.stem}{ext}`.")

    for img in [f for f in d.iterdir() if f.suffix.lower() in IMG]:
        if img.stem != md.stem:
            warn(img, f"card image should be named `{md.stem}{img.suffix}` to be picked up.")


def check_lab(d: Path):
    """book-* folders holding markdown steps: NN.ShortTitle.md"""
    steps = sorted(f for f in d.iterdir() if f.suffix == ".md")
    if not steps:
        if not any(f.suffix == ".pdf" for f in d.iterdir()):
            err(d, "`book-*` folder has neither markdown steps nor a PDF.")
        return
    for s in steps:
        parts = s.name.split(".")
        if len(parts) != 3:
            warn(s, "lab steps are named [sort-key].[short-title].md, e.g. 01.Profile.md")
        elif not parts[0].isdigit():
            warn(s, f"sort key `{parts[0]}` is not numeric; steps sort alphabetically.")


def walk(d: Path, root: Path):
    for child in sorted(d.iterdir()):
        if not child.is_dir() or child.name.startswith(".") or child.name in {"json", "html"}:
            continue
        name = child.name
        if " " in name:
            err(child, "folder names must not contain spaces.")

        prefix = name.split("-")[0]
        if prefix in CONTAINERS:
            check_container(child, prefix)
            walk(child, root)
        elif prefix in CARD_RULES:
            check_card(child, prefix)
            if prefix == "book":
                check_lab(child)
        elif name not in {"img", "archives"}:
            warn(child, f"folder prefix `{prefix}` is not a Tutors learning object; it will be ignored.")


def main():
    root = Path(sys.argv[1] if len(sys.argv) > 1 else __file__).resolve()
    if root.is_file():
        root = root.parent
    print(f"Validating {root}\n")

    check_root(root)
    walk(root, root)

    topics = sorted(p.name for p in root.iterdir() if p.is_dir() and p.name.startswith("topic"))
    print(f"  {len(topics)} topics")
    for t in topics:
        print(f"    {t}")
    print()

    for w in warnings:
        print(w)
    for e in errors:
        print(e)

    print(f"\n{len(errors)} errors, {len(warnings)} warnings")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())

#!/usr/bin/env python3
"""Audit skill references and report missing files."""

import re
from pathlib import Path

root = Path(r"C:\Users\bernh\OneDrive\dev_oc\bernhard-zechmann-skills\skills")

for skill_path in sorted(root.rglob("SKILL.md")):
    text = skill_path.read_text(encoding="utf-8")
    refs = set(
        re.findall(
            r"`([^`]*(?:references|scripts|agents|evals|assets|examples|tools)/[^`]*)`",
            text,
        )
    )
    if refs:
        print(f"\n{skill_path.relative_to(root)}:")
        for r in sorted(refs):
            exists = (skill_path.parent / r).exists()
            status = "OK" if exists else "MISSING"
            print(f"  {r} [{status}]")

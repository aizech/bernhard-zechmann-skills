#!/usr/bin/env python3
"""Sync bundled files from source skills to the new repo."""

import shutil
import sys
from pathlib import Path

REPO_ROOT = Path(r"C:\Users\bernh\OneDrive\dev_oc\bernhard-zechmann-skills")
SKILLS_DIR = REPO_ROOT / "skills"
WORKSPACE_ROOT = Path(r"C:\Users\bernh\OneDrive\dev_oc")

EXCLUDED_DIRS = {".git", "__pycache__", ".venv", "node_modules"}
EXCLUDED_FILES = {"SKILL.md", ".gitignore", "README.md"}  # Keep tightened SKILL.md; skip repo-level README


def find_source(skill_name: str) -> Path | None:
    """Find a source directory for the skill in the workspace."""
    candidates = [
        WORKSPACE_ROOT / "agent-blogger" / "skills" / skill_name,
        WORKSPACE_ROOT / "agent-skiller" / "skills" / skill_name,
        WORKSPACE_ROOT / "my-skills" / skill_name,
        WORKSPACE_ROOT / "agent-audio" / "skills" / skill_name,
        WORKSPACE_ROOT / "agent-scratch" / "skills" / skill_name,
        WORKSPACE_ROOT / "agent-scratch-master" / "skills" / skill_name,
    ]
    for candidate in candidates:
        if candidate.exists() and candidate.is_dir() and candidate != (SKILLS_DIR / skill_name):
            return candidate
    return None


def copy_bundled_files(src: Path, dst: Path) -> list[Path]:
    """Copy non-SKILL.md files from src to dst, preserving structure."""
    copied: list[Path] = []
    for item in src.rglob("*"):
        if item.is_dir():
            continue
        rel = item.relative_to(src)
        if rel.name in EXCLUDED_FILES:
            continue
        if any(part in EXCLUDED_DIRS for part in rel.parts):
            continue
        target = dst / rel
        target.parent.mkdir(parents=True, exist_ok=True)
        if target.exists():
            continue
        shutil.copy2(item, target)
        copied.append(target)
    return copied


def main() -> int:
    """Sync bundled files for all skills and report."""
    skills = sorted(p for p in SKILLS_DIR.rglob("SKILL.md") if p.parent != SKILLS_DIR)
    total_copied = 0
    for skill_path in skills:
        skill_name = skill_path.parent.name
        src = find_source(skill_name)
        if src is None:
            print(f"No source found for {skill_name}")
            continue
        copied = copy_bundled_files(src, skill_path.parent)
        if copied:
            print(f"\n{skill_name}: copied {len(copied)} files")
            for f in copied:
                print(f"  {f.relative_to(REPO_ROOT)}")
            total_copied += len(copied)
    print(f"\nTotal copied: {total_copied}")
    return 0


if __name__ == "__main__":
    sys.exit(main())

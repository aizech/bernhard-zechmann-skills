#!/usr/bin/env python3
"""Validate the bernhard-zechmann-skills repo."""

import json
import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).parent.parent
SKILLS_DIR = REPO_ROOT / "skills"
PUBLIC_BUCKETS = {"engineering", "productivity", "misc"}
REQUIRED_FRONTMATTER = {"name", "description", "license", "compatibility"}


def get_public_skills() -> set[str]:
    """Return public skill names from disk."""
    skills = set()
    for bucket in PUBLIC_BUCKETS:
        for path in (SKILLS_DIR / bucket).glob("*/SKILL.md"):
            skills.add(path.parent.name)
    return skills


def get_plugin_skills() -> set[str]:
    """Return skill names listed in .claude-plugin/plugin.json."""
    plugin_path = REPO_ROOT / ".claude-plugin" / "plugin.json"
    data = json.loads(plugin_path.read_text(encoding="utf-8"))
    return {Path(p).name for p in data.get("skills", [])}


def get_readme_skills() -> set[str]:
    """Return skill names referenced in top-level README.md."""
    readme = (REPO_ROOT / "README.md").read_text(encoding="utf-8")
    pattern = re.compile(r"- `([a-z0-9-]+)` —")
    return set(pattern.findall(readme))


def check_frontmatter(skill_path: Path) -> list[str]:
    """Return errors for missing required frontmatter."""
    text = skill_path.read_text(encoding="utf-8")
    if not text.startswith("---"):
        return ["missing frontmatter"]
    end = text.find("---", 3)
    if end == -1:
        return ["missing frontmatter closing"]
    frontmatter = text[3:end]
    errors = []
    for key in REQUIRED_FRONTMATTER:
        if f"{key}:" not in frontmatter:
            errors.append(f"missing frontmatter key: {key}")
    return errors


def check_emojis(text: str) -> list[str]:
    """Return lines containing emoji characters."""
    emoji_pattern = re.compile(
        "["
        "\U0001F300-\U0001F5FF"
        "\U0001F600-\U0001F64F"
        "\U0001F680-\U0001F6FF"
        "\U0001F700-\U0001F77F"
        "\U0001F780-\U0001F7FF"
        "\U0001F800-\U0001F8FF"
        "\U0001F900-\U0001F9FF"
        "\U0001FA00-\U0001FA6F"
        "\U0001FA70-\U0001FAFF"
        "\U0001FB00-\U0001FBFF"
        "\U00002600-\U000026FF"
        "\U00002700-\U000027BF"
        "]+",
        flags=re.UNICODE,
    )
    return [line for line in text.splitlines() if emoji_pattern.search(line)]


def main() -> int:
    """Run validation and return exit code."""
    errors: list[str] = []

    public = get_public_skills()
    plugin = get_plugin_skills()
    readme = get_readme_skills()

    missing_from_plugin = public - plugin
    if missing_from_plugin:
        errors.append(
            f"Public skills missing from plugin.json: {sorted(missing_from_plugin)}"
        )

    extra_in_plugin = plugin - public
    if extra_in_plugin:
        errors.append(
            f"Plugin.json lists non-existent skills: {sorted(extra_in_plugin)}"
        )

    missing_from_readme = public - readme
    if missing_from_readme:
        errors.append(
            f"Public skills missing from README.md: {sorted(missing_from_readme)}"
        )

    for skill_path in SKILLS_DIR.rglob("SKILL.md"):
        frontmatter_errors = check_frontmatter(skill_path)
        for error in frontmatter_errors:
            errors.append(f"{skill_path}: {error}")

        emoji_lines = check_emojis(skill_path.read_text(encoding="utf-8"))
        for line in emoji_lines:
            errors.append(f"{skill_path}: emoji found: {line.strip()}")

    if errors:
        print("Validation failed:")
        for error in errors:
            print(f"  - {error}")
        return 1

    print("Validation passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())

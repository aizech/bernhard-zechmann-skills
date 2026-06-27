# Agent Guidelines for This Repo

This file guides any agent working inside `bernhard-zechmann-skills`.

## Repo Structure

Skills are organized into buckets under `skills/`:

- `engineering/` — daily code work
- `productivity/` — daily non-code workflow tools
- `misc/` — kept around but rarely used
- `personal/` — tied to my own setup, not promoted
- `in-progress/` — drafts not yet ready to ship
- `deprecated/` — no longer used

Every skill in `engineering/`, `productivity/`, or `misc/` must appear in the top-level `README.md` and in `.claude-plugin/plugin.json`. Skills in `personal/`, `in-progress/`, and `deprecated/` must not appear in either.

## Skill Format

Every `SKILL.md` starts with frontmatter:

```yaml
---
name: skill-name
description: One-line description of when to use this skill.
license: MIT
compatibility: claude-code opencode github-copilot devin pi cursor
---
```

User-invoked skills also include:

```yaml
disable-model-invocation: true
```

## Writing Rules

- Use Lucide icons only. No emojis or Material icons in code or UI strings.
- Keep descriptions concise. One sentence beats a paragraph.
- Link to other skills with relative paths: `./skills/engineering/tdd/SKILL.md`.
- Include examples only when they make the skill clearer.
- Avoid generic AI filler. Prefer plain, direct language.

## Adding a Skill

1. Pick the right bucket.
2. Create a folder with a `SKILL.md`.
3. Add the skill to the bucket's `README.md` and the top-level `README.md`.
4. Add public skills to `.claude-plugin/plugin.json`.
5. Update `CHANGELOG.md`.

## Multi-Agent Support

- **Claude Code:** `.claude-plugin/plugin.json`
- **OpenCode:** `.opencode/skills/`
- **GitHub Copilot:** `.github/copilot-instructions.md`
- **Devin:** `.devin/devin.md`
- **Pi:** plain markdown `SKILL.md` files
- **Cursor:** `.cursor/skills/`

Keep skills agent-agnostic. Add agent-specific manifests only when the format differs.

# Contributing

## Adding a Skill

1. Pick the right bucket.
2. Create a folder with a `SKILL.md`.
3. Add required frontmatter:
   - `name`
   - `description`
   - `license: MIT`
   - `compatibility: claude-code opencode github-copilot devin pi`
   - `disable-model-invocation: true` for user-invoked skills
4. Add the skill to the bucket's `README.md` and the top-level `README.md`.
5. Add public skills to `.claude-plugin/plugin.json`.
6. Update `CHANGELOG.md`.
7. Run a linter or manual check for emojis and Material icons.

## Editing a Skill

- Keep the skill focused on one responsibility.
- Tighten the prose. Remove filler.
- Update examples if the skill behavior changes.
- Update `CHANGELOG.md`.

## Buckets

- `engineering/` — code work
- `productivity/` — writing, marketing, research
- `misc/` — occasional tools
- `personal/` — tied to my setup, not promoted
- `in-progress/` — drafts not yet ready
- `deprecated/` — retired skills

Public skills live only in `engineering/`, `productivity/`, and `misc/`.

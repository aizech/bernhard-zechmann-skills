# Multi-Agent Support

These skills are written as plain markdown files with frontmatter. They are agent-agnostic by default. Agent-specific manifests are added when the format requires it.

## Agents

### Claude Code

- Reads `.claude-plugin/plugin.json`.
- Each skill is a folder with a `SKILL.md`.
- Only public skills are listed in `plugin.json`.

### OpenCode

- Reads `.opencode/skills/<skill-name>/SKILL.md`.
- The `.opencode/skills/README.md` index lists public skills.

### GitHub Copilot

- Reads `.github/copilot-instructions.md`.
- Copilot uses the instructions as context, not as a strict skill registry.

### Devin

- Reads `.devin/devin.md`.
- Devin uses the file as high-level instructions for the repo.

### Pi

- Pi has no dedicated skill format.
- Plain markdown `SKILL.md` files are readable when Pi can load them.

### Cursor

- Reads `.cursor/skills/<skill-name>/SKILL.md`.
- The `.cursor/skills/README.md` index lists public skills.

## Adding a New Agent

1. Add a new agent-specific manifest or instructions file.
2. Keep the canonical skill in `skills/<bucket>/<skill-name>/SKILL.md`.
3. Do not duplicate skill logic unless the agent format requires it.

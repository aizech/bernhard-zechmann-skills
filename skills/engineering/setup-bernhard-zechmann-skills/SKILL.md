---
name: setup-bernhard-zechmann-skills
description: Configure the bernhard-zechmann-skills repo for a project. Run once before using the other skills.
disable-model-invocation: true
license: MIT
compatibility: claude-code opencode github-copilot devin pi
---

# Setup Bernhard Zechmann Skills

Run this once per project to wire the skills into your workflow.

## Questions

1. **Issue tracker**: GitHub, Linear, or local files?
2. **Triage labels**: What labels do you use when triaging work?
3. **Docs location**: Where should `CONTEXT.md`, ADRs, and specs live?
4. **Agents**: Which agents will use this repo? (Claude Code, OpenCode, Copilot, Devin, Pi)

## Actions

1. Create or update the target project's `AGENTS.md` with the chosen tracker and doc paths.
2. Copy the relevant agent manifest into the project:
   - Claude Code: `.claude-plugin/plugin.json`
   - OpenCode: `.opencode/skills/`
   - GitHub Copilot: `.github/copilot-instructions.md`
   - Devin: `.devin/devin.md`
   - Pi: plain `SKILL.md` references
3. Create a `CONTEXT.md` in the project root if it does not exist.
4. Report what was configured and what the next skill should be.

# Bernhard Zechmann's Agent Skills

Agent skills I use daily for coding, marketing, and writing. They are small, composable, and designed to work across any model or agent.

## Quickstart

Install via skills.sh:

```bash
npx skills@latest add bernhardzechmann/skills
```

Then run `/setup-bernhard-zechmann-skills` in your agent to configure the repo.

## Why These Skills Exist

Most agent failures come from three gaps:

1. **Misalignment** — what I want and what the agent builds are different.
2. **Drift** — skills live scattered across projects and are hard to discover.
3. **Weak feedback loops** — the agent works without tests, context, or review.

These skills fix that by giving the agent a shared vocabulary, clear disciplines, and focused tools.

## Reference

Skills are grouped into buckets. **User-invoked** skills only run when you type them. **Model-invoked** skills can be reached automatically by the agent when the task fits.

### Engineering

Skills for daily code work.

**User-invoked**

- `setup-bernhard-zechmann-skills` — Configure this skill repo for a project.
- `skill-creator` — Create a new skill from a pattern.
- `cli-creator` — Build a composable CLI from docs, specs, or scripts.
- `mcp-builder` — Create an MCP server from an API or SDK.
- `ai-agent-builder` — Build an agent with tools, memory, and reasoning.

**Model-invoked**

- `tdd` — Red-green-refactor test-driven development.
- `browser-automation` — Automate browser tasks with Playwright or Puppeteer.
- `playwright` — Test web apps with Playwright.

### Productivity

Skills for writing, marketing, and research.

**User-invoked**

- `humanizer` — Remove AI-generated patterns from text.
- `geo` — Optimize a website for AI search engines.
- `web-research` — Research a topic across multiple sources.
- `seo-audit` — Audit a website for technical SEO issues.
- `competitor-analysis` — Analyze a competitor's SEO/GEO strategy.
- `technical-blog-writer` — Write a technical blog post from research.

**Model-invoked**

- `find-skills` — Discover which skill fits a task.
- `caveman` — Compress communication into ultra-concise mode.

### Misc

Tools kept around but used less often.

- `free-search-aggregator` — Search across multiple providers with failover.
- `openai-whisper` — Transcribe audio locally with Whisper.

### Personal

Skills tied to my own setup. Not promoted for general use.

- `kaleko-poet` — Write German poetry in the style of Mascha Kaleko.
- `agent-interview` — Generate and conduct agent interviews.

### In-Progress

Drafts not yet ready to ship.

- `minimal-design-system` — Create a minimal design system.
- `hooked-framework` — Apply the Hooked model to product writing.
- `brainstorming` — Structured ideation before implementation.
- `scratch-coder` — Create Scratch projects with Python.

### Deprecated

No longer used.

## Agent Support

- **Claude Code:** `.claude-plugin/plugin.json`
- **OpenCode:** `.opencode/skills/`
- **GitHub Copilot:** `.github/copilot-instructions.md`
- **Devin:** `.devin/devin.md`
- **Pi:** plain markdown `SKILL.md` files
- **Cursor:** `.cursor/skills/`

## License

MIT

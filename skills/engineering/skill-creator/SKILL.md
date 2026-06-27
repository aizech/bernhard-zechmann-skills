---
name: skill-creator
description: Create a new skill or improve an existing one. Use when the user wants to capture a workflow as a reusable skill, edit a skill, or optimize its triggering.
license: MIT
compatibility: claude-code opencode github-copilot devin pi
---

# Skill Creator

Capture a workflow as a reusable skill, then test and tighten it.

## Process

### 1. Capture intent

Ask:

- What should the skill enable the agent to do?
- When should it trigger? Which phrases or contexts?
- What is the expected output format?
- Should we add test cases? (Yes for deterministic outputs; optional for subjective ones.)

### 2. Write the SKILL.md

Create a folder with the skill name and a `SKILL.md`:

```yaml
---
name: skill-name
description: When to trigger and what it does. Be specific.
license: MIT
compatibility: claude-code opencode github-copilot devin pi
---
```

Body rules:

- One responsibility per skill.
- Imperative instructions.
- Include examples only when they clarify.
- Keep it under 250 lines. Split into `references/` if it grows.
- No emojis or Material icons.

### 3. Create test cases

Write 2–3 realistic prompts a user would actually say. Save them to `evals/evals.json`:

```json
{
  "skill_name": "example-skill",
  "evals": [
    {
      "id": 1,
      "prompt": "User's realistic task",
      "expected_output": "Description of expected result",
      "files": []
    }
  ]
}
```

### 4. Run and evaluate

For each test case:

1. Run the skill against the prompt.
2. Run a baseline without the skill if needed.
3. Capture outputs and timing.
4. Review with the user. Use a viewer or inline comparison when subagents are not available.

### 5. Iterate

- Fix the biggest failure first.
- Remove instructions that do not pull their weight.
- Explain the why, not just the what.
- Avoid overfit changes that only help the test cases.

### 6. Optimize the description

When the skill is stable, tune the `description` frontmatter so the agent triggers it reliably on real prompts. Use a mix of should-trigger and should-not-trigger examples.

## Reference

- Progressive disclosure: metadata, SKILL.md body, bundled resources.
- Keep bundled resources in `scripts/`, `references/`, or `assets/`.

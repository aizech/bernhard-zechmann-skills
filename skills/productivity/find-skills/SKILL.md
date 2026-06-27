---
name: find-skills
description: Help the user discover and install agent skills. Use when the user asks how to do something that might have an existing skill, or says "find a skill for X" or "is there a skill that can...".
license: MIT
compatibility: claude-code opencode github-copilot devin pi cursor
---

# Find Skills

Discover and install skills from the open agent skills ecosystem.

## Skills CLI

- `npx skills find [query]` — search for skills
- `npx skills add <package>` — install a skill
- `npx skills check` — check for updates
- `npx skills update` — update all skills

Browse at https://skills.sh/.

## How to help

1. Understand the domain and task.
2. Check the skills.sh leaderboard for well-known skills.
3. If not found, run `npx skills find [query]`.
4. Verify quality before recommending:
   - Prefer 1K+ installs
   - Prefer official sources
   - Check GitHub stars
5. Present options with name, install count, install command, and link.
6. Offer to install with `npx skills add <owner/repo@skill> -g -y`.

## If no skills match

1. Acknowledge that no skill was found.
2. Offer to help directly.
3. Suggest creating a skill with `npx skills init`.

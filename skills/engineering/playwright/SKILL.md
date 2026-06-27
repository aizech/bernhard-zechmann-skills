---
name: playwright
description: Drive a real browser from the terminal for navigation, form filling, snapshots, screenshots, and UI debugging. Use when the user wants terminal-first browser automation with Playwright.
license: MIT
compatibility: claude-code opencode github-copilot devin pi
---

# Playwright CLI

Drive a real browser from the terminal using Playwright.

## Prerequisite

Check for `npx`:

```bash
command -v npx >/dev/null 2>&1
```

If missing, ask the user to install Node.js/npm.

## Quick start

Use the wrapper script or `npx` directly:

```bash
npx --package @playwright/cli playwright-cli open https://example.com --headed
npx --package @playwright/cli playwright-cli snapshot
npx --package @playwright/cli playwright-cli click e3
npx --package @playwright/cli playwright-cli screenshot
```

## Core workflow

1. Open the page.
2. Snapshot to get stable element refs.
3. Interact using refs from the latest snapshot.
4. Re-snapshot after navigation or big DOM changes.
5. Capture artifacts when useful.

## Re-snapshot after

- Navigation
- Clicking elements that change the UI
- Opening/closing modals or menus
- Tab switches

Refs can go stale. When a command fails, snapshot again.

## Patterns

**Form fill and submit**

```bash
npx --package @playwright/cli playwright-cli open https://example.com/form
npx --package @playwright/cli playwright-cli snapshot
npx --package @playwright/cli playwright-cli fill e1 "user@example.com"
npx --package @playwright/cli playwright-cli fill e2 "password123"
npx --package @playwright/cli playwright-cli click e3
npx --package @playwright/cli playwright-cli snapshot
```

**Debug with traces**

```bash
npx --package @playwright/cli playwright-cli open https://example.com --headed
npx --package @playwright/cli playwright-cli tracing-start
# ...interactions...
npx --package @playwright/cli playwright-cli tracing-stop
```

## Guardrails

- Snapshot before referencing element ids.
- Prefer explicit CLI commands over arbitrary code execution.
- Use `--headed` when a visual check helps.
- Default to CLI commands, not Playwright test specs.

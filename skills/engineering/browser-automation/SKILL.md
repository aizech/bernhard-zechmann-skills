---
name: browser-automation
description: Automate browser interactions for scraping, testing, and workflows. Use when the user wants to navigate pages, fill forms, extract data, or take screenshots with Puppeteer or Playwright.
license: MIT
compatibility: claude-code opencode github-copilot devin pi cursor
---

# Browser Automation

Automate browser tasks for scraping, testing, and workflows.

## Core capabilities

- **Navigation**: load URLs, wait for selectors, scroll, handle navigation.
- **Interaction**: click, type, select, upload files.
- **Extraction**: read text, attributes, tables, or lists.
- **Capture**: screenshots, PDFs, and traces.

## Workflow

1. Open the page.
2. Wait for the right selector.
3. Interact with elements.
4. Extract or capture the result.
5. Handle pagination or repeated steps with clear bounds.

## Best practices

- Use stable selectors like `data-testid` instead of CSS paths.
- Wait for elements before interacting.
- Add human-like delays when mimicking real users.
- Respect rate limits and robots.txt.
- Capture screenshots on failure.
- Use headless mode for production.

## Example

```javascript
await page.goto('https://example.com/login');
await page.fill('#email', 'user@example.com');
await page.fill('#password', 'securepass');
await page.click('button[type="submit"]');
await page.waitForNavigation();
```

## Guardrails

- Do not scrape behind authentication unless explicitly asked.
- Do not run aggressive crawlers without rate limiting.
- Keep personal data out of logs and screenshots.

---
name: geo
description: Optimize a website for AI-powered search engines. Use when the user mentions GEO, AI search, AI SEO, AI visibility, Perplexity, ChatGPT Search, Google AI Overviews, or provides a URL for AI search optimization.
license: MIT
compatibility: claude-code opencode github-copilot devin pi
---

# GEO

Optimize websites for AI-powered search engines.

## When to use

- Audit a site for AI search visibility.
- Check if AI crawlers can access a site.
- Analyze or generate schema markup.
- Optimize content for AI citation.
- Generate GEO recommendations.

## Workflow

1. **Discovery**: fetch homepage, detect business type, check robots.txt, fetch sitemap.
2. **Analysis**: score these areas:
   - AI crawler access
   - Structured data
   - Content citability
   - Technical foundations
   - Brand signals
   - llms.txt presence
3. **Report**: output a markdown report with score, breakdown, critical issues, and prioritized actions.

## Scoring

| Category | Weight |
|----------|--------|
| AI crawler access | 20 |
| Structured data | 20 |
| Content citability | 20 |
| Technical | 15 |
| Brand signals | 15 |
| llms.txt | 10 |

## Critical crawlers

- GPTBot
- OAI-SearchBot
- ClaudeBot
- PerplexityBot

## Must-have schema

- Organization
- WebSite + SearchAction
- Business type: LocalBusiness, Product, SoftwareApplication, or Article

## Output

Generate `GEO-AUDIT-REPORT.md` with:

- Overall score and rating
- Score breakdown
- Critical issues
- Prioritized recommendations
- Technical details

## Limits

- Max 5 pages per audit
- 10 seconds timeout per page
- Respect robots.txt
- 1 second between requests

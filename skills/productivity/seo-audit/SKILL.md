---
name: seo-audit
description: Audit a website for technical, on-page, and content SEO issues. Use when the user mentions SEO audit, technical SEO, rankings drop, page speed, Core Web Vitals, crawl errors, or indexing issues.
license: MIT
compatibility: claude-code opencode github-copilot devin pi
---

# SEO Audit

Identify SEO issues and provide actionable recommendations.

## Before starting

Ask:

- What type of site is it? (SaaS, e-commerce, blog, local)
- What are the priority pages or keywords?
- Any known issues or recent changes?
- Search Console or analytics access?

## Priority order

1. Crawlability and indexation
2. Technical foundations
3. On-page optimization
4. Content quality
5. Authority and links

## Technical checks

- **robots.txt**: no unintentional blocks, sitemap reference
- **Sitemap**: valid, submitted, indexable URLs
- **Indexation**: `site:domain`, canonicals, noindex, soft 404s
- **Core Web Vitals**: LCP < 2.5s, INP < 200ms, CLS < 0.1
- **Mobile**: responsive, viewport, tap targets
- **HTTPS**: valid certificate, no mixed content, redirects
- **URL structure**: lowercase, hyphens, no unnecessary parameters

## On-page checks

- Unique title tags (50-60 chars)
- Unique meta descriptions (150-160 chars)
- One H1 per page with primary keyword
- Image alt text, compressed, modern formats
- Internal linking, no orphan pages
- Clear keyword targeting without cannibalization

## Content checks

- E-E-A-T signals: experience, expertise, authority, trust
- Sufficient depth for the topic
- Updated and current information
- No thin or duplicate content

## International SEO

- Self-referencing hreflang with return tags
- Valid language-region codes
- `x-default` present
- No cross-locale canonicals

## Schema markup

`web_fetch` and `curl` cannot reliably detect JS-injected JSON-LD. Use a browser tool, Google's Rich Results Test, or a rendered export.

## Output

Produce a report with:

- Executive summary and top 3-5 priorities
- Technical findings (issue, impact, evidence, fix, priority)
- On-page findings
- Content findings
- Prioritized action plan

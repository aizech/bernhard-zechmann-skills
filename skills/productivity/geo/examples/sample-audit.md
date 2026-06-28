# GEO Audit Report Example

Example output format for a GEO audit. This demonstrates what the skill produces.

---

# GEO Audit Report: example-saas.com

**Date:** March 29, 2026
**GEO Score:** 62/100 (Foundation)
**Business Type:** SaaS

---

## Executive Summary

example-saas.com has solid technical foundations and allows major AI crawlers, but is missing critical structured data (Organization schema, sameAs links) and has content that could be better optimized for AI citation. The site appears in search results but lacks the entity signals AI systems need for strong citation in AI-generated responses.

**Top Priority:** Add Organization schema with sameAs links, optimize content for answer-first structure.

---

## Score Breakdown

| Category | Score | Status |
|----------|-------|--------|
| AI Crawler Access | 16/20 |  Good |
| Structured Data | 8/20 |  Needs Work |
| Content Citability | 14/20 | ️ Fair |
| Technical | 12/15 |  Good |
| Brand Signals | 6/15 |  Needs Work |
| llms.txt | 6/10 | ️ Not Found |

**Total: 62/100** - Foundation

---

## Critical Issues

###  High Priority

1. **Missing Organization Schema**
   - No JSON-LD Organization type found
   - AI cannot properly identify the business entity
   - Add Organization schema with sameAs links

2. **No sameAs Links**
   - Zero external platform links in schema
   - Weak entity recognition across AI platforms
   - Add Wikipedia, LinkedIn, Twitter, GitHub links

3. **Content Not Answer-First**
   - Homepage leads with marketing copy instead of clear value proposition
   - AI prefers direct answers in first 100 words

###  Medium Priority

4. **No Author Schema**
   - Blog posts lack author attribution with credentials
   - Add Person schema with sameAs to expertise pages

5. **No llms.txt File**
   - Missing emerging AI crawler standard
   - Create llms.txt with site overview and key pages

---

## Recommendations

### Immediate Actions (This Week)

1. **Add Organization Schema**

```json
{
  "@context": "https://schema.org",
  "@type": "Organization",
  "name": "Example SaaS",
  "url": "https://example-saas.com",
  "logo": "https://example-saas.com/logo.png",
  "description": "Example SaaS helps teams collaborate smarter with AI-powered workflows.",
  "sameAs": [
    "https://www.linkedin.com/company/example-saas",
    "https://twitter.com/examplesaas",
    "https://github.com/examplesaas"
  ],
  "knowsAbout": ["Workflow Automation", "AI Collaboration", "Team Productivity"]
}
```

2. **Allow AI Crawlers** (verify in robots.txt)
   -  GPTBot - Allowed
   -  ClaudeBot - Allowed
   -  PerplexityBot - Allowed
   -  Google-Extended - Allowed

### This Month

3. **Optimize Homepage for AI**
   - Lead with clear value proposition in first 100 words
   - Add statistics: "500+ companies trust us", "99.9% uptime"
   - Add FAQ section with direct answers

4. **Add Author Schema to Blog**
   ```json
   {
     "@type": "Person",
     "name": "Author Name",
     "jobTitle": "Head of Content",
     "sameAs": ["https://linkedin.com/in/author"]
   }
   ```

### Long-term

5. **Build Wikipedia Presence**
   - Apply for Wikipedia article
   - Add Wikidata entry

6. **Create llms.txt**
   ```
   # llms.txt
   ## About
   Example SaaS provides AI-powered workflow automation for teams.
   
   ## Products
   - Core Platform
   - API Integration
   - Enterprise Plans
   
   ## Resources
   - /blog
   - /docs
   - /pricing
   ```

---

## Technical Details

### AI Crawler Access

| Bot | Status | Notes |
|-----|--------|-------|
| GPTBot |  Allowed | Full access |
| OAI-SearchBot |  Allowed | Full access |
| ClaudeBot |  Allowed | Full access |
| PerplexityBot |  Allowed | Full access |
| Google-Extended |  Allowed | Full access |

**robots.txt:** Present, well-structured

### Detected Schemas

- WebSite (basic)
- SoftwareApplication (partial)

### Missing Schemas

- Organization 
- Person (Author) 
- FAQPage 
- BreadcrumbList 

### Technical Status

-  HTTPS enabled
-  Mobile-friendly
- ️ Server-side rendered (some JS dependencies)
- ️ Core Web Vitals need review

---

## Content Analysis

### Citability Score: 14/20

**Strengths:**
- Clear headings throughout
- Good use of bullet points
- Some statistics present

**Improvements Needed:**
- Lead with answers, not intros
- Add more data points and statistics
- Include cited sources for claims

---

## Brand Signals

| Platform | Status |
|----------|--------|
| Wikipedia |  Not found |
| Wikidata |  Not found |
| LinkedIn |  Present (not in schema) |
| Twitter/X |  Present (not in schema) |
| YouTube |  Not found |
| GitHub |  Present (not in schema) |

---

## Next Steps

1. Add Organization schema with sameAs (highest ROI)
2. Verify AI crawler access in robots.txt
3. Optimize homepage for answer-first structure
4. Add FAQ section
5. Create llms.txt file
6. Build Wikipedia presence (long-term)

---

## Score History

| Date | Score | Change |
|------|-------|--------|
| 2026-03-29 | 62 | Current |
| (after fix) | 75+ | Expected |

---

*Generated by GEO Skill*

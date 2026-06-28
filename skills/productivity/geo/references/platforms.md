# Platform-Specific Optimization Guide

Tips for optimizing visibility on each major AI search platform.

---

## ChatGPT Search

### How It Works
- Web browsing via GPTBot and OAI-SearchBot
- Citations with source links
- Sources from web search + plugins

### Key Factors for Visibility

| Factor | Priority | Notes |
|--------|----------|-------|
| GPTBot access |  Critical | Must allow in robots.txt |
| Clear answers |  Critical | Direct, factual responses |
| Fresh content |  Important | Favors recent information |
| Entity signals |  Important | Wikipedia, Wikidata presence |
| Statistics |  Important | Data points increase citation |

### Specific Recommendations

1. **Allow GPTBot** - Add to robots.txt
2. **Answer format** - Put key answers in first 100 words
3. **Cite sources** - Link to authoritative sources in content
4. **Statistics** - Include numbers, percentages, dates
5. **FAQ sections** - Direct Q&A format works well

### What ChatGPT Likes
- Clear, factual content
- Expert authorship (show credentials)
- Original data and research
- Well-structured articles with headings

---

## Perplexity

### How It Works
- Always cites sources (unique among AI search)
- Real-time web search
- Sources ranked by relevance

### Key Factors for Visibility

| Factor | Priority | Notes |
|--------|----------|-------|
| PerplexityBot access |  Critical | Must allow |
| Citation-friendly format |  Critical | Short, factual paragraphs |
| Direct answers |  Critical | Answer-first structure |
| Authority signals |  Important | Expert authors, citations |

### Specific Recommendations

1. **Allow PerplexityBot** - Highest referral traffic of AI search
2. **Answer-first structure** - Lead with the answer
3. **Paragraph length** - 50-150 words per paragraph
4. **Source citations** - Link to reputable sources
5. **Statistics and facts** - Numbers increase trust

### What Perplexity Likes
- Concise, accurate answers
- Authoritative sources cited
- Clear entity recognition
- Question-optimized headers

### Unique Advantage
Perplexity **always shows source links**. Getting cited = direct referral traffic.

---

## Claude Web Search

### How It Works
- Uses ClaudeBot for web discovery
- Citations in responses
- Less frequent than ChatGPT/Perplexity

### Key Factors for Visibility

| Factor | Priority | Notes |
|--------|----------|-------|
| ClaudeBot access |  Critical | Must allow |
| Quality content |  Critical | Thorough, well-reasoned |
| Expert attribution |  Important | Show author credentials |
| Depth |  Important | Comprehensive coverage |

### Specific Recommendations

1. **Allow ClaudeBot** - Check robots.txt
2. **Expert authorship** - Detailed author schema with credentials
3. **Comprehensive content** - Deep, thorough articles
4. **Clear structure** - Headings, lists, well-organized

### What Claude Likes
- Thoughtful, well-reasoned content
- Expert perspectives
- Clear attribution
- Nuanced analysis

---

## Google AI Overviews (SGE)

### How It Works
- Integrated into Google Search
- Gemini-powered summaries
- Multi-step reasoning

### Key Factors for Visibility

| Factor | Priority | Notes |
|--------|----------|-------|
| Google-Extended access |  Critical | Gemini training |
| Standard Googlebot |  Critical | Search ranking required |
| Structured data |  Critical | For rich results |
| E-E-A-T signals |  Critical | Experience, Expertise |
| Fresh content |  Important | Recent updates |

### Specific Recommendations

1. **Allow Google-Extended** - Does NOT affect search rankings
2. **Traditional SEO** - Still matters for AIO inclusion
3. **Schema markup** - Article, FAQ, HowTo
4. **Author credentials** - Show expertise
5. **Helpful content** - People-first content

### Important Notes
- Blocking Google-Extended does NOT remove you from Google Search
- AI Overviews pull from regular search results
- E-E-A-T is critical for YMYL topics

---

## Bing AI / Copilot

### How It Works
- Integrated into Bing search
- Citations with sources
- Uses Bing's search index

### Key Factors for Visibility

| Factor | Priority | Notes |
|--------|----------|-------|
| Bingbot access |  Critical | Standard search bot |
| BingAI-specific |  Important | Separate bot for AI |
| Traditional SEO |  Critical | Index-based |

### Specific Recommendations
1. **Standard Bing SEO** - Still applies
2. **Bing Webmaster Tools** - Submit sitemap
3. **Structured data** - Article, Organization
4. **Quality content** - Comprehensive answers

---

## Cross-Platform Optimization Checklist

### Technical (Required)

- [ ] Allow GPTBot, ClaudeBot, PerplexityBot, Google-Extended
- [ ] Server-rendered HTML (not JavaScript-only)
- [ ] Fast loading (<3 seconds)
- [ ] Mobile-friendly
- [ ] HTTPS

### Structured Data (Required)

- [ ] Organization schema with sameAs
- [ ] WebSite + SearchAction
- [ ] Business-type schema (LocalBusiness/Product/SaaS/Article)
- [ ] Author schema for content

### Content (Required)

- [ ] Answer-first structure
- [ ] Key info in first 100 words
- [ ] Statistics and data points
- [ ] Expert attribution
- [ ] Clear headings

### Authority (Long-term)

- [ ] Wikipedia presence
- [ ] Wikidata entry
- [ ] LinkedIn company page
- [ ] Industry directory listings
- [ ] Press coverage

---

## Platform Comparison

| Factor | ChatGPT | Perplexity | Claude | Google AIO |
|--------|---------|------------|--------|------------|
| Traffic Volume | Highest | High | Growing | Highest |
| Citations | Yes | Always | Yes | Sometimes |
| Training Use | Yes | Yes | Yes | Yes |
| Crawler | GPTBot | PerplexityBot | ClaudeBot | Google-Extended |
| Key Factor | Answers | Citations | Depth | Traditional SEO |
| Speed | Fast | Fast | Medium | Instant |

---

## Quick Wins by Priority

### This Week
1. Allow AI crawlers in robots.txt
2. Add Organization schema
3. Add sameAs with 3-5 links

### This Month
4. Add WebSite + SearchAction
5. Optimize content for answer-first
6. Add Author schema

### This Quarter
7. Build Wikipedia presence
8. Create comprehensive content
9. Add FAQ schema

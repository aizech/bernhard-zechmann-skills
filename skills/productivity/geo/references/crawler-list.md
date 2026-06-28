# AI Crawler Reference List

Complete reference for AI crawlers that access websites for search, training, and AI features.

---

## Tier 1: Critical for AI Search Visibility

These crawlers power the AI search products where users actively find answers. **ALWAYS ALLOW** for maximum visibility.

### GPTBot

- **Operator:** OpenAI
- **User-Agent:** `GPTBot`
- **Full String:** `Mozilla/5.0 AppleWebKit/537.36 (KHTML, like Gecko; compatible; GPTBot/1.2; +https://openai.com/gptbot)`
- **Purpose:** ChatGPT web browsing, plugins, search features
- **Impact:** Blocking = no ChatGPT Search visibility
- **Recommendation:**  **ALLOW**

### OAI-SearchBot

- **Operator:** OpenAI
- **User-Agent:** `OAI-SearchBot`
- **Full String:** `Mozilla/5.0 AppleWebKit/537.36 (KHTML, like Gecko; compatible; OAI-SearchBot/1.0; +https://docs.openai.com/bots/overview)`
- **Purpose:** ChatGPT search feature (NOT for training)
- **Impact:** Blocking = no ChatGPT Search results
- **Recommendation:**  **ALLOW**

### ChatGPT-User

- **Operator:** OpenAI
- **User-Agent:** `ChatGPT-User`
- **Full String:** `Mozilla/5.0 AppleWebKit/537.36 (KHTML, like Gecko; compatible; ChatGPT-User/1.0; +https://openai.com/bot)`
- **Purpose:** User-initiated URL browsing in ChatGPT
- **Impact:** Blocking = users can't browse your site via ChatGPT
- **Recommendation:**  **ALLOW**

### ClaudeBot

- **Operator:** Anthropic
- **User-Agent:** `ClaudeBot`
- **Full String:** `ClaudeBot/1.0; +https://www.anthropic.com/claude-bot`
- **Purpose:** Claude web search, citations, analysis
- **Impact:** Blocking = no Claude web search visibility
- **Recommendation:**  **ALLOW**

### PerplexityBot

- **Operator:** Perplexity AI
- **User-Agent:** `PerplexityBot`
- **Full String:** `Mozilla/5.0 AppleWebKit/537.36 (KHTML, like Gecko; compatible; PerplexityBot/1.0; +https://perplexity.ai/perplexitybot)`
- **Purpose:** Perplexity AI search with citations
- **Impact:** Blocking = no Perplexity results (always shows sources!)
- **Recommendation:**  **ALLOW** - Best referral traffic of any AI search

---

## Tier 2: Important for AI Ecosystem

These crawlers serve large platforms. **RECOMMEND ALLOW** for broader presence.

### Google-Extended

- **Operator:** Google
- **User-Agent:** `Google-Extended`
- **Purpose:** Gemini model training, AI Overviews improvement
- **Note:** Blocking does NOT affect Google Search rankings
- **Recommendation:**  **ALLOW**

### GoogleOther

- **Operator:** Google
- **User-Agent:** `GoogleOther`
- **Purpose:** Non-search Google AI research
- **Recommendation:**  **ALLOW**

### Applebot-Extended

- **Operator:** Apple
- **User-Agent:** `Applebot-Extended`
- **Purpose:** Apple Intelligence, Siri improvement
- **Note:** Separate from standard Applebot (Siri web search)
- **Recommendation:**  **ALLOW** - 2B+ Apple devices

### Amazonbot

- **Operator:** Amazon
- **User-Agent:** `Amazonbot`
- **Purpose:** Alexa, Amazon AI features
- **Recommendation:**  **ALLOW**

### FacebookBot

- **Operator:** Meta
- **User-Agent:** `FacebookBot`
- **Purpose:** Meta AI across Facebook, Instagram, WhatsApp
- **Recommendation:**  **ALLOW** - 3B+ combined users

---

## Tier 3: Training-Only

These crawlers are for AI model training, NOT live search. **CONTEXT-DEPENDENT**.

### CCBot

- **Operator:** Common Crawl (nonprofit)
- **User-Agent:** `CCBot`
- **Full String:** `CCBot/2.0 (https://commoncrawl.org/faq/)`
- **Purpose:** Build training datasets
- **Impact:** Blocking = no inclusion in Common Crawl (no live search impact)
- **Recommendation:** Context - Allow for training presence, block for data control

### anthropic-ai

- **Operator:** Anthropic
- **User-Agent:** `anthropic-ai`
- **Purpose:** Claude model training (separate from ClaudeBot)
- **Recommendation:** Context - No impact on live search

### Bytespider

- **Operator:** ByteDance
- **User-Agent:** `Bytespider`
- **Purpose:** TikTok AI, Doubao (China)
- **Note:** Reported aggressive crawling behavior
- **Recommendation:**  **BLOCK** for most Western sites

### cohere-ai

- **Operator:** Cohere
- **User-Agent:** `cohere-ai`
- **Purpose:** Cohere model training, enterprise AI
- **Recommendation:** Context - Low priority

---

## robots.txt Templates

### Maximum AI Visibility

```text
# Allow all AI search crawlers
User-agent: GPTBot
Allow: /

User-agent: OAI-SearchBot
Allow: /

User-agent: ChatGPT-User
Allow: /

User-agent: ClaudeBot
Allow: /

User-agent: anthropic-ai
Allow: /

User-agent: PerplexityBot
Allow: /

User-agent: Google-Extended
Allow: /

User-agent: GoogleOther
Allow: /

User-agent: Applebot-Extended
Allow: /

User-agent: Amazonbot
Allow: /

User-agent: FacebookBot
Allow: /

# Block aggressive/training-only crawlers
User-agent: Bytespider
Disallow: /

User-agent: CCBot
Disallow: /
```

### Conservative (Training Blocked)

```text
# Allow AI search crawlers only
User-agent: GPTBot
Allow: /

User-agent: OAI-SearchBot
Allow: /

User-agent: ClaudeBot
Allow: /

User-agent: PerplexityBot
Allow: /

User-agent: Google-Extended
Allow: /

# Block everything else
User-agent: *
Disallow: /
```

---

## Analysis Checklist

When auditing robots.txt:

1.  Fetch `[domain]/robots.txt`
2.  Check for specific User-agent blocks (case-insensitive)
3.  Check wildcard `User-agent: *` rules
4.  Note any `Crawl-delay` directives
5.  Look for `Sitemap:` directive
6.  Check meta robots tags on key pages
7.  Verify no blanket `Disallow: /` on AI bots

### Common Issues

| Issue | Impact | Fix |
|-------|--------|-----|
| `User-agent: * Disallow: /` | Blocks all AI bots | Add specific allow rules |
| Missing GPTBot | No ChatGPT visibility | Add GPTBot allow rule |
| Missing PerplexityBot | No Perplexity visibility | Add PerplexityBot allow rule |
| noai meta tag | Blocks AI usage | Remove or change to noindex |

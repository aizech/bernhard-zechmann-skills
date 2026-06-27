---
name: free-search-aggregator
description: Search across multiple web providers with automatic failover. Use when the user needs quota-aware, multi-provider web search.
license: MIT
compatibility: claude-code opencode github-copilot devin pi cursor
---

# Free Search Aggregator

Reliable web search with provider failover and quota awareness.

## Providers

Default order:

```
brave -> exa -> tavily -> duckduckgo -> bing_html -> mojeek -> serper -> searchapi -> google_cse -> baidu -> wikipedia
```

No-key providers: DuckDuckGo, Bing RSS, Mojeek, Wikipedia.

## Commands

```bash
# Normal search
scripts/search "latest AI agent frameworks" --max-results 5

# Task search (multi-query)
scripts/search task "@dual Compare Claude vs GPT-4"

# Deep research
scripts/search task "@deep autonomous vehicle safety" --max-results 8 --max-queries 10

# Quota and health
scripts/status
scripts/remaining --real
python3 -m free_search health
python3 -m free_search doctor
```

## Rules

- Default mode uses one worker for cost control.
- Use `@dual` or `@deep` only for research tasks.
- Results stored in `memory/search-cache/` and `memory/search-reports/`.

## Output

- Search: query, provider, results, attempted providers, quota
- Task search: task, queries, grouped and merged results

---
name: web-research
description: Research a topic across multiple web sources and produce a cited report. Use when the user asks to research online, search the web, compare options, or produce a research report.
license: MIT
compatibility: claude-code opencode github-copilot devin pi cursor
---

# Web Research

Research a topic across multiple sources and synthesize the findings.

## Process

1. **Plan**: create a folder `research_[topic_name]/` and write `research_plan.md` with:
   - Main question
   - 2-5 non-overlapping subtopics
   - Expected information per subtopic
   - How results will be synthesized

2. **Delegate**: for each subtopic, spawn a research task with:
   - Clear, specific question
   - Instructions to save findings to `findings_[subtopic].md`
   - 3-5 web searches maximum

3. **Synthesize**: read all findings files, then produce:
   - Direct answer to the original question
   - Integrated insights from all subtopics
   - Source citations with URLs
   - Gaps or limitations

4. **Report** (optional): write `research_report.md` if requested.

## Best practices

- Plan before delegating.
- Use file-based communication for subagents.
- Stop at 3-5 searches per subtopic.
- Cite specific sources.

## Note

Use `fetch_url` for URLs, not `read_file`.

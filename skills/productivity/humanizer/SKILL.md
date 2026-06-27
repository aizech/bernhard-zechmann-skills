---
name: humanizer
description: Remove signs of AI-generated writing from text. Use when editing or reviewing text to make it sound more natural and human-written.
license: MIT
compatibility: claude-code opencode github-copilot devin pi cursor
---

# Humanizer

Remove AI writing patterns from text while preserving meaning and adding voice.

## Process

1. Read the input text.
2. Identify AI patterns: inflated significance, promotional language, superficial -ing phrases, vague attributions, em dashes, overused AI words, passive voice, filler phrases, rule of three, emojis, curly quotes, and chatbot pleasantries.
3. Rewrite problematic sections. Keep the core message and match the intended tone.
4. Add voice: vary sentence length, include opinions, acknowledge complexity, use first person when appropriate, and be specific.
5. Do a final anti-AI pass: ask "What makes this still sound AI-generated?" and revise.

## Common patterns

- **Significance inflation**: "pivotal moment", "testament to", "evolving landscape"
- **Promotional language**: "breathtaking", "vibrant", "groundbreaking", "stunning"
- **Superficial -ing phrases**: "underscoring", "highlighting", "symbolizing"
- **Vague attributions**: "Experts say", "Industry reports", "Observers have cited"
- **AI vocabulary**: "delve", "crucial", "foster", "tapestry", "landscape", "testament"
- **Rule of three**: forcing ideas into groups of three
- **Emojis and curly quotes**: remove them
- **Filler**: "In order to", "At this point in time", "It is important to note that"
- **Hedging**: "could potentially be argued that"

## Output format

1. Draft rewrite
2. Remaining AI tells (brief bullets)
3. Final rewrite
4. Summary of changes

## Rule

Do not just remove bad patterns. Replace them with natural, human alternatives that have a clear point of view.

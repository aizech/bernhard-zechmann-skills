---
name: agent-interview
description: Create an audio interview with a selected agent using OpenAI TTS. Generates a single MP3 file with a Q&A podcast session.
license: MIT
compatibility: claude-code opencode github-copilot devin pi cursor
---

# Agent Interview Audio

Create a single MP3 audio file featuring a podcast-style interview with an agent.

## Requirements

- `OPENAI_API_KEY`
- `openai` Python package

## Process

1. Load the agent configuration from a JSON file.
2. Generate 4-6 topic exchanges based on the agent's role, skills, and purpose.
3. Write dialogue that feels alive: reactions, follow-ups, surprises, enthusiasm.
4. Use OpenAI TTS to create the complete interview.
5. Save as a single MP3 with speaker differentiation.

## Voices

- Host: alloy (warm, curious, energetic)
- Agent: nova (passionate, expressive, confident)

## Conversation flow

1. Warm intro
2. Icebreaker
3. Deep dive into a core capability
4. Host reaction and follow-up
5. Second deep dive or tougher angle
6. Spontaneous tangent
7. Closing reflection

## Rules

- Sound like a real podcast, not a scripted Q&A.
- Let the agent admit challenges or uncertainties.
- Frame answers as stories or examples.
- Include brief interjections and natural reactions.

## Output

File: `{agent_name}_interview.mp3`

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
- `openai` Python package (`pip install -r requirements.txt`)

## Folder layout

- `agent_interview.py` — main generator script
- `requirements.txt` — Python dependencies
- `examples/research-agent.json` — example agent config

## Agent config format

Save the agent as a JSON file:

```json
{
  "name": "Research Navigator",
  "role": "scientific literature assistant",
  "description": "An agent that searches, summarizes, and explains academic papers.",
  "skills": ["pubmed search", "paper summarization", "evidence synthesis"],
  "purpose": "To cut the time between a research question and a useful answer.",
  "tone": "curious, precise, and gently skeptical"
}
```

## Process

1. Load the agent configuration from a JSON file.
2. Generate 4-6 topic exchanges based on the agent's role, skills, and purpose.
3. Write dialogue that feels alive: reactions, follow-ups, surprises, enthusiasm.
4. Use OpenAI TTS to create the complete interview.
5. Save as a single MP3 with speaker differentiation.

## Usage

```bash
pip install -r requirements.txt
export OPENAI_API_KEY="..."

python agent_interview.py examples/research-agent.json
```

Optional CLI flags:

```bash
python agent_interview.py examples/research-agent.json \
  --output-dir audio \
  --interviewer-voice alloy \
  --agent-voice nova \
  --text-model gpt-4o-mini \
  --tts-model tts-1
```

## Voices

- Host: alloy (warm, curious, energetic)
- Agent: nova (passionate, expressive, confident)

Other OpenAI TTS voices: `echo`, `fable`, `onyx`, `shimmer`.

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

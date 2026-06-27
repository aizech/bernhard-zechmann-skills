---
name: openai-whisper
description: Transcribe audio locally with the Whisper CLI. No API key needed.
license: MIT
compatibility: claude-code opencode github-copilot devin pi
---

# Whisper CLI

Transcribe audio locally using OpenAI Whisper.

## Quick start

```bash
whisper /path/audio.mp3 --model medium --output_format txt --output_dir .
whisper /path/audio.m4a --task translate --output_format srt
```

## Notes

- Models download to `~/.cache/whisper` on first run.
- Default model is `turbo`.
- Use smaller models for speed, larger for accuracy.

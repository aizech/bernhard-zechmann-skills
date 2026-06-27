---
name: ai-agent-builder
description: Build an AI agent with tools, memory, and multi-step reasoning. Use when the user wants a chatbot, reasoning agent, or multi-agent system.
license: MIT
compatibility: claude-code opencode github-copilot devin pi cursor
---

# AI Agent Builder

Design and build an AI agent that uses tools, memory, and reasoning.

## Agent types

- **Reactive**: single-turn, no memory. Use for classification or simple Q&A.
- **Conversational**: multi-turn with conversation memory. Use for chatbots.
- **Tool-using**: calls external APIs. Use for actions and lookups.
- **Reasoning**: plans and executes multiple steps. Use for complex tasks.
- **Multi-agent**: specialized agents collaborating. Use for workflows.

## Tool design

- Clear, action-oriented names.
- Zod or Pydantic input schemas with constraints and examples.
- Concise descriptions that explain when to use the tool.
- Group related tools under a consistent prefix.

## Memory patterns

- **Buffer memory**: keep last N messages.
- **Summary memory**: summarize older turns to stay within context.
- **Vector memory**: retrieve relevant facts semantically.
- **Entity memory**: track entities mentioned across the conversation.

## Reasoning

- **ReAct**: thought, action, observation, repeat.
- **Planning**: plan first, execute each step, then synthesize.

Always keep the agent's goal visible. Let it ask for missing information before acting.

## Output

For a new agent, produce:

1. Architecture diagram or description.
2. List of tools with inputs and outputs.
3. System prompt.
4. Conversation flow example.
5. Deployment/integration notes.

## Guardrails

- Never make up credentials or endpoints.
- Escalate to human when confidence is low or stakes are high.
- Keep tools read-only until the user explicitly approves writes.

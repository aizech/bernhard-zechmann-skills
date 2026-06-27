---
name: brainstorming
description: Explore user intent, requirements, and design before implementation. Use before any creative work or feature build.
disable-model-invocation: true
license: MIT
compatibility: claude-code opencode github-copilot devin pi
---

# Brainstorming

Turn ideas into fully formed designs before writing code.

## Hard gate

Do not write code, scaffold projects, or invoke implementation skills until a design is presented and approved.

## Process

1. Explore the current project context.
2. Ask clarifying questions one at a time.
3. Propose 2-3 approaches with trade-offs and a recommendation.
4. Present the design and get approval.
5. Write the design doc to `docs/specs/YYYY-MM-DD-<topic>-design.md`.
6. Run a self-review for placeholders, contradictions, ambiguity, and scope.
7. Ask the user to review the spec.
8. Transition to implementation via a planning step.

## Principles

- One question at a time.
- Prefer multiple choice when possible.
- YAGNI: remove unnecessary features.
- Explore alternatives.
- Design for small, well-bounded units.

## Design doc sections

- Problem and goals
- Scope
- Architecture
- Components and interfaces
- Data flow
- Error handling
- Testing approach

## Notes

Even simple projects need a short design. The design can be a few sentences, but it must be explicit and approved.

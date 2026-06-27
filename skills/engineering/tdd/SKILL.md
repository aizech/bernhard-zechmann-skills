---
name: tdd
description: Test-driven development with red-green-refactor. Use when the user wants to build features or fix bugs test-first, or mentions unit, integration, or red-green-refactor tests.
license: MIT
compatibility: claude-code opencode github-copilot devin pi cursor
---

# Test-Driven Development

Build features and fix bugs one vertical slice at a time, using tests as the feedback loop.

## Core principle

Tests verify behavior through public interfaces, not implementation details. If you refactor and the test breaks without behavior changing, the test was wrong.

## Anti-pattern: horizontal slices

Do not write all tests first, then all implementation. Write one test, make it pass, then repeat.

```
Wrong:  RED test1, test2, test3 -> GREEN impl1, impl2, impl3
Right:  RED test1 -> GREEN impl1 -> RED test2 -> GREEN impl2 -> ...
```

## Workflow

### 1. Plan

- Confirm the interface changes with the user.
- Confirm which behaviors to test. You cannot test everything.
- List behaviors as observable outcomes, not implementation steps.
- Get user approval before writing code.

### 2. Tracer bullet

Write one test for one behavior. Watch it fail. Write the minimal code to make it pass.

### 3. Incremental loop

For each remaining behavior:

- Write the next test.
- Make it pass with minimal code.
- Do not anticipate future tests.

### 4. Refactor

After all tests pass:

- Extract duplication.
- Deepen modules: small interface, deep implementation.
- Run tests after each refactor step.

Never refactor while RED.

## Checklist per cycle

- [ ] Test describes behavior, not implementation.
- [ ] Test uses the public interface.
- [ ] Test would survive an internal refactor.
- [ ] Code is minimal for this test.
- [ ] No speculative features added.

## Rules

- Write tests before implementation for new behavior.
- Use type hints and clear names.
- Keep functions small and single-purpose.
- Fail fast with clear error messages.

# Skill Invocation

Every skill is either **user-invoked** or **model-invoked**.

## User-invoked

- Triggered only when the human types the skill name, e.g. `/tdd` or `tdd`.
- Marked with `disable-model-invocation: true` in frontmatter.
- Typically orchestrate other skills.
- Can invoke model-invoked skills.
- Must never invoke another user-invoked skill.

## Model-invoked

- Can be triggered by the human or reached automatically by the agent.
- No `disable-model-invocation` flag.
- Hold reusable discipline and task-specific instructions.
- Can be invoked from a user-invoked skill.

## Rules

- A user-invoked skill may call model-invoked skills, but never another user-invoked skill.
- Keep model-invoked skills focused on a single responsibility.
- Use the bucket `README.md` to document which bucket contains which invocation type.

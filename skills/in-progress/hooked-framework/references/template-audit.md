# Report Template — Audit Mode

> Use this template for existing products (Maturity Level 2–3, Mode = Audit).
> Focus: What to change. Recommendations target specific gaps in the existing Hook loop.
> Replace all [PLACEHOLDERS] with actual content. Remove this header before delivering.

---

#  Hook Model Audit: [Product Name]

**Mode:** Audit | **Maturity Level:** [2 / 3] | **Date:** [YYYY-MM-DD]

---

## Executive Summary

[Product Name] is [one-sentence description of what the product does and for whom].

This audit evaluates the product's existing Hook loop across all four phases.
The overall Hook Score is **[X]% — [Label]**.

[One sentence on the product's primary strength in the loop.]
[One sentence on the most significant gap or broken phase.]

The single highest-leverage improvement: **[one clear sentence — the top priority action]**

---

## Product Profile

| Attribute | Value |
|---|---|
| Product Name | [extracted] |
| Core User Action | [the single repeatable action] |
| Target Persona | [inferred or provided] |
| Intended Use Frequency | [daily / weekly / episodic] |
| Value Proposition | [extracted from homepage or README] |
| Tech Stack Summary | [key frameworks and services] |
| Maturity Level | [2 / 3 — one sentence reasoning] |
| Mode | Audit |

---

## Hook Score Summary

| Phase | Score | Gap | Ethics |
|---|---|---|---|
| Trigger | [X]/3 | [What's missing] | [/️/] |
| Action | [X]/3 | [What's missing] | [/️/] |
| Variable Reward | [X]/3 | [What's missing] | [/️/] |
| Investment | [X]/3 | [What's missing] | [/️/] |
| **Overall** | **[X]%** | | |

**Baseline context:** [One sentence comparing this score to typical products at this
maturity stage. Example: "Products at Level 2 typically score 35–55%. Primary gap is Phase 3."]

---

## Phase 1 — Trigger [Score: X/3] [Ethics: /️/]

### Evidence
- [Finding 1 — source]
- [Finding 2 — source]
- [Finding 3 — source]

### Analysis
[2–4 sentences: what does the current trigger design look like? What internal trigger
exists or is implied? What specific gap is preventing a higher score?]

### Gap: [One-line description of the main trigger gap]

###  Human Actions

- [PRIORITY] **Verb** [action — rationale]
- [PRIORITY] **Verb** [action — rationale]
- [PRIORITY] **Verb** [action — rationale]

###  Coding Actions

- [PRIORITY] `component-label` — [description with technical specifics]
- [PRIORITY] `component-label` — [description with technical specifics]
- [PRIORITY] `component-label` — [description with technical specifics]

---

## Phase 2 — Action [Score: X/3] [Ethics: /️/]

### Evidence
- [Finding 1 — source]
- [Finding 2 — source]
- [Finding 3 — source]

### Analysis
[2–4 sentences: where does friction exist in the current flow? What is the estimated
time-to-value? What specific change would have the highest impact on conversion?]

### Gap: [One-line description of the main action gap]

###  Human Actions

- [PRIORITY] **Verb** [action — rationale]
- [PRIORITY] **Verb** [action — rationale]
- [PRIORITY] **Verb** [action — rationale]

###  Coding Actions

- [PRIORITY] `component-label` — [description with technical specifics]
- [PRIORITY] `component-label` — [description with technical specifics]
- [PRIORITY] `component-label` — [description with technical specifics]

---

## Phase 3 — Variable Reward [Score: X/3] [Ethics: /️/]

### Evidence
- [Finding 1 — source]
- [Finding 2 — source]
- [Finding 3 — source]

### Analysis
[2–4 sentences: which reward types are present? How variable are they? What type
is most natural for this product and persona? What is the gap?]

### Gap: [One-line description of the main reward gap]

###  Human Actions

- [PRIORITY] **Verb** [action — rationale]
- [PRIORITY] **Verb** [action — rationale]
- [PRIORITY] **Verb** [action — rationale]

###  Coding Actions

- [PRIORITY] `component-label` — [description with technical specifics]
- [PRIORITY] `component-label` — [description with technical specifics]
- [PRIORITY] `component-label` — [description with technical specifics]

---

## Phase 4 — Investment [Score: X/3] [Ethics: /️/]

### Evidence
- [Finding 1 — source]
- [Finding 2 — source]
- [Finding 3 — source]

### Analysis
[2–4 sentences: what does the user store in this product today? How does stored
value compound over time? Is there a meaningful switching cost? What's the gap?]

### Gap: [One-line description of the main investment gap]

###  Human Actions

- [PRIORITY] **Verb** [action — rationale]
- [PRIORITY] **Verb** [action — rationale]
- [PRIORITY] **Verb** [action — rationale]

###  Coding Actions

- [PRIORITY] `component-label` — [description with technical specifics]
- [PRIORITY] `component-label` — [description with technical specifics]
- [PRIORITY] `component-label` — [description with technical specifics]

---

## Prioritized Action List

The highest-leverage changes across all phases, consolidated and prioritized.

###  Human Actions — Top 3

1. [HIGH] **Verb** [action — rationale]
2. [HIGH/MEDIUM] **Verb** [action — rationale]
3. [MEDIUM] **Verb** [action — rationale]

###  Coding Actions — Top 3

1. [HIGH] `component-label` — [description]
2. [HIGH/MEDIUM] `component-label` — [description]
3. [MEDIUM] `component-label` — [description]

---

## Ethics Summary

| Phase | Rating | Key Evidence |
|---|---|---|
| Trigger | [/️/] | [One-sentence evidence summary] |
| Action | [/️/] | [One-sentence evidence summary] |
| Variable Reward | [/️/] | [One-sentence evidence summary] |
| Investment | [/️/] | [One-sentence evidence summary] |

[If any ️ or  ratings: describe the specific pattern detected, name it from the
dark pattern catalog in ethics-guide.md, and state the recommended change.]

[If any  ratings found in codebase (not just UX copy): flag this explicitly.
Example: "The absence of a data export endpoint was confirmed by reviewing the API
routes in /src/routes — no export handler exists."]

**Overall ethics assessment:** [One sentence — is this product primarily a facilitator
or does it show manipulative design signals? What is the most important ethics action?]

---

## Recommended Next Analysis

**Re-run this audit when:**
- The top 3 actions from the Prioritized Action List have been implemented
- Or: [specific milestone relevant to this product — e.g. "after next major release",
  "after 90 days of retention data collection"]

**Focus of next audit (delta report):**
- Compare scores against this baseline: Trigger [X]/3, Action [X]/3,
  Variable Reward [X]/3, Investment [X]/3
- Measure whether internal trigger strength has increased (direct traffic trend,
  session initiation source data)
- Evaluate whether the top ethics flag has been resolved
- Assess Variable Reward variability improvements if Phase 3 was the primary gap

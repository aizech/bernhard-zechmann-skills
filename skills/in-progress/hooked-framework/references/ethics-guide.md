# Ethics Guide — Hooked Framework Skill

> Load this file before performing any ethics evaluation.
> Ethics checks are mandatory for every phase analysis.

## Table of Contents
1. [Facilitator vs. Manipulator](#1-facilitator-vs-manipulator)
2. [Ethics Rating System](#2-ethics-rating-system)
3. [Per-Phase Ethics Criteria](#3-per-phase-ethics-criteria)
4. [Dark Pattern Catalog](#4-dark-pattern-catalog)
5. [Ethics Action Item Rules](#5-ethics-action-item-rules)

---

## 1. Facilitator vs. Manipulator

Nir Eyal distinguishes between two types of Hook builders:

**Facilitators** build products that help users achieve goals they already have.
The internal trigger is a genuine aspiration or recurring need. The habit serves the user.
Example: a meditation app that helps someone build a mindfulness practice they wanted.

**Manipulators** build products that exploit psychological vulnerabilities to serve
the product's metrics at the user's expense. The "trigger" is manufactured anxiety.
The habit serves the company, not the user.
Example: a social app designed to make users feel inadequate so they scroll more.

The test Eyal proposes: **Would you use this product yourself, and would you
recommend it to someone you care about?** If the honest answer is no, the design
is likely manipulative.

A second test: **Does the habit make the user's life better in some measurable way?**
If extended use leads to regret, wasted time, or worsening outcomes for the user,
the product is exploiting rather than serving.

---

## 2. Ethics Rating System

Apply one of three ratings to each Hook phase:

###  Facilitator
The design pattern in this phase serves the user's genuine goals.
The habit being formed is one the user would consciously endorse.
No deceptive, exploitative, or manipulative mechanics detected.

### ️ Caution
The design pattern is potentially beneficial but edges toward exploitation.
The intent may be good but the implementation risks harm.
Recommend review and consider alternatives.
Generate a `[ETHICS]` action item.

###  Manipulator Risk
The design pattern exploits psychological vulnerabilities, obscures user
agency, or serves the product's metrics at the user's expense.
Flag prominently. Generate a mandatory `[ETHICS]` action item.
Do not recommend implementing or retaining this pattern.

---

## 3. Per-Phase Ethics Criteria

### Phase 1 — Trigger

** Facilitator signals:**
- Internal trigger is a genuine aspiration or recurring need (productivity, learning, creativity)
- External triggers are timely, relevant, and easy to opt out of
- Notification frequency matches actual user benefit

**️ Caution signals:**
- Internal trigger language uses mild social comparison ("see what others are doing")
- Notification defaults are aggressive but can be changed
- Urgency language is present but not false

** Manipulator Risk signals:**
- Internal trigger is manufactured anxiety, fear, or insecurity ("you're falling behind")
- Notifications are difficult to opt out of (buried settings, re-enabled after updates)
- Fear of missing out (FOMO) is the primary retention mechanism
- Notifications fire at psychologically vulnerable times (late night, early morning)
  without clear user benefit

---

### Phase 2 — Action

** Facilitator signals:**
- Friction reduction serves the user (faster to value, less setup)
- Cancellation is as easy as signup
- Dark patterns absent from conversion flows

**️ Caution signals:**
- Trial cancellation requires more steps than signup
- Default settings favor the product's interests over the user's preferences
- Upsell prompts appear frequently but are dismissible

** Manipulator Risk signals:**
- Cancellation is deliberately hidden or requires phone calls
- Confirmshaming present ("No thanks, I don't want to save money")
- Roach motel: easy to enter, difficult to exit
- Free trial requires credit card with opaque auto-renewal
- Progress is artificially inflated to create false sunk cost ("You're 80% done!")

---

### Phase 3 — Variable Reward

** Facilitator signals:**
- Variability produces genuine discovery or meaningful achievement
- Rewards are proportional to real user effort or contribution
- Users feel satisfied after reward, not compelled to keep seeking

**️ Caution signals:**
- Infinite scroll present but interruptible (explicit "end of feed" state)
- Streak mechanics present but loss is recoverable
- Social comparison is present but opt-out is available

** Manipulator Risk signals:**
- Slot machine mechanics designed to maximize session length, not user satisfaction
- Infinite scroll with no natural stopping point
- Streak mechanics designed to induce anxiety on near-miss days
- Social comparison intentionally designed to produce inadequacy
- Artificial scarcity used to manufacture urgency ("Only 2 left!" when untrue)
- Loot boxes or randomized paid rewards targeting compulsive behavior

---

### Phase 4 — Investment

** Facilitator signals:**
- Stored data genuinely improves the product for the user
- Data export is available and clearly documented
- Users understand what they're storing and why it benefits them

**️ Caution signals:**
- Export exists but is buried or requires support contact
- Switching cost is real but transparent (user aware they'll lose data)
- Data is used for personalization but also monetized (disclosed in policy)

** Manipulator Risk signals:**
- No data export available — users cannot retrieve their own content
- Social graph lock-in: connections cannot be migrated or contacted outside platform
- Deletion is deliberately difficult or delayed (dark pattern)
- Investment mechanics designed to trap rather than serve
- User data sold or shared without meaningful disclosure

---

## 4. Dark Pattern Catalog

Reference this when evaluating specific UI or product design signals:

| Pattern Name | Phase | Description |
|---|---|---|
| Roach Motel | Action | Easy to get in, hard to get out |
| Confirmshaming | Action | Opt-out language designed to induce guilt |
| Hidden cancellation | Action | Cancel flow buried or requires support |
| Trick questions | Action | Confusing double negatives in consent flows |
| Misdirection | Action | Attention drawn away from important info |
| Infinite scroll | Variable Reward | No natural stopping point in feed |
| Artificial urgency | Variable Reward | Countdown timers or scarcity that isn't real |
| Social pressure | Trigger | "Your friends are waiting for you" manipulation |
| Fear-based trigger | Trigger | Anxiety or insecurity as primary retention driver |
| Data hostage | Investment | User content held without export option |
| Shadow profiles | Investment | Data collected on non-users without consent |
| Guilt streak | Variable Reward | Streak mechanics designed to manufacture anxiety |

When a dark pattern is detected, rate the phase ` Manipulator Risk` and generate
an `[ETHICS]` action item. Name the specific pattern in the action item.

---

## 5. Ethics Action Item Rules

### When to Generate Ethics Action Items
- Any phase rated `️ Caution` → generate one `[ETHICS]` human action item
- Any phase rated ` Manipulator Risk` → generate one `[ETHICS]` human action item
  AND one `[ETHICS]` coding action item

### Format for Ethics Human Actions
```
[ETHICS][HIGH] **Audit** [specific pattern] — [why it's a risk and what to change]
```

Example:
```
[ETHICS][HIGH] **Remove** the hidden cancellation flow — users currently require 
a support email to cancel; replace with a self-serve one-click cancellation in 
account settings to comply with FTC guidelines and reduce churn driven by frustration
```

### Format for Ethics Coding Actions
```
[ETHICS][HIGH] `self-serve-cancellation` — implement one-click cancel in /settings/account; 
immediately terminate billing via Stripe subscription cancel API; send confirmation email; 
no retention popups after user confirms cancellation intent
```

### Ethics Summary Section Rules
The report's Ethics Summary section must:
- List all phases and their ethics rating
- Quote the specific evidence that drove any non- rating
- State whether any `` patterns were found in the codebase (not just UX copy)
- End with a one-sentence overall ethics assessment of the product

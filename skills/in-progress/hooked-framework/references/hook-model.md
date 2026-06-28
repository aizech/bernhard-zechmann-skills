# Hook Model Reference

> Core theory reference for the Hooked Framework skill.
> Load this file before beginning Phase 1 analysis.

## Table of Contents
1. [The Hook Model Overview](#1-the-hook-model-overview)
2. [Phase 1 — Trigger](#2-phase-1--trigger)
3. [Phase 2 — Action](#3-phase-2--action)
4. [Phase 3 — Variable Reward](#4-phase-3--variable-reward)
5. [Phase 4 — Investment](#5-phase-4--investment)
6. [The Loop](#6-the-loop)
7. [Common Anti-Patterns](#7-common-anti-patterns)

---

## 1. The Hook Model Overview

The Hook Model (Nir Eyal, *Hooked*, 2014) is a four-phase framework for building products that
create habitual use without relying on expensive advertising or aggressive push notifications alone.

The core insight: habits are formed through repeated cycles through the loop, not through a single
powerful experience. Each pass through the loop should feel slightly better than the last, because
the user has invested more, the product has learned more, and the trigger has become more internal.

The four phases are sequential and interdependent:
**Trigger → Action → Variable Reward → Investment → (loads next Trigger)**

A product with a strong Hook does not need to convince users to return — users return on their own,
driven by internal triggers. The goal is to become the default response to a recurring emotional state.

---

## 2. Phase 1 — Trigger

### Definition
The trigger is the cue that initiates the behavior. Without a trigger, the habit loop cannot begin.

### Two Types of Triggers

**External Triggers** are environmental cues embedded in the product or its marketing:
- Push notifications and email sequences
- Social referrals and word-of-mouth
- App icons, badges, and home screen placement
- Paid advertising and SEO-driven content
- Call-to-action buttons and prompts within the product

External triggers are expensive to maintain long-term. They are effective early in the habit
formation cycle but should reduce in importance as internal triggers strengthen.

**Internal Triggers** are emotional or situational states the user automatically associates
with the product:
- Boredom → open social feed
- Anxiety about missing out → check notifications
- Feeling unproductive → open task manager
- Loneliness → open messaging app
- Curiosity about a topic → open search or learning platform

Internal triggers are the goal. A product has achieved habit formation when users open it
without any external prompt — driven purely by a recurring emotional state.

### Design Patterns for Strong Triggers

- **Name the feeling** in onboarding copy: "For when you can't remember where you put that idea"
- **Match trigger to use frequency**: daily-use products need internal triggers;
  weekly-use products can rely more on external
- **Sequence external triggers** to teach the behavior before the internal trigger forms:
  notification → action → reward → repeat until automatic
- **Reduce notification fatigue**: variable timing of external triggers outperforms
  fixed schedules (users habituate to fixed patterns)

### What to Look for in a Product Analysis

- Is there emotional language in the homepage headline that names the internal trigger state?
- Are notification or email libraries present in the codebase?
- Is there a welcome or onboarding email sequence?
- Does the product define a specific "when" for use in its marketing?
- Do users return without being prompted (signal: direct traffic, low bounce on return visits)?

---

## 3. Phase 2 — Action

### Definition
The action is the simplest behavior performed in anticipation of a reward. The easier the action,
the more likely it is to become habit.

### The Fogg Behavior Model
Action occurs when three forces are present simultaneously:
```
Behavior = Motivation × Ability × Trigger
```

- **Motivation**: the user wants the reward
- **Ability**: the user can perform the action with minimal effort
- **Trigger**: the cue is present at the right moment

Increasing ability (reducing friction) is almost always more effective than increasing motivation.
Motivation is volatile; friction is structural.

### The Six Elements of Simplicity (BJ Fogg)
Reduce friction across these dimensions:
1. **Time** — how long does the action take?
2. **Money** — does it cost anything?
3. **Physical effort** — how many taps, clicks, or keystrokes?
4. **Mental effort** — how much does the user have to think?
5. **Social deviance** — does doing it feel normal or awkward?
6. **Non-routine** — does it fit into existing behavior patterns?

### Design Patterns for Frictionless Action

- **Reduce registration friction**: OAuth login, progressive profiling, no email verification
  before first value moment
- **Show value before asking for commitment**: demo mode, guest access, free tier
- **Single clear CTA above the fold**: one action, not three
- **Mobile-first core action**: if the product is meant for daily use, the action must work
  perfectly on a phone
- **Time-to-value under 5 minutes**: the user should reach the core value moment before
  they have a chance to abandon

### What to Look for in a Product Analysis

- How many steps exist between landing page and core action?
- Is there a registration wall before first value?
- Does the README require complex setup before the product can be used?
- Is there a demo, guest mode, or trial without credit card?
- Is the core action clearly named and singular on the homepage?
- Are there mobile/PWA signals in the codebase?

---

## 4. Phase 3 — Variable Reward

### Definition
Rewards must be variable — unpredictable in timing or magnitude — to sustain engagement.
Fixed rewards create satisfaction followed by satiation. Variable rewards create anticipation
and maintain motivation to return.

The neurological basis: dopamine is released in anticipation of a variable reward, not
(primarily) upon receiving it. This is why a social feed that might contain something
interesting is more compelling than a feed that always contains exactly what you expect.

### Three Types of Variable Reward

**Tribe Rewards** — social validation and belonging:
- Likes, comments, reactions from other users
- Follower counts, reputation scores
- Being featured or recognized by the community
- Collaborative features where others respond unpredictably
- *Examples: Twitter/X likes, GitHub stars, Stack Overflow votes*

**Hunt Rewards** — searching for information, resources, or deals:
- Algorithmic feeds and recommendations
- Search results (never exactly what you expected)
- Curated collections and "discover" sections
- Marketplaces and product listings
- *Examples: Google search, Pinterest discovery, Amazon recommendations*

**Self Rewards** — mastery, completion, and personal achievement:
- Progress bars and streak counters
- Level-ups, badges, and achievement systems
- Task completion (the satisfaction of checking something off)
- Skill progression and unlockable content
- *Examples: Duolingo streaks, Fitbit goals, GitHub contribution graph*

### Design Patterns for Variable Rewards

- **Combine reward types**: the strongest products use at least two
- **Maintain unpredictability**: avoid showing users exactly what they'll get before they act
- **Make the reward proportional to investment**: rare but meaningful rewards > frequent trivial ones
- **Avoid compulsive design**: variability should produce satisfaction, not anxiety
  (see ethics-guide.md for the distinction)

### What to Look for in a Product Analysis

- Is there a social feed, comments section, or reaction system? (Tribe)
- Is there search, a discovery section, or algorithmic recommendations? (Hunt)
- Are there streaks, progress bars, badges, or achievement systems? (Self)
- Is any reward variable in timing, content, or magnitude?
- Do users have reason to wonder "what's new?" when they return?

---

## 5. Phase 4 — Investment

### Definition
Investment is anything the user puts into the product that makes it more valuable to them
over time — and harder to leave. Unlike the previous phases, investment is not about
immediate gratification. It is about loading the next trigger and increasing switching costs.

Investment types:
- **Data**: preferences, history, saved items, configurations
- **Content**: posts, files, notes, projects the user has created
- **Social connections**: followers, contacts, team members
- **Reputation**: scores, ratings, track record, portfolio
- **Skill**: learned workflows, custom shortcuts, trained models
- **Integrations**: connected services, API keys, automated pipelines

### Why Investment Matters

Each investment the user makes:
1. Increases the product's personal relevance (more data = better personalization)
2. Raises the cost of switching to a competitor (sunk cost + migration effort)
3. Loads the next trigger (a user who has saved 200 notes will think of the product
   next time they want to capture an idea)

### The Stored Value Loop

```
User invests → Product becomes more valuable → User returns → User invests more
```

This is why products with strong investment mechanics grow more engaging over time,
while products without them feel the same on day 300 as they did on day 1.

### Design Patterns for Strong Investment

- **Make stored value visible**: show users what they've built ("You have 47 saved items")
- **Personalization that improves with use**: recommendations that get better over time
- **Social graph that compounds**: the more connections, the more reasons to return
- **Reputation that follows the user**: public profiles, portfolios, contribution history
- **Friction-aware data portability**: offer export (ethical requirement) while making
  import from competitors easy

### What to Look for in a Product Analysis

- Does the product store any user-specific data that personalizes the experience?
- Can users create content or projects that live in the product?
- Is there a social graph (followers, teams, connections)?
- Is there a reputation or scoring system visible to others?
- Is data export available? (Ethics signal — see ethics-guide.md)
- Does the product get more useful the longer it's used?

---

## 6. The Loop

A complete Hook cycle looks like this:

```
[Internal Trigger: "I need to capture this idea"]
        ↓
[Action: Open app, tap "New note"]
        ↓
[Variable Reward: Note saved, tag suggestions appear, related notes surface]
        ↓
[Investment: Note added to collection; collection now has 201 notes]
        ↓
[Next Trigger loaded: "When I next have an idea, I'll think of this app"]
```

The loop compounds. Each cycle through increases the internal trigger strength,
reduces the friction of the action (habit reduces cognitive load), and deepens
the investment. After enough repetitions, the behavior is automatic.

Designing for the loop means asking: **does completing one cycle make the next
cycle more likely?** If the answer is no, the loop is broken.

---

## 7. Common Anti-Patterns

These patterns break the loop or undermine habit formation:

| Anti-Pattern | Phase | Problem |
|---|---|---|
| Only external triggers, no internal | Trigger | Requires ongoing spend; no self-sustaining habit |
| Registration wall before value | Action | Users abandon before experiencing the reward |
| Fixed, predictable rewards | Variable Reward | Users habituate; engagement declines over time |
| No stored value | Investment | No reason to return; easy to switch |
| Onboarding that skips the core action | Action | Users don't learn the behavior during setup |
| Notifications with no variable content | Trigger | Users ignore after first few exposures |
| Rewards that serve the product, not the user | Variable Reward | Short-term engagement, long-term churn |
| No data portability | Investment | Ethical risk + regulatory exposure |

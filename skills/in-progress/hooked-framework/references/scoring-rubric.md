# Scoring Rubric — Hooked Framework Skill

> Load this file during phase analysis.
> Use it to assign scores 0–3 for each Hook phase.
> Every score must be backed by specific evidence from the fetched product data.

---

## Scoring Principles

1. **Evidence first.** Assign a score only after identifying specific evidence.
   Never assign a score based on assumptions or general product category.

2. **Cite the source.** Every score must name the source of its evidence:
   a filename, a URL, a specific copy quote, or a detected dependency.

3. **Score what exists, not what's planned.** If a feature is mentioned in
   issues or a roadmap but not yet shipped, it does not count toward the score.

4. **Partial credit is real.** A score of 1 or 2 reflects genuine partial
   implementation. Do not round up to be generous or round down to be harsh.

5. **Maturity context applies.** A Level 1 product scoring 0 on Variable Reward
   is expected and appropriate — note it without penalizing the overall assessment
   unfairly. Scores are always interpreted in maturity context.

---

## Phase 1 — Trigger Rubric

### Score 0 — No Trigger Mechanism
- No external trigger infrastructure detected (no email, notification, or referral system)
- Homepage copy is purely functional — no emotional language, no named feeling
- No defined "when" for product use in any copy
- No onboarding sequence

**Evidence examples:**
- "No email library found in package.json"
- "Homepage headline: 'Project management for teams' — functional, no internal trigger"
- "No push notification API detected"

---

### Score 1 — External Triggers Only
- External trigger infrastructure present (email library, notification system, or referral)
- No internal trigger language in homepage or onboarding copy
- The product does not name or speak to the emotional state that should prompt use
- Users are reached externally but not taught when or why to think of the product

**Evidence examples:**
- "SendGrid detected in package.json; no drip sequence found in /emails directory"
- "Push notification setup present; all notifications are transactional (not behavioral)"
- "Homepage copy does not name an emotional state or recurring situation"

---

### Score 2 — External + Implicit Internal Trigger
- External trigger infrastructure present AND active (sequences, behavioral triggers)
- Homepage or onboarding copy implies an emotional trigger but does not name it directly
- The "when" of product use is suggested but not explicit
- A user could infer the internal trigger from context but is not guided to it

**Evidence examples:**
- "Welcome email sequence found with 3-step drip (day 1, 3, 7)"
- "Homepage headline: 'Never lose a great idea again' — implies the feeling (sudden insight,
  fear of forgetting) but doesn't name it explicitly"
- "Feature copy mentions 'your morning routine' — implies daily use context"

---

### Score 3 — Explicit Internal Trigger
- External triggers present AND behavioral (variable timing, segmented messaging)
- Homepage or onboarding explicitly names the emotional state or recurring situation
  the product is built around
- Users are taught when to think of this product in onboarding or product copy
- The internal trigger is specific to a persona, not generic

**Evidence examples:**
- "Homepage hero: 'For that moment when a great idea appears and your notes app is three
  apps away' — names the exact trigger situation"
- "Onboarding step 2 asks: 'When do you usually capture ideas?' — actively teaching
  the internal trigger"
- "Email sequence is behavior-triggered (sent after 48h inactivity with personalized copy)"

---

## Phase 2 — Action Rubric

### Score 0 — High Friction, Unclear Action
- Core user action is not identifiable from homepage copy
- Setup requires significant effort (complex installation, manual configuration)
- Registration wall before any value is experienced
- No demo, trial, or guest mode available
- Multiple competing CTAs above the fold

---

### Score 1 — Identifiable Action, Significant Friction
- Core action is identifiable but the path to it has 3+ friction points
- Registration required before first value, OR setup is moderately complex
- No OAuth — email/password only, with email verification before access
- Mobile experience absent or clearly secondary
- Time-to-value estimated at 10+ minutes for a new user

---

### Score 2 — Low Friction, Some Gaps
- Core action is clear and prominent on homepage
- Registration friction is moderate (OAuth present, OR email verification skipped)
- Time-to-value estimated at 3–10 minutes
- Mobile-friendly but not mobile-first
- Minor friction points present (e.g. required profile fields, mandatory tutorial)

---

### Score 3 — Minimal Friction, Fast Value
- Core action is singular, obvious, and prominent
- OAuth login or magic link available; no email verification before first action
- Guest/demo mode OR free tier with no credit card required
- Time-to-value under 3 minutes for a new user
- Mobile-first design signals present (PWA, responsive framework, or native app)
- Single CTA above the fold

---

## Phase 3 — Variable Reward Rubric

### Score 0 — Fixed or No Reward
- No reward mechanic detectable in codebase or website
- Product delivers a fixed, predictable output every time
- No social features, discovery, or achievement system
- Users receive exactly what they expect, every time

---

### Score 1 — One Reward Type, Low Variability
- One reward type present (Tribe, Hunt, or Self) but with low variability
- Reward is predictable in timing or content
- Social features present but passive (e.g. static public profile, no interactions)
- Basic achievement or completion state present but no progression or surprise

---

### Score 2 — One Strong Reward Type OR Two Weak Types
- One reward type well-implemented with genuine variability, OR
- Two reward types present but neither deeply variable
- Some unpredictability in what the user will find or receive
- Users have reason to wonder "what's new?" on return visits

---

### Score 3 — Multiple Reward Types with Genuine Variability
- Two or three reward types present (Tribe + Hunt, or Tribe + Self, or all three)
- Variability is designed in — content, timing, or magnitude of reward is unpredictable
- Users cannot fully predict what they will encounter on return
- Reward system serves the user's genuine goals (see ethics-guide.md)
- Evidence of reward system sophistication in codebase (recommendation engine,
  randomization logic, personalization based on behavior)

---

## Phase 4 — Investment Rubric

### Score 0 — No Investment Mechanic
- No user-specific data persisted beyond session
- No user-generated content stored
- No social connections or reputation system
- The product is as useful to a new user as to a user of 2 years
- Switching to a competitor costs nothing

---

### Score 1 — Basic Data Persistence
- User preferences or history stored (e.g. saved settings, recent searches)
- No compounding value — stored data is convenience, not differentiation
- No user-generated content or social connections
- Switching cost: minor (re-enter preferences)

---

### Score 2 — Meaningful Stored Value
- User-generated content stored (notes, projects, posts, files)
- OR social connections established (followers, team members)
- Stored value is real but not yet compounding or deeply personalized
- Switching cost: moderate (would lose content or connections)
- Data export may or may not be present

---

### Score 3 — Compounding Investment Loop
- User-generated content + social graph + data personalization (multiple investment types)
- Product demonstrably improves with use (personalization, recommendations, history)
- Switching cost is significant and transparent to the user
- Data export available (ethical requirement for this score)
- Evidence of investment mechanics in codebase (user model richness, history tables,
  social graph schema, recommendation logic referencing stored user data)

---

## Scoring Evidence Template

Use this template when recording each phase score:

```
Phase: [1–4]
Score: [0–3]
Ethics: [ / ️ / ]

Evidence:
- [Specific finding 1 — source: filename / URL / copy quote]
- [Specific finding 2 — source: filename / URL / copy quote]
- [Specific finding 3 — source: filename / URL / copy quote]

Reasoning:
[2–3 sentences explaining why this evidence maps to this score,
 in context of this specific product and its maturity level]
```

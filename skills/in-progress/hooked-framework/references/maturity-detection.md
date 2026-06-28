# Maturity Detection — Hooked Framework Skill

> Load this file during Phase 0 (Product Profiling).
> Use it to assign a Maturity Level (1, 2, or 3) before analysis begins.
> Maturity Level controls which Hook phases are in scope and how deep recommendations go.

---

## Maturity Signals Table

Assess the product against each signal. Most signals will point clearly to one level.
Use the majority of signals to assign the level — do not require unanimity.

| Signal | Level 1 — Prototype | Level 2 — Early Product | Level 3 — Scaling Product |
|---|---|---|---|
| **Repo age** | < 6 months | 6–24 months | > 24 months |
| **Commit frequency** | Sporadic / burst | Regular cadence | Systematic / team-based |
| **README quality** | Minimal or missing | Structured with setup guide | Comprehensive with docs link |
| **Open issues** | Few or none | 10–100 | 100+ with labels/milestones |
| **Contributor count** | 1–2 | 2–5 | 5+ |
| **Website complexity** | Single landing page | Multi-page site | Full marketing site with blog |
| **Pricing page** | None / waitlist | 1–2 tiers or free only | 3+ tiers, enterprise, annual plans |
| **Analytics dependency** | Absent | Basic (GA, Plausible) | Advanced (Segment, Mixpanel, Amplitude) |
| **Email library** | Absent | Present (Resend, Nodemailer) | Present + sequence logic (drip flows) |
| **Notification system** | Absent | Basic push/email | Multi-channel (push + email + SMS) |
| **Auth complexity** | Single method | 2 methods | OAuth + SSO + team management |
| **Data storage** | Local / simple | Persistent user data | Rich user profiles + history |

---

## Level Definitions

### Level 1 — Prototype

**Characteristics:**
- Product is a proof of concept or very early MVP
- Core functionality exists but user experience is rough
- No meaningful user base yet
- Marketing is minimal or absent

**Analysis scope:**
- Analyze **Trigger and Action phases only**
- Variable Reward and Investment phases: mark as "Not yet in scope — recommend
  building Trigger and Action loop first"
- Recommendations should focus on: defining the internal trigger, reducing
  time-to-value, and establishing the simplest possible core action loop
- Do not recommend complex retention mechanics, social graphs, or analytics
  infrastructure — these are premature at Level 1

**Framing for report:**
> "This product is at Prototype stage. The priority is establishing a working
> Trigger → Action loop before building reward and investment mechanics.
> Phases 3 and 4 are noted as future scope."

---

### Level 2 — Early Product

**Characteristics:**
- Product has a defined user base (even if small)
- Core features are stable and regularly maintained
- Basic marketing and onboarding present
- Some user data is being collected

**Analysis scope:**
- Analyze **all four Hook phases**
- Emphasis on completing the full loop end-to-end
- Recommendations should focus on: strengthening internal triggers,
  introducing the first Variable Reward mechanics, and establishing
  basic Investment data storage
- Score all phases but weight the report toward phases with score 0 or 1

**Framing for report:**
> "This product is at Early Product stage. The full Hook loop is in scope.
> Priority is completing the loop — even a minimal version of each phase —
> before deepening any single phase."

---

### Level 3 — Scaling Product

**Characteristics:**
- Product has an established user base
- Full feature set is present and maintained
- Marketing, analytics, and operational infrastructure in place
- Multiple pricing tiers or enterprise presence

**Analysis scope:**
- Analyze **all four Hook phases** with full depth
- Emphasis on: deepening Variable Reward sophistication, compounding
  Investment mechanics, and refining internal trigger specificity
- Score all phases; weight recommendations toward closing the gap between
  current score and 3/3 on each phase
- Note competitive context if inferrable from positioning copy

**Framing for report:**
> "This product is at Scaling Product stage. The Hook loop exists in some form.
> The analysis focuses on deepening each phase and identifying where the loop
> is leaking — causing users to disengage before the next trigger fires."

---

## Mode Detection

After assigning Maturity Level, determine the analysis mode:

### Blueprint Mode
Applies when:
- Maturity Level = 1, OR
- The user explicitly describes a product idea or new project, OR
- The GitHub repo has no releases, no meaningful commit history, or is clearly
  a template/starter project

Focus: **What to build.** Recommendations are design directions and implementation
starting points. Scores reflect the current (low) state and project a target state.

### Audit Mode
Applies when:
- Maturity Level = 2 or 3, AND
- A working product exists with real users (inferred from website, pricing, or issue count)

Focus: **What to change.** Recommendations are specific improvements to existing
features and flows. Scores reflect current state against what's possible.

---

## Edge Cases

**Monorepo with multiple products:** Identify the primary user-facing product
(usually named in the README or the website). Analyze that product. Note the
multi-product structure in the profile.

**Internal tools / B2B products with no public website:** Use GitHub data only.
Note the limitation. Recommend the user share any internal product documentation
to improve analysis depth.

**Open source libraries (not end-user products):** The Hook Model applies to the
developer experience, not end-user UX. Redirect the analysis to: trigger (why
developers reach for this library), action (time to first working implementation),
variable reward (documentation quality, community responsiveness), investment
(ecosystem integrations, plugins, community contributions).

**Very new repo with polished website:** Website sophistication overrides repo age.
Assign based on website complexity + pricing presence. Mark the repo as "early stage"
in the tech notes but do not let it drag the maturity level down if the product
is clearly further along than the repo suggests.

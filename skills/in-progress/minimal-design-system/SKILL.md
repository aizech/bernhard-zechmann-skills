---
name: minimal-design-system
description: Create minimal, clean HTML artifacts with Tailwind CSS and shadcn-inspired HSL tokens. Use when the user requests a simple, professional design.
license: MIT
compatibility: claude-code opencode github-copilot devin pi cursor
---

# Minimal Design System

A minimalist design system for HTML artifacts, dashboards, and websites.

## Philosophy

- Generous whitespace
- Clear typography hierarchy
- Minimal color palette
- Auto dark mode via `prefers-color-scheme`
- Accessible: WCAG AA minimum

## Quick start template

Use Tailwind CSS via CDN and the HSL tokens from `references/design-tokens.md`.

## Core tokens

- `--background`: page background
- `--foreground`: primary text
- `--primary`: buttons and emphasis
- `--muted`: subtle backgrounds
- `--border`: borders and dividers
- `--card`: card backgrounds
- `--radius`: 0.5rem

## Common components

- **Primary button**: `bg-primary text-primary-foreground h-11 px-8 rounded-md`
- **Secondary button**: `border border-default h-11 px-8 rounded-md hover:bg-muted`
- **Card**: `p-6 rounded-lg border border-default bg-card`
- **Badge**: `text-xs px-2.5 py-1 rounded-full bg-muted`
- **Input**: `h-11 px-4 rounded-md border border-default focus:ring-2 focus:ring-[hsl(var(--ring))]`

## Layout

- Container max widths: `max-w-7xl`, `max-w-4xl`, `max-w-3xl`, `max-w-2xl`
- Section spacing: `py-16`, `py-24`
- Element gaps: `gap-4`, `gap-6`, `gap-8`

## Rules

- Use Lucide icons only. No emojis.
- Never overwrite existing styles without asking.
- Add focus-visible indicators.
- Keep touch targets at least 44px.

## Reference

- `references/design-tokens.md` — complete tokens
- `references/components.md` — full component library

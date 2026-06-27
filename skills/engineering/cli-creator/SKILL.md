---
name: cli-creator
description: Build a composable command-line tool from API docs, OpenAPI specs, SDKs, curl examples, or existing scripts. Use when the user wants a durable CLI that future agents can run from any directory.
license: MIT
compatibility: claude-code opencode github-copilot devin pi
---

# CLI Creator

Build a durable CLI that agents can run from any working directory.

## Start

Define:

- **Source**: API docs, OpenAPI JSON, SDK docs, curl examples, web app, or existing script.
- **Jobs**: literal reads/writes such as `list drafts`, `download logs`, `search messages`, `upload media`.
- **Install name**: short binary name like `ci-logs`, `slack-cli`, `sentry-cli`.

Check if the name already exists:

```bash
command -v <tool-name> || true
```

## Choose the runtime

Inspect the machine:

```bash
command -v cargo rustc node pnpm npm python3 uv || true
```

Choose the least surprising option:

- **Rust** for durable, fast binaries with strong JSON handling.
- **TypeScript/Node** when the SDK or browser tooling is the reason the CLI is better.
- **Python** for data, notebooks, SQLite, or existing Python-heavy tooling.

## Command surface

Sketch before coding. Every CLI should have:

- `--help` showing every major capability.
- `--json doctor` verifying config, auth, version, and endpoint reachability.
- `init` for local config when env-only auth is painful.
- Discovery commands for top-level containers.
- Resolve commands turning names, URLs, or slugs into stable IDs.
- Read commands with bounded `--limit` or clear pagination.
- Write commands that are narrow, named actions with `--dry-run` or preview when possible.
- A raw escape hatch named honestly, e.g. `request` or `api`.

## Auth and config

Precedence:

1. Environment variable with the service's standard name, e.g. `GITHUB_TOKEN`.
2. User config under `~/.<tool-name>/config.toml`.
3. `--api-key` flag only for explicit one-off tests.

Never print full tokens. `doctor --json` reports the auth source category and missing setup.

## Build workflow

1. Read the source to inventory resources, auth, pagination, IDs, file flows, rate limits, and dangerous writes.
2. Sketch the command list in chat.
3. Scaffold the CLI with a README.
4. Implement `doctor`, discovery, resolve, read, and a narrow dry-run write path.
5. Install the CLI on PATH.
6. Smoke test from another repo or `/tmp`.
7. Run format, typecheck, build, and unit tests.

## Defaults

**Rust**: `clap`, `reqwest`, `serde`, `toml`, `anyhow`. Add `make install-local` to `~/.local/bin`.

**TypeScript/Node**: `commander` or `cac`, `zod` only where needed, `package.json` `bin` entry.

**Python**: `argparse` or `typer`, `httpx`/`requests`, `pyproject.toml` console script.

## Companion skill

After the CLI works, create a small skill that explains how to verify it, configure auth, discover IDs, run safe reads, and use the write path.

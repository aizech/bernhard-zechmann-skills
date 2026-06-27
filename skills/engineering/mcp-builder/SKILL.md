---
name: mcp-builder
description: Create an MCP server that exposes external APIs or services as well-designed tools. Use when building a Model Context Protocol server in Python or TypeScript.
license: MIT
compatibility: claude-code opencode github-copilot devin pi
---

# MCP Builder

Create MCP servers that let agents interact with external services through clean tools.

## Process

### 1. Research

- Review the MCP specification at `https://modelcontextprotocol.io/sitemap.xml`.
- Fetch the TypeScript or Python SDK README from GitHub.
- Read the target API docs to identify endpoints, auth, pagination, and data models.

### 2. Plan

- List the tools to implement. Prefer comprehensive API coverage over one-off workflow tools.
- Use consistent, action-oriented names with prefixes, e.g. `github_create_issue`, `github_list_repos`.
- Decide transport: streamable HTTP for remote, stdio for local.

### 3. Implement

**TypeScript (default)**

- Use the MCP SDK with Zod for input schemas.
- Define `outputSchema` and `structuredContent` where supported.
- Annotate tools with `readOnlyHint`, `destructiveHint`, `idempotentHint`, `openWorldHint`.

**Python**

- Use FastMCP with Pydantic models.
- Add `@mcp.tool()` decorators.

Shared rules:

- Async I/O for network calls.
- Actionable error messages.
- Pagination on list operations.
- Return both text and structured data when possible.

### 4. Test

- Build and run the server.
- Test with the MCP Inspector:

```bash
npx @modelcontextprotocol/inspector
```

### 5. Evaluate

Create 10 read-only, complex, realistic questions that require multiple tool calls. Verify answers yourself. Store as `evals.xml` or `evals/evals.json`.

## Reference

- `references/mcp-best-practices.md` — server and tool conventions
- `references/node-mcp-server.md` — TypeScript patterns
- `references/python-mcp-server.md` — Python patterns
- `references/evaluation.md` — evaluation guidelines

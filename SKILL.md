---
name: gemini-smart-search
description: Search the web using Gemini with Google Search grounding through a local script, with model routing and quota fallback across Gemini Flash-Lite, Flash, and Pro. Use when web research should stay inside the Gemini family, when dynamic model switching is needed without restarting the OpenClaw gateway, when a separate Gemini API key/quota pool should be used, or when repeated search tasks need cheap/balanced/deep modes with structured JSON output.
---

# Gemini Smart Search

Use this skill when Gemini should be the search backend, but gateway-level `web_search` config is too static or too disruptive to change.

## Purpose

This skill is a **script-backed search workflow**, not a gateway tool override.

It exists to provide:
- dynamic Gemini model selection
- quota-aware fallback
- a separate Gemini API key path if desired
- structured JSON output
- no gateway restart requirement for model changes

## Modes

- **cheap**
  - Prefer `gemini-2.5-flash-lite`
  - Fallback to `gemini-2.5-flash`, then `gemini-2.5-pro`
- **balanced**
  - Prefer `gemini-2.5-flash`
  - Fallback to `gemini-2.5-flash-lite`, then `gemini-2.5-pro`
- **deep**
  - Prefer `gemini-2.5-pro`
  - Fallback to `gemini-2.5-flash`, then `gemini-2.5-flash-lite`

## Invocation

Run the Python script via `exec` and request JSON output.

Example:

```bash
python3 skills/gemini-smart-search/scripts/gemini_smart_search.py \
  --query "BoundaryML context engineering" \
  --mode cheap \
  --json
```

## Output contract

Expect JSON with at least:
- `ok`
- `query`
- `mode`
- `model_used`
- `fallback_chain`
- `answer`
- `citations`
- `error`

## API key policy

The script should prefer a dedicated key path for this skill, then fall back to the standard Gemini key.

Preferred order:
1. `SMART_SEARCH_GEMINI_API_KEY`
2. `GEMINI_API_KEY`

If neither key is present, the agent must explicitly ask the human for a Gemini API key before claiming setup is complete.

Do not store the key in tracked repository files. Prefer a repo-local, gitignored file such as `.env.local`.

See `references/config.md`.

## When to use this skill instead of built-in `web_search`

Use this skill when:
- you want Gemini-only search
- you want to test or isolate quota pools
- you want model routing without touching gateway config
- you want predictable JSON output for downstream orchestration

Do **not** use this skill when:
- a normal built-in `web_search` is sufficient
- you need non-Gemini providers
- you only need to fetch and read a known URL (`web_fetch`)
- you need logged-in or JS-heavy page interaction (`browser`)

## Fallback policy

Fallback only for errors like:
- quota exceeded / 429
- model unavailable
- transient upstream failure

Do not silently fallback on obvious local/script bugs or invalid arguments.

## References

- `references/config.md` — environment variables and design notes
- `assets/example-output.json` — expected response shape

## Status

This is the initial scaffold. The Python implementation is not complete yet.

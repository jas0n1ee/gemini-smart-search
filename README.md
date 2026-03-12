# gemini-smart-search

A Gemini-powered smart search skill for OpenClaw.

## For humans

You do **not** need to operate this skill manually.

If your agent needs it, just give the agent this repo URL:

```text
git@github.com:jas0n1ee/gemini-smart-search.git
```

The agent should:
- clone or fetch the repo
- read `SKILL.md`
- ask you for a Gemini API key if setup is incomplete

This skill expects a Gemini API key:
- preferred: `SMART_SEARCH_GEMINI_API_KEY`
- fallback: `GEMINI_API_KEY`

Keep the key in a gitignored local env file such as `.env.local`, not in tracked files.

## What it is

This skill gives an agent a Gemini-only search workflow with:
- Google Search grounding
- model routing (`cheap` / `balanced` / `deep`)
- fallback across Gemini model candidates
- structured JSON output for orchestration

## Notes

- This repo is primarily for agent use.
- Human-facing setup is intentionally minimal.
- Release notes and release checklist live under `references/`.

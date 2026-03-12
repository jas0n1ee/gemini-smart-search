# Gemini Smart Search Config Notes

## Environment variables

Preferred API key resolution order:

1. `SMART_SEARCH_GEMINI_API_KEY`
2. `GEMINI_API_KEY`

## Intended model chains

### cheap
- `gemini-2.5-flash-lite`
- `gemini-2.5-flash`
- `gemini-2.5-pro`

### balanced
- `gemini-2.5-flash`
- `gemini-2.5-flash-lite`
- `gemini-2.5-pro`

### deep
- `gemini-2.5-pro`
- `gemini-2.5-flash`
- `gemini-2.5-flash-lite`

## Notes

- The first implementation should stay Gemini-only.
- Keep the script output JSON-first for orchestration.
- Avoid coupling the script to gateway config.
- If later promoted to a plugin, preserve the same mode names and result schema.

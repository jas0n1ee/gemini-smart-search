#!/usr/bin/env python3
"""Gemini Smart Search scaffold.

Initial placeholder for a Gemini-only smart search worker with model routing and
quota fallback. The first real implementation should:
- accept --query / --mode / --json
- resolve API key from SMART_SEARCH_GEMINI_API_KEY then GEMINI_API_KEY
- try a model chain based on mode
- return standardized JSON
"""

from __future__ import annotations

import argparse
import json
import os
import sys
from typing import List

MODEL_CHAINS = {
    "cheap": ["gemini-2.5-flash-lite", "gemini-2.5-flash", "gemini-2.5-pro"],
    "balanced": ["gemini-2.5-flash", "gemini-2.5-flash-lite", "gemini-2.5-pro"],
    "deep": ["gemini-2.5-pro", "gemini-2.5-flash", "gemini-2.5-flash-lite"],
}


def resolve_api_key() -> str | None:
    return os.environ.get("SMART_SEARCH_GEMINI_API_KEY") or os.environ.get("GEMINI_API_KEY")


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(description="Gemini smart search scaffold")
    p.add_argument("--query", required=True, help="Search query")
    p.add_argument("--mode", choices=sorted(MODEL_CHAINS), default="balanced")
    p.add_argument("--json", action="store_true", help="Print JSON output")
    return p.parse_args()


def main() -> int:
    args = parse_args()
    api_key = resolve_api_key()
    result = {
        "ok": False,
        "query": args.query,
        "mode": args.mode,
        "model_used": None,
        "fallback_chain": MODEL_CHAINS[args.mode],
        "answer": None,
        "citations": [],
        "usage": {"provider": "gemini", "grounding": True},
        "error": {
            "type": "not_implemented",
            "message": "Scaffold only. Real Gemini smart search implementation not wired yet.",
            "api_key_present": bool(api_key),
        },
    }
    if args.json:
        print(json.dumps(result, ensure_ascii=False, indent=2))
    else:
        print(result["error"]["message"])
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

#!/usr/bin/env python3
"""Score video topic candidates for the video-topic-radar skill.

Input: JSON array of candidates. Each candidate may contain these numeric fields:
persona_fit, audience_value, core_relevance, freshness, hook_strength,
practicality, visual_material, source_confidence, penalty.

Output: JSON array sorted by total_score descending.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any


MAXIMA = {
    "persona_fit": 20,
    "audience_value": 20,
    "core_relevance": 15,
    "freshness": 15,
    "hook_strength": 10,
    "practicality": 10,
    "visual_material": 5,
    "source_confidence": 5,
}


def clamp_number(value: Any, minimum: int, maximum: int) -> int:
    try:
        number = int(round(float(value)))
    except (TypeError, ValueError):
        number = minimum
    return max(minimum, min(maximum, number))


def score_candidate(candidate: dict[str, Any]) -> dict[str, Any]:
    breakdown: dict[str, int] = {}
    for key, maximum in MAXIMA.items():
        breakdown[key] = clamp_number(candidate.get(key, 0), 0, maximum)

    penalty = clamp_number(candidate.get("penalty", 0), 0, 100)
    total = max(0, min(100, sum(breakdown.values()) - penalty))

    scored = dict(candidate)
    scored["score_breakdown"] = breakdown
    scored["penalty"] = penalty
    scored["total_score"] = total
    return scored


def main() -> int:
    parser = argparse.ArgumentParser(description="Score short-video topic candidates.")
    parser.add_argument("input", nargs="?", help="Path to candidate JSON. Reads stdin when omitted.")
    parser.add_argument("--pretty", action="store_true", help="Pretty-print JSON output.")
    args = parser.parse_args()

    if args.input:
        raw = Path(args.input).read_text(encoding="utf-8")
    else:
        raw = sys.stdin.read()

    raw = raw.lstrip("\ufeff").strip()
    candidates = json.loads(raw)
    if not isinstance(candidates, list):
        raise SystemExit("Input must be a JSON array.")

    scored = [score_candidate(c) for c in candidates if isinstance(c, dict)]
    scored.sort(key=lambda item: item.get("total_score", 0), reverse=True)

    indent = 2 if args.pretty else None
    print(json.dumps(scored, ensure_ascii=False, indent=indent))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

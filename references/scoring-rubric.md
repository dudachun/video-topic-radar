# Scoring Rubric

Score each selected topic out of 100.

## Dimensions

- Persona fit, 20: Fits AI game development, AI monetization, or practical AI tools while supporting long-term authority.
- Audience value, 20: Helps viewers understand an opportunity, workflow, risk, or decision.
- Core relevance, 15: Strong AI connection and, when game-related, materially connected to AI game development.
- Freshness, 15: New in the last 24-72 hours, or newly relevant due to a demo, launch, repo, pricing, benchmark, or major discussion.
- Hook strength, 10: Can open with a clear conflict, result, number, demo, or contrarian point.
- Practicality, 10: Can become a usable method, workflow, business angle, or creator takeaway.
- Visual material, 5: Has screenshots, demos, UI, charts, GitHub pages, or product visuals.
- Source confidence, 5: Supported by official or credible sources.

## Penalties

Subtract up to:

- 20 for weak or indirect AI relevance.
- 15 for hype without proof.
- 15 for no clear short-video visual.
- 10 for low fit with long-term persona.
- 10 for being stale unless the interpretation is newly valuable.
- 10 for requiring too much technical background for the user's audience.

## Recommendation Rule

Pick the best daily recommendation by:

1. Minimum score of 80 unless the day is weak.
2. Strong persona fit.
3. Strong viewpoint that can support a 120-300 second script.
4. Clear visual/source material.
5. Better long-term trust than short-term controversy.

If the top score is not the best recommendation, explain why.

## Score JSON Shape For Script

When using `scripts/score_topics.py`, provide JSON like:

```json
[
  {
    "title": "AI 3D world generation changes game prototyping",
    "persona_fit": 18,
    "audience_value": 17,
    "core_relevance": 15,
    "freshness": 14,
    "hook_strength": 9,
    "practicality": 8,
    "visual_material": 5,
    "source_confidence": 5,
    "penalty": 0
  }
]
```

---
name: video-topic-radar
description: Daily-style short-video topic radar for AI, AI game development, AI monetization, and practical AI tools. Use when the user asks to find video topics, run a topic radar, search AI/game-dev news for short-video ideas, rank daily AI topics, recommend the strongest AI-related short-video topic, or turn a selected topic into a 120-300 second plain-spoken Chinese script.
---

# Video Topic Radar

## Purpose

Find current AI-related news and turn it into short-video topics for a Chinese creator focused on AI game development, AI monetization, and practical AI tools. Prefer long-term creator authority over short-lived clickbait.

This skill is manually triggered. Do not create daily automations unless the user explicitly asks.

## Standard Run

1. Browse the web for recent information. Default to the last 24-72 hours; expand to 7 days only when the news cycle is thin.
2. Search across four pools:
   - AI game development: AI 3D/world generation, AI NPCs, AI animation, AI art pipelines, AI level design, game agents, Unity/Unreal AI workflows.
   - AI monetization: AI services, Vibe Coding, agent delivery, AI SaaS, automation businesses, solo/small-team opportunities.
   - AI tool practice: new models, developer tools, agent platforms, coding tools, workflow products.
   - AI industry opportunity: platform shifts, open-source vs closed-source, pricing, capability jumps, job changes.
3. Read `references/source-map.md` when choosing sources and search queries.
4. Read `references/topic-filters.md` before accepting candidates.
5. Collect at least 20 raw candidates when possible, then narrow to 10 short-video-ready topics.
6. Read `references/scoring-rubric.md` and score the 10 topics out of 100. Use `scripts/score_topics.py` when a structured candidate JSON is convenient; otherwise score manually with the same rubric.
7. Select one strongest topic. Do not select purely by total score; prefer the topic that best fits the user's long-term persona and can support a strong, useful viewpoint.
8. Read `references/script-framework.md` before writing the full script.
9. Read `references/plain-language-rewrites.md` when writing or revising scripts, especially when the user selects a topic and asks for copy.
10. Use `references/output-template.md` for the final response shape.
11. Before finalizing any script, do a plain-language rewrite pass: replace abstract claims with concrete people, scenes, actions, and measurable results.

## Source Requirements

- Use current web sources. Do not answer from memory for daily topic discovery.
- Prefer official announcements, product pages, GitHub repos, demos, credible tech media, and primary social posts from founders/researchers.
- Include source links for every selected topic.
- Separate confirmed facts from interpretation. Mark uncertain items clearly.
- For overseas news, translate into a Chinese short-video angle instead of copying the foreign headline.

## Topic Rules

- Game development items must be AI-related. Ordinary game launches, engine releases, esports, business earnings, or graphics updates should be rejected unless the AI angle is material.
- AI monetization topics must be practical and believable. Avoid exaggerated "easy money" claims.
- Practical tool topics must explain a real workflow, not only that a tool exists.
- Long-term persona beats temporary heat. Penalize panic, empty hype, and unsupported predictions.

## Deliverable

Always deliver:

1. Today's overall judgment.
2. The single strongest recommended topic.
3. A complete 120-300 second Chinese short-video script in a口语化强观点 style, using plain concrete scenes instead of abstract professional phrasing.
4. A ranked table of 10 topics with scores and sources.
5. Brief analysis for each topic, including why it is or is not the best one today.

The full script should be detailed enough for direct recording, but not padded. It should include a strong opening, factual setup, value translation, method/opportunity analysis, boundaries, and a final creator-positioning sentence.

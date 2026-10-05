# Skill design provenance

Reference only, researched 2026-09-30. These external sources are inspiration, not
runtime instructions or dependencies. The canonical recipes are original, scoped to
this bootstrap's task and authority model; no third-party skill text is vendored.
URLs track upstream branches/pages and may change after this review.

| Primary source inspected | Pattern considered / deliberate adaptation |
| --- | --- |
| [OpenAI skill guide](https://learn.chatgpt.com/docs/build-skills) | Name/description metadata and progressive disclosure; portable source plus explicit runtime discovery guidance. |
| [Matt Pocock skills](https://github.com/mattpocock/skills) | Narrow recipes and task routing; retain the requested 15 workflows without importing a broader skill suite. |
| [grilling](https://github.com/mattpocock/skills/blob/main/skills/productivity/grilling/SKILL.md), [grill-me](https://github.com/mattpocock/skills/blob/main/skills/productivity/grill-me/SKILL.md), [grill-with-docs](https://github.com/mattpocock/skills/blob/main/skills/engineering/grill-with-docs/SKILL.md) | Repository facts before product questions; use one decision cluster, bounded scope and explicit persistence instead of mandatory exhaustive questioning or delegation. |
| [domain-modeling](https://github.com/mattpocock/skills/blob/main/skills/engineering/domain-modeling/SKILL.md) | Scenario-grounded terminology; use the project's existing knowledge map and distinguish confirmed rules from proposals. |
| [to-spec](https://github.com/mattpocock/skills/blob/main/skills/engineering/to-spec/SKILL.md), [to-tickets](https://github.com/mattpocock/skills/blob/main/skills/engineering/to-tickets/SKILL.md) | Synthesis and observable slices; use existing local templates, without mandatory external publication or fixed document size. |
| [implement](https://github.com/mattpocock/skills/blob/main/skills/engineering/implement/SKILL.md) | Incremental validation and review; intentionally omit its automatic commit instruction. |
| [tdd](https://github.com/mattpocock/skills/blob/main/skills/engineering/tdd/SKILL.md) | Behavioral assertions and incremental feedback; retain red-green-refactor, without routine test-boundary approval ceremonies. |
| [diagnosing-bugs](https://github.com/mattpocock/skills/blob/main/skills/engineering/diagnosing-bugs/SKILL.md), [triage](https://github.com/mattpocock/skills/blob/main/skills/engineering/triage/SKILL.md) | Evidence-led diagnosis and classification; avoid automatic tracker transitions, arbitrary hypothesis counts and unbounded reproduction loops. |
| [architecture improvement](https://github.com/mattpocock/skills/blob/main/skills/engineering/improve-codebase-architecture/SKILL.md) | Inspect real architectural friction; assess independently without compulsory HTML reports, redesign, delegation or imposed domain terminology. |
| [Matt Pocock code-review](https://github.com/mattpocock/skills/blob/main/skills/engineering/code-review/SKILL.md), [OpenAI review-agent](https://github.com/openai/codex/blob/main/codex-rs/skills/src/assets/samples/review-agent/SKILL.md), [OpenAI review rubric](https://github.com/openai/codex/blob/main/codex-rs/prompts/templates/review/rubric.md) | Actual-change inspection and actionable, evidence-based findings; include dirty/untracked state, distinguish baseline risks, and use the requested BLOCKER/MAJOR/MINOR/NOTE vocabulary. |

Research, bounded prototypes, threat-driven review, release recommendations and concise
handoff are tailored to the Product Owner's requested operating model. External patterns
inform implementation; they neither supply approval nor replace the canonical policy.

The design-brief, ui-design and visual-review recipes were authored for the Product
Owner's Design System & Visual Governance work package (2026-10-04). They integrate
persistent repository design context with the existing quality model. No OpenDesign
code, skill text or assets are vendored; no dependency or API compatibility is implied.
The manifest and semantic token conventions are local portable formats that a future
optional adapter could map. Original authorship is not a license assessment of any
external design reference; record those rights per reference before reuse.

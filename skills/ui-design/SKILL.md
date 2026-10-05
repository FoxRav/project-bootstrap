---
name: ui-design
description: "Implement or change visual interfaces and outputs using the repository's persistent design context, semantic tokens and existing approved patterns."
---

# ui-design

## Purpose

Translate authorized product work into consistent visual output governed by the project design baseline.

## Use when

Changing UI components, layout, fonts, colors, effects, dashboards, pages, presentations, branded documents or other visual output.

## Do not use when

Work has no visual impact, or the request is review only. Use design-brief when the needed design intent remains unresolved.

## Required context

Read the work item, [project context](../../docs/PROJECT.md), applicable instructions and [testing commands](../../docs/TESTING.md). Before implementation, load [manifest](../../design/manifest.json), [DESIGN.md](../../design/DESIGN.md), [tokens](../../design/tokens.css), [reference index](../../design/references/README.md), relevant approved references and the existing UI/output and implementation.

## Inputs

Authorized behavior and acceptance criteria, design baseline, existing components, relevant states/viewports and renderer constraints.

## Process

1. Establish actual visual scope and load the required context in the order above. Do this explicitly in any runtime; native skill discovery is not assumed.
2. Check applicability and status. If the manifest is template, disabled or draft and the work needs a baseline, route to design-brief. An explicitly authorized exploratory prototype may proceed with its assumptions labeled; it cannot establish approved project identity.
3. Reuse approved components and patterns. Compare the planned change against Design DNA, negative specification and reference use boundaries. Resolve conflicting authorities through Bootstrap policy, not aesthetic preference.
4. Implement the bounded behavior using semantic tokens instead of arbitrary visual literals. Use the same semantic roles through a documented mapping for non-CSS output. Add a token only for a real reusable role and keep its meaning and value coherent.
5. Cover relevant responsive layouts, content density, empty/loading/error states, keyboard/focus behavior, contrast and reduced-motion needs. Record constraints rather than silently dropping requirements.
6. Run applicable behavioral/static checks and inspect actual rendered output. Update design context only when the task authorizes a lasting design change; do not regenerate it or introduce a new style because a reference looks attractive.
7. Submit actual rendered evidence and ordinary work-item evidence for visual-review and any required independent review. Repair scoped findings and recheck affected output.

## Decision points

Preserve existing approved design, including deliberate exceptions to generic defaults. A new visual surface in a non-visual project requires applicability reassessment. Missing render access limits visual evidence; source inspection alone cannot establish visual success.

## Approval boundaries

Apply the [shared contract](../README.md#shared-contract). Existing task authorization covers routine implementation; identity replacement, dependencies and other consequential changes follow existing boundaries. This skill does not approve redesigns or reserved Git operations.

## Outputs

Working visual implementation, scoped tests, rendered evidence and any authorized canonical design updates.

## Completion criteria

Acceptance criteria and applicable quality checks are evidenced under the existing completion model. Unresolved design or visual-review blockers remain explicit.

## Evidence

Record revision/content identity, commands/results, views and states inspected, token/reference decisions, limitations and review findings using the existing review record.

## Handoff

Give [visual-review](../visual-review/SKILL.md) the implemented scope, actual output, relevant design context and evidence. Follow the normal independent review and Product Owner Git handoff.

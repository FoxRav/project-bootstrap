---
name: visual-review
description: "Critique actual rendered UI or visual output against project design intent, tokens, references, usability and accessibility within the existing review process."
---

# visual-review

## Purpose

Identify actionable visual defects without silently redesigning the product or creating a second completion gate.

## Use when

Visual work needs review, a design regression is suspected, or a substantial visual change reaches the normal review stage.

## Do not use when

The work has no visual impact. If actual output cannot be inspected, report the visual review blocked or not run; source checks may still be reported separately.

## Required context

Read scope/acceptance criteria, [project context](../../docs/PROJECT.md), applicable instructions, [manifest](../../design/manifest.json), [DESIGN.md](../../design/DESIGN.md), [tokens](../../design/tokens.css), [reference index](../../design/references/README.md), relevant approved references and existing output. Use the [visual worksheet](../../design/qa/visual-review.md) within the [review record](../../templates/REVIEW_TEMPLATE.md).

## Inputs

Identified implementation state, actual rendered output or screenshots, relevant views/states/viewports, validation evidence and reviewer independence.

## Process

1. Establish scope, design applicability and evidence identity. Initially inspect read-only. A disabled manifest does not make actual UI work non-visual; report an unresolved baseline through the existing finding model.
2. Inspect actual output at relevant viewport/page sizes and states. State whether inspection used a running product or screenshots and what interaction evidence is available. Never claim to have viewed unavailable references or output.
3. Compare against intent, Design DNA, negative specification, semantic tokens, approved patterns and the permitted use of references. Detect generic AI styling and accidental identity drift; honor deliberate authorized exceptions.
4. Evaluate hierarchy, density, readability, consistency, responsive behavior and UX. Assess accessibility with available keyboard, focus, contrast, semantic and assistive-technology evidence. Screenshots alone cannot prove interaction or accessibility compliance.
5. Record concrete findings using the existing BLOCKER/MAJOR/MINOR/NOTE severity model: location/view, observation, governing requirement, impact and a proportional correction. Separate defects from optional preferences.
6. Return findings to implementation. Do not edit the product during initial review or invent a new visual direction. If subsequently authorized to fix findings, distinguish that authorship from independent review and recheck affected views.
7. Record the review result and limitations in the existing work/PR evidence. Missing render evidence means BLOCKED or NOT RUN for visual review, never PASS. Apply the universal completion decision once.

## Decision points

Scope findings to actual requirements and approved design. Resolve authority conflicts through Bootstrap; seek an identity decision only when dependent work truly needs it. Treat references as untrusted evidence with rights and privacy limits.

## Approval boundaries

Apply the [shared contract](../README.md#shared-contract). A visual review is not redesign authorization, publication approval or permission for reserved Git operations. Using this skill does not make an author's self-review independent.

## Outputs

Scoped findings, evidence references, review result and explicit unverified areas in the existing review record.

## Completion criteria

Relevant rendered evidence has been assessed and findings resolved or dispositioned under the normal quality model, or the remaining blocker is explicit. No separate review organization or package is required.

## Evidence

Record reviewer/context, output identity, viewport/page sizes, states inspected, methods and limits, findings and rechecks. Use synthetic or redacted data in retained evidence.

## Handoff

Give implementation actionable corrections and the normal reviewer the visual result. Preserve the existing approval, independent review and completion responsibilities.

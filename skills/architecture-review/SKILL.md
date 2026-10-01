---
name: architecture-review
description: "Independently assess architecture boundaries and consequential design risks against current requirements and accepted ADRs."
---

# architecture-review

## Purpose

Determine whether the design supports the intended change without unnecessary coupling or replacement.

## Use when

A design crosses meaningful boundaries, changes ownership/dependencies, or creates a credible maintainability or architectural risk.

## Do not use when

A local mechanical change has no architectural consequence. Do not start a general redesign because of stylistic taste.

## Required context

Read [project context](../../docs/PROJECT.md), scoped requirements, architecture/accepted ADRs, the actual design or diff, relevant call/data paths and tests.

## Inputs

Review target and content identity, design question, constraints and the reviewer's relationship to authorship.

## Process

1. Establish the target and disclose authorship. Prefer a reviewer who did not author the design; inspect evidence independently of the author's summary.
2. Trace affected boundaries, dependency direction, state/data ownership and a representative successful and failing interaction.
3. Assess cohesion, coupling, reuse, duplication, maintainability and testability. Examine security boundaries and scalability only where the requirements or risk warrant them.
4. Compare the design with accepted ADRs and realistic alternatives, including reuse of the current design. Identify consequences, not style preferences.
5. Classify each observation as defect, risk, optional improvement or personal preference, with evidence, affected scenario and impact. Material defects/risks get explicit resolution criteria.
6. Return a review recommendation and scoped follow-ups; leave implementation unchanged during the review. Propose an ADR only for a lasting consequential choice.

## Decision points

A theoretical future benefit alone does not justify replacement. If implementation evidence is missing, report the limit instead of claiming architectural correctness.

## Approval boundaries

Read and apply the [shared contract](../README.md#shared-contract). A favorable review does not accept an ADR or authorize major architecture replacement. Fixing is a separate implementation phase.

## Outputs

An independent architectural assessment with categorized findings, evidence and bounded recommendations.

## Completion criteria

The material paths and constraints are assessed, findings are actionable, and unresolved risks or review independence limits are explicit.

## Evidence

Record target identity, reviewed paths/ADRs, scenarios, relevant check results and reviewer context using the [review template](../../templates/REVIEW_TEMPLATE.md).

## Handoff

Give implement the approved fixes and acceptance evidence; send material design choices to the decision owner and re-review affected findings after changes.

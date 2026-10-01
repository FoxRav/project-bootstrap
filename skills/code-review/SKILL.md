---
name: code-review
description: "Independently review an actual change and evidence for actionable defects, regressions and scope violations before any fixing phase."
---

# code-review

## Purpose

Challenge whether the change meets its intended behavior and preserves relevant invariants.

## Use when

Implementation is ready for review, or a specific diff/revision needs an independent assessment.

## Do not use when

The user requested implementation rather than review. Use architecture-review for a design-only question without an implementation change.

## Required context

Read the work item/spec, applicable instructions, actual diff and surrounding code/call sites, relevant tests and [completion evidence](../../templates/REVIEW_TEMPLATE.md).

## Inputs

Exact review target/base, changed and untracked files, expected behavior, exclusions, author evidence and reviewer identity.

## Process

1. Establish content identity and coverage. Inspect staged and unstaged changes plus intentional untracked files; for a branch review establish the comparison base. If Git is absent, use an identified file inventory/comparison and disclose limits.
2. Assume the implementation may be wrong. Trace normal, failure and edge paths against the specification; author claims are hypotheses until checked.
3. Examine relevant correctness, regressions, spec compliance, hidden scope expansion, architecture drift, duplicate logic, complexity, error handling, concurrency, data integrity, security and compatibility risks.
4. Inspect tests and suspicious generated code for missing coverage or false confidence. Run safe relevant checks if needed; distinguish their results from author-reported evidence.
5. Record concrete findings with location, triggering scenario, expected/actual effect, severity and remediation direction. Separate pre-existing issues from defects introduced by the change; do not hide a material baseline risk.
6. Complete the initial pass read-only. Return findings first, then review coverage, gaps and recommendation. If there are no actionable findings, say so without implying proof of absence.

## Decision points

BLOCKER prevents safe acceptance; MAJOR is a material defect requiring resolution; MINOR is a bounded lower-impact issue; NOTE is optional advice or context. Tie severity to impact. Label speculative questions rather than presenting them as defects.

## Approval boundaries

Read and apply the [shared contract](../README.md#shared-contract). Do not edit implementation in the initial review. Authorized fixes are a separate implement phase. A self-review is labeled self-review and cannot satisfy required independence.

## Outputs

Prioritized BLOCKER/MAJOR/MINOR/NOTE findings, review coverage and a pass/changes-required/limited-evidence recommendation.

## Completion criteria

The scoped change has been inspected; material findings and evidence gaps are explicit. Re-review resolved findings on the final state before acceptance.

## Evidence

Record reviewer context, target/base or content inventory, actual inspected paths, commands/results and concise scenario-based findings.

## Handoff

Send approved fixes to implement and unresolved decisions to their owner. Give release-readiness the final findings and recheck evidence only when a release assessment is requested.

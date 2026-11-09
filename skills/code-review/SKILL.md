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
2. **Requirements conformance:** derive observable criteria from the authorized work
   item/spec and trace each criterion through the changed behavior and relevant tests.
   Report met, unmet and unverified criteria separately; do not substitute code style
   or a passing test count for the specified outcome.
3. **Technical quality:** in a distinct pass, assess the changed implementation against
   actual repository conventions and concrete risks such as correctness, regression,
   maintainability, architecture, error handling, concurrency, data integrity,
   security and compatibility. Ground concerns in changed code and affected behavior,
   not a generic checklist or preference.
4. Inspect tests and suspicious generated code for missing coverage or false
   confidence. Run safe relevant checks if needed; state the exact command, observed
   result and whether the evidence is yours or author-reported.
5. Record concrete findings with location, triggering scenario, expected/actual effect,
   evidence, severity and remediation direction. Separate pre-existing issues from
   defects introduced by the change; do not hide a material baseline risk.
6. If the same verified failure pattern recurs, recommend one durable regression test
   or targeted update to the canonical project guidance. Do not duplicate rules or
   silently edit policy during a read-only review; use existing authority and approval
   rules for lasting policy changes.
7. Complete the initial pass read-only. Report requirements conformance and technical
   quality as separate dimensions, then give review coverage, evidence gaps and
   recommendation. A pass in one dimension does not cancel a defect in the other.

## Decision points

BLOCKER prevents safe acceptance; MAJOR is a material defect requiring resolution; MINOR is a bounded lower-impact issue; NOTE is optional advice or context. Tie severity to impact. Label speculative questions rather than presenting them as defects.

## Approval boundaries

Read and apply the [shared contract](../README.md#shared-contract). Do not edit implementation in the initial review. Authorized fixes are a separate implement phase. A self-review is labeled self-review and cannot satisfy required independence.

## Outputs

Separate requirements-conformance and technical-quality results, with prioritized
BLOCKER/MAJOR/MINOR/NOTE findings, review coverage and a
pass/changes-required/limited-evidence recommendation.

## Completion criteria

The scoped change has been inspected; material findings and evidence gaps are explicit. Re-review resolved findings on the final state before acceptance.

## Evidence

Record reviewer context, target/base or content inventory, acceptance-criterion
mapping, actual inspected paths, commands/results and concise scenario-based findings.

## Handoff

Send approved fixes to implement and unresolved decisions to their owner. Give release-readiness the final findings and recheck evidence only when a release assessment is requested.

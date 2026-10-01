---
name: implement
description: "Execute an approved bounded work item incrementally, preserve test integrity and finish ready for independent review."
---

# implement

## Purpose

Deliver the specified behavior with focused changes and honest completion evidence.

## Use when

A bounded task has sufficient intent and authority for implementation.

## Do not use when

The user requested review only or unresolved product decisions block the change. Use diagnose-bug when the cause of a defect is still unknown.

## Required context

Read the active work item, [project context](../../docs/PROJECT.md), applicable scoped instructions, affected code/tests and relevant accepted ADRs. Use [testing commands](../../docs/TESTING.md).

## Inputs

Authorized scope, acceptance criteria, exclusions, validation plan and existing approval sources.

## Process

1. Read the active scope and inspect current implementation, tests, patterns and dirty/untracked work. Record baseline failures and reuse opportunities.
2. Identify unexpected risks, authority conflicts or scope changes. Pause only the affected approval-gated action; continue safe work and present a concrete decision when needed.
3. Implement one coherent increment at a time within scope. Use tdd when it materially improves behavior/regression confidence.
4. Run targeted checks after meaningful changes and investigate failures. Never weaken valid tests or relax lint, type or static-analysis rules to hide a defect.
5. Update affected canonical documentation and work checkpoints. Do not silently expand scope or replace architecture.
6. Run applicable broader validation, inspect the final changes and prepare [review evidence](../../templates/REVIEW_TEMPLATE.md), including omissions and unresolved findings.
7. Finish ready for the applicable review, with exact content identity and remaining approvals. Non-trivial work needs independent review; routine work may use labeled self-review. Separate implementation readiness from the universal completion and release decisions.

## Decision points

Reuse an existing path when coherent. If acceptance criteria prove contradictory or unsafe, resolve the conflict before dependent implementation; do not quietly revise the goal.

## Approval boundaries

Read and apply the [shared contract](../README.md#shared-contract). Do not run `git commit` or `git push`; the Product Owner performs them manually unless there is an explicit current-task override under Git authority. General completion instructions are insufficient.

## Outputs

Scoped implementation, relevant tests/docs and evidence ready for a reviewer.

## Completion criteria

Behavior is implemented and applicable checks are evidenced, or remaining blockers are explicit. Non-trivial work awaits independent review before being declared complete.

## Evidence

Record commands/cwd/results, baseline versus new failures, acceptance mapping, author review, status/diffs and any required approval sources.

## Handoff

Provide code-review the actual work item, final changed files and evidence. Recommend commit boundaries/message for the Product Owner when useful; execution remains with the owner.

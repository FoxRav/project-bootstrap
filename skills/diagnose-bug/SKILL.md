---
name: diagnose-bug
description: "Investigate a defect through reproduction, baseline, isolation and evidence before applying a minimal verified fix."
---

# diagnose-bug

## Purpose

Find the cause of a reported failure and correct it without speculative patching.

## Use when

Observed behavior differs from intended behavior and the cause needs investigation.

## Do not use when

The requested behavior is an undecided product change. A fully established cause and approved fix can go directly to implement with regression evidence.

## Required context

Read the bug report, affected expectations, [project context](../../docs/PROJECT.md), relevant code/tests, safe logs and [testing commands](../../docs/TESTING.md).

## Inputs

Symptom, expected/actual behavior, environment/version, reproduction information and authorized repair scope.

## Process

1. State the symptom and intended behavior with sources; preserve useful redacted evidence.
2. Reproduce with the smallest safe input. Establish the baseline, including whether the failure predates current changes.
3. Isolate affected paths, state and timing. Form ranked hypotheses and choose observations that distinguish them.
4. Test one falsifiable hypothesis at a time with a targeted check. Record the exact
   command/input and observed result, compare it with the prediction, and revise or
   reject the hypothesis rather than making random fix attempts.
5. Explain the causal chain from triggering conditions through the faulty mechanism
   to the observed symptom. Distinguish a demonstrated root cause from a plausible
   explanation and name the evidence that supports or weakens it.
6. Add a regression test at a seam that exercises the real failure where feasible,
   then make the minimal in-scope fix. Treat changes to unrelated code as separate
   work unless evidence makes them necessary.
7. When a verified cause recurs and generalizes, convert the lesson into one focused
   regression test or one update to the canonical project guidance. Do not create
   duplicate rules or change authority/policy without its existing approval.
8. Run targeted validation, relevant broader regression validation and review the
   final change independently under the quality policy.

## Decision points

If reproduction is unreliable, bound the investigation, capture frequency/conditions and propose the next discriminating experiment. Report an unproven cause honestly; do not invent a fix or claim success.

## Approval boundaries

Read and apply the [shared contract](../README.md#shared-contract). Shared/production data, destructive commands, dependency or contract changes retain their boundaries. Diagnosis does not authorize unrelated cleanup or history rewriting.

## Outputs

A causal explanation tied to observed evidence, reproduction/regression results and
minimal fix, or a precisely bounded unresolved investigation.

## Completion criteria

For a fix, the original failure is addressed and relevant regressions/review are evidenced. Otherwise state what remains unknown and who/what can resolve it.

## Evidence

Record symptom, baseline, reproduction, each tested prediction and result, hypotheses
ruled in/out, causal evidence, exact test commands/results, durable lesson if repeated,
and any validation gaps.

## Handoff

Send code-review the causal chain and fix; if blocked, handoff the next experiment, retained safe artifacts and unresolved conditions.

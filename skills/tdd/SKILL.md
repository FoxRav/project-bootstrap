---
name: tdd
description: "Use behavior-focused red-green-refactor cycles for bugs, business rules, parsers, transformations, APIs and regressions when useful."
---

# tdd

## Purpose

Prove a behavior change with a test that detects the defect and remains useful through refactoring.

## Use when

A behavior or regression can be expressed as a meaningful repeatable test and test-first work materially improves confidence.

## Do not use when

A trivial documentation or mechanical edit has no useful behavioral assertion. Use the appropriate validation instead of inventing tests.

## Required context

Read the bounded task, affected implementation and tests, relevant domain rules and [testing commands](../../docs/TESTING.md). Inspect baseline behavior before choosing a test boundary.

## Inputs

Expected observable behavior, representative input/output or failure case, authorized scope and available test harness.

## Process

1. Define or reproduce the behavior at a stable observable boundary, including a failure/edge case relevant to the risk.
2. Add one focused test with an independently known expectation. Run it and confirm it fails for the intended behavioral reason, not a broken import or fixture.
3. Make the smallest coherent implementation change that satisfies that behavior; run the test and related checks.
4. Refactor when useful while keeping tests green and preserving scope. Avoid coupling assertions to private implementation structure.
5. Repeat by behavior slice, then run applicable broader regressions and inspect whether the tests would catch the original failure.
6. Record red/green evidence and any limits, including when an existing passing test or infeasible reproduction prevented a new red phase.

## Decision points

Choose the test level that observes the risk without excessive mocking. Do not force a test boundary approval ceremony for routine additions; a new public contract follows normal approvals.

## Approval boundaries

Read and apply the [shared contract](../README.md#shared-contract). Do not delete or weaken valid coverage or quality gates to make tests pass. New tooling dependencies need their normal approval.

## Outputs

Behavioral regression coverage, minimal implementation and any justified refactoring within the authorized task.

## Completion criteria

The tests demonstrate intended behavior, failure causes are understood, and applicable broader checks are recorded.

## Evidence

Record the failing and passing commands/results, expected behavior, fixture assumptions and wider regression result; do not fabricate a red phase.

## Handoff

Return the change and test rationale to implement/code-review, identifying what remains untested and why.

---
name: testing-strategy
description: "Choose risk-based test boundaries and acceptance evidence for a technical change, API, data flow or operational behavior."
---

# testing-strategy

## Purpose

Select the smallest credible test portfolio that detects the change's realistic failure
modes, with evidence tied to requirements rather than a universal test checklist.

## Use when

A non-trivial behavior, contract, security boundary, data change or reliability claim
needs a validation plan or acceptance evidence.

## Do not use when

A trivial edit has an obvious deterministic check. Do not add a test framework or
require every test category for every project.

## Required context

Read project `docs/TESTING.md`, actual commands and fixtures, target boundary,
acceptance criteria, change risks and existing tests. Use `tdd` for a useful
red-green-refactor loop.

## Inputs

Observable requirement, affected users/components, important negative/failure states,
available environments, test cost and limits.

## Process

1. Translate each acceptance criterion into an observable assertion and identify the
   defect or regression it should catch.
2. Choose a test boundary close enough to isolate behavior but real enough to exercise
   the risk: unit, component, integration, contract, end-to-end, load, security or
   recovery. Justify omitted layers.
3. Include boundary inputs, authorization/invalid data where relevant, duplicate or
   concurrent operations, timeout/partial failure and recovery when those risks exist.
4. Use deterministic synthetic fixtures and controlled dependencies. Do not target
   live systems, production data or unapproved third parties.
5. Run the exact documented command; distinguish a failing assertion from a broken
   fixture/environment. Preserve valid existing assertions and gates.
6. Check that the test would fail for the hypothesized defect and remains meaningful
   after refactoring. Avoid testing implementation details unrelated to the contract.
7. Map acceptance criterion → test/evidence → result; report unavailable layers,
   uncertainty and any required review/approval.

## Decision points

Prefer one focused test at the narrowest boundary that proves the claim, plus broader
tests only for cross-boundary risks. Security scans and tabletop walkthroughs are
evidence with bounded scope, not proof of security or future runtime behavior.

## Approval boundaries

Apply the [shared contract](../README.md#shared-contract), [authority](../../PROJECT_BOOTSTRAP.md#1-authority-and-evidence)
and [approval boundaries](../../PROJECT_BOOTSTRAP.md#4-autonomy-and-approval-boundaries).
Never delete or weaken valid coverage, lower a gate or add test dependencies to force
a pass; such changes follow the explicit approval rules.

## Outputs

Risk-to-test matrix, exact test commands and results, acceptance mapping and visible
omissions. Keep detailed logs only when useful for reproduction.

## Completion criteria

Every acceptance criterion has evidence or an explicit gap; test boundaries are
appropriate; the reported state distinguishes tested runtime from design review.

## Evidence

Record revision, environment, command, exit code, relevant test count, fixture
assumptions, failures and limitations. A scenario review evaluates instructions or
design, not application runtime.

## Handoff

Use `tdd` during implementation and `code-review` to assess the actual diff; use
security/architecture review only where their independent scope applies.

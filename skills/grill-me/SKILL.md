---
name: grill-me
description: "Clarify an unclear idea or challenge a design before implementation, without automatically updating project documents."
---

# grill-me

## Purpose

Expose consequential ambiguity until the next decision or bounded work can be stated clearly.

## Use when

An idea has competing interpretations, hidden constraints or unresolved product choices.

## Do not use when

The accepted behavior is already clear; use to-spec or implement. Prefer grill-with-docs when confirmed decisions should update project sources.

## Required context

Read [project context](../../docs/PROJECT.md), the active request and only the affected code, tests, current requirements and accepted ADRs. Inspect repository facts before interviewing.

## Inputs

The idea, intended outcome, known constraints and decision owner; missing product choices may remain unknown.

## Process

1. Inspect existing behavior and documents; list what can be answered without the Product Owner.
2. Separate sourced facts, assumptions, confirmed decisions and unknowns. Identify contradictory intent using the shared conflict procedure.
3. Rank remaining decisions by impact and dependency. Use a concrete normal scenario and a failure/edge scenario to expose hidden rules.
4. Ask one focused decision cluster at a time, with meaningful options, trade-offs and a recommendation. Wait for the answer before dependent work; continue safe factual inspection.
5. Reconcile the answer with existing constraints. Record its source and scope in the conversation or requested decision summary; do not treat silence as agreement.
6. Stop questioning once enough is settled for the requested outcome. Summarize settled choices and the smallest remaining blocker.

## Decision points

Look up facts; ask for product choices. Return a bounded partial understanding if a decision remains unavailable. Do not demand answers to unrelated future questions.

## Approval boundaries

Read and apply the [shared contract](../README.md#shared-contract). This skill does not automatically edit canonical documents or start implementation. A consequential choice still needs the relevant decision authority.

## Outputs

A concise decision-ready summary with facts, assumptions, decisions, unknowns and recommended next step.

## Completion criteria

The requested ambiguity is resolved or precisely blocked; the next step has clear scope and no hidden product assumptions.

## Evidence

Cite inspected paths, behavior observations and the source/date of confirmed decisions. Label untested assertions.

## Handoff

Pass the summary and unresolved dependencies to grill-with-docs for requested persistence, or to-spec once design intent is sufficiently understood.

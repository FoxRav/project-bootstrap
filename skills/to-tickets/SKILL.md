---
name: to-tickets
description: "Decompose an accepted specification into bounded executable work items with observable increments and clear dependencies."
---

# to-tickets

## Purpose

Let a fresh agent execute one coherent slice without reconstructing the entire discussion.

## Use when

An accepted spec is too large or dependent to implement as one bounded work item.

## Do not use when

The scope already fits one clear task. Unsettled product decisions require definition, not speculative tickets.

## Required context

Read the accepted spec and its authority, [project context](../../docs/PROJECT.md), relevant architecture/ADRs, affected implementation and the [work-item template](../../templates/WORK_ITEM_TEMPLATE.md).

## Inputs

Accepted behavior and exclusions, constraints, dependencies, priority and known risks or approval conditions.

## Process

1. Verify the spec's acceptance and inspect the current state enough to avoid planning duplicate work.
2. Find the smallest observable end-to-end behavior; prefer vertical slices or tracer bullets over separate database/backend/frontend batches where practical.
3. Order slices by dependency and uncertainty. Isolate a research/prototype task when a prerequisite is unresolved; explain unavoidable enabling or migration-only work.
4. Create each work item using the existing template: goal/context, scope/exclusions, required current-state inspection, affected components, acceptance criteria and validation plan.
5. Add dependencies, risks, approval triggers and completion evidence expectations. Include source links so a fresh session can start without chat history.
6. Check acceptance coverage, duplication and dependency cycles. Identify work that is ready, blocked or proposed, and summarize recommended execution order.

## Decision points

Split by independently verifiable outcomes, not arbitrary size. Keep the plan adaptable when current-state inspection reveals new facts; do not silently expand the accepted spec.

## Approval boundaries

Read and apply the [shared contract](../README.md#shared-contract). Ticket creation does not approve its proposed high-risk actions. Draft locally; external issue creation or updates require the authorized destination and scope.

## Outputs

A bounded work-item set with acceptance coverage, sequencing and explicit readiness/approval state.

## Completion criteria

Each ready item can be executed in a fresh context, produces verifiable progress and has no hidden blocking dependency.

## Evidence

Map spec criteria to work items, note inspected components and record why any horizontal enabling task is necessary.

## Handoff

Give implement the first ready item and its dependency context. Keep one canonical copy of each item.

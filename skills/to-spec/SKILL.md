---
name: to-spec
description: "Turn sufficiently understood product and design decisions into an implementation-ready specification without restarting discovery."
---

# to-spec

## Purpose

Translate settled intent into behavior and acceptance criteria an implementer can execute.

## Use when

A feature or change is understood but lacks a coherent implementation specification.

## Do not use when

Core product choices remain unsettled; route only those choices to grill-with-docs. Do not rewrite an adequate accepted spec for ceremony.

## Required context

Read confirmed decisions, [project context](../../docs/PROJECT.md), affected code, relevant accepted ADRs/glossary and applicable research or prototype findings.

## Inputs

Goal, confirmed decisions, constraints, current behavior and the intended specification destination.

## Process

1. Reconcile the supplied decisions with current sources; identify gaps without reopening settled choices unnecessarily.
2. State goal, user/system behavior, in scope, out of scope and constraints.
3. Identify affected components, interfaces and ownership, including compatibility, error/edge cases and relevant data/security boundaries.
4. Write observable acceptance criteria and validation expectations tied to behavior, including failure paths and regressions.
5. Separate implementation choices that remain autonomous from unresolved blockers and approval-gated decisions; label the spec draft or accepted with its actual authority.
6. Update the existing spec/work item or create the smallest useful source and link it from project context. Check consistency and give the owner a decision-ready result.

## Decision points

A routine change can use the [work-item template](../../templates/WORK_ITEM_TEMPLATE.md) or a short task record. For new evidence, amend the spec and record the changed decision; it is not immutable.

## Approval boundaries

Read and apply the [shared contract](../README.md#shared-contract). Writing a spec does not accept proposed contracts, schemas or architecture. Publishing it to an external tracker is a separate authorized effect.

## Outputs

A specification containing goal, behavior, scope/exclusions, constraints, affected components/interfaces, edge cases, acceptance criteria, validation and unresolved blockers.

## Completion criteria

A fresh implementer can identify the intended behavior, boundaries, checks and remaining decisions; the document's approval status is accurate.

## Evidence

Link each consequential requirement to its decision/source and identify inspected code, accepted ADRs and supporting experiments.

## Handoff

Give an accepted scope to to-tickets or implement; send only blocking ambiguity back to definition/research.

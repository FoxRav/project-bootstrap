---
name: grill-with-docs
description: "Clarify product or project intent and write confirmed decisions into their existing canonical sources."
---

# grill-with-docs

## Purpose

Make early definition durable while resolving the decisions that would otherwise cause implementation drift.

## Use when

Defining a project or feature, reconciling design ambiguity, or capturing decisions in current project knowledge. This is the preferred early definition route.

## Do not use when

Only a conversational challenge is wanted; use grill-me. Do not rediscover a settled specification.

## Required context

Read [project context and its knowledge map](../../docs/PROJECT.md), the active request, affected code/tests and the relevant current requirements, glossary and accepted ADRs.

## Inputs

Idea or problem, existing decision sources, requested documentation scope and any unresolved owner choices.

## Process

1. Inspect the repository first. Separate observed facts, assumptions, confirmed decisions and unknowns; answer factual questions from available evidence.
2. Locate the current canonical home for each topic. Ask only consequential unresolved questions, one decision cluster at a time, with alternatives and a recommendation.
3. Capture explicit answers with authority, source and scope. Keep unanswered matters visibly open; do not promote a suggestion into an approved requirement.
4. Update the existing project context, PRD, architecture, glossary or active work item that owns the fact. Split a document only when useful, replacing the original material with a link and updating the context map.
5. Use the [ADR template](../../templates/ADR_TEMPLATE.md) for a lasting consequential technical choice; keep it Proposed until the appropriate authority accepts it.
6. Check the edited sources against each other and relevant observed behavior. Show the changed decisions, open questions and any approval still needed.

## Decision points

Persist confirmed intent; mark conflicting runtime behavior separately. If the requested outcome is already documented, link it instead of duplicating it. Load domain-modeling only when vocabulary needs work.

## Approval boundaries

Read and apply the [shared contract](../README.md#shared-contract). Documentation edits within the requested definition work are autonomous; recording a proposal does not authorize its implementation or accept an ADR.

## Outputs

Updated canonical sources and a short decision/open-question summary, without a parallel specification store.

## Completion criteria

Confirmed decisions are findable at one authoritative location, links are valid, and unresolved decisions block only dependent work.

## Evidence

Record decision sources, affected paths, discrepancies and documentation/link checks. Distinguish new approval from already supplied instructions.

## Handoff

Give to-spec the confirmed decisions and links, or give research/prototype a specific uncertainty. Identify the decision owner for each blocker.

---
name: handoff
description: "Transfer current work into a fresh human or agent context with concise state, evidence, decisions and the next action."
---

# handoff

## Purpose

Make work resumable without dependence on conversation memory.

## Use when

A session pauses, ownership changes, review begins or completed work needs a concise transfer.

## Do not use when

The existing current checkpoint already suffices. Do not create a second competing work record or dump the entire conversation.

## Required context

Read the active work item, [project context](../../docs/PROJECT.md), actual current content/status, decision sources and relevant checks/review findings.

## Inputs

Goal, destination role, current state, completed/remaining scope and available evidence.

## Process

1. Inspect the actual state, including revision and dirty/untracked work. If Git is absent, provide an identified file inventory/hash and disclose the limit.
2. Update the existing work checkpoint or requested handoff destination with goal, progress and decisions already made, including approval sources.
3. List affected files/components and the minimum context links required next; preserve unresolved assumptions and questions explicitly.
4. Record tests/checks actually run with results, current failures, blockers and review status. Distinguish outdated evidence and unrun checks.
5. Specify the next recommended action, its prerequisites and owner. Include safe reproduction commands when useful.
6. Confirm the summary matches current files. Add proposed commit boundaries/message or manual commands for the Product Owner only when relevant.

## Decision points

Link durable decisions rather than retelling discussion. Use the repository directly for review; choose a frozen package only when an applicable handoff need or explicit request makes it useful.

## Approval boundaries

Read and apply the [shared contract](../README.md#shared-contract). Preparing a handoff does not authorize sending it externally, publishing, releasing or executing reserved Git operations.

## Outputs

One concise handoff/checkpoint containing goal, state/identity, decisions, files, checks/failures, blockers, open questions, next action and context links.

## Completion criteria

A fresh agent can identify what to do next and what it may not yet do, with no hidden dependence on chat history.

## Evidence

Record inspected status/content identity and links to actual validation/review results; disclose any evidence-only edits after testing.

## Handoff

The receiving person or selected skill resumes at the stated next action after confirming the current state; it need not replay completed stages.

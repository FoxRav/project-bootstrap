---
name: release-readiness
description: "Assess a specific revision or artifact against release evidence and approvals without authorizing or performing release."
---

# release-readiness

## Purpose

Give the Product Owner an evidence-based recommendation for a particular release candidate.

## Use when

An identified revision/artifact is being considered for release approval.

## Do not use when

Routine local work only needs implementation/review evidence. A readiness assessment is not a deployment instruction.

## Required context

Read the release scope, [project context](../../docs/PROJECT.md), relevant deployment/recovery guidance, [testing requirements](../../docs/TESTING.md), final review findings and approvals.

## Inputs

Exact candidate identity, intended environment, release scope, evidence and required decision owners.

## Process

1. Identify the candidate revision and dirty content or artifact digest. Establish that the tested, reviewed and proposed release contents correspond.
2. Check applicable validation results and unresolved review findings, including whether later edits invalidated evidence.
3. Assess migrations, configuration, secrets provisioning, deployment assumptions, compatibility and rollback/recovery against the actual release risk. Mark irrelevant areas N/A with reasons.
4. Check release notes and operational handoff where relevant; identify missing access, configuration or recovery prerequisites.
5. Inventory required Product Owner approvals with source, scope, environment and candidate identity. Treat absent or mismatched approvals as pending.
6. Return ready-for-approval, blocked or incomplete-evidence with concrete next actions. Do not execute a release or any reserved Git operation.

## Decision points

If content changes, reassess affected evidence. Existing approval counts only for its exact scope; a ready recommendation does not create approval.

## Approval boundaries

Read and apply the [shared contract](../README.md#shared-contract). This skill authorizes no release, deployment, migration execution or Git mutation. Product Owner release approval and any current-task Git override are distinct.

## Outputs

A candidate-specific readiness recommendation with evidence, blockers and pending approvals.

## Completion criteria

The decision owner can identify precisely what is proposed, what was verified, remaining risk and which action needs approval.

## Evidence

Record revision/artifact identity, environment, validation/review links, migration/configuration/recovery checks and exact approval sources or gaps.

## Handoff

Give the Product Owner the recommendation and manual next steps. Give the authorized release operator only the approved candidate/action; use handoff for continuing context.

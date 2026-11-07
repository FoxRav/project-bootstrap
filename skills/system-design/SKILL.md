---
name: system-design
description: "Design or materially change a software system or capability when requirements, boundaries, failure behavior or trade-offs need an explicit technical design."
---

# system-design

## Purpose

Turn confirmed product needs into a bounded architecture decision that can be
implemented and operated without assuming microservices, cloud vendors or a
particular scale.

## Use when

The task creates or materially changes a service, subsystem, data flow, deployment
boundary or quality attribute whose design choices have meaningful consequences.

## Do not use when

The task is a local bug fix or a small change within an accepted design. Do not
redesign the system solely because a new pattern or technology is available.

## Required context

Read [project context](../../docs/PROJECT.md), accepted ADRs, the relevant code and
tests, actual runtime/deployment constraints and [testing requirements](../../docs/TESTING.md).
Load only the technical skills triggered by the design. Use the
[programming principles reference](../references/programming-principles.md) when a
specific abstraction or dependency-boundary decision needs a shared vocabulary.

## Inputs

Confirmed user outcomes, constraints, existing behavior, expected load and latency
where known, data sensitivity, availability needs and unresolved decisions. Separate
facts, estimates and product-owner questions.

## Process

1. Trace one representative successful user flow and one important failure or recovery
   flow through the current system; identify ownership, trust and persistence boundaries.
2. Convert the request into functional outcomes and measurable quality constraints.
   Record unknown load, latency, retention, recovery and compatibility values instead
   of inventing targets.
3. Sketch the smallest viable design and at least one realistic alternative when a
   consequential trade-off exists. Compare failure modes, state ownership, operational
   burden, security, cost and migration risk.
4. Choose boundaries based on change ownership and consistency needs. Keep a single
   process or shared database when it meets the requirements; introduce remote service,
   queue or replication boundaries only for an evidenced need.
5. Define each boundary's contract: inputs, outputs, errors, timeout, retries,
   idempotency, ordering, data ownership and observability. Route API, data, security,
   cache and concurrency details to their relevant skills.
6. Describe deployment, rollback, restore and partial-failure behavior proportional
   to the design. Distinguish an accepted failure from silent data loss.
7. Record the decision, rejected alternatives, assumptions and validation evidence in
   an ADR only when it is a lasting consequential choice. Split approved implementation
   into bounded work slices.

## Decision points

Prefer the least complex design meeting verified requirements. Add redundancy only
with explicit consistency and failure behavior. A cache, queue or service boundary
must have an owner, invalidation/recovery plan and measurable reason. Product choices,
public contracts and persistent schema decisions follow existing approval rules.

## Approval boundaries

Apply the [shared contract](../README.md#shared-contract), [authority](../../PROJECT_BOOTSTRAP.md#1-authority-and-evidence)
and [approval boundaries](../../PROJECT_BOOTSTRAP.md#4-autonomy-and-approval-boundaries).
This recipe does not authorize public-contract, schema, security, deployment or
architecture decisions that require Product Owner approval.

## Outputs

A concise design or ADR when warranted: requirements/constraints, component and data
ownership, one primary flow and failure path, alternatives/trade-offs, decision points,
implementation slices and validation plan.

## Completion criteria

The design follows an actual requirement, identifies meaningful boundaries and failure
behavior, names assumptions and approvals, and is small enough to implement and review.

## Evidence

Link the inspected paths, accepted decisions, relevant diagrams or prose, load/latency
measurements if available, test plan and unresolved assumptions. Do not present a
tabletop or estimate as runtime evidence.

## Handoff

Send bounded decisions to `to-spec` or `to-tickets` when those deliverables are needed;
use `architecture-review` for independent assessment. Continue with only the skills
needed for implementation.

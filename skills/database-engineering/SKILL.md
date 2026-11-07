---
name: database-engineering
description: "Change data models, SQL, transactions, indexes, locking or migrations when correctness and database-specific guarantees need deliberate validation."
---

# database-engineering

## Purpose

Preserve data invariants and recoverability while making database changes that fit
measured access patterns and the selected engine's actual guarantees.

## Use when

Changing a persistent model, query, transaction boundary, index, lock behavior,
migration, backup or database scaling strategy.

## Do not use when

A change does not touch database behavior. Do not select or shard a database based
only on a generic comparison or scale slogan.

## Required context

Read project data ownership, schema and migration conventions, relevant queries,
accepted ADRs, supported database/version documentation, fixtures and test commands.
Use `data-engineering` for pipelines and `concurrency` for in-process shared state.

## Inputs

Data invariants, current rows/volumes, read-write shape, concurrency, retention,
availability/recovery needs, engine/version and migration constraints. Mark unknown
production distributions as unknown.

## Process

1. Identify the source of truth, owners, invariants and all readers/writers affected.
   Trace a successful operation, a conflicting write and a rollback/recovery path.
2. Inspect the engine/version documentation for isolation, constraints, null behavior,
   locking, transactional DDL, index semantics and failure modes used by the change.
3. Examine representative query plans and data cardinality where performance motivates
   a change. State the measurement and expected bottleneck before adding an index,
   denormalizing or partitioning.
4. Design a migration that handles existing and new data, deployment ordering, locks,
   backfill/retry, partial failure and rollback/forward repair. Do not silently drop,
   truncate or rewrite user data.
5. Encode invariants in constraints/transactions where appropriate. Establish the
   retry boundary for serialization/deadlock errors and ensure retrying cannot duplicate
   an external side effect.
6. Test empty, typical, boundary, duplicate and concurrent cases using isolated
   fixtures. Exercise migration from the supported prior state and verify rollback or
   the documented forward-repair path.
7. Compare plan/latency evidence against the baseline. Update the canonical schema,
   migration and operational documentation without copying vendor-specific behavior
   into universal claims.

## Decision points

Prefer declarative constraints and short transactions. Separate ACID properties,
isolation level and distributed consistency; do not infer database guarantees from
“SQL” or “NoSQL”. Data deletion, schema compatibility and production execution follow
the project's approval boundaries.

## Approval boundaries

Apply the [shared contract](../README.md#shared-contract), [authority](../../PROJECT_BOOTSTRAP.md#1-authority-and-evidence)
and [approval boundaries](../../PROJECT_BOOTSTRAP.md#4-autonomy-and-approval-boundaries).
Persistent schema changes require the specified approval; destructive migration or
shared-data execution requires the explicit target and recovery approval.

## Outputs

Invariant/data-flow notes, engine/version-specific decision, migration and recovery
plan, query evidence, tests and updated data documentation.

## Completion criteria

Existing data remains valid or has an approved transformation; constraints, failure
handling and rollback/repair behavior are testable; no production action is implied.

## Evidence

Record engine/version, schema diff, query-plan/measurement inputs, migration test
source state and result, concurrency cases, rollback limits and omitted production
checks. Never include production records or credentials.

## Handoff

Use `system-design` for system boundaries, `data-engineering` for ingestion/index
pipelines, and `testing-strategy` for risk-based test selection.

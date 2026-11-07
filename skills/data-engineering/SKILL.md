---
name: data-engineering
description: "Design or change batch/stream ingestion, CDC, data quality, search indexing, replay or data movement between systems."
---

# data-engineering

## Purpose

Make data movement, transformation and derived indexes explainable, recoverable and
consistent with their source contracts.

## Use when

The task changes ETL/ELT, batch or stream ingestion, CDC, data validation, search
indexing, checkpoints, replay or downstream data delivery.

## Do not use when

The change is only a transactional application database operation; use
`database-engineering`. Do not call database CDC Event Sourcing unless the source
actually stores domain events as its system of record.

## Required context

Read source/target schemas, ownership, retention, pipeline code, engine/version
documentation, data-quality expectations, privacy constraints and recovery commands.

## Inputs

Source of truth, schema/version, volume/arrival rate, ordering and lateness, freshness
objective, duplicates, deletion semantics, retention and consumer behavior.

## Process

1. Define source and destination contracts, record identity, time semantics, ownership
   and allowed transformations. Separate domain events from row-change capture.
2. Determine batch/stream cadence from freshness and cost needs. Specify ordering,
   late data, duplicate detection, schema evolution, tombstones and backpressure.
3. Advance a source checkpoint only after its result is durably stored, or after
   responsibility for unfinished work has been transferred to a durable record that
   the recovery path actually processes. Persist enough to resume: source identity and
   position, operation identity, required payload or a guaranteed source reference,
   processing status/lease, and recovery owner. If output/work record and checkpoint
   share a transactional store, commit them in one transaction. If they are separate,
   durably write and verify the pending-work record first, then advance the checkpoint;
   never advance first and hope the work record is written afterward. A crash between
   those writes may replay the input, so processing and external side effects must be
   idempotent or reconcilable. Define which worker scans and claims pending work after
   restart, retry/lease behavior, and duplicate handling. Apply the same rule to broker
   offsets, cursors, watermarks and file positions. Source retention or a possible
   manual replay alone is not a transferred recovery responsibility.
4. Validate data at appropriate boundaries: schema, required fields, ranges,
   referential/aggregate invariants and quarantine behavior. Avoid silently dropping
   invalid records.
5. For indexes/derived views, define freshness, source version, rebuild, partial update,
   delete propagation and recovery from stale or corrupt state.
6. Test duplicate, reordered, late, malformed, deleted, partially written and replayed
   inputs using synthetic or approved fixtures. Verify counts/checksums/invariants.
7. Document lag/freshness metrics, alert owner, retention and repair/replay procedure;
   include sensitive-data restrictions.

## Decision points

A checkpoint may move past an item only when its result is durable or a durable pending
work record has taken over the item before checkpoint advancement, with a recovery
process that will actually resume it. If both are in one transactional store, commit
the result/work record and checkpoint together. If they are separate, durably write
and verify the pending record first, then advance the checkpoint; a crash between
those steps may replay the source item and therefore requires idempotent/reconcilable
processing. Never advance the checkpoint first. A source that still retains the input,
or an operator who could manually replay it, is not by itself a transferred recovery
responsibility. Specify persisted resume data, checkpoint/handoff ordering, post-crash
owner and path, and duplicate/external-effect handling. CDC exposes storage changes;
it does not define business meaning. Choose a search index as a rebuildable projection
unless the product explicitly makes it authoritative.

## Approval boundaries

Apply the [shared contract](../README.md#shared-contract), [authority](../../PROJECT_BOOTSTRAP.md#1-authority-and-evidence)
and [approval boundaries](../../PROJECT_BOOTSTRAP.md#4-autonomy-and-approval-boundaries).
Persistent schema, data retention/deletion, sensitive data movement and production
backfills use existing approval boundaries.

## Outputs

Source-target contract, transformation/checkpoint semantics, data-quality and
recovery plan, tests and freshness/lag evidence.

## Completion criteria

Duplicates, late data, schema changes, partial failure and rebuild/replay behavior are
defined; data loss or silent discard is not hidden.

## Evidence

Record source and target versions, fixture profile, validation counts, checkpoint
position, replay/rebuild result, lag and known data gaps. Do not include production
records in reports.

## Handoff

Use `database-engineering` for durable model/transaction changes and
`distributed-systems` for cross-process delivery and partial failure semantics.

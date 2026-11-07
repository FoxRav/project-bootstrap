---
name: caching
description: "Add, change or troubleshoot a cache, invalidation rule, eviction policy or cache failure path, including process-local caches."
---

# caching

## Purpose

Use caching only where measured value outweighs consistency, memory and operational
cost; make stale and unavailable behavior explicit.

## Use when

A local in-memory cache, shared cache service, cache invalidation, stampede or cache
outage behavior is part of the task.

## Do not use when

No performance or availability need justifies a cache. Do not assume a cache is the
source of truth or that a cache outage should block all backing-store access.

## Required context

Read source-of-truth ownership, data freshness requirements, current cache/runtime
implementation, memory limits, eviction semantics, workload and tests. Use the
runtime's version-specific documentation.

## Inputs

Candidate data, access frequency and cost, acceptable staleness, key identity/tenant
scope, memory budget, invalidation events and cache-down requirements.

## Process

1. Measure or establish the read/write cost and explain why caching is needed. Identify
   authoritative data and whether the cache is local to one process or shared.
2. Define key construction, tenant/authorization scope, value schema, freshness bound,
   invalidation/update path, negative-cache behavior and eviction/memory limit.
3. Choose cache-aside, write-through or another consistency model based on the
   operation. State what happens when an update races with a read or cache fill.
4. Bound stampede and load: use single-flight/request coalescing, TTL jitter, bounded
   stale serving or rate limits only when compatible with the freshness contract.
5. Specify cold start, cache miss, eviction, stale entry and cache-service failure.
   Keep fallback load bounded; do not turn a cache outage into unbounded database load.
6. For process-local caches, test lifecycle, concurrency, memory bounds and behavior
   across multiple instances only if the product actually has them. For shared caches,
   inspect network timeouts, partition/failure and service-specific guarantees.
7. Test stale invalidation, concurrent fill/update, eviction, restart and outage using
   deterministic fixtures. Measure hit/miss, age, evictions, errors and end-to-end
   latency with bounded-cardinality telemetry.

## Decision points

Prefer no cache until measurement establishes a useful target. TTL is a freshness and
resource decision, not a universal rule. A local cache is process-scoped and does not
require distributed-systems architecture; load `distributed-systems` only for shared
remote-cache delivery or multi-instance consistency. Do not use a generic “hot key”
percentage or blanket rule that hot entries must never expire; measure the workload
and choose freshness, jitter and fallback from the actual source-of-truth contract.

## Approval boundaries

Apply the [shared contract](../README.md#shared-contract), [authority](../../PROJECT_BOOTSTRAP.md#1-authority-and-evidence)
and [approval boundaries](../../PROJECT_BOOTSTRAP.md#4-autonomy-and-approval-boundaries).
Persistent schema, sensitive-data retention, external dependencies and production
configuration remain subject to existing approvals.

## Outputs

Cache decision, key/freshness/invalidation contract, memory/load/failure limits,
focused tests and before/after measurement where performance is the goal.

## Completion criteria

Source-of-truth behavior is preserved, stale/failure paths are bounded and the cache
has an observable purpose and removal/recovery strategy.

## Evidence

Record cache scope, workload and environment, freshness bound, hit/miss/latency,
race/outage test results and production behavior not tested. Redis latency is not
equivalent to memory access latency.

## Handoff

Use `concurrency` for local shared-state races, `database-engineering` for source
transactions, or `distributed-systems` for remote cache boundaries.

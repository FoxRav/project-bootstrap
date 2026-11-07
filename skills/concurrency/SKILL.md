---
name: concurrency
description: "Implement or diagnose in-process threads, async tasks, shared mutable state, locks, races, deadlocks, cancellation or bounded worker pools."
---

# concurrency

## Purpose

Make in-process concurrent behavior safe, bounded and testable without assuming
multiple services or machines.

## Use when

A race, deadlock, asynchronous workflow, thread pool, shared cache/state, cancellation,
shutdown or throughput limit occurs within one process.

## Do not use when

The issue is exclusively a database isolation problem or cross-process/network
coordination; use `database-engineering` or `distributed-systems` respectively.

## Required context

Read the selected language/runtime's memory and concurrency documentation, lifecycle,
shared state, existing synchronization, failure path and tests. Identify whether the
runtime has a GIL/event loop or other execution constraints rather than assuming.

## Inputs

Concurrent actors, shared data/invariants, work arrival rate, bounded resources,
ordering requirements, cancellation semantics and shutdown behavior.

## Process

1. Reproduce or trace the race with a concrete interleaving. State the invariant and
   ownership of each mutable object.
2. Prefer single-owner/message passing or immutable snapshots when they simplify the
   invariant. Otherwise define a minimal lock/atomic boundary and all protected state.
3. For multiple locks, document a consistent acquisition order. Keep critical sections
   short; do not call unknown blocking work while holding a lock.
4. Bound worker count, queue capacity, retries and memory. Define backpressure,
   rejection or caller-visible overload behavior.
5. Define task cancellation, exception propagation, cleanup, timeout and process
   shutdown. Ensure background work cannot silently outlive its owner.
6. Test the invariant with deterministic barriers/schedulers where possible, plus
   stress/repetition when useful. Test cancellation, exception, queue saturation and
   shutdown; avoid tests that rely only on arbitrary sleep.
7. Profile contention and throughput before replacing a simple lock with lock-free
   code. Recheck correctness and resource behavior after optimization.

## Decision points

Choose synchronization from the language/runtime contract. A database transaction
does not protect arbitrary in-memory state, and an in-process lock does not coordinate
separate processes. Do not add a distributed lock for a local race.

## Approval boundaries

Apply the [shared contract](../README.md#shared-contract), [authority](../../PROJECT_BOOTSTRAP.md#1-authority-and-evidence)
and [approval boundaries](../../PROJECT_BOOTSTRAP.md#4-autonomy-and-approval-boundaries).
Changes to public cancellation/order behavior, new dependencies and production
resource limits follow existing approval rules.

## Outputs

Concurrency invariant and ownership model, synchronization/backpressure decision,
lifecycle semantics, deterministic regression test and relevant measurement.

## Completion criteria

The race/failure case is reproduced or bounded, invariants hold under the selected
interleavings, resource limits are explicit and shutdown is safe.

## Evidence

Record runtime version, interleaving/test method, repetitions, stress conditions,
resource bounds, failure outcome and known nondeterminism. A passing stress test is
not proof that all interleavings are safe.

## Handoff

Use `caching` for cache lifecycle, `database-engineering` for transaction/lock
semantics, or `performance-observability` to diagnose measured contention.

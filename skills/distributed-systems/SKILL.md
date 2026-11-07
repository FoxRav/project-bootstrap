---
name: distributed-systems
description: "Design or troubleshoot process and network boundaries, queues, remote dependencies, partial failures, retries or multi-instance coordination."
---

# distributed-systems

## Purpose

Specify behavior where a request crosses an unreliable process/network boundary,
without promising exactly-once effects or imposing distributed architecture on local work.

## Use when

The task involves a remote dependency, queue, replicated state, multiple workers or
instances, message delivery, partial failure, or recovery across a process boundary.

## Do not use when

The work is limited to one process's cache or threads/async tasks; use `caching` or
`concurrency`. A single service still qualifies when it crosses a remote boundary.

## Required context

Read the relevant architecture, event/API contracts, state owner, retry and timeout
configuration, runtime limits, accepted ADRs and tests. Consult the current version
of the selected client/broker documentation. For payment or notification flows, load
the [payments](../references/payments.md) or
[notifications](../references/notifications.md) reference for domain-specific state,
consent and reconciliation rules.

## Inputs

Operation identity, boundary, state ownership, success condition, deadline, retry
budget, ordering needs, duplicate tolerance, persistence and recovery expectations.
Separate broker/client guarantees from application side effects.

## Process

1. Map request, acknowledgement, durable state and downstream effect. For each boundary,
   identify what can succeed while the caller observes a timeout or crash.
2. Define end-to-end deadline and per-attempt timeout. Ensure retries fit the caller's
   remaining budget; classify retryable failures and cap attempts/rate.
3. Decide whether the operation is safe to retry. Use a stable operation identity and
   dedupe/conditional-write boundary for the same logical operation; distinct operations
   must remain distinct.
4. Choose backoff with jitter and bounded concurrency. Prevent retry amplification,
   queue growth and synchronized recovery. Respect protocol/provider retry hints only
   within the operation's limits.
5. For consumers, define acknowledgement/offset progress after successful processing,
   partition/order behavior, poison-message handling and durable retry/DLQ semantics
   from the chosen client version. Commit the position that the client documents as
   the next record to consume, or the next consumption position after a fully processed
   batch. Do not treat `lastOffset + 1` as a generic next-record identifier: offsets
   may have gaps. With parallel processing, track completion per partition and advance
   only through the completed ordered prefix; a later record finishing first must not
   move the committed position past an earlier unfinished record. For Kafka, verify
   the selected client's `KafkaConsumer` commit/position contract for its exact version
   (for example, Kafka 4.2 Javadoc sections on manual offset control and multi-threaded
   processing). If processing fails, leave the commit behind the failed record unless
   the record has first been durably accepted by the explicitly selected retry/DLQ
   path; do not commit past unfinished work as exception cleanup.
6. Decide how state converges after interruption: idempotent replay, reconciliation,
   outbox/inbox, compensating operation or explicit manual recovery. Describe the
   consistency boundary rather than promising global atomicity.
7. Add controlled tests for timeout-after-success, duplicate, reorder, partial failure,
   retry exhaustion, worker restart and checkpoint recovery. Measure queue age and
   retry volume where operationally relevant.

## Decision points

At-least-once delivery is not exactly-once business effect. Idempotent producer
semantics do not include unrelated databases, payment providers or HTTP calls. Use
distributed coordination only when local ownership and database transactions cannot
meet the explicit requirement.

## Approval boundaries

Apply the [shared contract](../README.md#shared-contract), [authority](../../PROJECT_BOOTSTRAP.md#1-authority-and-evidence)
and [approval boundaries](../../PROJECT_BOOTSTRAP.md#4-autonomy-and-approval-boundaries).
Persistent schemas, public delivery contracts, new dependencies and major architecture
choices use existing approval routes.

## Outputs

Boundary diagram/prose, timeout and retry table, operation/dedupe semantics,
checkpoint/recovery decisions, tests and observable operational signals.

## Completion criteria

Success, ambiguous timeout, duplicate, failure and recovery paths are specified at
each boundary. No checkpoint skips unfinished work and no guarantee exceeds the
selected implementation's documented scope.

## Evidence

Record client/broker version and exact documentation, tested fault scenarios, committed
position/processing invariant, retry bounds, measured outcomes and untested failure
conditions.

## Handoff

Use `webhooks` for webhook-specific HTTP controls, `database-engineering` for database
transaction semantics, `data-engineering` for data pipelines, or `testing-strategy`
when a broader validation portfolio is needed.

---
name: performance-observability
description: "Investigate or design measurable performance, capacity, reliability or telemetry behavior using the application's actual workload and runtime."
---

# performance-observability

## Purpose

Make performance and operational behavior measurable, diagnose a real bottleneck and
verify that a bounded change improves the relevant user or service outcome.

## Use when

There is a reported latency/resource/reliability issue, a capacity objective, or a
change to production telemetry, SLI/SLO or alerting.

## Do not use when

No measurable performance or operational question exists. Do not add a monitoring
stack or optimize from a generic benchmark alone.

## Required context

Read user-visible requirements, runtime/deployment, current dashboards/logging,
load shape, privacy/retention rules, accepted SLOs and actual test tools. For media
workloads, use the [real-time media reference](../references/realtime-media.md).

## Inputs

Affected journey, baseline and environment, load/concurrency, percentile and error
measures, resource budgets, telemetry constraints and target outcome. Mark missing
baselines instead of fabricating them.

## Process

1. Define the user/service symptom and a metric that represents it (for example
   end-to-end latency percentile, error rate, queue age or resource saturation).
2. Capture a reproducible baseline in a representative safe environment. Record
   runtime, hardware/container limits, dataset, concurrency and warm/cold state.
3. Trace the critical path and correlate request/log/metric/trace identifiers without
   logging secrets or unnecessary personal data. Separate application, network,
   storage and scheduler delays.
4. Use profiling or controlled load to find the dominant measured cost. Form one
   bounded hypothesis; do not optimize a component based on theoretical hardware speed.
5. Make the smallest change and rerun the same measurement. Compare distributions and
   error/resource costs, not just averages; verify correctness and regression behavior.
6. For telemetry changes, specify signal meaning, cardinality, sampling, retention,
   access, alert threshold and response owner. Avoid high-cardinality or sensitive labels.
7. Update dashboards/runbooks or SLI definitions only in the canonical project location.
   Record environmental limits and whether production behavior remains unverified.

## Decision points

A benchmark must represent the workload and include end-to-end costs. Do not infer
Redis/network latency from RAM latency or use stale company-specific ROI figures.
Use a service objective only when its owner and measurement window are clear.

## Approval boundaries

Apply the [shared contract](../README.md#shared-contract), [authority](../../PROJECT_BOOTSTRAP.md#1-authority-and-evidence)
and [approval boundaries](../../PROJECT_BOOTSTRAP.md#4-autonomy-and-approval-boundaries).
Telemetry that changes data collection, retention or production cost follows existing
privacy, security and production approval boundaries.

## Outputs

Metric definition, baseline, trace/profile finding, bounded change, before/after
measurement, privacy-safe telemetry or operational update.

## Completion criteria

The result answers the original measured question, preserves correctness and states
the limits of the benchmark and its transfer to production.

## Evidence

Record commands/tool versions, environment, load, dataset, distributions, errors and
resource use. Separate observed results from estimates; omit sensitive payloads.

## Handoff

Use `system-design` for capacity/boundary decisions and `testing-strategy` for load
test design. Use `release-readiness` only for an identified release candidate.

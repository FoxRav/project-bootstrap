---
name: delivery-engineering
description: "Change build, configuration, infrastructure-as-code, deployment, rollback, backup or disaster-recovery behavior for a project."
---

# delivery-engineering

## Purpose

Make delivery and recovery repeatable and bounded while respecting the selected
platform's security, availability and human approval requirements.

## Use when

Build/release pipelines, runtime configuration, containers, infrastructure-as-code,
deployment, rollback, backup or disaster recovery change.

## Do not use when

The task changes application logic only and the delivery path remains untouched.
Do not select a cloud or CI vendor without a project need.

## Required context

Read current deployment topology, environments, configuration/secret handling,
release policy, restore procedures, relevant IaC and validation commands.
Consult the current platform documentation for version-sensitive behavior.

## Inputs

Artifact provenance, target environment, deployment owner, change risk, dependencies,
secret/data boundaries, rollback limits, RTO/RPO if approved and available.

## Process

1. Trace source-to-artifact-to-environment and identify which configuration differs
   by environment. Keep secrets out of source, logs and build artifacts.
2. Make builds reproducible where feasible; pin or verify inputs according to project
   policy. Check permissions, artifact integrity and environment separation.
   Consider the [NIST SSDF](https://csrc.nist.gov/pubs/sp/800/218/final) and
   [SLSA](https://slsa.dev/spec/v1.1/) as risk-tailored supply-chain references; do not
   claim conformance from one pipeline control.
3. Define rollout order, health/acceptance signal, failure threshold, rollback or
   forward-fix path, and who can execute each production action.
4. For IaC, inspect plan/diff and state effects before application. Separate safe
   preview from shared or destructive execution; never infer approval from a green plan.
5. For backup/DR, identify protected state, backup frequency/retention, dependencies,
   access, restore sequence and evidence. Treat RTO/RPO as owner-approved targets, not
   copied defaults.
6. Validate pipeline/config syntax and behavior with local or isolated fixtures.
   Exercise rollback/restore in a safe environment when supported; do not perform a
   production operation as a test.
7. Update operational documentation with exact commands, prerequisites, owner and
   recovery evidence; record untested production conditions.

## Decision points

Prefer a reversible, observable rollout. Distinguish artifact build, deploy approval
and actual release. A backup is not proven until restore evidence exists; a rollback
may not reverse data/schema changes.

## Approval boundaries

Apply the [shared contract](../README.md#shared-contract), [authority](../../PROJECT_BOOTSTRAP.md#1-authority-and-evidence)
and [approval boundaries](../../PROJECT_BOOTSTRAP.md#4-autonomy-and-approval-boundaries).
Production deployment, destructive infrastructure/data actions and release operations
require explicit approval tied to the target, revision and recovery limits.

## Outputs

Artifact/configuration change, deployment and rollback plan, safe validation results,
restore evidence or explicit test gap, updated runbook and approval record.

## Completion criteria

The change is reproducible and reviewable; secrets and environment boundaries are
preserved; failure and recovery behavior are explicit; no unapproved production
operation occurred.

## Evidence

Record tool/provider versions, plan/build output, artifact identity, test environment,
rollback/restore results, warnings and production actions not performed.

## Handoff

Use `security-review` for trust boundary changes and `release-readiness` only when
assessing a named candidate for release.

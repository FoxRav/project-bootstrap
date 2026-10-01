---
name: security-review
description: "Assess realistic threats and attack paths for changes involving sensitive data, trust boundaries or powerful capabilities."
---

# security-review

## Purpose

Find actionable security defects in the capabilities and data flows actually affected.

## Use when

A change affects auth, secrets/private data, untrusted inputs, AI instruction boundaries, dependencies, execution or filesystem/network/destructive access.

## Do not use when

No plausible security boundary is affected. Do not attach a generic checklist to unrelated changes or claim a compliance certification.

## Required context

Read scoped requirements, [project context and hazards](../../docs/PROJECT.md), relevant architecture/auth decisions, affected code/configuration/dependencies and tests/evidence.

## Inputs

Target identity, protected assets, actors, trust boundaries, permitted environment and review scope.

## Process

1. Identify assets, entry points, actors and capabilities. Trace data and privilege across the changed boundary.
2. Select plausible threats: authentication versus authorization, secret/private-data exposure, input/injection attacks, prompt injection when AI consumes untrusted content, outbound disclosure, filesystem traversal, network abuse, dependencies, unsafe execution or destructive operations as relevant.
3. Trace each credible attack path through actual validation, enforcement and failure behavior. Check denied cases and whether controls are real runtime restrictions rather than prose promises.
4. Use safe synthetic tests or code evidence within the permitted environment. Do not exploit live targets or expose private data merely to demonstrate a concern.
5. Record entry/preconditions, path, impact, evidence, severity and a specific mitigation. Distinguish demonstrated vulnerabilities from unresolved threats and accepted residual risk.
6. Return read-only findings, missing evidence and recheck criteria; avoid unsupported claims of security.

## Decision points

Prioritize reachable paths and asset impact. Broaden scope only where a demonstrated dependency requires it; identify missing access or evidence instead of assuming a control works.

## Approval boundaries

Read and apply the [shared contract](../README.md#shared-contract). Security-policy changes, live testing and external disclosure require their applicable authorization. A reviewer cannot accept residual risk on the Product Owner's behalf.

## Outputs

Threat-driven findings with attack path, impact and mitigation, using BLOCKER/MAJOR/MINOR/NOTE impact levels consistent with code-review.

## Completion criteria

Relevant paths are assessed and uncertainties are explicit; material findings require resolution/recheck or authorized risk disposition before completion.

## Evidence

Record reviewed state, boundaries and paths, safe test results, exclusions and mitigation verification. Redact secrets and private payloads.

## Handoff

Provide implement the authorized mitigations and tests, and the decision owner any policy/risk acceptance questions. Pass final security evidence to release-readiness when needed.

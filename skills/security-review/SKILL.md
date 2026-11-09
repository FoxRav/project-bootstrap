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

Read scoped requirements, [project context and hazards](../../docs/PROJECT.md), relevant architecture/auth decisions, affected code/configuration/dependencies and tests/evidence. For a security-control design or implementation task, route to [application-security](../application-security/SKILL.md); this skill remains the independent threat review, not the implementation procedure.

## Inputs

Target identity, protected assets, actors, trust boundaries, permitted environment and review scope.

## Process

1. Identify assets, entry points, actors and capabilities. Trace data and privilege across the changed boundary.
2. Select plausible threats: authentication versus authorization, secret/private-data exposure, input/injection attacks, prompt injection when AI consumes untrusted content, outbound disclosure, filesystem traversal, network abuse, dependencies, unsafe execution or destructive operations as relevant.
3. Treat each suspected issue as a candidate, not a finding. Re-read the current source
   and trace a lower-trust entry or action to an affected principal/resource and
   concrete security effect. Verify the strongest relevant validation, authorization,
   containment and failure controls; a missing defense-in-depth layer is not a
   vulnerability when an effective control prevents the claimed path.
4. Independently validate each material candidate: a reviewer who did not discover it
   re-reads the cited source and checks its preconditions, controls and claimed effect.
   Reproduce only the minimum decisive behavior with safe synthetic evidence where
   permitted. If an independent verifier or safe reproduction is unavailable, state
   the exact gap and keep the candidate unconfirmed; never invent agent orchestration
   or run target-controlled code without the required sandbox.
5. Disposition every candidate as **confirmed**, **needs validation** with the exact
   decisive missing fact and a bounded safe next check, or **rejected** with the
   evidence that disproves it. Keep optional hardening separate from confirmed
   vulnerabilities. Do not assign severity to unresolved or rejected candidates.
6. For each confirmed finding, record a stable identifier, reviewed revision,
   source location, attacker/preconditions, entry-to-effect path, observed evidence,
   existing controls, impact and likelihood rationale, confidence, severity, smallest
   effective mitigation and a regression/recheck criterion. Use the existing work or
   review record; do not require a new report schema.
7. Use safe synthetic tests or code evidence within the permitted environment. Do not
   exploit live targets or expose private data merely to demonstrate a concern.
8. Return read-only findings, coverage and evidence limits. Separate demonstrated
   defects from unresolved threats, accepted residual risk and style/hardening advice;
   do not make unsupported claims of security.

## Decision points

Prioritize reachable paths and asset impact. Use the project's severity vocabulary
(BLOCKER/MAJOR/MINOR/NOTE here) and justify priority from demonstrated likelihood and
impact; keep confidence distinct from severity. A confirmed guard that blocks the
candidate may refute the vulnerability while still leaving a separately labeled,
optional hardening opportunity. Broaden scope only where a demonstrated dependency
requires it; identify missing access or evidence instead of assuming a control works.

## Approval boundaries

Read and apply the [shared contract](../README.md#shared-contract). Security-policy changes, live testing and external disclosure require their applicable authorization. A reviewer cannot accept residual risk on the Product Owner's behalf.

## Outputs

Confirmed findings, exact needs-validation candidates and rejected false positives,
with attack-path evidence, impact rationale, mitigation and coverage limits. Confirmed
finding severity uses BLOCKER/MAJOR/MINOR/NOTE consistently with code-review; a
needs-validation candidate has no severity.

## Completion criteria

Relevant paths are assessed and uncertainties are explicit; material findings require resolution/recheck or authorized risk disposition before completion.

## Evidence

Record reviewed state, boundaries and paths, candidate dispositions, independent
validation context, safe test results, exclusions, risk rationale and mitigation
verification. Redact secrets and private payloads.

## Handoff

Provide implement the authorized mitigations and tests, and the decision owner any policy/risk acceptance questions. Pass final security evidence to release-readiness when needed.

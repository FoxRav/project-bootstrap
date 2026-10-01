---
name: prototype
description: "Run a bounded experiment when empirical evidence is needed for technical, API, UX or performance feasibility."
---

# prototype

## Purpose

Answer one consequential uncertainty with a controlled experiment.

## Use when

Reasoning or documentation cannot establish viability, interaction quality or performance feasibility.

## Do not use when

The behavior and implementation path are already settled. A prototype is not a shortcut around production review or approvals.

## Required context

Read [project context](../../docs/PROJECT.md), the uncertainty, relevant research, existing implementation and environment/data restrictions.

## Inputs

Hypothesis, experiment scope, success/failure criteria, time/complexity bound and a disposable or potentially promotable designation. Propose missing bounds before dependent risky work.

## Process

1. State the hypothesis and measurable success/failure criteria. Identify confounders and the smallest representative scenario.
2. Choose a contained workspace and permitted dependencies/data. Record the stopping bound and whether output is disposable or a candidate for later promotion.
3. Build only what tests the hypothesis; reuse existing tooling. Keep experiment code separated from production paths.
4. Run the experiment and capture environment, inputs, outputs, measurements and failures. Compare against the stated criteria.
5. Stop at the bound, including when the result is inconclusive. Explain limitations and what a production implementation would additionally require.
6. Recommend discard, another bounded experiment or a separately scoped implementation. Remove only verified disposable outputs when authorized or clearly routine.

## Decision points

An inconclusive experiment is a valid result. Promotion requires a deliberate work item, production checks and any policy approvals; success alone is insufficient.

## Approval boundaries

Read and apply the [shared contract](../README.md#shared-contract). Dependency adoption, sensitive/shared data, external effects and production access retain their normal boundaries even in experiments.

## Outputs

A bounded experimental artifact and result, including designation, limits and promotion/disposal recommendation.

## Completion criteria

The hypothesis is answered or bounded uncertainty is reported; experimental code has not silently become production architecture.

## Evidence

Record reproducible commands, input identity, environment, measurements, observed failures and criterion outcomes.

## Handoff

Send findings and limitations to research/to-spec; give implement an approved production scope only after the promotion decision.

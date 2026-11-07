---
name: ai-systems
description: "Design or change a product capability that relies on generative or other model-based AI for user-facing or automated decisions."
---

# ai-systems

## Purpose

Define the model-dependent behavior, safety controls and evaluation evidence for a
specific product use case without assuming an AI provider or requiring AI adoption.

## Use when

A feature sends user or business data to a model, generates content, ranks/classifies
information, or lets model output influence a tool or consequential workflow.

## Do not use when

The task does not use model-based behavior. Do not add a model, external service,
training data or AI infrastructure merely because this recipe exists.

## Required context

Read product purpose, user groups, data classification, existing AI policy, model/tool
boundary, runtime constraints and user-visible fallback requirements. Consult the
current provider/model documentation and relevant risk guidance.

## Inputs

Task success definition, inputs/outputs, human oversight, error tolerance, privacy,
latency/cost limits, action authority, known failure/abuse scenarios and evaluation data.

## Process

1. State why a model is needed and compare a deterministic/non-AI alternative where
   relevant. Define task-level success and prohibited outcomes.
2. Map data origin, consent/rights, sensitive fields, retention and provider boundary.
   Minimize sent data and record whether data leaves the project environment.
3. Define model output schema and validation, uncertainty handling, refusal/fallback,
   human review and user disclosure appropriate to the use case.
4. For tools/actions, scope permissions to the minimum task, validate arguments and
   bind authorization to the user/system rather than model prose. Treat retrieved
   content and model output as untrusted data.
5. Build a representative, rights-cleared evaluation set with expected outcomes and
   edge/abuse cases. Establish a baseline, failure categories and release threshold
   before tuning; separate deterministic safety assertions from subjective quality.
6. Test prompt injection, data exposure, malformed output, unavailable model, timeout,
   rate limits, cost/latency spikes and unsafe tool requests. Use synthetic fixtures
   and controlled endpoints.
7. Define monitoring for quality, refusal, error, latency, cost and safety incidents
   without logging secrets or unnecessary raw user content. Provide rollback/disable
   behavior and an accountable owner.

## Decision points

A model score is not a guarantee of behavior. A benchmark is only evidence for its
population and task. High-impact decisions need an explicit owner and human oversight
appropriate to risk. Review the [NIST AI Risk Management Framework 1.0](https://www.nist.gov/itl/ai-risk-management-framework),
[NIST AI 600-1](https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.600-1.pdf) and current
[OWASP LLM application risks](https://genai.owasp.org/llm-top-10/), but do not treat a
checklist as product approval.

## Approval boundaries

Apply the [shared contract](../README.md#shared-contract), [authority](../../PROJECT_BOOTSTRAP.md#1-authority-and-evidence)
and [approval boundaries](../../PROJECT_BOOTSTRAP.md#4-autonomy-and-approval-boundaries).
New external services, sensitive data use, autonomous actions and release changes
follow existing dependency, privacy, security and production approvals.

## Outputs

Use-case specification, data/model boundary, validated output/action contract,
evaluation protocol/results, fallback/monitoring plan and remaining risks.

## Completion criteria

Success and prohibited outcomes are testable, permissions/data are bounded, evaluation
is representative enough for the stated claim and limitations are explicit.

## Evidence

Record model/provider/version, prompt/config identity, dataset provenance, evaluation
results, test environment, known distribution gaps and review/approval status. Do not
include secrets or sensitive prompts/payloads.

## Handoff

Use `application-security` for trust/data controls, `testing-strategy` for validation
portfolio and `performance-observability` for production measurements.

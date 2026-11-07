---
name: api-design
description: "Design or change a software API, protocol boundary or event contract when compatibility, clients, errors or machine-readable documentation matter."
---

# api-design

## Purpose

Make an API predictable for its actual consumers, safely evolvable and testable without
prescribing REST, GraphQL, gRPC or a message broker in every project.

## Use when

An API or event contract is new, changes observable behavior, adds clients, or needs a
compatibility, versioning or documentation decision.

## Do not use when

An internal implementation change preserves the existing contract and needs no API
decision. Do not introduce an API-description format merely to satisfy this recipe.

## Required context

Read [project context](../../docs/PROJECT.md), existing routes/schemas/client use,
accepted contract decisions, auth boundaries and [testing commands](../../docs/TESTING.md).
Use [application-security](../application-security/SKILL.md) for security design;
load [webhooks](../webhooks/SKILL.md) only for webhook behavior. Load
[payments](../references/payments.md) or
[notifications](../references/notifications.md) when those domain flows are in scope.

## Inputs

Consumers, use cases, trust boundaries, transport constraints, current contract,
compatibility expectations, data sensitivity, error and pagination requirements.
Unknown client behavior stays an explicit question.

## Process

1. List consumers and operations/events from concrete use cases. Identify the owner of
   each contract and the compatibility promise already made.
2. Select a protocol based on client capabilities, interaction shape, streaming needs,
   operational support and versioning cost. Compare alternatives only when selection
   is consequential; no protocol is inherently fastest or most reliable.
3. Define request/event and response shapes, identifiers, null/optional semantics,
   validation, authorization, error categories, pagination and time limits. Specify
   behavior for unknown fields and version evolution.
4. Define observable semantics: side effects, idempotency for intended retries,
   duplicate/order handling, status codes or acknowledgements, retryable failures and
   reconciliation. Do not require unrelated POST requests to deduplicate.
5. Update the project's existing machine-readable contract if one is maintained:
   OpenAPI for HTTP interfaces, AsyncAPI for message-driven contracts, or the chosen
   protocol's native schema. For GraphQL, Section 6.2.3 of the October 2021
   specification defines subscriptions as application event streams, not a
   schema-change notification mechanism; document schema evolution separately.
6. Compare the contract to implementation and representative consumers. Add schema,
   compatibility and behavior tests that fail on a concrete breaking change.
7. Document examples, auth assumptions, deprecation/version policy and known limits in
   the canonical project location; do not create a duplicate specification.

## Decision points

Use the least surprising protocol and evolve in place when compatibility allows.
Machine-readable descriptions define shape, not delivery, authentication or runtime
guarantees. Ask the owner before changing a public promise or persisting a new shared
contract.

## Approval boundaries

Apply the [shared contract](../README.md#shared-contract), [authority](../../PROJECT_BOOTSTRAP.md#1-authority-and-evidence)
and [approval boundaries](../../PROJECT_BOOTSTRAP.md#4-autonomy-and-approval-boundaries).
Public API, event contract, auth and schema changes require the applicable existing
approval; this skill grants none.

## Outputs

Operation/event contract, compatibility decision, error and retry semantics, updated
canonical schema/docs and focused contract or behavior evidence.

## Completion criteria

The consumer-visible contract agrees with implementation and documentation; changed
behavior, compatibility, security assumptions and unverified guarantees are explicit.

## Evidence

Record before/after contract, affected consumers, schema diff, compatibility test
results and what was not exercised. A schema-valid example alone does not prove
delivery or security.

## Handoff

Use `webhooks` for webhook-specific signing and delivery controls, `testing-strategy`
for a larger test portfolio, or `code-review` for an independent implementation review.

# Payment flows

## Purpose

Give payment-related work a risk-focused flow for authorization, duplicate requests,
provider ambiguity, reconciliation and sensitive-data boundaries. This is engineering
guidance, not legal, accounting or PCI compliance advice.

## Use when

A feature initiates, captures, refunds, voids, reconciles or reports payments, or
handles payment-provider callbacks or payment-related identifiers.

## Procedure

1. Map customer intent to a business operation and provider operation. Define the
   authoritative transaction state, actor, currency/amount precision, lifecycle and
   allowed transitions before coding.
2. Keep cardholder data out of application storage and logs where the provider's
   hosted/tokenized flow can be used. Classify data and confirm the actual PCI scope
   with the responsible compliance owner; a token or provider does not itself prove
   scope reduction.
3. Create a stable idempotency identity for the same intended payment operation.
   Persist its key and outcome atomically with the local operation where possible.
   Reuse that key only for retrying the same operation; distinct purchases must not
   collide or be silently deduplicated.
4. Define provider timeout ambiguity: a timeout may occur after the provider acted.
   Query/reconcile by provider operation identity before initiating a new charge.
   Do not infer failure solely from a missing response.
5. Model authorization, capture, void, refund, partial refund and dispute as explicit
   state transitions with amount/currency bounds and audit actor. Prevent invalid or
   repeated transitions with transactional conditions.
6. Verify provider webhooks using the provider's current signature procedure; preserve
   `webhooks` controls for timestamp/replay, raw request bytes, secret rotation and
   asynchronous acknowledgement. Treat callback order and duplicates as normal cases.
7. Run reconciliation against provider reports or API state using a bounded, repeatable
   process. Report unmatched, delayed and conflicting records to an accountable owner;
   never silently rewrite an audited transaction.
8. Test same-operation retry with the same idempotency key, distinct operations,
   timeout-after-provider-success, duplicate/out-of-order callbacks, partial refund,
   reconciliation mismatch and secret/key failure using a sandbox or synthetic fixture.

## Decision points

HTTP method semantics alone do not provide payment deduplication. Use the provider's
documented idempotency scope and retention. Exactly-once payment effect is not implied
by a successful HTTP response or queue setting. Reconciliation and accounting rules
belong to the product/finance owner.

## Approval boundaries

Follow the [shared contract](../README.md#shared-contract), [authority](../../PROJECT_BOOTSTRAP.md#1-authority-and-evidence),
[approval boundaries](../../PROJECT_BOOTSTRAP.md#4-autonomy-and-approval-boundaries),
[quality model](../../PROJECT_BOOTSTRAP.md#5-one-quality-and-completion-model),
[Git authority](../../PROJECT_BOOTSTRAP.md#git-authority) and
[optional review packaging](../../PROJECT_BOOTSTRAP.md#optional-review-packaging).
Payment provider, public payment contract, sensitive-data retention, production
charges/refunds and compliance claims require the applicable explicit approval.

## Outputs and evidence

Document state transitions, operation identity, provider/version, amount/currency
invariants, callback/reconciliation paths, tests and unresolved compliance/accounting
questions. Use synthetic references; redact tokens and customer/payment data.

## Sources

- [PCI Security Standards Council, PCI DSS v4.0.1](https://www.pcisecuritystandards.org/document_library/), published June 2024; accessed 2026-11-08. Confirm the applicable requirements and scope with the responsible assessor.
- [RFC 9110, Section 9.2.2: Idempotent Methods](https://www.rfc-editor.org/rfc/rfc9110.html#section-9.2.2), accessed 2026-11-08. HTTP method semantics do not define a provider's idempotency-key contract.
- [Standard Webhooks specification](https://github.com/standard-webhooks/standard-webhooks/blob/main/spec/standard-webhooks.md), accessed 2026-11-08; provider-specific signing contracts take precedence.

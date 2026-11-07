# Notifications

## Purpose

Design user notifications as bounded, consent-aware delivery attempts with explicit
preference, retry, duplicate and observability behavior.

## Use when

A system sends email, SMS, push or in-product notifications, adds a provider, changes
notification preferences or handles delivery receipts and bounces.

## Procedure

1. Define the event that warrants a notification, intended recipient, urgency, channel,
   allowed content and whether it is transactional or promotional. Do not notify on
   every internal state change by default.
2. Resolve preferences, consent, suppression and legal/product rules at send time.
   Define precedence for user opt-out, organization policy and mandatory security
   notices with the appropriate owner; do not invent legal exceptions.
3. Minimize payload and metadata. Use secure short-lived links for sensitive actions;
   do not include credentials, full payment details or unnecessary sensitive content.
4. Identify a notification operation from the business event and intended recipient/
   channel. Deduplicate that same operation where delivery can be retried, while
   allowing a genuinely new event to notify again.
5. Persist a delivery attempt/outbox record before asynchronous dispatch where needed.
   Define provider acceptance versus final delivery, retryable failures, bounded
   exponential backoff with jitter, maximum age/attempts and terminal suppression.
6. Process provider callbacks as untrusted, duplicate and potentially out-of-order
   events. Verify their signature, correlate a stable message identifier, and update
   state without regressing a later terminal status.
7. Track queued/sent/accepted/delivered/bounced/failed/suppressed states according to
   provider capabilities. Provide opt-out and bounce handling; protect recipient and
   message contents in logs and telemetry.
8. Test preference changes, opt-out, duplicate event, provider timeout-after-accept,
   retry exhaustion, bounce, malformed callback and link expiry with fake providers.

## Decision points

Provider acceptance is not proof of inbox delivery or user receipt. Email/SMS/push
channels have different provider and regulatory semantics; use current provider and
jurisdiction guidance. Do not promise exactly-once delivery.

## Approval boundaries

Follow the [shared contract](../README.md#shared-contract), [authority](../../PROJECT_BOOTSTRAP.md#1-authority-and-evidence),
[approval boundaries](../../PROJECT_BOOTSTRAP.md#4-autonomy-and-approval-boundaries),
[quality model](../../PROJECT_BOOTSTRAP.md#5-one-quality-and-completion-model),
[Git authority](../../PROJECT_BOOTSTRAP.md#git-authority) and
[optional review packaging](../../PROJECT_BOOTSTRAP.md#optional-review-packaging).
New external providers, personal-data processing, consent semantics, costs and
production sends require applicable approval.

## Outputs and evidence

Record event/recipient/channel identity, preference decision, state model, retry
limits, provider callback controls, suppression behavior, tests and privacy review.
Use fake recipients and redact message content.

## Sources

- [RFC 9110, Section 9.2.2: Idempotent Methods](https://www.rfc-editor.org/rfc/rfc9110.html#section-9.2.2), accessed 2026-11-08.
- [Standard Webhooks specification](https://github.com/standard-webhooks/standard-webhooks/blob/main/spec/standard-webhooks.md), accessed 2026-11-08.
- [NIST Privacy Framework 1.0](https://www.nist.gov/privacy-framework), accessed 2026-11-08. This framework is voluntary and does not replace applicable law or organizational policy.

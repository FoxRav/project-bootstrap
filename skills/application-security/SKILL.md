---
name: application-security
description: "Design application controls for trust boundaries, identity, secrets, cryptography, sensitive data or outbound URL and network requests."
---

# application-security

## Purpose

Translate a concrete application threat into proportionate, testable controls using
maintained mechanisms and the project's approved authority.

## Use when

Authentication/authorization, tokens, sensitive data, cryptography, secret handling,
user-controlled destinations, outbound fetching or application trust boundaries change.

## Do not use when

The task only asks for an independent security assessment; use `security-review`.
Do not invent cryptographic schemes or imply this recipe is a penetration test.

## Required context

Read project security and data requirements, affected paths, identity provider/runtime,
data flows, existing controls, dependencies and applicable law/contract requirements.
Consult current standards and implementation-specific primary documentation.

## Inputs

Assets, actors, trust boundaries, entry points, attacker capabilities, data classes,
required security properties, deployment/effects and existing approved controls.
Unknown threat assumptions must be explicit.

## Process

1. Trace untrusted input to privileged action, sensitive data or outbound connection.
   Name the asset, trust boundary, abuse case and intended control.
2. Select established controls for the actual use case. Separate authentication from
   authorization. For a public browser OAuth client, use Authorization Code with PKCE;
   never place a client secret in browser code. Do not substitute Client Credentials,
   Implicit or Resource Owner Password Credentials for a user-facing browser flow.
   OAuth is authorization; use OIDC when an authentication protocol is needed.
3. If accepting JWTs, distinguish signed JWS from encrypted JWE. Pin an allowed
   algorithm in trusted configuration and validate signature, issuer, audience,
   expiration/not-before and intended token use; do not trust a token's algorithm
   header as policy. Match symmetric/asymmetric key roles to the selected protocol.
4. For passwords, use a maintained adaptive password KDF with parameters selected
   from current implementation guidance; do not use a fast general-purpose hash or
   invent a password-storage construction.
5. Classify outbound URL use before selecting SSRF controls, following the OWASP
   SSRF Prevention Cheat Sheet's Case 1/Case 2 distinction:
   - For a user-selected arbitrary external URL (Case 2), the feature may reach public
     destinations only, using an explicitly allowed scheme/port policy (HTTPS by
     default). Reject loopback, private/internal, link-local, multicast, reserved and
     cloud-metadata addresses for both IPv4 and IPv6. Do not let a user-supplied
     hostname, scheme, port, URL, redirect or other field extend this set.
   - For a known, pre-approved internal service (Case 1), allow only the configured
     service identity and its explicitly approved protocol, port and purpose. Enforce
     the same narrow destination at application and network-egress layers; do not
     permit arbitrary internal addresses or turn the rule into access to the whole
     private network. User input may provide business data or select a fixed approved
     service identifier, but cannot supply or widen the destination policy.
   For both cases, parse and normalize with the chosen client; resolve and validate all
   relevant IPv4/IPv6 results against that case's destination policy, then ensure the
   connection uses a validated address to resist DNS rebinding. Disable redirects or
   revalidate every redirect under the same policy. Recheck retries/fallbacks, restrict
   egress at the runtime/network layer, do not forward credentials to customer endpoints,
   and bound connection/read time and response size.
6. For cryptography, use maintained platform/library APIs and explicit key separation,
   nonce/IV rules, authentication-tag verification and failure handling. Define key
   generation, storage, access, rotation, revocation and recovery separately from the
   encryption mode.
7. Scope secrets and permissions to the workload/tenant. Keep credentials out of code,
   logs, URLs, test fixtures and error text. Define rotation and incident revocation.
8. Map each control to a negative test and safe telemetry. Test malformed, unauthorized,
   expired, redirected and boundary cases with controlled fixtures; avoid live targets.
9. Review changed data retention, external effects and residual risks against existing
   policy and approvals; update canonical security documentation.

## Decision points

Prefer platform-maintained mechanisms and deny-by-default boundaries. SSRF control
must match the network egress architecture as well as application validation. GCM
provides authenticated encryption; it does not store or manage keys. Key lifecycle is
separate; consult [NIST SP 800-38D](https://csrc.nist.gov/pubs/sp/800/38/d/final)
and [NIST SP 800-57 Part 1 Revision 5](https://csrc.nist.gov/pubs/sp/800/57/pt1/r5/final).
Use the OWASP SSRF Prevention Cheat Sheet's distinct
[Case 1: identified and trusted applications](https://cheatsheetseries.owasp.org/cheatsheets/Server_Side_Request_Forgery_Prevention_Cheat_Sheet.html#case-1-application-can-send-request-only-to-identified-and-trusted-applications)
and [Case 2: arbitrary external destinations](https://cheatsheetseries.owasp.org/cheatsheets/Server_Side_Request_Forgery_Prevention_Cheat_Sheet.html#case-2-application-can-send-requests-to-any-external-ip-address-or-domain-name)
controls. Do not conflate an approved internal dependency with a user-chosen URL.
Follow current primary specifications for
[OAuth security](https://www.rfc-editor.org/rfc/rfc9700.html),
[JWT best practices](https://www.rfc-editor.org/rfc/rfc8725.html) and
[password storage](https://cheatsheetseries.owasp.org/cheatsheets/Password_Storage_Cheat_Sheet.html);
do not treat a framework default as proof that the application validates the right
identity, audience or authorization. When security work surfaces a possible
vulnerability, keep it a candidate until `security-review` independently validates
the current source, controls and claimed effect. Record an exact validation gap rather
than assigning severity to an unresolved candidate; keep design concerns and optional
hardening distinct from confirmed vulnerabilities.

## Approval boundaries

Apply the [shared contract](../README.md#shared-contract), [authority](../../PROJECT_BOOTSTRAP.md#1-authority-and-evidence)
and [approval boundaries](../../PROJECT_BOOTSTRAP.md#4-autonomy-and-approval-boundaries).
Authentication/security boundary changes, reduced controls and new dependencies
require applicable approval. This recipe does not authorize live security testing.

## Outputs

Threat/control mapping, design decision, key/data lifecycle, implementation scope,
negative tests, safe logging requirements and residual-risk record. If the task also
produces vulnerability candidates, route their independent assessment through
`security-review`; do not present a design concern as a confirmed vulnerability.

## Completion criteria

Controls correspond to identified threats, failure is safe, sensitive data is
protected, test evidence is bounded and approval/review needs are visible.

## Evidence

Record threat scenarios, exact control paths, dependency/runtime versions, negative
test results, redaction checks and limits. Do not claim a scan proves security.

## Handoff

Use `security-review` for independent candidate validation and reporting,
`webhooks` for webhook verification details, and `testing-strategy` for risk-based
security-test selection.

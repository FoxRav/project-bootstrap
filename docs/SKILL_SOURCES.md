# Skill design provenance

Reference only, researched 2026-09-30 and updated for webhooks on 2026-11-07 and
technical skill expansion on 2026-11-08. These external sources are inspiration and
technical references, not runtime instructions or dependencies. The canonical recipes
are original, scoped to this bootstrap's task and authority model; no third-party skill
text is vendored. Versioned claims are tied to the named edition; unversioned living
documentation must be rechecked for the selected implementation.

| Primary source inspected | Pattern considered / deliberate adaptation |
| --- | --- |
| [OpenAI skill guide](https://learn.chatgpt.com/docs/build-skills) | Name/description metadata and progressive disclosure; portable source plus explicit runtime discovery guidance. |
| [Matt Pocock skills](https://github.com/mattpocock/skills) | Narrow recipes and task routing; retain the existing 18 general workflows without importing a broader skill suite. |
| [grilling](https://github.com/mattpocock/skills/blob/main/skills/productivity/grilling/SKILL.md), [grill-me](https://github.com/mattpocock/skills/blob/main/skills/productivity/grill-me/SKILL.md), [grill-with-docs](https://github.com/mattpocock/skills/blob/main/skills/engineering/grill-with-docs/SKILL.md) | Repository facts before product questions; use one decision cluster, bounded scope and explicit persistence instead of mandatory exhaustive questioning or delegation. |
| [domain-modeling](https://github.com/mattpocock/skills/blob/main/skills/engineering/domain-modeling/SKILL.md) | Scenario-grounded terminology; use the project's existing knowledge map and distinguish confirmed rules from proposals. |
| [to-spec](https://github.com/mattpocock/skills/blob/main/skills/engineering/to-spec/SKILL.md), [to-tickets](https://github.com/mattpocock/skills/blob/main/skills/engineering/to-tickets/SKILL.md) | Synthesis and observable slices; use existing local templates, without mandatory external publication or fixed document size. |
| [implement](https://github.com/mattpocock/skills/blob/main/skills/engineering/implement/SKILL.md) | Incremental validation and review; intentionally omit its automatic commit instruction. |
| [tdd](https://github.com/mattpocock/skills/blob/main/skills/engineering/tdd/SKILL.md) | Behavioral assertions and incremental feedback; retain red-green-refactor, without routine test-boundary approval ceremonies. |
| [diagnosing-bugs](https://github.com/mattpocock/skills/blob/main/skills/engineering/diagnosing-bugs/SKILL.md), [triage](https://github.com/mattpocock/skills/blob/main/skills/engineering/triage/SKILL.md) | Evidence-led diagnosis and classification; avoid automatic tracker transitions, arbitrary hypothesis counts and unbounded reproduction loops. |
| [architecture improvement](https://github.com/mattpocock/skills/blob/main/skills/engineering/improve-codebase-architecture/SKILL.md) | Inspect real architectural friction; assess independently without compulsory HTML reports, redesign, delegation or imposed domain terminology. |
| [Matt Pocock code-review](https://github.com/mattpocock/skills/blob/main/skills/engineering/code-review/SKILL.md), [OpenAI review-agent](https://github.com/openai/codex/blob/main/codex-rs/skills/src/assets/samples/review-agent/SKILL.md), [OpenAI review rubric](https://github.com/openai/codex/blob/main/codex-rs/prompts/templates/review/rubric.md) | Actual-change inspection and actionable, evidence-based findings; include dirty/untracked state, distinguish baseline risks, and use the requested BLOCKER/MAJOR/MINOR/NOTE vocabulary. |
| [Svix, The State of Webhooks 2027](https://www.svix.com/state-of-webhooks/) and [Standard Webhooks specification](https://github.com/standard-webhooks/standard-webhooks/blob/main/spec/standard-webhooks.md) | Informed the optional webhook recipe's delivery, verification, replay, deduplication, retry, observability and documentation prompts. The report is an industry documentation survey, not a normative standard or proof of runtime behavior. |
| [RFC 9110](https://www.rfc-editor.org/rfc/rfc9110.html), [RFC 9421](https://www.rfc-editor.org/rfc/rfc9421.html), [OpenAPI 3.1.1](https://spec.openapis.org/oas/v3.1.1.html) and [AsyncAPI 3.0](https://www.asyncapi.com/docs/reference/specification/v3.0.0) | Primary references for HTTP idempotency/retry semantics, HTTP message signatures and machine-readable webhook/event descriptions. The recipe keeps these standards' scopes distinct and treats project contracts as authoritative. |
| [ISO/IEC/IEEE 42010:2022](https://www.iso.org/standard/74393.html), [NIST SP 800-160 Vol. 1 Rev. 1](https://csrc.nist.gov/pubs/sp/800/160/v1/r1/final) | System-design vocabulary and security engineering lifecycle; used as design context, not a prescribed architecture. Accessed 2026-11-08. |
| [GraphQL October 2021 Specification, Section 6.2.3 and subsections 6.2.3.1–6.2.3.3](https://spec.graphql.org/October2021/#sec-Subscription), [OpenAPI 3.1.1](https://spec.openapis.org/oas/v3.1.1.html), [AsyncAPI 3.0.0](https://www.asyncapi.com/docs/reference/specification/v3.0.0) | API contract and description scopes. GraphQL subscriptions expose application event streams; they are not a schema-change notification mechanism. Exact versions/sections checked 2026-11-08. |
| [PostgreSQL 17 documentation: transactions, constraints and indexes](https://www.postgresql.org/docs/17/) | Engine-specific examples for transaction, schema and query-plan decisions. It is not a cross-database guarantee; use the selected engine/version docs. Accessed 2026-11-08. |
| [Python 3.14 threading and asyncio documentation](https://docs.python.org/3.14/library/threading.html), [Java SE 21 JLS Chapter 17](https://docs.oracle.com/javase/specs/jls/se21/html/jls-17.html) | First-party examples of runtime/language memory and concurrency contracts. They are illustrative only; use the actual project's current language/runtime version. Accessed 2026-11-08. |
| [Apache Kafka 4.2 KafkaConsumer Javadoc: Manual Offset Control, `commitSync`, `commitAsync`, `position` and Multi-threaded Processing](https://kafka.apache.org/42/javadoc/org/apache/kafka/clients/consumer/KafkaConsumer.html), [Kafka 4.2 Producer Configs](https://kafka.apache.org/42/configuration/producer-configs/), [Kafka 4.3 delivery semantics](https://kafka.apache.org/43/design/design/#message-delivery-semantics) | Offset/partition progress must follow the selected client contract; commit the next consumption position only after successful processing, including the completed partition-order prefix under concurrent work. Versioned documentation checked 2026-11-08. Offset gaps mean `lastOffset + 1` must not be generalized as the next record identifier; Kafka producer idempotence does not make an external side effect exactly-once. |
| [OWASP SSRF Prevention Cheat Sheet: Case 1, identified/trusted applications](https://cheatsheetseries.owasp.org/cheatsheets/Server_Side_Request_Forgery_Prevention_Cheat_Sheet.html#case-1-application-can-send-request-only-to-identified-and-trusted-applications) and [Case 2, arbitrary external destinations](https://cheatsheetseries.owasp.org/cheatsheets/Server_Side_Request_Forgery_Prevention_Cheat_Sheet.html#case-2-application-can-send-requests-to-any-external-ip-address-or-domain-name); [NIST SP 800-38D Sections 5.2, 7.1–7.2 and 8.1–8.3](https://csrc.nist.gov/pubs/sp/800/38/d/final); [NIST SP 800-57 Part 1 Revision 5](https://csrc.nist.gov/pubs/sp/800/57/pt1/r5/final) | OWASP distinguishes known/trusted application destinations (Case 1: strict allowlist and application/network defenses) from arbitrary external destinations (Case 2: public-only target policy and blocking internal destinations). Both require case-appropriate parsing, DNS/address and egress controls. GCM authenticated encryption is separate from key management. Sections/editions checked 2026-11-08. |
| [RFC 6749 Section 4.4](https://www.rfc-editor.org/rfc/rfc6749.html#section-4.4), [RFC 9700](https://www.rfc-editor.org/rfc/rfc9700.html), [RFC 7519](https://www.rfc-editor.org/rfc/rfc7519.html), [RFC 8725](https://www.rfc-editor.org/rfc/rfc8725.html), [OWASP Password Storage Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Password_Storage_Cheat_Sheet.html) | OAuth authorization flows, JWT validation and password-KDF guidance. RFC sections and editions checked 2026-11-08; living OWASP guidance accessed the same date. OAuth is not itself an end-user authentication protocol. |
| [Redis latency documentation](https://redis.io/docs/latest/operate/oss_and_stack/management/optimization/latency/), [OpenTelemetry Specification](https://opentelemetry.io/docs/specs/otel/) | Cache/network and telemetry concepts; use actual runtime/workload measurements and the deployed specification/tool version. Living documentation accessed 2026-11-08. |
| [SLSA v1.1](https://slsa.dev/spec/v1.1/), [NIST SP 800-218 SSDF v1.1](https://csrc.nist.gov/pubs/sp/800/218/final), [NIST SP 800-34 Rev. 1](https://csrc.nist.gov/pubs/sp/800/34/r1/upd1/final) | Supply-chain provenance, secure development and contingency/restore concepts; recommendations are scoped to a project's threat model and recovery targets. Editions/access checked 2026-11-08. |
| [NIST AI Risk Management Framework 1.0](https://www.nist.gov/itl/ai-risk-management-framework), [NIST AI 600-1, Generative AI Profile](https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.600-1.pdf), [OWASP Top 10 for LLM and Gen AI Apps 2025](https://genai.owasp.org/llm-top-10/) | Risk identification, evaluation, monitoring, data controls and human oversight for model-enabled features. Frameworks/risk lists inform analysis but do not validate a product or replace applicable policy. Editions accessed 2026-11-08. |
| [PCI DSS v4.0.1](https://www.pcisecuritystandards.org/document_library/), [RFC 9110 §9.2.2](https://www.rfc-editor.org/rfc/rfc9110.html#section-9.2.2) | Payment-data security and HTTP method idempotency boundaries. The references do not determine compliance scope, provider idempotency-key behavior or accounting policy. Accessed 2026-11-08. |
| [NIST Privacy Framework 1.0](https://www.nist.gov/privacy-framework), [W3C WebRTC 1.0](https://www.w3.org/TR/webrtc/), [RFC 8445](https://www.rfc-editor.org/rfc/rfc8445.html), [RFC 8489](https://www.rfc-editor.org/rfc/rfc8489.html), [RFC 8656](https://www.rfc-editor.org/rfc/rfc8656.html) | Privacy-aware notifications and real-time media/session, ICE, STUN and TURN boundaries. Transport/security statements remain scoped to each standard and implementation. Accessed 2026-11-08. |

Research, bounded prototypes, threat-driven review, release recommendations and concise
handoff are tailored to the Product Owner's requested operating model. External patterns
inform implementation; they neither supply approval nor replace the canonical policy.

The design-brief, ui-design and visual-review recipes were authored for the Product
Owner's Design System & Visual Governance work package (2026-10-04). They integrate
persistent repository design context with the existing quality model. No OpenDesign
code, skill text or assets are vendored; no dependency or API compatibility is implied.
The manifest and semantic token conventions are local portable formats that a future
optional adapter could map. Original authorship is not a license assessment of any
external design reference; record those rights per reference before reuse.

The optional webhooks recipe was added in 2.3.0 using the sources above. It is selected
only for projects with webhook flows and adds no dependency, mandatory workflow stage or
universal webhook contract.

The 12 task-selected technical recipes and four task-specific reference guides were
added in 2.4.0. The recipes turn the cited concepts into bounded procedures, decision
points and evidence prompts; the references are progressively loaded only for matching
work. External documents do not grant approval or prove a project's implementation.

The ByteByteGo 2024 guide remains secondary research, not a normative source. The
user-supplied screenshots of PDF pages 95, 108 and 167 were previously read as text
pages; this does not assert visual review of other pages or diagrams. No practice that
depends on an unreviewed diagram is claimed as verified here. The GraphQL, NIST GCM/key
management and Kafka offset corrections use the cited primary standards/vendor
documentation instead.

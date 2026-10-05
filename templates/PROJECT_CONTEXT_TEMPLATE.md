# Project context — [name]

Template: replace bracketed fields; remove guidance after use. Intended destination:
`docs/PROJECT.md`. Keep facts here until separate documents materially help.

Status: [current/draft]. Owner: [name]. Last verified: [date and relevant revision].
Adopted bootstrap: [version and source/revision; archive hash only if supplied]. Local deviations: [none or
rule, reason, scope, approval source; never silently override safety controls].

## Product intent

[Problem, users, intended outcome, in scope, non-goals, constraints, important business
rules and observable acceptance criteria. Mark open product decisions explicitly.]

## Architecture and implementation map

[Current versus proposed components, boundaries, key data flow, interfaces, storage,
external integrations and deployment. Link real entry points/configuration/tests;
do not duplicate implementation details. List applicable accepted ADRs, if any.]

## Local conventions and hazards

[Visual applicability: yes/no and why. Link the design manifest and DESIGN.md when
retained; record the actual renderer and approved existing output. For visual scope,
follow [design initialization](../docs/INITIALIZE.md#visual-or-non-visual-project).
Non-visual projects require no design brief or visual review. Repair links after copying.]

[Stack/tool versions, coding conventions, reuse points, fragile areas, domain invariants,
known failures, scoped instructions and any project-specific skills with usage triggers.
Use the extension convention in the [skill router](../skills/README.md); version local
recipes with the project and keep this map linked to their canonical paths.]

## Knowledge map and active work

| Topic | Canonical location/status |
| --- | --- |
| Product requirements | [this section or link] |
| Architecture / accepted ADRs | [this section or links; none if not needed] |
| Test commands and applicability | [link to project TESTING.md] |
| Security / operations | [this section or link] |
| Glossary | [this section or link] |
| Active work | [issue/file links; remove closed items from this active list] |

## Domain terminology

[Canonical terms, entity names, abbreviations and translations only where relevant.]

## Security and operations

[Data classification, secret handling, allowed paths/services/network destinations,
development versus production access, auth boundaries, backups/recovery and hazards.
Use synthetic data for validation. Name unknowns; no credentials here.]

## Delivery and release

[Setup/run entry point, environments, application version and changelog policy, commit
convention, tag/build/deployment identity, release approver, rollback limits. Keep
application and bootstrap versioning distinct. The Product Owner performs commits and
pushes manually; agents prepare the Git handoff under the universal Git authority rule.
Project conventions do not themselves override reserved Git operations. Review packaging is optional under the
universal policy, not the default release format or validation gate. Link runbooks only
when they exist.]

## Open questions

[Question, owner and which work it blocks. Convert confirmed discussions into the
canonical section or a bounded work item; raw transcripts are not requirements.]

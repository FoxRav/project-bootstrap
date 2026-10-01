# [ID] — [one coherent outcome]

Use for non-trivial work. Keep one canonical file or issue, not competing copies.
When stored under `docs/WORK/`, repair template links relative to that destination.
Routine changes may use a shorter task/PR record under
[the operating policy §3](../PROJECT_BOOTSTRAP.md#3-work-size-and-lifecycle).

Status: [draft / ready / active / blocked / ready for review / complete].
Owner: [implementer]. Reviewer: [independent reviewer or pending]. Updated: [date].
Authority: [request/issue reference; distinguish explicit approval from a proposal].
Risk: [routine / non-trivial / high-risk; triggers and why].
Relevant recipes: [optional links selected from the skill router; omit when unnecessary.
Recipes guide execution and do not approve this work or add completion gates.]

## Goal and context

[User-visible or operational result, reason, relevant current requirements/ADRs,
source of intent, and acceptance owner. Link context instead of copying it.]

## Scope

- In scope: [bounded change].
- Out of scope: [explicit exclusions and existing behavior to preserve].
- Affected components/interfaces/data: [paths and boundaries].
- Constraints and dependencies: [compatibility, performance, security, approved
  dependencies, sequencing and blocking work; none if none].

## Current-state inspection — before implementation

[Base revision and dirty/untracked state; inspected code/tests/configuration; current
behavior and baseline failures; existing patterns to reuse; why no parallel implementation
is needed; conflicts resolved or escalated with sources. Record actual inspection, not intent.]

## Acceptance criteria

- AC1: [observable behavior and how a reviewer can verify it].
- AC2: [regression/invariant or failure-path expectation].

## Plan, risks and approvals

[Small implementation steps, consequential alternatives if needed, regression/data/security
risks, recovery approach, and unknowns. For each approval-gated action record exact scope,
approver, source/date and status; existing explicit task authorization is sufficient.
Pending approval blocks that action only.]

## Validation plan

| Criterion/risk | Check and exact command/cwd or manual procedure | Expected result | When |
| --- | --- | --- | --- |
| [AC1] | [project testing command] | [observable result/count expectation] | [targeted/final] |

[Reproduction before fix where feasible; relevant broader checks and why other layers
are N/A. Project TESTING.md owns reusable commands; this table chooses applicable checks.]

## Checkpoint / handoff

[Current revision/content identity and dirty state; completed steps, new decisions,
checks already run, remaining work, blockers and exact next action. Update on interruption
or handoff. Identify who owns integration if multiple agents are authorized.]

[Git handoff when useful: recommended commit boundaries, proposed message and exact
commands for the Product Owner to run manually. Record any explicit current-task Git
override separately; implementation or release authorization alone is not an override.]

## Completion evidence

[Embed or link the completed REVIEW_TEMPLATE.md record. Map every acceptance criterion
to evidence. Record remaining issues and release state; do not copy another completion
checklist here. Close only under the universal quality model. A review ZIP is not a
work-item completion requirement; select one only for an applicable optional handoff.]

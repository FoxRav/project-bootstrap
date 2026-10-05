# Project context — canonical bootstrap

Status: current for bootstrap maintenance; replace when starting a product.
Owner: Product Owner (see [runtime mapping](RUNTIME.md)). Verified: 2026-10-04.
Adopted foundation: [BOOTSTRAP_VERSION](../BOOTSTRAP_VERSION). Local deviations: none.

## Product intent

Provide the canonical starting foundation for future software repositories, from
utilities to SaaS products. Users are the Product Owner, technical collaborators and
coding agents. Success is a usable copy-and-initialize path, clear authority, safe
autonomy and reproducible evidence without mandatory document sprawl.

Requirements: compact agent entry point; universal policy separated from project
knowledge; explicit conflict and approval rules; proportional validation; reusable
work/decision/review templates; version/change history; and optional on-demand review
packaging. The [skills layer](../skills/README.md) supplies reusable execution recipes.
No application framework, hosting provider, production system or customer
data is part of this repository.

## Architecture and current state

- Root entry points route humans and agents to one universal policy.
- `docs/` contains this repository's facts, actual check commands, initialization and
  the replaceable runtime adapter. Projects may split facts into PRD/architecture/
  security/glossary files later, keeping one canonical location per fact.
- `templates/` contains forms, not active requirements or approvals.
- `skills/` holds 18 universal recipes with selective routing; project copies can add
  local domain recipes. Policy remains in the bootstrap; runtime discovery is an adapter.
- `design/` holds an unconfigured, persistent design template for visual projects.
  Manifest status is `template` here; no product identity or compliant rendered UI is
  claimed. Existing README artwork is preserved, not a brief to invent a new brand.
  Copied projects explicitly activate the layer or mark it disabled during initialization.
- [scripts/bootstrap.py](../scripts/bootstrap.py) checks source integrity and, only on
  explicit invocation, creates a review ZIP; [tool tests](../tests/test_bootstrap.py) and
  [design tests](../tests/test_design.py) exercise failure modes. Python is maintenance
  tooling, not a mandated product stack.
- `REVIEW/` is an optional output area created only when packaging is requested.
  Review notes are included only when selected; no historical report is required.
  Research/cache folders are local and excluded from delivery.

Dependencies: Python 3.10+ standard library for optional maintenance tooling; no third-party
packages. Markdown itself requires no runtime. No app, database, service or deployment.
Conventions: UTF-8, LF, relative Markdown links, concise prose and explicit status.
Policy changes must keep templates and initialization consistent. Update the script's
source inventory when intentionally adding or removing canonical files.

## Knowledge and work map

| Topic | Canonical location |
| --- | --- |
| Product, architecture, terminology, hazards | This file |
| Universal rules and decision process | [Operating policy](../PROJECT_BOOTSTRAP.md) |
| Commands and applicability | [Testing](TESTING.md) |
| People/tools/runtime discovery | [Runtime adapter](RUNTIME.md) |
| Engineering recipes / extension convention | [Skill router](../skills/README.md) |
| Skill design provenance (reference only) | [Skill sources](SKILL_SOURCES.md) |
| Design applicability, intent, tokens and reference workflow | [Initialization](INITIALIZE.md#visual-or-non-visual-project), [design definition](../design/DESIGN.md), [manifest](../design/manifest.json) |
| Visual review evidence within normal review | [Visual worksheet](../design/qa/visual-review.md) |
| Current work | None; add links here when starting a bounded work item |

No accepted ADR is required for routine maintenance. Create `docs/ADR/` and a numbered
record when a new consequential choice needs one; do not invent acceptance history.

## Terminology

**Bootstrap:** the reusable operating foundation, versioned independently of products.
**Work item:** the canonical bounded scope, in a file or issue, not duplicated in both.
**Approval:** explicit authorization for a specified action; never inferred from a draft.
**Evidence:** results tied to commands and an identified content state.
**Independent review:** review by a person or agent that did not author the change.

## Security and operations

Data classification: ordinary process documentation; no customer data or credentials
belong here. Public official-documentation research is allowed without private query
content. Writes for bootstrap maintenance are restricted to this repository. Package
outputs must exclude local research, dependency directories and sensitive files.
No production credentials or outbound publishing integrations are needed.

Normal delivery evidence: validation commands/results, tests, review findings, Git
status/diff and relevant documentation updates. Review ZIPs follow the
[optional packaging policy](../PROJECT_BOOTSTRAP.md#optional-review-packaging); they are
not the required release format. A selected package carries a source manifest and
SHA-256 sidecar. Product Owner approval is still required for release/publication.
The Product Owner performs commits and pushes manually in the terminal; agents prepare
the handoff and follow [Git authority](../PROJECT_BOOTSTRAP.md#git-authority) for the
reserved operations and any explicit current-task override.
Use Git revision/tag and any actual release artifacts to identify released content.
New copied projects initialize their own Git history.

Known hazards: copying this context unchanged into a product; stale instructions after
tool upgrades; confusing a self-review with independent review; calling skipped checks
PASS; and treating an unsigned checksum as proof of publisher identity.

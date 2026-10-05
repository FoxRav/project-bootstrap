# Bootstrap changelog

This records canonical foundation releases, not the copied application's releases.
Version semantics and adoption policy: [PROJECT_BOOTSTRAP.md §7](PROJECT_BOOTSTRAP.md#7-living-knowledge-git-and-versions).

## 2.2.0 — 2026-10-04

Added persistent design context, semantic tokens, reference guidance and visual review
for projects with visual output, plus design-brief, ui-design and visual-review recipes.
Initialization distinguishes visual and non-visual projects; agents load applicable
design context before visual changes. Added deterministic design validation and failure
tests. Included existing README artwork in the source inventory with explicit PNG
integrity checks, fixing validation of the already tracked binary source.

Minor version: compatible conditional capability, with existing authority, lifecycle,
approvals, quality model, manual Git execution and optional packaging preserved. No
framework, external dependency or native runtime adapter is added. When adopting,
normalize an existing visual project's approved design instead of restyling it; populate
the brief/tokens and record authority before activation. Mark non-visual projects
disabled. Template values and manifest status are not product approval.

## 2.1.1 — 2026-10-01

Prepared public-facing documentation with Finnish and English reading paths, a concise
quick start and a repository map. Generalized the runtime team mapping, clarified new
project Git provenance and strengthened local-artifact ignore rules. Patch version:
these are documentation and publication-hygiene corrections; operating authority,
skills, quality gates and optional packaging behavior remain compatible.

## 2.1.0 — 2026-10-01

Added 15 reusable engineering skills, selective routing and a project-local extension
convention. Integrated recipes with agent discovery, project context, initialization,
work templates and runtime guidance. Added skill structure/link/policy regression
checks and independent behavioral review. Recorded primary-source design provenance
without vendoring external recipes.

Minor version: this is a compatible capability addition. Existing authority, approval,
quality, manual Product Owner Git execution and optional packaging rules are preserved;
no new mandatory development stages or native runtime installation are introduced.

## 2.0.2 — 2026-09-30

Made Git authority explicit: the Product Owner performs commits and pushes manually
in the terminal. Agents inspect changes and prepare messages, commit boundaries and
exact commands; they must not commit, push, create tags, rewrite history or merge
branches unless the Product Owner explicitly overrides the rule for the current task.
Aligned agent guidance, initialization and handoff templates. Reviewed, validated work
can be complete before the Product Owner performs Git operations. Review packaging
remains optional and on demand.

## 2.0.1 — 2026-09-30

Corrected review packaging to be optional and on demand. Normal work, commits, features
and validation require completion evidence, not a ZIP or SHA-256 sidecar. Kept the
explicit packaging commands, with optional selected review notes and safe creation of
the output directory. Removed one-time redesign artifacts and work history from the
canonical template. Normal checks now work without review files or package outputs.

## 2.0.0 — 2026-09-30

Redesigned the single-file 1.0 foundation into a repository with a compact agent entry
point, project context, initialization checklist and reusable work/ADR/review templates.
Added explicit authority/conflict handling, risk-based approval boundaries, one quality
model, auditable evidence, tool-neutral capability routing and versioned adoption.
Added standard-library validation and reproducible review packaging.

**Breaking adoption:** existing projects should compare rules and local exceptions,
migrate duplicated checklists into the quality model, and populate real validation
commands. Keep project-specific knowledge and application history. Do not overwrite an
existing project with this repository or treat its bootstrap-maintenance context as a
product specification. Review new approval boundaries with the Product Owner.

## 1.0 — original source, date not recorded

Single `PROJECT_BOOTSTRAP.md` operating model; original release date not recorded.

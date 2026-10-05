# Validation for the canonical bootstrap

Owner: bootstrap maintainer. Verified: 2026-10-04.
This is the project command registry for [the universal quality model](../PROJECT_BOOTSTRAP.md#5-one-quality-and-completion-model).
Replace it when initializing a product; these checks do not validate application code.

## Normal validation

Run from the repository root. Prerequisites: Python 3.10+ standard library. Git is
needed for Git evidence only; a source snapshot can be checked without it. No install,
network, credentials or third-party dependencies are required. Temporary test fixtures
stay inside excluded `.review-cache/` and are cleaned. No `REVIEW/` directory, review
report, ZIP, manifest or checksum is required for normal work or these checks.

| Layer / trigger | Exact command | Expected result |
| --- | --- | --- |
| Structure, skills, design, format, syntax and bounded pattern checks; after document/tool changes | `python scripts/bootstrap.py check` | Exit 0; inventory, skill/design structure, tokens, PNG framing/CRC, links/fragments, text hygiene and version pass; no review outputs created |
| Tool regression tests; after tooling changes and before completion when relevant | `python -m unittest discover -s tests -v` | Exit 0; all tests pass; no skipped tests |
| Git inspection; before delivery or a Product Owner commit where Git exists | `git status --short`, `git diff --check`, `git diff`, `git diff --cached` | No whitespace errors; all changes and untracked files inspected; status reported truthfully |

Normal completion evidence is validation commands/results, tests, review findings,
Git status/diff and relevant documentation updates. Packaging is not a work-item,
commit, feature or normal-validation gate. The tooling's regression suite tests packaging
behavior only with disposable fixtures; it does not leave a review package in the repository.
Validation does not commit, push, tag, rewrite history or merge branches. Those operations
follow [Git authority](../PROJECT_BOOTSTRAP.md#git-authority) and are not normal test steps.

## Optional review and handoff packaging

Choose packaging only for a reason in
[the optional packaging policy](../PROJECT_BOOTSTRAP.md#optional-review-packaging):
an explicit Product Owner request, substantial independent-review handoff, materially
useful frozen snapshot, or external handoff requiring a self-contained artifact.
Independent review can normally use repository access and the diff directly.

| Optional operation | Exact command | Expected result |
| --- | --- | --- |
| Build a selected review snapshot | `python scripts/bootstrap.py package` | Exit 0; creates `REVIEW/` if absent, then verifies ZIP, source manifest and SHA-256 sidecar |
| Verify that snapshot against current source | `python scripts/bootstrap.py verify-package` | Exit 0; entries/bytes, CRC, manifest and sidecar match; creates nothing |

Both package operations recheck source integrity. Neither is part of the normal command
loop. A missing/stale package is irrelevant to `check` and normal completion. An explicit
`verify-package` without a package reports that absence; it never creates one automatically.

Optional handoff notes can be selected using `--include-review REVIEW/notes.md` on both
commands (repeat the option for more files). Only explicitly selected `.md`/`.txt` files
under `REVIEW/` are added and validated; no report is mandatory and no other review files
are swept in. Use the same selections when verifying the package. Do not include secrets.

`verify-package` expects ZIP, sidecar and external source manifest in `REVIEW/`. Extracting
the ZIP supplies the manifest; retain/copy the original ZIP and supplied sidecar beside
it if using this command to verify a received copy. A checksum detects byte changes,
not publisher authenticity; obtain the expected checksum through a trusted channel.

The package inventory is in [scripts/bootstrap.py](../scripts/bootstrap.py). It includes
all canonical source files, including dotfiles, plus only the selected optional notes.
The ZIP also contains `REVIEW/SOURCE_MANIFEST.sha256.txt` with hashes of those inputs. ZIP and its own
checksum are not included recursively. The external manifest is regenerated from the
same byte snapshot. Entries are sorted with fixed timestamps/permissions; repeated
builds of unchanged sources on the same Python/zlib toolchain produce identical bytes.

Explicit exclusions: `.git`, research/review scratch, caches, virtual environments,
dependency/build directories, `.env*`, key files, temporary files and OS metadata.
`REVIEW/` is excluded from normal source discovery; its contents do not affect routine
checks. Unknown non-excluded source files fail the inventory check; review changes to
`SOURCES` before adding canonical source files. Do not add handoff reports to that required
inventory. Symlinks/junctions in included/output paths are rejected. Do not use this
tool as a general-purpose product packager or a substitute for a full secret scanner.

## Applicability and review

Skill validation requires all 18 universal recipes, matching metadata/title, nonempty
standard headings in order, an ordered process, router/entry-point links and references
to the shared authority contract. Canonical metadata uses a small YAML-compatible
subset: plain `name` and a single-line double-quoted `description` with JSON escaping;
no YAML library or runtime installation is needed. The closed inventory rejects
accidental files such as historical bootstrap work records outside the excluded outputs.

Design validation checks the local v1 manifest's exact fields and portable paths, status,
nonempty identity, required design sections and semantic tokens. Active status rejects
default identity names; it does not prove approval, resolved prose or a finished brief.
The canonical token checker accepts one `:root` block of custom-property declarations
with terminating semicolons; it rejects missing/empty/duplicate roles and undefined or
cyclic `var()` references. It is not a general CSS parser or a browser renderer. A copied
product adapts this bounded checker for its themes/stack alongside its normal checks.

The canonical template ships all design files even in template/disabled state so its
reusable capability can be validated. Non-visual products do not need to populate them,
adopt the sample tokens or perform visual review. Product adoption can remove unused
files after adapting/removing this closed inventory and repairing references. Tests in
[test_design.py](../tests/test_design.py) cover activation states, malformed manifests,
unsafe paths, broken context routing and token regressions.

Only explicitly listed PNG sources bypass UTF-8 text validation. The existing README
image receives signature, chunk framing, CRC and required-chunk checks, not full pixel
decoding, rights analysis or a metadata secret scan. Inspect image content/metadata and
rights manually when adding/changing assets. Only the named empty directory placeholder
may omit text/newline checks; unknown binaries still fail inventory and all real text
keeps its existing checks. Packaging preserves binary and empty-file bytes exactly.

The bounded skill-policy scan rejects common automatic Git, approval-bypass and mandatory
ZIP directives, including in descriptions and the router. It is a regression guard,
not a natural-language proof: paraphrases, mixed clauses and indirect instructions can
escape pattern matching. Independent semantic review must assess authority, test integrity,
optional packaging and workflow outcomes. When changing skills, walk realistic requests:
repository facts versus unanswered product choices, a blocked schema slice, a failing
valid test, read-only review of dirty/untracked code and a release awaiting approval.
Record which recipes were exercised; a tabletop is not application execution or a full
agent benchmark. Recheck any native discovery adapter in its actual runtime separately.

For design recipes, also walk initialization of a non-visual utility, a visual product
with an existing brand, and one with unresolved identity. Exercise a scoped UI change,
a conflicting reference and visual review with unavailable rendered evidence. Check
that context loads before visual edits, ordinary approved styling stays autonomous,
and no recipe substitutes source checks for a rendered visual PASS. For actual product
UI changes, use [the visual worksheet](../design/qa/visual-review.md) within the existing
review evidence; verify relevant states, viewport/page sizes and accessibility with the
product's real tools. This template has no rendered product UI to certify.

Normal layers are text/structure checks, Python syntax parsing, unit/negative-path
tests and bounded credential scanning. Package build/integrity checks apply only when
creating or verifying a selected review/handoff artifact, or testing the packaging tool.
The link checker supports this repository's inline Markdown links and ATX headings;
it does not crawl external URLs, reference-style links or arbitrary Markdown extensions.
Research links were fetched separately; future source changes require rechecking.

No application lint/type configuration, API/contract suite, database/migration checks,
service integration/E2E or runtime server smoke tests apply: there is no application.
Python tooling has syntax checks and regression tests; no third-party linter/type checker
is configured. No CI service is configured; run these commands locally, or wire the same
commands into the selected CI during adoption. None of these omissions is recorded as PASS.

For policy changes, manually walk a routine typo/fix, dependency addition, public contract
change, destructive migration, stale-doc conflict, unavailable validation and release.
Confirm they lead to the intended autonomy/approval/evidence paths. Walk the initialization
checklist as both a small utility and a service: optional documents must stay optional.
An independent reviewer should challenge contradictions, duplicated authority, unsafe
exceptions, portability and stale template references. Record actual review coverage,
findings and limits in [the review form](../templates/REVIEW_TEMPLATE.md).

## Choosing checks in a copied product

For each selected layer, replace the table with actual command/cwd, tool/setup versions,
safe fixtures/environment, expected success and local/CI trigger. Start with checks that
detect the first task's realistic failures; expand to contracts, integration, schema,
E2E, security, build and runtime smoke checks as those boundaries appear. Keep intentional
N/A explanations visible. A selected but unavailable check is BLOCKED/NOT RUN, never N/A
merely because it is inconvenient.

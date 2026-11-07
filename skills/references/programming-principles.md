# Programming principles

## Purpose

Use maintainable design principles to solve an observed change-pressure problem.
Principles are decision aids, not an instruction to maximize abstraction or minimize
line count.

## Use when

A design review or implementation has coupling, duplication, unclear ownership,
unstable interfaces, difficult testing or an abstraction decision.

## Procedure

1. Name the concrete change or failure that is expensive today; inspect real call
   sites, tests and expected next changes before proposing a principle or pattern.
2. Keep responsibilities cohesive and dependencies pointed toward stable contracts.
   Split a module only when its reasons to change or ownership differ in practice.
3. Prefer simple, explicit behavior and composition. Introduce an abstraction when it
   removes repeated policy or isolates a real volatility; avoid speculative interfaces,
   inheritance trees and wrappers with only one trivial implementation.
4. Preserve encapsulation: expose the smallest useful contract, keep invariants with
   their owning data and avoid global mutable state. Make side effects visible at
   boundaries.
5. Apply SOLID concepts as questions, not a checklist: does a change force unrelated
   consumers to change, does a contract permit the needed substitution, and is a
   module depending on details it should not know?
6. Apply DRY only to duplicated knowledge that must change together. Similar-looking
   code with different business rules may be safer kept separate.
7. Prefer readable control flow, meaningful names and explicit error behavior over
   clever compression. Measure before optimizing; choose the simplest implementation
   meeting verified constraints.
8. Test externally observable behavior and invariants. Refactor with focused tests,
   then compare the implementation against the original concrete problem.
9. Record a durable pattern or ADR only when it resolves a consequential repeated
   choice; do not create a policy document for a local implementation detail.

## Decision points

Do not treat SOLID, DRY, KISS, YAGNI, Clean Architecture, hexagonal architecture or
design patterns as universal mandates. YAGNI does not justify omitting a confirmed
requirement; DRY does not justify coupling unrelated concepts. Prefer a local
straightforward design until observed needs justify wider structure.

## Approval boundaries

Follow the [shared contract](../README.md#shared-contract), [authority](../../PROJECT_BOOTSTRAP.md#1-authority-and-evidence),
[approval boundaries](../../PROJECT_BOOTSTRAP.md#4-autonomy-and-approval-boundaries),
[quality model](../../PROJECT_BOOTSTRAP.md#5-one-quality-and-completion-model),
[Git authority](../../PROJECT_BOOTSTRAP.md#git-authority) and
[optional review packaging](../../PROJECT_BOOTSTRAP.md#optional-review-packaging).
This guidance does not authorize public-contract, schema, security or architecture
changes requiring Product Owner approval.

## Outputs and evidence

State the concrete problem, alternatives considered, why the chosen boundary or
abstraction helps, behavior tests and any trade-off. Link relevant code/tests/ADR.
Do not claim a principle was followed merely because its name appears in a review.

## Sources

- [Martin Fowler, YAGNI](https://martinfowler.com/bliki/Yagni.html), accessed 2026-11-08.
- [Robert C. Martin, The Dependency Inversion Principle](https://web.archive.org/web/20150905000000/http://www.objectmentor.com/resources/articles/dip.pdf), accessed 2026-11-08. Treat as a design essay, not a normative standard.
- [ISO/IEC/IEEE 42010:2022](https://www.iso.org/standard/74393.html), architecture description concepts; accessed 2026-11-08.

# Visual review worksheet

Reusable evidence prompts, not a second quality gate or an approval record. Use the
[visual-review skill](../../skills/visual-review/SKILL.md) within the existing
[review template](../../templates/REVIEW_TEMPLATE.md) and
[completion model](../../PROJECT_BOOTSTRAP.md#5-one-quality-and-completion-model).
Embed or link the completed evidence in the active work item/PR; leave this reusable
worksheet unfilled. No ZIP or separate agent organization is required.

## Scope and identity

Record work item, revision/dirty content, design manifest state/version, changed views
or artifacts, relevant existing approved views, reviewer and authorship relationship.
Name browser/device/viewport and state, or deck/document page size and renderer.
Select representative normal, loading, empty, error and constrained-size states as
relevant; justify omitted cases. Use synthetic content and redacted captures.

## Evidence to inspect

Read [DESIGN.md](../DESIGN.md), [tokens.css](../tokens.css), selected
[references](../references/README.md), actual rendered output, implementation and relevant
checks. Source inspection or a token lint alone is not a visual review. If rendering,
screenshots or a suitable viewer are unavailable, mark the affected review NOT RUN or
BLOCKED and identify what evidence is needed. Do not manufacture a pass.

## Review prompts

| Area | Questions |
| --- | --- |
| Design compliance | Do the view and its variants express the agreed intent/DNA? Are palette, typography, token usage, spacing, radius, borders and shadows consistent with their semantic roles? |
| Anti-generic constraints | Were unapproved gradients, sparkle/stock art, floating/oversized cards, pill controls, centered hero/three-card composition or decorative whitespace introduced? Does the visual hierarchy serve this product? Check explicit exceptions, not reviewer taste. |
| Negative specification | Does the result avoid the particular unwanted traits in This Product Must Not Look Like? |
| UX sanity | Is the highest-value information first? Does density fit the audience? Are controls near the task and states understandable? Does decoration obstruct use? |
| Accessibility | Check the project's applicable contrast, focus/keyboard, labels, non-color cues, zoom/reflow, reduced motion and text/chart alternatives. Record actual checks and limits. |
| Consistency | Does the new view look and behave like the approved existing product across relevant sizes/states/media? |
| Reference and asset use | Were only approved traits reused, exclusions respected, rights recorded and private data kept out of evidence? |

## Findings and result

Use existing BLOCKER / MAJOR / MINOR / NOTE severities. Each finding states location or
view/state, violated decision/token, observed effect, evidence and required correction.
Separate demonstrated defects from preferences or an unapproved proposed redesign.
Initial review is read-only; fixes return to the authorized implementation phase.

Record pass / changes required / insufficient evidence, commands/manual observations,
limits, unresolved decisions and recheck of affected findings on the final state.
Self-review is labeled; non-trivial changes require independent review under the same
universal model. A favorable visual review does not grant release approval or authority
to change identity. Product Owner approval applies where the existing rules require it.

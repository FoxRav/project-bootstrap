# Project design system

This is a reusable, unconfigured template, not an approved brand for every project.
Replace the bracketed prompts with project decisions during initialization. The
[manifest](manifest.json) owns identity and activation state; [tokens](tokens.css) own
concrete visual values. This file owns their meaning and use. Keep one persistent
design system per project; do not regenerate it for each work item or agent session.

The manifest uses the local `project-bootstrap-design/v1` format: identity (`id`, `name`),
one status and the five relative paths shown in the file. Paths are fixed within this
canonical scaffold; copied projects may adapt them and their checks deliberately. No
external schema service or OpenDesign dependency is involved. A future optional adapter
can map this repository-owned manifest, Markdown and CSS without owning design authority.

## Activation and authority

Use [initialization](../docs/INITIALIZE.md#visual-or-non-visual-project) to choose:

| Manifest status | Meaning |
| --- | --- |
| `template` | Shipped scaffold; applicability and product identity not yet decided |
| `disabled` | No visual output; no design brief, token adoption or visual review required |
| `draft` | Visual project being defined; proposals/experiments are not approved product design |
| `active` | Project identity and its decision sources are recorded; implement within that design |

Visual output includes web/desktop/mobile UI, dashboards, landing pages, portals, decks,
infographics, social visuals and branded documents. A CLI or service with no such output
can disable this layer. Reassess when its scope gains visual output. A README image
alone does not authorize inventing a new product brand from this template.

Within the [existing authority model](../PROJECT_BOOTSTRAP.md#1-authority-and-evidence),
resolve visual intent using: explicit Product Owner decision → this DESIGN.md → semantic
tokens → approved existing UI/output → approved references → design skill → model judgment.
This ordering does not outrank applicable project instructions, authorized scope, accepted
architecture or universal approval/security/quality rules. Tokens implement the intent
here; contradictory files require the existing conflict procedure, not a silent choice.
Observed UI is not automatically approved UI. External references are evidence, not policy.

Existing project design authority overrides model preferences. Preserve decisions unless
the task authorizes a change. Record an authorized identity change and its affected tokens,
references and implementations together; use an ADR only when its lasting trade-off merits
one. Routine UI work within the established system remains autonomous under
[the approval rules](../PROJECT_BOOTSTRAP.md#4-autonomy-and-approval-boundaries).

## Design intent

[State the product purpose and how it should feel. Translate each adjective into an
observable choice: for example, operational means scan-first hierarchy and explicit
status text. Explain why this fits the domain; avoid an unqualified "modern/premium".]

## Target audience and environment

[Users, their main decisions/tasks, expertise, devices, input methods, lighting, locale
and operational environment. Specify suitable information density and terminology.]

## Design DNA

[Define 3–6 project-specific traits. For each, state a visible consequence and a concrete
counterexample. Examples such as industrial precision or editorial typography are choices
to evaluate, not this template's mandatory identity.]

| Trait | Visible consequence / where it appears | Counterexample |
| --- | --- | --- |
| [Project trait] | [Observable layout, type or interaction choice] | [What would violate it] |

## Visual identity

[Describe the roles of primary/accent/neutral colors, surfaces, text and status colors;
contrast principles; borders, radius, shadows, spacing and iconography. Explain their
domain/brand rationale. Reference semantic token names instead of duplicating raw values.
Specify approved asset/font sources and relevant rights. Do not inherit sample colors
or fonts just because they compile.]

## Typography

[Choose heading, body and monospace families, their fallbacks and use cases. Define
heading hierarchy, weights and line-height roles through the typography tokens. Record
font availability/licensing, language coverage, long-text and zoom behavior. Agents must
not substitute another family or weight scheme for personal preference.]

## Layout principles

[Define content width, grid/alignment, density, margins, spacing rhythm, sidebar behavior,
card versus row/table use, table density, dashboards and responsive/adaptive rules.
For slides/documents specify page geometry and reading order instead of irrelevant UI
breakpoints. State what collapses, wraps or changes order at constrained sizes.]

## Component language

[Describe only relevant families: buttons, inputs, cards, tables, dialogs, navigation,
status indicators, notifications and charts. State hierarchy, interaction/state patterns,
disabled/loading/empty/error behavior and accessibility expectations. For static outputs
use the equivalent repeated visual structures. Link existing components; do not create
a parallel component library. Mark irrelevant families N/A with a reason.]

## Accessibility and interaction

[Record applicable accessibility requirements and how to verify them: contrast targets,
keyboard/focus order and visibility, names/labels, non-color status cues, zoom/reflow,
reduced motion and chart/text alternatives as relevant. Include constraints of the
chosen medium; do not label sample tokens or a screenshot as accessibility compliance.]

## Anti-Generic AI Design Rules

Do not make an interface look "AI-like". Design for the actual product domain.
The following are forbidden by default unless an explicit, recorded project design
decision justifies the exception and its scope:

- Gratuitous blue-purple gradients, random gradient text or decorative glow effects.
- Glassmorphism without a functional/design justification.
- Oversized rounded SaaS cards, excessive pill controls or unnecessary floating cards.
- Generic AI sparkle icons, generic hero art or unrelated stock illustrations.
- The default centered hero + CTA + three feature cards arrangement without a task reason.
- Excess whitespace whose only rationale is to look premium.
- Styling copied from generic AI/SaaS landing pages or arbitrary unbranded colors.
- Arbitrary font changes; choosing Inter/system fonts merely because they are familiar defaults.

These are constraints on unreasoned choices, not a ban on a legitimate product domain.
An established, approved interface is not a license for unsolicited redesign. Surface a
conflict with these defaults and resolve its authority/scope before changing that identity.

## This Product Must Not Look Like

[List project-specific negative references and the exact traits to avoid. Possibilities
include a generic Tailwind SaaS template, crypto/gaming dashboard, consumer social feed,
Apple-style marketing page, ChatGPT-style chat shell or generic startup landing page.
Choose only relevant contrasts; do not inherit this example list as universal taste.]

## References and assets

Use the [reference index](references/README.md) for source, approval, intended use and
"do not copy" limits. Read relevant references before implementation, not every image.
Store approved production assets under `assets/`; keep their source/rights and intended
uses in this section or the reference index. No prompts need updating when a reference
is added to the index. Unindexed material has no design authority.

## Technical constraints

[Existing UI stack/components, CSS or non-web rendering constraints, supported media,
asset/font delivery limits, performance constraints and approved tools. Map semantic
CSS values to the actual renderer for decks/native/document outputs; CSS need not execute
there. Preserve semantic names or document the mapping so values do not drift.]

## Decision record and maintenance

[Link confirmed Product Owner/brand decisions and their scope/date, including any default
rule exceptions. Identify the design owner, acceptance source and unresolved questions.
Changing manifest status alone is not approval. Resolve blocking prompts before activation;
record explicit N/A with rationale where a topic does not apply.]

Design brief establishes this once, revisiting only actual changes. Implementation consumes
it; [visual review](qa/visual-review.md) tests the result. Record findings in the existing
work/review evidence rather than creating another lifecycle or default report store.

# Initialize a project

Use this in the **new project directory**, never as instructions to erase the canonical
bootstrap. Each item needs a short answer or an explicit N/A, not a separate document.
Product decisions that are not yet known stay open; do not fabricate them.

## Copy and establish identity

- [ ] Copy the source into an empty destination. Exclude `.git`, caches, credentials,
  dependencies and any optional review artifacts. Direct copying requires no ZIP.
  If adopting a supplied review package, verify its checksum before extraction.
- [ ] A clone includes the bootstrap's history and remote. For a new product, copy its
  canonical source into a separate empty directory without `.git`, then let the Product
  Owner initialize the product's own repository. Keep the original clone intact; do not
  push the product to the bootstrap remote. Retain applicable license/attribution notices.
- [ ] Record the adopted [bootstrap version](../BOOTSTRAP_VERSION) and source/revision
  identity in project context (archive hash only when adopting an actual package).
  Retain this provenance when customizing the project.
- [ ] Replace [PROJECT.md](PROJECT.md) using the
  [project context template](../templates/PROJECT_CONTEXT_TEMPLATE.md): product name,
  owner, problem, users, scope/non-goals, initial acceptance criteria and constraints.
- [ ] Rewrite the root README for the product and update the opening identity in
  [AGENTS.md](../AGENTS.md). Preserve the agent navigation and universal-policy link.
- [ ] Update [RUNTIME.md](RUNTIME.md) for the actual team and tools. Keep repository-local
  conventions, hazards, domain terms and links to any relevant skills in project context.

## Visual or non-visual project

- [ ] Does this project produce a UI or other visual output? Include web/desktop/mobile
  interfaces, dashboards, landing pages, portals, presentations, infographics, social
  graphics and branded documents. A service or CLI with no visual output can answer no.
- [ ] Record applicability in project context and set [manifest](../design/manifest.json)
  status: `disabled` for non-visual projects, `draft` while defining visual intent,
  `active` for a resolved, authorized baseline. The shipped `template` is unconfigured.
  Status records readiness; it never grants approval. Reassess when visual scope is added.
- [ ] For a visual project, identify existing brand/UI/approved references. Use
  [design-brief](../skills/design-brief/SKILL.md) to normalize that design, or define it
  from product intent if absent. Fill [DESIGN.md](../design/DESIGN.md), replace illustrative
  [token values](../design/tokens.css) deliberately and maintain the
  [reference index](../design/references/README.md). Resolve meaningful unknowns through
  the existing decision process; do not invent an approved identity.
- [ ] For visual projects, record three to six Design DNA traits, project-specific negative choices,
  accessibility needs, layout/typography and technical constraints. Verify references,
  font/asset rights and token mappings for the actual renderer. Link approval sources
  for consequential choices; reuse existing specific authorization.
- [ ] For non-visual projects, no brief, populated tokens or visual review is required.
  Keeping the disabled template is harmless; removing unused design files in the copied
  product requires adapting its links/instructions and any retained maintenance inventory.
- [ ] Route visual implementation through [ui-design](../skills/ui-design/SKILL.md) and
  rendered review through [visual-review](../skills/visual-review/SKILL.md), using the
  existing work/review evidence. Design persists between tasks. No OpenDesign service,
  runtime installation, framework or additional approval workflow is needed.

## Choose only the foundation needed now

- [ ] Retain the [skill router](../skills/README.md) and load recipes only as needed.
  Add project-specific recipes using its extension convention and link their triggers
  from project context. Verify explicit-path loading and any deliberately added native
  discovery adapter using [runtime guidance](RUNTIME.md#skill-discovery).
- [ ] Document current/proposed architecture, boundaries, data and deployment in project
  context. For a small utility, a few paragraphs are enough. Mark proposals as proposals.
  Split into `docs/PRD.md`, `docs/ARCHITECTURE.md`, `docs/GLOSSARY.md` or `docs/SECURITY.md`
  only when useful; replace the original section with a link, updating the context map.
- [ ] Confirm consequential technology, dependency, compatibility and security choices
  under [the approval policy](../PROJECT_BOOTSTRAP.md#4-autonomy-and-approval-boundaries).
  Create `docs/ADR/` with [the ADR template](../templates/ADR_TEMPLATE.md) when the
  rationale merits preservation. Do not require an ADR for each library call or small edit.
- [ ] Identify permitted filesystem/network scope, private-data handling, secret injection,
  test environment and production boundaries. Do not copy live secrets or broad permissions.
- [ ] Replace [TESTING.md](TESTING.md) with actual setup and validation commands for the
  selected stack. For every applicable quality layer, specify command/cwd, prerequisites,
  expected result and trigger; explicitly explain N/A layers. Set equivalent CI checks
  when CI exists. Execute the first applicable check; placeholders are not a green baseline.
- [ ] Set application version/changelog/tag/artifact convention and release owner in project
  context. Keep `BOOTSTRAP_VERSION` as the adoption marker. Preserve the bootstrap
  changelog as provenance (move it and repair links if the app needs root `CHANGELOG.md`).

## Remove bootstrap-maintenance residue in the copy

- [ ] If the copy contains optional review artifacts or completed project-specific work
  records, omit them from the new project's active context after preserving any needed
  provenance. Repair references to removed files. The canonical template needs neither.
- [ ] The `scripts/bootstrap.py` inventory and `tests/` serve the canonical
  template only. Remove them and their commands/links in the copied product, or explicitly
  adapt them to the new repository. The packaging capability may be retained for optional
  handoffs, but must not constrain the product to the template's file list or become a
  default validation/commit/feature gate. Keep the reusable templates and universal policy.
- [ ] Review ignore rules and text settings for the chosen stack. Keep deliberate examples
  such as `.env.example` free of real credentials. Search remaining text for bootstrap-only
  identity, stale paths, sample owners and unresolved template fields.

## Establish the first working baseline

- [ ] Prepare the baseline files and inspect staged/untracked changes. The Product Owner
  initializes Git if absent and performs the baseline commit and any push manually in
  the terminal. Agents may propose the message, commit boundaries and exact commands;
  agent execution of reserved Git operations requires an explicit current-task override
  under [Git authority](../PROJECT_BOOTSTRAP.md#git-authority). Do not copy the canonical
  repository's `.git` history. Configure a remote only when appropriate.
- [ ] Create the first bounded issue or `docs/WORK/` item using the
  [work template](../templates/WORK_ITEM_TEMPLATE.md). Link it from project context.
  For routine work a short task/PR description is sufficient.
- [ ] Start an agent at `AGENTS.md`: confirm it can identify purpose, active scope, checks
  and stop conditions without reading all history. Verify any scoped instruction files
  with the runtime adapter's discovery procedure.
- [ ] Confirm the Product Owner's intended scope, approved high-risk choices and remaining
  unknowns. Implementation may begin for the bounded, sufficiently specified safe portion;
  unresolved decisions block only the work that depends on them.

Ready means the project has an identity, clear initial scope, a small current context,
an executable validation baseline and known access/approval boundaries. It does not mean
all future product questions have been answered.

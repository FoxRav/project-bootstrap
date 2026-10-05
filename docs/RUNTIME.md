# Runtime adapter

Replaceable project-local mapping. Owner: Product Owner. Last checked: 2026-09-30.
Universal responsibilities and capability classes are defined in
[the operating policy §2](../PROJECT_BOOTSTRAP.md#2-responsibilities-and-routing).

## Project team mapping

| Responsibility/capability | Current default |
| --- | --- |
| Product Owner | Name the project's human decision maker |
| Architect / reviewer / general builder | A person or agent capable of the specific design/review task |
| Implementation / repository engineering | A coding agent or developer with suitable repository access and verification tools |
| HIGH-REASONING | A suitable reasoning mode for the ambiguity and risk; verify availability in the chosen runtime |
| REVIEW | Separate capable reviewer context with access to the actual final change |
| LOW-COST / ROUTINE | Economical capable mode with deterministic verification |
| DETERMINISTIC / HUMAN | Shell/tool operations or the responsible person where simpler and safer |

Fill this mapping for each project. It does not require a particular provider or model.
Select current model/settings in the runtime; recheck this mapping after changes.
Do not copy model names into universal policy or task acceptance criteria.

## Verified instruction discovery

The official Codex guide describes guidance assembled at run startup: global guidance,
then project-root-to-working-directory guidance. Each directory contributes at most
one nonempty file, preferring `AGENTS.override.md`, then `AGENTS.md`, then configured
fallbacks. Later, deeper guidance overrides earlier guidance. Without a detected
project root, only the current directory is checked. The documented default combined
limit is 32 KiB. [Source: AGENTS.md guide](https://learn.chatgpt.com/docs/agent-configuration/agents-md).

Practical application here: start from the project root and keep `AGENTS.md` compact.
Before editing a subtree, inspect applicable instructions there explicitly; do not
assume a root-started session loaded every descendant file. After instruction edits,
verify the effective guidance in a fresh run. Override files can shadow normal files;
inspect them when behavior differs from expectations. Linking another document does
not establish that the runtime automatically read it; our entry point directs that read.
The repository's decision hierarchy is a team policy inside runtime constraints, not a
claim that repository text outranks system/developer instructions.

## Skill discovery

The portable source is [skills/README.md](../skills/README.md); AGENTS directs an agent
to select and read the relevant `skills/<name>/SKILL.md`. This explicit path workflow
works without installing anything. It does not claim native slash-command registration.

The current official Codex guide describes repository discovery under `.agents/skills`
from the working directory toward the Git root, and progressive loading of metadata
before a selected body. Our `/skills` directory is not that native discovery path.
Do not assume `$skill-name` or a skills menu finds these files automatically.
[Source: skill guide](https://learn.chatgpt.com/docs/build-skills).

If a copied project needs native discovery, implement and verify its runtime-specific
adapter deliberately: preserve one canonical body, repair relative links if relocating,
and test selection in a fresh session from root and a scoped directory. Native symlink
support does not make symlinks portable in our package tooling, which rejects them.
No adapter, global installation, permission override or vendor metadata is installed by
this foundation. A new runtime should first demonstrate selected-file loading without
loading every skill or treating its output as approval.

## Visual context loading

For UI and other visual output, follow the explicit path route in
[AGENTS.md](../AGENTS.md) before changing components, layout, fonts, colors or effects:
read [manifest](../design/manifest.json), [DESIGN.md](../design/DESIGN.md),
[tokens](../design/tokens.css), [reference index](../design/references/README.md), the
relevant approved references and existing output. Select the applicable design recipe
from the router. Template/draft/disabled status cannot stand in for an approved visual
baseline; non-visual work does not load this branch.

This instruction-based route is portable to Codex, Cursor and other agents able to read
repository files and SKILL.md. It does not assert native discovery in any editor. Verify
a fresh session can identify these sources before a harmless visual task; also exercise
a non-visual task and confirm it does not invent a design requirement. Test any native
adapter in its own runtime separately. Context lives in Git-versioned project files,
not vendor memory. OpenDesign is not installed or required; a future optional adapter
could map these files without becoming design authority. No adapter/API compatibility
is implemented or claimed here.

## Workflows and permissions

The official workflow guidance uses explicit goals, context, constraints and verification,
with targeted tests and local review. This foundation implements those ideas through
bounded work items and concise result records. A review must inspect actual changes;
an author summary alone is insufficient. [Source: prompting, Codex workflows](https://learn.chatgpt.com/docs/prompting).

Sandbox boundaries and approval policy are separate controls. Effective settings depend
on the environment; do not assume a default is active. Before consequential work,
check allowed paths, network access, credentials and approval behavior. This repository
ships no permission overrides or machine-wide configuration.
[Source: sandboxing](https://learn.chatgpt.com/docs/sandboxing).

## Porting or upgrading the runtime

Verify how the replacement discovers local instructions, scopes overrides and reloads
context. Ask it to identify the loaded sources and summarize applicable boundaries.
Exercise a harmless task from both root and any scoped directory. Confirm real check
commands and effective access controls. Keep decisions in repository files rather than
vendor-only memory. Recheck the dated sources above when relying on exact discovery
behavior; runtime-specific claims do not belong in universal rules.

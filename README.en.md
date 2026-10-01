````markdown
# Project Bootstrap

[Suomi](README.md) · **English**

A reusable foundation for people and AI coding agents to build software together.

Clone or copy this repository when starting a new project, then replace the project context with your own goals, constraints and commands.

Project Bootstrap gives people and AI coding agents shared working rules, 15 task-specific skills and reusable work and review templates.

It is designed for solo builders and teams. It does not require a specific application framework, AI provider or subscription.

Version: [BOOTSTRAP_VERSION](BOOTSTRAP_VERSION)

## What Project Bootstrap does

Project Bootstrap defines:

- who decides what
- what an agent may do independently
- when approval is required
- how work is scoped
- how project context is preserved
- how specifications and architecture decisions are handled
- how implementation is tested
- how work is independently reviewed
- how security is reviewed
- how work is handed off
- how Git operations remain under human control

Without a shared operating model, development can drift into:

prompt → code → more code → context loss → architecture drift → regressions

Project Bootstrap aims for:

idea → clarification → bounded work → implementation → tests → review → human decision authority

## Quick Start

```text
git clone https://github.com/FoxRav/project-bootstrap.git my-project
cd my-project
```
````

1. Clone or copy the foundation into a new project directory.
2. Follow [docs/INITIALIZE.md](docs/INITIALIZE.md), including the new-project Git history guidance.
3. Fill in [docs/PROJECT.md](docs/PROJECT.md): purpose, users, scope and constraints.
4. Define the project's real validation and test commands in [docs/TESTING.md](docs/TESTING.md).
5. Configure people, agents, models and tools in [docs/RUNTIME.md](docs/RUNTIME.md).
6. Start the agent from [AGENTS.md](AGENTS.md).
7. Select only the relevant [skill](skills/README.md). Do not load every skill at once.
8. For non-trivial work, define the task using [WORK_ITEM_TEMPLATE.md](templates/WORK_ITEM_TEMPLATE.md). A short task description is enough for a small, obvious change.

## Workflow and control

Typical workflow:

Idea
→ clarification
→ research or prototype when needed
→ specification
→ architecture / ADR when needed
→ work items
→ implementation and tests
→ independent review
→ Product Owner
→ manual commit and push

This is not a mandatory waterfall. Small changes can skip unnecessary stages, and testing should run throughout implementation.

The Product Owner is the project's decision maker. This may also be a solo developer.

Agents are expected to:

- inspect the current state before editing
- load only the context needed for the task
- stay within the defined scope
- preserve valid tests and quality gates
- request approval for major architecture, security, data-model or public API changes
- leave commits and pushes to the human by default

Non-trivial work should receive independent review before approval.

A review ZIP is an optional handoff artifact, not a normal mandatory step.

See [PROJECT_BOOTSTRAP.md](PROJECT_BOOTSTRAP.md) for the canonical authority and approval rules.

## Repository map

| Location                                                                       | Purpose                                                |
| ------------------------------------------------------------------------------ | ------------------------------------------------------ |
| [AGENTS.md](AGENTS.md)                                                         | Agent entry point, navigation and authority boundaries |
| [PROJECT_BOOTSTRAP.md](PROJECT_BOOTSTRAP.md)                                   | Universal operating policy                             |
| [docs/PROJECT.md](docs/PROJECT.md)                                             | Project-specific facts and knowledge map               |
| [docs/INITIALIZE.md](docs/INITIALIZE.md)                                       | Project initialization                                 |
| [docs/RUNTIME.md](docs/RUNTIME.md)                                             | People, agents, models and tools                       |
| [docs/TESTING.md](docs/TESTING.md)                                             | Validation and test commands                           |
| [docs/SKILL_SOURCES.md](docs/SKILL_SOURCES.md)                                 | Skill sources and provenance                           |
| [skills/README.md](skills/README.md)                                           | Skill selection and usage                              |
| [templates/WORK_ITEM_TEMPLATE.md](templates/WORK_ITEM_TEMPLATE.md)             | Work item template                                     |
| [templates/ADR_TEMPLATE.md](templates/ADR_TEMPLATE.md)                         | Architecture decision template                         |
| [templates/REVIEW_TEMPLATE.md](templates/REVIEW_TEMPLATE.md)                   | Review template                                        |
| [templates/PROJECT_CONTEXT_TEMPLATE.md](templates/PROJECT_CONTEXT_TEMPLATE.md) | Project context template                               |
| [scripts/bootstrap.py](scripts/bootstrap.py)                                   | Bootstrap validation and optional packaging            |
| [tests/test_bootstrap.py](tests/test_bootstrap.py)                             | Bootstrap regression tests                             |

## Skills

A skill is a reusable procedure for one class of work.

Project Bootstrap contains 15 universal skills:

`grill-with-docs` · `grill-me` · `domain-modeling` · `research` · `prototype` · `to-spec` ·
`architecture-review` · `to-tickets` · `implement` · `tdd` · `diagnose-bug` · `code-review` ·
`security-review` · `release-readiness` · `handoff`

Skills do not grant permission to bypass project authority or other rules.

A skill can be loaded directly by file path without installation. Runtime-specific native skill discovery can be configured in [docs/RUNTIME.md](docs/RUNTIME.md#skill-discovery).

Project-specific skills belong with their project.

See [skills/README.md](skills/README.md).

## Validate the foundation

Run from the repository root with Python 3.10+:

```text
python scripts/bootstrap.py check
python -m unittest discover -s tests -v
```

These commands validate the Project Bootstrap foundation itself.

When using the bootstrap for an application project, define that project's own validation commands in [docs/TESTING.md](docs/TESTING.md).

Normal work does not require a ZIP package.

See [docs/TESTING.md](docs/TESTING.md) for commands and optional packaging.

## License

This project is released under the [MIT License](LICENSE).

Skill design provenance: [docs/SKILL_SOURCES.md](docs/SKILL_SOURCES.md).

---

[Suomi](README.md) · **English**

```

```

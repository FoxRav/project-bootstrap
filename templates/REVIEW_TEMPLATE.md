# Review and completion evidence — [work item]

Evidence form, not a second quality policy. Apply
[PROJECT_BOOTSTRAP.md §5](../PROJECT_BOOTSTRAP.md#5-one-quality-and-completion-model).
Embed in the work item/PR or link one durable record. Repair links after copying.
Use only fields applicable to the change, with explicit reasons for omissions.
This evidence record does not require a ZIP, checksum, standalone report or `REVIEW/`
directory. Use the repository/diff directly unless an optional handoff package is useful
under the policy; record its reason and verification only when one is actually selected.

## Identity and outcome

Work/scope: [link]. Date: [timestamp/time zone]. Author: [identity].
Tested state: [commit/base plus dirty diff identity; file inventory/hash if Git is absent].
Environment: [OS, tool versions and relevant configuration; no secrets].
Outcome: [complete / ready for review / blocked / changes required].
Release state: [not requested / pending approval / approved artifact / deployed evidence].

## Acceptance evidence

| Criterion | Observed result and evidence location | Result |
| --- | --- | --- |
| [AC1] | [specific behavior, test or inspected artifact] | [PASS/FAIL/BLOCKED] |

## Executed validation

| Command or exact manual procedure | Cwd | Exit code | Result | Counts/build/warnings |
| --- | --- | --- | --- | --- |
| [exact invocation, including meaningful options] | [path] | [number or N/A] | [PASS/FAIL/BLOCKED/NOT RUN/N/A] | [relevant summary] |

Omitted checks: [which, why, effect on confidence; distinguish N/A from not run].
Baseline failures/flakes: [reproduction, disposition, owner and accepted exception/expiry
if applicable]. Detailed logs: [only useful retained links]. Never convert a missing
tool, failed prerequisite or skipped check into PASS.

## Review

Reviewer/context: [identity and separate context; explicitly say self-review if author].
Reviewed state: [revision/diff/content identity]. Scope: [files/behaviors actually reviewed].

| Finding and severity | Evidence | Resolution or accepted follow-up/owner | Recheck |
| --- | --- | --- | --- |
| [finding, or explicitly none found] | [path/behavior] | [change or disposition] | [result/state] |

Result: [pass / changes required / pending]. Human approvals: [action, approver,
source/date, artifact/scope; pending or N/A where appropriate]. A review is not release
authorization. Recheck affected findings after the final changes.

## Repository and delivery inspection

[Record git status --short, git diff --check, git diff, git diff --cached outcomes;
inspect untracked files explicitly. List intentional generated files, secret-scan/manual
review result and its limits, unrelated pre-existing work, commit/push state, documentation
updates and known limitations. If Git is absent, disclose it and use a file inventory/hash.]

Git handoff: [recommended commit boundaries, proposed message and exact commands when
useful; the Product Owner executes commits/pushes manually. Agents also do not create
tags, rewrite history or merge branches without an explicit current-task override.
Record that override only if actually given; an uncommitted state does not by itself
prevent work-item completion.]

Final content identity: [revision and dirty state, or file inventory/hash; identify any
evidence-only edits since testing]. Optional package: [omit this field unless selected;
reason, artifact identity and checksum verification]. Outstanding work: [none or next action].

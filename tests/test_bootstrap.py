"""Regression tests for link, path and archive failure modes, without external tools."""

import io
from contextlib import redirect_stderr, redirect_stdout
from pathlib import Path
import shutil
import sys
import tempfile
import unittest
import warnings
import zipfile

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
import bootstrap as b


def fixture_directory():
    scratch = b.safe_path(b.ROOT, ".review-cache")
    scratch.mkdir(exist_ok=True)
    return tempfile.TemporaryDirectory(dir=scratch)


class BootstrapTests(unittest.TestCase):
    def setUp(self):
        # Keep all fixtures under the repository, including on Windows.
        self.temp = fixture_directory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)

    def sample(self):
        return {"README.md": b"# Sample\n", "BOOTSTRAP_VERSION": b"2.0.0\n"}

    def seed(self):
        for name in b.SOURCES:
            target = self.root / name
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(b.ROOT / name, target)

    def run_cli(self, *args):
        output = io.StringIO()
        with redirect_stdout(output), redirect_stderr(output):
            code = b.main(list(args), root=self.root)
        return code, output.getvalue()

    def test_normal_check_needs_no_review_artifacts_and_creates_none(self):
        self.seed()
        before = {p.relative_to(self.root) for p in self.root.rglob("*")}
        code, output = self.run_cli("check")
        self.assertEqual(code, 0, output)
        self.assertEqual(before, {p.relative_to(self.root) for p in self.root.rglob("*")})
        self.assertFalse((self.root / "REVIEW").exists())

    def test_stale_review_artifacts_do_not_gate_normal_validation(self):
        self.seed()
        review = self.root / "REVIEW"
        review.mkdir()
        (review / "old-notes.md").write_bytes(b"unreadable historical bytes: \xff")
        (self.root / b.ZIP_NAME).write_bytes(b"stale archive")
        code, output = self.run_cli("check")
        self.assertEqual(code, 0, output)
        self.assertEqual((self.root / b.ZIP_NAME).read_bytes(), b"stale archive")
        self.assertFalse((self.root / b.HASH_NAME).exists())

    def test_explicit_package_creates_directory_without_any_report(self):
        self.seed()
        code, output = self.run_cli("package")
        self.assertEqual(code, 0, output)
        code, output = self.run_cli("verify-package")
        self.assertEqual(code, 0, output)
        with zipfile.ZipFile(self.root / b.ZIP_NAME) as archive:
            self.assertEqual(set(archive.namelist()), set(b.SOURCES) | {b.MANIFEST_NAME})
        self.assertEqual({p.name for p in (self.root / "REVIEW").iterdir()},
                         {Path(name).name for name in b.OUTPUTS})

    def test_verify_missing_optional_package_creates_nothing(self):
        self.seed()
        code, output = self.run_cli("verify-package")
        self.assertEqual(code, 1)
        self.assertIn("Packaging is optional", output)
        self.assertFalse((self.root / "REVIEW").exists())

    def test_only_explicitly_selected_review_notes_are_packaged(self):
        self.seed()
        review = self.root / "REVIEW"
        review.mkdir()
        (review / "notes.md").write_bytes(b"# Review\n[Source](../README.md)\n")
        (review / "private-draft.txt").write_bytes(b"Do not package this draft.\n")
        code, output = self.run_cli("package", "--include-review", "REVIEW/notes.md")
        self.assertEqual(code, 0, output)
        with zipfile.ZipFile(self.root / b.ZIP_NAME) as archive:
            self.assertIn("REVIEW/notes.md", archive.namelist())
            self.assertNotIn("REVIEW/private-draft.txt", archive.namelist())
        code, output = self.run_cli("verify-package", "--include-review", "REVIEW/notes.md")
        self.assertEqual(code, 0, output)
        (review / "notes.md").write_bytes(b"# Changed review\n")
        code, _ = self.run_cli("verify-package", "--include-review", "REVIEW/notes.md")
        self.assertEqual(code, 1)

    def test_review_selection_rejects_unsafe_paths_and_output_files(self):
        self.seed()
        for name in ("README.md", "REVIEW/../README.md", b.MANIFEST_NAME,
                     "REVIEW/source_manifest.sha256.txt",
                     "REVIEW/private.key", "REVIEW/.env.txt",
                     "REVIEW/notes.md:stream.md", "REVIEW/notes\ninjected.md"):
            with self.subTest(name=name):
                code, _ = self.run_cli("package", "--include-review", name)
                self.assertEqual(code, 1)
                self.assertFalse((self.root / "REVIEW").exists())

    def test_case_alias_review_inputs_are_rejected(self):
        self.seed()
        review = self.root / "REVIEW"
        review.mkdir()
        (review / "notes.md").write_bytes(b"# Notes\n")
        code, output = self.run_cli("package", "--include-review", "REVIEW/notes.md",
                                    "--include-review", "REVIEW/NOTES.md")
        self.assertEqual(code, 1)
        self.assertIn("Duplicate review input", output)
        self.assertFalse((self.root / b.ZIP_NAME).exists())

    def test_selected_review_notes_receive_validation(self):
        self.seed()
        review = self.root / "REVIEW"
        review.mkdir()
        notes = review / "notes.md"
        for text in ("# Notes\n[Missing](absent.md)\n", "ghp_" + "a" * 30 + "\n"):
            with self.subTest(text=text):
                notes.write_bytes(text.encode())
                code, _ = self.run_cli("package", "--include-review", "REVIEW/notes.md")
                self.assertEqual(code, 1)
                self.assertFalse((self.root / b.ZIP_NAME).exists())

    def test_relative_links_and_duplicate_heading_fragments(self):
        sources = {
            "README.md": b"# Start\n[doc](docs/file.md#same-1)\n",
            "docs/file.md": b"# Same\n# Same\n[back](../README.md#start)\n",
        }
        self.assertEqual(b.check_links(self.root, sources), 2)

    def test_missing_file_and_fragment_are_rejected(self):
        for target in ("absent.md", "README.md#absent"):
            with self.subTest(target=target), self.assertRaises(ValueError):
                b.check_links(self.root, {"README.md": f"# Present\n[x]({target})\n".encode()})

    def test_outside_workspace_link_is_rejected(self):
        with self.assertRaises(ValueError):
            b.check_links(self.root, {"README.md": b"[x](../private.md)\n"})

    def test_unexpected_file_is_rejected(self):
        self.seed()
        (self.root / "accidental.txt").write_text("private draft\n")
        with self.assertRaisesRegex(ValueError, "unexpected"):
            b.source_snapshot(self.root)

    def test_required_skill_inventory(self):
        expected_general = {
            "grill-with-docs", "grill-me", "domain-modeling", "research", "prototype",
            "to-spec", "architecture-review", "to-tickets", "implement", "tdd",
            "diagnose-bug", "code-review", "security-review", "release-readiness", "handoff",
            "design-brief", "ui-design", "visual-review",
        }
        expected_optional = {
            "webhooks", "system-design", "api-design", "database-engineering",
            "distributed-systems", "application-security", "performance-observability",
            "delivery-engineering", "testing-strategy", "data-engineering", "ai-systems",
            "caching", "concurrency",
        }
        self.assertEqual(set(b.UNIVERSAL_SKILLS), expected_general)
        self.assertEqual(set(b.OPTIONAL_SKILLS), expected_optional)
        self.assertNotIn("webhooks", b.UNIVERSAL_SKILLS)
        self.assertEqual(set(b.ALL_SKILLS), expected_general | expected_optional)
        self.seed()
        sources, _ = b.validate(self.root)
        for skill in expected_general | expected_optional:
            name = f"skills/{skill}/SKILL.md"
            with self.subTest(skill=skill):
                path = self.root / name
                path.unlink()
                with self.assertRaisesRegex(ValueError, "missing"):
                    b.source_snapshot(self.root)
                path.write_bytes(sources[name])
        self.assertEqual(set(b.REFERENCES), {
            "skills/references/programming-principles.md",
            "skills/references/payments.md",
            "skills/references/notifications.md",
            "skills/references/realtime-media.md",
        })
        for name in b.REFERENCES:
            path = self.root / name
            with self.subTest(reference=name):
                path.unlink()
                with self.assertRaisesRegex(ValueError, "missing"):
                    b.source_snapshot(self.root)
                path.write_bytes(sources[name])

    def test_reference_inventory_has_procedure_and_shared_policy_links(self):
        self.seed()
        sources, _ = b.validate(self.root)
        for name in b.REFERENCES:
            with self.subTest(reference=name):
                content = sources[name].decode("utf-8")
                self.assertFalse(content.startswith("---\n"))
                for anchor in (
                    "../README.md#shared-contract",
                    "PROJECT_BOOTSTRAP.md#1-authority-and-evidence",
                    "PROJECT_BOOTSTRAP.md#4-autonomy-and-approval-boundaries",
                    "PROJECT_BOOTSTRAP.md#5-one-quality-and-completion-model",
                    "PROJECT_BOOTSTRAP.md#git-authority",
                    "PROJECT_BOOTSTRAP.md#optional-review-packaging",
                ):
                    self.assertIn(anchor, content)

    def test_reference_policy_rejects_approval_bypass_instruction(self):
        self.seed()
        path = self.root / "skills/references/payments.md"
        original = path.read_bytes()
        path.write_bytes(original + b"\nSkip Product Owner approval for payment schema changes.\n")
        code, output = self.run_cli("check")
        self.assertEqual(code, 1, output)
        self.assertIn("skill policy violation", output)

    def test_reference_structure_rejects_skill_metadata_and_missing_procedure(self):
        self.seed()
        path = self.root / "skills/references/payments.md"
        original = path.read_bytes()
        invalid = (
            (b"---\nname: payments\n---\n" + original, "must not use skill metadata"),
            (original.replace(b"## Procedure", b"## Steps"), "reference headings"),
        )
        for content, expected in invalid:
            with self.subTest(expected=expected):
                path.write_bytes(content)
                code, output = self.run_cli("check")
                self.assertEqual(code, 1, output)
                self.assertIn(expected, output)
        path.write_bytes(original)

    def test_webhooks_skill_is_routed_only_for_webhook_projects(self):
        skill = (b.ROOT / "skills/webhooks/SKILL.md").read_text(encoding="utf-8")
        router = (b.ROOT / "skills/README.md").read_text(encoding="utf-8")
        self.assertIn("webhook", skill.split("## Use when", 1)[1].split("## Do not use when", 1)[0].lower())
        self.assertIn("webhooks/SKILL.md", router)
        self.assertIn("only for webhook projects", router)
        self.assertIn("only", skill.split("## Do not use when", 1)[1].split("## Required context", 1)[0].lower())

    def test_cross_skill_routing_links_remain_present(self):
        routes = {
            "skills/architecture-review/SKILL.md": (
                "../system-design/SKILL.md", "For an architecture design task",
            ),
            "skills/security-review/SKILL.md": (
                "../application-security/SKILL.md", "For a security-control design",
            ),
            "skills/tdd/SKILL.md": (
                "../testing-strategy/SKILL.md", "For a broader risk-based test portfolio",
            ),
            "skills/webhooks/SKILL.md": (
                "../api-design/SKILL.md", "For a broader HTTP API contract",
            ),
        }
        sources = b.source_snapshot(b.ROOT)
        for source, (target, condition) in routes.items():
            with self.subTest(source=source):
                text = sources[source].decode("utf-8")
                self.assertIn(f"]({target})", text)
                self.assertIn(condition, text)
        b.check_links(b.ROOT, sources)

    def test_quality_recipes_keep_security_review_dispositions(self):
        sources = b.source_snapshot(b.ROOT)
        security_review = sources["skills/security-review/SKILL.md"].decode("utf-8")
        application_security = sources["skills/application-security/SKILL.md"].decode("utf-8")
        for required in (
            "Treat each suspected issue as a candidate, not a finding.",
            "Independently validate each material candidate",
            "confirmed",
            "needs validation",
            "rejected",
            "Keep optional hardening separate from confirmed",
            "Do not assign severity to unresolved or rejected candidates.",
            "keep confidence distinct from severity",
        ):
            with self.subTest(required=required):
                self.assertIn(required, security_review)
        self.assertIn("security-review` for independent candidate validation", application_security)

    def test_quality_recipes_separate_review_axes_and_causal_debugging(self):
        sources = b.source_snapshot(b.ROOT)
        code_review = " ".join(
            sources["skills/code-review/SKILL.md"].decode("utf-8").split()
        )
        diagnose_bug = " ".join(
            sources["skills/diagnose-bug/SKILL.md"].decode("utf-8").split()
        )
        for required in (
            "**Requirements conformance:**",
            "**Technical quality:**",
            "A pass in one dimension does not cancel a defect in the other.",
            "observed result",
        ):
            with self.subTest(required=required):
                self.assertIn(required, code_review)
        for required in (
            "exact command/input and observed result",
            "causal chain from triggering conditions",
            "When a verified cause recurs and generalizes",
            "one update to the canonical project guidance",
        ):
            with self.subTest(required=required):
                self.assertIn(required, diagnose_bug)

    def test_frontend_quality_has_responsive_accessibility_and_react_vite_criteria(self):
        sources = b.source_snapshot(b.ROOT)
        ui_design = " ".join(
            sources["skills/ui-design/SKILL.md"].decode("utf-8").split()
        )
        visual_review = sources["skills/visual-review/SKILL.md"].decode("utf-8")
        scenarios = sources["docs/TESTING.md"].decode("utf-8")
        for required in (
            "For a React/Vite project",
            "visible focus",
            "supported narrow and wide layouts",
        ):
            with self.subTest(required=required):
                self.assertIn(required, ui_design)
        for required in (
            "For React/Vite work",
            "text scaling",
            "reduced-motion",
            "NOT RUN or BLOCKED",
        ):
            with self.subTest(required=required):
                self.assertIn(required, visual_review)
        self.assertIn("A React/Vite route or component changes", scenarios)
        self.assertIn("works at runtime", scenarios)

    def test_skill_metadata_rejects_invalid_name_description_and_duplicates(self):
        self.seed()
        path = self.root / "skills/research/SKILL.md"
        original = path.read_text(encoding="utf-8")
        bad_fronts = (
            'name: wrong-name\ndescription: "Research options"',
            'name: research\ndescription: ""',
            'name: research\ndescription: []',
            'name: research\ndescription: unquoted',
            'name: research\ndescription: "a"\ndescription: "b"',
            'name: research\ndescription: "a"\nallowed-tools: unrestricted',
        )
        body = original.split("---\n", 2)[2]
        for front in bad_fronts:
            with self.subTest(front=front):
                path.write_bytes(f"---\n{front}\n---\n{body}".encode())
                self.assertEqual(self.run_cli("check")[0], 1)

    def test_skill_sections_must_exist_and_contain_instructions(self):
        self.seed()
        path = self.root / "skills/research/SKILL.md"
        original = path.read_text(encoding="utf-8")
        variants = (
            original.replace("## Evidence", "## Evidence omitted"),
            original.replace("## Evidence", "## Purpose"),
            original.replace("# research\n", "# unrelated\n"),
            original.split("## Handoff")[0] + "## Handoff\n\n",
            original.replace("1. State", "State"),
            original + "\n[TODO: finish this recipe]\n",
        )
        for variant in variants:
            with self.subTest(variant=variant[-90:]):
                path.write_bytes(variant.encode())
                self.assertEqual(self.run_cli("check")[0], 1)

    def test_fenced_example_cannot_supply_required_skill_heading(self):
        self.seed()
        path = self.root / "skills/research/SKILL.md"
        original = path.read_text(encoding="utf-8")
        path.write_bytes(original.replace("## Evidence\n", "```\n## Evidence\n```\n").encode())
        self.assertEqual(self.run_cli("check")[0], 1)

    def test_entry_points_and_router_must_link_to_skills(self):
        self.seed()
        for source, link in (
            ("AGENTS.md", "skills/README.md"),
            ("PROJECT_BOOTSTRAP.md", "skills/README.md"),
            ("skills/README.md", "research/SKILL.md"),
            ("skills/research/SKILL.md", "../README.md#shared-contract"),
            ("skills/README.md", "../PROJECT_BOOTSTRAP.md#git-authority"),
            ("skills/README.md", "../PROJECT_BOOTSTRAP.md#optional-review-packaging"),
            ("skills/README.md", "../PROJECT_BOOTSTRAP.md#4-autonomy-and-approval-boundaries"),
        ):
            with self.subTest(source=source, link=link):
                path = self.root / source
                original = path.read_bytes()
                path.write_bytes(original.replace(f"({link})".encode(), b"(README.md)"))
                self.assertEqual(self.run_cli("check")[0], 1)
                path.write_bytes(original)

    def test_nested_skill_link_is_checked(self):
        self.seed()
        path = self.root / "skills/diagnose-bug/SKILL.md"
        path.write_bytes(path.read_bytes() + b"\n[Unknown context](../../docs/absent.md)\n")
        code, output = self.run_cli("check")
        self.assertEqual(code, 1)
        self.assertIn("Missing source link", output)

    def test_skill_policy_rejects_unsafe_instruction_fixtures(self):
        self.seed()
        path = self.root / "skills/implement/SKILL.md"
        original = path.read_bytes()
        directives = (
            "Run `git commit -am done`.",
            "When tests pass, execute git push origin main.",
            "Commit your work to the current branch.",
            "Automatically push the branch.",
            "Then create tags for the release.",
            "Bypass Product Owner approval for dependencies.",
            "No approval is required for schema changes.",
            "Always create a review ZIP for every task.",
            "A review package is mandatory before completion.",
            "Do not bypass policy. Then commit the changes.",
            "Never waive approval; run git push.",
        )
        for directive in directives:
            with self.subTest(directive=directive):
                path.write_bytes(original + f"\n{directive}\n".encode())
                code, output = self.run_cli("check")
                self.assertEqual(code, 1, output)
                self.assertIn("skill policy violation", output)

    def test_skill_policy_allows_prohibitions_and_manual_handoff(self):
        for instruction in (
            "Do not run git commit or git push.",
            "Agents must not run git push.",
            "Never bypass Product Owner approval.",
            "The Product Owner performs commits and pushes manually.",
            "Prepare a proposed commit message and manual commands for the owner.",
            "Review packaging is optional and on demand.",
        ):
            with self.subTest(instruction=instruction):
                b.check_skill_policy("fixture", instruction)

    def test_skill_router_and_discovery_description_are_policy_checked(self):
        self.seed()
        router = self.root / "skills/README.md"
        original = router.read_bytes()
        router.write_bytes(original + b"\nAlways create a review ZIP.\n")
        self.assertEqual(self.run_cli("check")[0], 1)
        router.write_bytes(original)
        skill = self.root / "skills/research/SKILL.md"
        body = skill.read_text(encoding="utf-8").split("---\n", 2)[2]
        skill.write_bytes(('---\nname: research\ndescription: "Automatically push the branch."\n'
                           '---\n' + body).encode())
        self.assertEqual(self.run_cli("check")[0], 1)

    def test_legacy_bootstrap_work_record_is_not_canonical_source(self):
        self.seed()
        path = self.root / "docs/WORK/W001-bootstrap-redesign.md"
        path.parent.mkdir(parents=True)
        path.write_bytes(b"# Historical development record\n")
        with self.assertRaisesRegex(ValueError, "unexpected"):
            b.validate(self.root)

    def test_caches_dependencies_and_sensitive_files_are_excluded(self):
        self.seed()
        for directory in (".git", "node_modules", ".venv", ".firecrawl", ".review-cache"):
            folder = self.root / directory
            folder.mkdir()
            (folder / "not-for-package.txt").write_text("excluded\n")
        (self.root / ".env").write_text("PRIVATE=fixture\n")
        (self.root / "private.key").write_text("fixture\n")
        self.assertEqual(set(b.source_snapshot(self.root)), set(b.SOURCES))

    def test_reparse_point_is_rejected(self):
        # Mock filesystem metadata so junction coverage does not need admin privileges.
        from types import SimpleNamespace
        from unittest.mock import patch
        target = self.root / "linked"
        target.mkdir()
        real_lstat = Path.lstat

        def fake_lstat(path):
            if path == target:
                return SimpleNamespace(st_mode=0o40755, st_file_attributes=0x400)
            return real_lstat(path)

        with patch.object(Path, "lstat", fake_lstat), self.assertRaisesRegex(ValueError, "Reparse"):
            b.safe_path(self.root, "linked/data.md")

    def test_reparse_scratch_is_rejected_before_fixture_creation(self):
        from types import SimpleNamespace
        from unittest.mock import patch
        scratch = b.ROOT / ".review-cache"
        real_lstat = Path.lstat

        def fake_lstat(path):
            if path == scratch:
                return SimpleNamespace(st_mode=0o40755, st_file_attributes=0x400)
            return real_lstat(path)

        with patch.object(Path, "lstat", fake_lstat):
            with patch.object(tempfile, "TemporaryDirectory") as create:
                with self.assertRaisesRegex(ValueError, "Reparse"):
                    fixture_directory()
                create.assert_not_called()

    def test_path_traversal_is_rejected(self):
        with self.assertRaises(ValueError):
            b.safe_path(self.root, "../outside.txt")

    def test_archive_is_reproducible_and_complete(self):
        sources = self.sample()
        first = b.archive_bytes(sources)
        self.assertEqual(first, b.archive_bytes(dict(reversed(list(sources.items())))))
        b.verify_archive(first, sources)
        with zipfile.ZipFile(io.BytesIO(first)) as archive:
            self.assertEqual(set(archive.namelist()), set(sources) | {b.MANIFEST_NAME})

    def test_changed_source_invalidates_archive(self):
        sources = self.sample()
        archive = b.archive_bytes(sources)
        sources["README.md"] = b"# Changed\n"
        with self.assertRaises(ValueError):
            b.verify_archive(archive, sources)

    def test_extra_archive_entry_is_rejected(self):
        stream = io.BytesIO(b.archive_bytes(self.sample()))
        with zipfile.ZipFile(stream, "a") as archive:
            archive.writestr("../outside.txt", "unexpected")
        with self.assertRaises(ValueError):
            b.verify_archive(stream.getvalue(), self.sample())

    def test_duplicate_archive_entry_is_rejected(self):
        stream = io.BytesIO(b.archive_bytes(self.sample()))
        with warnings.catch_warnings():
            warnings.simplefilter("ignore", UserWarning)
            with zipfile.ZipFile(stream, "a") as archive:
                archive.writestr("README.md", b"# Sample\n")
        with self.assertRaisesRegex(ValueError, "inventory"):
            b.verify_archive(stream.getvalue(), self.sample())

    def test_same_size_archive_tampering_is_rejected(self):
        expected = self.sample()
        altered = dict(expected)
        altered["README.md"] = b"# Tamper\n"
        self.assertEqual(len(altered["README.md"]), len(expected["README.md"]))
        with self.assertRaises(ValueError):
            b.verify_archive(b.archive_bytes(altered), expected)

    def test_oversized_archive_entry_is_rejected_before_decompression(self):
        from unittest.mock import patch
        expected = self.sample()
        altered = dict(expected)
        altered["README.md"] = b"x" * 100_000
        with patch.object(zipfile.ZipFile, "testzip", side_effect=AssertionError("Too late")):
            with self.assertRaisesRegex(ValueError, "size differs"):
                b.verify_archive(b.archive_bytes(altered), expected)

    def test_checksum_tampering_is_rejected(self):
        sources = self.sample()
        data = b.archive_bytes(sources)
        (self.root / "REVIEW").mkdir()
        (self.root / b.ZIP_NAME).write_bytes(data)
        (self.root / b.HASH_NAME).write_bytes(b"0" * 64 + b"  PROJECT_BOOTSTRAP_REVIEW.zip\n")
        (self.root / b.MANIFEST_NAME).write_bytes(b.manifest_bytes(sources))
        with self.assertRaisesRegex(ValueError, "SHA-256"):
            b.verify_package(self.root, sources)

    def test_credential_pattern_is_rejected_without_printing_value(self):
        self.seed()
        token = "ghp_" + "a" * 30
        with (self.root / "README.md").open("a", encoding="utf-8", newline="\n") as handle:
            handle.write(token + "\n")
        with self.assertRaisesRegex(ValueError, "Potential credential") as caught:
            b.validate(self.root)
        self.assertNotIn(token, str(caught.exception))


if __name__ == "__main__":
    unittest.main()

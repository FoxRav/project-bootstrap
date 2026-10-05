"""Design scaffold and explicit binary-source regression tests, standard library only."""

import io
import json
from pathlib import Path
import shutil
import unittest
import zipfile
import zlib

from test_bootstrap import b, fixture_directory


class DesignTests(unittest.TestCase):
    def setUp(self):
        temp = fixture_directory()
        self.addCleanup(temp.cleanup)
        self.root = Path(temp.name)
        for name in b.SOURCES:
            target = self.root / name
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(b.ROOT / name, target)

    def manifest(self, **changes):
        path = self.root / "design/manifest.json"
        value = json.loads(path.read_bytes())
        value.update(changes)
        path.write_bytes((json.dumps(value, indent=2) + "\n").encode())

    def test_unconfigured_disabled_and_draft_paths_need_no_product_brief(self):
        original = (self.root / "design/DESIGN.md").read_bytes()
        for status in ("template", "disabled", "draft"):
            with self.subTest(status=status):
                self.manifest(status=status)
                b.validate(self.root)
                self.assertEqual((self.root / "design/DESIGN.md").read_bytes(), original)
                self.assertFalse((self.root / "REVIEW").exists())

    def test_active_identity_is_required_but_validation_is_not_approval(self):
        self.manifest(status="active")
        with self.assertRaisesRegex(ValueError, "project identity"):
            b.validate(self.root)
        self.manifest(id="fleet-console", name="Fleet Console")
        # Structural validation cannot attest to product decisions in prose.
        b.validate(self.root)

    def test_manifest_rejects_invalid_json_duplicates_and_nonobject(self):
        path = self.root / "design/manifest.json"
        for value in (b"{\n", b"[]\n", b'{"status":"draft","status":"active"}\n'):
            with self.subTest(value=value), self.assertRaises(ValueError):
                path.write_bytes(value)
                b.validate(self.root)

    def test_manifest_rejects_unknown_fields_schema_status_and_empty_identity(self):
        path = self.root / "design/manifest.json"
        original = path.read_bytes()
        for changes in ({"schemaVersion": "vendor/v2"}, {"status": "approved"},
                        {"name": " "}, {"id": None}, {"extra": True}):
            with self.subTest(changes=changes), self.assertRaises(ValueError):
                path.write_bytes(original)
                self.manifest(**changes)
                b.validate(self.root)

    def test_manifest_cannot_redirect_authority_outside_canonical_paths(self):
        for field in b.DESIGN_PATHS:
            for target in ("../AGENTS.md", "/DESIGN.md", "C:/private", "other.md",
                           "https://example.org/remote", "assets/../DESIGN.md"):
                with self.subTest(field=field, target=target):
                    self.manifest(**{field: target})
                    with self.assertRaisesRegex(ValueError, "manifest path"):
                        b.validate(self.root)
                    self.manifest(**{field: b.DESIGN_PATHS[field]})

    def test_missing_design_sources_fail_in_every_activation_state(self):
        path = self.root / "design/DESIGN.md"
        path.unlink()
        for status in ("template", "disabled", "draft", "active"):
            with self.subTest(status=status), self.assertRaisesRegex(ValueError, "missing"):
                self.manifest(status=status)
                b.validate(self.root)

    def test_required_design_sections_cannot_be_removed_or_hidden_in_code(self):
        path = self.root / "design/DESIGN.md"
        original = path.read_bytes()
        for replacement in (b"## Unrelated", b"```\n## Design DNA\n```"):
            with self.subTest(replacement=replacement):
                path.write_bytes(original.replace(b"## Design DNA", replacement))
                with self.assertRaisesRegex(ValueError, "Design DNA"):
                    b.validate(self.root)

    def test_missing_empty_duplicate_and_dangling_tokens_fail(self):
        text = (self.root / "design/tokens.css").read_text(encoding="utf-8")
        mutations = (
            text.replace("--font-body: Arial, sans-serif;", ""),
            text.replace("--font-body: Arial, sans-serif;", "--font-body: ;"),
            text.replace("--font-body: Arial, sans-serif;", "--font-body: ...;"),
            text.replace("--font-body: Arial, sans-serif;", "--font-body: Arial; --font-body: serif;"),
            text.replace("var(--space-lg)", "var(--space-missing)"),
        )
        for index, value in enumerate(mutations):
            with self.subTest(index=index), self.assertRaises(ValueError):
                b.check_tokens(value)

    def test_token_cycles_fail_and_shared_aliases_pass(self):
        text = (self.root / "design/tokens.css").read_text(encoding="utf-8")
        b.check_tokens(text.replace("--space-sm: 0.5rem", "--space-sm: var(--space-xs)"))
        cycle = text.replace("--space-sm: 0.5rem", "--space-sm: var(--space-xs)")
        cycle = cycle.replace("--space-xs: 0.25rem", "--space-xs: var(--space-sm)")
        with self.assertRaisesRegex(ValueError, "Cyclic"):
            b.check_tokens(cycle)

    def test_canonical_token_subset_rejects_unparsed_declarations(self):
        text = (self.root / "design/tokens.css").read_text(encoding="utf-8")
        for value in (text + "body { color: red; }\n", text.replace(":root", "body"),
                      text.replace("#20231f1a;", "#20231f1a")):
            with self.subTest(value=value[-50:]), self.assertRaises(ValueError):
                b.check_tokens(value)

    def test_visual_entry_points_must_link_design_context(self):
        path = self.root / "AGENTS.md"
        path.write_bytes(path.read_bytes().replace(b"(design/tokens.css)", b"(design/DESIGN.md)"))
        with self.assertRaisesRegex(ValueError, "integration link"):
            b.validate(self.root)

    def test_binary_image_and_empty_directory_survive_optional_archive_exactly(self):
        sources, _ = b.validate(self.root)
        archive = b.archive_bytes(sources)
        b.verify_archive(archive, sources)
        with zipfile.ZipFile(io.BytesIO(archive)) as zipped:
            self.assertEqual(zipped.read("design/assets/.gitkeep"), b"")
            self.assertEqual(zipped.read("docs/assets/project-bootstrap-hero.png"),
                             (b.ROOT / "docs/assets/project-bootstrap-hero.png").read_bytes())

    def test_png_rejects_corruption_truncation_and_appended_content(self):
        data = (self.root / "docs/assets/project-bootstrap-hero.png").read_bytes()
        corrupt = bytearray(data)
        corrupt[20] ^= 1
        for value in (b"not an image", bytes(corrupt), data[:-1], data + b"hidden"):
            with self.subTest(size=len(value)), self.assertRaisesRegex(ValueError, "PNG"):
                b.check_png("image.png", value)

    def test_png_requires_header_pixel_chunk_and_ending_even_with_valid_crcs(self):
        def chunk(kind, payload=b""):
            return (len(payload).to_bytes(4, "big") + kind + payload
                    + zlib.crc32(kind + payload).to_bytes(4, "big"))

        header = chunk(b"IHDR", b"\0\0\0\1" * 2 + b"\x08\x02\0\0\0")
        for chunks in (chunk(b"IEND"), header + chunk(b"IEND"),
                       header + chunk(b"IDAT"), header + header + chunk(b"IDAT") + chunk(b"IEND")):
            with self.subTest(size=len(chunks)), self.assertRaises(ValueError):
                b.check_png("image.png", b"\x89PNG\r\n\x1a\n" + chunks)

    def test_binary_exceptions_cannot_bypass_text_or_inventory_checks(self):
        path = self.root / "design/assets/.gitkeep"
        path.write_bytes(b"hidden data\n")
        with self.assertRaisesRegex(ValueError, "placeholder must be empty"):
            b.validate(self.root)
        path.write_bytes(b"")
        (self.root / "README.md").write_bytes(b"\xff\n")
        with self.assertRaises(UnicodeError):
            b.validate(self.root)
        (self.root / "design/assets/unlisted.png").write_bytes(b"\x89PNG\r\n\x1a\n")
        with self.assertRaisesRegex(ValueError, "unexpected"):
            b.source_snapshot(self.root)


if __name__ == "__main__":
    unittest.main()

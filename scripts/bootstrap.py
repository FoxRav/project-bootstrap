"""Validate this canonical template. Python 3.10+, standard library only.

Normal validation is `check`; no review report, ZIP or checksum is required or created.
`package` and `verify-package` are optional, explicitly invoked review/handoff operations
under PROJECT_BOOTSTRAP.md. They are not per-work-item, commit, feature or development
gates. Optional notes are selected with --include-review on both package commands.
The source inventory fails closed. Adapt or remove this maintenance utility when
copying the bootstrap into an application repository.
"""

from __future__ import annotations

import argparse
import ast
import hashlib
import io
import json
import os
from pathlib import Path
import re
import stat
import sys
from urllib.parse import unquote, urlsplit
import zipfile


ROOT = Path(__file__).resolve().parents[1]
UNIVERSAL_SKILLS = (
    "grill-with-docs", "grill-me", "domain-modeling", "research", "prototype",
    "to-spec", "architecture-review", "to-tickets", "implement", "tdd",
    "diagnose-bug", "code-review", "security-review", "release-readiness", "handoff",
)
SKILL_HEADINGS = (
    "Purpose", "Use when", "Do not use when", "Required context", "Inputs", "Process",
    "Decision points", "Approval boundaries", "Outputs", "Completion criteria",
    "Evidence", "Handoff",
)
SOURCES = tuple(sorted((
    ".gitattributes", ".gitignore", "AGENTS.md", "BOOTSTRAP_VERSION",
    "CHANGELOG.md", "LICENSE", "PROJECT_BOOTSTRAP.md", "README.md",
    "docs/INITIALIZE.md", "docs/PROJECT.md", "docs/RUNTIME.md", "docs/TESTING.md",
    "docs/SKILL_SOURCES.md", "skills/README.md",
    "templates/ADR_TEMPLATE.md",
    "templates/PROJECT_CONTEXT_TEMPLATE.md", "templates/REVIEW_TEMPLATE.md",
    "templates/WORK_ITEM_TEMPLATE.md", "scripts/bootstrap.py",
    "tests/test_bootstrap.py",
) + tuple(f"skills/{name}/SKILL.md" for name in UNIVERSAL_SKILLS)))
ZIP_NAME = "REVIEW/PROJECT_BOOTSTRAP_REVIEW.zip"
HASH_NAME = "REVIEW/PROJECT_BOOTSTRAP_REVIEW.sha256.txt"
MANIFEST_NAME = "REVIEW/SOURCE_MANIFEST.sha256.txt"
OUTPUTS = {ZIP_NAME, HASH_NAME, MANIFEST_NAME}
EXCLUDED_DIRS = {
    ".git", ".firecrawl", ".review-cache", ".cache", ".pytest_cache",
    "__pycache__", ".venv", "venv", "env", "node_modules", "dist", "build",
}
LINK = re.compile(r"\[[^\]\n]+\]\(([^)\n]+)\)")
SECRET_PATTERNS = (
    re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----"),
    re.compile(r"\b(?:ghp_|github_pat_)[A-Za-z0-9_]{20,}\b"),
    re.compile(r"\bAKIA[A-Z0-9]{16}\b"),
    re.compile(r"\bsk-(?:proj-)?[A-Za-z0-9_-]{32,}\b"),
)


def digest(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def safe_path(root: Path, relative: str) -> Path:
    """Reject traversal, symlinks and Windows junction/reparse points."""
    root = root.resolve()
    path = root / relative
    if Path(relative).is_absolute() or ".." in Path(relative).parts:
        raise ValueError(f"Unsafe path: {relative}")
    for part in (path, *path.parents):
        if part == root:
            break
        if part.is_symlink():
            raise ValueError(f"Linked path is not allowed: {relative}")
        if part.exists():
            attrs = getattr(part.lstat(), "st_file_attributes", 0)
            if attrs & getattr(stat, "FILE_ATTRIBUTE_REPARSE_POINT", 0x400):
                raise ValueError(f"Reparse point is not allowed: {relative}")
    if not path.resolve().is_relative_to(root):
        raise ValueError(f"Path escapes repository: {relative}")
    return path


def ignored_file(name: str) -> bool:
    return (name in {".DS_Store", "Thumbs.db", ".env"}
            or name.startswith(".env.")
            or name.endswith((".pyc", ".pyo", ".pem", ".key", ".tmp")))


def source_snapshot(root: Path) -> dict[str, bytes]:
    """Inventory canonical source; never read optional review artifacts or caches."""
    root = root.resolve()
    found = set()
    for directory, dirs, files in os.walk(root, followlinks=False):
        dirs[:] = sorted(d for d in dirs if d not in EXCLUDED_DIRS)
        if Path(directory) == root and "REVIEW" in dirs:
            dirs.remove("REVIEW")
        for name in dirs:
            safe_path(root, (Path(directory) / name).relative_to(root).as_posix())
        for name in files:
            relative = (Path(directory) / name).relative_to(root).as_posix()
            if relative in OUTPUTS or ignored_file(name):
                continue
            safe_path(root, relative)
            found.add(relative)
    missing, unexpected = set(SOURCES) - found, found - set(SOURCES)
    if missing or unexpected:
        raise ValueError(f"Source inventory mismatch; missing={sorted(missing)}, "
                         f"unexpected={sorted(unexpected)}")
    return {name: safe_path(root, name).read_bytes() for name in SOURCES}


def heading_ids(markdown: str) -> set[str]:
    identifiers, counts = set(), {}
    in_fence = False
    for line in markdown.splitlines():
        if line.startswith("```"):
            in_fence = not in_fence
        if in_fence or not re.match(r"^#{1,6} ", line):
            continue
        heading = re.sub(r"^#+\s+", "", line).strip().lower()
        base = re.sub(r"[^\w\- ]", "", heading).replace(" ", "-")
        count = counts.get(base, 0)
        identifiers.add(base if count == 0 else f"{base}-{count}")
        counts[base] = count + 1
    return identifiers


def check_links(root: Path, sources: dict[str, bytes]) -> int:
    checked = 0
    for name, data in sources.items():
        if not name.endswith(".md"):
            continue
        # The maintained documents use inline links and ATX headings only.
        markdown = re.sub(r"```.*?```", "", data.decode("utf-8"), flags=re.S)
        for raw in LINK.findall(markdown):
            target = raw.strip().strip("<>")
            parsed = urlsplit(target)
            if parsed.scheme in {"https", "http", "mailto"}:
                continue  # External availability requires separate source research.
            if parsed.scheme or parsed.netloc or parsed.query:
                raise ValueError(f"Unsupported link in {name}: {target}")
            path_text = unquote(parsed.path)
            path = ((root / name).parent / path_text) if path_text else root / name
            resolved = path.resolve()
            if not resolved.is_relative_to(root.resolve()):
                raise ValueError(f"Link escapes repository in {name}: {target}")
            relative = resolved.relative_to(root.resolve()).as_posix()
            # Links must point to validated sources, never local scratch evidence.
            if relative not in sources:
                raise ValueError(f"Missing source link in {name}: {target}")
            if parsed.fragment:
                if not relative.endswith(".md"):
                    raise ValueError(f"Fragment on non-Markdown source: {target}")
                if unquote(parsed.fragment) not in heading_ids(sources[relative].decode("utf-8")):
                    raise ValueError(f"Missing heading in {name}: {target}")
            checked += 1
    return checked


def check_skill_policy(name: str, text: str) -> None:
    """Catch common unsafe directives, not arbitrary natural-language policy drift.

    Semantic review is still required. Check clauses separately so a prohibition in
    one sentence cannot hide an unsafe instruction in the next. Never execute text.
    """
    plain = re.sub(r"[`*_]", "", text)
    plain = re.sub(r"^\s*(?:\d+\.|[-+])\s+", "", plain, flags=re.M)
    clauses = re.split(r"(?<=[.!?;])\s+|\n\s*\n", plain)
    hazards = (
        r"(?:^|\b(?:run|execute)\s+)(?:git\s+(?:commit|push|tag|merge|rebase|reset))\b",
        r"\b(?:automatically|always|then|must|should)\s+(?:commit|push)\b",
        r"^(?:commit|push)\b.{0,60}\b(?:work|changes|branch|code)\b",
        r"\b(?:automatically|always|then|must)\s+(?:create tags|merge branches|rewrite (?:git )?history)\b",
        r"\b(?:skip|bypass|waive|ignore)\s+(?:the\s+)?(?:product owner\s+)?(?:approvals?|policy|quality gates?)\b",
        r"\b(?:no\s+(?:product owner\s+)?approval\s+(?:is\s+)?(?:needed|required)|without\s+(?:product owner\s+)?approval)\b",
        r"\b(?:zip|review package)\b.{0,60}\b(?:mandatory|required|must)\b",
        r"\b(?:always|must|require|mandatory)\b.{0,60}\b(?:zip|review package)\b",
    )
    for clause in clauses:
        clause = " ".join(clause.split()).lower()
        # Only a leading prohibition negates a directive. Mixed instructions still
        # need human review; the validator deliberately makes no semantic guarantee.
        if re.match(r"^(?:(?:agents?|you)\s+)?(?:do not|must not|never|cannot)\b", clause):
            continue
        if any(re.search(pattern, clause) for pattern in hazards):
            raise ValueError(f"Potential skill policy violation in {name}; inspect directive")


def check_skills(root: Path, sources: dict[str, bytes]) -> None:
    """Validate the deliberately small, dependency-free canonical skill format."""
    def require_link(source: str, target: str) -> None:
        expected = (root / target.split("#", 1)[0]).resolve()
        fragment = target.partition("#")[2]
        for raw in LINK.findall(sources[source].decode("utf-8")):
            parsed = urlsplit(raw.strip().strip("<>"))
            if parsed.scheme or parsed.netloc or parsed.query:
                continue
            path = ((root / source).parent / unquote(parsed.path)).resolve()
            if path == expected and unquote(parsed.fragment) == fragment:
                return
        raise ValueError(f"Missing skill integration link in {source}: {target}")

    require_link("AGENTS.md", "skills/README.md")
    require_link("PROJECT_BOOTSTRAP.md", "skills/README.md")
    check_skill_policy("skills/README.md", sources["skills/README.md"].decode("utf-8"))
    for anchor in ("1-authority-and-evidence", "4-autonomy-and-approval-boundaries",
                   "5-one-quality-and-completion-model", "git-authority",
                   "optional-review-packaging"):
        require_link("skills/README.md", f"PROJECT_BOOTSTRAP.md#{anchor}")
    for skill in UNIVERSAL_SKILLS:
        name = f"skills/{skill}/SKILL.md"
        if name not in sources:
            raise ValueError(f"Missing universal skill: {name}")
        text = sources[name].decode("utf-8")
        front = re.match(r"\A---\n(.*?)\n---\n", text, re.S)
        if not front:
            raise ValueError(f"Missing skill frontmatter: {name}")
        fields = {}
        for line in front[1].splitlines():
            key, sep, value = line.partition(": ")
            if not sep or key not in {"name", "description"} or key in fields:
                raise ValueError(f"Invalid canonical skill metadata: {name}")
            fields[key] = value
        if fields.get("name") != skill:
            raise ValueError(f"Skill name must match its folder: {name}")
        try:
            description = json.loads(fields.get("description", ""))
        except (ValueError, TypeError) as exc:
            raise ValueError(f"Skill description must be a quoted single-line string: {name}") from exc
        if (not isinstance(description, str) or not description.strip()
                or len(description) > 1024 or any(c in description for c in "<>\n\r")):
            raise ValueError(f"Invalid skill description: {name}")
        body = text[front.end():]
        if not re.match(rf"\n# {re.escape(skill)}\n", body):
            raise ValueError(f"Skill title must match its name: {name}")
        # Fenced examples cannot substitute for required instructions.
        visible = re.sub(r"```.*?```|~~~.*?~~~", "", body, flags=re.S)
        parts = re.split(r"^## ([^\n]+)\n", visible, flags=re.M)
        if tuple(parts[1::2]) != SKILL_HEADINGS:
            raise ValueError(f"Missing, duplicate or out-of-order skill headings: {name}")
        sections = dict(zip(parts[1::2], parts[2::2]))
        if any(not section.strip() for section in sections.values()):
            raise ValueError(f"Empty skill section: {name}")
        if not re.search(r"^1\. \S", sections["Process"], re.M):
            raise ValueError(f"Skill needs an ordered process: {name}")
        if re.search(r"\[TODO(?::|\])", body, re.I):
            raise ValueError(f"Unfinished skill placeholder: {name}")
        require_link(name, "skills/README.md#shared-contract")
        require_link("skills/README.md", name)
        check_skill_policy(name, description + "\n\n" + body)


def validate(root: Path, review_files: tuple[str, ...] = ()) -> tuple[dict[str, bytes], int]:
    sources = source_snapshot(root)
    for requested in review_files:
        path = Path(requested)
        name = path.as_posix()
        if (not path.parts or path.parts[0] != "REVIEW"
                or path.suffix not in {".md", ".txt"}
                or name.casefold() in {output.casefold() for output in OUTPUTS}
                or ignored_file(path.name)):
            raise ValueError("Optional review inputs must be .md/.txt notes under REVIEW/, not outputs")
        if any(re.search(r'[<>:"|?*\\\x00-\x1f]', part) or part.endswith((" ", "."))
               for part in path.parts):
            raise ValueError("Review input path must not contain nonportable characters or aliases")
        if name.casefold() in {source.casefold() for source in sources}:
            raise ValueError(f"Duplicate review input: {name}")
        sources[name] = safe_path(root, name).read_bytes()
    for name, data in sources.items():
        text = data.decode("utf-8")
        if text.startswith("\ufeff") or "\r" in text or not text.endswith("\n"):
            raise ValueError(f"Require UTF-8 without BOM, LF and final newline: {name}")
        if any(line.rstrip() != line for line in text.splitlines()):
            raise ValueError(f"Trailing whitespace: {name}")
        if re.search(r"^(?:<{7}|={7}|>{7})(?: |$)", text, re.M):
            raise ValueError(f"Merge marker: {name}")
        if any(pattern.search(text) for pattern in SECRET_PATTERNS):
            raise ValueError(f"Potential credential in {name}; inspect locally, do not print")
        if name.endswith(".py"):
            ast.parse(text, filename=name)
    version = sources["BOOTSTRAP_VERSION"].decode().strip()
    if not re.fullmatch(r"\d+\.\d+\.\d+", version):
        raise ValueError("BOOTSTRAP_VERSION must contain MAJOR.MINOR.PATCH")
    if not re.search(rf"^## {re.escape(version)} — \d{{4}}-\d{{2}}-\d{{2}}$",
                     sources["CHANGELOG.md"].decode(), re.M):
        raise ValueError("Current version needs a dated changelog entry")
    if len(sources["AGENTS.md"]) > 5000:
        raise ValueError("AGENTS.md exceeds the template's 5,000-byte entry-point budget")
    check_skills(root, sources)
    return sources, check_links(root, sources)


def manifest_bytes(sources: dict[str, bytes]) -> bytes:
    return "".join(f"{digest(data)}  {name}\n" for name, data in sorted(sources.items())).encode()


def archive_bytes(sources: dict[str, bytes]) -> bytes:
    payload = dict(sources)
    payload[MANIFEST_NAME] = manifest_bytes(sources)
    stream = io.BytesIO()
    with zipfile.ZipFile(stream, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=9) as archive:
        for name, data in sorted(payload.items()):
            entry = zipfile.ZipInfo(name, date_time=(2026, 1, 1, 0, 0, 0))
            entry.create_system = 3
            entry.external_attr = 0o100644 << 16
            entry.compress_type = zipfile.ZIP_DEFLATED
            archive.writestr(entry, data, compresslevel=9)
    return stream.getvalue()


def verify_archive(data: bytes, sources: dict[str, bytes]) -> None:
    """Check names/duplicates and every byte without extracting an archive."""
    expected = dict(sources)
    expected[MANIFEST_NAME] = manifest_bytes(sources)
    with zipfile.ZipFile(io.BytesIO(data)) as archive:
        names = archive.namelist()
        if len(names) != len(set(names)) or set(names) != set(expected):
            raise ValueError("Archive inventory differs from reviewed sources")
        for name, content in expected.items():
            if archive.getinfo(name).file_size != len(content):
                raise ValueError(f"Archive size differs: {name}")
        if archive.testzip() is not None:
            raise ValueError("Archive CRC validation failed")
        for name, content in expected.items():
            if archive.read(name) != content:
                raise ValueError(f"Archive content differs: {name}")


def checksum_bytes(data: bytes) -> bytes:
    return f"{digest(data)}  {Path(ZIP_NAME).name}\n".encode()


def verify_package(root: Path, sources: dict[str, bytes]) -> str:
    archive_path = safe_path(root, ZIP_NAME)
    if not archive_path.exists():
        raise ValueError("No review package exists. Packaging is optional; invoke package only for a selected review/handoff")
    data = archive_path.read_bytes()
    if safe_path(root, HASH_NAME).read_bytes() != checksum_bytes(data):
        raise ValueError("ZIP SHA-256 sidecar mismatch")
    if safe_path(root, MANIFEST_NAME).read_bytes() != manifest_bytes(sources):
        raise ValueError("Source manifest differs from current sources")
    verify_archive(data, sources)
    return digest(data)


def create_package(root: Path, sources: dict[str, bytes]) -> None:
    """Explicit optional operation; safely create the output directory on demand."""
    data = archive_bytes(sources)
    verify_archive(data, sources)
    # Preflight every destination before creating the directory or writing outputs.
    outputs = {name: safe_path(root, name) for name in OUTPUTS}
    safe_path(root, "REVIEW").mkdir(exist_ok=True)
    outputs[MANIFEST_NAME].write_bytes(manifest_bytes(sources))
    outputs[ZIP_NAME].write_bytes(data)
    outputs[HASH_NAME].write_bytes(checksum_bytes(data))


def main(argv: list[str] | None = None, root: Path = ROOT) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest="command", required=True)
    commands.add_parser("check", help="normal source validation; no review artifacts needed or created")
    for command, description in (
        ("package", "optional: create a selected review/handoff ZIP and SHA-256"),
        ("verify-package", "optional: verify an existing package against current source"),
    ):
        subparser = commands.add_parser(command, help=description, description=description)
        subparser.add_argument("--include-review", action="append", default=[], metavar="PATH",
                               help="include a selected .md/.txt note under REVIEW/; repeat as needed")
    args = parser.parse_args(argv)
    try:
        sources, links = validate(root, tuple(getattr(args, "include_review", ())))
        print(f"PASS: {len(sources)} source files; {links} local links/fragments; "
              f"{len(UNIVERSAL_SKILLS)} skills; version, text hygiene, Python syntax "
              "and bounded credential/policy scans")
        if args.command == "package":
            create_package(root, sources)
        if args.command != "check":
            sha = verify_package(root, sources)
            print(f"PASS: {len(sources) + 1} ZIP entries; CRC, source bytes, manifest and SHA-256")
            print(f"SHA-256: {sha}")
        return 0
    except (ValueError, OSError, UnicodeError, SyntaxError, zipfile.BadZipFile) as exc:
        print(f"FAIL: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())

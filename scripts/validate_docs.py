#!/usr/bin/env python3
"""Validate article metadata, local Markdown links, and Agent Skills wrappers."""

from __future__ import annotations

import re
import sys
from datetime import date
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
ARTICLE_FIELDS = (
    "title",
    "summary",
    "status",
    "last_updated",
    "last_verified",
    "vendors",
    "tags",
)
ALLOWED_STATUSES = {"current", "needs-review", "archived"}
LINK_PATTERN = re.compile(r"(?<!!)\[[^]]+\]\(([^)]+)\)")


def frontmatter(text: str, path: Path) -> tuple[dict[str, str], list[str]]:
    errors: list[str] = []
    if not text.startswith("---\n"):
        return {}, [f"{path}: отсутствует YAML frontmatter"]

    end = text.find("\n---\n", 4)
    if end == -1:
        return {}, [f"{path}: frontmatter не закрыт"]

    values: dict[str, str] = {}
    for line in text[4:end].splitlines():
        match = re.match(r"^([a-z_][a-z0-9_-]*):\s*(.*)$", line)
        if match:
            values[match.group(1)] = match.group(2).strip().strip('"')
    return values, errors


def validate_date(value: str, path: Path, field: str) -> list[str]:
    try:
        date.fromisoformat(value)
    except ValueError:
        return [f"{path}: {field} должен иметь формат YYYY-MM-DD"]
    return []


def validate_links(text: str, path: Path) -> list[str]:
    errors: list[str] = []
    for target in LINK_PATTERN.findall(text):
        clean = target.split("#", 1)[0]
        if not clean or clean.startswith(("http://", "https://", "mailto:")):
            continue
        resolved = (path.parent / clean).resolve()
        if not resolved.exists():
            errors.append(f"{path}: локальная ссылка не найдена: {target}")
    return errors


def validate_article(path: Path) -> list[str]:
    text = path.read_text(encoding="utf-8")
    values, errors = frontmatter(text, path)
    for field in ARTICLE_FIELDS:
        if field not in values:
            errors.append(f"{path}: отсутствует поле {field}")

    if values.get("status") not in ALLOWED_STATUSES:
        errors.append(f"{path}: недопустимый status: {values.get('status', '')}")

    for field in ("last_updated", "last_verified"):
        if values.get(field):
            errors.extend(validate_date(values[field], path, field))

    if "## Источники" not in text:
        errors.append(f"{path}: отсутствует раздел Источники")
    errors.extend(validate_links(text, path))
    return errors


def validate_skill(path: Path) -> list[str]:
    text = path.read_text(encoding="utf-8")
    values, errors = frontmatter(text, path)
    name = values.get("name", "")
    description = values.get("description", "")

    if name != path.parent.name:
        errors.append(f"{path}: name должен совпадать с именем каталога")
    if not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", name):
        errors.append(f"{path}: некорректное имя скилла")
    if not 1 <= len(description) <= 1024:
        errors.append(f"{path}: description должен содержать от 1 до 1024 символов")
    errors.extend(validate_links(text, path))
    return errors


def main() -> int:
    errors: list[str] = []
    for path in sorted((ROOT / "docs").rglob("*.md")):
        errors.extend(validate_article(path))

    for skill_root in (ROOT / ".agents" / "skills", ROOT / ".claude" / "skills"):
        for path in sorted(skill_root.glob("*/SKILL.md")):
            errors.extend(validate_skill(path))

    for path in sorted(ROOT.rglob("*.md")):
        if ".git" not in path.parts:
            errors.extend(validate_links(path.read_text(encoding="utf-8"), path))

    if errors:
        print("Validation failed:")
        for error in sorted(set(errors)):
            print(f"- {error}")
        return 1

    print("Validation passed")
    return 0


if __name__ == "__main__":
    sys.exit(main())

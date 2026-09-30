# Refresh an AI document

## Outcome

Audit an entire article against current primary sources, update changed information, and advance
`last_verified` only after a complete check.

## Workflow

1. Identify the article unambiguously. If several files match, show them to the user and stop.
2. List its substantive time-sensitive claims and the sources supporting them.
3. Reopen every primary source. Verify what it says, not merely whether its URL still works.
4. For a missing page, find a current official replacement or mark the related claim unverified.
5. Classify findings as confirmed, changed, unverified, or source replaced.
6. Show the user the proposed changes and wait for explicit approval.
7. Update the article, links, `last_updated`, status, and source verification dates.
8. Advance `last_verified` only if every substantive claim was verified.
9. If a full check is impossible, preserve the previous `last_verified` and set `status: needs-review`.
10. Run `python3 scripts/validate_docs.py`.

## Boundaries

- Prefer an available primary source over a secondary summary.
- Keep useful historical context, with an explanation of what changed.
- Do not expand the article with unrelated findings during the audit.

## Example pre-edit report

The following Russian text is an example of the report to show before editing:

```markdown
Подтверждено: формат name и description.
Изменилось: путь проектных скиллов Codex.
Не удалось проверить: лимит конкретной старой версии Claude Code.
Предлагаю обновить два раздела и оставить статус needs-review до проверки последнего пункта.
```

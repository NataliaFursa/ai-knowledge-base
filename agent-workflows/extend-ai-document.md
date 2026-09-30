# Extend an AI document

## Outcome

Add one verified finding to an existing article without implying that the whole article was rechecked.

## Workflow

1. Identify the article and the section that owns the finding.
2. Verify the finding against a primary source or a reproducible experiment.
3. Determine whether it supplements or contradicts the current article.
4. Show the user the proposed section, a concise formulation, and the source. Wait for explicit approval.
5. Make the smallest coherent edit and add the source to `Источники`.
6. Update `last_updated`. Keep `last_verified` unchanged unless every substantive claim was rechecked.
7. If the finding contradicts the article, set `status: needs-review` and identify what needs a full refresh.
8. Run `python3 scripts/validate_docs.py`.

## Boundaries

- The finding must fit the article's topic and level of detail. Do not add it merely because it is interesting.
- Do not rewrite neighboring sections without approval for the broader change.
- Do not present one experiment as documented behavior across all product versions.

## Example proposal

The following Russian text is an example of the proposal to show before editing:

```markdown
Документ: docs/agent-skills/limits.md
Раздел: OpenAI Codex
Дополнение: новое ограничение начального списка скиллов
Источник: официальная документация OpenAI, проверено сегодня
```

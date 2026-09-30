# Find AI knowledge

## Outcome

Answer a question using relevant repository articles, their verification dates, and their original sources.
This workflow is read-only.

## Workflow

1. Read `README.md` and select articles whose titles, summaries, or tags match the question.
2. Stop searching the repository when those articles answer the question or the index has no relevant topic.
3. Distinguish information from the knowledge base from your own inferences.
4. If the user asks about the current state of a time-sensitive fact, reopen its official source.
5. State `needs-review` or `archived` status before relying on an article with either status.
6. If a current source conflicts with an article, explain the difference. Do not edit the article without a
   separate request.
7. Link to the local article and primary sources beside the claims they support. Include the article's
   `last_verified` date.

## Boundaries

- `last_updated` is not evidence of current accuracy; use `last_verified`.
- Absence of a topic in this repository is not evidence that a product lacks a feature.
- Explain any use of a secondary source when an official source is available.

## Example answer

The following Russian text illustrates the response format, not a fact to reuse without verification:

```markdown
По статье, полностью проверенной 2026-09-23, Codex собирает AGENTS.md от корня проекта до рабочей директории.
Текущая документация OpenAI подтверждает этот порядок. Источники: статья базы, документация OpenAI.
```

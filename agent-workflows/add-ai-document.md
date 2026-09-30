# Add an AI document

## Outcome

Create one new article or experiment record, add it to the index, and validate the repository.

## Workflow

1. Identify the topic, document type, vendors, and scope.
2. Check `README.md` and related articles. If the topic is already covered, propose extending an existing article
   instead of creating a duplicate.
3. Choose the template by the requested outcome:
   - Use `templates/article.md` for an explanation, comparison, or guide that synthesizes sourced information.
   - Use `templates/experiment.md` for a reproducible test of specific behavior, recording the question,
     environment, steps, expected result, and actual result.
   If the request needs both, propose two linked documents and wait for approval. If the intended outcome is
   unclear, ask before choosing. Keep the resulting documents in Russian.
4. Gather primary sources. Open current official pages for facts that can change over time.
5. Show the user the proposed path, section outline, and main sources. Wait for explicit approval before writing.
6. Fill every frontmatter field and the `Источники` section. Cite sources beside time-sensitive claims.
7. Set `status: current` only after verifying every substantive claim. Otherwise use `needs-review`.
8. Add the document to the `README.md` navigation.
9. Run `python3 scripts/validate_docs.py` and fix errors caused by the change.

## Stop conditions

Ask for clarification if the topic could reasonably become several different documents, the relevant vendor is
unclear, or a required source cannot be used in a public repository. Do not choose a materially different scope
or publish a restricted source on the user's behalf.

## Example proposal

The following Russian text is an example of the proposal to show before creating the file:

```markdown
Путь: docs/models/context-windows.md
Тип: статья
Разделы: термины, ограничения по вендорам, практические последствия, источники
Основные источники: официальные страницы OpenAI и Anthropic
```

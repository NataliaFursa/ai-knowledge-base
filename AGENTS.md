# AI Knowledge Base

## Purpose

This repository contains Russian-language articles about AI tools and reproducible checks of their behavior.

## Working with documents

- Use `README.md` as the index and open only documents relevant to the request.
- Prefer official documentation, specifications, and source code.
- Cite a source next to each time-sensitive claim and include it in the article's `Источники` section.
- Distinguish documented facts, experimental observations, and author inferences.
- Change `last_verified` only after checking every substantive claim in the article.
- For a partial addition, change only `last_updated` and the verification date of the new source.
- Preserve uncertainty when a source does not unambiguously support a claim.

## Changes

Before creating a document or substantially restructuring an existing one, show the user its path, proposed
structure, and primary sources. Write the changes only after explicit approval.

After changing Markdown or skills, run `python3 scripts/validate_docs.py`.

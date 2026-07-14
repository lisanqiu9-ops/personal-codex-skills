---
name: ebook-world-visualizer
description: Analyzes long-form ebooks into chapter indexes, character profiles, factions, relationship graphs, worldbuilding databases, and image-generation prompts. Use when the user uploads or references an EPUB/TXT/MD/DOCX book and asks to extract characters, forces, relationships, story-world structure, visual concepts, or GPT image prompts.
metadata:
  short-description: Long ebook character, faction, relationship, and visual prompt analysis
---

# Ebook World Visualizer

Use this skill to turn an ebook into a structured story-world database and visual prompt pack. It is designed for long novels, serial fiction, biographies, historical narratives, and other books where the useful output is not a summary, but entities, factions, relationships, events, and image-ready visual briefs.

Do not process a long book by reading it all at once. Build an index first, cache intermediate results, then synthesize from the cached database.

## Core Outputs

Create an output folder with this shape unless the user asks for something narrower:

```text
output/
├── 00-book-profile.md
├── 01-chapter-index/
├── 02-world-db/
│   ├── characters.json
│   ├── factions.json
│   ├── relationships.json
│   ├── events.json
│   ├── locations.json
│   └── terms.json
├── 03-analysis/
│   ├── characters.md
│   ├── factions.md
│   ├── relationship-graph.mmd
│   ├── timeline.md
│   └── visual-opportunities.md
├── 04-prompts/
│   ├── character-prompts.md
│   ├── faction-prompts.md
│   ├── scene-prompts.md
│   └── cover-prompt.md
└── 05-images/
```

## Workflow

1. **Intake**
   - Identify file type, size, language, chapter count, and whether the user wants analysis only, prompts, or final images.
   - For copyrighted books, do private analysis only. Do not reproduce long passages. Use short evidence summaries instead of copied prose.

2. **Extract Chapters**
   - For EPUB, run `scripts/extract_epub.py` to extract readable chapter text and `manifest.json`.
   - For TXT/MD, split by chapter headings when obvious; otherwise split into stable chunks.
   - For DOCX, use the available document tooling or bundled workspace dependencies to extract text, then split.

3. **Chapter Index Pass**
   - Analyze chapters incrementally.
   - Each chapter index must capture: present characters, new characters, factions, locations, key events, relationship changes, world terms, visual opportunities, uncertainty notes, and short evidence summaries.
   - Save one JSON file per chapter under `01-chapter-index/`.

4. **Entity Merge Pass**
   - Merge aliases and duplicate entities.
   - Track uncertainty instead of forcing a false merge.
   - Save canonical databases under `02-world-db/`.
   - Use schemas from `references/schemas.md`.

5. **Global Analysis Pass**
   - Read the databases, not the entire source text.
   - Rank characters, factions, scenes, and conflicts by story importance and visual value.
   - Generate Mermaid relationship graphs and concise Markdown reports.

6. **Visual Prompt Pass**
   - Generate image prompts only for selected high-value targets by default:
     - Top 10 characters
     - Top 5 factions
     - Top 5 scenes
     - One cover or relationship poster prompt
   - Use `references/prompt_templates.md`.
   - Ask before generating images if the user has not already approved direct image generation.

7. **Image Generation**
   - If an image generation tool/model is available and the user approves, generate images from the final prompt pack.
   - If unavailable, deliver the prompt pack in a model-neutral format with optional `gpt-image-2` notes.

## Long Book Strategy

- Under 300k Chinese characters: full chapter indexing is acceptable.
- 300k-1M Chinese characters: process by volume or batches of 5-10 chapters.
- Over 1M Chinese characters: start with a pilot batch, then continue incrementally.
- Never redo completed chapter indexes unless the source changed or the user asks for a deeper pass.

## Quality Rules

- Prefer structured JSON for intermediate state and readable Markdown for final reports.
- Keep every claim traceable to chapter-level evidence summaries.
- Mark spoilers when the user asks for early-chapter-only analysis.
- Separate facts, inference, and visual invention.
- Do not invent physical appearance unless it is stated, strongly implied, or explicitly requested as concept art.
- Relationship graphs should be readable: split into subgraphs when there are more than 25 nodes.

## References

- `references/schemas.md`: JSON shapes for chapter indexes and world databases.
- `references/prompt_templates.md`: Prompt structure for characters, factions, scenes, covers, and relationship posters.

---
name: gongwen
description: Chinese alias for the user's official-document formatting workflow. Use when the user says gongwen, 公文, 公文规范, 正式文档, 公文格式, or asks to optimize/format a DOCX according to their official-document rules. This skill should route to chinese-official-document-format.
---

# Gongwen Alias

This is a short manual alias for `chinese-official-document-format`.

When this skill is invoked:

1. Read `../chinese-official-document-format/SKILL.md`.
2. If actual DOCX formatting or generation is needed, also read `../chinese-official-document-format/references/format_rules.md`.
3. Follow the original skill's rules as the authority.
4. Preserve the source document's layout unless the user explicitly asks for a deeper rewrite.
5. For existing DOCX documents with images, tables, or screenshots, use conservative edits first: keep page geometry, image/table placement, table widths, and captions intact; only adjust text styling where safe.


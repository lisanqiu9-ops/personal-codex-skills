---
name: gongwen
description: Use when formatting or drafting Chinese official documents,申报材料,正式函件,报告,投标/揭榜申报书,Word DOCX documents, or when the user asks for gongwen、公文格式、公文写作规范、仿宋/黑体/楷体、首行缩进2字符、标题黑色、附件/落款/页码规范、Word导航窗格、标题样式.
---

# 中文公文格式

## When To Use

Use this skill when the user asks to create, revise, or format a Chinese formal document such as:

- 公文、通知、报告、请示、函、纪要、答复
- 申报书、揭榜申报材料、投标技术文件、正式说明材料
- Word/DOCX documents that should look like Chinese official or quasi-official materials
- Any request mentioning 公文规范、正式格式、标题黑色、仿宋、黑体、楷体、首行缩进2字符、页码、附件、落款、Word导航窗格、标题样式

Prefer this skill over generic business-document styling for Chinese government, state-owned enterprise, power grid, school, or formal申报 materials.

## Core Workflow

1. Read the source/template requirements first, if provided.
2. Load `references/format_rules.md` when actual formatting, DOCX generation, or style correction is needed.
3. Keep the user's required document structure ahead of generic公文 rules. For example, if an附件2 template defines chapter order, preserve that order.
4. Apply a plain Chinese formal style unless the user asks for a richer design.
5. Do not use blue or decorative heading colors for公文/申报书 style unless the source template explicitly requires them.
6. Mark unverifiable facts with clear待补充 labels instead of inventing company, finance, credit, certificate, personnel, legal, or performance data.
7. For existing DOCX documents with images, tables, or screenshots, use conservative edits first: keep page geometry, image/table placement, table widths, and captions intact; only adjust text styling where safe.
8. For every paragraph containing an inline or anchored image, explicitly set single line spacing and clear any exact/fixed line spacing inherited from the body style. Never apply the body's fixed line spacing to an image paragraph; Word can otherwise clip the image to the line box.
9. For DOCX output, preserve or create real Word heading structure so the navigation pane works. Use built-in heading styles or OOXML outline levels; bold text, manual numbering, or table-only headings are not sufficient.

## Formatting Priorities

For DOCX work, enforce these first:

- Main title: black, centered, 2号约22pt, `方正小标宋_GBK` or fallback `小标宋体`/`华文中宋`/`宋体`. Do not use Word's default blue `Title` or `Heading` visual style for the main title.
- Subtitle or descriptive line under the title, if present: black, centered, 楷体 or 仿宋, smaller than the main title.
- Body in 仿宋-style Chinese font with first-line indent of 2 Chinese characters.
- Heading hierarchy: `一、` as 黑体, `（一）` as 楷体, `1.` and `（1）` as 仿宋 unless template says otherwise.
- Word navigation: first-level headings should appear in the navigation pane as level 1; second-level headings should appear as level 2 when the document needs subnavigation. Do not put image/table captions into the navigation pane.
- When using Word built-in `Heading 1`/`Heading 2` for navigation, override both the style and the runs to black 公文 formatting; do not leave the blue theme color in the style gallery.
- English letters and numbers in Times New Roman where practical.
- Tables readable, plain, black text, restrained borders, no decorative color fills unless useful for data tables.
- Page numbers and附件/落款 rules follow the reference when relevant.

## Delivery Audit

Before delivering a DOCX:

- Verify the main title is black, centered, about 22 pt, and uses 小标宋/宋体-family fallback.
- Verify structural headings appear in Word navigation and render black, not blue.
- Verify `Heading 1` and `Heading 2` style definitions are black if those styles are used.
- Verify figure/table captions and subtitles are not included in navigation.

## Writing Priorities

Use formal Chinese official-document prose:

- 总分总 where appropriate.
- Put important conclusions near the beginning of paragraphs.
- Keep wording concise, concrete, and non-duplicative.
- Use data to support claims when real data is available.
- Avoid overclaiming. Use cautious wording for related but not identical experience.

## Source

The detailed rules are distilled from the user's PDF: `1219_关于公文写作规范的几点要求.pdf`.

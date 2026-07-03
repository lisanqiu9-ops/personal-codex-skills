---
name: chinese-official-document-format
description: Use when formatting or drafting Chinese official documents,申报材料,正式函件,报告,投标/揭榜申报书,Word DOCX documents, or when the user asks for 公文格式、公文写作规范、仿宋/黑体/楷体、首行缩进2字符、标题黑色、附件/落款/页码规范.
---

# 中文公文格式

## When To Use

Use this skill when the user asks to create, revise, or format a Chinese formal document such as:

- 公文、通知、报告、请示、函、纪要、答复
- 申报书、揭榜申报材料、投标技术文件、正式说明材料
- Word/DOCX documents that should look like Chinese official or quasi-official materials
- Any request mentioning 公文规范、正式格式、标题黑色、仿宋、黑体、楷体、首行缩进2字符、页码、附件、落款

Prefer this skill over generic business-document styling for Chinese government, state-owned enterprise, power grid, school, or formal申报 materials.

## Core Workflow

1. Read the source/template requirements first, if provided.
2. Load `references/format_rules.md` when actual formatting, DOCX generation, or style correction is needed.
3. Keep the user's required document structure ahead of generic公文 rules. For example, if an附件2 template defines chapter order, preserve that order.
4. Apply a plain Chinese formal style unless the user asks for a richer design.
5. Do not use blue or decorative heading colors for公文/申报书 style unless the source template explicitly requires them.
6. Mark unverifiable facts with clear待补充 labels instead of inventing company, finance, credit, certificate, personnel, legal, or performance data.

## Formatting Priorities

For DOCX work, enforce these first:

- Title black, centered, formal Song-style title font.
- Body in 仿宋-style Chinese font with first-line indent of 2 Chinese characters.
- Heading hierarchy: `一、` as 黑体, `（一）` as 楷体, `1.` and `（1）` as 仿宋 unless template says otherwise.
- English letters and numbers in Times New Roman where practical.
- Tables readable, plain, black text, restrained borders, no decorative color fills unless useful for data tables.
- Page numbers and附件/落款 rules follow the reference when relevant.

## Writing Priorities

Use formal Chinese official-document prose:

- 总分总 where appropriate.
- Put important conclusions near the beginning of paragraphs.
- Keep wording concise, concrete, and non-duplicative.
- Use data to support claims when real data is available.
- Avoid overclaiming. Use cautious wording for related but not identical experience.

## Source

The detailed rules are distilled from the user's PDF: `1219_关于公文写作规范的几点要求.pdf`.

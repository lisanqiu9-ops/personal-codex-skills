# 中文公文格式规则

This reference is distilled from the user's PDF `1219_关于公文写作规范的几点要求.pdf`. Use it as the local style authority for Chinese official-document formatting unless a user-provided template conflicts.

## Page And General Style

- Use a sober, black-text document style.
- Avoid blue headings, decorative section bands, excessive shading, or presentation-style layout.
- Preserve required template structure and headings when a申报材料 or投标文件 template is provided.
- For formal Word documents, use Chinese fonts and sizes similar to official documents. If exact Founder fonts are unavailable, use reasonable Windows substitutes.

## Font Rules

Preferred fonts from the PDF:

- Main title: `方正小标宋_GBK`, 2号, centered.
- Body: `方正仿宋_GBK`, 3号.
- First-level heading `一、`: `方正黑体_GBK`.
- Second-level heading `（一）`: `方正楷体_GBK`.
- Third/fourth-level headings `1.` and `（1）`: `方正仿宋_GBK`.
- English letters and numbers: `Times New Roman`.

Fallback fonts when Founder fonts are not available:

- Main title: `小标宋体`, `华文中宋`, `宋体`, or `SimSun`.
- Body: `仿宋_GB2312`, `仿宋`, or `FangSong`.
- First-level heading: `黑体` or `SimHei`.
- Second-level heading: `楷体_GB2312`, `楷体`, or `KaiTi`.
- English/numbers: `Times New Roman`.

Approximate Word sizes:

- 2号: 22 pt.
- 3号: 16 pt.
- 4号: 14 pt.

## Paragraph Rules

- Body paragraphs should use first-line indent of 2 Chinese characters.
- In Word automation, this is usually about `2em`; with 3号 body text, use about `32 pt` first-line indent. If body is smaller, use twice the font size.
- Use formal line spacing suitable for 3号 Chinese body text, commonly 1.25 to 1.5 lines or fixed spacing if required by a local template.
- Keep heading paragraphs unindented unless the template shows otherwise.
- Keep title centered and unindented.

## Image Paragraph Rules

- Put each inline image in its own paragraph and center that paragraph unless the source template requires another alignment.
- Explicitly set the image paragraph to single line spacing. Clear inherited exact/fixed line spacing before saving the DOCX.
- Never reuse the body's fixed line spacing on an image paragraph. In Microsoft Word, a fixed line box can clip a full-size image into a narrow horizontal strip.
- Keep the caption in a separate paragraph immediately after the image. The caption may follow the document's caption spacing, but it must not force fixed line spacing onto the image paragraph.

## Heading Hierarchy

Use this hierarchy:

1. `一、二、三、` for first-level headings. Font: 黑体. Example: `一、企业基本情况`.
2. `（一）（二）（三）` for second-level headings. Font: 楷体. Example: `（一）基本信息`.
3. `1. 2. 3.` for third-level headings. Font: 仿宋.
4. `（1）（2）（3）` for fourth-level headings. Font: 仿宋.

Avoid mixing Markdown-style headings, colored headings, and decorative numbering in formal Chinese documents.

## Title Rules

- Use 2号方正小标宋_GBK or fallback title font.
- Center the title.
- If the title wraps, keep phrase meaning complete on each line.
- Wrapped title lines should look balanced, preferably trapezoid or diamond-like in visual arrangement.
- Do not add colored underline, borders, or decorative rules under the title unless a specific template requires it.

## Attachment Rules

- Put attachments one blank line below the body.
- Start at left indent of 2 Chinese characters with `附件：`.
- If multiple attachments exist, use Arabic numerals, e.g. `附件：1.XXXXXX`.
- Do not add punctuation after the attachment name.

## Signature And Date

- The written date is generally right-indented by 4 Chinese characters.
- Use Arabic numerals for year, month, and day.
- Use full year, e.g. `2026年6月11日`.
- Do not pad month/day with zero, e.g. use `6月1日`, not `06月01日`.
- The issuing unit name is centered relative to the written date.

## Page Number Rules

- Use 4号 half-width Song-style Arabic numerals.
- Put one Chinese character-width line on each side of the page number.
- Odd pages: page number right aligned, right indented by 1 Chinese character.
- Even pages: page number left aligned, left indented by 1 Chinese character.
- For simpler申报书 drafts, a centered or right footer page number is acceptable if exact odd/even footer control is not worth the risk, but mention the limitation if asked.

## Content Rules

- Structure should be clear and layered.
- A common structure is 总分总: overview/theme, evidence or breakdown, summary/requirements.
- Be concise and easy to understand; avoid repetition and ambiguous wording.
- Use punctuation correctly.
- Put important points near the beginning of paragraphs.
- Use quantitative data to support major claims when real data exists.
- Do not invent factual evidence, credit records, financial data, certificates, legal records, personnel records, or performance data.

## Naming And Abbreviation Notes

The PDF includes State Grid naming examples. Apply these principles generally:

- Use full names for external-facing documents where possible.
- If multiple departments/units are named, use consistent full names, standard abbreviations, or generic names.
- Keep separators consistent: use `、` between same-category units and `，` between different categories when listing many units.
- Avoid casual or inconsistent abbreviations.

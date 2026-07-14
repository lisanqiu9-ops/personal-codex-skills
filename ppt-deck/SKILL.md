---
name: ppt-deck
description: Generate or production-plan Chinese presentation decks with global style instructions, narrative slide structure, designer-ready visual direction, and optional final PNG page image workflow. Use when the user asks for PPT大纲、演示结构、视觉叙事、逐页设计、单页生图提示词, or finished PPT-style page images for reading and sharing.
metadata:
  short-description: 中文演示文稿大纲与视觉叙事
---

# PPT Deck

Use this skill to turn source material, a topic, or a user brief into a Chinese, designer-ready presentation deck plan, and when requested, into final PPT-style PNG page images. The deck is meant for reading and sharing, so every slide must be self-explanatory without a live speaker.

This skill has two output modes:

- **Blueprint Mode**: create the structured outline and visual brief for a designer.
- **Production Mode**: first create the blueprint, then generate final raster page images using an image generation model as the primary visual generator.
- **Single Page Prompt Mode**: analyze one dense slide/page/image, extract the key message, improve presentation clarity, and output only optimized image-generation prompts for the user's web image tool.

Do not substitute deterministic drawing scripts, HTML, SVG, canvas, or basic Pillow compositing as the main visual generator for polished final pages. Scripts are allowed for contact sheets, cropping, resizing, and exact text overlay after an image-model visual direction is accepted.

## Core Workflow

1. Ingest the source material and extract the deck's topic, audience, purpose, tone, source facts, must-keep details, and requested page limit.
2. Diagnose whether the user wants **Blueprint Mode**, **Production Mode**, or **Single Page Prompt Mode**. If they ask for PNG images, final slides, page images, effect images, or a folder of rendered pages, use Production Mode. If they provide one page/one image/one dense slide and ask only for prompt optimization, use Single Page Prompt Mode.
3. Before writing the outline, create a global `STYLE INSTRUCTIONS` block in a fenced code block.
4. Choose a visual narrative system that fits the content. Use blueprint/architectural language only when the topic benefits from systems thinking, technical structure, data display, or process decomposition.
5. Lock deck-level visual constants before page work: canvas ratio, cover/body distinction, palette, title scale, title position, text budget, recurring motifs, and what must never appear.
6. Build a complete slide sequence with page 1 as the cover and the final page as the back cover.
7. For every slide in Blueprint Mode, output exactly these four sections:
   - `// NARRATIVE GOAL (叙事目标)`
   - `// KEY CONTENT (关键内容)`
   - `// VISUAL (视觉画面)`
   - `// LAYOUT (布局结构)`
8. For Production Mode, compress each slide into one exact image-generation brief with one main point, one composition, and a short `Required text only` list.
9. Keep all slide content in Chinese. Preserve user-provided Chinese placeholders. If the user provides English source material, translate the slide-facing content into Chinese.

## Required Output Shape

Start with:

```markdown
**风格指令 (STYLE INSTRUCTIONS):**

Design Aesthetic: ...
Background Color: ...
Primary Font: ...
Secondary Font: ...
Color Palette:
    Primary Text Color: ...
    Primary Accent Color: ...
    Secondary Accent Color: ... (optional)
Visual Elements: ...
```

Then write:

```markdown
**绘制内容 (CONTENT TO DRAW):**

## 第 1 页｜[叙事性中文页名]
...
```

Each slide must include enough context for the designer to work without seeing the original source material.

## Slide Rules

- Default to 12-20 slides unless the user requests otherwise.
- Never exceed 30 slides. If the user asks for more, explain that the outline will compress or split the deck.
- The first slide must be a cover. The last slide must be a designed closing slide, never a generic "谢谢" or "有任何问题吗？" page.
- Covers and back covers should use a distinct visual treatment from inner content pages: poster composition, bold type, full-bleed visual, symbolic object, or strong typographic closure.
- Internal slides should use a consistent grid, information hierarchy, and visual grammar.
- Titles should be narrative Chinese statements, not `标题：副标题`.
- Data points, quotes, named facts, dates, statistics, and case details must come from the supplied source material. If the source does not include a specific fact, do not invent it.
- When data is missing but structurally needed, use a Chinese placeholder such as `待补充：具体数据来源` and state what kind of source is needed.
- Preserve essential elements from the source material, including names, numbers, sequence, tradeoffs, caveats, and conclusions.

## Production Mode

Use this mode when the user asks for final rendered slide images, PNGs, a folder of pages, PPT-style images, effect images, or production-ready visuals.

Production sequence:

1. Build or reuse the slide blueprint.
2. Write one compact **Deck Style Lock** and reuse it verbatim in every page prompt.
3. For each page, write a page-specific prompt for a complete 16:9 raster PPT page image. Use one image-generation call per page brief when image-generation tools are available.
4. Keep visible Chinese text short. Put exact required visible text in a `Required text only` list.
5. If the image model produces poor Chinese text, reduce the text budget and regenerate. If text remains unreliable, generate the visual with clean blank title/label areas, then add exact Chinese text with deterministic post-processing.
6. Save final pages into a folder and create a contact sheet for review.
7. Verify dimensions, page count, visual consistency, text fidelity, source fidelity, and deck rhythm before final response.

Never treat extracted source images plus simple overlays as polished final visual pages unless the user explicitly asks for a rough draft, wireframe, or editable layout mockup.

## Single Page Prompt Mode

Use this mode when the user provides one slide, one page image, one section of content, or one dense source page and asks to optimize it into a prompt for a web image-generation tool. Do not generate images in this mode.

Goal: turn dense source content into a clearer visual communication page.

Workflow:

1. Read the page/image content and identify the source page's real communication problem: too many bullets, weak hierarchy, no visual metaphor, no audience path, or unclear takeaway.
2. Extract one main message. If the page contains many details, group them into 2-4 semantic modules.
3. Preserve source-specific technical terms and categories. Do not invent facts.
4. Generate one complete copy-ready prompt that includes the visual composition and all text the user is likely to paste into the web image tool.
5. When Chinese fidelity is risky, still keep the full prompt copy-ready, but mark long text as "small readable annotation text" inside the prompt rather than separating it into another section the user might forget to paste.
6. Include a negative prompt.

Output exactly this structure:

```markdown
## 单页解析

**页面主旨：**
...

**信息重组：**
- ...
- ...
- ...

**建议可见文字：**
- 标题：...
- 模块标签：...
- 关键短句：...

**网页端生图 Prompt：**
```text
完整可复制提示词...
```

**Negative Prompt：**
...

**可选后期叠加文字：**
...
```

For dense technical/business slides, prefer visual restructuring over bullet preservation. Examples:

- Turn a long rule list into a three-module system diagram.
- Turn a table into a pipeline, dashboard, map, matrix, or diagnostic console.
- Turn policy/process text into an operating model.
- Turn many examples into 3 labeled clusters plus one takeaway.

Chinese text guidance:

- Default output should be one complete copy-ready prompt. Do not require the user to paste a second section to get enough text.
- Put title, module labels, and compact detail text inside the main prompt.
- Keep long explanations condensed into short annotation cards, usually 8-18 Chinese characters per card.
- Use "可选后期叠加文字" only as a fallback for exact correction, not as the primary content carrier.
- If the web image tool has poor Chinese fidelity, include an instruction in the prompt to reserve clean blank areas for later text overlay.

### Production Prompt Pattern

Use this pattern for each generated page:

```text
Use case: Chinese reading-and-sharing presentation page.
Asset type: one complete 16:9 polished PPT-style raster image.
Preferred final size: 1920x1080.

Create page <number>/<total> of a coherent deck.
Page role: <cover | body page | back cover>
Title exactly: <short Chinese title>
Subtitle exactly: <optional short Chinese subtitle>
Main point: <one sentence>

Apply the deck style lock: <paste compact style lock>.

Composition:
<specific scene, metaphor, focal point, foreground/background relationship, and where text should sit.>

Required text only:
<list every visible Chinese text item exactly. Keep it short.>

Avoid:
extra text, gibberish text, fake logos, watermarks, celebrity likenesses, generic stock-photo look, cluttered UI, inconsistent style, unreadable small text, heavy template boxes, and invented facts.
```

### Text Fidelity Fallback

If exact Chinese text is mission-critical:

- Ask the image model for clean visual space with no generated title text.
- Add title, subtitle, labels, and key quotes locally afterward.
- Keep the final output as PNG page images.
- Re-check that no duplicate or incorrect generated text remains.

## Language Quality

Use direct, confident, active human language. Avoid generic presentation filler.

Forbidden patterns:

- `不仅仅是 [X]，而是 [Y]`
- `赋能`
- `重塑未来`
- `开启新篇章`
- `有任何问题吗？`
- `谢谢观看`
- title formats that rely on `标题：副标题`
- vague praise such as `高级感`, `科技感`, or `震撼` without concrete visual direction

Assume the audience is intelligent, professionally curious, and capable of handling nuance. Do not over-simplify complex material.

## Visual Guidance

Visual descriptions must be concrete enough to guide production or image generation. Specify:

- composition and focal point
- chart or diagram type when relevant
- color and contrast behavior
- line, shape, texture, material, or photographic style
- information hierarchy
- what should not appear if it could undermine the narrative

Prefer visual metaphors that clarify the content, such as maps, ledgers, operating rooms, archives, control panels, blueprints, field notes, product teardown tables, timelines, triptychs, or evidence walls. Use photography only when the subject benefits from realism; never require realistic photos of famous people.

## Style Selection

Choose style based on content:

- Technical systems, AI, data, operations: precise blueprint, control-room, technical journal, or analytical dashboard.
- Education and beginner tutorials: bold, playful, step-by-step, generous diagrams, clear progress cues.
- Strategy and business: editorial, restrained, executive, evidence-led, sharp contrast between thesis and proof.
- Culture, history, humanities: archive, museum label, field notebook, cinematic essay, richly contextual visuals.
- Product or brand: object-forward, tactile, close-up, commercially polished, with the product visible early.
- Primary school technology innovation / district competition: bright cinematic technology, campus sunlight, robotics, aerospace, red scarf, Chinese red ribbon, blue HUD light trails, warm child-friendly expression, and clear competition-stage titles.

See `references/style_patterns.md` only when extra inspiration is needed.

## Final Quality Check

Before responding, verify:

- A `STYLE INSTRUCTIONS` block appears before the outline.
- Every slide has the four required sections.
- Page 1 is a cover and the last page is a designed closing page.
- The deck does not exceed 30 pages.
- No invented data appears.
- No forbidden filler phrases appear.
- Visual instructions are executable, not abstract mood words.
- If final PNG pages were requested, image generation was used as the primary visual path or the response clearly says only a rough layout draft was produced.

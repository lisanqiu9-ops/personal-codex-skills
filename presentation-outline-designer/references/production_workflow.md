# Production Workflow

Use this reference when the user wants final rendered PPT-style PNG pages rather than only an outline.

## Parse First, Generate Second

1. Extract source facts, quotes, dates, people, organizations, page-level visual evidence, and any school-specific requirements.
2. Compress the source into a slide spine. Each page gets one main point.
3. Assign each page a role:
   - cover
   - context
   - evidence
   - contrast
   - process
   - classroom practice
   - value statement
   - closing
4. Lock one deck style before image generation.
5. Generate or revise each page image with that same lock.
6. Use deterministic post-processing only for text correction, resizing, contact sheet, and packaging.

## Technology Innovation Campus Style Lock

Use this as a starting point when the user asks for a technology innovation deck for primary school or district competition.

```text
Polished Chinese primary-school technology innovation presentation.
16:9 cinematic PPT page, bright blue technology atmosphere blended with warm sunny campus.
Recurring visual motifs: friendly white robot, red scarf, Chinese red ribbon, school building, rocket or satellite, transparent blue HUD panels, light trails, shield symbol for protection, subtle circuit lines.
High-quality commercial event-poster rendering, crisp lighting, clean composition, vivid but not dark.
Use deep technology blue, clean white, Chinese red, and sunlight gold.
Children should look natural, positive, and school-appropriate; avoid uncanny faces and celebrity likeness.
Use large clear Chinese headline areas with enough blank space for exact text overlay if needed.
Keep each page visually rich but not crowded. Every page belongs to one coherent deck.
```

## Image Generation Page Prompt

```text
Use case: district competition presentation page for a Chinese primary school.
Asset type: one complete polished 16:9 PPT-style raster image, 1920x1080.

Create page <number>/<total>.
Page role: <cover | body page | back cover>.
Title exactly: <short Chinese title>.
Main point: <one sentence>.

Apply this deck style lock:
<paste style lock>

Composition:
<describe the exact scene, focal subject, text area, light direction, motion lines, and symbolic objects.>

Required text only:
<short exact Chinese visible text list>

Avoid:
extra Chinese or English text, fake school names, fake logos, watermarks, celebrity faces, militarized aggression, cluttered templates, unreadable UI, low-resolution collage, and generic stock-photo styling.
```

## Quality Gate

Before delivery:

- The contact sheet looks like one deck, not twelve unrelated images.
- Cover and back cover are visually distinct from body pages.
- Body pages share title scale, color behavior, and motif language.
- Chinese text is exact, readable, and short.
- No source facts are invented.
- No visible fake text, watermarks, or random English appears.
- The output folder contains only final PNGs unless the user asks for drafts or previews.

## Single Page Prompt Mode

Use when the user only wants a prompt for a web image generator.

Required output:

```markdown
## 单页解析

**页面主旨：**
<one sentence>

**信息重组：**
- <module 1>
- <module 2>
- <module 3>

**建议可见文字：**
- 标题：<short title>
- 模块标签：<2-4 labels>
- 关键短句：<optional>

**网页端生图 Prompt：**
```text
<complete copy-ready image prompt, including the visible text plan>
```

**Negative Prompt：**
<avoid list>

**可选后期叠加文字：**
<exact text to add locally only if the web model cannot render Chinese reliably>
```

Dense slide transformation rule:

- Preserve the original professional meaning.
- Do not carry over the original bullet density.
- Extract a visual metaphor first, then map content into the metaphor.
- Default to a single complete prompt the user can copy directly.
- Include enough compact visible text inside the main prompt for a useful reporting slide.
- Recommend post-overlay only as an optional correction path, not as required continuation content.

# PPT Deck Skills

一组用于 Codex 的中文 PPT 技能：

- `presentation-outline-designer`：核心技能。用于解析文章、PDF、截图或单页内容，生成 PPT 大纲、风格指令、视觉叙事方案、网页端生图提示词，或进入成品 PNG 生产流程。
- `ppt-deck`：短别名。日常调用时直接记 `$ppt-deck` 即可。

## 适合场景

- 把 PDF / 文章解析成演示文稿大纲
- 区赛、校赛、汇报、课程、路演、阅读型分享 PPT
- 单页密集 PPT 截图解析，提炼重点并生成网页端生图 prompt
- 先解析后生成：先做叙事骨架，再做视觉生成提示词
- 指定任意风格：科技创新风、政务汇报风、商业咨询风、杂志编辑风、儿童绘本风、数据仪表盘风等

## 安装

将本仓库中的两个文件夹复制到你的 Codex skills 目录：

```text
presentation-outline-designer
ppt-deck
```

Windows 默认路径通常是：

```text
C:\Users\你的用户名\.codex\skills\
```

复制后结构应类似：

```text
C:\Users\你的用户名\.codex\skills\presentation-outline-designer\SKILL.md
C:\Users\你的用户名\.codex\skills\presentation-outline-designer\references\style_patterns.md
C:\Users\你的用户名\.codex\skills\presentation-outline-designer\references\production_workflow.md
C:\Users\你的用户名\.codex\skills\ppt-deck\SKILL.md
```

## 常用调用

```text
用 $ppt-deck 解析这个 PDF，生成一套 15 页以内的中文 PPT 大纲。
```

```text
用 $ppt-deck 做单页解析，只输出网页端生图提示词。
风格：科技企业汇报风。
```

```text
用 $ppt-deck 先解析后生成 12 张科技创新校园风 PNG。
```

```text
用 $ppt-deck 把这页密集内容提炼成适合汇报展示的信息图 prompt。
```

## 输出模式

- `Blueprint Mode`：只输出 PPT 大纲、风格指令和逐页视觉方案。
- `Production Mode`：先解析，再生成成品 PNG 页面图。
- `Single Page Prompt Mode`：针对单页截图或单页内容，只输出完整可复制的网页端生图 prompt。

## 设计原则

这个技能不是固定某一种风格，而是一套流程：

```text
解析内容 → 判断受众与场景 → 提炼叙事主线 → 锁定视觉风格 → 输出大纲或生图 prompt
```

当用户明确指定风格时，以用户指定风格为准；未指定时，技能会根据主题和受众自动选择合适风格。

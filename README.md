# Personal Codex Skills

个人日常工作中持续整理的 Codex Skills，覆盖演示文稿、公文排版、手绘技术图和长篇电子书分析。每个目录都是可独立安装、直接调用的完整 Skill，不再使用“核心 Skill + 空壳别名”结构。

## Skills

| Skill | 用途 |
| --- | --- |
| `ppt-deck` | 生成中文 PPT 大纲、叙事结构、视觉方案和单页生图提示词。 |
| `ppt-handdrawn` | 将文章、课程或提纲制作成中文手绘技术风格页面图。 |
| `gongwen` | 起草或整理中文公文、申报材料及正式 DOCX 版式。 |
| `ebook-world-visualizer` | 从长篇电子书中提取章节、人物、势力、关系、世界观和视觉提示词。 |

## Quick Install

Windows PowerShell：

```powershell
$repo = "$env:TEMP\personal-codex-skills"
$dest = "$env:USERPROFILE\.codex\skills"

Remove-Item $repo -Recurse -Force -ErrorAction SilentlyContinue
git clone https://github.com/lisanqiu9-ops/personal-codex-skills.git $repo
New-Item -ItemType Directory -Force -Path $dest | Out-Null

Copy-Item "$repo\ppt-deck" -Destination $dest -Recurse -Force
Copy-Item "$repo\gongwen" -Destination $dest -Recurse -Force
Copy-Item "$repo\ppt-handdrawn" -Destination $dest -Recurse -Force
Copy-Item "$repo\ebook-world-visualizer" -Destination $dest -Recurse -Force
```

安装后重启 Codex。

## Common Calls

```text
用 $ppt-deck 解析这个 PDF，生成一套 15 页以内的中文 PPT 大纲。
```

```text
用 $gongwen 优化这个 DOCX，按我的公文规范处理。
```

```text
用 $ppt-handdrawn 把这份课程大纲整理成 8 页中文手绘技术课件图。
```

```text
用 $ebook-world-visualizer 分析这本 EPUB，整理人物、势力、关系和世界观资料。
```

## 来源与许可

- `ppt-handdrawn` 基于 Ian 创建的 [Ian Handdrawn PPT](https://github.com/helloianneo/ian-handdrawn-ppt) 修改，按 MIT License 再发布；原始版权、许可和署名保留在该目录中。
- 其他 Skill 的许可状态以各目录中的声明为准。仓库公开可见不等于自动授予未声明的使用许可。


# Codex Chinese Skill Aliases

一组个人常用 Codex skills 与中文友好别名，方便在新电脑上快速安装。

## Included Skills

- `presentation-outline-designer`：核心 PPT 大纲与视觉叙事技能。
- `ppt-deck`：`presentation-outline-designer` 的短别名。
- `chinese-official-document-format`：中文公文、申报材料、正式 DOCX 的格式规范技能。
- `gongwen`：`chinese-official-document-format` 的短别名。
- `ppt-handdrawn`：`ian-handdrawn-ppt` 的短别名。

## External Dependency

`ppt-handdrawn` 依赖另一个独立仓库中的核心技能：

```text
https://github.com/helloianneo/ian-handdrawn-ppt
```

如果要使用 `ppt-handdrawn`，需要先把该仓库里的 `ian-handdrawn-ppt` 安装到 Codex skills 目录。

## Quick Install

Windows PowerShell：

```powershell
$repo = "$env:TEMP\ppt-deck-skills"
$dest = "$env:USERPROFILE\.codex\skills"

Remove-Item $repo -Recurse -Force -ErrorAction SilentlyContinue
git clone https://github.com/lisanqiu9-ops/ppt-deck-skills.git $repo
New-Item -ItemType Directory -Force -Path $dest | Out-Null

Copy-Item "$repo\presentation-outline-designer" -Destination $dest -Recurse -Force
Copy-Item "$repo\ppt-deck" -Destination $dest -Recurse -Force
Copy-Item "$repo\chinese-official-document-format" -Destination $dest -Recurse -Force
Copy-Item "$repo\gongwen" -Destination $dest -Recurse -Force
Copy-Item "$repo\ppt-handdrawn" -Destination $dest -Recurse -Force
```

安装后重启 Codex。

## Optional: Install Handdrawn Core

只有需要使用 `ppt-handdrawn` 时才需要安装：

```powershell
$repo = "$env:TEMP\ian-handdrawn-ppt"
$dest = "$env:USERPROFILE\.codex\skills"

Remove-Item $repo -Recurse -Force -ErrorAction SilentlyContinue
git clone https://github.com/helloianneo/ian-handdrawn-ppt.git $repo
New-Item -ItemType Directory -Force -Path $dest | Out-Null

Copy-Item "$repo\ian-handdrawn-ppt" -Destination $dest -Recurse -Force
```

安装后重启 Codex。

## Alias Map

```text
ppt-deck      -> presentation-outline-designer
gongwen       -> chinese-official-document-format
ppt-handdrawn -> ian-handdrawn-ppt
```

## Common Calls

```text
用 /ppt-deck 解析这个 PDF，生成一套 15 页以内的中文 PPT 大纲。
```

```text
用 /gongwen 优化这个 DOCX，按我的公文规范处理。
```

```text
用 /ppt-handdrawn 把这份课程大纲整理成 8 页中文手绘技术课件图。
```


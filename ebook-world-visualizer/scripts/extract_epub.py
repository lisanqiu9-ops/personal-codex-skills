#!/usr/bin/env python3
"""Extract readable chapter text from an EPUB without third-party packages."""

from __future__ import annotations

import argparse
import html
import json
import re
import sys
import zipfile
from html.parser import HTMLParser
from pathlib import Path


SKIP_NAME_RE = re.compile(
    r"(cover|title|copyright|publisher|contents?|toc|dm|page-map|stylesheet)",
    re.IGNORECASE,
)


class TextExtractor(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.parts: list[str] = []
        self.skip_depth = 0

    def handle_starttag(self, tag: str, attrs) -> None:  # type: ignore[no-untyped-def]
        if tag.lower() in {"script", "style"}:
            self.skip_depth += 1
        if tag.lower() in {"p", "br", "div", "h1", "h2", "h3", "li"}:
            self.parts.append("\n")

    def handle_endtag(self, tag: str) -> None:
        if tag.lower() in {"script", "style"} and self.skip_depth:
            self.skip_depth -= 1
        if tag.lower() in {"p", "div", "h1", "h2", "h3", "li"}:
            self.parts.append("\n")

    def handle_data(self, data: str) -> None:
        if not self.skip_depth:
            self.parts.append(data)

    def text(self) -> str:
        raw = html.unescape("".join(self.parts))
        lines = []
        for line in raw.splitlines():
            clean = re.sub(r"\s+", " ", line).strip()
            if clean:
                lines.append(clean)
        return "\n".join(lines).strip()


def decode_html(data: bytes) -> str:
    declared = []
    match = re.search(br"encoding=[\"']([^\"']+)[\"']", data[:300])
    if match:
        declared.append(match.group(1).decode("ascii", errors="ignore"))
    match = re.search(br"charset=([A-Za-z0-9._-]+)", data[:2000], re.IGNORECASE)
    if match:
        declared.append(match.group(1).decode("ascii", errors="ignore"))

    candidates = []
    for enc in [*declared, "utf-8", "utf-8-sig", "gb18030", "gbk", "big5"]:
        if enc and enc.lower() not in [x.lower() for x in candidates]:
            candidates.append(enc)

    def score_text(text: str) -> int:
        chinese = len(re.findall(r"[\u4e00-\u9fff]", text))
        replacement = text.count("\ufffd")
        mojibake = sum(text.count(x) for x in ["鍏", "璇", "鈥", "涓", "鎴", "鐨", "呰", "", "€"])
        return chinese * 2 - replacement * 20 - mojibake * 30

    best = ""
    best_score = -10**9
    for enc in candidates:
        try:
            text = data.decode(enc, errors="replace")
        except LookupError:
            continue

        variants = [text]
        try:
            variants.append(text.encode("gb18030", errors="replace").decode("utf-8", errors="replace"))
        except UnicodeError:
            pass

        for variant in variants:
            score = score_text(variant)
            if score > best_score:
                best = variant
                best_score = score
    return best or data.decode("utf-8", errors="ignore")


def entry_sort_key(name: str) -> tuple[tuple[int, ...], int, tuple[int, ...], str]:
    parts = name.replace("\\", "/").split("/")
    folder_nums = []
    for part in parts[:-1]:
        if part.isdigit():
            folder_nums.append(int(part))

    filename = parts[-1]
    lower = filename.lower()
    if "prologue" in lower:
        rank = 0
    elif lower.startswith("ep"):
        rank = 1
    else:
        rank = 2
    file_nums = tuple(int(x) for x in re.findall(r"\d+", filename))
    return (tuple(folder_nums), rank, file_nums, name)


def extract_text(data: bytes) -> str:
    parser = TextExtractor()
    parser.feed(decode_html(data))
    return parser.text()


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("epub", type=Path)
    ap.add_argument("--out", type=Path, default=Path("output/source"))
    ap.add_argument("--limit", type=int, default=0, help="Maximum chapters to extract; 0 means all.")
    ap.add_argument("--min-chars", type=int, default=1200)
    args = ap.parse_args()

    if not args.epub.exists():
        print(f"EPUB not found: {args.epub}", file=sys.stderr)
        return 2

    chapters_dir = args.out / "chapters"
    chapters_dir.mkdir(parents=True, exist_ok=True)

    manifest = {
        "source": str(args.epub),
        "chapters": [],
        "skipped": [],
    }

    with zipfile.ZipFile(args.epub) as zf:
        names = sorted(
            [
                n
                for n in zf.namelist()
                if n.lower().endswith((".xhtml", ".html", ".htm"))
                and "/text/" in n.lower()
                and not SKIP_NAME_RE.search(Path(n).name)
            ],
            key=entry_sort_key,
        )

        count = 0
        for name in names:
            text = extract_text(zf.read(name))
            if len(text) < args.min_chars:
                manifest["skipped"].append({"path": name, "chars": len(text), "reason": "too_short"})
                continue
            count += 1
            chapter_id = f"chapter-{count:03d}"
            out_path = chapters_dir / f"{chapter_id}.txt"
            out_path.write_text(text, encoding="utf-8")
            manifest["chapters"].append(
                {
                    "chapter_id": chapter_id,
                    "source_path": name,
                    "output_path": str(out_path),
                    "chars": len(text),
                    "preview": text[:120],
                }
            )
            if args.limit and count >= args.limit:
                break

    (args.out / "manifest.json").write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
    print(json.dumps({"chapters": len(manifest["chapters"]), "out": str(args.out)}, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

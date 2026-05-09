#!/usr/bin/env python3
"""Parse python_learning.py into markdown + code cells; write the tutorial notebook (Python 3)."""
from __future__ import annotations

import json
from pathlib import Path


def parse_segments(source: str) -> list[tuple[str, str]]:
    """Return [(\"markdown\"|\"code\", content), ...]."""
    lines = source.splitlines(keepends=True)
    segments: list[tuple[str, str]] = []
    i = 0
    code_buf: list[str] = []

    def flush_code():
        nonlocal code_buf
        if code_buf:
            text = "".join(code_buf).rstrip() + "\n"
            if text.strip():
                segments.append(("code", text))
            code_buf = []

    while i < len(lines):
        line = lines[i]
        stripped_left = line.lstrip()
        if stripped_left.startswith("'''") or stripped_left.startswith("''''"):
            flush_code()
            opener = "''''" if stripped_left.startswith("''''") else "'''"
            opener_len = len(opener)
            idx = line.find(opener)
            after_open = line[idx + opener_len :]
            close_idx = after_open.find("'''")
            if close_idx != -1:
                inner = after_open[:close_idx]
                segments.append(("markdown", inner.strip()))
                i += 1
                continue
            md_lines = [after_open.rstrip("\n")]
            i += 1
            while i < len(lines):
                ln = lines[i]
                if "'''" in ln:
                    before, _, _ = ln.partition("'''")
                    md_lines.append(before.rstrip("\n"))
                    segments.append(("markdown", "\n".join(md_lines).strip()))
                    i += 1
                    break
                md_lines.append(ln.rstrip("\n"))
                i += 1
            continue
        code_buf.append(line)
        i += 1
    flush_code()
    return segments


def build_notebook(segments: list[tuple[str, str]]) -> dict:
    cells = []
    md_prefix = (
        "# Harnessing Python (tutorial)\n\n"
        "**Notebook kernel:** Python 3.8+.\n\n"
    )
    cells.append(
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": md_prefix.splitlines(keepends=True),
        }
    )

    for kind, text in segments:
        if kind == "markdown":
            lines = [ln + "\n" for ln in text.splitlines()]
            if not lines:
                lines = ["\n"]
            cells.append({"cell_type": "markdown", "metadata": {}, "source": lines})
        else:
            body = text
            lines = body.splitlines(keepends=True)
            if not lines:
                lines = ["\n"]
            cells.append(
                {
                    "cell_type": "code",
                    "metadata": {},
                    "source": lines,
                    "outputs": [],
                    "execution_count": None,
                }
            )

    kernelspec = {
        "display_name": "Python 3",
        "language": "python",
        "name": "python3",
    }

    return {
        "nbformat": 4,
        "nbformat_minor": 5,
        "metadata": {
            "kernelspec": kernelspec,
            "language_info": {
                "name": "python",
                "pygments_lexer": "ipython3",
            },
        },
        "cells": cells,
    }


def main():
    root = Path(__file__).resolve().parents[1]
    src = (root / "python_learning.py").read_text(encoding="utf-8")
    segments = parse_segments(src)

    out = root / "python_learning_py3.ipynb"
    nb = build_notebook(segments)
    out.write_text(json.dumps(nb, indent=1), encoding="utf-8")
    print(f"Wrote {out} ({len(nb['cells'])} cells)")


if __name__ == "__main__":
    main()

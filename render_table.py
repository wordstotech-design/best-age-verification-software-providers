#!/usr/bin/env python3
"""
Regenerate the comparison table in README.md from tools.yaml.

    python render_table.py            # print the table to stdout
    python render_table.py --write    # rewrite the block between the markers

Age verification is a compliance purchase, so the table compares methods,
coverage, and pricing model rather than a single score. Editing one YAML
entry and running this script keeps those columns and the writeups in sync.
"""
from __future__ import annotations

import argparse
from pathlib import Path

import yaml

START = "<!-- TABLE:START -->"
END = "<!-- TABLE:END -->"
COLUMNS = [
    ("name", "Provider"),
    ("methods", "Verification methods"),
    ("coverage", "Coverage"),
    ("pricing", "Pricing model"),
    ("best_for", "Best for"),
]


def linkify(provider: dict) -> str:
    name = provider.get("name", "")
    url = provider.get("url") or ""
    return f"[{name}]({url})" if url else name


def build_table(providers: list[dict]) -> str:
    header = "| " + " | ".join(label for _, label in COLUMNS) + " |"
    divider = "| " + " | ".join("---" for _ in COLUMNS) + " |"
    rows = []
    for p in providers:
        cells = []
        for key, _ in COLUMNS:
            cells.append(linkify(p) if key == "name" else str(p.get(key, "")))
        rows.append("| " + " | ".join(cells) + " |")
    return "\n".join([header, divider, *rows])


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--write", action="store_true")
    ap.add_argument("--data", type=Path, default=Path("tools.yaml"))
    ap.add_argument("--readme", type=Path, default=Path("README.md"))
    args = ap.parse_args()

    providers = yaml.safe_load(args.data.read_text(encoding="utf-8"))["providers"]
    table = build_table(providers)

    if not args.write:
        print(table)
        return 0

    text = args.readme.read_text(encoding="utf-8")
    if START not in text or END not in text:
        raise SystemExit("README is missing the TABLE markers.")
    before = text.split(START)[0]
    after = text.split(END)[1]
    new = f"{before}{START}\n{table}\n{END}{after}"
    args.readme.write_text(new, encoding="utf-8")
    print(f"Updated table in {args.readme} ({len(providers)} providers).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

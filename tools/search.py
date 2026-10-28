"""Full-text search over the knowledge base.

Usage:
  python tools/search.py TERM [TERM ...] [--game ts2|ts3|ts4] [--tag TAG] [--status STATUS] [--files] [-C N]

All terms must appear in a file (AND, case-insensitive, regex allowed). Searches topics/, research/ and sources/.
Files are ranked by number of hits; topics first. --files prints only paths.
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def front_matter(text: str) -> dict[str, str]:
    m = re.match(r"---\n(.*?)\n---", text, re.S)
    out = {}
    if m:
        for line in m.group(1).splitlines():
            if ":" in line:
                k, v = line.split(":", 1)
                out[k.strip()] = v.strip().lower()
    return out


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("terms", nargs="+")
    ap.add_argument("--game")
    ap.add_argument("--tag")
    ap.add_argument("--status", help="verified-in-game, verified-in-binary, community-reported or contradicted")
    ap.add_argument("--files", action="store_true")
    ap.add_argument("-C", type=int, default=0, help="context lines")
    ap.add_argument("--max", type=int, default=12, help="max matching lines per file")
    a = ap.parse_args()
    sys.stdout.reconfigure(encoding="utf-8")
    pats = [re.compile(t, re.I) for t in a.terms]
    files = [f for d in ("topics", "research", "sources") for f in sorted((ROOT / d).rglob("*.md"))]
    results = []
    for f in files:
        text = f.read_text(encoding="utf-8", errors="replace")
        if not all(p.search(text) for p in pats):
            continue
        fm = front_matter(text)
        if a.game and a.game.lower() not in fm.get("game", a.game.lower()):
            continue
        if a.tag and a.tag.lower() not in fm.get("tags", ""):
            continue
        if a.status and a.status.lower() != fm.get("status"):
            continue
        lines = text.splitlines()
        hits = [i for i, l in enumerate(lines) if any(p.search(l) for p in pats)]
        rank = (0 if "topics" in f.parts else 1 if "research" in f.parts else 2, -len(hits))
        results.append((rank, f, lines, hits))
    results.sort(key=lambda r: r[0])
    for _, f, lines, hits in results:
        rel = f.relative_to(ROOT).as_posix()
        if a.files:
            print(rel)
            continue
        title = next((l for l in lines if l.startswith("# ")), lines[2] if len(lines) > 2 else "")
        print(f"== {rel}  ({len(hits)} hits)  {title[:100]}")
        shown = set()
        for i in hits[: a.max]:
            for j in range(max(0, i - a.C), min(len(lines), i + a.C + 1)):
                if j not in shown:
                    shown.add(j)
                    print(f"  {j + 1:>5}: {lines[j][:220]}")
        print()
    if not results:
        print("no match")


if __name__ == "__main__":
    main()

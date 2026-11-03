#!/usr/bin/env python3
"""Checks a built _site against the relaunch spec's done-criteria.

Usage: python3 docs/superpowers/tools/site_check.py [--nav]
Run after docs/superpowers/tools/build-local.sh. Exit 1 on any failure.
--nav additionally asserts the final navigation (only meaningful once the
restructure tasks are done).
"""
import re
import sys
from html.parser import HTMLParser
from pathlib import Path

REPO = Path(__file__).resolve().parents[3]
SITE = REPO / "_site"
BASELINE = Path(__file__).with_name("baseline-urls.txt")

# Top-level nav order and required children (spec "Neue Struktur").
NAV_TOP = ["Verein", "Stationen", "Technik", "Projekte", "Publikationen", "Impressum"]
NAV_CHILDREN = {
    "Verein": ["Geschichte", "Mitglieder"],
    "Stationen": ["So funkst du über die Station"],
    "Technik": ["Hardware", "Software", "Mitbauen"],
    "Projekte": ["Einfache Remote Station 2025", "DX-Camp Döbriach 2026", "Ausblick 2027"],
}


class LinkParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.links, self.imgs, self.scripts = [], [], []

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag == "a" and a.get("href"):
            self.links.append(a["href"])
        if tag == "img" and a.get("src"):
            self.imgs.append(a["src"])
        if tag == "script" and a.get("src"):
            self.scripts.append(a["src"])


def resolve(page: Path, href: str) -> Path | None:
    href = href.split("#")[0].split("?")[0]
    if not href or re.match(r"^[a-z]+:", href) or href.startswith("//"):
        return None
    target = SITE / href.lstrip("/") if href.startswith("/") else page.parent / href
    if target.is_dir() or href.endswith("/"):
        target = target / "index.html"
    if not target.exists() and target.suffix == "":
        target = target.with_suffix(".html")
    return target


def main() -> int:
    errors: list[str] = []
    if not SITE.is_dir():
        print("no _site — run build-local.sh first")
        return 1

    for rel in BASELINE.read_text().split():
        if not (SITE / rel).exists():
            errors.append(f"old URL missing: {rel}")

    if (SITE / "docs" / "superpowers").exists():
        errors.append("docs/superpowers is published")

    for page in SITE.rglob("*.html"):
        if "-ibom" in page.name or "-bom" in page.name:
            continue  # KiBot-generated, not ours
        p = LinkParser()
        p.feed(page.read_text(errors="ignore"))
        for href in p.links + p.imgs:
            t = resolve(page, href)
            if t is not None and not t.exists():
                errors.append(f"broken link in {page.relative_to(SITE)}: {href}")

    home = LinkParser()
    home.feed((SITE / "index.html").read_text())
    for src in home.imgs:
        if re.match(r"^(https?:)?//", src):
            errors.append(f"external image on home page: {src}")

    if "--nav" in sys.argv:
        nav = (SITE / "index.html").read_text()
        m = re.search(r'<nav[^>]*aria-label="Main"[^>]*>(.*?)</nav>', nav, re.S)
        text = re.sub(r"<[^>]+>", "\n", m.group(1) if m else "")
        items = [t.strip() for t in text.splitlines() if t.strip()]
        pos = [items.index(t) if t in items else -1 for t in NAV_TOP]
        if -1 in pos or pos != sorted(pos):
            errors.append(f"top-level nav order wrong: {items}")
        for parent, kids in NAV_CHILDREN.items():
            for k in kids:
                if k not in items:
                    errors.append(f"nav entry missing: {parent} > {k}")
        for mod in ["FM Transceiver"]:
            if mod not in items:
                errors.append(f"HW module page lost from nav: {mod}")

    for e in errors:
        print("FAIL:", e)
    print("OK" if not errors else f"{len(errors)} failure(s)")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())

#!/usr/bin/env python3
"""AI-slop UI scanner.

Usage: slop_scan.py <path> [<path> ...] [--json] [--min P1|P2|P3] [--fail-on P1|P2|P3]

Every hit is a signal to review, not a verdict. Python 3.8+, stdlib only.
Exit code is 1 when --fail-on is given and a hit at that severity or worse exists.
"""
import json
import os
import re
import sys

SKIP_DIRS = {"node_modules", "dist", "build", ".next", ".nuxt", ".git", "out",
             "vendor", "coverage", ".turbo", ".vercel", "venv", ".venv",
             "__pycache__", "test-results", ".playwright-cli", "_backups"}
EXTS = {".html", ".htm", ".css", ".scss", ".js", ".jsx", ".ts", ".tsx",
        ".vue", ".svelte", ".astro", ".php", ".md", ".mdx"}

# Pictographic emoji. Dingbats such as ✓ ✕ ♡ ★ are reported separately as GLYPH.
EMOJI = re.compile("[\U0001F300-\U0001FAFF\U0001F000-\U0001F2FF☀-⛿⭐✅❌✨]")
GLYPH = re.compile("[✀-➿♥♡★☆]")
COMMENT = re.compile(r"^\s*(//|/\*|\*|#|<!--)")

# (category, severity, regex, fix hint)
RULES = [
    ("purple-gradient", "P1", re.compile(r"(from|via|to)-(purple|violet|indigo|fuchsia|pink)-\d{3}", re.I),
     "AI-default purple/pink gradient -> brand colour, solid fill"),
    ("purple-hex", "P2", re.compile(r"#(6366f1|8b5cf6|a855f7|7c3aed|9333ea|c084fc|ec4899|d946ef|4f46e5|818cf8)\b", re.I),
     "Tailwind indigo/violet/pink default -> brand token (ignore if it is a product colour swatch)"),
    ("gradient-text", "P1", re.compile(r"bg-clip-text|background-clip:\s*text|-webkit-text-fill-color:\s*transparent", re.I),
     "Gradient text -> solid colour, emphasise with weight"),
    ("glass", "P2", re.compile(r"backdrop-blur|backdrop-filter:\s*blur", re.I),
     "Glassmorphism -> solid surface + 1px border (a sticky header may be fine)"),
    ("big-radius", "P3", re.compile(r"\brounded-(2xl|3xl)\b|border-radius:\s*(2[0-9]|[3-9]\d)px", re.I),
     "Oversized radius -> one value, 6-8px"),
    ("heavy-shadow", "P3", re.compile(r"\bshadow-(xl|2xl)\b|shadow-\[0_0_", re.I),
     "Heavy or glowing shadow -> border or one light shadow"),
    ("hover-scale", "P2", re.compile(r"hover:scale-1[0-1]\d|:hover[^{]*\{[^}]*transform:\s*scale", re.I),
     "Grow-on-hover -> colour/background change"),
    ("transition-all", "P3", re.compile(r"\btransition-all\b|transition:\s*all", re.I),
     "transition-all -> name the property, 120-200ms"),
    ("decor-animation", "P2", re.compile(r"\banimate-(bounce|ping|spin|pulse)\b|data-aos=|\bfadeInUp\b|framer-motion", re.I),
     "Decorative animation -> animate state changes only; pulse only for skeletons"),
    ("scroll-reveal", "P1", re.compile(r"data-(ui-)?reveal|scroll-?reveal|reveal-on-scroll|\bwow\.js\b|ScrollReveal\(", re.I),
     "Content hidden until scrolled into view -> render it visible; blank page if JS/observer stalls"),
    ("huge-heading", "P3", re.compile(r"\btext-(6xl|7xl|8xl|9xl)\b", re.I),
     "Oversized heading -> 4-5 step type scale"),
    ("blob-decor", "P2", re.compile(r"\bblur-3xl\b|[.\"' ]blob[-_\"' {]|mix-blend-multiply|bg-\[radial-gradient"),
     "Abstract blob/orb decoration -> real photo or nothing"),
    ("fake-stats", "P1", re.compile(r">\s*(\d{1,3}[kK]?\+|\d{2,3}(\.\d)?%|24/7|10x|5\.0|4\.9/5)\s*<|\b(10k\+|500\+|1000\+|99\.9%)", re.I),
     "Possibly invented statistic -> delete unless there is a real source"),
    ("placeholder", "P1", re.compile(r"lorem ipsum|john doe|jane doe|acme( corp| inc)?\b|your company|placeholder\.com|via\.placeholder|unsplash\.it|picsum\.photos", re.I),
     "Placeholder content on a live page"),
    ("fake-testimonial", "P2", re.compile(r"testimonial|★★★★★|\"rating\":\s*5\b|stars?=\{?5", re.I),
     "Testimonial / 5 stars -> delete unless real and attributable"),
    ("slop-copy", "P2", re.compile(r"\b(unlock|unleash|supercharge|seamless(ly)?|elevate your|revolutioni[sz]e|game[- ]chang|next[- ]level|cutting[- ]edge|empower|effortless(ly)?|delve|tapestry|in today's (fast|digital))", re.I),
     "AI marketing cliché -> concrete benefit (see deslop-copy)"),
    ("slop-copy-az", "P2", re.compile(r"(inqilabi|növbəti səviyyəyə|yeni səviyyəyə|sərhədsiz imkanlar|müasir həllər|innovativ həllər|rəqəmsal dünyada|kəşf edin|möhtəşəm təcrübə|unikal təcrübə)", re.I),
     "Azerbaijani marketing cliché -> concrete benefit (see deslop-copy)"),
    ("slop-copy-ru", "P2", re.compile(r"(инновационн\w+ решени|новый уровень|безграничн\w+ возможност|уникальн\w+ опыт|в современном мире|откройте для себя)", re.I),
     "Russian marketing cliché -> concrete benefit (see deslop-copy)"),
    ("outline-none", "P2", re.compile(r"outline:\s*(none|0)\b|\boutline-none\b", re.I),
     "Focus is invisible -> add a :focus-visible style"),
]

COUNTDOWN = re.compile(r"countdown|deadline|timeLeft|secondsLeft", re.I)
STORAGE_RESET = re.compile(r"localStorage|sessionStorage|Date\.now\(\)\s*\+", re.I)


def iter_files(root):
    if os.path.isfile(root):
        yield root
        return
    for d, dirs, files in os.walk(root):
        dirs[:] = [x for x in dirs if x not in SKIP_DIRS and not x.startswith(".")]
        for f in files:
            if os.path.splitext(f)[1].lower() in EXTS and ".min." not in f:
                yield os.path.join(d, f)


def scan(root):
    hits = []
    for path in iter_files(root):
        try:
            if os.path.getsize(path) > 1_500_000:
                continue
            with open(path, encoding="utf-8", errors="ignore") as fh:
                lines = fh.readlines()
        except OSError:
            continue
        is_md = path.endswith((".md", ".mdx"))
        text = "".join(lines)
        has_focus = "focus-visible" in text or "focus:" in text
        if not is_md and COUNTDOWN.search(text) and STORAGE_RESET.search(text):
            ln = next(i for i, l in enumerate(lines, 1) if COUNTDOWN.search(l))
            hits.append((path, ln, "fake-countdown", "P1",
                         "Client-side countdown that may restart per visitor -> use a real server end date or remove",
                         lines[ln - 1]))
        for i, line in enumerate(lines, 1):
            if len(line) > 2000 or COMMENT.match(line):  # minified or comment
                continue
            if not is_md:
                if EMOJI.search(GLYPH.sub("", line)):
                    hits.append((path, i, "emoji", "P1", "Emoji in UI -> one line-icon set", line))
                elif GLYPH.search(line):
                    hits.append((path, i, "glyph-icon", "P3", "Dingbat used as icon (✓ ✕ ♡ ★) -> SVG icon; fine inside prose", line))
            for cat, sev, rx, fix in RULES:
                if is_md and not cat.startswith(("slop-copy", "placeholder")):
                    continue
                if cat == "outline-none" and has_focus:
                    continue
                if rx.search(line):
                    hits.append((path, i, cat, sev, fix, line))
    return hits


def main():
    args = sys.argv[1:]

    def opt(name, default):
        if name in args:
            i = args.index(name)
            value = args[i + 1].upper()
            del args[i:i + 2]
            return value
        return default

    min_sev = opt("--min", "P3")
    fail_on = opt("--fail-on", None)
    as_json = "--json" in args
    paths = [a for a in args if not a.startswith("--")]
    if not paths:
        print(__doc__)
        sys.exit(2)
    hits = [h for p in paths for h in scan(p) if h[3] <= min_sev]
    hits.sort(key=lambda h: (h[3], h[2], h[0], h[1]))
    if as_json:
        print(json.dumps([{"file": h[0], "line": h[1], "category": h[2], "severity": h[3],
                           "fix": h[4], "text": h[5].strip()[:200]} for h in hits], ensure_ascii=False, indent=1))
    else:
        counts = {}
        for h in hits:
            counts[(h[3], h[2])] = counts.get((h[3], h[2]), 0) + 1
        print("== Summary ==")
        for (sev, cat), n in sorted(counts.items()):
            print(f"{sev}  {cat:18} {n}")
        print(f"Total: {len(hits)}\n")
        for f, ln, cat, sev, fix, text in hits[:400]:
            print(f"{sev} {cat:16} {f}:{ln}\n    {text.strip()[:140]}\n    -> {fix}")
        if len(hits) > 400:
            print(f"... {len(hits) - 400} more (use --json for all)")
    if fail_on and any(h[3] <= fail_on for h in hits):
        sys.exit(1)


if __name__ == "__main__":
    main()

---
name: deslop-ui
description: Finds and removes "AI slop" design in an existing site, app, admin panel or HTML/CSS/React/Tailwind codebase — emoji icons, purple/indigo gradients, gradient text, glassmorphism, rounded-3xl and shadow-2xl everywhere, invented stats/testimonials, template heroes, fake countdowns, scroll-reveal, pointless animation, cluttered layouts. Scanner script + checklist + fix recipes. Triggers: AI slop, deslop, clean up the design, design audit, UI audit, UX audit, looks AI-generated, looks generic, looks like a template, cluttered, outdated, tidy up.
---

# Deslop UI — clean up an existing design

For new designs use `anti-slop-design`. This skill cleans **existing** code and screens. Functionality, copy and data stay unchanged — only the slop goes, unless the user says otherwise.

## Workflow

### 1. Scope
Which folder, page or component. Read `AGENTS.md` / `CLAUDE.md` / `DESIGN*.md` if present — approved tokens and bans there override this skill. Respect file ownership/locks.

### 2. Automated scan
```bash
python3 -I <skills-dir>/deslop-ui/scripts/slop_scan.py <dir> [--json] [--min P2] [--fail-on P1]
```
Skips `node_modules`, `dist`, `.next`, `build`, vendor and minified files. Each hit: file:line, category, severity, fix hint. Hits are **signals, not verdicts** — check context (a colour swatch named "purple" is fine; `backdrop-blur` on a sticky header may be fine). Expect the scanner to miss most layout-level slop; step 3 is where the real findings come from.

### 3. Visual review (mandatory)
Open the pages in a browser at 1440 and 390px and look at the screenshots yourself. Use the "Visual" questions in [references/slop-catalog.md](references/slop-catalog.md): everything centred, the same three-card rhythm, empty hero space, a weak primary action, repeated photos, mixed alignment, nothing product visible on the first mobile screen.

Measure what screenshots can't show reliably — via the browser console:
- distinct border radii, font sizes, font families and shadow recipes in use (a design system has few of each);
- elements with a gradient background;
- clickable elements without `cursor:pointer`; touch targets under 40px;
- horizontal overflow; sticky header height on mobile.

If a headless or hidden browser pauses animations, sections behind scroll-reveal will look blank — that itself is a finding.

### 4. Report (before changing anything)
Table: `# | P | Where (file:line or screen area) | What you see | Fix`.
- **P1** misleads or confuses the user, or screams "AI-made" (fake urgency, invented numbers, hidden content, no product on first mobile screen).
- **P2** cheap/template look.
- **P3** polish.

Also list what is good ("don't change") so working parts aren't broken, and what you could not verify. If the user only asked for an audit, stop here.

### 5. Clean up
Follow [references/fix-recipes.md](references/fix-recipes.md):
- Fix the token layer first (colour, radius, shadow, type) — components follow.
- Don't touch copy (use `deslop-copy` separately, with permission).
- Invented numbers/testimonials/logos: list them for the user before deleting — they might be real.
- One step = one category, so diffs stay reviewable.

### 6. Re-verify
Re-run the scanner (P1 = 0), take 1440/390 screenshots, check the console is clean and nothing overflows. Show before/after. State what was not verified.

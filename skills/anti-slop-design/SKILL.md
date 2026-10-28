---
name: anti-slop-design
description: Use when designing or redesigning any website, web app, admin panel, mobile/app screen, landing page or brochure. Prevents the "AI slop" look (purple gradients, emoji icons, template hero, invented stats, glassmorphism, centred three-card sections) and enforces a token-first, product-specific design process with mandatory visual verification. Triggers: design, redesign, build a site, UI, UX, landing page, admin panel, screen, page, web design, app design, modernise, simplify.
---

# Anti-slop design

Goal: an interface nobody would describe as "AI-generated". Every decision is made for **this product, this user, this task** — never because it is a default.

Field notes behind these rules: [references/field-notes.md](references/field-notes.md). Slop catalogue: `../deslop-ui/references/slop-catalog.md`.

## 0. Before writing code — five questions

Answer each in a sentence or two. If unknown, look in the project files; if still unknown, ask.

1. **Who uses it, and for what?** An operator processing 300 products a day and a shopper buying one phone do not get the same design.
2. **What is the primary action?** Nothing on the screen may compete with it. "Nice, but I don't know what to do here" is the most common complaint.
3. **Is there a reference?** If so, study its *structure*. Never copy its text, logo, photos or CSS.
4. **What is the real data?** Real product names, prices, images. If missing, label samples once, clearly — never invent numbers.
5. **What is the existing stack?** Don't bring React into a vanilla project or a second CSS system into a Tailwind one.

## 1. Visual system — tokens first

Write a small token set (CSS custom properties or Tailwind `@theme`) before any component.

- **Colour:** one brand colour + tinted neutrals + 1–2 status colours. The brand colour is a *signal* (primary action, active state, discount), not a page wash. Tint neutrals towards the brand instead of pure `#000`/`#fff` or stock `gray-*`.
- **Type:** at most 2 families; a 4–5 step scale (e.g. 32/21/14/12) with paired line heights. Check the font covers every script you ship (ə ğ ı ş, Cyrillic, etc.).
- **Spacing:** a 4- or 8-based scale. Fixed sizes: top bar 56–64px, buttons 36–44px, sidebar 260–300px.
- **Radius:** one value (6–8px) plus pill only for chips/badges. `rounded-2xl/3xl` everywhere is slop.
- **Shadow:** none, or one level for dropdowns/dialogs. Separate cards with a 1px border.
- **Icons:** one line-icon set (Lucide, Tabler, or your own SVG), 16–20px, one stroke width. **No emoji in UI.**
- **Motion:** 120–200ms, only when state changes. Support `prefers-reduced-motion`. No scroll-reveal, no `hover:scale-105`, no shimmering gradients.

## 2. Layout by product type

- **Work tools (admin, back office, studio):** list/catalogue on the left, workspace on the right; dense tables; status as text + colour; primary action fixed bottom or top-right. No decorative KPI cards or marketing headers.
- **E-commerce:** product before promotion; catalogue and search never hidden behind a hero. Fixed image ratio (1:1); dynamic badges never shift the grid. 4–6 key specs next to the price. Mobile is the primary surface — products must appear on the first screen.
- **Corporate site:** real photography (consistent daylight palette, no watermarks), full-width hero with large primary choices directly under it, left-aligned rhythm, 4-column footer. Diagonal splits, abstract blobs and 3D illustrations read as templates.
- **Documents/brochures:** if told "don't touch the words", change no text — only type, spacing, grid and hierarchy.
- **Every section must earn its place.** Hero → 3 icon cards → "10K+ customers" strip → testimonial carousel → "Ready to start?" CTA is the canonical slop sequence. Include a section only when real content exists.

## 3. UX rules

- **One screen, one obvious next step.** When data is missing, the primary button names the exact next action ("3 photos missing — find them"), not "Continue".
- **Don't add buttons for things that can be automatic** (e.g. auto-save drafts instead of a "Save to drafts" button).
- **State must survive navigation.** A removed or selected item must not reappear when the user comes back.
- **Large sections collapse** (+/−) and close when the task is done.
- **Don't change behaviour you weren't asked to change.** "Make it editable" does not mean "turn off auto-selection".
- **Bulk actions** show the plan/diff first, then run; failures stay visible with a reason.
- **Cursor & focus:** `cursor: pointer` on everything clickable, a visible `:focus-visible`. On mobile, focusing search must not hide the logo or header.
- **No fake urgency:** countdowns only with a real, server-side end date.
- **Languages:** each locale gets its own copy; no mixed languages.

## 4. Content honesty

- Invented statistics, client logos, testimonials, certificates, "500+ projects" — **forbidden**. No real fact → remove the section, or mark the sample once (e.g. in the footer), not under every block.
- Product images: exact model and colour, clean background, no people/hands/text/watermarks. If no correct image exists, show an empty slot — never another model's photo.
- For copy, use the `deslop-copy` skill.

## 5. Verification (mandatory before hand-off)

1. Open it in a real browser at **1440, 1280 and 390px**. No horizontal overflow, JS errors or blank screens.
2. Look at the screenshots yourself — reading code is not enough.
3. Run `python3 -I <skills-dir>/deslop-ui/scripts/slop_scan.py <dir>`; fix each hit or note why it stays.
4. Text contrast ≥ 4.5:1, touch targets ≥ 40px.
5. In the hand-off, state what you verified and what you **did not** (live server, real data, other locales). An agent's approval is not the client's approval.

When variants are requested: two (A/B), same content, only the differing part changes — the user chooses.

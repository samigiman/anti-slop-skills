---
name: deslop-copy
description: Finds and removes AI-slop writing in website, app, admin-panel, brochure and marketing copy (English, Azerbaijani, Russian) — "unlock", "seamless", "next level", "inqilabi həllər", "инновационные решения", invented numbers, empty triplets, dashes and exclamation marks everywhere. Use both when writing new UX copy and when cleaning existing text. Triggers: copy sounds AI-written, clean up copy, deslop text, UX copy, button label, error message, website copy, clean up a blog post, AI slop text.
---

# Deslop copy — remove AI slop from text

Rule: **a concrete fact beats an adjective.** Every sentence either tells the user something or helps them do something. If it does neither, it goes.

If the user said "don't touch the words", do not run this — only list findings.

## Symptoms

**English:** unlock, unleash, supercharge, seamless, effortless, elevate, empower, revolutionize, game-changer, next-level, cutting-edge, robust, leverage, delve, tapestry, "in today's fast-paced world", "whether you're X or Y", "not just X — it's Y".

**Azerbaijani:** "inqilabi", "innovativ həllər", "müasir həllər", "növbəti/yeni səviyyəyə", "sərhədsiz imkanlar", "rəqəmsal dünyada", "möhtəşəm/unikal təcrübə", "kəşf edin", "sizin üçün buradayıq", "keyfiyyət və etibarlılıq", "peşəkar komanda" (without proof), "biz sadəcə … deyilik, biz …", "gələcəyə doğru".

**Russian:** "инновационные решения", "новый уровень", "безграничные возможности", "уникальный опыт", "в современном мире", "откройте для себя".

**Structure:**
- Triplets everywhere ("Fast. Reliable. Professional.").
- An em dash or colon for drama in every line.
- Exclamation marks; a question in every heading ("Ready?").
- A subtitle that repeats the heading.
- Invented numbers, "thousands of customers", unproven "#1".
- Emoji bullets.
- English Title Case Forced Onto Other Languages.

## Method

1. **Find the fact:** what in the sentence is verifiable? (number, time, place, product name, condition). If nothing — check project files or ask the user; never invent.
2. **Rewrite:** fact + user benefit, active verb, short.
   - "Take your business to the next level with innovative logistics solutions" → "Road and sea freight from Baku to Europe. Quotes answered within one business day."
   - "Seamless checkout experience" → "Pay in 3 steps. No account needed."
3. **Delete:** if no fact exists, delete the sentence — empty space beats a lie.

## UX microcopy rules

- Button = verb + object: "Find photos", "Confirm order". Not a lone "Continue", "OK", "Submit".
- Error = what happened + what to do: "The server didn't respond. Check the connection and try again." No stack traces for users.
- Empty state = why it is empty + one action.
- Status in words ("Verified", "Pending", "Rejected"), not colour alone.
- One term, one meaning: "draft" is never also "project" elsewhere.
- Each locale has its own copy; no mixed languages (brand/model names excepted). Use correct native characters.
- Keep the form of address consistent.

## Report format

`# | Where | Before | After | Reason`. Don't change live copy without the user's approval; ask the user to confirm any claim that could be invented ("12 years of experience").

Scan: `python3 -I <skills-dir>/deslop-ui/scripts/slop_scan.py <dir> --min P2` (categories `slop-copy`, `slop-copy-az`, `slop-copy-ru`, `fake-stats`, `placeholder`).

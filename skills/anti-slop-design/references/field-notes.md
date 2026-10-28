# Field notes

These rules come from real client and owner feedback on production projects (an electronics retailer's storefront and admin, an internal product-data tool, a logistics company site, an education agency site, a training brochure). Names are removed; the lessons are not.

## Internal product-data tool

| What the user said | Rule |
|---|---|
| "The design is cluttered and outdated" | Fewer sections, clear hierarchy, calm modern neutrals; no old-school gradient panels |
| "It looks fine, but we don't know what to do" | One primary action per screen; visible steps |
| "Stop putting silly emojis in, use clean minimal icons" | No emoji in UI; one line-icon set |
| "Why is there a 'Send to drafts' button? It should go to drafts when I leave" | Don't add buttons for automatic behaviour |
| "I removed a photo, switched product, came back — it was there again" | Preserve state across navigation |
| "Let me collapse the photo section, it takes too much space" | Large sections collapse (+/−) |
| "I asked to make it editable, not to turn off auto-select" | Don't change unrequested behaviour |
| "Make the review step like Tinder — softer, nicer" | Repetitive decisions: one card at a time, two clear buttons |
| "Make the UI faster and simpler" | Speed is design: fewer requests, skeletons, optimistic UI |
| "It brings made-up photos — a white phone for a black one" | Data and images must match exact model and colour; show the real count when fewer exist |

An approved system from that project, as a concrete example of "calm": background `#f8f9f6`, surface `#fff`, text `#253a32`, muted `#768079`, accent `#315747`, selection `#e7eee7`, border `#e1e6df`, warning `#946329`; type 32/21/14/12px; top bar 64px, catalogue 300px; buttons 40px, radius 8px; 18px line icons at 1.7px; motion 160ms. "No large decorative cards, sales statistics or marketing headline."

## Electronics storefront

- Brand red is a signal, not a page wash, and not the only hue.
- Product clarity before promotion; catalogue and search never behind a hero; the first experience is not a marketing landing page.
- Product cards: fixed image ratio; dynamic badges never resize the grid.
- Never copy a competitor's layout, icons, copy, photography or CSS.
- Admin: "orders, customers and overview are all a mess" → dense tables, clear status, bulk-safe controls.
- "The top area is confusing, people get lost" → fewer header elements.
- The cursor sometimes showed a hand, sometimes an arrow → `cursor:pointer` on every interactive element.
- On a narrow phone, focusing search hid the logo → test every mobile header state.
- An audit found a "deal of the week" countdown that restarted for each visitor → fake urgency; remove or make it real.
- An audit found every below-the-fold section hidden until scrolled into view → when the observer stalls, the page is blank. Render content visible.

## Logistics company site

- The client rejected three landing pages, then said a later version was "awful, I can't show this to my customer".
- Review verdict: a diagonal navy/photo split hero "looks like a generic template". The chosen fix: full-width daylight photo with large service tiles (≥120px tall, 40–48px icons, 18px labels).
- A grey "sample / pending approval" note under every section cheapened the whole presentation → one global note.
- Don't repeat the same photo scene; a sunset photo breaks a daylight palette.
- Centred headings over left-aligned content break rhythm.
- Use the same wordmark rule in header and footer; use a chevron, not an arrow, for dropdowns.

## Other

- Brochure: "Don't touch the words, just tidy up the design" → text is untouchable.
- macOS mini-app: "It doesn't look like a Mac app" → on native platforms use system fonts, native controls and the platform's spacing and icon language.
- Agent approval (Claude, Codex, etc.) is not client approval — say so in the hand-off.

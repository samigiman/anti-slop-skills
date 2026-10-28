# Fix recipes

## Token layer (do this first)
```css
:root{
  --bg:#f8f9f6; --surface:#fff; --text:#1f2a24; --muted:#6b756f;
  --line:#e1e6df; --accent:/* brand */; --accent-ink:#fff;
  --ok:#2f6b45; --warn:#946329; --err:#b3261e;
  --r:8px; --r-pill:999px;
  --s1:4px; --s2:8px; --s3:12px; --s4:16px; --s5:24px; --s6:32px; --s7:48px;
  --fs-h1:32px/38px; --fs-h2:21px/28px; --fs-body:14px/21px; --fs-note:12px/18px;
  --ease:160ms ease;
}
@media (prefers-reduced-motion:reduce){*{transition:none!important;animation:none!important}}
```
Take the values from the project's existing brand; this only shows the shape.

## Tailwind replacements
| Slop | Replacement |
|---|---|
| `bg-gradient-to-r from-purple-600 to-pink-500` | `bg-[var(--accent)]` or `bg-brand` |
| `bg-clip-text text-transparent bg-gradient-…` | `text-[var(--text)] font-semibold` |
| `rounded-2xl` / `rounded-3xl` (cards) | `rounded-lg` (8px) |
| `shadow-xl` / `shadow-2xl` (cards) | `border border-[var(--line)]` |
| `backdrop-blur-xl bg-white/10` (cards) | `bg-[var(--surface)] border` |
| `hover:scale-105 transition-all duration-300` | `transition-colors duration-150 hover:bg-…` |
| `animate-bounce` / `animate-pulse` (decor) | remove; pulse only for skeletons |
| `text-center` on every section | `text-left` + grid |
| `text-6xl md:text-7xl tracking-tight` | `h1` from the scale (28–40px) |

## Emoji → icons
1. Find emojis (scanner category `emoji`).
2. Write down what each means (🚚 → delivery). No meaning → delete it, no icon either.
3. Use the project's icon set if it has one (e.g. `lucide-react`); otherwise inline SVG with `stroke="currentColor" stroke-width="1.75" fill="none"`, 18px.
4. `aria-hidden="true"` on decorative icons, `aria-label` on meaningful ones.

## Template hero → working hero
- Centred heading + 2 buttons + blob → heading on the left (≤ 2 lines) + one sentence + one primary button; real photo or product on the right/behind; primary choices (services/categories/search) right below.
- Height 480–560px desktop; on 390px mobile, heading ≤ 3 lines and something useful (products, categories) visible on the first screen.

## Feature cards → content
- 3 icon cards ("Fast / Reliable / Professional") → a real list of services with links, or a two-column "what we do / how", or delete.

## Invented social proof
- No real data: delete the section. If the user wants to keep it, mark it as a placeholder once; never invent a number.

## Fake urgency
- Countdown without a real end date → remove, or drive it from a server-side end date that is the same for every visitor. Never restart a timer per visitor.

## Scroll-reveal
- Remove the hide-until-visible rules (`opacity:0` + observer). If a subtle entrance is wanted, animate only from an already-visible state and never gate visibility on JS.

## Admin/panel cleanup
- Delete decorative KPI cards → one line of real counts at the top ("263 drafts · 17 awaiting decision").
- Tables: sticky header, right-aligned numbers, status chips with text + colour, rows 40–44px.
- One primary action, secondary actions as `ghost`, destructive actions red and confirmed.

## Motion
- Keep: dropdown/dialog open, selection highlight, skeletons.
- Remove: scroll-reveal, parallax, grow-on-hover, spinning icons, typing effects.

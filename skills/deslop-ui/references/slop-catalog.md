# AI-slop catalogue — UI and web

Each entry: **symptom → why it's slop → replacement**.

## Colour
- **Purple/indigo/fuchsia gradients** (`#6366f1`, `#8b5cf6`, `#a855f7`, `#ec4899`, `from-purple-* via-pink-*`) → the default of every AI demo → the brand's own colour, solid fill.
- **Gradient text** (`bg-clip-text text-transparent`) → "wow" effect, poor legibility → solid text, emphasis through weight.
- **Dark background + neon glow** → crypto/SaaS template → only if the brand truly calls for it.
- **Stock Tailwind greys everywhere** → no identity → neutrals tinted towards the brand.
- **Brand colour everywhere** (backgrounds, headings, icons, borders, every card button) → the signal is lost → primary action, active and selected states only.
- **Gradients on every surface** (top strip, hero, deal box, buttons, tiles) → flat fills; at most one deliberate gradient.

## Shape and depth
- **Glassmorphism** on every card → 2021 Dribbble → solid surface + 1px border.
- **rounded-2xl/3xl everywhere**, pill buttons, 24px cards → toy-like → one radius (6–8px). Seven different radii in one page = no system.
- **shadow-xl/2xl on cards**, coloured shadows under buttons → floating blocks → border or one light shadow.
- **Abstract blobs, gradient orbs, noise, grid-line backgrounds** → meaningless decoration → real photo/product or nothing.

## Icons and imagery
- **Emoji in UI** (🚀 ✨ 💡 🔥 ✅ 📦 🎯 ⚡) → the clearest AI tell → one line-icon set.
- **An icon next to every heading**, icons in tinted circles/boxes → decoration → icons only where they carry meaning.
- **3D/isometric illustrations, AI-generated stock people** → fake → real photography; otherwise typography.
- **The wrong product's photo** (other model or colour) → a lie → the exact image or an empty slot.

## Layout
- **The template sequence:** centred hero with two buttons → 3 icon feature cards → "10K+ / 99.9% / 24/7" strip → testimonial carousel → 3-column pricing → "Ready to start?" CTA → all centred.
- **Everything `text-center`** → no rhythm → left-aligned grid; centre only short blocks.
- **Diagonal/curved split hero** → generic → full-width photo + large primary choices.
- **Same-size card grid in every section** → monotone → shape follows content (table, list, two columns).
- **Empty or 100vh hero** → content falls below the fold → ~480–560px desktop, ~260–300px mobile, primary action right under it.
- **Duplicate logo** in header and hero.
- **Carousel controls on top of the product image.**
- **Badges shift the grid** → layout shift → fixed slot height.

## Motion
- `hover:scale-105`, `transition-all`, decorative `animate-bounce/pulse/ping`, fade-up on every block → cheap → 120–200ms state changes only; `prefers-reduced-motion`.
- **Scroll-reveal** (sections at `opacity:0` until an observer fires) → if JS, the observer or animations stall, the page is blank; also hurts screenshots and crawlers → render visible.

## Typography
- **Default Inter/Poppins only**, giant `text-6xl/7xl` heading with `tracking-tight` and a small grey subtitle → SaaS template → a fitting family and a 4–5 step scale. Eight font sizes on one page = no scale.
- **One word in the heading highlighted in colour/gradient** → cliché.
- **ALL-CAPS labels with wide tracking everywhere.**

## Content (visual side)
- **Invented numbers** ("500+ clients", "99.9% uptime", "10x faster"), fake testimonials (name + avatar + 5 stars), fake client logos.
- **Empty social proof**: "0 reviews ☆☆☆☆☆" above the fold → hide the rating row when there are no reviews.
- **Fake urgency**: a countdown with no real end date, or one that restarts per visitor.
- **Lorem ipsum / "Your Company" / "John Doe"** on a live page.
- **A "sample / pending approval" note under every section** → one global note.

## UX
- Unclear primary action; 4–5 buttons at the same level.
- Unnecessary confirmation/intermediate buttons for things that could be automatic.
- Missing `cursor:pointer`; missing `:focus-visible`; `outline:none` with no replacement.
- Toasts/modals confirming everything.
- Mobile: horizontal overflow, targets under 40px, a sticky header taking 15%+ of the screen, header elements disappearing on focus, cookie banner + promo strip + header + hero leaving no product on the first screen.

## Questions for the visual pass
1. In 3 seconds: what is this site and what is the primary action?
2. Swap the logo — could it be anyone else's site? If yes, it's slop.
3. Which element is specific to *this* product? None → slop.
4. What would be lost if you deleted it? Nothing → delete it.

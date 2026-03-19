# Batch 04 — UI/UX Style Audit Report

**Auditor:** UI Designer Agent
**Date:** 2026-03-20
**Styles Reviewed:** paper-cut, marble, terrazzo, origami, tactile-ui
**Scope:** Both A-Side and B-Side for each file

---

## Paper Cut (`paper-cut.html`)
**Style Authenticity Score: 7/10**

### Fonts
- **Family:** Nunito (weights 300, 400, 600, 700) loaded via Google Fonts `<link>` tag (line 8).
- **Appropriateness:** Nunito is a rounded sans-serif that works reasonably well for a friendly, crafted paper aesthetic. However, a more "handmade" or slightly irregular font (e.g., Patrick Hand, Architects Daughter, or a rounded geometric like Quicksand) would better reinforce the paper-craft metaphor. Nunito is too polished for a truly handcrafted look.

### Colors
- **A-Side Palette:**
  - Background: `#F0EBE3` (warm off-white)
  - Layers: `#F8E8D4` (warm peach), `#D4E8F0` (powder blue), `#E8D4E8` (lilac)
  - Text: `#3D3D3D` (dark gray), `#6B6B6B` (muted gray), `#2D2D2D` (near-black headings)
  - Accent: `#7A5C8D` (muted purple, hover only), `#5A3E6B` (button text)
  - Cards: `#FFF` on `#F0EBE3` background
- **B-Side Palette:**
  - Background: `#F0E8D4` (warm cream)
  - Accent: `#D4896B` (terracotta/copper)
  - Text: `#5C4A3A` (warm dark brown), `#8B7B68` (muted brown)
  - Cards: `#F8F0E4` (light cream), shadows `#E8DCC8` and `#E0D4C0` and `#D4C8B4`
- **Contrast ratios:** The `#8B7B68` text on `#F0E8D4` background yields roughly 3.2:1, which fails WCAG AA for normal-size body text (needs 4.5:1). Body copy in cards (`#8B7B68` on `#F8F0E4`) is even worse at approximately 2.8:1.
- **Accent usage:** Appropriate. Warm pastels match the paper-craft narrative. The B-Side uses a cohesive terracotta accent throughout.

### Layout
- **A-Side hero:** 70vh min-height, flex column, 2rem padding, left-aligned content (max-width 480px). The hero features three curved layers at the bottom using `border-radius: 50%` on absolutely positioned elements (lines 16-19). This works but the layers are only 120px tall.
- **B-Side hero:** 80vh min-height, centered layout (max-width 640px). Standard centered hero with tag, heading, paragraph, and button row.
- **Section spacing:** A-Side uses 3rem padding on `.components`. B-Side uses 5rem padding on `.bsec` sections with `max-width: 1100px` container.
- **Responsive:** Mobile breakpoint at 600px (A-Side) and 768px (B-Side). A-Side only adjusts h1 font-size and nav gap. B-Side hides nav entirely, reduces min-height and padding, switches to single-column grid.

### Sizing
- **Typography scale:**
  - A-Side: h1 `3rem` (48px), h2 `0.75rem` (12px, section label), h4 `1.1rem` (17.6px), body `1rem`
  - B-Side: h1 `clamp(2.5rem, 6vw, 4rem)`, h2 `1.8rem`, h3 `1.05rem`, body `0.88rem`, tag `0.8rem`, metrics `2.2rem`
- **Padding/margins:** Cards have 2rem padding in both sides. B-Side grid gap is 1.5rem. Section padding is generous at 5rem vertical.
- **Element proportions:** A-Side swatches are 48x48px. B-Side card icons are 40x40px. Buttons at 0.8rem padding vertical, 2rem horizontal.

### Sections
- **Current sections:** Hero, feature cards (3), metrics (4), quote, footer. This is the standard template structure.
- **Effectiveness:** The structure serves adequately but misses a major opportunity. Paper-cut style is fundamentally about visible layering and overlapping elements, which is hard to demonstrate in a flat card grid.
- **Better sections would include:**
  - A full-bleed section where "paper" layers visually overlap with wave-shaped clip-path dividers
  - A cutout section where content appears through windows in an upper layer
  - Step-by-step or timeline section with progressively stacked paper cards showing depth buildup
  - Collage-style hero with overlapping rectangular shapes at varied z-indices

### Visuals
- **A-Side pseudo-elements:** Cards use `::before` and `::after` with inset offsets and shadow halos (lines 43-50), creating a subtle stacked-paper effect. The hero has three absolutely positioned curved layers (`.layer-1`, `.layer-2`, `.layer-3`) at the bottom. This is the strongest paper-cut element in the file.
- **B-Side pseudo-elements:** Cards use `::before` (bottom -4px, offset left/right) and `::after` (bottom -8px, further offset) with solid background colors `#E0D4C0` and `#D4C8B4` (lines 111-112). This is a good stacked-paper simulation.
- **Missing elements:** No `clip-path` usage anywhere. No wave or organic-edge dividers. No cutout shapes. The visual DNA spec calls for hard offset shadows (e.g., `box-shadow: 6px 6px 0`) but the A-Side uses blurred shadows instead. The B-Side uses `box-shadow: 0 2px 0 #E8DCC8, 0 4px 0 #E0D4C0, 0 6px 12px rgba(0,0,0,.06)` which is closer but still includes a blurred component.
- **Background treatments:** A-Side body is flat `#F0EBE3`. B-Side body is flat `#F0E8D4`. Neither has a paper texture.

### Animations
- **@keyframes:** None defined.
- **Transitions:** A-Side button has `transition: all 0.3s` with hover `translateY(-2px)` and shadow expansion. B-Side buttons hover with `opacity: .9` and `translateY(-1px)`. Cards hover with `translateY(-3px)`.
- **Motion appropriateness:** The subtle vertical shifts are fine. For paper-cut, gentle lifts suggesting a paper piece peeling up from the surface would be ideal. Currently the animations are too generic.

### Content
- **Brand names:** "Papier" (A-Side), "Paperie" (B-Side). Both are charming and on-theme.
- **Hero copy:** A-Side: "Depth Through Layered Simplicity" with supporting text about stacked paper, pastels, and shadows. B-Side: "Cut, Layer & Create." Both are strong and directly reference the paper-cut aesthetic.
- **Card titles:** A-Side: "Parchment Layer," "Sky Sheet," "Lilac Fold" -- evocative and on-theme. B-Side: "Stacked Layers," "Soft Pastels," "Paper Depth" -- more descriptive but effective.
- **Metrics:** B-Side uses "3 Layers," "Infinity Colors," "0 Digital Feel," "100% Handmade." These are creative and reinforce the handmade metaphor.
- **Quote:** B-Side: "It looks like someone lovingly assembled each page from colored paper. Beautiful." Attributed to "Craft Weekly." Perfectly on-brand.

### Specific Fix Recommendations
1. **Add hard-offset shadows instead of blurred ones.** Replace `box-shadow: 0 2px 4px rgba(0,0,0,0.04), 0 4px 12px rgba(0,0,0,0.06)` with `box-shadow: 4px 4px 0 rgba(0,0,0,0.1)` to match the paper-cut DNA spec's signature technique.
2. **Introduce `clip-path` wave dividers between sections.** Add `clip-path: polygon()` or SVG wave shapes as section separators to replace the flat `border-top` dividers. This is the single most impactful change for style authenticity.
3. **Fix contrast ratios on B-Side.** Darken body text from `#8B7B68` to at least `#6B5A48` to meet WCAG AA 4.5:1 ratio against the cream backgrounds.
4. **Add paper texture to background.** A subtle repeating noise or fiber pattern via CSS would enhance the material feeling.
5. **Use flat colors per layer.** The visual DNA spec specifically says "flat colors with no gradients within each paper layer." Both sides comply, which is good, but the B-Side cards could benefit from more distinct color per card rather than all being `#F8F0E4`.

---

## Marble (`marble.html`)
**Style Authenticity Score: 8/10**

### Fonts
- **Family:** Cormorant Garamond (weights 400, 500, 600, 700 + italic 400) for headings, Inter (weights 300, 400) for body. Loaded via two Google Fonts `<link>` tags (lines 8 and 104 -- note the second is redundant with slightly different weight selection).
- **Appropriateness:** Excellent choices. Cormorant Garamond is a refined, high-contrast serif that evokes luxury engraving, which is precisely what the marble/luxury DNA calls for. Inter as body text provides clean readability without competing with the serif headlines.

### Colors
- **A-Side Palette (CSS custom properties, line 11):**
  - `--white: #F8F9FA` (near-white marble base)
  - `--gray: #DEE2E6` (light gray vein color)
  - `--dark-gray: #ADB5BD` (medium gray)
  - `--gold: #C9A84C` (warm gold accent)
  - `--gold-light: #E8D999` (light gold, defined but unused in CSS)
  - `--text: #343A40` (dark text)
  - `--dim: #868E96` (muted text)
- **B-Side Palette:**
  - Background: `#F8F9FA` with subtle linear gradient
  - Gold accent: `#C9A84C` used extensively (logo, tags, borders, metrics, icons)
  - Text: `#3D3D3D` (dark), `#6C757D` (muted gray)
  - Cards: `#FFFFFF` with `border: 1px solid rgba(201,168,76,.3)` (gold-tinted border)
- **Contrast ratios:** `#868E96` on `#F8F9FA` yields approximately 3.5:1, borderline failing for normal body text. The B-Side `#6C757D` on `#F8F9FA` is similar at roughly 4.1:1, which just barely passes for body at 16px+. At 14px (0.88rem), this fails.
- **Accent usage:** Gold is used consistently and appropriately as the singular luxury accent. The limited palette of white/gray/gold is a hallmark of marble aesthetics.

### Layout
- **A-Side hero:** Centered text, 64px top padding, 52px bottom. The `.gold-line` decorative divider (60px wide, 2px tall) sits above the h1. Cards grid at max-width 960px with 260px minimum column width.
- **B-Side hero:** 80vh min-height centered hero, max-width 640px inner content. Standard tag/heading/paragraph/buttons structure.
- **Symmetry:** Both sides properly center content, which matches the spec's call for "centered, symmetrical compositions."
- **Section spacing:** A-Side uses tighter spacing (40px section title padding, 48px card section bottom padding). B-Side uses 5rem (80px) vertical section padding.
- **Responsive:** A-Side has a single 600px breakpoint switching the `.features` grid to 1 column. B-Side has a 768px breakpoint hiding nav, reducing hero height and padding.

### Sizing
- **Typography scale:**
  - A-Side: h1 `52px`, section-title `32px`, card h3 `22px`, hero p `15px`, body `14px`, nav links `12px`, footer `14px`
  - B-Side: h1 `clamp(2.5rem, 6vw, 4rem)`, h2 `1.8rem`, h3 `1.05rem`, body `0.88rem`, tag `0.8rem`, quote `1.3rem`
- **A-Side letter-spacing:** Logo `4px`, nav links `2px`, section-sub `2px`, feature labels `2px`, testimonial cite `2px`, footer `2px`. This consistent use of generous letter-spacing creates an engraved, luxury feel -- very well done.
- **Element proportions:** Cards have 28px padding. The `.card-icon` is a 40x2px gold line (line 31), acting as a minimal decorative divider within cards. The veined divider element is 60px tall.

### Sections
- **Current sections:** Hero with gold-line divider, card trio ("The Collection"), veined divider, 2x2 features grid (metrics), testimonial, footer.
- **Effectiveness:** The 2x2 bordered feature grid (`.features`, line 36) is a strong design element that feels like an architect's specification sheet. The veined divider with its rotated diamond center (`.veined-divider`, lines 34-35) is clever.
- **Better sections would include:**
  - A full-width marble texture banner with gold-foil text overlay
  - Before/after slider showcasing different marble varieties (Calacatta, Statuario, etc.)
  - A horizontal scrolling gallery of marble patterns
  - A section with `background-clip: text` to show marble veining through large display text

### Visuals
- **A-Side marble background:** The `.marble-bg` class (line 13) uses a triple-layered gradient: a main `linear-gradient(135deg)` with multiple color stops for tonal variation, plus two `repeating-linear-gradient` layers (at 120deg and 60deg) with thin 1px semi-transparent lines simulating veins. This is a solid CSS-only marble texture.
- **A-Side gold-line:** Simple centered gradient (`transparent -> gold -> transparent`) creating an elegant horizontal rule.
- **A-Side veined-divider:** A vertical gradient band with a rotated diamond shape (created via `::after` pseudo-element with borders, line 35). Has a `transform` property declared twice (bug), but browsers will use the last one.
- **B-Side card accent:** Each `.bcard` has a `::before` pseudo-element creating a 2px gold gradient line across the top (line 96). Subtle and effective.
- **B-Side footer accent:** A `::before` pseudo-element creates a 40x1px gold line centered above the footer content (line 99).
- **B-Side background:** A simple linear gradient (`#F8F9FA` to `#EEF0F2` and back), which suggests tonal marble variation but lacks the vein detail of the A-Side.
- **Missing:** No actual marble vein SVG texture in the B-Side. No `background-clip: text` effect. No `border-image` with gold gradient.

### Animations
- **@keyframes:** None defined.
- **Transitions:** A-Side card hover: `box-shadow .3s` transition to `0 8px 30px rgba(0,0,0,.06)`. Button: `transition: all .3s` with hover fill change (gold background). B-Side card hover: `translateY(-3px)`. Buttons: `translateY(-1px)`.
- **Motion appropriateness:** The restrained, subtle transitions are appropriate for a luxury aesthetic. Marble should feel still, heavy, and permanent. No bouncing or playful motion needed.

### Content
- **Brand names:** "Pietra" (A-Side, Italian for "stone"), "AUREUM" (B-Side, Latin for "golden"). Both are excellent luxury brand names with appropriate cultural connotations.
- **Hero copy:** A-Side: "Carved from Living Stone" with italic gold "Living Stone." B-Side: "Polished Perfection." Both convey luxury craftsmanship.
- **Card titles:** A-Side: "Calacatta Oro," "Statuario Venato," "Nero Marquina" -- actual marble variety names with accurate descriptions. This is exceptional content authenticity.
- **Metrics:** A-Side: "47 Varieties, 12 Quarries, 200+ Projects, 1891 Established." B-Side: "Est. 1897, 100% Handcrafted, Global Presence, Eternal Quality." Both support the luxury narrative.
- **Quote:** A-Side: "The stone speaks if you know how to listen..." -- poetic and fitting. B-Side: "An unparalleled experience of luxury..." from "Luxury Living Magazine" -- appropriate but more generic.
- **Footer:** A-Side: "Pietra Atelier ~ Milano ~ MMXXVI" -- the Roman numerals are a nice luxury touch.

### Specific Fix Recommendations
1. **Add marble vein texture to B-Side background.** Copy or adapt the A-Side's triple-layered gradient technique (`marble-bg` class, line 13) to the `.b-side` selector. The current simple linear gradient is too plain.
2. **Fix the duplicate `transform` on `.veined-divider::after`** (line 35). The property is declared twice with different values (`translate(-50%,-50%)` then `translate(-50%,-50%) rotate(45deg)`). Remove the first declaration.
3. **Remove the duplicate Google Fonts link** (line 104). It loads Cormorant Garamond a second time with slightly different weight options and the italic variant. Merge into a single `<link>` tag.
4. **Improve body text contrast.** Darken `#868E96` (A-Side `--dim`) to at least `#6C757D` and darken B-Side `#6C757D` to `#5A6368` for safe WCAG AA compliance at small text sizes.
5. **Add `background-clip: text` treatment** to at least one heading to showcase marble texture through typography, which is a signature marble-style technique listed in the visual DNA.

---

## Terrazzo (`terrazzo.html`)
**Style Authenticity Score: 7.5/10**

### Fonts
- **Family:** Poppins (weights 300, 500, 700) loaded via Google Fonts (line 8).
- **Appropriateness:** Poppins is a geometric sans-serif that suits terrazzo's contemporary, design-studio feel. Its rounded terminals echo the organic shapes of terrazzo chips. This is a solid font choice for the style.

### Colors
- **A-Side Palette (CSS custom properties, line 11):**
  - `--base: #E8D5B7` (warm sand)
  - `--dark: #3A3530` (dark brown-black)
  - `--rose: #D4726A` (dusty rose/coral)
  - `--teal: #5BA6A6` (muted teal)
  - `--gold: #D4A843` (warm ochre/gold)
  - `--lavender: #9B7DB8` (soft purple)
  - `--sage: #7FA87F` (muted green)
- **B-Side Palette:**
  - Background: `#E8D5B7` (same warm sand as A-Side)
  - Primary accent: `#E88D97` (soft pink, different from A-Side `--rose`)
  - Secondary colors: `#7BC8C4` (teal on 2nd card icon), `#DBA159` (amber on 3rd card icon)
  - Text: `#5C4A3A` (warm dark brown), `#8B7B68` (muted brown)
  - Cards: `#FFFFFF` with `box-shadow: 0 2px 8px rgba(0,0,0,.06)`
  - Tertiary accent: `#9B8EC6` (purple, in background speckle only)
- **Contrast ratios:** `#8B7B68` on `#E8D5B7` yields approximately 2.8:1 -- fails WCAG AA. The B-Side `#5C4A3A` on `#E8D5B7` yields roughly 5.2:1 -- passes. Body text in cards (`#8B7B68` on `#FFFFFF`) is about 3.8:1 -- fails for text below 18.67px bold.
- **Accent usage:** The multi-color chip palette is essential for terrazzo authenticity. The A-Side has 5 accent colors; the B-Side only actively uses 3 (pink, teal, amber) plus a fourth purple in the background only. More color variety would better represent terrazzo's characteristically diverse aggregate.

### Layout
- **A-Side hero:** Center-aligned, 60px top / 80px bottom padding, full-width. Heading uses `clamp(36px, 6vw, 64px)` responsive sizing. Cards grid at 260px minimum columns, 24px gap.
- **B-Side hero:** 80vh min-height centered, max-width 640px.
- **Section spacing:** A-Side cards have 32px horizontal padding, 60px bottom. B-Side uses 5rem vertical section padding.
- **Background treatment:** A-Side has `.terrazzo-bg::before` (lines 14-29) as a fixed overlay with 14 `radial-gradient` circles at scattered positions, at 0.6 opacity. B-Side has `.b-side::before` (line 105) as a `position: fixed` overlay with 6 `radial-gradient` speckles at 0.4 opacity.
- **Responsive:** A-Side has no explicit breakpoint. B-Side has 768px breakpoint.

### Sizing
- **Typography scale:**
  - A-Side: h1 `clamp(36px, 6vw, 64px)`, h3 `18px`, body `16px`, card body `13px`, nav `14px`, footer `12px`
  - B-Side: h1 `clamp(2.5rem, 6vw, 4rem)`, h2 `1.8rem`, h3 `1.05rem`, body `0.88rem`
- **Chip/chip labels:** A-Side chips are `11px` font with `4px 12px` padding and `border-radius: 20px` (pill shape).
- **Swatches:** A-Side palette swatches are 48x48px circles (border-radius: 50%). B-Side has no explicit palette section.

### Sections
- **Current sections:** Hero, three feature cards, palette swatches (A-Side only), metrics (B-Side), quote (B-Side), footer.
- **Effectiveness:** The card grid is clean but generic. The A-Side's palette section is a good material showcase. The B-Side terrazzo speckle background is the most authentic element.
- **Better sections would include:**
  - A "material samples" grid showing different terrazzo base colors with varying chip mixes
  - A zoomed-in detail section with a large terrazzo texture and callout annotations for each chip color
  - A mosaic-style image gallery where photos are set into irregular terrazzo-chip-shaped masks
  - An interactive color mixer section where users see chip colors against different base tones

### Visuals
- **A-Side terrazzo pattern:** The `::before` pseudo-element (lines 14-29) uses 14 layered `radial-gradient` circles of varying sizes (3px to 8px) at scattered coordinates, in all five accent colors. This creates a convincing terrazzo speckle effect. The 0.6 opacity creates a subtle background without overwhelming content.
- **B-Side terrazzo pattern:** The `.b-side::before` (line 105) uses only 6 `radial-gradient` speckles (sizes 2-4px), which is significantly sparser than the A-Side. Being `position: fixed`, it stays in place while content scrolls, which is atypical for terrazzo (the pattern should feel like a physical surface that you scroll across, not a fixed overlay).
- **A-Side cards:** Semi-transparent white (`rgba(255,255,255,.65)`) with `backdrop-filter: blur(4px)`, creating a frosted glass effect over the terrazzo background. This is a strong design choice.
- **B-Side card icons:** Colored differently per card via `:nth-child` selectors (lines 103-104, 108), which brings terrazzo's multi-color nature into the components.
- **Missing:** Terrazzo chips should be irregular blob shapes, not perfect circles. The spec calls for `border-radius: 40% 60% 50% 50%` for organic shapes. All current chips are perfect circles via `radial-gradient(circle ...)`. No mix-blend-mode usage. No SVG chips with varied shapes.

### Animations
- **@keyframes:** None defined.
- **Transitions:** A-Side button: `transition: transform .2s, background .2s` with hover `scale(1.05)` and color change to rose. Cards: `transition: transform .2s` with hover `translateY(-4px)`. B-Side cards: `translateY(-3px)`.
- **Motion appropriateness:** Minimal motion is correct for a material/surface style. Terrazzo is a static physical material; animation should be limited to interaction responses.

### Content
- **Brand names:** "Terrazzo" (A-Side, literal), "Speckle" (B-Side, descriptive). "Speckle" is clever and memorable.
- **Hero copy:** A-Side: "Speckled Surface Design" -- direct and descriptive. B-Side: "Color Chips & Charm." -- more playful and evocative of the material.
- **Card titles:** A-Side: "Warm Neutrals," "Color Pops," "Aggregate Mix" -- accurate material terminology ("aggregate" is the correct terrazzo term). B-Side: "Rosy Pink," "Cool Teal," "Warm Amber" -- describes the palette colors.
- **Metrics:** B-Side: "4 Colors, Infinity Fragments, 100% Unique, Warm Vibes." Creative but "4 Colors" understates terrazzo's diversity (the page itself uses more than 4).
- **Quote:** "The perfect balance of playful and polished. Like a trendy cafe you never want to leave." From "Interior Design Monthly." Good contextual reference.

### Specific Fix Recommendations
1. **Make terrazzo chips irregular rather than circular.** Replace `radial-gradient(circle ...)` with `radial-gradient(ellipse ...)` at various aspect ratios, or better yet, use SVG shapes with varied `border-radius` values (e.g., `40% 60% 50% 50%`) for authentic chip shapes.
2. **Change B-Side `position: fixed` to `position: absolute`** on `.b-side::before` (line 105). Terrazzo is a physical surface; the pattern should scroll with the content, not remain fixed like a viewport overlay.
3. **Increase B-Side speckle density.** The B-Side has only 6 gradient speckles vs. the A-Side's 14. Double or triple the count and vary sizes more dramatically (2px to 10px) for better visual density.
4. **Fix B-Side text contrast.** Darken `#8B7B68` to at least `#6B5A48` for card body text to meet WCAG AA.
5. **Add chip variety.** Include some triangular or irregular polygon chips alongside circles. Terrazzo's defining visual characteristic is the variety of aggregate shapes, not just color.

---

## Origami (`origami.html`)
**Style Authenticity Score: 6.5/10**

### Fonts
- **Family:** Nunito (weights 300, 500, 700) loaded via Google Fonts (line 8).
- **Appropriateness:** Nunito is a rounded sans-serif, which conflicts with origami's essential geometric precision. Origami folds create sharp creases and angular geometry. A geometric sans-serif with sharper terminals (e.g., Roboto, Josefin Sans, or even a condensed font like Oswald for headings) would better communicate the crisp, angular nature of paper folding.

### Colors
- **A-Side Palette (CSS custom properties, line 11):**
  - `--paper: #F5F0E8` (warm off-white)
  - `--fold: #E8E0D5` (slightly darker cream)
  - `--crease: #D4CCBE` (muted tan)
  - `--dark: #4A453D` (dark brown)
  - `--accent: #C67A4A` (warm rust/copper)
- **B-Side Palette:**
  - Background: `#F5F0E8` (same as A-Side paper)
  - Accent: `#C4956A` (muted gold/copper, softer than A-Side)
  - Text: `#5C4A3A` (warm brown), `#8B7B68` (muted brown)
  - Cards: `#FFFFFF` with shadow
  - Border/dividers: `#E5DDD0` (light tan)
  - Card icon bg: `#EBE4D8`
- **Contrast ratios:** `#8B7B68` on `#F5F0E8` yields approximately 2.9:1 -- fails WCAG AA. The recurring `#8B7B68` color across all B-Sides in this batch is a systemic contrast failure.
- **Accent usage:** The palette is appropriately restrained, using only paper-like tones with a single warm accent. The DNA spec calls for "clean, flat color palette with systematic shade stepping across facets," and the A-Side achieves this with its paper/fold/crease progression.

### Layout
- **A-Side hero:** Center-aligned, 56px top / 72px bottom padding. Background uses a diagonal split (`linear-gradient(135deg, var(--paper) 50%, var(--fold) 50%)`, line 19) creating a fold-like division. The `::after` pseudo-element adds a corner fold (60px triangle, line 20).
- **B-Side hero:** Standard 80vh centered hero.
- **Cards:** A-Side cards have no border-radius, which is correct for origami's angular aesthetic. B-Side cards have `border-radius: 4px`, which is also restrained.
- **Section spacing:** A-Side uses 40px top / 32px sides on card grid. B-Side uses 5rem sections. The `.fold-divider` (line 34) in the A-Side is a subtle horizontal crease simulation.
- **Responsive:** A-Side has no explicit breakpoint. B-Side has 768px breakpoint.

### Sizing
- **Typography scale:**
  - A-Side: h1 `clamp(32px, 6vw, 56px)`, card number `36px`, h3 `16px`, body `13px`, hero body `15px`, nav `13px`
  - B-Side: h1 `clamp(2.5rem, 6vw, 4rem)`, h2 `1.8rem`, h3 `1.05rem`, body `0.88rem`
- **Card numbers:** The A-Side uses `36px` bold numbers ("01", "02", "03") in the crease color, which creates a strong typographic hierarchy within cards.
- **Button:** A-Side button has no border-radius, reinforcing angular origami geometry. The `::before` pseudo-element creates a small folded shadow triangle (6px) below the button (line 25).

### Sections
- **Current sections:** Hero, fold divider, three numbered cards, palette swatches, footer (A-Side). Standard template sections for B-Side.
- **Effectiveness:** The A-Side hero's diagonal split and corner fold are the strongest origami elements. The numbered cards with fold corners are effective. However, the overall layout feels too conventional for origami.
- **Better sections would include:**
  - A faceted polygon background using SVG triangles with varying shades
  - Content panels that appear to fold open (using CSS transforms with perspective)
  - A step-by-step section showing fold instructions with progressive complexity
  - Triangular navigation or tab system
  - A section where the background appears to be a low-poly mesh

### Visuals
- **A-Side corner folds:** Cards use dual `::before` and `::after` (lines 29-30) creating the classic "dog-ear" corner fold effect with CSS triangles. The hero also has a top-right corner fold. These are the most authentic origami visual elements.
- **A-Side fold-divider:** Uses a subtle double-line gradient (line 34) simulating a horizontal crease.
- **A-Side button shadow fold:** The button's `::before` creates a small triangular shadow beneath the left edge, suggesting a folded flap.
- **B-Side corner folds:** Cards have `::after` (line 88) creating a 24px corner triangle in the page background color, and `::before` (line 89) adding a subtle shadow line. This is simpler than the A-Side's technique but still recognizably origami.
- **Missing:** No faceted polygon backgrounds. No `clip-path: polygon()` for angular sections. No CSS `perspective` or `rotateY/X` for 3D fold effects. No adjacent triangles in varying shades to create the low-poly faceted look that is core to the origami DNA spec. The current implementation reads more as "paper with folded corners" than true origami.

### Animations
- **@keyframes:** None defined.
- **Transitions:** A-Side button background change on hover (`transition: background .2s`). B-Side cards `translateY(-3px)` on hover. Nav links color transition at `.2s`.
- **Motion appropriateness:** Origami could benefit from subtle fold/unfold animations -- a card that appears to fold open on hover using `transform: perspective(600px) rotateY(5deg)` would be highly appropriate. Currently the motion is too generic.

### Content
- **Brand names:** "Origami" (A-Side, literal), "Ori" (B-Side, abbreviated). "Ori" is clean and geometric.
- **Hero copy:** A-Side: "Paper Fold Design" -- descriptive. B-Side: "Paper Into Form." -- more poetic and evocative of the transformation process.
- **Card titles:** A-Side: "Valley Fold," "Mountain Fold," "Reverse Fold" -- actual origami terminology with accurate descriptions. Excellent educational content that demonstrates deep understanding of the craft.
- **B-Side cards:** "Clean Folds," "Natural Tones," "Shadow Depth" -- describe the visual system rather than origami techniques. Less authentic.
- **Metrics:** B-Side: "Triangle Folds, 3 Tones, 0 Glue, Infinity Patience." The "0 Glue" metric is a charming reference to real origami's no-adhesive rule.
- **Quote:** "The art of transforming a flat sheet into something dimensional. Beautiful restraint." From "Paper Arts Review." Appropriate and thoughtful.

### Specific Fix Recommendations
1. **Add a faceted polygon SVG background to the hero.** Create a mesh of adjacent triangles in varying shades of `--paper`, `--fold`, and `--crease` to produce the signature low-poly origami look.
2. **Add `perspective` and `rotateY` to card hover states.** Replace the generic `translateY(-3px)` with `transform: perspective(800px) rotateY(-2deg)` to simulate a card folding slightly.
3. **Replace Nunito with a geometric sans-serif.** Nunito's rounded terminals conflict with origami's sharp creases. Josefin Sans or Manrope would be better options.
4. **Add `clip-path: polygon()` to at least one section** to create angular, faceted section boundaries instead of flat horizontal dividers.
5. **Fix contrast ratio on B-Side body text.** Darken `#8B7B68` to at least `#6B5A48` against the `#F5F0E8` background.

---

## Tactile UI (`tactile-ui.html`)
**Style Authenticity Score: 7/10**

### Fonts
- **Family:** Nunito (weights 400, 600, 700, 800, 900) loaded via Google Fonts (line 8).
- **Appropriateness:** The A-Side's use of ultra-heavy weights (800, 900) suits the playful, squishy deformable UI. For the B-Side's reinterpretation as a "craft/material" tactile feel, Nunito's rounded forms work well for approachable warmth.

### Colors
- **A-Side Palette:**
  - Background: `#F0E6FF` (light lavender)
  - Hero gradient: `#E0D0FF` to `#F0E6FF`
  - Primary: `#7C3AED` (vivid violet)
  - Secondary: `#EC4899` (hot pink)
  - Tertiary: `#06B6D4` (cyan)
  - Dark text: `#2D1B69` (deep indigo)
  - Muted text: `rgba(45,27,105,0.55)` and `rgba(45,27,105,0.35)`
  - Shadow/depth: `#5B21B6` (dark violet), `#E0D0FF` (light violet)
  - Card surface: `#FFFFFF`
- **B-Side Palette:**
  - Background: `#F5F1E8` (warm cream)
  - Accent: `#D2B48C` (tan/cork color)
  - Text: `#4A3F35` (dark brown), `#8B7B68` (muted brown)
  - Cards: `#EBE4D8` (light warm beige) with `border: 2px dashed #C4B5A0`
  - Borders/dividers: `#C4B5A0` (warm tan), used as dashed lines
  - Card icon bg: `#D2B48C` (solid tan)
  - Button inset shadow: `rgba(0,0,0,.1)`
- **Contrast ratios:** A-Side `rgba(45,27,105,0.55)` on `#F0E6FF` is approximately 4.3:1 -- borderline. B-Side `#8B7B68` on `#F5F1E8` is approximately 2.9:1 -- fails. B-Side `#4A3F35` on `#F5F1E8` is approximately 5.8:1 -- passes.
- **A-Side vs B-Side identity split:** The A-Side is a playful, digital squishy UI (violet/pink/cyan). The B-Side is a physical-material tactile UI (cork/canvas/craft). These are two very different interpretations of "tactile." The A-Side matches the compendium's "Tactile / Deformable UI" definition (squish, stretch, bounce), while the B-Side leans toward a "handcraft/material" interpretation.

### Layout
- **A-Side hero:** 440px min-height, centered flex column, 48px top / 24px side padding. Nav is absolutely positioned at top. Three blob elements are absolutely positioned decorative shapes. Content is in a relatively positioned z-index:5 container.
- **A-Side components:** Narrow 560px max-width centered section with labeled groups: buttons, card, input, palette. This is a component showcase layout, not a page layout. This design choice is highly intentional and appropriate for demonstrating tactile interactions.
- **B-Side hero:** Standard 80vh centered hero.
- **Section spacing:** A-Side has 40px component section padding. B-Side uses 5rem sections with 1100px max-width.
- **Responsive:** A-Side has no explicit breakpoint. B-Side has 768px breakpoint.

### Sizing
- **Typography scale:**
  - A-Side: h1 `42px`, comp-title `26px`, card h3 `18px`, body `15px`, buttons `14px`, section-label `11px`, swatch-name `10px`
  - B-Side: h1 `clamp(2.5rem, 6vw, 4rem)`, h2 `1.8rem`, h3 `1.05rem`, body `0.88rem`
- **A-Side button dimensions:** 12px/24px padding (compact), 18px border-radius (pill-shaped), 6px bottom shadow height (creating physical depth).
- **A-Side CTA:** 16px/36px padding, 24px border-radius, 8px bottom box-shadow (prominent physical press feel).
- **Input field:** Full width, 16px/18px padding, 18px border-radius, 3px border, 4px bottom shadow.

### Sections
- **A-Side sections:** Hero with blobs, component showcase (buttons, card, input, palette). This is notably different from the standard template -- it functions as a component demo page.
- **B-Side sections:** Standard template: hero, feature cards, metrics, quote, footer.
- **Effectiveness:** The A-Side is excellent as a tactile component showcase. Each component demonstrates physical interaction metaphors (press, squish, bounce). The B-Side's standard layout with craft/material theming is less distinctive.
- **Better sections for B-Side would include:**
  - A "material board" section with cork, canvas, leather, and fabric texture swatches
  - Interactive slider or dial components that demonstrate physical control metaphors
  - A toggle section with physical rocker switches
  - A pinboard/bulletin-board section where cards appear pinned to a cork surface

### Visuals
- **A-Side blobs:** Three `.blob` elements with `blobFloat` animation (line 30-34) create organic, morphing background shapes. They use absolute positioning and 0.2 opacity for a subtle atmospheric effect.
- **A-Side physical depth:** Extensive use of offset `box-shadow` for 3D depth:
  - CTA button: `0 8px 0 #5B21B6` (hard 8px bottom shadow, line 111)
  - Primary button: `0 6px 0 #5B21B6` (6px shadow, line 163)
  - Card: `0 8px 0 #E0D0FF` (8px shadow, line 184)
  - Input: `0 4px 0 #E0D0FF` (4px shadow, line 213)
  - Swatches: `0 4px 0 rgba(0,0,0,0.08)` (line 228)
- **A-Side deformation on interaction:**
  - Button hover: `scale(1.08, 0.94)` -- horizontal stretch (line 158)
  - Button active: `scale(0.92, 1.06)` -- vertical squish (line 159)
  - Card hover: `scale(1.02, 0.98)` + reduced shadow (line 189)
  - Swatch hover: `scale(1.15, 0.9)` (line 232)
  - Swatch active: `scale(0.9, 1.1)` (line 233)
  - CTA active: `translateY(6px)` + minimal shadow (line 121) -- full press-down
- **A-Side cubic-bezier:** `cubic-bezier(0.34, 1.56, 0.64, 1)` used on buttons, cards, input, swatches (lines 155, 185, 214, 229). This "springy overshoot" curve is essential for tactile/squishy feel.
- **B-Side tactile elements:**
  - Dashed borders: `2px dashed #C4B5A0` on header, sections, card borders, footer (lines 248, 262, 267, 278). This evokes hand-stitched seams.
  - Inset card shadow: `inset 0 2px 4px rgba(0,0,0,.06)` on `.bcard` (line 267), making cards feel recessed.
  - Button inset: `box-shadow: inset 0 2px 4px rgba(0,0,0,.1)` on `.bbtn-p` (line 284), with hover deepening to `inset 0 3px 6px rgba(0,0,0,.15)` (line 285). Press-down effect.
  - Card inner border: `::before` with `inset: 4px` dashed border (line 287), suggesting a stitched frame.
- **Missing B-Side:** No actual texture pattern (canvas grain, cork, fabric weave). The B-Side mentions "Cork boards, woven fabric, canvas grain" in its hero copy but does not implement any visual texture. No SVG `feTurbulence` for procedural texture. No physical-world control metaphors (dials, sliders).

### Animations
- **A-Side @keyframes (4 defined):**
  - `bounce` (lines 18-23): Multi-stage vertical bounce with scale deformation. Applied to hero h1 span.
  - `jelly` (lines 24-29): Asymmetric scale wobble. Applied to card emoji.
  - `blobFloat` (lines 30-34): Morphing border-radius with vertical drift. Applied to blob decorative elements.
  - `squishPulse` (lines 35-38): Subtle breathing scale animation. Applied to card.
- **A-Side transitions:** Extensive use of `cubic-bezier(0.34, 1.56, 0.64, 1)` spring curves on all interactive elements.
- **B-Side animations:** None. No @keyframes, no spring curves. The B-Side's button hover actually has `transform: none` (line 285), explicitly removing the generic `translateY(-1px)` and replacing it with only shadow deepening. This is an intentional press-down-only interaction, which is conceptually correct but under-animated.
- **Motion appropriateness:** The A-Side has outstanding tactile motion design. The B-Side has almost no motion, which undermines the tactile concept (physical objects respond to touch with visible deformation).

### Content
- **Brand names:** "Squish" (A-Side), "Craft Co." (B-Side). "Squish" perfectly captures the deformable UI concept. "Craft Co." suits the B-Side's material/handmade reinterpretation.
- **Hero copy:** A-Side: "UI That Feels Squishy" with "Squishy" animated with bounce. B-Side: "Surfaces You Can Feel." Both are effective but describe very different concepts.
- **A-Side component labels:** "Buttons (Press them!)", "Card", "Input", "Palette (Squish the Swatches)" -- the imperative voice and exclamation marks encourage physical interaction.
- **B-Side card titles:** "Cork & Canvas," "Stitched Borders," "Pressed Buttons" -- accurately describe the visual techniques used.
- **Metrics:** B-Side: "Pen Handmade, 4 Textures, 0 Digital Feel, Real Touch." Creative and on-theme.
- **Quote:** "I keep wanting to reach out and touch the screen. The textures feel incredibly real." From "Tactile Design Lab." Perfect.
- **Footer bug:** B-Side footer text reads "Craft Co.." (double period, line 351).

### Specific Fix Recommendations
1. **Add actual texture patterns to B-Side.** Implement a CSS noise/grain texture overlay using SVG `feTurbulence` or a repeating `background-image` pattern to simulate cork, canvas, or linen. The hero copy promises textures that the visual design does not deliver.
2. **Add spring-curve transitions to B-Side interactions.** Replace the static B-Side card hover (`translateY(-3px)`) with `cubic-bezier(0.34, 1.56, 0.64, 1)` transitions and scale deformation to maintain the tactile identity.
3. **Fix the double period in the B-Side footer** (line 351). Change "Craft Co.." to "Craft Co."
4. **Fix B-Side body text contrast.** Change `#8B7B68` to a darker value for WCAG AA compliance.
5. **Add physical-world control metaphors to B-Side.** Include at least one non-standard interactive element (a toggle switch with physical press feel, a rotary selector, or a slider with textured handle) to demonstrate the "tactile" concept beyond standard cards and buttons.
6. **Remove duplicate CSS rules.** Lines 284-285 duplicate lines 289 (`.bbtn-p` box-shadow and hover rules). Lines 286-288 (`.bcard` position/before) are the unique rules; the duplication is just the button styles.

---

## Cross-Cutting Observations

### Systemic B-Side Issues

All five B-Sides share a common template structure with nearly identical class names (`.bh`, `.bhero`, `.bsec`, `.bcon`, `.bgrid`, `.bcard`, `.bmets`, `.bquote`, `.bfoot`), identical section headings ("What Sets Us Apart," "Numbers Speak"), and identical responsive breakpoints. This creates consistency across the collection but introduces several recurring problems:

1. **Contrast failure on `#8B7B68` text.** This exact color appears in all five B-Sides for secondary text and fails WCAG AA against every background it is paired with. A batch fix to darken this to `#6B5B4A` or darker would resolve the issue across all files.

2. **Generic section titles.** "What Sets Us Apart" and "Numbers Speak" appear in every B-Side verbatim. These should be customized per style.

3. **Missing style-specific visual treatments.** The B-Sides apply style-specific accents (color, border-radius, pseudo-elements) but share an identical layout skeleton. Some styles (particularly origami and tactile-ui) need fundamentally different layout approaches to be authentic.

4. **No A-Side responsive breakpoints for paper-cut and tactile-ui.** Both A-Sides lack explicit mobile breakpoints, which means they rely entirely on `auto-fit` grids.

### Strongest Implementation
Marble scores highest (8/10) because its A-Side has the most authentic visual treatment (multi-layered CSS marble texture, proper luxury typography, gold accents, symmetrical layout, contextual content with real marble variety names).

### Weakest Implementation
Origami scores lowest (6.5/10) because its core visual identity -- faceted polygon meshes, low-poly backgrounds, and CSS 3D transforms -- is almost entirely absent. The implementation achieves "paper with folded corners" rather than true origami geometry.

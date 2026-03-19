# B-Side Audit Report: Core Foundations (10 Styles)

**Report ID:** 01-core-foundations
**Date:** 2026-03-20
**Auditor:** UI Designer Agent
**Scope:** B-side implementations for 10 foundational design style sample pages

---

## Executive Summary

All 10 B-side implementations share an identical generic template. The template consists of a dark sticky header, centered hero with tag line, a 3-card features grid, a 4-column metrics row, a centered blockquote, and a centered footer. The only customizations applied per style are: (1) the style name swapped into headings/footer, (2) one or two accent colors changed, and (3) a light or dark background tone selected.

**Not a single B-side authentically represents its target design style.** The copy, layout structure, typography, spacing, shadows, border-radius, and visual effects are identical across all 10 files. Every B-side uses `font-family: Inter, system-ui, sans-serif`, `border-radius: 8px`, `box-shadow: 0 2px 8px rgba(0,0,0,.15)`, hover `translateY(-3px)`, and the same boilerplate content ("A distinctive visual approach that brings unique character and personality to every interface").

**Average Score: 1.6 / 10**

---

## Systemic Issues (Apply to ALL 10 B-sides)

Before individual reviews, these template-level failures affect every file:

1. **Identical HTML structure**: Every B-side has the exact same DOM: `.bh` > `.bhero` > `.bsec` (features grid) > `.bsec` (metrics) > `.bsec` (quote) > `.bfoot`. No structural variation whatsoever.
2. **Identical copy**: "Distinctive by design", "What Sets Us Apart", "Numbers Speak", "A truly distinctive design approach..." -- every page uses the same placeholder text that says nothing about the actual style.
3. **Same font everywhere**: `Inter, system-ui, sans-serif` regardless of whether the style demands monospace (brutalism, mono-space), serif (e-ink), DM Sans (bauhaus), Atkinson Hyperlegible (inclusive), or no font at all.
4. **Same border-radius: 8px** on cards and buttons regardless of style (brutalism needs 0, neubrutalism needs 10-16px, minimalism needs 0, flat needs 4px).
5. **Same box-shadow**: `0 2px 8px rgba(0,0,0,.15)` on every card, even for styles that explicitly forbid shadows (brutalism, flat, minimalism, e-ink).
6. **Same hover animation**: `transform: translateY(-3px)` on every card -- irrelevant to most styles and actively wrong for brutalism, e-ink, whitespace-maximalism.
7. **Same layout density**: Moderate padding (5rem 2rem sections, 2rem card padding, 1.5rem grid gaps). No style gets its own spatial rhythm.
8. **No style-specific CSS effects**: Zero scanlines, gradients, geometric shapes, textures, blinking cursors, offset shadows, focus rings, or any other signature visual treatment.
9. **Generic Unicode icons**: Diamond (&#9670;), diamond outline (&#9674;), and asterisk (&#10038;) used identically in every style's feature cards.

---

## 1. Minimalism (Swiss Style)

**File:** `samples/minimalism.html`
**Style Authenticity Score: 2 / 10**

### Color Palette
- **B-side uses:** Black background (#000) with white text -- an inverted scheme.
- **Problem:** Swiss minimalism is defined by white backgrounds with black type. The dark-mode approach directly contradicts the style. The A-side correctly uses `#FFFFFF` background.
- **Accent color:** Pure white (#FFFFFF) used as accent -- acceptable but lazy. Swiss style uses grayscale only, which the B-side technically does, but on the wrong background.

### Typography
- **Font:** `Inter, system-ui, sans-serif` -- Inter is acceptable for Swiss style (the A-side also uses Inter). However, `font-weight: 800` on headings is too heavy; Swiss style favors 400-700 range.
- **Letter-spacing:** `-0.03em` on hero h1 is fine. But the A-side's careful use of `0.15em` uppercase label spacing is completely absent from the B-side.
- **Missing:** No uppercase text-transform on section labels. Swiss style relies heavily on uppercase small-caps for hierarchy labels.

### Border Radius
- **B-side:** 8px on cards and buttons.
- **Required:** 0px everywhere. Swiss minimalism has zero decorative rounding. The A-side correctly uses no border-radius.

### Shadows & Depth
- **B-side:** `box-shadow: 0 2px 8px rgba(0,0,0,.15)` on cards.
- **Required:** Zero shadows. The A-side has no shadows. Swiss design is entirely flat with hierarchy from type and spacing.

### Layout & Spacing
- **Hero:** Centered text with centered buttons -- wrong. Swiss minimalism uses left-aligned asymmetric layouts with deliberate grid tension. The A-side correctly left-aligns with `max-width: 480px`.
- **Grid:** Generic `auto-fit, minmax(280px, 1fr)` instead of a precise 12-column grid with deliberate column placement.
- **Missing:** No visible grid lines, no asymmetric balance, no mathematical spacing ratios.

### Visual Effects
- None present. None needed for this style, which is correct. But the `backdrop-filter: blur(12px)` on the header is decorative and un-Swiss.

### Content & Voice
- Generic placeholder text. Should reference reduction, clarity, grid, Helvetica, Swiss tradition. The A-side says "Less is the ultimate sophistication" and "Clarity through reduction."

### Missing Elements
- White background with black type
- Zero border-radius on all elements
- Zero shadows on all elements
- Left-aligned hero layout
- Precise grid system (not auto-fit)
- Thin rule/border separators (1px solid, not rgba opacity borders)
- Uppercase small-caps section labels with wide letter-spacing
- Monochrome palette enforced (no colored accents)

### CSS Bugs
- No syntax errors, but `backdrop-filter` and `border-radius: 8px` are stylistically wrong.

### Recommendations
1. Switch to white background (#FFF), black text (#000)
2. Set `border-radius: 0` globally
3. Remove all `box-shadow`
4. Left-align hero content with `max-width: 480px`
5. Use thin `border-bottom: 1px solid #E0E0E0` for section dividers
6. Add uppercase letter-spaced section headings
7. Remove hover translateY animation; use underline hover if anything

---

## 2. Flat Design

**File:** `samples/flat-design.html`
**Style Authenticity Score: 2 / 10**

### Color Palette
- **B-side uses:** `#3498DB` (blue) background with `#2ECC71` (green) accent -- these are correct flat design colors from the A-side palette.
- **Problem:** The B-side uses them on a full blue background page, which is partially correct. But cards use `rgba(0,0,0,.02)` translucent backgrounds instead of solid flat colors. Flat design demands solid, opaque color fills with zero transparency.

### Typography
- **Font:** `Inter, system-ui, sans-serif` -- should be `Open Sans` as loaded in the `<head>`. The A-side correctly uses Open Sans.
- **Weight 800** on headings -- too heavy for flat design's clean, friendly weight (typically 600-700).

### Border Radius
- **B-side:** 8px. The A-side uses a consistent 4px. Flat design uses small, consistent radii (2-6px), not 8px.

### Shadows & Depth
- **B-side:** `box-shadow: 0 2px 8px rgba(0,0,0,.06)` on cards.
- **Required:** Zero shadows. Flat design is defined by the complete absence of shadows, gradients, and depth cues. This is a fundamental violation.

### Layout & Spacing
- Centered hero -- partially acceptable for flat design (it's flexible). But the A-side uses left-aligned hero.
- Cards should use solid color backgrounds, not transparent.

### Visual Effects
- `backdrop-filter: blur(12px)` on header -- violates flat design (blur is a depth/glass effect).
- `transform: translateY(-3px)` hover -- creates perceived depth, which flat design forbids.
- `translateY(-1px)` on button hover -- same issue.

### Content & Voice
- Generic. Should reference simplicity, clarity, "no noise" philosophy. A-side says "Design without the noise."

### Missing Elements
- Zero shadows enforced globally
- Zero gradients enforced (no linear-gradient, no blur)
- Solid opaque color fills on all surfaces
- Open Sans font family
- Consistent 4px border-radius (not 8px)
- Bold vibrant color blocks as the primary hierarchy mechanism
- Flat geometric shape decorations (the A-side has colored squares and circles)
- No hover elevation effects

### CSS Bugs
- Font declaration ignores the loaded Google Font (Open Sans loaded but Inter used).

### Recommendations
1. Change font to `'Open Sans', sans-serif`
2. Set `border-radius: 4px` globally
3. Remove ALL `box-shadow` declarations
4. Remove `backdrop-filter: blur`
5. Use solid color card backgrounds (`#FFF`, `#2ECC71`, `#E74C3C`)
6. Remove hover `translateY` effects; use color-only hover transitions
7. Add flat geometric shape elements for visual interest

---

## 3. Inclusive Design

**File:** `samples/inclusive-design.html`
**Style Authenticity Score: 1 / 10**

### Color Palette
- **B-side uses:** Dark navy (#0F172A) background with blue (#2563EB) accent.
- **Problem:** The A-side uses high-contrast combinations specifically chosen for WCAG compliance (dark navy on white, gold accent #E8B931 with 4.5:1+ ratios). The B-side accent `#2563EB` on dark background needs contrast verification, and `#aaa` paragraph text on `#0F172A` fails WCAG AA (approximately 3.9:1 ratio -- below 4.5:1 minimum).

### Typography
- **Font:** `Inter, system-ui, sans-serif` -- should be `Atkinson Hyperlegible`, the purpose-built accessibility font loaded in `<head>`. This is a critical failure -- Atkinson Hyperlegible was specifically designed for low-vision readers.
- **Base size:** Not specified in B-side (defaults to 16px). The A-side explicitly uses `18px` base for readability.
- **Font size .75rem** on section tags = 12px, which is below WCAG recommended minimum of 14px.

### Border Radius
- 8px -- acceptable for inclusive design (rounded corners are fine).

### Shadows & Depth
- `box-shadow: 0 2px 8px rgba(0,0,0,.15)` -- not inherently wrong for inclusive design, but subtle shadows can reduce contrast for low-vision users. The A-side uses no shadows.

### Layout & Spacing
- Generic centered layout. Inclusive design should have generous padding, large touch targets, and clear visual separation.

### Visual Effects
- `backdrop-filter: blur(12px)` -- problematic for cognitive accessibility (motion/visual effects should be minimal).
- No `prefers-reduced-motion` media query.

### Content & Voice
- Generic. Should reference accessibility, "design for everyone," WCAG compliance. The A-side says "Design for everyone, not just some."

### Missing Elements (Critical for this style)
- **Skip navigation link** (`<a href="#main" class="skip-link">`) -- completely absent
- **`aria-label`** attributes on navigation and interactive elements
- **`role`** attributes on landmark elements
- **Focus-visible outlines** (`outline: 3px solid #E8B931; outline-offset: 3px`) -- none present
- **`min-height: 48px`** on all interactive elements (buttons are not 48px in B-side)
- **Labeled form inputs** (no `<label>` elements)
- **Atkinson Hyperlegible font**
- **18px base font size**
- **WCAG AAA contrast ratios** (7:1 for normal text)
- **`prefers-reduced-motion`** media query
- **Semantic HTML** (`<main>`, `<nav aria-label>`, proper heading hierarchy)
- **High-contrast mode support**

### CSS Bugs
- `#aaa` text on `#0F172A` background likely fails WCAG AA 4.5:1 contrast requirement.
- `.bhero-tag` at `.8rem` (12.8px) is too small for accessible design.

### Recommendations
1. Switch font to `'Atkinson Hyperlegible', sans-serif`
2. Set base font-size to 18px
3. Add skip-link, aria-labels, role attributes throughout
4. Add `outline: 3px solid #E8B931; outline-offset: 3px` on all `:focus-visible` states
5. Set `min-height: 48px; min-width: 48px` on all buttons/links
6. Add `<label>` elements for any form inputs
7. Ensure all color combinations meet WCAG AAA (7:1 ratio)
8. Add `@media (prefers-reduced-motion: reduce)` to disable animations
9. Increase minimum text size to 14px (no .75rem labels)
10. Use semantic landmarks: `<main>`, `<nav aria-label="Primary">`, etc.

---

## 4. Bauhaus

**File:** `samples/bauhaus.html`
**Style Authenticity Score: 1 / 10**

### Color Palette
- **B-side uses:** Red (#FF0000) background with blue (#0000FF) accent and white text.
- **Problem:** Using red as a full-page background is overwhelming and not Bauhaus. Bauhaus uses white/cream backgrounds with red, blue, and yellow as accent colors on geometric shapes -- not as background fills. The A-side correctly uses white background with R/B/Y geometric shapes.

### Typography
- **Font:** `Inter, system-ui, sans-serif` -- should be `DM Sans` as loaded. Bauhaus also calls for geometric sans-serifs.
- **Missing:** All-uppercase headings and labels. Bauhaus typography is militant about uppercase and geometric letterforms.

### Border Radius
- **B-side:** 8px. Bauhaus uses 0px for rectangles and 50% for circles -- nothing in between. Geometric purity demands sharp corners or perfect circles only.

### Shadows & Depth
- `box-shadow: 0 2px 8px rgba(0,0,0,.15)` -- Bauhaus uses zero shadows. Form follows function; decorative shadows are antithetical.

### Layout & Spacing
- Generic centered layout. Bauhaus demands a strict grid with asymmetric composition. The A-side uses a 3-column bordered grid with thick black borders.

### Visual Effects
- No geometric shapes (circles, squares, triangles) anywhere in the B-side.
- No thick black borders.
- No primary-color geometric decorations.

### Content & Voice
- Generic. Should reference "form follows function," "art and industry," geometric principles. A-side says "Form Follows Function."

### Missing Elements
- **Geometric shapes** (CSS circles, squares, triangles using border tricks or clip-path) -- the absolute core of Bauhaus
- **Primary colors only** (red #FF0000, blue #0000FF, yellow #FFD700, black, white)
- **DM Sans font**
- **Thick black borders** (3-4px) on all elements
- **Zero border-radius** (or 50% for circles)
- **Zero shadows**
- **Asymmetric grid layout** with thick dividers
- **Uppercase text-transform** on all headings
- **Wide letter-spacing** on labels

### CSS Bugs
- `#aaa` text on `#FF0000` background has poor contrast (approximately 2.5:1 -- fails WCAG AA).
- Blue (#0000FF) text on red (#FF0000) background is nearly illegible.

### Recommendations
1. Switch to white background, black text
2. Use DM Sans font
3. Add large geometric shapes (CSS circles, squares, triangles) as decorative elements
4. Set border-radius to 0 (or 50% only for circle elements)
5. Use thick 3-4px black borders on cards and sections
6. Restrict palette to R/B/Y/black/white only
7. Add text-transform: uppercase on all headings
8. Remove all box-shadows
9. Fix contrast issues (no blue-on-red, no light-gray-on-red)

---

## 5. Single-Color (Monochromatic Blue)

**File:** `samples/single-color.html`
**Style Authenticity Score: 3 / 10**

### Color Palette
- **B-side uses:** Deep blue background (#1E40AF) with mid-blue accent (#3B82F6) and white text. These are correct blue-family colors.
- **Problem:** Text color `#aaa` (gray) breaks the monochromatic rule. In a single-color system, ALL colors must be tints/shades of one hue (blue). Gray is achromatic and violates the concept. Should use light blue (#93C5FD or #BFDBFE) for secondary text.
- **Positive:** The background and accent are both blue-family, which is partially correct.

### Typography
- **Font:** Inter -- acceptable (A-side also uses Inter).
- No issues with typography per se, but weight 800 is heavier than the A-side's 700.

### Border Radius
- 8px -- the A-side uses 6-10px, so this is acceptable for this style.

### Shadows & Depth
- `box-shadow: 0 2px 8px rgba(0,0,0,.15)` -- should use blue-tinted shadow (`rgba(30,64,175,0.1)`) to stay monochromatic. Black shadows introduce a non-blue tone.

### Layout & Spacing
- Centered layout -- acceptable. The A-side uses left-aligned hero, but centered is not fundamentally wrong for this style.

### Visual Effects
- No shade scale visualization (the A-side has a beautiful 10-step gradient bar).
- No visual demonstration of hierarchy through shade variation.

### Content & Voice
- Generic. Should reference "one hue," "tints and shades," "infinite hierarchy." A-side says "One Color, Infinite Hierarchy."

### Missing Elements
- **Shade scale bar** showing 10 blue steps from lightest to darkest
- **All secondary text in blue tints** (not gray #aaa)
- **Blue-tinted shadows** (not black)
- **Blue-tinted borders** (not white/transparent rgba)
- **Color bar accents** on cards (A-side has card-bar elements)
- **Zero non-blue colors** enforced throughout

### CSS Bugs
- `color: #aaa` on paragraphs violates the monochromatic constraint.
- `border: 1px solid rgba(255,255,255,.08)` is white-tinted, not blue-tinted.

### Recommendations
1. Replace all `#aaa` and `#666` with blue tints (#93C5FD, #BFDBFE)
2. Replace all `rgba(255,255,255,...)` borders with `rgba(147,197,253,...)`
3. Use blue-tinted shadows: `rgba(30,64,175,0.15)`
4. Add shade scale visualization bar
5. Add card-top color bars in different blue shades
6. Ensure every pixel on the page is a shade of blue or white (which is the lightest tint)

---

## 6. Whitespace Maximalism

**File:** `samples/whitespace-maximalism.html`
**Style Authenticity Score: 1 / 10**

### Color Palette
- **B-side uses:** Black (#000) background with white text.
- **Problem:** Whitespace maximalism is about vast expanses of WHITE space. A black background fundamentally inverts the entire concept. The A-side correctly uses `#FFFFFF`.

### Typography
- **Font:** Inter -- acceptable (A-side uses Inter too).
- **H1 size:** `clamp(2.5rem, 6vw, 4rem)` -- too small. The A-side uses 5rem with extreme contrast between the huge headline and tiny (0.65-0.8rem) body text. This size contrast IS the style.
- **Body text:** 1.05rem is far too large. Should be 0.65-0.8rem to create the dramatic size differential.

### Border Radius
- 8px -- should be 0. Whitespace maximalism strips away all decorative elements. No rounding.

### Shadows & Depth
- Shadows present -- should be zero. This style is about pure emptiness.

### Layout & Spacing
- **Section padding:** `5rem 2rem` -- far too little. The A-side uses `8rem 6rem`. Whitespace maximalism needs sections that are 80-90% empty space.
- **Grid gap:** `1.5rem` -- the A-side uses `6rem`. The breathing room IS the design.
- **Max-width:** `1100px` -- generic. The A-side has no max-width constraint on the container; content is sparse and centered.
- **Content density:** The 3-card grid, 4-metric row, blockquote, and footer create a content-dense page. Whitespace maximalism should have near-empty sections with a single element each.

### Visual Effects
- Hover translateY animation -- wrong. This style should have minimal or no interaction effects.
- `backdrop-filter: blur` -- too decorative.

### Content & Voice
- Generic. Should use poetic, minimal language. A-side: "Space." (single word hero), "When everything is removed, what remains is everything that matters."
- **Name truncated:** "Whitespace Maximalis" (missing final 'm') appears in header, hero, and footer. This is a content bug.

### Missing Elements
- **White background** (not black)
- **Enormous padding** (8rem+ between sections)
- **Huge hero type** (5rem+) with tiny body text (0.65rem)
- **Near-empty sections** (single centered line of text)
- **6rem+ grid gaps**
- **Zero border-radius**
- **Zero shadows**
- **Tiny, light-gray navigation text** (0.65rem, #BBB color)
- **Minimal dot/point decorations** instead of card icons
- **B&W only palette** (no accent colors)

### CSS Bugs
- Style name truncated: "Whitespace Maximalis" should be "Whitespace Maximalism" (appears 4 times in HTML).

### Recommendations
1. Switch to white background, black text
2. Increase section padding to 8-10rem
3. Increase grid gaps to 6rem
4. Make hero h1 5rem+, body text 0.65-0.8rem
5. Remove cards; replace with single centered text elements per section
6. Remove all shadows and border-radius
7. Fix truncated name to "Whitespace Maximalism"
8. Use only black, white, and light gray (#CCC)

---

## 7. Mono Space

**File:** `samples/mono-space.html`
**Style Authenticity Score: 1 / 10**

### Color Palette
- **B-side uses:** Dark charcoal (#2D3436) background -- matches A-side.
- **Problem:** Accent color is `#636E72` (gray), not the signature green (#00B894). The A-side's entire identity centers on green terminal accent. The B-side demotes green to gray, destroying the style.

### Typography
- **Font:** `Inter, system-ui, sans-serif` -- this is the single most critical failure. The ENTIRE POINT of this style is monospace typography. The A-side loads JetBrains Mono. Using a proportional sans-serif font completely negates the style's reason for existing.

### Border Radius
- 8px -- should be 0. Code/terminal aesthetic uses sharp rectangles exclusively.

### Shadows & Depth
- `box-shadow: 0 2px 8px rgba(0,0,0,.15)` -- should be zero. Terminal interfaces have no shadows.

### Layout & Spacing
- No grid-line background pattern (the A-side has `repeating-linear-gradient` for ruled-paper lines).
- No code-block styling.
- No line numbers.
- No terminal-style prompts (`>`, `$`, `//`).

### Visual Effects
- **Missing blinking cursor** animation (the A-side has `@keyframes blink` for a terminal cursor).
- **Missing `::before` content** prefixes (`> `, `/ `, `## `, `// `) that give the terminal feel.
- **Missing code syntax highlighting** (`.kw`, `.str`, `.cm` classes in A-side).
- **Missing dashed borders** (A-side uses `border-bottom: 1px dashed`).

### Content & Voice
- Generic. Should use code/terminal language. A-side: "Code is the medium," "$ init --start," file path labels like `grid.config`.

### Missing Elements
- **JetBrains Mono monospace font** -- the defining element
- **Green (#00B894) accent color**
- **Blinking cursor animation**
- **Terminal prompt prefixes** (`>`, `$`, `//`, `##`)
- **Line numbers** on content
- **Code block** with syntax highlighting
- **Ruled-line background** (`repeating-linear-gradient`)
- **Dashed borders** instead of solid
- **`data-file` attribute** labels on cards
- **Zero border-radius**
- **Zero shadows**

### CSS Bugs
- Uses gray (#636E72) as accent instead of green (#00B894) -- the style's signature color is completely absent.
- Font-family fails to use the loaded monospace font.

### Recommendations
1. Change font to `'JetBrains Mono', monospace`
2. Change accent to `#00B894` (green)
3. Add blinking cursor animation
4. Add terminal prefixes via `::before` pseudo-elements
5. Add ruled-line background pattern
6. Set border-radius to 0
7. Remove all box-shadows
8. Use dashed borders
9. Add code block with syntax highlighting
10. Add line numbers to card content

---

## 8. E-Ink / Paper

**File:** `samples/e-ink.html`
**Style Authenticity Score: 2 / 10**

### Color Palette
- **B-side uses:** Warm off-white (#FAF8F5) background -- close to A-side's #F6F1EB. This is the closest any B-side gets to its target palette.
- **Accent:** Dark brown (#2C2C2C) -- acceptable neutral, though the A-side uses warmer browns (#3D3529, #6B5F4D).
- **Secondary text:** `#666` -- should be warm-toned (#8A7E6B or similar) to maintain the paper warmth.

### Typography
- **Font:** `Inter, system-ui, sans-serif` -- should be `Merriweather` (serif). E-ink style is defined by serif typography for a book/e-reader feel. The A-side loads both Merriweather and Source Sans 3.
- **Line-height:** 1.6 -- the A-side uses 1.8 for the generous reading rhythm that defines e-ink.
- **Missing:** Italic hero description text, dateline with small-caps, `max-width: 65ch` for optimal reading width.

### Border Radius
- 8px -- should be 0. E-ink/paper aesthetic is rectilinear with no rounding, like a printed page.

### Shadows & Depth
- `box-shadow: 0 2px 8px rgba(0,0,0,.06)` -- should be zero. Paper has no shadows. The A-side has zero shadows.

### Layout & Spacing
- **Max-width:** `1100px` -- far too wide. The A-side constrains everything to `560px` (close to 65ch) for book-like readability.
- **Hero:** Centered text -- the A-side uses left-aligned, column-style layout like a book page.

### Visual Effects
- No paper texture (the A-side has a subtle SVG noise texture via `body::before`).
- No decorative separator (`&bull; &bull; &bull;` in A-side).
- No dateline/volume number.

### Content & Voice
- Generic. Should use literary, contemplative language. A-side: "On the quiet beauty of paper and ink," "Volume XII -- Spring 2026."

### Missing Elements
- **Merriweather serif font** -- defines the reading experience
- **Source Sans 3** for UI labels (dual font system)
- **max-width: 560px (65ch)** content constraint
- **line-height: 1.8** for generous reading rhythm
- **Zero shadows**
- **Zero border-radius**
- **Paper texture** (SVG noise background)
- **Decorative text separators** (`&bull; &bull; &bull;`)
- **Warm brown palette** (#3D3529, #6B5F4D, #8A7E6B)
- **Italic text** for descriptive passages
- **Dateline** ("Volume XII" style)

### CSS Bugs
- No syntax errors, but font and layout fundamentally wrong for the style.

### Recommendations
1. Change font to `'Merriweather', Georgia, serif`
2. Add Source Sans 3 for labels and buttons
3. Set max-width to 560px for main content
4. Increase line-height to 1.8
5. Remove all shadows
6. Remove all border-radius
7. Add paper texture via SVG background
8. Use warm browns instead of neutral grays
9. Add decorative separators between sections
10. Left-align hero layout

---

## 9. Brutalism

**File:** `samples/brutalism.html`
**Style Authenticity Score: 1 / 10**

### Color Palette
- **B-side uses:** Black (#000) background with white text.
- **Problem:** Brutalism's defining palette is WHITE background with BLACK type. The A-side uses `var(--white)` background. The dark-mode treatment directly contradicts the raw, exposed HTML feel.
- **Missing:** Raw red (#FF0000) and blue (#0000FF) accent flashes present in the A-side.

### Typography
- **Font:** `Inter, system-ui, sans-serif` -- brutalism demands monospace (the A-side uses Space Mono). Monospace is essential for the "raw code" feeling.
- **Size/weight:** Normal web proportional type with -0.03em letter-spacing is the opposite of brutalist typography (which uses tight uppercase with wide letter-spacing).

### Border Radius
- **B-side:** `border-radius: 8px` on cards and buttons.
- **Required:** **Absolutely zero.** This is the most fundamental rule of brutalism. Zero radius, zero rounding, zero softening. The A-side has zero border-radius on everything.

### Shadows & Depth
- **B-side:** `box-shadow: 0 2px 8px rgba(0,0,0,.15)` on cards.
- **Required:** **Absolutely zero.** Brutalism has zero shadows, zero depth, zero elevation. The A-side has zero shadows. This is non-negotiable for the style.

### Layout & Spacing
- **B-side:** Centered hero, padded sections, auto-fit grid.
- **Required:** Full-width elements, zero padding concepts, thick 4px black borders as dividers, elements that touch edges. The A-side uses full-width nav buttons with `flex: 1`, `border-right: 4px solid var(--black)`, and no decorative spacing.

### Visual Effects
- `backdrop-filter: blur(12px)` -- absolutely wrong. Brutalism rejects all visual effects.
- `translateY(-3px)` hover -- wrong. Brutalism uses binary state changes (black to white swap).
- **Missing:** Thick 4px black borders on everything. The A-side's entire structure is defined by 4px solid black borders.

### Content & Voice
- Generic. Should be aggressive, raw, functional. A-side: "Raw Design," "No decoration. No pretense. Structure exposed."
- Should use uppercase text extensively.

### Missing Elements
- **White background, black text** (not inverted)
- **Space Mono monospace font**
- **border-radius: 0** on absolutely everything
- **box-shadow: none** on absolutely everything
- **4px solid black borders** on all elements
- **Full-width elements** that span the viewport
- **Zero gradients, zero blur, zero transparency**
- **Binary hover states** (background swap, not translate)
- **Uppercase text-transform** on headings and labels
- **Raw HTML feel** -- exposed grid markers, counters
- **Section labels** with border and background (#F0F0F0)
- **Grid-marker metadata** text

### CSS Bugs
- Every stylistic property contradicts brutalism. The border-radius, shadows, blur, rounded corners, and opacity transitions all violate the core tenets.

### Recommendations
1. White background, black text -- invert the entire scheme
2. Space Mono monospace font
3. `border-radius: 0` everywhere (add `!important` to override defaults)
4. `box-shadow: none` everywhere
5. `border: 4px solid #000` on all structural elements
6. Full-width sections with no max-width
7. Remove all backdrop-filter, translateY, opacity transitions
8. Add uppercase text-transform on all text
9. Binary hover: `&:hover { background: #000; color: #FFF; }`
10. Expose grid structure (counters, column/row labels)

---

## 10. Neubrutalism

**File:** `samples/neubrutalism.html`
**Style Authenticity Score: 1 / 10**

### Color Palette
- **B-side uses:** Black (#000) background with white text.
- **Problem:** Neubrutalism uses light/warm backgrounds (the A-side uses `#F5F0EB`). The dark background eliminates the playful, approachable feel that distinguishes neubrutalism from brutalism.
- **Missing:** Signature accent colors -- coral/pink (#FF6B6B), teal (#4ECDC4), yellow (#FFE66D) -- are completely absent.

### Typography
- **Font:** `Inter, system-ui, sans-serif` -- should be `Space Grotesk` as loaded. Space Grotesk's geometric personality matches neubrutalism's playful-but-structured feel.

### Border Radius
- **B-side:** 8px -- close but not quite. Neubrutalism uses 10-16px border-radius (larger than standard, contributing to the playful feel). The A-side uses 8-16px range. 8px is the minimum acceptable.

### Shadows & Depth
- **B-side:** `box-shadow: 0 2px 8px rgba(0,0,0,.15)` -- a soft diffused shadow.
- **Required:** Hard offset shadows with zero blur: `5px 5px 0 #000` (the A-side's `var(--shadow)`). The hard offset shadow is THE signature element of neubrutalism. Without it, the style does not exist.

### Layout & Spacing
- Centered hero -- acceptable for neubrutalism (the A-side is also centered).
- But cards should have visible thick borders and hard shadows, which are absent.

### Visual Effects
- **Missing 3px solid black borders** on all interactive elements.
- **Missing hard offset shadows** (`5px 5px 0 #000`) on cards, buttons, inputs.
- **Missing hover interaction**: Elements should shift toward shadow on hover (`transform: translate(3px, 3px); box-shadow: 2px 2px 0 #000`), not float upward.
- **Missing color banner** bars (the A-side has a tri-color repeating gradient banner on cards).
- **Missing rotated badge** (`transform: rotate(-2deg)`).
- **Missing pill-shaped tags** with borders.

### Content & Voice
- Generic. Should be playful, bold. A-side: "Bold ideas, raw edges," "Playfully brutal, unapologetically bold."

### Missing Elements
- **Light warm background** (#F5F0EB or similar)
- **Space Grotesk font**
- **3px solid black borders** on ALL interactive elements
- **5px 5px 0 #000 hard offset shadows** -- the defining signature
- **Coral (#FF6B6B), teal (#4ECDC4), yellow (#FFE66D)** accent fills
- **Hover: translate toward shadow** (not translateY up)
- **Card color banners** (tri-color stripe)
- **Rotated badge elements** with slight rotation
- **Pill-shaped elements** (border-radius: 50px on badges)
- **Input with shadow that collapses on focus**

### CSS Bugs
- Soft diffused shadow instead of hard offset shadow fundamentally breaks the style.
- No syntax errors, but every style choice is wrong for neubrutalism.

### Recommendations
1. Switch to light warm background (#F5F0EB), dark text
2. Use Space Grotesk font
3. Add `border: 3px solid #000` to all cards, buttons, inputs
4. Replace all shadows with `5px 5px 0 #000` (hard offset, zero blur)
5. Add coral, teal, yellow backgrounds to cards and buttons
6. Change hover to `transform: translate(3px, 3px); box-shadow: 2px 2px 0 #000`
7. Add tri-color banner stripe on cards
8. Add rotated badge element in hero
9. Use border-radius: 10-16px (not 8px)

---

## Score Summary

| # | Style | Score | Primary Issue |
|---|-------|-------|---------------|
| 1 | Minimalism | 2/10 | Dark bg inverts the style; has shadows and radius |
| 2 | Flat Design | 2/10 | Has shadows (forbidden); wrong font; wrong radius |
| 3 | Inclusive Design | 1/10 | No accessibility features; wrong font; fails WCAG |
| 4 | Bauhaus | 1/10 | Red bg destroys balance; no geometric shapes; wrong font |
| 5 | Single-Color | 3/10 | Correct blue tones but gray text breaks monochrome rule |
| 6 | Whitespace Maximalism | 1/10 | Dense layout is antithesis of style; name truncated |
| 7 | Mono Space | 1/10 | Uses proportional font (the ONE thing that cannot be wrong) |
| 8 | E-Ink | 2/10 | Warm bg is close; but serif font and narrow width missing |
| 9 | Brutalism | 1/10 | Has border-radius and shadows (both absolutely forbidden) |
| 10 | Neubrutalism | 1/10 | Missing hard offset shadows (the defining characteristic) |

**Average: 1.5 / 10**

---

## Root Cause Analysis

All B-sides were generated from a single template with a find-and-replace for the style name and a simple color swap. The template itself is a generic "dark SaaS landing page" with:

- Dark background with sticky blur header
- Centered hero with tagline, h1, paragraph, two buttons
- 3-column feature card grid with icon, heading, paragraph
- 4-column metrics row
- Centered blockquote with citation
- Centered footer with nav links

This template has no mechanism for expressing style-specific characteristics. Each B-side needs to be rebuilt from scratch using the A-side's design language as reference.

## Priority Fix Order

1. **Brutalism** and **Neubrutalism** -- these have the most extreme CSS requirements (zero radius/shadows vs. hard offset shadows) and are most visually broken
2. **Mono Space** -- wrong font family is instantly recognizable as broken
3. **Inclusive Design** -- accessibility failures have functional (not just aesthetic) consequences
4. **Bauhaus** -- missing geometric shapes eliminate the style entirely
5. **Whitespace Maximalism** -- layout density is the opposite of the style; name is truncated
6. **Minimalism** -- inverted color scheme is wrong but otherwise closest to correct
7. **E-Ink** -- warm background is close; needs font and width fixes
8. **Flat Design** -- needs shadow removal and correct font
9. **Single-Color** -- closest to correct; needs gray-to-blue text swap
10. **All** -- replace generic copy with style-specific content

---

*Report generated 2026-03-20 by UI Designer Agent*

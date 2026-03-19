# Audit Report 05: Retro & Nostalgic Styles -- B-Side Evaluation

**Auditor:** UI Designer Agent
**Date:** 2026-03-20
**Scope:** B-side CSS and HTML for 10 retro/nostalgic style sample pages
**Verdict:** All 10 B-sides use an identical generic template with only surface-level color token swaps. None authentically embody their respective design styles.

---

## Executive Summary

Every B-side in this batch follows the exact same structural template: a sticky header with logo and nav links, an 80vh centered hero with tagline/heading/paragraph/two buttons, a three-card features grid, a four-metric stats row, a centered pull-quote, and a footer. The only variations between files are the background color, the accent color applied to logos/tags/metrics/icons, and the text color (dark vs light scheme). The HTML content is word-for-word identical across all 10 files -- same headings ("What Sets Us Apart"), same card text ("A strong, recognizable aesthetic..."), same quote ("A truly distinctive design approach..."), same metrics ("100% / Unique / Bold / checkmark").

This means every B-side fails the fundamental test of style authenticity: the CSS contains no signature visual effects, the typography uses the generic `Inter, system-ui, sans-serif` stack for every style, and the layout is a cookie-cutter modern SaaS landing page. The detailed per-file analysis below documents the specific failures.

---

## 1. Retro-Futurism (`retro-futurism.html`)

**Style Authenticity Score: 2/10**

| Criterion | Assessment |
|---|---|
| **Color Palette** | Background is solid `#FF6B35` (burnt orange), accent `#004E64` (deep blue). These are correct palette colors from the A-side, but using burnt orange as a full-page background is garish and not how retro-futurism deploys color. The A-side uses deep navy `#1A1A2E` as base with orange as highlights. |
| **Typography** | Uses `Inter, system-ui, sans-serif`. Missing entirely: Orbitron (the signature space-age display font) and Space Mono. Retro-futurism demands geometric, wide-tracking display fonts. This is a critical failure. |
| **Border Radius** | Cards use `8px` rounded corners. Retro-futurism calls for either pill shapes (50px, as in the A-side CTA) or sharp geometric edges. The 8px is generic and style-inappropriate. |
| **Shadows & Depth** | Minimal `box-shadow: 0 2px 8px rgba(0,0,0,.06)` on cards. No neon glow, no chrome sheen, no radial gradient depth. The A-side has glowing box-shadows on orbit dots and CTA buttons. |
| **Layout & Spacing** | Generic SaaS template layout. Missing: starburst patterns, orbit rings, atomic decorations, or any space-age compositional elements. |
| **Visual Effects** | None. No chrome gradients, no rotating starbursts, no orbit animations, no radial gradient backgrounds. Zero retro-futurism DNA. |
| **Content & Voice** | Completely generic. "Distinctive by design", "What Sets Us Apart" -- no atomic-age vocabulary. Should reference: missions, orbits, space stations, thrusters, atomic energy. The A-side nails this with "Engage Thrusters" and "Space Station Alpha". |
| **Missing Elements** | Orbitron font, atomic/orbit motifs, starburst backgrounds, chrome buttons, pill-shaped CTAs, space-age color deployment (dark base + glowing accents), letter-spacing, uppercase text treatment. |
| **CSS Bugs** | No technical bugs, but `.bh` uses `background:#FF6B35;` which creates a stark orange header bar that would be visually jarring. |

---

## 2. Y2K Aesthetic (`y2k.html`)

**Style Authenticity Score: 2/10**

| Criterion | Assessment |
|---|---|
| **Color Palette** | Background is solid `#C0C0C0` (chrome silver), accent `#87CEEB` (sky blue). While silver is in the Y2K palette, the flat solid application misses the point entirely. Y2K demands chrome gradients, holographic shimmer, and iridescent surface treatments. |
| **Typography** | Uses `Inter, system-ui, sans-serif`. Missing: Quicksand (the A-side's bubbly, rounded font). Y2K typography is playful, rounded, and often features chrome/gradient text fills. |
| **Border Radius** | Cards use `8px`. Y2K demands heavily rounded pill shapes (50px radius) on buttons and bubbly, inflated-looking UI elements. The A-side correctly uses `border-radius: 50px` on all interactive elements. |
| **Shadows & Depth** | Flat, minimal shadows. Y2K requires glossy, pillowy depth -- multi-layer box-shadows with pastel glows, the "wet plastic" look. |
| **Layout & Spacing** | Generic grid layout. No bubbles, no floating decorations, no chrome sphere accents. |
| **Visual Effects** | None. Missing: chrome gradient text, holographic shimmer animations, bubble/sphere decorations, iridescent surfaces, backdrop-filter glass effects. The A-side has `holoShift` animation and chrome text gradients. |
| **Content & Voice** | Generic boilerplate. Should reference: digital butterflies, millennium dreams, chrome futures, cyber glamour. |
| **Missing Elements** | Chrome text gradients, holographic backgrounds, bubble decorations, glossy pill buttons, star/sparkle decorations, magenta+cyan color play, iridescent card surfaces. |
| **CSS Bugs** | No technical bugs. The flat silver background on a full page looks like unfinished UI rather than Y2K aesthetic. |

---

## 3. Vaporwave (`vaporwave.html`)

**Style Authenticity Score: 2/10**

| Criterion | Assessment |
|---|---|
| **Color Palette** | Background `#9B59B6` (flat purple), accent `#FF6B9D` (hot pink). The purple is correct conceptually, but vaporwave demands deep gradient backgrounds (purple-to-blue-to-pink horizon) not a flat solid. The A-side uses a masterful multi-stop gradient simulating a sunset horizon. |
| **Typography** | Uses `Inter, system-ui, sans-serif`. Missing: Press Start 2P (the A-side's pixel/retro font). Vaporwave uses either pixel fonts or full-width Japanese-inspired display faces. |
| **Border Radius** | `8px` on all elements. Vaporwave tends toward minimal radius (2-4px) or sharp edges, giving a digital/mechanical feel. |
| **Shadows & Depth** | Standard subtle shadows. Missing: neon glow effects (text-shadow with cyan/pink, box-shadow with neon spread). The A-side has `text-shadow: 0 0 10px #01CDFE` neon glow throughout. |
| **Layout & Spacing** | Generic centered layout. Missing: perspective grid floor, setting sun, horizon line -- the iconic vaporwave visual vocabulary. |
| **Visual Effects** | None. Missing: perspective grid animation, sunset/sun disc with scan lines, neon border glow, gradient text fills, scanline overlays, CRT curvature hints. |
| **Content & Voice** | Generic boilerplate. Should feature: spaced-out A E S T H E T I C lettering, references to plazas, late-night malls, smooth jazz, digital sunsets. |
| **Missing Elements** | Perspective grid, sun disc, horizon gradient, neon text glow, Press Start 2P font, scanline texture, cyan+magenta neon borders, italic dreamy body text. |
| **CSS Bugs** | No technical bugs. The solid purple background with `backdrop-filter:blur(12px)` on header is pointless since there is nothing behind it to blur. |

---

## 4. Pixel Art (`pixel-art.html`)

**Style Authenticity Score: 2/10**

| Criterion | Assessment |
|---|---|
| **Color Palette** | Background `#2C2137` (correct dark purple from A-side), accent `#446176` (muted blue-gray). The dark background is correct, but using the subdued gray-blue as the accent color instead of the bold gold `#F0C674` or pixel red `#CD4631` makes the page feel washed out. |
| **Typography** | Uses `Inter, system-ui, sans-serif`. This is the single most damaging failure for pixel art. The entire style identity depends on `Press Start 2P` or `VT323` -- a bitmap/pixel font is non-negotiable. Without it, nothing reads as 8-bit. |
| **Border Radius** | `8px` rounded corners on cards and buttons. Pixel art demands `0px` border-radius on everything. Rounded corners are antithetical to the 8-bit grid aesthetic. |
| **Shadows & Depth** | `box-shadow: 0 2px 8px rgba(0,0,0,.15)` -- smooth, diffused shadows. Pixel art requires hard-edge `box-shadow` offsets with zero blur (e.g., `4px 4px 0 #000`). The A-side correctly uses this throughout. |
| **Layout & Spacing** | Generic modern layout. Should feel like a game UI with chunky, grid-aligned elements. |
| **Visual Effects** | None. Missing: `image-rendering: pixelated`, box-shadow pixel art sprites, hard-edge button press animations (`translate(2px, 2px)`), pixel star backgrounds via box-shadow. |
| **Content & Voice** | Generic boilerplate. Should use game vocabulary: START GAME, Attack, Heal, Loot, Inventory, quest language. |
| **Missing Elements** | Pixel font, zero border-radius, hard-edge shadows, pixel art decorations, `image-rendering: pixelated`, chunky borders (3px solid), game-inspired UI metaphors, limited color palette feel. |
| **CSS Bugs** | No technical bugs. The hover effect `transform: translateY(-3px)` with smooth transition is antithetical to pixel art's snappy, discrete movement. |

---

## 5. Memphis Design (`memphis.html`)

**Style Authenticity Score: 2/10**

| Criterion | Assessment |
|---|---|
| **Color Palette** | Background `#FF6B6B` (coral red), accent `#4ECDC4` (teal). These are correct Memphis colors. Using coral as the full background is actually somewhat on-brand for Memphis's bold, clashing philosophy, though the A-side wisely uses yellow `#FFE66D` as hero background with coral as accents. |
| **Typography** | Uses `Inter, system-ui, sans-serif`. Missing: Rubik (the A-side's bold geometric sans-serif). Memphis demands extra-bold (900 weight), chunky typography. The B-side uses `font-weight: 800` on the h1, which helps slightly, but Inter is too refined and neutral for Memphis. |
| **Border Radius** | `8px` on all elements. Memphis uses zero radius (sharp corners) with thick black borders creating a graphic/print aesthetic. The A-side has `border: 3px solid #222` on everything. |
| **Shadows & Depth** | Soft, subtle shadows. Memphis requires hard-offset graphic shadows: `box-shadow: 6px 6px 0 #4ECDC4` with zero blur. This is a signature Memphis technique. |
| **Layout & Spacing** | Generic centered layout. Memphis should feel scattered, playful, and deliberately asymmetric. |
| **Visual Effects** | None. Missing: geometric scatter decorations (triangles, circles, zigzags), dot patterns, stripe patterns, multi-color top bars, circle/square shape alternation on swatches. The A-side has five different geometric decorations. |
| **Content & Voice** | Generic boilerplate. Should be bold, rebellious, playful: "GO BOLD", "Break Rules", "Radical", "Postmodern Vibes". |
| **Missing Elements** | Thick black borders, hard-offset shadows, geometric scatter decorations, dot/stripe patterns, alternating shape swatches, bold 900-weight display text, multi-color divider bars, text-shadow offsets. |
| **CSS Bugs** | No technical bugs. The coral background with generic card styling looks like a broken theme rather than Memphis design. |

---

## 6. Vintage Analog (`vintage-analog.html`)

**Style Authenticity Score: 2/10**

| Criterion | Assessment |
|---|---|
| **Color Palette** | Background `#D4A574` (warm tan), accent `#8B6914` (dark gold). The warm tone is directionally correct but too saturated and flat. The A-side uses `#F5EFE0` (aged cream paper) as the base -- a much softer, more authentic vintage surface. The B-side's tan reads more like a terracotta than aged paper. |
| **Typography** | Uses `Inter, system-ui, sans-serif`. Missing: Playfair Display (elegant serif) and Source Serif 4. Vintage analog absolutely requires serif typography -- this is foundational to the style. Serif fonts evoke letterpress, old books, and pre-digital printing. |
| **Border Radius** | `8px` rounded corners. Vintage/analog should use minimal radius (0-4px) or no radius, evoking physical photo prints and paper edges. |
| **Shadows & Depth** | Subtle modern shadows. Missing: vignette effect, film grain overlay, light leak gradient, sepia filter treatment. The A-side implements all four as layered pseudo-elements. |
| **Layout & Spacing** | Generic modern layout. Should feel like a photo album or vintage magazine with editorial sensibility. |
| **Visual Effects** | None. Missing: `filter: sepia()`, film grain SVG noise overlay, vignette box-shadow, light leak gradients, instant photo frame styling, desaturated color treatment. |
| **Content & Voice** | Generic boilerplate. Should reference: film rolls, darkroom development, archives, frame numbers, Kodak Portra. The A-side has beautiful copy like "Roll 24, Frame 18" and "Shot on Kodak Portra 400." |
| **Missing Elements** | Serif fonts, sepia/warm filtering, film grain texture, vignette, light leaks, photo frame elements, editorial dividers, italic styling, faded/aged color treatments. |
| **CSS Bugs** | No technical bugs. |

---

## 7. Cassette Futurism (`cassette-futurism.html`)

**Style Authenticity Score: 3/10**

| Criterion | Assessment |
|---|---|
| **Color Palette** | Background `#0A0A0A` (near-black), accent `#FFB000` (amber/industrial orange). This is the strongest color match of any B-side in this batch. Dark background with amber text directly evokes the Alien/Nostromo terminal aesthetic. |
| **Typography** | Uses `Inter, system-ui, sans-serif`. Missing: Courier New (the A-side's monospace terminal font). Cassette futurism is defined by monospaced, terminal-style typography. Inter is completely wrong for this style. |
| **Border Radius** | `8px` on all elements. Cassette futurism demands zero radius -- sharp, industrial, mechanical edges. Equipment bezels are rectangular, not rounded. |
| **Shadows & Depth** | Subtle modern shadows. Missing: amber CRT glow (`text-shadow: 0 0 20px rgba(255,176,0,0.4)`), scanline overlay, inset shadows simulating CRT screen curvature. |
| **Layout & Spacing** | Generic modern layout. Missing: bezel bar with LED indicators, VU meter decorations, equipment panel framing, industrial border treatments. |
| **Visual Effects** | None. Missing: scanline overlay (repeating-linear-gradient), LED indicator dots, blinking animations, VU meter bars, CRT glow/bloom, brushed-metal textures, "REC" indicators. The A-side has all of these. |
| **Content & Voice** | Generic boilerplate. Should use: industrial/technical vocabulary -- EXECUTE, INITIALIZE, ABORT, system modules, tape reels, baud rates. |
| **Missing Elements** | Monospace font, scanlines, LED indicators, VU meters, bezel/panel framing, CRT glow, blinking animations, zero border-radius, uppercase letter-spacing, industrial color accents (green/red/amber LEDs). |
| **CSS Bugs** | No technical bugs. The amber accent on dark is the most successful color pairing but the modern UI framework undermines it entirely. |

---

## 8. Retrocomputing / DOS Shell (`retrocomputing.html`)

**Style Authenticity Score: 2/10**

| Criterion | Assessment |
|---|---|
| **Color Palette** | Background `#000000` (black), accent `#00FF00` (green phosphor). This is correct -- the classic green-on-black CRT terminal palette. However, the B-side applies this as modern UI accents rather than as full-screen terminal emulation. |
| **Typography** | Uses `Inter, system-ui, sans-serif`. This destroys the retrocomputing aesthetic. The entire style identity is built on monospace fonts (Courier New, VT323). A proportional sans-serif font on a "retrocomputing" page is paradoxical. |
| **Border Radius** | `8px` on all elements. CRT terminals have zero border-radius. Period. The A-side correctly uses no rounded corners anywhere. |
| **Shadows & Depth** | Subtle modern shadows. Missing: phosphor glow text-shadow (`0 0 5px rgba(0,255,0,0.5)`), CRT vignette (radial gradient darkening edges), scanline overlay. |
| **Layout & Spacing** | Generic modern centered layout. Retrocomputing demands a text-mode, left-aligned, full-width terminal layout. The A-side uses DOS-style prompts, directory trees, and ASCII art -- all left-aligned with no max-width constraints. |
| **Visual Effects** | None. Missing: scanline overlay (both `body::before` and `body::after` in the A-side), blinking cursor, CRT curvature vignette, phosphor glow on all text, ASCII art rendering. |
| **Content & Voice** | Generic boilerplate. Should use: DOS commands (C:\>, dir /w), ASCII art, system specs (640K RAM, 20MB disk), file listings, [EXECUTE] bracket-style buttons. The A-side is a masterclass in authentic DOS voice. |
| **Missing Elements** | Monospace font, scanlines, CRT vignette, phosphor text glow, blinking cursor, ASCII art, DOS prompt styling, left-aligned terminal layout, menu bar styling, system info bar, bracket-button conventions. |
| **CSS Bugs** | No technical bugs. |

---

## 9. Polaroid / Instant Film (`polaroid.html`)

**Style Authenticity Score: 2/10**

| Criterion | Assessment |
|---|---|
| **Color Palette** | Background `#F5E6D3` (warm cream), accent `#E8D5C4` (barely-there beige). The cream background is correct, but the accent color is far too close to the background -- there is almost no contrast. The A-side uses `#8B6F47` (rich brown) and `#4A3728` (dark walnut) as meaningful contrast points against the cream. |
| **Typography** | Uses `Inter, system-ui, sans-serif`. Missing: Caveat (the handwriting/cursive font that is absolutely central to the Polaroid aesthetic). Instant film captions are handwritten -- this is non-negotiable for the style. |
| **Border Radius** | `8px` on all elements. Polaroid frames have sharp corners (0-2px radius). The thick white border with sharp edges is the defining visual element. |
| **Shadows & Depth** | Subtle shadows. Missing: the specific polaroid shadow -- slightly warm, soft, conveying a physical object sitting on a surface. The A-side uses `box-shadow: 2px 4px 16px var(--shadow)` with warm-toned `rgba(74,55,40,.15)`. |
| **Layout & Spacing** | Generic centered layout. Should feature: scattered polaroid frames at slight rotations, a gallery wall feel with overlapping photos, tape/pin decorations. |
| **Visual Effects** | None. Missing: slight CSS rotation on cards (`transform: rotate(-3deg)`), thick white borders simulating instant film, warm gradient photo placeholders, tape decoration elements, hover-to-straighten interactions. The A-side rotates each polaroid differently and straightens on hover. |
| **Content & Voice** | Generic boilerplate. Should be warm, personal, handwritten-feeling: "Moments Worth Keeping", "Summer '25 -- the good old days", "Golden hour walk", story dates. The A-side has charming, intimate copy. |
| **Missing Elements** | Caveat handwriting font, polaroid frame styling (thick bottom border), slight rotations, warm photo gradients, tape decorations, gallery wall scatter layout, handwritten captions, personal/nostalgic copy, dashed footer border. |
| **CSS Bugs** | The accent color `#E8D5C4` used for the logo, tags, metrics, and icons is nearly invisible against the `#F5E6D3` background. This is a contrast/readability failure -- these elements would be essentially invisible. The WCAG contrast ratio between `#E8D5C4` and `#F5E6D3` is approximately 1.1:1, failing even the minimum 3:1 for large text. |

---

## 10. Chalkboard (`chalkboard.html`)

**Style Authenticity Score: 3/10**

| Criterion | Assessment |
|---|---|
| **Color Palette** | Background `#2D4A3E` (dark green), accent `#F0EDE5` (chalk white). This is the correct chalkboard palette and is the best color match in this entire batch. The dark green board with chalk-white text is immediately recognizable. |
| **Typography** | Uses `Inter, system-ui, sans-serif`. Missing: Patrick Hand (the handwriting font loaded in the A-side). Chalkboard style requires a hand-drawn font to simulate chalk writing. `Inter` is a clean geometric sans-serif -- the polar opposite of chalk. |
| **Border Radius** | `8px` on all elements. Chalkboard elements should have minimal radius (2-4px) with dashed borders simulating chalk outlines. The A-side uses `border: 2px dashed var(--chalk-dim)`. |
| **Shadows & Depth** | Standard modern shadows. Missing: chalk text shadow (`text-shadow: 1px 1px 2px rgba(0,0,0,.3)`), the subtle uneven quality of chalk marks. |
| **Layout & Spacing** | Generic modern centered layout. Missing: wooden frame border, full-chalkboard-surface feel, hand-drawn sketch lines, tally marks, checklist formatting. |
| **Visual Effects** | None. Missing: wooden frame border (`border: 12px solid #5C3A1E`), chalk dust smudge effects, dashed-border cards, subtle radial gradient simulating uneven board lighting, wavy underline hover on links. |
| **Content & Voice** | Generic boilerplate. Should use classroom vocabulary: "Today's Lesson", "Key Concepts", chapters, attendance tallies, to-do checklists, professor attribution. The A-side is full of charming classroom detail. |
| **Missing Elements** | Patrick Hand font, wooden frame border, dashed borders throughout, chalk-colored accent marks (yellow, pink, blue, orange), tally marks, checklist items, sketch lines, erased text effect, chalk dust smudges, wavy underline hovers, classroom-themed content. |
| **CSS Bugs** | No technical bugs. The green background with white accent is the most style-coherent combination in this batch, though the modern UI framework still undermines it. |

---

## Cross-Cutting Issues (All 10 B-Sides)

### 1. Template Reuse Problem
Every B-side uses the exact same HTML structure and nearly identical CSS, differing only in:
- `background` color on `.b-side`
- Accent color used for `.bh .logo`, `.bhero-tag`, `.bst`, `.bmet-v`, `.bcard-icon`, `.bfoot .logo`
- Light/dark text scheme (`color: #000` vs `color: #fff`)

### 2. Identical Content
All 10 files contain word-for-word identical content:
- Hero tag: "Distinctive by design"
- Hero heading: "[Style Name] Style."
- Hero paragraph: "A distinctive visual approach that brings unique character and personality to every interface."
- Card headings: "Visual Identity", "Consistent Language", "Authentic Detail"
- All card descriptions, metrics, and quotes are identical

### 3. Universal Font Failure
All 10 B-sides use `Inter, system-ui, sans-serif` regardless of style. Not a single B-side loads or references the style-appropriate font from its A-side counterpart.

### 4. Uniform Layout
All 10 B-sides use the identical layout pattern:
- Sticky header with 8px rounded-corner buttons
- 80vh centered hero
- Three-card grid with 8px rounded corners
- Four-column metrics
- Centered blockquote
- Centered footer

### 5. No Signature Effects
Not one B-side implements any signature visual effect from its style:
- No scanlines, no neon glow, no pixel shadows, no chrome gradients
- No sepia filters, no film grain, no vignettes
- No dashed borders, no hard-offset shadows, no geometric decorations
- No perspective grids, no orbit animations, no chalk textures

---

## Scoring Summary

| # | Style | Score | Best Aspect | Worst Aspect |
|---|---|---|---|---|
| 1 | Retro-Futurism | 2/10 | Uses palette colors as bg/accent | No Orbitron font, no space-age effects |
| 2 | Y2K Aesthetic | 2/10 | Silver background nod | No chrome gradients, no glossy pills |
| 3 | Vaporwave | 2/10 | Purple + pink pairing | No perspective grid, no neon glow |
| 4 | Pixel Art | 2/10 | Dark background maintained | No pixel font, rounded corners, smooth shadows |
| 5 | Memphis Design | 2/10 | Coral + teal color match | No thick borders, no geometric scatter |
| 6 | Vintage Analog | 2/10 | Warm tone attempt | No serif font, no sepia/grain/vignette |
| 7 | Cassette Futurism | 3/10 | Best color pairing (amber on black) | No monospace font, no scanlines/LEDs |
| 8 | Retrocomputing | 2/10 | Green-on-black phosphor colors | No monospace, no terminal layout, no CRT effects |
| 9 | Polaroid | 2/10 | Cream background correct | Accent nearly invisible (1.1:1 contrast) |
| 10 | Chalkboard | 3/10 | Best overall color coherence | No handwriting font, no chalk/board textures |

**Overall Average: 2.2/10**

---

## Recommendations

To bring each B-side to a minimum acceptable authenticity score (7/10), each file needs at minimum:

1. **Load the style-appropriate Google Font** and apply it to `.b-side` (not Inter)
2. **Replace the background** with a style-appropriate treatment (gradient, texture, pattern -- not a flat solid)
3. **Adjust border-radius** per style demands (0px for pixel/retro/terminal, 50px for Y2K pills, 2px for vintage)
4. **Add 2-3 signature visual effects** via CSS (scanlines, glow, grain, hard shadows, geometric decorations)
5. **Rewrite all content** to match each style's voice and vocabulary
6. **Customize card/section styling** to use style-specific border treatments, shadow types, and interaction patterns
7. **Fix the Polaroid contrast bug** -- the accent color must be distinguishable from the background

---

*Report generated by UI Designer Agent -- 2026-03-20*

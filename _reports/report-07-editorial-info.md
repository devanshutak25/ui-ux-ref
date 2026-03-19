# B-Side Audit Report 07 -- Editorial & Informational Styles

**Auditor:** UI Designer Agent
**Date:** 2026-03-20
**Scope:** 10 sample pages -- B-side CSS and HTML evaluation for style authenticity

---

## Systemic Finding: Identical Template Problem

Before evaluating each style individually, a critical overarching issue must be noted. **All 10 B-sides use an identical generic template.** The HTML structure is copy-pasted verbatim across every file:

- Same header (`.bh`) with logo + four generic nav links (Home, About, Work, Contact)
- Same 80vh centered hero with tagline "Distinctive by design", title "[Style Name] Style.", and identical body copy
- Same three-card feature grid with diamond/lozenge/asterisk icons and identical text
- Same four-metric row (100%, Unique, Bold, checkmark)
- Same blockquote ("A truly distinctive design approach...")
- Same footer with Privacy/Terms/Contact

The only customization across files is **color token substitution** -- swapping the accent color and background color into the template variables. The HTML content, layout structure, section ordering, and copy are all identical.

This means every B-side fails as a style demonstration because the template itself has no style-specific structural, typographic, or layout adaptations. The scores below reflect this fundamental deficiency.

---

## 1. Newspaper Classified (`newspaper.html`)

**Style Authenticity Score: 2/10**

| Criterion | Assessment |
|-----------|------------|
| **Color Palette** | Background is `#F5F5DC` (beige), accent is `#333333`. Reasonable warm tone but lacks the A-side's `#F4F1EA` newsprint warmth. No black ink vs. paper contrast. |
| **Typography** | Uses `Inter, system-ui, sans-serif`. WRONG. Newspaper style demands a serif body font (Libre Baskerville is loaded in the `<head>` but unused by the B-side). No monospace for metadata. |
| **Border Radius** | `8px` on cards and buttons. WRONG. Newspapers use `0` border-radius -- sharp rectangular shapes mimicking print. |
| **Shadows & Depth** | Generic card shadow `0 2px 8px rgba(0,0,0,.06)`. WRONG. Newspapers are flat -- depth comes from rule lines, not drop shadows. |
| **Layout & Spacing** | Single centered column with uniform grid. WRONG. Newspaper style requires multi-column layout with `column-count`, thin rule dividers between columns, and dense information packing. The A-side demonstrates this correctly. |
| **Visual Effects** | No column rules, no thin horizontal rules, no double-rule borders, no dashed classified dividers, no pull quotes. MISSING ALL signature elements. |
| **Content & Voice** | Generic corporate copy ("Distinctive by design", "What Sets Us Apart"). WRONG. Should use newspaper-specific language: datelines, bylines, classified ad copy, editorial voice. |
| **Missing Elements** | Masthead, column layout, thin rules, double-rule borders, classifieds-style dense type, justified text, hyphens, bylines, pull quotes, all-caps section headers. |
| **CSS Bugs** | No syntax errors, but the `.bh .logo` class uses `::before` from the A-side's `.logo` class which could conflict when the A-side body pseudo-elements are active. |

---

## 2. Editorial Grid (`editorial-grid.html`)

**Style Authenticity Score: 2/10**

| Criterion | Assessment |
|-----------|------------|
| **Color Palette** | Background `#000000`, text white. This captures the A-side hero's dark theme but misses the warm off-white (`#F5F5F0`) body and the critical crimson accent (`#DC143C`) that defines editorial style. The accent `#FFFFFF` is just white. |
| **Typography** | Uses `Inter, system-ui, sans-serif`. WRONG. Editorial grid demands oversized Playfair Display serif for display headlines (loaded but unused). No italic serif for pull quotes. No drop-cap styling. |
| **Border Radius** | `8px` on cards. WRONG. Editorial/magazine layouts use `0` radius -- sharp geometric frames with thin rule borders. |
| **Shadows & Depth** | Generic card shadows. WRONG. Editorial style uses flat design with depth from whitespace and typographic scale, not box shadows. |
| **Layout & Spacing** | Symmetric three-column auto-fit grid. WRONG. Editorial grid specifically requires asymmetric layouts -- unequal column widths, dramatic whitespace, and intentional tension between elements. |
| **Visual Effects** | No thin rules, no oversized drop caps, no accent color bars, no asymmetric grid, no pull quotes with colored left borders. MISSING ALL signature elements. |
| **Content & Voice** | Identical generic copy. Should use magazine-style editorial voice: issue numbers, volume references, quotations, author attribution. |
| **Missing Elements** | Asymmetric grid, Playfair Display typography, crimson accent color, drop caps, thin rule dividers, editorial pull quotes, oversized headline hierarchy, italic serif styling. |
| **CSS Bugs** | No syntax errors. |

---

## 3. Bento Box Grid (`bento-grid.html`)

**Style Authenticity Score: 2/10**

| Criterion | Assessment |
|-----------|------------|
| **Color Palette** | Background `#F5F5F7` with accent `#1D1D1F`. Matches Apple's silver/dark palette. But the B-side should use pure black background with charcoal cards, not light gray. The spec calls for "pure black, dark charcoal cards." |
| **Typography** | Uses `Inter` which is close but the A-side's Apple aesthetic demands SF Pro Display or at minimum a tighter letter-spacing system with specific weight usage. Acceptable but not ideal. |
| **Border Radius** | `8px` on cards. WRONG. Bento grid style uses `16-20px` radius (the A-side uses `20px`). Apple's signature is generous, smooth radius. |
| **Shadows & Depth** | Generic small shadow. WRONG. Bento style uses barely-there borders (`rgba(0,0,0,.08)`) with almost no shadow -- depth comes from card color differentiation against the dark background. |
| **Layout & Spacing** | Standard three-column auto-fit grid. WRONG. Bento grid specifically requires mixed-size cells -- some spanning 2 columns (`.wide`), some small, creating the characteristic bento box arrangement. The A-side demonstrates this with `grid-column: 1 / -1` spanning items. |
| **Visual Effects** | No mixed-size grid cells, no dark/blue variant cards, no large display numbers, no pill-shaped buttons. MISSING ALL signature elements. |
| **Content & Voice** | Generic copy. Should use Apple-style terse, aspirational copy: large metric numbers, minimal descriptions, technology-focused language. |
| **Missing Elements** | Mixed-size bento grid, dark background, charcoal cards, 20px border radius, pill buttons (980px radius), blue accent `#0071E3`, large display metrics, Apple-style minimal copy. |
| **CSS Bugs** | No syntax errors. |

---

## 4. Receipt / Thermal Print (`receipt.html`)

**Style Authenticity Score: 1/10**

| Criterion | Assessment |
|-----------|------------|
| **Color Palette** | Background `#FFFFFF`, accent `#F5F5F5`. WRONG. The light gray accent on white background is nearly invisible. Should use yellowed paper `#faf8f4` background with `#2a2a2a` dark text. |
| **Typography** | Uses `Inter, system-ui, sans-serif`. CRITICALLY WRONG. Receipt style absolutely requires monospace (`IBM Plex Mono` is loaded in `<head>` but unused). This is the most defining characteristic of a receipt -- monospaced thermal print font. |
| **Border Radius** | `8px` on cards and buttons. WRONG. Receipt style uses `0` radius -- thermal printers produce sharp-edged output. |
| **Shadows & Depth** | Generic card shadows. WRONG. Receipts are flat paper. No shadows. If anything, a slight paper curl shadow on the wrapper. |
| **Layout & Spacing** | Full-width 1100px max container. WRONG. Receipt style demands narrow width (380px max), single centered column, mimicking the physical dimensions of a thermal receipt. |
| **Visual Effects** | No dashed dividers, no torn paper edge, no barcode, no monospace line items, no thermal fade effect. MISSING ALL signature elements. |
| **Content & Voice** | Generic corporate copy. Should use transactional receipt language: line items, prices, totals, timestamps, transaction numbers, "THANK YOU" messages. |
| **Missing Elements** | Narrow 380px width, monospace font, dashed `hr` dividers, torn paper edge (zigzag), barcode, line-item format, total calculations, timestamp footer, thermal fade effect, yellowed paper color. |
| **CSS Bugs** | The accent color `#F5F5F5` used for `.bh .logo`, `.bhero-tag`, `.bst`, `.bmet-v`, `.bfoot .logo` is nearly invisible against the `#FFFFFF` background. This is a functional visibility bug -- key text elements are unreadable. |

---

## 5. Passport / Official Document (`passport.html`)

**Style Authenticity Score: 3/10**

| Criterion | Assessment |
|-----------|------------|
| **Color Palette** | Background `#003366` with gold `#FFD700` accent. This is the strongest color match of any B-side -- deep navy background with gold accents correctly evokes passport/official document styling. |
| **Typography** | Uses `Inter, system-ui, sans-serif`. WRONG. Passport style requires `Playfair Display` or similar serif for formality, plus `IBM Plex Mono` for MRZ/data fields. Neither is used despite being loaded. |
| **Border Radius** | `8px` on cards and buttons. WRONG. Official documents use `0` radius -- sharp rectangles conveying authority and formality. |
| **Shadows & Depth** | Generic card shadows. WRONG. Passport style should use inset borders (double borders for frames), not drop shadows. |
| **Layout & Spacing** | Standard template layout. Acceptable width but missing the formal document structure -- field labels, data rows, document sections. |
| **Visual Effects** | No guilloche patterns, no seal/emblem, no MRZ zone, no stamp overlays, no double-border inset frames, no gold border accents. MISSING ALL signature elements. |
| **Content & Voice** | Generic copy. Should use official/governmental language: "Bearer is entitled to...", document numbers, field labels (Surname, Given Names, Nationality), authority stamps. |
| **Missing Elements** | Guilloche background pattern, official seal, MRZ data zone, stamp/watermark overlays, parchment-colored content areas, gold border accents, formal field labels, document-style data presentation. |
| **CSS Bugs** | No syntax errors. The color scheme is at least recognizable as passport-themed. |

---

## 6. Cartographic / Wayfinding (`cartographic.html`)

**Style Authenticity Score: 2/10**

| Criterion | Assessment |
|-----------|------------|
| **Color Palette** | Background `#2D5016` (dark green) with `#4682B4` (steel blue) accent. The green background is somewhat map-like but the A-side uses parchment `#f4ede1` as the base. The earthy palette of greens, blues, and browns is partially captured but inverted from the intended light parchment map surface. |
| **Typography** | Uses `Inter, system-ui, sans-serif`. WRONG. Cartographic style requires monospace (`DM Mono`) for coordinates and data labels, plus serif (`Source Serif 4`) for titles. Neither is used. |
| **Border Radius** | `8px` on cards. WRONG. Cartographic elements use `0` radius -- maps have sharp rectangular legend boxes and label frames. |
| **Shadows & Depth** | Generic card shadows. WRONG. Maps are flat -- depth comes from layered contour lines and coordinate grids, not box shadows. |
| **Layout & Spacing** | Standard template grid. WRONG. Should include a legend box, coordinate annotations, contour-line backgrounds, and map-specific layout elements. |
| **Visual Effects** | No contour lines, no coordinate grid overlay, no compass rose, no legend box, no "Fig." labels, no dashed trail lines. MISSING ALL signature elements. |
| **Content & Voice** | Generic copy. Should use geographic/survey language: coordinates, scale ratios, elevation data, survey point references. |
| **Missing Elements** | Parchment background, contour line overlays, coordinate grid, compass rose, legend box with colored line samples, monospace coordinate labels, "Fig." card labels, earthy color palette on light surface. |
| **CSS Bugs** | No syntax errors. The dark green background creates poor contrast with `#aaa` text elements. |

---

## 7. Subway / Transit Diagram (`subway-map.html`)

**Style Authenticity Score: 2/10**

| Criterion | Assessment |
|-----------|------------|
| **Color Palette** | Background `#FFFFFF` with `#FF0000` accent. White background is correct for transit diagrams, but `#FF0000` is pure red rather than the A-side's more specific transit red `#e4002b`. Missing blue, green, gold, and purple route colors. |
| **Typography** | Uses `Inter, system-ui, sans-serif`. Acceptable. DM Sans (the A-side font) is similar in character to Inter. This is the least problematic typography mismatch. |
| **Border Radius** | `8px` on cards. PARTIALLY WRONG. Transit style uses `50px` pill-shaped buttons and `50%` circular badges. Cards use `12px` in the A-side. The `8px` is slightly low. |
| **Shadows & Depth** | Generic card shadows. WRONG. Transit diagrams are flat schematic designs -- no shadows. Thick solid borders (`2.5px`) define elements instead. |
| **Layout & Spacing** | Standard template grid. WRONG. Should include a transit map diagram with colored route lines, station dots, and interchange markers. |
| **Visual Effects** | No route lines, no station circles, no interchange markers, no route badge circles, no thick border styling, no schematic map illustration. MISSING ALL signature elements. |
| **Content & Voice** | Generic copy. Should use transit language: station names, line designations, journey planning, accessibility info, wait times. |
| **Missing Elements** | Transit map diagram, colored route lines (R/B/G/Gold), station circles with labels, interchange nodes, route badge circles, thick ink borders (`3px`), pill-shaped buttons, thick border-bottom on nav. |
| **CSS Bugs** | No syntax errors. |

---

## 8. Collage Zine (`collage-zine.html`)

**Style Authenticity Score: 1/10**

| Criterion | Assessment |
|-----------|------------|
| **Color Palette** | Background `#000000` with `#FFFFFF` accent. WRONG. Collage/zine style uses paper-colored background (`#F2EDE4`) with black ink and limited red. The dark mode inversion completely undermines the paper/photocopy aesthetic. |
| **Typography** | Uses `Inter, system-ui, sans-serif`. CRITICALLY WRONG. Zine style demands mixed fonts -- `Special Elite` (typewriter), `Archivo Black` (bold display), deliberately mismatched sizes and weights. The uniform sans-serif destroys the collage effect entirely. |
| **Border Radius** | `8px` on cards. WRONG. Zine/punk aesthetic uses `0` radius -- raw, unfinished rectangles. Rounded corners are antithetical to the DIY ethos. |
| **Shadows & Depth** | Generic card shadows. WRONG. Zine style uses hard offset shadows (`4px 4px 0`) or no shadows at all -- tape strips and overlapping elements create depth. |
| **Layout & Spacing** | Clean centered grid. WRONG. Zine style demands chaotic, overlapping layout with random rotations (`transform: rotate()`), misaligned elements, and deliberate visual disorder. |
| **Visual Effects** | No tape strips, no torn edges, no ransom-note mixed typography, no rotation on elements, no overlapping, no stamp marks, no cut-here marks, no paper texture. MISSING ALL signature elements. |
| **Content & Voice** | Generic corporate copy. Should use punk/DIY zine language: manifestos, cut-paste instructions, issue numbers, raw emotional tone. |
| **Missing Elements** | Paper texture, tape strips, torn edges, mixed/ransom-note typography, random element rotation, overlapping layout, B&W + red-only color restriction, stamp marks, "CUT HERE" marks, photocopied texture. |
| **CSS Bugs** | No syntax errors, but the entire design is thematically inverted. |

---

## 9. Whiteboard / Collaborative Canvas (`whiteboard.html`)

**Style Authenticity Score: 1/10**

| Criterion | Assessment |
|-----------|------------|
| **Color Palette** | Background `#FFFFFF` with `#FFF3BF` (light yellow) accent. White background is correct for whiteboard, but the accent color `#FFF3BF` is nearly invisible on white. Should use marker colors (blue `#2D5BD7`, red `#E8453C`, green `#2DA562`) as accents, with pastel sticky note colors for cards. |
| **Typography** | Uses `Inter, system-ui, sans-serif`. WRONG. Whiteboard style demands `Caveat` handwriting font for all primary text. The hand-drawn, informal quality is the defining characteristic. |
| **Border Radius** | `8px` on cards. PARTIALLY ACCEPTABLE. The A-side uses `6px` which is close. But the cards should look like sticky notes, not generic rounded rectangles. |
| **Shadows & Depth** | Generic card shadows. PARTIALLY WRONG. Should use sticky-note-style shadows (`2px 3px 6px`) with visible offset direction, plus tape strips pseudo-elements. |
| **Layout & Spacing** | Standard grid. WRONG. Should feature sticky notes with slight random rotations, a dot-grid background overlay, marker-colored borders, and tape/pin decorations. |
| **Visual Effects** | No dot-grid background, no sticky notes, no tape strips, no handwriting font, no marker-colored borders, no slight rotation on elements, no sketch-box illustrations. MISSING ALL signature elements. |
| **Content & Voice** | Generic copy. Should use collaborative/brainstorming language: quick notes, action items, idea fragments, "Ship the MVP", informal tone. |
| **Missing Elements** | Dot-grid background, Caveat handwriting font, pastel sticky notes (yellow/pink/blue), tape strip decorations, marker-colored borders, slight element rotation, sketch boxes, dashed input borders, collaborative/informal copy. |
| **CSS Bugs** | The accent color `#FFF3BF` is extremely low contrast against `#FFFFFF` background. The logo, tagline, section titles, metric values, and footer logo are all nearly invisible. This is a significant accessibility and readability failure. |

---

## 10. Conversion-Optimized (`conversion-optimized.html`)

**Style Authenticity Score: 1/10**

| Criterion | Assessment |
|-----------|------------|
| **Color Palette** | Background `#FF6B35` (solid orange). WRONG. The A-side correctly uses white background with orange as a CTA accent color. Making the entire page background orange completely inverts the conversion-optimized approach where orange should be reserved for attention-grabbing call-to-action buttons against a clean white surface. |
| **Typography** | Uses `Inter` which is correct for conversion-optimized style. The one correct element. |
| **Border Radius** | `8px` on cards. ACCEPTABLE. The A-side uses `6-12px` radius which is in range. |
| **Shadows & Depth** | Generic card shadows. PARTIALLY WRONG. Conversion style uses strategic shadows on CTAs (`box-shadow: 0 4px 14px rgba(255,107,53,.35)`) and featured pricing cards, not uniform shadows everywhere. |
| **Layout & Spacing** | Standard template grid. WRONG. Conversion-optimized layout requires a very specific structure: hero with CTA above fold, trust badges, pricing comparison table, testimonial cards with star ratings, urgency banners, and footer. |
| **Visual Effects** | No prominent CTA buttons, no trust badges, no pricing comparison grid, no testimonial cards with stars, no urgency/scarcity messaging, no "Most Popular" badge, no social proof numbers. MISSING ALL signature elements. |
| **Content & Voice** | Generic copy. CRITICALLY WRONG. Conversion-optimized style is entirely defined by its persuasive copy: "Start Free Trial", "No credit card required", "12,000+ teams", "34% conversion increase", scarcity urgency, specific pricing. |
| **Missing Elements** | White background, orange CTA buttons (not orange background), trust badge row, pricing comparison table with featured plan, testimonial cards with star ratings, urgency banner, social proof numbers, "Start Free Trial" CTAs, "Most Popular" badges, specific benefit-driven copy. |
| **CSS Bugs** | Dark gray text (`#666`) on bright orange (`#FF6B35`) background fails WCAG AA contrast requirements. The body copy is difficult to read. Card backgrounds at `rgba(0,0,0,.02)` are barely visible against orange. |

---

## Summary Scorecard

| # | Style | Score | Primary Failure |
|---|-------|-------|----------------|
| 1 | Newspaper | 2/10 | No multi-column layout, serif fonts, or thin rules |
| 2 | Editorial Grid | 2/10 | No asymmetric grid, serif display type, or accent color |
| 3 | Bento Grid | 2/10 | No mixed-size cells, wrong radius, not dark enough |
| 4 | Receipt | 1/10 | No monospace font, no narrow width, invisible accent color |
| 5 | Passport | 3/10 | Best color match but no guilloche, seals, or formal structure |
| 6 | Cartographic | 2/10 | No contour lines, legend box, or coordinate systems |
| 7 | Subway Map | 2/10 | No route lines, station circles, or transit diagram |
| 8 | Collage Zine | 1/10 | Inverted color scheme, no mixed fonts or chaotic layout |
| 9 | Whiteboard | 1/10 | No handwriting font, sticky notes, or dot grid; invisible accent |
| 10 | Conversion-Optimized | 1/10 | Orange background inverts CTA strategy; no pricing/testimonials |

**Average Score: 1.7/10**

---

## Root Cause Analysis

All B-sides were generated from a single generic template with only two customization points:

1. **Background color** -- picked from the style's palette (often incorrectly)
2. **Accent color** -- used for logo, tagline, metrics, and hover states

Everything else is identical: layout structure, HTML content, typography (always Inter/system-ui), border radius (always 8px), shadow system, section ordering, and copy text.

The template lacks any mechanism for:
- Style-specific fonts (even though Google Fonts are loaded in the `<head>`)
- Style-specific layout patterns (columns, asymmetry, narrow width)
- Signature visual elements (sticky notes, route lines, torn edges, contour lines)
- Thematic content and voice
- Style-appropriate border-radius values
- Style-appropriate shadow/depth treatments

---

## Recommendations

1. **Each B-side needs a unique layout structure** that reflects its style's defining characteristics (multi-column for newspaper, narrow single-column for receipt, bento grid for bento, etc.)

2. **Typography must match the style** -- use the Google Fonts already loaded in each file's `<head>` tag. The fonts are right there, just not referenced in the B-side CSS.

3. **Color application needs inversion awareness** -- accent colors should not become background colors. The conversion-optimized page making orange the background instead of the CTA color is the clearest example of this mistake.

4. **Signature elements are non-negotiable** -- a newspaper without columns is not a newspaper; a receipt without monospace is not a receipt; a whiteboard without handwriting is not a whiteboard. Each B-side needs 3-5 CSS-only signature elements.

5. **Content must be style-appropriate** -- even placeholder copy should match the style's voice and domain vocabulary.

6. **Contrast bugs need fixing** -- Receipt (#F5F5F5 on #FFFFFF) and Whiteboard (#FFF3BF on #FFFFFF) have text that is effectively invisible.

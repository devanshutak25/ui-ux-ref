# Audit Report 02 -- Surface & Material Styles (B-Side)

**Date:** 2026-03-20
**Auditor:** UI Designer Agent
**Category:** Surface & Material (10 styles)
**Scope:** B-side CSS and HTML only

---

## Executive Summary

All 10 B-sides in this category use an identical generic template. The HTML structure, class names, section layout, copy text, and card/metrics/quote sections are the same across every file. The only differentiation is a superficial color token swap applied to the accent color and background. None of the B-sides authentically embody their respective design style. The template is a flat, minimal landing page with `8px` border-radius cards, thin `1px` borders, `translateY(-3px)` hover effects, and `Inter` as the font family -- characteristics that belong to no specific style and actively contradict many of them.

**Aggregate Score: 1.6 / 10**

---

## 1. Glassmorphism (`glassmorphism.html`)

### Style Authenticity Score: 2 / 10

| Criterion | Assessment |
|---|---|
| **Color Palette** | Background is solid `#667eea` (one of the gradient stops from the A-side). No gradient background, no vibrant color field behind translucent panels. Accent color `#764ba2` is used for text only. The entire point of glassmorphism is color showing *through* frosted layers -- there is nothing to show through. |
| **Typography** | Uses `Inter` which is acceptable for glassmorphism, but the font is declared generically as `font-family:Inter,system-ui,sans-serif` without loading Google Fonts in the B-side scope. The A-side loads Inter via Google Fonts, so it will render if A-side CSS loaded first, but the B-side relies on this side effect. |
| **Border Radius** | `8px` on cards and buttons. Glassmorphism demands `16px` radius as a minimum. This is too sharp. |
| **Shadows & Depth** | Cards use `box-shadow:0 2px 8px rgba(0,0,0,.06)` -- a generic light shadow. Glassmorphism requires no traditional box-shadow; its depth comes from backdrop-filter blur and translucent layering. |
| **Layout & Spacing** | Standard centered hero + grid sections. Acceptable layout but nothing glass-specific. |
| **Visual Effects** | **CRITICAL FAILURE:** No `backdrop-filter: blur()`. No `rgba()` semi-transparent backgrounds on panels. No translucent borders (`border: 1px solid rgba(255,255,255,0.2)`). The singular defining CSS property of glassmorphism is completely absent. |
| **Content & Voice** | Generic copy: "A distinctive visual approach that brings unique character..." -- this is boilerplate shared across all 10 files. No glass-related language. |
| **Missing Elements** | Backdrop-filter blur on all panels; vibrant gradient background; floating orbs or colorful shapes behind glass; translucent rgba backgrounds on cards; frosted border treatment; light refraction or glow effects. |
| **CSS Bugs** | No bugs per se, but the B-side background (`#667eea`) is a flat solid color, making even hypothetical translucent panels pointless. The logo color `#764ba2` against `#667eea` background has questionable contrast. |

---

## 2. Neumorphism (`neumorphism.html`)

### Style Authenticity Score: 2 / 10

| Criterion | Assessment |
|---|---|
| **Color Palette** | Background `#E0E5EC` is correct -- this is the canonical neumorphism surface color. However, it is only used as a flat backdrop. The accent color is `#FFFFFF` (white), used for logo/tags/metrics text, which creates poor contrast against the light gray background. |
| **Typography** | `Inter` is appropriate for neumorphism. Not explicitly loaded by B-side. |
| **Border Radius** | `8px` on cards. Neumorphism typically uses `16px` or higher for that soft, pillowy feel. |
| **Shadows & Depth** | **CRITICAL FAILURE:** Cards use `box-shadow:0 2px 8px rgba(0,0,0,.06)` -- a standard drop shadow. Neumorphism's defining characteristic is the dual-shadow system: a light shadow (white/light offset top-left) paired with a dark shadow (darker offset bottom-right), both on the same `#E0E5EC` background. Zero neumorphic shadows are present. |
| **Layout & Spacing** | Generic template layout. |
| **Visual Effects** | No raised extrusion effect. No inset shadows for pressed/input states. No soft-shadow icon containers. The entire neumorphic visual language is absent. |
| **Content & Voice** | Identical boilerplate copy. No reference to soft UI, extrusion, or tactile feel. |
| **Missing Elements** | Dual light+dark shadows (`6px 6px 12px #a3b1c6, -6px -6px 12px #ffffff`); inset shadows for pressed states; same-color background on all elements (cards should match body); no borders (cards have `border:1px solid rgba(0,0,0,.08)` which contradicts neumorphism's borderless doctrine). |
| **CSS Bugs** | White accent text (`#FFFFFF`) on `#E0E5EC` background fails WCAG contrast at 1.16:1 ratio. Tags, metric values, logo, and footer logo are nearly invisible. |

---

## 3. Claymorphism (`claymorphism.html`)

### Style Authenticity Score: 2 / 10

| Criterion | Assessment |
|---|---|
| **Color Palette** | Background `#F0E6FF` is a nice pastel lavender, appropriate for the style. Accent `#D4BBFF` is soft enough. Colors are directionally correct but under-utilized. |
| **Typography** | **WRONG FONT.** B-side uses `Inter` instead of `Nunito`. The A-side correctly loads and uses Nunito with weight 800. Claymorphism's puffy, rounded personality depends heavily on a rounded font like Nunito. Inter is too geometric and sharp. |
| **Border Radius** | `8px` on cards. Claymorphism demands `24px` radius for that inflated, clay-like balloon shape. This is one-third the required radius. |
| **Shadows & Depth** | Standard `0 2px 8px rgba(0,0,0,.06)`. Claymorphism requires a specific multi-shadow formula: inner light highlight (top), inner dark shadow (bottom), plus outer colored shadow. None present. |
| **Layout & Spacing** | Generic template. |
| **Visual Effects** | No inset shadows. No puffy/inflated appearance. No gradient backgrounds on cards. No colored outer glow shadows. The clay-like tactile quality is completely absent. |
| **Content & Voice** | Boilerplate. No playful, squishy, or tactile language. |
| **Missing Elements** | Nunito font; 24px border-radius; multi-layer inset+outer shadows; pastel gradient fills on cards; 2px colored borders; blob/organic decorative shapes; playful tone. |
| **CSS Bugs** | `#D4BBFF` accent on `#F0E6FF` background has low contrast (~1.3:1). Section tags and metric values will be difficult to read. |

---

## 4. Skeuomorphism (`skeuomorphism.html`)

### Style Authenticity Score: 1 / 10

| Criterion | Assessment |
|---|---|
| **Color Palette** | Background `#C0C0C0` is a flat silver-gray. Accent is `#8B8B8B`. The A-side uses rich leather browns, warm wood tones, and metallic gradients. The B-side looks like a 1990s system dialog, not a crafted skeuomorphic interface. |
| **Typography** | Uses `Inter` instead of Georgia (serif) for headings or Roboto for body text. Skeuomorphism traditionally uses serif fonts for headings to evoke print/physical media. |
| **Border Radius** | `8px` on cards. The A-side correctly uses `6px-8px` with beveled edges, but more importantly, skeuomorphism uses small, precise radii with visible borders and inset highlights -- none of which are present. |
| **Shadows & Depth** | Flat `0 2px 8px rgba(0,0,0,.06)`. Skeuomorphism requires multi-layer shadows simulating physical depth: outer drop shadows, inset highlights at top edges, dark inset shadows at bottom edges, embossed text shadows. |
| **Layout & Spacing** | Generic template. |
| **Visual Effects** | **TOTAL ABSENCE:** No texture patterns (leather, wood grain, linen). No multi-stop gradients simulating metallic or glossy surfaces. No beveled button effects. No embossed/debossed text. No inset shadows on input fields. No border treatments simulating physical edges. |
| **Content & Voice** | Boilerplate copy. No references to craftsmanship, materials, or tactile realism. |
| **Missing Elements** | Texture backgrounds (repeating gradients); beveled button gradients with highlight/shadow bands; metallic logo treatment; leather/stitching decorative elements; Georgia or serif headings; text-shadow for embossed effect; realistic input field styling with inset shadow. |
| **CSS Bugs** | `#8B8B8B` accent on `#C0C0C0` has very poor contrast (~1.6:1). Logo, tags, metrics are barely readable. |

---

## 5. Candy UI (`candy-ui.html`)

### Style Authenticity Score: 2 / 10

| Criterion | Assessment |
|---|---|
| **Color Palette** | Background `#FF69B4` (hot pink) is on-brand for candy. Accent `#DDA0DD` (plum) works. The overall pink direction is correct but flat -- candy UI uses multi-color pastels (pink, mint green, lavender, lemon yellow, baby blue). Only two colors are used. |
| **Typography** | **WRONG FONT.** Uses `Inter` instead of `Quicksand`. The A-side correctly loads Quicksand, which has the bubbly, rounded letterforms essential for candy UI. Inter is completely wrong for this playful style. |
| **Border Radius** | `8px` on cards and buttons. Candy UI demands `22px` minimum on cards and `50px` (fully rounded pill shape) on buttons and inputs. The sharp corners destroy the bubbly personality. |
| **Shadows & Depth** | Generic flat shadow. Candy UI requires glossy, multi-layer shadows with colored tints: outer glow in the element's hue, inner highlight (top) for glass-like shine, inner shadow (bottom) for volume. |
| **Layout & Spacing** | Generic template. |
| **Visual Effects** | No glossy/candy-button shine. No drip effects. No floating animation. No inset highlight on buttons. No thick colored borders. No confetti or sprinkle decorations. |
| **Content & Voice** | Boilerplate. No sweet/fun/adorable language. Should use words like "sweet," "tasty," "delightful," "sprinkle." |
| **Missing Elements** | Quicksand font; pill-shaped border-radius (50px); thick 2.5px colored borders on inputs; candy-gloss inset shadows; multi-pastel color scheme; drip or wave decorative edge; floating animation on elements; playful emoji or candy icons. |
| **CSS Bugs** | `#DDA0DD` on `#FF69B4` has moderate contrast (~1.5:1). Nav link color `#666` on `#FF69B4` is borderline. |

---

## 6. Paper Cut (`paper-cut.html`)

### Style Authenticity Score: 2 / 10

| Criterion | Assessment |
|---|---|
| **Color Palette** | Background `#F8E8D4` (warm parchment) is appropriate. Accent `#D4E8F0` (soft blue) is one of the A-side's layer colors. Palette direction is reasonable. |
| **Typography** | **WRONG FONT.** Uses `Inter` instead of `Nunito`. The A-side correctly uses Nunito with its friendly rounded forms that complement the soft paper aesthetic. |
| **Border Radius** | `8px` on cards. The A-side uses `16px` with stacked pseudo-element layers at `20px` and `24px`. Paper cut cards should have generous rounding. |
| **Shadows & Depth** | Single flat shadow `0 2px 8px rgba(0,0,0,.06)`. Paper cut's defining visual is **multiple stacked shadows** creating visible depth layers -- like paper sheets stacked on top of each other. The A-side uses triple-layer shadows (`0 2px 4px, 0 4px 12px, 0 8px 24px`) plus `::before` and `::after` pseudo-elements for additional shadow layers. |
| **Layout & Spacing** | Generic template. |
| **Visual Effects** | **CRITICAL FAILURE:** No layered paper effect. No `::before`/`::after` pseudo-elements creating depth. No overlapping colored shapes at section boundaries. No paper-layer dividers. The entire paper-cut illusion depends on visible stacking of offset layers. |
| **Content & Voice** | Boilerplate. No paper/craft/layer language. |
| **Missing Elements** | Nunito font; multi-layer shadow stacking; `::before`/`::after` offset layers behind cards; overlapping elliptical shapes at hero bottom (the A-side's `.layer` elements); pastel-colored card tags; soft muted pastel palette across multiple hues. |
| **CSS Bugs** | `#D4E8F0` accent on `#F8E8D4` has very poor contrast (~1.15:1). Tags, metric values, and logo text will be nearly invisible against the warm background. |

---

## 7. Marble (`marble.html`)

### Style Authenticity Score: 1 / 10

| Criterion | Assessment |
|---|---|
| **Color Palette** | Background `#F8F9FA` is the correct cool white marble base. But the accent color is `#DEE2E6` (light gray), which is the gray token from the A-side -- **NOT the gold accent** (`#C9A84C`). Gold is THE signature accent of marble/luxury design. Using gray removes all luxury signaling. |
| **Typography** | **WRONG FONT.** Uses `Inter` instead of `Cormorant Garamond`. The A-side prominently loads and uses Cormorant Garamond, a refined serif that conveys classical luxury. Inter is a modern sans-serif that completely destroys the marble aesthetic. |
| **Border Radius** | `8px` on cards. The A-side uses `0px` (sharp rectangular cards) with thin `1px` gray borders. Marble/luxury style demands sharp, architectural edges -- not rounded corners. The B-side is wrong in a different way than most: `8px` is too round for marble, but zero would be correct. |
| **Shadows & Depth** | Generic shadow. The A-side uses minimal shadow (`hover: 0 8px 30px rgba(0,0,0,.06)`), preferring clean edges. Marble style relies on fine lines and gold accents for hierarchy, not shadow depth. |
| **Layout & Spacing** | Generic template. Missing the A-side's elegant gold-line dividers, centered diamond-shaped decorative elements, and 2-column features grid with internal borders. |
| **Visual Effects** | **TOTAL ABSENCE:** No marble texture background (the A-side creates this with multi-layer gradients and repeating fine lines). No gold accent line dividers. No gold border on buttons. No diamond/geometric decorative elements. No uppercase letter-spacing treatment. |
| **Content & Voice** | Boilerplate. No luxury/atelier/stone language. The A-side uses words like "Carved," "Living Stone," "Carrara," "Atelier." |
| **Missing Elements** | Cormorant Garamond serif font; gold (`#C9A84C`) accent throughout; marble texture via layered gradients; gold-line dividers; sharp 0px border-radius; uppercase letter-spacing on nav/labels; thin gold-bordered buttons; veined-divider decorative elements; diamond rotated decorative shapes. |
| **CSS Bugs** | `#DEE2E6` accent on `#F8F9FA` background is essentially invisible (~1.07:1 contrast ratio). Logo, tags, metric values, card icons are all practically invisible. This is the worst contrast failure in the entire batch. |

---

## 8. Terrazzo (`terrazzo.html`)

### Style Authenticity Score: 2 / 10

| Criterion | Assessment |
|---|---|
| **Color Palette** | Background `#E8D5B7` (warm base) is correct. Accent `#E88D97` is a softened rose, loosely related to `--rose: #D4726A`. The warm base direction is right but the multi-color confetti palette (rose, teal, gold, lavender, sage) is reduced to a single pink accent. |
| **Typography** | **WRONG FONT.** Uses `Inter` instead of `Poppins`. The A-side loads Poppins with its geometric-rounded personality that matches terrazzo's playful sophistication. |
| **Border Radius** | `8px` on cards. The A-side uses `16px` with a more generous, playful feel. Terrazzo cards also use `backdrop-filter:blur(4px)` with semi-transparent white backgrounds. |
| **Shadows & Depth** | Generic shadow. Acceptable minimalism for terrazzo (the A-side also keeps shadows subtle), but missing the card's semi-transparent background treatment. |
| **Layout & Spacing** | Generic template. |
| **Visual Effects** | **CRITICAL FAILURE:** No terrazzo speckle pattern. The A-side creates this with a `::before` pseudo-element containing 14+ radial-gradient circles in different colors and sizes. This is THE defining visual of terrazzo. No colored chip elements. No round badge/chips on cards. |
| **Content & Voice** | Boilerplate. No material/surface/speckle language. |
| **Missing Elements** | Poppins font; terrazzo confetti `::before` pseudo-element background; multi-color accent system (rose, teal, gold, lavender, sage); colored chip badges on cards; round swatch shapes; semi-transparent white card backgrounds with blur. |
| **CSS Bugs** | No severe contrast issues (pink on tan is readable), but the single-accent approach fails to represent terrazzo's defining multi-color characteristic. |

---

## 9. Origami (`origami.html`)

### Style Authenticity Score: 1 / 10

| Criterion | Assessment |
|---|---|
| **Color Palette** | Background `#F5F0E8` (warm paper) is correct. But accent `#E8E0D5` is the fold color -- an extremely light warm gray that has almost no contrast against the background. The A-side uses `#C67A4A` (warm terracotta/burnt orange) as the accent, providing a strong warm contrast point. |
| **Typography** | **WRONG FONT.** Uses `Inter` instead of `Nunito`. The A-side loads Nunito which complements the soft, approachable paper aesthetic. |
| **Border Radius** | `8px` on cards. The A-side cards have `0px` border-radius -- origami uses sharp, geometric, angular forms. Paper does not have rounded corners; it has crisp folds and creases. `8px` is doubly wrong here. |
| **Shadows & Depth** | Generic shadow. The A-side uses subtle directional shadows (`2px 2px 8px rgba(0,0,0,.06)`) suggesting a light source, plus fold-corner pseudo-elements. |
| **Layout & Spacing** | Generic template. Missing diagonal crease dividers and fold effects. |
| **Visual Effects** | **TOTAL ABSENCE:** No fold-corner effects (`::before`/`::after` border-trick triangles). No diagonal gradient split (`linear-gradient(135deg, var(--paper) 50%, var(--fold) 50%)`). No crease-line dividers. No shadow-tab on buttons (`::before` bottom-left shadow triangle). The entire origami vocabulary is missing. |
| **Content & Voice** | Boilerplate. No fold/crease/paper language. |
| **Missing Elements** | Nunito font; sharp 0px border-radius; fold-corner triangles via CSS border trick on cards and hero; diagonal gradient background on hero; crease-line dividers; directional shadows; warm accent color (#C67A4A); numbered cards (01, 02, 03); shadow-tab on CTA button. |
| **CSS Bugs** | `#E8E0D5` accent on `#F5F0E8` background has ~1.04:1 contrast ratio. **This is effectively invisible.** Logo, tags, metric values, card icons, button backgrounds, and footer logo are all the same color as the page. The B-side is essentially monochrome with no readable accent. |

---

## 10. Tactile UI (`tactile-ui.html`)

### Style Authenticity Score: 2 / 10

| Criterion | Assessment |
|---|---|
| **Color Palette** | Background `#FF6B9D` (bright pink) does not match the A-side's `#F0E6FF` (soft lavender). The A-side is a gentle purple-lavender, not hot pink. Accent `#C084FC` (purple) is loosely related to the A-side's `#7C3AED` but lighter. The bright pink background is jarring and does not convey "tactile" or "touchable." |
| **Typography** | **WRONG FONT.** Uses `Inter` instead of `Nunito`. The A-side uses Nunito at weights 800-900 for a chunky, squeezable personality. |
| **Border Radius** | `8px` on cards. The A-side uses `24px` on cards and `18px` on buttons/inputs for that puffy, rubber-like feel. |
| **Shadows & Depth** | Generic shadow. The A-side's defining shadow technique is the **solid offset shadow** (`box-shadow: 0 8px 0 #E0D0FF`) creating a 3D extruded/pressed appearance -- like buttons physically elevate off the surface. This is completely absent. |
| **Layout & Spacing** | Generic template. |
| **Visual Effects** | **CRITICAL FAILURE:** No squish/jelly/bounce animations. No solid-offset "platform" shadows. No spring-physics CSS transitions (`cubic-bezier(0.34, 1.56, 0.64, 1)`). No blob-float organic shapes. No squash-and-stretch hover effects. No thick input borders with platform shadows. |
| **Content & Voice** | Boilerplate. No tactile/squishy/bouncy language. The A-side uses "Squishy," "Press Me!", "Squish the Swatches." |
| **Missing Elements** | Nunito font; 24px border-radius; solid-offset platform shadows (`0 8px 0 color`); spring-physics transitions; squash-stretch hover transforms (`scale(1.08, 0.94)`); blob floating animations; chunky 3px borders; active-press shadow reduction with translateY; purple (#7C3AED) primary accent. |
| **CSS Bugs** | The description says "cork/fabric textures, dashed stitch borders" but the A-side is actually a springy/rubbery/squishy style, not a cork/stitching style. The B-side description in the audit prompt may not match the actual implementation. Regardless, neither interpretation is present. `#C084FC` on `#FF6B9D` has moderate contrast (~1.7:1). |

---

## Cross-Cutting Issues (All 10 Files)

### 1. Identical Template Problem
Every B-side shares the exact same:
- HTML structure: `bh` header, `bhero` hero, `bsec` sections, `bgrid` card grid, `bmets` metrics, `bquote` quote, `bfoot` footer
- CSS class names and selectors
- Copy text (headlines, descriptions, card content, quote, metrics labels)
- Layout behavior and spacing values
- Hover effects (`translateY(-3px)` on cards)
- Border radius (`8px` everywhere)
- Shadow formula (`0 2px 8px rgba(0,0,0,.06)`)

### 2. Font Loading Failure
All B-sides declare `font-family:Inter,system-ui,sans-serif` but none import Inter via Google Fonts themselves. They rely on the A-side's font import being in the same document. This works because the `<link>` tag loads globally, but it means the B-side has no independent font control and cannot use the correct style-specific font.

### 3. Contrast Failures (WCAG)
The accent color is often chosen from a light tone in the A-side palette, resulting in near-invisible text:
- **Marble:** `#DEE2E6` on `#F8F9FA` = ~1.07:1 (invisible)
- **Origami:** `#E8E0D5` on `#F5F0E8` = ~1.04:1 (invisible)
- **Paper Cut:** `#D4E8F0` on `#F8E8D4` = ~1.15:1 (invisible)
- **Neumorphism:** `#FFFFFF` on `#E0E5EC` = ~1.16:1 (invisible)
- **Claymorphism:** `#D4BBFF` on `#F0E6FF` = ~1.3:1 (barely visible)
- **Skeuomorphism:** `#8B8B8B` on `#C0C0C0` = ~1.6:1 (unreadable)

Six of ten B-sides have accent text that is essentially unreadable. This is a systematic failure in the accent-color selection logic.

### 4. No Style-Specific CSS Properties
The following CSS properties, which are essential to various styles in this batch, appear zero times across all B-sides:
- `backdrop-filter` (glassmorphism)
- `inset` shadow variants for neumorphism/claymorphism
- Multi-stop `linear-gradient` for skeuomorphism textures
- `::before` / `::after` pseudo-elements for paper-cut layers, origami folds, terrazzo specks
- CSS animations / `@keyframes` for tactile/candy bounce effects
- `border-width` greater than `1.5px`
- `border-radius` greater than `8px`

---

## Recommendations

1. **Each B-side needs a unique CSS implementation** that recreates the A-side's visual vocabulary in the B-side's landing-page structure. The current approach of color-swapping a generic template produces pages that all look the same.

2. **Load the correct font** for each style in the B-side scope (Nunito for claymorphism/paper-cut/origami/tactile, Quicksand for candy, Cormorant Garamond for marble, Poppins for terrazzo).

3. **Apply style-defining CSS properties** to the B-side cards, buttons, hero, and sections:
   - Glassmorphism: `backdrop-filter:blur(20px)` + `rgba` backgrounds
   - Neumorphism: dual `box-shadow` (light + dark offsets), no borders
   - Claymorphism: inset + outer shadows, 24px radius, pastel gradients
   - Skeuomorphism: texture gradients, beveled buttons, serif font
   - Candy: pill shapes, glossy insets, thick borders, bouncy radius
   - Paper Cut: stacked multi-layer shadows, pseudo-element layers
   - Marble: gold accents, sharp edges, Cormorant Garamond, marble texture
   - Terrazzo: confetti radial-gradient pseudo-element, multi-color chips
   - Origami: fold-corner triangles, diagonal gradients, crease lines
   - Tactile: solid-offset shadows, spring transitions, squish animations

4. **Fix contrast ratios** by selecting accent colors with at least 4.5:1 ratio against the background, or by using the accent on darker/lighter elements where contrast is achievable.

5. **Write unique copy** for each B-side that reflects the style's personality and material language.

---

## Score Summary

| # | Style | Score | Primary Failure |
|---|---|---|---|
| 1 | Glassmorphism | 2/10 | No backdrop-filter, no translucent panels |
| 2 | Neumorphism | 2/10 | No dual shadows, borders contradict style |
| 3 | Claymorphism | 2/10 | Wrong font, no inset shadows, flat radius |
| 4 | Skeuomorphism | 1/10 | No textures, no gradients, no realism |
| 5 | Candy UI | 2/10 | Wrong font, no pill shapes, no gloss |
| 6 | Paper Cut | 2/10 | No layered shadows, no pseudo-elements |
| 7 | Marble | 1/10 | No gold accent, wrong font, invisible text |
| 8 | Terrazzo | 2/10 | No confetti pattern, wrong font |
| 9 | Origami | 1/10 | No fold corners, invisible accent, wrong font |
| 10 | Tactile UI | 2/10 | No platform shadows, no spring physics |

**Average: 1.7 / 10**

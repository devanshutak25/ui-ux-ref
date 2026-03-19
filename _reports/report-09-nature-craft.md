# Report 09 -- Nature, Craft & Specialty Styles: B-Side Audit

**Auditor:** UI Designer Agent
**Date:** 2026-03-20
**Scope:** B-side implementations of 10 sample pages evaluated for style authenticity

---

## Executive Summary

All 10 B-side implementations share an identical boilerplate template structure. The template swaps only the background color and a single accent color per style. None of the B-sides authentically embody their respective design styles. They all use the same `Inter` / `system-ui` font stack, the same `8px` border-radius cards, the same layout grid, the same generic copy, and the same interaction patterns. The A-sides, by contrast, are rich and distinctive implementations. The B-sides are effectively a single "tech startup landing page" template with a color wash applied.

**Average Authenticity Score: 1.8 / 10**

---

## 1. Organic Biophilic (`organic-biophilic.html`)

**Style Authenticity Score: 2 / 10**

| Criterion | Assessment |
|---|---|
| **Color Palette** | Background is `#2D5016` (deep forest green) with `#8B4513` (saddle brown) accent. The green-and-brown combination is on-theme, but the implementation is a flat dark-mode slab with no warmth, no cream/sand tones, and no layered earthy palette. Missing the warm `#F4E9D8` beige that defines the A-side. |
| **Typography** | Uses `Inter, system-ui, sans-serif`. Should use a rounded humanist sans like `Nunito` or at minimum `DM Sans` (as the A-side does) paired with a serif like `DM Serif Display`. The clean geometric Inter contradicts the organic nature. Font weight 800 on the hero heading feels industrial, not biophilic. |
| **Border Radius** | Cards use `border-radius: 8px` -- a standard tech radius. Organic biophilic demands asymmetric organic blob radii (e.g. `40% 60% 55% 45% / 55% 45% 55% 45%`) as the A-side demonstrates. The 8px radius reads as generic SaaS. |
| **Shadows & Depth** | Standard `box-shadow: 0 2px 8px rgba(0,0,0,.15)` on cards. Missing soft, diffuse nature-like shadows. No layered depth suggesting leaves or foliage canopy. |
| **Layout & Spacing** | Standard centered hero + 3-column grid + metrics + quote + footer. Biophilic design should feature flowing, non-rigid layouts with organic negative space. The rigid grid contradicts the style. |
| **Visual Effects** | Zero signature elements. Missing: organic blob shapes, leaf/vine decorations, root-line patterns, organic CTA border-radius morphing, translucent overlapping nature forms. The A-side has all of these. |
| **Content & Voice** | Completely generic. "Distinctive by design", "What Sets Us Apart", "Numbers Speak" -- no nature vocabulary. Should reference roots, growth, canopy, greenhouse, living systems. |
| **Missing Elements** | Organic blob backgrounds, leaf icons, vine decorations, CSS-drawn plant forms, warm cream/sand background tones, linen-like texture, asymmetric border radii. |
| **CSS Bugs** | Logo text `Soviet Constructivis` is truncated in a different file but no CSS bugs specific to this file. The `.bh .logo` color `#8B4513` on `#2D5016` background may have contrast issues (brown on dark green). |

---

## 2. Solarpunk (`solarpunk.html`)

**Style Authenticity Score: 2 / 10**

| Criterion | Assessment |
|---|---|
| **Color Palette** | Background `#2D5016` (same dark forest green as organic biophilic!) with `#F0C808` gold accent. The gold is a reasonable solarpunk accent but the dark green background does not convey the warm, utopian, sun-drenched cream (`#F7F3E3`) that defines solarpunk. Missing sky blue entirely. |
| **Typography** | Uses `Inter` instead of the specified `Nunito`. Solarpunk demands a friendly, rounded, warm sans-serif. Inter is cold and geometric. The A-side correctly loads Nunito at weight 800. |
| **Border Radius** | `8px` standard radius. Solarpunk should use generously rounded `50px` pill shapes (as the A-side does) to convey friendliness and organic technology. |
| **Shadows & Depth** | Minimal dark-mode shadows. Should have warm, colorful shadows with green/gold tints suggesting dappled sunlight. |
| **Layout & Spacing** | Identical boilerplate layout. Missing the nature-tech fusion aesthetic -- no gradient skies, no sun rays, no vine elements, no leaf decorations. |
| **Visual Effects** | Zero signature elements. Missing: animated sun rays, leaf decorations, vine borders, gradient sky backgrounds, cooperative/community iconography, nature-tech hybrid ornamentation. |
| **Content & Voice** | Generic corporate copy. Should reference collective action, community gardens, sustainable futures, renewable energy, cooperative ownership -- the utopian solarpunk vocabulary. |
| **Missing Elements** | Sun animation, leaf shapes, sky-to-earth gradient, vine lines, community iconography, warm cream background, green-to-gold gradients on buttons. |
| **CSS Bugs** | Background is identical to organic-biophilic B-side (`#2D5016`), making these two styles visually indistinguishable in B-side view. This is a critical differentiation failure. |

---

## 3. Wabi-Sabi (`wabi-sabi.html`)

**Style Authenticity Score: 2 / 10**

| Criterion | Assessment |
|---|---|
| **Color Palette** | Background `#8B7355` (medium brown) with `#6B7B3B` (olive green) accent. The brown is close to the earthy tone family but applied as a flat slab rather than a textured, weathered surface. Missing the essential quiet `#F5F0E8` warm paper background and `#C4B5A0` patina tones. |
| **Typography** | Uses `Inter` instead of `Noto Serif JP`. This is perhaps the most egregious font mismatch in this batch -- wabi-sabi is fundamentally a Japanese aesthetic and `Noto Serif JP` carries essential cultural weight. The A-side uses it at weight 300 (light), creating the delicate, contemplative feel. Inter at weight 800 is the opposite of wabi-sabi. |
| **Border Radius** | `8px` standard radius. Wabi-sabi should use barely-there radius (`2px`) or none at all, reflecting imperfection and naturalness. The A-side uses minimal radii throughout. |
| **Shadows & Depth** | Standard card shadows. Wabi-sabi should have almost no shadows -- just subtle single-pixel borders or hairline rules. The aesthetic is about flatness, space, and restraint. |
| **Layout & Spacing** | Standard symmetric grid. Wabi-sabi demands intentional asymmetry, generous negative space (the A-side hero has 6rem top margin and 8% left offset), and breathing room between elements. The B-side is densely packed by comparison. |
| **Visual Effects** | Zero signature elements. Missing: enso circle, texture strips (the A-side has a beautiful `repeating-linear-gradient` reed/woven texture), asymmetric card accent bars, hairline dividers. |
| **Content & Voice** | Generic copy. Should reference imperfection, impermanence, kintsugi, moss, weathering, patina, contemplation, tea ceremony -- the core wabi-sabi vocabulary. The B-side header says "Japanese Minimalism" rather than "Wabi-Sabi", which is at least on-theme but loses the specific concept. |
| **Missing Elements** | Enso circle, texture strip, asymmetric layout, generous whitespace, light font weights, hairline borders, muted earth tones, contemplative pacing. |
| **CSS Bugs** | No functional bugs, but the `#8B7355` background with `#aaa` text color for paragraphs likely fails WCAG AA contrast (gray on brown). |

---

## 4. Watercolor UI (`watercolor-ui.html`)

**Style Authenticity Score: 2 / 10**

| Criterion | Assessment |
|---|---|
| **Color Palette** | Background `#E8D5B7` (warm beige) with `#A7C7E7` (soft blue) accent. The beige is reasonable as a paper tone and the blue references the watercolor wash, but the implementation is flat -- no soft washes, no bleeding edges, no layered translucency. Missing lavender `#C5B3E6` entirely. |
| **Typography** | Uses `Inter` instead of `Cormorant Garamond`. Watercolor UI demands an elegant, painterly serif. Cormorant Garamond at various weights creates the artistic, gallery-like atmosphere. Inter is clinical and contradicts the painted aesthetic. |
| **Border Radius** | `8px` standard radius. Should use large soft radii (`20px+`) or organic shapes suggesting water pooling. The A-side uses `border-radius: 20px` on cards and `30px` pill buttons. |
| **Shadows & Depth** | Standard card shadows. Should use no hard shadows -- only diffuse, blurred, colored glows suggesting watercolor pigment bleeding. The A-side uses `backdrop-filter: blur(8px)` and `filter: blur(20px)` extensively. |
| **Layout & Spacing** | Standard grid layout. Watercolor UI should feel flowing and gallery-like, with generous padding and organic card placement. |
| **Visual Effects** | Zero signature elements. Missing: blurred radial gradient washes (`filter: blur(40px)`), backdrop-filter glass effects, soft color blob backgrounds on cards, translucent overlapping color forms. The A-side hero has a triple radial gradient with 40px blur -- this is the defining watercolor technique. |
| **Content & Voice** | Generic copy. Should reference washes, pigment, bleeding edges, canvas, palette, studio -- the watercolor painting vocabulary. |
| **Missing Elements** | Blurred gradient washes, backdrop-filter effects, soft color blobs, translucent card backgrounds, organic radial gradients, painterly atmosphere. |
| **CSS Bugs** | The `.bh` lacks `backdrop-filter: blur(12px)` unlike other B-sides (which have it on their dark-bg variants). Minor inconsistency. |

---

## 5. Embroidery (`embroidery.html`)

**Style Authenticity Score: 2 / 10**

| Criterion | Assessment |
|---|---|
| **Color Palette** | Background `#F5E6D3` (linen fabric tone -- correct!) with `#CC4444` (red thread) accent. The background color is the one correct element in this B-side. But the palette is reduced to just red + gray rather than the full red/blue/green thread system. |
| **Typography** | Uses `Inter` instead of `Lora` serif. Embroidery/cross-stitch should use a serif that echoes traditional sampler lettering. Lora has the slight formality that works for this craft aesthetic. |
| **Border Radius** | `8px` standard radius. Embroidery should use `0px` radius -- cross-stitch is fundamentally grid-based and rectilinear. The A-side uses zero radius on cards and swatches, relying on dashed borders instead. |
| **Shadows & Depth** | Standard subtle shadows. Embroidery should have zero shadows -- stitchwork is flat by nature. The A-side achieves depth through layered borders and pattern, not shadows. |
| **Layout & Spacing** | Standard grid. Should feel grid-based and structured, reflecting the cross-stitch grid (12px repeat in the A-side). |
| **Visual Effects** | Zero signature elements. Missing: the defining dashed stitch borders (`border: 3px dashed`), cross-stitch grid background pattern (`repeating-linear-gradient` creating a 12px linen grid), X-mark decorations (`\2716` cross symbols), thread-colored section dividers. The A-side's entire identity is built on dashed borders and the grid texture -- none of this carries to the B-side. |
| **Content & Voice** | Generic copy. Should reference stitches, threads, patterns, samplers, hoops, needlework -- the craft vocabulary. |
| **Missing Elements** | Dashed stitch borders, linen grid background texture, cross-stitch symbols, colored thread accents (blue `#4477AA`, green `#44AA44`), zero border-radius, flat presentation without shadows. |
| **CSS Bugs** | No functional bugs. |

---

## 6. Woodcut (`woodcut.html`)

**Style Authenticity Score: 2 / 10**

| Criterion | Assessment |
|---|---|
| **Color Palette** | Background `#1A1A1A` (near-black) with `#F5F0E8` (cream) accent. This inverts the woodcut palette -- woodcut is cream background with black ink, not black background with cream text. The A-side correctly uses `--cream: #F5F0E8` as the body background with `--black: #1A1A1A` for ink. The inversion fundamentally misrepresents the style (woodcuts print dark ink on light paper). |
| **Typography** | Uses `Inter` instead of `Playfair Display`. Woodcut demands a high-contrast serif with thick/thin stroke variation that evokes carved letterforms. Playfair Display at weight 900 with uppercase + letter-spacing creates the printmaking atmosphere. Inter is antithetical. |
| **Border Radius** | `8px` standard radius. Woodcut demands `0px` radius -- absolutely zero roundness. Printmaking is angular, carved, deliberate. The A-side uses zero radius on every single element. |
| **Shadows & Depth** | Standard card shadows with `rgba(0,0,0,.15)`. Woodcut should have zero shadows. The visual depth comes from crosshatching patterns, thick rule lines, and stark black/white contrast -- never from drop shadows. |
| **Layout & Spacing** | Standard grid. Woodcut should use thick rule dividers (3px+ solid borders), grid-based card layouts with visible borders, and a clear editorial structure. The A-side has `border: 3px solid var(--black)` on almost every element. |
| **Visual Effects** | Zero signature elements. Missing: crosshatch patterns (`repeating-linear-gradient(45deg, ...)`), woodblock texture strips (the A-side has a brilliant multi-section woodblock demo with hatching, cross-hatching, and dot patterns), thick solid rule lines, high-contrast black/cream only palette. |
| **Content & Voice** | Generic copy. Should reference carving, ink, press, gouge marks, block printing, relief -- the printmaking vocabulary. |
| **Missing Elements** | Crosshatch patterns, thick 3px+ borders, woodblock texture strips, zero border-radius, cream-on-dark-is-wrong (should be dark-on-cream), Playfair Display serif, uppercase text treatment, editorial rule structure. |
| **CSS Bugs** | The inverted palette (dark bg instead of light) is technically not a CSS bug but a design error that misrepresents the woodcut medium. |

---

## 7. Risograph (`risograph.html`)

**Style Authenticity Score: 2 / 10**

| Criterion | Assessment |
|---|---|
| **Color Palette** | Background `#FF6B6B` (bright coral/salmon) with `#4169E1` (royal blue) accent. While coral + blue is in the risograph family, the implementation is wrong: the background should be the paper tone (`#f5f0e8` uncoated stock) with coral and blue as the two ink colors printed on top. A solid coral background looks like a flat UI theme, not a riso print. |
| **Typography** | Uses `Inter` instead of `Space Grotesk`. Space Grotesk has the slightly quirky, independent-press character that suits risograph aesthetics. |
| **Border Radius** | `8px` standard radius. Risograph should use `0px` radius -- riso prints are angular, with hard registration edges. The A-side uses zero radius on all elements. |
| **Shadows & Depth** | Standard card shadows. Risograph should use zero conventional shadows. Instead, depth comes from `mix-blend-mode: multiply` overlapping layers and misregistration offsets (shifted pseudo-elements). |
| **Layout & Spacing** | Standard grid. Risograph should feel like a printed page with ink borders and limited registration precision. |
| **Visual Effects** | Zero signature elements. This is the most technique-heavy style and the B-side captures none of it. Missing: `mix-blend-mode: multiply` overprint effects, halftone dot patterns (`radial-gradient` at small `background-size`), misregistration offsets (shifted `::after` pseudo-elements), paper grain texture (SVG noise filter), two-color-only ink limitation, overlap color (#2a1848). |
| **Content & Voice** | Generic copy. Should reference ink layers, overprint, registration, soy-based inks, print runs, duotone -- the riso printing vocabulary. |
| **Missing Elements** | Multiply blend mode, halftone dots, misregistration offsets, paper texture, two-ink limitation, overlap/overprint color mixing, angular zero-radius elements. |
| **CSS Bugs** | `#666` text on `#FF6B6B` background likely fails WCAG contrast requirements. |

---

## 8. Constructivism (`constructivism.html`)

**Style Authenticity Score: 2 / 10**

| Criterion | Assessment |
|---|---|
| **Color Palette** | Background `#CC0000` (red) with `#000000` (black) accent and `#fff` text. The red background is on-theme for Soviet constructivism. However, the A-side uses aged cream (`#F5E6CC`) as the primary background with red and black as accent/structural elements -- matching actual propaganda poster design where red is a highlight, not the ground. |
| **Typography** | Uses `Inter` instead of `Oswald` / `Roboto Condensed`. Constructivism demands a condensed, bold, all-uppercase sans-serif evoking Soviet typography. Oswald at weight 700 with 2-4px letter-spacing and `text-transform: uppercase` creates the propaganda poster feel. Inter is neutral and apolitical. |
| **Border Radius** | `8px` standard radius. Constructivism demands `0px` radius -- absolute geometric precision. Soviet design is angular, sharp, ideological. The A-side uses zero radius everywhere with thick 3px solid borders. |
| **Shadows & Depth** | Standard card shadows. Constructivism should have zero drop shadows. Depth comes from geometric overlapping shapes (diagonal bars, circles, triangles) and thick borders. The A-side has a dramatic diagonal red bar, geometric circle, and triangle as compositional elements. |
| **Layout & Spacing** | Standard centered symmetric grid. Constructivism demands diagonal composition, asymmetric placement, and dynamic tension. The A-side has a 15-degree rotated diagonal bar cutting across the hero. |
| **Visual Effects** | Zero signature elements. Missing: diagonal composition bars (`transform: rotate(-15deg)`), geometric shapes (circle, triangle), repeating diagonal stripe dividers (`repeating-linear-gradient(-45deg, ...)`), red left-bar accents on cards, propaganda-style tag labels, thick-border input fields. |
| **Content & Voice** | Generic copy. Should reference collective, masses, manifesto, directive, production quotas, forward -- the Soviet propaganda vocabulary. |
| **Missing Elements** | Diagonal composition, geometric shapes, striped dividers, red accent bars, condensed uppercase typography, propaganda voice, zero radius, thick borders, aged paper texture. |
| **CSS Bugs** | The logo and header text read "Soviet Constructivis" (truncated, missing the "m"). This string appears in three places in the HTML. This is a content/generation bug. Also, `#aaa` text on `#CC0000` background likely fails WCAG contrast. |

---

## 9. Pharmaceutical (`pharmaceutical.html`)

**Style Authenticity Score: 3 / 10**

| Criterion | Assessment |
|---|---|
| **Color Palette** | Background `#F0FDFA` (minty white) with `#0D9488` (teal) accent. The `#F0FDFA` background is exactly the specified minty white -- this is the most accurate color choice among all 10 B-sides. The teal `#0D9488` is a reasonable clinical accent. However, the A-side uses a blue system (`#0066CC`) rather than teal, and the specification calls for "deep teal" which `#0D9488` approximates. |
| **Typography** | Uses `Inter` -- which is actually reasonable for pharmaceutical/clinical design. The A-side also uses Inter. This is the one case where the default font choice happens to work. |
| **Border Radius** | `8px` standard radius on cards. Pharmaceutical should use pill-shaped buttons (`border-radius: 24px-28px`) as the A-side does, with softer `12px` card radius. The `8px` is close but the buttons lack the signature pill shape. |
| **Shadows & Depth** | Standard card shadows. Pharmaceutical should have very minimal, clinical shadows -- the A-side uses `box-shadow: 0 4px 16px rgba(0,102,204,.3)` only on hover. |
| **Layout & Spacing** | Standard grid. Close enough to clinical precision, though the A-side has a more restrained, centered layout with smaller max-widths. |
| **Visual Effects** | Missing signature elements: blister pack grid (the A-side has a clever CSS blister-cell grid), pill-shaped buttons with full `border-radius: 28px`, dosage badges, clinical card-dot indicators, blue-tinted gradient background. |
| **Content & Voice** | Generic copy. Should reference clinical trials, monographs, dosage, formulations, patient safety -- the pharmaceutical vocabulary. |
| **Missing Elements** | Pill-shaped buttons, blister pack grid, dosage badges, clinical gradient hero, blue-tinted light background (`#E8F2FF`), sterile/clean atmosphere. |
| **CSS Bugs** | No functional CSS bugs. This is the cleanest B-side technically. |

---

## 10. Vibrant Blocks (`vibrant-blocks.html`)

**Style Authenticity Score: 2 / 10**

| Criterion | Assessment |
|---|---|
| **Color Palette** | Background `#FF6B6B` (salmon/coral) with `#4ECDC4` (teal) accent. This is a generic "trendy" palette, not the specified dark bg (`#0D0D0D`) with large blocks of fiery orange/hot pink/navy/green/yellow. The A-side uses a near-black base with `#FF3366` (hot pink), `#FFDD00` (yellow), `#00D4AA` (green), `#4D4DFF` (blue) as distinct block sections. The B-side reduces this to a single salmon wash. |
| **Typography** | Uses `Inter` instead of `Space Grotesk`. Space Grotesk brings the bold, slightly geometric, startup-energy character. But more importantly, the B-side is missing `text-transform: uppercase` and tight letter-spacing that define the bold, shouty typographic voice. |
| **Border Radius** | `8px` standard radius. Vibrant Blocks demands `0px` radius -- the A-side uses zero radius on every element (buttons, cards, inputs, swatches). The sharp edges create the bold, punchy, graphic design feel. |
| **Shadows & Depth** | Standard subtle shadows. Vibrant Blocks should use thick `3px solid #0D0D0D` borders instead of shadows, with offset shadows on focus (`box-shadow: 4px 4px 0 #FF3366`). |
| **Layout & Spacing** | Standard grid. Vibrant Blocks should use large color-block sections as layout containers (nav = yellow block, hero = pink block, metrics strip = teal/blue/yellow blocks). The A-side's block-strip with three colored metric blocks is a signature element. |
| **Visual Effects** | Zero signature elements. Missing: large color block sections, thick solid borders, zero-radius angular elements, uppercase treatment throughout, high-energy offset shadows, color-block metric strips. |
| **Content & Voice** | Generic copy. Should have high-energy startup language: "Bold moves only", "Launch Now", "10x Growth" -- punchy, uppercase, attention-demanding. |
| **Missing Elements** | Dark background with color blocks, zero border-radius, thick borders, block-strip metric sections, uppercase typography, Space Grotesk font, offset/brutalist shadows, high-contrast color blocking. |
| **CSS Bugs** | Background `#FF6B6B` is identical to the risograph B-side, making these two styles indistinguishable. `#666` text on `#FF6B6B` likely fails WCAG contrast. |

---

## Cross-Cutting Issues

### 1. Template Duplication Problem

All 10 B-sides share an identical HTML structure and nearly identical CSS. The only variations are:

| Property | Variation Method |
|---|---|
| `background` on `.b-side` | One color per style |
| Accent color (logo, tags, icons, buttons, metrics) | One color per style |
| Text color (white for dark bg, black for light bg) | Binary toggle |
| Logo/title text | Style name string |

Everything else is identical: layout, spacing, typography, border-radius, shadows, content copy, card structure, section structure, footer structure.

### 2. Duplicate Background Colors

- **`#2D5016`** used for both Organic Biophilic and Solarpunk
- **`#FF6B6B`** used for both Risograph and Vibrant Blocks

This means 4 of the 10 styles are visually indistinguishable in pairs.

### 3. Font Loading Failure

None of the 10 B-sides load their style-appropriate Google Font. All fall back to `Inter, system-ui, sans-serif`. The A-sides correctly load: DM Serif Display + DM Sans, Nunito, Noto Serif JP, Cormorant Garamond, Lora, Playfair Display + Inter, Space Grotesk, Oswald + Roboto Condensed, Inter (pharmaceutical only), Space Grotesk.

### 4. Generic Content

Every B-side uses identical placeholder copy:
- "Distinctive by design"
- "What Sets Us Apart"
- "Visual Identity / Consistent Language / Authentic Detail"
- "Numbers Speak" with "100% Authentic / Unique Voice / Bold Statement"
- Same testimonial quote

This generic content contradicts the craft, nature, and art vocabulary each style demands.

### 5. Missing Signature CSS Techniques

| Style | Signature CSS Technique | Present in B-side? |
|---|---|---|
| Organic Biophilic | Asymmetric `border-radius` blobs | No |
| Solarpunk | `conic-gradient` sun rays, pill `border-radius` | No |
| Wabi-Sabi | Minimal weight, asymmetric layout, enso | No |
| Watercolor | `filter: blur()`, `backdrop-filter`, radial washes | No |
| Embroidery | Dashed borders, grid background pattern | No |
| Woodcut | Crosshatch `repeating-linear-gradient`, thick rules | No |
| Risograph | `mix-blend-mode: multiply`, halftone dots, offset | No |
| Constructivism | Diagonal `transform: rotate`, geometric shapes | No |
| Pharmaceutical | Pill-shaped buttons, blister grid | No |
| Vibrant Blocks | Color block sections, zero radius, thick borders | No |

### 6. Contrast / Accessibility Concerns

Several B-sides have questionable text contrast:
- `#aaa` on `#CC0000` (Constructivism) -- likely fails AA
- `#666` on `#FF6B6B` (Risograph, Vibrant Blocks) -- likely fails AA
- `#aaa` on `#8B7355` (Wabi-Sabi) -- likely fails AA
- `#aaa` on `#2D5016` (Organic Biophilic, Solarpunk) -- likely fails AA

### 7. Content Bug

Constructivism B-side truncates "Soviet Constructivism" to "Soviet Constructivis" in the logo, hero heading, and footer copyright. This appears to be a string truncation bug during generation.

---

## Score Summary

| # | Style | Score | Primary Failure |
|---|---|---|---|
| 1 | Organic Biophilic | 2/10 | No organic shapes, wrong font, no nature atmosphere |
| 2 | Solarpunk | 2/10 | Identical bg to biophilic, no sun/leaf elements, wrong font |
| 3 | Wabi-Sabi | 2/10 | Wrong font (most critical), no asymmetry, no negative space |
| 4 | Watercolor UI | 2/10 | No blur/wash effects, wrong font, no translucency |
| 5 | Embroidery | 2/10 | No dashed borders, no grid texture, wrong font |
| 6 | Woodcut | 2/10 | Inverted palette, no crosshatching, wrong font, has radius |
| 7 | Risograph | 2/10 | No multiply blend, no halftone, no misregistration |
| 8 | Constructivism | 2/10 | No diagonal composition, wrong font, truncated name |
| 9 | Pharmaceutical | 3/10 | Correct bg color and font family; still missing pill shapes |
| 10 | Vibrant Blocks | 2/10 | No color blocks, no dark bg, has border-radius |

**Overall Average: 2.1 / 10**

---

## Recommendations

1. **Each B-side needs a unique CSS implementation** that carries at least 3-5 signature visual elements from the A-side into the B-side layout structure.

2. **Load the correct Google Font** for each B-side and apply appropriate font weights and text treatments (uppercase for constructivism/woodcut/vibrant, light for wabi-sabi/watercolor, etc.).

3. **Fix border-radius per style**: organic shapes for biophilic/solarpunk, zero for woodcut/constructivism/embroidery/risograph/vibrant, pill for pharmaceutical, minimal for wabi-sabi.

4. **Add at least one signature visual effect** per style: blob shapes, blur washes, dashed borders, crosshatch patterns, multiply blends, diagonal bars, etc.

5. **Deduplicate background colors** so no two styles share the same B-side appearance.

6. **Replace generic copy** with style-appropriate vocabulary and voice.

7. **Fix the "Soviet Constructivis" truncation** to read "Constructivism" or "Soviet Constructivism".

8. **Audit contrast ratios** for all B-side text-on-background combinations against WCAG AA (4.5:1).

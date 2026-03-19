# Report 08 -- Thematic & Atmospheric B-Side Audit

**Auditor:** UI Designer Agent
**Date:** 2026-03-20
**Scope:** B-side CSS/HTML authenticity for 10 thematic/atmospheric design style samples
**Verdict:** All 10 B-sides use an identical generic template with only superficial color swaps. None authentically embodies its target style.

---

## Executive Summary

Every B-side across all 10 files shares the same boilerplate HTML structure and CSS framework: a sticky header with logo and nav, an 80vh centered hero with tagline/heading/paragraph/two-buttons, a three-card features grid, a four-metric stats row, a centered blockquote, and a simple footer. The only customization is a mechanical color substitution (background color + one accent color) derived from each style's A-side palette. Typography, layout, spacing, border radius, shadows, visual effects, content voice, and decorative elements are identical across all 10 files. The B-sides uniformly use `Inter, system-ui, sans-serif`, `border-radius: 8px`, and the same generic copy ("Distinctive by design", "A strong, recognizable aesthetic that sets this style apart from all others", etc.).

**Overall Pattern Score: 2/10** -- The template demonstrates competent generic SaaS landing page design but zero style-specific authenticity.

---

## 1. Art Deco (`art-deco.html`)

### Style Authenticity Score: 2/10

| Criterion | Assessment |
|-----------|------------|
| **Color Palette** | Background is `#D4AF37` (gold) with dark text. The A-side uses dark bg with gold accents -- the B-side inverts this entirely, making the whole page gold. This is not Art Deco; it reads as a mustard-colored SaaS page. Correct approach: dark navy `#1A1A2E` background with gold `#D4AF37` accents and geometric patterns. |
| **Typography** | Uses `Inter, system-ui, sans-serif`. Art Deco demands `Playfair Display` (already loaded in the A-side), uppercase display type, high letter-spacing, and geometric serif forms. The B-side has none of this. |
| **Border Radius** | `8px` rounded corners throughout. Art Deco is defined by sharp geometry -- zero border-radius, angular corners, or octagonal clips. Rounded corners are antithetical to this style. |
| **Shadows & Depth** | Generic `box-shadow: 0 2px 8px rgba(0,0,0,.06)`. Art Deco uses flat, graphic depth through layered geometric borders and metallic gradients, not soft modern shadows. |
| **Layout & Spacing** | Standard centered SaaS hero layout. Art Deco demands strict bilateral symmetry, vertical axis emphasis, and tiered geometric compositions. |
| **Visual Effects** | None. Missing: geometric chevron patterns, fan/sunburst motifs, repeating conic gradients, double-line borders with inset borders, gold metallic gradients. The A-side has `repeating-conic-gradient`, `.fan` elements with conic gradients, and `.chevron` pseudo-elements -- the B-side has nothing. |
| **Content & Voice** | Generic tech copy. Should reference "the golden age", use period-appropriate language ("Collection", "Atelier"), uppercase headings. |
| **Missing Elements** | Gold geometric patterns, fan/sunburst decorations, chevron dividers, double-line ornate borders, symmetrical axis composition, uppercase headings, Playfair Display font. |
| **CSS Bugs** | `.bh nav a:hover{color:#1A1A2E}` -- dark navy hover on gold background creates low contrast but is functionally acceptable. No syntax errors. |

---

## 2. Film Noir (`film-noir.html`)

### Style Authenticity Score: 2/10

| Criterion | Assessment |
|-----------|------------|
| **Color Palette** | Background `#000000` with white text and white accent -- technically dark, but missing the critical single blood-red `#CC0000` accent. The B-side accent colors are all `#FFFFFF`, losing the signature noir red completely. |
| **Typography** | Uses `Inter, system-ui, sans-serif`. Film Noir demands `Playfair Display` serif (loaded in A-side) with italic emphasis, thin sans-serif body (`Source Sans 3` at weight 300). The B-side uses chunky 800-weight sans-serif headings -- the opposite of noir's elegant thinness. |
| **Border Radius** | `8px` rounded corners. Film noir demands zero border-radius -- hard rectangular edges like shadow-cut geometry. |
| **Shadows & Depth** | Generic card shadows. Missing: venetian blind shadow strips (`repeating-linear-gradient`), spotlight radial gradients, chiaroscuro light/dark contrast. The A-side has `.blinds-overlay` and `.spotlight` -- the B-side has nothing. |
| **Layout & Spacing** | Standard centered layout. Film noir should use asymmetric compositions, off-center elements, dramatic negative space. |
| **Visual Effects** | None present. Missing: venetian blind stripe overlay, spotlight effect, film grain texture, red accent line dividers, high-contrast chiaroscuro. |
| **Content & Voice** | Generic "Distinctive by design" copy. Should use noir narrative voice: "The city never sleeps", detective/crime metaphors, chapter numbering, italic emphasis on key words. |
| **Missing Elements** | Venetian blind shadows, spotlight effects, blood-red accent color, Playfair Display serif, thin font weights, asymmetric layout, noir narrative voice, film grain overlay. |
| **CSS Bugs** | No syntax errors. |

---

## 3. Cinematic (`cinematic.html`)

### Style Authenticity Score: 1/10

| Criterion | Assessment |
|-----------|------------|
| **Color Palette** | Background `#000000` with `#1A1A1A` as accent. The accent color is nearly black-on-black, making the B-side logo (`.bh .logo{color:#1A1A1A}`), tagline (`.bhero-tag{color:#1A1A1A}`), section labels (`.bst{color:#1A1A1A}`), metric values (`.bmet-v{color:#1A1A1A}`), and footer logo all essentially invisible against the black background. This is a **critical visibility bug**. |
| **Typography** | Uses `Inter, system-ui, sans-serif`. Cinematic demands `Playfair Display` serif for dramatic headings and `Inter` for body at weight 300. The B-side uses weight 800 sans-serif headings -- opposite of the elegant, thin cinematic look. |
| **Border Radius** | `8px` rounded corners. Cinematic style uses sharp, rectangular forms -- zero radius for dramatic, filmic geometry. |
| **Shadows & Depth** | Generic card shadows. Missing: dramatic chiaroscuro gradients, film grain overlay, venetian blind patterns, red accent line `::before` on cards. |
| **Layout & Spacing** | Standard centered SaaS layout. Cinematic demands wide-format compositions (widescreen aspect ratios), dramatic spacing, asymmetric arrangements. |
| **Visual Effects** | None. Missing: film grain noise texture (the A-side has an SVG turbulence `body::after`), venetian blind `repeating-linear-gradient`, spotlight `radial-gradient`, red accent gradients on cards. |
| **Content & Voice** | Generic copy. Should reference cinematic language: "Act", "Scene", "The Reckoning", atmospheric noir prose. |
| **Missing Elements** | Film grain texture, venetian blind overlay, spotlight radial gradient, crimson `#c41e3a` accent color, dramatic serif typography, cinematic content voice, widescreen composition feel. |
| **CSS Bugs** | **CRITICAL:** Accent color `#1A1A1A` on `#000000` background creates near-invisible text for logo, tags, section labels, metric values, and footer elements. Contrast ratio is approximately 1.1:1, far below any readability threshold. |

---

## 4. Astrological (`astrological.html`)

### Style Authenticity Score: 3/10

| Criterion | Assessment |
|-----------|------------|
| **Color Palette** | Background `#0A0A2A` (midnight) with `#FFD700` (gold) accent. This is the closest of all 10 to being correct -- the dark midnight blue with gold is thematically appropriate for celestial/astrological. However, using pure gold `#FFD700` instead of the A-side's more muted `#D4A847` creates a harsher, less mystical feel. |
| **Typography** | Uses `Inter, system-ui, sans-serif`. Astrological demands `Cinzel` serif or `Cormorant Garamond` (both loaded in A-side) -- elegant, thin serifs that evoke classical astrology texts. Weight 800 sans-serif headings feel tech-corporate, not celestial. |
| **Border Radius** | `8px` rounded corners. The A-side uses `border-radius: 24px` for pill-shaped buttons and `16px` for cards, plus `50%` circles for swatches -- celestial/orbital rounded forms. The B-side's generic 8px is neither sharp nor celestially round. |
| **Shadows & Depth** | Generic card shadows. Missing: glowing gold `box-shadow` effects (`0 0 40px` glow), celestial ambient light, the A-side's `0 0 20px var(--gold)` sun glow and `0 0 30px var(--dim)` hover effects. |
| **Layout & Spacing** | Standard centered layout. Astrological should have central-axis symmetry with radial composition hints, constellation dot patterns, zodiac ring elements. |
| **Visual Effects** | None. Missing: starfield background (`radial-gradient` dots), zodiac ring animation (`@keyframes spin`), constellation dot patterns, gold glow effects, dashed orbital borders. The A-side has an animated zodiac ring, starfield, and constellation dots -- the B-side has zero celestial decoration. |
| **Content & Voice** | Generic copy. Should reference celestial concepts: "Mercury in Retrograde", zodiac houses, star charts, cosmic language. |
| **Missing Elements** | Starfield background, animated zodiac ring, constellation dot patterns, gold glow shadows, orbital/circular shapes, Cinzel/Cormorant serif fonts, celestial content. |
| **CSS Bugs** | No syntax errors. Color choices are functional. |

---

## 5. Blackletter (`blackletter.html`)

### Style Authenticity Score: 2/10

| Criterion | Assessment |
|-----------|------------|
| **Color Palette** | Background `#1A1A1A` with `#8B0000` (dark red/burgundy) accent. The dark background is correct; using burgundy as the sole accent is partially thematic but loses the essential gold `#C9A84C` which is the primary accent in blackletter/gothic design. Without gold, this reads as a generic dark-red page, not medieval. |
| **Typography** | Uses `Inter, system-ui, sans-serif`. Blackletter **requires** `UnifrakturMaguntia` (the actual blackletter font loaded in the A-side) for headings and `Cinzel` for body text. Using a modern sans-serif completely destroys the Gothic identity. This is the single most important element for this style and it is entirely absent. |
| **Border Radius** | `8px` rounded corners. Gothic/blackletter demands zero border-radius -- sharp angular forms echoing cathedral architecture and ironwork. |
| **Shadows & Depth** | Generic card shadows. Missing: no shadows in traditional blackletter -- instead, flat layered borders with `outline` + `outline-offset`, cross (`\2720`) decorative markers, burgundy tinted backgrounds. |
| **Layout & Spacing** | Standard centered layout. Blackletter demands centered, formal, vertical-axis compositions with ornate border framing, heraldic symmetry. |
| **Visual Effects** | None. Missing: ornate double borders (the A-side's `.ornate-border` with `outline` + `outline-offset`), Maltese cross card decorators (`\2720::before`), burgundy gradient backgrounds on hero, gold rule dividers. |
| **Content & Voice** | Generic copy. Should reference medieval language: "Scriptorium", "Codex", "Anno Domini", Latin phrases, chapter numbering with Roman feel. |
| **Missing Elements** | UnifrakturMaguntia blackletter font, gold accent color, ornate double borders, Maltese cross decorations, parchment tones, medieval content voice, formal centered composition. |
| **CSS Bugs** | No syntax errors. |

---

## 6. Mosaic (`mosaic.html`)

### Style Authenticity Score: 2/10

| Criterion | Assessment |
|-----------|------------|
| **Color Palette** | Background `#1A5276` (navy) with `#922B21` (crimson) accent. Using the A-side's navy as the full background is a poor choice -- mosaic style should use `#FDF6E3` (cream/grout) as the dominant background with jewel-toned tile accents. The B-side inverts the palette, losing the essential "tiles on cream grout" visual. |
| **Typography** | Uses `Inter, system-ui, sans-serif`. Mosaic demands `Cinzel` serif (loaded in A-side) -- classical Roman inscriptional forms with high letter-spacing. |
| **Border Radius** | `8px` rounded corners. Mosaic tiles are defined by `1px` border-radius (barely rounded) or zero -- tiny square tesserae. The `8px` modern rounding has no mosaic character. |
| **Shadows & Depth** | Generic card shadows. Mosaic style uses flat tiles with grout gaps (the A-side achieves this with `gap: 3px` and `background: var(--grout)` on the grid container) -- no modern shadows. |
| **Layout & Spacing** | Standard centered layout. Mosaic demands grid layouts with uniform small gaps (3px "grout lines"), tile-based grid metrics with aspect-ratio squares, the repeating-linear-gradient grout texture on body. |
| **Visual Effects** | None. Missing: grout-line background texture (`repeating-linear-gradient` grid on body), tile-shaped elements with 3px gaps, jewel-colored square tiles in decorative rows, `aspect-ratio: 1` grid tiles. |
| **Content & Voice** | Generic copy. Should reference "tesserae", "Ravenna", "Pompeii", Roman villa language, artisan/ancient craft terminology. |
| **Missing Elements** | Grout-line background texture, tile-based grid layout with 3px gaps, jewel-colored decorative tile rows, Cinzel serif font, cream background, square tile elements, classical Roman content. |
| **CSS Bugs** | No syntax errors. The `#922B21` accent on `#1A5276` background has adequate contrast. |

---

## 7. Camouflage (`camouflage.html`)

### Style Authenticity Score: 2/10

| Criterion | Assessment |
|-----------|------------|
| **Color Palette** | Background `#4A5D23` (olive) with `#7A8450` (sage) accent. Using flat olive as the entire background captures one camo color but loses the multi-tone disruption pattern that defines camouflage. Should use `#1E1E16` dark background with multi-color camo blob overlays. |
| **Typography** | Uses `Inter, system-ui, sans-serif`. Camouflage demands `Barlow` (loaded in A-side) at weight 800, all-uppercase, with heavy letter-spacing -- stenciled military typography. The B-side's modern sans-serif at mixed weights is not military. |
| **Border Radius** | `8px` rounded corners. Military/camouflage uses zero border-radius -- sharp, utilitarian, stamped-metal edges. |
| **Shadows & Depth** | Generic card shadows. Camouflage uses flat, utilitarian styling with heavy 2-3px solid borders in olive, no soft modern shadows. |
| **Layout & Spacing** | Standard centered layout. Camouflage demands rigid, utilitarian grid layouts with zero-gap cards, heavy `border-bottom: 2px/3px`, stenciled badge labels, specification text. |
| **Visual Effects** | None. Missing: camo blob pattern (`radial-gradient ellipse` overlays -- the A-side's `.camo-bg::before`), stenciled badge labels (`.badge`), specification text (`.spec`), heavy olive border accents throughout. |
| **Content & Voice** | Generic copy. Should use military jargon: "Deploy", "Ops", "Intel", "Field Manual FM-26", specification codes like "Pattern: DPM-W / Zone: Temperate", classification markings. |
| **Missing Elements** | Camo blob radial-gradient overlay, stencil-style badges, military specification text, Barlow heavy uppercase font, thick olive borders, zero border-radius, military content voice. |
| **CSS Bugs** | No syntax errors. Sage `#7A8450` accent on olive `#4A5D23` background may have low contrast in some contexts. |

---

## 8. Diorama (`diorama.html`)

### Style Authenticity Score: 2/10

| Criterion | Assessment |
|-----------|------------|
| **Color Palette** | Background `#87CEEB` (sky blue) with `#90EE90` (light green) accent. While sky blue is thematically connected to the diorama's sky, using CSS named-color equivalents (`skyblue`, `lightgreen`) feels naive. The A-side uses carefully composed pastels: `#b8d8e8`, `#7cb668`, `#d4654a`, `#f2e6c9`. The B-side's `#90EE90` neon green is too saturated and artificial for a miniature/tilt-shift aesthetic. |
| **Typography** | Uses `Inter, system-ui, sans-serif`. Diorama demands `Nunito` (loaded in A-side) -- a friendly, rounded sans-serif with weight 800 that fits the miniature toylike aesthetic. |
| **Border Radius** | `8px` is actually not far off for diorama (the A-side uses 10-16px+ rounded forms), but the B-side's uniform 8px lacks the deliberately playful range of the A-side (50px pill buttons, 14px cards, 10px inputs). |
| **Shadows & Depth** | Generic card shadows. Diorama demands layered depth shadows: `drop-shadow` on buildings, multiple depth planes, the A-side's `box-shadow: 0 8px 32px rgba(0,0,0,.08)` hero overlay. |
| **Layout & Spacing** | Standard centered layout. Diorama demands layered scene composition with absolute-positioned depth planes, a parallax-like scene area, frosted glass overlays (`backdrop-filter: blur`). |
| **Visual Effects** | None. Missing: tilt-shift blur bands (`body::before/::after` with `filter: blur(2px)` at top/bottom), layered scene with sky/hills/ground planes, miniature buildings, tiny trees with CSS shapes, paper-cutout aesthetic, frosted glass hero overlay. |
| **Content & Voice** | Generic copy. Should reference "Tiny Worlds", "miniature", "paper layers", "village", scale/craft language. |
| **Missing Elements** | Tilt-shift blur bands (top/bottom), layered scene composition, miniature CSS buildings/trees, sky-to-ground gradient, frosted glass overlay, Nunito font, playful pastel palette, paper-cutout aesthetic. |
| **CSS Bugs** | No syntax errors. The `#90EE90` on `#87CEEB` creates a pastel-on-pastel low-contrast situation for labels and icons. |

---

## 9. Folkloric (`folkloric.html`)

### Style Authenticity Score: 2/10

| Criterion | Assessment |
|-----------|------------|
| **Color Palette** | Background `#8B4513` (SaddleBrown) with `#228B22` (ForestGreen) accent. The A-side uses warm cream `#faf3e7` background with earthy terracotta `#c75c3a`, mustard `#d4a843`, forest `#3d6b4e`, and navy `#2a3d5c` accents. The B-side's dark brown background with neon forest green is entirely wrong -- folkloric is warm cream with earth-tone accents, not a dark brown page with single green accent. |
| **Typography** | Uses `Inter, system-ui, sans-serif`. Folkloric demands `Lora` serif for body and `Playfair Display` serif for headings (both loaded in A-side) -- warm, literary, handcraft-feeling typefaces. |
| **Border Radius** | `8px` uniform. The A-side uses deliberately irregular "handmade" radii (`3px 5px 2px 6px`, `4px 6px 3px 5px`) to simulate hand-crafted imperfection -- a key signature of the folkloric style. The B-side's uniform 8px destroys this. |
| **Shadows & Depth** | Generic card shadows. Folkloric uses heavy `2px solid` ink borders instead of shadows, creating a hand-drawn frame effect. |
| **Layout & Spacing** | Standard centered layout. Folkloric demands traditional craft-market composition with decorative border strips, banner dividers with diamond motifs, folk pattern decorative elements. |
| **Visual Effects** | None. Missing: folk border stripe (`repeating-linear-gradient` in terracotta/mustard/forest/navy), diamond motif decorations, folk-motif circle-and-diamond pseudo-elements, paper texture (`feTurbulence`), hand-drawn underline on logo, imperfect border-radius on all elements, banner dividers. |
| **Content & Voice** | Generic copy. Should reference "Handmade Heritage", "artisan", "craft", "market", regional folk language. |
| **Missing Elements** | Folk border stripe pattern, diamond decorations, paper texture, Lora + Playfair Display fonts, warm cream background, imperfect/asymmetric border-radii, hand-drawn aesthetic, earthy multi-color accents, folk motif decorations. |
| **CSS Bugs** | No syntax errors. `#228B22` on `#8B4513` provides adequate contrast. |

---

## 10. Ukiyo-e (`ukiyo-e.html`)

### Style Authenticity Score: 2/10

| Criterion | Assessment |
|-----------|------------|
| **Color Palette** | Background `#1B4B6B` (indigo) with `#C65D4A` (vermilion) accent. Using indigo as the full background is partially thematic but inverts the A-side's approach of parchment `#E8D5B7` background with indigo accents. Ukiyo-e woodblock prints are printed on parchment/washi paper -- the paper color should dominate, with indigo and vermilion as accent colors. |
| **Typography** | Uses `Inter, system-ui, sans-serif`. Ukiyo-e demands `Noto Serif JP` (loaded in A-side) -- a Japanese serif typeface essential for the woodblock print aesthetic. This is one of the most culturally specific font requirements in the entire set. |
| **Border Radius** | `8px` rounded corners. Ukiyo-e uses zero border-radius throughout -- flat, graphic, print-inspired edges with heavy 2-3px solid borders in indigo. Woodblock prints have sharp, decisive edges. |
| **Shadows & Depth** | Generic card shadows. Ukiyo-e is fundamentally flat -- no shadows. Depth comes from layered flat color planes and bold outlines (thick borders), exactly as in woodblock printing where each color is a separate carved block. |
| **Layout & Spacing** | Standard centered layout. Ukiyo-e demands zero-gap card grids with heavy indigo borders between sections, stamp/seal decorative elements, strong horizontal banding. |
| **Visual Effects** | None. Missing: SVG wave patterns (the A-side has `.wave` and `.wave2` with inline SVG paths), vermilion stamp/seal element (`.stamp` with `transform: rotate(-5deg)`), kanji characters as decorative headers, flat color-block sections, thick indigo horizontal rules. |
| **Content & Voice** | Generic copy. Should reference "Floating World", include kanji characters, reference specific print subjects (waves, mountains, pine forests), use Edo-period cultural language. |
| **Missing Elements** | Wave SVG patterns, vermilion stamp/seal, kanji decorative elements, Noto Serif JP font, parchment background, flat color planes with zero shadows, heavy indigo borders, Japanese cultural content, woodblock print aesthetic. |
| **CSS Bugs** | No syntax errors. Colors are functional. |

---

## Cross-Cutting Issues

### The Template Problem

All 10 B-sides share identical:

1. **HTML structure:** `bh` > `bhero` > `bsec`(features grid) > `bsec`(metrics) > `bsec`(quote) > `bfoot`
2. **CSS framework:** Same class names (`.bh`, `.bhero`, `.bbtn`, `.bcard`, `.bmets`, `.bquote`, `.bfoot`), same layout values, same responsive breakpoints
3. **Copy:** Identical text across all 10 files:
   - "Distinctive by design"
   - "A distinctive visual approach that brings unique character and personality to every interface"
   - "A strong, recognizable aesthetic that sets this style apart from all others"
   - "Every element speaks the same visual dialect, creating cohesion"
   - "Small touches that make this style feel genuine rather than generic"
   - "A truly distinctive design approach that brings real character to every project"
4. **Icons:** Same three Unicode symbols across all: `&#9670;`, `&#9674;`, `&#10038;`
5. **Font:** `Inter, system-ui, sans-serif` everywhere
6. **Border radius:** `8px` everywhere
7. **Hover:** `translateY(-3px)` on cards, `translateY(-1px)` on buttons

### Color Substitution Logic

The only customization follows a mechanical pattern:
- **Background:** One color from the A-side palette (often not the best choice)
- **Accent:** A secondary color from the A-side palette
- **Text:** White `#fff` on dark backgrounds, black `#000` on light backgrounds
- **Muted text:** `#aaa` on dark, `#666` on light

### Severity Rankings

| Rank | File | Score | Critical Issue |
|------|------|-------|----------------|
| 10 | Cinematic | 1/10 | Invisible text (near-black accent on black bg) |
| 9 | Art Deco | 2/10 | Inverted palette, no geometric motifs |
| 8 | Film Noir | 2/10 | No venetian blinds, no red accent, wrong font |
| 7 | Blackletter | 2/10 | Missing blackletter font entirely |
| 6 | Mosaic | 2/10 | No tile/grout texture, wrong background |
| 5 | Camouflage | 2/10 | No camo pattern, no military typography |
| 4 | Folkloric | 2/10 | Wrong background color, no folk decorations |
| 3 | Diorama | 2/10 | No tilt-shift blur, no scene layers |
| 2 | Ukiyo-e | 2/10 | No wave patterns, no Japanese font, no stamps |
| 1 | Astrological | 3/10 | Best color match, but still no celestial effects |

### Recommendations

For each B-side to achieve a score of 7/10 or higher, the following minimum changes would be needed:

1. **Load the correct fonts** -- each A-side already imports them; the B-side should reference them
2. **Use style-appropriate border-radius** -- 0px for Art Deco/Film Noir/Cinematic/Blackletter/Mosaic/Camouflage/Ukiyo-e; irregular for Folkloric; large-round for Diorama/Astrological
3. **Add at least one signature visual effect** per style (venetian blinds, starfield, camo blobs, wave patterns, etc.)
4. **Write style-specific copy** instead of shared generic text
5. **Correct the color application** -- use the right color as background vs. accent (cream bg for Mosaic/Folkloric/Ukiyo-e; dark for Film Noir/Cinematic/Astrological/Art Deco)
6. **Fix the Cinematic visibility bug** immediately -- accent color is invisible on the background
7. **Replace generic icons** with style-appropriate symbols (zodiac for Astrological, kanji for Ukiyo-e, crosses for Blackletter, etc.)

---

*Report generated 2026-03-20 by UI Designer Agent*

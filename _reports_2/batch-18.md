# Batch 18 Audit Report

**Auditor:** UI Designer Agent
**Date:** 2026-03-20
**Styles reviewed:** woodcut, risograph, constructivism, pharmaceutical, vibrant-blocks

---

## Woodcut
**Style Authenticity Score: 7/10**

### Fonts
- **Family:** Playfair Display (700, 900) for display; Inter (400, 500) for body. Loaded via Google Fonts link on line 8, with a duplicate link on line 103 that also loads weight 400.
- **Appropriateness:** Playfair Display is a strong choice. Its high-contrast thick/thin strokes echo the incised quality of relief printing. Inter for body is neutral and clean -- acceptable but a slab serif like Courier or a rougher serif would reinforce the handmade quality more. The B-side drops Inter entirely (line 58 sets `font-family: 'Playfair Display', 'Georgia', serif`), which is actually more authentic.

### Colors
- **A-side palette (line 11):** `--black: #1A1A1A`, `--cream: #F5F0E8`, `--ink: #2A2A2A`, `--mid: #8A8478`.
- **B-side palette:** `#1A1A1A` (black), `#F5F0E8` (cream), `#555555` (mid-gray), `#EBE4D8` (card background).
- **Accuracy:** The cream-on-dark-ink palette is historically correct for woodcut. Real woodcuts use warm paper stock and pure black ink. The `#F5F0E8` cream is an excellent warm paper tone. `#1A1A1A` is near-black without being harsh -- this is accurate to how printing ink actually appears.
- **Contrast ratios:** `#1A1A1A` on `#F5F0E8` yields approximately 14.5:1 -- well above WCAG AAA. `#8A8478` on `#F5F0E8` is approximately 3.2:1, which fails WCAG AA for body text (needs 4.5:1). The `#555555` used in the B-side on `#F5F0E8` is approximately 5.7:1 -- passes AA.
- **Accent usage:** No color accent exists beyond black, cream, and mid-gray. This is correct for woodcut. The absence of color is itself the design decision.

### Layout
- **Hero (A-side):** Centered text with `padding: 56px 24px 44px` (line 19). No max-width constraint on the hero section itself, though the paragraph caps at `max-width: 500px` (line 21).
- **Hero (B-side):** `min-height: 80vh`, flexbox centered (line 65), `max-width: 640px` inner container (line 66). The border-bottom rule on line 96/100 is duplicated.
- **Section spacing:** A-side uses `36px` padding for section heads (line 26). B-side uses `5rem` (80px) section padding (line 74). Both are reasonable.
- **Max-width:** A-side has no container max-width -- cards and content flow to full viewport width. B-side caps at `1100px` (line 75). The A-side is more authentic (broadside posters were not max-width constrained) but needs guardrails on large screens.
- **Responsive:** B-side includes a media query at 768px (line 99) hiding nav, reducing hero height to 60vh, and collapsing grid to 1 column. A-side has no responsive rules at all.

### Sizing
- **Typography scale (A-side):** h1 is `56px` (line 20), section heads `32px` (line 26), card h3 `20px` (line 30), body `14px` (line 12), card text `13px` (line 31), nav links `12px` (line 17).
- **Typography scale (B-side):** h1 is `clamp(2.5rem, 6vw, 4rem)` (line 68), section title `1.8rem` (line 77), card h3 `1.05rem` (line 81), body `1.05rem` hero paragraph (line 69), card body `.88rem` (line 82).
- **Padding and margins:** A-side cards use `28px 24px` padding (line 29). B-side cards use `2rem` (line 79). Sections in B-side are generous at `5rem 2rem`.
- **Element proportions:** The woodblock strip (line 33) at `80px` height is a nice illustrative element. Card numbers at `48px` (line 32) with very light opacity serve as decorative indices.

### Sections
- **Current sections:** A-side has hero, woodblock pattern strip, process cards (Carve/Ink/Press), quotes, footer. B-side has hero, feature cards, metrics, quote, footer.
- **Process cards are excellent** for woodcut -- they walk through the actual printmaking process. This is one of the strongest content choices in the batch.
- **The woodblock pattern strip** (lines 33-40) demonstrating dark, hatch, crosshatch, dot, and light fill patterns is a standout feature that directly showcases the visual vocabulary of woodcut.
- **B-side metrics** using unicode block characters (lines 140: `&#9608;`, `&#9618;`, `&#9617;`, `&#9616;`) instead of numbers is a creative and style-appropriate choice -- these represent ink density/tone values.
- **What would better demonstrate the style:** A section showing a woodcut illustration (CSS-only or SVG), a before/after "carved vs printed" comparison, or a gallery of different hatching techniques applied to shapes.

### Visuals
- **Hatching patterns (A-side):** `.hatch-bg` (line 13) uses `repeating-linear-gradient(45deg, ...)` at 3-4px intervals. `.crosshatch` (line 14) layers two opposing 45-degree gradients. Both are authentic woodcut shading techniques.
- **Woodblock strip:** Five distinct fill patterns -- solid black (`.wb-dark`), diagonal hatch (`.wb-hatch`), crosshatch (`.wb-cross`), dot pattern (`.wb-dot` using `radial-gradient`), and plain cream (`.wb-light`). This is a museum-quality tonal reference strip.
- **B-side global overlay (line 98):** A fixed `::before` pseudo-element applying a very subtle full-page hatch at `.015` opacity. This is a nice atmospheric touch.
- **B-side even-section hatch (line 97):** `repeating-linear-gradient` at `.03` opacity on alternating sections.
- **Border treatments:** Thick 3px solid black borders throughout (lines 15, 19, 28, 29, 33) simulate the strong lines of carved relief blocks. This is one of the most authentic visual decisions in the file.
- **Missing:** No rough/irregular edge treatment. Real woodcuts have imperfect edges where the gouge meets wood grain. A CSS `filter: url()` with a displacement map or irregular SVG border could simulate this.

### Animations
- **@keyframes:** None defined in either A-side or B-side.
- **Transitions (A-side):** `.cut-btn` has `transition: all .2s` (line 22) with a hover that inverts colors. Nav links have no explicit transition.
- **Transitions (B-side):** `.bcard:hover` has `transform: translateY(-3px)` (line 80). Buttons have `translateY(-1px)` on hover (lines 72-73).
- **Motion appropriateness:** The minimal animation is correct for woodcut. This is a print-first medium; excessive motion would undermine the static, printed quality. The subtle card lifts are acceptable. No animations is the right call.

### Content
- **Brand name:** "Pressmark" (A-side), "WOODBLOCK" (B-side) -- both are strong, evocative, and directly reference printmaking.
- **Tagline:** "Carved in Wood" is direct and powerful. B-side "Bold Impressions" is good but more generic.
- **Hero copy:** "Bold lines cut into blocks. Ink pressed onto paper. The ancient art of relief printing..." is excellent. Educational, evocative, and specific to the medium.
- **Card titles/descriptions:** "Carve," "Ink," "Press" -- these are the actual three steps of woodcut printmaking. The descriptions are technically accurate and well-written.
- **Quote:** "The woodcut is the most original graphic technique..." attributed to Ernst Ludwig Kirchner is a real quote from a real printmaker (German Expressionist). Excellent authenticity.
- **B-side content:** More generic ("What Sets Us Apart"), but the card topics (Deep Black, Hatching, Thick Lines) are on-point for the medium.

### Specific Fix Recommendations
1. **Fix the contrast issue on `--mid: #8A8478`** used for hero paragraph text (line 21). Darken to at least `#6B6158` to achieve 4.5:1 against `#F5F0E8`.
2. **Add rough edge treatment** to borders. Use an SVG filter with `feTurbulence` and `feDisplacementMap` to make the 3px solid borders appear hand-carved rather than pixel-perfect.
3. **Remove the duplicate Google Fonts link** on line 103 (already loaded on line 8) and the duplicate `.bhero` border-bottom rule on line 100 (already defined on line 96).
4. **Add responsive styles for the A-side.** The card grid uses `auto-fit` (line 28) which helps, but nav, hero, and typography need breakpoint adjustments.
5. **Introduce a CSS-only woodcut illustration** in the hero -- even a simple tree, bird, or abstract geometric carved from a solid black rectangle using `clip-path` would dramatically increase the style's visual impact.

---

## Risograph
**Style Authenticity Score: 7/10**

### Fonts
- **Family:** Space Grotesk (400, 600, 700) loaded via Google Fonts on line 8, with a duplicate link on line 190 adding weight 500.
- **Appropriateness:** Space Grotesk is a contemporary geometric grotesque that pairs well with the indie print-studio aesthetic of risograph. Riso prints often use modern sans-serifs or hand-drawn type. The choice works, though a slightly quirkier option like `'Roc Grotesk'` or `'Basier Circle'` could push the indie-studio vibe further.

### Colors
- **A-side palette (lines 11-18):** `--bg: #f5f0e8`, `--coral: #e8594f`, `--blue: #3a5ba0`, `--overlap: #2a1848`, `--ink: #2a2a2a`, `--dim: #999`.
- **B-side palette:** `#F5F0E8` (background), `#FF6B6B` (primary coral), `#333333` (text), `#888888` (muted), `#4169E1` (royal blue -- via card nth-child), `#C85078` (pink -- via card nth-child).
- **Accuracy:** The A-side nails the classic riso two-color scheme. Coral (`#e8594f`) and blue (`#3a5ba0`) are spot-on for common riso ink colors. The overlap color `#2a1848` (deep purple) is what you actually get when coral and blue multiply. The B-side shifts to `#FF6B6B` which is brighter and less "ink-like" -- real riso inks are slightly muted by paper absorption.
- **Contrast:** `#2a2a2a` on `#f5f0e8` is approximately 13:1 (AAA). `#999` on `#f5f0e8` is approximately 2.8:1 -- fails WCAG AA. B-side `#888888` on `#F5F0E8` is approximately 3.4:1 -- also fails AA for body text.
- **Paper tone:** `#f5f0e8` is perfect for uncoated stock. Riso printing always happens on recycled/uncoated paper with this warm off-white tone.

### Layout
- **Hero (A-side):** Left-aligned, `padding: 40px 24px 30px` (line 38). No hero height constraint. Content max-width achieved via the `max-width: 350px` on the paragraph (line 73) and `max-width: 300px` on h1 (implicit from its font size and context).
- **Hero (B-side):** Centered, `min-height: 80vh` (line 149), inner max-width `640px` (line 150).
- **Section spacing:** A-side components section has `padding: 36px 24px` (line 87). B-side sections have `5rem 2rem` (line 158).
- **Poster quality:** The A-side has a more poster-like composition with the overprint decoration circles positioned absolutely in the top-right corner. This is authentic to riso poster design. The B-side is a standard landing page layout.
- **Responsive:** B-side has a 768px breakpoint (line 186). A-side has no responsive rules.

### Sizing
- **Typography scale (A-side):** h1 `36px` (line 63), card h3 `16px` (line 109), section label `10px` (line 88), body text `13px` (line 73), button `13px` (line 77), input `13px` (line 117), nav `12px` (line 35).
- **Typography scale (B-side):** h1 `clamp(2.5rem, 6vw, 4rem)` (line 152), section title `1.8rem` (line 161), card h3 `1.05rem` (line 165), hero paragraph `1.05rem` (line 153).
- **Padding:** A-side card padding `20px` (line 101). B-side card padding `2rem` (line 163). Swatches are `48px` square (line 123).

### Sections
- **Current A-side sections:** Hero with overprint decoration, components showcase (buttons, card, input, color palette). This is more of a design system showcase than a landing page.
- **Current B-side sections:** Hero, feature cards (Coral Ink, Blue Ink, Misregistration), metrics (2 Inks, Multiply, Offset, Halftone), quote, footer.
- **B-side metrics are creative:** Using symbols (`x` for multiply, `~` for offset, a circle for halftone) to represent riso concepts instead of traditional numbers.
- **What would better demonstrate the style:** A "print run" gallery showing overlapping color layers, a step-by-step visualization of ink passes (first pass coral, second pass blue, combined result), or a zine-style grid layout with torn-edge sections.

### Visuals
- **Overprint decoration (A-side, lines 41-53):** Two overlapping circles using `::before` (coral, opacity 0.6) and `::after` (blue, opacity 0.6) with `mix-blend-mode: multiply`. This is the defining visual of risograph printing and it is executed correctly.
- **Halftone dot pattern (lines 56-60):** `radial-gradient(circle, var(--coral) 1px, transparent 1px)` at `background-size: 6px 6px`, opacity 0.15. This simulates the visible halftone screen of riso printing. Correct technique.
- **Misregistration on logo (lines 30-33):** Logo `::after` pseudo-element offset by `top: 1px; left: 2px` in coral at `opacity: .5`. This simulates the color registration offset between drum passes. Authentic.
- **Misregistration on "Duotone" text (lines 66-72):** `attr(data-text)` pseudo-element offset `top: 2px; left: 3px` in coral. Same technique as logo -- good consistency.
- **CTA shadow (lines 80-84):** Blue pseudo-element at `top: 3px; left: 3px` with `mix-blend-mode: multiply`. Simulates a second ink pass shadow.
- **Card offset border (lines 104-108):** Coral `::before` border at `top: 4px; left: 4px` with multiply blend. Continues the misregistration motif.
- **Halftone on swatches (lines 126-130):** Dot pattern overlay on color swatches. Good detail.
- **Paper grain texture (line 22):** Inline SVG `feTurbulence` filter at `baseFrequency='0.9'` with `opacity: .04`. This is exactly the technique specified in the visual DNA reference. Excellent.
- **B-side:** Has a subtle blue overlay on the hero via `::after` (line 184) but loses almost all of the A-side's rich visual effects. No halftone, no misregistration, no overprint circles.

### Animations
- **@keyframes:** None defined.
- **Transitions (A-side):** Nav links `opacity .3s` (line 35), CTA `all .3s` with `transform: translate(-1px, -1px)` on hover (line 85), buttons `all .3s` (line 93), input focus `border-color .3s` (line 117).
- **Transitions (B-side):** Card `transform .2s` (line 163), buttons `all .2s` (line 155).
- **Motion appropriateness:** Minimal motion is appropriate. Riso is a physical print medium -- the CTA hover shift simulates slight paper misalignment which is a clever touch. No keyframe animations needed.

### Content
- **Brand name:** "RISO" -- direct and literal. Effective for a reference page, though a more evocative studio name like "Drum Press" or "Two Pass" would feel more authentic.
- **Tagline:** "Overprint Duotone" is descriptive. B-side "Happy Accidents" references the beautiful imperfection of riso -- this is stronger.
- **Hero copy (A-side):** "Misregistered layers, halftone dots, and limited-palette charm. Two-color printing elevated to art." Concise and technically accurate.
- **Hero copy (B-side):** "Two inks -- coral and royal blue. Multiply blend. Halftone dots. Misregistration. Print-studio charm." This reads like a specification list, which actually works for a reference page.
- **Card content (A-side):** "Ink Layer" card with "Soy-based inks on uncoated stock" -- technically correct. Riso uses soy-based inks.
- **Quote:** "Handmade, indie, artfully imperfect. Straight from a small-batch print studio." Generic but on-theme.
- **Metrics:** "2 Inks," "Multiply," "Offset," "Halftone" -- these are the four defining characteristics of risograph printing. Excellent.

### Specific Fix Recommendations
1. **Fix the contrast failure on `--dim: #999`** (line 17) and B-side `#888888`. Both fail WCAG AA for body text against `#f5f0e8`. Darken to at least `#757575` (A-side) and `#6E6E6E` (B-side).
2. **Port the A-side's visual effects to the B-side.** The B-side loses the halftone dots, overprint circles, misregistration on text, and card offset borders. Without these, the B-side looks like a generic landing page with a coral accent color. At minimum, add halftone overlays and text misregistration.
3. **Remove the duplicate Google Fonts link** on line 190 and the duplicate card nth-child rules on line 187 (already defined on lines 180-183).
4. **Add a section border-top to the B-side.** Currently `bsec` has `border-top: none` (line 158), which makes sections blend together without visual separation. Riso prints have strong edge contrast -- use a border or a contrasting ink-color divider.
5. **Increase halftone dot visibility.** The A-side halftone at `opacity: .15` (line 59) is almost invisible. Real riso prints have clearly visible halftone screens. Increase to `opacity: 0.25-0.35` and apply to more elements (headlines, card backgrounds).

---

## Constructivism
**Style Authenticity Score: 8/10**

### Fonts
- **Family:** Oswald (400, 600, 700) as the primary font; Roboto Condensed (700) for display headlines. Loaded via Google Fonts on line 8.
- **Appropriateness:** Both are excellent choices. Oswald's condensed, bold proportions echo the compact sans-serifs used in Soviet posters. Roboto Condensed at 700 weight provides the heavy, architectural headline treatment that constructivism demands. The `text-transform: uppercase` applied throughout (lines 24, 26, 54, 59, 69, 94) is mandatory for this style and is correctly implemented.

### Colors
- **A-side palette (lines 11-17):** `--red: #CC0000`, `--black: #000`, `--cream: #F5E6CC`, `--dark-cream: #e0cba6`, `--ink: #1a1410`.
- **B-side palette:** `#CC0000` (red), `#000000` (black), `#F5E6CC` (cream), `#666666` (gray).
- **Accuracy:** The red-black-cream triad is the canonical constructivist palette. `#CC0000` is a strong Soviet red, though `#C41E3A` (referenced in the visual DNA) would be marginally more historically accurate. The warm `#F5E6CC` cream suggests aged paper or propaganda poster stock -- correct.
- **Contrast:** `#000000` on `#F5E6CC` is maximum effective contrast (approximately 16:1). `#CC0000` on `#F5E6CC` is approximately 4.8:1 -- passes AA for normal text. `#666666` on `#F5E6CC` is approximately 4.9:1 -- passes AA.
- **This is the best color implementation in the batch** -- every combination meets or exceeds WCAG AA requirements.

### Layout
- **Hero (A-side):** No padding on the hero container (line 29); content padded at `50px 24px 40px` (line 50). Asymmetric composition with geometric elements (diagonal bar, circle, triangle) positioned absolutely on the right side. This diagonal asymmetry is the hallmark of constructivist layout.
- **Hero (B-side):** Left-aligned on line 150 (`justify-content` is absent, defaulting to flex-start, but the `text-align` is not set either -- the inner `bhero-inner` is not explicitly centered). The `::before` pseudo-element (line 184) creates a skewed red bar at `opacity: .06` which references the A-side's diagonal bar. Button alignment is left via `justify-content` omission on `.bhero-btns`.
- **Section spacing:** B-side sections use `5rem 2rem` with a `3px solid #CC0000` border-top (line 159). The red section dividers are style-appropriate.
- **Diagonal energy:** The A-side achieves this with the diagonal bar rotated at `-15deg` (line 34) and the repeating diagonal stripe divider (line 80). The B-side has a subtle skewed `::before` and diagonal hatching on the third section (line 185). More diagonal elements would strengthen the B-side.

### Sizing
- **Typography scale (A-side):** h1 `42px` (line 58), hero tag `10px` (line 54), hero paragraph `13px` (line 64), CTA `14px` (line 69), card h3 `16px` (line 111), card body `12px` (line 114), section label `11px` (line 87).
- **Typography scale (B-side):** h1 `clamp(3rem, 8vw, 5rem)` (line 181, overriding 153), section title `1.8rem` (line 162), card h3 `1.05rem` (line 166), body `.88rem` (line 167).
- **The B-side h1 is notably larger** than other B-sides in this batch (`clamp(3rem, 8vw, 5rem)` vs the typical `clamp(2.5rem, 6vw, 4rem)`), which is correct -- constructivism demands maximum typographic impact.
- **Line height on B-side h1:** `.85` (line 181) -- this extremely tight leading is authentic. Soviet posters packed enormous type into tight spaces.

### Sections
- **A-side sections:** Hero with geometric decorations, diagonal-stripe divider, components (buttons, card, input, palette).
- **B-side sections:** Hero, feature cards (Red Power, Black Force, Diagonal Cut), metrics (1920 Born, 2 Colors, 45 degree Angle, 900 Weight), quote (Rodchenko), footer.
- **Content themes are strong.** The B-side text is rendered in ALL CAPS throughout the HTML content (line 237-239), which is both style-authentic and a deliberate content decision.
- **Metrics are excellent:** "1920" (the year constructivism emerged), "2" (the two primary colors), "45 degrees" (the characteristic diagonal angle), "900" (maximum font weight). These are educational and accurate.
- **What would better demonstrate the style:** A propaganda-poster section with radiating lines (`repeating-conic-gradient`), a photomontage section using `clip-path: polygon()` to crop images into angular shapes, or a manifest/manifesto section with numbered declarations.

### Visuals
- **Diagonal bar (line 32-35):** `width: 250px; height: 600px; transform: rotate(-15deg)` in Soviet red. This is the single most important visual element for constructivism and it is present and correct.
- **Geometric shapes (lines 38-47):** A circle (`border: 6px solid var(--black); border-radius: 50%`) and a triangle (CSS border trick). These reference constructivist geometric vocabulary (Lissitzky, Rodchenko).
- **Diagonal stripe divider (lines 79-83):** `repeating-linear-gradient(-45deg, var(--black) 8px, var(--red) 8px, var(--red) 16px)` at `height: 8px`. This hazard-stripe pattern is a period-accurate decorative element.
- **Card left-bar accent (lines 106-109):** 8px-wide red bar on the left edge of cards via `::before`. This creates a visual anchor reminiscent of constructivist sidebar markers on posters.
- **CTA offset shadow (lines 72-75):** Black-bordered pseudo-element at `bottom: -4px; left: 4px`. Adds dimensionality consistent with the layered poster aesthetic.
- **B-side background pattern (line 185):** `repeating-linear-gradient(-45deg, ...)` at very low opacity on the third section. Subtle but present.
- **Missing:** Radiating lines (conic gradient), rotated text elements, and photomontage clip-paths are absent. These are the visual DNA's signature CSS techniques for constructivism.

### Animations
- **@keyframes:** None defined.
- **Transitions:** Nav links `opacity .3s` (line 27), buttons `all .3s` (lines 95, 98), CTA `all .3s` (line 70), input `border-color .3s` (line 125), B-side cards `transform .2s` (line 164).
- **Motion appropriateness:** Correct. Constructivism is a print/poster movement. Animations would be anachronistic. The hover state on the CTA changing to black background (line 76) is a strong, decisive interaction that matches the style's bold directness.

### Content
- **Brand name:** "Construct" (A-side), "WORKERS" (B-side). "WORKERS" is outstanding -- it directly references the worker-centric ideology that drove constructivism as an art movement.
- **Tagline:** "Manifesto No. 7" (A-side hero tag) is a genius touch -- constructivists published numbered manifestos. B-side "UNITE!" is similarly appropriate.
- **Hero copy:** "Design for the Masses" with "Masses" in red -- this is the core thesis of constructivism. "Diagonal compositions, bold geometry, and revolutionary typography" accurately describes the visual hallmarks.
- **Card content:** "Collective Unit" with "Production quotas exceeded. Output metrics indicate 140% efficiency gain through unified design." This reads like actual Soviet production reports. Darkly humorous and stylistically perfect.
- **Rodchenko quote:** "THE ART OF THE REVOLUTION IS THE REVOLUTION OF ART" attributed to Alexander Rodchenko. This is a well-known constructivist sentiment, appropriately rendered in all capitals.
- **This is the strongest content in the entire batch.** Every text element reinforces the historical and ideological context of the style.

### Specific Fix Recommendations
1. **Add rotated text elements to the B-side.** Constructivism is defined by diagonal compositions, but the B-side layout is entirely horizontal. Add at least one rotated headline (e.g., `transform: rotate(-15deg)`) or a diagonal section divider.
2. **Implement radiating lines** using `repeating-conic-gradient` as a background pattern for the hero or a decorative section. This is called out as a signature CSS technique in the visual DNA.
3. **Add `clip-path: polygon()` treatments** for at least one visual element -- angular crops on images or sections would reinforce the geometric aggression of the style.
4. **Clean up CSS redundancy.** Line 146 has a double color declaration (`color:#CC0000;color:#F5E6CC`), line 148 overrides the same color twice, and line 181/187 duplicates the h1 sizing and nav hover color rules.
5. **Consider adding an A-side responsive breakpoint.** The absolute-positioned geometric decorations (diagonal bar, circle, triangle) will overflow on small screens.

---

## Pharmaceutical
**Style Authenticity Score: 6/10**

### Fonts
- **Family:** Inter (300, 400, 500, 600) loaded via Google Fonts on line 8.
- **Appropriateness:** Inter is an excellent choice for pharmaceutical/clinical UI. Its tall x-height ensures legibility at small sizes (critical for drug information), and its neutral, clinical character avoids personality or warmth that would undermine the sterile aesthetic. The use of `font-weight: 300` for body text (lines 20, 37) is a deliberate design decision that conveys precision and lightness, though it may reduce readability at small sizes.

### Colors
- **A-side palette (line 11):** `--white: #FAFCFF`, `--blue: #0066CC`, `--light-blue: #E8F2FF`, `--clinical: #F0F4F8`, `--gray: #8899AA`, `--dark: #1A2B3C`, `--pill: #D4E5F7`.
- **B-side palette:** `#F0FDFA` (mint-white background), `#0D9488` (teal), `#134E4A` (dark teal), `#5F9EA0` (cadet blue), `#B2DFDB` (light teal border), `#E0F2F1` (very light teal), `#FFFFFF` (cards).
- **A-side accuracy:** The cool blue palette (`#0066CC` primary, `#E8F2FF` light, `#FAFCFF` near-white) is spot-on for pharmaceutical branding. Think Pfizer, Johnson & Johnson, or any drug monograph. The subtle blue-tinted white (`#FAFCFF` instead of `#FFFFFF`) adds a clinical coolness.
- **B-side deviation:** The B-side switches from blue to teal (`#0D9488`), which is more "wellness app" than "pharmaceutical." Real pharma brands overwhelmingly use blue (trust, authority, clinical cleanliness). The teal shift weakens authenticity.
- **Contrast:** A-side `#1A2B3C` on `#FAFCFF` is approximately 13:1 (AAA). `#8899AA` on `#FAFCFF` is approximately 3.7:1 -- fails AA for body text. B-side `#134E4A` on `#F0FDFA` is approximately 9.5:1 (AAA). `#5F9EA0` on `#F0FDFA` is approximately 3.2:1 -- fails AA.

### Layout
- **Hero (A-side):** Centered text, `padding: 40px 28px 44px` (line 13), with a gradient background `linear-gradient(180deg, var(--light-blue), var(--white))` (line 13). Clean, professional, and entirely typical of pharmaceutical product pages.
- **Hero (B-side):** Centered, `min-height: 80vh` (line 68), max-width `640px` (line 69).
- **Section spacing:** A-side components section uses `padding: 28px` (line 25). B-side sections use `5rem 2rem` (line 77).
- **The A-side centered-nav layout** (line 14) with centered links is very pharma-authentic. Drug websites use centered, minimal navigation to keep focus on the product.
- **Responsive:** B-side has the standard 768px breakpoint (line 103). A-side has no responsive rules.

### Sizing
- **Typography scale (A-side):** h1 `28px` (line 19), subtitle `13px` (line 20), section label `10px` (line 26), card h3 `15px` (line 36), card body `12px` (line 37), CTA `13px` (line 21), nav `11px` (line 14).
- **Typography scale (B-side):** h1 `clamp(2.5rem, 6vw, 4rem)` (line 71), section title `1.8rem` (line 80), card h3 `1.05rem` (line 84), body `.88rem` (line 85).
- **The A-side h1 at 28px is notably restrained** -- pharmaceutical sites avoid shouting. This is authentic. The B-side's `4rem` (64px) max is far too aggressive for a clinical aesthetic.
- **Pill-shaped elements:** The `.cta` has `border-radius: 28px` (line 21). Cards have `border-radius: 12px` (line 33). Blister cells are `border-radius: 50%` (line 24). The B-side uses `border-radius: 9999px` (line 74) for fully capsule-shaped buttons. These rounded forms consistently reference pill/capsule shapes.

### Sections
- **A-side sections:** Hero with pill icon and blister-pack grid, components (buttons, product card with dosage badge, input, palette).
- **B-side sections:** Hero, feature cards (Sterile Clean, Pill Shapes, High Contrast), metrics (AAA Contrast, 100% Sterile, 48px Touch, Verified), quote, footer.
- **Blister-pack grid (lines 23-24):** A 4-column grid of circular cells with radial gradients simulating blister-pack pill cavities. This is a highly specific and authentic pharmaceutical visual element. Outstanding.
- **Dosage badge (line 38):** `<span class="dosage">250 mg / tablet</span>` -- a pill-shaped badge showing drug dosage. This is exactly what you see on pharma packaging.
- **Product card content:** "Azitrex 250mg" with "Film-coated tablets for oral administration" -- this reads like actual drug monograph copy.
- **What would better demonstrate the style:** A drug information section with structured data (indications, contraindications, dosage schedule), a safety information banner with fine print, a molecular structure visualization, or a clinical trial data table.

### Visuals
- **Pill icon (lines 17-18):** Gradient circle with a "+" symbol. Simple, clean, universal medical symbol.
- **Blister-pack grid (lines 23-24):** Radial gradient (`circle at 40% 35%, #fff, var(--pill)`) creates a 3D dome effect on each cell. The light offset at 40%/35% simulates overhead light hitting a plastic blister bubble. This is meticulous.
- **Card dot indicator (line 35):** 8px blue circle beside the card title, reminiscent of clinical status indicators on medical dashboards.
- **B-side card top bar (line 101):** A `3px` teal bar at the top of each card via `::before`. This is common in medical/clinical dashboards for categorization.
- **B-side card border-radius conflict:** Line 82 sets `border-radius: 9999px` on `.bcard`, then line 99 overrides it to `12px`, then line 104 duplicates `12px`. The `9999px` pill-shape on cards would have been nonsensical, so the override is correct but the code is messy.
- **Missing:** No pharmaceutical-specific patterns like molecular structures, hexagonal grids, or DNA-helix motifs. No clinical data visualization (progress bars, status indicators). The sterile whitespace is present but underutilized.

### Animations
- **@keyframes:** None defined.
- **Transitions (A-side):** CTA `all .2s` (line 21), nav `color .2s` (line 15), buttons `all .2s` (line 28), input `border-color .2s` (line 41).
- **Transitions (B-side):** Cards `transform .2s` (line 82), buttons `all .2s` (line 74).
- **Motion appropriateness:** Minimal transitions are correct. Pharmaceutical interfaces prioritize reliability and predictability over delight. The subdued `.2s` timing is appropriate -- faster than the standard `.3s`, conveying precision and responsiveness.

### Content
- **Brand name:** "MedaCure Clinical" (A-side), "MediCare+" (B-side). "MedaCure" sounds like a real pharmaceutical brand. "MediCare+" risks confusion with the actual Medicare government program -- this should be changed.
- **Tagline:** "Precision therapeutics backed by evidence-based formulations" -- this could be pulled from any real pharma website. Authentic tone.
- **Hero copy (B-side):** "Pristine minty white. Deep teal. Pill-shaped buttons. Precision inspires confidence." This is meta-commentary on the design rather than product copy. For a reference page this works, but for authenticity it should read like an actual pharma landing page.
- **Metrics (B-side):** "AAA Contrast," "100% Sterile," "48px Touch," "Verified" -- these mix accessibility metrics with clinical language in a clever way.
- **Quote:** "Clinical clarity that inspires absolute confidence in every interaction" -- generic but tonally appropriate.

### Specific Fix Recommendations
1. **Change the B-side primary color from teal (`#0D9488`) back to blue (`#0066CC`).** Pharmaceutical branding is overwhelmingly blue. The teal makes it look like a wellness/spa app rather than a clinical product.
2. **Fix contrast failures.** A-side `--gray: #8899AA` on `#FAFCFF` needs darkening to at least `#6B7D8F`. B-side `#5F9EA0` on `#F0FDFA` needs darkening to at least `#4A7C7E`.
3. **Rename "MediCare+" to avoid confusion** with the US government Medicare program. Consider "MedaCure+" or "ClarityRx" or "PrecisionMed."
4. **Clean up the B-side CSS redundancy:** `.bcard` border-radius is set three times (lines 82, 99, 104). Remove lines 82's `9999px` and line 104's duplicate.
5. **Add a structured drug information section** with a data table or definition list showing Indication, Dosage, Contraindications, and Side Effects. This would dramatically improve the pharmaceutical authenticity beyond the current generic card layout.

---

## Vibrant Blocks
**Style Authenticity Score: 8/10**

### Fonts
- **Family:** Space Grotesk (400, 500, 700) loaded on line 8, with a duplicate link on line 275 loading (500, 600, 700, 800).
- **Appropriateness:** Space Grotesk is an excellent choice for vibrant blocks. Its geometric construction and available heavy weights (700, 800) deliver the bold, graphic impact this style requires. The `text-transform: uppercase` applied throughout (lines 31, 39-40, 58-59, 78, 109-110, 117, 132-133) creates the shouting, unapologetic energy that defines the style.

### Colors
- **A-side palette:** `#0D0D0D` (near-black body), `#FFDD00` (yellow nav), `#FF3366` (pink hero), `#00D4AA` (teal blocks/card), `#4D4DFF` (blue blocks/buttons), `#F5F5F0` (off-white components section).
- **B-side palette:** `#1A1A2E` (dark navy body), `#FF6B35` (fire orange primary), `#004E89` (navy card), `#00A878` (emerald card), `#FCBF49` (golden yellow card), `#CCCCCC` (muted text).
- **Accuracy:** Both sides deliver high-saturation, bold color blocks -- the defining characteristic of this style. The A-side uses a five-color palette (pink, yellow, teal, blue, black) that is very Bloomberg Businessweek / Spotify Wrapped. The B-side uses a four-color palette (orange, navy, emerald, yellow) against dark navy, which is more Mailchimp-rebrand.
- **Contrast:** A-side `#FFF` on `#FF3366` is approximately 3.9:1 -- fails AA for body text, marginal for large text. `#0D0D0D` on `#FFDD00` is approximately 15:1 (excellent). B-side `#FFFFFF` on `#FF6B35` is approximately 3.3:1 -- fails AA. `#FFFFFF` on `#004E89` is approximately 7.2:1 (passes).
- **Each card being a different color** (lines 265-269 in B-side) is the most important color technique for this style, and it is correctly implemented.

### Layout
- **Hero (A-side):** Full-bleed composition with no max-width constraints. Nav in yellow, hero content in pink, block strip at bottom -- three distinct color zones stacked vertically. `min-height: 70vh` (line 15). This is textbook vibrant-blocks layout.
- **Block strip (lines 85-97):** Three equal-width color blocks (`flex: 1`) displaying metrics. This is a signature element -- using colored blocks as data containers rather than cards or panels.
- **Hero (B-side):** `min-height: 80vh`, centered text, entire hero in `#FF6B35` orange (line 270). Bold full-bleed color. No gradients, no shadows -- pure flat color. Correct.
- **Section spacing:** B-side sections at `5rem 2rem` (line 243) with `border-top: none` (line 243). The lack of borders is correct -- blocks are defined by color changes, not lines.
- **Responsive:** B-side has the 768px breakpoint (line 271). A-side has no responsive rules -- the block strip will compress poorly on mobile.

### Sizing
- **Typography scale (A-side):** h1 `3rem` (48px, line 55), hero paragraph `1rem` (line 62), nav `0.85rem` (line 37), component group h3 `0.7rem` (line 114), button text `0.85rem` (line 125), card h4 `1.05rem` (line 178), card body `0.85rem` (line 183).
- **Typography scale (B-side):** h1 `clamp(2.5rem, 6vw, 4rem)` (line 237), section title `1.8rem` (line 246), metrics `2.2rem` (line 254).
- **The A-side h1 at 3rem (48px) is impactful** but could be larger. The visual DNA specifies `font-size: clamp(2rem, 6vw, 5rem); font-weight: 900` -- the A-side uses 700 weight rather than 900.
- **Block strip values at 1.5rem with labels at 0.7rem** (lines 96-97) create a clean data hierarchy within the colored blocks.

### Sections
- **A-side sections:** Hero (nav + content + block strip), components (buttons, card, input, palette). The hero is the star -- three stacked color blocks forming a single composition.
- **B-side sections:** Hero (full orange), feature cards (each a different color), metrics, quote, footer.
- **Feature cards as colored blocks** (lines 248, 265-269): Navy (`#004E89`), emerald (`#00A878`), and golden (`#FCBF49`) cards deliver the core promise of the style -- every section and container is a bold, distinct color block.
- **What would better demonstrate the style:** Full-width alternating color sections (instead of cards within a neutral section), a gallery of color block compositions, or a statistics section where each stat lives in its own full-width color band. The visual DNA specifies "full-width color blocks stacked vertically, each section a different color" -- the B-side uses colored cards within neutral sections instead.

### Visuals
- **Zero rounded corners:** A-side buttons have no `border-radius` (default 0). Cards use no radius. B-side `.bbtn` has `border-radius: 0px` (line 240). `.bcard` has `border-radius: 0px` (line 248). This adherence to sharp edges is correct per the visual DNA ("No `border-radius`, no `box-shadow`, no `border`").
- **Zero shadows:** Neither side uses `box-shadow` on any element. Correct -- vibrant blocks relies purely on color and type.
- **Thick borders (A-side):** `3px solid #0D0D0D` on cards (line 158), inputs (line 195), card headers (line 166), and swatches (line 214). These borders add structure without undermining the flat-color aesthetic.
- **Focus state (line 204-207):** `border-color: #FF3366; box-shadow: 4px 4px 0 #FF3366` -- an offset block-shadow focus ring that matches the bold, geometric language. Good detail.
- **Card header with "BOLD" watermark (lines 168-176):** The `.card-header::after` content reads "BOLD" at 30% opacity. This meta-label reinforces the style identity.
- **B-side hero background (line 270):** Full solid orange. Clean, bold, and correct.
- **Missing:** No full-width alternating color sections in the B-side (the most iconic vibrant-blocks pattern). The B-side wraps colored cards inside a neutral dark section, which dilutes the impact.

### Animations
- **@keyframes:** None defined.
- **Transitions (A-side):** Hero button `all 0.15s` (line 80), all buttons `all 0.15s` (line 134), input `all 0.15s` (line 202).
- **Transitions (B-side):** Cards `transform .2s` (line 248), buttons `all .2s` (line 240).
- **Motion appropriateness:** Minimal transitions are correct. This style is about static visual impact -- color, type, and proportion. The 0.15s timing is even snappier than usual, conveying decisiveness. No keyframes needed.

### Content
- **Brand name:** "Blockhaus" (A-side), "BOLD" (B-side). "Blockhaus" references Bauhaus (appropriate given the geometric simplicity). "BOLD" is literal and effective.
- **Tagline:** "Bold moves only." is punchy and matches the visual energy. B-side "Color is everything" tag and "Make a Statement" headline are similarly direct.
- **Hero copy:** "Vibrant color blocks as layout containers. High energy, maximum contrast, startup-ready design that demands attention." Accurate and self-aware.
- **Card content (B-side):** "Fire Orange" ("Commanding attention like a traffic cone"), "Deep Navy" ("Authority, depth, quiet confidence"), "Emerald Green" ("Fresh, alive, vibrant"). Each card describes its own color -- this meta-approach works well for a reference page.
- **Metrics:** "4 Blocks," "0px Radius," "900 Weight," "Infinity Impact" -- these cleverly describe the style's own design parameters. The "0px Radius" entry specifically calls out the zero-border-radius rule.

### Specific Fix Recommendations
1. **Make each B-side section a different background color** instead of using colored cards within a neutral dark section. The visual DNA specifies "Full-width color blocks stacked vertically, each section a different color." The features section could be solid emerald, the metrics section solid navy, and the quote section solid yellow-gold. This is the single most impactful change for style authenticity.
2. **Fix contrast failures.** White text on `#FF3366` (A-side hero, ~3.9:1) and white on `#FF6B35` (B-side hero, ~3.3:1) both fail AA. For the orange hero, use `#1A1A2E` dark navy text instead of white, or darken the orange to `#D45A2B`.
3. **Remove the duplicate Google Fonts link** on line 275 and the duplicate CSS rules on line 272.
4. **Increase the A-side h1 font-weight from 700 to 900** (or 800). The visual DNA calls for `font-weight: 900` and the B-side already loads weight 800 via the duplicate font link.
5. **Add responsive styles for the A-side.** The three-column block strip (lines 85-97) will not stack gracefully on mobile without a breakpoint.

---

## Summary Table

| Style | Score | Best Element | Biggest Gap |
|-------|-------|-------------|-------------|
| Woodcut | 7/10 | Woodblock tonal strip with 5 fill patterns | No rough/irregular edge treatment on borders |
| Risograph | 7/10 | A-side overprint circles with mix-blend-mode: multiply | B-side loses all signature visual effects (halftone, misregistration) |
| Constructivism | 8/10 | Content writing (manifesto numbering, production quotes, Rodchenko attribution) | Missing radiating lines and rotated text elements in B-side |
| Pharmaceutical | 6/10 | Blister-pack grid with radial gradient dome effect | B-side uses teal instead of blue, undermining pharma identity |
| Vibrant Blocks | 8/10 | Colored cards and zero-radius/zero-shadow discipline | B-side uses colored cards within neutral sections instead of full-width color blocks |

### Cross-Cutting Issues

1. **Contrast failures in muted text colors.** Four of five styles fail WCAG AA on their secondary/muted text color. This is a systemic issue across the batch: woodcut `#8A8478`, risograph `#999`, pharmaceutical `#8899AA` and `#5F9EA0`, vibrant-blocks white-on-orange.

2. **A-side responsive gaps.** None of the five A-sides include any responsive breakpoints. The B-sides all share a common 768px media query, but the A-sides would break on mobile (especially constructivism's absolute-positioned geometric elements and vibrant-blocks' flex strip).

3. **Duplicate CSS rules and font links.** Every file has either a duplicate Google Fonts `<link>` tag or duplicate CSS rule declarations (often both). This indicates the B-side CSS was appended without auditing for conflicts with the A-side's font loading.

4. **B-side visual dilution.** A consistent pattern: the A-sides have rich, style-specific visual treatments (overprint circles, hatching patterns, diagonal bars, blister grids, color blocks), while the B-sides share a near-identical structural template with only color and font changes. The B-sides would benefit from porting at least one signature visual technique from their respective A-sides.

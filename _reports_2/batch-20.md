# Batch 20 Audit Report

**Auditor:** UI Designer Agent
**Date:** 2026-03-20
**Styles Reviewed:** split-flap, scratch-card, lenticular, isometric-ui, gen-z-chaos

---

## Split-Flap
**Style Authenticity Score: 8/10**

### Fonts
- **A-Side:** JetBrains Mono (400-800) and Inter (400-700) loaded via Google Fonts link tag. JetBrains Mono is used for all board text, labels, and nav. Inter is the body fallback on the reset but barely appears since nearly everything is forced to the mono face.
- **B-Side:** Share Tech Mono loaded via a second Google Fonts link (line 355). Used as the primary font family on `.b-side` (line 309). This is a strong, authentic choice -- Share Tech Mono closely emulates the rigid, mechanical letterforms you see on real Solari boards.
- **Appropriateness:** Excellent for both sides. Monospaced fonts are the single most critical typographic choice for a departure-board aesthetic. Both JetBrains Mono and Share Tech Mono succeed. The A-Side is slightly more refined; the B-Side is slightly more raw, which fits the "mechanical" angle.

### Colors
- **A-Side palette (from palette swatches, lines 431-436):**
  - Board: `#111` (near-black background)
  - Amber: `#FFBF00` (primary accent, used on logo, headers, h1, buttons, input focus)
  - White: `#fff` (flap text)
  - Go: `#4ADE80` (green status)
  - Alert: `#EF4444` (red cancel/alert)
  - Supporting dark tones: `#0a0a0a`, `#0D0D0D`, `#1A1A1A`, `#222`, `#333`, `#444`
- **B-Side palette:**
  - Background: `#0D0D0D`
  - Primary accent: `#F0E68C` (khaki/pale yellow -- departure board amber analogue)
  - Text muted: `#666666`
  - Borders: `#333333`
  - Cards: `#1A1A1A`
- **Contrast ratios:** Amber `#FFBF00` on `#111` delivers roughly 9.5:1 -- excellent. Khaki `#F0E68C` on `#0D0D0D` yields approximately 12:1 -- excellent. Muted text `rgba(255,255,255,0.35)` on dark backgrounds is the weakest point at roughly 3.5:1, falling below WCAG AA for normal text.
- **Accent usage:** Amber and khaki dominate appropriately, matching the warm phosphor glow of real split-flap displays. Status colors (green, amber, red) are used semantically and match airport signage convention.

### Layout
- **A-Side hero:** Full-width stacked layout -- nav at top (`padding: 14px 20px`), board header, departure table rows in a grid (`grid-template-columns: 70px 1fr 90px 70px`), then a centered hero message. This mimics a real departure board extremely well.
- **A-Side components:** Max-width of `560px`, centered with auto margins. Compact, single-column. Feels like a kiosk display.
- **B-Side:** Standard landing page layout with `.bcon` at `max-width: 1100px`. Hero is 80vh, full-center. Standard three-column `.bgrid` at `minmax(280px, 1fr)`.
- **Responsive:** B-Side collapses to single column at 768px, hides nav. A-Side has no media queries, which is a gap since the departure grid would break on small screens.

### Sizing
- **A-Side typography scale:**
  - h1: `28px` (line 175)
  - Board title: `12px` (line 78)
  - Board time: `14px` (line 84)
  - Nav logo: `15px` (line 49)
  - Nav links: `11px` (line 62)
  - Flap characters: `13px` (line 137)
  - Dep-header labels: `9px` (line 106)
  - Card title: `13px` (line 250)
  - Body text: `13px` (line 268)
- **B-Side typography scale:**
  - h1: `clamp(2.5rem, 6vw, 4rem)` (line 319)
  - h2: `1.8rem` (line 328)
  - Card h3: `1.05rem` (line 332)
  - Body: `0.88rem` (line 333)
  - Tag: `0.8rem` (line 318)
  - Metric value: `2.2rem` (line 336)
- **Spacing:** A-Side uses tight spacing (6-20px padding) appropriate for a compact data display. B-Side uses generous `5rem` section padding, `2rem` card padding.

### Sections
- **Current sections (B-Side):** Header, Hero, Feature Cards (gates), Metrics, Quote, Footer.
- **Effectiveness:** The feature cards styled as "GATE A1", "GATE B3", "GATE C7" with departure-formatted descriptions are clever and thematic. The horizontal split line on cards (`.bcard::after`, line 348) simulates the mechanical split across each flap panel. Metrics formatted as departure time, gate, status, and destination are on-point.
- **What would better demonstrate this style:**
  - A live departure board section with animated row-by-row character flipping (the A-Side has this; the B-Side lacks it)
  - A status ticker or marquee-style announcement bar
  - A section showing individual character flaps cycling through letters

### Visuals
- **A-Side pseudo-elements:** `.flap::after` (line 143-150) creates the horizontal midline split on every character cell -- this is the signature visual of a split-flap display and is well-executed. `.card::before` with `content: 'WINNER'` is not present; instead, `.card-badge` is used for "Active" label.
- **B-Side pseudo-elements:** `.bcard::after` (line 348) adds horizontal midline across cards, reinforcing the split-flap metaphor on content cards. Duplicated at line 352 -- minor code duplication.
- **Box shadows on flaps:** `box-shadow: 0 1px 2px rgba(0,0,0,0.4), inset 0 1px 0 rgba(255,255,255,0.05)` (line 141) gives each character cell a subtle physical depth.
- **Status dot glows:** Green, amber, and red dots use `box-shadow` glow effects (lines 162-164), simulating LED indicator lights.
- **Background treatment:** Purely dark flat colors, no textures. This is acceptable -- real departure boards are matte black. A subtle noise texture could add physical presence.

### Animations
- **@keyframes defined (A-Side):**
  - `flipDown` (lines 19-23): 3D rotateX flip on the X axis, 0.6s. Applied via `.flap.flip` class on select rows. Authentic mechanical flip motion.
  - `blink` (lines 24-27): Opacity pulse between 1 and 0.3, 2s. Used on `.board-time` and `.status-red`. Simulates LED blinking.
  - `slideReveal` (lines 28-31): translateY(-8px) to 0 with fade. Defined but not applied anywhere in the HTML -- dead code.
- **@keyframes defined (B-Side):**
  - `flipChar` (line 350): Stepped opacity animation on `.bmet-v`, 3s. Simulates the stutter of a flap mid-rotation. Subtle but effective.
- **Transitions:** Hover transitions on buttons (`translateY(-1px)`), cards (`translateY(-3px)`). Appropriate -- understated and mechanical.
- **Motion appropriateness:** Excellent. The flip animation is the defining motion of this style. The blink on time and cancelled flights is a clever touch. One improvement: the A-Side `flipDown` should use `transform-origin: top` to simulate a top-hinged flap more realistically.

### Content
- **Brand names:** "TRANSIT" (A-Side, line 362), "DEPARTURES" (B-Side, line 440). Both appropriate.
- **Tagline:** "Mechanical beauty, digital precision" (line 401) -- solid, evocative.
- **Hero copy:** "FLIGHT STATUS." with "NOW BOARDING" tag (B-Side) -- strong and thematic.
- **Card titles and descriptions:** "GATE B12 / Active" (A-Side); "GATE A1 / DEPARTURE: 14:30 / STATUS: ON TIME / DESTINATION: FUTURE" (B-Side). The metaphorical destinations ("FUTURE", "INNOVATION", "PERFECTION") are playful while maintaining the format.
- **Metrics:** "14:30 / B3 / ON TIME / FWD" -- formatted as departure data. Relevant and well-themed.
- **Quote:** "The satisfying clatter of flipping panels. Mechanical precision meets charm." attributed to "Airport Architecture Review" -- apt and evocative.

### Specific Fix Recommendations
1. **A-Side missing responsive styles.** The departure table grid (`70px 1fr 90px 70px`) will overflow on screens below 400px. Add a media query at 480px that stacks or simplifies the departure rows.
2. **Dead animation `slideReveal` (lines 28-31).** Either apply it to departure rows on page load (e.g., staggered row entrance) or remove it to reduce dead code.
3. **Muted text contrast issue.** `color: rgba(255,255,255,0.35)` on `.hero-message p` (line 183) and `rgba(255,255,255,0.45)` on `.card-body p` (line 268) fall below WCAG AA. Increase to at least `rgba(255,255,255,0.55)` for 4.5:1 ratio.
4. **B-Side missing the actual flap character treatment.** The A-Side has individual `.flap` spans with the `::after` midline creating each split-flap letter. The B-Side has no equivalent -- text is plain. Add a CSS-only flap treatment (dark background panels behind each character) to at least the hero heading or metric values.
5. **Duplicate CSS rules.** `.bcard::after` is defined at line 348 and duplicated at line 352. `.bcard{position:relative}` is declared twice. Clean up.
6. **Add `transform-origin: center top` to `.flap.flip`** so the `flipDown` animation hinges from the top edge, matching real mechanical flip behavior.

---

## Scratch Card
**Style Authenticity Score: 7/10**

### Fonts
- **A-Side:** Poppins (400, 600, 700, 800, 900) via Google Fonts. Rounded, friendly, high-energy -- matches the gamified, promotional feel of lottery/scratch card branding.
- **B-Side:** Inter with system-ui fallback (line 338). Generic sans-serif. Loses the playful energy of the A-Side.
- **Appropriateness:** Poppins is a strong choice for this style -- real scratch cards use bold, rounded, high-impact type. The B-Side downgrade to Inter makes it feel like a generic SaaS page rather than a gamified experience. A bolder display font (e.g., Rubik, Fredoka, or even keeping Poppins) would serve the B-Side better.

### Colors
- **A-Side palette (from swatches, lines 449-453):**
  - Gold: `#FFD700` (primary -- prize color)
  - Night: `#1a0a2e` (deep purple background)
  - Purple: `#6B21A8` (secondary)
  - Amber: `#FFA000` (gold gradient endpoint)
  - Silver: `#bbb` (scratch surface)
  - Supporting: `#2d1450`, `#4a1c6b` (purple gradient midpoints)
  - Scratch overlay metals: `#888`, `#999`, `#aaa`, `#bbb`, `#ccc` (line 154)
- **B-Side palette:**
  - Background: `#1A1A2E` (dark navy)
  - Primary accent: `#FF6B35` (warm orange -- not gold)
  - Card backgrounds: `linear-gradient(135deg, #C0C0C0, #E8E8E8, #C0C0C0)` (silver)
  - Card borders: `#999999`
  - Muted text: `#888888`
- **Contrast ratios:** Gold `#FFD700` on `#1a0a2e` is approximately 8.2:1 -- excellent. Orange `#FF6B35` on `#1A1A2E` is approximately 4.9:1 -- passes AA for normal text. Muted `rgba(255,255,255,0.5)` on purple backgrounds is roughly 4.1:1 -- borderline.
- **Palette accuracy issue:** The B-Side switches from gold/purple to orange/silver. Real scratch cards are gold, silver, and high-saturation jewel tones. The orange `#FF6B35` reads more as a tech startup accent than a lottery/prize color.

### Layout
- **A-Side hero:** Centered flex column, `min-height: 460px`, `padding: 48px 24px`. Contains a scratch card widget (280px wide), sparkle dots, and a CTA button. The scratch card being embedded in the hero is the strongest layout decision -- it makes the interactive reveal the focal point.
- **A-Side components:** `max-width: 560px`, single column, centered.
- **B-Side:** Standard landing page with `.bcon` at `max-width: 1100px`. Hero at 80vh. Standard three-column card grid.
- **Responsive:** B-Side has 768px breakpoint collapsing grid to single column. A-Side has no media queries, but the centered single-column layout is inherently flexible.

### Sizing
- **A-Side typography scale:**
  - h1: `40px` (line 85)
  - h3 (card): `17px` (line 267)
  - Body: `13-14px` (lines 99, 268)
  - Buttons: `13px` (line 222)
  - Labels: `10px` (line 209)
  - CTA: `15px` (line 183)
  - Scratch label: `10px` (line 126)
  - Scratch prize: `28px` (line 147)
- **B-Side typography scale:**
  - h1: `clamp(2.5rem, 6vw, 4rem)` (line 348)
  - h2: `1.8rem` (line 357)
  - Card h3: `1.05rem` (line 361)
  - Body: `0.88rem` (line 362)
- **Spacing:** A-Side hero padding `48px 24px`, component section `40px 24px`. B-Side section padding `5rem 2rem`. Proportions are standard.

### Sections
- **Current sections (B-Side):** Header, Hero, Feature Cards (silver surfaces), Metrics, Quote, Footer.
- **Effectiveness:** The silver-gradient card backgrounds (`.bcard`, line 359) that reveal a colorful gradient on hover (`linear-gradient(135deg, #FF6B35, #22C55E)`, line 379) is the strongest B-Side decision. The "SCRATCH" watermark text (`.bcard::before`, line 377) that fades on hover adds to the reveal metaphor.
- **What would better demonstrate this style:**
  - A prize tier section showing different reward levels with masked/revealed states
  - A "match 3" game grid (the A-Side has `reveal-grid` tiles; the B-Side lacks this)
  - A progress bar or "scratched X of Y" counter
  - A confetti/celebration animation on reveal (the `confetti` keyframe is defined at line 31-34 but never used)

### Visuals
- **A-Side pseudo-elements:**
  - Hero `::before` (lines 49-54): Radial gold glow overlay at 50% 30%, creating a spotlight effect.
  - `.card::before` (lines 255-266): Diagonal "WINNER" banner, `rotate(45deg)`, gold on purple. Classic scratch-card/lottery visual.
  - `.scratch-overlay` (lines 151-169): Silver metallic gradient with `clip-path` reveal on hover. This is the core scratch mechanic and is well-executed.
- **B-Side pseudo-elements:**
  - `.bcard::before` (line 377): "SCRATCH" watermark centered on cards with `opacity: 0` on hover. Adds thematic texture.
  - `.bcard:hover` color shift (lines 379-380): Cards flip from silver to a vibrant orange/green gradient, simulating the reveal.
- **Sparkle dots (A-Side):** Five absolutely positioned gold circles with staggered sparkle animations (lines 57-67). Evocative of scratch-card "lucky" visual language.
- **Shimmer animation on B-Side cards:** `shimmerScratch` keyframe (line 381) sweeps a light band across the card `::before`. Simulates the metallic shimmer of an unscratched surface.

### Animations
- **@keyframes defined (A-Side):**
  - `sparkle` (lines 19-22): Scale 0 to 1 with rotation. Used on sparkle dots. Festive, appropriate.
  - `shimmerGold` (lines 23-26): Background-position sweep on gold gradient text. Used on `.hero h1 .gold`. Creates a "premium gold" shimmer.
  - `pulse` (lines 27-30): Scale 1 to 1.05. Applied to `.scratch-card` (line 114). Draws attention to the interactive element.
  - `confetti` (lines 31-34): Translate up + rotate + fade. NEVER USED -- dead code.
- **@keyframes defined (B-Side):**
  - `shimmerScratch` (line 381): Background-position sweep, 3s linear infinite. Applied to `.bcard::before`. Good metallic shimmer effect.
- **Transitions:** Scratch overlay uses `clip-path` transition (line 164) for the reveal. Reveal tiles use `opacity 0.5s` (line 303). Buttons have `translateY(-2px)` hover.
- **Motion appropriateness:** The scratch/reveal animations are central to this style. The `clip-path` reveal is clever as a CSS-only scratch simulation. Missing: a "win" celebration animation -- the `confetti` keyframe exists but is wasted.

### Content
- **Brand names:** "LOOT" (A-Side, line 397), "Lucky" (B-Side, line 458). Both work for a gamified reveal brand.
- **Tagline:** "Uncover hidden rewards. Every interaction is a chance to discover something extraordinary." (line 406) -- appropriate gamification language.
- **Hero copy:** "What Will You Win?" (B-Side) -- direct, exciting, fits the scratch-card anticipation.
- **Card content:** A-Side card "Grand Prize" with gamified description. B-Side cards "Silver Surface", "Prize Reveal", "Scratch Texture" -- descriptive of the visual technique. Effective.
- **Metrics:** Emoji slot machine, "3x Match", "$$$", checkmark "Winner" (B-Side, line 461). Playful and thematic.
- **Quote:** "That breathless moment of scratching to reveal. Part game, part surprise." -- "Gamification Weekly" (line 462). Appropriate source and sentiment.

### Specific Fix Recommendations
1. **Use the `confetti` keyframe (lines 31-34).** It is defined but never applied. Trigger it on the scratch-card hover state or create a JS-triggered celebration when the overlay is fully removed. Without it, the "win" moment lacks climax.
2. **B-Side accent should be gold, not orange.** Replace `#FF6B35` with `#FFD700` or `#F5A623` (warm gold) throughout the B-Side. The orange reads as a tech brand, not a prize/lottery aesthetic.
3. **B-Side needs Inter font loaded.** The B-Side declares `font-family: 'Inter', system-ui, sans-serif` (line 338) but the Google Fonts link (line 8) only loads Poppins. Either add Inter to the font link or switch the B-Side to Poppins for consistency.
4. **B-Side cards should have a more interactive reveal.** Currently the silver-to-color transition happens instantly on hover. Add a `transition: background 0.6s ease` or use a `clip-path` wipe to simulate an actual scratch motion rather than an instant color swap.
5. **Muted text contrast.** `color: rgba(255,255,255,0.5)` (hero paragraph, line 100) on dark purple is approximately 4.1:1. Increase to `rgba(255,255,255,0.65)` for reliable AA compliance.
6. **B-Side cards text color on hover.** When `.bcard:hover` activates (line 379), card text changes from `#333333` to `#fff`, but `.bcard p` color (line 362) stays `#888888` unless the `:hover p` rule (line 380) overrides it. The `.bcard h3` color is inherited from the initial dark text -- verify that headings also become readable on the vivid gradient background.

---

## Lenticular
**Style Authenticity Score: 6/10**

### Fonts
- **A-Side:** Inter (400, 700, 900) via Google Fonts. Clean, neutral geometric sans-serif.
- **B-Side:** Inter with system-ui fallback (line 118). Same font.
- **Appropriateness:** Adequate but not distinctive. Lenticular design is about optical illusion and visual trickery -- the typography could lean more experimental. A wider, more optical font (e.g., Darker Grotesque, Outfit, or even a variable-width font that shifts on hover) would reinforce the angle-shift concept.

### Colors
- **A-Side palette (from swatches, lines 202-206):**
  - `#E94560` (vibrant pink-red)
  - `#533483` (deep purple)
  - `#0F3460` (navy blue)
  - `#16213E` (dark navy)
  - `#1A1A2E` (near-black blue)
- **B-Side palette:**
  - Background: `#0F172A` (very dark slate)
  - Primary accent: `#818CF8` (soft indigo)
  - Text muted: `#6B7B8B`
  - Card background: `#1E293B`
  - Card border: `rgba(129, 140, 248, 0.1)`
- **Contrast ratios:** A-Side gradient text (`#E94560` to `#533483` to `#0F3460`) is background-clipped so contrast depends on which gradient slice is visible; the pink end achieves roughly 5.2:1 on `#1A1A2E`, the purple end drops to roughly 2.8:1 -- fail. B-Side indigo `#818CF8` on `#0F172A` is approximately 5.6:1 -- passes AA. Muted `#6B7B8B` on `#0F172A` is approximately 3.8:1 -- fails AA for body text.
- **Palette accuracy:** The A-Side palette is vibrant and has enough color variation to simulate lenticular color-shifting. The B-Side's uniform indigo monochrome loses the multi-color angle-shift essence. A lenticular palette should have at least two contrasting hues that appear to shift between states.

### Layout
- **A-Side hero:** Flex column, `min-height: 55vh`, with `perspective: 600px` on the hero container. Contains a `tilt-card` with front/back content. The shift-bands are decorative vertical strips animated across the background. This layout places the interactive tilt card as the centerpiece.
- **A-Side components:** Padding `2rem`, no max-width set on `.components` (line 73). Cards and buttons are full-width in their container.
- **B-Side:** Standard layout -- `.bcon` at `max-width: 1100px`, 80vh hero, three-column grid. Nearly identical structure to other B-Sides in this batch.
- **Responsive:** B-Side has 768px breakpoint. A-Side has no media queries, which is acceptable for the simpler layout.

### Sizing
- **A-Side typography scale:**
  - h1: `2.8rem` (line 48)
  - Subtitle: `1rem` (line 52)
  - Components h2: `1.3rem` (line 74)
  - Card h3: `1rem` (line 91)
  - Card p: `0.8rem` (line 92)
  - Button: `0.8rem` (line 77)
  - CTA: `0.9rem` (line 54)
  - Swatch label: `0.55rem` (line 106)
- **B-Side typography scale:**
  - h1: `clamp(2.5rem, 6vw, 4rem)` (line 128)
  - h2: `1.8rem` (line 137)
  - Body: `0.88rem` (line 142)
  - Tag: `0.8rem` (line 127)
- **Spacing:** A-Side hero padding `2rem`, components `2rem`. B-Side sections `5rem 2rem`.

### Sections
- **Current sections (B-Side):** Header, Hero, Feature Cards ("Front Layer", "Mid Layer", "Back Layer"), Metrics, Quote, Footer.
- **Effectiveness:** The card content about depth layers (Front, Mid, Back) is thematically aligned. The perspective-based hover transforms on cards (`perspective(800px) rotateY(3deg)`) are the strongest B-Side element. However, the sections themselves are structurally identical to every other B-Side -- there is nothing visually that creates a lenticular illusion.
- **What would better demonstrate this style:**
  - An image-swap section where hovering reveals a different image (like physical lenticular cards)
  - Vertical stripe overlay across the entire page (the A-Side has this via `.lenticular-stripe::after`; the B-Side does not)
  - A section with layered elements at different z-depths that shift on scroll/hover
  - Split-view comparisons that change based on cursor position

### Visuals
- **A-Side pseudo-elements:**
  - `.lenticular-stripe::after` (lines 17-20): Repeating vertical stripe overlay -- `repeating-linear-gradient(90deg, rgba(0,0,0,0.15) 0px, 3px, transparent 3px, 6px)`. This is the most critical lenticular visual -- it mimics the ribbed plastic surface that creates the angle-shift illusion. Well-executed.
  - `.card::before` (lines 88-89): Top gradient accent line.
- **B-Side pseudo-elements:** None specific to lenticular. No stripe overlay, no depth layering. This is the biggest B-Side gap.
- **Shift bands (A-Side, lines 60-70):** Five absolutely positioned, animated vertical strips at various positions with translucent color fills. They slide vertically with `shiftSlide` animation. Simulates the optical shimmer of a lenticular surface.
- **Tilt card (A-Side, lines 37-46):** Front/back content that swaps opacity on hover while the card rotates 8deg Y and -3deg X. This is the core lenticular interaction -- viewing angle changes the visible content.
- **Card hover (B-Side, line 157):** `transform: perspective(800px) rotateY(3deg)` -- subtle but present perspective tilt. Each card tilts a different direction (lines 157-159). This is good but minimal.
- **Missing from B-Side:** No lenticular stripe overlay, no content-swap on tilt, no multi-layer parallax.

### Animations
- **@keyframes defined (A-Side):**
  - `shiftSlide` (line 70): TranslateY -10% to 10% with opacity 0.5 to 1, 6s ease alternate. Used on shift-band spans. Simulates vertical shimmer movement.
- **@keyframes defined (B-Side):** None. Zero keyframe animations on the B-Side. This is a significant authenticity gap for a style centered on visual motion and angle-dependent change.
- **Transitions:** A-Side tilt card has `transition: transform 0.5s ease` and `opacity 0.5s` for content swap. B-Side cards have `transition: transform 0.3s`. Both use hover-triggered transforms.
- **Motion appropriateness:** The A-Side animations are good but could be more pronounced. The B-Side has essentially no motion beyond hover transforms, which undermines the lenticular concept. This style demands more animation: parallax scrolling, angle-reactive movement, or periodic shimmer effects.

### Content
- **Brand names:** "LENTIK" (A-Side, line 171), "Parallax" (B-Side, line 211). "Parallax" is more descriptive of the depth effect but strays into parallax-scrolling territory rather than lenticular-card territory.
- **Tagline:** "Interactive surfaces that reveal hidden layers as you explore." (line 177) -- accurate description of lenticular behavior.
- **Hero copy:** "Shift Your Perspective." (B-Side) -- strong, directly references the angle-shift mechanic.
- **Card content:** "Front Layer", "Mid Layer", "Back Layer" with depth descriptions. Thematic and clear.
- **Metrics:** "3 Layers", "5 deg Tilt", "800px Perspective", "Infinity Depth" (line 214). Technical CSS values used as thematic metrics -- clever and authentic.
- **Quote:** "Like a premium lenticular card. Tilt it and watch the layers dance." -- "Spatial Design Review" (line 215). Appropriate.

### Specific Fix Recommendations
1. **B-Side critically needs the lenticular stripe overlay.** Add a `::before` or `::after` on `.b-side` or `.bhero` with `repeating-linear-gradient(90deg, rgba(255,255,255,0.03) 0px, rgba(255,255,255,0.03) 2px, transparent 2px, transparent 5px)` to simulate the ribbed lenticular surface. Without this, it is just a dark landing page with mild tilt.
2. **Add a shimmer animation to the B-Side.** Define a keyframe that sweeps a highlight band across the hero or cards, simulating the angle-dependent light reflection of a lenticular surface.
3. **Muted text `#6B7B8B` on `#0F172A` fails WCAG AA.** Lighten to `#8B9BAB` or similar for 4.5:1 ratio.
4. **B-Side cards should swap content on hover,** not just tilt. The defining feature of lenticular printing is that two different images are visible depending on viewing angle. Add a front/back text swap (like the A-Side tilt-card) to at least one section.
5. **Duplicate CSS at line 161.** `.bcard{transition:transform .3s} .bcard:hover{transform:perspective(800px) rotateY(3deg)}` repeats the rules already on lines 156-159. Clean up.
6. **A-Side `.components` section lacks a `max-width`.** The palette swatches and buttons will stretch to full viewport width on large screens. Add `max-width: 600px; margin: 0 auto;` to contain them.

---

## Isometric UI
**Style Authenticity Score: 8/10**

### Fonts
- **A-Side:** Space Grotesk (400, 500, 700) via Google Fonts. Also redundantly loaded again at line 128 with weights 400-700.
- **B-Side:** Space Grotesk with Inter fallback (line 79). Same primary font.
- **Appropriateness:** Space Grotesk is an excellent choice. Its geometric construction and slightly techy feel complement the precise, mathematical nature of isometric design. The clean letterforms do not compete with the geometric shapes.

### Colors
- **A-Side palette (from swatches, lines 167-171):**
  - `#4ECDC4` (teal -- primary)
  - `#FF6B6B` (coral red)
  - `#45B7D1` (sky blue)
  - `#FFE66D` (yellow)
  - `#1A1A2E` (dark background)
  - Supporting: `#16213E` (card background), `#2A2A4E` (borders)
- **B-Side palette:**
  - Background: `#1A1A2E` (same dark)
  - Primary: `#4ECDC4` (teal -- carried over)
  - Card 1: `#4ECDC4` with shadow `#36a89f`
  - Card 2: `#FF6B6B` with shadow `#CC5555` (line 117)
  - Card 3: `#45B7D1` with shadow `#3595AB` (line 119)
  - Card text on colored bg: `rgba(0,0,0,0.6)` (line 121)
  - Muted text: `#888888`
- **Contrast ratios:** Teal `#4ECDC4` on `#1A1A2E` is approximately 8.3:1 -- excellent. Card text `rgba(0,0,0,0.6)` on `#4ECDC4` is approximately 3.4:1 -- fails AA for normal text. `#888888` on `#1A1A2E` is approximately 4.8:1 -- passes AA.
- **Palette accuracy:** The vibrant, flat, saturated colors are authentic for isometric illustration. Real isometric UIs (think Monument Valley, isometric infographics) use this exact palette approach: bold primaries with darker shadow variants. The shadow colors (`#36a89f`, `#CC5555`, `#3595AB`) being manually darker versions of the base colors is correct for simulating isometric lighting.

### Layout
- **A-Side hero:** `min-height: 70vh`, flex with `justify-content: space-between` splitting text left and isometric grid right. The `.iso-grid` uses a 2x2 CSS grid rotated with `rotateX(55deg) rotateZ(-45deg)` and `perspective: 600px`. This is the canonical isometric CSS transform.
- **A-Side components:** `padding: 3rem 2rem`, no explicit max-width. Uses `grid-template-columns: repeat(auto-fit, minmax(260px, 1fr))` for cards.
- **B-Side:** Standard centered layout, `max-width: 1100px`. B-Side cards use solid colored backgrounds with hard offset shadows -- the strongest isometric visual.
- **Responsive:** Both sides handle 768px with column stacking. A-Side hero stacks to `flex-direction: column` at mobile.

### Sizing
- **A-Side typography scale:**
  - h1: `3rem` (line 24), mobile `2.2rem` (line 64)
  - Components h2: `0.75rem` uppercase label (line 45)
  - Card h4: `1.05rem` (line 53)
  - Card p: `0.85rem` (line 54)
  - Body: `1rem` (line 26)
  - Button: `0.85rem` (line 29)
- **B-Side typography scale:**
  - h1: `clamp(2.5rem, 6vw, 4rem)` (line 89)
  - h2: `1.8rem` (line 98)
  - Card h3: `1.05rem` (line 102)
  - Body: `0.88rem` (line 103)
  - Metric: `2.2rem` (line 106)
- **Isometric block sizing:** Each block is `80px x 80px` (line 35) with `12px` gap. Blocks are elevated at different `translateZ` values: 20px, 40px, 60px, 10px (lines 39-42). These staggered heights create a convincing isometric cityscape.
- **B-Side card shadows:** `6px 6px 0` hard offset (line 100) -- the right scale for the card size. Creates the isometric illusion of a raised platform.

### Sections
- **Current sections (B-Side):** Header, Hero, Feature Cards, Metrics, Quote, Footer.
- **Effectiveness:** The colored cards with hard-offset shadows (`.bcard`, line 100) are the strongest B-Side element -- they look like isometric blocks viewed from above. The hexagonal icon clip-path (`.bcard-icon`, line 123) adds geometric interest. Card content about "Teal Blocks", "Coral Accents", and "Precise Angles" directly references the isometric vocabulary.
- **What would better demonstrate this style:**
  - An actual isometric scene/illustration section (the A-Side has the `.iso-grid`; the B-Side lacks it entirely)
  - A stacked/layered section where elements overlap at isometric angles
  - Cards arranged in an isometric grid pattern rather than a flat CSS grid
  - A "build" or "stack" interactive section where blocks assemble

### Visuals
- **A-Side pseudo-elements:** None beyond standard card borders. The visual emphasis is on the 3D transforms.
- **B-Side pseudo-elements:** `.bcard-icon` uses `clip-path: polygon(50% 0%, 100% 25%, 100% 75%, 50% 100%, 0% 75%, 0% 25%)` (line 123) -- a hexagonal shape. Hexagons are strongly associated with isometric design (they tile perfectly in isometric space). Excellent detail.
- **Hard offset shadows (B-Side):** `box-shadow: 6px 6px 0 #36a89f, -6px 6px 0 rgba(0,0,0,0.15)` (line 100). Two shadows -- right-bottom in a darker shade of the card color, and left-bottom in black. This creates a convincing isometric "side face" on each card.
- **Isometric CSS transform (A-Side):** `rotateX(55deg) rotateZ(-45deg)` (line 33) is close to the standard isometric projection (typically 60deg X, -45deg Z). The 55deg is slightly off-standard but creates an acceptable visual.
- **Card hover (A-Side):** `translateY(-4px) translateX(-4px); box-shadow: 8px 8px 0 rgba(78,205,196,0.15)` (line 51) -- lifts the card "up" in isometric space and extends the shadow. Precise and authentic.
- **Button border-radius 0px (B-Side):** `.bbtn` has `border-radius: 0px` (line 92). Sharp corners reinforce the geometric, block-like isometric aesthetic.

### Animations
- **@keyframes defined:** None on either side. The style relies on CSS transforms and transitions.
- **Transitions:** A-Side cards use `transition: transform 0.3s, box-shadow 0.3s` (line 49). B-Side cards `transition: transform 0.2s` (line 100). Hero button has `transition: all 0.3s` (line 29).
- **Motion appropriateness:** Isometric design is typically static and illustrative, so the lack of keyframe animations is acceptable. The hover transforms (lift + shadow extend) are the right type of motion -- they reinforce the 3D spatial metaphor without being distracting.

### Content
- **Brand names:** "IsoMetric" (A-Side, line 135), "ISO" (B-Side, line 178). Both are clear and direct.
- **Tagline:** "Build in Three Dimensions" (line 144) -- direct reference to the isometric projection.
- **Hero copy:** "Isometric Vision. 3D blocks showing top and side faces simultaneously." (B-Side) -- technically accurate description of isometric projection.
- **Card content:** "Teal Platform", "Coral Tower", "Sky Bridge" (A-Side); "Teal Blocks", "Coral Accents", "Precise Angles" (B-Side). Both use building/construction vocabulary that maps to the isometric world-building metaphor.
- **Metrics:** "60 deg Rotate X", "-45 deg Rotate Z", "3D Blocks", "Infinity Axes" (line 181). These are the literal CSS transform values for isometric projection used as content metrics. Very on-brand.
- **Quote:** "Technical precision meets playful color. Isometric illustration come to life." -- "Isometric Arts Collective". Minor grammar: "come" should be "comes".

### Specific Fix Recommendations
1. **Card text on colored backgrounds fails contrast.** `rgba(0,0,0,0.6)` on `#4ECDC4` yields approximately 3.4:1. Darken to `rgba(0,0,0,0.75)` or use `#1A1A2E` for reliable 4.5:1+.
2. **Duplicate font loading.** Space Grotesk is loaded twice -- once at line 8 (`400;500;700`) and again at line 128 (`400;500;600;700`). Remove the duplicate at line 128.
3. **Duplicate CSS rules at line 125.** The `.bcard:nth-child(2)`, `.bcard:nth-child(3)`, and `.bcard p` color rules are fully duplicated from lines 117-121. Remove the block at line 125.
4. **A-Side isometric angle should be 60deg, not 55deg.** Standard isometric projection uses `rotateX(60deg) rotateZ(-45deg)` for equal 120-degree angles between axes. Changing from 55 to 60 on line 33 would make the projection mathematically correct.
5. **B-Side needs an isometric visual element.** The A-Side has the `.iso-grid` with rotated blocks; the B-Side has no equivalent 3D illustration. Add a decorative isometric grid or block arrangement, even if purely CSS, to establish the visual identity beyond flat colored cards.
6. **Fix the quote grammar:** "Isometric illustration come to life" should be "Isometric illustration comes to life" (or "Isometric illustrations come to life").

---

## Gen Z Chaos
**Style Authenticity Score: 9/10**

### Fonts
- **A-Side:** Three fonts loaded via Google Fonts (line 8):
  - Bungee Shade -- decorative, dimensional display face used for h1 (line 27). Chunky, shadow-built-in, extremely loud. Perfect for Gen Z chaos.
  - Space Grotesk (400, 700) -- geometric sans body text.
  - Permanent Marker -- handwritten/marker feel used for stickers (line 26) and section labels (line 39). Adds raw, DIY energy.
- **B-Side:** Space Grotesk with Inter fallback (line 75). Also loaded separately at line 126 with weights 500-800.
- **Appropriateness:** The A-Side font combination is outstanding. Bungee Shade is the visual equivalent of screaming -- its 3D shadow effect creates maximum visual impact. Permanent Marker adds the handmade, meme-sticker quality. The B-Side downgrade to only Space Grotesk loses the chaotic typographic energy -- it should retain at least one display font.

### Colors
- **A-Side palette (CSS variables, line 11):**
  - `--magenta: #FF00FF` (pure magenta)
  - `--lime: #00FF00` (pure lime green)
  - `--yellow: #FFFF00` (pure yellow)
  - `--hot-pink: #FF3366` (hot pink)
  - `--cyan: #00CCFF` (electric cyan)
  - `--dark: #1A0A2E` (deep purple-black background)
- **B-Side palette:**
  - Background: `#000000` (pure black)
  - Primary accent: `#FF00FF` (magenta -- carried over)
  - Card borders: `#00FF00` (lime), `#FFFF00` (yellow), `#00CCFF` (cyan)
  - Card shadows: `#FFFF00`, `#00CCFF`, `#FF00FF`, `#00FF00` -- each card uses a different clashing pair
  - Muted text: `#AAAAAA`
  - Section borders: `3px solid #00CCFF` (line 91)
- **Contrast ratios:** Magenta `#FF00FF` on `#000000` is approximately 3.9:1 -- fails AA for normal text (but Gen Z chaos deliberately violates readability norms). Lime `#00FF00` on black is approximately 8.2:1 -- passes. Yellow `#FFFF00` on black is approximately 18:1 -- excellent. `#AAAAAA` on black is approximately 6.9:1 -- passes AA.
- **Palette accuracy:** Flawless. These are the pure, fully-saturated neon values (0 or FF on each channel) that define Gen Z visual culture. The deliberate use of clashing colors, multiple neon hues in a single view, and maximum saturation is exactly what this style demands. The color combinations intentionally violate traditional harmony rules.

### Layout
- **A-Side hero:** Centered, `padding: 28px 20px 36px`, `text-align: center`. Nav links are pill-shaped buttons with different neon backgrounds, each randomly rotated (`rotate(-3deg)`, `rotate(2deg)`, etc., lines 21-24). Floating emoji elements are absolutely positioned. The layout itself is intentionally unstructured -- center-stacked chaos.
- **A-Side components:** `padding: 24px 20px`, no max-width. Full-width chaos.
- **B-Side:** Standard layout with `.bcon` at `max-width: 1100px`. Cards use `border: 3px solid` with different neon colors per card (lines 113-117). Bold `3px` section borders in cyan (line 91). More structured than the A-Side, but the thick neon borders and hard-offset colored shadows maintain the energy.
- **Responsive:** B-Side has 768px breakpoint. A-Side nav is flexible with `flex-wrap: wrap`.

### Sizing
- **A-Side typography scale:**
  - h1: `32px` Bungee Shade (line 27)
  - Sticker: `14px` Permanent Marker (line 26)
  - Subtitle: `14px` (line 28)
  - Section labels: `16px` Permanent Marker (line 39)
  - Buttons: `12px` (line 41)
  - Card h3: `16px` (line 49)
  - Card p: `12px` (line 50)
  - CTA: `15px` (line 30)
  - Nav links: `11px` (line 20)
- **B-Side typography scale:**
  - h1: `clamp(3rem, 10vw, 6rem)` (line 119) -- significantly larger than other B-Sides. At maximum, 6rem (96px). This is intentionally oversized.
  - h2: `1.8rem` (line 94)
  - Body: `0.88rem` (line 99)
  - Buttons: `0.9rem` (line 88)
  - Metric values: `2.2rem` (line 102)
- **Weight:** B-Side h1 is `font-weight: 900` (line 119), buttons have `border: 3px solid` (line 118). Everything is heavy, thick, and aggressive. Appropriate for the maximalist aesthetic.

### Sections
- **Current sections (B-Side):** Header, Hero, Feature Cards, Metrics, Quote, Footer.
- **Effectiveness:** The B-Side execution is strong. Cards have different neon border colors and clashing shadow colors (lines 113-117). The hero heading is oversized with a cycling glow animation (`chaosGlow`, line 120). Section dividers are thick `3px solid #00CCFF` (line 91) instead of subtle hairlines. Metrics use ironic/absurdist values ("0 Rules", "Infinity Chaos", "100% Volume", "NOW When") that nail the Gen Z tone.
- **What would better demonstrate this style:**
  - Randomly rotated elements (the A-Side nav pills are rotated; the B-Side is entirely grid-aligned)
  - Emoji/sticker overlays scattered across sections
  - A meme-style image or text block with ironic humor
  - Intentionally "broken" layout elements (overlapping boxes, text outside containers)
  - A marquee or scrolling text ticker with chaotic phrases

### Visuals
- **A-Side pseudo-elements:**
  - `body::before` (lines 14-17): Fixed overlay with three radial gradients in magenta, lime, and cyan creating a hazy neon atmosphere across the entire page.
  - `.card::before` (line 48): "FIRE" label in hot pink, absolutely positioned at top-right. Sticker-like badge using Permanent Marker font.
- **B-Side pseudo-elements:** None beyond the standard structure.
- **Hard offset shadows (B-Side):** Cards use `box-shadow: 6px 6px 0 [color]` with deliberately mismatched neon colors per card. Card 1: magenta border + cyan shadow. Card 2: yellow border + magenta shadow. Card 3: cyan border + lime shadow. Each combination clashes intentionally -- this is core Gen Z visual language.
- **Floating elements (A-Side):** Sparkle, fire, rocket emojis (lines 132-134) with `float` animation bouncing them up and down. Standard Gen Z "sticker dump" aesthetic.
- **Glow effects:** A-Side buttons have `box-shadow: 0 0 15px` in their respective neon colors. CTA pulses with magenta glow. B-Side hero heading has `chaosGlow` cycling between magenta and green text-shadow. All authentic for the neon-heavy style.

### Animations
- **@keyframes defined (A-Side):**
  - `pulse` (line 32): Scale-based box-shadow expansion on CTA button, 2s infinite. Attention-grabbing, urgent.
  - `float` (line 37): TranslateY 0 to -10px with rotation 0 to 10deg, 4s ease infinite. Used on floating emoji elements. Chaotic, playful.
- **@keyframes defined (B-Side):**
  - `chaosGlow` (line 120): Alternates between magenta text-shadow and lime/cyan text-shadow on the hero h1, 2s infinite. This is excellent -- the color-cycling glow is a signature Gen Z visual effect.
- **Transitions:** Buttons scale + rotate on hover (`scale(1.1) rotate(-2deg)`, line 42). Nav pills scale + un-rotate on hover (line 25). Aggressive, snappy 0.15s timing.
- **Motion appropriateness:** Strong. Gen Z chaos demands constant, attention-grabbing motion. The pulse, float, glow-cycle, and snappy hover transforms all contribute to sensory overload, which is the point. Could be pushed further with scroll-triggered animations or random position shifts.

### Content
- **Brand names:** No traditional brand name on the A-Side; nav items are "Vibes", "Chaos", "Drop", "Slay". B-Side uses "CHAOS" (line 176). Anti-brand branding -- authentic.
- **Sticker text:** "no cap fr fr" (line 141) -- genuine Gen Z slang.
- **Hero copy:** "MAIN CHARACTER ENERGY" (A-Side, line 142) and "BREAK EVERYTHING." (B-Side, line 177) -- both capture the self-assured, irreverent tone perfectly.
- **Subtitle:** "the internet is unhinged and we love it" (line 143) -- lowercase, casual, authentic Gen Z voice.
- **B-Side card descriptions:** All caps, deliberately aggressive: "SCREAMING, VIBRATING, IN-YOUR-FACE MAGENTA. DEAL WITH IT." -- this is exceptional content writing for the style. It mirrors the visual intensity.
- **Metrics:** "0 Rules / Infinity Chaos / 100% Volume / NOW When" -- absurdist, ironic, exactly right.
- **Quote:** "THE VISUAL EQUIVALENT OF SCREAMING INTO THE VOID AND HEARING IT SCREAM BACK IN NEON." attributed to "NOBODY" (line 180) -- all-caps, self-aware, anti-authority attribution. Perfect.

### Specific Fix Recommendations
1. **B-Side needs more visual chaos.** It is currently the most "orderly" version of Gen Z chaos -- perfectly aligned grid, consistent spacing, no rotation or overlap. Add random `transform: rotate()` values to cards (e.g., `-2deg`, `1deg`, `-3deg`), and consider breaking the grid alignment slightly with negative margins or overlapping elements.
2. **B-Side should use Bungee Shade or Permanent Marker for the hero heading.** The current Space Grotesk at 900 weight is bold but not chaotic enough. The A-Side's Bungee Shade is the typographic embodiment of Gen Z maximalism.
3. **Magenta `#FF00FF` on `#000000` is 3.9:1.** While this style intentionally pushes readability limits, the primary accent failing AA is a concern for body text. For paragraphs, use `#AAAAAA` (which passes at 6.9:1). Reserve magenta for headings, labels, and decorative elements where large text (3:1 threshold) applies.
4. **Add floating/scattered emoji elements to the B-Side.** The A-Side has floating sparkle/fire/rocket emojis. The B-Side has none. Scatter 4-5 fixed-position emojis with random rotation and float animations to inject visual noise.
5. **Duplicate CSS block at line 123.** The entire set of card color overrides, button borders, and hero heading overrides from lines 113-119 is duplicated. Remove line 123.
6. **B-Side missing the background neon glow overlay.** The A-Side has `body::before` with radial neon gradients creating atmospheric haze. Add a similar fixed overlay to `.b-side` to establish the neon environment rather than using flat `#000000` black.

---

## Cross-Cutting Observations

### B-Side Template Uniformity
All five B-Sides share an identical structural skeleton: sticky header with logo + nav links, 80vh centered hero with tag/h1/p/buttons, feature cards in a 3-column grid, metrics in a 4-column grid, centered quote with blockquote/cite, and a standard footer. The CSS class naming (`.bh`, `.bhero`, `.bsec`, `.bcon`, `.bgrid`, `.bcard`, `.bmets`, `.bmet-v`, `.bquote`, `.bfoot`) is identical across all files. While this ensures consistency, it means the B-Sides differentiate only through color, font, and minor CSS effects. The A-Sides are significantly more unique and style-authentic because their structure varies per style.

### Recurring Issues
1. **Duplicate CSS rules.** Every B-Side in this batch has at least one block of duplicate rules appended at the end of the stylesheet. This appears to be a generation artifact.
2. **Muted text contrast.** Four of five files have muted text colors that fail WCAG AA on their respective backgrounds. This is the most common accessibility issue.
3. **Missing font loading for B-Sides.** Scratch-card B-Side references Inter but does not load it. Lenticular B-Side references Inter but only loads it from the A-Side link tag (which works but is fragile).
4. **A-Side vs B-Side authenticity gap.** In every case, the A-Side is more visually authentic to the named style than the B-Side. The A-Sides have custom layouts, unique visual techniques, and style-specific interactions. The B-Sides rely on the shared template with surface-level theming.

### Strongest Execution
**Gen Z Chaos** scores highest (9/10) because both the A-Side and B-Side commit fully to the aesthetic -- oversized type, neon clashing colors, ironic content, aggressive weight, anti-design decisions. The style is inherently about breaking rules, and the implementation follows through.

### Weakest Execution
**Lenticular** scores lowest (6/10) because the defining visual feature -- the ribbed surface overlay that creates angle-dependent image shifting -- is only present on the A-Side hero. The B-Side has minimal tilt transforms and zero stripe overlay or content-swap mechanics. Without these, it reads as a generic dark landing page with purple accents.

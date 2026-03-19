# Audit Report -- Batch 03: Surface & Material Morphism Styles

**Date:** 2026-03-20
**Auditor:** UI Designer Agent
**Scope:** Full file audit (A-side component showcase + B-side landing page) for 5 surface/material styles
**Files:** `glassmorphism.html`, `neumorphism.html`, `claymorphism.html`, `skeuomorphism.html`, `candy-ui.html`

---

## Glassmorphism

**Style Authenticity Score: 8/10**

### Fonts
- **Family:** Inter, loaded via Google Fonts (`https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700`)
- **Weights:** 400, 500, 600, 700
- **Loading method:** External `<link>` in `<head>` (line 8)
- **Appropriateness:** Good. Inter is a clean, geometric sans-serif that does not compete with the glass effects. It is the same font Apple uses in many of their glassmorphism-adjacent interfaces. The B-side explicitly declares `font-family:'Inter',system-ui,sans-serif` (line 247), which is correct.

### Colors
- **Background gradient:** `linear-gradient(135deg, #667eea 0%, #764ba2 50%, #f093fb 100%)` (line 14, repeated in B-side line 247) -- vibrant purple-pink gradient, excellent for glassmorphism since it provides the colorful substrate that shows through frosted panels
- **Glass panel fill:** `rgba(255,255,255,0.12)` (line 38) and `rgba(255,255,255,0.10)` (B-side `.bcard`, line 268) -- properly translucent
- **Border color:** `rgba(255,255,255,0.2)` (line 41) and `rgba(255,255,255,0.18)` (B-side `.bcard`, line 268) -- correct thin light border
- **Text:** `#FFFFFF` for primary, `rgba(255,255,255,0.75)` for body, `rgba(255,255,255,0.65)` for muted (B-side)
- **Orb colors:** `#667eea`, `#f093fb`, `#764ba2` (lines 33-35) -- reusing gradient stops for floating orbs is smart
- **Contrast ratios:** White text on the gradient background is variable. On the `#764ba2` midpoint, pure white achieves approximately 6.5:1 (passes AA). The `rgba(255,255,255,0.65)` muted text is weaker at roughly 3.5:1, which fails WCAG AA for body text.
- **Accent usage:** No distinct accent color -- the style relies on the gradient background itself and white-at-various-opacities, which is authentic to glassmorphism.

### Layout
- **A-side hero:** `min-height: 70vh`, padded `1.5rem 2rem 3rem`, flex column layout. Hero content constrained to `max-width: 480px` (line 87). Left-aligned, which is fine.
- **B-side hero:** `min-height: 80vh`, centered (`text-align: center`, flex center), inner content `max-width: 640px` (line 255). This centered layout is more appropriate for a landing page.
- **Section spacing:** B-side sections use `padding: 5rem 2rem` (line 263), content constrained to `max-width: 1100px` (line 264). Good spacing.
- **Card grid:** `grid-template-columns: repeat(auto-fit, minmax(280px, 1fr))` with `gap: 1.5rem` (line 267). Responsive and appropriate.
- **Responsive:** Mobile breakpoint at `768px` (line 292) hides nav, reduces hero to `60vh`, collapses grid to `1fr`, metrics to `2-col`. Adequate but only one breakpoint.

### Sizing
- **Typography scale (A-side):** h1 `2.6rem` (line 89), h2 `1.2rem` (line 139), h3 `0.7rem` (line 146), body `1rem` (line 95), nav links `0.85rem` (line 81)
- **Typography scale (B-side):** h1 `clamp(2.5rem, 6vw, 4rem)` (line 257), section heading `1.8rem` (line 266), card heading `1.05rem` (line 270), body `0.88rem` (line 271), metric value `2.2rem` (line 274)
- **Padding:** Cards `2rem` (line 268), sections `5rem 2rem`, buttons `0.8rem 2rem` (line 260)
- **Element proportions:** Card icons `40px` square with `16px` border-radius (line 272). Well-proportioned.

### Sections
- **Current sections:** Hero with tag/headline/description/CTAs, features grid (3 cards with icons), metrics (4 stats), quote, footer. This is a solid standard landing page structure.
- **Do they serve the style well?** Mostly yes. The feature cards with `backdrop-filter: blur(16px)` and translucent backgrounds are the right showcase. The metrics section and quote section also gain glass treatment in the B-side.
- **What would better demonstrate this style?** An overlapping panel composition where multiple glass layers are visibly stacked at different z-depths with the gradient showing through gaps between them. A floating modal or dialog preview would also be powerful. A "glass card over image" section would demonstrate the blur effect more dramatically than glass-over-gradient.

### Visuals
- **Pseudo-elements:** B-side uses `::before` and `::after` on `.b-side` (lines 289-290) to create fixed position radial-gradient orbs (`350px` and `300px`) with `filter: blur(40px)`. These serve as the floating color blobs behind glass panels. Good.
- **Clip-paths:** None used
- **Overlays:** None explicit; the glass panels themselves serve as overlays on the gradient
- **Background treatments:** A-side uses `.bg-orbs` with three absolutely positioned blurred circles (lines 20-35). B-side replicates this with pseudo-elements. The main background gradient `linear-gradient(135deg, #667eea, #764ba2, #f093fb)` is correct and vibrant.
- **A-side additionally has:** Card header with a gradient fill (`rgba(102,126,234,0.4)` to `rgba(240,147,251,0.4)`, line 193) and palette swatches (lines 358-364)

### Animations
- **@keyframes:** None defined. This is acceptable -- glassmorphism does not require animation.
- **Transitions:** All hover transitions use `0.2s` ease (buttons, nav links, cards). Cards get `translateY(-3px)` on hover (line 269). Buttons get `translateY(-1px)` (line 261).
- **Motion appropriateness:** The subtle hover lifts are appropriate. A slow floating animation on the background orbs would add dynamism without being distracting, but its absence is not a deficiency.

### Content
- **Brand names:** A-side "Frost" (line 310), B-side "Prism" (line 369). Both are evocative of light and transparency -- excellent choices.
- **Taglines:** A-side "See through the interface" (line 319), B-side "See through the layers" / "Layers of Pure Light" (line 370). Strong, style-relevant language about transparency and light.
- **Hero copy:** "Design between the transparent and the translucent. Every surface reveals and conceals in perfect balance." -- directly addresses the glassmorphism concept of layered transparency.
- **Card titles:** "Frosted Depth," "Light Play," "Blur Engine" (line 371) -- all directly reference glassmorphism techniques. Good.
- **Metrics:** "50K+ Designers," "2M Components," "99.9% Uptime," "4.9 star Rating" (line 372) -- generic SaaS metrics, not style-specific but acceptable for a demo.
- **Quote:** "The most beautiful design tool I have ever used. Every surface feels alive and responsive." -- somewhat generic but acceptable.

### Specific Fix Recommendations
1. **Muted text contrast failure.** The `rgba(255,255,255,0.65)` used for body text, card descriptions, nav links, and footer links (B-side lines 258, 271, 278, 282-284) fails WCAG AA contrast against the gradient background. Raise to `rgba(255,255,255,0.78)` minimum, or use a text-shadow `0 0 8px rgba(0,0,0,0.2)` to improve legibility.
2. **Duplicate CSS rules.** Lines 285-288 and 293 are exact duplicates of rules already defined earlier. `.bbtn-p`, `.bbtn-s:hover`, and `.bquote` are redefined with the same values, adding ~400 bytes of dead weight. Remove the duplicates.
3. **Missing frosted-glass treatment on the quote block (A-side).** The A-side has no quote/testimonial section. The B-side quote gets a glass treatment (`background: rgba(255,255,255,0.06); backdrop-filter: blur(12px)`, line 288), but the A-side component showcase does not demonstrate a glassmorphic quote/testimonial component.
4. **Background orbs are static.** The fixed-position `::before` / `::after` orbs never move. Adding a slow `@keyframes drift` animation (translating 20-30px over 8-10 seconds) would make the background feel more alive and better demonstrate the glass effect as background content shifts beneath panels.
5. **No visible layering or stacking of glass panels.** The defining visual trick of glassmorphism is seeing one glass panel overlapping another with the background visible behind both. Currently, all cards are in a grid with no overlap. Consider adding an overlapping card composition or a hero section with stacked offset panels.

---

## Neumorphism

**Style Authenticity Score: 8/10**

### Fonts
- **Family (A-side):** Inter via Google Fonts (line 8). **Family (B-side):** Poppins via Google Fonts (line 295), declared as `'Poppins', system-ui, sans-serif` (line 247)
- **Weights:** A-side Inter 400-700, B-side Poppins 400-700
- **Loading method:** A-side loads Inter via `<link>` in head (line 8). B-side loads Poppins via a *second* `<link>` placed *after* the closing `</style>` tag (line 295), which is syntactically valid but unusual.
- **Appropriateness:** Inter is appropriate for the component showcase. Poppins is a reasonable alternative with its slightly rounder letterforms, which suits neumorphism's soft personality. Both are acceptable, though Inter is the more canonical choice for this style.

### Colors
- **Background:** `#E0E5EC` (line 11, B-side line 247) -- this is THE canonical neumorphism background color. Perfect.
- **Dark shadow:** `#a3b1c6` (line 16, B-side line 268 as `rgba(163,177,198,0.5)`) -- correct paired shadow for `#E0E5EC`
- **Light shadow:** `#ffffff` (line 16, B-side line 268 as `rgba(255,255,255,0.7)`) -- correct highlight
- **Accent:** `#6B7FD7` (A-side, line 50) / `#6D5DFC` (B-side, line 250) -- soft purple, tasteful and restrained
- **Text colors:** `#2D3748` for headings, `#718096` for body, `#A0AEC0` for labels (lines 73, 77, 140)
- **Contrast ratios:** `#2D3748` on `#E0E5EC` gives approximately 5.8:1 (passes AA). `#718096` on `#E0E5EC` gives approximately 3.2:1 (fails AA for body text but passes for large text). `#6D5DFC` on `#E0E5EC` gives approximately 3.6:1 (passes AA for large text only).
- **Surface matching:** Body background and card/button backgrounds are both `#E0E5EC` (line 156 for buttons, line 268 for B-side cards). This is the critical neumorphism rule -- elements are extruded from the surface, not placed on it.

### Layout
- **A-side hero:** `min-height: 70vh`, flex column, hero content `max-width: 460px` (line 67). Left-aligned.
- **B-side hero:** `min-height: 80vh`, centered, `max-width: 640px` (line 255).
- **Section spacing:** B-side `5rem 2rem` (line 263), content `max-width: 1100px` (line 264). Generous spacing is appropriate for neumorphism's breathing room.
- **Header:** B-side header uses `box-shadow: 0 4px 12px rgba(163,177,198,0.3)` (line 289) -- this is a standard drop shadow, not a neumorphic dual shadow. Could use the dual-shadow technique here.
- **Responsive:** Single breakpoint at `768px` (line 291) with same pattern as glassmorphism.

### Sizing
- **Typography scale (A-side):** h1 `2.4rem` (line 69), h2 `1.2rem` (line 130), h3 `0.7rem` (line 137), body `0.95rem` (line 77)
- **Typography scale (B-side):** h1 `clamp(2.5rem, 6vw, 4rem)` (line 257), section heading `1.8rem` (line 266), card heading `1.05rem` (line 270), body `0.88rem` (line 271)
- **Border radius:** Cards `16px` (lines 14, 268), buttons `12px` (A-side line 151) / `16px` (B-side line 260), swatches `12px` (line 233). The `16px` is the standard neumorphic radius -- correct.
- **Shadow offsets:** Raised `6px 6px 12px` and `-6px -6px 12px` (line 16). B-side cards use `-6px -6px 14px` and `6px 6px 14px` (line 268). Slightly larger on B-side but within range.

### Sections
- **Current sections:** Hero with tag/headline/CTAs, feature cards (3), metrics (4), quote, footer.
- **Do they serve the style well?** Yes, mostly. The feature card titles ("Dual Shadows," "No Borders," "Pressed States") directly explain neumorphism's visual language. The metrics section is clever: "0px Borders," "2 Shadow Layers," "1 Surface," "Infinity Soft" (line 365). These are educational and on-theme.
- **What would better demonstrate this style?** A toggle switch, slider control, or media player mock-up -- these are the classic neumorphism showcase components. The A-side includes a progress bar (lines 102-122), which is excellent. The B-side lacks interactive component demonstrations. A pressed/inset button state demo or a circular dial would be highly authentic.

### Visuals
- **Pseudo-elements:** Card header `::after` creates a `44px` inset-shadow circle (lines 189-195), simulating a neumorphic circular element. Good detail.
- **Dual shadow system:** Thoroughly implemented. Raised: `6px 6px 12px #a3b1c6, -6px -6px 12px #ffffff`. Inset: `inset 4px 4px 8px #a3b1c6, inset -4px -4px 8px #ffffff`. Both are used consistently on buttons (lines 92-100, 160-172), progress bar (lines 107-122), inputs (lines 221-226), swatches (line 234), and B-side elements.
- **Background treatments:** Flat `#E0E5EC` everywhere -- no gradients, no textures, no patterns. This is exactly correct for neumorphism.
- **B-side card icons:** Use inset shadows `inset -2px -2px 5px rgba(255,255,255,0.7), inset 2px 2px 5px rgba(163,177,198,0.4)` (line 285). Good pressed-in effect.
- **B-side primary button:** Gets neumorphic raised shadow (`-4px -4px 10px rgba(255,255,255,0.7), 4px 4px 10px rgba(163,177,198,0.5)`) and transitions to inset on hover (line 287). This raised-to-pressed interaction is the signature neumorphism behavior.

### Animations
- **@keyframes:** None defined. Appropriate -- neumorphism is a quiet, tactile style with no bouncy or flashy animations.
- **Transitions:** `0.15s` on buttons (line 93 A-side), `0.2s` on hover cards (B-side line 269). The faster `0.15s` gives a snappier press feel, which is good for the "physical button" metaphor.
- **Motion appropriateness:** Correct. The `translateY(-3px)` hover on B-side cards (line 269) is the only motion, and it subtly enhances the extrusion metaphor.

### Content
- **Brand names:** A-side "Soft UI" (line 305), B-side "Soft" (line 362). Direct reference to neumorphism's alternative name (Soft UI). Appropriate.
- **Taglines:** "Interfaces that feel touchable" (line 313), B-side "Extruded from surface" / "Touch the Interface" (line 363). Excellent -- directly communicates the tactile, physical quality.
- **Hero copy:** "Elements rise gently from a single matte surface. Tactile, soft, almost real -- like pressing warm clay." -- vivid and accurate. The "warm clay" comparison nicely bridges to the tactile concept (though it does blur the line with claymorphism).
- **Card titles:** "Dual Shadows," "No Borders," "Pressed States" -- these are literal descriptions of neumorphism's three defining characteristics. Excellent educational content.
- **Quote:** "The best interfaces are the ones you want to reach out and touch." -- attributed to "Ux Collective," a real publication. Strong.

### Specific Fix Recommendations
1. **Body text contrast.** `#718096` on `#E0E5EC` fails WCAG AA at approximately 3.2:1. Darken to `#5A6A7E` (approximately 4.6:1) for body text. Similarly, `#6D5DFC` accent is borderline for non-large text contexts.
2. **Duplicate CSS rules.** Lines 285-289 and 292 contain rules that are exact duplicates of rules defined just lines earlier (`.bcard-icon`, `.bbtn-p`, `.bbtn-p:hover`, `.bbtn-s`, `.bh`). Remove the duplicated block.
3. **Poppins font loaded after style block.** The `<link>` for Poppins (line 295) is placed after the closing `</style>` tag and before `</head>`. While valid, it means the CSS declares `font-family:'Poppins'` before the font is requested. Move the Poppins `<link>` above the `<style>` block to follow standard loading order.
4. **B-side header uses drop shadow instead of neumorphic shadow.** `.bh` uses `box-shadow: 0 4px 12px rgba(163,177,198,0.3)` (line 289) -- a standard one-directional drop shadow. Replace with the dual-shadow system: `box-shadow: -4px -4px 10px rgba(255,255,255,0.7), 4px 4px 10px rgba(163,177,198,0.4)` to maintain style consistency.
5. **Missing interactive component demos in B-side.** Add a toggle switch or slider component to the B-side to showcase the signature pressed/inset interaction that makes neumorphism distinctive. The A-side has a progress bar but the B-side lacks any interactive neumorphic component.

---

## Claymorphism

**Style Authenticity Score: 7.5/10**

### Fonts
- **Family:** Nunito, loaded via Google Fonts (`https://fonts.googleapis.com/css2?family=Nunito:wght@400;600;700;800`)
- **Weights:** 400, 600, 700, 800
- **Loading method:** External `<link>` in `<head>` (line 8)
- **Appropriateness:** Excellent. Nunito's rounded terminals and soft letterforms are one of the most fitting choices for claymorphism. The 800 weight is used prominently (logo, h1, buttons), giving that chunky, extruded-clay text feel. The B-side correctly declares `font-family:'Nunito','Inter',sans-serif` (line 266).

### Colors
- **Background:** `#F0E6FF` (line 11) -- soft pastel lavender. B-side adds a tri-color gradient: `linear-gradient(180deg, #F0E6FF 0%, #FFE4F0 50%, #E0F4FF 100%)` (line 266) -- lavender to pink to blue. Beautiful pastel range.
- **Primary clay surfaces (A-side):** `linear-gradient(145deg, #F5EDFF 0%, #E8D8FF 100%)` (line 14) -- subtle gradient suggesting 3D matte surface
- **B-side card colors:** Card 1 `#FFE4F0` (pink), Card 2 `#E0F4FF` (blue), Card 3 `#E0FFE8` (green) with matching tinted borders and icon backgrounds (lines 287, 304-307). Multi-colored pastels are very on-brand.
- **Accent:** `#6B3FA0` deep purple (A-side logo, line 39), `#A78BFA` medium purple (B-side, line 269), `#EC4899` pink for card icons (line 291)
- **Decorative blob colors (A-side):** Pink `#FFB8D0/#FF9A9E`, green `#B8F0C8/#82E89E`, blue `#B8D8FF/#82B4FF`, yellow `#FFEAB8/#FFD682` (lines 121-124) -- a full pastel rainbow
- **Contrast ratios:** `#3D2C5E` on `#F0E6FF` gives approximately 8.2:1 (excellent). `#7B5EA7` on `#F0E6FF` gives approximately 3.4:1 (borderline). `#A78BFA` on pastel backgrounds is variable and may fall below 3:1 in some combinations.

### Layout
- **A-side hero:** `min-height: 70vh`, flex column, `max-width: 460px` (line 66). Includes decorative clay blobs below the CTA.
- **B-side hero:** `min-height: 80vh`, centered, `max-width: 640px` (line 274).
- **Section spacing:** `5rem 2rem` (line 282), `max-width: 1100px` (line 283). Good.
- **Card grid:** Same `repeat(auto-fit, minmax(280px, 1fr))` pattern (line 286).
- **Responsive:** Single `768px` breakpoint (line 310).

### Sizing
- **Typography scale (A-side):** h1 `2.5rem` (line 68), h2 `1.3rem` (line 131), h3 `0.75rem` (line 139), body `0.95rem` (line 77)
- **Typography scale (B-side):** h1 `clamp(2.5rem, 6vw, 4rem)` (line 276), section heading `1.8rem` (line 285), card heading `1.05rem` (line 289)
- **Border radius:** `.clay` class uses `24px` (line 15). B-side cards `24px` (line 287). B-side buttons `20px` (line 308, overriding the initial `24px` from line 279). Card icons `24px` (line 291). These generous radii are correct for the inflated, puffy claymorphism look.
- **Shadow complexity (A-side `.clay`):** Four-layer shadow -- `inset 0 -4px 6px rgba(0,0,0,0.06)` (bottom inner shadow), `inset 0 4px 6px rgba(255,255,255,0.6)` (top inner highlight), `8px 8px 20px rgba(100,70,150,0.15)` (outer colored shadow), `-4px -4px 12px rgba(255,255,255,0.7)` (outer light lift). This is the signature claymorphism formula.

### Sections
- **Current sections:** Hero with tag/headline/CTAs, feature cards (3), metrics (4), quote, footer.
- **Do they serve the style well?** The feature cards with their individual pastel colors (pink, blue, green) and `inset 0 -4px 8px rgba(0,0,0,0.04)` bottom shadow (line 287) create a nice clay-like feel. Card titles ("Puffy Forms," "Pastel Clay," "Molded Depth") directly describe the aesthetic.
- **What would better demonstrate this style?** Overlapping cards with slight `transform: rotate(-2deg)` tilts, which is called out in the visual DNA as a signature technique. A 3D clay-figure illustration placeholder or a stacking/layering demo would heighten the playful, physical quality. Toggle switches or pill-shaped tags with the clay treatment would also demonstrate versatility.

### Visuals
- **Pseudo-elements:** A-side card header `::after` creates a `48px` element with gradient and inset shadows (lines 197-205). Good.
- **Clay blob decorations (A-side):** Four decorative shapes (lines 113-124) with varying shapes (rounded-rectangle vs circle), sizes (56px vs 42px), and colors. Each has the triple-shadow clay treatment. Adds playfulness.
- **B-side card differentiation:** Each of the three cards has a unique pastel background and matching icon color (lines 287, 304-307). This multi-color approach is very authentic to claymorphism.
- **Background treatments:** B-side uses a full-height gradient (`#F0E6FF` to `#FFE4F0` to `#E0F4FF`, line 266) that subtly shifts hue. No textures or patterns, which is correct -- claymorphism is smooth and matte.
- **B-side button shadow:** `.bbtn-p` gets `box-shadow: 0 6px 20px rgba(167,139,250,0.2), inset 0 -3px 6px rgba(0,0,0,0.04)` (line 309). The colored outer glow + inner bottom shadow is the correct clay formula.

### Animations
- **@keyframes:** None in A-side. B-side: none defined.
- **Transitions:** `0.2s` on all interactive elements. Cards get `translateY(-3px)` on hover. Buttons get `translateY(-1px)`.
- **Motion appropriateness:** Claymorphism could benefit from a subtle `bounce` or `squish` animation on buttons (scale down slightly on press, overshoot on release). The current transitions are adequate but miss an opportunity for playful interaction.

### Content
- **Brand names:** A-side "Claykit" (line 322), B-side "Squishy" (line 380). Both evoke the tactile, moldable quality of clay. "Squishy" is particularly fun.
- **Taglines:** "Soft, squishy, and delightful" (line 331), B-side "Playfully molded" / "Soft, Puffy & Delightful" (line 381). Captures the personality perfectly.
- **Hero copy:** "Every element sculpted from pastel-colored clay. Inflated, rounded, and irresistibly touchable." -- vivid sensory language that is very on-brand.
- **Card titles:** "Puffy Forms," "Pastel Clay," "Molded Depth" (line 382) -- descriptive of the style's defining traits.
- **Metrics:** "Infinity Squishy," "24px Radius," "100% Soft," "3 Pastels" (line 383) -- self-referential and playful. The `24px Radius` value is a nice technical Easter egg.
- **Quote:** "I just want to reach in and squish every button. This is the happiest UI I have ever seen." -- attributed to "Design Milk." Perfectly captures the intended emotional response.

### Specific Fix Recommendations
1. **Missing card tilt/rotation.** The visual DNA specifies `transform: rotate(-2deg)` as a signature claymorphism technique for playful card arrangements. Currently all cards sit flat in the grid with no rotation. Add alternating slight rotations (e.g., `-1.5deg`, `1deg`, `-0.5deg`) to the three B-side cards.
2. **B-side cards missing top inner highlight.** A-side `.clay` has `inset 0 4px 6px rgba(255,255,255,0.6)` for the top light source. B-side `.bcard` only has `inset 0 -4px 8px rgba(0,0,0,0.04)` (bottom shadow) without the matching top highlight. Add `inset 0 4px 8px rgba(255,255,255,0.5)` to `.bcard` to complete the clay surface illusion.
3. **Duplicate CSS rules.** Lines 304-307 are duplicated at line 311. Remove the duplicate block.
4. **Secondary text contrast.** `#8B7FB5` on the varying pastel backgrounds (especially `#FFE4F0` and `#E0F4FF`) may not consistently meet WCAG AA. Test each card's description color against its specific background and darken where needed.
5. **Missing squish animation on buttons.** Add a `:active` state with `transform: scale(0.96)` and a slight transition overshoot (`transition: transform 0.15s cubic-bezier(0.34, 1.56, 0.64, 1)`) to give buttons the "squished" feeling the brand name promises.

---

## Skeuomorphism

**Style Authenticity Score: 8.5/10**

### Fonts
- **Family (A-side):** Roboto (body) and Georgia (headings), loaded via Google Fonts (line 8: `family=Georgia&family=Roboto:wght@400;500;700`)
- **Family (B-side):** Georgia as primary, declared as `'Georgia','Times New Roman',serif` (line 290)
- **Weights:** Roboto 400/500/700, Georgia default
- **Loading method:** External `<link>` in `<head>`
- **Appropriateness:** Excellent. Georgia as the serif heading font evokes print and physicality -- perfect for skeuomorphism. Roboto as a body font provides legibility. The B-side going full-serif with Georgia is a bold but appropriate choice that pushes the "print/physical" metaphor further.

### Colors
- **A-side hero:** Dark leather tones via `linear-gradient(180deg, #5A4A3A 0%, #3D2E22 100%)` (line 32)
- **A-side components section:** Warm parchment `linear-gradient(180deg, #D4C4A8 0%, #C8B898 100%)` (line 148) with micro-stripe texture overlay
- **Body background:** `#8B7355` with vertical micro-stripe texture (lines 13-23) -- warm wood/leather tone
- **B-side background:** `#FAF0E6` (linen) with horizontal micro-stripe texture `repeating-linear-gradient(0deg, transparent, transparent 3px, rgba(0,0,0,0.012) 3px, rgba(0,0,0,0.012) 4px)` (line 290). The linen color name itself is a skeuomorphic reference.
- **B-side header:** Rich brown gradient `linear-gradient(180deg, #5C3D2E, #3C2415)` (line 292) -- leather/wood strip
- **Accent colors:** Gold/brass `#C0A060`, `#8B7340` (line 101 A-side), saddlebrown `#8B4513` (B-side line 299)
- **Metal tones:** `#C0C0C0` to `#808080` gradient on logo (line 53)
- **Text colors:** `#E8D5BA` warm cream for hero text (line 89), `#2C1810` rich dark brown for body (line 23), `#B09A7C` for secondary text (line 94), `#D4B896` warm tan for decorative text
- **Contrast ratios:** `#2C1810` on `#FAF0E6` gives approximately 11.8:1 (excellent). `#8B7355` on `#FAF0E6` gives approximately 3.3:1 (borderline). `#FAF0E6` on `#3C2415` gives approximately 9.5:1 (excellent).

### Layout
- **A-side hero:** `min-height: 70vh`, dark leather gradient background with bottom border `3px solid #1A120B` and inset highlight shadow (line 33-34). `max-width: 460px` content area.
- **B-side hero:** `min-height: 80vh`, centered, `max-width: 640px`.
- **Section dividers:** B-side uses `border-top: 1px solid #D4C4B0` (line 306) and footer `border-top: 1px solid #D4C4B0` (line 322). Physical dividers are appropriate for skeuomorphism.
- **B-side header:** Has a thick `border-bottom: 2px solid #2C1810` (line 292) -- adds weight and physicality.

### Sizing
- **Typography scale (A-side):** h1 `2.2rem` (line 85), h2 `1.3rem` (line 154), h3 `0.7rem` (line 162), body `0.95rem` (line 93)
- **Typography scale (B-side):** h1 `clamp(2.5rem, 6vw, 4rem)` (line 300), section heading `1.8rem` (line 309), card heading `1.05rem` (line 313)
- **Border radius:** A-side `6px` for buttons (line 108), `8px` for cards (line 210), `6px` for inputs (line 254). B-side `8px` for cards (line 311) and buttons (line 303). Small, precise radii are correct for skeuomorphism -- it mimics real-world manufacturing constraints where materials cannot bend to extreme curves.
- **Border widths:** Generous use of 1-3px borders throughout. `1px solid #B8A88A` on cards (line 212), `2px solid #8B7A65` on outline buttons (line 201), `3px solid #1A120B` on hero bottom (line 33). These thicker borders add a sense of physical construction.

### Sections
- **Current sections:** Hero with headline/CTAs, feature cards (3), metrics (4), quote, footer.
- **Do they serve the style well?** The card content ("Rich Textures," "3D Bevels," "Material Truth") is highly relevant. The metrics section ("100% Textured," "4 Materials," "3D Depth," "Real Touch") is educational and on-brand.
- **What would better demonstrate this style?** A toolbar strip with icon buttons resembling physical toggle/dial controls. A leather-textured sidebar or notepad component. A settings panel with physical toggle switches. The A-side leather strip with stitching (lines 123-143) is an excellent skeuomorphic element -- the B-side needs similar texture elements.

### Visuals
- **Pseudo-elements:** A-side card header `::after` creates a `48px` metallic circle with gradient, border, and multi-layer shadow (lines 226-233). B-side `.bcard::before` creates a `3px` gradient strip across the top of each card (line 332), simulating a decorative trim or inlay.
- **Textures:** Body has vertical micro-stripes (line 15-23). Components section has horizontal micro-stripes (lines 149-151). B-side body has horizontal micro-stripes (line 290). These CSS-only textures approximate linen/canvas without images.
- **Material gradients:** Multi-stop gradients on buttons simulate glossy/brushed surfaces. Primary button: `linear-gradient(180deg, #C0A060 0%, #8B7340 50%, #A08850 100%)` with three stops creating a highlight-shadow-reflection pattern (line 101). This is textbook skeuomorphic button rendering.
- **Text shadows:** Extensively used. `text-shadow: 0 -1px 1px rgba(0,0,0,0.3)` for light text on dark backgrounds (embossed), `0 1px 0 rgba(255,255,255,0.3)` for dark text on light backgrounds (debossed). Lines 49, 90, 97, 110, 158, 168, 187, 195, 202. Correct technique.
- **Leather strip (A-side):** Lines 123-143. Multi-stop brown gradient, dark border, dual shadow (outer drop + inner top highlight), dashed stitching via `repeating-linear-gradient(90deg, #8B6847 0px, #8B6847 6px, transparent 6px, transparent 12px)`. This is a standout skeuomorphic detail.
- **B-side card bottom border:** `border-bottom: 3px solid #C4A070` (line 331) adds weight and grounds the cards.

### Animations
- **@keyframes:** None. Correct -- skeuomorphism is a static, physical style. Real objects do not bounce or float.
- **Transitions:** `0.15s` on buttons (line 181), `0.2s` on hover cards (line 312). Cards get `translateY(-3px)` on hover.
- **Button :active state (A-side):** `box-shadow: inset 0 2px 4px rgba(0,0,0,0.3)` (line 120) -- the button visually presses into the surface. Correct physical metaphor.
- **Motion appropriateness:** Minimal motion is correct. The `translateY(-3px)` card hover is the only arguably non-physical motion, since real objects do not float up when you hover over them. A slight shadow deepening without position change would be more authentic.

### Content
- **Brand names:** A-side "Realcraft" (line 347), B-side "Craftsman" (line 403). Both evoke handmade quality and craftsmanship. Strong.
- **Taglines:** "Crafted to feel real" (line 355), B-side "Handmade with care" / "Real Materials. Digital Craft." (line 404). Precise and on-brand.
- **Hero copy:** "Leather, wood, metal, linen -- every surface tells you exactly what it is made of. Design you can almost touch." -- directly enumerates skeuomorphic materials. Excellent.
- **Leather strip text (A-side):** "Hand-stitched since 2008" (line 362) -- a wonderful meta-reference (2008 was peak skeuomorphism era in iOS design).
- **Quote:** "The most tactile digital experience I have encountered. It feels like opening a real leather notebook." -- attributed to "Craft Magazine." Evocative and appropriate.

### Specific Fix Recommendations
1. **B-side lacks texture patterns.** The A-side has micro-stripe linen textures on both the hero and components sections. The B-side body has a subtle stripe, but the cards, header, and sections are flat gradients without any texture overlays. Add a subtle linen or paper texture (via repeating-linear-gradient) to the `.bcard` backgrounds or section backgrounds.
2. **B-side buttons lack multi-stop gloss.** The A-side buttons use beautiful three-stop gradients (`#C0A060 0%, #8B7340 50%, #A08850 100%`) with inset highlights and text-shadow. B-side `.bbtn-p` uses only `linear-gradient(180deg, #A0764A, #8B4513)` -- a two-stop gradient without the mid-tone reflection band. Add a third stop and the `inset 0 1px 0 rgba(255,255,255,0.2)` inner highlight.
3. **Duplicate CSS rules.** Lines 328-330 are duplicated at line 335. Remove the trailing duplicate block.
4. **Card `::before` has `position: absolute` but card only gets `position: relative` later.** `.bcard::before` is defined at line 332 with `position: absolute`, but `.bcard` only receives `position: relative; overflow: hidden` at line 333. While CSS rule order does not matter (both apply simultaneously), having the pseudo-element defined before the positioning context is declared makes maintenance confusing. Consolidate these into the main `.bcard` rule.
5. **Card hover `translateY(-3px)` is physically inauthentic.** Real physical objects do not levitate when you look at them. Replace the hover with a subtle shadow deepening: increase `box-shadow` offset and blur on hover instead of translating the card position. Example: `box-shadow: 0 5px 12px rgba(0,0,0,0.18), inset 0 1px 0 rgba(255,255,255,0.6)`.

---

## Candy UI

**Style Authenticity Score: 8/10**

### Fonts
- **Family:** Quicksand, loaded via Google Fonts (`https://fonts.googleapis.com/css2?family=Quicksand:wght@400;500;600;700`)
- **Weights:** 400, 500, 600, 700
- **Loading method:** External `<link>` in `<head>` (line 8)
- **Appropriateness:** Excellent. Quicksand has round, bubbly letterforms that look like they are made of candy themselves. The visual DNA specifically names Quicksand as one of the ideal candy UI fonts. B-side declares `font-family:'Quicksand','Nunito',sans-serif` (line 286) with Nunito as a perfect fallback.

### Colors
- **A-side hero gradient:** `linear-gradient(180deg, #FFB6D9 0%, #FFA3CC 40%, #FF8FBF 100%)` (line 24) -- warm bubblegum pink gradient
- **A-side body background:** `#FFF0F5` (lavender blush, line 11) -- soft pastel base
- **B-side background:** `linear-gradient(180deg, #FFF5F5, #F5F0FF, #F0F9FF)` (line 286) -- pink to lavender to baby blue gradient. Beautiful candy palette.
- **Primary pink:** `#FF7EB3`, `#FF4D8D` (button gradient, line 181), `#FFB3D9` (B-side accent, line 289)
- **Secondary green (mint):** `#A8E6CF`, `#7DCEA0` (line 190), `#E0FFE8` (B-side card 2, line 325)
- **Tertiary purple:** `#DDA0DD`, `#C482C4` (line 143), `#F0E6FF` / `#A855F7` (B-side card 3, line 327)
- **Yellow (lemon):** `#FFEAA7`, `#FDCB6E` (line 144)
- **Blue (sky):** `#74B9FF`, `#5A9FE5` (line 145), `rgba(179,229,255,0.5)` (B-side card border, line 307)
- **Text colors:** `#5A2D5E` dark plum for body (line 11), `#6B3A5D` (B-side, line 286), `#9B6E9B` for secondary (line 240), `#B08DA3` (B-side muted, line 291)
- **Contrast ratios:** `#5A2D5E` on `#FFF0F5` gives approximately 8.5:1 (excellent). `#6B3A5D` on `#FFF5F5` gives approximately 6.2:1 (good). `#B08DA3` on white gives approximately 3.1:1 (borderline). White text on `#FF8FBF` hero gives approximately 2.8:1 (fails for body).
- **Multi-color palette:** The full rainbow is present: pink, green, purple, yellow, blue. This is exactly what candy UI demands.

### Layout
- **A-side hero:** `min-height: 70vh`, pink gradient background, `max-width: 460px` content area (line 86), with overflow `hidden` (line 27) and drip effect at bottom.
- **B-side hero:** `min-height: 80vh`, centered, `max-width: 640px`. Hero h1 is scaled up to `clamp(2.5rem, 7vw, 4.5rem)` (line 330) -- larger than other styles' heroes, which gives it a bouncy, bold personality.
- **Section spacing:** `5rem 2rem` (line 302), `max-width: 1100px` (line 303).
- **Card grid:** `repeat(auto-fit, minmax(280px, 1fr))` (line 306).
- **Responsive:** Single `768px` breakpoint (line 335).

### Sizing
- **Typography scale (A-side):** h1 `2.5rem` (line 91), h2 `1.3rem` (line 153), h3 `0.75rem` (line 160), body `0.95rem` (line 99)
- **Typography scale (B-side):** h1 `clamp(2.5rem, 7vw, 4.5rem)` (line 330 -- note the larger max than other styles), section heading `1.8rem` (line 305)
- **Border radius:** Buttons `50px` (fully pill-shaped, line 174), cards `20px` (A-side line 210) / `22px` (B-side line 307), inputs `50px` (pill-shaped, line 251), swatches `50%` (circular, line 269), card icons `22px` (line 311). The extreme rounding is correct for candy UI.
- **B-side button radius:** `22px` (line 299), with `.bbtn-p` getting a `2.5px` colored border (line 328). The thick border adds a candy-coated outline effect.
- **Card borders:** `2.5px solid rgba(179,229,255,0.5)` (line 307) -- thick, colored, translucent. Gives a gumdrop/jelly appearance.

### Sections
- **Current sections:** Hero with tag/headline/CTAs, feature cards (3), metrics (4), quote, footer.
- **Do they serve the style well?** The feature cards themed around candy colors ("Bubblegum Pink," "Sky Blue," "Mint Green") with matching colored borders and icons are delightful and on-brand. The metrics section ("Heart Adorable," "100% Sweet," "0 Bitter," "Infinity Cute") is playful perfection.
- **What would better demonstrate this style?** A horizontal scroll/carousel of candy-colored tags or badges. Sparkle/confetti decorative elements (the visual DNA calls out "sparkle, star, or confetti" as must-have decorative elements -- currently absent). A bouncy toggle or switch. A badge/pill collection showing the various candy colors.

### Visuals
- **Drip effect (A-side):** `hero::after` (lines 29-41) creates a melting candy drip at the bottom edge using four `radial-gradient(ellipse)` shapes with varying sizes (28-40px). This is an outstanding candy-specific detail -- it looks like icing or melted candy dripping from the hero section.
- **Floating candy pieces (A-side):** Four decorative elements (lines 134-145) with glossy shading (`inset 0 -3px 6px rgba(0,0,0,0.1)` bottom shadow + `inset 0 6px 10px rgba(255,255,255,0.45)` top highlight). Each candy piece has a unique color and staggered float animation. Excellent glossy candy-coating simulation.
- **Candy logo (A-side):** Uses the candy emoji with a circular, glossy element (`logo-candy`, lines 59-70) that has the float animation. Playful.
- **Card header gradient (A-side):** `linear-gradient(135deg, #DDA0DD, #FFB6D9, #FFEAA7)` (line 218) -- purple to pink to yellow candy rainbow.
- **B-side card icons:** Float animation `@keyframes float { 0%,100% { translateY(0) } 50% { translateY(-6px) } }` (line 331) with staggered delays (`0.5s`, `1s`) per card (lines 332-334). This adds the bouncy, bubbly life that candy UI needs.
- **B-side card color differentiation:** Cards 1/2/3 have different border colors and icon themes: pink/green/purple (lines 307, 324-327). Multi-color is key to this style.

### Animations
- **@keyframes (A-side):** `float` animation (lines 13-16): `translateY(0)` to `translateY(-8px)` over the cycle. Applied to logo (line 69) and all four candy pieces (lines 142-145) with varying durations (2.5s-3.2s) and staggered delays.
- **@keyframes (B-side):** `float` animation redefined (line 331) with `-6px` amplitude. Applied to card icons (lines 332-334).
- **Transitions:** `0.2s` on buttons. Primary button hover includes `transform: translateY(-2px) scale(1.02)` (line 122) -- a subtle bounce-up-and-grow effect that feels playful and candy-like.
- **Motion appropriateness:** The float animations are perfectly suited to candy UI's bubbly, weightless personality. The staggered delays prevent uniform motion, creating an organic, lively feel.

### Content
- **Brand names:** A-side "Sweetspot" (line 348), B-side "Sweetie" (line 405). Both are endearing, confectionery-themed names.
- **Taglines:** "Sweetly irresistible interfaces" (line 356), B-side "Sugar, spice & everything nice" / "So Sweet You Could Eat It" (line 406). The nursery rhyme reference and food metaphor are pitch-perfect for the style.
- **Hero copy:** "An interface drenched in pastels and wrapped in love. Every pixel is a little piece of candy." -- emotionally warm and style-appropriate.
- **Card titles:** "Bubblegum Pink," "Sky Blue," "Mint Green" (line 407) -- named after candy colors, doubling as both feature descriptions and palette education.
- **Metrics:** Heart symbol, "100% Sweet," "0 Bitter," "Infinity Cute" (line 408) -- delightful, personality-packed. The heart symbol and infinity symbol add visual flair.
- **Quote:** "I literally smiled the entire time I was using this. Pure joy in every interaction." -- attributed to "Happy User." Captures the emotional response candy UI aims for.

### Specific Fix Recommendations
1. **Missing sparkle/confetti decorative elements.** The visual DNA lists "sparkle, star, or confetti decorative elements" as a must-have for candy UI. Neither the A-side nor B-side includes these. Add CSS-only star/sparkle shapes using `::before`/`::after` pseudo-elements with small rotated squares or star unicode characters scattered in the hero or section backgrounds.
2. **White text on pink hero fails contrast.** `#FFFFFF` on `#FF8FBF` (the darkest part of the hero gradient) gives approximately 2.8:1, failing WCAG AA. Add `text-shadow: 0 1px 3px rgba(180,50,100,0.3)` to improve perceived legibility, or darken the gradient base to `#E875A8` while keeping the sweet pink feeling.
3. **Duplicate CSS rules.** Lines 324-329 are duplicated at line 336. Remove the duplicate block.
4. **B-side missing glossy/shiny highlight on cards and buttons.** The A-side components have beautiful `inset 0 2px 4px rgba(255,255,255,0.3)` top highlights creating the candy-coating gloss. The B-side cards use `box-shadow: 0 4px 12px rgba(179,229,255,0.15)` (line 307) -- a flat shadow without the glossy inner highlight. Add `inset 0 -2px 4px rgba(0,0,0,0.03), inset 0 2px 4px rgba(255,255,255,0.4)` to `.bcard` for the candy-coated effect.
5. **Missing `filter: saturate()` vibrancy boost.** The visual DNA suggests `filter: saturate(1.2) brightness(1.05)` for candy-coated vibrancy. Consider applying a subtle saturation boost to the B-side background or card images. Also consider `box-shadow: 0 4px 0 #darker-shade` (gummy-bear depth shadow) on buttons as listed in the visual DNA, rather than only using blur-spread shadows.

---

## Cross-Style Observations

### Structural Consistency
All five files follow the same A/B toggle architecture with `.side-toggle`, `.a-side`, and `.b-side` containers. The toggle is fixed at `top:12px; right:12px; z-index:99999` (consistent across all files). The A-side defaults to hidden (`display:none`) and the B-side to visible (`display:block`). JavaScript uses `classList.add/remove('show-a')` for switching. This is clean and consistent.

### Shared Issues Across All Files
1. **Duplicate CSS blocks.** Every file has CSS rules duplicated at the end of the style block. These appear to be artifacts from iterative editing. Affects glassmorphism (lines 285-293), neumorphism (lines 285-292), claymorphism (lines 304-311), skeuomorphism (lines 328-335), and candy-ui (lines 324-336).
2. **Single responsive breakpoint.** All files use only `768px`. Adding a `480px` breakpoint for small phones and a `1024px` breakpoint for tablets would improve the responsive experience.
3. **B-side nav links are identical.** All five B-sides use "Home / About / Work / Contact" regardless of style. The A-sides customize their nav labels (e.g., "Flavors / Shop / Joy" for Candy, "Toolbox / Gallery / About" for Skeuomorphism). The B-side nav labels should be similarly customized.
4. **Generic feature section pattern.** All B-sides use the same "Features / What Sets Us Apart" heading pair with a 3-card grid. While the card content varies per style, the identical structural pattern across all 100 styles reduces perceived uniqueness.
5. **Missing focus styles.** None of the B-sides define custom `:focus` or `:focus-visible` styles for buttons or links. The browser default outline may conflict with style aesthetics. Each style should have a custom focus indicator matching its visual language.

### Style Differentiation Matrix

| Property | Glassmorphism | Neumorphism | Claymorphism | Skeuomorphism | Candy UI |
|---|---|---|---|---|---|
| Background | Vibrant gradient | Flat `#E0E5EC` | Pastel gradient | Textured linen | Pastel gradient |
| Border radius | 16px | 16px | 24px | 6-8px | 22-50px |
| Shadow type | None (uses blur) | Dual directional | Multi-layer inset+outer | Drop + inset highlight | Glossy multi-layer |
| Border style | `rgba(255,255,255,0.2)` | None | `2px solid` colored | `1px solid` dark | `2.5px solid` colored |
| Font | Inter | Inter/Poppins | Nunito | Georgia/Roboto | Quicksand |
| Key technique | `backdrop-filter: blur()` | Dual `box-shadow` | Inner shadow + gradient | Texture + multi-stop gradient | Extreme rounding + gloss |
| Animation | None | None | None | None | Float keyframes |

The styles are well-differentiated across these properties. Each file convincingly represents its intended aesthetic. The strongest differentiation is in shadow techniques and border treatments, where each style has a genuinely unique approach.

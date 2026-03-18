# Visual & UI Style Compendium v2

A curated catalog of 65 web-implementable design styles, organized into 9 categories. Trimmed from 149 raw entries — removed textures, art references, interaction paradigms, and micro-techniques that don't constitute standalone web design approaches.

---

## Core Foundations

### 1. Minimalism & Swiss Style
**Category:** Core Foundations | **Era:** 1950s–present | **Complexity:** Low

> Grid-based layouts, sans-serif typography, generous whitespace, restrained color palette, Müller-Brockmann influence.

- Grid system (12–16 columns), mathematical spacing
- Sans-serif type hierarchy (Inter, Helvetica, Neue Haas Grotesk)
- Monochrome or single-accent-color palette
- No decorative elements; content is the design
- **Best for:** Corporate sites, SaaS dashboards, portfolios, documentation
- **Don't use for:** Playful brands, entertainment, children's products
- **Frameworks:** Tailwind 10/10, Bootstrap 9/10, MUI 9/10
- **A11y:** AAA

### 2. Flat Design
**Category:** Core Foundations | **Era:** 2013–2017 | **Complexity:** Low

> Zero gradients or shadows, solid color fills, simple iconography, emphasis on typography and color.

- No box-shadow, no gradients, no depth cues
- Bright solid-color palette (5–8 colors)
- Simple geometric icons, consistent border-radius
- Clear visual hierarchy through color and size alone
- **Best for:** Mobile apps, icon systems, dashboards, utility apps
- **Don't use for:** Luxury brands, immersive experiences, 3D showcases
- **Frameworks:** MUI 10/10, Bootstrap 9/10, Tailwind 9/10
- **A11y:** AA

### 3. Inclusive Design
**Category:** Core Foundations | **Era:** Timeless | **Complexity:** Medium

> Universal usability — WCAG-compliant contrast, clear focus states, multi-modal input, cognitive load reduction, assistive-tech compatibility.

- 4.5:1+ contrast ratios on all text
- Visible focus indicators (3px+ ring)
- Touch targets ≥44px, large readable type scales
- Reduced motion support, screen-reader-friendly markup
- **Best for:** Government services, healthcare, banking, education
- **Don't use for:** (applicable everywhere — philosophy, not aesthetic limitation)
- **Frameworks:** Radix UI 10/10, MUI 9/10, Chakra UI 9/10
- **A11y:** AAA

### 4. AI-Native UI
**Category:** Core Foundations | **Era:** 2023–present | **Complexity:** Medium

> Interfaces designed around AI interaction — conversational flows, generative content areas, shimmer loading states, adaptive layouts.

- Purple-cyan gradient palette as brand signal
- Shimmer/skeleton loading for streaming responses
- Conversational message bubbles, typing indicators
- Glow effects on AI-generated elements
- **Best for:** AI assistants, prompt tools, generative platforms
- **Don't use for:** Static brochure sites, traditional e-commerce
- **Frameworks:** Vercel AI SDK 10/10, Tailwind 9/10, Framer Motion 9/10
- **A11y:** AA

### 5. Dark Mode (OLED)
**Category:** Core Foundations | **Era:** 2020s | **Complexity:** Low

> True-black backgrounds optimized for OLED, high-contrast neon accent colors, glow effects.

- Background: #000000 (pure black for pixel-off power saving)
- Neon accent colors with box-shadow glow
- Surface hierarchy: #000 → #0D0D0D → #1A1A1A
- Border: 1px solid rgba(255,255,255,0.1) for separation
- **Best for:** Developer tools, music apps, dashboards, mobile apps
- **Don't use for:** Print-focused designs, light-first branding
- **Frameworks:** Tailwind 10/10, MUI 9/10, Chakra UI 9/10
- **A11y:** AA

### 6. E-Ink / Paper
**Category:** Core Foundations | **Era:** Timeless | **Complexity:** Low

> Low-contrast, paper-textured backgrounds, serif typography, reading-optimized layouts, minimal chrome.

- Warm off-white backgrounds (#FAF8F5, #F5F1E8)
- Serif body text (Merriweather, Georgia, Lora)
- Minimal UI chrome; content-first reading experience
- Muted, desaturated color accents
- **Best for:** Reading apps, journals, digital publications, calm-tech
- **Don't use for:** Gaming, dashboards, high-energy brands
- **Frameworks:** Tailwind 8/10, vanilla CSS 10/10
- **A11y:** AA

---

## Surface & Material

### 7. Glassmorphism
**Category:** Surface & Material | **Era:** 2020s | **Complexity:** Medium

> Frosted-glass translucent panels with background blur, subtle borders, and layered depth. Includes Apple's "Liquid Glass" evolution.

- `backdrop-filter: blur(12px) saturate(180%)`
- `background: rgba(255,255,255,0.1–0.4)`
- Subtle white border for edge definition
- Layered z-depth with translucent surfaces
- **Best for:** Overlays, cards, modals, dashboards, iOS/macOS style
- **Don't use for:** Text-heavy content, data tables, accessibility-critical
- **Frameworks:** Tailwind 9/10, CSS Modules 8/10
- **A11y:** AA

### 8. Neumorphism
**Category:** Surface & Material | **Era:** 2020s | **Complexity:** Medium

> Soft extruded shapes using background-matching colors with paired light/dark shadows, creating a pressed-plastic effect.

- Background matches container (#E0E5EC)
- Dual box-shadow: light (#fff) + dark (#a3b1c6)
- Inset shadows for pressed/active states
- Large border-radius (12px+)
- **Best for:** Music players, calculators, toggles, settings panels
- **Don't use for:** Complex dashboards, text-heavy apps
- **Frameworks:** Vanilla CSS 10/10, Tailwind 7/10
- **A11y:** A (contrast issues common)

### 9. Claymorphism
**Category:** Surface & Material | **Era:** 2021–2023 | **Complexity:** Medium

> 3D clay-like rendered elements with soft rounded forms, pastel palette, playful material simulation.

- Large border-radius (16px+), inner shadow for clay depth
- Pastel gradients (linear-gradient 145deg)
- Soft outer shadow for floating effect
- Playful, illustrated feel
- **Best for:** Onboarding, children's education, friendly SaaS
- **Don't use for:** Enterprise dashboards, data-dense interfaces
- **Frameworks:** Vanilla CSS 9/10, Tailwind 8/10
- **A11y:** AA

### 10. Skeuomorphism
**Category:** Surface & Material | **Era:** 2007–2013 | **Complexity:** High

> UI elements mimicking real-world materials — leather, wood, metal, felt, paper. Physical metaphors everywhere.

- Multi-layered box-shadows for realistic depth
- CSS gradients simulating metallic/leather surfaces
- Inset highlights (`inset 0 1px 0 rgba(255,255,255,0.5)`)
- Texture overlays via CSS noise patterns
- **Best for:** Music apps, nostalgic UIs, utility apps
- **Don't use for:** Modern SaaS, scalable design systems
- **Frameworks:** Vanilla CSS 10/10, Tailwind 5/10
- **A11y:** AA

### 11. Candy UI / Confectionery
**Category:** Surface & Material | **Era:** 2020s | **Complexity:** Medium

> Glossy sugar-coat surfaces, pastel drips, rounded bubblegum geometry, sweet-shop palette.

- Glossy highlight gradients on buttons/cards
- Pastel pink, mint, lavender, yellow palette
- Extreme border-radius (20px+), bubbly shapes
- Playful, youthful, confectionery feel
- **Best for:** Kids' games, bakery brands, playful e-commerce
- **Don't use for:** Enterprise, finance, healthcare
- **Frameworks:** Vanilla CSS 8/10, Tailwind 7/10
- **A11y:** A

---

## Color & Light

### 12. Vibrant & Block-based
**Category:** Color & Light | **Era:** 2020s | **Complexity:** Low

> Bold saturated color blocks as layout containers, high-contrast pairings, energetic palette.

- Full-bleed color sections as layout structure
- 4–6 bold saturated colors in rotation
- High contrast between adjacent blocks
- Typography inverts per block (white on color, dark on light)
- **Best for:** Startup landing pages, event sites, campaigns
- **Don't use for:** Calm/minimal brands, reading-heavy content
- **Frameworks:** Tailwind 10/10, Bootstrap 9/10
- **A11y:** AA

### 13. Gradient Mesh / Aurora
**Category:** Color & Light | **Era:** 2020s | **Complexity:** Low

> Complex multi-point gradient meshes creating painterly color fields, fluid organic color transitions, aurora borealis effect.

- `background: linear-gradient(135deg, multi-stop)` with 4+ color stops
- Radial gradient overlays for mesh effect
- Glass card overlay for content readability
- Smooth transitions, no harsh boundaries
- **Best for:** Hero backgrounds, branding, creative portfolios
- **Don't use for:** Data dashboards, text-heavy content
- **Frameworks:** Tailwind 8/10, vanilla CSS 9/10
- **A11y:** AA

### 14. Holographic / Iridescent
**Category:** Color & Light | **Era:** 2020s | **Complexity:** Medium

> Rainbow-shift iridescence, angle-reactive gradients, metallic substrate, prismatic shimmer.

- Multi-color linear-gradient with animation (hue-rotate)
- Metallic/chrome base with rainbow overlay
- CSS `filter: hue-rotate()` for dynamic color shifting
- Premium, collectible, futuristic feel
- **Best for:** Premium product pages, crypto/fintech, collectibles
- **Don't use for:** Corporate, government, accessibility-first
- **Frameworks:** Vanilla CSS 9/10, Tailwind 7/10
- **A11y:** A

---

## Layout & Structure

### 15. Bento Box Grid
**Category:** Layout & Structure | **Era:** 2023–present | **Complexity:** Medium

> Modular rectangular compartments of varying sizes, inspired by Apple-style marketing pages.

- CSS Grid with mixed `grid-column: span` values
- Consistent gap (8px), rounded corners (12–16px)
- Cards contain isolated content pieces (stat, image, text)
- Neutral palette with selective accent
- **Best for:** Feature showcases, product pages, SaaS marketing
- **Don't use for:** Long-form content, linear storytelling
- **Frameworks:** Tailwind 10/10, CSS Grid 10/10
- **A11y:** AA

### 16. Editorial Grid / Magazine
**Category:** Layout & Structure | **Era:** Timeless | **Complexity:** Medium

> Print-magazine layout ported to digital — pull quotes, column breaks, drop caps, asymmetric grids, strong type hierarchy.

- Asymmetric CSS Grid (2fr 1fr, 3fr 2fr etc.)
- Large serif headings, small sans-serif body
- Pull quotes, drop caps, red editorial accents
- Column-based text flow
- **Best for:** Online publications, journalism, fashion editorial
- **Don't use for:** App interfaces, gaming, utility tools
- **Frameworks:** Tailwind 9/10, CSS Grid 10/10
- **A11y:** AAA

### 17. Dimensional Layering
**Category:** Layout & Structure | **Era:** 2020s | **Complexity:** Medium

> Stacked z-axis planes creating explicit depth, parallax separation between content tiers.

- Multiple overlapping layers via z-index and transform
- Translucent backgrounds revealing layers beneath
- Shadow depth between planes
- Content organized by depth level (foreground, mid, back)
- **Best for:** Feature pages, immersive storytelling, product launches
- **Don't use for:** Data tables, form-heavy UIs
- **Frameworks:** CSS Transforms 10/10, Framer Motion 9/10
- **A11y:** AA

### 18. Comic Panel Layout
**Category:** Layout & Structure | **Era:** Timeless | **Complexity:** Medium

> Gutters, speech bubbles, Ben-Day dots, sequential frame navigation, panel-grid storytelling.

- CSS Grid panels with thick borders (gutters)
- Speech bubble shapes via CSS (border-radius + pseudo-elements)
- Ben-Day dot patterns via radial-gradient
- Bold primary colors, thick black outlines
- **Best for:** Webcomics, children's education, interactive narratives
- **Don't use for:** Enterprise SaaS, finance, formal brands
- **Frameworks:** CSS Grid 10/10, Tailwind 7/10
- **A11y:** AA

### 19. Trading Card
**Category:** Layout & Structure | **Era:** 2020s | **Complexity:** Medium

> Bordered frames, stat blocks, rarity badges, foil variant accents, collectible structure.

- Card frame with ornate border (double/ridge)
- Stat blocks with key-value pairs
- Rarity indicators (color-coded badges)
- Metallic/foil gradient accents on premium variants
- **Best for:** Gaming platforms, NFT markets, sports apps
- **Don't use for:** Corporate, productivity tools
- **Frameworks:** Tailwind 8/10, vanilla CSS 9/10
- **A11y:** AA

### 20. Newspaper Classified / Dense Type
**Category:** Layout & Structure | **Era:** Timeless | **Complexity:** Low

> Dense column text, abbreviated shorthand, category headers, thin rule dividers, small type.

- Multi-column layout (CSS columns or grid)
- Small type (11–13px), high density
- Thin horizontal rules between sections
- Category headers in bold/caps
- **Best for:** Directories, job boards, marketplaces, listings
- **Don't use for:** Consumer apps, luxury brands
- **Frameworks:** CSS Multi-column 10/10, Tailwind 8/10
- **A11y:** A (small type concern)

---

## Motion & Interaction

### 21. Motion-Driven Design
**Category:** Motion & Interaction | **Era:** 2020s | **Complexity:** High

> Animation as primary design language — transitions, state changes, and motion convey hierarchy and meaning. Includes micro-interactions.

- Every state change has a transition (150–300ms)
- Hover/active/focus states with transform feedback
- Scroll-triggered reveals, staggered animations
- `prefers-reduced-motion` fallbacks required
- **Best for:** Interactive portfolios, onboarding, storytelling
- **Don't use for:** Static content, print-like experiences
- **Frameworks:** GSAP 10/10, Framer Motion 10/10, CSS Transitions 9/10
- **A11y:** AA (with reduced-motion support)

### 22. Kinetic Typography
**Category:** Motion & Interaction | **Era:** 2020s | **Complexity:** High

> Text as animated, moving, transforming visual element — scale shifts, path animations, rhythm-driven type.

- Large display type (clamp(3rem, 8vw, 8rem))
- CSS @keyframes for text reveals, scaling, rotation
- Minimal supporting elements; text IS the design
- High contrast, few colors (black/white + one accent)
- **Best for:** Portfolios, agencies, brand manifestos
- **Don't use for:** Data dashboards, form UIs
- **Frameworks:** GSAP 10/10, Framer Motion 9/10
- **A11y:** A

### 23. Parallax Storytelling
**Category:** Motion & Interaction | **Era:** 2015–present | **Complexity:** High

> Scroll-driven depth layers moving at different speeds to create narrative progression.

- `position: sticky` sections, `transform: translateZ()`
- Perspective-based parallax depth
- Full-viewport sections for cinematic feel
- Progressive content reveal on scroll
- **Best for:** Brand stories, annual reports, campaign microsites
- **Don't use for:** Dashboards, utility apps
- **Frameworks:** GSAP ScrollTrigger 10/10, Lenis 9/10
- **A11y:** A (motion-sensitive users)

### 24. Tactile / Deformable UI
**Category:** Motion & Interaction | **Era:** 2020s | **Complexity:** Medium

> Elements that squish, stretch, bounce with physics simulation, rubber-like material response.

- `transition: transform 0.3s cubic-bezier(0.34, 1.56, 0.64, 1)`
- Hover: `transform: scale(1.05)`, Active: `scale(0.95)`
- Soft shadows that grow/shrink with interaction
- Rounded shapes, playful spring animations
- **Best for:** Children's apps, playful onboarding, experimental UIs
- **Don't use for:** Enterprise, finance, medical
- **Frameworks:** Framer Motion 10/10, React Spring 9/10
- **A11y:** AA

### 25. Split-Flap / Departure Board
**Category:** Motion & Interaction | **Era:** Retro-modern | **Complexity:** High

> Mechanical letter-tile flip animation, terminal-schedule grids, clacking transition rhythm.

- Segmented character tiles with flip animation
- Dark background, white/amber characters
- Grid-based time/text displays
- `perspective` + `rotateX` for flip effect
- **Best for:** Travel booking, countdown timers, event schedules
- **Don't use for:** Casual apps, children's products
- **Frameworks:** Vanilla CSS 8/10, GSAP 9/10
- **A11y:** AA

### 26. Scratch Card / Gamified Reveal
**Category:** Motion & Interaction | **Era:** 2020s | **Complexity:** Medium

> Masked reveal layers, metallic scratch surface, exposed prize zones, gamified discovery.

- CSS `clip-path` or canvas for scratch-off effect
- Metallic gradient for unscratched surface
- Bright reward colors underneath
- Promotional, exciting, gamified feel
- **Best for:** Promotions, gamified onboarding, loyalty programs
- **Don't use for:** Serious enterprise, medical, government
- **Frameworks:** Canvas API 10/10, vanilla CSS 7/10
- **A11y:** A

### 27. Lenticular / Angle-Shift
**Category:** Motion & Interaction | **Era:** 2020s | **Complexity:** Medium

> Content that changes on scroll or cursor position, stripe-interleaved image layers, tilt reveal.

- CSS hover/scroll transitions between states
- Before/after image comparisons
- `transform: perspective()` for tilt effect
- Reveal animations triggered by position
- **Best for:** Product reveals, before/after comparisons, portfolios
- **Don't use for:** Text-heavy content, accessibility-first
- **Frameworks:** CSS Transforms 9/10, GSAP 8/10
- **A11y:** A

---

## Retro & Nostalgic

### 28. Retro-Futurism
**Category:** Retro & Nostalgic | **Era:** 1960s aesthetic | **Complexity:** Medium

> Mid-century space-age aesthetics — atomic motifs, googie architecture influence, chrome and starbursts.

- Circular/orbital shapes, starburst decorations
- Chrome metallic gradients
- Wide letter-spacing, condensed sans-serif type
- Orange, gold, teal, chrome palette
- **Best for:** Entertainment, nostalgia brands, sci-fi media
- **Don't use for:** Minimalist SaaS, modern fintech
- **Frameworks:** Vanilla CSS 8/10, Tailwind 7/10
- **A11y:** AA

### 29. Cassette Futurism
**Category:** Retro & Nostalgic | **Era:** 1970s–80s aesthetic | **Complexity:** Medium

> Analog-tech interfaces — toggle switches, amber CRTs, chunky bezels, reel-to-reel, VU meters, oscilloscope traces.

- Amber (#FFB000) or green (#0f0) on black
- Monospace fonts, CRT glow effect (text-shadow)
- Chunky bordered UI elements, toggle switches
- Analog gauge/meter elements
- **Best for:** Synthwave media, retro-tech products, audio tools
- **Don't use for:** Modern SaaS, minimal brands
- **Frameworks:** Vanilla CSS 9/10, Tailwind 6/10
- **A11y:** AA

### 30. Y2K Aesthetic
**Category:** Retro & Nostalgic | **Era:** 2000s aesthetic | **Complexity:** Medium

> Early-2000s digital nostalgia — metallic gradients, bubble fonts, translucent plastic, techno-optimism.

- Chrome/silver metallic gradients
- Bubbly rounded shapes (16px+ border-radius)
- Pastel + metallic palette (sky blue, pink, lavender)
- Holographic/iridescent accents
- **Best for:** Fashion brands, pop culture, youth campaigns
- **Don't use for:** Enterprise, legal, government
- **Frameworks:** Vanilla CSS 8/10, Tailwind 7/10
- **A11y:** A

### 31. Vaporwave
**Category:** Retro & Nostalgic | **Era:** 1990s aesthetic | **Complexity:** Medium

> Pastel pink/cyan/purple, retro grid perspective, 90s nostalgia, sunset palette, consumer irony.

- Purple-to-pink sunset gradients
- Perspective grid background (repeating-linear-gradient)
- Chrome/holographic text effects
- Roman bust imagery references, Japanese text
- **Best for:** Music platforms, aesthetic blogs, art collectives
- **Don't use for:** B2B SaaS, enterprise, news sites
- **Frameworks:** Vanilla CSS 9/10, Tailwind 7/10
- **A11y:** A

### 32. Memphis Design
**Category:** Retro & Nostalgic | **Era:** 1980s revival | **Complexity:** Medium

> Bold geometric patterns, clashing colors, squiggles, terrazzo fills, Italian postmodernism.

- Bright primary colors in geometric shapes
- CSS shapes: circles, triangles (via border tricks), zigzags
- Playful asymmetric layouts
- Pattern backgrounds with repeating geometric elements
- **Best for:** Creative agencies, art platforms, playful brands
- **Don't use for:** Finance, healthcare, government
- **Frameworks:** Vanilla CSS 8/10, Tailwind 7/10
- **A11y:** AA

### 33. Pixel Art
**Category:** Retro & Nostalgic | **Era:** 1980s aesthetic | **Complexity:** Medium

> Deliberately low-resolution grid-locked artwork, limited palettes, retro game nostalgia.

- `image-rendering: pixelated` / `crisp-edges`
- Limited 4–8 color palette
- Grid-perfect alignment, no anti-aliasing
- Blocky shapes, bitmap-style fonts
- **Best for:** Indie games, retro brands, 8-bit campaigns
- **Don't use for:** Corporate, luxury, data dashboards
- **Frameworks:** Vanilla CSS 9/10, Canvas 8/10
- **A11y:** AA

### 34. Vintage Analog / Retro Film
**Category:** Retro & Nostalgic | **Era:** Timeless | **Complexity:** Medium

> Film grain, light leaks, color fade, expired-stock color shifts, instant-photo borders.

- CSS noise overlay for film grain (`url(data:image/svg+xml...)`)
- Warm sepia/desaturated color treatment
- Light leak gradients (warm orange/yellow overlays)
- White-border instant-photo framing
- **Best for:** Photography portfolios, indie films, heritage brands
- **Don't use for:** Tech startups, data platforms
- **Frameworks:** Vanilla CSS 9/10, CSS Filters 8/10
- **A11y:** AA

### 35. Retrocomputing / DOS Shell
**Category:** Retro & Nostalgic | **Era:** 1980s aesthetic | **Complexity:** Low

> 80-column text, command prompt, system font, directory trees, C:\> nostalgia. Includes teletype/ticker aesthetics.

- Monospace everything (VT323, IBM Plex Mono)
- Green (#0f0) or amber (#FFB000) on black
- CRT scanline overlay
- Blinking cursor, directory-tree structure
- **Best for:** Developer tools, hacker-aesthetic sites, terminal UIs
- **Don't use for:** Consumer apps, luxury brands
- **Frameworks:** Vanilla CSS 10/10
- **A11y:** AA

### 36. Receipt / Thermal Print
**Category:** Retro & Nostalgic | **Era:** Modern retro | **Complexity:** Low

> Narrow-column monospace, dashed dividers, faded-edge roll paper, transaction-log format.

- Narrow content width (300–400px)
- Monospace type, dashed border dividers
- White/cream background, black text
- Transaction-line-item structure
- **Best for:** Expense trackers, POS systems, order confirmations
- **Don't use for:** Marketing sites, portfolios
- **Frameworks:** Vanilla CSS 10/10
- **A11y:** AA

---

## Thematic & Atmospheric

### 37. Cyberpunk UI
**Category:** Thematic & Atmospheric | **Era:** Futuristic | **Complexity:** High

> Neon-on-dark, glitch effects, CJK typography accents, scan lines, high-tech-low-life atmosphere. Includes datamosh/glitch textile elements.

- Dark base (#0a0a1a) with neon accents (#FF006E, #00F0FF, #39FF14)
- `text-shadow: 0 0 8px neon` for glow
- Scanline overlay via repeating-linear-gradient
- `clip-path: polygon()` for angular shapes
- **Best for:** Gaming, entertainment, creative portfolios
- **Don't use for:** Healthcare, education, corporate, elderly audiences
- **Frameworks:** Vanilla CSS 9/10, Three.js 8/10
- **A11y:** A

### 38. Solarpunk
**Category:** Thematic & Atmospheric | **Era:** 2020s | **Complexity:** Low

> Lush greens, cooperative iconography, sun-drenched warmth, utopian sustainable-tech optimism.

- Warm greens, golden yellows, sky blues
- Rounded organic shapes, optimistic feel
- Nature + technology harmony imagery
- Warm gradients, natural textures
- **Best for:** Climate tech, community apps, sustainability platforms
- **Don't use for:** Finance, military, industrial
- **Frameworks:** Tailwind 9/10, vanilla CSS 8/10
- **A11y:** AA

### 39. Organic Biophilic
**Category:** Thematic & Atmospheric | **Era:** Timeless | **Complexity:** Low

> Nature-derived shapes, earth-tone palettes, leaf/root/water motifs, Voronoi cells, growth-simulation patterns.

- Earth tones: forest green, brown, warm beige, sage
- Organic blob shapes (`border-radius: 50% 30% 50% 70%`)
- Warm neutral backgrounds (#F4E9D8)
- Flowing curves, no sharp angles
- **Best for:** Wellness, eco brands, sustainability, retreats
- **Don't use for:** Tech startups, gaming, neon aesthetics
- **Frameworks:** Tailwind 8/10, vanilla CSS 9/10
- **A11y:** AA

### 40. HUD / Sci-Fi FUI
**Category:** Thematic & Atmospheric | **Era:** Futuristic | **Complexity:** High

> Fantasy user interfaces — targeting reticles, holographic panels, data-stream overlays. Includes air traffic control aesthetic.

- Cyan monochrome on dark (#000D1A + #00F0FF)
- Monospace typography with glow
- Circular/radar UI elements, grid overlays
- Wireframe borders, scanning animations
- **Best for:** Gaming HUDs, data viz, monitoring, tech demos
- **Don't use for:** E-commerce, blogs, accessibility-critical
- **Frameworks:** Vanilla CSS 9/10, Canvas/Three.js 8/10
- **A11y:** A

### 41. Cinematic / Film Noir
**Category:** Thematic & Atmospheric | **Era:** Timeless | **Complexity:** Medium

> Deep chiaroscuro, venetian-blind shadow bars, monochrome with single accent, dramatic contrast. Includes film-leader/countdown aesthetics.

- Near-black backgrounds with dramatic light pools
- Single color accent (typically red #DC143C)
- High-contrast monochrome imagery
- Film grain CSS overlay, venetian-blind shadow patterns
- **Best for:** Film sites, thriller media, cocktail brands, noir fiction
- **Don't use for:** Children's products, bright consumer brands
- **Frameworks:** Vanilla CSS 9/10, Tailwind 7/10
- **A11y:** AA

### 42. Pharmaceutical / Clinical
**Category:** Thematic & Atmospheric | **Era:** Modern | **Complexity:** Low

> Sterile white fields, blister-pack grids, monograph typography, pill-shaped UI elements.

- Clean white backgrounds, clinical blue accents
- Grid-based layouts with precise spacing
- Sans-serif type, medical-precise alignment
- Pill-shaped buttons (`border-radius: 9999px`)
- **Best for:** Health apps, medical platforms, clinical dashboards
- **Don't use for:** Entertainment, creative, playful brands
- **Frameworks:** Tailwind 9/10, MUI 8/10
- **A11y:** AAA

### 43. Astrological / Celestial
**Category:** Thematic & Atmospheric | **Era:** Timeless | **Complexity:** Medium

> Star-chart radials, constellation line-art, zodiac-wheel navigation, celestial patterns.

- Deep navy/indigo backgrounds (#0A0A2A)
- Gold (#FFD700) and star-white accents
- Constellation line-art (thin lines connecting dots)
- Radial/circular navigation elements
- **Best for:** Horoscope apps, astronomy, mystical brands
- **Don't use for:** Corporate, engineering, minimalist
- **Frameworks:** Vanilla CSS 8/10, SVG 9/10
- **A11y:** AA

### 44. Passport / Official Document
**Category:** Thematic & Atmospheric | **Era:** Timeless | **Complexity:** Medium

> Security guilloche patterns, stamped seals, machine-readable zones, official-credential layout. Includes ballot/civic form aesthetics.

- Fine-line guilloche patterns (SVG/CSS)
- Navy blue, gold, cream palette
- Serif typography for formality
- Seal/stamp decorative elements
- **Best for:** Identity verification, government services, certificates
- **Don't use for:** Casual consumer apps, playful brands
- **Frameworks:** SVG 10/10, vanilla CSS 8/10
- **A11y:** AA

### 45. Whiteboard / Collaborative Canvas
**Category:** Thematic & Atmospheric | **Era:** 2020s | **Complexity:** Medium

> Marker strokes, magnet-pinned cards, hasty diagrams, sticky notes, ideation-in-progress feel.

- White/off-white infinite canvas background
- Colored sticky notes (yellow, pink, green, blue)
- Hand-drawn feel with slightly rough CSS borders
- Marker-style colors, informal layout
- **Best for:** Brainstorming tools, Agile boards, collaborative workspaces
- **Don't use for:** Formal corporate, luxury, government
- **Frameworks:** Tailwind 8/10, vanilla CSS 9/10
- **A11y:** AA

### 46. Stage Lighting / Theatre
**Category:** Thematic & Atmospheric | **Era:** Timeless | **Complexity:** Medium

> Spotlight cones, color gel washes, curtain-reveal transitions, proscenium framing.

- Dark background with CSS radial-gradient spotlights
- Rich reds, golds, velvet texture gradients
- Curtain-reveal effect on scroll/interaction
- Dramatic focus/unfocus on content areas
- **Best for:** Theater companies, event promotions, talent showcases
- **Don't use for:** Data tools, enterprise SaaS
- **Frameworks:** GSAP 9/10, vanilla CSS 8/10
- **A11y:** AA

---

## Experimental & Avant-garde

### 47. Brutalism
**Category:** Experimental & Avant-garde | **Era:** 2020s revival | **Complexity:** Low

> Raw, unpolished layouts with exposed structure, harsh typography, minimal decoration. Includes anti-polish and text-only brutalist variants.

- No decoration: thick borders, raw backgrounds
- Monospace or heavy sans-serif type
- Visible grid structure, exposed layout mechanics
- Intentional awkwardness, default HTML aesthetic
- **Best for:** Art galleries, experimental portfolios, zines
- **Don't use for:** Corporate enterprise, healthcare, luxury
- **Frameworks:** Vanilla CSS 10/10
- **A11y:** AAA (high contrast)

### 48. Neubrutalism
**Category:** Experimental & Avant-garde | **Era:** 2020s | **Complexity:** Low

> Brutalism refined — bold outlines, flat bright fills, offset shadows, visible borders, playful rawness.

- `border: 3px solid #000`
- `box-shadow: 4px 4px 0 #000` (hard offset)
- Bright flat color fills (yellow, coral, teal)
- Bold type (700–900 weight)
- **Best for:** Web3, creative agencies, developer blogs, indie SaaS
- **Don't use for:** Healthcare, finance, elderly audiences
- **Frameworks:** Tailwind 9/10, vanilla CSS 10/10
- **A11y:** AAA

### 49. Gen Z Chaos / Maximalism
**Category:** Experimental & Avant-garde | **Era:** 2020s | **Complexity:** Medium

> Sensory overload — mixed fonts, sticker overlays, clashing neon colors, meme energy, anti-hierarchy.

- Clashing neon colors (#FF00FF, #00FF00, #FFFF00)
- Mixed font weights and families in one view
- Rotated elements (`transform: rotate(-2deg)`)
- High energy visual density, no white space
- **Best for:** Youth culture, memes, social media, viral campaigns
- **Don't use for:** Corporate, healthcare, finance, government
- **Frameworks:** Vanilla CSS 9/10, Tailwind 7/10
- **A11y:** A

### 50. Collage Zine
**Category:** Experimental & Avant-garde | **Era:** Timeless | **Complexity:** Medium

> Torn-edge layering, mixed media fragments, ransom-note type, tape strips, photocopy decay. Includes xerox/photocopy aesthetic.

- Layered elements with rotation and overlap
- Mixed typefaces (intentionally mismatched)
- High-contrast toner texture, grain overlays
- Tape-strip decorative elements
- **Best for:** Music labels, underground culture, activist platforms
- **Don't use for:** Corporate, medical, government
- **Frameworks:** Vanilla CSS 9/10
- **A11y:** A

### 51. Op Art
**Category:** Experimental & Avant-garde | **Era:** 1960s revival | **Complexity:** Medium

> High-contrast geometric patterns producing optical vibration, Bridget Riley influence, perceptual movement illusion.

- Black/white repeating geometric patterns
- CSS `repeating-linear-gradient` for stripe patterns
- Optical shimmer/movement from pattern density
- Minimal color (monochrome or duochrome)
- **Best for:** Art galleries, fashion campaigns, experimental brands
- **Don't use for:** Reading-heavy content, accessibility-sensitive
- **Frameworks:** CSS Patterns 10/10
- **A11y:** Caution (motion/vestibular triggers)

### 52. Spatial UI / VisionOS
**Category:** Experimental & Avant-garde | **Era:** 2023–present | **Complexity:** High

> Floating panels in 3D space, depth-aware window management, gaze/pinch interaction targets.

- Frosted translucent panels with heavy blur (20px)
- Multiple z-depth layers
- Apple-style rounded corners (12px+) everywhere
- `rgba(255,255,255,0.08)` surface colors on dark base
- **Best for:** AR/VR interfaces, spatial computing, immersive workspaces
- **Don't use for:** Content-heavy sites, low-end devices
- **Frameworks:** Apple Design Resources 10/10, Tailwind 8/10
- **A11y:** AA

### 53. Wireframe Mesh
**Category:** Experimental & Avant-garde | **Era:** 2020s | **Complexity:** Medium

> Bare 3D polygon edges, no fills, depth via line density and perspective, structural transparency.

- Dark background with thin colored grid lines
- CSS perspective transforms for 3D wireframe feel
- No fill colors — structure defined by lines only
- Technical, blueprint-adjacent aesthetic
- **Best for:** 3D tool showcases, tech portfolios, architecture viz
- **Don't use for:** Consumer apps, content sites
- **Frameworks:** Three.js 10/10, CSS 3D Transforms 7/10
- **A11y:** A

### 54. Particle Cloud
**Category:** Experimental & Avant-garde | **Era:** 2020s | **Complexity:** High

> UI elements composed of dot swarms, density encodes emphasis, emergent-form shapes.

- Dark background with clusters of dots/particles
- CSS `box-shadow` multiple values or canvas for particles
- Density = visual weight (more dots = more important)
- Generative, science-communication feel
- **Best for:** Data viz, generative landing pages, science comms
- **Don't use for:** Forms, text-heavy, accessibility-first
- **Frameworks:** Three.js 10/10, Canvas 9/10
- **A11y:** A

### 55. Diorama / Tilt-Shift
**Category:** Experimental & Avant-garde | **Era:** 2020s | **Complexity:** Medium

> Miniature-world depth blur, layered paper-cutout parallax planes, model-village scale.

- Layered paper-like elements with drop shadows
- Edge blur simulating tilt-shift depth of field
- Soft, warm color palette
- Parallax separation between content planes
- **Best for:** City guides, tourism, scroll storytelling, educational viz
- **Don't use for:** Data dashboards, enterprise tools
- **Frameworks:** CSS Filters 8/10, GSAP 9/10
- **A11y:** AA

---

## Data & Technical

### 56. Cartographic / Wayfinding
**Category:** Data & Technical | **Era:** Timeless | **Complexity:** Medium

> Map-derived UI with contour lines, legend boxes, coordinate grids, route indicators.

- Topographic color palette (greens, blues, browns)
- Contour line patterns as background texture
- Legend/key UI components
- Coordinate grid overlays
- **Best for:** Travel platforms, outdoor brands, urban planning
- **Don't use for:** Fashion, entertainment, playful brands
- **Frameworks:** Mapbox GL 10/10, Leaflet 9/10
- **A11y:** AA

### 57. Diagrammatic
**Category:** Data & Technical | **Era:** Timeless | **Complexity:** Medium

> Everything rendered as technical drawings — exploded views, annotation callouts, dimension lines.

- Clean white background, thin precise lines
- Dimension annotations with measurement marks
- Callout arrows and labels
- Technical illustration precision
- **Best for:** Documentation, technical education, engineering portfolios
- **Don't use for:** Consumer apps, playful brands
- **Frameworks:** SVG 10/10, D3.js 9/10
- **A11y:** AA

### 58. Subway / Transit Diagram
**Category:** Data & Technical | **Era:** Timeless | **Complexity:** Medium

> Beck-style schematic abstraction, colored route lines, interchange nodes, simplified topology.

- 45°/90° angle constraint on all lines
- Color-coded routes with circle station nodes
- Simplified topology (not geographic)
- Bold sans-serif labels, clean intersections
- **Best for:** Process flows, step-by-step guides, organizational maps
- **Don't use for:** Free-form content, imagery-heavy sites
- **Frameworks:** SVG 10/10, D3.js 9/10
- **A11y:** AA

### 59. Blueprint / Cyanotype
**Category:** Data & Technical | **Era:** Timeless | **Complexity:** Low

> White-on-blue technical drawing, dimension lines, annotation arrows, construction-document feel.

- Blueprint blue background (#1B3A5C or #003366)
- White/light cyan lines and text
- Grid overlay, dimension markings
- Technical drawing aesthetic
- **Best for:** Architecture firms, manufacturing, project planning
- **Don't use for:** Consumer retail, fashion, entertainment
- **Frameworks:** Vanilla CSS 10/10, SVG 9/10
- **A11y:** AA

### 60. Assembly Instruction
**Category:** Data & Technical | **Era:** Timeless | **Complexity:** Low

> IKEA-style isometric diagrams, numbered callouts, wordless sequencing, minimal line art.

- Clean white background, simple black line art
- Numbered step indicators
- Isometric perspective for 3D representation
- Minimal text, visual-instruction focus
- **Best for:** Product guides, onboarding flows, how-to platforms
- **Don't use for:** Marketing, storytelling, brand campaigns
- **Frameworks:** SVG 10/10, vanilla CSS 8/10
- **A11y:** AA

### 61. Switchboard / Node Editor
**Category:** Data & Technical | **Era:** 2020s | **Complexity:** High

> Jack-socket nodes, patch-cable connections, rack-mount framing, modular routing.

- Dark background with colored connection lines
- Node blocks with input/output ports
- Bezier curve connections between nodes
- Modular, rack-mounted panel layout
- **Best for:** Audio software, visual programming, data pipelines
- **Don't use for:** Content sites, marketing, simple apps
- **Frameworks:** React Flow 10/10, SVG 9/10
- **A11y:** A

### 62. Sports Scoreboard / Instrument Panel
**Category:** Data & Technical | **Era:** Modern | **Complexity:** Medium

> LED dot-matrix numerals, stat tickers, dial gauges, amber-on-dark, dense instrument readouts.

- Dark background with glowing numerals
- Monospace LED-style font (Digital-7, DSEG)
- Segmented displays, indicator lights
- Dense information layout, panel grid
- **Best for:** Sports apps, vehicle telemetry, industrial controls
- **Don't use for:** Consumer retail, creative portfolios
- **Frameworks:** Vanilla CSS 9/10, Canvas 8/10
- **A11y:** AA

### 63. Risograph / Overprint
**Category:** Data & Technical | **Era:** 2020s revival | **Complexity:** Medium

> Misregistered duotone layers, halftone dots, soy-ink grain, intentional overprint color mixing.

- Two-color palette with overlap zone (third color)
- Slight offset between layers (1–3px)
- Halftone dot patterns via radial-gradient
- Grain texture overlay
- **Best for:** Indie publishers, event posters, zine platforms
- **Don't use for:** Corporate, medical, precision-critical
- **Frameworks:** CSS mix-blend-mode 10/10, SVG Filters 8/10
- **A11y:** AA

### 64. Soviet Constructivism
**Category:** Data & Technical | **Era:** 1920s revival | **Complexity:** Medium

> Diagonal compositions, red/black/cream, propaganda poster geometry, photomontage influence.

- Red (#CC0000), black, cream (#F5E6CC) palette
- Diagonal lines and angular compositions
- Heavy condensed typography, all-caps
- Geometric shapes, triangles, circles
- **Best for:** Political campaigns, bold editorial, history education
- **Don't use for:** Subtle brands, minimalist, corporate
- **Frameworks:** CSS Transforms 9/10, Tailwind 7/10
- **A11y:** AA

### 65. Folkloric / Vernacular
**Category:** Data & Technical | **Era:** Timeless | **Complexity:** Medium

> Hand-painted sign aesthetics, regional craft motifs, imperfect geometry, local tradition.

- Warm earthy colors, hand-drawn feel
- Slightly imperfect shapes and borders
- Decorative folk-art border patterns
- Artisan, handcrafted aesthetic
- **Best for:** Artisan marketplaces, cultural tourism, craft brands
- **Don't use for:** Tech startups, minimalist SaaS
- **Frameworks:** Vanilla CSS 9/10, SVG 8/10
- **A11y:** AA

---

## Migration Notes

**Merged entries (old → new):**
- #8 → #3, #10 → #13, #14 → #7, #16 → #21, #19 → #8, #29 → #1, #32 → #1, #35 → #15, #39 → #39, #40 → #47, #42 → #39, #45 → (trimmed into 3D), #51 → #37, #54 → #47, #66/#96 → #29, #74 → #50, #84 → #40, #99 → #35, #118 → #36, #127 → #62, #128 → #20, #132 → #36, #136 → #16, #142 → #41, #147 → #44

**Total: 65 styles** (down from 149 — trimmed 54, merged 25, added 5 not in original styles.html)

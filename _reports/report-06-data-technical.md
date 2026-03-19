# Report 06 -- Data & Technical Styles: B-Side Audit

**Auditor:** UI Designer Agent
**Date:** 2026-03-20
**Scope:** B-side implementation review for 10 data/technical style sample pages
**Verdict:** All 10 B-sides are identical generic templates with zero style authenticity.

---

## Executive Summary

Every single B-side in this batch is generated from the same boilerplate template. The template follows a fixed structure: sticky header, 80vh centered hero with tagline/title/description/two buttons, three generic feature cards, four metrics, a blockquote, and a footer. The only parameterization is (1) background color pulled from the A-side's primary background, (2) a single accent color used for logo/tags/buttons/metrics/icons, and (3) light vs. dark text inversion.

None of the B-sides contain any style-specific visual effects, typography, layout patterns, content vocabulary, or signature design elements from their respective styles. The HTML content is word-for-word identical across all 10 files (and likely all 100 files in the project). The B-sides are functionally indistinguishable from one another aside from color theming.

**Batch average score: 1.5 / 10**

---

## 1. Data-Dense Dashboard (`data-dense-dashboard.html`)

**Style Authenticity Score: 2 / 10**

| Criterion | Assessment |
|---|---|
| **Color Palette** | Background is `#0F172A` (correct slate-900). Accent color is `#1E293B` -- this is the surface color from the A-side, not the blue (#3B82F6) that defines the dashboard style. The accent is dark and nearly invisible against the dark background. This is a **color mapping bug**: the template grabbed the wrong variable. |
| **Typography** | Uses `Inter, system-ui, sans-serif`. Missing the critical `IBM Plex Mono` monospace font that defines dashboard number readouts. No monospace anywhere. |
| **Border Radius** | Generic 8px rounded cards. Correct for a modern dashboard but not differentiated. |
| **Shadows & Depth** | Generic `0 2px 8px rgba(0,0,0,.15)`. No depth hierarchy. A dashboard should have flat, borderline zero-shadow panels to maximize density. |
| **Layout & Spacing** | 80vh hero is the antithesis of data-dense. Enormous whitespace, spacious padding (5rem sections). A data-dense style demands compact grids, tight 12px gaps, and information-first layouts. |
| **Visual Effects** | None. No sparklines, no status indicators, no grid layout, no data tables, no KPI cards, no live-update indicators. |
| **Content & Voice** | "Distinctive by design," "Visual Identity," "Consistent Language" -- entirely generic marketing copy. No ops terminology (latency, RPS, throughput, uptime, error rate). |
| **Missing Elements** | Sparklines, status tags, monospace numbers, compact data tables, KPI metrics with up/down arrows, service status rows, resource usage bars. Everything. |
| **CSS Bugs** | Accent color `#1E293B` on background `#0F172A` has a contrast ratio of roughly 1.5:1 -- essentially invisible. The `.bh .logo`, `.bhero-tag`, `.bst`, `.bmet-v`, `.bcard-icon` all use this near-invisible color. |

---

## 2. Financial Dashboard (`financial-dashboard.html`)

**Style Authenticity Score: 2 / 10**

| Criterion | Assessment |
|---|---|
| **Color Palette** | Background `#0C0F1D` is correct ultra-dark. Accent `#22C55E` (green) is appropriate for a trading "gains" theme. This is the best color mapping in the batch. |
| **Typography** | Uses `Inter, system-ui, sans-serif`. No `IBM Plex Mono` monospace. Trading dashboards are defined by monospace numbers, ticker readouts, and tabular figures. |
| **Border Radius** | 8px rounded cards. Financial dashboards typically use sharper 4px or less for a professional, data-dense look. |
| **Shadows & Depth** | Generic shadows. Trading UIs are flat and dense -- no shadows needed. |
| **Layout & Spacing** | 80vh hero, 5rem section padding. Financial dashboards pack maximum data into minimum space. This layout is the opposite. |
| **Visual Effects** | None. No ticker bar, no candlestick charts, no gain/loss color coding, no scrolling prices, no portfolio allocation bars. |
| **Content & Voice** | Zero financial terminology. No stock symbols, no P&L language, no "positions," "holdings," "day change," or market data. Generic "Visual Identity" cards instead. |
| **Missing Elements** | Ticker bar with streaming prices, candlestick visualization, holdings table with gain/loss coloring, portfolio allocation bars, monospace price displays, red/green color system. |
| **CSS Bugs** | No critical bugs. Green accent on dark background works. |

---

## 3. IDE Theme (`ide-theme.html`)

**Style Authenticity Score: 2 / 10**

| Criterion | Assessment |
|---|---|
| **Color Palette** | Background `#282C34` is correct One Dark Pro base. Accent `#61AFEF` (blue) is the correct IDE blue. Good color choice. |
| **Typography** | Uses `Inter, system-ui, sans-serif`. An IDE theme absolutely demands `Fira Code` or another monospace font as the primary typeface. This is the single most defining trait of the style, and it is absent. |
| **Border Radius** | 8px rounded cards. IDE windows use sharp corners (0-2px) or no radius at all. The rounded cards feel completely wrong. |
| **Shadows & Depth** | Generic card shadows. IDEs have flat panel boundaries defined by borders, not shadows. |
| **Layout & Spacing** | 80vh centered hero. IDEs are characterized by three-panel layouts: sidebar, editor, and minimap. No trace of this. |
| **Visual Effects** | None. No syntax highlighting, no line numbers, no tab bar, no file tree, no status bar, no minimap, no traffic-light window dots. |
| **Content & Voice** | No code, no programming terminology, no file names, no branch indicators, no error/warning counts. |
| **Missing Elements** | Syntax-colored code blocks, line number gutter, tab bar with file names, file explorer sidebar, status bar (branch, language, encoding), minimap, traffic-light dots. Everything that makes an IDE an IDE. |
| **CSS Bugs** | No critical bugs. Colors are well-chosen even if unused effectively. |

---

## 4. Terminal / CLI (`terminal-cli.html`)

**Style Authenticity Score: 2 / 10**

| Criterion | Assessment |
|---|---|
| **Color Palette** | Background `#0D0208` (near-black) is correct. Accent `#00FF41` (matrix green) is the perfect terminal color. |
| **Typography** | Uses `Inter, system-ui, sans-serif`. A terminal style MUST use `Fira Code` or a monospace font exclusively. The A-side correctly loads Fira Code. The B-side ignores it entirely. |
| **Border Radius** | 8px rounded cards. Terminal UIs have zero border radius -- everything is rectilinear. |
| **Shadows & Depth** | Generic shadows with hover float effect (`translateY(-3px)`). Terminals are completely flat with no depth effects. |
| **Layout & Spacing** | 80vh hero centered layout. Terminals are full-width, left-aligned, dense text flows with no centering whatsoever. |
| **Visual Effects** | None. No scanline overlay (the A-side has an excellent `body::after` scanline effect), no blinking cursor, no command prompt symbols, no ASCII art, no progress bars, no text-based UI elements. |
| **Content & Voice** | No command prompts, no `$` or `>` symbols, no file paths, no system output, no technical jargon. "Distinctive by design" is not terminal language. |
| **Missing Elements** | Scanline CRT effect, blinking cursor, command prompt with colored segments, ASCII art, text-based tables, progress bars using block characters, system status output, green-on-black everything. |
| **CSS Bugs** | No critical bugs. The B-side does not inherit the `body::after` scanline overlay, which is actually correct since it uses its own `.b-side` container, but it also does not recreate the effect. |

---

## 5. PCB / Circuit Trace (`pcb-circuit.html`)

**Style Authenticity Score: 2 / 10**

| Criterion | Assessment |
|---|---|
| **Color Palette** | Background `#0A3D0A` (PCB green) is correct. Accent `#B87333` (copper) is the exact right color. Best thematic color pairing in this batch. |
| **Typography** | Uses `Inter, system-ui, sans-serif`. Should be `Share Tech Mono` -- the monospace technical font loaded in the A-side. PCB designs are exclusively monospace with technical lettering. |
| **Border Radius** | 8px rounded cards. PCBs have zero border radius. Components are rectilinear. Solder pads are circular but card containers should be sharp-cornered. |
| **Shadows & Depth** | Generic shadows. PCBs are completely flat (they are literally flat boards). No shadows appropriate. |
| **Layout & Spacing** | 80vh hero. PCB layouts are dense grid-based arrangements. No trace of this. |
| **Visual Effects** | None. No grid overlay (the A-side has a beautiful 24px PCB grid), no copper trace borders, no solder dot circles, no component designators (U1, R1, C1), no via holes, no silkscreen text. |
| **Content & Voice** | No electronics vocabulary. No "schematic," "BOM," "gerber," "trace," "via," "pad," "component" terminology. |
| **Missing Elements** | PCB grid background, copper trace line borders, solder dot decorations on corners, component designator labels, silkscreen-style text, DRC pass/fail indicators, layer indicators (TOP/BOTTOM). |
| **CSS Bugs** | No critical bugs. |

---

## 6. Scoreboard / Instrument Panel (`scoreboard.html`)

**Style Authenticity Score: 1 / 10**

| Criterion | Assessment |
|---|---|
| **Color Palette** | Background `#0A0A0A` is correct (near-black). Accent is `#FF4444` -- a red that is somewhat appropriate but the A-side's primary accent is amber `#FF9500`. The scoreboard style is defined by amber LED glow, not red. Incorrect accent choice. |
| **Typography** | Uses `Inter, system-ui, sans-serif`. Should be `VT323` (pixel/LED font) and `Russo One` (bold display). The A-side loads both. These fonts are the essence of the scoreboard look. |
| **Border Radius** | 8px rounded cards. Scoreboards use sharp-cornered rectangular panels (0-4px max). The instrument panel aesthetic is boxy. |
| **Shadows & Depth** | Generic shadows. Scoreboard elements should have `text-shadow` LED glow effects (`0 0 20px rgba(255,149,0,.5)`), not box shadows. |
| **Layout & Spacing** | 80vh hero. Scoreboards are dense instrument readouts with compact gauges, not spacious marketing layouts. |
| **Visual Effects** | None. No LED text-shadow glow, no seven-segment digit styling, no gauge bars, no indicator lights, no dot-matrix feel, no score display. |
| **Content & Voice** | No sports/instrument terminology. No "QTR," "FG%," "3PT%," no team names, no time displays, no stat readouts. |
| **Missing Elements** | LED glow text-shadow effects, seven-segment or pixel font digits, score display with team names, stat ticker, gauge bars, indicator light dots, amber-on-black color scheme. |
| **CSS Bugs** | The `.bh .logo` uses `#FF4444` but the A-side's `.logo` uses `font-family: 'Russo One'` and `color: var(--amber)` -- neither is reflected. |

---

## 7. Blueprint / Cyanotype (`blueprint.html`)

**Style Authenticity Score: 2 / 10**

| Criterion | Assessment |
|---|---|
| **Color Palette** | Background `#1B3A5C` is the correct deep cyanotype blue. Accent is `#FFFFFF` (white) which is technically correct -- blueprints use white lines on blue. However, using white as an accent makes the B-side feel generic and unstyled rather than distinctly blueprint. |
| **Typography** | Uses `Inter, system-ui, sans-serif`. Should be `JetBrains Mono` -- the precise, technical monospace font loaded in the A-side. Blueprint text is exclusively monospace engineering lettering. |
| **Border Radius** | 8px rounded cards. Blueprints have zero border radius. Everything is straight-edged, technical, and precise. Rounded corners contradict the entire aesthetic. |
| **Shadows & Depth** | Generic shadows. Blueprints are entirely flat -- they are 2D technical drawings. No depth whatsoever. |
| **Layout & Spacing** | 80vh hero. Blueprints maximize the drawing area with dense technical information. |
| **Visual Effects** | None. No grid overlay (the A-side has an excellent multi-scale grid using `body::before`), no dimension annotation lines, no room/floorplan outlines, no scale indicators, no section markers. |
| **Content & Voice** | No architectural or engineering terminology. No dimensions ("24'-6\""), no scale references ("1:48"), no section views, no detail callouts. |
| **Missing Elements** | Multi-scale grid background, dimension lines with arrows, floorplan/technical drawings, scale indicator, section view labels (A-A, B-B), white-line-only aesthetic, engineering text labels. |
| **CSS Bugs** | No backdrop-filter on header (uses `background:#1B3A5Cee` which will work). No significant bugs but the white-on-blue scheme lacks the grid that makes it read as "blueprint." |

---

## 8. Switchboard / Node Editor (`switchboard.html`)

**Style Authenticity Score: 1 / 10**

| Criterion | Assessment |
|---|---|
| **Color Palette** | Background `#1A1A2E` is correct dark purple-navy. Accent is `#FF6B6B` -- a coral/salmon red that does not match any color from the A-side's palette. The A-side uses green (`#44CC66`), blue (`#4488FF`), yellow (`#FFCC33`), and red (`#FF4444`). The chosen accent fails to represent the multi-color port system that defines node editors. |
| **Typography** | Uses `Inter, system-ui, sans-serif`. Should be `Space Mono` -- the monospace font loaded in the A-side. Node editors are technical tools with monospace text. |
| **Border Radius** | 8px rounded cards. Passable -- node editors do use 4-6px radius on node panels. Slightly too round but not egregiously wrong. |
| **Shadows & Depth** | Generic shadows. Node editors use subtle panel depth but the signature visual is cable/connection lines between nodes, not card shadows. |
| **Layout & Spacing** | 80vh hero. Node editors are canvas-based with draggable nodes, not centered marketing layouts. |
| **Visual Effects** | None. No node panels with headers and ports, no colored port dots, no cable/connection lines, no knob controls, no rack-mount grid lines, no status LEDs, no patch connections. |
| **Content & Voice** | No audio/signal processing vocabulary. No "oscillator," "filter," "frequency," "CV," "patch," "module," "gain," "dB" terminology. |
| **Missing Elements** | Node panels with input/output ports, colored port jacks, cable connections between nodes, knob dials, rack-mount horizontal lines, status LEDs, multi-color port system (red/green/blue/yellow/purple). |
| **CSS Bugs** | No critical bugs but the accent color choice `#FF6B6B` does not appear in the A-side's design system at all. |

---

## 9. Diagrammatic (`diagrammatic.html`)

**Style Authenticity Score: 2 / 10**

| Criterion | Assessment |
|---|---|
| **Color Palette** | Background `#FFFFFF` is correct. Accent is `#333333` -- a generic dark gray. The A-side's signature colors are red callouts `#E63946` and blue accent `#457B9D`. Neither is used. The B-side looks like an unstyled default. |
| **Typography** | Uses `Inter, system-ui, sans-serif`. Should be `IBM Plex Mono` (primary) with `IBM Plex Sans` for headings. The diagrammatic style demands a precise, technical monospace font. |
| **Border Radius** | 8px rounded cards. Diagrammatic style uses zero border radius -- everything is precise rectangles, like technical drawings. |
| **Shadows & Depth** | `0 2px 8px rgba(0,0,0,.06)` -- faint generic shadows. Diagrammatic uses hairline 0.5px borders with no shadows. The aesthetic is flat technical illustration. |
| **Layout & Spacing** | 80vh hero, centered. Diagrammatic style should be annotation-heavy with dimension lines, callout markers, and exploded views. |
| **Visual Effects** | None. No dimension lines, no red callout dots, no annotation markers (A, B, C circles), no exploded view diagrams, no 20px measurement grid, no dashed leader lines. |
| **Content & Voice** | No technical illustration language. No "Detail A," "Rev. 03," "Fig. 2," "tolerance," "cross-reference," or dimension measurements. |
| **Missing Elements** | Red callout circles with letters, dimension lines with measurements, exploded view diagrams, annotation leaders, thin 0.5px borders, 20px background grid, part numbering system. |
| **CSS Bugs** | No critical bugs, but the B-side does not have `backdrop-filter:blur()` on the header (just solid white background). Minor inconsistency with other B-sides. |

---

## 10. Assembly Instruction (`assembly-instruction.html`)

**Style Authenticity Score: 2 / 10**

| Criterion | Assessment |
|---|---|
| **Color Palette** | Background `#FFFFFF` is correct. Accent is `#333333` -- generic dark gray. The A-side's signature IKEA blue is `#2D7DD2` and caution yellow is `#FFD23F`. Neither characteristic color is present. |
| **Typography** | Uses `Inter, system-ui, sans-serif`. The A-side also uses Inter, so this is actually correct for once. However, the B-side does not use the specific weight range (300/400/600/800) that gives the assembly instruction style its distinctive light-to-heavy contrast. |
| **Border Radius** | 8px rounded cards. The A-side also uses 8-10px radius. This is one of the few B-sides where the border radius is appropriate. |
| **Shadows & Depth** | `0 2px 8px rgba(0,0,0,.06)`. Assembly instructions use flat, clean, minimal shadow. The shadow is present but subtle enough to be acceptable. |
| **Layout & Spacing** | 80vh hero, centered. Assembly instructions use step-by-step horizontal flows, numbered sequences, and illustration-heavy layouts -- not centered hero blocks. |
| **Visual Effects** | None. No numbered step circles (blue circle with white number), no isometric box illustrations, no dashed connector arrows between steps, no callout warning bubbles, no step-by-step flow. |
| **Content & Voice** | No assembly language. No "Step 1," "Unpack," "Align," no part numbers, no safety callouts ("Two persons recommended"), no "Verify all parts." |
| **Missing Elements** | Blue numbered step indicators, isometric/exploded part illustrations, dashed arrow connectors, yellow warning callout bubble, step sequence horizontal flow, part number references, wordless instruction aesthetic. |
| **CSS Bugs** | No critical bugs. The B-side is clean but completely generic. |

---

## Cross-Cutting Findings

### The Template Problem

All 10 B-sides share identical:

1. **HTML structure**: `bh` (header) > `bhero` (hero) > `bsec` (features with `bgrid`/`bcard`) > `bsec` (metrics with `bmets`) > `bsec` (quote with `bquote`) > `bfoot` (footer)
2. **Content copy**: "Distinctive by design," "What Sets Us Apart," "Visual Identity," "Consistent Language," "Authentic Detail," "Numbers Speak," "100% Authentic, Unique Voice, Bold Statement, Distinct"
3. **Layout pattern**: 80vh centered hero, 1100px max-width container, auto-fit 280px min card grid, 140px min metrics grid
4. **Interaction pattern**: `translateY(-3px)` hover on cards, `translateY(-1px)` hover on primary button
5. **Class naming**: All use `.bh`, `.bhero`, `.bsec`, `.bcon`, `.bgrid`, `.bcard`, `.bmets`, `.bmet-v`, `.bmet-l`, `.bquote`, `.bfoot`, `.bbtn`, `.bbtn-p`, `.bbtn-s`

### What the Template Gets Right

- Background color is pulled from each style (7/10 are correct)
- Accent color is attempted (5/10 are reasonable choices)
- Light vs. dark mode inversion works for text readability
- Responsive breakpoint at 768px is consistent
- No CSS syntax errors in any B-side

### What the Template Gets Wrong (Universally)

| Issue | Impact |
|---|---|
| **No style-specific fonts** | 9/10 should use monospace; 0/10 do |
| **No signature visual effects** | 0/10 have scanlines, grids, glows, traces, or other effects |
| **Generic marketing content** | 0/10 have domain-appropriate vocabulary |
| **Spacious hero layout** | 10/10 use 80vh hero; most styles demand dense/compact layouts |
| **Rounded 8px cards** | 8/10 styles demand sharper or zero radius |
| **No style-specific components** | 0/10 have sparklines, code blocks, nodes, gauges, steps, etc. |
| **Identical HTML** | Content is word-for-word the same across all 10 files |

### Color Mapping Bugs

| File | Expected Accent | Actual Accent | Issue |
|---|---|---|---|
| data-dense-dashboard | `#3B82F6` (blue) | `#1E293B` (surface) | Nearly invisible; wrong variable grabbed |
| scoreboard | `#FF9500` (amber) | `#FF4444` (red) | Wrong signature color; amber defines the style |
| switchboard | `#44CC66` (green) | `#FF6B6B` (coral) | Color not in A-side palette at all |
| diagrammatic | `#E63946` (red) | `#333333` (gray) | Lost the signature callout red entirely |
| assembly-instruction | `#2D7DD2` (blue) | `#333333` (gray) | Lost the signature IKEA blue |

---

## Scoring Summary

| # | Style | Score | Primary Failure |
|---|---|---|---|
| 1 | Data-Dense Dashboard | 2/10 | Invisible accent color; no data density |
| 2 | Financial Dashboard | 2/10 | No financial data, no monospace, no ticker |
| 3 | IDE Theme | 2/10 | No code, no monospace, no IDE layout |
| 4 | Terminal / CLI | 2/10 | No monospace, no scanlines, no prompts |
| 5 | PCB / Circuit Trace | 2/10 | No grid, no traces, no monospace |
| 6 | Scoreboard | 1/10 | Wrong accent, no LED glow, no pixel font |
| 7 | Blueprint | 2/10 | No grid, no dimension lines, no monospace |
| 8 | Switchboard | 1/10 | Wrong accent color, no nodes/ports/cables |
| 9 | Diagrammatic | 2/10 | Generic gray, no callouts, no dimension lines |
| 10 | Assembly Instruction | 2/10 | Generic gray, no steps, no IKEA blue |

**Batch Average: 1.8 / 10**

---

## Recommendations

1. **Font loading**: Each B-side must load and use the same Google Font as its A-side. For 9/10 of these styles, monospace is mandatory.
2. **Signature effects**: Each B-side needs at minimum one signature CSS effect from its A-side (grid overlays, scanlines, LED glow, copper trace borders, etc.).
3. **Content rewrite**: Replace the generic "Distinctive by design" copy with domain-appropriate vocabulary drawn from each style's A-side.
4. **Layout adaptation**: Dense/technical styles should not use 80vh hero sections. Compact grid layouts with real data components are essential.
5. **Accent color audit**: Fix the 5 incorrect accent color mappings identified above.
6. **Border radius per style**: Technical/data styles generally demand 0-4px radius, not the universal 8px.
7. **Component parity**: Each B-side should include at least one signature component adapted from the A-side (sparkline, code block, node panel, gauge, step sequence, etc.).

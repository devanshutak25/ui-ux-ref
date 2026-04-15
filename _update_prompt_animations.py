#!/usr/bin/env python3
"""Update AI prompts in styles.html with animation documentation.

Adds detailed animation philosophy and specific animation descriptions
to the Effects & Animation section of each style's prompt.
"""

import re
import os

STYLES_FILE = "styles.html"

# Import category mapping and descriptions from the animation script
STYLE_CAT = {
    "minimalism": "subtle", "flat-design": "subtle", "inclusive-design": "subtle",
    "mono-space": "subtle", "whitespace-maximalism": "subtle", "bento-grid": "subtle",
    "conversion-optimized": "subtle", "e-ink": "subtle", "single-color": "subtle",
    "cyberpunk": "neon", "dark-mode": "neon", "neon-sign": "neon",
    "bioluminescent": "neon", "holographic": "neon", "vaporwave": "neon",
    "stage-lighting": "neon", "neon-calligraphy": "neon", "chromatic-aberration": "neon",
    "retrocomputing": "retro", "cassette-futurism": "retro", "terminal-cli": "retro",
    "ide-theme": "retro", "scoreboard": "retro", "split-flap": "retro",
    "y2k": "retro", "vintage-analog": "retro", "retro-futurism": "retro",
    "glassmorphism": "glass", "ice-crystalline": "glass", "dimensional-layering": "glass",
    "gradient-mesh": "glass", "spatial-ui": "glass", "lenticular": "glass",
    "organic-biophilic": "organic", "solarpunk": "organic", "watercolor-ui": "organic",
    "wabi-sabi": "organic", "terrazzo": "organic", "folkloric": "organic",
    "brutalism": "bold", "neubrutalism": "bold", "constructivism": "bold",
    "bauhaus": "bold", "op-art": "bold", "vibrant-blocks": "bold",
    "memphis": "bold", "gen-z-chaos": "bold",
    "risograph": "craft", "collage-zine": "craft", "woodcut": "craft",
    "chalkboard": "craft", "embroidery": "craft", "stained-glass": "craft",
    "mosaic": "craft", "ukiyo-e": "craft", "camouflage": "craft",
    "claymorphism": "depth", "neumorphism": "depth", "skeuomorphism": "depth",
    "isometric-ui": "depth", "diorama": "depth", "origami": "depth",
    "paper-cut": "depth", "tactile-ui": "depth",
    "candy-ui": "playful", "comic-panel": "playful", "trading-card": "playful",
    "psychedelic": "playful", "astrological": "playful", "pixel-art": "playful",
    "polaroid": "playful", "scratch-card": "playful",
    "data-dense-dashboard": "tech", "financial-dashboard": "tech",
    "hud-fui": "tech", "ai-native": "tech", "blueprint": "tech",
    "pcb-circuit": "tech", "diagrammatic": "tech", "subway-map": "tech",
    "switchboard": "tech", "wireframe-mesh": "tech",
    "art-deco": "luxury", "marble": "luxury", "film-noir": "luxury",
    "cinematic": "luxury", "hyperrealism": "luxury", "blackletter": "luxury",
    "kinetic-typography": "motion", "motion-driven": "motion",
    "parallax-storytelling": "motion", "particle-cloud": "motion",
    "newspaper": "print", "editorial-grid": "print", "passport": "print",
    "receipt": "print", "assembly-instruction": "print", "pharmaceutical": "print",
    "whiteboard": "print", "cartographic": "print",
}

CATEGORY_ANIM_DESC = {
    "subtle": "Minimal, purposeful motion. Entrance animations use soft fade-and-slide with staggered timing (hero tag at 0.1s, heading at 0.2s, paragraph at 0.5s, buttons at 0.7s). Hover states use gentle vertical elevation (-6px translateY). No continuous animations — stillness IS the brand. Transitions: 300ms ease. Maximum restraint.",
    "neon": "Neon-pulsing energy. Hero elements fade in with dramatic stagger. Metrics and step numbers pulse with a 3s glow cycle (bPulse). Logo flickers like a neon tube (bFlicker 6s). Cards gain a luminous glow box-shadow on hover. Featured pricing card floats with bFloat (4s). FAQ summaries get text-shadow glow on hover. Motion is electric but controlled.",
    "retro": "Stepped, digital motion. Animations use steps() timing functions to feel pixelated and mechanical (bPulse 2s steps(3)). Metrics pulse in discrete steps. Featured card pulses in 5-step increments. Transitions feel snappy and quantized. Tabular-nums for clean number alignment. Nothing is smooth — everything is deliberately digitized.",
    "glass": "Floating, weightless motion. Cards rise 8px and scale 1.01x on hover with deep shadow (0 12px 40px). Uses cubic-bezier(.16,1,.3,1) for springy, overshooting easing. Metrics glow with bGlow (3s brightness cycle). Featured card floats with bFloat (5s). Everything feels suspended in transparent layers.",
    "organic": "Breathing, living motion. Elements use bBreathe (4-5s scale cycle) for a living pulse. Cards drift and rotate 0.5deg on hover like leaves. Metrics breathe at 4s, process numbers at 5s. Nothing mechanical — every movement feels alive. Timing is relaxed with ease-in-out curves.",
    "bold": "Punchy, immediate impact. No fade-ins on metrics — elements stamp in with bScaleIn. Cards shift with translate(3px,3px) on hover (no easing needed). Featured card scales to 1.08x for dominance. FAQ items punch 4px sideways on hover. Transitions at 150ms for snap. Motion is blunt and unapologetic.",
    "craft": "Handmade, imperfect motion. Cards lift -4px and tilt -0.5deg on hover, like physical objects being examined. Featured card breathes slowly (bBreathe 5s). Elements fade in gently. FAQ items shift 4px right on hover. Transitions at 350ms ease for a considered, unhurried feel. Motion suggests a human hand.",
    "depth": "Elevation-driven motion. Cards rise -8px on hover, enhancing shadow depth. Process numbers glow (bGlow 3s) to suggest luminous surfaces. Featured card floats (bFloat 5s) to push forward in z-space. Metrics scale in to emerge from the surface. All transitions at 350ms to feel physical.",
    "playful": "Bouncy, joyful motion. Metrics bounce continuously (bBounce 2s). Process numbers wiggle (bWiggle 3s). Cards lift -8px and rotate -1deg on hover. FAQ items leap 6px sideways. Uses cubic-bezier(.16,1,.3,1) for spring physics. Featured card bounces at 3s cycle. UI feels alive and delighted.",
    "tech": "Precise, data-driven motion. Metrics pulse at measured 2s rate (bPulse). Numbers use tabular-nums for grid alignment. Cards elevate -4px subtly on hover. Featured card glows (bGlow 3s) steadily. Process numbers use font-variant for clean data display. Transitions at 250ms. Motion is measured and clinical.",
    "luxury": "Slow, deliberate elegance. Metrics fade in over 1s with 0.3s delay. Process numbers fade in over 0.8s. Hover transitions are languid (500ms). FAQ hover shifts letter-spacing 0.3px for a refined micro-detail. Featured card glows slowly (bGlow 4s). Motion whispers, never shouts. Every movement earns its moment.",
    "motion": "Kinetic, expressive motion. Cards scale 1.02x and lift -8px on hover with spring easing. Metrics bounce energetically (bBounce 2.5s). Process numbers float freely (bFloat 3s). FAQ items slide 8px on hover. Uses cubic-bezier(.16,1,.3,1) throughout for overshooting spring physics. Motion IS the design.",
    "print": "Subdued, editorial motion. Elements fade up 24px gently (bFadeUp). Cards lift -4px modestly on hover. No continuous animations — static media come alive with minimum motion. Process numbers fade in. Featured card uses a thicker border instead of animation. Transitions at 300ms. Functional, not decorative.",
}

# Common entrance animation spec (same for all)
ENTRANCE_SPEC = """
### Entrance Animations (Staggered Hero Sequence)
~~~css
.hero-tag:     fade-in 0.6s ease, delay 0.1s
.hero-heading: fade-up 0.8s cubic-bezier(.16,1,.3,1), delay 0.2s
.hero-text:    fade-in 0.6s ease, delay 0.5s
.hero-buttons: fade-up 0.6s ease, delay 0.7s
.process-step: scale-in 0.5s ease, staggered 0.15s per step
.cta-section:  fade-up 0.6s ease, delay 0.3s
~~~
All entrance animations use animation-fill-mode: forwards with opacity: 0 initial state."""


def get_style_slug(name):
    """Convert style name to file slug."""
    slug = name.lower()
    slug = re.sub(r'[^a-z0-9]+', '-', slug)
    slug = slug.strip('-')
    # Handle common name → slug mappings
    replacements = {
        'minimalism-swiss-style': 'minimalism',
        'dark-mode-oled': 'dark-mode',
        'e-ink-paper': 'e-ink',
        'candy-ui-confectionery': 'candy-ui',
        'vibrant-block-based': 'vibrant-blocks',
        'gradient-mesh-aurora': 'gradient-mesh',
        'holographic-iridescent': 'holographic',
        'bento-box-grid': 'bento-grid',
        'editorial-grid-magazine': 'editorial-grid',
        'comic-panel-layout': 'comic-panel',
        'data-dense-dashboard': 'data-dense-dashboard',
        'cassette-futurism-frutiger-aero': 'cassette-futurism',
        'gen-z-chaotic-maximalism': 'gen-z-chaos',
        'ai-native-ui': 'ai-native',
        'hud-fui-sci-fi-interface': 'hud-fui',
        'hud-sci-fi-fui': 'hud-fui',
        'subway-transit-diagram': 'subway-map',
        'sports-scoreboard-instrument-panel': 'scoreboard',
        'soviet-constructivism': 'constructivism',
        'japanese-minimalism-wabi-sabi': 'wabi-sabi',
        '3d-hyperrealism': 'hyperrealism',
        'mosaic-tesserae': 'mosaic',
        'woodcut-linocut': 'woodcut',
        'marble-veined-stone': 'marble',
        'blackletter-gothic': 'blackletter',
        'embroidery-cross-stitch': 'embroidery',
        'ice-crystalline': 'ice-crystalline',
        'origami-paper-fold': 'origami',
        'pcb-circuit-trace': 'pcb-circuit',
        'ukiyo-e-digital': 'ukiyo-e',
        'camouflage-dpm': 'camouflage',
        'chromatic-aberration': 'chromatic-aberration',
        'vintage-analog-tape': 'vintage-analog',
        'polaroid-instant-film': 'polaroid',
        'neon-calligraphy': 'neon-calligraphy',
        'kinetic-typography': 'kinetic-typography',
        'parallax-storytelling': 'parallax-storytelling',
        'motion-driven-ui': 'motion-driven',
        'stage-lighting-spotlight': 'stage-lighting',
        'conversion-optimized-saas': 'conversion-optimized',
    }
    for long, short in replacements.items():
        if slug.startswith(long[:10]):
            return short
    return slug


def main():
    with open(STYLES_FILE, 'r', encoding='utf-8') as f:
        content = f.read()

    # Find all style names and their aiPrompt positions
    # Pattern: name:"StyleName",...aiPrompt:`...`
    updated = 0
    # Find each style's effects section in the prompt
    # We need to find "## Effects & Animation" and replace/enhance it

    # Strategy: find each aiPrompt backtick block, extract style name,
    # look up category, replace Effects & Animation section

    # Find all name:"X" entries
    name_matches = list(re.finditer(r'name:"([^"]+)"', content))

    for nm in reversed(name_matches):  # reverse to avoid position shifts
        style_name = nm.group(1)
        slug = get_style_slug(style_name)
        cat = STYLE_CAT.get(slug)

        if not cat:
            # Try without some common suffixes
            for k, v in STYLE_CAT.items():
                if slug.startswith(k) or k.startswith(slug[:8]):
                    cat = v
                    break

        if not cat:
            print(f"  ? No category for: {style_name} (slug: {slug})")
            continue

        anim_desc = CATEGORY_ANIM_DESC[cat]

        # Find the Effects & Animation section in this style's prompt
        # It's between nm.start() and the next name:" or end of styles array
        # Look for "## Effects & Animation\n{old_text}\n\n##" pattern

        # Find the aiPrompt for this style (starts after the name match)
        prompt_start = content.find('aiPrompt:`', nm.start())
        if prompt_start < 0:
            continue

        # Find end of this prompt
        pos = prompt_start + len('aiPrompt:`')
        while pos < len(content):
            if content[pos] == '\\':
                pos += 2
                continue
            if content[pos] == '`':
                break
            pos += 1
        prompt_end = pos

        prompt_text = content[prompt_start + len('aiPrompt:`'):prompt_end]

        # Find and replace the Effects & Animation section
        old_effects = re.search(
            r'(## Effects & Animation\n)(.*?)(\n\n(?:##|\n## |</design-system>))',
            prompt_text, re.DOTALL
        )

        if old_effects:
            old_line = old_effects.group(2).strip()
            # Skip if already has animation docs
            if 'Animation Philosophy' in old_line:
                continue
            new_section = f"""### Animation Philosophy
{anim_desc}
{ENTRANCE_SPEC}

### Style-Specific Effects
{old_line}"""

            new_prompt = (prompt_text[:old_effects.start(2)] +
                         new_section +
                         prompt_text[old_effects.end(2):])

            # Replace in content
            full_old = 'aiPrompt:`' + prompt_text + '`'
            full_new = 'aiPrompt:`' + new_prompt + '`'
            content = content.replace(full_old, full_new, 1)
            updated += 1

    with open(STYLES_FILE, 'w', encoding='utf-8') as f:
        f.write(content)

    print(f"Done: {updated} prompts updated with animation docs")


if __name__ == '__main__':
    main()

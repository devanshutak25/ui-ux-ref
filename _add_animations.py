#!/usr/bin/env python3
"""Add per-style animations to all B-sides.

Each style gets:
1. Shared entrance keyframes (fade, slide, scale)
2. Category-specific ongoing/hover animations
3. Staggered hero entrance sequence
4. Enhanced card/pricing/FAQ interactions
5. Style-matched decorative motion

13 animation categories, 100 styles mapped.
Skips elements that already have animations.
"""

import re
import os
import glob

SAMPLES_DIR = "samples"
STYLES_FILE = "styles.html"
ANIM_MARKER = "/* ANIM-system */"

# ---------------------------------------------------------------------------
# Keyframes — only added if not already present in the file
# ---------------------------------------------------------------------------
KEYFRAMES = {
    "bFadeUp": "@keyframes bFadeUp{from{opacity:0;transform:translateY(24px)}to{opacity:1;transform:translateY(0)}}",
    "bFadeIn": "@keyframes bFadeIn{from{opacity:0}to{opacity:1}}",
    "bScaleIn": "@keyframes bScaleIn{from{opacity:0;transform:scale(.92)}to{opacity:1;transform:scale(1)}}",
    "bFloat": "@keyframes bFloat{0%,100%{transform:translateY(0)}50%{transform:translateY(-8px)}}",
    "bPulse": "@keyframes bPulse{0%,100%{opacity:1}50%{opacity:.7}}",
    "bGlow": "@keyframes bGlow{0%,100%{filter:brightness(1)}50%{filter:brightness(1.2)}}",
    "bFlicker": "@keyframes bFlicker{0%,19%,21%,23%,25%,54%,56%,100%{opacity:1}20%{opacity:.4}24%{opacity:.7}55%{opacity:.5}}",
    "bBreathe": "@keyframes bBreathe{0%,100%{transform:scale(1)}50%{transform:scale(1.03)}}",
    "bBounce": "@keyframes bBounce{0%,100%{transform:translateY(0)}50%{transform:translateY(-6px)}}",
    "bWiggle": "@keyframes bWiggle{0%,100%{transform:rotate(0)}25%{transform:rotate(-2deg)}75%{transform:rotate(2deg)}}",
}

# ---------------------------------------------------------------------------
# Style → Category mapping (100 styles)
# ---------------------------------------------------------------------------
STYLE_CAT = {
    # subtle — clean, minimal
    "minimalism": "subtle", "flat-design": "subtle", "inclusive-design": "subtle",
    "mono-space": "subtle", "whitespace-maximalism": "subtle", "bento-grid": "subtle",
    "conversion-optimized": "subtle", "e-ink": "subtle", "single-color": "subtle",

    # neon — dark + neon/glow
    "cyberpunk": "neon", "dark-mode": "neon", "neon-sign": "neon",
    "bioluminescent": "neon", "holographic": "neon", "vaporwave": "neon",
    "stage-lighting": "neon", "neon-calligraphy": "neon", "chromatic-aberration": "neon",

    # retro — CRT/terminal/vintage digital
    "retrocomputing": "retro", "cassette-futurism": "retro", "terminal-cli": "retro",
    "ide-theme": "retro", "scoreboard": "retro", "split-flap": "retro",
    "y2k": "retro", "vintage-analog": "retro", "retro-futurism": "retro",

    # glass — transparent/floating/depth
    "glassmorphism": "glass", "ice-crystalline": "glass", "dimensional-layering": "glass",
    "gradient-mesh": "glass", "spatial-ui": "glass", "lenticular": "glass",

    # organic — nature/soft
    "organic-biophilic": "organic", "solarpunk": "organic", "watercolor-ui": "organic",
    "wabi-sabi": "organic", "terrazzo": "organic", "folkloric": "organic",

    # bold — high-contrast graphic
    "brutalism": "bold", "neubrutalism": "bold", "constructivism": "bold",
    "bauhaus": "bold", "op-art": "bold", "vibrant-blocks": "bold",
    "memphis": "bold", "gen-z-chaos": "bold",

    # craft — textured/handmade
    "risograph": "craft", "collage-zine": "craft", "woodcut": "craft",
    "chalkboard": "craft", "embroidery": "craft", "stained-glass": "craft",
    "mosaic": "craft", "ukiyo-e": "craft", "camouflage": "craft",

    # depth — 3D/material/tactile
    "claymorphism": "depth", "neumorphism": "depth", "skeuomorphism": "depth",
    "isometric-ui": "depth", "diorama": "depth", "origami": "depth",
    "paper-cut": "depth", "tactile-ui": "depth",

    # playful — fun/whimsical
    "candy-ui": "playful", "comic-panel": "playful", "trading-card": "playful",
    "psychedelic": "playful", "astrological": "playful", "pixel-art": "playful",
    "polaroid": "playful", "scratch-card": "playful",

    # tech — data/dashboard/HUD
    "data-dense-dashboard": "tech", "financial-dashboard": "tech",
    "hud-fui": "tech", "ai-native": "tech", "blueprint": "tech",
    "pcb-circuit": "tech", "diagrammatic": "tech", "subway-map": "tech",
    "switchboard": "tech", "wireframe-mesh": "tech",

    # luxury — elegant/cinematic
    "art-deco": "luxury", "marble": "luxury", "film-noir": "luxury",
    "cinematic": "luxury", "hyperrealism": "luxury", "blackletter": "luxury",

    # motion — kinetic/parallax
    "kinetic-typography": "motion", "motion-driven": "motion",
    "parallax-storytelling": "motion", "particle-cloud": "motion",

    # print — document/editorial
    "newspaper": "print", "editorial-grid": "print", "passport": "print",
    "receipt": "print", "assembly-instruction": "print", "pharmaceutical": "print",
    "whiteboard": "print", "cartographic": "print",
}

# ---------------------------------------------------------------------------
# Category animation templates
# Each has: entrance overrides, ongoing, hover, and featured effects
# GLOW is replaced with the style's glow color at generation time
# ---------------------------------------------------------------------------

# Entrance animations (common base, applied to all categories)
# Each rule is (selector, css_properties)
ENTRANCE_RULES = [
    (".bhero-tag",  "opacity:0;animation:bFadeIn .6s ease .1s forwards"),
    (".bhero h1",   "opacity:0;animation:bFadeUp .8s cubic-bezier(.16,1,.3,1) .2s forwards"),
    (".bhero p",    "opacity:0;animation:bFadeIn .6s ease .5s forwards"),
    (".bhero-btns", "opacity:0;animation:bFadeUp .6s ease .7s forwards"),
    (".bstep",      "opacity:0;animation:bScaleIn .5s ease forwards"),
    (".bstep:nth-child(2)", "animation-delay:.15s"),
    (".bstep:nth-child(3)", "animation-delay:.3s"),
    (".bcta-inner", "opacity:0;animation:bFadeUp .6s ease .3s forwards"),
]

# Category-specific rules: (selector, css_properties)
# Applied AFTER entrance rules, only if selector doesn't already have the property
CATEGORY_RULES = {
    "subtle": [
        (".bcard", "transition:transform .3s ease,box-shadow .3s ease"),
        (".bcard:hover", "transform:translateY(-6px)"),
        (".bprice-card:hover", "transform:translateY(-6px)"),
        (".bfaq-item summary", "transition:opacity .2s ease"),
        (".bfaq-item summary:hover", "opacity:.8"),
    ],
    "neon": [
        (".bcard", "transition:transform .3s ease,box-shadow .3s ease"),
        (".bcard:hover", "transform:translateY(-6px);box-shadow:0 0 24px GLOW"),
        (".bmet-v", "animation:bPulse 3s ease-in-out infinite"),
        (".bstep-num", "animation:bPulse 3s ease-in-out infinite"),
        (".bprice-card.bfeatured", "animation:bFloat 4s ease-in-out infinite"),
        (".bfaq-item summary", "transition:text-shadow .2s ease"),
        (".bfaq-item summary:hover", "text-shadow:0 0 8px GLOW"),
        (".bh .logo", "animation:bFlicker 6s ease-in-out infinite"),
    ],
    "retro": [
        (".bcard", "transition:transform .2s ease"),
        (".bcard:hover", "transform:translateY(-4px)"),
        (".bmet-v", "animation:bPulse 2s steps(3) infinite"),
        (".bstep-num", "font-variant-numeric:tabular-nums"),
        (".bprice-card.bfeatured", "animation:bPulse 3s steps(5) infinite"),
        (".bfaq-item summary", "transition:opacity .15s steps(2)"),
        (".bfaq-item summary:hover", "opacity:.8"),
    ],
    "glass": [
        (".bcard", "transition:transform .4s cubic-bezier(.16,1,.3,1),box-shadow .4s ease"),
        (".bcard:hover", "transform:translateY(-8px) scale(1.01);box-shadow:0 12px 40px rgba(0,0,0,.15)"),
        (".bmet-v", "animation:bGlow 3s ease-in-out infinite"),
        (".bprice-card.bfeatured", "animation:bFloat 5s ease-in-out infinite"),
        (".bfaq-item summary", "transition:opacity .3s ease"),
        (".bfaq-item summary:hover", "opacity:.85"),
    ],
    "organic": [
        (".bcard", "transition:transform .4s ease"),
        (".bcard:hover", "transform:translateY(-6px) rotate(.5deg)"),
        (".bmet-v", "animation:bBreathe 4s ease-in-out infinite"),
        (".bstep-num", "animation:bBreathe 5s ease-in-out infinite"),
        (".bprice-card.bfeatured", "animation:bBreathe 4s ease-in-out infinite"),
        (".bfaq-item summary", "transition:opacity .3s ease"),
        (".bfaq-item summary:hover", "opacity:.8"),
    ],
    "bold": [
        (".bcard", "transition:transform .15s ease"),
        (".bcard:hover", "transform:translate(3px,3px)"),
        (".bmet-v", "opacity:0;animation:bScaleIn .5s ease forwards"),
        (".bstep-num", "opacity:0;animation:bScaleIn .5s ease forwards"),
        (".bprice-card.bfeatured", "transform:scale(1.08)"),
        (".bprice-card.bfeatured:hover", "transform:scale(1.08) translate(3px,3px)"),
        (".bfaq-item summary", "transition:transform .15s ease"),
        (".bfaq-item summary:hover", "transform:translateX(4px)"),
    ],
    "craft": [
        (".bcard", "transition:transform .35s ease"),
        (".bcard:hover", "transform:translateY(-4px) rotate(-.5deg)"),
        (".bmet-v", "opacity:0;animation:bFadeUp .6s ease .2s forwards"),
        (".bstep-num", "animation:bFadeIn .5s ease forwards"),
        (".bprice-card.bfeatured", "animation:bBreathe 5s ease-in-out infinite"),
        (".bfaq-item summary", "transition:transform .3s ease,opacity .3s ease"),
        (".bfaq-item summary:hover", "opacity:.8;transform:translateX(4px)"),
    ],
    "depth": [
        (".bcard", "transition:transform .35s ease,box-shadow .35s ease"),
        (".bcard:hover", "transform:translateY(-8px)"),
        (".bmet-v", "opacity:0;animation:bScaleIn .5s ease forwards"),
        (".bstep-num", "animation:bGlow 3s ease-in-out infinite"),
        (".bprice-card.bfeatured", "animation:bFloat 5s ease-in-out infinite"),
        (".bfaq-item summary", "transition:opacity .3s ease"),
        (".bfaq-item summary:hover", "opacity:.85"),
    ],
    "playful": [
        (".bcard", "transition:transform .3s cubic-bezier(.16,1,.3,1)"),
        (".bcard:hover", "transform:translateY(-8px) rotate(-1deg)"),
        (".bmet-v", "animation:bBounce 2s ease-in-out infinite"),
        (".bstep-num", "animation:bWiggle 3s ease-in-out infinite"),
        (".bprice-card.bfeatured", "animation:bBounce 3s ease-in-out infinite"),
        (".bfaq-item summary", "transition:transform .2s cubic-bezier(.16,1,.3,1)"),
        (".bfaq-item summary:hover", "transform:translateX(6px)"),
    ],
    "tech": [
        (".bcard", "transition:transform .25s ease,box-shadow .25s ease"),
        (".bcard:hover", "transform:translateY(-4px)"),
        (".bmet-v", "animation:bPulse 2s ease-in-out infinite"),
        (".bstep-num", "font-variant-numeric:tabular-nums;animation:bFadeIn .4s ease forwards"),
        (".bprice-card.bfeatured", "animation:bGlow 3s ease-in-out infinite"),
        (".bfaq-item summary", "transition:opacity .2s ease"),
        (".bfaq-item summary:hover", "opacity:.8"),
    ],
    "luxury": [
        (".bcard", "transition:transform .5s ease,box-shadow .5s ease"),
        (".bcard:hover", "transform:translateY(-6px)"),
        (".bmet-v", "opacity:0;animation:bFadeIn 1s ease .3s forwards"),
        (".bstep-num", "opacity:0;animation:bFadeIn .8s ease .2s forwards"),
        (".bprice-card.bfeatured", "animation:bGlow 4s ease-in-out infinite"),
        (".bfaq-item summary", "transition:all .4s ease"),
        (".bfaq-item summary:hover", "opacity:.8;letter-spacing:.3px"),
    ],
    "motion": [
        (".bcard", "transition:transform .4s cubic-bezier(.16,1,.3,1)"),
        (".bcard:hover", "transform:translateY(-8px) scale(1.02)"),
        (".bmet-v", "animation:bBounce 2.5s ease-in-out infinite"),
        (".bstep-num", "animation:bFloat 3s ease-in-out infinite"),
        (".bprice-card.bfeatured", "animation:bFloat 4s ease-in-out infinite"),
        (".bfaq-item summary", "transition:transform .3s cubic-bezier(.16,1,.3,1)"),
        (".bfaq-item summary:hover", "transform:translateX(8px)"),
    ],
    "print": [
        (".bcard", "transition:transform .3s ease"),
        (".bcard:hover", "transform:translateY(-4px)"),
        (".bmet-v", "opacity:0;animation:bFadeUp .6s ease .2s forwards"),
        (".bstep-num", "animation:bFadeIn .5s ease forwards"),
        (".bprice-card.bfeatured", "border-width:2px"),
        (".bfaq-item summary", "transition:opacity .2s ease"),
        (".bfaq-item summary:hover", "opacity:.8"),
    ],
}

# Animation philosophy text per category (for prompt updates)
CATEGORY_ANIM_DESC = {
    "subtle": "Minimal, purposeful motion. Entrance animations are soft fade-and-slide with staggered timing. Hover states use gentle elevation only. No continuous animations — stillness IS the brand. Transitions: 300ms ease. Maximum restraint.",
    "neon": "Neon-pulsing energy. Hero fades in with drama, metrics pulse with a glow cycle, logo flickers like a neon tube. Cards gain a luminous glow shadow on hover. The featured pricing card floats gently. Motion is electric but controlled — never frantic.",
    "retro": "Stepped, digital motion. Animations use step() timing to feel pixelated and mechanical. Metrics pulse in discrete steps. Transitions feel snappy and quantized. Nothing is smooth — everything is deliberately digitized and nostalgic.",
    "glass": "Floating, weightless motion. Cards rise and scale on hover like glass panes shifting in space. Metrics glow softly. The featured card floats with a dreamy up-down drift. Transitions use long cubic-bezier easing for that ethereal, suspended feel.",
    "organic": "Breathing, living motion. Elements subtly scale in a breathing rhythm. Cards drift and rotate slightly on hover like leaves in a breeze. Nothing is mechanical — every movement feels alive and natural. Timing is relaxed (4-5s cycles).",
    "bold": "Punchy, immediate impact. No fade-ins — elements stamp into place. Cards shift with instant translate-on-hover (no easing). The featured card is oversized for dominance. FAQ items punch sideways on hover. Motion is blunt, confident, unapologetic.",
    "craft": "Handmade, imperfect motion. Cards lift and tilt slightly on hover, like physical objects being picked up. Metrics fade in gently. Elements breathe slowly. Motion feels tactile and organic, with subtle rotation that suggests a human hand at work.",
    "depth": "Elevation-driven motion. Cards rise dramatically on hover, casting deeper shadows. Elements scale in to suggest emerging from the surface. The featured card floats to indicate it's pushed forward in z-space. All transitions prioritize depth perception.",
    "playful": "Bouncy, joyful motion. Metrics bounce continuously. Process numbers wiggle. Cards lift and tilt on hover like excited gestures. FAQ items leap sideways. Everything uses spring-like cubic-bezier curves. The UI feels alive and delighted to interact with you.",
    "tech": "Precise, data-driven motion. Metrics pulse at a measured rate. Numbers use tabular-nums for clean alignment. Cards elevate subtly on hover — nothing excessive. The featured card glows with a steady brightness cycle. Motion is measured and clinical.",
    "luxury": "Slow, deliberate elegance. Everything fades in with extended timing (0.8-1s). Hover transitions are languid (500ms). Letter-spacing shifts on FAQ hover for a refined detail. The featured card glows with a slow, prestigious rhythm. Motion whispers, never shouts.",
    "motion": "Kinetic, expressive motion. Cards scale and lift dramatically. Metrics bounce with energy. Process numbers float freely. FAQ items slide boldly. Uses aggressive cubic-bezier curves for spring-like overshooting. Motion IS the design — not decoration.",
    "print": "Subdued, editorial motion. Elements fade up gently as if rising off a press. Cards lift modestly. No continuous animations — this is static media brought to life with the minimum motion needed. Transitions are functional, never decorative.",
}


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def get_b_side_css(content):
    """Extract B-side CSS section as string."""
    m = re.search(r'/\* B-Side:', content)
    if not m:
        return ''
    end = content.find('</style>', m.start())
    return content[m.start():end]


def has_anim_on_selector(b_css, selector):
    """Check if selector already has animation or opacity:0 (entrance) defined."""
    escaped = re.escape(selector)
    # Check for exact selector match (not substring)
    pattern = escaped + r'\s*\{[^}]*(?:animation|opacity\s*:\s*0)'
    return bool(re.search(pattern, b_css))


def has_property_on_selector(b_css, selector, prop):
    """Check if selector has a specific CSS property."""
    escaped = re.escape(selector)
    pattern = escaped + r'\s*\{[^}]*' + re.escape(prop)
    return bool(re.search(pattern, b_css))


def extract_glow_color(b_css):
    """Extract a glow color from the style's accent color."""
    # Try .bmet-v color
    m = re.search(r'\.bmet-v\{[^}]*?color:\s*([^;}\s]+)', b_css)
    if m:
        color = m.group(1).strip()
        # Convert hex to rgba glow
        if color.startswith('#'):
            # Simple hex to rgba conversion
            h = color.lstrip('#')
            if len(h) == 3:
                h = h[0]*2 + h[1]*2 + h[2]*2
            if len(h) == 6:
                r, g, b = int(h[0:2], 16), int(h[2:4], 16), int(h[4:6], 16)
                return f'rgba({r},{g},{b},.25)'
        if 'rgba' in color or 'rgb' in color:
            # Reduce opacity for glow
            return re.sub(r'[\d.]+\)$', '.25)', color)
        return color

    # Try .bst color
    m2 = re.search(r'\.bst\{[^}]*?color:\s*([^;}\s]+)', b_css)
    if m2:
        color = m2.group(1).strip()
        if color.startswith('#'):
            h = color.lstrip('#')
            if len(h) == 3:
                h = h[0]*2 + h[1]*2 + h[2]*2
            if len(h) == 6:
                r, g, b = int(h[0:2], 16), int(h[2:4], 16), int(h[4:6], 16)
                return f'rgba({r},{g},{b},.25)'

    return 'rgba(129,140,248,.2)'  # Fallback indigo glow


# ---------------------------------------------------------------------------
# Core
# ---------------------------------------------------------------------------

def process_file(filepath):
    """Add animations to a single sample file."""
    name = os.path.splitext(os.path.basename(filepath))[0]

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    if ANIM_MARKER in content:
        return False, "already has animations"

    if '/* B-Side:' not in content:
        return False, "no B-side"

    cat = STYLE_CAT.get(name)
    if not cat:
        return False, f"no category mapping"

    b_css = get_b_side_css(content)
    glow = extract_glow_color(b_css)

    css_lines = [ANIM_MARKER]

    # 1. Add missing keyframes
    for kf_name, kf_css in KEYFRAMES.items():
        if f'@keyframes {kf_name}' not in content:
            css_lines.append(kf_css)

    # 2. Add entrance animations (skip if element already animated)
    for selector, props in ENTRANCE_RULES:
        if not has_anim_on_selector(b_css, selector):
            css_lines.append(f'{selector}{{{props}}}')

    # 3. Add category-specific animations
    cat_rules = CATEGORY_RULES.get(cat, [])
    for selector, props in cat_rules:
        # Replace GLOW placeholder
        props = props.replace('GLOW', glow)

        # Skip if selector already has the key property
        if 'animation' in props and has_anim_on_selector(b_css, selector):
            continue
        if 'transform' in props and ':hover' not in selector and has_property_on_selector(b_css, selector, 'transform'):
            continue
        # For hover rules, always add (they enhance existing)
        css_lines.append(f'{selector}{{{props}}}')

    # Only inject if we have more than just the marker
    if len(css_lines) <= 1:
        return False, "no animations needed"

    block = '\n' + '\n'.join(css_lines) + '\n'

    # Inject before </style>
    content = content.replace('</style>', block + '</style>', 1)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

    return True, f"{cat} ({len(css_lines)-1} rules)"


def main():
    files = sorted(glob.glob(os.path.join(SAMPLES_DIR, '*.html')))
    added = skipped = errors = 0

    for fp in files:
        fname = os.path.basename(fp)
        try:
            ok, msg = process_file(fp)
            if ok:
                added += 1
                print(f"  + {fname} ({msg})")
            else:
                skipped += 1
                if msg != "already has animations":
                    print(f"  - {fname} ({msg})")
        except Exception as e:
            errors += 1
            print(f"  ! {fname}: {e}")

    print(f"\nDone: {added} animated, {skipped} skipped, {errors} errors (total: {len(files)})")


if __name__ == '__main__':
    main()

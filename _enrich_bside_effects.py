#!/usr/bin/env python3
"""Enrich B-sides with unique effects extracted from their A-sides.

For each sample file:
1. Extracts @keyframes, pseudo-element overlays, text-shadows, and
   decorative CSS from the A-side
2. Checks which effects are missing from the B-side
3. Generates remapped B-side CSS and injects it

Selector remapping:
  body::after     -> .b-side::after
  body::before    -> .b-side::before
  .hero::before   -> .bhero::before
  .hero::after    -> .bhero::after
  h1 text-shadow  -> .bhero h1 text-shadow
  .card::before   -> .bcard::before
  .card::after    -> .bcard::after
  nav .logo anim  -> .bh .logo animation
"""

import re
import os
import glob

SAMPLES_DIR = "samples"

# Styles that are intentionally minimal — skip effect porting
INTENTIONALLY_SIMPLE = {
    "minimalism", "flat-design", "inclusive-design",
    "whitespace-maximalism", "mono-space",
}

ALREADY_ENRICHED_MARKER = "/* FX-enriched */"


# ---------------------------------------------------------------------------
# CSS Parsing Helpers
# ---------------------------------------------------------------------------

def split_a_b_css(content):
    """Split file content into A-side CSS and B-side CSS strings."""
    style_start = content.find('<style>') + len('<style>')
    toggle = content.find('/* A/B Toggle */')
    bside = re.search(r'/\* B-Side:', content)
    style_end = content.find('</style>')

    a_css = content[style_start:toggle] if toggle > style_start else ''
    b_css = content[bside.start():style_end] if bside else ''
    return a_css, b_css


def extract_keyframes(css):
    """Extract @keyframes blocks using brace-matching. Returns {name: full_block}."""
    results = {}
    i = 0
    while i < len(css):
        m = re.search(r'@keyframes\s+([\w-]+)\s*\{', css[i:])
        if not m:
            break
        name = m.group(1)
        brace_start = i + m.end() - 1
        depth = 0
        end = brace_start
        for j in range(brace_start, len(css)):
            if css[j] == '{':
                depth += 1
            elif css[j] == '}':
                depth -= 1
                if depth == 0:
                    end = j
                    break
        results[name] = css[i + m.start():end + 1]
        i = end + 1
    return results


def extract_pseudo_rules(css, selectors):
    """Extract ::before/::after rules for given base selectors.
    Returns {full_selector: css_body}.
    """
    results = {}
    for sel in selectors:
        for pseudo in ('::before', '::after'):
            full = sel + pseudo
            # Escape for regex, handle possible whitespace
            escaped = re.escape(sel) + r'\s*' + re.escape(pseudo)
            pattern = escaped + r'\s*\{([^}]+)\}'
            m = re.search(pattern, css)
            if m:
                results[full] = m.group(1).strip()
    return results


def extract_property(css, selector, prop):
    """Extract a CSS property value from a specific selector's rule block."""
    escaped_sel = re.escape(selector)
    pattern = escaped_sel + r'(?:\s*,\s*[^{]*)?\s*\{([^}]+)\}'
    m = re.search(pattern, css)
    if not m:
        return None
    block = m.group(1)
    pm = re.search(rf'{prop}\s*:\s*([^;}}]+)', block)
    return pm.group(1).strip() if pm else None


def has_selector(css, selector):
    """Check if a selector exists in the CSS."""
    return bool(re.search(re.escape(selector) + r'\s*\{', css))


# ---------------------------------------------------------------------------
# Effect Generation
# ---------------------------------------------------------------------------

def generate_enrichment(a_css, b_css, style_name):
    """Generate additional B-side CSS from A-side effects.
    Returns CSS string to inject.
    """
    additions = []

    # 1. Port @keyframes not already in B-side
    a_kf = extract_keyframes(a_css)
    b_kf = extract_keyframes(b_css)
    b_kf_names = set(b_kf.keys())

    for name, block in a_kf.items():
        b_name = 'b' + name[0].upper() + name[1:] if not name.startswith('b') else name
        if b_name not in b_kf_names and name not in b_kf_names:
            # Rename keyframe
            renamed = block.replace(f'@keyframes {name}', f'@keyframes {b_name}', 1)
            additions.append(renamed)

    # 2. Port body::after/::before overlays to .b-side
    overlay_map = {
        'body': '.b-side',
    }
    for a_sel, b_sel in overlay_map.items():
        for pseudo in ('::after', '::before'):
            a_full = a_sel + pseudo
            b_full = b_sel + pseudo
            a_rule = extract_pseudo_rules(a_css, [a_sel]).get(a_full)
            if a_rule and not has_selector(b_css, b_full):
                additions.append(f'{b_full}{{{a_rule}}}')

    # 3. Port .hero::before/::after to .bhero
    hero_map = {'.hero': '.bhero'}
    for a_sel, b_sel in hero_map.items():
        for pseudo in ('::before', '::after'):
            a_full = a_sel + pseudo
            b_full = b_sel + pseudo
            a_rule = extract_pseudo_rules(a_css, [a_sel]).get(a_full)
            if a_rule and not has_selector(b_css, b_full):
                additions.append(f'{b_full}{{{a_rule}}}')

    # 4. Port .card::before/::after to .bcard
    card_map = {'.card': '.bcard'}
    for a_sel, b_sel in card_map.items():
        for pseudo in ('::before', '::after'):
            a_full = a_sel + pseudo
            b_full = b_sel + pseudo
            a_rule = extract_pseudo_rules(a_css, [a_sel]).get(a_full)
            if a_rule and not has_selector(b_css, b_full):
                additions.append(f'{b_full}{{{a_rule}}}')

    # 5. Port h1 text-shadow if missing from .bhero h1
    h1_shadow = extract_property(a_css, 'h1', 'text-shadow')
    if h1_shadow:
        bhero_h1_shadow = extract_property(b_css, '.bhero h1', 'text-shadow')
        if not bhero_h1_shadow:
            # Check if .bhero h1 rule exists - if so, we'd need to modify it
            # For safety, add a new rule (CSS cascade will resolve)
            if not has_selector(b_css, '.bhero h1') or True:
                additions.append(f'.bhero h1{{text-shadow:{h1_shadow}}}')

    # 6. Port logo animation if A-side nav .logo has text-shadow or animation
    logo_shadow = extract_property(a_css, 'nav .logo', 'text-shadow')
    if logo_shadow:
        b_logo_shadow = extract_property(b_css, '.bh .logo', 'text-shadow')
        if not b_logo_shadow:
            additions.append(f'.bh .logo{{text-shadow:{logo_shadow}}}')

    logo_anim = extract_property(a_css, 'nav .logo', 'animation')
    if logo_anim:
        b_logo_anim = extract_property(b_css, '.bh .logo', 'animation')
        if not b_logo_anim:
            # Remap keyframe name
            remapped = logo_anim
            for name in a_kf:
                b_name = 'b' + name[0].upper() + name[1:] if not name.startswith('b') else name
                remapped = remapped.replace(name, b_name)
            additions.append(f'.bh .logo{{animation:{remapped}}}')

    # 7. Port button clip-path if present
    cta_clip = extract_property(a_css, '.cta', 'clip-path')
    if cta_clip:
        btn_clip = extract_property(b_css, '.bbtn-p', 'clip-path')
        if not btn_clip:
            additions.append(f'.bbtn-p{{clip-path:{cta_clip}}}')

    # 8. Port card hover effects
    card_hover_transform = extract_property(a_css, '.card:hover', 'transform')
    card_hover_shadow = extract_property(a_css, '.card:hover', 'box-shadow')
    if card_hover_transform or card_hover_shadow:
        existing = extract_property(b_css, '.bcard:hover', 'transform')
        if not existing and card_hover_transform:
            props = f'transform:{card_hover_transform}'
            if card_hover_shadow:
                props += f';box-shadow:{card_hover_shadow}'
            additions.append(f'.bcard:hover{{{props}}}')

    # 9. Update animation references in existing B-side to use ported keyframes
    #    (handled by the renamed keyframes above)

    return additions


# ---------------------------------------------------------------------------
# Injection
# ---------------------------------------------------------------------------

def inject_effects(content, css_additions):
    """Inject additional CSS into the B-side CSS section."""
    if not css_additions:
        return content

    block = '\n' + ALREADY_ENRICHED_MARKER + '\n' + '\n'.join(css_additions) + '\n'

    # Find insertion point: before </style> but after B-side CSS
    # Insert right before the expanded sections marker or before </style>
    marker = '/* Expanded B-Side'
    if marker in content:
        content = content.replace(marker, block + marker, 1)
    else:
        content = content.replace('</style>', block + '</style>', 1)

    return content


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def process_file(filepath):
    """Process a single sample file. Returns (ok, msg)."""
    name = os.path.splitext(os.path.basename(filepath))[0]

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Skip if already enriched
    if ALREADY_ENRICHED_MARKER in content:
        return False, "already enriched"

    # Skip intentionally simple styles
    if name in INTENTIONALLY_SIMPLE:
        return False, "intentionally simple"

    # Skip if no A/B structure
    if '/* A/B Toggle */' not in content:
        return False, "no A/B structure"

    a_css, b_css = split_a_b_css(content)
    if not a_css or not b_css:
        return False, "could not split CSS"

    additions = generate_enrichment(a_css, b_css, name)

    if not additions:
        return False, "no effects to port"

    content = inject_effects(content, additions)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

    return True, f"{len(additions)} effects"


def main():
    files = sorted(glob.glob(os.path.join(SAMPLES_DIR, '*.html')))
    enriched = skipped = errors = 0

    for fp in files:
        name = os.path.basename(fp)
        try:
            ok, msg = process_file(fp)
            if ok:
                enriched += 1
                print(f"  + {name} ({msg})")
            else:
                skipped += 1
                if msg not in ("no effects to port", "already enriched", "intentionally simple"):
                    print(f"  - {name} ({msg})")
        except Exception as e:
            errors += 1
            print(f"  ! {name}: {e}")

    print(f"\nDone: {enriched} enriched, {skipped} skipped, {errors} errors "
          f"(total: {len(files)})")


if __name__ == '__main__':
    main()

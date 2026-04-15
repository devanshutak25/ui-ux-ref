#!/usr/bin/env python3
"""Expand AI agent prompts from 2-3 sentences into comprehensive design system specs.

For each style in styles.html:
1. Reads existing metadata (colors, effects, keywords, designVars, etc.)
2. Reads the sample file's B-side CSS to extract actual component styling
3. Generates a detailed design system prompt following designprompts.dev format
4. Updates the aiPrompt field in styles.html (using backtick template literals)

The expanded prompt includes: role, philosophy, color tokens, typography,
component CSS, effects, layout, accessibility, bold choices, and success criteria.
"""

import re
import os

STYLES_FILE = "styles.html"
SAMPLES_DIR = "samples"


# ---------------------------------------------------------------------------
# CSS Extraction from Sample Files
# ---------------------------------------------------------------------------

def extract_prop(block, prop):
    """Extract a CSS property value from a rule block string."""
    m = re.search(rf'{prop}\s*:\s*([^;}}]+)', block)
    return m.group(1).strip() if m else None


def extract_sample_css(sample_path):
    """Extract key CSS values from a sample's B-side."""
    if not os.path.exists(sample_path):
        return {}

    with open(sample_path, 'r', encoding='utf-8') as f:
        content = f.read()

    bside = re.search(r'/\* B-Side:', content)
    if not bside:
        return {}
    style_end = content.find('</style>', bside.start())
    b_css = content[bside.start():style_end]

    result = {}

    # .b-side base
    m = re.search(r'\.b-side\{([^}]+)\}', b_css)
    if m:
        block = m.group(1)
        result['page_bg'] = extract_prop(block, 'background') or ''
        result['page_color'] = extract_prop(block, 'color') or ''
        result['page_font'] = extract_prop(block, 'font-family') or ''

    # .bbtn base
    m = re.search(r'\.bbtn\{([^}]+)\}', b_css)
    if m:
        result['btn_css'] = m.group(1).strip()

    # .bbtn-p
    m = re.search(r'\.bbtn-p\{([^}]+)\}', b_css)
    if m:
        result['btn_primary_css'] = m.group(1).strip()

    # .bbtn-s
    m = re.search(r'\.bbtn-s\{([^}]+)\}', b_css)
    if m:
        result['btn_secondary_css'] = m.group(1).strip()

    # .bcard
    m = re.search(r'\.bcard\{([^}]+)\}', b_css)
    if m:
        result['card_css'] = m.group(1).strip()

    # .bhero h1
    m = re.search(r'\.bhero h1\{([^}]+)\}', b_css)
    if m:
        result['h1_css'] = m.group(1).strip()

    # .bh (header)
    m = re.search(r'\.bh\{([^}]+)\}', b_css)
    if m:
        result['header_css'] = m.group(1).strip()

    # Check for overlays, keyframes, pseudo-elements
    result['has_keyframes'] = bool(re.search(r'@keyframes\s+b', b_css))
    result['has_overlay'] = bool(re.search(r'\.b-side::(?:before|after)', b_css))
    result['has_pseudo'] = bool(re.search(r'\.bcard::(?:before|after)', b_css))

    return result


# ---------------------------------------------------------------------------
# Style Metadata Parsing from styles.html
# ---------------------------------------------------------------------------

def parse_styles_metadata(content):
    """Parse the const styles=[...] array into a list of dicts."""
    # Find the array
    start = content.find('const styles=[')
    if start < 0:
        return []

    # Extract entries using {name:" as delimiter
    # Each entry starts with {name:" and we need to find matching }
    entries = []
    pos = content.find('{name:"', start)
    while pos >= 0:
        # Find the end of this entry (},\n or }]; accounting for nested backticks)
        depth = 0
        in_str = False
        str_char = None
        i = pos
        while i < len(content):
            ch = content[i]
            if in_str:
                if ch == '\\':
                    i += 2
                    continue
                if ch == str_char:
                    in_str = False
            else:
                if ch in ('"', "'", '`'):
                    in_str = True
                    str_char = ch
                elif ch == '{':
                    depth += 1
                elif ch == '}':
                    depth -= 1
                    if depth == 0:
                        entries.append(content[pos:i+1])
                        break
            i += 1

        pos = content.find('{name:"', i + 1) if i < len(content) else -1

    # Parse each entry into a dict
    styles = []
    for entry in entries:
        d = {}
        # Extract string fields
        for field in ['name', 'cat', 'effects', 'bestFor', 'keywords', 'perf',
                      'a11y', 'mobile', 'doNotUseFor', 'framework', 'era',
                      'complexity', 'cssKeywords', 'checklist', 'designVars',
                      'sample', 'aiPrompt']:
            m = re.search(rf'{field}:"((?:[^"\\]|\\.)*)"', entry)
            if m:
                d[field] = m.group(1).replace('\\"', '"')
            else:
                # Try backtick version
                m2 = re.search(rf'{field}:`((?:[^`\\]|\\.)*)`', entry)
                if m2:
                    d[field] = m2.group(1)
                else:
                    d[field] = ''

        # Extract colors array
        colors_m = re.search(r'colors:\[([^\]]+)\]', entry)
        if colors_m:
            d['colors'] = re.findall(r'"([^"]+)"', colors_m.group(1))
        else:
            d['colors'] = []

        # Extract booleans
        d['dark'] = 'dark:true' in entry
        d['light'] = 'light:true' in entry

        if d.get('name'):
            styles.append(d)

    return styles


# ---------------------------------------------------------------------------
# Prompt Generation
# ---------------------------------------------------------------------------

ROLE_PREFIX = """You are an expert frontend engineer, UI/UX designer, visual design specialist, and typography expert. Your goal is to help integrate this design system into an existing codebase while maintaining visual consistency, accessibility, and the style's unique character.

Before proposing or writing any code:
- Identify the tech stack (React, Next.js, Vue, Tailwind, shadcn/ui, etc.)
- Understand existing design tokens, global styles, and utility patterns
- Review current component architecture and naming conventions
- Note constraints (legacy CSS, design library, performance)

Always aim to:
- Preserve or improve accessibility
- Maintain visual consistency with this design system
- Make deliberate, creative design choices that express the style's personality
- Ensure responsive layouts across devices
- Leave the codebase in a cleaner, more coherent state"""


def format_colors(colors, name):
    """Generate color token documentation."""
    if not colors:
        return "No specific palette defined."

    labels = ['primary', 'secondary', 'accent', 'surface', 'muted']
    lines = []
    for i, c in enumerate(colors[:5]):
        label = labels[i] if i < len(labels) else f'color-{i+1}'
        lines.append(f"  {label}: {c}")
    return '\n'.join(lines)


def format_design_vars(dv):
    """Format design variables for display."""
    if not dv:
        return "  (none specified)"
    return '\n'.join(f'  {line.strip()}' for line in dv.split('\\n') if line.strip())


def format_checklist(cl):
    """Format checklist into bullet points."""
    if not cl:
        return "  (none specified)"
    return '\n'.join(f'  - {item.strip()}' for item in cl.split('|') if item.strip())


def generate_prompt(style, sample_css):
    """Generate a comprehensive design system prompt."""
    name = style.get('name', 'Unknown')
    current = style.get('aiPrompt', '')
    colors = style.get('colors', [])
    effects = style.get('effects', '')
    keywords = style.get('keywords', '')
    era = style.get('era', '')
    complexity = style.get('complexity', '')
    css_kw = style.get('cssKeywords', '')
    design_vars = style.get('designVars', '')
    checklist = style.get('checklist', '')
    do_not = style.get('doNotUseFor', '')
    best_for = style.get('bestFor', '')
    framework = style.get('framework', '')
    a11y = style.get('a11y', 'AA')
    cat = style.get('cat', '')
    dark = style.get('dark', False)
    light = style.get('light', False)

    # Extract component CSS from sample
    page_bg = sample_css.get('page_bg', '')
    page_color = sample_css.get('page_color', '')
    page_font = sample_css.get('page_font', '')
    btn_css = sample_css.get('btn_css', '')
    btn_p = sample_css.get('btn_primary_css', '')
    btn_s = sample_css.get('btn_secondary_css', '')
    card_css = sample_css.get('card_css', '')
    h1_css = sample_css.get('h1_css', '')

    # Build theme mode string
    modes = []
    if light: modes.append('Light')
    if dark: modes.append('Dark')
    mode_str = ' + '.join(modes) if modes else 'Both'

    # Build the prompt
    sections = []

    # --- Role ---
    sections.append(f"<role>\n{ROLE_PREFIX}\n</role>")

    # --- Design System ---
    ds = []
    ds.append(f"# Design Style: {name}")

    # Philosophy
    ds.append(f"""
## Design Philosophy

### Core Principle
{current}

### Visual Vibe
**Keywords**: {keywords}
**Category**: {cat} | **Era**: {era} | **Complexity**: {complexity}
**Theme Modes**: {mode_str}

### Best Used For
{best_for}

### What This Design Is NOT Good For
{do_not if do_not else 'No specific restrictions.'}""")

    # Color Tokens
    ds.append(f"""
## Design Token System

### Colors
~~~
{format_colors(colors, name)}
~~~""")

    # Typography
    if page_font:
        ds.append(f"""
### Typography
**Font Stack**: {page_font}
**Page Color**: {page_color}""")
    if h1_css:
        ds.append(f"""
### Heading (H1)
~~~css
.heading {{
  {'; '.join(p.strip() for p in h1_css.split(';') if p.strip())}
}}
~~~""")

    # Design Variables
    if design_vars:
        ds.append(f"""
### Design Variables
~~~css
{format_design_vars(design_vars)}
~~~""")

    # Component Stylings
    ds.append("\n## Component Stylings")

    if btn_css or btn_p:
        btn_full = btn_css or ''
        ds.append(f"""
### Buttons
**Base**:
~~~css
.button {{
  {'; '.join(p.strip() for p in btn_full.split(';') if p.strip())}
}}
~~~""")
        if btn_p:
            ds.append(f"""**Primary**: {btn_p.replace(chr(10), ' ')}""")
        if btn_s:
            ds.append(f"""**Secondary**: {btn_s.replace(chr(10), ' ')}""")

    if card_css:
        ds.append(f"""
### Cards
~~~css
.card {{
  {'; '.join(p.strip() for p in card_css.split(';') if p.strip())}
}}
~~~""")

    # CSS Foundations
    if css_kw:
        ds.append(f"""
## CSS Foundations
Key properties that define this style:
~~~css
{css_kw}
~~~""")

    # Page Background
    if page_bg:
        ds.append(f"""
### Page Background
~~~css
background: {page_bg};
~~~""")

    # Effects & Animation
    ds.append(f"""
## Effects & Animation
{effects}""")

    if sample_css.get('has_keyframes'):
        ds.append("**Note**: This style uses CSS @keyframes animations for dynamic elements.")
    if sample_css.get('has_overlay'):
        ds.append("**Note**: This style uses ::before/::after overlays for texture/atmosphere.")

    # Accessibility
    ds.append(f"""
## Accessibility
**Target**: WCAG {a11y}
**Contrast**: Ensure all text meets {a11y} contrast ratios against backgrounds.
**Touch Targets**: Minimum 44x44px for all interactive elements on mobile.
**Focus States**: Visible focus indicators on all interactive elements.""")

    # Bold Choices
    if checklist:
        ds.append(f"""
## Bold Choices (Non-Negotiable)
{format_checklist(checklist)}""")

    # Framework Compatibility
    if framework:
        ds.append(f"""
## Framework Compatibility
{', '.join(f.strip() for f in framework.split(','))}""")

    # Success Criteria
    ds.append(f"""
## What Success Looks Like
A successfully implemented {name} design should immediately evoke the style's character through its use of color, typography, spacing, and effects. It should NOT look like a generic template or a different design style with changed colors. Every component should feel intentionally crafted to express this specific aesthetic.""")

    full_ds = '\n'.join(ds)
    sections.append(f"<design-system>\n{full_ds}\n</design-system>")

    return '\n\n'.join(sections)


# ---------------------------------------------------------------------------
# File Update
# ---------------------------------------------------------------------------

def update_styles_html(content, styles_meta, new_prompts):
    """Replace aiPrompt values in styles.html with expanded versions."""
    for style, prompt in zip(styles_meta, new_prompts):
        name = style['name']
        old_prompt = style.get('aiPrompt', '')

        if not old_prompt:
            continue

        # Escape the old prompt for regex
        old_escaped = re.escape(old_prompt)

        # Try to find aiPrompt:"old text"
        pattern = rf'aiPrompt:"({old_escaped})"'
        match = re.search(pattern, content)

        if match:
            # Replace with backtick version
            safe_prompt = prompt.replace('\\', '\\\\').replace('`', '\\`').replace('${', '\\${')
            content = content[:match.start()] + f'aiPrompt:`{safe_prompt}`' + content[match.end():]
        else:
            # Try backtick version
            pattern2 = rf'aiPrompt:`({old_escaped})`'
            match2 = re.search(pattern2, content)
            if match2:
                safe_prompt = prompt.replace('\\', '\\\\').replace('`', '\\`').replace('${', '\\${')
                content = content[:match2.start()] + f'aiPrompt:`{safe_prompt}`' + content[match2.end():]
            else:
                print(f"  ! Could not find aiPrompt for: {name}")

    return content


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    # Read styles.html
    with open(STYLES_FILE, 'r', encoding='utf-8') as f:
        content = f.read()

    # Parse metadata
    styles = parse_styles_metadata(content)
    print(f"Parsed {len(styles)} styles from {STYLES_FILE}")

    # Generate new prompts
    new_prompts = []
    for style in styles:
        sample_path = style.get('sample', '')
        if sample_path:
            sample_css = extract_sample_css(sample_path)
        else:
            sample_css = {}

        prompt = generate_prompt(style, sample_css)
        new_prompts.append(prompt)
        name = style['name']
        old_len = len(style.get('aiPrompt', ''))
        new_len = len(prompt)
        print(f"  + {name}: {old_len} -> {new_len} chars")

    # Update styles.html
    updated = update_styles_html(content, styles, new_prompts)

    with open(STYLES_FILE, 'w', encoding='utf-8') as f:
        f.write(updated)

    print(f"\nDone: {len(styles)} prompts expanded in {STYLES_FILE}")


if __name__ == '__main__':
    main()

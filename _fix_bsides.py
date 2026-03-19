"""
Phase 1: Systemic B-Side Fixes
Applies across all 100 samples/*.html files:
  1A. Fix WCAG AA contrast failures (muted text colors)
  1B. Remove duplicate CSS blocks at end of B-side styles
  1C. Remove duplicate Google Font <link> tags
  1D. Fix double-period footer typos
  1E. Move misplaced font links (after </style>) to before <style>
"""

import os, re, glob
from urllib.parse import unquote, parse_qs, urlparse, urlencode

SAMPLES_DIR = os.path.join(os.path.dirname(__file__), 'samples')

# ──────────────────────────────────────────────
# 1A. Contrast color replacements
# Only apply within B-side CSS (after /* B-Side or .b-side selectors)
# ──────────────────────────────────────────────

# Map of old → new for light-background B-sides
LIGHT_BG_CONTRAST_FIXES = {
    '#8B7B68': '#6B5A48',
    '#8b7b68': '#6B5A48',
    '#808080': '#666666',
    '#7F8C8D': '#5F6C6D',
    '#7f8c8d': '#5F6C6D',
}

# Map of old → new for dark-background B-sides
DARK_BG_CONTRAST_FIXES = {
    'rgba(255,255,255,0.65)': 'rgba(255,255,255,0.78)',
    'rgba(255, 255, 255, 0.65)': 'rgba(255, 255, 255, 0.78)',
}

# #888888 needs context - different fix for light vs dark backgrounds
DARK_BG_888_REPLACE = '#A0A0A0'
LIGHT_BG_888_REPLACE = '#6B6B6B'

def is_dark_background(content):
    """Detect if B-side uses a dark background by checking .b-side or body bg color."""
    # Look for background colors in B-side CSS
    bside_css = get_bside_css(content)
    if not bside_css:
        return False
    # Check for dark background indicators
    dark_patterns = [
        r'background\s*:\s*#0[0-9a-fA-F]{5}',  # #0xxxxx
        r'background\s*:\s*#1[0-9a-fA-F]{5}',  # #1xxxxx
        r'background\s*:\s*#2[0-3][0-9a-fA-F]{4}',  # #2[0-3]xxxx
        r'background-color\s*:\s*#0[0-9a-fA-F]{5}',
        r'background-color\s*:\s*#1[0-9a-fA-F]{5}',
    ]
    for p in dark_patterns:
        if re.search(p, bside_css):
            return True
    return False

def get_bside_css(content):
    """Extract just the B-side CSS portion from the file."""
    # B-side CSS typically starts with .b-side{ or /* B-Side comments
    # and ends at </style>
    match = re.search(r'(\.b-side\s*\{.*?)(</style>)', content, re.DOTALL)
    if match:
        return match.group(1)
    # Alternative: look for .b-side selector
    match = re.search(r'(\.b-side\s*[{,].*?)(</style>)', content, re.DOTALL)
    if match:
        return match.group(1)
    return ''

def fix_contrast(content):
    """Fix WCAG AA contrast failures in B-side CSS."""
    dark = is_dark_background(content)

    # Split at .b-side to only modify B-side CSS
    # Find the position where B-side CSS starts
    bside_start = content.find('.b-side')
    style_end = content.find('</style>')

    if bside_start == -1 or style_end == -1:
        return content

    # Only modify the B-side CSS portion
    before = content[:bside_start]
    bside_section = content[bside_start:style_end]
    after = content[style_end:]

    # Apply light-bg fixes (always safe - these colors only appear on light backgrounds)
    for old, new in LIGHT_BG_CONTRAST_FIXES.items():
        bside_section = bside_section.replace(old, new)

    # Apply dark-bg fixes
    if dark:
        for old, new in DARK_BG_CONTRAST_FIXES.items():
            bside_section = bside_section.replace(old, new)
        bside_section = bside_section.replace('#888888', DARK_BG_888_REPLACE)
        bside_section = bside_section.replace('#888', DARK_BG_888_REPLACE)
    else:
        # For light backgrounds, #888888 becomes darker
        bside_section = bside_section.replace('#888888', LIGHT_BG_888_REPLACE)

    return before + bside_section + after


# ──────────────────────────────────────────────
# 1B. Remove duplicate CSS blocks
# The pattern: last line(s) before </style> repeat earlier rules
# ──────────────────────────────────────────────

def remove_duplicate_css(content):
    """Remove duplicate CSS rule blocks that appear at the end of the style section."""
    style_match = re.search(r'(<style>)(.*?)(</style>)', content, re.DOTALL)
    if not style_match:
        return content

    style_content = style_match.group(2)

    # Split into lines, find the last substantial line(s)
    lines = style_content.split('\n')

    # Work backwards from end, find lines that contain CSS rules
    cleaned_lines = []
    seen_rules = set()
    duplicate_lines = set()

    # First pass: collect all CSS rules by selector
    # We look for patterns like .selector{...} and track which selectors we've seen
    # The duplicates are typically on the last few lines

    # Find @media line and the lines after it (but before empty lines at end)
    # The pattern in these files: rules, @media query, then duplicate rules on one long line

    # Simpler approach: find the @media line (responsive query),
    # then check if any lines after it duplicate rules from before it
    media_idx = -1
    for i in range(len(lines) - 1, -1, -1):
        if '@media' in lines[i] and 'max-width' in lines[i]:
            media_idx = i
            break

    if media_idx == -1:
        return content

    # Collect all selector patterns before the @media line
    pre_media_text = '\n'.join(lines[:media_idx])

    # Check lines after @media for duplicates
    new_lines = lines[:media_idx + 1]  # Keep everything up to and including @media

    for i in range(media_idx + 1, len(lines)):
        line = lines[i].strip()
        if not line:
            new_lines.append(lines[i])
            continue

        # Extract selectors from this line
        # Pattern: .selector{...} repeated
        selectors_in_line = re.findall(r'(\.[a-zA-Z][\w-]*(?:\s*[\w:.>~+\s-]*)?)\s*\{', line)

        if not selectors_in_line:
            new_lines.append(lines[i])
            continue

        # Check if ALL selectors in this line already appear before @media
        all_duplicate = True
        for sel in selectors_in_line:
            sel_clean = sel.strip()
            # Check if this selector+rules appear in pre_media_text
            if sel_clean not in pre_media_text:
                all_duplicate = False
                break

        if all_duplicate and len(selectors_in_line) >= 2:
            # This is a duplicate line, skip it
            continue
        else:
            new_lines.append(lines[i])

    new_style_content = '\n'.join(new_lines)
    return content[:style_match.start(2)] + new_style_content + content[style_match.end(2):]


# ──────────────────────────────────────────────
# 1C. Remove duplicate Google Font <link> tags
# ──────────────────────────────────────────────

def dedupe_font_links(content):
    """Remove duplicate Google Fonts link tags, keeping the one with more weights."""
    font_links = re.findall(r'<link\s+[^>]*fonts\.googleapis\.com[^>]*>', content)

    if len(font_links) <= 1:
        return content

    # Group by font family
    family_links = {}
    for link in font_links:
        # Extract font family names
        families = re.findall(r'family=([^&"\'>\s]+)', link)
        key = tuple(sorted(set(f.split(':')[0] for f in families)))
        if key not in family_links:
            family_links[key] = []
        family_links[key].append(link)

    # For each family group with duplicates, keep the longer/more complete one
    for key, links in family_links.items():
        if len(links) > 1:
            # Keep the longest link (most weights)
            links_sorted = sorted(links, key=len, reverse=True)
            keep = links_sorted[0]
            for link in links_sorted[1:]:
                content = content.replace(link + '\n', '', 1)
                if link in content:
                    content = content.replace(link, '', 1)

    return content


# ──────────────────────────────────────────────
# 1D. Fix double-period footer typos
# ──────────────────────────────────────────────

def fix_double_periods(content):
    """Fix BRAND.. typos in footer copyright text."""
    # Match word followed by .. then space or &nbsp; or < (but not ...)
    content = re.sub(r'(\w)\.\.(\s|&|<)', r'\1.\2', content)
    return content


# ──────────────────────────────────────────────
# 1E. Move misplaced font links
# ──────────────────────────────────────────────

def fix_font_link_placement(content):
    """Move Google Font links from after </style> to before <style>."""
    # Find font links between </style> and </head>
    pattern = r'(</style>)\s*(<link\s+[^>]*fonts\.googleapis\.com[^>]*>)\s*(</head>)'
    match = re.search(pattern, content)

    if not match:
        return content

    misplaced_link = match.group(2)

    # Remove from current position
    content = content.replace(match.group(0), '</style>\n</head>')

    # Insert before first <style>
    content = content.replace('<style>', misplaced_link + '\n<style>', 1)

    return content


# ──────────────────────────────────────────────
# Main
# ──────────────────────────────────────────────

def process_file(filepath):
    """Apply all systemic fixes to a single file."""
    with open(filepath, 'r', encoding='utf-8') as f:
        original = f.read()

    content = original

    # Apply fixes in order
    content = fix_font_link_placement(content)  # 1E first (before dedup)
    content = dedupe_font_links(content)         # 1C
    content = fix_contrast(content)              # 1A
    content = remove_duplicate_css(content)      # 1B
    content = fix_double_periods(content)        # 1D

    if content != original:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        return True
    return False


if __name__ == '__main__':
    files = sorted(glob.glob(os.path.join(SAMPLES_DIR, '*.html')))
    print(f"Found {len(files)} HTML files in {SAMPLES_DIR}")

    modified = 0
    for filepath in files:
        name = os.path.basename(filepath)
        changed = process_file(filepath)
        if changed:
            modified += 1
            print(f"  FIXED: {name}")
        else:
            print(f"  OK:    {name}")

    print(f"\nDone. Modified {modified}/{len(files)} files.")

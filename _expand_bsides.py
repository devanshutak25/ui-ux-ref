#!/usr/bin/env python3
"""Expand B-sides with Process, Pricing, FAQ, and CTA sections.

Adds 4 new sections before the footer in each sample's B-side,
making them full SaaS landing pages similar to designprompts.dev.
CSS inherits visual styling from each style's existing classes.
"""

import re
import os
import glob

SAMPLES_DIR = "samples"

# ---------------------------------------------------------------------------
# CSS template — layout only; visual styling inherits from .bcard / .bbtn / .bsec
# FAQ_BORDER_COLOR is replaced per-file with the style's card border color
# ---------------------------------------------------------------------------
NEW_CSS = r"""
/* Expanded B-Side: process, pricing, FAQ, CTA */
.bsteps{display:grid;grid-template-columns:repeat(3,1fr);gap:2rem}
.bstep{text-align:center;padding:1.5rem}
.bstep-num{font-size:2.5rem;font-weight:800;opacity:.15;line-height:1;margin-bottom:.75rem}
.bstep h3{font-size:1rem;font-weight:600;margin-bottom:.5rem}
.bstep p{font-size:.85rem;opacity:.7;line-height:1.6}
.bpricing{display:grid;grid-template-columns:repeat(3,1fr);gap:1.5rem;align-items:start}
.bcard.bprice-card{padding:2rem;text-align:center;transition:transform .2s}
.bcard.bprice-card:hover{transform:translateY(-4px)}
.bcard.bprice-card.bfeatured{position:relative;transform:scale(1.05)}
.bcard.bprice-card.bfeatured:hover{transform:scale(1.05) translateY(-4px)}
.bprice-name{font-size:.8rem;text-transform:uppercase;letter-spacing:2px;margin-bottom:.75rem;font-weight:600}
.bprice-amount{font-size:2.5rem;font-weight:800;line-height:1;margin-bottom:.25rem}
.bprice-period{font-size:.8rem;opacity:.6;margin-bottom:1.5rem}
.bprice-features{list-style:none;text-align:left;margin-bottom:2rem;font-size:.85rem;line-height:2.2}
.bprice-features li::before{content:'\2713\0020';opacity:.5}
.bfaq{max-width:700px;margin:0 auto}
.bfaq-item{border-bottom:1px solid FAQ_BORDER_COLOR;padding:1.25rem 0}
.bfaq-item summary{font-weight:600;cursor:pointer;display:flex;justify-content:space-between;align-items:center;font-size:.95rem}
.bfaq-item summary::-webkit-details-marker{display:none}
.bfaq-item summary::after{content:'+';font-size:1.3rem;font-weight:300;flex-shrink:0;margin-left:1rem}
.bfaq-item[open] summary::after{content:'\2212'}
.bfaq-item p{font-size:.88rem;opacity:.75;line-height:1.7;padding-top:.75rem}
.bcta-inner{text-align:center;max-width:560px;margin:0 auto}
.bcta-inner h2{font-size:2rem;font-weight:700;margin-bottom:1rem;letter-spacing:-.02em}
.bcta-inner p{font-size:1rem;opacity:.65;margin-bottom:2rem;line-height:1.7}
@media(max-width:768px){.bsteps{grid-template-columns:1fr}.bpricing{grid-template-columns:1fr}.bcard.bprice-card.bfeatured{transform:none}}
"""

# ---------------------------------------------------------------------------
# HTML sections inserted before <footer class="bfoot">
# ---------------------------------------------------------------------------
NEW_HTML = (
    '<section class="bsec"><div class="bcon">'
    '<p class="bst">Process</p><h2 class="bsh">How It Works</h2>'
    '<div class="bsteps">'
    '<div class="bstep"><div class="bstep-num">01</div>'
    '<h3>Discovery</h3>'
    '<p>We learn your vision, audience, and constraints through focused research and strategic workshops.</p></div>'
    '<div class="bstep"><div class="bstep-num">02</div>'
    '<h3>Design</h3>'
    '<p>Concepts take shape through iterative prototyping, user testing, and continuous refinement.</p></div>'
    '<div class="bstep"><div class="bstep-num">03</div>'
    '<h3>Deliver</h3>'
    '<p>Polished, production-ready output with full documentation and ongoing support.</p></div>'
    '</div></div></section>\n'

    '<section class="bsec"><div class="bcon">'
    '<p class="bst">Pricing</p><h2 class="bsh">Simple, Transparent</h2>'
    '<div class="bpricing">'
    # --- Starter ---
    '<div class="bcard bprice-card">'
    '<div class="bprice-name">Starter</div>'
    '<div class="bprice-amount">$9</div>'
    '<div class="bprice-period">per month</div>'
    '<ul class="bprice-features">'
    '<li>3 projects</li>'
    '<li>Basic analytics</li>'
    '<li>48-hour support</li>'
    '<li>1 team member</li>'
    '</ul>'
    '<button class="bbtn bbtn-s" style="width:100%">Get Started</button>'
    '</div>'
    # --- Pro (featured) ---
    '<div class="bcard bprice-card bfeatured">'
    '<div class="bprice-name">Pro</div>'
    '<div class="bprice-amount">$29</div>'
    '<div class="bprice-period">per month</div>'
    '<ul class="bprice-features">'
    '<li>Unlimited projects</li>'
    '<li>Advanced analytics</li>'
    '<li>Priority support</li>'
    '<li>5 team members</li>'
    '<li>Custom exports</li>'
    '</ul>'
    '<button class="bbtn bbtn-p" style="width:100%">Get Started</button>'
    '</div>'
    # --- Enterprise ---
    '<div class="bcard bprice-card">'
    '<div class="bprice-name">Enterprise</div>'
    '<div class="bprice-amount">$99</div>'
    '<div class="bprice-period">per month</div>'
    '<ul class="bprice-features">'
    '<li>Everything in Pro</li>'
    '<li>Unlimited members</li>'
    '<li>Dedicated manager</li>'
    '<li>SLA guarantee</li>'
    '<li>Custom integrations</li>'
    '</ul>'
    '<button class="bbtn bbtn-s" style="width:100%">Contact Us</button>'
    '</div>'
    '</div></div></section>\n'

    '<section class="bsec"><div class="bcon">'
    '<p class="bst">FAQ</p><h2 class="bsh">Common Questions</h2>'
    '<div class="bfaq">'
    '<details class="bfaq-item"><summary>How do I get started?</summary>'
    '<p>Sign up for a free trial with no credit card required. '
    'Full access to Starter features for 14 days.</p></details>'
    '<details class="bfaq-item"><summary>Can I change plans later?</summary>'
    '<p>Absolutely. Upgrade or downgrade anytime. '
    'Changes take effect at your next billing cycle.</p></details>'
    '<details class="bfaq-item"><summary>Is there a free trial?</summary>'
    '<p>Yes. Every new account gets 14 days of Pro '
    'with all features unlocked.</p></details>'
    '<details class="bfaq-item"><summary>What support is included?</summary>'
    '<p>Starter includes 48-hour email support. Pro and Enterprise '
    'get priority responses under 4 hours.</p></details>'
    '</div></div></section>\n'

    '<section class="bsec"><div class="bcon">'
    '<div class="bcta-inner">'
    '<h2>Ready to Start?</h2>'
    '<p>Join thousands of teams already building better products with our platform.</p>'
    '<div class="bhero-btns" style="justify-content:center">'
    '<button class="bbtn bbtn-p">Start Free Trial</button>'
    '<button class="bbtn bbtn-s">Book a Demo</button>'
    '</div></div></div></section>\n'
)


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def extract_faq_border(content):
    """Derive a suitable FAQ-item border color from existing .bcard CSS."""
    m = re.search(r'\.bcard\{[^}]*?border:\s*([^;}]+)', content)
    if m:
        parts = re.split(r'\s+', m.group(1).strip(), 2)
        if len(parts) >= 3:
            return parts[2].rstrip(';')

    # Fallback: detect dark vs light theme from .b-side background
    bg_match = re.search(r'\.b-side\{[^}]*?background:\s*([^;}]+)', content)
    if bg_match:
        bg = bg_match.group(1).lower()
        if any(d in bg for d in ['#000', '#0d', '#0f', '#1e', '#11', '#12',
                                  '#13', '#0a', '#08', '#09', 'rgb(0',
                                  'linear-gradient']):
            return 'rgba(255,255,255,0.12)'
    return 'rgba(0,0,0,0.1)'


def already_expanded(content):
    """True if file already contains expanded sections."""
    return '.bsteps{' in content or '.bpricing{' in content


# ---------------------------------------------------------------------------
# Core
# ---------------------------------------------------------------------------

def expand_file(filepath):
    """Add new sections to a single sample's B-side. Returns (ok, msg)."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    if already_expanded(content):
        return False, "already expanded"
    if '<div class="b-side">' not in content:
        return False, "no b-side"
    # Find footer tag (may have extra attributes like role="contentinfo")
    footer_match = re.search(r'<footer class="bfoot"[^>]*>', content)
    if not footer_match:
        return False, "no bfoot"

    faq_border = extract_faq_border(content)
    css_block = NEW_CSS.replace('FAQ_BORDER_COLOR', faq_border)

    # Inject CSS before </style>
    content = content.replace('</style>', css_block + '</style>', 1)

    # Inject HTML before footer
    footer_tag = footer_match.group(0)
    content = content.replace(footer_tag, NEW_HTML + footer_tag, 1)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    return True, "ok"


def main():
    files = sorted(glob.glob(os.path.join(SAMPLES_DIR, '*.html')))
    expanded = skipped = errors = 0

    for fp in files:
        name = os.path.basename(fp)
        try:
            ok, msg = expand_file(fp)
            if ok:
                expanded += 1
                print(f"  + {name}")
            else:
                skipped += 1
                print(f"  - {name} ({msg})")
        except Exception as e:
            errors += 1
            print(f"  ! {name}: {e}")

    print(f"\nDone: {expanded} expanded, {skipped} skipped, {errors} errors "
          f"(total: {len(files)})")


if __name__ == '__main__':
    main()

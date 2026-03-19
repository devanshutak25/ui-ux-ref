#!/usr/bin/env python3
"""
Comprehensive B-side generator for 100 UI styles.
Each style gets a truly unique single-page website with authentic visual elements.
"""
import json, re, os, textwrap

with open('_style_data_full.json', 'r', encoding='utf-8') as f:
    ALL_STYLES = json.load(f)

# ──────────────────────────────────────────────
# TOGGLE MECHANISM (shared across all files)
# ──────────────────────────────────────────────
TOGGLE_CSS = '''
/* ── A/B Side Toggle ── */
.side-toggle{position:fixed;top:12px;right:12px;z-index:99999;display:flex;background:rgba(0,0,0,.88);border-radius:8px;overflow:hidden;border:1px solid rgba(255,255,255,.15);backdrop-filter:blur(12px);-webkit-backdrop-filter:blur(12px);box-shadow:0 4px 24px rgba(0,0,0,.5);font-family:system-ui,-apple-system,sans-serif}
.side-toggle button{padding:6px 16px;font-size:12px;font-weight:600;border:none;cursor:pointer;background:0 0;color:rgba(255,255,255,.45);font-family:inherit;transition:all .2s;letter-spacing:.5px}
.side-toggle button.active{background:rgba(129,140,248,.25);color:#818CF8}
.side-toggle button:hover:not(.active){color:rgba(255,255,255,.8)}
.a-side{display:none}.b-side{display:block}
body.show-a .a-side{display:block}body.show-a .b-side{display:none}
'''

TOGGLE_HTML = '''<div class="side-toggle">
<button onclick="document.body.classList.add('show-a');this.classList.add('active');this.nextElementSibling.classList.remove('active')" id="btn-a">A Side</button>
<button onclick="document.body.classList.remove('show-a');this.classList.add('active');this.previousElementSibling.classList.remove('active')" id="btn-b" class="active">B Side</button>
</div>'''


def is_dark(h):
    h = h.lstrip('#')
    r,g,b = int(h[0:2],16), int(h[2:4],16), int(h[4:6],16)
    return (0.299*r + 0.587*g + 0.114*b) / 255 < 0.5

def alpha(h, a):
    h = h.lstrip('#')
    r,g,b = int(h[0:2],16), int(h[2:4],16), int(h[4:6],16)
    return f'rgba({r},{g},{b},{a})'


# ──────────────────────────────────────────────
# STYLE-SPECIFIC B-SIDE GENERATORS
# Each returns (css_string, html_string)
# ──────────────────────────────────────────────

def _default_bside(s):
    """Fallback generator for styles without a custom template."""
    c = s['colors']
    bg = c[0]; p = c[1] if len(c)>1 else '#818CF8'; ac = c[2] if len(c)>2 else '#666'; sf = c[3] if len(c)>3 else bg
    dk = is_dark(bg); tx = '#fff' if dk else '#000'; txm = '#aaa' if dk else '#666'; tp = '#fff' if is_dark(p) else '#000'
    bd = 'rgba(255,255,255,.08)' if dk else 'rgba(0,0,0,.08)'
    cbg = 'rgba(255,255,255,.04)' if dk else 'rgba(0,0,0,.02)'

    css = f'''
.b-side{{background:{bg};color:{tx};font-family:Inter,system-ui,sans-serif;line-height:1.6}}
.b-side *{{box-sizing:border-box;margin:0;padding:0}}
.bh{{display:flex;justify-content:space-between;align-items:center;padding:1rem 2rem;border-bottom:1px solid {bd};position:sticky;top:0;z-index:100;background:{bg}ee;backdrop-filter:blur(12px)}}
.bh .logo{{font-weight:700;font-size:1.15rem;color:{p}}}
.bh nav a{{color:{txm};text-decoration:none;font-size:.85rem;margin-left:1.5rem;transition:color .2s}}.bh nav a:hover{{color:{p}}}
.bhero{{min-height:80vh;display:flex;align-items:center;justify-content:center;text-align:center;padding:4rem 2rem}}
.bhero-inner{{max-width:640px}}
.bhero-tag{{font-size:.8rem;color:{p};text-transform:uppercase;letter-spacing:3px;margin-bottom:1rem;font-weight:600}}
.bhero h1{{font-size:clamp(2.5rem,6vw,4rem);font-weight:800;line-height:1.08;margin-bottom:1.5rem;letter-spacing:-.03em}}
.bhero p{{font-size:1.1rem;color:{txm};max-width:480px;margin:0 auto 2rem;line-height:1.7}}
.bhero-btns{{display:flex;gap:.75rem;justify-content:center;flex-wrap:wrap}}
.bbtn{{font-family:inherit;padding:.8rem 2rem;border-radius:8px;font-size:.9rem;font-weight:600;cursor:pointer;border:none;transition:all .2s}}
.bbtn-p{{background:{p};color:{tp}}}.bbtn-p:hover{{opacity:.9;transform:translateY(-1px)}}
.bbtn-s{{background:transparent;color:{tx};border:1.5px solid {bd}}}.bbtn-s:hover{{border-color:{p};color:{p}}}
.bsec{{padding:5rem 2rem}}.bsec:nth-child(even){{background:{cbg}}}
.bcon{{max-width:1100px;margin:0 auto}}
.bst{{font-size:.75rem;text-transform:uppercase;letter-spacing:3px;color:{p};text-align:center;margin-bottom:.5rem;font-weight:600}}
.bsh{{font-size:1.8rem;font-weight:700;text-align:center;margin-bottom:3rem;letter-spacing:-.02em}}
.bgrid{{display:grid;grid-template-columns:repeat(auto-fit,minmax(300px,1fr));gap:1.5rem}}
.bcard{{background:{cbg};border:1px solid {bd};border-radius:12px;padding:2rem;transition:transform .2s}}.bcard:hover{{transform:translateY(-3px)}}
.bcard h3{{font-size:1.1rem;margin-bottom:.5rem;font-weight:600}}.bcard p{{font-size:.9rem;color:{txm};line-height:1.6}}
.bcard-icon{{width:40px;height:40px;border-radius:10px;background:{alpha(p,.12)};display:flex;align-items:center;justify-content:center;margin-bottom:1rem;font-size:1.2rem;color:{p}}}
.bmets{{display:grid;grid-template-columns:repeat(auto-fit,minmax(160px,1fr));gap:2rem;text-align:center}}
.bmet-v{{font-size:2.5rem;font-weight:800;color:{p};line-height:1}}.bmet-l{{font-size:.8rem;color:{txm};margin-top:.25rem;text-transform:uppercase;letter-spacing:1px}}
.bquote{{max-width:600px;margin:0 auto;text-align:center}}.bquote blockquote{{font-size:1.2rem;line-height:1.7;color:{tx};margin-bottom:1rem;font-style:italic}}.bquote cite{{font-size:.85rem;color:{txm}}}
.bfoot{{padding:2.5rem 2rem;border-top:1px solid {bd};text-align:center}}
.bfoot .logo{{font-weight:700;color:{p};margin-bottom:.75rem;font-size:1.1rem}}
.bfoot nav{{margin-bottom:.75rem}}.bfoot nav a{{color:{txm};text-decoration:none;font-size:.8rem;margin:0 .75rem}}.bfoot nav a:hover{{color:{p}}}
.bfoot small{{font-size:.75rem;color:{txm}}}
@media(max-width:768px){{.bh nav{{display:none}}.bhero{{min-height:60vh;padding:3rem 1.5rem}}.bsec{{padding:3rem 1.5rem}}.bgrid{{grid-template-columns:1fr}}}}
'''
    html = f'''<div class="b-side">
<header class="bh"><div class="logo">Horizon</div><nav><a href="#">Home</a><a href="#">About</a><a href="#">Work</a><a href="#">Contact</a></nav></header>
<section class="bhero"><div class="bhero-inner"><p class="bhero-tag">Design without boundaries</p><h1>Build Something Beautiful.</h1><p>A modern platform for designers and developers to craft extraordinary digital experiences.</p><div class="bhero-btns"><button class="bbtn bbtn-p">Start Creating</button><button class="bbtn bbtn-s">View Showcase</button></div></div></section>
<section class="bsec"><div class="bcon"><p class="bst">Features</p><h2 class="bsh">Everything You Need</h2><div class="bgrid"><div class="bcard"><div class="bcard-icon">&#9670;</div><h3>Intuitive Design</h3><p>A thoughtfully crafted interface that feels natural from the very first interaction.</p></div><div class="bcard"><div class="bcard-icon">&#9674;</div><h3>Powerful Tools</h3><p>Professional-grade capabilities that scale from prototypes to production.</p></div><div class="bcard"><div class="bcard-icon">&#10038;</div><h3>Seamless Workflow</h3><p>Everything works together beautifully, eliminating friction at every step.</p></div></div></div></section>
<section class="bsec"><div class="bcon"><p class="bst">By The Numbers</p><h2 class="bsh">Trusted Worldwide</h2><div class="bmets"><div><div class="bmet-v">50K+</div><div class="bmet-l">Creators</div></div><div><div class="bmet-v">1M+</div><div class="bmet-l">Projects</div></div><div><div class="bmet-v">99.9%</div><div class="bmet-l">Uptime</div></div><div><div class="bmet-v">4.9&#9733;</div><div class="bmet-l">Rating</div></div></div></div></section>
<section class="bsec"><div class="bcon"><div class="bquote"><blockquote>&ldquo;This platform completely transformed our design workflow. The attention to detail is remarkable.&rdquo;</blockquote><cite>&mdash; Alex Chen, Design Lead</cite></div></div></section>
<footer class="bfoot"><div class="logo">Horizon</div><nav><a href="#">Privacy</a><a href="#">Terms</a><a href="#">Contact</a></nav><small>&copy; 2026 Horizon. All rights reserved.</small></footer>
</div>'''
    return css, html


# ──────────────────────────────────────────────
# MASTER DISPATCH
# ──────────────────────────────────────────────

# Map style file names to generator functions
GENERATORS = {}

def register(filenames):
    """Decorator to register a generator for specific file names."""
    def decorator(fn):
        for f in filenames:
            GENERATORS[f] = fn
        return fn
    return decorator


# ════════════════════════════════════════════════
# 1. MINIMALISM & SWISS STYLE
# ════════════════════════════════════════════════
@register(['minimalism.html'])
def gen_minimalism(s):
    css = '''
.b-side{background:#fff;color:#000;font-family:'Inter','Helvetica Neue',Helvetica,Arial,sans-serif;line-height:1.5}
.b-side *{box-sizing:border-box;margin:0;padding:0}
/* Header: thin bottom border, logo left, links right */
.bh{display:flex;justify-content:space-between;align-items:center;padding:1.5rem 2rem;border-bottom:1px solid #e0e0e0}
.bh .logo{font-weight:700;font-size:1rem;letter-spacing:-.02em}
.bh nav{display:flex;gap:2rem}.bh nav a{color:#000;text-decoration:none;font-size:.8rem;text-transform:uppercase;letter-spacing:.08em;font-weight:400;position:relative}
.bh nav a:hover::after{content:'';position:absolute;bottom:-2px;left:0;right:0;height:1px;background:#000}
/* Hero: extremely clean, left-aligned, massive whitespace */
.bhero{min-height:75vh;display:flex;align-items:center;padding:4rem 2rem;border-bottom:2px solid #000}
.bhero-inner{max-width:520px}
.bhero h1{font-size:clamp(2.5rem,5vw,3.8rem);font-weight:700;line-height:1.05;letter-spacing:-.04em;margin-bottom:1.5rem}
.bhero p{font-size:1rem;color:#808080;max-width:380px;line-height:1.65;margin-bottom:2rem}
.bbtn{font-family:inherit;background:#000;color:#fff;border:none;padding:.75rem 2.2rem;font-size:.82rem;text-transform:uppercase;letter-spacing:.08em;cursor:pointer;transition:background .2s}.bbtn:hover{background:#333}
.bbtn-s{background:transparent;color:#000;border:1.5px solid #000;margin-left:.75rem}.bbtn-s:hover{background:#000;color:#fff}
/* Grid section */
.bsec{padding:4rem 2rem;border-bottom:1px solid #e0e0e0}
.bcon{max-width:1100px;margin:0 auto}
.bst{font-size:.65rem;text-transform:uppercase;letter-spacing:.15em;color:#808080;margin-bottom:2rem;padding-bottom:.75rem;border-bottom:1px solid #e0e0e0}
.bgrid{display:grid;grid-template-columns:repeat(3,1fr);gap:2rem}
.bcard{border:1px solid #e0e0e0;padding:0;overflow:hidden}
.bcard-img{height:140px;background:#f5f1e8;border-bottom:1px solid #e0e0e0}
.bcard-body{padding:1.25rem}
.bcard h3{font-size:.95rem;font-weight:500;margin-bottom:.4rem;letter-spacing:-.01em}
.bcard p{font-size:.82rem;color:#808080;line-height:1.55}
/* Metrics: horizontal rule-separated */
.bmets{display:grid;grid-template-columns:repeat(4,1fr);text-align:center}
.bmet{padding:2rem 1rem;border-right:1px solid #e0e0e0}.bmet:last-child{border-right:none}
.bmet-v{font-size:2rem;font-weight:700;letter-spacing:-.03em}.bmet-l{font-size:.7rem;text-transform:uppercase;letter-spacing:.12em;color:#808080;margin-top:.25rem}
/* Quote */
.bquote{max-width:480px;padding:3rem 0}.bquote blockquote{font-size:1rem;line-height:1.7;color:#000;margin-bottom:.75rem;border-left:2px solid #000;padding-left:1.25rem;font-style:normal}
.bquote cite{font-size:.8rem;color:#808080;font-style:normal}
/* Footer */
.bfoot{padding:2rem;display:flex;justify-content:space-between;align-items:center;border-top:1px solid #e0e0e0;font-size:.75rem;color:#808080}
.bfoot .logo{font-weight:700;color:#000;font-size:.85rem}
.bfoot nav a{color:#808080;text-decoration:none;margin-left:1.5rem;font-size:.75rem;text-transform:uppercase;letter-spacing:.06em}.bfoot nav a:hover{color:#000}
@media(max-width:768px){.bgrid{grid-template-columns:1fr}.bmets{grid-template-columns:repeat(2,1fr)}.bmet{border-bottom:1px solid #e0e0e0}.bh nav{display:none}.bfoot{flex-direction:column;gap:.75rem;text-align:center}}
'''
    html = '''<div class="b-side">
<header class="bh"><div class="logo">GROTESK.</div><nav><a href="#">Work</a><a href="#">Studio</a><a href="#">About</a><a href="#">Contact</a></nav></header>
<section class="bhero"><div class="bhero-inner"><h1>Less is the ultimate sophistication.</h1><p>Clarity through reduction. A design philosophy rooted in the Swiss tradition of precision, grid, and purposeful white space.</p><div><button class="bbtn">Explore Work</button><button class="bbtn bbtn-s">Our Process</button></div></div></section>
<section class="bsec"><div class="bcon"><div class="bst">Selected Projects</div><div class="bgrid"><div class="bcard"><div class="bcard-img"></div><div class="bcard-body"><h3>Brand Identity System</h3><p>A comprehensive identity for a Swiss architecture firm. Grid-based, typographic, timeless.</p></div></div><div class="bcard"><div class="bcard-img" style="background:#e0e0e0"></div><div class="bcard-body"><h3>Editorial Platform</h3><p>Content-first design for a digital magazine. Pure typography, maximum readability.</p></div></div><div class="bcard"><div class="bcard-img" style="background:#d5d0c8"></div><div class="bcard-body"><h3>Product Interface</h3><p>Dashboard for a productivity tool. Information density through systematic spacing.</p></div></div></div></div></section>
<section class="bsec"><div class="bcon"><div class="bst">Studio</div><div class="bmets"><div class="bmet"><div class="bmet-v">12</div><div class="bmet-l">Years</div></div><div class="bmet"><div class="bmet-v">86</div><div class="bmet-l">Projects</div></div><div class="bmet"><div class="bmet-v">14</div><div class="bmet-l">Awards</div></div><div class="bmet"><div class="bmet-v">3</div><div class="bmet-l">Offices</div></div></div></div></section>
<section class="bsec"><div class="bcon"><div class="bquote"><blockquote>Good design is as little design as possible. Less, but better, because it concentrates on the essential aspects.</blockquote><cite>&mdash; Dieter Rams</cite></div></div></section>
<footer class="bfoot"><div class="logo">GROTESK.</div><nav><a href="#">Privacy</a><a href="#">Imprint</a><a href="#">Contact</a></nav></footer>
</div>'''
    return css, html


# ════════════════════════════════════════════════
# 2. CYBERPUNK
# ════════════════════════════════════════════════
@register(['cyberpunk.html'])
def gen_cyberpunk(s):
    css = '''
.b-side{background:#0a0a1a;color:#e0e0e0;font-family:'Rajdhani','Share Tech Mono',sans-serif;line-height:1.5;position:relative}
.b-side *{box-sizing:border-box;margin:0;padding:0}
/* Scanlines overlay */
.b-side::before{content:'';position:fixed;inset:0;z-index:9998;pointer-events:none;background:repeating-linear-gradient(0deg,rgba(0,0,0,.08) 0px,rgba(0,0,0,.08) 1px,transparent 1px,transparent 3px)}
/* Glitch keyframes */
@keyframes glitchFlicker{0%,92%,100%{opacity:0}93%{opacity:.6;transform:translateX(4px)}95%{opacity:0}96%{opacity:.3;transform:translateX(-3px)}}
@keyframes neonPulse{0%,100%{opacity:1}50%{opacity:.85}}
.bh{display:flex;justify-content:space-between;align-items:center;padding:1rem 2rem;border-bottom:1px solid rgba(0,240,255,.15);position:sticky;top:0;z-index:100;background:rgba(10,10,26,.92);backdrop-filter:blur(8px)}
.bh .logo{font-family:'Share Tech Mono',monospace;font-size:1rem;color:#FF006E;letter-spacing:4px;text-shadow:0 0 10px #FF006E,0 0 30px rgba(255,0,110,.2);animation:neonPulse 3s infinite}
.bh nav a{color:rgba(0,240,255,.5);text-decoration:none;font-size:.72rem;letter-spacing:2px;text-transform:uppercase;font-family:'Share Tech Mono',monospace;margin-left:1.5rem;transition:all .3s}.bh nav a:hover{color:#00F0FF;text-shadow:0 0 8px rgba(0,240,255,.5)}
/* Hero with neon lines */
.bhero{min-height:85vh;display:flex;align-items:center;justify-content:center;text-align:center;padding:4rem 2rem;position:relative;overflow:hidden;background:linear-gradient(180deg,#0a0a1a,#0d0d2b 50%,#0a0a1a)}
.bhero::before{content:'';position:absolute;top:0;left:0;right:0;height:2px;background:linear-gradient(90deg,transparent,#FF006E,#00F0FF,transparent);box-shadow:0 0 15px rgba(255,0,110,.4)}
.bhero::after{content:'';position:absolute;bottom:0;left:0;right:0;height:1px;background:linear-gradient(90deg,transparent,#00F0FF,transparent)}
.bhero-inner{position:relative;z-index:2;max-width:600px}
.bhero-badge{width:60px;height:60px;margin:0 auto 1.5rem;clip-path:polygon(50% 0%,100% 25%,100% 75%,50% 100%,0% 75%,0% 25%);background:linear-gradient(135deg,rgba(255,0,110,.3),rgba(0,240,255,.3));display:flex;align-items:center;justify-content:center;position:relative}
.bhero-badge::after{content:'';position:absolute;inset:2px;clip-path:polygon(50% 0%,100% 25%,100% 75%,50% 100%,0% 75%,0% 25%);background:#0a0a1a}
.bhero-badge span{position:relative;z-index:1;font-family:'Share Tech Mono',monospace;font-size:.7rem;color:#00F0FF}
.bhero h1{font-size:clamp(2rem,5vw,3.5rem);font-weight:700;text-transform:uppercase;letter-spacing:6px;color:#fff;text-shadow:0 0 20px rgba(0,240,255,.4);margin-bottom:1rem;position:relative}
.bhero h1::after{content:attr(data-glitch);position:absolute;left:2px;top:1px;color:#FF006E;opacity:.25;clip-path:inset(0 0 60% 0)}
.bhero p{font-family:'Share Tech Mono',monospace;font-size:.8rem;color:rgba(0,240,255,.5);max-width:420px;margin:0 auto 2rem;line-height:1.8;letter-spacing:.5px}
.bbtn{font-family:'Rajdhani',sans-serif;padding:.7rem 2.2rem;font-size:.82rem;font-weight:700;letter-spacing:3px;text-transform:uppercase;cursor:pointer;transition:all .3s;border:none}
.bbtn-p{background:transparent;color:#FF006E;border:2px solid #FF006E;clip-path:polygon(0 0,calc(100% - 12px) 0,100% 12px,100% 100%,12px 100%,0 calc(100% - 12px));box-shadow:0 0 20px rgba(255,0,110,.2)}.bbtn-p:hover{background:#FF006E;color:#0a0a1a;box-shadow:0 0 40px rgba(255,0,110,.5)}
.bbtn-s{background:transparent;color:#00F0FF;border:1px solid rgba(0,240,255,.3);margin-left:.75rem;clip-path:polygon(0 0,calc(100% - 8px) 0,100% 8px,100% 100%,8px 100%,0 calc(100% - 8px))}.bbtn-s:hover{border-color:#00F0FF;box-shadow:0 0 15px rgba(0,240,255,.3)}
/* Sections */
.bsec{padding:5rem 2rem;border-top:1px solid rgba(255,0,110,.12)}
.bcon{max-width:1100px;margin:0 auto}
.bst{font-family:'Share Tech Mono',monospace;font-size:.7rem;color:#39FF14;letter-spacing:4px;text-shadow:0 0 8px rgba(57,255,20,.3);margin-bottom:.5rem}
.bsh{font-size:1.6rem;font-weight:700;text-transform:uppercase;letter-spacing:3px;margin-bottom:3rem;color:#fff}
/* Cards with angled corners */
.bgrid{display:grid;grid-template-columns:repeat(auto-fit,minmax(300px,1fr));gap:1.5rem}
.bcard{background:rgba(255,255,255,.03);border:1px solid rgba(0,240,255,.12);padding:2rem;clip-path:polygon(0 0,calc(100% - 16px) 0,100% 16px,100% 100%,16px 100%,0 calc(100% - 16px));position:relative;transition:all .3s}
.bcard::before{content:'';position:absolute;top:0;left:0;right:0;height:1px;background:linear-gradient(90deg,transparent,rgba(0,240,255,.3),transparent)}
.bcard:hover{border-color:rgba(0,240,255,.3);box-shadow:0 0 20px rgba(0,240,255,.08)}
.bcard h3{font-size:1rem;text-transform:uppercase;letter-spacing:2px;margin-bottom:.5rem;color:#00F0FF}
.bcard p{font-size:.85rem;color:rgba(224,224,224,.6);line-height:1.6}
.bcard-icon{font-family:'Share Tech Mono',monospace;font-size:.7rem;color:#FF006E;margin-bottom:.75rem;text-shadow:0 0 6px rgba(255,0,110,.4)}
/* Metrics */
.bmets{display:grid;grid-template-columns:repeat(4,1fr);gap:1rem;text-align:center}
.bmet{background:rgba(0,240,255,.04);border:1px solid rgba(0,240,255,.08);padding:2rem 1rem;clip-path:polygon(0 0,calc(100% - 8px) 0,100% 8px,100% 100%,8px 100%,0 calc(100% - 8px))}
.bmet-v{font-family:'Share Tech Mono',monospace;font-size:2rem;font-weight:700;color:#00F0FF;text-shadow:0 0 10px rgba(0,240,255,.4)}.bmet-l{font-size:.7rem;color:rgba(224,224,224,.4);text-transform:uppercase;letter-spacing:2px;margin-top:.25rem}
/* Glitch decoration */
.b-side .glitch-line{position:absolute;left:0;right:0;height:1px;background:#FF006E;opacity:0;animation:glitchFlicker 5s infinite;pointer-events:none}
/* Quote */
.bquote{max-width:560px;margin:0 auto;text-align:center;position:relative;padding:2rem 0}
.bquote::before{content:'//';font-family:'Share Tech Mono',monospace;color:rgba(0,240,255,.2);font-size:3rem;display:block;margin-bottom:1rem}
.bquote blockquote{font-size:1rem;color:rgba(224,224,224,.7);line-height:1.8;font-style:normal;font-family:'Share Tech Mono',monospace}.bquote cite{font-size:.75rem;color:rgba(0,240,255,.4);display:block;margin-top:.75rem;letter-spacing:2px}
/* Footer */
.bfoot{padding:2rem;border-top:1px solid rgba(0,240,255,.1);display:flex;justify-content:space-between;align-items:center;font-family:'Share Tech Mono',monospace}
.bfoot .logo{color:#FF006E;font-size:.85rem;letter-spacing:3px;text-shadow:0 0 8px rgba(255,0,110,.3)}
.bfoot nav a{color:rgba(0,240,255,.3);text-decoration:none;font-size:.7rem;letter-spacing:1px;margin-left:1.5rem}.bfoot nav a:hover{color:#00F0FF}
.bfoot small{font-size:.65rem;color:rgba(224,224,224,.2)}
@media(max-width:768px){.bmets{grid-template-columns:repeat(2,1fr)}.bh nav{display:none}.bhero{min-height:70vh}}
'''
    html = '''<div class="b-side">
<header class="bh"><div class="logo">NEXUS://SYS</div><nav><a href="#">Protocols</a><a href="#">Network</a><a href="#">Terminal</a><a href="#">Uplink</a></nav></header>
<section class="bhero"><div class="bhero-inner"><div class="bhero-badge"><span>NX</span></div><h1 data-glitch="INITIALIZE THE GRID">Initialize The Grid</h1><p>&gt; Next-gen interface systems for operators who demand absolute control. Precision-engineered. Battle-tested. Zero compromise.</p><div><button class="bbtn bbtn-p">ACCESS TERMINAL</button><button class="bbtn bbtn-s">SYS STATUS</button></div></div></section>
<section class="bsec"><div class="bcon"><div class="bst">[SYS::CAPABILITIES]</div><div class="bsh">Core Systems</div><div class="bgrid"><div class="bcard"><div class="bcard-icon">[MODULE_01]</div><h3>Neural Mesh</h3><p>Quantum-encrypted processing nodes with adaptive bandwidth allocation and real-time threat response.</p></div><div class="bcard"><div class="bcard-icon">[MODULE_02]</div><h3>Threat Matrix</h3><p>Predictive anomaly detection across all network segments. 0.3ms response time to hostile intrusion vectors.</p></div><div class="bcard"><div class="bcard-icon">[MODULE_03]</div><h3>Core Sync</h3><p>Multi-system synchronization with zero-downtime failover. Seamless handoff across distributed nodes.</p></div></div></div></section>
<section class="bsec"><div class="bcon"><div class="bst">[SYS::METRICS]</div><div class="bsh">System Status</div><div class="bmets"><div class="bmet"><div class="bmet-v">100%</div><div class="bmet-l">Uplink</div></div><div class="bmet"><div class="bmet-v">0.3ms</div><div class="bmet-l">Latency</div></div><div class="bmet"><div class="bmet-v">256bit</div><div class="bmet-l">Encrypted</div></div><div class="bmet"><div class="bmet-v">&infin;</div><div class="bmet-l">Scalable</div></div></div></div></section>
<section class="bsec"><div class="bcon"><div class="bquote"><blockquote>&gt; The most robust command interface we have ever deployed. Performance metrics exceeded all projections by 340%.</blockquote><cite>// CMDR. K. TANAKA &mdash; SECTOR 7</cite></div></div></section>
<footer class="bfoot"><div class="logo">NEXUS://SYS</div><nav><a href="#">Protocols</a><a href="#">Docs</a><a href="#">Status</a></nav></footer>
</div>'''
    return css, html


# ════════════════════════════════════════════════
# 3. GLASSMORPHISM
# ════════════════════════════════════════════════
@register(['glassmorphism.html'])
def gen_glass(s):
    css = '''
.b-side{background:linear-gradient(135deg,#667eea 0%,#764ba2 50%,#f093fb 100%);color:#fff;font-family:'Inter',system-ui,sans-serif;line-height:1.6;min-height:100vh;position:relative;overflow-x:hidden}
.b-side *{box-sizing:border-box;margin:0;padding:0}
/* Floating orbs */
.b-side .orb{position:fixed;border-radius:50%;filter:blur(80px);pointer-events:none;z-index:0}
.b-side .orb-1{width:400px;height:400px;background:rgba(102,126,234,.6);top:-100px;left:-100px}
.b-side .orb-2{width:300px;height:300px;background:rgba(240,147,251,.5);bottom:10%;right:-50px}
.b-side .orb-3{width:250px;height:250px;background:rgba(118,75,162,.5);top:40%;left:30%}
/* Glass panel mixin via shared class */
.glass{background:rgba(255,255,255,.1);backdrop-filter:blur(16px);-webkit-backdrop-filter:blur(16px);border:1px solid rgba(255,255,255,.18);border-radius:16px;box-shadow:0 8px 32px rgba(0,0,0,.12)}
.bh{position:sticky;top:0;z-index:100;padding:1rem 2rem}
.bh-inner{display:flex;justify-content:space-between;align-items:center;max-width:1100px;margin:0 auto;background:rgba(255,255,255,.08);backdrop-filter:blur(20px);-webkit-backdrop-filter:blur(20px);border:1px solid rgba(255,255,255,.15);border-radius:12px;padding:.75rem 1.5rem}
.bh .logo{font-weight:700;font-size:1.1rem;letter-spacing:-.01em}
.bh nav a{color:rgba(255,255,255,.7);text-decoration:none;font-size:.85rem;margin-left:1.5rem;transition:color .2s}.bh nav a:hover{color:#fff}
.bhero{min-height:80vh;display:flex;align-items:center;justify-content:center;text-align:center;padding:4rem 2rem;position:relative;z-index:1}
.bhero-inner{max-width:580px}
.bhero-tag{font-size:.8rem;text-transform:uppercase;letter-spacing:3px;color:rgba(255,255,255,.6);margin-bottom:1rem}
.bhero h1{font-size:clamp(2.5rem,5vw,3.5rem);font-weight:700;line-height:1.1;margin-bottom:1.5rem;letter-spacing:-.02em}
.bhero p{font-size:1.05rem;color:rgba(255,255,255,.7);max-width:460px;margin:0 auto 2rem;line-height:1.7}
.bbtn{font-family:inherit;padding:.8rem 2rem;border-radius:12px;font-size:.9rem;font-weight:600;cursor:pointer;transition:all .25s;border:none}
.bbtn-p{background:rgba(255,255,255,.2);color:#fff;backdrop-filter:blur(8px);border:1px solid rgba(255,255,255,.25)}.bbtn-p:hover{background:rgba(255,255,255,.3);transform:translateY(-2px);box-shadow:0 8px 24px rgba(0,0,0,.15)}
.bbtn-s{background:transparent;color:rgba(255,255,255,.8);border:1px solid rgba(255,255,255,.2);margin-left:.75rem}.bbtn-s:hover{border-color:rgba(255,255,255,.4)}
.bsec{padding:5rem 2rem;position:relative;z-index:1}
.bcon{max-width:1100px;margin:0 auto}
.bst{font-size:.75rem;text-transform:uppercase;letter-spacing:3px;color:rgba(255,255,255,.5);text-align:center;margin-bottom:.5rem}
.bsh{font-size:1.8rem;font-weight:700;text-align:center;margin-bottom:3rem}
.bgrid{display:grid;grid-template-columns:repeat(auto-fit,minmax(300px,1fr));gap:1.5rem}
.bcard{padding:2rem;transition:transform .3s,box-shadow .3s}
.bcard:hover{transform:translateY(-4px);box-shadow:0 12px 40px rgba(0,0,0,.2)}
.bcard h3{font-size:1.1rem;margin-bottom:.5rem}.bcard p{font-size:.9rem;color:rgba(255,255,255,.6);line-height:1.6}
.bcard-icon{width:44px;height:44px;border-radius:12px;background:rgba(255,255,255,.15);display:flex;align-items:center;justify-content:center;margin-bottom:1rem;font-size:1.3rem}
.bmets{display:grid;grid-template-columns:repeat(4,1fr);gap:1.5rem;text-align:center}
.bmet{padding:2rem 1rem}
.bmet-v{font-size:2.2rem;font-weight:800;line-height:1}.bmet-l{font-size:.8rem;color:rgba(255,255,255,.5);margin-top:.3rem;text-transform:uppercase;letter-spacing:1px}
.bquote{max-width:560px;margin:0 auto;text-align:center;padding:2.5rem;background:rgba(255,255,255,.06);backdrop-filter:blur(12px);border:1px solid rgba(255,255,255,.12);border-radius:20px}
.bquote blockquote{font-size:1.15rem;line-height:1.7;margin-bottom:.75rem;font-style:italic;color:rgba(255,255,255,.9)}.bquote cite{font-size:.85rem;color:rgba(255,255,255,.5)}
.bfoot{padding:2.5rem 2rem;position:relative;z-index:1;text-align:center}
.bfoot .logo{font-weight:700;font-size:1.1rem;margin-bottom:.75rem}
.bfoot nav{margin-bottom:.75rem}.bfoot nav a{color:rgba(255,255,255,.5);text-decoration:none;font-size:.8rem;margin:0 .75rem}.bfoot nav a:hover{color:#fff}
.bfoot small{font-size:.75rem;color:rgba(255,255,255,.3)}
@media(max-width:768px){.bh nav{display:none}.bmets{grid-template-columns:repeat(2,1fr)}.bgrid{grid-template-columns:1fr}}
'''
    html = '''<div class="b-side">
<div class="orb orb-1"></div><div class="orb orb-2"></div><div class="orb orb-3"></div>
<header class="bh"><div class="bh-inner"><div class="logo">Prism</div><nav><a href="#">Product</a><a href="#">Features</a><a href="#">Pricing</a><a href="#">About</a></nav></div></header>
<section class="bhero"><div class="bhero-inner"><p class="bhero-tag">The future of design</p><h1>Create Through Layers of Light.</h1><p>A design platform that brings depth, translucency, and beauty to every interface you build.</p><div><button class="bbtn bbtn-p">Get Started</button><button class="bbtn bbtn-s">Watch Demo</button></div></div></section>
<section class="bsec"><div class="bcon"><p class="bst">Features</p><h2 class="bsh">Frosted Perfection</h2><div class="bgrid"><div class="bcard glass"><div class="bcard-icon">&#9672;</div><h3>Depth Engine</h3><p>Multi-layered transparency system that creates authentic frosted glass depth in real time.</p></div><div class="bcard glass"><div class="bcard-icon">&#9673;</div><h3>Light Refraction</h3><p>Dynamic color blending that responds to background content, creating living surfaces.</p></div><div class="bcard glass"><div class="bcard-icon">&#9674;</div><h3>Blur Dynamics</h3><p>Variable backdrop blur intensities that establish clear visual hierarchy through opacity.</p></div></div></div></section>
<section class="bsec"><div class="bcon"><p class="bst">Metrics</p><h2 class="bsh">Crystal Clear Results</h2><div class="bmets"><div class="bmet glass"><div class="bmet-v">50K+</div><div class="bmet-l">Designers</div></div><div class="bmet glass"><div class="bmet-v">2M</div><div class="bmet-l">Components</div></div><div class="bmet glass"><div class="bmet-v">99.9%</div><div class="bmet-l">Uptime</div></div><div class="bmet glass"><div class="bmet-v">4.9&#9733;</div><div class="bmet-l">Rating</div></div></div></div></section>
<section class="bsec"><div class="bcon"><div class="bquote"><blockquote>&ldquo;The most beautiful design tool I have ever used. Every surface feels alive and responsive.&rdquo;</blockquote><cite>&mdash; Sarah Kim, Creative Director</cite></div></div></section>
<footer class="bfoot"><div class="logo">Prism</div><nav><a href="#">Privacy</a><a href="#">Terms</a><a href="#">Contact</a></nav><small>&copy; 2026 Prism. All rights reserved.</small></footer>
</div>'''
    return css, html


# ──────────────────────────────────────────────
# PROCESSOR
# ──────────────────────────────────────────────

def process_file(style):
    filepath = os.path.join('samples', style['file'])
    if not os.path.exists(filepath):
        print(f"SKIP: {filepath} not found")
        return False

    with open(filepath, 'r', encoding='utf-8') as f:
        original = f.read()

    if 'side-toggle' in original:
        print(f"SKIP: {style['file']} already processed")
        return False

    # Get generator
    gen_fn = GENERATORS.get(style['file'], _default_bside)
    bside_css, bside_html = gen_fn(style)

    # Extract body content
    body_match = re.search(r'<body[^>]*>(.*?)</body>', original, re.DOTALL)
    body_tag_match = re.search(r'(<body[^>]*>)', original)
    if not body_match:
        print(f"SKIP: {style['file']} no body")
        return False

    body_content = body_match.group(1)
    body_tag = body_tag_match.group(1) if body_tag_match else '<body>'

    # Insert CSS before </style>
    new_content = original.replace('</style>', TOGGLE_CSS + bside_css + '\n</style>')

    # Replace body
    body_start = re.search(r'<body[^>]*>', new_content)
    body_end = new_content.rfind('</body>')
    if body_start and body_end > 0:
        before = new_content[:body_start.start()]
        after = new_content[body_end + 7:]
        new_content = (before + body_tag + '\n' + TOGGLE_HTML + '\n<div class="a-side">\n' +
                      body_content + '\n</div>\n' + bside_html + '\n</body>' + after)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_content)

    print(f"OK: {style['file']} ({'custom' if gen_fn != _default_bside else 'default'})")
    return True


if __name__ == '__main__':
    ok = 0
    custom = 0
    for s in ALL_STYLES:
        if process_file(s):
            ok += 1
            if s['file'] in GENERATORS:
                custom += 1
    print(f"\nDone: {ok}/100 files ({custom} custom, {ok-custom} default)")

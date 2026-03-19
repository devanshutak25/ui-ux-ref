# Decisions

Architectural, tooling, and design decisions made during this project.

---

<!-- Format:
## YYYY-MM-DD — Decision Title
**Context:** Why the decision was needed
**Decision:** What was decided
**Rationale:** Why this option was chosen
-->

## 2026-03-20 — Batch 02 B-side CSS audit fixes
**Context:** Audit report (_reports_2/batch-02.md) identified B-side CSS/HTML issues across 5 styles: whitespace-maximalism, mono-space, e-ink, brutalism, neubrutalism. E-ink scored lowest at 5/10.
**Decision:** Applied targeted B-side-only CSS fixes per audit recommendations. No A-side code was modified.
**Rationale:** Each fix aligned with the style's Visual DNA specification. Key changes:
- whitespace-maximalism: h1 weight 200, padding 15vh 20vw, max-width 520px, @keyframes bFadeInUp, single-column card grid
- mono-space: max-width 80ch, ASCII-art ::before borders on sections, border-left hover instead of translateY, white-space:pre, muted foreground #b0b0b0
- e-ink: palette shifted from sepia to pure B&W (#FAFAFA/#111), stipple overlay via repeating-conic-gradient, text-align:justify;hyphens:auto, transition .8s steps(3), filter:grayscale(1) contrast(1.5) on card icons
- brutalism: raw #FF0000/#0000FF accents added, borders increased to 4px, padding reduced to 2rem, border-radius:0 on icons, color-inversion hover, footer double-period fixed
- neubrutalism: card border-radius 4px->12px, pastel section backgrounds, .bhero-tag as pill badge with border+shadow, quote wrapped in bordered card

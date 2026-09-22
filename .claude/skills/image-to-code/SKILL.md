---
name: image-to-code
description: Turn a reference image, screenshot, or mockup into token-driven, accessible code — infer the design system from the reference (palette, type scale, spacing, radius, layout archetype), map it to the 3-tier tokens, rebuild it, then verify with the kit's gates. Use when the user provides a design/screenshot and wants matching UI code.
invocation: user
---

# Skill: Image to Code

Reconstruct a design from a visual reference as a real design system, not a one-off copy. Match the *system* (color/type/spacing language), never lift copyrighted imagery or brand assets.

## Steps
1. **Read the reference like a designer.** Infer and write down:
   - **Palette** — 1 dominant surface family, text colors, 1 primary action + at most 1 accent (sample the hues; don't guess random hex).
   - **Type** — family feel (geometric/grotesk/serif), the scale jumps, display vs. body contrast, weights.
   - **Spacing & density** — base unit, section rhythm, card padding; airy vs. compact.
   - **Radius & depth** — radius language (sharp/soft/pill), shadow vs. hairline separation.
   - **Layout archetype + sequence** — full-bleed hero / asymmetric split / bento / editorial stack (`taste/design-taste.md` → Variance Mandate).
2. **Anchor to a known system** if it's close — browse `taste/aesthetic-systems.md` / `python3 scripts/design_systems.py search <term>` and adopt that recipe to stabilize decisions.
3. **Build the token theme** from the inferred values → 3-tier DTCG (`design-tokens` skill); generate a single `theme.css`. Verify every color pair with `scripts/contrast.py` / `scripts/validate_contrast.py` (light + dark) — a sampled brand color that fails AA gets adjusted; taste never overrides POUR.
4. **Rebuild layout + components** token-driven via `frameworks/adapter-protocol.md` + `components/*`: one shared primitive layer, all 8 states, a11y wired, no emoji (lucide), single theme. Apply taste (`taste/design-taste.md`) so it doesn't regress to generic.
5. **Verify against the reference** — render and screenshot it, compare side-by-side to the reference; run `node scripts/measure_render.mjs <file.html>`, `python3 scripts/lint_hardcodes.py <src>` and `node scripts/taste_audit.mjs <file.html>`, and report their actual output.

## Verification (definition of done)
- Every bundled gate passes over YOUR output — no hardcodes (`scripts/lint_hardcodes.py`), contrast AA in light **and** dark (`scripts/contrast.py` per pair, `scripts/validate_contrast.py` for a DTCG token file), and real-render WCAG (`scripts/measure_render.mjs`, plus `--dark`).
- The rebuilt UI uses ONE inferred token theme — no per-section palettes.
- A screenshot of the result visibly matches the reference's design language.

> Honest limit: this matches the design **system**, not a pixel-perfect copy. Do not reproduce the reference's photographs, logos, or copyrighted copy — substitute your own or generic placeholders.

## Bundled files (this skill is self-contained)

| Path | What |
|:---|:---|
| `taste/design-taste.md`, `taste/aesthetic-systems.md` | Aesthetic pre-flight + named system recipes |
| `design-systems/library/` | 138 design-system recipes, browsable via `scripts/design_systems.py` |
| `frameworks/` | Adapter protocol + per-framework adapters for the rebuild |
| `components/` | Component specs referenced by step 4 |
| `tokens/` | The 3-tier DTCG token set (`scripts/validate_contrast.py` reads `tokens/colors.json`) |
| `scripts/` | The gates — see below |

### Gates and their prerequisites

- `contrast.py`, `validate_contrast.py`, `lint_hardcodes.py`, `design_systems.py` — `python3`
  only, no dependencies. Usage is in each file's docstring.
- `taste_audit.mjs`, `measure_render.mjs` — render-based, so they need Node **and**
  Playwright (`npm i -D playwright && npx playwright install chromium`). Without it they
  fail to launch; say so rather than reporting a result you did not get.

### Not bundled

The upstream `npm run verify` wrapper and its `accuracy_report.mjs` gate are that repo's own
CI self-test over its own example tree — they do not test your generated code, so the steps above name
the real gates instead. The `design-tokens` and `apply-aesthetic` skills this file mentions
are not installed here; build the DTCG theme inline instead.

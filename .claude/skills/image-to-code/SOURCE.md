# Source

Bundled from [plugin87/ux-ui-agent-skills](https://github.com/plugin87/ux-ui-agent-skills).

- Upstream commit: `f2e2f7fcc5cb9d99bbd8ec5e0d75cebb98e21e7e` (v2.8.0, 2026-09-16)
- Bundled: 2026-09-22
- License: MIT — see `LICENSE` (© 2026 Thientan Soparat)

## Why the layout differs from upstream

Upstream is a **plugin** repo: its `SKILL.md` files sit under `.claude/skills/<name>/`
while everything they reference (`scripts/`, `frameworks/`, `components/`, `tokens/`,
`taste/`, `accessibility/`, `content/`, `workflows/`, `design-systems/`, `.claude/rules/`)
lives at the repo root. An earlier install here copied only the `SKILL.md`, which left
every reference in it pointing at a file that did not exist.

This skill now bundles those support files **inside the skill directory**, so it is
self-contained and its paths resolve. `.claude/rules/tokens-and-color.md` moved to
`rules/tokens-and-color.md` and the reference in `SKILL.md` was updated to match.

## Deliberately not bundled

- `accuracy_report.mjs` and the `npm run verify` wrapper — they are upstream's own CI
  self-test, hardcoded against that repo's `examples/` tree and `dist/` output. They do
  not check code this skill generates, so `SKILL.md` now names the portable gates instead.
- Upstream's `tests/`, `evals/`, `bin/` and `package.json`, and its other 17 skills
  (`design-tokens`, `apply-aesthetic`, `a11y-audit`, …) which are not installed here.

## Prerequisites

The Python gates need `python3` only. The render-based `.mjs` gates need Node plus
Playwright (`npm i -D playwright && npx playwright install chromium`); without it they
print "playwright not installed — SKIPPED" and exit 0, so a skipped gate must be reported
as skipped, never as a pass.

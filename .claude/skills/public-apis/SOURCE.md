# Source

Catalog data extracted from [public-apis/public-apis](https://github.com/public-apis/public-apis).

- Upstream commit: `f4e3de11d81c745a68b28850f7ffcfd9322ab339` (2026-09-21)
- Extracted: 2026-09-22
- Rows: 1888 APIs across 51 categories
- License: MIT — see `LICENSE` (© 2022 public-apis)

## What was and was not taken

The upstream repository is **not a Claude Code skill** — it is a `README.md`
listing APIs plus Python scripts that CI uses to validate the table format and
check links. Only the curated API tables were taken, converted to
`references/apis.csv` / `references/apis.md` by `scripts/build-catalog.py`.
The `SKILL.md`, the search helper and this file were written for this repo.

Not included: the upstream APILayer sponsor/promo block at the top of the
README, its `scripts/` link-validation CI tooling, and `CONTRIBUTING.md`.

## Known data quirks handled by the builder

- One row (`CalorieNinjas`) has a BEL control character where upstream meant
  `\apiKey\`; the builder restores it to `apiKey`.
- A few rows carry stray trailing pipes, which the builder tolerates.
- Auth values are normalized to `No`, `apiKey`, `OAuth`, `X-Mashape-Key`,
  `User-Agent`.

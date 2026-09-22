---
name: public-apis
description: Find a free or public HTTP API for a given need — weather, geocoding, currency rates, test data, ML, sports, government open data and 45 other categories. Use when the user asks "is there an API for X", needs a data source for a demo/prototype, wants an API that works without a key, or is comparing providers for a feature. Searches a bundled, offline catalog of ~1,900 community-curated APIs with auth, HTTPS and CORS flags.
---

# public-apis

An offline, greppable catalog of ~1,900 public APIs, bundled from
[public-apis/public-apis](https://github.com/public-apis/public-apis) (MIT).
Use it to answer "what API can I use for X?" without a web search.

## Files

| Path | What it is |
|:---|:---|
| `references/apis.csv` | The catalog: `category,name,url,auth,https,cors,description` (~240 KB) |
| `references/apis.md` | Same data as Markdown tables, grouped by category |
| `scripts/find-api.py` | Search helper — filters and prints a Markdown table |
| `scripts/build-catalog.py` | Regenerates both catalogs from an upstream `README.md` |

**Do not read `apis.csv` or `apis.md` in full** — each is ~240 KB and will
swamp the context. Always search first.

## How to search

Prefer the helper:

```bash
python3 .claude/skills/public-apis/scripts/find-api.py weather --no-auth --limit 5
python3 .claude/skills/public-apis/scripts/find-api.py --category "Machine Learning"
python3 .claude/skills/public-apis/scripts/find-api.py currency exchange --https
```

Every positional term must match the name, description or category
(case-insensitive). Flags: `--category NAME`, `--no-auth` (no API key needed),
`--cors`, `--https`, `--limit N` (0 = all), `--format md|csv`.

Plain `grep` works too when you want a raw line:

```bash
grep -i "geocod" .claude/skills/public-apis/references/apis.csv
```

## Categories

`Animals`, `Anime`, `Anti-Malware`, `Art & Design`, `Authentication & Authorization`,
`Blockchain`, `Books`, `Business`, `Calendar`, `Cloud Storage & File Sharing`,
`Continuous Integration`, `Cryptocurrency`, `Currency Exchange`, `Data Validation`,
`Development`, `Dictionaries`, `Documents & Productivity`, `Email`, `Entertainment`,
`Environment`, `Events`, `Finance`, `Food & Drink`, `Games & Comics`, `Geocoding`,
`Government`, `Health`, `Jobs`, `Machine Learning`, `Music`, `News`, `Open Data`,
`Open Source Projects`, `Patent`, `Personality`, `Phone`, `Photography`,
`Programming`, `Science & Math`, `Security`, `Shopping`, `Social`,
`Sports & Fitness`, `Test Data`, `Text Analysis`, `Tracking`, `Transportation`,
`URL Shorteners`, `Vehicle`, `Video`, `Weather`

## Reporting results

Give a short shortlist (3–5), not the raw dump, and for each one say: what it
does, whether it needs a key (`auth`), whether it is browser-callable (`cors`),
and the docs link. When the user is building something client-side, prefer
`--no-auth --cors --https`. When they need production reliability, say plainly
that this catalog does not rank APIs by uptime or rate limits.

## Caveats — state these when they matter

- The catalog is **community-curated and a point-in-time snapshot** (see
  `SOURCE.md` for the upstream commit and date). Endpoints get deprecated,
  free tiers get removed, and the `auth`/`https`/`cors` columns can be stale.
  Verify against the provider's own docs before anyone builds on it.
- "Public" means publicly documented, **not** vetted, audited, or safe for
  sensitive data. Do not send personal or secret data to an API just because
  it is on this list.
- Some entries are paid products with a free tier, and a few links carry the
  upstream repo's `utm_*` referral parameters.
- Not all listed APIs are still reachable; the catalog is not link-checked here.

## Refreshing the catalog

```bash
git clone --depth 1 https://github.com/public-apis/public-apis /tmp/public-apis
python3 .claude/skills/public-apis/scripts/build-catalog.py /tmp/public-apis/README.md
```

It rewrites `references/apis.csv` and `references/apis.md` in place and prints
the row count. Update `SOURCE.md` with the new commit afterwards.

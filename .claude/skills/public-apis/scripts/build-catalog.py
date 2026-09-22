#!/usr/bin/env python3
"""Rebuild the bundled catalog from a public-apis README.md.

usage: build-catalog.py <path-to-public-apis-README.md>

Writes references/apis.csv and references/apis.md next to this skill.
Run it after pulling a fresh copy of https://github.com/public-apis/public-apis
to refresh the catalog.
"""
import csv
import pathlib
import re
import sys

ROW = re.compile(r"^\|\s*\[(?P<name>[^\]]+)\]\((?P<url>[^)]+)\)\s*\|(?P<rest>.*)$")
SKILL_DIR = pathlib.Path(__file__).resolve().parent.parent

# A handful of upstream rows carry stray backticks, backslashes or control
# characters in the auth cell (e.g. a literal BEL in "\apiKey\"). Normalize so
# the column stays greppable.
AUTH_ALIASES = {"apikey": "apiKey", "oauth": "OAuth", "no": "No",
                "unknown": "Unknown", "user-agent": "User-Agent",
                "x-mashape-key": "X-Mashape-Key"}


def clean_auth(cell: str) -> str:
    # "\apiKey\" reached the README with its "\a" already collapsed to a BEL;
    # put the letter back before dropping the remaining control characters.
    value = re.sub(r"[`\\\x00-\x1f]", "", cell.replace("\x07", "a")).strip()
    return AUTH_ALIASES.get(value.lower(), value or "Unknown")


def parse(readme: pathlib.Path):
    category = None
    started = False
    for line in readme.read_text(encoding="utf-8").splitlines():
        if line.startswith("## License"):
            break
        if line.startswith("### "):
            name = line[4:].strip()
            # The promo block above the catalog also uses "###" headings;
            # the catalog proper starts at the first category with a table.
            if not started and name != "Animals":
                continue
            started = True
            category = name
            continue
        if not started:
            continue
        m = ROW.match(line)
        if not m:
            continue
        cells = [c.strip() for c in m.group("rest").split("|")]
        # description | auth | https | cors  (some rows carry stray trailing pipes)
        desc, auth, https, cors = (cells + ["", "", "", ""])[:4]
        yield {
            "category": category,
            "name": m.group("name").strip(),
            "url": m.group("url").strip(),
            "auth": clean_auth(auth),
            "https": https or "Unknown",
            "cors": cors or "Unknown",
            "description": desc,
        }


def main() -> int:
    if len(sys.argv) != 2:
        print(__doc__.strip(), file=sys.stderr)
        return 1
    rows = list(parse(pathlib.Path(sys.argv[1])))
    if not rows:
        print("no API rows parsed — is that a public-apis README?", file=sys.stderr)
        return 1

    fields = ["category", "name", "url", "auth", "https", "cors", "description"]
    csv_path = SKILL_DIR / "references" / "apis.csv"
    with csv_path.open("w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=fields)
        w.writeheader()
        w.writerows(rows)

    md = ["# Public APIs catalog", "",
          f"{len(rows)} APIs across {len({r['category'] for r in rows})} categories.",
          "Source: https://github.com/public-apis/public-apis (MIT).", ""]
    current = None
    for r in rows:
        if r["category"] != current:
            current = r["category"]
            md += ["", f"## {current}", "",
                   "| API | Description | Auth | HTTPS | CORS |",
                   "|:---|:---|:---|:---|:---|"]
        md.append(f"| [{r['name']}]({r['url']}) | {r['description']} | "
                  f"{r['auth']} | {r['https']} | {r['cors']} |")
    (SKILL_DIR / "references" / "apis.md").write_text("\n".join(md) + "\n", encoding="utf-8")

    print(f"{len(rows)} APIs -> {csv_path} and references/apis.md")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

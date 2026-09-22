#!/usr/bin/env python3
"""Search the bundled public-apis catalog.

usage: find-api.py <terms...> [--category NAME] [--no-auth] [--cors]
                              [--https] [--limit N] [--format md|csv]

Every term must match somewhere in the row (name, description or category),
case-insensitively. Examples:

  find-api.py weather --no-auth
  find-api.py currency exchange --https --limit 5
  find-api.py --category "Machine Learning"
"""
import argparse
import csv
import pathlib
import sys

CATALOG = pathlib.Path(__file__).resolve().parent.parent / "references" / "apis.csv"


def main() -> int:
    ap = argparse.ArgumentParser(add_help=True, description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("terms", nargs="*", help="all terms must match")
    ap.add_argument("--category", help="restrict to one category (substring match)")
    ap.add_argument("--no-auth", action="store_true", help="only APIs needing no key")
    ap.add_argument("--cors", action="store_true", help="only APIs with CORS=Yes")
    ap.add_argument("--https", action="store_true", help="only APIs with HTTPS=Yes")
    ap.add_argument("--limit", type=int, default=25, help="max rows (default 25, 0 = all)")
    ap.add_argument("--format", choices=("md", "csv"), default="md")
    args = ap.parse_args()

    if not CATALOG.exists():
        print(f"catalog missing: {CATALOG}", file=sys.stderr)
        return 1

    rows = []
    with CATALOG.open(encoding="utf-8") as fh:
        for row in csv.DictReader(fh):
            hay = f"{row['name']} {row['description']} {row['category']}".lower()
            if not all(t.lower() in hay for t in args.terms):
                continue
            if args.category and args.category.lower() not in row["category"].lower():
                continue
            if args.no_auth and row["auth"] != "No":
                continue
            if args.cors and row["cors"] != "Yes":
                continue
            if args.https and row["https"] != "Yes":
                continue
            rows.append(row)

    total = len(rows)
    if args.limit:
        rows = rows[: args.limit]

    if args.format == "csv":
        w = csv.DictWriter(sys.stdout, fieldnames=list(rows[0]) if rows else
                           ["category", "name", "url", "auth", "https", "cors", "description"])
        w.writeheader()
        w.writerows(rows)
    else:
        if not rows:
            print("No match. Try fewer terms, or drop --no-auth/--cors.")
            return 0
        print("| API | Category | Description | Auth | HTTPS | CORS |")
        print("|:---|:---|:---|:---|:---|:---|")
        for r in rows:
            print(f"| [{r['name']}]({r['url']}) | {r['category']} | {r['description']} "
                  f"| {r['auth']} | {r['https']} | {r['cors']} |")
        if total > len(rows):
            print(f"\n({len(rows)} of {total} matches shown — raise --limit for more.)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

#!/usr/bin/env python3
"""Fetch all publications from the HAL API for a given IdHAL and write them
to Jekyll's _data/publications.json.

Fails safe: if the API is unreachable or returns an error, the existing
publications.json (if any) is left untouched and the script exits non-zero.
"""

import json
import re
import sys
import time
import urllib.parse
import urllib.request
from pathlib import Path

IDHAL = "ninon-burgos"
API_URL = "https://api.archives-ouvertes.fr/search/"
PAGE_SIZE = 100
MAX_PAGES = 50
OUTPUT = Path(__file__).resolve().parents[1] / "_data" / "publications.json"

FIELDS = ",".join(
    [
        "title_s",
        "authFullName_s",
        "authFirstName_s",
        "authLastName_s",
        "docType_s",
        "audience_s",
        "proceedings_s",
        "publicationDate_s",
        "producedDate_s",
        "journalTitle_s",
        "journalPublisher_s",
        "conferenceTitle_s",
        "bookTitle_s",
        "publisher_s",
        "volume_s",
        "issue_s",
        "page_s",
        "doiId_s",
        "uri_s",
        "submittedDate_s",
    ]
)

DOCTYPE_LABELS = {
    "ART": "Journal articles",
    "COMM": "Conference papers",
    "COUV": "Book chapters",
    "OTHER": "Other publications",
    "OUV": "Books",
    "DOUV": "Book directions",
    "PROCEEDINGS": "Conference proceedings",
    "POSTER": "Posters",
    "HDR": "Thesis",
    "THESES": "Thesis",
    "LECT": "Lectures",
    "IMG": "Images",
    "VIDEO": "Videos",
    "SON": "Sounds",
    "MAP": "Maps",
    "REPORT": "Reports",
    "UNDEFINED": "Other",
}


def fetch_page(start):
    """Fetch one page of results from the HAL API."""
    params = {
        "q": f"authIdHal_s:{IDHAL}",
        "wt": "json",
        "rows": str(PAGE_SIZE),
        "start": str(start),
        "fl": FIELDS,
        "sort": "publicationDate_s desc",
    }
    url = f"{API_URL}?{urllib.parse.urlencode(params)}"
    req = urllib.request.Request(url, headers={"User-Agent": "ninonburgos.com HAL sync"})
    with urllib.request.urlopen(req, timeout=60) as response:
        return json.load(response)["response"]


def clean(value):
    """Return the first element for list fields, None for missing fields."""
    if isinstance(value, list):
        return value[0] if value else None
    return value


def initial(first_name):
    """Convert a first name to initials: 'Hugues' -> 'H.', 'Jean-Baptiste' -> 'J.-B.'."""
    if not first_name:
        return ""
    return "-".join(
        f"{part[0].upper()}." for part in re.split(r"[\s-]+", first_name.strip()) if part
    )


def format_authors(doc):
    """Build the author string with first-name initials, e.g. 'H. Roy, R. Dorent, N. Burgos'.

    Uses HAL's parallel authFirstName_s/authLastName_s lists when available,
    falling back to authFullName_s otherwise.
    """
    first_names = doc.get("authFirstName_s") or []
    last_names = doc.get("authLastName_s") or []
    full_names = doc.get("authFullName_s") or []
    if last_names and len(last_names) == len(first_names):
        return ", ".join(
            f"{initial(first)} {last}".strip()
            for first, last in zip(first_names, last_names)
        )
    return ", ".join(full_names)


def normalize(doc):
    """Map a raw HAL document to a flat record for the website."""
    venue_parts = []
    journal = clean(doc.get("journalTitle_s"))
    conference = clean(doc.get("conferenceTitle_s"))
    book = clean(doc.get("bookTitle_s"))
    publisher = clean(doc.get("journalPublisher_s")) or clean(doc.get("publisher_s"))
    volume = clean(doc.get("volume_s"))
    issue = clean(doc.get("issue_s"))
    pages = clean(doc.get("page_s"))

    if journal:
        venue_parts.append(journal)
        if volume:
            venue_parts.append(f"vol. {volume}")
        if issue:
            venue_parts.append(f"no. {issue}")
        if pages:
            venue_parts.append(f"pp. {pages}")
    elif conference:
        venue_parts.append(f"In {conference}")
        if pages:
            venue_parts.append(f"pp. {pages}")
    elif book:
        venue_parts.append(f"In {book}")
    if publisher:
        venue_parts.append(publisher)

    pub_date = clean(doc.get("publicationDate_s"))
    year = pub_date[:4] if pub_date else None

    doc_type = clean(doc.get("docType_s"))
    type_label = DOCTYPE_LABELS.get(doc_type, "Other")
    section_label = type_label
    if doc_type == "COMM":
        audience = clean(doc.get("audience_s"))
        proceedings = clean(doc.get("proceedings_s"))
        scope = "national" if audience == "3" else "international"
        proc = "with proceedings" if proceedings == "1" else "without proceedings"
        section_label = f"Conference papers — {scope}, {proc}"

    return {
        "title": clean(doc.get("title_s")),
        "authors": format_authors(doc),
        "type": doc_type,
        "type_label": type_label,
        "section_label": section_label,
        "venue": ", ".join(venue_parts) if venue_parts else None,
        "year": year,
        "doi": clean(doc.get("doiId_s")),
        "uri": clean(doc.get("uri_s")),
        "submitted": clean(doc.get("submittedDate_s")),
    }


def main():
    try:
        response = fetch_page(0)
    except Exception as exc:  # noqa: BLE001
        print(f"ERROR: could not reach HAL API: {exc}", file=sys.stderr)
        sys.exit(1)

    total = response.get("numFound", 0)
    if total == 0:
        print("ERROR: HAL API returned 0 documents — aborting to protect existing data.", file=sys.stderr)
        sys.exit(1)

    docs = list(response.get("docs", []))
    start = PAGE_SIZE
    while len(docs) < total and (start // PAGE_SIZE) < MAX_PAGES:
        time.sleep(0.5)
        try:
            response = fetch_page(start)
        except Exception as exc:  # noqa: BLE001
            print(f"ERROR: could not reach HAL API: {exc}", file=sys.stderr)
            sys.exit(1)
        docs.extend(response.get("docs", []))
        start += PAGE_SIZE

    pubs = [normalize(doc) for doc in docs]
    # Deterministic order for stable diffs between runs
    pubs.sort(key=lambda p: (p["year"] or "0000", p["submitted"] or "", p["title"] or ""))
    pubs.reverse()

    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    with OUTPUT.open("w", encoding="utf-8") as f:
        json.dump(pubs, f, ensure_ascii=False, indent=2, sort_keys=True)
        f.write("\n")

    print(f"OK: wrote {len(pubs)} publications to {OUTPUT}")


if __name__ == "__main__":
    main()

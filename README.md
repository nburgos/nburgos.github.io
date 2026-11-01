# ninonburgos.com

Personal website of Ninon Burgos, built with Jekyll and hosted on GitHub Pages.
Live at <https://nburgos.github.io> until the custom domain is connected (see
[Deployment](#deployment) below).

## Editing content

Pages are Markdown files at the repository root. Edit them on GitHub (or
locally) and push to `main` — the site rebuilds automatically.

| Task | Where |
| --- | --- |
| Home bio, contact card | `index.md` |
| Email, photo, CV link, footer/social links, nav labels | `_config.yml` |
| CV PDF | drop the file into `files/`, set `author.cv` in `_config.yml` |
| Research projects | `research-projects/*.md`; add the page + one entry under `nav:` in `_config.yml` (Ongoing/Past group) |
| Software page | `software.md` (foldable `<details>` sections) |

## Publications

`_data/publications.json` is **auto-generated** — never edit it manually.

- `scripts/fetch_publications.py` fetches all publications from the
  [HAL API](https://api.archives-ouvertes.fr) for IdHAL `ninon-burgos` and
  classifies them into sections (e.g. national vs international conference
  abstracts, from HAL's `audience`/`proceedings` fields).
- A scheduled GitHub Action
  (`.github/workflows/update-publications.yml`) runs the script every Monday
  at 06:00 UTC and commits the result if anything changed. It can also be
  triggered manually from the Actions tab
  ("Update publications from HAL" → "Run workflow").
- The homepage shows the 9 most recent publications, **excluding national
  conference abstracts** (filter in `_includes/latest-pubs.html`).

## Styling & front-end

- Colors live in `_sass/_variables.scss` (palette from Awesome-CV). Partials
  in `_sass/` are imported by `assets/css/main.scss`.
- `assets/js/main.js`: dark/light theme toggle, mobile hamburger menu, and
  the year filter chips on the publications page.
- Breakpoints: ≤ 900px switches to the hamburger menu, ≤ 767px stacks the
  page layout.

## Local development

```sh
export PATH="/opt/homebrew/opt/ruby@3.3/bin:$PATH"  # Homebrew Ruby 3.3 (macOS)
bundle install
bundle exec jekyll serve   # → http://localhost:4000
```

To refresh publications manually:

```sh
python3 scripts/fetch_publications.py
```

## Deployment

Push to `main` — GitHub Pages builds and deploys automatically.

**Custom domain (ninonburgos.com):** DNS still points to the old WordPress
site. The `CNAME` file is intentionally **absent** until the cutover at the
registrar — with a `CNAME` present, GitHub redirects `nburgos.github.io` to
`ninonburgos.com`, which would break the preview URL. At cutover: point the
domain's A/AAAA records and the `www` CNAME at GitHub Pages, restore the
`CNAME` file, then enforce HTTPS in the repository's Pages settings.

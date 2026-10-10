# ninonburgos.com

Personal website of Ninon Burgos, built with Jekyll and hosted on GitHub Pages.

## Structure

- Pages are Markdown files at the repository root (edit on GitHub → site rebuilds automatically).
- `_data/publications.json` is **auto-generated** — do not edit it manually.
- `_layouts`, `_includes`, `_sass`: templates and styles. Colors live in `_sass/_variables.scss`.

## Publications sync

`scripts/fetch_publications.py` fetches all publications from the
[HAL API](https://api.archives-ouvertes.fr) for IdHAL `ninon-burgos` and writes
`_data/publications.json`. A scheduled GitHub Action
(`.github/workflows/update-publications.yml`) runs it every Monday and commits
the result if anything changed. It can also be triggered manually from the
Actions tab ("Update publications from HAL" → "Run workflow").

## Local development

```sh
bundle install
bundle exec jekyll serve
# → http://localhost:4000
```

To refresh publications manually:

```sh
python3 scripts/fetch_publications.py
```

## Deployment

Push to the `main` branch — GitHub Pages builds and deploys automatically.
The custom domain (ninonburgos.com) is configured via the `CNAME` file and the
repository settings.

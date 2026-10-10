# Migration Plan: ninonburgos.com → GitHub Pages

Personal website of Ninon Burgos (CNRS researcher), migrating from WordPress to a GitHub Pages + Jekyll site with automatic HAL publication syncing.

## 1. Stack & rationale

- **GitHub Pages + Jekyll**: pages are plain Markdown, GitHub builds and hosts for free, editable directly on github.com (even from a browser). Lowest-machinery option that satisfies "simple to manage".
- No database, no PHP, no local tooling required for day-to-day edits.
- Alternatives considered and rejected: Hugo (needs local build tooling / more setup), Astro (more JS machinery than needed).

## 2. Repository

- Repo: **`nburgos/nburgos.github.io`** (GitHub username: `nburgos`; name verified free — existing repos are `aramis-lab.github.io` and `OHBM2020_ML4NI`).
- A user-site repo gets the automatic preview URL `https://nburgos.github.io` before the domain switch.
- Local development copy: `/Users/ninon.burgos/OpenCode/ninon_website`.

## 3. Site structure

```
nburgos.github.io/
├── _config.yml                  # title, description, domain, Jekyll settings
├── _layouts/                    # base.html, home, page templates
├── _includes/                   # header, footer, pub-card, latest-pubs widget
├── _sass/ + assets/             # responsive, dual-theme design (see §4–6)
├── _data/
│   └── publications.json        # AUTO-GENERATED from HAL (all ~155 docs)
├── index.md                     # Home: bio + photo + CV link + "Latest publications" (auto)
├── publications.md              # full auto-generated list, grouped by type, newest first
├── research-projects/
│   ├── ongoing/                 # deep generative models (brain PET); ML/clinical data warehouse
│   └── past/                    # PhD; postdoc MRRTP; postdoc abnormality maps
├── software.md                  # Clinica, ClinicaDL, AD-ML/AD-DL, NiftyWeb, NiftySeg
├── files/                       # CV PDF + photo (copied from WordPress)
├── scripts/
│   └── fetch_publications.py     # queries HAL API → writes publications.json
├── CNAME                        # contains: ninonburgos.com
└── .github/workflows/
    └── update-publications.yml   # weekly sync + manual trigger + keepalive
```

**Navigation:** Home ● Research projects ● Publications ● Software ● ARAMIS Lab (external), plus social links bar (Google Scholar, HAL, Publons, LinkedIn, ResearchGate, Zotero).

**Home page contains only** the About section (bio, photo, CV link) and the auto-generated latest publications — representative publications were deliberately removed per decision.

## 4. Colour system: dual theme (light + dark)

All colours defined once as **CSS custom properties**, switched via `data-theme` attribute on `<html>`:

| Token | Light mode | Dark mode | Used for |
|---|---|---|---|
| `--bg` | `#ffffff` | `#0b1618` (near-black, teal-tinted) | page background |
| `--text` | `#1f2933` | `#e4edf0` | body text |
| `--accent` | `#0a7e8c` (Metallic Seaweed) | `#4cc3d3` (lightened seaweed, WCAG AA on dark) | links, nav hover/active, accent rules, badges |
| `--accent-strong` | `#064b54` (dark awesome) | `#9fd8e0` | site title, page headings, button hover |
| `--surface` | `#e6f3f4` (10% tint) | `#12323a` (dark teal surface) | cards, highlight boxes, latest-pubs background |
| `--footer-bg` | `#064b54` | `#064b54` (white text works on both) | footer |

SCSS source tokens: `$awesome: #0a7e8c;` and `$dark-awesome: #064b54;` (palette from Awesome-CV, `\definecolor{awesome}{HTML}{0a7e8c}`, `\definecolor{darkawesome}{HTML}{064B54}`).

Rationale: `#0a7e8c` has poor contrast on dark backgrounds, so dark mode links use a lightened variant — **both themes meet WCAG AA (≥4.5:1)** for text and UI elements.

## 5. Theme behaviour

1. Default: follow the OS/browser setting via `prefers-color-scheme`.
2. Manual override: sun/moon toggle button in the header (inline SVG, no icon library), persisted in `localStorage`, applied on every page.
3. No flash of wrong theme: tiny inline `<script>` in `<head>` resolves theme (localStorage → OS fallback) and sets `data-theme` before first paint.
4. Pure CSS switching — no page reload; Jekyll/GitHub Pages compatible out of the box.

## 6. Mobile responsiveness

- Viewport meta on all pages; fluid typography via `clamp()`.
- Collapsible hamburger navigation under ~768px (nav + social links); horizontal bar on desktop.
- Single column on phones; bio photo floats beside text on desktop, stacks on mobile. Breakpoints ~640/768/1024px.
- Images: `max-width: 100%`; profile photo served at 2 sizes via `srcset`.
- Publication cards: metadata stacks vertically on narrow screens; DOI/HAL links get ≥44px tap targets.
- Tables horizontally scrollable on mobile.
- Accessibility: visible focus styles, `aria-label` on theme toggle and menu button, `prefers-reduced-motion` respected.

## 7. HAL automation (core requirement)

- `fetch_publications.py` queries `https://api.archives-ouvertes.fr/search/?q=authIdHal_s:ninon-burgos` (IdHAL `ninon-burgos`; verified working, 155 docs) with pagination (`start`/`rows`), retrieving title, authors, doc type, journal/conference, year, volume/issue/pages, DOI, HAL URI, deposit date.
- Writes `_data/publications.json`; Jekyll renders it. **Publications are never edited manually.**
- Home page: top ~9 by deposit date ("Latest publications", matching the old WordPress sidebar behaviour).
- Publications page: all documents grouped by type (Journal articles / Conference papers / etc.), newest first, each with DOI + HAL links.
- GitHub Action (`update-publications.yml`): weekly cron + `workflow_dispatch` manual trigger; commits updated JSON only if changed → triggers rebuild. Fails safe: if HAL is unreachable, existing data is kept. A keepalive touch-commit prevents GitHub's 60-day scheduled-workflow auto-disable.
- BibTeX: Publications page links to HAL's live export (`...&wt=bibtex`) — always current, zero maintenance.

## 8. Content migration

From the WordPress site (fetched and reviewed):

- About/bio text, CV PDF (`https://ninonburgos.com/wp-content/uploads/2025/10/2025.10.16_CV_NinonBurgos.pdf`), profile photo (`NinonBurgos_2019.jpg`).
- 5 research project pages (2 ongoing, 3 past).
- Software page: Clinica, ClinicaDL, AD-ML/AD-DL, NiftyWeb, NiftySeg with references.
- Social links: Google Scholar, HAL, Publons, LinkedIn, ResearchGate, Zotero.
- Malformed WordPress-generated DOI/link URLs are fixed during migration.

## 9. Custom domain: ninonburgos.com

1. `CNAME` file in repo + custom domain set in repo Settings → Pages.
2. DNS records at the registrar:

| Type | Name | Value |
|---|---|---|
| A | `@` | `185.199.108.153`, `185.199.109.153`, `185.199.110.153`, `185.199.111.153` |
| AAAA | `@` | `2606:50c0:8000::153`, `2606:50c0:8001::153`, `2606:50c0:8002::153`, `2606:50c0:8003::153` |
| CNAME | `www` | `nburgos.github.io` |

3. GitHub auto-redirects `www` ↔ apex; remove any wildcard records.
4. After DNS propagates (up to 24h), enable **Enforce HTTPS** (free Let's Encrypt certificate).

## 10. Launch sequence (zero downtime)

1. Build the full site locally in `~/OpenCode/ninon_website`.
2. Push to `nburgos/nburgos.github.io`; review at `https://nburgos.github.io`.
3. Switch DNS per §9; WordPress stays up until propagation completes.
4. Verify `https://ninonburgos.com` + enforce HTTPS.
5. Cancel WordPress hosting (keep the domain registered; consider moving DNS to a standalone registrar if currently bundled with the host).

## 11. Day-to-day maintenance

- Edit content: open the Markdown file on github.com → edit → commit → live in ~1 minute.
- Publications: update themselves weekly (plus manual "Run workflow" button). New HAL deposits appear automatically.

## 12. Caveats

- GitHub auto-disables scheduled workflows after 60 days of no repo activity — mitigated by the keepalive commit in the Action; otherwise one click re-enables.
- Ensure `ninonburgos.com` is registered in the owner's name so DNS stays under her control.
- No comments, no forms, no dynamic features — by design (static site).

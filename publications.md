---
layout: page
title: Publications
permalink: /publications/
---

<p class="pub-intro">
  All my publications, automatically synced from
  <a href="{{ site.social.hal }}" target="_blank" rel="noopener">HAL</a>.
</p>

{%- assign pubs = site.data.publications -%}
{%- assign groups = pubs | group_by: "section_label" -%}
{%- assign ordered_groups = "" | split: "" -%}
{%- assign order = "Journal articles|Conference papers — international, with proceedings|Conference papers — international, without proceedings|Conference papers — national, without proceedings|Conference papers — national, with proceedings|Conference proceedings|Book chapters|Books|Other" | split: "|" -%}
{%- for label in order -%}
  {%- for group in groups -%}
    {%- if group.name == label -%}
      {%- assign ordered_groups = ordered_groups | push: group -%}
    {%- endif -%}
  {%- endfor -%}
{%- endfor -%}
{%- assign counter = 0 -%}
{%- for group in ordered_groups -%}
{%- assign counter = counter | plus: 1 -%}
{%- assign years = "" | split: "" -%}
{%- for pub in group.items -%}
  {%- if pub.year -%}
    {%- unless years contains pub.year -%}
      {%- assign years = years | push: pub.year -%}
    {%- endunless -%}
  {%- endif -%}
{%- endfor -%}
{%- assign years = years | sort | reverse -%}
<details class="pub-group" {% if counter == 1 %}open{% endif %}>
  <summary class="pub-type-heading">
    <span class="pub-type-title">{{ group.name }}</span>
    <span class="pub-count">{{ group.items | size }} documents</span>
  </summary>
  <div class="year-filters" role="group" aria-label="Filter {{ group.name }} by year">
    <button type="button" class="year-filter is-active" data-year="all" aria-pressed="true">All</button>
    {%- for year in years -%}
    <button type="button" class="year-filter" data-year="{{ year }}" aria-pressed="false">{{ year }}</button>
    {%- endfor -%}
  </div>
  <div class="pub-list">
  {%- for pub in group.items -%}
  {%- include pub.html pub=pub -%}
  {%- endfor -%}
  </div>
</details>
{%- endfor -%}

<p class="bibtex-note">
  All publications are also available in
  <a href="{{ site.bibtex_url }}" target="_blank" rel="noopener">BibTeX format</a>
  from the HAL API. The list on this page is refreshed automatically every week.
</p>

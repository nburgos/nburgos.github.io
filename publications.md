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
{%- assign groups = pubs | group_by: "type_label" -%}
{%- assign ordered_groups = "" | split: "" -%}
{%- assign order = "Journal articles|Conference papers|Book chapters|Books|Other" | split: "|" -%}
{%- for label in order -%}
  {%- for group in groups -%}
    {%- if group.name == label -%}
      {%- assign ordered_groups = ordered_groups | push: group -%}
    {%- endif -%}
  {%- endfor -%}
{%- endfor -%}
{%- for group in ordered_groups -%}
<section class="pub-group">
  <div class="pub-type-heading">
    <h2>{{ group.name }}</h2>
    <span class="pub-count">{{ group.items | size }} documents</span>
  </div>
  {%- for pub in group.items -%}
  {%- include pub.html pub=pub -%}
  {%- endfor -%}
</section>
{%- endfor -%}

<p class="bibtex-note">
  All publications are also available in
  <a href="{{ site.bibtex_url }}" target="_blank" rel="noopener">BibTeX format</a>
  from the HAL API. The list on this page is refreshed automatically every week.
</p>

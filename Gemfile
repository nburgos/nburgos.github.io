source "https://rubygems.org"

# csv/bigdecimal were removed from Ruby's default gems (>= 3.4) but are still
# required by the Jekyll version pinned by github-pages.
gem "csv"
gem "bigdecimal"

# Liquid 4.0.3 (pinned by github-pages) calls String#tainted?, removed in
# Ruby 3.2+; 4.0.4 fixes it and stays API-compatible.
gem "liquid", "~> 4.0.4"

# GitHub Pages gem: pins Jekyll and plugins to the exact versions that
# GitHub Pages runs, so local builds match production.
gem "github-pages", group: :jekyll_plugins

group :jekyll_plugins do
  gem "jekyll-seo-tag"
end

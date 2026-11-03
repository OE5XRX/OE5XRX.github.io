#!/usr/bin/env bash
# Local build of oe5xrx.org in Docker, mirroring .github/workflows/jekyll.yml.
# Usage: docs/superpowers/tools/build-local.sh [BRANDING_CHECKOUT]
# Output: <repo>/_site (gitignored). Brand files are copied into a temp copy,
# never into the working tree.
set -euo pipefail
REPO="$(cd "$(dirname "$0")/../../.." && pwd)"
BRAND="${1:-/tmp/brand}"   # OE5XRX/branding checked out at the tag pinned in jekyll.yml
WORK="$(mktemp -d)"
trap 'rm -rf "$WORK"' EXIT
rsync -a --exclude .git --exclude _site "$REPO/" "$WORK/"
mkdir -p "$WORK/_sass/color_schemes" "$WORK/_sass/custom" "$WORK/_includes" "$WORK/assets/fonts" "$WORK/assets/css"
cp "$BRAND"/jekyll/_sass/color_schemes/oe5xrx*.scss "$WORK/_sass/color_schemes/"
cp "$BRAND/jekyll/_sass/custom/custom.scss" "$WORK/_sass/custom/"
cp "$BRAND/jekyll/_includes/head_custom.html" "$BRAND/jekyll/_includes/nav_footer_custom.html" "$BRAND/jekyll/_includes/mermaid_config.js" "$WORK/_includes/"
cp "$BRAND/jekyll/assets/css/just-the-docs-oe5xrx-dark.scss" "$WORK/assets/css/"
cp "$BRAND"/type/fonts/*.woff2 "$WORK/assets/fonts/"
cp "$BRAND/logo/oe5xrx-horizontal.svg" "$WORK/assets/oe5xrx-logo.svg"
cp "$BRAND/export/favicon.ico" "$WORK/favicon.ico"
cp "$BRAND/export/apple-touch-icon-180.png" "$WORK/apple-touch-icon.png"
docker run --rm -e HOST_UID="$(id -u)" -e HOST_GID="$(id -g)" \
  -v "$WORK":/srv -v oe5xrx-site-gems:/usr/local/bundle -w /srv ruby:3.4 \
  bash -c 'bundle install --quiet && JEKYLL_ENV=production bundle exec jekyll build --quiet; rc=$?; chown -R "$HOST_UID:$HOST_GID" /srv; exit $rc'
rm -rf "$REPO/_site" && cp -r "$WORK/_site" "$REPO/_site"
echo "built: $REPO/_site"

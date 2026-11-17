#!/bin/sh
# Assemble the publishable site into dist/. Only the page, stylesheet and
# logo crops are published; docs, scripts and the reference board are not.
set -eu
cd "$(dirname "$0")"
rm -rf dist
mkdir -p dist/assets
cp index.html styles.css dist/
cp -R assets/img dist/assets/img

# Deployment guards: the concept must stay unindexed and clearly disclosed.
grep -q '<meta name="robots" content="noindex' dist/index.html || { echo "build: noindex meta missing" >&2; exit 1; }
[ "$(grep -c 'class="concept-notice"\|class="footer-concept"' dist/index.html)" -eq 2 ] || { echo "build: concept notices missing" >&2; exit 1; }
if grep -qi '<script\|<form' dist/index.html; then echo "build: unexpected script or form" >&2; exit 1; fi
echo "build: dist/ ready ($(find dist -type f | wc -l | tr -d ' ') files)"

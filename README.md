# Cobra Plumbing LLC — redesign concept

Independent, unsolicited redesign concept by Hunter Made. Not the official
Cobra Plumbing website. Not deployed; `index.html` carries `noindex`.

## Preview

Static files, no build step.

```bash
python3 -m http.server 4173
```

Then open http://localhost:4173. Opening `index.html` directly also works.

## Files

- `index.html`, `styles.css` — the whole site. No JavaScript, no external requests.
- `assets/img/` — interim logo crops (see below).
- `assets/reference/` — the original logo comparison board, unmodified.
- `scripts/extract-logo.py` — regenerates the logo crops (needs Pillow).
- `CONTENT-SOURCES.md` — where each fact came from and what awaits owner confirmation.

## Known limitations

- The logo is a raster crop from the comparison board. A vector master of the
  B1 logo is required for production.
- Typography uses a system font stack (Avenir Next on Apple devices, Segoe UI
  on Windows), so headings vary slightly by platform. A licensed webfont
  matched to the wordmark would fix this.

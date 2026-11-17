# Cobra Plumbing LLC — redesign concept

Independent, unsolicited redesign concept by Hunter Made. Not the official
Cobra Plumbing website. `index.html` carries `noindex`.

## Preview

Static files, no build step.

```bash
python3 -m http.server 4173
```

Then open http://localhost:4173. Opening `index.html` directly also works.

## Build and deploy

`sh build.sh` copies the page, stylesheet and logo crops into `dist/` and
fails if the noindex tag or either concept notice is missing. `netlify.toml`
runs it and publishes `dist/`, and adds a noindex response header to every
file. Docs, scripts and the reference board are not published.

## Files

- `index.html`, `styles.css` — the whole site. No JavaScript, no external requests.
- `assets/img/` — interim logo crops (see below).
- `assets/reference/` — the original logo comparison board, unmodified.
- `scripts/extract-logo.py` — regenerates the logo crops (needs Pillow).
- `CONTENT-SOURCES.md` — where each fact came from and what awaits owner confirmation.

## Known limitations

- The logo is a raster crop from the comparison board. A vector master of the
  B1 logo is required for production.
- Typography uses a system grotesque stack (Helvetica Neue on Apple devices,
  Arial on Windows, the default sans serif on Android), so headings vary
  slightly by platform. A licensed webfont matched to the wordmark would fix this.

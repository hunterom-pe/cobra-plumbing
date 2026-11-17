"""Build the 1200x630 link-preview card (Open Graph image).

Usage: python3 scripts/make-share-card.py
Reads  assets/img/logo-emblem.png (the interim B1 crop)
Writes assets/img/share-card.png

The emblem is placed at its natural size, never enlarged. Text uses the
system Helvetica Neue (macOS) to match the page's font stack.
"""
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parent.parent
EMBLEM = ROOT / "assets/img/logo-emblem.png"
OUT = ROOT / "assets/img/share-card.png"
FONT = "/System/Library/Fonts/HelveticaNeue.ttc"

IVORY, CHARCOAL, BRICK = (245, 240, 230), (41, 40, 36), (164, 71, 53)
MUTED = (92, 88, 80)
W, H, BAND = 1200, 630, 64


def face(style, size):
    for i in range(12):
        try:
            f = ImageFont.truetype(FONT, size, index=i)
        except OSError:
            break
        if f.getname()[1] == style:
            return f
    raise SystemExit(f"Helvetica Neue {style} not found")


card = Image.new("RGB", (W, H), IVORY)
draw = ImageDraw.Draw(card)

emblem = Image.open(EMBLEM).convert("RGBA")
ew, eh = emblem.size
ex, ey = 84, (H - BAND - eh) // 2
card.paste(emblem, (ex, ey), emblem)

x = ex + ew + 56
draw.text((x, 150), "PHOENIX, ARIZONA", font=face("Bold", 22), fill=BRICK)
draw.text((x, 188), "Cobra Plumbing LLC", font=face("Bold", 58), fill=CHARCOAL)
draw.text((x, 272), "Phoenix plumbing.", font=face("Regular", 40), fill=CHARCOAL)
draw.text((x, 322), "Repairs done right.", font=face("Regular", 40), fill=CHARCOAL)
draw.text((x, 398), "Residential  ·  Drain & sewer  ·  Light commercial",
          font=face("Medium", 22), fill=MUTED)

draw.rectangle((0, H - BAND, W, H), fill=CHARCOAL)
note = "Independent redesign concept by Hunter Made. Not the official Cobra Plumbing website."
nf = face("Regular", 21)
nw = draw.textlength(note, font=nf)
draw.text(((W - nw) / 2, H - BAND / 2), note, font=nf, fill=IVORY, anchor="lm")

card.save(OUT, optimize=True)
print(f"wrote {OUT.relative_to(ROOT)} ({W}x{H})")

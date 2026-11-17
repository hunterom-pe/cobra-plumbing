"""Crop the approved B1 logo out of the comparison board (interim raster asset).

Usage: python3 scripts/extract-logo.py
Reads  assets/reference/logo-comparison-board.webp (never modified)
Writes assets/img/logo-stacked.{png,webp}, logo-emblem.{png,webp}, favicon.png

This only crops and removes the board's flat ivory backdrop. It does not
redraw, trace, or alter the artwork. A vector master is still required.
"""
from pathlib import Path
from PIL import Image, ImageDraw, ImageFilter

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "assets/reference/logo-comparison-board.webp"
OUT = ROOT / "assets/img"

# Crop boxes (left, top, right, bottom) on the 1536x1024 board, B1 column only.
STACKED = (56, 118, 504, 712)   # emblem + COBRA / PLUMBING LLC wordmark
EMBLEM = (70, 118, 470, 556)    # Arizona emblem only


def knock_out_backdrop(img, tol=14):
    """Make the board backdrop transparent by flood-filling from the corners."""
    rgb = img.convert("RGB")
    marker = (255, 0, 255)
    w, h = rgb.size
    for seed in [(0, 0), (w - 1, 0), (0, h - 1), (w - 1, h - 1)]:
        if rgb.getpixel(seed) != marker:
            ImageDraw.floodfill(rgb, seed, marker, thresh=tol)
    mask = Image.new("L", rgb.size, 255)
    mp, px = mask.load(), rgb.load()
    for y in range(h):
        for x in range(w):
            if px[x, y] == marker:
                mp[x, y] = 0
    mask = mask.filter(ImageFilter.GaussianBlur(0.6))
    out = img.convert("RGBA")
    out.putalpha(mask)
    return out


def save(img, name):
    img.save(OUT / f"{name}.png", optimize=True)
    img.save(OUT / f"{name}.webp", quality=90, method=6)


board = Image.open(SRC)
print("backdrop sample:", board.convert("RGB").getpixel((20, 300)))
save(knock_out_backdrop(board.crop(STACKED)), "logo-stacked")
emblem = knock_out_backdrop(board.crop(EMBLEM))
save(emblem, "logo-emblem")

side = max(emblem.size)
square = Image.new("RGBA", (side, side), (0, 0, 0, 0))
square.paste(emblem, ((side - emblem.width) // 2, (side - emblem.height) // 2))
square.resize((180, 180), Image.LANCZOS).save(OUT / "favicon.png", optimize=True)

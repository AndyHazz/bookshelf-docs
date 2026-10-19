"""Social share cards: one 1200x630 image per page, made at build time.

Each card is the site header's dark band with the Bookshelf mark and the
page's title, over a row of a real shelf from the recording rig (spines with
some books turned face out). The row is picked from social/strip-*.jpg by the
page's address, so neighbouring pages show different books and a page keeps
its card from build to build.

Cards land at site/assets/social/<slug>.png; overrides/main.html points
og:image and twitter:image at the same path (slug: the page URL with "/"
as "-", "index" for the home page).
"""
import hashlib
import os

from PIL import Image, ImageDraw, ImageFont

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(ROOT, "social")
W, H = 1200, 630
INK = (30, 28, 25)          # --bs-ink, the header
CREAM = (251, 248, 242)     # the page colour, used for type on the band
SUB = (196, 188, 172)

_pages = []


def slug(url):
    return url.strip("/").replace("/", "-") or "index"


def on_page_context(context, page, config, nav):
    title = page.meta.get("title") or page.title or config["site_name"]
    _pages.append((slug(page.url), title, page.is_homepage))
    return context


def _font(name, size, weight):
    f = ImageFont.truetype(os.path.join(SRC, name), size)
    try:
        f.set_variation_by_axes([weight] if name == "RobotoCondensed.ttf" else [32, weight])
    except Exception:
        pass
    return f


def _mark(d, x, y, s, colour):
    """The logo-mark.svg drawing (48x48 grid: four books and a leaning one on
    two shelf boards) at scale s."""
    rects = [(7, 7, 5, 17, 1), (13.5, 10, 4, 14, 1), (19, 6, 6, 18, 1), (26.5, 11, 4, 13, 1),
             (32, 8.5, 9, 15.5, .75), (4, 26, 40, 5, 1), (4, 35, 40, 5, 1)]
    for rx, ry, rw, rh, op in rects:
        c = tuple(round(colour[i] * op + INK[i] * (1 - op)) for i in range(3))
        d.rounded_rectangle((x + rx * s, y + ry * s, x + (rx + rw) * s, y + (ry + rh) * s), radius=s, fill=c)


def _wrap(d, text, font, width):
    words, lines, line = text.split(), [], ""
    for w in words:
        t = (line + " " + w).strip()
        if d.textlength(t, font=font) <= width or not line:
            line = t
        else:
            lines.append(line)
            line = w
    lines.append(line)
    return lines


def card(title, home, strip):
    im = Image.new("RGB", (W, H), CREAM)
    row = Image.open(strip).convert("RGB")
    row = row.resize((W, round(row.height * W / row.width)), Image.LANCZOS)
    im.paste(row, (0, H - row.height))
    band = H - row.height
    d = ImageDraw.Draw(im)
    d.rectangle((0, 0, W, band), fill=INK)
    pad = 56
    _mark(d, pad, (band - 112) / 2, 112 / 48, CREAM)
    tx = pad + 112 + 40
    tw = W - tx - pad
    size = 72
    while True:
        tf = _font("Inter.ttf", size, 800)
        lines = _wrap(d, title, tf, tw)
        if (len(lines) <= 2 and all(d.textlength(l, font=tf) <= tw for l in lines)) or size <= 40:
            break
        size -= 4
    sf = _font("RobotoCondensed.ttf", 30, 500)
    sub = "A nicer way to find something to read next" if home else "Bookshelf for KOReader"
    asc, desc = tf.getmetrics()
    lh = round((asc + desc) * 0.98)
    s_asc, s_desc = sf.getmetrics()
    block = len(lines) * lh + 10 + s_asc + s_desc
    y = (band - block) / 2
    for ln in lines:
        d.text((tx, y), ln, font=tf, fill=CREAM)
        y += lh
    d.text((tx, y + 10), sub, font=sf, fill=SUB)
    return im


def on_post_build(config):
    strips = sorted(os.path.join(SRC, f) for f in os.listdir(SRC) if f.startswith("strip-"))
    if not strips:
        return
    out = os.path.join(config["site_dir"], "assets", "social")
    os.makedirs(out, exist_ok=True)
    for sl, title, home in _pages:
        n = int(hashlib.md5(sl.encode()).hexdigest(), 16) % len(strips)
        card(title, home, strips[n]).save(os.path.join(out, sl + ".png"), optimize=True)
    _pages.clear()
